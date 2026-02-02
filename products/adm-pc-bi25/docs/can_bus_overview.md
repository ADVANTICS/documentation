# CAN databases

## Kayak format

Kayak is an open [format](https://github.com/julietkilo/kcd) based on XML, and is rather human readable (more than DBCs…). This is the main format for us. That is, we author the CAN DBs in this format, and our software and firmware use it directly.

Find ADB-PC-DC01 CAN bus .kcd file here: [**ADM_PC_BI25.kcd**](../assets/ADM_PC_BI25.kcd)

## DBC format

As a courtesy we also provide our CAN DBs in the more usual DBC format. Note these are automatically converted from the Kayak ones. Therefore, they are not the reference DBs.

Find ADB-PC-DC01 CAN bus .dbc file here: [**ADM_PC_BI25.dbc**](../assets/ADM_PC_BI25.dbc)

# CAN frame ID format

The CAN frame ID is formatted as follows (24-bit identifier):

CAN ID (24‑bit) — field layout

| Field | Bits | Size | Description |
|-------|------|------:|------------|
| Register address | [15:0] | 16 bits | 16bit field allocated that is intended to address a sub-set of the registers 0x0000 to 0x7fff in the base frame (16 identifier bits). The bit 15 is reserved as direction bit. |
| Device (service) type | [23:16] | 8 bits | 8bit field allows for up to 256 device types. This field uniquely identifies the addressed device by its type. This filed can be also used by common services running on modules. Typically these are services run temporarily and behave as a “virtual” device, therefore they have device type assigned to them. |
|Position within stack field | [28:24] | 5 bits | 5bit field allows for up to 32 stacked devices. In systems where more than one device is stacked (i.e. paralleled), this field indicates the position of the addressed device in the stack. The position 0 is reserved to the master if master semantics make sense for given stack setup.|
