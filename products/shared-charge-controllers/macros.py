"""Numbered figures for the four charge-controller sites.

Same contract as the power-module manuals (`products/adm-pc-*/docs/assets/macros.py`):

    {{ figure('assets/interlock.svg', 'The interlock loop', id='fig-interlock') }}
    ... as shown in {{ figref('fig-interlock') }} ...

emits a `<figure>` with a globally numbered `<figcaption>`, and a link that resolves to
that number.

Numbering is deterministic and independent of MkDocs' render order: before the first page
is rendered we walk the sources once, in nav order, counting `{{ figure( }}` occurrences to
get each page's starting offset. Pages that are *not* in the nav are appended after the nav
pages in sorted order, so they still get unique numbers instead of all sharing offset 0
(`evse_overview.md` on the SECC and SPCC sites is such a page).

This file is the single source for all four products; each one symlinks it in at
`docs/assets/macros.py` (the path the power modules use, so `module_name` reads the same).
The pages under `shared-charge-controllers/` are symlinked into two sites each, so the same
figure legitimately carries a different number on each site -- the number always matches
the nav the reader is looking at.

Note that a caption is emitted into raw HTML, so Markdown inside it is *not* processed.
Write captions as plain prose; use HTML entities if you need a special character.
"""

from urllib.parse import quote
from pathlib import Path
import os
import re
import json

# mkdocs-macros serialises the config for its debug/`{{ config }}` support, and our
# superfences config carries `!!python/name:` values whose keys are functions. Make
# json.dumps tolerate them rather than crash the build.
_orig_json_dumps = json.dumps


def _clean(obj):
    if isinstance(obj, dict):
        return {
            (k if isinstance(k, (str, int, float, bool, type(None))) else str(k)): _clean(v)
            for k, v in obj.items()
        }
    if isinstance(obj, (list, tuple, set)):
        return [_clean(x) for x in obj]
    return obj


def _patched_dumps(o, *a, **kw):
    return _orig_json_dumps(_clean(o), *a, **kw)


json.dumps = _patched_dumps

_PAGE_OFFSETS = {}        # rel_path -> number of figures before this page
_PAGE_TOTAL_COUNTS = {}   # rel_path -> count of figure macros on the page
_LOCAL_PAGE_COUNTS = {}   # src_path -> per-render counter, reset every build
_FIG_ID_MAP = {}          # explicit id -> global number
_SCANNED_DOCS_DIR = None  # guards against rescanning on live reload

FIGURE_BLOCK_RE = re.compile(r"\{\{\s*figure\s*\((.*?)\)\s*\}\}", re.DOTALL)
ID_RE = re.compile(r"""\bid\s*=\s*['"]([^'"]+)['"]""")


def _flatten(nav):
    for item in nav:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, list):
                    yield from _flatten(value)
                else:
                    yield value
        elif isinstance(item, str):
            yield item


def _all_pages(docs_dir):
    """Every Markdown page under docs_dir, as posix paths relative to it, sorted.

    Uses os.walk(followlinks=True) rather than Path.rglob: on Python 3.12 rglob does not
    descend into symlinked directories, and the shared sections of these sites --
    `vehicle-features`, `charger-can-interfaces`, `advos-yocto-system`, ... -- are all
    symlinks into products/shared-charge-controllers. With rglob every shared page that is
    absent from the nav silently fell through to offset 0 and restarted numbering at 1.
    """
    found, visited = [], set()
    for dirpath, dirnames, filenames in os.walk(docs_dir, followlinks=True):
        real = os.path.realpath(dirpath)
        if real in visited:  # a symlink pointing back up would otherwise loop
            dirnames[:] = []
            continue
        visited.add(real)
        for name in filenames:
            if name.endswith(".md"):
                rel = Path(dirpath, name).relative_to(docs_dir).as_posix()
                found.append(rel)
    return sorted(found)


def _scan_order(nav, docs_dir):
    """Nav pages in nav order, then every other Markdown page, sorted."""
    order, seen = [], set()
    for rel_path in _flatten(nav):
        if isinstance(rel_path, str) and rel_path.endswith(".md") and rel_path not in seen:
            seen.add(rel_path)
            order.append(rel_path)
    for rel_path in _all_pages(docs_dir):
        if rel_path not in seen:
            seen.add(rel_path)
            order.append(rel_path)
    return order


