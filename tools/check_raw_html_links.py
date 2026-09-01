#!/usr/bin/env python3
"""Validate the links MkDocs cannot see.

MkDocs rewrites and validates links it parsed from Markdown. A link written as raw HTML --
`<a href="advos-yocto-system/ssh.md#...">` -- is passed through untouched, so two things happen:

* the `.md` reaches the browser and 404s, because the published file is `.html`;
* MkDocs never validates it, so `mkdocs build` stays silent. Nothing warns, ever.

48 such links were live on the MEVC and SPCC "Software Releases" pages. They are inside a raw
`<table class="custom-table">` with no `markdown="1"`, so Markdown link syntax cannot be used
there -- Markdown is not processed inside that table -- and the fix was to point them at the
built URL instead. That is safe only while `use_directory_urls: false`, which this checks.

So this closes the loop MkDocs leaves open: every raw-HTML link is resolved against the built
site, target page *and* anchor.

Usage:
    python tools/check_raw_html_links.py                 # every product with a built site/
    python tools/check_raw_html_links.py adm-cs-mevc
"""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
ANCHOR = re.compile(r'''\sid=["']([^"']+)["']''')
LINK = re.compile(r'<a\s[^>]*href\s*=\s*"([^"]+)"', re.I)


def anchors(page: pathlib.Path) -> set[str]:
    return set(ANCHOR.findall(page.read_text(encoding='utf-8', errors='replace')))


def main() -> int:
    wanted = sys.argv[1:]
    products = sorted(p for p in (ROOT / 'products').iterdir() if (p / 'site').is_dir())
    if wanted:
        products = [p for p in products if p.name in wanted]

    problems = 0
    for product in products:
        site = product / 'site'
        # A raw `.md` href is always wrong: the published file is `.html`.
        stale = [
            (md.relative_to(ROOT), href)
            for md in product.rglob('docs/**/*.md')
            for href in LINK.findall(md.read_text(encoding='utf-8', errors='replace'))
            if re.search(r'\.md(#|$)', href)
        ]
        checked = 0
        for page in site.rglob('*.html'):
            # Material generates 404.html with site-root-absolute links; they are the theme's,
            # not the docs', and cannot be resolved against a local build directory.
            if page.name == '404.html':
                continue
            for href in LINK.findall(page.read_text(encoding='utf-8', errors='replace')):
                if re.match(r'^[a-z][a-z0-9+.\-]*:', href, re.I) or href.startswith('#'):
                    continue  # http(s), mailto:, tel:, data:, and same-page anchors
                path, _, fragment = href.partition('#')
                # Filenames with spaces are percent-encoded in the href
                # ('9. Disposal.md' -> '9.%20Disposal/'); compare against the real name.
                path = urllib.parse.unquote(path)
                fragment = urllib.parse.unquote(fragment)
                if not path:
                    continue
                base = site if path.startswith('/') else page.parent
                target = (base / path.lstrip('/')).resolve()
                # Under `use_directory_urls: true` (the power modules) a link points at a
                # directory, which is served as its index.html.
                if target.is_dir():
                    target = target / 'index.html'
                checked += 1
                if not target.is_file():
                    print(f'  {product.name}: {page.relative_to(site)} -> {href}  NO SUCH PAGE')
                    problems += 1
                elif fragment and fragment not in anchors(target):
                    print(f'  {product.name}: {page.relative_to(site)} -> {href}  NO SUCH ANCHOR')
                    problems += 1
        for where, href in stale:
            print(f'  {product.name}: {where} has a raw-HTML .md link: {href}')
            problems += 1
        print(f'  {product.name}: {checked} raw-HTML links checked')

    print(f'\n{problems} problem(s)' if problems else '\nall raw-HTML links resolve')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
