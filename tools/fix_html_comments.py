#!/usr/bin/env python3
"""Make commented-out blocks actually stay hidden.

Three pages published commented-out content *visibly*, because of how python-markdown and
`pymdownx.superfences` interact with HTML comments. Two distinct triggers, both verified:

1. **A fence on the same line as `<!--`.** `superfences` is a *preprocessor*, so it runs before
   raw-HTML blocks are handled -- but it only matches a fence at the start of a line. In

       <!-- ```bash
       $ unzip /path/to/your/release.zip
       ```
        (Replace ...) -->

   the opening fence is not at line start, so it is not matched; the *closing* fence then acts as
   an opening one and swallows the following prose into a code block, leaving `<!--` as text.
   This is what made `<!-- ```bash` visible on the SECC/EVCC update page.

2. **An indented comment inside a list item.** Indented `<!--` is not a raw-HTML block, so it is
   treated as ordinary text and escaped to `&lt;!--`, publishing the whole "hidden" block. This
   put four commented blocks on the TLS & Plug'n'Charge page in front of customers.

The shape that reliably stays hidden -- checked by rendering, not assumed:

    <!--
    ...content, no ``` fence lines...
    -->

with both markers alone on their own line at column 0. So that is what this rewrites to. Fence
lines *inside* a comment are dropped: the content is not rendered anyway, and their presence is
trigger 1 waiting to happen.

Usage:
    python tools/fix_html_comments.py --dry-run
    python tools/fix_html_comments.py
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys

FENCE_LINE = re.compile(r'^\s*(?:```|~~~)\S*\s*$')
COMMENT = re.compile(r'[ \t]*<!--.*?-->', re.S)


def needs_fix(block: str, line_prefix: str) -> list[str]:
    """Why this comment is unsafe, or [] if it is already fine.

    `line_prefix` is whatever precedes the comment on its own line. An inline comment after
    text -- `#### Heading <!-- {docsify-ignore} -->` -- is safe and very common here; only a
    comment opening an *indented* line is swallowed into a list item and rendered as text.
    """
    reasons = []
    first = block.split('\n', 1)[0]
    if line_prefix and not line_prefix.strip():
        reasons.append('indented (renders as text)')
    if re.search(r'<!--[^\n]*(?:```|~~~)', first):
        reasons.append('fence on the opening line (swallows following content)')
    return reasons

# Deliberately NOT treated as defects, because they were checked and render correctly:
#   * content on the opening line -- `<!-- a note -->` is the common, working form;
#   * a fence on its own line inside an otherwise well-formed comment (sys3_update.md:206,
#     tls_pnc_config.md:173). Those pair up correctly today. They are fragile rather than
#     broken, so they are reported by --audit instead of rewritten; changing a page that
#     renders correctly risks a regression for no gain.


def rewrite(block: str) -> str:
    inner = block.strip()
    inner = inner[len('<!--'):] if inner.startswith('<!--') else inner
    inner = inner[: -len('-->')] if inner.rstrip().endswith('-->') else inner
    lines = [line for line in inner.split('\n') if not FENCE_LINE.match(line)]
    # keep relative indentation, drop the common prefix the whole block sat at
    body = [line for line in lines if line.strip()]
    pad = min((len(line) - len(line.lstrip()) for line in body), default=0)
    lines = [line[pad:] if line.strip() else '' for line in lines]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return '<!--\n' + '\n'.join(lines) + '\n-->'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--root', default='products')
    args = parser.parse_args()

    seen: set[pathlib.Path] = set()
    changed = fixed = 0
    for root, dirs, files in os.walk(args.root, followlinks=True):
        dirs[:] = [d for d in dirs if d not in ('site', 'node_modules', '.git', 'to-migrate')]
        for name in sorted(files):
            if not name.endswith('.md'):
                continue
            page = pathlib.Path(root) / name
            real = page.resolve()
            if real in seen:
                continue
            seen.add(real)

            original = page.read_text(encoding='utf-8')
            report: list[str] = []

            def replace(match: re.Match[str]) -> str:
                block = match.group(0)
                # COMMENT swallows the leading whitespace, so measure from the `<!--` token
                marker = match.start() + match.group(0).index('<!--')
                prefix = original[:marker].rsplit('\n', 1)[-1]
                reasons = needs_fix(block, prefix)
                if not reasons or (prefix and prefix.strip()):
                    return block
                line_no = original[: match.start()].count('\n') + 1
                report.append(f'    line {line_no}: {", ".join(reasons)}')
                new = rewrite(block)
                # a comment lifted out of a list needs a blank line before it to end the list
                before = original[: match.start()].rsplit('\n', 1)[-1]
                return ('\n' if before.strip() else '') + new

            text = COMMENT.sub(replace, original)
            if text != original:
                changed += 1
                fixed += len(report)
                print(f'{page}')
                print('\n'.join(report))
                if not args.dry_run:
                    page.write_text(text, encoding='utf-8')

    verb = 'would fix' if args.dry_run else 'fixed'
    print(f'\n{verb} {fixed} comments in {changed} files')
    return 0


if __name__ == '__main__':
    sys.exit(main())
