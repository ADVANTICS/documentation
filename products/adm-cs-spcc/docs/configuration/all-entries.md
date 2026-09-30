# Complete configuration reference

Every configuration entry of the ADM-CS-SPCC that you can set, generated from the
controller software itself so that it cannot fall behind. Use it to check a name, a default
or an allowed value; the other pages in this section explain what the entries are *for*.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode. Anything
not listed here is internal and not meant to be changed. The same goes for values: only
the ones supported for your use are given under *Allowed*.

!!! warning "A misspelled entry is silently ignored"
    The configuration is loaded non-strictly: an option the controller does not recognise is
    skipped without any error or log line, and the built-in default applies instead. Check the
    spelling and the section before anything else if a setting appears to have no effect.

!!! note "Sub-sections are separated by a colon"
    A heading like `[tls:client]` means a sub-section of `[tls]`, written exactly that way in
    the file.

## `[applications]`

### Logging

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `log_level` | str | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | Verbosity of the application logging |

### Storage

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `persistent_data` **advanced** | str | `/var/advantics/` | — | Folder that survives reboots and software updates. Applications keep their own data there, for instance a CAN database override. |

## `[hardware]`

### Inputs

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dig_in1` | str | `Not_Connected` | `Not_Connected`, `CHAdeMO_Start`, `Stop`, `CCS_DC_Stop`, `CCS_AC_Stop`, `CHAdeMO_Stop`, `Monitor` | Defines the function controlled by digital input 1. |
| `dig_in2` | str | `Not_Connected` | `Not_Connected`, `CHAdeMO_Start`, `Stop`, `CCS_DC_Stop`, `CCS_AC_Stop`, `CHAdeMO_Stop`, `Monitor` | Defines the function controlled by digital input 2. |
| `dig_in3` | str | `Not_Connected` | `Not_Connected`, `CHAdeMO_Start`, `Stop`, `CCS_DC_Stop`, `CCS_AC_Stop`, `CHAdeMO_Stop`, `Monitor` | Defines the function controlled by digital input 3. |
| `dig_in4` | str | `Not_Connected` | `Not_Connected`, `CHAdeMO_Start`, `Stop`, `CCS_DC_Stop`, `CCS_AC_Stop`, `CHAdeMO_Stop`, `Monitor` | Defines the function controlled by digital input 4. |

### Leds

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `led1` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled` | Defines the control of LED 1. |
| `led2` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled` | Defines the control of LED 2. |
| `led3` | str | `Not_Connected` | — | Defines the control of LED 3. |

### Outputs

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dig_out1` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled`, `Contactor_Enable` | Defines the function controlled by digital output 1. |
| `dig_out2` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled`, `Contactor_Enable` | Defines the function controlled by digital output 2. |
| `dig_out3` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled`, `Contactor_Enable` | Defines the function controlled by digital output 3. |
| `dig_out4` | str | `Not_Connected` | `Not_Connected`, `CAN_Controlled`, `Contactor_Enable` | Defines the function controlled by digital output 4. |

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `temperature_filter_window` **advanced** | int | `5` | — | Size of the median filter window for temperature readings |

## `[ocpp]`

### Behavior

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ignore_sequence_flags_for_ocpp_availability` | bool | `false` | — | Keep reporting the connector as available to the central system when the charger is only waiting for authorization. Stops maps and apps showing the charge point as out of service. *(Only when `enabled` = `true`.)* |
| `inoperative_pistols` | list | *(empty)* | — | Persistent data about inoperative pistols. *(Only when `enabled` = `true`.)* |
| `resend_ev_needs_on_limits_changed` | bool | `true` | — | (OCPP 2.0.1 only). Whether NotifyEVNeeds should be resent when EV updates its limits in the middle of a transaction. NotifyEVNeeds is always sent at the beginning of a transaction for dynamic charging, and can be re-triggered while being in the transaction if the limits change depending on this parameter. This is required by the standard and should be the default. However, when managing schedule on the CSMS side (i.e. CSMS sends a new schedule on each new setpoint), if the EV incorporates the charger side limit in its own reported limit, you can get an infinite feedback loop where the CSMS keeps re-adjusting its own setpoints. In that case, you might consider using this. *(Only when `enabled` = `true`.)* |

### Connection

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `connection_retry_delay` | float | `60.0` | — | How long to wait before trying to reconnect to the central system, in seconds. *(Only when `enabled` = `true`.)* |
| `connection_timeout` | float (s) | `30.0` | — | Timeout for websocket, do not confuse with ConnectionTimeout. *(Only when `enabled` = `true`.)* |
| `connection_url` | str | *(empty)* | — | Endpoint URL of the OCPP server *(Only when `enabled` = `true`.)* |
| `enabled` | bool | `false` | — | Enables support for OCPP on this controller |
| `ping_timeout` | float (s) | `20.0` | — | How long to wait for the answer to a WebSocket ping before treating the connection as lost. *(Only when `enabled` = `true`.)* |
| `protocol_order` | list | `['1.6']` | `1.6`, `2.0.1` | List of targeted OCPP versions in preference order. Used as the `subprotocols` in the websockets communications. The central server should respect the order, if supported, according to RFC 6455. Examples: Using [2.0.1, 1.6] will ask to use preferrably 2.0.1 but accept to downgrade to 1.6. Using [1.6] will refuse to use 2.0.1 even if the central server supports it. *(Only when `enabled` = `true`.)* |
| `server_uses_self_signed_certificate` | bool | `false` | — | Whether we should accept self-signed certificates for TLS. Self-signed certificates are useful for testing, however, using this in production might create a security risk. *(Only when `enabled` = `true`.)* |

