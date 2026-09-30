#!/usr/bin/env python3
"""Regenerate every configuration page from `controller-config`.

Two kinds of page are kept in sync here:

* `configuration/all-entries.md`, one per product -- the exhaustive reference, written whole
  by `generate_config_reference.py`.
* the topic pages -- hand-written prose plus one machine-emitted bullet block per section.
  `emit_config_block.py` renders those blocks; this splices each one back into its page,
  leaving the prose above it alone.

Which pages are emitted and which are curated is not guessable from the file, hence the BLOCKS
table below. `generalities.md` and `ocpp.md` are deliberately absent: they collapse
`dig_in1 … dig_in4` into one bullet and carry notes that no generator would produce, so
regenerating them would destroy editorial work. New entries in those sections are reported by
`--check` and added by hand.

**Generate from the tag the release pins, not the working tree.** The pages describe a
released controller; the working tree routinely carries unreleased entries that must not be
published:

    python tools/sync_config_pages.py --tag 1.5.0
    python tools/sync_config_pages.py --tag 1.5.0 --check    # report drift, write nothing
    python tools/sync_config_pages.py --tag 1.5.0 blocks     # skip the all-entries pages

The `controller-config` version each release pins is in that release's `[version:X.Y.Z]`
section of `evse-controller/setup.cfg`.

Choice values are shown only when `public_choices.py` lists them. Every run then audits all the
configuration pages, hand-written ones included, for a hidden value or a hidden entry.
"""

from __future__ import annotations

import argparse
import dataclasses
import pathlib
import shutil
import subprocess
import sys
import tempfile

_HERE = pathlib.Path(__file__).resolve()
ROOT = _HERE.parent.parent  # documentation/
APPS = ROOT.parent  # Applications/
PRODUCTS = ROOT / 'products'
SHARED = PRODUCTS / 'shared-charge-controllers' / 'charger-configuration'

# The line every topic page ends its prose with. The emitted block starts right after it.
MARKER = 'Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.'


@dataclasses.dataclass(frozen=True)
class Block:
    """One machine-emitted bullet block inside a topic page."""

    controller: str
    section: str
    page: pathlib.Path
    after: str = MARKER
    # Heading that ends the block. None means it runs to the end of the file.
    before: str | None = None
    # True for pages that also document entries in hand-written prose above the block; those
    # entries are left out of it so the two do not repeat each other.
    skip_documented: bool = False
    # Pages under shared-charge-controllers/ are served to both the SPCC and the SECC, so the
    # two controllers must agree on the section or one product gets the other's page.
    shared: bool = False


BLOCKS = {
    'ccs-dc': Block('spcc', 'pistol:CCS DC', SHARED / 'pistol-ccs-dc.md',
                    skip_documented=True, shared=True),
    'ccs-ac': Block('spcc', 'pistol:CCS AC', SHARED / 'pistol-ccs-ac.md', shared=True),
    'chademo': Block('spcc', 'pistol:CHAdeMO', SHARED / 'pistol-chademo.md', shared=True),
    'mcs': Block('spcc', 'pistol:MCS',
                 PRODUCTS / 'adm-cs-spcc/docs/configuration/pistol-mcs.md',
                 before='## `[t1s_driver]`'),
}


def export_tag(tag: str) -> pathlib.Path:
    """Check `controller-config` out at a tag, into a temporary directory."""
    out = pathlib.Path(tempfile.mkdtemp(prefix=f'controller-config-{tag}-'))
    archive = subprocess.run(['git', 'archive', tag], cwd=APPS / 'controller-config',
                             capture_output=True)
    if archive.returncode:
        shutil.rmtree(out, ignore_errors=True)
        raise SystemExit(f'controller-config has no tag {tag}\n'
                         f'{archive.stderr.decode(errors="replace")[:200]}')
    subprocess.run(['tar', '-x', '-C', str(out)], input=archive.stdout, check=True)
    return out


