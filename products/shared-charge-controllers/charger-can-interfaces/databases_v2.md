# CAN databases

## Kayak format

Kayak is an [open format](https://github.com/julietkilo/kcd) based on XML, and is rather human
readable (more than DBCs...). This is the main format for us. That is, we author the CAN DBs in this
format, and our software and firmware use it directly.

- [Advantics Generic EVSE protocol v2.5](../charger-can-interfaces/Advantics_Generic_EVSE_protocol_v2.4.kcd ':ignore')

## DBC format

As a courtesy we also provide our CAN DBs in the more usual DBC format. Note these are automatically
converted from the Kayak ones. Therefore, they are not the reference DBs.

- [Advantics Generic EVSE protocol v2.5](../charger-can-interfaces/Advantics_Generic_EVSE_protocol_v2.4.dbc ':ignore')


## CAN ID index field

This section provides details about the config file section `[pistols]` for ADVANTICS SECC **releases 4.x**.
&nbsp;

**For customers using versions 3.x, please consult the actual config file, as it contains all the necessary information on each section.**

The generic interface abstracts away various charging standards operating over up to 3 pistols in parallel (CCS DC, AC, CHAdeMO).

The CAN ID index field serves as an identifier for each pistol (charging connector) in the charging system. It acts as an offset to the CAN IDs, allowing independent addressing of each pistol via the generic interface as an individual charger. 

Users must include the index value configured for each pistol in the CAN message identifier. The index field in the CAN identifier is represented by bits [28:24].

The following is an example:

    [pistols]
    enabled =
        CCS DC
    #    CCS AC
    #    CHAdeMO

    [pistol:CCS DC]
    # Pistol index. Must be a non-zero positive integer
    # unique with respect to other pistols.
    # Used to offset CAN addressing as well.
    index = 1

Based on this configuration, the CAN IDs of the generic interface used for the CCS DC pistol should be offset by the index value (01). The CAN message [**New_Charge_Session**](can.md#new_charge_session) declaration in the CAN database should become as follows:

    <Message id="0x01068001" length="8" name="New_Charge_Session" interval="100" format="extended">