### Internal Endpoints

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `management_dealer_endpoint` **advanced** | str | `tcp://*:60501` | — | Dealer endpoint for the management RPC |
| `management_router_endpoint` **advanced** | str | `tcp://*:60500` | — | Router endpoint for the management RPC |

### Test and Debug

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enable_test_rpc` | bool | `false` | — | Enables a tiny OCPP RPC simulator that can be used from the web interface. WARNING: do not enable this if you have your own RPC, as they would likely collide. |

## `[ocpp:1.6_core]`

### Authorization

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `AuthorizationCacheEnabled` | bool | `true` | — | Remember accepted ID tags locally so a repeat user can be authorized without asking the central system. |
| `AuthorizeRemoteTxRequests` | bool | `false` | — | Ask the central system to authorize a charge it started itself, instead of starting it straight away. |
| `StopTransactionOnInvalidId` | bool | `true` | — | Stop the charge as soon as the central system rejects the ID tag, instead of only refusing to start. |

### Boot Notification

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `BootNotificationOverwriteChargePointFirmwareVersion` **advanced** | str | *(empty)* | — | Replace the firmware version sent to the central system at boot. Leave empty to send the real one. |
| `BootNotificationOverwriteChargePointModel` **advanced** | str | *(empty)* | — | Replace the model name sent to the central system at boot. Leave empty to send the real one. |
| `BootNotificationOverwriteChargePointSerialNumber` **advanced** | str | *(empty)* | — | Replace the serial number sent to the central system at boot. Leave empty to send the real one. |
| `BootNotificationOverwriteChargePointVendor` **advanced** | str | *(empty)* | — | Replace the vendor name sent to the central system at boot. Leave empty to send the real one. |

### Charge Point Capabilities

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ConnectorPhaseRotation` | str | `0.Unknown,1.NotApplicable,2.Unknown,3.NotApplicable` | — | Wiring order of the three AC phases per connector, reported to the central system. |
| `GetConfigurationMaxKeys` | int | `1000` | — | Most configuration keys the central system may ask for in one GetConfiguration request. |
| `NumberOfConnectors` | int | `3` | — | Number of connectors this charge point reports to the central system. |
| `ResetRetries` | int | `0` | — | How many times to retry a reset command that failed. |
| `SupportedFeatureProfiles` **advanced** | str | `Core,LocalAuthListManagement,Reservation` | — | OCPP feature profiles this charge point reports as supported. |

### Connection

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `HeartbeatInterval` **advanced** | int (ms) | `86400` | — | How long the charger may stay silent before it sends a heartbeat. |
| `MessageTimeout` **advanced** | float (s) | `30.0` | — | How long to wait for the central system to answer a message before treating it as failed. |
| `WebSocketPingInterval` **advanced** | float (s) | `20.0` | — | How often a WebSocket ping is sent to keep the connection to the central system alive. |

### Meter Values

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ClockAlignedDataInterval` | float (ms) | `900.0` | — | How often clock-aligned meter values are sent. Set to 0 to turn them off. |
| `MeterValueSampleInterval` | float | `300.0` | — | How often meter values are sampled during a transaction, in seconds. Set to 0 to turn them off. |
| `MeterValuesAlignedData` | str | `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC` | — | Measurands included in clock-aligned meter values. |
| `MeterValuesSampledData` | str | `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC` | — | Measurands included in meter values sampled during a transaction. |

### Transactions

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ConnectionTimeOut` | float (ms) | `300.0` | — | How long the charger waits for the user to plug in after authorising, before cancelling. |
| `StopTransactionOnEVSideDisconnect` | bool | `true` | — | Stop the transaction when the cable is unplugged at the vehicle end. |
| `TransactionMessageAttempts` **advanced** | int | `3` | — | How many times a transaction message is retried when the central system does not answer. |
| `TransactionMessageRetryInterval` **advanced** | float (s) | `10.0` | — | How long to wait between retries of a transaction message. |
| `UnlockConnectorOnEVSideDisconnect` | bool | `false` | — | Unlock the connector when the cable is unplugged at the vehicle end. |

## `[ocpp:1.6_local_auth]`

### Local Authorization List

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `LocalAuthListEnabled` | bool | `false` | — | Use the local authorization list, so known users can be authorized without the central system. |
| `LocalAuthListMaxLength` | int | `1000` | — | Most entries the local authorization list can hold. |
| `SendLocalListMaxLength` | int | `1000` | — | Most entries the central system may send in one SendLocalList request. |

## `[ocpp:1.6_reservation]`

