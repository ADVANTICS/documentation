# Complete configuration reference

Every configuration entry of the ADM-CS-EVCC that you can set, generated from the
controller software itself so that it cannot fall behind. Use it to check a name, a default
or an allowed value; the other pages in this section explain what the entries are *for*.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode. Anything
not listed here is internal and not meant to be changed.

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

## `[ccs]`

### Charging Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `allow_dynamic_power_limits` **advanced** | bool | `true` | — | Follow the charger's maximum power, voltage and current as they change during the charge, instead of keeping the values it announced at the start of the session. DIN and ISO 15118-2 only. |
| `bulk_soc` | int (%) | `80` | — | State of Charge threhsold in % at which the bulk charge stage should end. Current will drop from that point. |
| `full_soc` | int (%) | `100` | — | State of Charge threhsold in % at which the charge should stop. |
| `preferred_control_mode` **advanced** | str | `Dynamic` | `Dynamic`, `Scheduled` | Control mode the vehicle asks for in ISO 15118-20. `Dynamic` lets the charger schedule the power, `Scheduled` follows a schedule agreed up front. |

### General

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ac_enabled` | bool | `true` | — | Whether the AC charging interface is allowed to operate |
| `enabled` | bool | `true` | — | Whether the CCS charging interface is allowed to operate |

### Hold Off Session Until BMS/HV Ready

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `hold_off_until_bms_ready` **advanced** | bool | `false` | — | When True, the session will always be held off at Connected_With_Full_Info stage until the vehicle BMS starts sending CAN messages and explicitly clears the hold-off signal (using EV_Status message). This prevents proceeding to the powered states before the vehicle internal equipment has finished preparing/waking up after init/sleep. The wait is bounded by wait_hv_ready_timeout_ms. |
| `wait_hv_ready_timeout_ms` **advanced** | int (ms) | `40000` | — | Used in combination with CAN bus signal EV_Status.HV_Preparing_Hold_Off which Allows the vehicle to delay the transition to powered states (powered states start from the insulation test) until the HV system is ready. This entry defines how long the delay should be. |

### Plug and Charge

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enable_pnc` **advanced** | bool | `false` | — | Whether Plug and Charge (PnC) should be enabled |
| `log_signature_details` **advanced** | bool | `false` | — | Write the details of every signature check to the log. Only useful when debugging Plug and Charge. |
| `pnc_contract_p12` **advanced** | str | *(empty)* | — | Path to the PKCS#12 file holding the Plug and Charge contract certificate. |
| `pnc_contract_p12_passphrase` **advanced** | str | *(empty)* | — | Passphrase for the Plug and Charge contract file, if it has one. |

### Process timeouts

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `cable_check_process_timeout_s` **advanced** | int (s) | `40` | — | Timeout for the cable check process, in seconds. This is the maximum time allowed for the cable check process to complete. If the process takes longer than this time, it will be considered a failure and the charging session will be stopped. |
| `communication_setup_timeout_s` **advanced** | int (s) | `20` | — | How long to wait for the charger to finish setting up communication before giving up on the session. |
| `precharge_process_timeout_s` **advanced** | int (s) | `7` | — | Timeout for the precharge process, in seconds. This is the maximum time allowed for the precharge process to complete. If the process takes longer than this time, it will be considered a failure and the charging session will be stopped. |

