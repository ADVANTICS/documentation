# Pistols

In this section, you should enable the pistols to be used. In the following example only `CCS DC` pistol is enabled:

    [pistols]
    enabled =
        CCS DC
    #    CCS AC
    #    CHAdeMO

- **`enabled`**: The list of pistols this controller drives. One name per line, indented. `CCS DC`, `CCS AC`, `CHAdeMO` or `MCS`, depending on the hardware (default: the pistol the controller ships configured for)
{: #enabled }

For each pistol enabled, you should configure the correspondent pistol
section to use the right charger configuration.

!!! note "How many pistols at once"
    A multi-pistol charge controller can have several enabled simultaneously, one per physical
    connector. A single-pistol controller accepts exactly one — enabling a second is a
    configuration error.

Each enabled pistol is then configured in its own section:

| Pistol | Section | Page |
|---|---|---|
| MCS    | `[pistol:MCS]` | [MCS pistol](pistol-mcs.md) |
| CCS DC | `[pistol:CCS DC]` | [CCS DC pistol](pistol-ccs-dc.md) |
| CCS AC | `[pistol:CCS AC]` | [CCS AC pistol](pistol-ccs-ac.md) |
| CHAdeMO | `[pistol:CHAdeMO]` | [CHAdeMO pistol](pistol-chademo.md) |
