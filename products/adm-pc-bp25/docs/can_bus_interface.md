---
hide:
  - toc
---

# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [AFE_Voltage_Limits](#AFE_Voltage_Limits) | 0x70030 | 8 |  |  |
| [AFE_Current_Limits](#AFE_Current_Limits) | 0x70031 | 4 |  |  |
| [AFE_Power_Setpoint_Control](#AFE_Power_Setpoint_Control) | 0x70039 | 4 |  |  |
| [AFE_Mode_Control](#AFE_Mode_Control) | 0x70040 | 8 |  | 1000 |
| [AFE_Reactive_Current_Setpoint_Control](#AFE_Reactive_Current_Setpoint_Control) | 0x70041 | 2 |  | 1000 |
| [AFE_PWM_Duty_Control](#AFE_PWM_Duty_Control) | 0x70042 | 6 |  |  |
| [AFE_Current_Setpoint_Control](#AFE_Current_Setpoint_Control) | 0x70043 | 2 |  | 1000 |
| [AFE_Voltage_Setpoint_Control](#AFE_Voltage_Setpoint_Control) | 0x70044 | 2 |  | 100 |
| [AFE_Stack_Control](#AFE_Stack_Control) | 0x70045 | 6 |  |  |
| [_AFE_Calibration_Offset_Update](#_AFE_Calibration_Offset_Update) | 0x70046 | 6 |  |  |
| [_AFE_Calibration_Scale_Update](#_AFE_Calibration_Scale_Update) | 0x70047 | 6 |  |  |
| [AFE_Frequency_Setpoint_Control](#AFE_Frequency_Setpoint_Control) | 0x70048 | 2 |  | 100 |
| [AFE_Phase_Setpoint_Control](#AFE_Phase_Setpoint_Control) | 0x70049 | 2 |  | 100 |
| [_AFE_ADC_Calibration_Mode](#_AFE_ADC_Calibration_Mode) | 0x7004a | 1 |  |  |
| [_AFE_ADC_Calibration_Setpoint](#_AFE_ADC_Calibration_Setpoint) | 0x7004b | 3 |  |  |
| [AFE_Group_Control](#AFE_Group_Control) | 0x7004c | 1 |  |  |
| [AFE_DC_droop_control](#AFE_DC_droop_control) | 0x7004d | 4 |  |  |
| [AFE_DC_setpoint_control](#AFE_DC_setpoint_control) | 0x7004e | 6 |  |  |
| [AFE_Power_Limit_Control](#AFE_Power_Limit_Control) | 0x7004f | 4 |  |  |
| [AFE_Fault_Control](#AFE_Fault_Control) | 0x70050 | 1 |  |  |
| [AFE_Inverter_Droop_Control](#AFE_Inverter_Droop_Control) | 0x70051 | 6 |  |  |
| [AFE_Firmware_Dev](#AFE_Firmware_Dev) | 0x70052 | 6 |  |  |
| [AFE_Power_Limit_Control_Readback](#AFE_Power_Limit_Control_Readback) | 0x7005f | 4 |  | 100 |
| [AFE_Keep_Alive](#AFE_Keep_Alive) | 0x70060 | 1 |  |  |
| [AFE_System_Flags_Control](#AFE_System_Flags_Control) | 0x70061 | 8 |  |  |
| [AFE_Rectifier_Setpoint_Control](#AFE_Rectifier_Setpoint_Control) | 0x70070 | 8 |  | 100 |
| [AFE_CAN_API_Version](#AFE_CAN_API_Version) | 0x700f3 | 3 |  | 1000 |
| [AFE_Identification](#AFE_Identification) | 0x78000 | 8 |  | 1000 |
| [AFE_FwInfo](#AFE_FwInfo) | 0x78001 | 8 |  | 1000 |
| [AFE_Debug](#AFE_Debug) | 0x78002 | 8 |  | 1000 |
| [AFE_Currents](#AFE_Currents) | 0x78003 | 6 |  | 100 |
| [AFE_Voltages](#AFE_Voltages) | 0x78004 | 8 |  | 10 |
| [AFE_Temperatures](#AFE_Temperatures) | 0x78005 | 4 |  | 1000 |
| [AFE_Faults](#AFE_Faults) | 0x78006 | 3 |  | 1000 |
| [AFE_Status](#AFE_Status) | 0x78007 | 8 |  | 100 |
| [AFE_Setpoints_PWM_Duty](#AFE_Setpoints_PWM_Duty) | 0x78008 | 6 |  | 1000 |
| [AFE_Setpoints](#AFE_Setpoints) | 0x78009 | 6 |  | 1000 |
| [AFE_Voltages_RMS](#AFE_Voltages_RMS) | 0x7800a | 6 |  | 100 |
| [AFE_Currents_RMS](#AFE_Currents_RMS) | 0x7800b | 6 |  | 100 |
| [AFE_Mains](#AFE_Mains) | 0x7800c | 4 |  | 100 |
| [_AFE_Boot_FwInfo](#_AFE_Boot_FwInfo) | 0x7800d | 8 |  | 1000 |
| [_AFE_Broadcast](#_AFE_Broadcast) | 0x7800e | 8 |  | 10 |
| [AFE_Group_Info](#AFE_Group_Info) | 0x7800f | 1 |  | 1000 |
| [AFE_DC_Bus_current](#AFE_DC_Bus_current) | 0x78010 | 2 |  | 100 |
| [AFE_AC_Power](#AFE_AC_Power) | 0x78011 | 8 |  | 1000 |
| [AFE_DC_Power](#AFE_DC_Power) | 0x78012 | 2 |  | 10 |
| [_AFE_Currents_Raw](#_AFE_Currents_Raw) | 0x78020 | 8 |  | 100 |
| [_AFE_Voltages_Raw](#_AFE_Voltages_Raw) | 0x78021 | 8 |  | 100 |
| [AFE_Droop_setpoints](#AFE_Droop_setpoints) | 0x78050 | 8 |  | 1000 |
| [_AFE_Calibration_Adc_Scale](#_AFE_Calibration_Adc_Scale) | 0x78051 | 6 |  | 1000 |
| [_AFE_Calibration_Adc_Fs](#_AFE_Calibration_Adc_Fs) | 0x78052 | 6 |  | 1000 |
| [_AFE_Calibration_Adc_Offset](#_AFE_Calibration_Adc_Offset) | 0x78053 | 4 |  | 1000 |
| [_AFE_Calibration_Adc_Gain](#_AFE_Calibration_Adc_Gain) | 0x78054 | 4 |  | 1000 |
| [AFE_Interlock_Faults](#AFE_Interlock_Faults) | 0x78056 | 2 |  | 1000 |
| [AFE_DC_Setpoints](#AFE_DC_Setpoints) | 0x78069 | 6 |  | 1000 |
| [AFE_Inverter_Droop_Readback](#AFE_Inverter_Droop_Readback) | 0x78151 | 8 |  | 100 |


<a id="AFE_Voltage_Limits"></a>
## AFE_Voltage_Limits { #AFE_Voltage_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x70030 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set the input and output voltage limits (minimum and maximum)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_voltage_min | 16 | Signed |
| Phase_voltage_max | 16 | Signed |
| DC_voltage_min | 16 | Signed |
| DC_voltage_max | 16 | Signed |

### Payload description

#### Phase_voltage_min { #AFE_Voltage_Limits-Phase_voltage_min }

Minimum tolerated phase voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 | 0 |  |

#### Phase_voltage_max { #AFE_Voltage_Limits-Phase_voltage_max }

Maximum allowable phase voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  | 850 |

#### DC_voltage_min { #AFE_Voltage_Limits-DC_voltage_min }

Minimum allowable dc voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 | 0 |  |

#### DC_voltage_max { #AFE_Voltage_Limits-DC_voltage_max }

Maximum allowable dc voltage

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | V | 0.1 | 0 |  | 850 |


<a id="AFE_Current_Limits"></a>
## AFE_Current_Limits { #AFE_Current_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x70031 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set the output current limits (mminimum and maximum)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_current_min | 16 | Signed |
| Phase_current_max | 16 | Signed |

### Payload description

#### Phase_current_min { #AFE_Current_Limits-Phase_current_min }

Minimum allowable output current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Phase_current_max { #AFE_Current_Limits-Phase_current_max }

Maximum allowable output current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |


<a id="AFE_Power_Setpoint_Control"></a>
## AFE_Power_Setpoint_Control { #AFE_Power_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70039 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set Power setpoints. Only used in Inverter 3-Phase mode! These setpoints are not
      absolute power setpoints. Rather, they refer to an offset with respect to the equilibrium
      position when sharing load with other inverters. Typically this number is kept to zero,
      unless you want to move from the equilibrium position.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Active_Power | 16 | Signed |
| Reactive_Power | 16 | Signed |

### Payload description

#### Active_Power { #AFE_Power_Setpoint_Control-Active_Power }

Active power setpoint in Watts

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |

#### Reactive_Power { #AFE_Power_Setpoint_Control-Reactive_Power }

Reactive power setpoint in Watts

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | W | 10 | 0 |  |  |


<a id="AFE_Mode_Control"></a>
## AFE_Mode_Control { #AFE_Mode_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70040 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Operation Mode control: sets the converter operation mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Converter_ON | 1 | Single bit |
| PWM_ON | 1 | Single bit |
| DC_Current_feedback_ON | 1 | Single bit |
| AC_Current_feedback_ON | 1 | Single bit |
| Buck_ON | 1 | Single bit |
| Boost_ON | 1 | Single bit |
| Rectifier_3ph_ON | 1 | Single bit |
| Inverter_1ph_ON | 1 | Single bit |
| Rectifier_1ph_ON | 1 | Single bit |
| Boost_Neutral_ON | 1 | Single bit |
| Inverter_3ph_ON | 1 | Single bit |
| Inverter_1ph_Sync_ON | 1 | Single bit |
| Neutral_ON | 1 | Single bit |
| Rectifier_1ph_Buck_ON | 1 | Single bit |
| Inverter_1ph_Boost_ON | 1 | Single bit |
| Rectifier_Distributed_ON | 1 | Single bit |
| MPPT_buck_ON | 1 | Single bit |
| MPPT_boost_ON | 1 | Single bit |
| Buck_2p_float_ON | 1 | Single bit |
| Inverter_1ph_Distributed_ON | 1 | Single bit |

### Payload description

#### Converter_ON { #AFE_Mode_Control-Converter_ON }

Enable the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_ON { #AFE_Mode_Control-PWM_ON }

Enable the PWM control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### DC_Current_feedback_ON { #AFE_Mode_Control-DC_Current_feedback_ON }

Enable the DC current loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### AC_Current_feedback_ON { #AFE_Mode_Control-AC_Current_feedback_ON }

Enable the AC current loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Buck_ON { #AFE_Mode_Control-Buck_ON }

Enable the buck control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### Boost_ON { #AFE_Mode_Control-Boost_ON }

Enable the boost control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_3ph_ON { #AFE_Mode_Control-Rectifier_3ph_ON }

Enable the three-phase rectifier control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_ON { #AFE_Mode_Control-Inverter_1ph_ON }

Enable the single-phase inverter control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_1ph_ON { #AFE_Mode_Control-Rectifier_1ph_ON }

Enable the single-phase rectifier control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Single bit |  | 1 | 0 |  |  |

#### Boost_Neutral_ON { #AFE_Mode_Control-Boost_Neutral_ON }

Enable the boost control mode with neutral generation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_3ph_ON { #AFE_Mode_Control-Inverter_3ph_ON }

Enable the three-phase inverter control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Sync_ON { #AFE_Mode_Control-Inverter_1ph_Sync_ON }

Single-phase inverter control mode with phase synchronization.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Single bit |  | 1 | 0 |  |  |

#### Neutral_ON { #AFE_Mode_Control-Neutral_ON }

Open-loop neutral generation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_1ph_Buck_ON { #AFE_Mode_Control-Rectifier_1ph_Buck_ON }

Single-phase rectifier with buck on one leg.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Boost_ON { #AFE_Mode_Control-Inverter_1ph_Boost_ON }

Single-phase inverter with boost on one leg.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_Distributed_ON { #AFE_Mode_Control-Rectifier_Distributed_ON }

Single-phase (floating) distributed rectifier

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Single bit |  | 1 | 0 |  |  |

#### MPPT_buck_ON { #AFE_Mode_Control-MPPT_buck_ON }

MPPT buck

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Single bit |  | 1 | 0 |  |  |

#### MPPT_boost_ON { #AFE_Mode_Control-MPPT_boost_ON }

MPPT boost

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Single bit |  | 1 | 0 |  |  |

#### Buck_2p_float_ON { #AFE_Mode_Control-Buck_2p_float_ON }

Boost on L1 and L2. Floating L3 (high-impedance)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Distributed_ON { #AFE_Mode_Control-Inverter_1ph_Distributed_ON }

Single-phase inverter mode distributed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="AFE_Reactive_Current_Setpoint_Control"></a>
## AFE_Reactive_Current_Setpoint_Control { #AFE_Reactive_Current_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70041 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Reactive power setpoint control.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Reactive_current_setpoint | 16 | Signed |

### Payload description

#### Reactive_current_setpoint { #AFE_Reactive_Current_Setpoint_Control-Reactive_current_setpoint }

This defines reactive current setpoint for 3-phase rectifier mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -150 | 150 |


<a id="AFE_PWM_Duty_Control"></a>
## AFE_PWM_Duty_Control { #AFE_PWM_Duty_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70042 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

PWM duty cycle control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Unsigned |
| Phase_V | 16 | Unsigned |
| Phase_W | 16 | Unsigned |

### Payload description

#### Phase_U { #AFE_PWM_Duty_Control-Phase_U }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | % | 0.001526 | 0 |  |  |

#### Phase_V { #AFE_PWM_Duty_Control-Phase_V }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | % | 0.001526 | 0 |  |  |

#### Phase_W { #AFE_PWM_Duty_Control-Phase_W }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | % | 0.001526 | 0 |  |  |


<a id="AFE_Current_Setpoint_Control"></a>
## AFE_Current_Setpoint_Control { #AFE_Current_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70043 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Current setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_setpoint | 16 | Signed |

### Payload description

#### Current_setpoint { #AFE_Current_Setpoint_Control-Current_setpoint }

Sets the output current setpoint. Active only when the current loop is enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -150 | 150 |


<a id="AFE_Voltage_Setpoint_Control"></a>
## AFE_Voltage_Setpoint_Control { #AFE_Voltage_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70044 |
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

#### Voltage_setpoint { #AFE_Voltage_Setpoint_Control-Voltage_setpoint }

Sets the output voltage setpoint. Active only when the voltage loop is enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |


<a id="AFE_Stack_Control"></a>
## AFE_Stack_Control { #AFE_Stack_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

PFC stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| Stack_size | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Stack_position { #AFE_Stack_Control-Stack_position }

The converter position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_size { #AFE_Stack_Control-Stack_size }

How many PFC converters are in stack in total

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #AFE_Stack_Control-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="_AFE_Calibration_Offset_Update"></a>
## _AFE_Calibration_Offset_Update { #_AFE_Calibration_Offset_Update }


| * | * |
|---|---|
| **Frame ID** | 0x70046 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for offsets.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 16 | Signed |
| Current_V | 16 | Signed |
| Current_W | 16 | Signed |
| Voltage_U | 16 | Signed |
| Voltage_V | 16 | Signed |
| Voltage_W | 16 | Signed |
| Voltage_DC | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Offset_Update-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Offset_Update-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Offset_Update-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Offset_Update-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Offset_Update-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Offset_Update-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Offset_Update-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Calibration_Index { #_AFE_Calibration_Offset_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_AFE_Calibration_Offset_Update-CRC }

Checksum of bytes 0 to 3, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="_AFE_Calibration_Scale_Update"></a>
## _AFE_Calibration_Scale_Update { #_AFE_Calibration_Scale_Update }


| * | * |
|---|---|
| **Frame ID** | 0x70047 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Update of the calibration table for scales.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 16 | Signed |
| Current_V | 16 | Signed |
| Current_W | 16 | Signed |
| Voltage_U | 16 | Signed |
| Voltage_V | 16 | Signed |
| Voltage_W | 16 | Signed |
| Voltage_DC | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Scale_Update-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Scale_Update-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Scale_Update-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Scale_Update-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Scale_Update-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Scale_Update-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Scale_Update-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | scale = 1.0 + value | 0.000015 | 0 |  |  |

#### Calibration_Index { #_AFE_Calibration_Scale_Update-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC { #_AFE_Calibration_Scale_Update-CRC }

Checksum of bytes 0 to 3, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="AFE_Frequency_Setpoint_Control"></a>
## AFE_Frequency_Setpoint_Control { #AFE_Frequency_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70048 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Frequency setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency_setpoint | 16 | Unsigned |

### Payload description

#### Frequency_setpoint { #AFE_Frequency_Setpoint_Control-Frequency_setpoint }

Sets the frequency for single-phase and three-phase generator modes.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 | 40 | 70 |


<a id="AFE_Phase_Setpoint_Control"></a>
## AFE_Phase_Setpoint_Control { #AFE_Phase_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70049 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Phase setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_setpoint | 16 | Unsigned |

### Payload description

#### Phase_setpoint { #AFE_Phase_Setpoint_Control-Phase_setpoint }

Sets the phase for inverter control modes.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | deg | 1 | 0 | 0 | 360 |


<a id="_AFE_ADC_Calibration_Mode"></a>
## _AFE_ADC_Calibration_Mode { #_AFE_ADC_Calibration_Mode }


| * | * |
|---|---|
| **Frame ID** | 0x7004a |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Automatic ADC calibration.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 2 | Unsigned |
| Current_V | 2 | Unsigned |
| Current_W | 2 | Unsigned |
| Voltage_U | 2 | Unsigned |
| Voltage_V | 2 | Unsigned |
| Voltage_W | 2 | Unsigned |
| Voltage_DC | 2 | Unsigned |
| Calibration_Index | 5 | Unsigned |
| start | 1 | Single bit |

### Payload description

#### Current_U { #_AFE_ADC_Calibration_Mode-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Current_V { #_AFE_ADC_Calibration_Mode-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Current_W { #_AFE_ADC_Calibration_Mode-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Voltage_U { #_AFE_ADC_Calibration_Mode-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Voltage_V { #_AFE_ADC_Calibration_Mode-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Voltage_W { #_AFE_ADC_Calibration_Mode-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_ADC_Calibration_Mode-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 2 | Unsigned |  | 1 | 0 |  |  |

#### Calibration_Index { #_AFE_ADC_Calibration_Mode-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 5 | Unsigned |  | 1 | 0 |  |  |

#### start { #_AFE_ADC_Calibration_Mode-start }

Start automatic calibration. Multiplexer index must be 0!

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_AFE_ADC_Calibration_Setpoint"></a>
## _AFE_ADC_Calibration_Setpoint { #_AFE_ADC_Calibration_Setpoint }


| * | * |
|---|---|
| **Frame ID** | 0x7004b |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Setpoint for automatic ADC calibration.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 16 | Signed |
| Current_V | 16 | Signed |
| Current_W | 16 | Signed |
| Voltage_U | 16 | Unsigned |
| Voltage_V | 16 | Unsigned |
| Voltage_W | 16 | Unsigned |
| Voltage_DC | 16 | Unsigned |
| Calibration_Index | 5 | Unsigned |
| point | 3 | Unsigned |

### Payload description

#### Current_U { #_AFE_ADC_Calibration_Setpoint-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -100 | 100 |

#### Current_V { #_AFE_ADC_Calibration_Setpoint-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -100 | 100 |

#### Current_W { #_AFE_ADC_Calibration_Setpoint-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -100 | 100 |

#### Voltage_U { #_AFE_ADC_Calibration_Setpoint-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Voltage_V { #_AFE_ADC_Calibration_Setpoint-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Voltage_W { #_AFE_ADC_Calibration_Setpoint-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Voltage_DC { #_AFE_ADC_Calibration_Setpoint-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Calibration_Index { #_AFE_ADC_Calibration_Setpoint-Calibration_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 5 | Unsigned |  | 1 | 0 |  |  |

#### point { #_AFE_ADC_Calibration_Setpoint-point }

Calibration point index.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 3 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Group_Control"></a>
## AFE_Group_Control { #AFE_Group_Control }


| * | * |
|---|---|
| **Frame ID** | 0x7004c |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set the Group ID of the device. If a module is assigned a Group other than one It will coordinate it&#x27;s output current with other modules in the same group to share load

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID | 8 | Unsigned |

### Payload description

#### Group_ID { #AFE_Group_Control-Group_ID }

Desired group ID for the device

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_DC_droop_control"></a>
## AFE_DC_droop_control { #AFE_DC_droop_control }


| * | * |
|---|---|
| **Frame ID** | 0x7004d |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set parameters for DC Droop control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Enable | 1 | Single bit |
| Multiplex_Index | 8 | Unsigned |
| Reserved | 16 | Unsigned |
| Droop_resistance_positive_current | 16 | Unsigned |
| Droop_resistance_negative_current | 16 | Unsigned |
| Droop_voltage_offset | 16 | Signed |

### Payload description

#### Enable { #AFE_DC_droop_control-Enable }

Flag to enable droop. If enabled, the voltage Setpoint
          will be modified according to the following equation:
          Vref&#x27; = Vref - I*Rdroop. Droop is disabled by default upon
          power cycle.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Multiplex_Index { #AFE_DC_droop_control-Multiplex_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Reserved { #AFE_DC_droop_control-Reserved }

Reserved for future use. Makes it possible to Enable or
              Disable DC droop without affecting resistance values

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | - | 1 | 0 |  |  |

#### Droop_resistance_positive_current { #AFE_DC_droop_control-Droop_resistance_positive_current }

Virtual droop resistance in Ohms when current is positive. Its default
              value after power cycling is 1 Ohm for VA08,VA01 and VA04 variants, and 3 Ohm for VA03
              variant.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Droop_resistance_negative_current { #AFE_DC_droop_control-Droop_resistance_negative_current }

Virtual droop resistance in Ohms when current is negative. Its default
                value after power cycling is 1 Ohm for VA08,VA01 and VA04 variants, and 3 Ohm for VA03
                variant.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Droop_voltage_offset { #AFE_DC_droop_control-Droop_voltage_offset }

Direct voltage offset on the voltage reference.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.001 | 0 | -30 | 30 |


<a id="AFE_DC_setpoint_control"></a>
## AFE_DC_setpoint_control { #AFE_DC_setpoint_control }


| * | * |
|---|---|
| **Frame ID** | 0x7004e |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Control of the setpoints in DC/DC modes (buck and boost)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Setpoint | 16 | Unsigned |
| positive_current_limit | 16 | Signed |
| negative_current_limit | 16 | Signed |

### Payload description

#### Voltage_Setpoint { #AFE_DC_setpoint_control-Voltage_Setpoint }

The voltage setpoint in DC/DC modes. This message is an alternate way of defining the &#x27;normal&#x27; voltage setpoint, but only applies in DC/DC modes. In boost mode this value needs to be larger than the low side voltage at all times.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### positive_current_limit { #AFE_DC_setpoint_control-positive_current_limit }

The current limit for current in forward direction (DC-&gt;Phases in Buck, Phases-&gt;DC in Boost), this limit applies to the phase side currents

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | 0 | 150 |

#### negative_current_limit { #AFE_DC_setpoint_control-negative_current_limit }

The current limit in reverse direction. (Phases-&gt;DC in Buck, DC-&gt;Phases in Boost) This limit applies to the phase side currents

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 | -150 | 0 |


<a id="AFE_Power_Limit_Control"></a>
## AFE_Power_Limit_Control { #AFE_Power_Limit_Control }


| * | * |
|---|---|
| **Frame ID** | 0x7004f |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Power limit control in DC/DC buck and boost modes.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_power_limit | 16 | Signed |
| Negative_power_limit | 16 | Signed |

### Payload description

#### Positive_power_limit { #AFE_Power_Limit_Control-Positive_power_limit }

Sets the positive power limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |

#### Negative_power_limit { #AFE_Power_Limit_Control-Negative_power_limit }

Sets the negative power limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | W | 10 | 0 |  |  |


<a id="AFE_Fault_Control"></a>
## AFE_Fault_Control { #AFE_Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70050 |
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
| Trip_Interlock | 1 | Single bit |

### Payload description

#### Clear_Interlock { #AFE_Fault_Control-Clear_Interlock }

Clears the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor { #AFE_Fault_Control-Reset_Processor }

Reset the converter DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock { #AFE_Fault_Control-Trip_Interlock }

Trip the inetrnal Interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="AFE_Inverter_Droop_Control"></a>
## AFE_Inverter_Droop_Control { #AFE_Inverter_Droop_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70051 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

This message is used to define the droop characteristics of the module in Inverter 3-Phase operation. The droop curve for both voltage and frequency is
             defined as a symetric 3 linear segments. The &#x27;nominal&#x27; segment is defined solely
             by the slope (it intersects the zero). Then the other two segments, called
             &#x27;auxiliary&#x27; are symetric around the zero, and they are defined by an intersection
             point and another slope. For more info, check the user manual.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Freq_droop_nominal | 16 | Signed |
| Volt_droop_nominal | 16 | Signed |
| Reserved | 16 | Unsigned |
| Virtual_Impedance | 16 | Signed |
| Parameter_Index | 16 | Unsigned |
| Disable_Harmonic_Compensation | 1 | Single bit |
| Enable_Integral_Action | 1 | Single bit |
| Enable_Legacy_Mode | 1 | Single bit |
| Enable_Droop | 1 | Single bit |

### Payload description

#### Freq_droop_nominal { #AFE_Inverter_Droop_Control-Freq_droop_nominal }

Sets the nominal droop slope for the Frequency in Hz/MW. By default
                   (i.e: after power cycle), this value is 40 Hz/MW

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | Hz/MW | 0.01 | 0 |  |  |

#### Volt_droop_nominal { #AFE_Inverter_Droop_Control-Volt_droop_nominal }

Sets the nominal droop slope for the Voltage in V/MVAr. By default
                   (i.e: after power cycle), this value is 630 V/MVAr

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V/MVAr | 0.1 | 0 |  |  |

#### Reserved { #AFE_Inverter_Droop_Control-Reserved }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Virtual_Impedance { #AFE_Inverter_Droop_Control-Virtual_Impedance }

Sets the inductive virtual impedance in microhenries (uH). By default
                   (i.e: after power cycle), this value is 8000 uH

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | uH | 1 | 0 |  |  |

#### Parameter_Index { #AFE_Inverter_Droop_Control-Parameter_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Disable_Harmonic_Compensation { #AFE_Inverter_Droop_Control-Disable_Harmonic_Compensation }

Set this flag when harmonic compensation needs to be disabled (i.e, when
               the module is connected in parallel to the grid or to other diesel generators).
               Harmonic compensation is enabled by default on startup.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_Integral_Action { #AFE_Inverter_Droop_Control-Enable_Integral_Action }

Enable integral action for the Power loops. Enable this only if connected
               to the utility grid. If you go off-grid, this bit must be immediately cleared.
               This is disabled by default on startup.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_Legacy_Mode { #AFE_Inverter_Droop_Control-Enable_Legacy_Mode }

If legacy mode is enabled, module will behave as previous to the
               introduction of the droop feature. It will generate the AC waveform in
               open loop, and will not be able to be paralleled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_Droop { #AFE_Inverter_Droop_Control-Enable_Droop }

Enables droop control extension for INVERTER_1PH_SYNC control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 35 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="AFE_Firmware_Dev"></a>
## AFE_Firmware_Dev { #AFE_Firmware_Dev }


| * | * |
|---|---|
| **Frame ID** | 0x70052 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Used for firmware development

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Flag | 1 | Single bit |
| U16 | 16 | Unsigned |
| I16 | 16 | Signed |
| U32 | 32 | Unsigned |
| I32 | 32 | Signed |
| F32 | 32 | Unsigned |
| Data_Type | 4 | Unsigned |
| Index | 12 | Unsigned |

### Payload description

#### Flag { #AFE_Firmware_Dev-Flag }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### U16 { #AFE_Firmware_Dev-U16 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### I16 { #AFE_Firmware_Dev-I16 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed |  | 1 | 0 |  |  |

#### U32 { #AFE_Firmware_Dev-U32 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Unsigned |  | 1 | 0 |  |  |

#### I32 { #AFE_Firmware_Dev-I32 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed |  | 1 | 0 |  |  |

#### F32 { #AFE_Firmware_Dev-F32 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Unsigned |  | 1 | 0 |  |  |

#### Data_Type { #AFE_Firmware_Dev-Data_Type }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 4 | Unsigned |  | 1 | 0 |  |  |

#### Index { #AFE_Firmware_Dev-Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 12 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Power_Limit_Control_Readback"></a>
## AFE_Power_Limit_Control_Readback { #AFE_Power_Limit_Control_Readback }


| * | * |
|---|---|
| **Frame ID** | 0x7005f |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_power_limit | 16 | Signed |
| Negative_power_limit | 16 | Signed |

### Payload description

#### Positive_power_limit { #AFE_Power_Limit_Control_Readback-Positive_power_limit }

Sets the positive power limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |

#### Negative_power_limit { #AFE_Power_Limit_Control_Readback-Negative_power_limit }

Sets the negative power limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | W | 10 | 0 |  |  |


<a id="AFE_Keep_Alive"></a>
## AFE_Keep_Alive { #AFE_Keep_Alive }


| * | * |
|---|---|
| **Frame ID** | 0x70060 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Keep alive ping message.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Keep_Alive_Enable | 8 | Unsigned |

### Payload description

#### Keep_Alive_Enable { #AFE_Keep_Alive-Keep_Alive_Enable }

If set to 1, module will expect to receive this message every second repeatedly, or it will stop operation

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_System_Flags_Control"></a>
## AFE_System_Flags_Control { #AFE_System_Flags_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70061 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Control the system flags

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Factory_mode | 1 | Single bit |
| Silent_CAN_mode | 1 | Single bit |
| Disable_3rd_harmonic | 1 | Single bit |
| Enable_current_limit_setpoints | 1 | Single bit |
| Enable_voltage_setpoint_as_difference | 1 | Single bit |
| Enable_VF_droop_mode | 1 | Single bit |
| Enable_PQ_droop_mode | 1 | Single bit |
| Enable_DC_droop_mode | 1 | Single bit |
| Legacy_DC_control | 1 | Single bit |
| Enable_high_side_current_setpoint | 1 | Single bit |
| Enable_DC_power_limits | 1 | Single bit |
| Differential_power | 1 | Single bit |

### Payload description

#### Factory_mode { #AFE_System_Flags_Control-Factory_mode }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Silent_CAN_mode { #AFE_System_Flags_Control-Silent_CAN_mode }

Customers MUST NOT USE this bit. If set to 1, module will enter in factory mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Disable_3rd_harmonic { #AFE_System_Flags_Control-Disable_3rd_harmonic }

If set to true, then the module will not do 3rd harmonic injection. This only
       has an effect in Rectifier 3-phase mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_current_limit_setpoints { #AFE_System_Flags_Control-Enable_current_limit_setpoints }

When enabled, 3-phase rectifier, DC/DC buck, and DC/DC boost control modes will use negative current setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_voltage_setpoint_as_difference { #AFE_System_Flags_Control-Enable_voltage_setpoint_as_difference }

When enabled, voltage setpoint means relative difference to input voltage in DC/DC buck and boost control modes.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_VF_droop_mode { #AFE_System_Flags_Control-Enable_VF_droop_mode }

Enables V-f droop in inverter control modes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_PQ_droop_mode { #AFE_System_Flags_Control-Enable_PQ_droop_mode }

Enables P-Q droop in inverter control modes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_DC_droop_mode { #AFE_System_Flags_Control-Enable_DC_droop_mode }

Enables droop in DC/DC and rectifier modes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |

#### Legacy_DC_control { #AFE_System_Flags_Control-Legacy_DC_control }

Legacy control for DC/DC modes (buck and boost)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_high_side_current_setpoint { #AFE_System_Flags_Control-Enable_high_side_current_setpoint }

Current setpoint is give for the high side (DC link)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### Enable_DC_power_limits { #AFE_System_Flags_Control-Enable_DC_power_limits }

Enables power limits in DC/DC Buck and Boost modes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Single bit |  | 1 | 0 |  |  |

#### Differential_power { #AFE_System_Flags_Control-Differential_power }

Power measurements and setpoints are calculated using differential voltage (high-side minus low-side voltage)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="AFE_Rectifier_Setpoint_Control"></a>
## AFE_Rectifier_Setpoint_Control { #AFE_Rectifier_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x70070 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Additional voltage and current setpoints in single-phase rectifier and inverter control modes.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_setpoint_2 | 16 | Unsigned |
| Current_setpoint_2 | 16 | Signed |

### Payload description

#### Voltage_setpoint_2 { #AFE_Rectifier_Setpoint_Control-Voltage_setpoint_2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Current_setpoint_2 { #AFE_Rectifier_Setpoint_Control-Current_setpoint_2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | -150 | 150 |


<a id="AFE_CAN_API_Version"></a>
## AFE_CAN_API_Version { #AFE_CAN_API_Version }


| * | * |
|---|---|
| **Frame ID** | 0x700f3 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

This message declares the version of the API that is provided by the converter. The version follows semver conventsion.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Major | 8 | Unsigned |
| Minor | 8 | Unsigned |
| Patch | 8 | Unsigned |

### Payload description

#### Major { #AFE_CAN_API_Version-Major }

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Minor { #AFE_CAN_API_Version-Minor }

The Minor version number. This number increases if there are backwards compatible changes, like new messages or the use of previously reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Patch { #AFE_CAN_API_Version-Patch }

The Patch number. This number increases when changes to descriptions and documentation/comments are made

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Identification"></a>
## AFE_Identification { #AFE_Identification }


| * | * |
|---|---|
| **Frame ID** | 0x78000 |
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

#### Device_type { #AFE_Identification-Device_type }

The device identification field, uniquely identifies the sender in the network

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| AFE | 7 |

#### HW_revision { #AFE_Identification-HW_revision }

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### HW_variant { #AFE_Identification-HW_variant }

The DSP firmware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_position { #AFE_Identification-Stack_position }

Position of the module within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number { #AFE_Identification-SN_number }

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_FwInfo"></a>
## AFE_FwInfo { #AFE_FwInfo }


| * | * |
|---|---|
| **Frame ID** | 0x78001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

The Info about the firmware running on the AFE

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

#### FW_revision_0 { #AFE_FwInfo-FW_revision_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 { #AFE_FwInfo-FW_revision_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 { #AFE_FwInfo-FW_datecode_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 { #AFE_FwInfo-FW_datecode_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 { #AFE_FwInfo-FW_revision_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 { #AFE_FwInfo-FW_revision_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 { #AFE_FwInfo-FW_datecode_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 { #AFE_FwInfo-FW_datecode_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 { #AFE_FwInfo-FW_revision_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 { #AFE_FwInfo-FW_revision_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 { #AFE_FwInfo-FW_datecode_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 { #AFE_FwInfo-FW_datecode_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 { #AFE_FwInfo-FW_revision_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 { #AFE_FwInfo-FW_revision_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 { #AFE_FwInfo-FW_datecode_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 { #AFE_FwInfo-FW_datecode_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 { #AFE_FwInfo-FW_revision_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 { #AFE_FwInfo-FW_revision_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 { #AFE_FwInfo-FW_datecode_4 }

Character 4

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 { #AFE_FwInfo-FW_datecode_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 { #AFE_FwInfo-FW_revision_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 { #AFE_FwInfo-FW_revision_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 { #AFE_FwInfo-FW_datecode_5 }

Character 5

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 { #AFE_FwInfo-FW_datecode_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 { #AFE_FwInfo-FW_revision_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 { #AFE_FwInfo-FW_revision_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 { #AFE_FwInfo-FW_datecode_6 }

Character 6

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 { #AFE_FwInfo-FW_datecode_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_info_mux { #AFE_FwInfo-FW_info_mux }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Debug"></a>
## AFE_Debug { #AFE_Debug }


| * | * |
|---|---|
| **Frame ID** | 0x78002 |
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

#### Status_Error_Code { #AFE_Debug-Status_Error_Code }

Main status / error code as defined in errno/errno.h

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_1 { #AFE_Debug-Data_1 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_2 { #AFE_Debug-Data_2 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_3 { #AFE_Debug-Data_3 }

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Currents"></a>
## AFE_Currents { #AFE_Currents }


| * | * |
|---|---|
| **Frame ID** | 0x78003 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Current of flowing in U/L1, V/L2, W/L3

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |

### Payload description

#### Phase_U { #AFE_Currents-Phase_U }

Current flowing through the Inductor of Phase U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_V { #AFE_Currents-Phase_V }

Current flowing through the Inductor of Phase V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_W { #AFE_Currents-Phase_W }

Current flowing through the Inductor of Phase W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="AFE_Voltages"></a>
## AFE_Voltages { #AFE_Voltages }


| * | * |
|---|---|
| **Frame ID** | 0x78004 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 10 |
| **Direction** |  |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |
| DC | 16 | Signed |

### Payload description

#### Phase_U { #AFE_Voltages-Phase_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Phase_V { #AFE_Voltages-Phase_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Phase_W { #AFE_Voltages-Phase_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 |  |  |

#### DC { #AFE_Voltages-DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="AFE_Temperatures"></a>
## AFE_Temperatures { #AFE_Temperatures }


| * | * |
|---|---|
| **Frame ID** | 0x78005 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readouts of the module temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Temp_Bridge | 16 | Signed |
| Temp_Inductors | 16 | Signed |

### Payload description

#### Temp_Bridge { #AFE_Temperatures-Temp_Bridge }

Temperature of the MOSFET block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Inductors { #AFE_Temperatures-Temp_Inductors }

Temperature of the inductors

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | °C | 0.01 | 0 |  |  |


<a id="AFE_Faults"></a>
## AFE_Faults { #AFE_Faults }


| * | * |
|---|---|
| **Frame ID** | 0x78006 |
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
| Phase_U_overcurrent | 1 | Label set |
| Phase_U_overvoltage | 1 | Label set |
| Phase_U_undervoltage | 1 | Label set |
| Phase_V_overvoltage | 1 | Label set |
| Phase_V_undervoltage | 1 | Label set |
| Phase_V_overcurrent | 1 | Label set |
| Phase_W_overvoltage | 1 | Label set |
| Phase_W_undervoltage | 1 | Label set |
| Phase_W_overcurrent | 1 | Label set |
| DC_undervoltage | 1 | Label set |
| DC_overvoltage | 1 | Label set |
| MOSFET_overtemperature | 1 | Label set |
| Inductor_overtemperature | 1 | Label set |
| Keep_Alive_not_served | 1 | Label set |
| PLL_not_locked | 1 | Label set |
| NFO | 1 | Label set |
| Measurement_system_failure | 1 | Label set |
| EEPROM_failure | 1 | Label set |
| System | 1 | Label set |

### Payload description

#### Protection_trip_internal { #AFE_Faults-Protection_trip_internal }

The hardware protection of this module has been triggered by an overcurrent/overvoltage contdition

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Protection_trip_external { #AFE_Faults-Protection_trip_external }

The hardware protection of this module has been triggered by a signal coming from other modules in the system

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_U_overcurrent { #AFE_Faults-Phase_U_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_U_overvoltage { #AFE_Faults-Phase_U_overvoltage }

Indicates an overvoltage event on Phase U. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_U_undervoltage { #AFE_Faults-Phase_U_undervoltage }

Indicates an undervoltage event on Phase U. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_V_overvoltage { #AFE_Faults-Phase_V_overvoltage }

Indicates an overvoltage event on Phase V. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_V_undervoltage { #AFE_Faults-Phase_V_undervoltage }

Indicates an undervoltage event on Phase U. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_V_overcurrent { #AFE_Faults-Phase_V_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_W_overvoltage { #AFE_Faults-Phase_W_overvoltage }

Indicates an overvoltage event on Phase U. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_W_undervoltage { #AFE_Faults-Phase_W_undervoltage }

Indicates an undervoltage event on Phase U. The overvoltage event is triggered when the measured phase voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Phase_W_overcurrent { #AFE_Faults-Phase_W_overcurrent }

Indicates an overcurrent event on Phase U. The overcurrent event is triggered when the measured phase current is over the programmed current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### DC_undervoltage { #AFE_Faults-DC_undervoltage }

DC bus undervoltage condition. The undervoltage condition is asserted when the measured dc bus voltage is under the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### DC_overvoltage { #AFE_Faults-DC_overvoltage }

DC bus overvoltage condition. The overvoltage condition is asserted when the measured dc bus voltage is over the programmed voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### MOSFET_overtemperature { #AFE_Faults-MOSFET_overtemperature }

This flag is asserted when the temperature of the MOSFET block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Inductor_overtemperature { #AFE_Faults-Inductor_overtemperature }

This flag is asserted when the temperature of the inductor block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Keep_Alive_not_served { #AFE_Faults-Keep_Alive_not_served }

The Keep Alive feature is enabled but it was not served with the periodic message.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |

#### PLL_not_locked { #AFE_Faults-PLL_not_locked }

Flag asserted when in rectifier modes, the PLL went out of lock condition

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |

#### NFO { #AFE_Faults-NFO }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |

#### Measurement_system_failure { #AFE_Faults-Measurement_system_failure }

The voltages/currents measurement system is malfunctionning, and readouts are not guaranteed to be accurate.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |

#### EEPROM_failure { #AFE_Faults-EEPROM_failure }

The configuration EEPROM failed to load or save the module configuration.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |

#### System { #AFE_Faults-System }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| fault | 1 |


<a id="AFE_Status"></a>
## AFE_Status { #AFE_Status }


| * | * |
|---|---|
| **Frame ID** | 0x78007 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Status bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Running | 1 | Single bit |
| PWM | 1 | Single bit |
| Current_dc_loop_mode | 1 | Single bit |
| Current_ac_loop_mode | 1 | Single bit |
| Buck | 1 | Single bit |
| Boost | 1 | Single bit |
| Precharge_dc_buck_mode | 1 | Single bit |
| Precharge_dc_boost_mode | 1 | Single bit |
| Rectifier_3ph | 1 | Single bit |
| Stack_mode | 1 | Single bit |
| Master | 1 | Single bit |
| Slave | 1 | Single bit |
| Inverter_1ph | 1 | Single bit |
| Boost_Neutral | 1 | Single bit |
| Rectifier_1ph | 1 | Single bit |
| Inverter_3ph | 1 | Single bit |
| Ready | 1 | Single bit |
| Inverter_1ph_Sync | 1 | Single bit |
| Neutral | 1 | Single bit |
| Rectifier_1ph_Buck | 1 | Single bit |
| Inverter_1ph_Boost | 1 | Single bit |
| Rectifier_distributed | 1 | Single bit |
| MPPT_buck | 1 | Single bit |
| MPPT_boost | 1 | Single bit |
| Buck_2p_float | 1 | Single bit |
| Inverter_1ph_Distributed | 1 | Single bit |

### Payload description

#### Running { #AFE_Status-Running }

Indicates if converter is running.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM { #AFE_Status-PWM }

Indicates if converter is in PWM control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Current_dc_loop_mode { #AFE_Status-Current_dc_loop_mode }

Indicates if the current DC loop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Current_ac_loop_mode { #AFE_Status-Current_ac_loop_mode }

Indicates if the current AC loop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Buck { #AFE_Status-Buck }

Indicates if converter is in buck control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### Boost { #AFE_Status-Boost }

Indicates if converter is in boost control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### Precharge_dc_buck_mode { #AFE_Status-Precharge_dc_buck_mode }

Indicates if the precharge DC mode is enabled - buck direction.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |

#### Precharge_dc_boost_mode { #AFE_Status-Precharge_dc_boost_mode }

Indicates if the precharge DC mode is enabled - boost direction.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_3ph { #AFE_Status-Rectifier_3ph }

Indicates if converter is in three-phase rectifier control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |

#### Stack_mode { #AFE_Status-Stack_mode }

Indicates if converter is operating in stack mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Single bit |  | 1 | 0 |  |  |

#### Master { #AFE_Status-Master }

Indicates if converter is master in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Single bit |  | 1 | 0 |  |  |

#### Slave { #AFE_Status-Slave }

Indicates if converter is slave in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph { #AFE_Status-Inverter_1ph }

Indicates if converter is in single-phase inverter control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Single bit |  | 1 | 0 |  |  |

#### Boost_Neutral { #AFE_Status-Boost_Neutral }

Indicates if converter is in boost control mode with neutral generation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_1ph { #AFE_Status-Rectifier_1ph }

Indicates if converter is in single-phase rectifier control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_3ph { #AFE_Status-Inverter_3ph }

Indicates if converter is in three-phase inverter control mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Single bit |  | 1 | 0 |  |  |

#### Ready { #AFE_Status-Ready }

Indicates if converter is ready for operation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Sync { #AFE_Status-Inverter_1ph_Sync }

Single-phase inverter control mode with phase synchronization.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Single bit |  | 1 | 0 |  |  |

#### Neutral { #AFE_Status-Neutral }

Open-loop neutral generation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_1ph_Buck { #AFE_Status-Rectifier_1ph_Buck }

Single-phase rectifier with buck on one leg.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Boost { #AFE_Status-Inverter_1ph_Boost }

Single-phase inverter with boost on one leg.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Single bit |  | 1 | 0 |  |  |

#### Rectifier_distributed { #AFE_Status-Rectifier_distributed }

Not available at the moment

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Single bit |  | 1 | 0 |  |  |

#### MPPT_buck { #AFE_Status-MPPT_buck }

Not available at the moment

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Single bit |  | 1 | 0 |  |  |

#### MPPT_boost { #AFE_Status-MPPT_boost }

Not available at the moment

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Single bit |  | 1 | 0 |  |  |

#### Buck_2p_float { #AFE_Status-Buck_2p_float }

Buck in phases L1 and L2. Phase L3 is left floating (high impedance)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Single bit |  | 1 | 0 |  |  |

#### Inverter_1ph_Distributed { #AFE_Status-Inverter_1ph_Distributed }

Single-phase inverter mode  distributed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="AFE_Setpoints_PWM_Duty"></a>
## AFE_Setpoints_PWM_Duty { #AFE_Setpoints_PWM_Duty }


| * | * |
|---|---|
| **Frame ID** | 0x78008 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Setpoints for the PWM Mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Unsigned |
| Phase_V | 16 | Unsigned |
| Phase_W | 16 | Unsigned |

### Payload description

#### Phase_U { #AFE_Setpoints_PWM_Duty-Phase_U }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | % | 0.001526 | 0 |  |  |

#### Phase_V { #AFE_Setpoints_PWM_Duty-Phase_V }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | % | 0.001526 | 0 |  |  |

#### Phase_W { #AFE_Setpoints_PWM_Duty-Phase_W }

The actual PWM duty cycle setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | % | 0.001526 | 0 |  |  |


<a id="AFE_Setpoints"></a>
## AFE_Setpoints { #AFE_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x78009 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_setpoint | 16 | Signed |
| Voltage_setpoint | 16 | Unsigned |
| Frequency_setpoint | 16 | Unsigned |

### Payload description

#### Current_setpoint { #AFE_Setpoints-Current_setpoint }

The actual current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Voltage_setpoint { #AFE_Setpoints-Voltage_setpoint }

The actual voltage setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Frequency_setpoint { #AFE_Setpoints-Frequency_setpoint }

The actual frequency setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |


<a id="AFE_Voltages_RMS"></a>
## AFE_Voltages_RMS { #AFE_Voltages_RMS }


| * | * |
|---|---|
| **Frame ID** | 0x7800a |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Unsigned |
| Phase_V | 16 | Unsigned |
| Phase_W | 16 | Unsigned |

### Payload description

#### Phase_U { #AFE_Voltages_RMS-Phase_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Phase_V { #AFE_Voltages_RMS-Phase_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Phase_W { #AFE_Voltages_RMS-Phase_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | V | 0.1 | 0 |  |  |


<a id="AFE_Currents_RMS"></a>
## AFE_Currents_RMS { #AFE_Currents_RMS }


| * | * |
|---|---|
| **Frame ID** | 0x7800b |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

RMS Current of phases U, V, W

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Unsigned |
| Phase_V | 16 | Unsigned |
| Phase_W | 16 | Unsigned |

### Payload description

#### Phase_U { #AFE_Currents_RMS-Phase_U }

RMS Phase current is the MOSFET loop current, in the branch U of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | A | 0.01 | 0 |  |  |

#### Phase_V { #AFE_Currents_RMS-Phase_V }

RMS Phase current is the MOSFET loop current, in the branch V of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.01 | 0 |  |  |

#### Phase_W { #AFE_Currents_RMS-Phase_W }

RMS Phase current is the MOSFET loop current, in the branch W of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.01 | 0 |  |  |


<a id="AFE_Mains"></a>
## AFE_Mains { #AFE_Mains }


| * | * |
|---|---|
| **Frame ID** | 0x7800c |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Three-Phase mains health (frequency, phase...)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency | 16 | Unsigned |
| Phase | 16 | Signed |

### Payload description

#### Frequency { #AFE_Mains-Frequency }

Frequency of Three-Phase system

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |

#### Phase { #AFE_Mains-Phase }

Phase of Three-Phase system

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Deg. | 0.1 | 0 |  |  |


<a id="_AFE_Boot_FwInfo"></a>
## _AFE_Boot_FwInfo { #_AFE_Boot_FwInfo }


| * | * |
|---|---|
| **Frame ID** | 0x7800d |
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

#### FW_revision_0 { #_AFE_Boot_FwInfo-FW_revision_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 { #_AFE_Boot_FwInfo-FW_revision_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 { #_AFE_Boot_FwInfo-FW_datecode_0 }

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 { #_AFE_Boot_FwInfo-FW_datecode_7 }

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 { #_AFE_Boot_FwInfo-FW_revision_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 { #_AFE_Boot_FwInfo-FW_revision_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 { #_AFE_Boot_FwInfo-FW_datecode_1 }

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 { #_AFE_Boot_FwInfo-FW_datecode_8 }

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 { #_AFE_Boot_FwInfo-FW_revision_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 { #_AFE_Boot_FwInfo-FW_revision_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 { #_AFE_Boot_FwInfo-FW_datecode_2 }

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 { #_AFE_Boot_FwInfo-FW_datecode_9 }

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 { #_AFE_Boot_FwInfo-FW_revision_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 { #_AFE_Boot_FwInfo-FW_revision_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 { #_AFE_Boot_FwInfo-FW_datecode_3 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 { #_AFE_Boot_FwInfo-FW_datecode_10 }

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 { #_AFE_Boot_FwInfo-FW_revision_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 { #_AFE_Boot_FwInfo-FW_revision_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 { #_AFE_Boot_FwInfo-FW_datecode_4 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 { #_AFE_Boot_FwInfo-FW_datecode_11 }

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 { #_AFE_Boot_FwInfo-FW_revision_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 { #_AFE_Boot_FwInfo-FW_revision_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 { #_AFE_Boot_FwInfo-FW_datecode_5 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 { #_AFE_Boot_FwInfo-FW_datecode_12 }

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 { #_AFE_Boot_FwInfo-FW_revision_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 { #_AFE_Boot_FwInfo-FW_revision_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 { #_AFE_Boot_FwInfo-FW_datecode_6 }

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 { #_AFE_Boot_FwInfo-FW_datecode_13 }

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Boot_FW_info_mux { #_AFE_Boot_FwInfo-Boot_FW_info_mux }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="_AFE_Broadcast"></a>
## _AFE_Broadcast { #_AFE_Broadcast }


| * | * |
|---|---|
| **Frame ID** | 0x7800e |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 10 |
| **Direction** |  |

### Description

All AFEs will listen to this message

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 5 | Unsigned |
| Group_ID | 3 | Unsigned |
| Phase_U | 16 | Signed |
| Phase | 16 | Unsigned |
| Phase_V | 16 | Signed |
| Voltage | 16 | Signed |
| Phase_W | 16 | Signed |
| Diagnostics_Index | 8 | Unsigned |

### Payload description

#### Stack_position { #_AFE_Broadcast-Stack_position }

Sender Stack position

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 5 | Unsigned |  | 1 | 0 |  |  |

#### Group_ID { #_AFE_Broadcast-Group_ID }

Sender Group ID

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 3 | Unsigned |  | 1 | 0 |  |  |

#### Phase_U { #_AFE_Broadcast-Phase_U }

Phase current is the MOSFET loop current, in the branch U of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase { #_AFE_Broadcast-Phase }

Phase sampled on low-latency trigger (rad)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 16 | Unsigned | rad | 0.0001 | 0 |  |  |

#### Phase_V { #_AFE_Broadcast-Phase_V }

Phase current is the MOSFET loop current, in the branch V of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Voltage { #_AFE_Broadcast-Voltage }

Output from Q/V droop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Signed | V | 0.01 | 0 |  |  |

#### Phase_W { #_AFE_Broadcast-Phase_W }

Phase current is the MOSFET loop current, in the branch W of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Diagnostics_Index { #_AFE_Broadcast-Diagnostics_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Group_Info"></a>
## AFE_Group_Info { #AFE_Group_Info }


| * | * |
|---|---|
| **Frame ID** | 0x7800f |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID | 8 | Unsigned |

### Payload description

#### Group_ID { #AFE_Group_Info-Group_ID }

Group ID of the device

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_DC_Bus_current"></a>
## AFE_DC_Bus_current { #AFE_DC_Bus_current }


| * | * |
|---|---|
| **Frame ID** | 0x78010 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Current of of the DC Bus, this is a calculated value using the phase currents and voltage difference accross the converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Bus_current | 16 | Signed |

### Payload description

#### Bus_current { #AFE_DC_Bus_current-Bus_current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="AFE_AC_Power"></a>
## AFE_AC_Power { #AFE_AC_Power }


| * | * |
|---|---|
| **Frame ID** | 0x78011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

AC measured power (only for Inverter modes)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| P_u | 16 | Signed |
| Q_u | 16 | Signed |
| P_total | 16 | Signed |
| P_v | 16 | Signed |
| Q_v | 16 | Signed |
| Q_total | 16 | Signed |
| P_w | 16 | Signed |
| Q_w | 16 | Signed |
| Index | 8 | Unsigned |

### Payload description

#### P_u { #AFE_AC_Power-P_u }

Active power in phase U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |

#### Q_u { #AFE_AC_Power-Q_u }

Reactive power in phase U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |

#### P_total { #AFE_AC_Power-P_total }

Total active power (W)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 1 | 0 |  |  |

#### P_v { #AFE_AC_Power-P_v }

Active power in phase V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | W | 10 | 0 |  |  |

#### Q_v { #AFE_AC_Power-Q_v }

Reactive power in phase V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | W | 10 | 0 |  |  |

#### Q_total { #AFE_AC_Power-Q_total }

Total reactive power (VAr)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | VAr | 1 | 0 |  |  |

#### P_w { #AFE_AC_Power-P_w }

Active power in phase W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 10 | 0 |  |  |

#### Q_w { #AFE_AC_Power-Q_w }

Reactive power in phase W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 10 | 0 |  |  |

#### Index { #AFE_AC_Power-Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_DC_Power"></a>
## AFE_DC_Power { #AFE_DC_Power }


| * | * |
|---|---|
| **Frame ID** | 0x78012 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 10 |
| **Direction** |  |

### Description

DC measured power

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| DC_Power | 16 | Signed |

### Payload description

#### DC_Power { #AFE_DC_Power-DC_Power }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | W | 10 | 0 |  |  |


<a id="_AFE_Currents_Raw"></a>
## _AFE_Currents_Raw { #_AFE_Currents_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x78020 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Raw ADC values of the ADC channels connected to the current sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |

### Payload description

#### Phase_U { #_AFE_Currents_Raw-Phase_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed |  | 1 | 0 |  |  |

#### Phase_V { #_AFE_Currents_Raw-Phase_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed |  | 1 | 0 |  |  |

#### Phase_W { #_AFE_Currents_Raw-Phase_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed |  | 1 | 0 |  |  |


<a id="_AFE_Voltages_Raw"></a>
## _AFE_Voltages_Raw { #_AFE_Voltages_Raw }


| * | * |
|---|---|
| **Frame ID** | 0x78021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Raw ADC values of the channels connected to the voltage sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |
| DC | 16 | Signed |

### Payload description

#### Phase_U { #_AFE_Voltages_Raw-Phase_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | LSB | 1 | 0 |  |  |

#### Phase_V { #_AFE_Voltages_Raw-Phase_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | LSB | 1 | 0 |  |  |

#### Phase_W { #_AFE_Voltages_Raw-Phase_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | LSB | 1 | 0 |  |  |

#### DC { #_AFE_Voltages_Raw-DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | LSB | 1 | 0 |  |  |


<a id="AFE_Droop_setpoints"></a>
## AFE_Droop_setpoints { #AFE_Droop_setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x78050 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Reads the droop resistance values of user

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_droop | 16 | Unsigned |
| Negative_droop | 16 | Unsigned |
| droop_enable | 1 | Single bit |
| droop_enable_2 | 1 | Single bit |

### Payload description

#### Positive_droop { #AFE_Droop_setpoints-Positive_droop }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Negative_droop { #AFE_Droop_setpoints-Negative_droop }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### droop_enable { #AFE_Droop_setpoints-droop_enable }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Single bit |  | 1 | 0 |  |  |

#### droop_enable_2 { #AFE_Droop_setpoints-droop_enable_2 }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_AFE_Calibration_Adc_Scale"></a>
## _AFE_Calibration_Adc_Scale { #_AFE_Calibration_Adc_Scale }


| * | * |
|---|---|
| **Frame ID** | 0x78051 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc scale (resolution) value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 32 | Float |
| Current_V | 32 | Float |
| Current_W | 32 | Float |
| Voltage_U | 32 | Float |
| Voltage_V | 32 | Float |
| Voltage_W | 32 | Float |
| Voltage_DC | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Adc_Scale-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Adc_Scale-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Adc_Scale-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Adc_Scale-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Adc_Scale-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Adc_Scale-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Adc_Scale-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Adc_Index { #_AFE_Calibration_Adc_Scale-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_AFE_Calibration_Adc_Fs"></a>
## _AFE_Calibration_Adc_Fs { #_AFE_Calibration_Adc_Fs }


| * | * |
|---|---|
| **Frame ID** | 0x78052 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Adc fullscale value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 32 | Float |
| Current_V | 32 | Float |
| Current_W | 32 | Float |
| Voltage_U | 32 | Float |
| Voltage_V | 32 | Float |
| Voltage_W | 32 | Float |
| Voltage_DC | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Adc_Fs-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Adc_Fs-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Adc_Fs-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Adc_Fs-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Adc_Fs-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Adc_Fs-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Adc_Fs-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Adc_Index { #_AFE_Calibration_Adc_Fs-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_AFE_Calibration_Adc_Offset"></a>
## _AFE_Calibration_Adc_Offset { #_AFE_Calibration_Adc_Offset }


| * | * |
|---|---|
| **Frame ID** | 0x78053 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readout of ADC calibration data (offset) from EEPROM.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 16 | Signed |
| Current_V | 16 | Signed |
| Current_W | 16 | Signed |
| Voltage_U | 16 | Signed |
| Voltage_V | 16 | Signed |
| Voltage_W | 16 | Signed |
| Voltage_DC | 16 | Signed |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Adc_Offset-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Adc_Offset-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Adc_Offset-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Adc_Offset-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Adc_Offset-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Adc_Offset-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Adc_Offset-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Adc_Index { #_AFE_Calibration_Adc_Offset-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_AFE_Calibration_Adc_Gain"></a>
## _AFE_Calibration_Adc_Gain { #_AFE_Calibration_Adc_Gain }


| * | * |
|---|---|
| **Frame ID** | 0x78054 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Readout of ADC calibration data (gain) from EEPROM.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U | 16 | Signed |
| Current_V | 16 | Signed |
| Current_W | 16 | Signed |
| Voltage_U | 16 | Signed |
| Voltage_V | 16 | Signed |
| Voltage_W | 16 | Signed |
| Voltage_DC | 16 | Signed |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_U { #_AFE_Calibration_Adc_Gain-Current_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Current_V { #_AFE_Calibration_Adc_Gain-Current_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Current_W { #_AFE_Calibration_Adc_Gain-Current_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_U { #_AFE_Calibration_Adc_Gain-Voltage_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_V { #_AFE_Calibration_Adc_Gain-Voltage_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_W { #_AFE_Calibration_Adc_Gain-Voltage_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Voltage_DC { #_AFE_Calibration_Adc_Gain-Voltage_DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | - | 1 | 0 |  |  |

#### Adc_Index { #_AFE_Calibration_Adc_Gain-Adc_Index }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="AFE_Interlock_Faults"></a>
## AFE_Interlock_Faults { #AFE_Interlock_Faults }


| * | * |
|---|---|
| **Frame ID** | 0x78056 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_U_High | 1 | Label set |
| Current_U_Low | 1 | Label set |
| Current_V_High | 1 | Label set |
| Current_V_Low | 1 | Label set |
| Current_W_High | 1 | Label set |
| Current_W_Low | 1 | Label set |
| Voltage_DC | 1 | Label set |
| Reboot | 1 | Label set |
| Unknown | 1 | Label set |

### Payload description

#### Current_U_High { #AFE_Interlock_Faults-Current_U_High }

This flag is set if a hight current on U tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_U_Low { #AFE_Interlock_Faults-Current_U_Low }

This flag is set if a low current on U tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_V_High { #AFE_Interlock_Faults-Current_V_High }

This flag is set if a hight current on V tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_V_Low { #AFE_Interlock_Faults-Current_V_Low }

This flag is set if a low current on V tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_W_High { #AFE_Interlock_Faults-Current_W_High }

This flag is set if a hight current on W tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_W_Low { #AFE_Interlock_Faults-Current_W_Low }

This flag is set if a low current on W tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_DC { #AFE_Interlock_Faults-Voltage_DC }

This flag is set if a voltage on DC tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Reboot { #AFE_Interlock_Faults-Reboot }

This flag is set if a reboot tripped the internal interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Unknown { #AFE_Interlock_Faults-Unknown }

This flag the reason for the internal interlock is unknown

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |


<a id="AFE_DC_Setpoints"></a>
## AFE_DC_Setpoints { #AFE_DC_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x78069 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_Setpoint | 16 | Unsigned |
| positive_Current_setpoint | 16 | Signed |
| negative_Current_setpoint | 16 | Signed |

### Payload description

#### Voltage_Setpoint { #AFE_DC_Setpoints-Voltage_Setpoint }

The actual negative current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### positive_Current_setpoint { #AFE_DC_Setpoints-positive_Current_setpoint }

The actual negative current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |

#### negative_Current_setpoint { #AFE_DC_Setpoints-negative_Current_setpoint }

The actual negative current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="AFE_Inverter_Droop_Readback"></a>
## AFE_Inverter_Droop_Readback { #AFE_Inverter_Droop_Readback }


| * | * |
|---|---|
| **Frame ID** | 0x78151 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Readback for droop control parameters set in the 0x70051

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Freq_droop_nominal | 16 | Signed |
| Volt_droop_nominal | 16 | Signed |
| Virtual_Impedance | 16 | Signed |

### Payload description

#### Freq_droop_nominal { #AFE_Inverter_Droop_Readback-Freq_droop_nominal }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | Hz/MW | 0.01 | 0 |  |  |

#### Volt_droop_nominal { #AFE_Inverter_Droop_Readback-Volt_droop_nominal }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V/MVAr | 0.1 | 0 |  |  |

#### Virtual_Impedance { #AFE_Inverter_Droop_Readback-Virtual_Impedance }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | uH | 1 | 0 |  |  |
