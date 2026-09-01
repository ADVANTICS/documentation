# CHAdeMO pistol

These configuration entries are all under the `[pistol:CHAdeMO]` section.

!!! note "Names are what you write in the file"
    These are the option names exactly as the configuration file expects them. The Web UI
    displays them as capitalised labels ("Charger Type"); writing that label into the file
    does **not** work -- the option is ignored without an error and the default applies.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

### Bidirectional Charging Extra Parameters
- **`is_bidirectional`**: Whether this charger supports both charge and discharge (default: `false`)
{: #is_bidirectional }
- **`limit_non_bidir_to_positive_current`**: default `true` **advanced**
{: #limit_non_bidir_to_positive_current }
- **`supports_range_mode`**: Tells if charger can handle setpoints range mode, or if it is constrained to target mode only. NB.: Range mode is only supported since Generic DC v3 (and for specific charger interfaces using the Generic interface in parallel for external control). For charger interfaces not actually supporting range mode (eg. Generic DC v2), this option is forced to false (and you will see an harmless warning in evse-controller logs about it) (default: `true`)
{: #supports_range_mode }

### CAN BUS
- **`charger_can_if`**: default `can0` **advanced**
{: #charger_can_if }
- **`charger_can_timeout_ms`**: Timeout for reception of Power_Modules_Status message in generic interface (ms) (default: `500.0` ms) **advanced**
{: #charger_can_timeout_ms }
- **`charger_type`**: One of `Advantics_Generic_DC_v1`, `Advantics_Generic_DC_v2`, `Advantics_Generic_DC_v3`, `Advantics_ADS_PC_UPUD`, `Advantics_ADS_PC_BPUD`, `Advantics_ADS_PC_AC01_DC01`, `Advantics_ADM_PC_BP25_BoostBuck`, `PRE_Charger`, `Maxwell_MXR` (default: `Advantics_Generic_DC_v2`)
{: #charger_type }

### Cable Limits
- **`max_cable_current`**: Maximum current rated for the cable (default: `100.0` A)
{: #max_cable_current }
- **`max_cable_power`**: Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided (default: `0.0` W)
{: #max_cable_power }
- **`max_cable_voltage`**: Maximum voltage rated for the cable (default: `500.0` V)
{: #max_cable_voltage }

### Charge Limits

Charger and cable electrical limits. Should describe the actual limitations of these components. Ie.: - Charger and cable limits are combined (by lowest value) to provide a single set of limits to vehicle. - But they are actually taken into consideration separately when doing deratings when each get hot. - Power can be set to 0 to just use max voltage * max current. But you can set something different in order to define a power enveloppe. - When giving our combined max current to vehicle during charging, we also use the max power limits divided by actual present output voltage at that time. Defaults are sensible limits for a 50kW unidirectional station.

- **`max_charger_current`**: default `120.0` A
{: #max_charger_current }
- **`max_charger_power`**: default `0.0` W
{: #max_charger_power }
- **`max_charger_voltage`**: default `500.0` V
{: #max_charger_voltage }
- **`min_charger_current`**: default `0.0` A
{: #min_charger_current }
- **`min_charger_power`**: default `0.0` W
{: #min_charger_power }
- **`min_charger_voltage`**: default `0.0` V
{: #min_charger_voltage }

### Discharge Limits

Charger and cable electrical limits. Should describe the actual limitations of these components. Ie.: - Charger and cable limits are combined (by lowest value) to provide a single set of limits to vehicle. - But they are actually taken into consideration separately when doing deratings when each get hot. - Power can be set to 0 to just use max voltage * max current. But you can set something different in order to define a power enveloppe. - When giving our combined max current to vehicle during charging, we also use the max power limits divided by actual present output voltage at that time. Defaults are sensible limits for a 50kW unidirectional station.

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

### Insulation Monitor
- **`insulation_monitor_address`**: RS485 address ID of the insulation monitor. One of `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90`. Only when `insulation_monitor_type` = `BenderISOCHA425HV` (default: `3`)
{: #insulation_monitor_address }
- **`insulation_monitor_baudrate`**: Baudrate the RS485 serial com with the insulation monitor. One of `1200`, `2400`, `4800`, `9600`, `19200`, `38400`, `57600`, `115200`. Only when `insulation_monitor_type` = `BenderISOCHA425HV` (default: `9600` Bd)
{: #insulation_monitor_baudrate }
- **`insulation_monitor_parity`**: Parity of the RS485 serial com with the insulation monitor. One of `Odd`, `No_Parity`, `Even`. Only when `insulation_monitor_type` = `BenderISOCHA425HV` (default: `Even`)
{: #insulation_monitor_parity }
- **`insulation_monitor_stopbits`**: Number of stopbits of the RS485 serial com with the insulation monitor. The number of stopbits depends on the parity chosen. Check our documentation and the insulation monitor documentation to check the available combinations. One of `1`, `2`. Only when `insulation_monitor_type` = `BenderISOCHA425HV` (default: `1`)
{: #insulation_monitor_stopbits }
- **`insulation_monitor_type`**: Whether you are using one of our supported insulation monitors and which one. One of `BenderISOCHA425HV`, `Not_Used` (default: `Not_Used`)
{: #insulation_monitor_type }

### Specific Charger Interface Extra Parameters
- **`do_not_rearm_after_fault`**: Only for ADVANTICS power module (default: `false`) **advanced**
{: #do_not_rearm_after_fault }
- **`llc_use_external_voltage`**: Only for ADVANTICS power module (default: `0.0` V) **advanced**
{: #llc_use_external_voltage }
- **`stack_pos`**: Stack position to use when working in conjonction with ADVANTICS power module (default: `0`) **advanced**
{: #stack_pos }

### General
- **`always_use_dynamic_max_current`**: When enabled, the dynamic maximum current(s) received over the Generic CAN interface are always used as the current limit (still capped by the configured maximum current), instead of being ignored when reported as zero. Note: a reported dynamic maximum of 0 A will then limit the current to 0 A (default: `false`) **advanced**
{: #always_use_dynamic_max_current }
- **`current_ramp_down_rate`**: Rate of the current ramp at the end of the charge, A/s (default: `-20.0` A/s) **advanced**
{: #current_ramp_down_rate }
- **`current_ramp_up_rate`**: Rate of the current ramp at the beginning of the charge, A/s (default: `20.0` A/s) **advanced**
{: #current_ramp_up_rate }
- **`index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. One of `1` to `16` (default: `3`)
{: #index }
- **`precharge_resistance`**: default `true` **advanced**
{: #precharge_resistance }
- **`support_welding_detection`**: Whether the charger supports welding detection (default: `true`) **advanced**
{: #support_welding_detection }
- **`use_sequence_flags`**: Tells if flags in Sequence_Control message of the Generic CAN interface should be used (default: `true`)
{: #use_sequence_flags }
