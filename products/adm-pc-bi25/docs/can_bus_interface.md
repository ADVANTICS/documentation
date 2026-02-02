# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [DAB_Current_Limits](#DAB_Current_Limits) | 0x80030 | 8 | OUT |  |
| [DAB_Phase_Current_Limits](#DAB_Phase_Current_Limits) | 0x80031 | 8 | OUT |  |
| [DAB_Voltage_Limits](#DAB_Voltage_Limits) | 0x80032 | 8 | OUT |  |
| [DAB_Mode_Control](#DAB_Mode_Control) | 0x80040 | 1 | OUT | 100 |
| [_DAB_Calibration_Offset_Update](#_DAB_Calibration_Offset_Update) | 0x80041 | 6 | OUT |  |
| [_DAB_Calibration_Scale_Update](#_DAB_Calibration_Scale_Update) | 0x80042 | 6 | OUT |  |
| [DAB_PWM_Phase_Control](#DAB_PWM_Phase_Control) | 0x80043 | 4 | OUT |  |
| [CLLC_PWM_Frequency_Control](#CLLC_PWM_Frequency_Control) | 0x80044 | 2 | OUT |  |
| [DAB_Stack_Control](#DAB_Stack_Control) | 0x80045 | 6 | OUT |  |
| [DAB_Current_Setpoint_Control](#DAB_Current_Setpoint_Control) | 0x80046 | 4 | OUT | 100 |
| [DAB_Voltage_Setpoint_Control](#DAB_Voltage_Setpoint_Control) | 0x80047 | 2 | OUT | 100 |
| [CLLC_PWM_Gain_Control](#CLLC_PWM_Gain_Control) | 0x80048 | 2 | OUT |  |
| [CLLC_PWM_Phase_Mode](#CLLC_PWM_Phase_Mode) | 0x80049 | 1 | OUT |  |
| [DAB_Group_Control](#DAB_Group_Control) | 0x8004c | 1 | OUT |  |
| [DAB_Fault_Control](#DAB_Fault_Control) | 0x80050 | 1 | OUT |  |
| [EPWM_control](#EPWM_control) | 0x80052 | 8 | OUT |  |
| [DAB_Identification](#DAB_Identification) | 0x88000 | 8 | IN | 1000 |
| [DAB_FwInfo](#DAB_FwInfo) | 0x88001 | 8 | IN | 1000 |
| [DAB_Debug](#DAB_Debug) | 0x88002 | 8 | IN | 1000 |
| [DAB_Status](#DAB_Status) | 0x88003 | 2 | IN | 100 |
| [DAB_Faults](#DAB_Faults) | 0x88004 | 3 | IN | 100 |
| [DAB_Voltages_Currents](#DAB_Voltages_Currents) | 0x88005 | 8 | IN | 100 |
| [DAB_Phase_Currents](#DAB_Phase_Currents) | 0x88006 | 4 | IN | 100 |
| [_DAB_Voltages_Currents_Raw](#_DAB_Voltages_Currents_Raw) | 0x88007 | 8 | IN | 100 |
| [_DAB_Phase_Currents_Raw](#_DAB_Phase_Currents_Raw) | 0x88008 | 8 | IN | 100 |
| [DAB_Temperatures](#DAB_Temperatures) | 0x88009 | 8 | IN | 100 |
| [DAB_Setpoints_PWM_Phase](#DAB_Setpoints_PWM_Phase) | 0x8800a | 4 | IN | 100 |
| [_DAB_Broadcast](#_DAB_Broadcast) | 0x8800e | 8 | OUT | 50 |
| [DAB_Group_Info](#DAB_Group_Info) | 0x8800f | 1 | IN | 1000 |
| [_DAB_Calibration_Adc_Fs](#_DAB_Calibration_Adc_Fs) | 0x88041 | 6 | IN | 1000 |
| [_DAB_Calibration_Adc_Scale](#_DAB_Calibration_Adc_Scale) | 0x88042 | 6 | IN | 1000 |
| [CLLC_PWM_Frequency_value](#CLLC_PWM_Frequency_value) | 0x88048 | 4 | IN | 1000 |
| [Data_test_out](#Data_test_out) | 0x88090 | 1 | IN | 100 |
| [Data_phase_shift](#Data_phase_shift) | 0x88091 | 4 | IN | 100 |
| [DAB_CAN_API_Version](#DAB_CAN_API_Version) | 0x880f3 | 3 | IN | 1000 |


<a id="DAB_Current_Limits"></a>
## DAB_Current_Limits


| * | * |
|---|---|
| **Frame ID** | 0x80030 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_In_Min | 16 | Signed |
| Current_In_Max | 16 | Signed |
| Current_Out_Min | 16 | Signed |
| Current_Out_Max | 16 | Signed |

### Payload description

#### Current_In_Min :id=DAB_Current_Limits-Current_In_Min

Minimum allowable input current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_In_Max :id=DAB_Current_Limits-Current_In_Max

Maximum allowable input current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_Out_Min :id=DAB_Current_Limits-Current_Out_Min

Minimum allowable output current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_Out_Max :id=DAB_Current_Limits-Current_Out_Max

Maximum allowable output current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |


<a id="DAB_Phase_Current_Limits"></a>
## DAB_Phase_Current_Limits


| * | * |
|---|---|
| **Frame ID** | 0x80031 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_In_Min | 16 | Signed |
| Current_In_Max | 16 | Signed |
| Current_Out_Min | 16 | Signed |
| Current_Out_Max | 16 | Signed |

### Payload description

#### Current_In_Min :id=DAB_Phase_Current_Limits-Current_In_Min

Minimum allowable input current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_In_Max :id=DAB_Phase_Current_Limits-Current_In_Max

Maximum allowable input current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_Out_Min :id=DAB_Phase_Current_Limits-Current_Out_Min

Minimum allowable output current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |

#### Current_Out_Max :id=DAB_Phase_Current_Limits-Current_Out_Max

Maximum allowable output current of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | A | 0.01 | 0 | -60 | 60 |


<a id="DAB_Voltage_Limits"></a>
## DAB_Voltage_Limits


| * | * |
|---|---|
| **Frame ID** | 0x80032 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Set the voltage limits (mminimum and maximum)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_In_Min | 16 | Signed |
| Voltage_In_Max | 16 | Signed |
| Voltage_Out_Min | 16 | Signed |
| Voltage_Out_Max | 16 | Signed |

### Payload description

#### Voltage_In_Min :id=DAB_Voltage_Limits-Voltage_In_Min

Minimum allowable input voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 | 0 | 850 |

#### Voltage_In_Max :id=DAB_Voltage_Limits-Voltage_In_Max

Minimum allowable input voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 | 0 | 850 |

#### Voltage_Out_Min :id=DAB_Voltage_Limits-Voltage_Out_Min

Minimum allowable output voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 | 0 | 850 |

#### Voltage_Out_Max :id=DAB_Voltage_Limits-Voltage_Out_Max

Minimum allowable output voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | V | 0.1 | 0 | 0 | 850 |


<a id="DAB_Mode_Control"></a>
## DAB_Mode_Control


| * | * |
|---|---|
| **Frame ID** | 0x80040 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Operation Mode control: sets the converter operation mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Converter_ON | 1 | Single bit |
| PWM_mode_ON | 1 | Single bit |
| DC_DC_mode_ON | 1 | Single bit |
| Voltage_follower_mode_ON | 1 | Single bit |
| PFC_Voltage_mode_ON | 1 | Single bit |
| Gain_mode_on | 1 | Single bit |

### Payload description

#### Converter_ON :id=DAB_Mode_Control-Converter_ON

Enable the converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_mode_ON :id=DAB_Mode_Control-PWM_mode_ON

Enable the PWM mode (this will set the converter in open loop).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### DC_DC_mode_ON :id=DAB_Mode_Control-DC_DC_mode_ON

Enable the DC DC mode (this will set the converter in automatic angle control).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Voltage_follower_mode_ON :id=DAB_Mode_Control-Voltage_follower_mode_ON

This mode will regulate a 1:1 ratio voltage from A to B (A is reference voltage)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### PFC_Voltage_mode_ON :id=DAB_Mode_Control-PFC_Voltage_mode_ON

This mode regulates output (port B) current/voltage while sending voltage commands to an Upstream AFE working as PFC (AC to DC), to ensure a 1:1 voltage ratio.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### Gain_mode_on :id=DAB_Mode_Control-Gain_mode_on

Enable the GAIN mode (this will set the converter in open loop).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="_DAB_Calibration_Offset_Update"></a>
## _DAB_Calibration_Offset_Update


| * | * |
|---|---|
| **Frame ID** | 0x80041 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Update of the calibration table for offsets.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 16 | Signed |
| Current_Side_B | 16 | Signed |
| Current_Phase_Side_A | 16 | Signed |
| Voltage_Side_A | 16 | Signed |
| Voltage_Side_B | 16 | Signed |
| Current_Phase_Side_B | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_Side_A :id=_DAB_Calibration_Offset_Update-Current_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Side_B :id=_DAB_Calibration_Offset_Update-Current_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Phase_Side_A :id=_DAB_Calibration_Offset_Update-Current_Phase_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Side_A :id=_DAB_Calibration_Offset_Update-Voltage_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Side_B :id=_DAB_Calibration_Offset_Update-Voltage_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Phase_Side_B :id=_DAB_Calibration_Offset_Update-Current_Phase_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Calibration_Index :id=_DAB_Calibration_Offset_Update-Calibration_Index

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC :id=_DAB_Calibration_Offset_Update-CRC

Checksum of bytes 0 to 2, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="_DAB_Calibration_Scale_Update"></a>
## _DAB_Calibration_Scale_Update


| * | * |
|---|---|
| **Frame ID** | 0x80042 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Update of the calibration table for scales.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 16 | Signed |
| Current_Side_B | 16 | Signed |
| Current_Phase_Side_A | 16 | Signed |
| Voltage_Side_A | 16 | Signed |
| Voltage_Side_B | 16 | Signed |
| Current_Phase_Side_B | 16 | Signed |
| Calibration_Index | 16 | Unsigned |
| CRC | 16 | Unsigned |

### Payload description

#### Current_Side_A :id=_DAB_Calibration_Scale_Update-Current_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Side_B :id=_DAB_Calibration_Scale_Update-Current_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Phase_Side_A :id=_DAB_Calibration_Scale_Update-Current_Phase_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Side_A :id=_DAB_Calibration_Scale_Update-Voltage_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Voltage_Side_B :id=_DAB_Calibration_Scale_Update-Voltage_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Current_Phase_Side_B :id=_DAB_Calibration_Scale_Update-Current_Phase_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ADC Counts | 1 | 0 |  |  |

#### Calibration_Index :id=_DAB_Calibration_Scale_Update-Calibration_Index

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### CRC :id=_DAB_Calibration_Scale_Update-CRC

Checksum of bytes 0 to 2, CRC-CCITT, corresponding to qChecksum (www.qt.io)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | - | 1 | 0 |  |  |


<a id="DAB_PWM_Phase_Control"></a>
## DAB_PWM_Phase_Control


| * | * |
|---|---|
| **Frame ID** | 0x80043 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

PWM duty cycle control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_A | 16 | Signed |
| Phase_B | 16 | Signed |

### Payload description

#### Phase_A :id=DAB_PWM_Phase_Control-Phase_A

PWM Phase setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ° | 0.003 | 0 |  |  |

#### Phase_B :id=DAB_PWM_Phase_Control-Phase_B

PWM Phase setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | ° | 0.003 | 0 |  |  |


<a id="CLLC_PWM_Frequency_Control"></a>
## CLLC_PWM_Frequency_Control


| * | * |
|---|---|
| **Frame ID** | 0x80044 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

PWM frequency control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| PWM_frequency | 16 | Unsigned |

### Payload description

#### PWM_frequency :id=CLLC_PWM_Frequency_Control-PWM_frequency

Sets the PWM frequency. Active only when the converter is in PWM mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 10 | 0 |  |  |


<a id="DAB_Stack_Control"></a>
## DAB_Stack_Control


| * | * |
|---|---|
| **Frame ID** | 0x80045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

PFC stack control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| Stack_size | 8 | Unsigned |
| SN_number | 32 | Unsigned |

### Payload description

#### Stack_position :id=DAB_Stack_Control-Stack_position

The converter position within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_size :id=DAB_Stack_Control-Stack_size

How many PFC converters are in stack in total

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number :id=DAB_Stack_Control-SN_number

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Current_Setpoint_Control"></a>
## DAB_Current_Setpoint_Control


| * | * |
|---|---|
| **Frame ID** | 0x80046 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Current setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_setpoint | 16 | Signed |
| Negative_Current_setpoint | 16 | Signed |

### Payload description

#### Positive_Current_setpoint :id=DAB_Current_Setpoint_Control-Positive_Current_setpoint

Sets the port B positive current setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -55 | 55 |

#### Negative_Current_setpoint :id=DAB_Current_Setpoint_Control-Negative_Current_setpoint

Sets the port B negative current setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 | -55 | 55 |


<a id="DAB_Voltage_Setpoint_Control"></a>
## DAB_Voltage_Setpoint_Control


| * | * |
|---|---|
| **Frame ID** | 0x80047 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Voltage setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_setpoint | 16 | Unsigned |

### Payload description

#### Voltage_setpoint :id=DAB_Voltage_Setpoint_Control-Voltage_setpoint

Sets the output voltage setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1000 |


<a id="CLLC_PWM_Gain_Control"></a>
## CLLC_PWM_Gain_Control


| * | * |
|---|---|
| **Frame ID** | 0x80048 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

PWM gain control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Gain | 16 | Unsigned |

### Payload description

#### Gain :id=CLLC_PWM_Gain_Control-Gain

Sets voltage gain in open loop

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | none | 0.01 | 0 |  |  |


<a id="CLLC_PWM_Phase_Mode"></a>
## CLLC_PWM_Phase_Mode


| * | * |
|---|---|
| **Frame ID** | 0x80049 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

PWM duty cycle control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| phase_mode | 8 | Unsigned |

### Payload description

#### phase_mode :id=CLLC_PWM_Phase_Mode-phase_mode

PWM Phase shift mode/gain mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Group_Control"></a>
## DAB_Group_Control


| * | * |
|---|---|
| **Frame ID** | 0x8004c |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Set the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID | 8 | Unsigned |

### Payload description

#### Group_ID :id=DAB_Group_Control-Group_ID

Desired group ID for the device

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Fault_Control"></a>
## DAB_Fault_Control


| * | * |
|---|---|
| **Frame ID** | 0x80050 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

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

#### Clear_Interlock :id=DAB_Fault_Control-Clear_Interlock

Clears the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor :id=DAB_Fault_Control-Reset_Processor

Reset the converter DSP

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Clear_Faults :id=DAB_Fault_Control-Clear_Faults

Clear software faults

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Bleeder_Pulse :id=DAB_Fault_Control-Bleeder_Pulse

Bleed out output

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock :id=DAB_Fault_Control-Trip_Interlock

Trips the converter interlock

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="EPWM_control"></a>
## EPWM_control


| * | * |
|---|---|
| **Frame ID** | 0x80052 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Control the EPWM_control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| update | 8 | Unsigned |
| EPWM1 | 8 | Unsigned |
| EPWM2 | 8 | Unsigned |
| EPWM3 | 8 | Unsigned |
| EPWM4 | 8 | Unsigned |

### Payload description

#### update :id=EPWM_control-update

Customers MUST NOT USE this bit. If set to 1, EPWM is turned on.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### EPWM1 :id=EPWM_control-EPWM1

Customers MUST NOT USE this bit. If set to 1, EPWM is turned on.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### EPWM2 :id=EPWM_control-EPWM2

Customers MUST NOT USE this bit. If set to 1, EPWM is turned on.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### EPWM3 :id=EPWM_control-EPWM3

Customers MUST NOT USE this bit. If set to 1, EPWM is turned on.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### EPWM4 :id=EPWM_control-EPWM4

Customers MUST NOT USE this bit. If set to 1, EPWM is turned on.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Identification"></a>
## DAB_Identification


| * | * |
|---|---|
| **Frame ID** | 0x88000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

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

#### Device_type :id=DAB_Identification-Device_type

The device identification field, uniquely identifies the sender in the network.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| ADM_PC_BI25 | 8 |

#### HW_revision :id=DAB_Identification-HW_revision

The hardware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### HW_variant :id=DAB_Identification-HW_variant

The DSP firmware revision number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Stack_position :id=DAB_Identification-Stack_position

Position of the module within the stack

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### SN_number :id=DAB_Identification-SN_number

Unique module serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_FwInfo"></a>
## DAB_FwInfo


| * | * |
|---|---|
| **Frame ID** | 0x88001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

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

#### FW_revision_0 :id=DAB_FwInfo-FW_revision_0

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_7 :id=DAB_FwInfo-FW_revision_7

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_0 :id=DAB_FwInfo-FW_datecode_0

Character 0

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_7 :id=DAB_FwInfo-FW_datecode_7

Character 7

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_1 :id=DAB_FwInfo-FW_revision_1

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_8 :id=DAB_FwInfo-FW_revision_8

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_1 :id=DAB_FwInfo-FW_datecode_1

Character 1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_8 :id=DAB_FwInfo-FW_datecode_8

Character 8

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_2 :id=DAB_FwInfo-FW_revision_2

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_9 :id=DAB_FwInfo-FW_revision_9

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_2 :id=DAB_FwInfo-FW_datecode_2

Character 2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_9 :id=DAB_FwInfo-FW_datecode_9

Character 9

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_3 :id=DAB_FwInfo-FW_revision_3

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_10 :id=DAB_FwInfo-FW_revision_10

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_3 :id=DAB_FwInfo-FW_datecode_3

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_10 :id=DAB_FwInfo-FW_datecode_10

Character 10

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_4 :id=DAB_FwInfo-FW_revision_4

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_11 :id=DAB_FwInfo-FW_revision_11

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_4 :id=DAB_FwInfo-FW_datecode_4

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_11 :id=DAB_FwInfo-FW_datecode_11

Character 11

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_5 :id=DAB_FwInfo-FW_revision_5

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_12 :id=DAB_FwInfo-FW_revision_12

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_5 :id=DAB_FwInfo-FW_datecode_5

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_12 :id=DAB_FwInfo-FW_datecode_12

Character 12

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_6 :id=DAB_FwInfo-FW_revision_6

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_revision_13 :id=DAB_FwInfo-FW_revision_13

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_6 :id=DAB_FwInfo-FW_datecode_6

Character 3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_datecode_13 :id=DAB_FwInfo-FW_datecode_13

Character 13

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned |  | 1 | 0 |  |  |

#### FW_info_mux :id=DAB_FwInfo-FW_info_mux

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Debug"></a>
## DAB_Debug


| * | * |
|---|---|
| **Frame ID** | 0x88002 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

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

#### Status_Error_Code :id=DAB_Debug-Status_Error_Code

Main status / error code as defined in errno/errno.h

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_1 :id=DAB_Debug-Data_1

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_2 :id=DAB_Debug-Data_2

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Data_3 :id=DAB_Debug-Data_3

Additional information for the error/status

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Status"></a>
## DAB_Status


| * | * |
|---|---|
| **Frame ID** | 0x88003 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Status bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Converter_running | 1 | Single bit |
| Stack_mode | 1 | Single bit |
| Master | 1 | Single bit |
| Slave | 1 | Single bit |
| PWM_mode | 1 | Single bit |
| DC_DC_mode | 1 | Single bit |
| Voltage_follower_mode | 1 | Single bit |
| PFC_Voltage_mode | 1 | Single bit |
| Gain_mode | 1 | Single bit |
| Ready | 1 | Single bit |

### Payload description

#### Converter_running :id=DAB_Status-Converter_running

Indicates that the converter is running, and its output is active.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Stack_mode :id=DAB_Status-Stack_mode

Indicates if running in stack mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Master :id=DAB_Status-Master

Indicates if the current converter is the Master in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Slave :id=DAB_Status-Slave

Indicates if the current converter is a Slave in the stack.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 |  |  |

#### PWM_mode :id=DAB_Status-PWM_mode

Indicates if the converter is in PWM mode, and therefore working in open loop.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 |  |  |

#### DC_DC_mode :id=DAB_Status-DC_DC_mode

Indicates if the converter is in DC DC mode with automatic bi-dir angle control.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 |  |  |

#### Voltage_follower_mode :id=DAB_Status-Voltage_follower_mode

Indicates if the converter is in Voltage follower mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Single bit |  | 1 | 0 |  |  |

#### PFC_Voltage_mode :id=DAB_Status-PFC_Voltage_mode

Indicates if the converter is in PFC Voltage mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Single bit |  | 1 | 0 |  |  |

#### Gain_mode :id=DAB_Status-Gain_mode

Indicates if the converter is in Gain Mode.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Single bit |  | 1 | 0 |  |  |

#### Ready :id=DAB_Status-Ready

Indicates if converter is ready for operation.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Single bit |  | 1 | 0 |  |  |


<a id="DAB_Faults"></a>
## DAB_Faults


| * | * |
|---|---|
| **Frame ID** | 0x88004 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Fault bitfield

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Protection_trip_internal | 1 | Label set |
| Protection_trip_external | 1 | Label set |
| Current_Side_A_overcurrent | 1 | Label set |
| Current_Side_B_overcurrent | 1 | Label set |
| Current_Phase_Side_A_overcurrent | 1 | Label set |
| Current_Phase_Side_B_overcurrent | 1 | Label set |
| Voltage_Side_A_undervoltage | 1 | Label set |
| Voltage_Side_A_overvoltage | 1 | Label set |
| Voltage_Side_B_undervoltage | 1 | Label set |
| Voltage_Side_B_overvoltage | 1 | Label set |
| Bar_A_overtemperature | 1 | Label set |
| Bar_B_overtemperature | 1 | Label set |
| Switching_failure | 1 | Label set |
| CAN_failure | 1 | Label set |
| Control_response_timedout | 1 | Label set |
| Measurement_system_failure | 1 | Label set |
| EEPROM_failure | 1 | Label set |
| System | 1 | Label set |
| NFO | 1 | Label set |
| ADC | 1 | Label set |
| WCH | 1 | Label set |
| Transformer_1_overtemperature | 1 | Label set |
| Transformer_2_overtemperature | 1 | Label set |

### Payload description

#### Protection_trip_internal :id=DAB_Faults-Protection_trip_internal

This flag is asserted if the interlock is open due to an internal fault condition (self-protection).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Protection_trip_external :id=DAB_Faults-Protection_trip_external

This flag is asserted if the interlock is open due to an external condition received in the module.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_Side_A_overcurrent :id=DAB_Faults-Current_Side_A_overcurrent

Indicates an overcurrent event on input current. The overcurrent event is triggered
when the measured phase current is over the programmed / absolute current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_Side_B_overcurrent :id=DAB_Faults-Current_Side_B_overcurrent

Indicates an overcurrent event on output current. The overcurrent event is
triggered when the measured current is over the programmed / absolute current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_Phase_Side_A_overcurrent :id=DAB_Faults-Current_Phase_Side_A_overcurrent

Indicates an overcurrent event on input phase current. The overcurrent event is
triggered when the measured current is over the programmed / absolute current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Current_Phase_Side_B_overcurrent :id=DAB_Faults-Current_Phase_Side_B_overcurrent

Indicates an overcurrent event on output phase current. The overcurrent event is
triggered when the measured current is over the programmed / absolute current limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_Side_A_undervoltage :id=DAB_Faults-Voltage_Side_A_undervoltage

Indicates an undervoltage event on Voltage In. The undervoltage event is triggered
when the measured voltage is under the programmed / absolute voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_Side_A_overvoltage :id=DAB_Faults-Voltage_Side_A_overvoltage

Indicates an overvoltage event Voltage In. The overvoltage event is triggered when
the measured phase voltage is over the programmed / absolute voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_Side_B_undervoltage :id=DAB_Faults-Voltage_Side_B_undervoltage

Indicates an undervoltage event on Voltage Out. The undervoltage event is triggered
when the measured voltage is under the programmed / absolute voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Voltage_Side_B_overvoltage :id=DAB_Faults-Voltage_Side_B_overvoltage

Indicates an overvoltage event Voltage Out. The overvoltage event is triggered when
the measured phase voltage is over the programmed / absolute voltage limit.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Bar_A_overtemperature :id=DAB_Faults-Bar_A_overtemperature

This flag is asserted when the temperature of the Bar A block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Bar_B_overtemperature :id=DAB_Faults-Bar_B_overtemperature

This flag is asserted when the temperature of the Bar B block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Switching_failure :id=DAB_Faults-Switching_failure

Failure in the MOSFET block or in their drivers.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### CAN_failure :id=DAB_Faults-CAN_failure

CAN bus or transceiver not operating properly.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Control_response_timedout :id=DAB_Faults-Control_response_timedout

The control system did not answer within the allowed time window, and a time out
condition was triggered. The converter is switched off as the control system is
not present.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Measurement_system_failure :id=DAB_Faults-Measurement_system_failure

The voltages/currents measurement system is malfunctionning, and readouts are not
guaranteed to be accurate.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### EEPROM_failure :id=DAB_Faults-EEPROM_failure

The configuration EEPROM failed to load or save the module configuration.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### System :id=DAB_Faults-System

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### NFO :id=DAB_Faults-NFO

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### ADC :id=DAB_Faults-ADC

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### WCH :id=DAB_Faults-WCH

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Transformer_1_overtemperature :id=DAB_Faults-Transformer_1_overtemperature

This flag is asserted when the temperature of the Bar B block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |

#### Transformer_2_overtemperature :id=DAB_Faults-Transformer_2_overtemperature

This flag is asserted when the temperature of the Bar B block is too high.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| fault | 1 |


<a id="DAB_Voltages_Currents"></a>
## DAB_Voltages_Currents


| * | * |
|---|---|
| **Frame ID** | 0x88005 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Voltages and currents of Input/Output

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 16 | Signed |
| Current_Side_B | 16 | Signed |
| Voltage_Side_A | 16 | Signed |
| Voltage_Side_B | 16 | Signed |

### Payload description

#### Current_Side_A :id=DAB_Voltages_Currents-Current_Side_A

Input current of the converter (direction from input to output is positive).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Current_Side_B :id=DAB_Voltages_Currents-Current_Side_B

Input current of the converter (direction from input to output is positive).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Voltage_Side_A :id=DAB_Voltages_Currents-Voltage_Side_A

Input voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Voltage_Side_B :id=DAB_Voltages_Currents-Voltage_Side_B

Output voltage of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="DAB_Phase_Currents"></a>
## DAB_Phase_Currents


| * | * |
|---|---|
| **Frame ID** | 0x88006 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Phase currents of Input/Output

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Phase_Side_A | 16 | Signed |
| Current_Phase_Side_B | 16 | Signed |

### Payload description

#### Current_Phase_Side_A :id=DAB_Phase_Currents-Current_Phase_Side_A

Input phase current of the converter (direction from input to output is positive).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Current_Phase_Side_B :id=DAB_Phase_Currents-Current_Phase_Side_B

Input phase current of the converter (direction from input to output is positive).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="_DAB_Voltages_Currents_Raw"></a>
## _DAB_Voltages_Currents_Raw


| * | * |
|---|---|
| **Frame ID** | 0x88007 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Raw Voltages and currents of Input/Output

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 16 | Unsigned |
| Current_Side_B | 16 | Signed |
| Voltage_Side_A | 16 | Unsigned |
| Voltage_Side_B | 16 | Signed |

### Payload description

#### Current_Side_A :id=_DAB_Voltages_Currents_Raw-Current_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Current_Side_B :id=_DAB_Voltages_Currents_Raw-Current_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed |  | 1 | 0 |  |  |

#### Voltage_Side_A :id=_DAB_Voltages_Currents_Raw-Voltage_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Voltage_Side_B :id=_DAB_Voltages_Currents_Raw-Voltage_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed |  | 1 | 0 |  |  |


<a id="_DAB_Phase_Currents_Raw"></a>
## _DAB_Phase_Currents_Raw


| * | * |
|---|---|
| **Frame ID** | 0x88008 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Raw ADC values from the Phase current sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Phase_Side_A | 16 | Unsigned |
| Current_Phase_Side_B | 16 | Unsigned |

### Payload description

#### Current_Phase_Side_A :id=_DAB_Phase_Currents_Raw-Current_Phase_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned |  | 1 | 0 |  |  |

#### Current_Phase_Side_B :id=_DAB_Phase_Currents_Raw-Current_Phase_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Temperatures"></a>
## DAB_Temperatures


| * | * |
|---|---|
| **Frame ID** | 0x88009 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Readouts of the module temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Temp_Bar_In | 16 | Signed |
| Temp_Bar_Out | 16 | Signed |
| Temp_Transformer | 16 | Signed |
| Temp_Magnetics | 16 | Signed |

### Payload description

#### Temp_Bar_In :id=DAB_Temperatures-Temp_Bar_In

Temperature of the Bar A block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Bar_Out :id=DAB_Temperatures-Temp_Bar_Out

Temperature of the Bar A block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Transformer :id=DAB_Temperatures-Temp_Transformer

Temperature of the Bar B block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | °C | 0.01 | 0 |  |  |

#### Temp_Magnetics :id=DAB_Temperatures-Temp_Magnetics

Temperature of the Magnetic B block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | °C | 0.01 | 0 |  |  |


<a id="DAB_Setpoints_PWM_Phase"></a>
## DAB_Setpoints_PWM_Phase


| * | * |
|---|---|
| **Frame ID** | 0x8800a |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

PWM duty cycle control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_A | 16 | Signed |
| Phase_B | 16 | Signed |

### Payload description

#### Phase_A :id=DAB_Setpoints_PWM_Phase-Phase_A

PWM Phase setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | ° | 0.003 | 0 |  |  |

#### Phase_B :id=DAB_Setpoints_PWM_Phase-Phase_B

PWM Phase setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | ° | 0.003 | 0 |  |  |


<a id="_DAB_Broadcast"></a>
## _DAB_Broadcast


| * | * |
|---|---|
| **Frame ID** | 0x8800e |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 50 |
| **Direction** | OUT |

### Description

All DABs will listen to this message

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 5 | Unsigned |
| Group_ID | 3 | Unsigned |
| Port_A | 16 | Signed |
| Port_B | 16 | Signed |
| Diagnostics_Index | 8 | Unsigned |

### Payload description

#### Stack_position :id=_DAB_Broadcast-Stack_position

Sender Stack position

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 5 | Unsigned |  | 1 | 0 |  |  |

#### Group_ID :id=_DAB_Broadcast-Group_ID

Sender Group ID

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 3 | Unsigned |  | 1 | 0 |  |  |

#### Port_A :id=_DAB_Broadcast-Port_A

'Input' port A current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Port_B :id=_DAB_Broadcast-Port_B

'Output' port B current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Diagnostics_Index :id=_DAB_Broadcast-Diagnostics_Index

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="DAB_Group_Info"></a>
## DAB_Group_Info


| * | * |
|---|---|
| **Frame ID** | 0x8800f |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Contains the Group ID of the device

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Group_ID | 8 | Unsigned |

### Payload description

#### Group_ID :id=DAB_Group_Info-Group_ID

Group ID of the device

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="_DAB_Calibration_Adc_Fs"></a>
## _DAB_Calibration_Adc_Fs


| * | * |
|---|---|
| **Frame ID** | 0x88041 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Fullscale value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 32 | Float |
| Current_Side_B | 32 | Float |
| Current_Phase_Side_A | 32 | Float |
| Voltage_Side_A | 32 | Float |
| Voltage_Side_B | 32 | Float |
| Current_Phase_Side_B | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_Side_A :id=_DAB_Calibration_Adc_Fs-Current_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_Side_B :id=_DAB_Calibration_Adc_Fs-Current_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_Phase_Side_A :id=_DAB_Calibration_Adc_Fs-Current_Phase_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Side_A :id=_DAB_Calibration_Adc_Fs-Voltage_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Voltage_Side_B :id=_DAB_Calibration_Adc_Fs-Voltage_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Current_Phase_Side_B :id=_DAB_Calibration_Adc_Fs-Current_Phase_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | Fullscale | 1 | 0 |  |  |

#### Adc_Index :id=_DAB_Calibration_Adc_Fs-Adc_Index

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="_DAB_Calibration_Adc_Scale"></a>
## _DAB_Calibration_Adc_Scale


| * | * |
|---|---|
| **Frame ID** | 0x88042 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Adc scale (resolution) value of readouts.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_Side_A | 32 | Signed |
| Current_Side_B | 32 | Signed |
| Current_Phase_Side_A | 32 | Signed |
| Voltage_Side_A | 32 | Signed |
| Voltage_Side_B | 32 | Signed |
| Current_Phase_Side_B | 32 | Float |
| Adc_Index | 16 | Unsigned |

### Payload description

#### Current_Side_A :id=_DAB_Calibration_Adc_Scale-Current_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | 1 / adc_bins | 1 | 0 |  |  |

#### Current_Side_B :id=_DAB_Calibration_Adc_Scale-Current_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | 1 / adc_bins | 1 | 0 |  |  |

#### Current_Phase_Side_A :id=_DAB_Calibration_Adc_Scale-Current_Phase_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Side_A :id=_DAB_Calibration_Adc_Scale-Voltage_Side_A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | 1 / adc_bins | 1 | 0 |  |  |

#### Voltage_Side_B :id=_DAB_Calibration_Adc_Scale-Voltage_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Signed | 1 / adc_bins | 1 | 0 |  |  |

#### Current_Phase_Side_B :id=_DAB_Calibration_Adc_Scale-Current_Phase_Side_B

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 32 | Float | 1 / adc_bins | 1 | 0 |  |  |

#### Adc_Index :id=_DAB_Calibration_Adc_Scale-Adc_Index

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="CLLC_PWM_Frequency_value"></a>
## CLLC_PWM_Frequency_value


| * | * |
|---|---|
| **Frame ID** | 0x88048 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

PWM duty cycle Readout

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| frequency | 16 | Unsigned |

### Payload description

#### frequency :id=CLLC_PWM_Frequency_value-frequency

PWM frequency setpoint.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 10 | 0 |  |  |


<a id="Data_test_out"></a>
## Data_test_out


| * | * |
|---|---|
| **Frame ID** | 0x88090 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Readouts of the module temperature sensors

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| gain | 8 | Unsigned |

### Payload description

#### gain :id=Data_test_out-gain

Gain mode select

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="Data_phase_shift"></a>
## Data_phase_shift


| * | * |
|---|---|
| **Frame ID** | 0x88091 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Readouts of the module phase shifts

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| phase_shift_a | 16 | Signed |
| phase_shift_b | 16 | Unsigned |

### Payload description

#### phase_shift_a :id=Data_phase_shift-phase_shift_a

Phase_shift_A of the Bar A block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### phase_shift_b :id=Data_phase_shift-phase_shift_b

Phase_shift_B of the Bar A block

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Hz | 0.1 | 0 |  |  |


<a id="DAB_CAN_API_Version"></a>
## DAB_CAN_API_Version


| * | * |
|---|---|
| **Frame ID** | 0x880f3 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

This message declares the version of the API that is provided by the converter. The version follows newer convention.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Major | 8 | Unsigned |
| Minor | 8 | Unsigned |
| Patch | 8 | Unsigned |

### Payload description

#### Major :id=DAB_CAN_API_Version-Major

The Major version number. This number increases if there are backwards incompatible changes

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Minor :id=DAB_CAN_API_Version-Minor

The Minor version number. This number increases if there are backwards compatible changes, like new messages or the use of previously reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Patch :id=DAB_CAN_API_Version-Patch

The Patch number. This number increases when changes to descriptions and documentation/comments are made

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |
