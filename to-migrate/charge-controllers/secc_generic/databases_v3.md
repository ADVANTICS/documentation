> [!UPDATE] {docsify-updated}
# CAN databases

See [all messages page](charge-controllers/secc_generic/can_v3).

Download CAN DBs:

- [Advantics Generic EVSE protocol v3.3 (Kayak format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.3.kcd ':ignore')
- [Advantics Generic EVSE protocol v3.3 (DBC format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.3.dbc ':ignore')

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

Based on this configuration, the CAN IDs of the generic interface used for the CCS DC pistol should be offset by the index value (01). The CAN message [**New_Charge_Session**](charge-controllers/secc_generic/can_v3.md#new_charge_session) declaration in the CAN database should become as follows:

    <Message id="0x0106B001" length="8" name="New_Charge_Session" interval="100" format="extended">
