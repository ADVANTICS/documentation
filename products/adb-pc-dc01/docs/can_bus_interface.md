# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [B_Port_Setpoints](#B_Port_Setpoints) | 0x820020 | 6 | IN | 1000 |
| [B_Port_Applied_Setpoints](#B_Port_Applied_Setpoints) | 0x820021 | 8 | OUT | 1000 |
| [B_Port_Droop_Setpoints](#B_Port_Droop_Setpoints) | 0x820022 | 8 | IN |  |
| [B_Port_Applied_Droop_Setpoints](#B_Port_Applied_Droop_Setpoints) | 0x820023 | 5 | OUT | 1000 |
| [B_Port_Measurements](#B_Port_Measurements) | 0x820024 | 4 | OUT | 100 |
| [A_Port_Setpoints](#A_Port_Setpoints) | 0x820030 | 6 | IN | 1000 |
| [A_Port_Applied_Setpoints](#A_Port_Applied_Setpoints) | 0x820031 | 8 | OUT | 1000 |
| [A_Port_Measurements](#A_Port_Measurements) | 0x820032 | 4 | OUT | 100 |
| [DC01_Mode_Set](#DC01_Mode_Set) | 0x820040 | 2 | IN |  |
| [DC01_Mode_Applied](#DC01_Mode_Applied) | 0x820041 | 2 | OUT | 1000 |
| [DC01_faults](#DC01_faults) | 0x820042 | 8 | OUT | 1000 |
| [DC01_warning](#DC01_warning) | 0x820043 | 8 | OUT | 1000 |
| [DC01_info](#DC01_info) | 0x820044 | 8 | OUT | 1000 |
| [DC01_debug](#DC01_debug) | 0x8200f2 | 8 | IN | 1000 |
| [DC01_debug_connection](#DC01_debug_connection) | 0x8200f3 | 8 | OUT | 1000 |


<a id="B_Port_Setpoints"></a>
## B_Port_Setpoints { #B_Port_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820020 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

The setpoints control the behaviour of the B Port of the DC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #B_Port_Setpoints-Voltage }

Control the target B port voltage. This voltage will be maintained as long as the current required to do so is smaller than the current limits specified in this message

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Source_Current_Limit { #B_Port_Setpoints-Source_Current_Limit }

The maximum current that the DC01 will source on the B port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |

#### Sink_Current_Limit { #B_Port_Setpoints-Sink_Current_Limit }

The maximum current that the AC01 will sink into the B port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |


<a id="B_Port_Applied_Setpoints"></a>
## B_Port_Applied_Setpoints { #B_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the DC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #B_Port_Applied_Setpoints-Voltage }

The voltage target of the B port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Source_Current_Limit { #B_Port_Applied_Setpoints-Source_Current_Limit }

The maximum current that the DC01 will source on the B Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 |  |  |

#### Sink_Current_Limit { #B_Port_Applied_Setpoints-Sink_Current_Limit }

The maximum amount of current that the DC01 will sink into the B port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  |  |


<a id="B_Port_Droop_Setpoints"></a>
## B_Port_Droop_Setpoints { #B_Port_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820022 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints for applying Droop on the DC Port B. Droop is needed for paralleling multiple DC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |
| Reserved | 31 | Unsigned |

### Payload description

#### Positive_Current_Droop { #B_Port_Droop_Setpoints-Positive_Current_Droop }

The droop resistance to apply for current flowing out of the DC port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #B_Port_Droop_Setpoints-Negative_Current_Droop }

The droop resistance to apply for current flowing in to the DC Port B (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Enable { #B_Port_Droop_Setpoints-Enable }

Enable DC Droop. If this feature is enabled the output voltage of the DC port  Bvaries with output current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #B_Port_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  |  |


<a id="B_Port_Applied_Droop_Setpoints"></a>
## B_Port_Applied_Droop_Setpoints { #B_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820023 |
| **Length [Bytes]** | 5 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Droop setpoints that are applied by the DC01 on port b

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |

### Payload description

#### Positive_Current_Droop { #B_Port_Applied_Droop_Setpoints-Positive_Current_Droop }

The droop resistance applied for current flowing out of the DC port B (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #B_Port_Applied_Droop_Setpoints-Negative_Current_Droop }

The droop resistance applied for current flowing in to the DC Port B (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Enable { #B_Port_Applied_Droop_Setpoints-Enable }

Show is B port Droop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |


<a id="B_Port_Measurements"></a>
## B_Port_Measurements { #B_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x820024 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements of the B port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #B_Port_Measurements-Voltage }

Voltage on the B Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Current { #B_Port_Measurements-Current }

Current through the B Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="A_Port_Setpoints"></a>
## A_Port_Setpoints { #A_Port_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820030 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

The setpoints control the behaviour of the A Port of the DC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #A_Port_Setpoints-Voltage }

Control the target A port voltage. This voltage will be maintained as long as the current required to do so is smaller than the current limits specified in this message

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |

#### Source_Current_Limit { #A_Port_Setpoints-Source_Current_Limit }

The maximum current that the DC01 will source on the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |

#### Sink_Current_Limit { #A_Port_Setpoints-Sink_Current_Limit }

The maximum current that the AC01 will sink into the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 | 0 | 220 |


<a id="A_Port_Applied_Setpoints"></a>
## A_Port_Applied_Setpoints { #A_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820031 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the DC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Source_Current_Limit | 16 | Unsigned |
| Sink_Current_Limit | 16 | Unsigned |

### Payload description

#### Voltage { #A_Port_Applied_Setpoints-Voltage }

The voltage target of the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Source_Current_Limit { #A_Port_Applied_Setpoints-Source_Current_Limit }

The maximum current that the DC01 will source on the A Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | A | 0.1 | 0 |  |  |

#### Sink_Current_Limit { #A_Port_Applied_Setpoints-Sink_Current_Limit }

The maximum amount of current that the DC01 will sink into the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  |  |


<a id="A_Port_Measurements"></a>
## A_Port_Measurements { #A_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x820032 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements of the A port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #A_Port_Measurements-Voltage }

Voltage on the A Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Current { #A_Port_Measurements-Current }

Current through the A Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="DC01_Mode_Set"></a>
## DC01_Mode_Set { #DC01_Mode_Set }


| * | * |
|---|---|
| **Frame ID** | 0x820040 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Set the mode of AC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |
| connection | 8 | Label set |

### Payload description

#### mode { #DC01_Mode_Set-mode }

require mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| B_port_Controlled | 0 |
| A_port_Controlled | 1 |
| Bleeding | 2 |

#### connection { #DC01_Mode_Set-connection }

require connection

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| automatic | 0 |
| forced_serial | 1 |
| forced_parallel | 2 |


<a id="DC01_Mode_Applied"></a>
## DC01_Mode_Applied { #DC01_Mode_Applied }


| * | * |
|---|---|
| **Frame ID** | 0x820041 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

read back the modes

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |
| connection | 8 | Label set |

### Payload description

#### mode { #DC01_Mode_Applied-mode }

actual mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| B_side_Controlled | 0 |
| A_side_Controlled | 1 |
| Bleeding | 2 |

#### connection { #DC01_Mode_Applied-connection }

connection mode

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| open | 0 |
| serial | 1 |
| parallel | 2 |


<a id="DC01_faults"></a>
## DC01_faults { #DC01_faults }


| * | * |
|---|---|
| **Frame ID** | 0x820042 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

DC01 Critical and Error Faults

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| CABLE_2_4_DC | 1 | Label set |
| CABLE_1_2_DC | 1 | Label set |
| CABLE_3_4_DC | 1 | Label set |
| CABLE_1_L1_L2 | 1 | Label set |
| CABLE_1_L2_L3 | 1 | Label set |
| CABLE_3_L1_L2 | 1 | Label set |
| CABLE_3_L2_L3 | 1 | Label set |
| CABLE_1_3_L1 | 1 | Label set |
| CABLE_2_IN_OUT | 1 | Label set |
| CABLE_4_IN_OUT | 1 | Label set |
| MODULE_1_RUNNING | 1 | Label set |
| MODULE_2_RUNNING | 1 | Label set |
| MODULE_3_RUNNING | 1 | Label set |
| MODULE_4_RUNNING | 1 | Label set |
| CONTACTOR_1_CLOSED | 1 | Label set |
| CONTACTOR_2_CLOSED | 1 | Label set |
| CONTACTOR_3_CLOSED | 1 | Label set |
| CONTACTOR_4_CLOSED | 1 | Label set |
| CONTACTOR_1_OPEN | 1 | Label set |
| CONTACTOR_2_OPEN | 1 | Label set |
| CONTACTOR_3_OPEN | 1 | Label set |
| CONTACTOR_4_OPEN | 1 | Label set |
| CONTACTOR_1_FAIL | 1 | Label set |
| CONTACTOR_2_FAIL | 1 | Label set |
| CONTACTOR_3_FAIL | 1 | Label set |
| CONTACTOR_4_FAIL | 1 | Label set |
| PORT_B_OVERVOLTAGE | 1 | Label set |
| CS_REV_INCOMPATIBLE | 1 | Label set |
| CONTACTORS_CONNECTION_UNDEFINED | 1 | Label set |
| AFE_NOT_OFF | 1 | Label set |
| AFE_PWM_NOT_RUNNING | 1 | Label set |
| AFE_PWM_STOP_RUNNING | 1 | Label set |
| BLEEDING_FAILED | 1 | Label set |
| BI25_PWM_NOT_RUNNING | 1 | Label set |

### Payload description

#### CABLE_2_4_DC { #DC01_faults-CABLE_2_4_DC }

BI25(2).DC -> BI25(4).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_DC { #DC01_faults-CABLE_1_2_DC }

BI25(2).DC -> BP25(1).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_4_DC { #DC01_faults-CABLE_3_4_DC }

BI25(4).DC -> BI25(2).DC mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_L1_L2 { #DC01_faults-CABLE_1_L1_L2 }

BP25(1).L1 -> BI25(1).L2 mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_L2_L3 { #DC01_faults-CABLE_1_L2_L3 }

BP25(1).L2 -> BI25(1).L3 mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_L1_L2 { #DC01_faults-CABLE_3_L1_L2 }

BP25(3).L1 -> BI25(3).L2 mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_L2_L3 { #DC01_faults-CABLE_3_L2_L3 }

BP25(3).L2 -> BI25(3).L3 mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L1 { #DC01_faults-CABLE_1_3_L1 }

BP25(1).L1 -> BI25(3).L1 mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_2_IN_OUT { #DC01_faults-CABLE_2_IN_OUT }

BI25(2).IN -> BI25(2).OUT mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_IN_OUT { #DC01_faults-CABLE_4_IN_OUT }

BI25(4).IN -> BI25(4).OUT mismatch

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### MODULE_1_RUNNING { #DC01_faults-MODULE_1_RUNNING }

Module 1 running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_2_RUNNING { #DC01_faults-MODULE_2_RUNNING }

Module 2 running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_3_RUNNING { #DC01_faults-MODULE_3_RUNNING }

Module 3 running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_4_RUNNING { #DC01_faults-MODULE_4_RUNNING }

Module 4 running error

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_1_CLOSED { #DC01_faults-CONTACTOR_1_CLOSED }

Contactor 1 unexpectedly closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_2_CLOSED { #DC01_faults-CONTACTOR_2_CLOSED }

Contactor 2 unexpectedly closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_3_CLOSED { #DC01_faults-CONTACTOR_3_CLOSED }

Contactor 3 unexpectedly closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_4_CLOSED { #DC01_faults-CONTACTOR_4_CLOSED }

Contactor 4 unexpectedly closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_1_OPEN { #DC01_faults-CONTACTOR_1_OPEN }

Contactor 1 failed to close

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_2_OPEN { #DC01_faults-CONTACTOR_2_OPEN }

Contactor 2 failed to close

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_3_OPEN { #DC01_faults-CONTACTOR_3_OPEN }

Contactor 3 failed to close

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_4_OPEN { #DC01_faults-CONTACTOR_4_OPEN }

Contactor 4 failed to close

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_1_FAIL { #DC01_faults-CONTACTOR_1_FAIL }

Contactor 1 feedback failure

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_2_FAIL { #DC01_faults-CONTACTOR_2_FAIL }

Contactor 2 feedback failure

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_3_FAIL { #DC01_faults-CONTACTOR_3_FAIL }

Contactor 3 feedback failure

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CONTACTOR_4_FAIL { #DC01_faults-CONTACTOR_4_FAIL }

Contactor 4 feedback failure

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### PORT_B_OVERVOLTAGE { #DC01_faults-PORT_B_OVERVOLTAGE }

Port B overvoltage detected

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### CS_REV_INCOMPATIBLE { #DC01_faults-CS_REV_INCOMPATIBLE }

Controller board incompatible

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 27 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CONTACTORS_CONNECTION_UNDEFINED { #DC01_faults-CONTACTORS_CONNECTION_UNDEFINED }

Contactors connection state undefined

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 28 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_NOT_OFF { #DC01_faults-AFE_NOT_OFF }

AFE not off when expected

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 29 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_NOT_RUNNING { #DC01_faults-AFE_PWM_NOT_RUNNING }

AFE PWM not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 30 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_STOP_RUNNING { #DC01_faults-AFE_PWM_STOP_RUNNING }

AFE PWM stopped unexpectedly

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 31 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### BLEEDING_FAILED { #DC01_faults-BLEEDING_FAILED }

Bleeding resistor discharge failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### BI25_PWM_NOT_RUNNING { #DC01_faults-BI25_PWM_NOT_RUNNING }

Bleeding resistor discharge failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |


<a id="DC01_warning"></a>
## DC01_warning { #DC01_warning }


| * | * |
|---|---|
| **Frame ID** | 0x820043 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

DC01 Warnings

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| MODE_NOT_SUPPORTED | 1 | Label set |
| RQ_V_B_SET_ABOVE_MAX | 1 | Label set |
| RQ_V_B_SET_BELLOW_MIN | 1 | Label set |
| RQ_C_SOURCE_B_ABOVE_MAX | 1 | Label set |
| RQ_C_SOURCE_B_BELLOW_MIN | 1 | Label set |
| RQ_C_SINK_B_ABOVE_MAX | 1 | Label set |
| RQ_C_SINK_B_BELLOW_MIN | 1 | Label set |
| RQ_V_B_SET_ABOVE_A | 1 | Label set |
| RQ_DC_DROOP_POS_INVALID | 1 | Label set |
| RQ_DC_DROOP_NEG_INVALID | 1 | Label set |
| V_A_LOW | 1 | Label set |
| V_A_HIGH | 1 | Label set |
| NEED_UPDATE | 1 | Label set |

### Payload description

#### MODE_NOT_SUPPORTED { #DC01_warning-MODE_NOT_SUPPORTED }

Mode not supported

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_B_SET_ABOVE_MAX { #DC01_warning-RQ_V_B_SET_ABOVE_MAX }

Requested Port B voltage above maximum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_B_SET_BELLOW_MIN { #DC01_warning-RQ_V_B_SET_BELLOW_MIN }

Requested Port B voltage below minimum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SOURCE_B_ABOVE_MAX { #DC01_warning-RQ_C_SOURCE_B_ABOVE_MAX }

Source current Port B above maximum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SOURCE_B_BELLOW_MIN { #DC01_warning-RQ_C_SOURCE_B_BELLOW_MIN }

Source current Port B below minimum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SINK_B_ABOVE_MAX { #DC01_warning-RQ_C_SINK_B_ABOVE_MAX }

Sink current Port B above maximum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_C_SINK_B_BELLOW_MIN { #DC01_warning-RQ_C_SINK_B_BELLOW_MIN }

Sink current Port B below minimum

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_V_B_SET_ABOVE_A { #DC01_warning-RQ_V_B_SET_ABOVE_A }

Requested Port B voltage higher than Port A

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_DC_DROOP_POS_INVALID { #DC01_warning-RQ_DC_DROOP_POS_INVALID }

DC droop positive invalid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### RQ_DC_DROOP_NEG_INVALID { #DC01_warning-RQ_DC_DROOP_NEG_INVALID }

DC droop negative invalid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_LOW { #DC01_warning-V_A_LOW }

voltage port a too low

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_HIGH { #DC01_warning-V_A_HIGH }

voltage port a too high

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 11 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### NEED_UPDATE { #DC01_warning-NEED_UPDATE }

power converter need update

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |


<a id="DC01_info"></a>
## DC01_info { #DC01_info }


| * | * |
|---|---|
| **Frame ID** | 0x820044 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

DC01 Informational Flags

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| BLEEDING_DONE | 1 | Label set |
| CONTACTORS_CONNECTION_SERIAL | 1 | Label set |
| CONTACTORS_CONNECTION_PARALLEL | 1 | Label set |
| CONTACTORS_CONNECTION_OPEN | 1 | Label set |
| CONNECTION_MANAGER_RQ_CHANGE | 1 | Label set |

### Payload description

#### BLEEDING_DONE { #DC01_info-BLEEDING_DONE }

Bleeding completed successfully

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CONTACTORS_CONNECTION_SERIAL { #DC01_info-CONTACTORS_CONNECTION_SERIAL }

Contactors connected in series

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CONTACTORS_CONNECTION_PARALLEL { #DC01_info-CONTACTORS_CONNECTION_PARALLEL }

Contactors connected in parallel

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CONTACTORS_CONNECTION_OPEN { #DC01_info-CONTACTORS_CONNECTION_OPEN }

All contactors open

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CONNECTION_MANAGER_RQ_CHANGE { #DC01_info-CONNECTION_MANAGER_RQ_CHANGE }

Connection manager requests topology change

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |


<a id="DC01_debug"></a>
## DC01_debug { #DC01_debug }


| * | * |
|---|---|
| **Frame ID** | 0x8200f2 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

The setpoints that are currently used by the DC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| allow_close_contactor | 1 | Label set |

### Payload description

#### allow_close_contactor { #DC01_debug-allow_close_contactor }

The voltage target of the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |


<a id="DC01_debug_connection"></a>
## DC01_debug_connection { #DC01_debug_connection }


| * | * |
|---|---|
| **Frame ID** | 0x8200f3 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the DC01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| current_connection_mode | 8 | Label set |
| new_connection_mode | 8 | Label set |

### Payload description

#### current_connection_mode { #DC01_debug_connection-current_connection_mode }

The voltage target of the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| contactors_open | 0 |
| contactors_serial | 1 |
| contactors_parallel | 2 |
| contactors_undefined | 3 |

#### new_connection_mode { #DC01_debug_connection-new_connection_mode }

The voltage target of the A port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| contactors_open | 0 |
| contactors_serial | 1 |
| contactors_parallel | 2 |
| contactors_undefined | 3 |