### Protocols

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `din_priority` | int | `3` | — | Priority of the different protocols. The priority is used to determine which protocol is used to charge the EV, among DIN, ISO 15118-2 and ISO15118-20. Protocols with the lowest priority value gets picked first whenever possible. |
| `enable_din` | bool | `true` | — | Allow DIN protocol for CCS charging |
| `enable_iso_part2` | bool | `true` | — | Allow ISO 15118-2 protocol for CCS charging |
| `enable_iso_part20` | bool | `true` | — | Allow ISO 15118-20 protocol for CCS charging |
| `iso_ed1_priority` | int | `2` | — | Priority of the different protocols. The priority is used to determine which protocol is used to charge the EV, among DIN, ISO 15118-2 and ISO15118-20. Protocols with the lowest priority value gets picked first whenever possible. |
| `iso_part20_dc_priority` | int | `1` | — | Priority of the different protocols. The priority is used to determine which protocol is used to charge the EV, among DIN, ISO 15118-2 and ISO15118-20. Protocols with the lowest priority value gets picked first whenever possible. |
| `iso_part2_priority` | int | `2` | — | Priority of the different protocols. The priority is used to determine which protocol is used to charge the EV, among DIN, ISO 15118-2 and ISO15118-20. Protocols with the lowest priority value gets picked first whenever possible. |

### Proximity Pilot

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `pp_mode` | str | `B2` | — | As specified by IEC 61851-1:2017, Annex B or SAE J1772. Possible values are: - B1: Corresponds to Type 1 inlets (latch release button on pistol, no current coding) - B2: Corresponds to Type 2 and Type 3 inlets (current coding). |

### TLS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `allow_no_tls_for_iso_part20` **advanced** | bool | `false` | — | Whether we should accept communications without TLS on -20 This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild. |
| `allow_tls_for_din` **advanced** | bool | `false` | — | Whether TLS should be allowed for DIN charging |

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `scheduled_mode_control_voltage_and_current` **advanced** | bool | `true` | — | Whether scheduled mode control for both voltage and current is enabled. |

## `[ev]`

### Vehicle Identification

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `id` | str | `33A51A0001AA` | — | Vehicle identifier sent to the charger for DIN and ISO 15118-2. Six bytes, written as hex. |
| `id_part20` | str | `VFRVO123456789ABCDEF` | — | Vehicle identifier sent to the charger for ISO 15118-20. Normally the VIN: 20 to 255 characters, and the first three must not contain I, O or Q. |

## `[generic_v1]`

### CAN ID Overrides

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `AC_Control` **advanced** | int | `0` | — | CAN ID for `AC_Control` message (decimal format). 0 means keep original ID. |
| `AC_Status` **advanced** | int | `0` | — | CAN ID for `AC_Status` message (decimal format). 0 means keep original ID. |
| `ADM_CS_EVCC_Inputs` **advanced** | int | `0` | — | CAN ID for `ADM_CS_EVCC_Inputs` message (decimal format). 0 means keep original ID. |
| `ADM_CS_EVCC_MEVC_Outputs` **advanced** | int | `0` | — | CAN ID for `ADM_CS_EVCC_MEVC_Outputs` message (decimal format). 0 means keep original ID. |
| `CCS_Extra_Information` **advanced** | int | `0` | — | CAN ID for `CCS_Extra_Information` message (decimal format). 0 means keep original ID. |
| `DC_Control` **advanced** | int | `0` | — | CAN ID for `DC_Control` message (decimal format). 0 means keep original ID. |
| `DC_Status1` **advanced** | int | `0` | — | CAN ID for `DC_Status1` message (decimal format). 0 means keep original ID. |
| `DC_Status2` **advanced** | int | `0` | — | CAN ID for `DC_Status2` message (decimal format). 0 means keep original ID. |
| `EVCC_MEVC_Diagnostic_Status` **advanced** | int | `0` | — | CAN ID for `EVCC_MEVC_Diagnostic_Status` message (decimal format). 0 means keep original ID. |
| `EVSE_Information` **advanced** | int | `0` | — | CAN ID for `EVSE_Information` message (decimal format). 0 means keep original ID. |
| `EV_Information` **advanced** | int | `0` | — | CAN ID for `EV_Information` message (decimal format). 0 means keep original ID. |
| `EV_Status` **advanced** | int | `0` | — | CAN ID for `EV_Status` message (decimal format). 0 means keep original ID. |
| `MCS_Extra_Information` **advanced** | int | `0` | — | CAN ID for `MCS_Extra_Information` message (decimal format). 0 means keep original ID. |

