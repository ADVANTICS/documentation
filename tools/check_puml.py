#!/usr/bin/env python3
"""Detect PlantUML server warning banners baked into the built site, and deprecated skinparams.

The plantuml server renders a yellow banner *inside the diagram* when it dislikes the source,
e.g. "Please use CSS style instead of skinparam ParticipantPadding". Three things make this
nasty to find:

  * `mkdocs build` reports nothing -- the SVG came back HTTP 200
  * the text is split one <text> element per word, so grepping the built HTML for the phrase
    finds nothing; you have to reassemble the text nodes
  * mkdocs_puml caches rendered SVG **outside the repo**, at
    `~/.cache/mkdocs_puml/<project>/storage.mpack`. Once a bad render is cached it survives
    every subsequent build, including after the source is fixed and after `--clean`, and it
    is baked into whatever CI publishes. Deleting the source construct changes the cache key
    for that diagram, but to be sure: remove the storage.mpack and rebuild.

Usage:
    python tools/check_puml.py                 # scan built sites + sources
    python tools/check_puml.py --sources-only  # no build needed
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
CACHE = pathlib.Path.home() / ".cache" / "mkdocs_puml"

# skinparams the server has deprecated in favour of the <style> syntax
DEPRECATED = ("ParticipantPadding",)
TEXT_NODE = re.compile(r">([^<>]{1,80})</text>")
WARNING = re.compile(r"(Please use[^|]{0,100}|.{0,40}\bis deprecated\b.{0,40})")


def banners(html: pathlib.Path) -> Counter:
    """Reassemble SVG text nodes and pull out any warning sentence."""
    text = html.read_text(encoding="utf-8", errors="replace")
    found: Counter = Counter()
    for m in re.finditer(r"|".join(DEPRECATED) + r"|Please use", text):
        window = text[max(0, m.start() - 1500): m.start() + 200]
        words = " ".join(TEXT_NODE.findall(window))
        hit = WARNING.search(re.sub(r"\s+", " ", words))
        if hit:
            found[hit.group(1).strip()] += 1
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources-only", action="store_true")
    args = ap.parse_args()
    problems = 0

    # 1. deprecated constructs still in the Markdown
    src = Counter()
    for p in PRODUCTS.rglob("*.md"):
        if "site" in p.parts:
            continue
        body = p.read_text(encoding="utf-8", errors="replace")
        for name in DEPRECATED:
            n = len(re.findall(rf"^skinparam {name}\b", body, re.M | re.I))
            if n:
                src[f"{p.relative_to(PRODUCTS)}: skinparam {name}"] += n
    print(f"=== deprecated skinparams in source: {sum(src.values())} ===")
    for k, n in src.most_common():
        print(f"  {k} x{n}")
    problems += sum(src.values())

    # 2. warning banners already rendered into the built site
    if not args.sources_only:
        total = Counter()
        pages = 0
        for html in PRODUCTS.glob("*/site/**/*.html"):
            b = banners(html)
            if b:
                pages += 1
                total.update(b)
                print(f"  {html.relative_to(PRODUCTS)}: {sum(b.values())} banner(s)")
        print(f"\n=== rendered warning banners: {sum(total.values())} on {pages} page(s) ===")
        for k, n in total.most_common():
            print(f"  x{n}: {k}")
        problems += sum(total.values())
        if total:
            print("\n  Cached renders are the usual cause. Clear them and rebuild:")
            for d in sorted(p.name for p in CACHE.iterdir()) if CACHE.is_dir() else []:
                print(f"    rm -f {CACHE / d / 'storage.mpack'}")

    print(f"\n{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
