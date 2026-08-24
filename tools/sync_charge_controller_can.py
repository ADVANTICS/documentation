#!/usr/bin/env python3
"""Regenerate the charge controllers' "CAN messages" pages from their source-of-truth `.kcd`.

Source of truth: the **`master` branch of this repository**, which carries every released
version of both databases under `charge-controllers/{evcc,secc}_generic/`. (Unlike the power
modules -- see `sync_power_module_can.py` -- these do not come from the CAN_Databases repo.)

Each generation of the protocol has one page, and that page must document the **latest minor
version** of its generation, which is what `VERSIONS` below pins. It had drifted badly:

    page                     generated from   latest on master   gap
    vehicle  can.md    (v1)  PEV  v1          PEV  v1.5          3 messages
    vehicle  can_v2.md (v2)  PEV  ~v2.1       PEV  v2.5          2 messages, 4 signals
    charger  can_v2.md       EVSE v2.6        EVSE v2.7          6 signals
    charger  can_v3.md       EVSE v3.5        EVSE v3.6          6 signals

Nothing regenerated them as the databases moved on: the KCDDOC-era `make_can*.sh` scripts each
hardcoded the *base* version (`..._v2.kcd`), and they cannot run anyway -- they call a 2017 tool
via `../../../../Manuals/`, a path that does not exist in this repo. Beyond missing messages the
pages had wrong facts: the vehicle v2 page typed 37 signals as "Single bit" that are label sets,
and gave EV_Information as 1 byte when it is 3.

Style is preserved per page rather than unified, so the diff stays reviewable and the ~40
existing inbound anchor links keep resolving: the vehicle pages keep KCDDOC's bare `## Name`
headings (addressed as `#name`) and per-label admonitions, the charger pages keep
`## Name { #Name }` and bullet lists.

Usage:
    python tools/sync_charge_controller_can.py                  # regenerate all four
    python tools/sync_charge_controller_can.py vehicle-v2
    python tools/sync_charge_controller_can.py --check          # report drift, write nothing
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # documentation/
SHARED = ROOT / "products" / "shared-charge-controllers"

VEHICLE = "charge-controllers/evcc_generic/Advantics_Generic_PEV_protocol_%s.kcd"
CHARGER = "charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_%s.kcd"

# Both databases name the controller node the same way, so Direction is always relative to it:
# OUT = the controller sends it, IN = the controller receives it.
NODE = "Advantics_Charge_Controller"

# The two vehicle databases cross-reference documentation pages by title. KCDDOC had no notion of
# this and `make_can.sh` patched the output with two `sed` calls; passing the map keeps it in one
# place. Paths are relative to the page, which lives in <product>/docs/vehicle-can-interfaces/.
VEHICLE_XREFS = {
    "CAN sensor": "../configuration/can_sensor.md",
    "No BMS mode": "../configuration/no_bms.md",
}

FRONT_MATTER = "---\nhide:\n  - toc\n---"

# Sentences that live only in the documentation, never in the database. Someone typed them
# straight into master's generated page (the "Pleaase" typo is the giveaway), so the first
# regeneration silently deleted them. They are real integrator information, so they are
# reinstated here -- but the right home is the `.kcd` note, and only the database owners can
# put them there. Until they do, this map is what keeps them alive.
#   keyed by page -> signal anchor ("Message-Signal")
ADDENDA = {
    "vehicle-v2": {
        "EV_Information-Energy_Capacity": [
            "Please note that providing the energy capacity of the battery is mandatory if "
            "ISO15118-20 is used.",
        ],
        "EV_Energy_Request-Target_Energy_Request": [
            "The target energy request can be lower than the current energy level present in "
            "the battery represented by the SoC.",
            "This represents a discharge request. More details available in the ISO15118-20 "
            "documentation.",
        ],
    },
}
# Both vehicle v2 pages come from the same database, so they carry the same addenda. The
# signals they attach to (EV_Information, EV_Energy_Request) are not AC, so both pages have them.
ADDENDA["vehicle-v2-mcs"] = ADDENDA["vehicle-v2"]

VERSIONS = {
    # name              kcd on master       page                                     version
    "vehicle-v1":     (VEHICLE, "vehicle-can-interfaces/can.md", "v1.5"),
    "vehicle-v2":     (VEHICLE, "vehicle-can-interfaces/can_v2.md", "v2.5"),
    "vehicle-v2-mcs": (VEHICLE, "vehicle-can-interfaces/can_v2_mcs.md", "v2.5"),
    "charger-v2":     (CHARGER, "charger-can-interfaces/can_v2.md", "v2.7"),
    "charger-v3":     (CHARGER, "charger-can-interfaces/can_v3.md", "v3.6"),
}

# The vehicle v2 database is shared by the CCS and the MCS vehicle controllers, and it is the
# CAN database a customer downloads -- so it stays complete, AC messages included. But an MCS
# controller has no AC charging (its config class has no `enable_din`, no `pp_mode`, and MCS is
# ISO 15118-20 DC only), so its page must not document AC. Hence two pages from one database:
# `can_v2.md` for CCS, `can_v2_mcs.md` for MCS with these messages left out.
#
# `CCS_Extra_Information` goes too: it carries only Control Pilot and Proximity Pilot readings,
# which do not exist on an MCS connector.
#
# Keep this next to VERSIONS rather than in the page: the page is regenerated, so anything
# written into it by hand is lost on the next sync.
EXCLUDE_MESSAGES = {
    "vehicle-v2-mcs": ["AC_Control", "AC_Status", "CCS_Extra_Information"],
}

PROTOCOL = {"vehicle": "Advantics Generic PEV protocol", "charger": "Advantics Generic EVSE protocol"}


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "show", f"master:{path}"], cwd=ROOT, capture_output=True)
    if r.returncode:
        raise SystemExit(f"not on master: {path}\n{r.stderr.decode(errors='replace')[:200]}")
    return r.stdout


def provenance(path: str) -> str:
    r = subprocess.run(
        ["git", "log", "-1", "--format=%h %ad :: %s", "--date=short", "master", "--", path],
        cwd=ROOT, capture_output=True, text=True,
    )
    return r.stdout.strip()


def generate(name: str, out: Path) -> None:
    tmpl, rel, version = VERSIONS[name]
    side = name.split("-")[0]
    kcd_rel = tmpl % version
    kcd_name = Path(kcd_rel).name

    # Generate from the copy published next to the page. It is byte-identical to master's (the
    # sync check below is what guarantees that), and using it keeps the generated header, the
    # download link on the databases page and the file a reader actually receives in agreement.
    kcd = SHARED / Path(rel).parent / kcd_name
    if kcd.read_bytes() != git_show(kcd_rel):
        raise SystemExit(f"{kcd.relative_to(ROOT)} differs from master:{kcd_rel} -- refresh it first")

    cmd = [
        sys.executable, str(ROOT / "tools" / "kcd_to_md.py"),
        "--kcd", str(kcd), "--out", str(out),
        "--reference-node", NODE,
        "--front-matter", FRONT_MATTER,
    ]
    for message in EXCLUDE_MESSAGES.get(name, []):
        cmd += ["--exclude-message", message]
    if side == "vehicle":
        # KCDDOC's conventions, which the vehicle pages and their inbound links still follow
        cmd += ["--wrap-tables-in-divs", "--message-id-style", "slug",
                "--definition-list-style", "admonitions"]
        for target, link in VEHICLE_XREFS.items():
            cmd += ["--page-xref", f"{target}={link}"]

    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        raise SystemExit(r.stderr)
    for line in r.stderr.splitlines():
        if line.startswith("warning:"):
            print(f"    {line}")

    # Which database version the page describes. Its absence is why four pages could sit years
    # behind their database without anyone being able to tell by reading them.
    text = out.read_text(encoding="utf-8")
    lead = f"_Generated from {PROTOCOL[side]} {version.lstrip('v')} ([`{kcd_name}`]({kcd_name}))._"
    text = text.replace("# CAN messages\n", f"# CAN messages\n\n{lead}\n", 1)
    out.write_text(insert_addenda(text, name), encoding="utf-8")


def insert_addenda(text: str, name: str) -> str:
    """Append the docs-only sentences to their signal's description.

    Inserted at the end of the prose, i.e. just before the signal's parameter table -- which is
    where a reader expects it and where it was on the pre-regeneration page.
    """
    for anchor, lines in ADDENDA.get(name, {}).items():
        signal = anchor.split("-", 1)[1]
        head = re.search(rf"^#### {re.escape(signal)}(?: \{{ #{re.escape(anchor)} \}})?$",
                         text, re.MULTILINE)
        if not head:
            raise SystemExit(f"{name}: addendum target '{anchor}' is no longer on the page")
        table = re.compile(r"^(<div class=|\| Start bit)", re.MULTILINE).search(text, head.end())
        if not table:
            raise SystemExit(f"{name}: no parameter table after '{anchor}'")
        text = text[:table.start()] + "\n".join(lines) + "\n\n" + text[table.start():]
    return text


def sync(name: str, check_only: bool) -> bool:
    tmpl, rel, version = VERSIONS[name]
    page = SHARED / rel
    kcd_rel = tmpl % version

    # Header first: generate() reports unresolved cross-references as it goes, and those lines
    # have to appear under the page they belong to.
    print(f"=== {name}  <-  master:{kcd_rel}")
    print(f"    database : {provenance(kcd_rel)}")
    print(f"    page     : {page.relative_to(ROOT)}")

    tmp = page.with_suffix(".md.new")
    generate(name, tmp)
    new = tmp.read_text(encoding="utf-8")
    old = page.read_text(encoding="utf-8") if page.exists() else ""
    changed = new != old
    state = "NEW" if not page.exists() else ("DIFFERS" if changed else "up to date")
    print(f"    status   : {state}"
          f" ({len(old.splitlines())} -> {len(new.splitlines())} lines)")

    if check_only or not changed:
        tmp.unlink()
        return changed
    tmp.replace(page)
    print("    updated")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", nargs="*", default=list(VERSIONS),
                    help=f"default: all ({', '.join(VERSIONS)})")
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = ap.parse_args()

    unknown = [p for p in args.pages if p not in VERSIONS]
    if unknown:
        raise SystemExit(f"unknown page(s): {', '.join(unknown)}")

    drift = [p for p in (args.pages or VERSIONS) if sync(p, args.check)]
    verb = "out of date" if args.check else "updated"
    print(f"\n{len(drift)} page(s) {verb}: {', '.join(drift) or 'none'}")
    return 1 if (args.check and drift) else 0


if __name__ == "__main__":
    sys.exit(main())
