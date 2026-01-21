# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [DC_Ports_Setpoints](#DC_Ports_Setpoints) | 0x810020 | 6 | IN | 1000 |
| [DC_Port_Applied_Setpoints](#DC_Port_Applied_Setpoints) | 0x810021 | 8 | OUT | 1000 |
| [DC_Port_Droop_Setpoints](#DC_Port_Droop_Setpoints) | 0x810022 | 8 | IN |  |
| [DC_Port_Applied_Droop_Setpoints](#DC_Port_Applied_Droop_Setpoints) | 0x810023 | 8 | OUT | 1000 |
| [DC_Port_Measurements](#DC_Port_Measurements) | 0x810024 | 4 | OUT | 100 |
| [AC_Port_Setpoints](#AC_Port_Setpoints) | 0x810030 | 8 | IN |  |
| [AC_Port_Applied_Setpoints](#AC_Port_Applied_Setpoints) | 0x810031 | 8 | OUT | 1000 |
| [AC_Port_Measurements](#AC_Port_Measurements) | 0x810032 | 8 | OUT | 1000 |
| [L1_Measurements](#L1_Measurements) | 0x810033 | 8 | OUT | 100 |
| [L2_Measurements](#L2_Measurements) | 0x810034 | 8 | OUT | 100 |
| [L3_Measurements](#L3_Measurements) | 0x810035 | 8 | OUT | 100 |
| [AC01_Mode_Set](#AC01_Mode_Set) | 0x810040 | 1 | IN |  |
| [AC01_Mode_Applied](#AC01_Mode_Applied) | 0x810041 | 1 | OUT | 1000 |
| [AC01_faults](#AC01_faults) | 0x810042 | 8 | OUT | 1000 |
| [AC01_warning](#AC01_warning) | 0x810043 | 8 | OUT | 1000 |
| [AC01_info](#AC01_info) | 0x810044 | 8 | OUT | 1000 |


<a id="DC_Ports_Setpoints"></a>
## DC_Ports_Setpoints { #DC_Ports_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810020 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

The setpoints control the behaviour of the DC Port of the AC01. The AC01 operates this port in CVCC mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #DC_Ports_Setpoints-Voltage }

Control the target dc side voltage. This voltage will be maintained as long as the current required to do so is smaller than the current limits specified in this message

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Source_Current_Limit { #DC_Ports_Setpoints-Source_Current_Limit }

The maximum current that the AC01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |

#### Sink_Current_Limit { #DC_Ports_Setpoints-Sink_Current_Limit }

The maximum current that the AC01 will sink into the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |


<a id="DC_Port_Applied_Setpoints"></a>
## DC_Port_Applied_Setpoints { #DC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the AC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #DC_Port_Applied_Setpoints-Voltage }

The voltage target of the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Source_Current_Limit { #DC_Port_Applied_Setpoints-Source_Current_Limit }

The maximum current that the AC01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 |  |  |

#### Sink_Current_Limit { #DC_Port_Applied_Setpoints-Sink_Current_Limit }

The maximum amount of current that the AC01 will sink into the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  |  |


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
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #DC_Port_Droop_Setpoints-Negative_Current_Droop }

The droop resistance to apply for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

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

This space is reserved. This region should contain only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  |  |


<a id="DC_Port_Applied_Droop_Setpoints"></a>
## DC_Port_Applied_Droop_Setpoints { #DC_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810023 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
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
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #DC_Port_Applied_Droop_Setpoints-Negative_Current_Droop }

The droop resistance applied for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

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

This space is reserved. This region should contain only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  |  |


<a id="DC_Port_Measurements"></a>
## DC_Port_Measurements { #DC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810024 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
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
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Current { #DC_Port_Measurements-Current }

Current through the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


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
| Q | 16 | Signed |
| Reserved | 48 | Unsigned |

### Payload description

#### Q { #AC_Port_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the AC01 to behave inductively, negative values cause the AC01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | VAR | 10 | 0 |  |  |

#### Reserved { #AC_Port_Setpoints-Reserved }

This space is reserved. This region should contain only 0s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 48 | Unsigned |  | 1 | 0 |  |  |


<a id="AC_Port_Applied_Setpoints"></a>
## AC_Port_Applied_Setpoints { #AC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x810031 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Setpoints that are currently being applied to the the AC Port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Q | 16 | Signed |
| Reserved | 48 | Unsigned |

### Payload description

#### Q { #AC_Port_Applied_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the AC01 to behave inductively, negative values cause the AC01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | VAR | 10 | 0 |  |  |

#### Reserved { #AC_Port_Applied_Setpoints-Reserved }

This space is reserved. This region should contain only 0s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 48 | Unsigned |  | 1 | 0 |  |  |


<a id="AC_Port_Measurements"></a>
## AC_Port_Measurements { #AC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810032 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
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
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |

#### Voltage { #AC_Port_Measurements-Voltage }

Average RMS Line to Line voltage at the AC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Reserved { #AC_Port_Measurements-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="L1_Measurements"></a>
## L1_Measurements { #L1_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810033 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
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
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L1_Measurements-I }

RMS Current of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L1_Measurements-P }

Active power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L1_Measurements-Q }

Reactive power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="L2_Measurements"></a>
## L2_Measurements { #L2_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810034 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
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
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L2_Measurements-I }

RMS Current of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L2_Measurements-P }

Active power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L2_Measurements-Q }

Reactive power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="L3_Measurements"></a>
## L3_Measurements { #L3_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x810035 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
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
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L3_Measurements-I }

RMS Current of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L3_Measurements-P }

Active power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L3_Measurements-Q }

Reactive power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="AC01_Mode_Set"></a>
## AC01_Mode_Set { #AC01_Mode_Set }


| * | * |
|---|---|
| **Frame ID** | 0x810040 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Set the mode of AC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #AC01_Mode_Set-mode }

require mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

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
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

read back the modes

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #AC01_Mode_Applied-mode }

actual mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

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
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

AC01 Critical and Error Faults

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
| FILTER_1_RELAY_FAIL | 1 | Label set |
| FILTER_4_RELAY_FAIL | 1 | Label set |
| FILTER_1_RELAY_NOT_OFF | 1 | Label set |
| FILTER_4_RELAY_NOT_OFF | 1 | Label set |
| PRECHARGE_RELAY_CLOSING | 1 | Label set |
| PRECHARGE_RELAY_OPENING | 1 | Label set |
| FILTER_NOT_RUNNING | 1 | Label set |
| RECTIFIER_3P_NOT_RUNNING | 1 | Label set |
| AFE_NOT_OFF | 1 | Label set |
| FILTER_STOP_RUNNING | 1 | Label set |
| RECTIFIER_3P_STOP_RUNNING | 1 | Label set |
| AFE_PWM_NOT_RUNNING | 1 | Label set |
| AFE_PWM_STOP_RUNNING | 1 | Label set |
| BLEEDING_FAILED | 1 | Label set |
| FILTER_NOT_OFF | 1 | Label set |

### Payload description

#### CABLE_1_2_L1 { #AC01_faults-CABLE_1_2_L1 }

DMF1(1).L1  BP25(2).U mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L1 { #AC01_faults-CABLE_1_3_L1 }

DMF1(1).L1  BP25(3).U mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L2 { #AC01_faults-CABLE_1_2_L2 }

DMF1(1).L2  BP25(2).V mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L2 { #AC01_faults-CABLE_1_3_L2 }

DMF1(1).L2  BP25(3).V mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L3 { #AC01_faults-CABLE_1_2_L3 }

DMF1(1).L3  BP25(2).W mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L3 { #AC01_faults-CABLE_1_3_L3 }

DMF1(1).L3  BP25(3).W mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L1 { #AC01_faults-CABLE_4_5_L1 }

DMF1(4).L1  BP25(5).U mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L1 { #AC01_faults-CABLE_4_6_L1 }

DMF1(4).L1  BP25(6).U mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L2 { #AC01_faults-CABLE_4_5_L2 }

DMF1(4).L2  BP25(5).V mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L2 { #AC01_faults-CABLE_4_6_L2 }

DMF1(4).L2  BP25(6).V mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L3 { #AC01_faults-CABLE_4_5_L3 }

DMF1(4).L3  BP25(5).W mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_6_L3 { #AC01_faults-CABLE_4_6_L3 }

DMF1(4).L3  BP25(6).W mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L1 { #AC01_faults-CABLE_1_4_L1 }

Grid L1  DMF1(1).in vs DMF1(4).in mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L2 { #AC01_faults-CABLE_1_4_L2 }

Grid L2  DMF1(1).in vs DMF1(4).in mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L3 { #AC01_faults-CABLE_1_4_L3 }

Grid L3 - DMF1(1).in vs DMF1(4).in mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_2_3_DC { #AC01_faults-CABLE_2_3_DC }

BP25(2).DC  BP25(3).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_5_6_DC { #AC01_faults-CABLE_5_6_DC }

BP25(5).DC  BP25(6).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_5_DC { #AC01_faults-CABLE_3_5_DC }

BP25(3).DC  BP25(5).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### MODULE_1_RUNNING { #AC01_faults-MODULE_1_RUNNING }

DMF1(1) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_2_RUNNING { #AC01_faults-MODULE_2_RUNNING }

DMF1(2) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_3_RUNNING { #AC01_faults-MODULE_3_RUNNING }

DMF1(3) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_4_RUNNING { #AC01_faults-MODULE_4_RUNNING }

DMF1(4) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_5_RUNNING { #AC01_faults-MODULE_5_RUNNING }

DMF1(5) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_6_RUNNING { #AC01_faults-MODULE_6_RUNNING }

DMF1(6) running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_1_RELAY_FAIL { #AC01_faults-FILTER_1_RELAY_FAIL }

Relay 1 fail

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_4_RELAY_FAIL { #AC01_faults-FILTER_4_RELAY_FAIL }

Relay 4 fail

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_1_RELAY_NOT_OFF { #AC01_faults-FILTER_1_RELAY_NOT_OFF }

Relay 1 not off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_4_RELAY_NOT_OFF { #AC01_faults-FILTER_4_RELAY_NOT_OFF }

Relay 4 not off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 27 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### PRECHARGE_RELAY_CLOSING { #AC01_faults-PRECHARGE_RELAY_CLOSING }

Precharge relay closing

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 28 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### PRECHARGE_RELAY_OPENING { #AC01_faults-PRECHARGE_RELAY_OPENING }

Precharge relay opening

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 29 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_RUNNING { #AC01_faults-FILTER_NOT_RUNNING }

Filter not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 30 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_NOT_RUNNING { #AC01_faults-RECTIFIER_3P_NOT_RUNNING }

Rectifier not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 31 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_NOT_OFF { #AC01_faults-AFE_NOT_OFF }

AFE not off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_STOP_RUNNING { #AC01_faults-FILTER_STOP_RUNNING }

Filter stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_STOP_RUNNING { #AC01_faults-RECTIFIER_3P_STOP_RUNNING }

Rectifier stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 35 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_NOT_RUNNING { #AC01_faults-AFE_PWM_NOT_RUNNING }

BLEEDING not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_STOP_RUNNING { #AC01_faults-AFE_PWM_STOP_RUNNING }

Bleeding stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 37 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### BLEEDING_FAILED { #AC01_faults-BLEEDING_FAILED }

Bleeding failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 38 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_OFF { #AC01_faults-FILTER_NOT_OFF }

filter not off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 39 | 1 | Label set |  | 1 | 0 |  |  |

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
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

AC01 Warning

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| GHM_INIT | 1 | Label set |
| GHM_RMS | 1 | Label set |
| GHM_FREQ | 1 | Label set |
| GHM_PHASE | 1 | Label set |
| RQ_V_SET_DC_BELOW_AC | 1 | Label set |
| RQ_C_SINK_SET_LOW | 1 | Label set |
| RQ_C_SOURCE_SET_LOW | 1 | Label set |
| RQ_C_SET_DC_ABOVE_MAX | 1 | Label set |
| RQ_C_SET_DC_BELOW_MIN | 1 | Label set |
| RQ_V_SET_DC_BELOW_MIN | 1 | Label set |
| RQ_DC_DROOP_NEG_INVALID | 1 | Label set |
| RQ_DC_DROOP_POS_INVALID | 1 | Label set |
| RQ_V_SET_DC_ABOVE_MAX | 1 | Label set |
| AFE_DROOP_NOT_ENABLE | 1 | Label set |
| MODE_NOT_SUPPORTED | 1 | Label set |

### Payload description

#### GHM_INIT { #AC01_warning-GHM_INIT }

GHM init failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### GHM_RMS { #AC01_warning-GHM_RMS }

GHM RMS failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### GHM_FREQ { #AC01_warning-GHM_FREQ }

GHM freq failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### GHM_PHASE { #AC01_warning-GHM_PHASE }

GHM phase failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_SET_DC_BELOW_AC { #AC01_warning-RQ_V_SET_DC_BELOW_AC }

DC voltage too low vs AC

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SINK_SET_LOW { #AC01_warning-RQ_C_SINK_SET_LOW }

Sink current too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SOURCE_SET_LOW { #AC01_warning-RQ_C_SOURCE_SET_LOW }

Source current too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SET_DC_ABOVE_MAX { #AC01_warning-RQ_C_SET_DC_ABOVE_MAX }

Current above max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SET_DC_BELOW_MIN { #AC01_warning-RQ_C_SET_DC_BELOW_MIN }

Sink current too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_SET_DC_BELOW_MIN { #AC01_warning-RQ_V_SET_DC_BELOW_MIN }

Source current too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_DC_DROOP_NEG_INVALID { #AC01_warning-RQ_DC_DROOP_NEG_INVALID }

Current limited by power max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_DC_DROOP_POS_INVALID { #AC01_warning-RQ_DC_DROOP_POS_INVALID }

Current limited by power max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_SET_DC_ABOVE_MAX { #AC01_warning-RQ_V_SET_DC_ABOVE_MAX }

Current above max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### AFE_DROOP_NOT_ENABLE { #AC01_warning-AFE_DROOP_NOT_ENABLE }

Group ID not set

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### MODE_NOT_SUPPORTED { #AC01_warning-MODE_NOT_SUPPORTED }

Mode not supported

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

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
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

AC01 Info

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| BLEEDING_DONE | 1 | Label set |
| RQ_C_LIMITED_BY_POWER | 1 | Label set |

### Payload description

#### BLEEDING_DONE { #AC01_info-BLEEDING_DONE }

Current limited by power max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### RQ_C_LIMITED_BY_POWER { #AC01_info-RQ_C_LIMITED_BY_POWER }

Current limited by power max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |
