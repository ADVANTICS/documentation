#!/usr/bin/env python3
"""
Generate Markdown documentation from a CAN bus .kcd database file.

Usage:
  python tools/kcd_to_md.py --kcd /path/to/db.kcd --out /path/to/output.md \
      [--reference-node NODE_NAME]

If --reference-node is provided, message Direction will be computed relative to
that node: messages produced by the node are marked OUT; messages received by
the node are marked IN. If not provided or unknown, Direction is left blank.

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


def _direction_for_message(msg, reference_node: Optional[str],
                           kcd_producers: Optional[Dict[str, List[str]]] = None) -> str:
    if not reference_node:
        return ""
    ref = reference_node
    # Prefer producers extracted from KCD to be robust to loader differences
    if kcd_producers is not None and msg.name in kcd_producers:
        prod = kcd_producers.get(msg.name, [])
        if ref in prod:
            return "OUT"
        if prod:  # someone else produces it
            return "IN"

    senders = list(msg.senders or [])
    receivers = list(msg.receivers or [])
    if ref in senders:
        return "OUT"
    # Some KCDs omit explicit receivers; if our node is not the sender and there is a sender,
    # treat as IN relative to our node.
    if senders and ref not in senders:
        return "IN"
    if ref in receivers:
        return "IN"
    return ""


def _noheader_table_header(wrap_tables: bool, classes: str = "noheader-table small-table compact-table") -> str:
    """Return the header lines for a two-column captionless table, optionally wrapped in a div."""
    header = "| * | * |\n|---|---|"
    if wrap_tables:
        return f"\n<div class=\"{classes}\">\n\n{header}"
    return "\n" + header


def _escape(s: Optional[str]) -> str:
    return html.escape(s or "")


def _normalize_notes_text(text: Optional[str]) -> str:
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


def generate_markdown(kcd_path: str, out_path: str, reference_node: Optional[str], *, wrap_tables: bool = False) -> str:
    db = cantools.db.load_file(kcd_path)
    kcd_producers = _parse_kcd_producers(kcd_path)

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    rel_note = f"{kcd_path} CAN Database documentation file\nAutomatically generated by KCDDOC"

    # Build message index rows
    index_rows: List[Tuple[str, str, int, str, Optional[int]]] = []
    for msg in db.messages:
        name = msg.name
        frame_id = _hex_id(msg.frame_id)
        length = msg.length
        direction = _direction_for_message(msg, reference_node, kcd_producers)
        cycle = msg.cycle_time  # may be None
        index_rows.append((name, frame_id, length, direction, cycle))

    # Sort by frame_id ascending
    index_rows.sort(key=lambda r: int(r[1], 16))

    out_lines: List[str] = []

    out_lines.append("<!--")
    out_lines.append(_escape(rel_note))
    out_lines.append("-->")
    out_lines.append("")
    out_lines.append("# CAN messages")
    out_lines.append("")
    out_lines.append("## Message index")
    out_lines.append("")
    if wrap_tables:
        out_lines.append("\n<div class=\"compact-table\">\n")
    out_lines.append("| Name | ID | Length | Direction | Cycle time |")
    out_lines.append("|------|----|--------|-----------|------------|")
    for name, fid, length, direction, cycle in index_rows:
        anchor = _anchorize(name)
        dir_s = direction or ""
        cyc_s = _format_num(cycle)
        out_lines.append(f"| [{name}](#{anchor}) | {fid} | {length} | {dir_s} | {cyc_s} |")
    if wrap_tables:
        out_lines.append("\n</div>\n")
    out_lines.append("")

    # Details per message
    for msg in sorted(db.messages, key=lambda m: m.frame_id):
        m_anchor = _anchorize(msg.name)
        out_lines.append("")
        # Explicit HTML anchor for robust linking in Markdown renderers
        out_lines.append(f"<a id=\"{m_anchor}\"></a>")
        out_lines.append(f"## {msg.name} {{ #{m_anchor} }}")
        out_lines.append("")
        out_lines.append(_noheader_table_header(wrap_tables))
        out_lines.append("| **Frame ID** | " + _hex_id(msg.frame_id) + " |")
        out_lines.append("| **Length [Bytes]** | " + str(msg.length) + " |")
        out_lines.append("| **Periodicity [ms]** | " + _format_num(msg.cycle_time) + " |")
        out_lines.append("| **Direction** | " + _direction_for_message(msg, reference_node, kcd_producers) + " |")
        if wrap_tables:
            out_lines.append("\n</div>\n")
        out_lines.append("")

        out_lines.append("### Description")
        out_lines.append("")
        if msg.comment:
            normalized = _normalize_notes_text(msg.comment)
            if normalized:
                out_lines.append(_escape(normalized))
                out_lines.append("")
        else:
            out_lines.append("\n")

        # Payload signals summary table
        out_lines.append("### Payload")
        out_lines.append("")
        if wrap_tables:
            out_lines.append("\n<div class=\"small-table compact-table\">\n")
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
            out_lines.append(f"#### {sig.name} {{ #{sig_anchor} }}")
            out_lines.append("")
            if sig.comment:
                normalized_sig = _normalize_notes_text(sig.comment)
                if normalized_sig:
                    out_lines.append(_escape(normalized_sig))
                    out_lines.append("")

            # Per-signal parameter table
            if wrap_tables:
                out_lines.append("\n<div class=\"small-table compact-table\">\n")
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
                    out_lines.append("\n<div class=\"small-table compact-table\">\n")
                out_lines.append("| Label name | Value |")
                out_lines.append("|------------|-------|")
                # choices: Dict[value(int)] = name(str)
                for val, name in sorted(sig.choices.items(), key=lambda kv: kv[0]):
                    out_lines.append(f"| {name} | {val} |")
                if wrap_tables:
                    out_lines.append("\n</div>\n")
                out_lines.append("")

    content = "\n".join(out_lines).rstrip() + "\n"

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
        default=None,
        help=(
            "Node name used to decide Direction (OUT if producer is this node, IN if receiver)."
        ),
    )
    ap.add_argument(
        "--wrap-tables-in-divs",
        action="store_true",
        help="Wrap Markdown tables in HTML <div> with CSS classes (disabled by default for mkdocs)",
    )
    args = ap.parse_args()

    out = generate_markdown(args.kcd, args.out, args.reference_node, wrap_tables=args.wrap_tables_in_divs)
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()