## `[generic_v2]`

### CAN ID Overrides

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `AC_Control` **advanced** | int | `0` | — | CAN ID for `AC_Control` message (decimal format). 0 means keep original ID. |
| `AC_Status` **advanced** | int | `0` | — | CAN ID for `AC_Status` message (decimal format). 0 means keep original ID. |
| `ADM_CS_EVCC_Inputs` **advanced** | int | `0` | — | CAN ID for `ADM_CS_EVCC_Inputs` message (decimal format). 0 means keep original ID. |
| `ADM_CS_EVCC_MEVC_Outputs` **advanced** | int | `0` | — | CAN ID for `ADM_CS_EVCC_MEVC_Outputs` message (decimal format). 0 means keep original ID. |
| `CCS_Extra_Information` **advanced** | int | `0` | — | CAN ID for `CCS_Extra_Information` message (decimal format). 0 means keep original ID. |
| `DC_Control` **advanced** | int | `0` | — | CAN ID for `DC_Control` message (decimal format). 0 means keep original ID. |
| `DC_Status1` **advanced** | int | `0` | — | CAN ID for `DC_Status1` message (decimal format). 0 means keep original ID. |
| `DC_Status2` **advanced** | int | `0` | — | CAN ID for `DC_Status2` message (decimal format). 0 means keep original ID. |
| `EVCC_MEVC_Diagnostic_Status` **advanced** | int | `0` | — | CAN ID for `EVCC_MEVC_Diagnostic_Status` message (decimal format). 0 means keep original ID. |
| `EVSE_Information` **advanced** | int | `0` | — | CAN ID for `EVSE_Information` message (decimal format). 0 means keep original ID. |
| `EV_Energy_Request` **advanced** | int | `0` | — | CAN ID for `EV_Energy_Request` message (decimal format). 0 means keep original ID. |
| `EV_Extra_BPT_Information` **advanced** | int | `0` | — | CAN ID for `EV_Extra_BPT_Information` message (decimal format). 0 means keep original ID. |
| `EV_Information` **advanced** | int | `0` | — | CAN ID for `EV_Information` message (decimal format). 0 means keep original ID. |
| `EV_Status` **advanced** | int | `0` | — | CAN ID for `EV_Status` message (decimal format). 0 means keep original ID. |
| `EV_V2X_Energy_Request` **advanced** | int | `0` | — | CAN ID for `EV_V2X_Energy_Request` message (decimal format). 0 means keep original ID. |
| `MCS_Extra_Information` **advanced** | int | `0` | — | CAN ID for `MCS_Extra_Information` message (decimal format). 0 means keep original ID. |

## `[hardware]`

### Inputs

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dig_in1` | str | `Not_Connected` | `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` | Function assigned to digital input 1 |
| `dig_in2` | str | `Not_Connected` | `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` | Function assigned to digital input 2 |
| `dig_in3` | str | `Not_Connected` | `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` | Function assigned to digital input 3 |

### Leds

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `led1` | str | `Not_Connected` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to LED 1 |
| `led2` | str | `Not_Connected` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to LED 2 |
| `led3` | str | `Not_Connected` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to LED 3 |

### Outputs

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `dig_out1` | str | `Plugged_In` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to digital output 1 |
| `dig_out2` | str | `Not_Connected` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to digital output 2 |
| `dig_out3` | str | `Not_Connected` | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` | Function assigned to digital output 3 |
| `plugged_in_pulse_ms` | int (ms) | `0` | — | Duration of the Plugged_In output pulse. By default (0) the output configured as Plugged_In latches HIGH on plug-in and stays HIGH for the whole charge session. Set a non-zero value to instead emit a single pulse of this length (in ms) on the plug-in rising edge, then return LOW. This is useful to wake up a vehicle VCU on connection without keeping it powered for the entire session, avoiding LV battery drain during long charges. |

