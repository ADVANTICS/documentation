# CCS DC pistol

These configuration entries are all under the `[pistol:CCS DC]` section.

**The following is an example for \[pistol:CCS DC\]**

## index
Pistol index. Must be a non-zero positive integer unique with respect to
other pistols. Used to offset CAN addressing as well.

Example:

    index = 1

The CAN ID index field serves as an identifier for each pistol (charging connector) in the charger. It acts as an offset to the CAN IDs, allowing independent addressing of each pistol via the generic CAN bus interface as an individual charger.

Users must include the index value configured for each pistol in the CAN message identifier. The index field in the CAN identifier is represented by bits [28:24].

Please refer to [**CAN ID index field**](../charger-can-interfaces/databases_v2.md#can-id-index-field) for more information.

## charger_type
This entry should indicate the type of charger interface to be used. It can be either a [**Generic Interface**](../charger-can-interfaces/overview.md#general-operation) or a specific [**Charger Interface**](../charger-features/charger_interfaces.md)


Example 1:

    charger_type = Advantics_Generic_DC_v3

Check the following section for the Generic Interface V3 documentation:  [**Generic Interface V3**](../charger-can-interfaces/README_v3.md)

Example 2:

    charger_type = Advantics_ADS_PC_BPUD

The [**Advantics\_ADS\_PC\_BPUD**](../charger-features/charger_interfaces.md#advantics-acdc-charger-interface) is a charger interface for an ADVANTICS charger composed of 3 Advantics power modules: Filter + AFE + LLC.

## stack_pos
Entry for Advantics power module chargers only.

stack\_pos tells which modules are associated with this particular
pistol. Space or comma separated list of integers.  

Example:

In case the charger is composed of 2 sets of modules stacked in
parallel. The stack position numbers of each level should be specified :

    stack_pos = 0, 1

## min_charger_voltage
Minimum output voltage (V) supported by the charger in.

Example:

    min_charger_voltage = 0

## max_charger_voltage
Maximum output voltage (V) supported by the charger.

Example:

    max_charger_voltage = 500

## min_charger_current
Minimum output current (A) supported by the charger.

Example:

    min_charger_current = 0

## max_charger_current
Maximum output current (A) supported by the charger.

Example:

    max_charger_current = 60

## max_charger_power
Maximum output power (W) supported by the charger.

Example:

    max_charger_power = 25000

## use_sequence_flags
Tells if flags in Sequence\_Control message of the Generic CAN interface
should be used.

Example:

    use_sequence_flags = true

## evse_id
Customize your EVSE ID with this entry.

Example:

    evse_id = 33A51A0001

## enable_din
enabled by default.

Example:

    enable_din = true

## enable_iso_part2
enabled by default.

Example:

    enable_iso_part2 = true

## free_service
If the charging station is for free. If not, see with Advantics about
how to integrate a payment method.

Example:

    free_service = true

## energy_transfer_type
Defines how the DC power is transmitted to the vehicle among:

-   **DC\_core**: DC charging according to IEC 62196 on the core pins.

-   **DC\_extended**: DC charging using the extended pins of an IEC
    62196-3 Configuration EE or Configuration FF connector.

Example:

    energy_transfer_type = DC_extended

## current_ripple
Peak-to-peak magnitude of the current ripple (A) at the output of the
charger.

Example:

    current_ripple = 1

## skip_cable_check
With this entry you can configure the charger to skip cable check.

Example:

    skip_cable_check = true

## protocol_priority_order
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

## slac_app_version
With this entry you can select the slack app version.

Example:

    slac_app_version = 2

## C_EV_match_MNBC
Number of M-Sounds for the SLAC. Min 1, max 255.

Example:

    C_EV_match_MNBC = 10

## TT_EVSE_SLAC_init
Timeout between detecting CP state B and receiving first valid
CM\_SLAC\_PARAM.REQ. In seconds, min 20, max 50.

Example:

    TT_EVSE_SLAC_init = 20

## Attn_bias
Fixed bias value added to the average of each carrier group we send to
the vehicle.

Example:

    Attn_bias = 0

## insulation_monitor_type
Whether you are using one of our supported insulation monitors and which one

Available:

- **BenderISOCHA425HV**: Bender isoCHA425HV
- **Not_Used**: No insulation monitor

Example:

    insulation_monitor_type = BenderISOCHA425HV

or

    insulation_monitor_type = Not_Used

## insulation_monitor_stopbits
Number of stop bits for the RS485 serial communication with the insulation monitor. The required number of stop bits depends on the selected parity. Check  our documentation  and the insulation monitor’s documentation for valid combinations.

Available:

- **1**
- **2**

Example:

```
insulation_monitor_stopbits = 1
```

---

## insulation_monitor_parity
Parity setting for the RS485 serial communication with the insulation monitor.

Available:

- **N**: None
- **E**: Even
- **O**: Odd

Example:

```
insulation_monitor_parity = E
```

---

## insulation_monitor_baudrate
Baud rate for the RS485 serial communication with the insulation monitor.

Available:

- Bender isoCHA425HV allowed baudrates

Example:

```
insulation_monitor_baudrate = 9600
```

---

## insulation_monitor_address
RS485 address ID of the insulation monitor.

- Bender isoCHA425HV allowed addresses

Example:

```
insulation_monitor_address = 3
```

## Other entries

The entries above are the ones an integration normally sets. The remainder of
`[pistol:CCS DC]` is listed here, generated from the controller software so that the names,
defaults and units cannot drift from it.

!!! note "How the charger and cable limits combine"
    The charger limits and the cable limits describe two different physical things, and both
    are declared here. The controller combines them by taking the lowest value and advertises
    that single set to the vehicle -- but it keeps them apart when derating, because the
    charger and the cable heat up independently. A power limit of `0` means "no power
    envelope": the controller then uses max voltage x max current. Setting one lets you
    describe a genuine power envelope instead, and during charging the combined maximum
    current is also derived from the power limit divided by the present output voltage.

    The defaults are sensible limits for a 50 kW unidirectional station.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

### Bidirectional Charging Extra Parameters
- **`is_bidirectional`**: Whether this charger supports both charge and discharge (default: `false`)
{: #is_bidirectional }
- **`limit_non_bidir_to_positive_current`**: default `true` **advanced**
{: #limit_non_bidir_to_positive_current }
- **`supports_range_mode`**: Tells if charger can handle setpoints range mode, or if it is constrained to target mode only. NB.: Range mode is only supported since Generic DC v3 (and for specific charger interfaces using the Generic interface in parallel for external control). For charger interfaces not actually supporting range mode (eg. Generic DC v2), this option is forced to false (and you will see an harmless warning in evse-controller logs about it) (default: `true`) **advanced**
{: #supports_range_mode }

### CAN BUS
- **`charger_can_if`**: default `can0` **advanced**
{: #charger_can_if }
- **`charger_can_timeout_ms`**: Timeout for reception of Power_Modules_Status message in generic interface (ms) (default: `500.0` ms) **advanced**
{: #charger_can_timeout_ms }

### CCS Params
- **`allow_no_tls_for_iso_part20`**: Whether we should accept communications without TLS on -20This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild (default: `false`) **advanced**
{: #allow_no_tls_for_iso_part20 }
- **`din_iso_part2_cpd_force_evse_ready_on_processing_finished`**: Whether to force EVSE_Ready status in DC_EVSEStatus when charge parameter discovery processing EVSEProcessing is Finished in DIN SPEC 70121 and ISO 15118-2 (default: `false`) **advanced**
{: #din_iso_part2_cpd_force_evse_ready_on_processing_finished }
- **`enable_iso_part20`**: Whether ISO15118-20 communications are allowed (default: `false`)
{: #enable_iso_part20 }

### Cable Limits
- **`max_cable_current`**: Maximum current rated for the cable (default: `100.0` A)
{: #max_cable_current }
- **`max_cable_power`**: Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided (default: `0.0` W)
{: #max_cable_power }
- **`max_cable_voltage`**: Maximum voltage rated for the cable (default: `500.0` V)
{: #max_cable_voltage }

### Charge Limits
- **`min_charger_power`**: Minimum power the charger can deliver (default: `0.0` W)
{: #min_charger_power }

### Discharge Limits
- **`max_charger_discharge_current`**: default `0.0` A
{: #max_charger_discharge_current }
- **`max_charger_discharge_power`**: default `0.0` W
{: #max_charger_discharge_power }
- **`max_charger_discharge_voltage`**: default `0.0` V
{: #max_charger_discharge_voltage }
- **`min_charger_discharge_current`**: default `0.0` A
{: #min_charger_discharge_current }
- **`min_charger_discharge_power`**: default `0.0` W
{: #min_charger_discharge_power }
- **`min_charger_discharge_voltage`**: default `0.0` V
{: #min_charger_discharge_voltage }

### Specific Charger Interface Extra Parameters
- **`do_not_rearm_after_fault`**: Only for ADVANTICS power module (default: `false`) **advanced**
{: #do_not_rearm_after_fault }
- **`llc_use_external_voltage`**: Only for ADVANTICS power module (default: `0.0` V) **advanced**
{: #llc_use_external_voltage }

### General
- **`always_use_dynamic_max_current`**: When enabled, the dynamic maximum current(s) received over the Generic CAN interface are always used as the current limit (still capped by the configured maximum current), instead of being ignored when reported as zero. Note: a reported dynamic maximum of 0 A will then limit the current to 0 A (default: `false`) **advanced**
{: #always_use_dynamic_max_current }
- **`current_ramp_down_rate`**: Rate of the current ramp at the end of the charge, A/s (default: `-20.0` A/s) **advanced**
{: #current_ramp_down_rate }
- **`current_ramp_up_rate`**: Rate of the current ramp at the beginning of the charge, A/s (default: `20.0` A/s) **advanced**
{: #current_ramp_up_rate }
- **`evse_id_for_iso_part2`**: Identifier of the EVSE in a ISO15118-2 session (default: *(empty)*) **advanced**
{: #evse_id_for_iso_part2 }
- **`log_signature_details`**: default `false` **advanced**
{: #log_signature_details }
- **`skip_voltage_lowering_after_insulation_test`**: Once the insulation test is done, do not ask the charger to lower its output voltage below 20 V before proceeding. Insulation_Test_Done is set to True immediately and the charger is left in its previous state (default: `false`) **advanced**
{: #skip_voltage_lowering_after_insulation_test }
