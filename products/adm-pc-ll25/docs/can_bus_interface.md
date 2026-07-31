---
hide:
  - toc
---

# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [LLC_Mode_Control](#LLC_Mode_Control) | 0x30041 | 1 |  | 100 |
| [LLC_PWM_Frequency_Control](#LLC_PWM_Frequency_Control) | 0x30043 | 2 |  |  |
| [LLC_Current_Setpoint_Control](#LLC_Current_Setpoint_Control) | 0x30044 | 2 |  | 100 |
| [LLC_Voltage_Setpoint_Control](#LLC_Voltage_Setpoint_Control) | 0x30045 | 2 |  | 100 |
| [LLC_Stack_Control](#LLC_Stack_Control) | 0x30046 | 6 |  |  |
| [LLC_Voltage_Limits](#LLC_Voltage_Limits) | 0x30047 | 8 |  | 100 |
| [LLC_Current_Limits](#LLC_Current_Limits) | 0x30048 | 4 |  | 100 |
| [LLC_Ground_Fault_Control](#LLC_Ground_Fault_Control) | 0x30049 | 1 |  | 100 |
| [LLC_PWM_Control](#LLC_PWM_Control) | 0x3004a | 8 |  |  |
| [LLC_Fault_Control](#LLC_Fault_Control) | 0x30050 | 1 |  |  |
| [_LLC_Calibration_Offset_Update](#_LLC_Calibration_Offset_Update) | 0x30051 | 6 |  |  |
| [_LLC_Calibration_Scale_Update](#_LLC_Calibration_Scale_Update) | 0x30052 | 6 |  |  |
| [LLC_Keep_Alive](#LLC_Keep_Alive) | 0x30060 | 1 |  |  |
| [LLC_System_Flags_Control](#LLC_System_Flags_Control) | 0x30061 | 8 |  |  |
| [LLC_Identification](#LLC_Identification) | 0x38000 | 8 |  | 1000 |
| [LLC_FwInfo](#LLC_FwInfo) | 0x38001 | 8 |  | 1000 |
| [LLC_Debug](#LLC_Debug) | 0x38002 | 8 |  | 1000 |
| [LLC_Phase_Current_U_V_W](#LLC_Phase_Current_U_V_W) | 0x38003 | 6 |  | 100 |
| [LLC_Voltages_Currents](#LLC_Voltages_Currents) | 0x38004 | 6 |  | 100 |
| [LLC_Temperatures](#LLC_Temperatures) | 0x38005 | 6 |  | 1000 |
| [LLC_Faults](#LLC_Faults) | 0x38006 | 3 |  | 1000 |
| [LLC_Status](#LLC_Status) | 0x38007 | 3 |  | 1000 |
| [LLC_Setpoints](#LLC_Setpoints) | 0x38008 | 6 |  | 1000 |
| [LLC_Voltages_External](#LLC_Voltages_External) | 0x38009 | 4 |  | 100 |
| [LLC_Ground_Fault](#LLC_Ground_Fault) | 0x3800a | 5 |  | 100 |
| [_LLC_Ground_Fault_Raw](#_LLC_Ground_Fault_Raw) | 0x3800b | 2 |  | 100 |
| [_LLC_External_Raw](#_LLC_External_Raw) | 0x3800c | 4 |  | 100 |
| [LLC_PWM_Setpoints](#LLC_PWM_Setpoints) | 0x3800d | 8 |  | 1000 |
| [_LLC_Voltages_Currents_Raw](#_LLC_Voltages_Currents_Raw) | 0x38010 | 6 |  | 100 |
| [_LLC_Calibration_Adc_Scale](#_LLC_Calibration_Adc_Scale) | 0x38051 | 6 |  | 1000 |
| [_LLC_Calibration_Adc_Fs](#_LLC_Calibration_Adc_Fs) | 0x38052 | 6 |  | 1000 |


<a id="LLC_Mode_Control"></a>
## LLC_Mode_Control { #LLC_Mode_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30041 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Operation Mode control: sets the converter operation mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Converter_ON | 1 | Single bit |
| PWM_mode_ON | 1 | Single bit |
| Current_feedback_ON | 1 | Single bit |
| Voltage_feedback_ON | 1 | Single bit |
| _Precharge_ON | 1 | Single bit |
| _PFC_Current_feedback_ON | 1 | Single bit |
| _PFC_Voltage_feedback_ON | 1 | Single bit |
| PWM_v2_mode_ON | 1 | Single bit |

### Payload description

#### Converter_ON { #LLC_Mode_Control-Converter_ON }

Enable the converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_mode_ON { #LLC_Mode_Control-PWM_mode_ON }

Enable the PWM mode (this will set the converter in open loop)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Current_feedback_ON { #LLC_Mode_Control-Current_feedback_ON }

Enable the current loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Voltage_feedback_ON { #LLC_Mode_Control-Voltage_feedback_ON }

Enable the voltage loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### _Precharge_ON { #LLC_Mode_Control-_Precharge_ON }

Enable precharge mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### _PFC_Current_feedback_ON { #LLC_Mode_Control-_PFC_Current_feedback_ON }

Enable PFC current feedback loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### _PFC_Voltage_feedback_ON { #LLC_Mode_Control-_PFC_Voltage_feedback_ON }

Enable PFC voltage feedback loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_v2_mode_ON { #LLC_Mode_Control-PWM_v2_mode_ON }

Enable the PWM v2 mode (this will set the converter in open loop)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_PWM_Frequency_Control"></a>
## LLC_PWM_Frequency_Control { #LLC_PWM_Frequency_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30043 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

PWM frequency control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| PWM_frequency | 16 | Unsigned |

### Payload description

#### PWM_frequency { #LLC_PWM_Frequency_Control-PWM_frequency }

Sets the PWM frequency. Active only when the converter is in PWM mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 10 | 0 |  |  |


<a id="LLC_Current_Setpoint_Control"></a>
## LLC_Current_Setpoint_Control { #LLC_Current_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30044 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Current setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_setpoint | 16 | Unsigned |

### Payload description

#### Current_setpoint { #LLC_Current_Setpoint_Control-Current_setpoint }

Sets the output current setpoint. Active only when the current loop is enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | A | 0.01 | 0 |  | 70 |


<a id="LLC_Voltage_Setpoint_Control"></a>
## LLC_Voltage_Setpoint_Control { #LLC_Voltage_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30045 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Voltage setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_setpoint | 16 | Unsigned |

### Payload description

#### Voltage_setpoint { #LLC_Voltage_Setpoint_Control-Voltage_setpoint }

Sets the output voltage setpoint. Active only when the voltage loop is enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 500 |


<a id="LLC_Stack_Control"></a>
## LLC_Stack_Control { #LLC_Stack_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30046 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

LLC stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| Stack_size | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Stack_position { #LLC_Stack_Control-Stack_position }

The converter position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_size { #LLC_Stack_Control-Stack_size }

How many Buck converters are in stack in total

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #LLC_Stack_Control-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="LLC_Voltage_Limits"></a>
## LLC_Voltage_Limits { #LLC_Voltage_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x30047 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Set the input and output voltage limits (minimum and maximum)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Input_voltage_min | 16 | Unsigned |
| Input_voltage_max | 16 | Unsigned |
| Output_voltage_min | 16 | Unsigned |
| Output_voltage_max | 16 | Unsigned |

### Payload description

#### Input_voltage_min { #LLC_Voltage_Limits-Input_voltage_min }

Minimum tolerated input voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 800 |

#### Input_voltage_max { #LLC_Voltage_Limits-Input_voltage_max }

Maximum allowable input voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 | 0 | 800 |

#### Output_voltage_min { #LLC_Voltage_Limits-Output_voltage_min }

Minimum allowable output voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 | 0 |  |

#### Output_voltage_max { #LLC_Voltage_Limits-Output_voltage_max }

Maximum allowable output voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned | V | 0.1 | 0 | 0 | 800 |


<a id="LLC_Current_Limits"></a>
## LLC_Current_Limits { #LLC_Current_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x30048 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Current limits

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Output_current_min | 16 | Unsigned |
| Output_current_max | 16 | Unsigned |

### Payload description

#### Output_current_min { #LLC_Current_Limits-Output_current_min }

Minimum allowable output current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | A | 0.01 | 0 | 0 |  |

#### Output_current_max { #LLC_Current_Limits-Output_current_max }

Maximum allowable output current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.01 | 0 |  | 75 |


<a id="LLC_Ground_Fault_Control"></a>
## LLC_Ground_Fault_Control { #LLC_Ground_Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30049 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Ground fault control. This byte can enable/disable monitoring of the ground Insulation
            and enable/disable the ground insulation test circuit.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Ground_Fault_Enable | 1 | Single bit |
| Ground_Test_Enable | 1 | Single bit |

### Payload description

#### Ground_Fault_Enable { #LLC_Ground_Fault_Control-Ground_Fault_Enable }

If true, it enables the ground fault monitoring. Ground fault monitoring is
                disabled by default.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Ground_Test_Enable { #LLC_Ground_Fault_Control-Ground_Test_Enable }

If true, it enables the ground test circuit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_PWM_Control"></a>
## LLC_PWM_Control { #LLC_PWM_Control }


| * | * |
|---|---|
| **Frame ID** | 0x3004a |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Direct PWM control via period, duty cycle, and deadtime.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| PWM_Period | 16 | Unsigned |
| PWM_Duty_Cycle | 16 | Unsigned |
| PWM_Deadtime | 16 | Unsigned |
| PWM_Mode | 2 | Unsigned |
| PWM_Lock | 1 | Single bit |

### Payload description

#### PWM_Period { #LLC_PWM_Control-PWM_Period }

PWM period (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Duty_Cycle { #LLC_PWM_Control-PWM_Duty_Cycle }

PWM duty cycle (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Deadtime { #LLC_PWM_Control-PWM_Deadtime }

PWM deadtime (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Mode { #LLC_PWM_Control-PWM_Mode }

PWM switching mode (0: Off, 1: 2-phase, 2: 3-phase)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 2 | Unsigned |  | 1 | 0 |  |  |

#### PWM_Lock { #LLC_PWM_Control-PWM_Lock }

Locks duty cycle to period (50%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 50 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_Fault_Control"></a>
## LLC_Fault_Control { #LLC_Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30050 |
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
| Clear_Faults | 1 | Single bit |
| Bleeder_Pulse | 1 | Single bit |
| Trip_Interlock | 1 | Single bit |

### Payload description

#### Clear_Interlock { #LLC_Fault_Control-Clear_Interlock }

Clears the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor { #LLC_Fault_Control-Reset_Processor }

Reset the converter DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Clear_Faults { #LLC_Fault_Control-Clear_Faults }

Clear software faults

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Bleeder_Pulse { #LLC_Fault_Control-Bleeder_Pulse }

Bleed out output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock { #LLC_Fault_Control-Trip_Interlock }

Trips the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_LLC_Calibration_Offset_Update"></a>
## _LLC_Calibration_Offset_Update { #_LLC_Calibration_Offset_Update }


| * | * |
|---|---|
| **Frame ID** | 0x30051 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for offsets.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Output_Calib | 16 | Signed |
| Voltage_Output_Calib | 16 | Signed |
| Voltage_Input_Calib | 16 | Signed |
| Ground_Fault_Calib | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_Output_Calib { #_LLC_Calibration_Offset_Update-Current_Output_Calib }

Current offset at the converter output (Iout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Output_Calib { #_LLC_Calibration_Offset_Update-Voltage_Output_Calib }

Voltage offset at the converter output (Vout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Input_Calib { #_LLC_Calibration_Offset_Update-Voltage_Input_Calib }

Voltage offset at the converter input (Vin)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Ground_Fault_Calib { #_LLC_Calibration_Offset_Update-Ground_Fault_Calib }

Current offset at the converter output (Iout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Calibration_Index { #_LLC_Calibration_Offset_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_LLC_Calibration_Offset_Update-CRC }

Checksum of bytes 0 to 2, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="_LLC_Calibration_Scale_Update"></a>
## _LLC_Calibration_Scale_Update { #_LLC_Calibration_Scale_Update }


| * | * |
|---|---|
| **Frame ID** | 0x30052 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for scales.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Output_Calib | 16 | Signed |
| Voltage_Output_Calib | 16 | Signed |
| Voltage_Input_Calib | 16 | Signed |
| Ground_Fault_Calib | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_Output_Calib { #_LLC_Calibration_Scale_Update-Current_Output_Calib }

Current offset at the converter output (Iout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Output_Calib { #_LLC_Calibration_Scale_Update-Voltage_Output_Calib }

Voltage offset at the converter output (Vout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_Input_Calib { #_LLC_Calibration_Scale_Update-Voltage_Input_Calib }

Voltage offset at the converter input (Vin)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Ground_Fault_Calib { #_LLC_Calibration_Scale_Update-Ground_Fault_Calib }

Current offset at the converter output (Iout)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Calibration_Index { #_LLC_Calibration_Scale_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_LLC_Calibration_Scale_Update-CRC }

Checksum of bytes 0 to 2, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="LLC_Keep_Alive"></a>
## LLC_Keep_Alive { #LLC_Keep_Alive }


| * | * |
|---|---|
| **Frame ID** | 0x30060 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Keep alive ping message.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Keep_Alive_Enable | 1 | Single bit |

### Payload description

#### Keep_Alive_Enable { #LLC_Keep_Alive-Keep_Alive_Enable }

If set to 1, module will expect to receive this message every second repeatedly, or it will stop operation

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_System_Flags_Control"></a>
## LLC_System_Flags_Control { #LLC_System_Flags_Control }


| * | * |
|---|---|
| **Frame ID** | 0x30061 |
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

#### Factory_mode { #LLC_System_Flags_Control-Factory_mode }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_Identification"></a>
## LLC_Identification { #LLC_Identification }


| * | * |
|---|---|
| **Frame ID** | 0x38000 |
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

#### Device_type { #LLC_Identification-Device_type }

The device identification field, uniquely identifies the sender in the network

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| LLC | 3 |

#### HW_revision { #LLC_Identification-HW_revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### HW_variant { #LLC_Identification-HW_variant }

The DSP firmware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_position { #LLC_Identification-Stack_position }

Position of the module within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #LLC_Identification-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="LLC_FwInfo"></a>
## LLC_FwInfo { #LLC_FwInfo }


| * | * |
|---|---|
| **Frame ID** | 0x38001 |
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

#### FW_revision_0 { #LLC_FwInfo-FW_revision_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 { #LLC_FwInfo-FW_revision_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 { #LLC_FwInfo-FW_datecode_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 { #LLC_FwInfo-FW_datecode_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 { #LLC_FwInfo-FW_revision_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 { #LLC_FwInfo-FW_revision_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 { #LLC_FwInfo-FW_datecode_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 { #LLC_FwInfo-FW_datecode_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 { #LLC_FwInfo-FW_revision_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 { #LLC_FwInfo-FW_revision_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 { #LLC_FwInfo-FW_datecode_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 { #LLC_FwInfo-FW_datecode_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 { #LLC_FwInfo-FW_revision_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 { #LLC_FwInfo-FW_revision_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 { #LLC_FwInfo-FW_datecode_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 { #LLC_FwInfo-FW_datecode_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 { #LLC_FwInfo-FW_revision_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 { #LLC_FwInfo-FW_revision_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 { #LLC_FwInfo-FW_datecode_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 { #LLC_FwInfo-FW_datecode_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 { #LLC_FwInfo-FW_revision_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 { #LLC_FwInfo-FW_revision_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 { #LLC_FwInfo-FW_datecode_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 { #LLC_FwInfo-FW_datecode_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 { #LLC_FwInfo-FW_revision_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 { #LLC_FwInfo-FW_revision_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 { #LLC_FwInfo-FW_datecode_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 { #LLC_FwInfo-FW_datecode_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_info_mux { #LLC_FwInfo-FW_info_mux }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="LLC_Debug"></a>
## LLC_Debug { #LLC_Debug }


| * | * |
|---|---|
| **Frame ID** | 0x38002 |
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

#### Status_Error_Code { #LLC_Debug-Status_Error_Code }

Main status / error code as defined in errno/errno.h

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_1 { #LLC_Debug-Data_1 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_2 { #LLC_Debug-Data_2 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_3 { #LLC_Debug-Data_3 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="LLC_Phase_Current_U_V_W"></a>
## LLC_Phase_Current_U_V_W { #LLC_Phase_Current_U_V_W }


| * | * |
|---|---|
| **Frame ID** | 0x38003 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Current of phases U,V and W

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |

### Payload description

#### Phase_U { #LLC_Phase_Current_U_V_W-Phase_U }

Current of the phase U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_V { #LLC_Phase_Current_U_V_W-Phase_V }

Current of the phase V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_W { #LLC_Phase_Current_U_V_W-Phase_W }

Current of phase W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="LLC_Voltages_Currents"></a>
## LLC_Voltages_Currents { #LLC_Voltages_Currents }


| * | * |
|---|---|
| **Frame ID** | 0x38004 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Input and output currents and voltages readout. Realtime readouts of the sensed variables. The voltage is measured at the input and output of the converter, while the current is measured at the output only

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Out | 16 | Signed |
| Voltage_In | 16 | Signed |
| Voltage_Out | 16 | Signed |

### Payload description

#### Current_Out { #LLC_Voltages_Currents-Current_Out }

Current measured at the converter output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Voltage_In { #LLC_Voltages_Currents-Voltage_In }

Voltage measured at the converter input

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Voltage_Out { #LLC_Voltages_Currents-Voltage_Out }

Voltage measured at the converter output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="LLC_Temperatures"></a>
## LLC_Temperatures { #LLC_Temperatures }


| * | * |
|---|---|
| **Frame ID** | 0x38005 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readouts of the module temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Temp_Rectifier | 16 | Signed |
| Temp_Bridge | 16 | Signed |
| Temp_Transformer | 16 | Signed |

### Payload description

#### Temp_Rectifier { #LLC_Temperatures-Temp_Rectifier }

Temperature of the output rectifier block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Bridge { #LLC_Temperatures-Temp_Bridge }

Temperature of the switching bridge

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Transformer { #LLC_Temperatures-Temp_Transformer }

Temperature of the transformer

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | °C | 0.01 | 0 |  |  |


<a id="LLC_Faults"></a>
## LLC_Faults { #LLC_Faults }


| * | * |
|---|---|
| **Frame ID** | 0x38006 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Protection_trip_internal | 1 | Label set |
| Protection_trip_external | 1 | Label set |
| Output_overcurrent | 1 | Label set |
| Output_overvoltage | 1 | Label set |
| Output_undervoltage | 1 | Label set |
| Input_overvoltage | 1 | Label set |
| Input_undervoltage | 1 | Label set |
| MOSFET_overtemperature | 1 | Label set |
| Transformer_overtemperature | 1 | Label set |
| Current_sharing_failure | 1 | Label set |
| Switching_failure | 1 | Label set |
| Current_loop_failure | 1 | Label set |
| Voltage_loop_failure | 1 | Label set |
| CAN_failure | 1 | Label set |
| Control_response_timedout | 1 | Label set |
| Measurement_system_failure | 1 | Label set |
| EEPROM_failure | 1 | Label set |
| Ground_fault | 1 | Label set |
| Phase_U_overcurrent | 1 | Label set |
| Phase_V_overcurrent | 1 | Label set |
| Phase_W_overcurrent | 1 | Label set |
| Rectifier_overtemperature | 1 | Label set |

### Payload description

#### Protection_trip_internal { #LLC_Faults-Protection_trip_internal }

This flagg is asserted if the interlock is open due to an internal fault condition (self-protection)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Protection_trip_external { #LLC_Faults-Protection_trip_external }

This flag is asserted if the interlock is open due to an external condition received in the module.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Output_overcurrent { #LLC_Faults-Output_overcurrent }

Indicates an output overcurrent event. The overcurrent event is triggered when the measured output current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Output_overvoltage { #LLC_Faults-Output_overvoltage }

Indicates an output overvoltage event. The overvoltage event is triggered when the measured output voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Output_undervoltage { #LLC_Faults-Output_undervoltage }

Output undervoltage condition. The undervoltage condition is asserted when the measured output voltage is under the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Input_overvoltage { #LLC_Faults-Input_overvoltage }

Input overvoltage condition. The overvoltage condition is asserted when the measured input voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Input_undervoltage { #LLC_Faults-Input_undervoltage }

Input undervoltage condition. The undervoltage condition is asserted when the measured input voltage is under the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### MOSFET_overtemperature { #LLC_Faults-MOSFET_overtemperature }

This flag is asserted when the temperature of the MOSFET block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Transformer_overtemperature { #LLC_Faults-Transformer_overtemperature }

This flag is asserted when the temperature of the Transformer block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_sharing_failure { #LLC_Faults-Current_sharing_failure }

A failure in the internal current sharing. The operation up to the nominal output current cannot be guaranteed.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Switching_failure { #LLC_Faults-Switching_failure }

Failure in the MOSFET block or in their drivers.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_loop_failure { #LLC_Faults-Current_loop_failure }

The current loop is not operational, and therefore current regulation is not guaranteed.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_loop_failure { #LLC_Faults-Voltage_loop_failure }

The voltage loop is not operational, and therefore voltage regulation is not guaranteed.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### CAN_failure { #LLC_Faults-CAN_failure }

CAN bus or transceiver not operating properly.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Control_response_timedout { #LLC_Faults-Control_response_timedout }

The control system did not answer within the allowed time window, and a time out condition was triggered. The converter is switched off as the control system is not present.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Measurement_system_failure { #LLC_Faults-Measurement_system_failure }

The voltages/currents measurement system is malfunctionning, and readouts are not guaranteed to be accurate.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### EEPROM_failure { #LLC_Faults-EEPROM_failure }

The configuration EEPROM failed to load or save the module configuration.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Ground_fault { #LLC_Faults-Ground_fault }

A ground fault has been detected.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_U_overcurrent { #LLC_Faults-Phase_U_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_V_overcurrent { #LLC_Faults-Phase_V_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_W_overcurrent { #LLC_Faults-Phase_W_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Rectifier_overtemperature { #LLC_Faults-Rectifier_overtemperature }

This flag is asserted when the temperature of the Rectifier block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |


<a id="LLC_Status"></a>
## LLC_Status { #LLC_Status }


| * | * |
|---|---|
| **Frame ID** | 0x38007 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Status bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Converter_running | 1 | Single bit |
| PWM_mode | 1 | Single bit |
| Current_loop_mode | 1 | Single bit |
| Voltage_loop_mode | 1 | Single bit |
| Master | 1 | Single bit |
| Slave | 1 | Single bit |
| Precharge_mode | 1 | Single bit |
| PFC_current_loop_mode | 1 | Single bit |
| PFC_voltage_loop_mode | 1 | Single bit |
| PWM_v2_mode | 1 | Single bit |

### Payload description

#### Converter_running { #LLC_Status-Converter_running }

Indicates that the converter is running, and its output is active.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_mode { #LLC_Status-PWM_mode }

Indicates if the converter is in PWM mode, and therefore working in open loop.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Current_loop_mode { #LLC_Status-Current_loop_mode }

Indicates if the current loop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Voltage_loop_mode { #LLC_Status-Voltage_loop_mode }

Indicates if the voltage loop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Master { #LLC_Status-Master }

Indicates if the current converter is the Master in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### Slave { #LLC_Status-Slave }

Indicates if the current converter is an Slave in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### Precharge_mode { #LLC_Status-Precharge_mode }

Indickates if the precharge mode is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### PFC_current_loop_mode { #LLC_Status-PFC_current_loop_mode }

Indicates id the pfc current loop mode is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |

#### PFC_voltage_loop_mode { #LLC_Status-PFC_voltage_loop_mode }

Indicates id the pfc voltage loop mode is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_v2_mode { #LLC_Status-PWM_v2_mode }

Indicates if the converter is in PWM v2 mode, and therefore working in open loop.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="LLC_Setpoints"></a>
## LLC_Setpoints { #LLC_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x38008 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| PWM_frequency | 16 | Unsigned |
| Current_setpoint | 16 | Unsigned |
| Voltage_setpoint | 16 | Unsigned |

### Payload description

#### PWM_frequency { #LLC_Setpoints-PWM_frequency }

The current PWM frequency

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 10 | 0 |  |  |

#### Current_setpoint { #LLC_Setpoints-Current_setpoint }

The actual current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.01 | 0 |  |  |

#### Voltage_setpoint { #LLC_Setpoints-Voltage_setpoint }

The actual voltage setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="LLC_Voltages_External"></a>
## LLC_Voltages_External { #LLC_Voltages_External }


| * | * |
|---|---|
| **Frame ID** | 0x38009 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Output external voltage channels readout. Realtime readouts of the sensed variables. The voltage is measured at the two external voltage sensors (EXT1,EXT2), with reference to output DC-.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_EXT1 | 16 | Signed |
| Voltage_EXT2 | 16 | Signed |

### Payload description

#### Voltage_EXT1 { #LLC_Voltages_External-Voltage_EXT1 }

Voltage measured at the converter output EXT1 channel

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Voltage_EXT2 { #LLC_Voltages_External-Voltage_EXT2 }

Voltage measured at the converter output EXT2 channel

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="LLC_Ground_Fault"></a>
## LLC_Ground_Fault { #LLC_Ground_Fault }


| * | * |
|---|---|
| **Frame ID** | 0x3800a |
| **Length [Bytes]** | 5 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Ground fault measurement

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| InsulationResistance | 32 | Signed |
| Valid | 1 | Single bit |
| Gnd_monitor_enabled | 1 | Single bit |
| Gnd_test_enabled | 1 | Single bit |

### Payload description

#### InsulationResistance { #LLC_Ground_Fault-InsulationResistance }

The insulation resistance between output terminals and ground

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | kOhm | 0.01 | 0 |  |  |

#### Valid { #LLC_Ground_Fault-Valid }

Signs that the calculated insulation resistance is valid.
Value can be invalid e.g. in case of too low voltage on the output terminals.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Single bit |  | 1 | 0 |  |  |

#### Gnd_monitor_enabled { #LLC_Ground_Fault-Gnd_monitor_enabled }

True if the Ground insulation monitor is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 1 | Single bit |  | 1 | 0 |  |  |

#### Gnd_test_enabled { #LLC_Ground_Fault-Gnd_test_enabled }

True if the Ground test circuit is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_LLC_Ground_Fault_Raw"></a>
## _LLC_Ground_Fault_Raw { #_LLC_Ground_Fault_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x3800b |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Ground fault measurement

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| InsulationResistance_Raw | 16 | Signed |

### Payload description

#### InsulationResistance_Raw { #_LLC_Ground_Fault_Raw-InsulationResistance_Raw }

The insulation resistance between output terminals and ground

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed |  | 1 | 0 |  |  |


<a id="_LLC_External_Raw"></a>
## _LLC_External_Raw { #_LLC_External_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x3800c |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

LLC_External without calibration

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| External1_Raw | 16 | Unsigned |
| External2_Raw | 16 | Unsigned |

### Payload description

#### External1_Raw { #_LLC_External_Raw-External1_Raw }

The external measurement 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### External2_Raw { #_LLC_External_Raw-External2_Raw }

The external measurement 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="LLC_PWM_Setpoints"></a>
## LLC_PWM_Setpoints { #LLC_PWM_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x3800d |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

PWM Setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| PWM_Period | 16 | Unsigned |
| PWM_Duty_Cycle | 16 | Unsigned |
| PWM_Deadtime | 16 | Unsigned |
| PWM_Mode | 2 | Unsigned |
| PWM_Lock | 1 | Single bit |

### Payload description

#### PWM_Period { #LLC_PWM_Setpoints-PWM_Period }

PWM period (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Duty_Cycle { #LLC_PWM_Setpoints-PWM_Duty_Cycle }

PWM duty cycle (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Deadtime { #LLC_PWM_Setpoints-PWM_Deadtime }

PWM deadtime (16-bit)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 | 0 | 65535 |

#### PWM_Mode { #LLC_PWM_Setpoints-PWM_Mode }

PWM switching mode (0: Off, 1: 2-phase, 2: 3-phase)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 2 | Unsigned |  | 1 | 0 |  |  |

#### PWM_Lock { #LLC_PWM_Setpoints-PWM_Lock }

Lock duty cycle to period (50%)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 50 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_LLC_Voltages_Currents_Raw"></a>
## _LLC_Voltages_Currents_Raw { #_LLC_Voltages_Currents_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x38010 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

LLC_Voltages_Currents without calibration

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Out_Raw | 16 | Signed |
| Voltage_In_Raw | 16 | Signed |
| Voltage_Out_Raw | 16 | Signed |

### Payload description

#### Current_Out_Raw { #_LLC_Voltages_Currents_Raw-Current_Out_Raw }

Current measured at the converter output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed |  | 1 | 0 |  |  |

#### Voltage_In_Raw { #_LLC_Voltages_Currents_Raw-Voltage_In_Raw }

Voltage measured at the converter input

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed |  | 1 | 0 |  |  |

#### Voltage_Out_Raw { #_LLC_Voltages_Currents_Raw-Voltage_Out_Raw }

Voltage measured at the converter output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed |  | 1 | 0 |  |  |


<a id="_LLC_Calibration_Adc_Scale"></a>
## _LLC_Calibration_Adc_Scale { #_LLC_Calibration_Adc_Scale }


| * | * |
|---|---|
| **Frame ID** | 0x38051 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc scale (resolution) value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_In | 32 | Float |
| Voltage_Out | 32 | Float |
| Current_Out | 32 | Float |
| InsulationResistance | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Voltage_In { #_LLC_Calibration_Adc_Scale-Voltage_In }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Out { #_LLC_Calibration_Adc_Scale-Voltage_Out }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Current_Out { #_LLC_Calibration_Adc_Scale-Current_Out }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### InsulationResistance { #_LLC_Calibration_Adc_Scale-InsulationResistance }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Adc_Index { #_LLC_Calibration_Adc_Scale-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_LLC_Calibration_Adc_Fs"></a>
## _LLC_Calibration_Adc_Fs { #_LLC_Calibration_Adc_Fs }


| * | * |
|---|---|
| **Frame ID** | 0x38052 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc fullscale value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_In | 32 | Float |
| Voltage_Out | 32 | Float |
| Current_Out | 32 | Float |
| InsulationResistance | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Voltage_In { #_LLC_Calibration_Adc_Fs-Voltage_In }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Out { #_LLC_Calibration_Adc_Fs-Voltage_Out }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_Out { #_LLC_Calibration_Adc_Fs-Current_Out }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### InsulationResistance { #_LLC_Calibration_Adc_Fs-InsulationResistance }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Adc_Index { #_LLC_Calibration_Adc_Fs-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |
