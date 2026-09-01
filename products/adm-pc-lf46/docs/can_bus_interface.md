---
hide:
  - toc
---

# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [_Filter_Calibration_Offset_Update](#_Filter_Calibration_Offset_Update) | 0x10043 | 6 |  |  |
| [_Filter_Calibration_Scale_Update](#_Filter_Calibration_Scale_Update) | 0x10044 | 6 |  |  |
| [Filter_Stack_Control](#Filter_Stack_Control) | 0x10045 | 6 |  |  |
| [Filter_Independent_Relay_Control](#Filter_Independent_Relay_Control) | 0x10049 | 1 |  |  |
| [Filter_Fault_Control](#Filter_Fault_Control) | 0x10050 | 1 |  |  |
| [Filter_System_Flags_Control](#Filter_System_Flags_Control) | 0x10061 | 8 |  |  |
| [Filter_Identification](#Filter_Identification) | 0x18000 | 8 |  | 1000 |
| [Filter_FwInfo](#Filter_FwInfo) | 0x18001 | 8 |  | 1000 |
| [Filter_Debug](#Filter_Debug) | 0x18002 | 8 |  | 1000 |
| [Filter_Input_Voltages](#Filter_Input_Voltages) | 0x18003 | 6 |  | 100 |
| [Filter_Output_Voltages](#Filter_Output_Voltages) | 0x18004 | 6 |  | 100 |
| [Filter_Input_Frequencies](#Filter_Input_Frequencies) | 0x18005 | 6 |  | 100 |
| [Filter_Temperature](#Filter_Temperature) | 0x18006 | 2 |  | 1000 |
| [Filter_Relays_Status](#Filter_Relays_Status) | 0x18007 | 1 |  | 100 |
| [Filter_Faults](#Filter_Faults) | 0x18008 | 1 |  | 100 |
| [Filter_Input_Phases](#Filter_Input_Phases) | 0x18009 | 6 |  | 100 |
| [Filter_Supply_24V](#Filter_Supply_24V) | 0x1800a | 2 |  | 1000 |
| [Filter_Status_and_Fault](#Filter_Status_and_Fault) | 0x1800b | 2 |  | 100 |
| [_Filter_Boot_FwInfo](#_Filter_Boot_FwInfo) | 0x1800d | 8 |  | 1000 |
| [_Filter_Input_Voltages_Raw](#_Filter_Input_Voltages_Raw) | 0x18021 | 6 |  | 100 |
| [_Filter_Output_Voltages_Raw](#_Filter_Output_Voltages_Raw) | 0x18022 | 6 |  | 100 |
| [Filter_Relays](#Filter_Relays) | 0x18040 | 1 |  | 100 |
| [_Filter_Calibration_Adc_Scale](#_Filter_Calibration_Adc_Scale) | 0x18043 | 6 |  | 1000 |
| [_Filter_Calibration_Adc_Fs](#_Filter_Calibration_Adc_Fs) | 0x18044 | 6 |  | 1000 |
| [_Filter_Input_Voltages_DC](#_Filter_Input_Voltages_DC) | 0x18053 | 6 |  | 100 |
| [_Filter_Output_Voltages_DC](#_Filter_Output_Voltages_DC) | 0x18054 | 6 |  | 100 |


<a id="_Filter_Calibration_Offset_Update"></a>
## _Filter_Calibration_Offset_Update { #_Filter_Calibration_Offset_Update }


| * | * |
|---|---|
| **Frame ID** | 0x10043 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for offsets.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1_Calib | 16 | Signed |
| Voltage_Input_L2_Calib | 16 | Signed |
| Voltage_Input_L3_Calib | 16 | Signed |
| Voltage_Output_L1_Calib | 16 | Signed |
| Voltage_Output_L2_Calib | 16 | Signed |
| Voltage_Output_L3_Calib | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1_Calib { #_Filter_Calibration_Offset_Update-Voltage_Input_L1_Calib }

Voltage offset at the converter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Input_L2_Calib { #_Filter_Calibration_Offset_Update-Voltage_Input_L2_Calib }

Voltage offset at the converter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Input_L3_Calib { #_Filter_Calibration_Offset_Update-Voltage_Input_L3_Calib }

Voltage offset at the converter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_L1_Calib { #_Filter_Calibration_Offset_Update-Voltage_Output_L1_Calib }

Voltage offset at the converter output, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_L2_Calib { #_Filter_Calibration_Offset_Update-Voltage_Output_L2_Calib }

Voltage offset at the converter output, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_L3_Calib { #_Filter_Calibration_Offset_Update-Voltage_Output_L3_Calib }

Voltage offset at the converter output, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Calibration_Index { #_Filter_Calibration_Offset_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_Filter_Calibration_Offset_Update-CRC }

Checksum of bytes 0 to 5, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="_Filter_Calibration_Scale_Update"></a>
## _Filter_Calibration_Scale_Update { #_Filter_Calibration_Scale_Update }


| * | * |
|---|---|
| **Frame ID** | 0x10044 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for offsets.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1_Calib | 16 | Signed |
| Voltage_Input_L2_Calib | 16 | Signed |
| Voltage_Input_L3_Calib | 16 | Signed |
| Voltage_Output_L1_Calib | 16 | Signed |
| Voltage_Output_L2_Calib | 16 | Signed |
| Voltage_Output_L3_Calib | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1_Calib { #_Filter_Calibration_Scale_Update-Voltage_Input_L1_Calib }

Voltage offset at the converter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Input_L2_Calib { #_Filter_Calibration_Scale_Update-Voltage_Input_L2_Calib }

Voltage offset at the converter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Input_L3_Calib { #_Filter_Calibration_Scale_Update-Voltage_Input_L3_Calib }

Voltage offset at the converter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Output_L1_Calib { #_Filter_Calibration_Scale_Update-Voltage_Output_L1_Calib }

Voltage offset at the converter output, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Output_L2_Calib { #_Filter_Calibration_Scale_Update-Voltage_Output_L2_Calib }

Voltage offset at the converter output, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Output_L3_Calib { #_Filter_Calibration_Scale_Update-Voltage_Output_L3_Calib }

Voltage offset at the converter output, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Calibration_Index { #_Filter_Calibration_Scale_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_Filter_Calibration_Scale_Update-CRC }

Checksum of bytes 0 to 5, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="Filter_Stack_Control"></a>
## Filter_Stack_Control { #Filter_Stack_Control }


| * | * |
|---|---|
| **Frame ID** | 0x10045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Filter stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| Stack_size | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Stack_position { #Filter_Stack_Control-Stack_position }

The converter position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_size { #Filter_Stack_Control-Stack_size }

How many Filter converters are in stack in total

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #Filter_Stack_Control-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="Filter_Independent_Relay_Control"></a>
## Filter_Independent_Relay_Control { #Filter_Independent_Relay_Control }


| * | * |
|---|---|
| **Frame ID** | 0x10049 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

INTERNAL USE. User MUST NOT use this message under any circumstance. The user should instead
            use the &quot;Filter_Relays&quot; message to operate the LF45.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Precharge_Relay_ON | 1 | Single bit |
| Grid_Relay_ON | 1 | Single bit |

### Payload description

#### Precharge_Relay_ON { #Filter_Independent_Relay_Control-Precharge_Relay_ON }

Internal use. User MUST NOT modify this

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Grid_Relay_ON { #Filter_Independent_Relay_Control-Grid_Relay_ON }

Internal use. User MUST NOT modify this

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Filter_Fault_Control"></a>
## Filter_Fault_Control { #Filter_Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x10050 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Fault Control: actions to clear faults and reset the system

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Clear_Interlock | 1 | Single bit |
| Reset_Processor | 1 | Single bit |

### Payload description

#### Clear_Interlock { #Filter_Fault_Control-Clear_Interlock }

Clears the filter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor { #Filter_Fault_Control-Reset_Processor }

Reset the filter DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Filter_System_Flags_Control"></a>
## Filter_System_Flags_Control { #Filter_System_Flags_Control }


| * | * |
|---|---|
| **Frame ID** | 0x10061 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Control the system flags

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Factory_mode | 1 | Single bit |

### Payload description

#### Factory_mode { #Filter_System_Flags_Control-Factory_mode }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Filter_Identification"></a>
## Filter_Identification { #Filter_Identification }


| * | * |
|---|---|
| **Frame ID** | 0x18000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Identification of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Device_type | 8 | Label set |
| HW_revision | 8 | Unsigned |
| HW_variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Device_type { #Filter_Identification-Device_type }

The device identification field, uniquely identifies the sender in the network

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Filter | 1 |

#### HW_revision { #Filter_Identification-HW_revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### HW_variant { #Filter_Identification-HW_variant }

The DSP firmware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_position { #Filter_Identification-Stack_position }

Position of the module within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #Filter_Identification-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="Filter_FwInfo"></a>
## Filter_FwInfo { #Filter_FwInfo }


| * | * |
|---|---|
| **Frame ID** | 0x18001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Git revision of the DSP firmware

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| FW_revision_0 | 8 | Unsigned |
| FW_revision_7 | 8 | Unsigned |
| FW_datecode_0 | 8 | Unsigned |
| FW_datecode_7 | 8 | Unsigned |
| FW_revision_1 | 8 | Unsigned |
| FW_revision_8 | 8 | Unsigned |
| FW_datecode_1 | 8 | Unsigned |
| FW_datecode_8 | 8 | Unsigned |
| FW_revision_2 | 8 | Unsigned |
| FW_revision_9 | 8 | Unsigned |
| FW_datecode_2 | 8 | Unsigned |
| FW_datecode_9 | 8 | Unsigned |
| FW_revision_3 | 8 | Unsigned |
| FW_revision_10 | 8 | Unsigned |
| FW_datecode_3 | 8 | Unsigned |
| FW_datecode_10 | 8 | Unsigned |
| FW_revision_4 | 8 | Unsigned |
| FW_revision_11 | 8 | Unsigned |
| FW_datecode_4 | 8 | Unsigned |
| FW_datecode_11 | 8 | Unsigned |
| FW_revision_5 | 8 | Unsigned |
| FW_revision_12 | 8 | Unsigned |
| FW_datecode_5 | 8 | Unsigned |
| FW_datecode_12 | 8 | Unsigned |
| FW_revision_6 | 8 | Unsigned |
| FW_revision_13 | 8 | Unsigned |
| FW_datecode_6 | 8 | Unsigned |
| FW_datecode_13 | 8 | Unsigned |
| FW_info_mux | 8 | Unsigned |

### Payload description

#### FW_revision_0 { #Filter_FwInfo-FW_revision_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 { #Filter_FwInfo-FW_revision_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 { #Filter_FwInfo-FW_datecode_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 { #Filter_FwInfo-FW_datecode_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 { #Filter_FwInfo-FW_revision_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 { #Filter_FwInfo-FW_revision_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 { #Filter_FwInfo-FW_datecode_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 { #Filter_FwInfo-FW_datecode_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 { #Filter_FwInfo-FW_revision_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 { #Filter_FwInfo-FW_revision_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 { #Filter_FwInfo-FW_datecode_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 { #Filter_FwInfo-FW_datecode_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 { #Filter_FwInfo-FW_revision_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 { #Filter_FwInfo-FW_revision_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 { #Filter_FwInfo-FW_datecode_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 { #Filter_FwInfo-FW_datecode_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 { #Filter_FwInfo-FW_revision_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 { #Filter_FwInfo-FW_revision_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 { #Filter_FwInfo-FW_datecode_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 { #Filter_FwInfo-FW_datecode_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 { #Filter_FwInfo-FW_revision_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 { #Filter_FwInfo-FW_revision_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 { #Filter_FwInfo-FW_datecode_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 { #Filter_FwInfo-FW_datecode_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 { #Filter_FwInfo-FW_revision_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 { #Filter_FwInfo-FW_revision_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 { #Filter_FwInfo-FW_datecode_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 { #Filter_FwInfo-FW_datecode_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_info_mux { #Filter_FwInfo-FW_info_mux }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="Filter_Debug"></a>
## Filter_Debug { #Filter_Debug }


| * | * |
|---|---|
| **Frame ID** | 0x18002 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Values for debugging of HW/SW problems

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Status_Error_Code | 16 | Unsigned |
| Data_1 | 16 | Unsigned |
| Data_2 | 16 | Unsigned |
| Data_3 | 16 | Unsigned |

### Payload description

#### Status_Error_Code { #Filter_Debug-Status_Error_Code }

Main status / error code as defined in errno/errno.h

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_1 { #Filter_Debug-Data_1 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_2 { #Filter_Debug-Data_2 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_3 { #Filter_Debug-Data_3 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="Filter_Input_Voltages"></a>
## Filter_Input_Voltages { #Filter_Input_Voltages }


| * | * |
|---|---|
| **Frame ID** | 0x18003 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input voltages readout. Realtime RMS readouts of the sensed variables. The voltage measured before the contactors.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1 | 16 | Unsigned |
| Voltage_Input_L2 | 16 | Unsigned |
| Voltage_Input_L3 | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1 { #Filter_Input_Voltages-Voltage_Input_L1 }

Voltage measured at the filter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Input_L2 { #Filter_Input_Voltages-Voltage_Input_L2 }

Voltage measured at the filter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Input_L3 { #Filter_Input_Voltages-Voltage_Input_L3 }

Voltage measured at the filter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="Filter_Output_Voltages"></a>
## Filter_Output_Voltages { #Filter_Output_Voltages }


| * | * |
|---|---|
| **Frame ID** | 0x18004 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Output voltages readout. Realtime RMS readouts of the sensed variables. The voltage measured after the contactors.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Output_L1 | 16 | Unsigned |
| Voltage_Output_L2 | 16 | Unsigned |
| Voltage_Output_L3 | 16 | Unsigned |

### Payload description

#### Voltage_Output_L1 { #Filter_Output_Voltages-Voltage_Output_L1 }

Voltage measured at the filter output, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Output_L2 { #Filter_Output_Voltages-Voltage_Output_L2 }

Voltage measured at the filter output, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Output_L3 { #Filter_Output_Voltages-Voltage_Output_L3 }

Voltage measured at the filter output, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="Filter_Input_Frequencies"></a>
## Filter_Input_Frequencies { #Filter_Input_Frequencies }


| * | * |
|---|---|
| **Frame ID** | 0x18005 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input voltage frequencies&gt;

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| L1_Freq | 16 | Unsigned |
| L2_Freq | 16 | Unsigned |
| L3_Freq | 16 | Unsigned |

### Payload description

#### L1_Freq { #Filter_Input_Frequencies-L1_Freq }

Frequency measured at the filter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.1 | 0 |  |  |

#### L2_Freq { #Filter_Input_Frequencies-L2_Freq }

Frequency measured at the filter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Hz | 0.1 | 0 |  |  |

#### L3_Freq { #Filter_Input_Frequencies-L3_Freq }

Frequency measured at the filter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Hz | 0.1 | 0 |  |  |


<a id="Filter_Temperature"></a>
## Filter_Temperature { #Filter_Temperature }


| * | * |
|---|---|
| **Frame ID** | 0x18006 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readouts of the module temperature sensor

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Temp_Inductor | 16 | Signed |

### Payload description

#### Temp_Inductor { #Filter_Temperature-Temp_Inductor }

Temperature of the inductor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 |  |  |


<a id="Filter_Relays_Status"></a>
## Filter_Relays_Status { #Filter_Relays_Status }


| * | * |
|---|---|
| **Frame ID** | 0x18007 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

State of the filter relays.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Off | 1 | Single bit |
| Precharge | 1 | Single bit |
| Monitor | 1 | Single bit |
| Main | 1 | Single bit |
| On | 1 | Single bit |
| Fail | 1 | Single bit |

### Payload description

#### Off { #Filter_Relays_Status-Off }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Precharge { #Filter_Relays_Status-Precharge }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Monitor { #Filter_Relays_Status-Monitor }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Main { #Filter_Relays_Status-Main }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### On { #Filter_Relays_Status-On }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### Fail { #Filter_Relays_Status-Fail }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="Filter_Faults"></a>
## Filter_Faults { #Filter_Faults }


| * | * |
|---|---|
| **Frame ID** | 0x18008 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Protection_trip_internal | 1 | Label set |
| Protection_trip_external | 1 | Label set |
| Mains_Voltage | 1 | Label set |
| Mains_Frequency | 1 | Label set |
| Mains_Phase | 1 | Label set |
| Precharge | 1 | Label set |
| Mains_Monitor | 1 | Label set |

### Payload description

#### Protection_trip_internal { #Filter_Faults-Protection_trip_internal }

This flagg is asserted if the interlock is open due to an internal fault condition (self-protection)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Protection_trip_external { #Filter_Faults-Protection_trip_external }

This flag is asserted if the interlock is open due to an external condition received in the module.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Mains_Voltage { #Filter_Faults-Mains_Voltage }

Mains voltage out of tolerance

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Mains_Frequency { #Filter_Faults-Mains_Frequency }

Mains frequency out of tolerance

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Mains_Phase { #Filter_Faults-Mains_Phase }

Mains phase advance out of tolerance

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Precharge { #Filter_Faults-Precharge }

Precharge failed (check output voltage)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Mains_Monitor { #Filter_Faults-Mains_Monitor }

Grid health monitor is not ready

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |


<a id="Filter_Input_Phases"></a>
## Filter_Input_Phases { #Filter_Input_Phases }


| * | * |
|---|---|
| **Frame ID** | 0x18009 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input voltage frequencies&gt;

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| L1L2_Phase | 16 | Unsigned |
| L2L3_Phase | 16 | Unsigned |
| L3L1_Phase | 16 | Unsigned |

### Payload description

#### L1L2_Phase { #Filter_Input_Phases-L1L2_Phase }

Phase advance measured at the filter input, phase 1 to phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | ° | 0.1 | 0 |  |  |

#### L2L3_Phase { #Filter_Input_Phases-L2L3_Phase }

Phase advance measured at the filter input, phase 2 to phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | ° | 0.1 | 0 |  |  |

#### L3L1_Phase { #Filter_Input_Phases-L3L1_Phase }

Phase advance measured at the filter input, phase 3 to phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | ° | 0.1 | 0 |  |  |


<a id="Filter_Supply_24V"></a>
## Filter_Supply_24V { #Filter_Supply_24V }


| * | * |
|---|---|
| **Frame ID** | 0x1800a |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readouts of the 24-V supply voltage

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Supply_Voltage | 16 | Unsigned |

### Payload description

#### Supply_Voltage { #Filter_Supply_24V-Supply_Voltage }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="Filter_Status_and_Fault"></a>
## Filter_Status_and_Fault { #Filter_Status_and_Fault }


| * | * |
|---|---|
| **Frame ID** | 0x1800b |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Status and fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Ready | 1 | Single bit |
| Running | 1 | Single bit |
| Master | 1 | Single bit |
| Slave | 1 | Single bit |
| NFO | 1 | Label set |
| Measurement_system_failure | 1 | Label set |
| EEPROM_failure | 1 | Label set |
| System | 1 | Label set |

### Payload description

#### Ready { #Filter_Status_and_Fault-Ready }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Running { #Filter_Status_and_Fault-Running }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Master { #Filter_Status_and_Fault-Master }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Slave { #Filter_Status_and_Fault-Slave }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### NFO { #Filter_Status_and_Fault-NFO }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Measurement_system_failure { #Filter_Status_and_Fault-Measurement_system_failure }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### EEPROM_failure { #Filter_Status_and_Fault-EEPROM_failure }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### System { #Filter_Status_and_Fault-System }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |


<a id="_Filter_Boot_FwInfo"></a>
## _Filter_Boot_FwInfo { #_Filter_Boot_FwInfo }


| * | * |
|---|---|
| **Frame ID** | 0x1800d |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Git revision of the bootloader firmware.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| FW_revision_0 | 8 | Unsigned |
| FW_revision_7 | 8 | Unsigned |
| FW_datecode_0 | 8 | Unsigned |
| FW_datecode_7 | 8 | Unsigned |
| FW_revision_1 | 8 | Unsigned |
| FW_revision_8 | 8 | Unsigned |
| FW_datecode_1 | 8 | Unsigned |
| FW_datecode_8 | 8 | Unsigned |
| FW_revision_2 | 8 | Unsigned |
| FW_revision_9 | 8 | Unsigned |
| FW_datecode_2 | 8 | Unsigned |
| FW_datecode_9 | 8 | Unsigned |
| FW_revision_3 | 8 | Unsigned |
| FW_revision_10 | 8 | Unsigned |
| FW_datecode_3 | 8 | Unsigned |
| FW_datecode_10 | 8 | Unsigned |
| FW_revision_4 | 8 | Unsigned |
| FW_revision_11 | 8 | Unsigned |
| FW_datecode_4 | 8 | Unsigned |
| FW_datecode_11 | 8 | Unsigned |
| FW_revision_5 | 8 | Unsigned |
| FW_revision_12 | 8 | Unsigned |
| FW_datecode_5 | 8 | Unsigned |
| FW_datecode_12 | 8 | Unsigned |
| FW_revision_6 | 8 | Unsigned |
| FW_revision_13 | 8 | Unsigned |
| FW_datecode_6 | 8 | Unsigned |
| FW_datecode_13 | 8 | Unsigned |
| Boot_FW_info_mux | 8 | Unsigned |

### Payload description

#### FW_revision_0 { #_Filter_Boot_FwInfo-FW_revision_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 { #_Filter_Boot_FwInfo-FW_revision_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 { #_Filter_Boot_FwInfo-FW_datecode_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 { #_Filter_Boot_FwInfo-FW_datecode_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 { #_Filter_Boot_FwInfo-FW_revision_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 { #_Filter_Boot_FwInfo-FW_revision_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 { #_Filter_Boot_FwInfo-FW_datecode_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 { #_Filter_Boot_FwInfo-FW_datecode_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 { #_Filter_Boot_FwInfo-FW_revision_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 { #_Filter_Boot_FwInfo-FW_revision_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 { #_Filter_Boot_FwInfo-FW_datecode_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 { #_Filter_Boot_FwInfo-FW_datecode_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 { #_Filter_Boot_FwInfo-FW_revision_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 { #_Filter_Boot_FwInfo-FW_revision_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 { #_Filter_Boot_FwInfo-FW_datecode_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 { #_Filter_Boot_FwInfo-FW_datecode_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 { #_Filter_Boot_FwInfo-FW_revision_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 { #_Filter_Boot_FwInfo-FW_revision_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 { #_Filter_Boot_FwInfo-FW_datecode_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 { #_Filter_Boot_FwInfo-FW_datecode_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 { #_Filter_Boot_FwInfo-FW_revision_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 { #_Filter_Boot_FwInfo-FW_revision_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 { #_Filter_Boot_FwInfo-FW_datecode_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 { #_Filter_Boot_FwInfo-FW_datecode_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 { #_Filter_Boot_FwInfo-FW_revision_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 { #_Filter_Boot_FwInfo-FW_revision_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 { #_Filter_Boot_FwInfo-FW_datecode_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 { #_Filter_Boot_FwInfo-FW_datecode_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Boot_FW_info_mux { #_Filter_Boot_FwInfo-Boot_FW_info_mux }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="_Filter_Input_Voltages_Raw"></a>
## _Filter_Input_Voltages_Raw { #_Filter_Input_Voltages_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x18021 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input voltages readout. Debug only values, for calibration

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1_Raw | 16 | Unsigned |
| Voltage_Input_L2_Raw | 16 | Unsigned |
| Voltage_Input_L3_Raw | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1_Raw { #_Filter_Input_Voltages_Raw-Voltage_Input_L1_Raw }

Voltage measured at the filter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |

#### Voltage_Input_L2_Raw { #_Filter_Input_Voltages_Raw-Voltage_Input_L2_Raw }

Voltage measured at the filter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |

#### Voltage_Input_L3_Raw { #_Filter_Input_Voltages_Raw-Voltage_Input_L3_Raw }

Voltage measured at the filter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |


<a id="_Filter_Output_Voltages_Raw"></a>
## _Filter_Output_Voltages_Raw { #_Filter_Output_Voltages_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x18022 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Output voltages readout. Debug only values, for calibration

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Output_L1_Raw | 16 | Unsigned |
| Voltage_Output_L2_Raw | 16 | Unsigned |
| Voltage_Output_L3_Raw | 16 | Unsigned |

### Payload description

#### Voltage_Output_L1_Raw { #_Filter_Output_Voltages_Raw-Voltage_Output_L1_Raw }

Voltage measured at the filter output, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_L2_Raw { #_Filter_Output_Voltages_Raw-Voltage_Output_L2_Raw }

Voltage measured at the filter output, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_L3_Raw { #_Filter_Output_Voltages_Raw-Voltage_Output_L3_Raw }

Voltage measured at the filter output, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | ADC Counts | 1 | 0 |  |  |


<a id="Filter_Relays"></a>
## Filter_Relays { #Filter_Relays }


| * | * |
|---|---|
| **Frame ID** | 0x18040 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Close or open Filter relays. Strobe controlled.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Close_Relays | 1 | Single bit |
| Open_Relays | 1 | Single bit |

### Payload description

#### Close_Relays { #Filter_Relays-Close_Relays }

Command to close the relays.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Open_Relays { #Filter_Relays-Open_Relays }

Command to open the relays.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_Filter_Calibration_Adc_Scale"></a>
## _Filter_Calibration_Adc_Scale { #_Filter_Calibration_Adc_Scale }


| * | * |
|---|---|
| **Frame ID** | 0x18043 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc scale (resolution) value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1 | 32 | Float |
| Voltage_Input_L2 | 32 | Float |
| Voltage_Input_L3 | 32 | Float |
| Voltage_Output_L1 | 32 | Float |
| Voltage_Output_L2 | 32 | Float |
| Voltage_Output_L3 | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1 { #_Filter_Calibration_Adc_Scale-Voltage_Input_L1 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Input_L2 { #_Filter_Calibration_Adc_Scale-Voltage_Input_L2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Input_L3 { #_Filter_Calibration_Adc_Scale-Voltage_Input_L3 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Output_L1 { #_Filter_Calibration_Adc_Scale-Voltage_Output_L1 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Output_L2 { #_Filter_Calibration_Adc_Scale-Voltage_Output_L2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Output_L3 { #_Filter_Calibration_Adc_Scale-Voltage_Output_L3 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Adc_Index { #_Filter_Calibration_Adc_Scale-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_Filter_Calibration_Adc_Fs"></a>
## _Filter_Calibration_Adc_Fs { #_Filter_Calibration_Adc_Fs }


| * | * |
|---|---|
| **Frame ID** | 0x18044 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc fullscale value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1 | 32 | Float |
| Voltage_Input_L2 | 32 | Float |
| Voltage_Input_L3 | 32 | Float |
| Voltage_Output_L1 | 32 | Float |
| Voltage_Output_L2 | 32 | Float |
| Voltage_Output_L3 | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1 { #_Filter_Calibration_Adc_Fs-Voltage_Input_L1 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Input_L2 { #_Filter_Calibration_Adc_Fs-Voltage_Input_L2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Input_L3 { #_Filter_Calibration_Adc_Fs-Voltage_Input_L3 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Output_L1 { #_Filter_Calibration_Adc_Fs-Voltage_Output_L1 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Output_L2 { #_Filter_Calibration_Adc_Fs-Voltage_Output_L2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Output_L3 { #_Filter_Calibration_Adc_Fs-Voltage_Output_L3 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Adc_Index { #_Filter_Calibration_Adc_Fs-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_Filter_Input_Voltages_DC"></a>
## _Filter_Input_Voltages_DC { #_Filter_Input_Voltages_DC }


| * | * |
|---|---|
| **Frame ID** | 0x18053 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input voltages readout. Realtime readouts of the sensed variables. The voltage measured before the contactors.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Input_L1 | 16 | Unsigned |
| Voltage_Input_L2 | 16 | Unsigned |
| Voltage_Input_L3 | 16 | Unsigned |

### Payload description

#### Voltage_Input_L1 { #_Filter_Input_Voltages_DC-Voltage_Input_L1 }

Voltage measured at the filter input, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Input_L2 { #_Filter_Input_Voltages_DC-Voltage_Input_L2 }

Voltage measured at the filter input, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Input_L3 { #_Filter_Input_Voltages_DC-Voltage_Input_L3 }

Voltage measured at the filter input, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="_Filter_Output_Voltages_DC"></a>
## _Filter_Output_Voltages_DC { #_Filter_Output_Voltages_DC }


| * | * |
|---|---|
| **Frame ID** | 0x18054 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Output voltages readout. Realtime RMS readouts of the sensed variables. The voltage measured after the contactors.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Output_L1 | 16 | Unsigned |
| Voltage_Output_L2 | 16 | Unsigned |
| Voltage_Output_L3 | 16 | Unsigned |

### Payload description

#### Voltage_Output_L1 { #_Filter_Output_Voltages_DC-Voltage_Output_L1 }

Voltage measured at the filter output, phase 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Output_L2 { #_Filter_Output_Voltages_DC-Voltage_Output_L2 }

Voltage measured at the filter output, phase 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Voltage_Output_L3 { #_Filter_Output_Voltages_DC-Voltage_Output_L3 }

Voltage measured at the filter output, phase 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |
