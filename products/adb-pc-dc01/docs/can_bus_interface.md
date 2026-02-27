# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [Identification_0_BASE](#Identification_0_BASE) | 0x820000 | 8 | IN |  |
| [Bootloader_UID_0_BASE](#Bootloader_UID_0_BASE) | 0x820001 | 8 | IN |  |
| [Firmware_UID_0_BASE](#Firmware_UID_0_BASE) | 0x820002 | 8 | IN |  |
| [ADB_CAN_API_Version_0_BASE](#ADB_CAN_API_Version_0_BASE) | 0x820003 | 3 | IN |  |
| [Status_0__BOX](#Status_0__BOX) | 0x820010 | 8 | IN |  |
| [Faults_0__BOX](#Faults_0__BOX) | 0x820011 | 8 | IN |  |
| [Converter_Control_0__BOX](#Converter_Control_0__BOX) | 0x820012 | 1 | IN |  |
| [Converter_Power_Info_0__BOX](#Converter_Power_Info_0__BOX) | 0x820013 | 6 | IN |  |
| [Broadcast_Group_Control_0__BOX](#Broadcast_Group_Control_0__BOX) | 0x820014 | 1 | IN |  |
| [Interface_Status_0__BOX](#Interface_Status_0__BOX) | 0x820015 | 3 | IN |  |
| [Keep_Alive_Control_0__BOX](#Keep_Alive_Control_0__BOX) | 0x820016 | 2 | IN |  |
| [Converter_Temperature_0__BOX](#Converter_Temperature_0__BOX) | 0x820017 | 8 | IN |  |
| [Converter_Fans_0__BOX](#Converter_Fans_0__BOX) | 0x820018 | 6 | IN |  |
| [Keep_Alive_Feed_0__BOX](#Keep_Alive_Feed_0__BOX) | 0x820019 | 1 | IN |  |
| [GC01_Analog_0_GC01](#GC01_Analog_0_GC01) | 0x820020 | 8 | IN |  |
| [FAN_Speed_Control_0_GC01](#FAN_Speed_Control_0_GC01) | 0x820022 | 1 | IN |  |
| [FAN_Enable_Control_0_GC01](#FAN_Enable_Control_0_GC01) | 0x820023 | 1 | IN |  |
| [GC01_cont_main_ctrl_0_GC01](#GC01_cont_main_ctrl_0_GC01) | 0x820024 | 1 | IN |  |
| [GC01_cont_main_status_0_GC01](#GC01_cont_main_status_0_GC01) | 0x820025 | 1 | IN |  |
| [GC01_cont_secondary_ctrl_0_GC01](#GC01_cont_secondary_ctrl_0_GC01) | 0x820026 | 1 | IN |  |
| [GC01_cont_secondary_status_0_GC01](#GC01_cont_secondary_status_0_GC01) | 0x820027 | 1 | IN |  |
| [contactors_cmd_0_GC01](#contactors_cmd_0_GC01) | 0x820028 | 1 | IN |  |
| [Stack_Control_0_BASE](#Stack_Control_0_BASE) | 0x820045 | 6 | IN |  |
| [Fault_Control_0_BASE](#Fault_Control_0_BASE) | 0x820050 | 1 | IN |  |
| [_Factory_Config_0__BOX](#_Factory_Config_0__BOX) | 0x820060 | 8 | IN |  |
| [Factory_Control_0_BASE](#Factory_Control_0_BASE) | 0x820061 | 8 | IN |  |
| [_Calibration_writing_0__BOX](#_Calibration_writing_0__BOX) | 0x820062 | 6 | IN |  |
| [_Calibration_reading_cmd_0__BOX](#_Calibration_reading_cmd_0__BOX) | 0x820063 | 2 | IN |  |
| [_Calibration_reading_0__BOX](#_Calibration_reading_0__BOX) | 0x820064 | 8 | IN |  |
| [_Factory_Debug_cmd_0__BOX](#_Factory_Debug_cmd_0__BOX) | 0x820065 | 8 | IN |  |
| [info_adm_cs_0__BOX](#info_adm_cs_0__BOX) | 0x820080 | 8 | IN |  |
| [info_adm_pc_0__BOX](#info_adm_pc_0__BOX) | 0x820081 | 4 | IN |  |
| [info_adm_pc_id_1_0__BOX](#info_adm_pc_id_1_0__BOX) | 0x820082 | 8 | IN |  |
| [info_adm_pc_id_2_0__BOX](#info_adm_pc_id_2_0__BOX) | 0x820083 | 8 | IN |  |
| [info_adm_pc_id_3_0__BOX](#info_adm_pc_id_3_0__BOX) | 0x820084 | 8 | IN |  |
| [info_adm_pc_id_4_0__BOX](#info_adm_pc_id_4_0__BOX) | 0x820085 | 8 | IN |  |
| [info_adm_pc_id_5_0__BOX](#info_adm_pc_id_5_0__BOX) | 0x820086 | 8 | IN |  |
| [info_adm_pc_id_6_0__BOX](#info_adm_pc_id_6_0__BOX) | 0x820087 | 8 | IN |  |
| [info_adm_pc_status_1_0__BOX](#info_adm_pc_status_1_0__BOX) | 0x820088 | 8 | IN |  |
| [info_adm_pc_status_2_0__BOX](#info_adm_pc_status_2_0__BOX) | 0x820089 | 8 | IN |  |
| [info_adm_pc_status_3_0__BOX](#info_adm_pc_status_3_0__BOX) | 0x82008a | 8 | IN |  |
| [info_adm_pc_status_4_0__BOX](#info_adm_pc_status_4_0__BOX) | 0x82008b | 8 | IN |  |
| [info_adm_pc_status_5_0__BOX](#info_adm_pc_status_5_0__BOX) | 0x82008c | 8 | IN |  |
| [info_adm_pc_status_6_0__BOX](#info_adm_pc_status_6_0__BOX) | 0x82008d | 8 | IN |  |
| [cs_performance_0__BOX](#cs_performance_0__BOX) | 0x820090 | 8 | IN |  |
| [info_can_api_error_0__BOX](#info_can_api_error_0__BOX) | 0x820091 | 8 | IN |  |
| [_fms_state_0__BOX](#_fms_state_0__BOX) | 0x8200f0 | 8 | IN |  |
| [_interlocks_status_0__BOX](#_interlocks_status_0__BOX) | 0x8200f1 | 3 | IN |  |


<a id="Identification_0_BASE"></a>
## Identification_0_BASE { #Identification_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Identification of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0_BASE | 8 | Label set |
| Revision_0_BASE | 8 | Label set |
| Variant_0_BASE | 8 | Label set |
| Stack_position_0_BASE | 8 | Unsigned |
| serial_number_0_BASE | 32 | Unsigned |

### Payload description

#### Type_0_BASE { #Identification_0_BASE-Type_0_BASE }

The device identification field, uniquely identifies the sender in the network

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| GC01 | 128 |
| AC01 | 129 |
| DC01 | 130 |

#### Revision_0_BASE { #Identification_0_BASE-Revision_0_BASE }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| R0A | 0 |
| R0B | 1 |
| R0C | 2 |

#### Variant_0_BASE { #Identification_0_BASE-Variant_0_BASE }

The hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| VA00 | 0 |
| VA01 | 1 |

#### Stack_position_0_BASE { #Identification_0_BASE-Stack_position_0_BASE }

Position of the module within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0_BASE { #Identification_0_BASE-serial_number_0_BASE }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="Bootloader_UID_0_BASE"></a>
## Bootloader_UID_0_BASE { #Bootloader_UID_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Unique Identifier of the Bootloader used on this module

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID_0_BASE | 64 | Unsigned |

### Payload description

#### UID_0_BASE { #Bootloader_UID_0_BASE-UID_0_BASE }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  | 18446744073709549568 |


<a id="Firmware_UID_0_BASE"></a>
## Firmware_UID_0_BASE { #Firmware_UID_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820002 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Unique Identifier of the Firmware used on this module

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID_0_BASE | 64 | Unsigned |

### Payload description

#### UID_0_BASE { #Firmware_UID_0_BASE-UID_0_BASE }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  | 18446744073709549568 |


<a id="ADB_CAN_API_Version_0_BASE"></a>
## ADB_CAN_API_Version_0_BASE { #ADB_CAN_API_Version_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820003 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

This message declares the version of the API that is provided by the converter. The version follows newer convention, as this file is an API definition, patch does not apply

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Major_0_BASE | 8 | Unsigned |
| Minor_0_BASE | 8 | Unsigned |
| Patch_0_BASE | 8 | Unsigned |

### Payload description

#### Major_0_BASE { #ADB_CAN_API_Version_0_BASE-Major_0_BASE }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor_0_BASE { #ADB_CAN_API_Version_0_BASE-Minor_0_BASE }

The Minor version number. This number increases if there are backwards compatible changes, like new messages or the use of previously reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch_0_BASE { #ADB_CAN_API_Version_0_BASE-Patch_0_BASE }

The Patch number. This number increases when changes to descriptions and documentation/comments are made

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Status_0__BOX"></a>
## Status_0__BOX { #Status_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820010 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

General Status of the converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| State_0__BOX | 16 | Label set |
| flag_enable_0__BOX | 1 | Single bit |
| flag_ready_0__BOX | 1 | Single bit |
| flag_energized_0__BOX | 1 | Single bit |
| flag_busy_0__BOX | 1 | Single bit |
| flag_eco_0__BOX | 1 | Single bit |
| flag_warning_0__BOX | 1 | Single bit |
| flag_degraded_0__BOX | 1 | Single bit |
| flag_error_0__BOX | 1 | Single bit |
| flag_factory_0__BOX | 1 | Single bit |
| flag_god_mode_0__BOX | 1 | Single bit |

### Payload description

#### State_0__BOX { #Status_0__BOX-State_0__BOX }

box state

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

#### flag_enable_0__BOX { #Status_0__BOX-flag_enable_0__BOX }

flag to know if the system is Enable

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_ready_0__BOX { #Status_0__BOX-flag_ready_0__BOX }

box has receive correct set point and can be turned one

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_energized_0__BOX { #Status_0__BOX-flag_energized_0__BOX }

the box is energized

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_busy_0__BOX { #Status_0__BOX-flag_busy_0__BOX }

box is busy

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_eco_0__BOX { #Status_0__BOX-flag_eco_0__BOX }

box is in eco mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_warning_0__BOX { #Status_0__BOX-flag_warning_0__BOX }

box has warning and might be in degraded mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_degraded_0__BOX { #Status_0__BOX-flag_degraded_0__BOX }

box function in degraded mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_error_0__BOX { #Status_0__BOX-flag_error_0__BOX }

box has error those need to ble cleared to allow operation

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_factory_0__BOX { #Status_0__BOX-flag_factory_0__BOX }

box function in factory mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 1 | Single bit |  | 1 | 0 |  |  |

#### flag_god_mode_0__BOX { #Status_0__BOX-flag_god_mode_0__BOX }

box function in degraded mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 49 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Faults_0__BOX"></a>
## Faults_0__BOX { #Faults_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| internal_0__BOX | 1 | Label set |
| external_0__BOX | 1 | Label set |
| system_0__BOX | 1 | Label set |
| EEPROM_failure_0__BOX | 1 | Label set |
| wrong_nfo_0__BOX | 1 | Label set |
| Measurement_system_failure_0__BOX | 1 | Label set |
| PLL_not_locked_0__BOX | 1 | Label set |
| overtemperature_0__BOX | 1 | Label set |
| fan_stuck_0__BOX | 1 | Label set |
| dead_module_0__BOX | 1 | Label set |
| keep_alive_not_serv_internal_0__BOX | 1 | Label set |
| error_temperature_0__BOX | 1 | Label set |
| internal_modules_ready_0__BOX | 1 | Label set |
| internal_modules_can_api_0__BOX | 1 | Label set |
| internal_modules_missing_0__BOX | 1 | Label set |
| internal_modules_wrong_0__BOX | 1 | Label set |
| internal_modules_stack_0__BOX | 1 | Label set |
| internal_modules_init_0__BOX | 1 | Label set |
| wrong_revision_0__BOX | 1 | Label set |
| v_in_low_0__BOX | 1 | Label set |
| v_in_critical_0__BOX | 1 | Label set |
| keep_alive_not_serv_0__BOX | 1 | Label set |

### Payload description

#### internal_0__BOX { #Faults_0__BOX-internal_0__BOX }

This g is asserted if the interlock is open due to an internal fault condition (self-protection)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Tripped | 1 |

#### external_0__BOX { #Faults_0__BOX-external_0__BOX }

This flag is asserted if the interlock is open due to an external condition received in the module.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Tripped | 1 |

#### system_0__BOX { #Faults_0__BOX-system_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### EEPROM_failure_0__BOX { #Faults_0__BOX-EEPROM_failure_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### wrong_nfo_0__BOX { #Faults_0__BOX-wrong_nfo_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### Measurement_system_failure_0__BOX { #Faults_0__BOX-Measurement_system_failure_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### PLL_not_locked_0__BOX { #Faults_0__BOX-PLL_not_locked_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### overtemperature_0__BOX { #Faults_0__BOX-overtemperature_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### fan_stuck_0__BOX { #Faults_0__BOX-fan_stuck_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### dead_module_0__BOX { #Faults_0__BOX-dead_module_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### keep_alive_not_serv_internal_0__BOX { #Faults_0__BOX-keep_alive_not_serv_internal_0__BOX }

keep alive internal not served

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### error_temperature_0__BOX { #Faults_0__BOX-error_temperature_0__BOX }

trigger when a temperature has an errror

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### internal_modules_ready_0__BOX { #Faults_0__BOX-internal_modules_ready_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### internal_modules_can_api_0__BOX { #Faults_0__BOX-internal_modules_can_api_0__BOX }

internal module wrong API

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_missing_0__BOX { #Faults_0__BOX-internal_modules_missing_0__BOX }

internal modules missing

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_wrong_0__BOX { #Faults_0__BOX-internal_modules_wrong_0__BOX }

internal modules wrong

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_stack_0__BOX { #Faults_0__BOX-internal_modules_stack_0__BOX }

internal modules stack error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### internal_modules_init_0__BOX { #Faults_0__BOX-internal_modules_init_0__BOX }

internal module failed init

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### wrong_revision_0__BOX { #Faults_0__BOX-wrong_revision_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### v_in_low_0__BOX { #Faults_0__BOX-v_in_low_0__BOX }

24v input too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### v_in_critical_0__BOX { #Faults_0__BOX-v_in_critical_0__BOX }

24v input too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### keep_alive_not_serv_0__BOX { #Faults_0__BOX-keep_alive_not_serv_0__BOX }

keep alive not served

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |


<a id="Converter_Control_0__BOX"></a>
## Converter_Control_0__BOX { #Converter_Control_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820012 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

box commands

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| enable_0__BOX | 1 | Single bit |

### Payload description

#### enable_0__BOX { #Converter_Control_0__BOX-enable_0__BOX }

Enable the system

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Converter_Power_Info_0__BOX"></a>
## Converter_Power_Info_0__BOX { #Converter_Power_Info_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820013 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Converter power info

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| load_0__BOX | 8 | Unsigned |
| efficiency_0__BOX | 8 | Unsigned |
| Power_capability_0__BOX | 16 | Signed |
| low_power_input_0__BOX | 16 | Signed |

### Payload description

#### load_0__BOX { #Converter_Power_Info_0__BOX-load_0__BOX }

load in percent

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### efficiency_0__BOX { #Converter_Power_Info_0__BOX-efficiency_0__BOX }

load in percent

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### Power_capability_0__BOX { #Converter_Power_Info_0__BOX-Power_capability_0__BOX }

Power capabilities in kw

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | kw | 0.1 | 0 | -3276.8 | 3276.7 |

#### low_power_input_0__BOX { #Converter_Power_Info_0__BOX-low_power_input_0__BOX }

low power iunput voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | v | 0.01 | 0 | -327.68 | 327.67 |


<a id="Broadcast_Group_Control_0__BOX"></a>
## Broadcast_Group_Control_0__BOX { #Broadcast_Group_Control_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820014 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure the broadcast group that the module belongs to.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID_0__BOX | 8 | Unsigned |

### Payload description

#### Group_ID_0__BOX { #Broadcast_Group_Control_0__BOX-Group_ID_0__BOX }

Broadcast Group that the module should monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Interface_Status_0__BOX"></a>
## Interface_Status_0__BOX { #Interface_Status_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820015 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

interface status

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Broadcast_Group_0__BOX | 8 | Unsigned |
| keep_Alive_0__BOX | 4 | Label set |
| reserved_0__BOX | 4 | Label set |
| keep_Alive_Period_0__BOX | 8 | Unsigned |

### Payload description

#### Broadcast_Group_0__BOX { #Interface_Status_0__BOX-Broadcast_Group_0__BOX }

The broadcast group that the module belongs to. Broadcast group 0 implies that the module is not part of a broadcast group.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 30 |

#### keep_Alive_0__BOX { #Interface_Status_0__BOX-keep_Alive_0__BOX }

keep alive requires the supervisory controller to send a heartbeat message at regular intervals

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 4 | Label set |  | 1 | 0 |  | 15 |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### reserved_0__BOX { #Interface_Status_0__BOX-reserved_0__BOX }

If this signal and the &#x27;keep alive&#x27; is enabled, violating the heartbeat will trip the interlock, shutting down all connected power converters

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 4 | Label set |  | 1 | 0 |  | 15 |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### keep_Alive_Period_0__BOX { #Interface_Status_0__BOX-keep_Alive_Period_0__BOX }

The maximum period of the keep alive message. If the time between two heart-beat messages is longer than this value, the module ceases operation. This only applies when the Heartbeat signal is Enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | s | 0.1 | 0 |  | 25.5 |


<a id="Keep_Alive_Control_0__BOX"></a>
## Keep_Alive_Control_0__BOX { #Keep_Alive_Control_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820016 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure the Heartbeat for the Module. The &#x27;Trip interlock&#x27; and &#x27;Heartbeat Period&#x27; only apply if the heartbeat signals are enabled

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Enable_0__BOX | 1 | Label set |
| reserved_0__BOX | 1 | Label set |
| Period_0__BOX | 8 | Unsigned |

### Payload description

#### Enable_0__BOX { #Keep_Alive_Control_0__BOX-Enable_0__BOX }

Enable/Disable the Heartbeat feature of the Module

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### reserved_0__BOX { #Keep_Alive_Control_0__BOX-reserved_0__BOX }

Set if the external interlock should be tripped if a heartbeat is not received within the configured period. If this signal is enabled the interlock is triped and the module is disabled. If this signal is set to Disabled, the interlock like will not be tripped but the module will cease operation

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Period_0__BOX { #Keep_Alive_Control_0__BOX-Period_0__BOX }

Set the maximum period of the Heartbeat message. If the time between two heart-beat messages is longer than this value, the module ceases operation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | s | 0.1 | 0 |  | 25.5 |


<a id="Converter_Temperature_0__BOX"></a>
## Converter_Temperature_0__BOX { #Converter_Temperature_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820017 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Readouts of the converter temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Cooling_plate_0__BOX | 16 | Signed |
| Magnetics_0__BOX | 16 | Signed |
| Transistors_0__BOX | 16 | Signed |
| RESERVED_0__BOX | 16 | Signed |

### Payload description

#### Cooling_plate_0__BOX { #Converter_Temperature_0__BOX-Cooling_plate_0__BOX }

Temperature of the cooling plate

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### Magnetics_0__BOX { #Converter_Temperature_0__BOX-Magnetics_0__BOX }

Highest mesured temp of magnetics

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### Transistors_0__BOX { #Converter_Temperature_0__BOX-Transistors_0__BOX }

Highest mesured temp of transistors

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### RESERVED_0__BOX { #Converter_Temperature_0__BOX-RESERVED_0__BOX }

Lowest measured temp internally

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |


<a id="Converter_Fans_0__BOX"></a>
## Converter_Fans_0__BOX { #Converter_Fans_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820018 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Readouts of the converter fans

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| A_rpm_0__BOX | 16 | Unsigned |
| A_pwm_0__BOX | 8 | Unsigned |
| B_rpm_0__BOX | 16 | Unsigned |
| B_pwm_0__BOX | 8 | Unsigned |

### Payload description

#### A_rpm_0__BOX { #Converter_Fans_0__BOX-A_rpm_0__BOX }

Measured speed of Fan 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | rpm | 1 | 0 |  | 65535 |

#### A_pwm_0__BOX { #Converter_Fans_0__BOX-A_pwm_0__BOX }

Fan speed in percentage (0 to 100%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### B_rpm_0__BOX { #Converter_Fans_0__BOX-B_rpm_0__BOX }

Measured speed of Fan 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Unsigned | rpm | 1 | 0 |  | 65535 |

#### B_pwm_0__BOX { #Converter_Fans_0__BOX-B_pwm_0__BOX }

Fan speed in percentage (0 to 100%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | % | 1 | 0 |  | 255 |


<a id="Keep_Alive_Feed_0__BOX"></a>
## Keep_Alive_Feed_0__BOX { #Keep_Alive_Feed_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820019 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

keep alive feeding

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| feed_0__BOX | 1 | Single bit |

### Payload description

#### feed_0__BOX { #Keep_Alive_Feed_0__BOX-feed_0__BOX }

the value don&#x27;t matter her tin order to feed the alive

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="GC01_Analog_0_GC01"></a>
## GC01_Analog_0_GC01 { #GC01_Analog_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820020 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Readouts of the module temperature sensor

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Temp_NTC_A_0_GC01 | 16 | Signed |
| v_in_0_GC01 | 16 | Signed |
| Voltage_prob_b_0_GC01 | 16 | Unsigned |
| Voltage_prob_b_raw_0_GC01 | 16 | Unsigned |

### Payload description

#### Temp_NTC_A_0_GC01 { #GC01_Analog_0_GC01-Temp_NTC_A_0_GC01 }

Temperature of the inductor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 | -327.68 | 327.67 |

#### v_in_0_GC01 { #GC01_Analog_0_GC01-v_in_0_GC01 }

Temperature of the inductor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 | -3276.8 | 3276.7 |

#### Voltage_prob_b_0_GC01 { #GC01_Analog_0_GC01-Voltage_prob_b_0_GC01 }

Temperature of the inductor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  | 6553.5 |

#### Voltage_prob_b_raw_0_GC01 { #GC01_Analog_0_GC01-Voltage_prob_b_raw_0_GC01 }

Temperature of the inductor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned | V | 1 | 0 |  | 65535 |


<a id="FAN_Speed_Control_0_GC01"></a>
## FAN_Speed_Control_0_GC01 { #FAN_Speed_Control_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820022 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Manual control of fan speed pwm (for debug)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| FAN1_speed_0_GC01 | 8 | Unsigned |

### Payload description

#### FAN1_speed_0_GC01 { #FAN_Speed_Control_0_GC01-FAN1_speed_0_GC01 }

Fan speed in percentage (0 to 100%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="FAN_Enable_Control_0_GC01"></a>
## FAN_Enable_Control_0_GC01 { #FAN_Enable_Control_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820023 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Manual control of enable/disable (for debug)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| FAN1_enable_0_GC01 | 1 | Single bit |

### Payload description

#### FAN1_enable_0_GC01 { #FAN_Enable_Control_0_GC01-FAN1_enable_0_GC01 }

Fan enable/disable

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="GC01_cont_main_ctrl_0_GC01"></a>
## GC01_cont_main_ctrl_0_GC01 { #GC01_cont_main_ctrl_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820024 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Control: contactors 1 and 2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| pwr_enable_0_GC01 | 1 | Single bit |
| not_eco_0_GC01 | 1 | Single bit |
| cont_1_2_en_0_GC01 | 1 | Single bit |
| cont_1_close_0_GC01 | 1 | Single bit |
| cont_2_close_0_GC01 | 1 | Single bit |

### Payload description

#### pwr_enable_0_GC01 { #GC01_cont_main_ctrl_0_GC01-pwr_enable_0_GC01 }

enable power to contactors

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### not_eco_0_GC01 { #GC01_cont_main_ctrl_0_GC01-not_eco_0_GC01 }

economised mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### cont_1_2_en_0_GC01 { #GC01_cont_main_ctrl_0_GC01-cont_1_2_en_0_GC01 }

enable cont 1 and 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### cont_1_close_0_GC01 { #GC01_cont_main_ctrl_0_GC01-cont_1_close_0_GC01 }

close cont 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### cont_2_close_0_GC01 { #GC01_cont_main_ctrl_0_GC01-cont_2_close_0_GC01 }

close cont 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="GC01_cont_main_status_0_GC01"></a>
## GC01_cont_main_status_0_GC01 { #GC01_cont_main_status_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820025 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

status of contactors 1 and 2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| cont_1_good_0_GC01 | 1 | Label set |
| cont_2_good_0_GC01 | 1 | Label set |
| cont_1_aux_0_GC01 | 1 | Label set |
| cont_2_aux_0_GC01 | 1 | Label set |

### Payload description

#### cont_1_good_0_GC01 { #GC01_cont_main_status_0_GC01-cont_1_good_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 0 |
| good | 1 |

#### cont_2_good_0_GC01 { #GC01_cont_main_status_0_GC01-cont_2_good_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 0 |
| good | 1 |

#### cont_1_aux_0_GC01 { #GC01_cont_main_status_0_GC01-cont_1_aux_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| open | 0 |
| closed | 1 |

#### cont_2_aux_0_GC01 { #GC01_cont_main_status_0_GC01-cont_2_aux_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| open | 0 |
| closed | 1 |


<a id="GC01_cont_secondary_ctrl_0_GC01"></a>
## GC01_cont_secondary_ctrl_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820026 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Control: contactors 3 and 4

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| pwr_enable_0_GC01 | 1 | Single bit |
| not_eco_0_GC01 | 1 | Single bit |
| reserved_0_GC01 | 1 | Single bit |
| cont_3_ctrl_0_GC01 | 1 | Single bit |
| cont_4_ctrl_0_GC01 | 1 | Single bit |

### Payload description

#### pwr_enable_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01-pwr_enable_0_GC01 }

enable power to contactors

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### not_eco_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01-not_eco_0_GC01 }

economised mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### reserved_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01-reserved_0_GC01 }

economised mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### cont_3_ctrl_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01-cont_3_ctrl_0_GC01 }

close cont 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### cont_4_ctrl_0_GC01 { #GC01_cont_secondary_ctrl_0_GC01-cont_4_ctrl_0_GC01 }

close cont 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="GC01_cont_secondary_status_0_GC01"></a>
## GC01_cont_secondary_status_0_GC01 { #GC01_cont_secondary_status_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820027 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

status of contactors 1 and 2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| cont_3_aux_0_GC01 | 1 | Label set |
| cont_4_aux_0_GC01 | 1 | Label set |

### Payload description

#### cont_3_aux_0_GC01 { #GC01_cont_secondary_status_0_GC01-cont_3_aux_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| open | 0 |
| closed | 1 |

#### cont_4_aux_0_GC01 { #GC01_cont_secondary_status_0_GC01-cont_4_aux_0_GC01 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| open | 0 |
| closed | 1 |


<a id="contactors_cmd_0_GC01"></a>
## contactors_cmd_0_GC01 { #contactors_cmd_0_GC01 }


| * | * |
|---|---|
| **Frame ID** | 0x820028 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

status of contactors 1 and 2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| conf_0_GC01 | 8 | Label set |

### Payload description

#### conf_0_GC01 { #contactors_cmd_0_GC01-conf_0_GC01 }

Enable the systeme

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| open | 0 |
| dc01_serial | 1 |
| dc01_parallel | 2 |
| manual | 3 |


<a id="Stack_Control_0_BASE"></a>
## Stack_Control_0_BASE { #Stack_Control_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Module stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position_0_BASE | 8 | Unsigned |
| reserved_0_BASE | 8 | Unsigned |
| SN_number_0_BASE | 32 | Unsigned |

### Payload description

#### Stack_position_0_BASE { #Stack_Control_0_BASE-Stack_position_0_BASE }

The module position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### reserved_0_BASE { #Stack_Control_0_BASE-reserved_0_BASE }

was stack size before

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### SN_number_0_BASE { #Stack_Control_0_BASE-SN_number_0_BASE }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="Fault_Control_0_BASE"></a>
## Fault_Control_0_BASE { #Fault_Control_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820050 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Fault Control: actions to clear faults and reset the system

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Clear_Interlock_0_BASE | 1 | Single bit |
| Reset_Processor_0_BASE | 1 | Single bit |
| Trip_Interlock_0_BASE | 1 | Single bit |
| Reserved_0_BASE | 5 | Unsigned |

### Payload description

#### Clear_Interlock_0_BASE { #Fault_Control_0_BASE-Clear_Interlock_0_BASE }

Clears the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor_0_BASE { #Fault_Control_0_BASE-Reset_Processor_0_BASE }

Reset the converter DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock_0_BASE { #Fault_Control_0_BASE-Trip_Interlock_0_BASE }

Trip the inetrnal Interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reserved_0_BASE { #Fault_Control_0_BASE-Reserved_0_BASE }

Reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 5 | Unsigned |  | 1 | 0 |  | 31 |


<a id="_Factory_Config_0__BOX"></a>
## _Factory_Config_0__BOX { #_Factory_Config_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820060 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

factory setting of controller and boxs

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| select_0__BOX | 8 | Label set |
| set_id_0__BOX | 8 | Unsigned |
| set_revision_0__BOX | 8 | Unsigned |
| set_variant_0__BOX | 8 | Unsigned |

### Payload description

#### select_0__BOX { #_Factory_Config_0__BOX-select_0__BOX }

set ID, need factory mode = 1 (will change revision and variant as well)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| cs | 1 |
| adb | 2 |
| reset | 3 |

#### set_id_0__BOX { #_Factory_Config_0__BOX-set_id_0__BOX }

set ID, need factory mode = 1 (will change revision and variant as well)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### set_revision_0__BOX { #_Factory_Config_0__BOX-set_revision_0__BOX }

set revision, need factory mode = 1 , applied if set_id is valid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### set_variant_0__BOX { #_Factory_Config_0__BOX-set_variant_0__BOX }

set variant, need factory mode = 1, applied if set_id is valid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="Factory_Control_0_BASE"></a>
## Factory_Control_0_BASE { #Factory_Control_0_BASE }


| * | * |
|---|---|
| **Frame ID** | 0x820061 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Control the system flags

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Factory_mode_0_BASE | 1 | Single bit |

### Payload description

#### Factory_mode_0_BASE { #Factory_Control_0_BASE-Factory_mode_0_BASE }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_Calibration_writing_0__BOX"></a>
## _Calibration_writing_0__BOX { #_Calibration_writing_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820062 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Calibration control (factory mode need to be set)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index_0__BOX | 8 | Label set |
| select_0__BOX | 8 | Label set |
| value_0__BOX | 32 | Signed |

### Payload description

#### index_0__BOX { #_Calibration_writing_0__BOX-index_0__BOX }

index of the device that nee calibration (0 is unvalid)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| voltage_sensor_b | 1 |

#### select_0__BOX { #_Calibration_writing_0__BOX-select_0__BOX }

select what value to set

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| prob_offset | 1 |
| prob_scale_factor | 2 |

#### value_0__BOX { #_Calibration_writing_0__BOX-value_0__BOX }

require calibration valut

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Signed |  | 0.0001 | 0 | -214748.3648 | 214748.3647 |


<a id="_Calibration_reading_cmd_0__BOX"></a>
## _Calibration_reading_cmd_0__BOX { #_Calibration_reading_cmd_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820063 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Calibration reading cmd (factory mode need to be set)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index_0__BOX | 8 | Label set |
| select_0__BOX | 8 | Label set |

### Payload description

#### index_0__BOX { #_Calibration_reading_cmd_0__BOX-index_0__BOX }

index of the device that need reading

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| invalid | 0 |
| voltage_sensor_b | 1 |

#### select_0__BOX { #_Calibration_reading_cmd_0__BOX-select_0__BOX }

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


<a id="_Calibration_reading_0__BOX"></a>
## _Calibration_reading_0__BOX { #_Calibration_reading_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820064 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Calibration reading cmd (factory mode need to be set)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| index_0__BOX | 8 | Label set |
| select_0__BOX | 8 | Label set |
| calibration_status_0__BOX | 1 | Label set |
| reserved_0__BOX | 7 | Unsigned |
| value_0__BOX | 32 | Signed |

### Payload description

#### index_0__BOX { #_Calibration_reading_0__BOX-index_0__BOX }

index of the device that need reading

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| unvalid | 0 |
| voltage_sensor_b | 1 |

#### select_0__BOX { #_Calibration_reading_0__BOX-select_0__BOX }

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

#### calibration_status_0__BOX { #_Calibration_reading_0__BOX-calibration_status_0__BOX }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| bad | 0 |
| ok | 1 |

#### reserved_0__BOX { #_Calibration_reading_0__BOX-reserved_0__BOX }

select what value to read

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 7 | Unsigned |  | 1 | 0 |  | 127 |

#### value_0__BOX { #_Calibration_reading_0__BOX-value_0__BOX }

require calibration valut

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 32 | Signed |  | 0.0001 | 0 | -214748.3648 | 214748.3647 |


<a id="_Factory_Debug_cmd_0__BOX"></a>
## _Factory_Debug_cmd_0__BOX { #_Factory_Debug_cmd_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820065 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

factory debug cmd, need factory mode flag set to 1

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| god_mode_0__BOX | 1 | Single bit |
| internal_power_a_0__BOX | 1 | Label set |
| internal_power_b_0__BOX | 1 | Label set |
| offset_stack_internal_0__BOX | 8 | Unsigned |

### Payload description

#### god_mode_0__BOX { #_Factory_Debug_cmd_0__BOX-god_mode_0__BOX }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### internal_power_a_0__BOX { #_Factory_Debug_cmd_0__BOX-internal_power_a_0__BOX }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| on | 0 |
| off | 1 |

#### internal_power_b_0__BOX { #_Factory_Debug_cmd_0__BOX-internal_power_b_0__BOX }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| on | 0 |
| off | 1 |

#### offset_stack_internal_0__BOX { #_Factory_Debug_cmd_0__BOX-offset_stack_internal_0__BOX }

Customers MUST NOT USE this bit. need factory mode = 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | offset | 1 | 0 |  | 255 |


<a id="info_adm_cs_0__BOX"></a>
## info_adm_cs_0__BOX { #info_adm_cs_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820080 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| reserved_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_cs_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| GC01 | 16 |

#### Revision_0__BOX { #info_adm_cs_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_cs_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### reserved_0__BOX { #info_adm_cs_0__BOX-reserved_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_cs_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_0__BOX"></a>
## info_adm_pc_0__BOX { #info_adm_pc_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820081 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| nb_detected_0__BOX | 8 | Unsigned |
| nd_side_a_0__BOX | 8 | Unsigned |
| nd_side_b_0__BOX | 8 | Unsigned |
| Collision_0__BOX | 8 | Unsigned |

### Payload description

#### nb_detected_0__BOX { #info_adm_pc_0__BOX-nb_detected_0__BOX }

number of modules detectedce

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### nd_side_a_0__BOX { #info_adm_pc_0__BOX-nd_side_a_0__BOX }

number of modules detectedce

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### nd_side_b_0__BOX { #info_adm_pc_0__BOX-nd_side_b_0__BOX }

number of modules detectedce

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Collision_0__BOX { #info_adm_pc_0__BOX-Collision_0__BOX }

collision between module

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="info_adm_pc_id_1_0__BOX"></a>
## info_adm_pc_id_1_0__BOX { #info_adm_pc_id_1_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820082 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_1_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_1_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_1_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_1_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_1_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_2_0__BOX"></a>
## info_adm_pc_id_2_0__BOX { #info_adm_pc_id_2_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820083 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_2_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_2_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_2_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_2_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_2_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_3_0__BOX"></a>
## info_adm_pc_id_3_0__BOX { #info_adm_pc_id_3_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820084 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_3_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_3_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_3_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_3_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_3_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_4_0__BOX"></a>
## info_adm_pc_id_4_0__BOX { #info_adm_pc_id_4_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820085 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_4_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_4_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_4_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_4_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_4_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_5_0__BOX"></a>
## info_adm_pc_id_5_0__BOX { #info_adm_pc_id_5_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820086 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_5_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_5_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_5_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_5_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_5_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_id_6_0__BOX"></a>
## info_adm_pc_id_6_0__BOX { #info_adm_pc_id_6_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820087 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Revision_0__BOX | 8 | Unsigned |
| Variant_0__BOX | 8 | Unsigned |
| Stack_position_0__BOX | 8 | Unsigned |
| serial_number_0__BOX | 32 | Unsigned |

### Payload description

#### Type_0__BOX { #info_adm_pc_id_6_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Revision_0__BOX { #info_adm_pc_id_6_0__BOX-Revision_0__BOX }

The hardware revision numbere

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Variant_0__BOX { #info_adm_pc_id_6_0__BOX-Variant_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Stack_position_0__BOX { #info_adm_pc_id_6_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### serial_number_0__BOX { #info_adm_pc_id_6_0__BOX-serial_number_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  | 4294967295 |


<a id="info_adm_pc_status_1_0__BOX"></a>
## info_adm_pc_status_1_0__BOX { #info_adm_pc_status_1_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820088 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_1_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_1_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_1_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_1_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_1_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_1_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_2_0__BOX"></a>
## info_adm_pc_status_2_0__BOX { #info_adm_pc_status_2_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820089 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_2_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_2_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_2_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_2_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_2_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_2_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_3_0__BOX"></a>
## info_adm_pc_status_3_0__BOX { #info_adm_pc_status_3_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x82008a |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_3_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_3_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_3_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_3_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_3_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_3_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_4_0__BOX"></a>
## info_adm_pc_status_4_0__BOX { #info_adm_pc_status_4_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x82008b |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_4_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_4_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_4_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_4_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_4_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_4_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_5_0__BOX"></a>
## info_adm_pc_status_5_0__BOX { #info_adm_pc_status_5_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x82008c |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_5_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_5_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_5_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_5_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_5_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_5_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="info_adm_pc_status_6_0__BOX"></a>
## info_adm_pc_status_6_0__BOX { #info_adm_pc_status_6_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x82008d |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Available_0__BOX | 1 | Single bit |
| Side_0__BOX | 2 | Label set |
| Status_0__BOX | 2 | Label set |
| Interlock_I_0__BOX | 1 | Single bit |
| Interlock_E_0__BOX | 1 | Single bit |
| mode_0__BOX | 16 | Unsigned |

### Payload description

#### Available_0__BOX { #info_adm_pc_status_6_0__BOX-Available_0__BOX }

The device available

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Side_0__BOX { #info_adm_pc_status_6_0__BOX-Side_0__BOX }

The device is Ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| side_unk | 0 |
| side_a | 1 |
| side_b | 2 |

#### Status_0__BOX { #info_adm_pc_status_6_0__BOX-Status_0__BOX }

The device is Running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 2 | Label set |  | 1 | 0 |  | 3 |

| Label name | Value |
|------------|-------|
| off | 0 |
| ready | 1 |
| running | 2 |

#### Interlock_I_0__BOX { #info_adm_pc_status_6_0__BOX-Interlock_I_0__BOX }

The device have interlock internal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Interlock_E_0__BOX { #info_adm_pc_status_6_0__BOX-Interlock_E_0__BOX }

The device have interlock external

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### mode_0__BOX { #info_adm_pc_status_6_0__BOX-mode_0__BOX }

Mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  | 65535 |


<a id="cs_performance_0__BOX"></a>
## cs_performance_0__BOX { #cs_performance_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820090 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Status of internal modules

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| cpu_1_usage_0__BOX | 8 | Unsigned |
| cpu_2_usage_0__BOX | 8 | Unsigned |
| can_bus_load_A_0__BOX | 8 | Unsigned |
| can_bus_load_B_0__BOX | 8 | Unsigned |
| main_loop_freq_0__BOX | 16 | Unsigned |

### Payload description

#### cpu_1_usage_0__BOX { #cs_performance_0__BOX-cpu_1_usage_0__BOX }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### cpu_2_usage_0__BOX { #cs_performance_0__BOX-cpu_2_usage_0__BOX }

Controller cpu 2 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### can_bus_load_A_0__BOX { #cs_performance_0__BOX-can_bus_load_A_0__BOX }

Controller cup 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### can_bus_load_B_0__BOX { #cs_performance_0__BOX-can_bus_load_B_0__BOX }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned | % | 1 | 0 |  | 255 |

#### main_loop_freq_0__BOX { #cs_performance_0__BOX-main_loop_freq_0__BOX }

Controller cpu 1 usage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Hz | 1 | 0 |  | 65535 |


<a id="info_can_api_error_0__BOX"></a>
## info_can_api_error_0__BOX { #info_can_api_error_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x820091 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

debug - Allow to knwow  what module has wrong can api

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type_0__BOX | 8 | Label set |
| Stack_position_0__BOX | 8 | Unsigned |
| Major_expected_0__BOX | 8 | Unsigned |
| Minor_expected_0__BOX | 8 | Unsigned |
| Patch_expected_0__BOX | 8 | Unsigned |
| Major_actual_0__BOX | 8 | Unsigned |
| Minor_actual_0__BOX | 8 | Unsigned |
| Patch_actual_0__BOX | 8 | Unsigned |

### Payload description

#### Type_0__BOX { #info_can_api_error_0__BOX-Type_0__BOX }

The device identification field

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  | 255 |

| Label name | Value |
|------------|-------|
| BP25 | 7 |
| BI25 | 8 |
| DMF1 | 19 |

#### Stack_position_0__BOX { #info_can_api_error_0__BOX-Stack_position_0__BOX }

Hardware variant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Major_expected_0__BOX { #info_can_api_error_0__BOX-Major_expected_0__BOX }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor_expected_0__BOX { #info_can_api_error_0__BOX-Minor_expected_0__BOX }

The minor version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch_expected_0__BOX { #info_can_api_error_0__BOX-Patch_expected_0__BOX }

The patch version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Major_actual_0__BOX { #info_can_api_error_0__BOX-Major_actual_0__BOX }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Minor_actual_0__BOX { #info_can_api_error_0__BOX-Minor_actual_0__BOX }

The minor version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### Patch_actual_0__BOX { #info_can_api_error_0__BOX-Patch_actual_0__BOX }

The patch version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="_fms_state_0__BOX"></a>
## _fms_state_0__BOX { #_fms_state_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x8200f0 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

FSm status for debug

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| init_0__BOX | 8 | Unsigned |
| ready_0__BOX | 8 | Unsigned |
| turned_on_0__BOX | 8 | Unsigned |
| turned_off_0__BOX | 8 | Unsigned |
| bleeding_0__BOX | 8 | Unsigned |

### Payload description

#### init_0__BOX { #_fms_state_0__BOX-init_0__BOX }

box state init

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### ready_0__BOX { #_fms_state_0__BOX-ready_0__BOX }

box state ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### turned_on_0__BOX { #_fms_state_0__BOX-turned_on_0__BOX }

box state turned on

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### turned_off_0__BOX { #_fms_state_0__BOX-turned_off_0__BOX }

box state turned off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  | 255 |

#### bleeding_0__BOX { #_fms_state_0__BOX-bleeding_0__BOX }

box state bleeding

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  | 255 |


<a id="_interlocks_status_0__BOX"></a>
## _interlocks_status_0__BOX { #_interlocks_status_0__BOX }


| * | * |
|---|---|
| **Frame ID** | 0x8200f1 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

BOX interlock status used for debug

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| e_0__BOX | 1 | Label set |
| a_0__BOX | 1 | Label set |
| b_0__BOX | 1 | Label set |
| i_0__BOX | 1 | Label set |
| x_0__BOX | 1 | Label set |

### Payload description

#### e_0__BOX { #_interlocks_status_0__BOX-e_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### a_0__BOX { #_interlocks_status_0__BOX-a_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### b_0__BOX { #_interlocks_status_0__BOX-b_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### i_0__BOX { #_interlocks_status_0__BOX-i_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |

#### x_0__BOX { #_interlocks_status_0__BOX-x_0__BOX }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Tripped | 0 |
| Clear | 1 |