### Reservation

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ReserveConnectorZeroSupported` | bool | `false` | — | Allow the central system to reserve the whole charge point rather than one connector. |

## `[ocpp:1.6_smart_charging]`

### Charging Profiles

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ChargeProfileMaxStackLevel` | int | `100` | — | Highest stack level a charging profile may use. Higher levels override lower ones. |
| `ChargingScheduleAllowedChargingRateUnit` | str | `Current,Power` | — | Units a charging schedule may be expressed in: current in amps, power in watts, or both. |
| `ChargingScheduleMaxPeriods` | float | `1000.0` | — | Most periods a single charging schedule may contain. |
| `ConnectorSwitch3to1PhaseSupported` | bool | `false` | — | The charger can switch a connector between three-phase and single-phase AC. |
| `MaxChargingProfilesInstalled` | int | `1000` | — | Most charging profiles that can be stored at once. |

### Current Limiting

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `TargetCurrent` | float (A) | `0.0` | — | Target current set by the central system for a running transaction. Not part of OCPP 1.6: sent through ChangeConfiguration together with the transaction ID. |
| `allow_limiting_to_zero` | bool | `false` | — | Let a smart charging limit go all the way down to 0 A. Off by default, because 0 A can abort the session. |
| `update_interval` | float (s) | `30.0` | — | How often the smart charging limit is recomputed and applied during a session. |

## `[ocpp:tls]`

### TLS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `check_hostname` | bool | `false` | — | Whether the charge point should check hostname of the CA file. Should only be disabled for local testing. |

## `[pistol:CCS AC]`

### CAN BUS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `charger_can_if` **advanced** | str | `can0` | — | CAN interface the power stage of this connector is wired to. |
| `charger_can_timeout_ms` **advanced** | float (ms) | `500.0` | — | Timeout for reception of Power_Modules_Status message in generic interface (ms). |
| `charger_type` | str | `Advantics_Generic_AC_v2` | `Advantics_Generic_AC_v2` | The type of CAN interfacer to communicate with your charger. |

### Diagnostics

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `clear_error_codes_on_idle` **advanced** | bool | `false` | — | Clear the error codes when the pistol goes back to idle, instead of keeping them until the next plug-in. |

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `index` | int | `2` | `1` to `16` | Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. |
| `use_sequence_flags` | bool | `true` | — | Tells if flags in Sequence_Control message of the Generic CAN interface should be used. |

### Lock Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `lock_feedback_low_is_locked` | bool | `true` | — | There are various lock feedback mechanisms existing. The one provided as default here correspond to a simple Normally Open switch that will short to ground (ie. R~=0) when locked. For a 1K/11K lock feedback, you would have to change the R threshold (eg. 5000) as well as inverse the polarity option by setting it to false. |
| `lock_feedback_r_threshold` | float | `100.0` | — | Threshold, in ohms, between locked and unlocked state. |
| `lock_pulse_ms` | float (ms) | `600.0` | — | Time in milliseconds of the locking or unlocking pulses. |
| `no_cable_lock` | bool | `true` | — | In case cable is detachable from charger side, or for R&D usage. |

### Phases, charger limits and cable limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_cable_phase_current` | float (A) | `32.0` | — | AC cable limits, per phase Max current rated for the cable, in A. |
| `max_cable_phase_power` | float (W) | `0.0` | — | AC cable limits, per phase Max current rated for the cable, in A. Can be ommitted if a current limit is set. |
| `max_cable_phase_voltage` | float (V) | `250.0` | — | AC cable limits, per phase Max voltage rated for the cable, in V. |
| `max_charger_phase_current` | float (A) | `32.0` | — | The current threshold at which request the charger to cap,for every phase. |
| `number_of_phases` **advanced** | int | `3` | — | Only used in OCPP GetCompositeSchedule |