### Power Management

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `auto_sleep` | bool | `false` | — | If enabled the EVCC will go to sleep automatically when reaching an IDLE state. It will be woken up on the next pistol plug. This can help reducing 24V power consumption when idle. |

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `temperature_filter_window` **advanced** | int | `5` | — | Size of the median filter window for temperature readings. |

## `[j1939]`

### J1939 Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `default_priority` | int | `0` | — | Priority applied to J1939 messages *(Only when `enable_j1939_bridge` = `true`.)* |
| `device_address` | int | `0` | `0` to `253` | J1939 source device address that should be used by the controller. Note that this address is static and that the controller does currently not implement the address claim protocol. Thus you need to make sure that the address configured here does not clash with other J1939 devices on the same bus. *(Only when `enable_j1939_bridge` = `true`.)* |
| `enable_j1939_bridge` | bool | `false` | — | Uses J1939 for the communications with the backend |
| `j1939_can_if` | str | `can0` | — | CAN interface to which J1939 messages should be sent *(Only when `enable_j1939_bridge` = `true`.)* |
| `peer_address` | int | `255` | `0` to `255` | The device address used by your side. Default (0xFF) is to accept messages from any device address, but in case of PGN conflicts you may want to filter in the messages from a given source address. *(Only when `enable_j1939_bridge` = `true`.)* |
| `vendor_pgn_offset` **advanced** | int | `0` | `0` to `192` | Can be used to solve ID conflicts in the J1939 vendoring space. All ADVANTICS vendor PGNs will be shifted by this offset *(Only when `enable_j1939_bridge` = `true`.)* |

## `[system]`

