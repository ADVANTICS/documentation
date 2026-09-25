#!/usr/bin/env python3
"""Publish a new version of a generic CAN interface: `.kcd`, `.dbc`, download list, pages.

The charger databases are authored in `etka-mcp-25-chargers`, one unversioned file per
generation (`.../generic/v3/Advantics_Generic_EVSE_protocol_v3.kcd`). The version a reader
cares about is inside the file, in `<Document version="3.7">` -- the filename does not carry
it. Publishing a release means turning that into `Advantics_Generic_EVSE_protocol_v3.7.kcd`
next to the page, converting it to DBC, listing it for download, and regenerating the CAN
messages page from it. All of that was done by hand.

Read the version with the `<Document ...>` tag, never a bare `version="..."` search: the XML
declaration on line 1 also matches, and silently names every file `v1.0`.

    python tools/sync_can_databases.py --tag 2.6.0            # both charger generations
    python tools/sync_can_databases.py --tag 2.6.0 --check    # report, write nothing
    python tools/sync_can_databases.py --tag 2.6.0 charger-v3

The vehicle databases are deliberately absent. Their source is `etka-bms`, not the copies
vendored into `etka-mcp-25-core` (those sit three minor versions behind what is published), and
adding them means pinning that down first.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
import re
import subprocess
import sys

_HERE = pathlib.Path(__file__).resolve()
ROOT = _HERE.parent.parent  # documentation/
APPS = ROOT.parent  # Applications/
SHARED = ROOT / 'products' / 'shared-charge-controllers'

# Written here, read by sync_charge_controller_can.py, so the version a page is generated from
# is stated once instead of in both tools.
PINS = _HERE.parent / 'can_versions.json'

DOCUMENT_VERSION = re.compile(r'<Document\b[^>]*\bversion="([0-9][0-9.]*)"')


@dataclasses.dataclass(frozen=True)
class Database:
    repo: str
    source: str  # path inside that repo
    published: pathlib.Path  # directory the page and its assets live in
    page: str  # download list page, relative to `published`
    label: str  # how the download bullets name it, minus the version
    archive: str  # where master keeps released versions


CHARGER = dict(
    repo='etka-mcp-25-chargers',
    published=SHARED / 'charger-can-interfaces',
    label='Advantics Generic EVSE protocol',
    archive='charge-controllers/secc_generic',
)

DATABASES = {
    'charger-v2': Database(
        source='etka/chargers/advantics/generic/v2/Advantics_Generic_EVSE_protocol_v2.kcd',
        page='databases_v2.md', **CHARGER),
    'charger-v3': Database(
        source='etka/chargers/advantics/generic/v3/Advantics_Generic_EVSE_protocol_v3.kcd',
        page='databases_v3.md', **CHARGER),
}


def git(repo: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(['git', *args], cwd=repo, capture_output=True)


def read_source(database: Database, ref: str | None) -> bytes:
    """The `.kcd` at `ref`, or from the working tree when `ref` is None."""
    repo = APPS / database.repo
    if ref is None:
        return (repo / database.source).read_bytes()
    result = git(repo, 'show', f'{ref}:{database.source}')
    if result.returncode:
        raise SystemExit(f'{database.repo} has no {database.source} at {ref}\n'
                         f'{result.stderr.decode(errors="replace")[:200]}')
    return result.stdout


def document_version(kcd: bytes) -> str:
    match = DOCUMENT_VERSION.search(kcd.decode('utf-8', errors='replace'))
    if not match:
        raise SystemExit('the .kcd has no <Document version="..."> -- refusing to guess a name')
    return match.group(1)


def published_names(database: Database, version: str) -> tuple[pathlib.Path, pathlib.Path]:
    stem = f'{database.label.replace(" ", "_")}_v{version}'
    return database.published / f'{stem}.kcd', database.published / f'{stem}.dbc'


def to_dbc(kcd: pathlib.Path, dbc: pathlib.Path) -> None:
    result = subprocess.run(
        [sys.executable, str(_HERE.parent / 'kcd_to_dbc.py'), '--kcd', str(kcd), '--out', str(dbc)],
        capture_output=True, text=True, cwd=ROOT,
    )
    if result.returncode:
        raise SystemExit(f'kcd_to_dbc failed for {kcd.name}:\n{result.stderr}')


def add_download_links(database: Database, version: str) -> tuple[str, str]:
    """Return (current page, page with the new version at the top of each format list).

    The page carries one list per format, newest first. A version already listed is left alone
    rather than duplicated, so re-running is harmless.
    """
    page = database.published / database.page
    text = page.read_text(encoding='utf-8')
    updated = text
    stem = database.label.replace(' ', '_')
    for suffix in ('kcd', 'dbc'):
        # The two charger pages word their bullets differently ("... v3.6 (Kayak format)" on one,
        # a bare "... v2.7" on the other), so the new bullet is cloned from the one above it
        # instead of being spelled out here.
        first = re.search(
            rf'^- \[{re.escape(database.label)} v[0-9.]+(?P<tail>[^]]*)\]\([^)]+\.{suffix}\)$',
            updated, re.MULTILINE)
        if not first:
            raise SystemExit(f'{page.relative_to(ROOT)}: no {suffix.upper()} download list to '
                             'add to')
        bullet = (f'- [{database.label} v{version}{first.group("tail")}]'
                  f'({stem}_v{version}.{suffix})')
        if bullet in updated:
            continue
        updated = updated[:first.start()] + bullet + '\n' + updated[first.start():]
    return text, updated


def archived_on_master(database: Database, kcd: pathlib.Path, source: bytes) -> str:
    """Whether master already carries this exact file, since that is where releases are kept."""
    path = f'{database.archive}/{kcd.name}'
    result = git(ROOT, 'show', f'master:{path}')
    if result.returncode:
        return f'NOT on master -- commit it there as {path}'
    return 'matches master' if result.stdout == source else f'DIFFERS from master:{path}'


def sync(name: str, ref: str | None, check_only: bool) -> bool:
    database = DATABASES[name]
    source = read_source(database, ref)
    version = document_version(source)
    kcd, dbc = published_names(database, version)
    page_before, page_after = add_download_links(database, version)

    kcd_changed = not kcd.exists() or kcd.read_bytes() != source
    print(f'=== {name}  <-  {database.repo}@{ref or "working tree"}')
    print(f'    version : {version}  ({database.source})')
    print(f'    kcd     : {kcd.relative_to(ROOT)} -- '
          f'{"NEW" if not kcd.exists() else ("DIFFERS" if kcd_changed else "up to date")}')
    print(f'    archive : {archived_on_master(database, kcd, source)}')
    print(f'    page    : {database.page} -- '
          f'{"download links to add" if page_after != page_before else "links present"}')

    changed = kcd_changed or page_after != page_before
    if check_only:
        return changed

    if kcd_changed:
        kcd.write_bytes(source)
    # The DBC is a conversion of whatever is published, so it is rewritten every run: that is
    # what keeps the two formats describing the same database.
    to_dbc(kcd, dbc)
    if page_after != page_before:
        (database.published / database.page).write_text(page_after, encoding='utf-8')

    pins = json.loads(PINS.read_text()) if PINS.exists() else {}
    pins[name] = f'v{version}'
    PINS.write_text(json.dumps(pins, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'    updated (pinned {name} = v{version})')
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('databases', nargs='*', choices=[*DATABASES, []],
                        help=f'default: all ({", ".join(DATABASES)})')
    parser.add_argument('--tag', help='tag of the source repo to publish from '
                                      '(default: its working tree)')
    parser.add_argument('--check', action='store_true', help='report, write nothing')
    parser.add_argument('--no-pages', action='store_true',
                        help='skip regenerating the CAN messages pages')
    args = parser.parse_args()

    chosen = args.databases or list(DATABASES)
    drift = [name for name in chosen if sync(name, args.tag, args.check)]

    if drift and not args.check and not args.no_pages:
        print('\n--- regenerating the CAN messages pages ---')
        pages = subprocess.run(
            [sys.executable, str(_HERE.parent / 'sync_charge_controller_can.py'), *drift],
            cwd=ROOT,
        )
        if pages.returncode:
            return pages.returncode

    verb = 'out of date' if args.check else 'updated'
    print(f'\n{len(drift)} database(s) {verb}: {", ".join(drift) or "none"}')
    return 1 if (args.check and drift) else 0


if __name__ == '__main__':
    sys.exit(main())
