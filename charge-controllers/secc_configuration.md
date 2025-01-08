> [!UPDATE] {docsify-updated}

# SECC configuration

This document provides details about the config file sections and entries for ADVANTICS SECC **releases 4.x**.

> Version 4.x of the SW as well as update instructions are available here: [development branch](https://www.notion.so/EVSE-Migration-from-3-x-to-4-x-7526d289f055493db054452cbbfeb98f).

&nbsp;

**For customers using versions 3.x, please consult the actual config file, as it contains all the necessary information on each section.**

> **Note**
>
> Depending on the application the customer can add configuration entries relevant to the specific use case.


In Advantics controller the configuration file is accessible at this path: `/srv/config.cfg`. To edit the file, `nano` and `vi` editors are already installed on the system.

> **Note**
>
> - When modifying the `/srv/config.cfg` file, always remember that
> Advantics charge controllers works in *fake read-writable mode* by
> default. Ie. changes are only written in RAM, and not persisted to the
> actual read-only partition. See section [**Read-only file system**](charge-controllers/sys3_user/read-only.md) to
> learn how to temporarily or permanently switch to real writable mode.

> [!WARNING]
>  - Any line starting with the "#" sign will be treated as a commented line and will not be taken into account during execution.
> - Remove the “#” at the beginning of every parameter you modify.
> - Leave no white space at the beginning of the line.


## Applications

Here you can change the logging level of the applications running.

    [applications]
    log_level=INFO

## Hardware

In this section, you can configure the controller version as well as the
digital inputs and outputs.
> **Note**
>
> Digital inputs and outputs can be interfaced via the generic interface. check section [**Controller IOs on CAN**](charge-controllers/secc_can_ios.md#controllers-ios-on-can)

The following is an example:

    [hardware]
    # version possible values:
    #   mobile_charger_controller_v2018-1
    #   din_controller_v2020-1
    #   pev_controller_v2018-1
    version = din_controller_v2020-1

    # dig_inX possible values: CHAdeMO_Start, Stop, Monitor, Not_Connected
    dig_in1 = CHAdeMO_Start
    dig_in2 = Stop
    dig_in3 = Monitor
    dig_in4 = Not_Connected

## Pistols

In this section, you should enable the pistols to be used. In the following example only `CCS DC` pistol is enabled:

    [pistols]
    enabled =
        CCS DC
    #    CCS AC
    #    CHAdeMO

For each pistol enabled, you should configure the correspondent pistol
section to use the right charger configuration.
&nbsp;

**The following is an example for \[pistol:CCS DC\]**

`index`

Pistol index. Must be a non-zero positive integer unique with respect to
other pistols. Used to offset CAN addressing as well.

Example:

    index = 1

The CAN ID index field serves as an identifier for each pistol (charging connector) in the charger. It acts as an offset to the CAN IDs, allowing independent addressing of each pistol via the generic CAN bus interface as an individual charger.

Users must include the index value configured for each pistol in the CAN message identifier. The index field in the CAN identifier is represented by bits [28:24].

Please refer to [**CAN ID index field**](charge-controllers/secc_generic/databases.md#CAN_ID_index_field) for more information.

`charger_type`

This entry should indicate the type of charger interface to be used. It can be either a [**Generic Interface**](charge-controllers/secc_generic/overview.md#general-operation) or a specific [**Charger Interface**](charge-controllers/charger_interfaces.md)


Example 1:

    charger_type = Advantics_Generic_DC_v3

Check the following section for the Generic Interface V3 documentation:  [**Generic Interface V3**](charge-controllers/secc_generic/README_v3.md)

Example 2:

    charger_type = Advantics_ADS_PC_BPUD

The [**Advantics\_ADS\_PC\_BPUD**](charge-controllers/charger_interfaces.md#advantics-acdc-charger-interface) is a charger interface for an ADVANTICS charger composed of 3 Advantics power modules: Filter + AFE + LLC.

`stack_pos`

Entry for Advantics power module chargers only.

stack\_pos tells which modules are associated with this particular
pistol. Space or comma separated list of integers.  

Example:

In case the charger is composed of 2 sets of modules stacked in
parallel. The stack position numbers of each level should be specified :

    stack_pos = 0, 1

`min_voltage`


Minimum output voltage (V) supported by the charger in.

Example:

    min_voltage = 0

`max_voltage`


Maximum output voltage (V) supported by the charger.

Example:

    max_voltage = 500

`min_current`


Minimum output current (A) supported by the charger.

Example:

    min_current = 0

`max_current`


Maximum output current (A) supported by the charger.

Example:

    max_current = 60

`max_power`


Maximum output power (W) supported by the charger.

Example:

    max_power = 25000

`use_sequence_flags`

Tells if flags in Sequence\_Control message of the Generic CAN interface
should be used.

Example:

    use_sequence_flags = true

`evse_id`
Customize your EVSE ID with this entry.

Example:

    evse_id = 33A51A0001

`enable_din`

enabled by default.

Example:

    enable_din = true

`enable_iso_ed1`

enabled by default.

Example:

    enable_iso_ed1 = true

`free_service`

If the charging station is for free. If not, see with Advantics about
how to integrate a payment method.

Example:

    free_service = true

`energy_transfer_type`

Defines how the DC power is transmitted to the vehicle among:

-   **DC\_core**: DC charging according to IEC 62196 on the core pins.

-   **DC\_extended**: DC charging using the extended pins of an IEC
    62196-3 Configuration EE or Configuration FF connector.

Example:

    energy_transfer_type = DC_extended

`current_ripple`

Peak-to-peak magnitude of the current ripple (A) at the output of the
charger.

Example:

    current_ripple = 1

`skip_cable_check`

With this entry you can configure the charger to skip cable check.

Example:

    skip_cable_check = true

`protocol_priority_order`

Which priority order to use for choosing a protocol.

-   **standard**: Corresponds to the order specified in CCS standards.
    Ie. the vehicle gives its own priority. But we noticed car
    manufacturers still default to DIN even if they support ISO

-   **latest**: Protocols more recently published are favored. Eg. ISO
    would be preferred over DIN if vehicle does support it. Ignores
    vehicle priority ordering.

-   **oldest**: Protocols less recently published are favored. Eg. DIN
    would be preferred over ISO if vehicle does support it. Ignores
    vehicle priority ordering.

Example:

    protocol_priority_order = standard

`slac_app_version`

With this entry you can select the slack app version.

Example:

    slac_app_version = 2

`C_EV_match_MNBC`

Number of M-Sounds for the SLAC. Min 1, max 255.

Example:

    C_EV_match_MNBC = 10

`TT_EVSE_SLAC_init`

Timeout between detecting CP state B and receiving first valid
CM\_SLAC\_PARAM.REQ. In seconds, min 20, max 50.

Example:

    TT_EVSE_SLAC_init = 20

`Attn_bias`

Fixed bias value added to the average of each carrier group we send to
the vehicle.

Example:

    Attn_bias = 0

## OCPP Configuration

Advantics charge controllers can provide OCPP functionality. Please refer to the [**OCPP documentation**](charge-controllers/ocpp16j.md) for more details on the application.
&nbsp;

By default, OCPP is disabled. To enable it, you need to at least set the `enabled`
and `connection_url` in the `ocpp` section of the config file.

    [ocpp]
    enabled = true
    connection_url = ws://your-ocpp-endpoint.example.com/your/ocpp/path/charge-point-id                  

-   In `connection_url` replace `charge-point-id` with the id this
    charge point should identify as.

OCPP Options that are specified in the OCPP standard (e.g.
`AuthorizationCacheEnabled`) are grouped in config sections according to
the OCPP feature profile they belong to (e.g.
`AuthorizationCacheEnabled` is used as part of the core feature profile
and is thus configured in section `ocpp:1.6_core`). Names for OCPP
options are case-sensitive. Some examples include

    [ocpp:1.6_core]
    AuthorizationCacheEnabled = true
    ...

    [ocpp:1.6_local_auth]
    LocalAuthListEnabled = false
    ...