### Proximity Pilot

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ignore_pp` **advanced** | bool | `true` | — | Ignore the values from Proximity Pilot |
| `is_cable_detachable` | bool | `false` | — | The AC cable can be unplugged from the charger. Connects the Proximity Pilot pull-up so the charger can read the cable's current rating. |

#### Notes on some `[pistol:CCS AC]` entries

**`clear_error_codes_on_idle`**

By default a code outlives the session that raised it: it stays raised through the return to idle and is cleared when the next plug-in starts a new session. Codes read while the controller is idle are then the post-mortem of the session that just ended.
Turn this on to clear them on the way back to idle instead, so codes are only ever visible while a vehicle is connected. The trade-off is that nobody who arrives after the vehicle is unplugged can still see why the last session failed.

## `[pistol:CCS DC]`

### Bidirectional Charging Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `is_bidirectional` | bool | `false` | — | Whether this charger supports both charge and discharge |
| `limit_non_bidir_to_positive_current` **advanced** | bool | `true` | — | Never report a negative present current to a vehicle that does not support bidirectional charging. Some vehicles refuse to charge otherwise. |
| `supports_range_mode` **advanced** | bool | `true` | — | — |

### CAN BUS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `charger_can_if` **advanced** | str | `can0` | — | CAN interface the power stage of this connector is wired to. |
| `charger_can_timeout_ms` **advanced** | float (ms) | `500.0` | — | Timeout for reception of Power_Modules_Status message in generic interface (ms). |
| `charger_type` | str | `Advantics_Generic_DC_v2` | `Advantics_Generic_DC_v1`, `Advantics_Generic_DC_v2`, `Advantics_Generic_DC_v3`, `Advantics_ADS_PC_UPUD`, `Advantics_ADS_PC_BPUD`, `Advantics_ADM_PC_BP25_BoostBuck`, `PRE_Charger`, `Maxwell_MXR` | Power stage this connector talks to. Picks the CAN protocol used between the controller and the charger. |

### CCS Params

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `V2G_SECC_CommunicationSetup_Performance_Time` **advanced** | float (s) | `60.0` | `0` to `300` | Time the vehicle is given, from the data link coming up, to complete session setup. The standard mandates 18 s, we are a bit more flexible. 0 disables the timeout. |
| `allow_no_tls_for_iso_part20` **advanced** | bool | `false` | — | Whether we should accept communications without TLS on -20This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild. |
| `current_ripple` **advanced** | float | `1.0` | — | Peak-to-peak ripple of the output current, in amps. Reported to the vehicle so it can decide how much ripple to accept. |
| `din_iso_part2_cpd_force_evse_ready_on_processing_finished` **advanced** | bool | `false` | — | Whether to force EVSE_Ready status in DC_EVSEStatus when charge parameter discovery processing EVSEProcessing is Finished in DIN SPEC 70121 and ISO 15118-2. |
| `enable_din` | bool | `true` | — | Whether DIN70121 communications are allowed. |
| `enable_iso_part2` | bool | `true` | — | Whether ISO15118-2 communications are allowed. |
| `enable_iso_part20` | bool | `false` | — | Whether ISO15118-20 communications are allowed. |
| `evse_id` **advanced** | str | `33A51A0001` | — | Identifier of the EVSE as used by OCCP communications. |
| `evse_id_for_iso_part2` **advanced** | str | *(empty)* | — | Identifier of the EVSE in a ISO15118-2 session. |
| `free_service` **advanced** | bool | `true` | — | Tell the vehicle that charging on this connector is free of charge. |
| `log_signature_details` **advanced** | bool | `false` | — | Write the details of every signature check to the log. Only useful when debugging Plug and Charge. |

### Cable Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_cable_current` | float (A) | `100.0` | `0` to `inf` | Maximum current rated for the cable. |
| `max_cable_power` | float (W) | `0.0` | `0` to `inf` | Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided |
| `max_cable_voltage` | float (V) | `500.0` | `0` to `inf` | Maximum voltage rated for the cable. |

### Charge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `current_ramp_down_rate` **advanced** | float (A/s) | `-20.0` | — | Rate of the current ramp at the end of the charge, A/s. |
| `current_ramp_enabled` **advanced** | bool | `true` | — | Apply the current ramp rates. Turn off to hand the power modules the current the vehicle asked for, unchanged. |
| `current_ramp_up_rate` **advanced** | float (A/s) | `20.0` | — | Rate of the current ramp at the beginning of the charge, A/s. |
| `max_charger_current` | float (A) | `120.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current above that value. |
| `max_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power above that value. |
| `max_charger_voltage` | float (V) | `500.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages above that value. |
| `min_charger_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current below that value. |
| `min_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power below that value. |
| `min_charger_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages below that value. |

### Diagnostics

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `clear_error_codes_on_idle` **advanced** | bool | `false` | — | Clear the error codes when the pistol goes back to idle, instead of keeping them until the next plug-in. |

### Discharge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current above that value. |
| `max_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power above that value. |
| `max_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages above that value. |
| `min_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current below that value. |
| `min_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power below that value. |
| `min_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages below that value. |

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `always_use_dynamic_max_current` **advanced** | bool | `false` | — | — |
| `index` | int | `1` | `1` to `16` | Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. |
| `use_sequence_flags` | bool | `true` | — | Tells if flags in Sequence_Control message of the Generic CAN interface should be used https://documentation.advantics.fr/adm-cs-secc/charger-can-interfaces/can_v3.html#Sequence_Control |

### Insulation Monitor

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `insulation_monitor_address` | int | `3` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90` | RS485 address ID of the insulation monitor *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_baudrate` | int (Bd) | `9600` | `1200`, `2400`, `4800`, `9600`, `19200`, `38400`, `57600`, `115200` | Baudrate the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_parity` | str | `Even` | `Odd`, `No_Parity`, `Even` | Parity of the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_stopbits` | int | `1` | `1`, `2` | Number of stopbits of the RS485 serial com with the insulation monitor. The number of stopbits depends on the parity chosen. Check our documentation and the insulation monitor documentation to check the available combinations *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_type` | str | `Not_Used` | `BenderISOCHA425HV`, `Not_Used` | Whether you are using one of our supported insulation monitors and which one |

### Specific Charger Interface Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dc_link_voltage` **advanced** | float (V) | `920.0` | — | Only for ADVANTICS AC01+DC01 power module: DC-link voltage the AC01 holds. Must stay above the maximum vehicle voltage; values below the charger minimum are clamped up. |
| `do_not_rearm_after_fault` **advanced** | bool | `false` | — | Only for ADVANTICS power module. |
| `force_charger_range_target_current` **advanced** | bool | `false` | — | Test only: drive the interface Range_Target_Current clamped by the charger current range only, ignoring the vehicle-requested/negotiated current. Only for ADVANTICS power module. |
| `llc_use_external_voltage` **advanced** | float (V) | `0.0` | — | Only for ADVANTICS power module |
| `stack_pos` **advanced** | str | `0` | — | Stack position to use when working in conjonction with ADVANTICS power module. |

### Test and Debug

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `skip_cable_check` **advanced** | bool | `false` | — | Should not be used in production. For R&D, allows skipping the cable check step in the charging sequence. |
| `skip_voltage_lowering_after_insulation_test` **advanced** | bool | `false` | — | Once the insulation test is done, do not ask the charger to lower its output voltage below 20 V before proceeding. Insulation_Test_Done is set to True immediately and the charger is left in its previous state. |

#### Notes on some `[pistol:CCS DC]` entries

**`always_use_dynamic_max_current`**

When enabled, the dynamic maximum current(s) received over the Generic CAN interface are always used as the current limit (still capped by the configured maximum current), instead of being ignored when reported as zero. Note: a reported dynamic maximum of 0 A will then limit the current to 0 A.

**`clear_error_codes_on_idle`**

By default a code outlives the session that raised it: it stays raised through the return to idle and is cleared when the next plug-in starts a new session. Codes read while the controller is idle are then the post-mortem of the session that just ended.
Turn this on to clear them on the way back to idle instead, so codes are only ever visible while a vehicle is connected. The trade-off is that nobody who arrives after the vehicle is unplugged can still see why the last session failed.

**`max_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`supports_range_mode`**

Tells if charger can handle setpoints range mode, or if it is constrained to target mode only. NB.: Range mode is only supported since Generic DC v3 (and for specific charger interfaces using the Generic interface in parallel for external control). For charger interfaces not actually supporting range mode (eg. Generic DC v2), this option is forced to false (and you will see an harmless warning in evse-controller logs about it).

## `[pistol:CHAdeMO]`

### Bidirectional Charging Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `is_bidirectional` | bool | `false` | — | Whether this charger supports both charge and discharge |
| `limit_non_bidir_to_positive_current` **advanced** | bool | `true` | — | Never report a negative present current to a vehicle that does not support bidirectional charging. Some vehicles refuse to charge otherwise. |
| `supports_range_mode` | bool | `true` | — | — |

### CAN BUS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `charger_can_if` **advanced** | str | `can0` | — | CAN interface the power stage of this connector is wired to. |
| `charger_can_timeout_ms` **advanced** | float (ms) | `500.0` | — | Timeout for reception of Power_Modules_Status message in generic interface (ms) |
| `charger_type` | str | `Advantics_Generic_DC_v2` | `Advantics_Generic_DC_v1`, `Advantics_Generic_DC_v2`, `Advantics_Generic_DC_v3`, `Advantics_ADS_PC_UPUD`, `Advantics_ADS_PC_BPUD`, `Advantics_ADM_PC_BP25_BoostBuck`, `PRE_Charger`, `Maxwell_MXR` | Power stage this connector talks to. Picks the CAN protocol used between the controller and the charger. |

### CHAdeMO Params

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `precharge_resistance` **advanced** | bool | `true` | — | — |
| `support_welding_detection` **advanced** | bool | `true` | — | Whether the charger supports welding detection |

### Cable Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_cable_current` | float (A) | `100.0` | `0` to `inf` | Maximum current rated for the cable |
| `max_cable_power` | float (W) | `0.0` | `0` to `inf` | Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided |
| `max_cable_voltage` | float (V) | `500.0` | `0` to `inf` | Maximum voltage rated for the cable |

### Charge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `current_ramp_down_rate` **advanced** | float (A/s) | `-20.0` | — | Rate of the current ramp at the end of the charge, A/s |
| `current_ramp_enabled` **advanced** | bool | `true` | — | Apply the current ramp rates. Turn off to hand the power modules the current the vehicle asked for, unchanged. |
| `current_ramp_up_rate` **advanced** | float (A/s) | `20.0` | — | Rate of the current ramp at the beginning of the charge, A/s |
| `max_charger_current` | float (A) | `120.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current above that value |
| `max_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power above that value |
| `max_charger_voltage` | float (V) | `500.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages above that value |
| `min_charger_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current below that value |
| `min_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power below that value |
| `min_charger_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages below that value |

### Diagnostics

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `clear_error_codes_on_idle` **advanced** | bool | `false` | — | Clear the error codes when the pistol goes back to idle, instead of keeping them until the next plug-in. |

### Discharge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current above that value |
| `max_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power above that value |
| `max_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages above that value |
| `min_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current below that value |
| `min_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power below that value |
| `min_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages below that value |

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `always_use_dynamic_max_current` **advanced** | bool | `false` | — | — |
| `index` | int | `3` | `1` to `16` | Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. |
| `use_sequence_flags` | bool | `true` | — | Tells if flags in Sequence_Control message of the Generic CAN interface should be used |

### Insulation Monitor

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `insulation_monitor_address` | int | `3` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90` | RS485 address ID of the insulation monitor *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_baudrate` | int (Bd) | `9600` | `1200`, `2400`, `4800`, `9600`, `19200`, `38400`, `57600`, `115200` | Baudrate the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_parity` | str | `Even` | `Odd`, `No_Parity`, `Even` | Parity of the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_stopbits` | int | `1` | `1`, `2` | Number of stopbits of the RS485 serial com with the insulation monitor. The number of stopbits depends on the parity chosen. Check our documentation and the insulation monitor documentation to check the available combinations *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_type` | str | `Not_Used` | `BenderISOCHA425HV`, `Not_Used` | Whether you are using one of our supported insulation monitors and which one |

### Specific Charger Interface Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `do_not_rearm_after_fault` **advanced** | bool | `false` | — | Only for ADVANTICS power module |
| `llc_use_external_voltage` **advanced** | float (V) | `0.0` | — | Only for ADVANTICS power module |
| `stack_pos` **advanced** | str | `0` | — | Stack position to use when working in conjonction with ADVANTICS power module |

#### Notes on some `[pistol:CHAdeMO]` entries

**`always_use_dynamic_max_current`**

When enabled, the dynamic maximum current(s) received over the Generic CAN interface are always used as the current limit (still capped by the configured maximum current), instead of being ignored when reported as zero. Note: a reported dynamic maximum of 0 A will then limit the current to 0 A.

**`clear_error_codes_on_idle`**

By default a code outlives the session that raised it: it stays raised through the return to idle and is cleared when the next plug-in starts a new session. Codes read while the controller is idle are then the post-mortem of the session that just ended.
Turn this on to clear them on the way back to idle instead, so codes are only ever visible while a vehicle is connected. The trade-off is that nobody who arrives after the vehicle is unplugged can still see why the last session failed.

**`max_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`supports_range_mode`**

Tells if charger can handle setpoints range mode, or if it is constrained to target mode only.
NB.: Range mode is only supported since Generic DC v3 (and for specific charger interfaces using the Generic interface in parallel for external control). For charger interfaces not actually supporting range mode (eg. Generic DC v2), this option is forced to false (and you will see an harmless warning in evse-controller logs about it).

## `[pistol:MCS]`

### Bidirectional Charging Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `is_bidirectional` | bool | `false` | — | Whether this charger supports both charge and discharge |
| `limit_non_bidir_to_positive_current` **advanced** | bool | `true` | — | Never report a negative present current to a vehicle that does not support bidirectional charging. Some vehicles refuse to charge otherwise. |
| `supports_range_mode` **advanced** | bool | `true` | — | — |

### CAN BUS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `charger_can_if` **advanced** | str | `can0` | — | CAN interface the power stage of this connector is wired to. |
| `charger_can_timeout_ms` **advanced** | float (ms) | `500.0` | — | Timeout for reception of Power_Modules_Status message in generic interface (ms). |
| `charger_type` | str | `Advantics_Generic_DC_v3` | `Advantics_Generic_DC_v1`, `Advantics_Generic_DC_v2`, `Advantics_Generic_DC_v3`, `Advantics_ADS_PC_UPUD`, `Advantics_ADS_PC_BPUD`, `Advantics_ADM_PC_BP25_BoostBuck`, `PRE_Charger`, `Maxwell_MXR` | Power stage this connector talks to. Picks the CAN protocol used between the controller and the charger. |

### CCS Params

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `V2G_SECC_CommunicationSetup_Performance_Time` **advanced** | float (s) | `60.0` | `0` to `300` | Time the vehicle is given, from the data link coming up, to complete session setup. The standard mandates 18 s, we are a bit more flexible. 0 disables the timeout. |
| `current_ripple` **advanced** | float | `1.0` | — | Peak-to-peak ripple of the output current, in amps. Reported to the vehicle so it can decide how much ripple to accept. |
| `din_iso_part2_cpd_force_evse_ready_on_processing_finished` **advanced** | bool | `false` | — | Whether to force EVSE_Ready status in DC_EVSEStatus when charge parameter discovery processing EVSEProcessing is Finished in DIN SPEC 70121 and ISO 15118-2. |
| `evse_id` **advanced** | str | `33A51A0001` | — | Identifier of the EVSE as used by OCCP communications. |
| `evse_id_for_iso_part2` **advanced** | str | *(empty)* | — | Identifier of the EVSE in a ISO15118-2 session. |
| `free_service` **advanced** | bool | `true` | — | Tell the vehicle that charging on this connector is free of charge. |
| `log_signature_details` **advanced** | bool | `false` | — | Write the details of every signature check to the log. Only useful when debugging Plug and Charge. |

### Cable Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_cable_current` | float (A) | `100.0` | `0` to `inf` | Maximum current rated for the cable. |
| `max_cable_power` | float (W) | `0.0` | `0` to `inf` | Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided |
| `max_cable_voltage` | float (V) | `500.0` | `0` to `inf` | Maximum voltage rated for the cable. |

### Charge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `current_ramp_down_rate` **advanced** | float (A/s) | `-20.0` | — | Rate of the current ramp at the end of the charge, A/s. |
| `current_ramp_enabled` **advanced** | bool | `true` | — | Apply the current ramp rates. Turn off to hand the power modules the current the vehicle asked for, unchanged. |
| `current_ramp_up_rate` **advanced** | float (A/s) | `20.0` | — | Rate of the current ramp at the beginning of the charge, A/s. |
| `max_charger_current` | float (A) | `120.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current above that value. |
| `max_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power above that value. |
| `max_charger_voltage` | float (V) | `500.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages above that value. |
| `min_charger_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with current below that value. |
| `min_charger_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with power below that value. |
| `min_charger_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to in charge direction (current going to the vehicle). Charger will refuse to work with voltages below that value. |

### Diagnostics

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `clear_error_codes_on_idle` **advanced** | bool | `false` | — | Clear the error codes when the pistol goes back to idle, instead of keeping them until the next plug-in. |

### Discharge Limits

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current above that value. |
| `max_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power above that value. |
| `max_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages above that value. |
| `min_charger_discharge_current` | float (A) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with current below that value. |
| `min_charger_discharge_power` | float (W) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with power below that value. |
| `min_charger_discharge_voltage` | float (V) | `0.0` | `0` to `inf` | This limit applies to the discharge direction (current coming from the vehicle) # NB.: Use positive values Charger will refuse to work with voltages below that value. |

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `always_use_dynamic_max_current` **advanced** | bool | `false` | — | — |
| `index` | int | `1` | `1` to `16` | Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. |
| `use_sequence_flags` | bool | `true` | — | Tells if flags in Sequence_Control message of the Generic CAN interface should be used https://documentation.advantics.fr/adm-cs-secc/charger-can-interfaces/can_v3.html#Sequence_Control |

### Insulation Monitor

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `insulation_monitor_address` | int | `3` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90` | RS485 address ID of the insulation monitor *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_baudrate` | int (Bd) | `9600` | `1200`, `2400`, `4800`, `9600`, `19200`, `38400`, `57600`, `115200` | Baudrate the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_parity` | str | `Even` | `Odd`, `No_Parity`, `Even` | Parity of the RS485 serial com with the insulation monitor. *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_stopbits` | int | `1` | `1`, `2` | Number of stopbits of the RS485 serial com with the insulation monitor. The number of stopbits depends on the parity chosen. Check our documentation and the insulation monitor documentation to check the available combinations *(Only when `insulation_monitor_type` = `BenderISOCHA425HV`.)* |
| `insulation_monitor_type` | str | `Not_Used` | `BenderISOCHA425HV`, `Not_Used` | Whether you are using one of our supported insulation monitors and which one |

### MCS Params

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `allow_no_tls_for_iso_part20` **advanced** | bool | `false` | — | Whether we should accept communications without TLS on -20 This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild. |
| `communication_start_delay_s` **advanced** | int (s) | `0` | `0` to `10` | How long to wait, after the vehicle is detected, before asserting CE state B and thus letting the vehicle start high-level communication. Leaves the user time to finish inserting the connector, so the link is not interrupted while SDP is running. Set to 0 to assert CE state B immediately. |
| `ignore_id_change` **advanced** | bool | `false` | — | Whether to ignore changes in the ID line (which can be caused by noise) only for testing purposes. Supported only for MCS. |
| `io_channel` **advanced** | str | `MCS_A` | `MCS_A` | Which hardware interface to use for MCS. |
| `mcs_ce_id_debouncer_count` **advanced** | int | `3` | — | Number of consistent readings required for debouncer of CE ID readings. |
| `mcs_ce_id_enable_extended_logging` **advanced** | bool | `false` | — | Whether to enable extended logging for CE ID readings. |
| `mcs_ce_id_filter_buffer_size` **advanced** | int | `5` | — | Size of the buffer used for median filtering of CE ID readings. |
| `mcs_ce_id_use_debouncer` **advanced** | bool | `false` | — | Whether to use debouncer on CE ID readings. |
| `mcs_ce_id_use_median_filter` **advanced** | bool | `false` | — | Whether to use median filter on CE ID readings. |

### Specific Charger Interface Extra Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dc_link_voltage` **advanced** | float (V) | `920.0` | — | Only for ADVANTICS AC01+DC01 power module: DC-link voltage the AC01 holds. Must stay above the maximum vehicle voltage; values below the charger minimum are clamped up. |
| `do_not_rearm_after_fault` **advanced** | bool | `false` | — | Only for ADVANTICS power module. |
| `force_charger_range_target_current` **advanced** | bool | `false` | — | Test only: drive the interface Range_Target_Current clamped by the charger current range only, ignoring the vehicle-requested/negotiated current. Only for ADVANTICS power module. |
| `llc_use_external_voltage` **advanced** | float (V) | `0.0` | — | Only for ADVANTICS power module |
| `stack_pos` **advanced** | str | `0` | — | Stack position to use when working in conjonction with ADVANTICS power module. |

### Test and Debug

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `skip_cable_check` **advanced** | bool | `false` | — | Should not be used in production. For R&D, allows skipping the cable check step in the charging sequence. |
| `skip_voltage_lowering_after_insulation_test` **advanced** | bool | `false` | — | Once the insulation test is done, do not ask the charger to lower its output voltage below 20 V before proceeding. Insulation_Test_Done is set to True immediately and the charger is left in its previous state. |

#### Notes on some `[pistol:MCS]` entries

