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
