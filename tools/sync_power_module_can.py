#!/usr/bin/env python3
"""Refresh a power module's CAN artefacts from the CAN_Databases repo -- the source of truth.

Confirmed source of truth: **the tip of the module's own branch in
`Applications/CAN_Databases`** (github.com/ADVANTICS/CAN_Databases). Each documented module has
a single-file branch named after it, e.g. `ADM_PC_BP25` containing only `ADM_PC_BP25.kcd`.

For each module this script:
  1. fetches the CAN_Databases repo (never touching its checked-out branch or working tree)
  2. extracts the .kcd from the branch tip into `docs/assets/`
  3. converts it to .dbc with `kcd_to_dbc.py` (the .dbc is a courtesy artefact, always derived)
  4. regenerates `can_bus_interface.md` with `kcd_to_md.py`
  5. prints the provenance (branch, commit, date) so a published page can be traced to a commit

Usage:
    python tools/sync_power_module_can.py BP25 LL25 LF46
    python tools/sync_power_module_can.py --check BP25      # report drift, change nothing
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # documentation/
WORKSPACE = ROOT.parent                                # Applications/
CAN_REPO = WORKSPACE / "CAN_Databases"

# module -> ref holding its database.
# BP25 has a dedicated single-file branch. LL25 and LF46 have none -- their databases live only
# on master (LL25 last touched 2025-07-15, LF46's 2023-05-22; both stable). If a per-module
# branch is created for them later, change it here and nowhere else.
REFS = {
    "BI25": "origin/ADM_PC_BI25",
    "BP25": "origin/ADM_PC_BP25",
    "LL25": "origin/master",
    "LF46": "origin/master",
}

# The .kcd file name, where it differs from the module name. ADM-PC-LF45 was renamed ADM-PC-LF46,
# but CAN_Databases still calls the database ADM_PC_LF45.kcd -- there is no ADM_PC_LF46.kcd on any
# branch. The published artefact keeps the upstream name so a customer can match it against the
# repo and the firmware packages; renaming it here would invent a file that does not exist.
DB_NAMES = {"LF46": "ADM_PC_LF45"}


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", *args], cwd=CAN_REPO, capture_output=True)
    if r.returncode:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.decode(errors='replace')[:300]}")
    return r.stdout if binary else r.stdout.decode("utf-8", errors="replace").strip()


def provenance(ref: str, name: str) -> str:
    return git("log", "-1", "--format=%h %ad %an :: %s", "--date=short", ref, "--", name)


def sync(mod: str, check_only: bool) -> bool:
    ref = REFS[mod]
    name = f"{DB_NAMES.get(mod, f'ADM_PC_{mod}')}.kcd"
    docs = ROOT / "products" / f"adm-pc-{mod.lower()}" / "docs"
    dest = docs / "assets" / name

    blob = git("show", f"{ref}:{name}", binary=True)
    changed = (not dest.exists()) or dest.read_bytes() != blob

    print(f"=== {mod}  <-  {ref}")
    print(f"    tip     : {git('log', '-1', '--format=%h %ad %an :: %s', '--date=short', ref)}")
    print(f"    {name} : {provenance(ref, name)}")
    print(f"    status  : {'DIFFERS from docs/assets' if changed else 'up to date'}")
    if check_only or not changed:
        return changed

    dest.write_bytes(blob)
    dbc = dest.with_suffix(".dbc")
    subprocess.run([sys.executable, str(ROOT / "tools" / "kcd_to_dbc.py"),
                    "--kcd", str(dest), "--out", str(dbc)], check=True,
                   capture_output=True, cwd=ROOT)
    page = docs / "can_bus_interface.md"
    subprocess.run([sys.executable, str(ROOT / "tools" / "kcd_to_md.py"),
                    "--kcd", str(dest), "--out", str(page)], check=True,
                   capture_output=True, cwd=ROOT)
    # the 8-column signal tables need the whole content column, and the page opens with its own
    # message index, so its ToC would just be a duplicate hundreds of entries long
    page.write_text("---\nhide:\n  - toc\n---\n\n" + page.read_text(encoding="utf-8"),
                    encoding="utf-8")
    print(f"    updated : {name}, {dbc.name}, can_bus_interface.md "
          f"({len(page.read_text().splitlines())} lines)")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="*", default=list(REFS), help="default: all")
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    ap.add_argument("--no-fetch", action="store_true")
    args = ap.parse_args()

    if not (CAN_REPO / ".git").exists():
        raise SystemExit(f"{CAN_REPO} is not a git repo -- cannot resolve the source of truth")
    if not args.no_fetch:
        git("fetch", "--all", "--quiet")
        print(f"fetched {CAN_REPO.relative_to(WORKSPACE.parent)}\n")

    drift = [m for m in (args.modules or REFS) if sync(m.upper(), args.check)]
    if args.check:
        print(f"\n{len(drift)} module(s) out of date: {', '.join(drift) or 'none'}")
        return 1 if drift else 0
    print(f"\n{len(drift)} module(s) updated: {', '.join(drift) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