def working_tree_state() -> str:
    def git(*args: str) -> str:
        return subprocess.run(['git', *args], cwd=APPS / 'controller-config',
                              capture_output=True, text=True).stdout.strip()

    dirty = len(git('status', '--porcelain', '--', 'advantics').splitlines())
    at = git('describe', '--tags', '--always')
    return f'{at}, {dirty} file(s) modified' if dirty else at


def load_config_classes(tag_dir: pathlib.Path | None) -> None:
    """Put the chosen `controller-config` on the import path, then import from it.

    `generate_config_reference` prepends the *working tree* to `sys.path` when it is imported,
    so a tagged export has to be imported before that happens -- once the modules are in
    `sys.modules` the later path entry cannot win.
    """
    # etka is a namespace package split across etka-*/etka. etka-devices/etka has an
    # __init__.py and therefore shadows every other portion; drop it.
    sys.path = [p for p in sys.path if not p.rstrip('/').endswith('etka-devices')]
    for package in ('etka-core', 'etka-tls'):
        sys.path.insert(0, str(APPS / package))
    sys.path.insert(0, str(tag_dir or APPS / 'controller-config'))

    import advantics.configcls.evcc  # noqa: F401
    import advantics.configcls.mevc  # noqa: F401
    import advantics.configcls.secc  # noqa: F401
    import advantics.configcls.spcc

    origin = pathlib.Path(advantics.configcls.spcc.__file__)
    expected = tag_dir or APPS / 'controller-config'
    if expected not in origin.parents:
        raise SystemExit(f'config classes came from {origin}, expected them under {expected}')


def splice(block: Block, rendered: str) -> tuple[str, str]:
    """Return (current page, page with `rendered` in place of its emitted block)."""
    text = block.page.read_text(encoding='utf-8')
    lines = text.splitlines()

    try:
        start = lines.index(block.after) + 1
    except ValueError:
        raise SystemExit(f'{block.page.relative_to(ROOT)}: marker line not found:\n  {block.after}')

    if block.before is None:
        end = len(lines)
    else:
        matches = [i for i, line in enumerate(lines) if line == block.before and i > start]
        if not matches:
            raise SystemExit(f'{block.page.relative_to(ROOT)}: end heading not found:\n'
                             f'  {block.before}')
        end = matches[0]

    head = '\n'.join(lines[:start]) + '\n\n'
    tail = '\n' + '\n'.join(lines[end:]) + '\n' if block.before is not None else ''
    return text, head + rendered + tail


def documented_above(block: Block) -> set[str]:
    """Entry names the prose above the block already explains under a heading."""
    from emit_config_block import documented_names

    text = block.page.read_text(encoding='utf-8')
    prose = text[:text.index(block.after)]
    scratch = block.page.with_suffix('.prose.tmp')
    scratch.write_text(prose, encoding='utf-8')
    try:
        return documented_names(scratch)
    finally:
        scratch.unlink()


def sync_block(name: str, check_only: bool) -> bool:
    from emit_config_block import render_block

    block = BLOCKS[name]
    skip = documented_above(block) if block.skip_documented else set()
    rendered = render_block(block.controller, block.section, skip)
    if not rendered:
        raise SystemExit(f'{name}: [{block.section}] emits nothing')

    if block.shared:
        other = 'secc' if block.controller == 'spcc' else 'spcc'
        if render_block(other, block.section, skip) != rendered:
            raise SystemExit(
                f'{name}: [{block.section}] differs between {block.controller} and {other}, but '
                f'{block.page.relative_to(PRODUCTS)} is served to both -- split the page first')

    old, new = splice(block, rendered)
    changed = new != old
    print(f'=== {name}  <-  [{block.section}] of {block.controller}')
    print(f'    page   : {block.page.relative_to(ROOT)}')
    print(f'    status : {"DIFFERS" if changed else "up to date"}'
          f' ({len(old.splitlines())} -> {len(new.splitlines())} lines)')
    if changed and not check_only:
        block.page.write_text(new, encoding='utf-8')
        print('    updated')
    return changed