**`always_use_dynamic_max_current`**

When enabled, the dynamic maximum current(s) received over the Generic CAN interface are always used as the current limit (still capped by the configured maximum current), instead of being ignored when reported as zero. Note: a reported dynamic maximum of 0 A will then limit the current to 0 A.

**`clear_error_codes_on_idle`**

By default a code outlives the session that raised it: it stays raised through the return to idle and is cleared when the next plug-in starts a new session. Codes read while the controller is idle are then the post-mortem of the session that just ended.
Turn this on to clear them on the way back to idle instead, so codes are only ever visible while a vehicle is connected. The trade-off is that nobody who arrives after the vehicle is unplugged can still see why the last session failed.

**`max_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`max_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_current`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_discharge_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_power`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`min_charger_voltage`**

Charger and cable electrical limits.
Should describe the actual limitations of these components. Ie.:
    - Charger and cable limits are combined (by lowest value)
    to provide a single set of limits to vehicle.
    - But they are actually taken into consideration separately
    when doing deratings when each get hot.
    - Power can be set to 0 to just use max voltage * max current.
    But you can set something different in order to define a power enveloppe.
    - When giving our combined max current to vehicle during charging,
    we also use the max power limits divided by actual present output
    voltage at that time.

Defaults are sensible limits for a 50kW unidirectional station

**`supports_range_mode`**

Tells if charger can handle setpoints range mode, or if it is constrained to target mode only. NB.: Range mode is only supported since Generic DC v3 (and for specific charger interfaces using the Generic interface in parallel for external control). For charger interfaces not actually supporting range mode (eg. Generic DC v2), this option is forced to false (and you will see an harmless warning in evse-controller logs about it).

## `[pistols]`

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enabled` | list | `['MCS']` | `MCS`, `CCS DC`, `CCS AC`, `CHAdeMO` / Length[1, 1] | Name of the pistols that you would like to enable |

## `[system]`

### Web Interface

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enable_web_interface` | bool | `true` | — | Makes the administration web interface available |
| `web_interface_certificate` | str | *(empty)* | — | Name of the certificate file to use to serve the web interface over HTTPS, as present in the certificate folder. Leave empty to serve the web interface over plain HTTP. |
| `web_interface_certificate_key` | str | *(empty)* | — | Name of the private key file matching `web_interface_certificate`, as present in the certificate folder. |
| `web_interface_ip` **advanced** | str | `0.0.0.0` | — | IP address the http server for the web interface will be bound to. This is not used to set the IP of the controller itself 0.0.0.0 means it will accept connection to any IP used by the controller, and should be the default unless you know what you are doing |
| `web_interface_port` | int | `80` | — | Port the web interface is served on. Left at 80, plain HTTP is served on 80; if a certificate is also configured, HTTPS is automatically served on 443. Set to any other value to serve both HTTP and HTTPS on that same port instead. |

## `[t1s_driver]`

### Network

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `mac_address` **advanced** | str | `advantics-serial` | — | How the 10BASE-T1S interface picks its MAC address: `advantics-serial` derives it from the board serial number, `advantics-random` and `random` generate one, `from-tap` keeps what the system set, or write a MAC address directly. |

## `[temperature_action:cable_stop_threshold]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `limit` | float (°C) | `90.0` | — | Temperature threshold at which the charge stop should be triggered, in °C |
| `mode` | str | `threshold` | `threshold` | Action type. `threshold` acts once the temperature crosses a limit. |
| `target` | str | `charge_stop` | `charge_stop` | What happens when the limit is crossed. `charge_stop` ends the session. |

## `[temperature_action:monitor]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `mode` | str | `monitor` | `monitor` | Action type. `monitor` only reports the temperature, it never changes the charge. |
| `target` | str | `monitor` | `monitor` | Not used by `monitor`: the reading is only reported. |

## `[temperature_function:cable]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `actions` | list | `['cable_derate_current', 'cable_stop_threshold', 'monitor']` | `cable_derate_current`, `cable_stop_threshold`, `monitor` | Actions run for every sensor assigned to the cable function. |

## `[tls]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `allow_iso_20_without_tls` | bool | `true` | — | Allow ISO 20 communication without TLS. |
| `allow_no_cert` | bool | `true` | — | Allow no certificate verification. |
| `enabled` | bool | `false` | — | Whether TLS is enabled. |
| `side` | str | `server` | `server` | — |

## `[tls:server]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ca_file` | str | `/app/certs/CA.pem` | — | Path to the CA certificate file. |
| `keyfile` | str | `/app/certs/server.key` | — | Path to the server key file. |
| `keyfile_passphrase` | str | *(empty)* | — | Passphrase for your server certificate, if any |
| `max_version` | str | `1.3` | `1.1`, `1.2`, `1.3`, `none` | — |
| `min_version` | str | `1.2` | `1.1`, `1.2`, `1.3`, `none` | — |
| `server_certificate` | str | `/app/certs/server.pem` | — | Path to the server certificate file. |
| `server_certificate_chain` | str | *(empty)* | — | Path to the server certificate chain |

<!-- Generated by documentation/tools/generate_config_reference.py -- do not edit by hand. -->