### Web Interface

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enable_web_interface` | bool | `true` | — | Makes the administration web interface available |
| `web_interface_certificate` | str | *(empty)* | — | Name of the certificate file to use to serve the web interface over HTTPS, as present in the certificate folder. Leave empty to serve the web interface over plain HTTP. |
| `web_interface_certificate_key` | str | *(empty)* | — | Name of the private key file matching `web_interface_certificate`, as present in the certificate folder. |
| `web_interface_ip` **advanced** | str | `0.0.0.0` | — | IP address the http server for the web interface will be bound to. This is not used to set the IP of the controller itself 0.0.0.0 means it will accept connection to any IP used by the controller, and should be the default unless you know what you are doing |
| `web_interface_port` | int | `80` | — | Port the web interface is served on. Left at 80, plain HTTP is served on 80; if a certificate is also configured, HTTPS is automatically served on 443. Set to any other value to serve both HTTP and HTTPS on that same port instead. |

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
| `side` | str | `client` | `client`, `server` | — |

## `[tls:client]`

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `ca_file` | str | `/app/certs/CA.pem` | — | Path to the CA certificate file. |
| `client_certificate` | str | `/app/certs/client.pem` | — | Path to the client certificate file. |
| `client_certificate_chain` | str | *(empty)* | — | Path to the client certificate chain |
| `keyfile` | str | `/app/certs/client.key` | — | Path to the client key file. |
| `keyfile_passphrase` | str | *(empty)* | — | Passphrase for your server certificate, if any |
| `max_version` | str | `1.3` | `1.1`, `1.2`, `1.3`, `none` | — |
| `min_version` | str | `1.2` | `1.1`, `1.2`, `1.3`, `none` | — |

## `[vehicle]`

### CAN BUS

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `can_if` | str | `can0` | `can0`, `vcan0` | WARNING: only modify if you are using J1939 ! Can be set to vcan0 if J1939 bridge is enabled, so that generic communications are not exposed on the physical CAN bus. |
| `can_timeout_ms` **advanced** | int (ms) | `2000` | — | Timeout in milliseconds for receiving critical frames during powered phases, before triggering a fault. |
| `force_extended_ids` **advanced** | bool | `false` | — | If we should send 29-bits extended frame IDs even if the ID fits on the 11 bits of a simple frame ID. |
| `type` | str | `Advantics_Generic_v1` | `Advantics_Internal`, `Advantics_Generic_v1`, `Advantics_Generic_v2`, `Emus_G1`, `EDN_FEX4432A0`, `VG11BMS` | Which BMS you are using |

### Contactors

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `contactor_force_open_current_not_reliable_delay_ms` **advanced** | int (ms) | `60000` | — | Delay in milliseconds to force open the contactor during E-stop when the current measurement is not reliable. This timeout is only effective if delay_e_stop_contactor_force_open_current_not_reliable is set to True. This is only effective if disable_e_stop_contactor_force_open_current_not_reliable is set to False. |
| `contactor_force_open_timeout_ms` **advanced** | int (ms) | `60000` | — | Timeout in milliseconds to force open the contactor during E-stop while current is still flowing (current above 5A). This timeout is only effective if enable_e_stop_contactor_force_open_timeout is set to True. |
| `dc_contactors_ios_delay` | int (s) | `1` | — | How long a DC contactor takes to physically close. The controller waits this long after the close command before treating the contactor as closed. |
| `dc_contactors_ios_has_feedback` | bool | `true` | — | Advantics controllers have a dedicated digital input to receive feedback when the contactor is closed (it has to contact to ground when closed). However, some contactors don’t have any wireable feedback. But feedback is always needed. If this is set to false, you should provide contactor feedback through the vehicle communication interface (CAN generic interface). If set to true, it means the feedback is provided through the dedicated digital input. |
| `dc_contactors_use_ios` | bool | `false` | — | Specify if DC contactors control is done with the dedicated controller IOs or through the vehicle communication interface. If set to false, it means the communication interface is used. Otherwise, if set to true, the corresponding message in the communication interface are ignored. |
| `delay_e_stop_contactor_force_open_current_not_reliable` **advanced** | bool | `false` | — | Delay force opening the contactors during E-stop when the current measurement is not reliable (e.g. due to a CAN reporting failure), giving time for the system to stabilize. Note: The default behavior during E-stop when current measurement is not reliable is to immediately force open the contactors to ensure safety. This is only effective if disable_e_stop_contactor_force_open_current_not_reliable is set to False. |
| `disable_e_stop_contactor_force_open_current_not_reliable` **advanced** | bool | `false` | — | Disables force opening the contactors during E-stop when the current measurement is not reliable (e.g. due to a CAN reporting failure). Note: The default behavior during E-stop when current measurement is not reliable is to immediately force open the contactors to ensure safety. |
| `enable_e_stop_contactor_force_open_timeout` **advanced** | bool | `false` | — | Enable timeout to force open the contactor during E-stop while current is still flowing (current above 5A). This can be used to force open the contactors as a last resort if the current does not drop after E-stop. Note: The default behavior during E-stop when the current is still flowing is to not force open the contactors to avoid damaging them. |
| `inhibit_precharge_unmatch_t` **advanced** | int | `1` | — | When charging DC, in precharge the controller is actively checking the voltage at the inlet is within ±20 V of the battery voltage. When the inlet voltage match this range, the contactors are commanded to close. |

### Inlet lock

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `enable_custom_lock_timing` **advanced** | bool | `false` | — | Lock the plug a delay after the charger is detected, see inlet_lock_delay_s. When off, the plug is locked once the charge parameters are known, which takes much longer on CCS because of the SLAC pairing. |
| `inlet_lock_delay_s` **advanced** | int (s) | `5` | `3` to `60` | How long to wait, once the charger is detected on the inlet, before locking the plug. Only used when enable_custom_lock_timing is on. Leaves the user time to finish inserting the connector. Whatever the value, the plug is locked at the latest when the charge parameters are known, just before the insulation test. |
| `lock_feedback_low_is_locked` | bool | `true` | — | Polarity for lock_feedback_r_threshold when lock is locked. For instance, true means that the lock is locked when resistance is below the threshold. Whereas false means lock is locked when the resistance is above the threshold. |
| `lock_feedback_median_filter_length` **advanced** | int | `5` | — | Length of the median filter applied to the lock feedback resistance measurement. A value of 1 disables filtering. <!> High values add latency. |
| `lock_feedback_r_threshold` | int (Ω) | `100` | — | Threshold, in ohms, between locked and unlocked state. |
| `locking_pulse_ms` | int (ms) | `600` | — | To avoid burning the lock motor, it is driven only for a certain amount of time in one or the other direction. The length of these driving pulses default to 600 ms as it seems to correspond to most locking system available on the market. It can be configured to a different value if your lock is more peculiar. |
| `no_inlet_lock` **advanced** | bool | `false` | — | If no inlet lock is used. Typical of table test use case, where you don’t want to be blocking a simulated charge test because it cannot detects any lock. |

### Isabellenhütte Current Sensor

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `can_sensor_if` | str | `can0` | `can0`, `can1` | CAN interface for the IVT-S sensor. Can be separate from the main CAN interface used for the BMS communication, which allows for using a different bitrate |
| `ivt_init_timeout_s` | float (s) | `10.0` | — | Timeout for IVT-S sensor initialisation. Increase if the sensor needs more time to wake up after power is applied. |
| `use_can_sensor` | str | *(empty)* | `Isabellenhutte`, `IVT-S` | The CAN sensor to use. Currently only Isabellenhutte IVT-S is supported. Empty string (in the config file) means no can Sensor. |

### No BMS Mode

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `max_charge_voltage` **advanced** | int (V) | `0` | — | Mandatory with no BMS mode, optional otherwise. But if it is specified, it should be below or equal to max_voltage. A value of 0 makes it optional. |
| `no_bms` **advanced** | bool | `false` | — | No BMS mode should NEVER be used in normal conditions. |

### Power Parameters

| Entry | Type | Default | Allowed | Description |
|---|---|---|---|---|
| `allow_bpt_at_full_soc` **advanced** | bool | `false` | — | Keep the session open for discharging once the battery is full, instead of reporting the charge as complete. |
| `current_deviation_a` **advanced** | int (A) | `10` | — | Current deviation limit threshold, in Amps. If charger is doing more or less current than this value, Advantics controller will consider it enters in current deviation error. This error will have to persist for a certain time (see current_deviation_t) to actually trigger a charge stop. |
| `current_deviation_accept_less` **advanced** | bool | `true` | — | If charger is doing less current than requested, we can accept it and not consider it to be a current deviation error. |
| `current_deviation_t` **advanced** | int (s) | `10` | — | Current deviation offending time before cut-off, in seconds. If charger is doing more or less current than current_deviation_a for this amount of time, the current deviation error will be confirmed and a charge stop will be triggered. |
| `current_ramp` **advanced** | int (A/s) | `20` | — | Maximum current ramp-up rate, in A/s. Will be used to limit current requests sent to charger. |
| `dynamic_target_voltage` **advanced** | bool | `false` | — | Take the target voltage from the BMS on every cycle instead of the fixed value set here. Falls back to the fixed value if the BMS sends 0 V. |
| `energy_capacity` | float (Wh) | `50000.0` | — | Energy capacity of the battery, in Wh. Required for bidirectional power transfers. Otherwise it is optional but recommended. Used for various informational calculations (SoC, remaining time, etc.). |
| `is_bidirectional` | bool | `false` | — | Enables bi-directional charging on EVCC |
| `max_current` | int (A) | `0` | — | Absolute maximum current EV systems (inlet, wires, contactors, battery, etc.) can safely accept. |
| `max_discharge_current` | int (A) | `0` | — | Absolute maximum current EV systems (inlet, wires, contactors, battery, etc.) can safely accept. during discharge. |
| `max_discharge_power` | int (W) | `0` | — | Highest power the vehicle can discharge at. ISO 15118-20 bidirectional charging only. |
| `max_energy_request` | float (Wh) | `0.0` | — | Most energy the vehicle asks the charger for, in ISO 15118-20. Only a fallback: the Advantics Generic v2 BMS overrides it from `EV_Energy_Request`, and only falls back here when the vehicle does not send that message. Left at 0, the battery energy capacity is used instead. |
| `max_power` | int (W) | `0` | — | Absolute maximum power EV systems (inlet, wires, contactors, battery, etc.) can safely accept. This specifies a power envelop used to determine capping of current requests depending on the present battery voltage. A value of 0 means no maximum power is configured and it will not be used to limit current requests. |
| `max_soc` | int | `99` | — | Maximum state of charge above which Advantics controller will trigger a normal stop. Only valid for DC charging. Set it to 80 to only do bulk charging. |
| `max_voltage` | int (V) | `500` | — | Absolute maximum voltage EV systems (inlet, wires, contactors, battery, etc.) can safely accept. |
| `min_current` | int (A) | `0` | — | Minimum current we want the charger to deliver (only relevant for CCS ISO AC). |
| `min_discharge_power` | int (W) | `0` | — | Lowest power the vehicle can discharge at. ISO 15118-20 bidirectional charging only. |
| `min_energy_request` | float (Wh) | `0.0` | — | Least energy the vehicle asks the charger for, in ISO 15118-20. Only a fallback: the Advantics Generic v2 BMS overrides it from `EV_Energy_Request`, and only falls back here when the vehicle does not send that message. Capped to `max_energy_request`. |
| `min_voltage` | int (V) | `200` | — | Minimum voltage that battery could reach at lowest possible state of charge (used for compatibility checks with charger capabilities). |
| `target_voltage` | int (V) | `450` | — | The target voltage sent to EVSE during the current delivery loop. |

#### Notes on some `[vehicle]` entries

**`current_ramp`**

The ramp uses a linear interpolation, such that the current increase between two requests does not exceed this rate. For instance, between two requests spaced by 100ms, with a ramp-up rate limit of 20 A/s, the current request can only increase by 2 A in that time period.

**`inhibit_precharge_unmatch_t`**

Contactors do not necessarily close immediately. In situations where contactors are actually managed by the vehicle and not the charge controller, the vehicle could be “preparing” for a few seconds before actually closing the contactors. While the controller waits to receive feedback that the contactors are closed, it will keep checking the inlet voltage is matching. If it no longer does for whatever reason, the controller considers it is an unmatch, and commands the contactors to reopen in order to avoid arcing.

However in other situations, the moment contactors are actually closing, the reading of the inlet voltage could vary widely, by a few hundreds volt. This is particularly the case when using a CAN sensor that measures the inlet voltage as a difference of two channels, themselves referenced to the battery DC-. If both contactors do not close exactly at the same time, the measured then calculated inlet voltage is invalid for a short amount of time. This config entry is here to prevent reopening the contactors for a specified amount of time after commanding them to close, in case there is a voltage unmatch.

**`no_bms`**

This is a special mode intended ONLY for testing or prototyping purposes. It allows you to not have to use a BMS (or not have to develop a bridge between our generic interface and the BMS protocol). The intended goal of this mode is to help you evaluate our controller and reach a demonstrative working charge in a short time span.
Normally, a BMS provide safe current request values with respect to the present state of charge of the battery. No BMS mode works by charging at a specific and static current, and automatically stops once a certain voltage is reached.

**`target_voltage`**

This is a Constant Current charging process. Target voltage should be higher than the battery voltage will ever reach at maximum state of charge.

<!-- Generated by documentation/tools/generate_config_reference.py -- do not edit by hand. -->
