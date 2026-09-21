# CAN databases

## Format

The control interface for the ADB-PC-CH01 is provided as `.kcd` and `.dbc` files.
KCD is an open [format](https://github.com/julietkilo/kcd) based on XML. The KCD format is human readable and
is the core definition of the interface written by the firmware team at Advantics.
The more common DBC files that are provided are derived from the KCD files using automated procedures.

<!-- Find ADB-PC-CH01 CAN bus .kcd file here: [**ADB_PC_CH01.kcd**](../assets/ADB_PC_CH01.kcd) -->
<!-- Find ADB-PC-CH01 CAN bus .dbc file here: [**ADB_PC_CH01.dbc**](../assets/ADB_PC_CH01.dbc) -->

## API Versions

When new firmware is flashed to the device to e.g. improve electrical characteristics, the control interface may stay the same.
With other firmware updates new features may have been added that require a change to the control interface. To indicate if the control interface
has changed and in what way, each converter emmits a `CAN_API_Version` message that reports the version of the control interface. Different firmwares
with the same control interface are designed to behave the same way to external commands.

## CAN API Versions

| CAN API Version | .kcd file | .dbc file |
|-----------------|-----------|-----------|


# CAN frame ID format

The CAN frame ID is formatted as follows (24-bit identifier):

CAN ID (24‑bit) — field layout

| Field | Bits | Size | Description |
|-------|------|------:|------------|
| Register address | [7:0] | 8 bits | Register within the base frame (0x00–0xFF). |
| stack Position | [15:8] | 8 bits | Device address for multiple devices on the same CAN bus as in a stacked/parallel system. |
| Device type | [23:16] | 8 bits | Device type identifier (0–255).

**Device Type**

| ID   | Name | Function |
|------|------|----------|
| `0x81` | AC01 | 100 kW AC/DC (PFC) power module |
| `0x82` | DC01 | 100 kW DC/DC (isolated) power module |
| `0x83` | CH01 | 50 kW CCS EV charger power module |
| `0x85` | GN01 | Genset |
