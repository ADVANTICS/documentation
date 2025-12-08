# CAN databases

## Kayak format

Kayak is an open [format](https://github.com/julietkilo/kcd) based on XML, and is rather human readable (more than DBCs…). This is the main format for us. That is, we author the CAN DBs in this format, and our software and firmware use it directly.

Find ADB-PC-DC01 CAN bus .kcd file here: [**ADB_PC_DC01.kcd**](../assets/ADB_PC_DC01.kcd)

## DBC format

As a courtesy we also provide our CAN DBs in the more usual DBC format. Note these are automatically converted from the Kayak ones. Therefore, they are not the reference DBs.

Find ADB-PC-DC01 CAN bus .dbc file here: [**ADB_PC_DC01.dbc**](../assets/ADB_PC_DC01.dbc)

# CAN frame ID format

The CAN frame ID is formatted as follows (24-bit identifier):

CAN ID (24‑bit) — field layout

| Field | Bits | Size | Description |
|-------|------|------:|------------|
| Register address | [7:0] | 8 bits | Register within the base frame (0x00–0xFF). |
| stack Position | [15:8] | 8 bits | Device position in a stacked/parallel system. 0 = master/upper controller. |
| Device type | [23:16] | 8 bits | Device type identifier (0–255). Bit 23 is reserved as a CAN‑format flag — ADB series converters use IDs ≥ `0x80`. |

**Device Type**

| ID   | Name | Function |
|------|------|----------|
| `0x81` | AC01 | 100 kW AC/DC (PFC) power module |
| `0x82` | DC01 | 100 kW DC/DC (isolated) power module |
| `0x83` | CH01 | 50 kW CCS EV charger power module |
| `0x84` | DC02 | Non-isolated DC/DC |
| `0x85` | GN01 | Genset |
