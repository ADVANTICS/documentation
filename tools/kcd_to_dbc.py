#!/usr/bin/env python3
"""Convert CAN databases from KCD to DBC format."""

from __future__ import annotations

import argparse
import os
import sys
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Optional, Tuple

try:
    import cantools
    from cantools.database import load_file as load_can_database
    from cantools.database.can.formats import dbc as dbc_format
except Exception as exc:  # pragma: no cover - dependency import error path
    print("cantools is required. Install with: pip install cantools", file=sys.stderr)
    raise

ADB_DEVICE_TYPE_MAP: Dict[str, int] = {
    "GC01": 0x80,
    "AC01": 0x81,
    "DC01": 0x82,
    "CH01": 0x83,
    "DC02": 0x84,
    "GN01": 0x85,
}


def _transform_adb_id(base_id: int, device_type: int, position_within_stack: int = 0) -> int:
    """Compose a 24-bit ADB identifier from components."""
    reg = base_id & 0xFF
    pos = (position_within_stack & 0xFF) << 8
    dtype = (device_type & 0xFF) << 16
    return dtype | pos | reg


def _resolve_adb_device_value(adb_device_type: Optional[str]) -> int:
    if not adb_device_type:
        msg = "--generate-adb-ids requires --adb-device-type {GC01,AC01,DC01,CH01,DC02,GN01}"
        raise SystemExit(msg)

    if adb_device_type in ADB_DEVICE_TYPE_MAP:
        return ADB_DEVICE_TYPE_MAP[adb_device_type]

    try:
        return int(adb_device_type, 0)
    except Exception as exc:  # pragma: no cover - argument parsing error path
        valid = ", ".join(ADB_DEVICE_TYPE_MAP.keys())
        raise SystemExit(f"Unknown --adb-device-type '{adb_device_type}'. Expected one of {{{valid}}} or a numeric value.") from exc


@contextmanager
def _suppress_dbc_extended_flag() -> None:
    """Prevent cantools from OR-ing bit 31 so IDs stay within 24-bit ADB layout."""
    original = dbc_format.get_dbc_frame_id

    def _patched(message):  # type: ignore[override]
        return message.frame_id

    dbc_format.get_dbc_frame_id = _patched  # type: ignore[assignment]
    try:
        yield
    finally:
        dbc_format.get_dbc_frame_id = original  # type: ignore[assignment]


def _write_modified_kcd(
    *,
    source_path: str,
    destination_path: str,
    updated_ids: Dict[str, int],
) -> str:
    tree = ET.parse(source_path)
    root = tree.getroot()

    if "}" in root.tag:
        namespace = root.tag.split("}")[0].strip("{")
        ET.register_namespace("", namespace)
        msg_xpath = f".//{{{namespace}}}Message"
    else:
        msg_xpath = ".//Message"

    for msg in root.findall(msg_xpath):
        name = msg.get("name")
        if not name:
            continue
        if name in updated_ids:
            msg.set("id", hex(updated_ids[name]))

    os.makedirs(os.path.dirname(os.path.abspath(destination_path)), exist_ok=True)
    tree.write(destination_path, encoding="utf-8", xml_declaration=True)
    return destination_path


def convert_kcd_to_dbc(
    *,
    kcd_path: str,
    out_path: str,
    generate_adb_ids: bool,
    adb_device_type: Optional[str],
    write_modified_kcd: bool,
) -> Tuple[str, Optional[str]]:
    """Convert the given KCD file to DBC format and optionally emit a patched KCD."""
    if write_modified_kcd and not generate_adb_ids:
        raise SystemExit("--emit-modified-kcd requires --generate-adb-ids")

    db = load_can_database(kcd_path)
    id_map: Dict[str, int] = {}

    if generate_adb_ids:
        device_value = _resolve_adb_device_value(adb_device_type)
        for message in db.messages:
            new_id = _transform_adb_id(message.frame_id, device_value)
            message.frame_id = new_id
            id_map[message.name] = new_id

        with _suppress_dbc_extended_flag():
            dbc_content = dbc_format.dump_string(db)
    else:
        dbc_content = dbc_format.dump_string(db)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(dbc_content)

    modified_kcd_path: Optional[str] = None
    if write_modified_kcd:
        out_dir = Path(out_path).resolve().parent
        kcd_output = out_dir / (Path(out_path).stem + ".kcd")
        modified_kcd_path = _write_modified_kcd(
            source_path=kcd_path,
            destination_path=str(kcd_output),
            updated_ids=id_map,
        )

    return out_path, modified_kcd_path


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a DBC file from a KCD database")
    parser.add_argument("--kcd", required=True, help="Path to the source .kcd file")
    parser.add_argument("--out", required=True, help="Path to the output .dbc file")
    parser.add_argument(
        "--generate-adb-ids",
        action="store_true",
        help="Transform message IDs to ADB format (requires --adb-device-type)",
    )
    parser.add_argument(
        "--adb-device-type",
        default=None,
        help="ADB device type (GC01, AC01, DC01, CH01, DC02, GN01) or numeric value like 0x80",
    )
    parser.add_argument(
        "--emit-modified-kcd",
        action="store_true",
        help="Write a copy of the input KCD with transformed IDs next to the DBC output",
    )
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    dbc_out, modified_kcd = convert_kcd_to_dbc(
        kcd_path=args.kcd,
        out_path=args.out,
        generate_adb_ids=args.generate_adb_ids,
        adb_device_type=args.adb_device_type,
        write_modified_kcd=args.emit_modified_kcd,
    )
    print(f"Generated: {dbc_out}")
    if modified_kcd:
        print(f"Modified KCD: {modified_kcd}")


if __name__ == "__main__":
    main()
