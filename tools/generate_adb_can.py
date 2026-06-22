#!/usr/bin/env python3
"""Headless ADB power module CAN database generator.

Replaces the interactive TUI entry point of db-generator/db_generator.py for
CI/CD use. Stages per-module KCDs from the CAN_Databases git repo (checking
out one branch per module), applies the 24-bit ADB ID transformation, merges
all modules into a single combined KCD, and writes it to the output directory.

Output filename: <PROFILE>_<version>.kcd  (version read from the primary
module's <Document version="..."> element, e.g. ADB_PC_DC01_4.0.0.kcd).

Usage example:
    python tools/generate_adb_can.py \\
        --profile ADB_PC_AC01 \\
        --can-databases-path CAN_Databases \\
        --out-dir products/adb-pc-ac01/docs/assets
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import canmatrix
import canmatrix.formats
import yaml
from git import Repo

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NAMESPACE = "http://kayak.2codeornot2code.org/1.0"
NS = f"{{{NAMESPACE}}}"

_TOOLS_DIR = Path(__file__).parent
_DEFAULT_CONFIG = _TOOLS_DIR / "adb_generation_config.json"
_DEFAULT_POWER_MODULES = _TOOLS_DIR / "power_modules.yaml"


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def _checkout_branch(repo: Repo, branch: str) -> None:
    """Fetch and checkout *branch* in *repo*, resetting to the remote state."""
    local_names = [b.name for b in repo.branches]
    if branch not in local_names:
        repo.git.fetch("origin", branch)
        repo.git.checkout("-b", branch, f"origin/{branch}")
    else:
        repo.git.checkout(branch)
    repo.git.reset("--hard", f"origin/{branch}")


# ---------------------------------------------------------------------------
# ID transformation  (mirrors parse_and_change in db-generator/db_generator.py)
# ---------------------------------------------------------------------------

def _transform_ids(root: ET.Element, stack_pos: int, nfo_id: int) -> None:
    """Apply the 24-bit ADB ID layout to every message in *root* (in-place).

    Box files (nfo_id >= 0x80):
        final_id = register + (stack_pos << 8) + (nfo_id << 16)

    Internal files (nfo_id == 0):
        Uses the Node id of the Document's named node as the device byte.
        offset = stack_pos << 24  (internal bus; 29-bit extended CAN IDs)
    """
    if nfo_id >= 0x80:
        offset = stack_pos << 8
    else:
        offset = stack_pos << 24  # internal modules use extended 29-bit IDs

    nfo_offseted = nfo_id << 16

    # For newer-style KCDs the device byte may be inferred from the Node id
    # whose name matches the Document name (nfo_offseted_2 path).
    doc_el = root.find(f"./{NS}Document")
    doc_name = doc_el.attrib.get("name", "") if doc_el is not None else ""
    node_id = 0
    if doc_name:
        for node in root.findall(f"./{NS}Node"):
            if node.attrib.get("name") == doc_name:
                raw = node.attrib.get("id", "0")
                node_id = int(raw, 16) if raw.startswith("0x") else int(raw)
                break
    nfo_offseted_2 = node_id << 16

    for msg in root.findall(f".//{NS}Message"):
        cur = int(msg.attrib["id"], 16)
        if nfo_id > 0 and cur <= 0xFF:
            # Old-style raw register ID — apply full ADB offset
            msg.attrib["id"] = hex(cur + offset + nfo_offseted)
        elif cur < nfo_offseted_2:
            # New-style: device byte not yet in ID, infer from Node id
            msg.attrib["id"] = hex(cur + offset + nfo_offseted_2)
        else:
            # ID already contains the device byte; only add stack offset
            msg.attrib["id"] = hex(cur + offset)


# ---------------------------------------------------------------------------
# Version extraction
# ---------------------------------------------------------------------------

def _read_version(kcd_path: str) -> str | None:
    """Return the version attribute from the <Document> element, or None."""
    try:
        tree = ET.parse(kcd_path)
        root = tree.getroot()
        for tag in (f"./{NS}Document", "./Document"):
            el = root.find(tag)
            if el is not None:
                return el.attrib.get("version")
    except Exception as exc:
        print(f"  WARNING: could not parse {kcd_path}: {exc}", file=sys.stderr)
    return None


# ---------------------------------------------------------------------------
# Staging
# ---------------------------------------------------------------------------

def _stage_kcds(
    profile_data: dict,
    can_db_path: str,
    power_modules: set,
    staging_dir: str,
) -> None:
    """Checkout each needed branch and copy its .kcd to *staging_dir*."""
    repo = Repo(can_db_path)
    try:
        initial_branch = repo.active_branch.name
    except TypeError:
        # detached HEAD (e.g. submodule pinned to a commit)
        initial_branch = None

    # Collect (fname, branch) pairs — deduplicate by (fname, branch)
    seen: set = set()
    files_by_branch: dict[str, list[str]] = {}

    def _add(fname: str, branch_override: str | None) -> None:
        branch = branch_override or (fname if fname in power_modules else initial_branch)
        if (fname, branch) not in seen:
            seen.add((fname, branch))
            files_by_branch.setdefault(branch, [])
            files_by_branch[branch].append(fname)

    for entry in profile_data.get("box", {}).get("files", []):
        _add(entry["name"], entry.get("branch"))
    for entry in profile_data.get("internal", []):
        _add(entry["name"], entry.get("branch"))

    print(f"  Branches needed: {list(files_by_branch.keys())}")
    try:
        for branch, files in files_by_branch.items():
            print(f"  → checkout '{branch}'")
            _checkout_branch(repo, branch)
            for fname in files:
                src = os.path.join(can_db_path, f"{fname}.kcd")
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(staging_dir, f"{fname}.kcd"))
                    print(f"    staged {fname}.kcd")
                else:
                    print(f"    WARNING: {src} not found on '{branch}'", file=sys.stderr)
    finally:
        if initial_branch:
            _checkout_branch(repo, initial_branch)
            print(f"  → restored '{initial_branch}'")


# ---------------------------------------------------------------------------
# Per-module KCD generation
# ---------------------------------------------------------------------------

def _generate_one(
    source_kcd: str,
    stack_pos: int,
    nfo_id: int,
    work_dir: str,
) -> str:
    """Apply ID transformation to *source_kcd* and write result to *work_dir*.

    Returns the path to the written KCD.
    """
    ET.register_namespace("", NAMESPACE)
    tree = ET.parse(source_kcd)
    root = tree.getroot()
    _transform_ids(root, stack_pos, nfo_id)

    stem = Path(source_kcd).stem
    out = os.path.join(work_dir, f"{stem}_{stack_pos}.kcd")
    tree.write(out, xml_declaration=True, encoding="utf-8")
    return out


def _generate_profile(
    profile_data: dict,
    staging_dir: str,
    work_dir: str,
) -> list[str]:
    """Generate transformed per-stack KCDs. Returns list of output KCD paths."""
    generated: list[str] = []

    box = profile_data.get("box", {})
    if box:
        box_id = int(box["ID"], 16)
        box_sp = int(box.get("stack_pos", 0))
        for entry in box.get("files", []):
            src = os.path.join(staging_dir, f"{entry['name']}.kcd")
            if not os.path.exists(src):
                print(f"  SKIP {entry['name']}: not in staging dir", file=sys.stderr)
                continue
            out = _generate_one(src, box_sp, box_id, work_dir)
            generated.append(out)
            print(f"  BOX   {entry['name']} id={box['ID']} sp={box_sp} → {Path(out).name}")

    for entry in profile_data.get("internal", []):
        src = os.path.join(staging_dir, f"{entry['name']}.kcd")
        if not os.path.exists(src):
            print(f"  SKIP {entry['name']}: not in staging dir", file=sys.stderr)
            continue
        sp = int(entry["stack_pos"])
        # Each stack_pos produces a distinct output — use a unique temp name
        stem = f"{entry['name']}_sp{sp}"
        ET.register_namespace("", NAMESPACE)
        tree = ET.parse(src)
        root = tree.getroot()
        _transform_ids(root, sp, 0)
        out = os.path.join(work_dir, f"{stem}.kcd")
        tree.write(out, xml_declaration=True, encoding="utf-8")
        generated.append(out)
        print(f"  INT   {entry['name']} sp={sp} → {Path(out).name}")

    return generated


# ---------------------------------------------------------------------------
# Merge
# ---------------------------------------------------------------------------

def _merge(kcd_paths: list[str], out_kcd: str) -> None:
    """Merge all *kcd_paths* into a single combined KCD at *out_kcd*."""
    combined = canmatrix.CanMatrix()
    # Use the bare profile name (without version) so the Bus name in the KCD
    # matches the reference output from db-generator (e.g. "ADB_PC_DC01").
    combined.name = Path(out_kcd).stem.rsplit("_", 1)[0]

    for p in kcd_paths:
        db = canmatrix.formats.loadp_flat(p)
        if db is None:
            print(f"  WARNING: could not load {p}", file=sys.stderr)
            continue
        combined.merge([db])

    os.makedirs(os.path.dirname(os.path.abspath(out_kcd)), exist_ok=True)
    canmatrix.formats.dumpp({combined.name: combined}, out_kcd)


# ---------------------------------------------------------------------------
# Downstream: DBC + Markdown
# ---------------------------------------------------------------------------

def _run_downstream(kcd_path: str, docs_dir: str, profile: str, config: dict) -> None:
    """Run kcd_to_dbc and kcd_to_md on the combined KCD.

    Reference nodes and device type are derived from the profile config so
    no extra manifest fields are needed.
    """
    import subprocess

    # DBC — IDs are already transformed; no --generate-adb-ids needed
    dbc_path = kcd_path[:-4] + ".dbc"
    subprocess.run(
        [sys.executable, str(_TOOLS_DIR / "kcd_to_dbc.py"), "--kcd", kcd_path, "--out", dbc_path],
        check=True,
    )
    print(f"  DBC → {dbc_path}")

    # Markdown
    ref_nodes = [e["name"] for e in config[profile].get("box", {}).get("files", [])]
    device_type = profile.split("_")[-1]  # "ADB_PC_AC01" → "AC01"
    md_out = os.path.join(docs_dir, "docs", "can_bus_interface.md")
    subprocess.run(
        [
            sys.executable, str(_TOOLS_DIR / "kcd_to_md.py"),
            "--kcd", kcd_path,
            "--out", md_out,
            "--reference-node", *ref_nodes,
            "--generate-adb-ids",
            "--adb-device-type", device_type,
        ],
        check=True,
    )
    print(f"  MD  → {md_out}")


# ---------------------------------------------------------------------------
# Core: single-profile run
# ---------------------------------------------------------------------------

def run_profile(
    profile: str,
    can_databases_path: str,
    out_dir: str,
    config: dict,
    power_modules: set,
    docs_dir: str | None = None,
) -> str:
    """Generate the combined KCD for *profile* and write it to *out_dir*.

    If *docs_dir* is given, also produces the DBC and can_bus_interface.md.
    Returns the path to the combined KCD.
    """
    if profile not in config:
        sys.exit(
            f"Profile '{profile}' not found in config.\n"
            f"Available: {list(config.keys())}"
        )

    profile_data = config[profile]

    with tempfile.TemporaryDirectory(prefix="adb_can_gen_") as tmp:
        staging_dir = os.path.join(tmp, "staged")
        work_dir = os.path.join(tmp, "per_module")
        os.makedirs(staging_dir)
        os.makedirs(work_dir)

        print(f"\n[1/3] Staging KCDs for '{profile}'…")
        _stage_kcds(profile_data, can_databases_path, power_modules, staging_dir)

        primary_kcd = os.path.join(staging_dir, f"{profile}.kcd")
        version = _read_version(primary_kcd) if os.path.exists(primary_kcd) else None
        if not version:
            print(f"  WARNING: could not read version; using 'unknown'")
            version = "unknown"
        print(f"  Version: {version}")

        print(f"\n[2/3] Transforming IDs…")
        generated = _generate_profile(profile_data, staging_dir, work_dir)
        if not generated:
            sys.exit("No KCDs generated — check staging output above.")

        print(f"\n[3/3] Merging {len(generated)} file(s)…")
        out_kcd = os.path.join(out_dir, f"{profile}_{version}.kcd")
        _merge(generated, out_kcd)

    print(f"\n  KCD → {out_kcd}")

    if docs_dir is not None:
        _run_downstream(out_kcd, docs_dir, profile, config)

    return out_kcd


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

_DEFAULT_DOCS_MANIFEST = _TOOLS_DIR / "adb_docs_manifest.json"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Generate ADB power module CAN databases (KCD + DBC + Markdown)."
    )
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--profile",
        help="Single profile to generate, e.g. ADB_PC_AC01",
    )
    mode.add_argument(
        "--all", action="store_true",
        help="Generate all products listed in adb_docs_manifest.json",
    )
    p.add_argument(
        "--can-databases-path", required=True,
        help="Path to a local clone/submodule of the CAN_Databases git repo",
    )
    p.add_argument(
        "--out-dir",
        help="Output directory for the KCD (single-profile mode only; "
             "in --all mode the docs dir from the manifest is used)",
    )
    p.add_argument(
        "--config", default=str(_DEFAULT_CONFIG),
        help=f"Path to adb_generation_config.json (default: {_DEFAULT_CONFIG})",
    )
    p.add_argument(
        "--power-modules", default=str(_DEFAULT_POWER_MODULES),
        help=f"Path to power_modules.yaml (default: {_DEFAULT_POWER_MODULES})",
    )
    p.add_argument(
        "--docs-manifest", default=str(_DEFAULT_DOCS_MANIFEST),
        help=f"Path to adb_docs_manifest.json used by --all (default: {_DEFAULT_DOCS_MANIFEST})",
    )
    return p


def main() -> None:
    args = _build_parser().parse_args()

    with open(args.config) as f:
        config: dict = json.load(f)
    with open(args.power_modules) as f:
        power_modules: set = set(yaml.safe_load(f).get("power_modules", []))

    if args.all:
        with open(args.docs_manifest) as f:
            manifest: dict = json.load(f)
        print(f"Generating {len(manifest)} product(s) from manifest…")
        for profile, docs_dir in manifest.items():
            print(f"\n{'='*60}")
            print(f"Profile: {profile}  →  {docs_dir}")
            print('='*60)
            out_dir = os.path.join(docs_dir, "docs", "assets")
            run_profile(profile, args.can_databases_path, out_dir, config, power_modules,
                        docs_dir=docs_dir)
        print("\nAll products done.")

    else:
        if not args.out_dir:
            sys.exit("--out-dir is required in single-profile mode")
        out_kcd = run_profile(
            args.profile, args.can_databases_path, args.out_dir, config, power_modules
        )
        version = Path(out_kcd).stem.rsplit("_", 1)[1]
        print(f"VERSION={version}")


if __name__ == "__main__":
    main()
