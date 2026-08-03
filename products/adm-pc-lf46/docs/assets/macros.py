"""Deterministic global figure numbering based on nav order.

First figure in first nav page -> 1, then increases through nav pages.
Implementation: scan source files in nav order to count occurrences of the
`{{ figure(` macro pattern; compute per-page offsets; during render, assign
`Figure <offset + local_index>`.
Resilient to live reload (numbers won't jump) and independent of render sequence.
"""

from urllib.parse import quote
from pathlib import Path
import re
import json

# Monkeypatch json.dumps to avoid serialization errors caused by function keys.
_orig_json_dumps = json.dumps
def _clean(obj):
    if isinstance(obj, dict):
        return { (k if isinstance(k, (str,int,float,bool,type(None))) else str(k)) : _clean(v) for k,v in obj.items() }
    if isinstance(obj, (list,tuple,set)):
        return [ _clean(x) for x in obj ]
    return obj
def _patched_dumps(o,*a,**kw):
    return _orig_json_dumps(_clean(o),*a,**kw)
json.dumps = _patched_dumps

_PAGE_OFFSETS = {}     # rel_path -> starting figure number (0-based)
_PAGE_TOTAL_COUNTS = {}# rel_path -> count of figure macros
_LOCAL_PAGE_COUNTS = {}# src_path -> local counter during render
_SCAN_DONE = False

FIGURE_CALL_RE = re.compile(r"\{\{\s*figure\s*\(")

def _flatten(nav):
    for item in nav:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, list):
                    for sub in _flatten(value):
                        yield sub
                else:
                    yield title, value
        else:
            yield str(item), str(item)

def _scan_sources(env):
    global _SCAN_DONE
    if _SCAN_DONE:
        return
    nav = env.conf.get('nav', [])
    config_file = env.conf.get('config_file_path')
    root_dir = Path(config_file).parent if config_file else Path.cwd()
    docs_dir = root_dir / env.conf.get('docs_dir','docs')
    total = 0
    for _title, rel_path in _flatten(nav):
        candidate = docs_dir / rel_path
        if not candidate.exists():
            candidate = root_dir / rel_path
        try:
            text = candidate.read_text(encoding='utf-8')
        except Exception:
            text = ''
        count = len(FIGURE_CALL_RE.findall(text))
        _PAGE_OFFSETS[rel_path] = total
        _PAGE_TOTAL_COUNTS[rel_path] = count
        total += count
    _SCAN_DONE = True

def define_env(env):
    # Perform scan once per build
    _scan_sources(env)

    def _page_key():
        page = getattr(env,'page',None)
        if page and getattr(page,'file',None):
            return getattr(page.file,'src_path','')
        return ''

    def figure(path: str, caption: str, alt: str = '') -> str:
        pk = _page_key()  # e.g. 'overview.md'
        _LOCAL_PAGE_COUNTS[pk] = _LOCAL_PAGE_COUNTS.get(pk,0) + 1
        local_idx = _LOCAL_PAGE_COUNTS[pk]
        # Offset lookup (try exact, then basename)
        offset = _PAGE_OFFSETS.get(pk)
        if offset is None:
            offset = _PAGE_OFFSETS.get(Path(pk).name, 0)
        global_num = offset + local_idx
        fig_id = f'fig-{global_num}'
        href = quote(path)
        return (
            f'<figure id="{fig_id}">' \
            f'<img src="{href}" alt="{alt}" style="max-width:100%;height:auto;">' \
            f'<figcaption>Figure {global_num}: {caption}</figcaption>' \
            f'</figure>'
        )

    def figures_index() -> str:
        # Build index from offsets and counts
        items = []
        for rel_path, offset in sorted(_PAGE_OFFSETS.items(), key=lambda kv: kv[1]):
            count = _PAGE_TOTAL_COUNTS.get(rel_path,0)
            for i in range(count):
                num = offset + i + 1
                items.append(f'<li><a href="#fig-{num}">Figure {num}</a></li>')
        if not items:
            return '<p>No figures.</p>'
        return ('<section class="figures-index">'
                '<h2>List of Figures</h2>'
                '<ol>' + ''.join(items) + '</ol>'
                '</section>')

    env.macro('figure', figure)
    env.macro('figures_index', figures_index)
    # Provide variable access fallback
    env.variables['figure'] = figure
    env.variables['figures_index'] = figures_index