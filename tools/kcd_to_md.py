#!/usr/bin/env python3
"""
Generate Markdown documentation from a CAN bus .kcd database file.

Usage:
    python tools/kcd_to_md.py --kcd /path/to/db.kcd --out /path/to/output.md \
            [--reference-node NODE_NAME [NODE_NAME ...]] [--generate-adb-ids --adb-device-type {GC01,AC01,DC01,CH01,DC02,GN01}]

If --reference-node is provided, message Direction will be computed relative to
those nodes: messages produced by any of the nodes are marked OUT; messages received by
any of the nodes are marked IN. If not provided or unknown, Direction is left blank.

This script uses cantools to parse the KCD.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import os
import re
import sys
from typing import Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET
import textwrap

try:
    import cantools  # type: ignore
except Exception as e:  # pragma: no cover - dependency import error path
    print("cantools is required. Install with: pip install cantools", file=sys.stderr)
    raise


def _anchorize(name: str) -> str:
    # Match the style from existing docs: replace spaces with underscores, strip non-word except underscores
    safe = re.sub(r"\s+", "_", name.strip())
    safe = re.sub(r"[^A-Za-z0-9_\-]", "", safe)
    return safe


def _hex_id(frame_id: int) -> str:
    return f"0x{frame_id:x}"


def _signal_type(sig) -> str:
    # Determine human type name similar to examples
    if sig.choices:  # enumeration
        return "Label set"
    if sig.length == 1:
        return "Single bit"
    # cantools signals expose is_signed / is_float
    if getattr(sig, "is_float", False):
        return "Float"
    return "Signed" if sig.is_signed else "Unsigned"


def _format_num(val, default_blank: bool = True):
    if val is None:
        return "" if default_blank else "0"
    # ints are printed as-is; floats may need trimming
    if isinstance(val, float):
        # Avoid trailing .0; keep up to 6 decimals
        s = ("%.6f" % val).rstrip("0").rstrip(".")
        return s
    return str(val)


def _direction_for_message(msg, reference_nodes: Optional[List[str]],
                           kcd_producers: Optional[Dict[str, List[str]]] = None) -> str:
    if not reference_nodes:
        return ""
    # Prefer producers extracted from KCD to be robust to loader differences
    if kcd_producers is not None and msg.name in kcd_producers:
        prod = kcd_producers.get(msg.name, [])
        if any(ref in prod for ref in reference_nodes):
            return "OUT"
        if prod:  # someone else produces it
            return "IN"

    senders = list(msg.senders or [])
    receivers = list(msg.receivers or [])
    if any(ref in senders for ref in reference_nodes):
        return "OUT"
    # Some KCDs omit explicit receivers; if our node is not the sender and there is a sender,
    # treat as IN relative to our node.
    if senders and not any(ref in senders for ref in reference_nodes):
        return "IN"
    if any(ref in receivers for ref in reference_nodes):
        return "IN"
    return ""


# Mapping for ADB device types
ADB_DEVICE_TYPE_MAP: Dict[str, int] = {
    "GC01": 0x80,
    "AC01": 0x81,
    "DC01": 0x82,
    "CH01": 0x83,
    "DC02": 0x84,
    "GN01": 0x85,
}


def _transform_adb_id(base_id: int, device_type: int, position_within_stack: int = 0) -> int:
    """Compose 24-bit ADB-style ID from components.

    Layout:
    - bits [7:0]   Register address      -> base_id & 0xFF
    - bits [15:8]  Position within stack -> position_within_stack (default 0)
    - bits [23:16] Device type           -> device_type from ADB_DEVICE_TYPE_MAP
    Bits [31:24] are zero.
    """
    reg = base_id & 0xFF
    pos = (position_within_stack & 0xFF) << 8
    dtype = (device_type & 0xFF) << 16
    return dtype | pos | reg


def _div_open(classes: str) -> str:
    """Open a table wrapper div.

    ``markdown="1"`` is not optional: with the ``md_in_html`` extension enabled (it is, in
    every product here) python-markdown passes an HTML block through VERBATIM unless the
    element carries the attribute -- so the Markdown tables inside would render as literal
    "|---|---|" text. This is the single most repeated defect in this repo's history.
    """
    return f'\n<div class="{classes}" markdown="1">\n'


def _noheader_table_header(wrap_tables: bool, classes: str = "noheader-table small-table compact-table") -> str:
    """Return the header lines for a two-column captionless table, optionally wrapped in a div."""
    header = "| * | * |\n|---|---|"
    if wrap_tables:
        return f"{_div_open(classes)}\n{header}"
    return "\n" + header


def _escape(s: Optional[str]) -> str:
    # quote=False keeps apostrophes and quotation marks as themselves. They are harmless in
    # Markdown, and escaping them turned prose into "Controller&#x27;s applications" /
    # "&quot;max_current&quot;" -- which renders correctly but makes the generated page
    # unreadable and ungreppable at the source level.
    return html.escape(s or "", quote=False)


XREF_RE = re.compile(r"<<\s*([^<>]+?)\s*>>")


def _resolve_xrefs(
    s: str,
    message_names: set,
    message_anchor: "callable",
    page_xrefs: Dict[str, str],
    unresolved: Optional[set] = None,
) -> str:
    """Turn AsciiDoc cross-references in KCD notes into Markdown links.

    The databases use three forms:
      ``<<Message>>``          -> link to that message's section
      ``<<Message.Signal>>``   -> link to that signal's subsection
      ``<<Some page title>>``  -> only resolvable via ``page_xrefs`` (the KCDDOC-era
                                  ``make_can.sh`` did this with two hand-written ``sed``
                                  calls; passing a map keeps it declarative)

    Anything unresolved degrades to its plain text. It must never survive as ``<<x>>``:
    `_escape` would turn it into ``&lt;&lt;x&gt;&gt;`` and the reader sees the raw AsciiDoc
    markup on the page -- 40 of those are live on the charger pages today.
    """

    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        if target in page_xrefs:
            return f"[{target}]({page_xrefs[target]})"
        msg, _, sig = target.partition(".")
        if sig and msg in message_names:
            return f"[{target}](#{_anchorize(f'{msg}-{sig}')})"
        if target in message_names:
            return f"[{target}](#{message_anchor(target)})"
        # Dangling reference *in the database*: EVSE v3.5/v3.6 point at a
        # "Power_Transfer_Parameters" message that no longer exists. Degrade to plain text so
        # the page reads correctly, but record it -- silently swallowing it would hide a real
        # defect that only the DB owners can fix.
        if unresolved is not None:
            unresolved.add(target)
        return target

    return XREF_RE.sub(repl, s)


def _demote_headings(s: str) -> str:
    """Push ATX headings found inside a KCD note below the generated heading levels.

    A note may contain its own ``# Power function`` section (3 of them in EVSE v3.6). Left
    alone that emits an <h1> in the middle of a message's payload description: it outranks
    the page title, lands in the ToC as a top-level entry, and now also carries a permalink.
    Only unindented headings are touched -- an indented ``#`` is inside a code block.
    """
    return re.sub(
        r"^(#{1,6})(?=\s)",
        lambda m: "#" * min(6, len(m.group(1)) + 4),
        s,
        flags=re.MULTILINE,
    )


def _reindent_admonition_bodies(s: str) -> str:
    """Force every ``!!! type`` body to exactly one 4-space level.

    Some notes are authored with MkDocs admonition syntax directly in the ``.kcd`` -- and with
    the body indented 8 spaces (PEV v2.5's ``HV_Preparing_Hold_Off``). MkDocs takes the first 4
    as the admonition body and the next 4 as a *code block*, so the sentence renders in a grey
    monospace box. Relative indentation deeper than the block's own minimum is preserved, so
    genuine nested lists and code samples inside an admonition survive.
    """
    lines = s.split("\n")
    out: List[str] = []
    i = 0
    while i < len(lines):
        m = re.match(r"^(?P<ind>[ \t]*)!!!\s+\S", lines[i])
        out.append(lines[i])
        i += 1
        if not m:
            continue
        base = len(m.group("ind"))
        start = i
        while i < len(lines) and (
            not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > base
        ):
            i += 1
        body = lines[start:i]
        while body and not body[-1].strip():  # trailing blanks belong to the document
            body.pop()
        i = start + len(body)
        if body:
            inner = min(len(b) - len(b.lstrip()) for b in body if b.strip())
            out.extend("" if not b.strip() else " " * (base + 4) + b[inner:] for b in body)
    return "\n".join(out)


def _blank_line_before_lists(s: str) -> str:
    """python-markdown will not start a list on the line directly after a paragraph.

    The databases write notes the way AsciiDoc accepts them::

        This signal does nothing in the following situations:
        - <<DC_Power_Control.Setpoints_Mode>> == __Target_Mode__.

    which python-markdown renders as one run-on paragraph ("...situations: - Setpoints_Mode
    == Target_Mode."). Only the *first* marker of a block gets the blank line; inserting one
    before a later marker would split a single list in two. Lines indented by 4+ are skipped:
    they are code blocks or definition-list continuations.
    """
    return re.sub(
        r"^(?P<prev>(?!\s*$)(?![-*+] )(?!\d+\. )(?!#)(?!>)(?!\|)(?! {4})[^\n]*\S)\n"
        r"(?P<list>[ \t]{0,3}(?:[-*+]|\d+\.) )",
        lambda m: f"{m.group('prev')}\n\n{m.group('list')}",
        s,
        flags=re.MULTILINE,
    )


def _indent_for_admonition(body: str, indent: str = "    ") -> str:
    """Indent content for MkDocs '!!!' blocks. Blank lines must also be indented."""
    lines = body.split("\n")
    return "\n".join((indent + ln) if ln.strip() != "" else "" for ln in lines)


def _asciidoc_admonitions_to_mkdocs(s: str) -> str:
    """
    Convert blocks like:
        [IMPORTANT]
        ====
        body...
        ====
    into:
        !!! important
            body...
    """
    tag_map = {
        "important": "important",
        "warning": "warning",
        "caution": "warning",
        "note": "note",
        "tip": "tip",
        "info": "info",
        "danger": "danger",
    }

    lines = s.split("\n")
    out: List[str] = []
    i = 0
    
    # Regex for the tag line: [TAG]
    tag_re = re.compile(r"^\s*\[(?P<tag>[A-Za-z0-9_-]+)\]\s*$")
    # Regex for the fence line: ==== (4 or more =)
    fence_re = re.compile(r"^\s*={4,}\s*$")

    while i < len(lines):
        line = lines[i]
        m = tag_re.match(line)
        
        # Check if this line is a tag AND the next line is a fence
        is_block_start = False
        fence_idx = -1
        
        if m:
            # Check immediate next line
            if (i + 1 < len(lines)) and fence_re.match(lines[i+1]):
                is_block_start = True
                fence_idx = i + 1
            # Check next line if current is followed by blank line (optional robustness)
            elif (i + 2 < len(lines)) and not lines[i+1].strip() and fence_re.match(lines[i+2]):
                is_block_start = True
                fence_idx = i + 2
        
        if is_block_start:
            tag = m.group("tag").lower()
            mk_tag = tag_map.get(tag, tag)
            
            # Skip to body
            i = fence_idx + 1
            
            body_lines = []
            while i < len(lines):
                if fence_re.match(lines[i]):
                    # Found closing fence
                    i += 1
                    break
                body_lines.append(lines[i])
                i += 1
            
            # Format as MkDocs admonition
            if out and out[-1].strip():
                out.append("")
            
            out.append(f"!!! {mk_tag}")
            
            # Process body: dedent and indent
            body = "\n".join(body_lines)
            body = textwrap.dedent(body)
            out.append(_indent_for_admonition(body))
            out.append("")
            
        else:
            # AsciiDoc's *single-line* form: "NOTE: text", continuing until a blank line.
            # Without this the label leaks onto the page as literal "NOTE:" / "WARNING:"
            # text -- 6 of those in PEV v2.5 alone. The trailing colon is what distinguishes
            # it from label names such as "WARNING_CertificateExpired".
            m1 = INLINE_ADMONITION_RE.match(line)
            if m1:
                mk_tag = tag_map.get(m1.group("tag").lower(), "note")
                body = [m1.group("body").strip()]
                i += 1
                while i < len(lines) and lines[i].strip():
                    body.append(lines[i].strip())
                    i += 1
                if out and out[-1].strip():
                    out.append("")
                out.append(f"!!! {mk_tag}")
                out.extend(f"    {b}" for b in body)
                out.append("")
                continue
            out.append(line)
            i += 1

    return "\n".join(out)


INLINE_ADMONITION_RE = re.compile(
    r"^(?P<tag>NOTE|TIP|IMPORTANT|WARNING|CAUTION):[ \t]+(?P<body>\S.*)$"
)


def _mkdocs_admonitions_to_github_callouts(s: str) -> str:
    """Convert MkDocs admonitions:

        !!! info
            text

    into GitHub callouts:

        > [!INFO]
        > text
    """

    # Accept common MkDocs tags; leave unknown tags as-is but uppercased.
    tag_re = re.compile(
        r'^\s*!!!\s+(?P<tag>[A-Za-z0-9_-]+)(?:\s+"(?P<title>[^"]+)")?\s*$'
    )

    lines = s.split("\n")
    out: List[str] = []
    i = 0
    while i < len(lines):
        m = tag_re.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        tag = m.group("tag").upper()
        title = m.group("title")

        # Collect indented body lines following the '!!!' line.
        i += 1
        body: List[str] = []
        while i < len(lines):
            ln = lines[i]

            # Stop if next admonition starts or we hit a non-indented line (end of block).
            if tag_re.match(ln):
                break

            if ln.strip() == "":
                body.append("")
                i += 1
                continue

            if ln.startswith("\t"):
                # Remove exactly one indent level; we'll dedent the remainder later.
                body.append(ln[1:])
                i += 1
                continue

            if ln.startswith("    "):
                # Remove exactly one indent level; we'll dedent the remainder later.
                body.append(ln[4:])
                i += 1
                continue

            # Not indented => block ended.
            break

        # Dedent body in case it had deeper indentation than a single level.
        body_text = "\n".join(body)
        body_text = textwrap.dedent(body_text)
        body = body_text.split("\n") if body_text else []

        # Emit GitHub callout.
        # Use Markdown hard line breaks (two trailing spaces) to preserve
        # original newlines inside the callout in renderers that reflow text.
        out.append(f"> [!{tag}]")
        if title:
            out.append(f"> {title}  ")
        for bl in body:
            if bl == "":
                out.append(">")
            else:
                out.append(f"> {bl}  ")

        # Add a blank line after the callout if the next line is normal text
        # (keeps separation similar to MkDocs rendering).
        if i < len(lines) and lines[i].strip() and out and out[-1].strip():
            out.append("")

    return "\n".join(out)


DEF_LIST_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<term>[^\s:][^\n]*?)::[ \t]+(?P<def>.*)$")


def _convert_asciidoc_definition_lists(s: str, style: str = "bullets") -> str:
    """Convert AsciiDoc definition lists (``Term:: Definition``) to Markdown.

    ``bullets``      -> ``- **Term**: Definition``  (compact; used by the charger pages and
                        the power modules)
    ``admonitions``  -> ``!!! note "Term"`` + indented body, which is what KCDDOC emitted and
                        therefore what the vehicle pages have always looked like. Underscores
                        in the term become spaces, as KCDDOC did.

    Continuation lines (more deeply indented than the term) belong to the definition and are
    re-indented under it -- otherwise an admonition body would fall outside the block.
    """
    lines = s.split("\n")
    out: List[str] = []
    i = 0
    while i < len(lines):
        m = DEF_LIST_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        base = len(m.group("indent"))
        body = [m.group("def")]
        j = i + 1
        while j < len(lines):
            ln = lines[j]
            if not ln.strip():  # a blank line ends the item unless a deeper line follows
                nxt = next((k for k in range(j + 1, len(lines)) if lines[k].strip()), None)
                if (nxt is not None and not DEF_LIST_RE.match(lines[nxt])
                        and len(lines[nxt]) - len(lines[nxt].lstrip()) > base):
                    body.append("")
                    j += 1
                    continue
                break
            if DEF_LIST_RE.match(ln) or len(ln) - len(ln.lstrip()) <= base:
                break
            body.append(ln.strip())
            j += 1
        indent = m.group("indent")
        if style == "admonitions":
            out.append(f'{indent}!!! note "{m.group("term").replace("_", " ").strip()}"')
            out.extend(f"{indent}    {b}" if b else "" for b in body)
            out.append("")
        else:
            out.append(f'{indent}- **{m.group("term")}**: {body[0]}')
            out.extend(f"{indent}    {b}" if b else "" for b in body[1:])
        i = j
    return "\n".join(out)


def _normalize_notes_text(
    text: Optional[str],
    *,
    github_callouts: bool = False,
    definition_list_style: str = "bullets",
    xref_resolver: "callable" = None,
) -> str:
    """Normalize KCD Notes to be Markdown-friendly (remove leading indentation,
    trim trailing spaces, and collapse excessive blank lines)."""
    if not text:
        return ""
    # Normalize newlines and dedent common leading indentation
    s = text.replace("\r\n", "\n").replace("\r", "\n")
    s = textwrap.dedent(s)
    # Normalize exotic spaces often coming from XML editors (NBSP, narrow no-break)
    s = s.replace("\u00A0", " ").replace("\u2007", " ").replace("\u202F", " ")
    # Dedent common indentation but preserve relative extra indentation (for code blocks)
    s = textwrap.dedent(s)
    # Strip trailing spaces per line but keep leading spaces (to preserve relative indentation)
    lines = [ln.rstrip() for ln in s.split("\n")]
    s = "\n".join(lines)
    # Trim leading/trailing blank lines
    s = s.strip("\n")
    # Collapse 3+ consecutive blank lines to max 1
    s = re.sub(r"\n{3,}", "\n\n", s)

    # Convert Asciidoc-like admonitions to MkDocs admonitions
    s = _asciidoc_admonitions_to_mkdocs(s)

    # Optionally convert MkDocs admonitions (!!!) to GitHub callouts (> [!TAG])
    if github_callouts:
        s = _mkdocs_admonitions_to_github_callouts(s)

    # Convert AsciiDoc definition lists to Markdown bullet lists
    s = _convert_asciidoc_definition_lists(s, definition_list_style)

    # Cross-references and stray headings, before the caller HTML-escapes the text (an
    # unresolved "<<x>>" would come out of _escape() as visible "&lt;&lt;x&gt;&gt;").
    if xref_resolver is not None:
        s = xref_resolver(s)
    s = _demote_headings(s)
    s = _blank_line_before_lists(s)
    s = _reindent_admonition_bodies(s)

    # Final cleanup
    s = re.sub(r"\n{3,}", "\n\n", s).strip("\n")
    return s


def _parse_kcd_producers(kcd_path: str) -> Dict[str, List[str]]:
    """Parse raw KCD to map message name -> list of producer node names."""
    try:
        tree = ET.parse(kcd_path)
        root = tree.getroot()
    except Exception:
        return {}

    # Namespace handling
    ns = {'kcd': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    # Map node id -> name
    nodes: Dict[str, str] = {}
    for n in root.findall('kcd:Node', ns) if ns else root.findall('Node'):
        nid = n.get('id')
        nname = n.get('name')
        if nid is not None and nname:
            nodes[nid] = nname

    producers: Dict[str, List[str]] = {}
    msg_paths = 'kcd:Bus/kcd:Message' if ns else 'Bus/Message'
    for m in root.findall(msg_paths, ns):
        mname = m.get('name')
        if not mname:
            continue
        prods: List[str] = []
        for pref in m.findall('kcd:Producer/kcd:NodeRef', ns) if ns else m.findall('Producer/NodeRef'):
            nid = pref.get('id')
            if nid in nodes:
                prods.append(nodes[nid])
        if prods:
            producers[mname] = prods
    return producers


def generate_markdown(
    kcd_path: str,
    out_path: str,
    reference_nodes: Optional[List[str]],
    *,
    wrap_tables: bool = False,
    id_style: str = "braces",
    generate_adb_ids: bool = False,
    adb_device_type: Optional[str] = None,
    github_callouts: bool = False,
    message_id_style: str = "explicit",
    definition_list_style: str = "bullets",
    page_xrefs: Optional[Dict[str, str]] = None,
    front_matter: Optional[str] = None,
    exclude_messages: Optional[List[str]] = None,
) -> str:
    db = cantools.db.load_file(kcd_path)
    kcd_producers = _parse_kcd_producers(kcd_path)

    # One database serves several controllers, and a controller that cannot do AC charging should
    # not be handed the AC messages: the MCS vehicle controller has no AC at all. The database is
    # shared and stays complete -- the filtering is a property of the *page*, not of the .kcd.
    #
    # A name listed here that the database does not have is an error, not a no-op: if a message is
    # renamed upstream, silently dropping the filter would republish AC messages on a page that
    # must not carry them, and nothing would say so.
    excluded = list(exclude_messages or [])
    present = {m.name for m in db.messages}
    missing = [name for name in excluded if name not in present]
    if missing:
        raise SystemExit(
            f"--exclude-message: not in {kcd_path}: {', '.join(sorted(missing))}. "
            "The database may have renamed them; update the exclusion list."
        )
    messages = [m for m in db.messages if m.name not in set(excluded)]

    # How a message section is addressed. "explicit" gives '## Name { #Name }', matching the
    # power modules and the charger pages. "slug" leaves the heading bare and lets the toc
    # extension slugify it (lowercased, underscores kept), which is what KCDDOC produced and
    # what the ~40 inbound links to the vehicle pages already point at.
    message_names = {m.name for m in messages}

    def message_anchor(name: str) -> str:
        return name.lower() if message_id_style == "slug" else _anchorize(name)

    unresolved_xrefs: set = set()

    def notes(text: Optional[str]) -> str:
        return _normalize_notes_text(
            text,
            github_callouts=github_callouts,
            definition_list_style=definition_list_style,
            xref_resolver=lambda s: _resolve_xrefs(
                s, message_names, message_anchor, page_xrefs or {}, unresolved_xrefs
            ),
        )

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    rel_note = f"{kcd_path} CAN Database documentation file\nAutomatically generated by KCDDOC"

    # Build message index rows
    index_rows: List[Tuple[str, str, int, str, Optional[int]]] = []
    # Resolve device type value if requested
    adb_device_value: Optional[int] = None
    if generate_adb_ids:
        if not adb_device_type:
            raise SystemExit("--generate-adb-ids requires --adb-device-type {GC01,AC01,DC01,CH01,DC02,GN01}")
        if adb_device_type in ADB_DEVICE_TYPE_MAP:
            adb_device_value = ADB_DEVICE_TYPE_MAP[adb_device_type]
        else:
            # Allow numeric hex like 0x80 as fallback
            try:
                adb_device_value = int(adb_device_type, 0)
            except Exception as e:
                raise SystemExit(f"Unknown --adb-device-type '{adb_device_type}'. Expected one of {list(ADB_DEVICE_TYPE_MAP.keys())} or a hex value.")

    for msg in messages:
        name = msg.name
        # Apply optional ADB ID transformation
        id_num = _transform_adb_id(msg.frame_id, adb_device_value) if (generate_adb_ids and adb_device_value is not None) else msg.frame_id
        frame_id = _hex_id(id_num)
        length = msg.length
        direction = _direction_for_message(msg, reference_nodes, kcd_producers)
        cycle = msg.cycle_time  # may be None
        index_rows.append((name, frame_id, length, direction, cycle))

    # Sort by frame_id ascending
    index_rows.sort(key=lambda r: int(r[1], 16))

    out_lines: List[str] = []

    if front_matter:
        out_lines.append(front_matter.rstrip("\n"))
        out_lines.append("")
    out_lines.append("# CAN messages")
    out_lines.append("")
    out_lines.append("## Message index")
    out_lines.append("")
    if wrap_tables:
        out_lines.append(_div_open("compact-table"))
    out_lines.append("| Name | ID | Length | Direction | Cycle time |")
    out_lines.append("|------|----|--------|-----------|------------|")
    for name, fid, length, direction, cycle in index_rows:
        anchor = message_anchor(name)
        dir_s = direction or ""
        cyc_s = _format_num(cycle)
        out_lines.append(f"| [{name}](#{anchor}) | {fid} | {length} | {dir_s} | {cyc_s} |")
    if wrap_tables:
        out_lines.append("\n</div>\n")
    out_lines.append("")

    # Details per message
    for msg in sorted(messages, key=lambda m: m.frame_id):
        m_anchor = _anchorize(msg.name)
        out_lines.append("")
        if message_id_style == "slug":
            # The toc extension slugifies '## EVSE_Information' to '#evse_information'; adding
            # an explicit id here instead would silently break every existing inbound link.
            out_lines.append(f"## {msg.name}")
        else:
            # Explicit HTML anchor for robust linking in Markdown renderers
            out_lines.append(f"<a id=\"{m_anchor}\"></a>")
            if id_style == "colon":
                # Docsify-style IDs (example legacy format)
                out_lines.append(f"## {msg.name}")
            else:
                # MkDocs-style heading ID
                out_lines.append(f"## {msg.name} {{ #{m_anchor} }}")
        out_lines.append("")
        out_lines.append(_noheader_table_header(wrap_tables))
        # Apply the same optional ADB ID transformation in details
        id_num = _transform_adb_id(msg.frame_id, adb_device_value) if (generate_adb_ids and adb_device_value is not None) else msg.frame_id
        out_lines.append("| **Frame ID** | " + _hex_id(id_num) + " |")
        out_lines.append("| **Length [Bytes]** | " + str(msg.length) + " |")
        out_lines.append("| **Periodicity [ms]** | " + _format_num(msg.cycle_time) + " |")
        out_lines.append("| **Direction** | " + _direction_for_message(msg, reference_nodes, kcd_producers) + " |")
        if wrap_tables:
            out_lines.append("\n</div>\n")
        out_lines.append("")

        out_lines.append("### Description")
        out_lines.append("")
        if msg.comment:
            normalized = notes(msg.comment)
            if normalized:
                out_lines.append(normalized if github_callouts else _escape(normalized))
                out_lines.append("")
        else:
            out_lines.append("\n")

        # Payload signals summary table
        out_lines.append("### Payload")
        out_lines.append("")
        if wrap_tables:
            out_lines.append(_div_open("small-table compact-table"))
        out_lines.append("| Signal | Length (bits) | Type |")
        out_lines.append("|--------|---------------|------|")
        for sig in msg.signals:
            out_lines.append(
                f"| {sig.name} | {sig.length} | {_signal_type(sig)} |"
            )
        if wrap_tables:
            out_lines.append("\n</div>\n")
        out_lines.append("")

        out_lines.append("### Payload description")
        out_lines.append("")
        for sig in msg.signals:
            sig_anchor = _anchorize(f"{msg.name}-{sig.name}")
            if id_style == "colon":
                out_lines.append(f"#### {sig.name} :id={sig_anchor}")
            else:
                out_lines.append(f"#### {sig.name} {{ #{sig_anchor} }}")
            out_lines.append("")
            if sig.comment:
                normalized_sig = notes(sig.comment)
                if normalized_sig:
                    out_lines.append(normalized_sig if github_callouts else _escape(normalized_sig))
                    out_lines.append("")

            # Per-signal parameter table
            if wrap_tables:
                out_lines.append(_div_open("small-table compact-table"))
            out_lines.append(
                "| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |"
            )
            out_lines.append(
                "|-----------|---------------|------|------|-------|--------|-----|-----|"
            )
            unit = sig.unit or ""
            scale = _format_num(sig.scale if hasattr(sig, "scale") else sig.factor)
            if scale == "":
                scale = _format_num(getattr(sig, "factor", None))
            # cantools uses factor/offset; also exposes minimum/maximum
            offset = _format_num(sig.offset)
            smin = _format_num(sig.minimum)
            smax = _format_num(sig.maximum)
            out_lines.append(
                f"| {sig.start} | {sig.length} | {_signal_type(sig)} | {unit} | {scale or 1} | {offset or 0} | {smin} | {smax} |"
            )
            if wrap_tables:
                out_lines.append("\n</div>\n")
            out_lines.append("")

            # Label set table if present
            if sig.choices:
                if wrap_tables:
                    out_lines.append(_div_open("small-table compact-table"))
                out_lines.append("| Label name | Value |")
                out_lines.append("|------------|-------|")
                # choices: Dict[value(int)] = name(str)
                for val, name in sorted(sig.choices.items(), key=lambda kv: kv[0]):
                    out_lines.append(f"| {name} | {val} |")
                if wrap_tables:
                    out_lines.append("\n</div>\n")
                out_lines.append("")

    content = "\n".join(out_lines).rstrip() + "\n"

    if unresolved_xrefs:
        print(
            f"warning: {len(unresolved_xrefs)} cross-reference(s) in {os.path.basename(kcd_path)} "
            f"point at nothing and were rendered as plain text: "
            + ", ".join(f"<<{x}>>" for x in sorted(unresolved_xrefs)),
            file=sys.stderr,
        )

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Generate Markdown docs from a KCD file")
    ap.add_argument("--kcd", required=True, help="Path to .kcd file")
    ap.add_argument("--out", required=True, help="Path to output .md file")
    ap.add_argument(
        "--reference-node",
        nargs="+",
        default=None,
        help=(
            "Node name(s) used to decide Direction (OUT if producer is one of these nodes, IN if receiver)."
        ),
    )
    ap.add_argument(
        "--wrap-tables-in-divs",
        action="store_true",
        help="Wrap Markdown tables in HTML <div> with CSS classes (disabled by default for mkdocs)",
    )
    ap.add_argument(
        "--id-style",
        choices=["braces", "colon"],
        default="braces",
        help=(
            "Heading ID syntax: 'braces' -> '#### Name { #id }' (MkDocs style), "
            "'colon' -> '#### Name :id=id' (Docsify style)."
        ),
    )
    ap.add_argument(
        "--generate-adb-ids",
        action="store_true",
        help="Generate ADB-styled message IDs (device type in bits [23:16], position [15:8]=0, register [7:0]=original ID)",
    )
    ap.add_argument(
        "--adb-device-type",
        default=None,
        help="ADB device type (one of GC01, AC01, DC01, CH01, DC02, GN01) or a numeric value like 0x80. Required when --generate-adb-ids is set.",
    )
    ap.add_argument(
        "--message-id-style",
        choices=["explicit", "slug"],
        default="explicit",
        help=(
            "How message sections are addressed. 'explicit' -> '## Name { #Name }' (power "
            "modules, charger pages). 'slug' -> bare '## Name', addressed as '#name' by the "
            "toc extension (KCDDOC's behaviour, which the vehicle pages' inbound links use)."
        ),
    )
    ap.add_argument(
        "--definition-list-style",
        choices=["bullets", "admonitions"],
        default="bullets",
        help=(
            "Render AsciiDoc 'Term:: text' notes as '- **Term**: text' (default) or as "
            "'!!! note \"Term\"' blocks, which is what KCDDOC emitted."
        ),
    )
    ap.add_argument(
        "--page-xref",
        action="append",
        default=[],
        metavar="TARGET=LINK",
        help=(
            "Resolve a non-message '<<TARGET>>' cross-reference to LINK, e.g. "
            "--page-xref 'CAN sensor=../configuration/can_sensor.md'. Repeatable."
        ),
    )
    ap.add_argument(
        "--exclude-message",
        action="append",
        default=[],
        metavar="NAME",
        help=(
            "Leave a message out of the page entirely -- index, body and cross-reference "
            "targets. For a controller the message does not apply to (the MCS vehicle "
            "controller has no AC charging). Repeatable. Errors if NAME is not in the database."
        ),
    )
    ap.add_argument(
        "--front-matter",
        default=None,
        help="YAML front matter to prepend, e.g. $'---\\nhide:\\n  - toc\\n---'",
    )
    ap.add_argument(
        "--github-callouts",
        action="store_true",
        help="Convert MkDocs admonitions (!!! info/warning/...) found in Notes into GitHub callouts (> [!INFO]).",
    )
    args = ap.parse_args()

    out = generate_markdown(
        args.kcd,
        args.out,
        args.reference_node,
        wrap_tables=args.wrap_tables_in_divs,
        id_style=args.id_style,
        generate_adb_ids=args.generate_adb_ids,
        adb_device_type=args.adb_device_type,
        github_callouts=args.github_callouts,
        message_id_style=args.message_id_style,
        definition_list_style=args.definition_list_style,
        page_xrefs=dict(x.split("=", 1) for x in args.page_xref),
        front_matter=args.front_matter,
        exclude_messages=args.exclude_message,
    )
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()