def _scan_sources(env):
    global _SCANNED_DOCS_DIR
    config_file = env.conf.get("config_file_path")
    root_dir = Path(config_file).parent if config_file else Path.cwd()
    docs_dir = root_dir / env.conf.get("docs_dir", "docs")
    if _SCANNED_DOCS_DIR == docs_dir:
        return
    _PAGE_OFFSETS.clear()
    _PAGE_TOTAL_COUNTS.clear()
    _FIG_ID_MAP.clear()

    total = 0
    for rel_path in _scan_order(env.conf.get("nav") or [], docs_dir):
        try:
            text = (docs_dir / rel_path).read_text(encoding="utf-8")
        except OSError:
            text = ""
        matches = FIGURE_BLOCK_RE.findall(text)
        _PAGE_OFFSETS[rel_path] = total
        _PAGE_TOTAL_COUNTS[rel_path] = len(matches)
        for i, call_args in enumerate(matches):
            found = ID_RE.search(call_args)
            if found:
                _FIG_ID_MAP[found.group(1)] = total + i + 1
        total += len(matches)
    _SCANNED_DOCS_DIR = docs_dir


def _img_style(size: str) -> str:
    """Turn a `size=` argument into an inline style.

    Percentages come from Docsify's `':size=80%'` annotation, which set the image width.
    Anything above 100% would overflow the content column (Docsify's own renderer let it),
    so it is clamped -- ">100%" only ever meant "as wide as you can". Absolute lengths come
    from the `bigger-NNN` wrappers and cap the width while staying responsive.
    """
    size = (size or "").strip()
    if not size:
        return "max-width:100%;height:auto;"
    if size.endswith("%"):
        try:
            pct = min(float(size[:-1]), 100.0)
        except ValueError:
            return "max-width:100%;height:auto;"
        pct = int(pct) if pct == int(pct) else pct
        return f"width:{pct}%;max-width:100%;height:auto;"
    return f"max-width:{size};width:100%;height:auto;"


def define_env(env):
    _scan_sources(env)
    # Per-page counters must start from zero on every build, or `mkdocs serve` renumbers
    # figures upwards on each reload.
    _LOCAL_PAGE_COUNTS.clear()

    def _page_key():
        page = getattr(env, "page", None)
        if page is not None and getattr(page, "file", None) is not None:
            return getattr(page.file, "src_path", "")
        return ""

    def figure(path: str, caption: str, alt: str = "", id: str = "", size: str = "") -> str:
        key = _page_key()
        _LOCAL_PAGE_COUNTS[key] = _LOCAL_PAGE_COUNTS.get(key, 0) + 1
        offset = _PAGE_OFFSETS.get(key)
        if offset is None:
            offset = _PAGE_OFFSETS.get(Path(key).name, 0)
        number = offset + _LOCAL_PAGE_COUNTS[key]

        fig_id = id or f"fig-{number}"
        return (
            f'<figure id="{fig_id}">'
            f'<img src="{quote(path)}" alt="{alt or caption}" style="{_img_style(size)}">'
            f"<figcaption>Figure {number}: {caption}</figcaption>"
            f"</figure>"
        )

    def figref(id: str) -> str:
        return f'<a href="#{id}">Figure {_FIG_ID_MAP.get(id, "?")}</a>'

    def figures_index() -> str:
        items = []
        for rel_path, offset in sorted(_PAGE_OFFSETS.items(), key=lambda kv: kv[1]):
            for i in range(_PAGE_TOTAL_COUNTS.get(rel_path, 0)):
                number = offset + i + 1
                items.append(f'<li><a href="#fig-{number}">Figure {number}</a></li>')
        if not items:
            return "<p>No figures.</p>"
        return (
            '<section class="figures-index">'
            "<h2>List of Figures</h2>"
            "<ol>" + "".join(items) + "</ol>"
            "</section>"
        )

    env.macro("figure", figure)
    env.macro("figref", figref)
    env.macro("figures_index", figures_index)
    env.variables["figure"] = figure
    env.variables["figref"] = figref
    env.variables["figures_index"] = figures_index