def sync_reference(controller: str, check_only: bool) -> bool:
    from generate_config_reference import CONTROLLERS, DESTINATIONS, collect, render

    module_name, class_name, product = CONTROLLERS[controller]
    config = getattr(__import__(module_name, fromlist=[class_name]), class_name)()
    entries: list = []
    collect(config, '', entries, controller)
    new = render(controller, product, entries)

    page = PRODUCTS / DESTINATIONS[controller]
    old = page.read_text(encoding='utf-8') if page.exists() else ''
    changed = new != old
    print(f'=== {controller}  <-  every user-facing entry')
    print(f'    page   : {page.relative_to(ROOT)}')
    print(f'    status : {"NEW" if not old else ("DIFFERS" if changed else "up to date")}'
          f' ({len(entries)} entries, {len(old.splitlines())} -> {len(new.splitlines())} lines)')
    if changed and not check_only:
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(new, encoding='utf-8')
        print('    updated')
    return changed


def parse_args() -> argparse.Namespace:
    """Parsed before anything is imported: `--tag` decides where the config classes come from."""
    parser = argparse.ArgumentParser()
    parser.add_argument('targets', nargs='*',
                        help=f'default: all. Blocks: {", ".join(BLOCKS)}; references: evcc, '
                             'mevc, secc, spcc. "reference" or "blocks" selects a whole kind')
    parser.add_argument('--tag', help='controller-config tag to generate from '
                                      '(default: the working tree)')
    parser.add_argument('--check', action='store_true', help='report drift, write nothing')
    return parser.parse_args()


def main(args: argparse.Namespace) -> int:
    from generate_config_reference import CONTROLLERS

    targets = {**{c: 'reference' for c in CONTROLLERS}, **{b: 'block' for b in BLOCKS}}
    chosen = args.targets or list(targets)
    if 'reference' in chosen:
        chosen = [c for c in chosen if c != 'reference'] + list(CONTROLLERS)
    if 'blocks' in chosen:
        chosen = [c for c in chosen if c != 'blocks'] + list(BLOCKS)
    unknown = [t for t in chosen if t not in targets]
    if unknown:
        raise SystemExit(f'unknown target(s): {", ".join(unknown)}')

    print(f'source: controller-config {args.tag or f"working tree ({working_tree_state()})"}\n')

    drift = []
    for target in chosen:
        if targets[target] == 'block':
            changed = sync_block(target, args.check)
        else:
            changed = sync_reference(target, args.check)
        if changed:
            drift.append(target)

    verb = 'out of date' if args.check else 'updated'
    print(f'\n{len(drift)} page(s) {verb}: {", ".join(drift) or "none"}')

    # The hand-written pages are not regenerated, so they are checked instead: they must not
    # show a value or an entry that the generated pages hide.
    from generate_config_reference import audit_pages, unreviewed_choices

    unreviewed = unreviewed_choices()
    if unreviewed:
        print(f'\n{len(unreviewed)} choice list(s) in public_choices.py not reviewed yet, so their '
              'pages show the default only:')
        for pattern in unreviewed:
            print(f'    {pattern}')

    values, entries = audit_pages(PRODUCTS)
    print(f'\n{len(values)} place(s) where a configuration page shows a value that is not public'
          + (':' if values else ''))
    for finding in values:
        print(f'    {finding}')
    # Reported, not failed: whether these entries are public is a scope question for the owner
    # of controller-config, and each needs deciding one way or the other.
    print(f'\n{len(entries)} entry(ies) documented on a topic page but left off the generated one'
          + (':' if entries else ''))
    for finding in entries:
        print(f'    {finding}')
    return 1 if (args.check and (drift or values or unreviewed)) else 0


if __name__ == '__main__':
    arguments = parse_args()
    tag_export = export_tag(arguments.tag) if arguments.tag else None
    try:
        load_config_classes(tag_export)
        sys.path.insert(0, str(_HERE.parent))
        sys.exit(main(arguments))
    finally:
        if tag_export:
            shutil.rmtree(tag_export, ignore_errors=True)
