# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [Identification](#Identification) | 0x810000 | 8 | OUT |  |
| [Bootloader_UID](#Bootloader_UID) | 0x810001 | 8 | OUT |  |
| [Firmware_UID](#Firmware_UID) | 0x810002 | 8 | OUT |  |
| [ADB_CAN_API_Version](#ADB_CAN_API_Version) | 0x810003 | 3 | OUT |  |
| [Status](#Status) | 0x810010 | 8 | OUT |  |
| [Faults](#Faults) | 0x810011 | 8 | OUT |  |
| [Converter_Control](#Converter_Control) | 0x810012 | 1 | IN |  |
| [Converter_Power_Info](#Converter_Power_Info) | 0x810013 | 6 | OUT |  |
| [Broadcast_Group_Control](#Broadcast_Group_Control) | 0x810014 | 1 | IN |  |
| [Interface_Status](#Interface_Status) | 0x810015 | 3 | OUT |  |
| [Keep_Alive_Control](#Keep_Alive_Control) | 0x810016 | 2 | IN |  |
| [Converter_Temperature](#Converter_Temperature) | 0x810017 | 8 | OUT |  |
| [Converter_Fans](#Converter_Fans) | 0x810018 | 6 | OUT |  |
| [Keep_Alive_Feed](#Keep_Alive_Feed) | 0x810019 | 1 | IN |  |
| [DC_Ports_Setpoints](#DC_Ports_Setpoints) | 0x810020 | 6 | IN |  |
| [DC_Port_Applied_Setpoints](#DC_Port_Applied_Setpoints) | 0x810021 | 8 | OUT |  |
| [DC_Port_Droop_Setpoints](#DC_Port_Droop_Setpoints) | 0x810022 | 8 | IN |  |
| [DC_Port_Applied_Droop_Setpoints](#DC_Port_Applied_Droop_Setpoints) | 0x810023 | 8 | OUT |  |
| [DC_Port_Measurements](#DC_Port_Measurements) | 0x810024 | 4 | OUT |  |
| [AC_Port_Setpoints](#AC_Port_Setpoints) | 0x810030 | 8 | IN |  |
| [AC_Port_Applied_Setpoints](#AC_Port_Applied_Setpoints) | 0x810031 | 8 | OUT |  |
| [AC_Port_Measurements](#AC_Port_Measurements) | 0x810032 | 8 | OUT |  |
| [L1_Measurements](#L1_Measurements) | 0x810033 | 8 | OUT |  |
| [L2_Measurements](#L2_Measurements) | 0x810034 | 8 | OUT |  |
| [L3_Measurements](#L3_Measurements) | 0x810035 | 8 | OUT |  |
| [AC01_Mode_Set](#AC01_Mode_Set) | 0x810040 | 1 | IN |  |
| [AC01_Mode_Applied](#AC01_Mode_Applied) | 0x810041 | 1 | OUT |  |
| [AC01_faults](#AC01_faults) | 0x810042 | 8 | OUT |  |
| [AC01_warning](#AC01_warning) | 0x810043 | 8 | OUT |  |
| [AC01_info](#AC01_info) | 0x810044 | 8 | OUT |  |
| [Stack_Control](#Stack_Control) | 0x810045 | 6 | IN |  |
| [Fault_Control](#Fault_Control) | 0x810050 | 1 | IN |  |
| [_Factory_Config](#_Factory_Config) | 0x810060 | 8 | IN |  |
| [Factory_Control](#Factory_Control) | 0x810061 | 8 | IN |  |
| [_Calibration_writing](#_Calibration_writing) | 0x810062 | 6 | IN |  |
| [_Calibration_reading_cmd](#_Calibration_reading_cmd) | 0x810063 | 2 | IN |  |
| [_Calibration_reading](#_Calibration_reading) | 0x810064 | 8 | OUT |  |
| [_Factory_Debug_cmd](#_Factory_Debug_cmd) | 0x810065 | 8 | IN |  |
| [info_adm_cs](#info_adm_cs) | 0x810080 | 8 | OUT |  |
| [info_adm_pc](#info_adm_pc) | 0x810081 | 4 | OUT |  |
| [info_adm_pc_id_1](#info_adm_pc_id_1) | 0x810082 | 8 | OUT |  |
| [info_adm_pc_id_2](#info_adm_pc_id_2) | 0x810083 | 8 | OUT |  |
| [info_adm_pc_id_3](#info_adm_pc_id_3) | 0x810084 | 8 | OUT |  |
| [info_adm_pc_id_4](#info_adm_pc_id_4) | 0x810085 | 8 | OUT |  |
| [info_adm_pc_id_5](#info_adm_pc_id_5) | 0x810086 | 8 | OUT |  |
| [info_adm_pc_id_6](#info_adm_pc_id_6) | 0x810087 | 8 | OUT |  |
| [info_adm_pc_status_1](#info_adm_pc_status_1) | 0x810088 | 8 | OUT |  |
| [info_adm_pc_status_2](#info_adm_pc_status_2) | 0x810089 | 8 | OUT |  |
| [info_adm_pc_status_3](#info_adm_pc_status_3) | 0x81008a | 8 | OUT |  |
| [info_adm_pc_status_4](#info_adm_pc_status_4) | 0x81008b | 8 | OUT |  |
| [info_adm_pc_status_5](#info_adm_pc_status_5) | 0x81008c | 8 | OUT |  |
| [info_adm_pc_status_6](#info_adm_pc_status_6) | 0x81008d | 8 | OUT |  |
| [cs_performance](#cs_performance) | 0x810090 | 8 | OUT |  |
| [info_can_api_error](#info_can_api_error) | 0x810091 | 8 | OUT |  |
| [_fms_state](#_fms_state) | 0x8100f0 | 8 | OUT |  |
| [_interlocks_status](#_interlocks_status) | 0x8100f1 | 3 | OUT |  |


<a id="Identification"></a>
## Identification { #Identification }


| * | * |
|---|---|
| **Frame ID** | 0x810000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Identification of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Label set |
| Variant | 8 | Label set |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #Identification-Type }

Type of device

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| GC01 | 128 |
| AC01 | 129 |
| DC01 | 130 |

#### Revision { #Identification-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| R0A | 0 |
| R0B | 1 |
| R0C | 2 |

#### Variant { #Identification-Variant }

The hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| VA00 | 0 |
| VA01 | 1 |

#### Stack_position { #Identification-Stack_position }

Position of the device within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #Identification-serial_number }

Unique device serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="Bootloader_UID"></a>
## Bootloader_UID { #Bootloader_UID }


| * | * |
|---|---|
| **Frame ID** | 0x810001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Unique Identifier of the Bootloader used on this device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID | 64 | Unsigned |

### Payload description

#### UID { #Bootloader_UID-UID }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  | 18446744073709549568 |


<a id="Firmware_UID"></a>
## Firmware_UID { #Firmware_UID }


| * | * |
|---|---|
| **Frame ID** | 0x810002 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Unique Identifier of the Firmware used on this device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID | 64 | Unsigned |

### Payload description

#### UID { #Firmware_UID-UID }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  | 18446744073709549568 |


<a id="ADB_CAN_API_Version"></a>
## ADB_CAN_API_Version { #ADB_CAN_API_Version }


| * | * |
|---|---|
| **Frame ID** | 0x810003 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

This message declares the version of the API that is provided by the device. The version follows newer convention, as this file is an API definition, patch does not apply

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Major | 8 | Unsigned |
| Minor | 8 | Unsigned |
| Patch | 8 | Unsigned |

### Payload description

#### Major { #ADB_CAN_API_Version-Major }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor { #ADB_CAN_API_Version-Minor }

The Minor version number. This number increases if there are backwards compatible changes, like new messages or the use of previously reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch { #ADB_CAN_API_Version-Patch }

The Patch number. This number increases when changes to descriptions and documentation/comments are made

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Status"></a>
## Status { #Status }


| * | * |
|---|---|
| **Frame ID** | 0x810010 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

General Status of the power converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| State | 16 | Label set |
| flag_enable | 1 | Single bit |
| flag_ready | 1 | Single bit |
| flag_energized | 1 | Single bit |
| flag_busy | 1 | Single bit |
| flag_sleep | 1 | Single bit |
| flag_warning | 1 | Single bit |
| flag_degraded | 1 | Single bit |
| flag_error | 1 | Single bit |
| flag_factory | 1 | Single bit |
| flag_god_mode | 1 | Single bit |

### Payload description

#### State { #Status-State }

Current operating state of the power converter.

                        Init: The converter is initializing. It will transition to Standby if initialization succeeds,
                        or to Critical/Error if it fails.
                        Standby: The converter is idle and ready to be turned-on if conditions are met (no errors, no warnings).
                        Turning_on: The converter is powering up.
                        Running: The converter is actively operating.
                        Turning_off: The converter is shutting down.
                        Error: A recoverable fault has occurred.
                        Critical: A critical fault has occurred, requiring reboot (please inform Advantics).
                        God: For Developer (mode cannot be used by customers).
                        Sleeping: The converter is in sleeping mode in order to save energy.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Label set |  | 1 | 0 |  | 65535 |

| Label name | Value |
|------------|-------|
| init | 0 |
| standby | 1 |
| turning_on | 2 |
| running | 3 |
| turning_off | 4 |
| error | 5 |
| critical | 6 |
| god | 7 |
| sleeping | 8 |

#### flag_enable { #Status-flag_enable }

Indicates  that the converter is asked to be enabled.
                        once condition are meet (no wanring nor error) the converter will do to turning-on

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_ready { #Status-flag_ready }

Indicates that a valid setpoint has been received and conditions are met to turn on the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_energized { #Status-flag_energized }

Indicates that the converter is energized (internal and external &gt; 24V)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_busy { #Status-flag_busy }

Indicates that the converter is in a transition state (init, turning on, or turning off). Some commands may be ignored during this step.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_sleep { #Status-flag_sleep }

Indicates that the converter is asked to operating in energy-saving (sleep) mode.

                        the converter will go in sleeping mode
                        Turning on the power converter in eco mode may take a little more time (feature not yet implemented).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_warning { #Status-flag_warning }

Indicates that one or more warnings are active.

                        When in standby mode, all warnings must be cleared before turning on the power converter.
                        If &quot;Enable&quot; is set in &quot;Converter_Control&quot;, the power converter will turn on as soon as all warnings are cleared.
                        The system may be operating in degraded mode.
                        During operation (Running), the power converter will continue to run, but degraded performance may be expected.
                        Refer to the &quot;Warning&quot; message for more details.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_degraded { #Status-flag_degraded }

Indicates that the converter is running in degraded performance mode

                    This can be due to high temperature.
                    Refer to the &quot;Warning&quot; message for more details.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_error { #Status-flag_error }

Indicates that one or more Errors are active.

                    When in standby mode, all errors must be cleared before turning on the power converter.
                    If &quot;Enable&quot; is set in &quot;Converter_Control&quot;, the power converter will turn on as soon as all warnings are cleared.
                    During operation (Running), the power converter will turn off.
                    Errors can be cleared using &quot;Clear_Interlock&quot; signals from the &quot;Fault_Control&quot; message.
                    The system may be operating in degraded mode.
                    Refer to the &quot;Errors&quot; or &quot;Faults&quot; message for more details.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_factory { #Status-flag_factory }

Indicates that the converter is operating in factory or service mode.

                        This flag should not be active for customers

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_god_mode { #Status-flag_god_mode }

Indicates that the converter is in special diagnostic or unrestricted mode (god mode).

                        This flag should not be active for customers

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 49 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Faults"></a>
## Faults { #Faults }


| * | * |
|---|---|
| **Frame ID** | 0x810011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Fault status bitfield (1-bit flags per fault type)

                    Severity levels and clearing:
                    - Tripped: Can be cleared using &quot;Clear_Interlock&quot; signals from &quot;Fault_Control&quot; message.
                    - Critical: Requires system reboot (contact Advantics support).
                    - Error: Can be cleared using &quot;Clear_Interlock&quot; signals from &quot;Fault_Control&quot; message.

                    State machine behavior:
                    - Standby: All errors must be cleared before power-on is allowed. if &quot;Enable&quot;  is active, the converter will
                      turns on when all faults/warnings are cleared.
                    - Running: Any Error fault triggers the turning-off sequence shutdown. And any Critical fault trigger immediate shutdown

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| internal | 1 | Label set |
| external | 1 | Label set |
| system | 1 | Label set |
| EEPROM_failure | 1 | Label set |
| wrong_nfo | 1 | Label set |
| Measurement_system_failure | 1 | Label set |
| PLL_not_locked | 1 | Label set |
| overtemperature | 1 | Label set |
| fan_stuck | 1 | Label set |
| dead_module | 1 | Label set |
| keep_alive_not_serv_internal | 1 | Label set |
| error_temperature | 1 | Label set |
| internal_modules_ready | 1 | Label set |
| internal_modules_can_api | 1 | Label set |
| internal_modules_missing | 1 | Label set |
| internal_modules_wrong | 1 | Label set |
| internal_modules_stack | 1 | Label set |
| internal_modules_init | 1 | Label set |
| wrong_revision | 1 | Label set |
| v_in_low | 1 | Label set |
| v_in_critical | 1 | Label set |
| keep_alive_not_serv | 1 | Label set |

### Payload description

#### internal { #Faults-internal }

Internal interlock trip

                    An internal issue has arisen.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Tripped | 1 |

#### external { #Faults-external }

External interlock trip

                    Common causes:
                    - External emergency stop button pressed
                    - External safety interlock opened (door switch, guard, etc.)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Tripped | 1 |

#### system { #Faults-system }

Critical system fault detected (contact Advantics support)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### EEPROM_failure { #Faults-EEPROM_failure }

EEPROM read/write failure (contact Advantics support)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### wrong_nfo { #Faults-wrong_nfo }

Invalid configuration detected (contact Advantics support)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### Measurement_system_failure { #Faults-Measurement_system_failure }

Voltage/current measurement system fault (contact Advantics support)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### PLL_not_locked { #Faults-PLL_not_locked }

PLL not locked (contact Advantics support)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### overtemperature { #Faults-overtemperature }

Over-temperature condition detected

                    Cooling plate temperature exceeded 75°C threshold
                    Can be cleared once temperature is bellow 75°C. check message &quot;Converter_Temperature&quot;

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### fan_stuck { #Faults-fan_stuck }

Cooling fan stalled or not running

                        The system may overheat(contact Advantics support if the problem persist)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### dead_module { #Faults-dead_module }

Lost communication between the ADM-CS and one or more ADM-PC

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### keep_alive_not_serv_internal { #Faults-keep_alive_not_serv_internal }

Internal ADM-PC keep-alive watchdog timeout. Was not served in time by ADM-CS

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### error_temperature { #Faults-error_temperature }

Temperature sensor error. One or more sensors are unavailable or reporting invalid data.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### internal_modules_ready { #Faults-internal_modules_ready }

One or more internal modules (ADM-PC) are NOT ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### internal_modules_can_api { #Faults-internal_modules_can_api }

One or more internal modules (ADM-PC) have mismatched CAN API versions expected by ADM-CS

                        check message &quot;info_can_api_error&quot; for more detail

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_missing { #Faults-internal_modules_missing }

One or more internal modules (ADM-PC) are  missing (not detect on can bus)

                        check message &quot;info_adm_pc&quot; for more detail

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_wrong { #Faults-internal_modules_wrong }

One or more internal modules (ADM-PC) are not compatible with the NFO of ADM-CS

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_stack { #Faults-internal_modules_stack }

One or more internal modules (ADM-PC) don&#x27;t respect the required stack position for the NFO of ADM-CS

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_init { #Faults-internal_modules_init }

One or more internal modules (ADM-PC) failed at init (ready flag)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### wrong_revision { #Faults-wrong_revision }

One or more internal modules (ADM-PC) don&#x27;t have the required revision for the NFO of ADM-CS

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### v_in_low { #Faults-v_in_low }

24V input voltage too low

                        Increase voltage and/or current before clearing the error.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### v_in_critical { #Faults-v_in_critical }

24V input voltage critically low,

                        Increase voltage and/or current and reboot the power converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### keep_alive_not_serv { #Faults-keep_alive_not_serv }

keep-alive watchdog timeout

                    Upper controller did not service the keepalive watchdog in time.
                    Check &quot;Interface_Status&quot; message and increase &quot;keep_Alive_Period&quot; if needed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |


<a id="Converter_Control"></a>
## Converter_Control { #Converter_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810012 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Converter control command

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| enable | 1 | Single bit |
| sleep | 1 | Single bit |

### Payload description

#### enable { #Converter_Control-enable }

Enable the power converter
                       enable takes priority over sleep

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### sleep { #Converter_Control-sleep }

Ask the converter to go to sleep mode

                        the converter will go to sleep mode only from standby mode
                        enable  takes priority over sleep

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Converter_Power_Info"></a>
## Converter_Power_Info { #Converter_Power_Info }


| * | * |
|---|---|
| **Frame ID** | 0x810013 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Real-time power converter performance metrics

                  Some signals are still experimental and may change in the future.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| load | 8 | Unsigned |
| efficiency | 8 | Unsigned |
| Power_capability | 16 | Signed |
| low_power_input | 16 | Signed |

### Payload description

#### load { #Converter_Power_Info-load }

Current load utilization

                    Actual power demand relative to Power_capability limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### efficiency { #Converter_Power_Info-efficiency }

Converter efficiency

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### Power_capability { #Converter_Power_Info-Power_capability }

Maximum deliverable power based on configured setpoints (V * A).

                   Examples:
                       - 1000V * 50A = 50kW ✓ (within limits)
                       - 1500V * 200A = 300kW → capped at 100kW (converter maximum)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | kw | 0.1 | 0 | -3276.8 | 3276.7 |

#### low_power_input { #Converter_Power_Info-low_power_input }

low-voltage input (typically 24V)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | v | 0.01 | 0 | -327.68 | 327.67 |


<a id="Broadcast_Group_Control"></a>
## Broadcast_Group_Control { #Broadcast_Group_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810014 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure the broadcast group that the power converter belongs to.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID | 8 | Unsigned |

### Payload description

#### Group_ID { #Broadcast_Group_Control-Group_ID }

Broadcast Group that the power converter should monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Interface_Status"></a>
## Interface_Status { #Interface_Status }


| * | * |
|---|---|
| **Frame ID** | 0x810015 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

interface status

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Broadcast_Group | 8 | Unsigned |
| keep_Alive | 4 | Label set |
| reserved | 4 | Label set |
| keep_Alive_Period | 8 | Unsigned |

### Payload description

#### Broadcast_Group { #Interface_Status-Broadcast_Group }

The broadcast group that the module belongs to. Broadcast group 0 implies that the module is not part of a broadcast group.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 30 |

#### keep_Alive { #Interface_Status-keep_Alive }

keep alive requires the supervisory/upper controller to send a heartbeat message at regular intervals

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 4 | Label set |  | 1 | 0 |  | 15 |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### reserved { #Interface_Status-reserved }

reserved for future usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 4 | Label set |  | 1 | 0 |  | 15 |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### keep_Alive_Period { #Interface_Status-keep_Alive_Period }

The maximum period of the keep alive message. If the time between two heart-beat messages is longer than this value, the power converter will go to Error. This only applies when the Heartbeat signal is Enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | s | 0.1 | 0 |  | 25.5 |


<a id="Keep_Alive_Control"></a>
## Keep_Alive_Control { #Keep_Alive_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810016 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure the Heartbeat for the Module. The &#x27;Heartbeat Period&#x27; signal only apply if the heartbeat signals are enabled

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Enable | 1 | Label set |
| reserved | 1 | Label set |
| Period | 8 | Unsigned |

### Payload description

#### Enable { #Keep_Alive_Control-Enable }

Enable/Disable the Heartbeat feature of the Module

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### reserved { #Keep_Alive_Control-reserved }

Reserved for future usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Period { #Keep_Alive_Control-Period }

Set the maximum period of the Heartbeat message. If the time between two heart-beat messages is longer than this value, the power converter will go to Error.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | s | 0.1 | 0 |  | 25.5 |


<a id="Converter_Temperature"></a>
## Converter_Temperature { #Converter_Temperature }


| * | * |
|---|---|
| **Frame ID** | 0x810017 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Readouts of the power converter temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Cooling_plate | 16 | Signed |
| Magnetics | 16 | Signed |
| Transistors | 16 | Signed |
| reserved | 16 | Signed |

### Payload description

#### Cooling_plate { #Converter_Temperature-Cooling_plate }

Temperature of the cooling plate

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### Magnetics { #Converter_Temperature-Magnetics }

Highest measured temp of magnetics

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### Transistors { #Converter_Temperature-Transistors }

Highest measured temp of transistors

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### reserved { #Converter_Temperature-reserved }

reserved for future usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |


<a id="Converter_Fans"></a>
## Converter_Fans { #Converter_Fans }


| * | * |
|---|---|
| **Frame ID** | 0x810018 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Readouts from the power converter&#x27;s internal fans.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| A_rpm | 16 | Unsigned |
| A_pwm | 8 | Unsigned |
| B_rpm | 16 | Unsigned |
| B_pwm | 8 | Unsigned |

### Payload description

#### A_rpm { #Converter_Fans-A_rpm }

Measured speed of Fan A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | rpm | 1 | 0 |  | 65535 |

#### A_pwm { #Converter_Fans-A_pwm }

Fan A target speed in percentage (0 to 100%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### B_rpm { #Converter_Fans-B_rpm }

Measured speed of Fan B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Unsigned | rpm | 1 | 0 |  | 65535 |

#### B_pwm { #Converter_Fans-B_pwm }

Fan B target speed in percentage (0 to 100%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | % | 1 | 0 |  | 255 |


<a id="Keep_Alive_Feed"></a>
## Keep_Alive_Feed { #Keep_Alive_Feed }


| * | * |
|---|---|
| **Frame ID** | 0x810019 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

keep alive feeding

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| feed | 1 | Single bit |

### Payload description

#### feed { #Keep_Alive_Feed-feed }

The value doesn&#x27;t matter here, it is only used to feed the keepalive

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="DC_Ports_Setpoints"></a>
## DC_Ports_Setpoints { #DC_Ports_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810020 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

The setpoints control the behaviour of the DC Port of the AC01. The AC01 operates this port in CVCC mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Positive_Current_Limit | 16 | Signed |
| Negative_Current_Limit | 16 | Signed |

### Payload description

#### Voltage { #DC_Ports_Setpoints-Voltage }

Control the target dc side voltage. This voltage will be maintained as long as the current required to do so is smaller than the current limits specified in this message

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  | 6553.5 |

#### Positive_Current_Limit { #DC_Ports_Setpoints-Positive_Current_Limit }

The maximum current that the AC01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |

#### Negative_Current_Limit { #DC_Ports_Setpoints-Negative_Current_Limit }

The maximum current that the AC01 will sink into the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="DC_Port_Applied_Setpoints"></a>
## DC_Port_Applied_Setpoints { #DC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the AC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Positive_Current_Limit | 16 | Signed |
| Negative_Current_Limit | 16 | Signed |

### Payload description

#### Voltage { #DC_Port_Applied_Setpoints-Voltage }

The voltage target of the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  | 6553.5 |

#### Positive_Current_Limit { #DC_Port_Applied_Setpoints-Positive_Current_Limit }

The maximum current that the AC01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |

#### Negative_Current_Limit { #DC_Port_Applied_Setpoints-Negative_Current_Limit }

The maximum amount of current that the AC01 will sink into the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="DC_Port_Droop_Setpoints"></a>
## DC_Port_Droop_Setpoints { #DC_Port_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810022 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints for applying Droop on the DC Port. Droop is needed for paralleling multiple AC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |
| Reserved | 31 | Unsigned |

### Payload description

#### Positive_Current_Droop { #DC_Port_Droop_Setpoints-Positive_Current_Droop }

The droop resistance to apply for current flowing out of the DC port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  | 655.35 |

#### Negative_Current_Droop { #DC_Port_Droop_Setpoints-Negative_Current_Droop }

The droop resistance to apply for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  | 655.35 |

#### Enable { #DC_Port_Droop_Setpoints-Enable }

Enable DC Droop. If this feature is enabled the output voltage of the DC port varies with output current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #DC_Port_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only &#x27;0&#x27;s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  | 2147483647 |


<a id="DC_Port_Applied_Droop_Setpoints"></a>
## DC_Port_Applied_Droop_Setpoints { #DC_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810023 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Droop setpoints that are applied by the AC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |
| Reserved | 31 | Unsigned |

### Payload description

#### Positive_Current_Droop { #DC_Port_Applied_Droop_Setpoints-Positive_Current_Droop }

The droop resistance applied for current flowing out of the DC port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  | 655.35 |

#### Negative_Current_Droop { #DC_Port_Applied_Droop_Setpoints-Negative_Current_Droop }

The droop resistance applied for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  | 655.35 |

#### Enable { #DC_Port_Applied_Droop_Setpoints-Enable }

Show is DC Droop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #DC_Port_Applied_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only &#x27;0&#x27;s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  | 2147483647 |


<a id="DC_Port_Measurements"></a>
## DC_Port_Measurements { #DC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810024 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Measurements of the DC Bus

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #DC_Port_Measurements-Voltage }

Voltage on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  | 6553.5 |

#### Current { #DC_Port_Measurements-Current }

Current through the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="AC_Port_Setpoints"></a>
## AC_Port_Setpoints { #AC_Port_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810030 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints to apply to the AC Port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| grid | 16 | Label set |
| Q | 16 | Signed |
| RMS_Phase_Current_Limit | 16 | Unsigned |

### Payload description

#### grid { #AC_Port_Setpoints-grid }

select grid type that should be generated. All grids are 3-phase.

                FOLLOWING (0): Follows existing grid if compatible (see below).
                230V_400V_50HZ (1): 3-Phase 230V (line-to-neutral) / 400V (line-to-line), 50Hz
                277V_480V_60HZ (2): 3-Phase 277V (line-to-neutral) / 480V (line-to-line), 60Hz
                120V_208V_60HZ (3): 3-Phase 120V (line-to-neutral) / 208V (line-to-line), 60Hz

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Label set |  | 1 | 0 |  | 65535 |

| Label name | Value |
|------------|-------|
| FOLLOWING | 0 |
| 230V_400V_50HZ | 1 |
| 277V_480V_60HZ | 2 |
| 120V_208V_60HZ | 3 |

#### Q { #AC_Port_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the AC01 to behave inductively, negative values cause the AC01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | VAR | 10 | 0 | -327680 | 327670 |

#### RMS_Phase_Current_Limit { #AC_Port_Setpoints-RMS_Phase_Current_Limit }

The maximum RMS current that the AC01 will supply at its AC terminals.
                This value limits the the magnitute of the AC current and applies
                symmetrically to both source and sink currents. This limit applies to
                the current carried by a single phase.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  | 6553.5 |


<a id="AC_Port_Applied_Setpoints"></a>
## AC_Port_Applied_Setpoints { #AC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810031 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Setpoints that are currently being applied to the the AC Port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| grid | 16 | Label set |
| Q | 16 | Signed |
| RMS_Phase_Current_Limit | 16 | Unsigned |

### Payload description

#### grid { #AC_Port_Applied_Setpoints-grid }

select grid type that should be generated. All grids are 3-phase.

                FOLLOWING (0): Follows existing grid if compatible (see below).
                230V_400V_50HZ (1): 3-Phase 230V (line-to-neutral) / 400V (line-to-line), 50Hz
                277V_480V_60HZ (2): 3-Phase 277V (line-to-neutral) / 480V (line-to-line), 60Hz
                120V_208V_60HZ (3): 3-Phase 120V (line-to-neutral) / 208V (line-to-line), 60Hz

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Label set |  | 1 | 0 |  | 65535 |

| Label name | Value |
|------------|-------|
| FOLLOWING | 0 |
| 230V_400V_50HZ | 1 |
| 277V_480V_60HZ | 2 |
| 120V_208V_60HZ | 3 |

#### Q { #AC_Port_Applied_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the AC01 to behave inductively, negative values cause the AC01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | VAR | 10 | 0 | -327680 | 327670 |

#### RMS_Phase_Current_Limit { #AC_Port_Applied_Setpoints-RMS_Phase_Current_Limit }

The maximum RMS current that the AC01 will supply at its AC terminals.
                This value limits the the magnitute of the AC current and applies
                symmetrically to both source and sink currents. This limit applies to
                the current carried by a single phase.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  | 6553.5 |


<a id="AC_Port_Measurements"></a>
## AC_Port_Measurements { #AC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810032 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Mesured values of the Grid connection

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency | 16 | Unsigned |
| Voltage | 16 | Unsigned |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency { #AC_Port_Measurements-Frequency }

RMS Voltage of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  | 655.35 |

#### Voltage { #AC_Port_Measurements-Voltage }

Average RMS Line to Line voltage at the AC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  | 6553.5 |

#### Reserved { #AC_Port_Measurements-Reserved }

This space is reserved. This region contains only &#x27;0&#x27;s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="L1_Measurements"></a>
## L1_Measurements { #L1_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810033 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Measurements for L1 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L1_Measurements-U }

RMS Voltage of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 | -3276.8 | 3276.7 |

#### I { #L1_Measurements-I }

RMS Current of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |

#### P { #L1_Measurements-P }

Active power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 | -3276.8 | 3276.7 |

#### Q { #L1_Measurements-Q }

Reactive power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="L2_Measurements"></a>
## L2_Measurements { #L2_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810034 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Measurements for L2 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L2_Measurements-U }

RMS Voltage of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 | -3276.8 | 3276.7 |

#### I { #L2_Measurements-I }

RMS Current of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |

#### P { #L2_Measurements-P }

Active power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 | -3276.8 | 3276.7 |

#### Q { #L2_Measurements-Q }

Reactive power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="L3_Measurements"></a>
## L3_Measurements { #L3_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810035 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Measurements for L3 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L3_Measurements-U }

RMS Voltage of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 | -3276.8 | 3276.7 |

#### I { #L3_Measurements-I }

RMS Current of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 | -3276.8 | 3276.7 |

#### P { #L3_Measurements-P }

Active power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 | -3276.8 | 3276.7 |

#### Q { #L3_Measurements-Q }

Reactive power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 | -3276.8 | 3276.7 |


<a id="AC01_Mode_Set"></a>
## AC01_Mode_Set { #AC01_Mode_Set }


| * | * |
|---|---|
| **Frame ID** | 0x810040 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure AC01 operating mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #AC01_Mode_Set-mode }

Requested operating mode

            DC_Controlled (0): DC side voltage controlled to setpoint, requires AC side input present
            AC_Controlled (1): AC side voltage controlled (not yet supported)
            Bleeding (2): Discharge internal capacitors/remaining charge

            changing mode can only be done when the power converter is not &quot;Enable&quot;

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| DC_Controlled | 0 |
| AC_Controlled | 1 |
| Bleeding | 2 |


<a id="AC01_Mode_Applied"></a>
## AC01_Mode_Applied { #AC01_Mode_Applied }


| * | * |
|---|---|
| **Frame ID** | 0x810041 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

AC01 actual operating mode (readback)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #AC01_Mode_Applied-mode }

Currently applied operating mode

                changing mode can only be done when the power converter is not &quot;Enable&quot;

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| DC_Controlled | 0 |
| AC_Controlled | 1 |
| Bleeding | 2 |


<a id="AC01_faults"></a>
## AC01_faults { #AC01_faults }


| * | * |
|---|---|
| **Frame ID** | 0x810042 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

AC01 Critical and error conditions

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| CABLE_1_2_L1 | 1 | Label set |
| CABLE_1_3_L1 | 1 | Label set |
| CABLE_1_2_L2 | 1 | Label set |
| CABLE_1_3_L2 | 1 | Label set |
| CABLE_1_2_L3 | 1 | Label set |
| CABLE_1_3_L3 | 1 | Label set |
| CABLE_4_5_L1 | 1 | Label set |
| CABLE_4_6_L1 | 1 | Label set |
| CABLE_4_5_L2 | 1 | Label set |
| CABLE_4_6_L2 | 1 | Label set |
| CABLE_4_5_L3 | 1 | Label set |
| CABLE_4_6_L3 | 1 | Label set |
| CABLE_1_4_L1 | 1 | Label set |
| CABLE_1_4_L2 | 1 | Label set |
| CABLE_1_4_L3 | 1 | Label set |
| CABLE_2_3_DC | 1 | Label set |
| CABLE_5_6_DC | 1 | Label set |
| CABLE_3_5_DC | 1 | Label set |
| MODULE_1_RUNNING | 1 | Label set |
| MODULE_2_RUNNING | 1 | Label set |
| MODULE_3_RUNNING | 1 | Label set |
| MODULE_4_RUNNING | 1 | Label set |
| MODULE_5_RUNNING | 1 | Label set |
| MODULE_6_RUNNING | 1 | Label set |
| reserved_1 | 1 | Label set |
| reserved_2 | 1 | Label set |
| reserved_3 | 1 | Label set |
| reserved_4 | 1 | Label set |
| PRECHARGE_FAILED | 1 | Label set |
| Main_Contactors_failed | 1 | Label set |
| FILTER_NOT_RUNNING | 1 | Label set |
| RECTIFIER_3P_NOT_RUNNING | 1 | Label set |
| AFE_NOT_OFF | 1 | Label set |
| FILTER_STOP_RUNNING | 1 | Label set |
| RECTIFIER_3P_STOP_RUNNING | 1 | Label set |
| AFE_PWM_NOT_RUNNING | 1 | Label set |
| AFE_PWM_STOP_RUNNING | 1 | Label set |
| BLEEDING_FAILED | 1 | Label set |
| FILTER_NOT_OFF | 1 | Label set |
| INVERTER_3P_NOT_RUNNING | 1 | Label set |
| INVERTER_3P_STOP_RUNNING | 1 | Label set |

### Payload description

#### CABLE_1_2_L1 { #AC01_faults-CABLE_1_2_L1 }

Critical: Phase mismatch between DMF1(1).L1 and BP25(2).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L1 { #AC01_faults-CABLE_1_3_L1 }

Critical: Phase mismatch between DMF1(1).L1 and BP25(3).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L2 { #AC01_faults-CABLE_1_2_L2 }

Critical: Phase mismatch between DMF1(1).L2 and BP25(2).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L2 { #AC01_faults-CABLE_1_3_L2 }

Critical: Phase mismatch between DMF1(1).L2 and BP25(3).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L3 { #AC01_faults-CABLE_1_2_L3 }

Critical: Phase mismatch between DMF1(1).L3 and BP25(2).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L3 { #AC01_faults-CABLE_1_3_L3 }

Critical: Phase mismatch between DMF1(1).L3 and BP25(3).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L1 { #AC01_faults-CABLE_4_5_L1 }

Critical: Phase mismatch between DMF1(4).L1 and BP25(5).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L1 { #AC01_faults-CABLE_4_6_L1 }

Critical: Phase mismatch between DMF1(4).L1 and BP25(6).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L2 { #AC01_faults-CABLE_4_5_L2 }

Critical: Phase mismatch between DMF1(4).L2 and BP25(5).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L2 { #AC01_faults-CABLE_4_6_L2 }

Critical: Phase mismatch between DMF1(4).L2 and BP25(6).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L3 { #AC01_faults-CABLE_4_5_L3 }

Critical: Phase mismatch between DMF1(4).L3 and BP25(5).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L3 { #AC01_faults-CABLE_4_6_L3 }

Critical: Phase mismatch between DMF1(4).L3 and BP25(6).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L1 { #AC01_faults-CABLE_1_4_L1 }

Critical: Grid L1 mismatch between DMF1(1).IN and DMF1(4).IN

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L2 { #AC01_faults-CABLE_1_4_L2 }

Critical: Phase mismatch between DMF1(1).L2 and DMF1(4).L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L3 { #AC01_faults-CABLE_1_4_L3 }

Critical: Phase mismatch between DMF1(1).L3 and DMF1(4).L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_2_3_DC { #AC01_faults-CABLE_2_3_DC }

Critical: DC mismatch between BP25(2) and BP25(3)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_5_6_DC { #AC01_faults-CABLE_5_6_DC }

Critical: DC mismatch between BP25(5) and BP25(6)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_5_DC { #AC01_faults-CABLE_3_5_DC }

Critical: DC mismatch between BP25(3) and BP25(5)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### MODULE_1_RUNNING { #AC01_faults-MODULE_1_RUNNING }

Error: Module 1 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_2_RUNNING { #AC01_faults-MODULE_2_RUNNING }

Error: Module 2 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_3_RUNNING { #AC01_faults-MODULE_3_RUNNING }

Error: Module 3 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_4_RUNNING { #AC01_faults-MODULE_4_RUNNING }

Error: Module 4 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_5_RUNNING { #AC01_faults-MODULE_5_RUNNING }

Error: Module 5 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_6_RUNNING { #AC01_faults-MODULE_6_RUNNING }

Error: Module 6 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_1 { #AC01_faults-reserved_1 }

reserved_1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_2 { #AC01_faults-reserved_2 }

reserved_2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_3 { #AC01_faults-reserved_3 }

reserved_3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_4 { #AC01_faults-reserved_4 }

reserved_4

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 27 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### PRECHARGE_FAILED { #AC01_faults-PRECHARGE_FAILED }

Error: Precharge failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 28 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### Main_Contactors_failed { #AC01_faults-Main_Contactors_failed }

Error: Main contactors did not closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 29 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_RUNNING { #AC01_faults-FILTER_NOT_RUNNING }

Error: Filter is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 30 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_NOT_RUNNING { #AC01_faults-RECTIFIER_3P_NOT_RUNNING }

Error: Three-phase rectifier is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 31 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_NOT_OFF { #AC01_faults-AFE_NOT_OFF }

Error: AFE is not off, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_STOP_RUNNING { #AC01_faults-FILTER_STOP_RUNNING }

Error: Filter stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_STOP_RUNNING { #AC01_faults-RECTIFIER_3P_STOP_RUNNING }

Error: Rectifier stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 35 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_NOT_RUNNING { #AC01_faults-AFE_PWM_NOT_RUNNING }

Error: BLEEDING is not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_STOP_RUNNING { #AC01_faults-AFE_PWM_STOP_RUNNING }

Error: Bleeding stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 37 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### BLEEDING_FAILED { #AC01_faults-BLEEDING_FAILED }

Error: Bleeding process failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 38 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_OFF { #AC01_faults-FILTER_NOT_OFF }

Error: Filter is not off, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 39 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### INVERTER_3P_NOT_RUNNING { #AC01_faults-INVERTER_3P_NOT_RUNNING }

Error: Three-phase inverter is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### INVERTER_3P_STOP_RUNNING { #AC01_faults-INVERTER_3P_STOP_RUNNING }

Error: Three-phase inverter stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 41 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |


<a id="AC01_warning"></a>
## AC01_warning { #AC01_warning }


| * | * |
|---|---|
| **Frame ID** | 0x810043 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

AC01 warning flags, it need to be cleared to &quot;Enable&quot; the power converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| grid_not_supported | 1 | Label set |
| grid_not_existing | 1 | Label set |
| grid_selection_wrong | 1 | Label set |
| reserved_3 | 1 | Label set |
| V_SET_DC_BELOW_AC | 1 | Label set |
| V_DC_BELOW_AC | 1 | Label set |
| AFE_DROOP_NOT_ENABLE | 1 | Label set |
| MODE_NOT_SUPPORTED | 1 | Label set |
| V_A_LOW | 1 | Label set |
| V_A_HIGH | 1 | Label set |
| V_B_LOW | 1 | Label set |
| V_B_HIGH | 1 | Label set |

### Payload description

#### grid_not_supported { #AC01_warning-grid_not_supported }

Warning: Grid is not supported

          3-Phase 230V (line-to-neutral) / 400V (line-to-line), 50Hz
          3-Phase 277V (line-to-neutral) / 480V (line-to-line), 60Hz
          3-Phase 120V (line-to-neutral) / 208V (line-to-line), 60Hz

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### grid_not_existing { #AC01_warning-grid_not_existing }

Warning: The converter is not connected to existing grid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### grid_selection_wrong { #AC01_warning-grid_selection_wrong }

Warning: grid selection is wrong

            converter see an existing grid and the selected grid mode is different

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### reserved_3 { #AC01_warning-reserved_3 }

reserved

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_SET_DC_BELOW_AC { #AC01_warning-V_SET_DC_BELOW_AC }

Warning: DC voltage setpoint is lower than the measured AC voltage

              It needs to follow this equation::
                    Vset DC &gt; VAC rms * sqrt(2) * 2 + 20

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_DC_BELOW_AC { #AC01_warning-V_DC_BELOW_AC }

Warning: DC voltage measured is too low to generate AC voltage

              It needs to follow this equation::
                    Vset DC &gt; VAC rms * sqrt(2) * 2 + 20

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### AFE_DROOP_NOT_ENABLE { #AC01_warning-AFE_DROOP_NOT_ENABLE }

Warning: AFE droop control is disabled but expected to be enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### MODE_NOT_SUPPORTED { #AC01_warning-MODE_NOT_SUPPORTED }

Warning: The selected operating mode is not supported

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_LOW { #AC01_warning-V_A_LOW }

Warning: Port A voltage is below the minimum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_HIGH { #AC01_warning-V_A_HIGH }

Warning: Port A voltage exceeds the maximum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_B_LOW { #AC01_warning-V_B_LOW }

Warning: Port A voltage is below the minimum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_B_HIGH { #AC01_warning-V_B_HIGH }

Warning: Port A voltage exceeds the maximum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |


<a id="AC01_info"></a>
## AC01_info { #AC01_info }


| * | * |
|---|---|
| **Frame ID** | 0x810044 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Info: Informational status and operating conditions

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| BLEEDING_DONE | 1 | Label set |
| CURRENT_LIMIT | 1 | Label set |
| CURRENT_LIMITED_BY_POWER | 1 | Label set |
| VB_LIMITED_BY_VA | 1 | Label set |

### Payload description

#### BLEEDING_DONE { #AC01_info-BLEEDING_DONE }

Info: Bleeding process completed successfully

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CURRENT_LIMIT { #AC01_info-CURRENT_LIMIT }

Info: Current limit has been reached

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CURRENT_LIMITED_BY_POWER { #AC01_info-CURRENT_LIMITED_BY_POWER }

Info: Output current is limited because the maximum power is reached

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### VB_LIMITED_BY_VA { #AC01_info-VB_LIMITED_BY_VA }

Info: Output voltage VB is limited because input voltage VA is insufficient

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |


<a id="Stack_Control"></a>
## Stack_Control { #Stack_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Device stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| reserved | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Stack_position { #Stack_Control-Stack_position }

Device position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### reserved { #Stack_Control-reserved }

reserved

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### SN_number { #Stack_Control-SN_number }

Unique device serial number, that require change of stack address

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="Fault_Control"></a>
## Fault_Control { #Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810050 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Fault Control: actions to clear faults and reset the system

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Clear_Interlock | 1 | Single bit |
| Reset_Processor | 1 | Single bit |
| Trip_Interlock | 1 | Single bit |
| Reserved | 5 | Unsigned |

### Payload description

#### Clear_Interlock { #Fault_Control-Clear_Interlock }

Clears the device interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor { #Fault_Control-Reset_Processor }

Reset the device DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock { #Fault_Control-Trip_Interlock }

Trip the internal Interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reserved { #Fault_Control-Reserved }

Reserved

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 5 | Unsigned |  | 1 | 0 |  | 31 |


<a id="_Factory_Config"></a>
## _Factory_Config { #_Factory_Config }


| * | * |
|---|---|
| **Frame ID** | 0x810060 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FACTORY USE ONLY - Factory configuration (requires factory mode)

                    Should only be used in factory, not customers. In case of issues, contact Advantics support.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| select | 8 | Label set |
| set_id | 8 | Unsigned |
| set_revision | 8 | Unsigned |
| set_variant | 8 | Unsigned |

### Payload description

#### select { #_Factory_Config-select }

set ID (will apply setted revision and variant as well)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| cs | 1 |
| adb | 2 |
| reset | 3 |

#### set_id { #_Factory_Config-set_id }

set ID, need factory mode = 1 (will change revision and variant as well)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### set_revision { #_Factory_Config-set_revision }

set revision, need factory mode = 1 , applied if set_id is valid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### set_variant { #_Factory_Config-set_variant }

set variant, need factory mode = 1, applied if set_id is valid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Factory_Control"></a>
## Factory_Control { #Factory_Control }


| * | * |
|---|---|
| **Frame ID** | 0x810061 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FACTORY USE ONLY - Control the device factory flags

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Factory_mode | 1 | Single bit |

### Payload description

#### Factory_mode { #Factory_Control-Factory_mode }

If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_Calibration_writing"></a>
## _Calibration_writing { #_Calibration_writing }


| * | * |
|---|---|
| **Frame ID** | 0x810062 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FACTORY USE ONLY - Calibration control (requires factory mode)

                    Should only be used in factory, not customers. For calibration issues, contact Advantics support.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index | 8 | Label set |
| select | 8 | Label set |
| value | 32 | Signed |

### Payload description

#### index { #_Calibration_writing-index }

index of the device that nee calibration (0 is invalid)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| voltage_sensor_b | 1 |

#### select { #_Calibration_writing-select }

select what value to set

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| prob_offset | 1 |
| prob_scale_factor | 2 |

#### value { #_Calibration_writing-value }

require calibration value

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Signed |  | 0.0001 | 0 | -214748.3648 | 214748.3647 |


<a id="_Calibration_reading_cmd"></a>
## _Calibration_reading_cmd { #_Calibration_reading_cmd }


| * | * |
|---|---|
| **Frame ID** | 0x810063 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FACTORY USE ONLY - Calibration reading cmd (requires factory mode)

                Should only be used in factory, not customers. For calibration issues, contact Advantics support.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index | 8 | Label set |
| select | 8 | Label set |

### Payload description

#### index { #_Calibration_reading_cmd-index }

index of the device that need reading

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| voltage_sensor_b | 1 |

#### select { #_Calibration_reading_cmd-select }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| raw | 0 |
| value | 1 |
| prob_offset | 2 |
| prob_scale_factor | 3 |


<a id="_Calibration_reading"></a>
## _Calibration_reading { #_Calibration_reading }


| * | * |
|---|---|
| **Frame ID** | 0x810064 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

FACTORY USE ONLY - Calibration reading (requires factory mode)

                Should only be used in factory, not customers. For calibration issues, contact Advantics support

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index | 8 | Label set |
| select | 8 | Label set |
| calibration_status | 1 | Label set |
| reserved | 7 | Unsigned |
| value | 32 | Signed |

### Payload description

#### index { #_Calibration_reading-index }

index of the device that need reading

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| unvalid | 0 |
| voltage_sensor_b | 1 |

#### select { #_Calibration_reading-select }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| raw | 0 |
| value | 1 |
| prob_offset | 2 |
| prob_scale_factor | 3 |

#### calibration_status { #_Calibration_reading-calibration_status }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| bad | 0 |
| ok | 1 |

#### reserved { #_Calibration_reading-reserved }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 7 | Unsigned |  | 1 | 0 |  | 127 |

#### value { #_Calibration_reading-value }

require calibration valut

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 32 | Signed |  | 0.0001 | 0 | -214748.3648 | 214748.3647 |


<a id="_Factory_Debug_cmd"></a>
## _Factory_Debug_cmd { #_Factory_Debug_cmd }


| * | * |
|---|---|
| **Frame ID** | 0x810065 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FACTORY USE ONLY - Factory debug command (requires factory mode)

                    Should only be used in factory, not customers. In case of issues, contact Advantics support.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| god_mode | 1 | Single bit |
| internal_power_a | 1 | Label set |
| internal_power_b | 1 | Label set |
| offset_stack_internal | 8 | Unsigned |

### Payload description

#### god_mode { #_Factory_Debug_cmd-god_mode }

If set to 1, module will enter in god mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### internal_power_a { #_Factory_Debug_cmd-internal_power_a }

If set to 1, ADM-PC on side A will be turned off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| on | 0 |
| off | 1 |

#### internal_power_b { #_Factory_Debug_cmd-internal_power_b }

If set to 1, ADM-PC on side B will be turned off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| on | 0 |
| off | 1 |

#### offset_stack_internal { #_Factory_Debug_cmd-offset_stack_internal }

Allow to generate a virtual offset in the stack address for internal ADM-PC

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | offset | 1 | 0 |  | 255 |


<a id="info_adm_cs"></a>
## info_adm_cs { #info_adm_cs }


| * | * |
|---|---|
| **Frame ID** | 0x810080 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about the ADM-CS (controller).

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| reserved | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_cs-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| GC01 | 16 |

#### Revision { #info_adm_cs-Revision }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_cs-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### reserved { #info_adm_cs-reserved }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_cs-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc"></a>
## info_adm_pc { #info_adm_pc }


| * | * |
|---|---|
| **Frame ID** | 0x810081 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| nb_detected | 8 | Unsigned |
| nd_side_a | 8 | Unsigned |
| nd_side_b | 8 | Unsigned |
| Collision | 8 | Unsigned |

### Payload description

#### nb_detected { #info_adm_pc-nb_detected }

number of ADM-PC detected

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### nd_side_a { #info_adm_pc-nd_side_a }

number of ADM-PC detected

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### nd_side_b { #info_adm_pc-nd_side_b }

number of ADM-PC detected

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Collision { #info_adm_pc-Collision }

collision between module

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="info_adm_pc_id_1"></a>
## info_adm_pc_id_1 { #info_adm_pc_id_1 }


| * | * |
|---|---|
| **Frame ID** | 0x810082 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #1.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_1-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_1-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_1-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_1-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_1-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_2"></a>
## info_adm_pc_id_2 { #info_adm_pc_id_2 }


| * | * |
|---|---|
| **Frame ID** | 0x810083 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #2.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_2-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_2-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_2-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_2-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_2-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_3"></a>
## info_adm_pc_id_3 { #info_adm_pc_id_3 }


| * | * |
|---|---|
| **Frame ID** | 0x810084 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #3.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_3-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_3-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_3-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_3-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_3-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_4"></a>
## info_adm_pc_id_4 { #info_adm_pc_id_4 }


| * | * |
|---|---|
| **Frame ID** | 0x810085 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #4.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_4-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_4-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_4-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_4-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_4-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_5"></a>
## info_adm_pc_id_5 { #info_adm_pc_id_5 }


| * | * |
|---|---|
| **Frame ID** | 0x810086 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #5.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_5-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_5-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_5-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_5-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_5-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_6"></a>
## info_adm_pc_id_6 { #info_adm_pc_id_6 }


| * | * |
|---|---|
| **Frame ID** | 0x810087 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains information about detected ADM-PC #6.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Unsigned |
| Variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #info_adm_pc_id_6-Type }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision { #info_adm_pc_id_6-Revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant { #info_adm_pc_id_6-Variant }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position { #info_adm_pc_id_6-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number { #info_adm_pc_id_6-serial_number }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_status_1"></a>
## info_adm_pc_status_1 { #info_adm_pc_status_1 }


| * | * |
|---|---|
| **Frame ID** | 0x810088 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #1.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_1-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_1-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_1-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_1-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_1-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_1-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_2"></a>
## info_adm_pc_status_2 { #info_adm_pc_status_2 }


| * | * |
|---|---|
| **Frame ID** | 0x810089 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #2.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_2-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_2-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_2-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_2-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_2-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_2-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_3"></a>
## info_adm_pc_status_3 { #info_adm_pc_status_3 }


| * | * |
|---|---|
| **Frame ID** | 0x81008a |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #3.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_3-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_3-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_3-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_3-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_3-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_3-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_4"></a>
## info_adm_pc_status_4 { #info_adm_pc_status_4 }


| * | * |
|---|---|
| **Frame ID** | 0x81008b |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #4.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_4-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_4-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_4-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_4-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_4-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_4-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_5"></a>
## info_adm_pc_status_5 { #info_adm_pc_status_5 }


| * | * |
|---|---|
| **Frame ID** | 0x81008c |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #5.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_5-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_5-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_5-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_5-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_5-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_5-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_6"></a>
## info_adm_pc_status_6 { #info_adm_pc_status_6 }


| * | * |
|---|---|
| **Frame ID** | 0x81008d |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG/FACTORY USE ONLY - Not important for customers.

                    Contains status information about detected ADM-PC #6.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available | 1 | Single bit |
| Side | 2 | Label set |
| Status | 2 | Label set |
| Interlock_I | 1 | Single bit |
| Interlock_E | 1 | Single bit |
| mode | 16 | Unsigned |

### Payload description

#### Available { #info_adm_pc_status_6-Available }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side { #info_adm_pc_status_6-Side }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status { #info_adm_pc_status_6-Status }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I { #info_adm_pc_status_6-Interlock_I }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E { #info_adm_pc_status_6-Interlock_E }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode { #info_adm_pc_status_6-mode }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="cs_performance"></a>
## cs_performance { #cs_performance }


| * | * |
|---|---|
| **Frame ID** | 0x810090 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Performance status of the AMD-CS

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| cpu_1_usage | 8 | Unsigned |
| cpu_2_usage | 8 | Unsigned |
| can_bus_load_A | 8 | Unsigned |
| can_bus_load_B | 8 | Unsigned |
| main_loop_freq | 16 | Unsigned |

### Payload description

#### cpu_1_usage { #cs_performance-cpu_1_usage }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### cpu_2_usage { #cs_performance-cpu_2_usage }

Controller cpu 2 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### can_bus_load_A { #cs_performance-can_bus_load_A }

Controller cup 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### can_bus_load_B { #cs_performance-can_bus_load_B }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### main_loop_freq { #cs_performance-main_loop_freq }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Hz | 1 | 0 |  | 65535 |


<a id="info_can_api_error"></a>
## info_can_api_error { #info_can_api_error }


| * | * |
|---|---|
| **Frame ID** | 0x810091 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

DEBUG - Allow to know  what ADM-PC has wrong can api

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Stack_position | 8 | Unsigned |
| Major_expected | 8 | Unsigned |
| Minor_expected | 8 | Unsigned |
| Patch_expected | 8 | Unsigned |
| Major_actual | 8 | Unsigned |
| Minor_actual | 8 | Unsigned |
| Patch_actual | 8 | Unsigned |

### Payload description

#### Type { #info_can_api_error-Type }

The ADM-PC identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Stack_position { #info_can_api_error-Stack_position }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Major_expected { #info_can_api_error-Major_expected }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor_expected { #info_can_api_error-Minor_expected }

The minor version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch_expected { #info_can_api_error-Patch_expected }

The patch version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Major_actual { #info_can_api_error-Major_actual }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor_actual { #info_can_api_error-Minor_actual }

The minor version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch_actual { #info_can_api_error-Patch_actual }

The patch version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="_fms_state"></a>
## _fms_state { #_fms_state }


| * | * |
|---|---|
| **Frame ID** | 0x8100f0 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

FSM  status - DEBUG ONLY, not for customer visibility

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| init | 8 | Unsigned |
| ready | 8 | Unsigned |
| turned_on | 8 | Unsigned |
| turned_off | 8 | Unsigned |
| bleeding | 8 | Unsigned |

### Payload description

#### init { #_fms_state-init }

state: INIT (initialization phase)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### ready { #_fms_state-ready }

state: READY

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### turned_on { #_fms_state-turned_on }

state: TURNED_ON

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### turned_off { #_fms_state-turned_off }

state: TURNED_OFF

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### bleeding { #_fms_state-bleeding }

state: BLEEDING

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="_interlocks_status"></a>
## _interlocks_status { #_interlocks_status }


| * | * |
|---|---|
| **Frame ID** | 0x8100f1 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

INTERNAL DEBUG ONLY - Customer systems should NOT monitor or display this message

                    Split power converter interlock status

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| e | 1 | Label set |
| a | 1 | Label set |
| b | 1 | Label set |
| i | 1 | Label set |
| x | 1 | Label set |

### Payload description

#### e { #_interlocks_status-e }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### a { #_interlocks_status-a }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### b { #_interlocks_status-b }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### i { #_interlocks_status-i }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### x { #_interlocks_status-x }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |
