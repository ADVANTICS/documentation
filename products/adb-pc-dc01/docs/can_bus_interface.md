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

Setpoints for applying Droop on the B Port. Droop is needed for paralleling multiple DC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Enable | 4 | Label set |
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Reserved | 28 | Unsigned |

### Payload description

#### Enable { #B_Port_Droop_Setpoints-Enable }

Enable DC Droop. If this feature is enabled the output voltage of the B port varies with output current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 4 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Positive_Current_Droop { #B_Port_Droop_Setpoints-Positive_Current_Droop }

The droop resistance to apply for current flowing out of the B port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #B_Port_Droop_Setpoints-Negative_Current_Droop }

The droop resistance to apply for current flowing in to the B Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Reserved { #B_Port_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only &#x27;0&#x27;s

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 28 | Unsigned |  | 1 | 0 |  |  |


<a id="B_Port_Applied_Droop_Setpoints"></a>
## B_Port_Applied_Droop_Setpoints { #B_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820023 |
| **Length [Bytes]** | 5 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Droop setpoints that are applied by the DC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Enable | 4 | Label set |
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |

### Payload description

#### Enable { #B_Port_Applied_Droop_Setpoints-Enable }

Show is DC Droop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 4 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Positive_Current_Droop { #B_Port_Applied_Droop_Setpoints-Positive_Current_Droop }

The droop resistance applied for current flowing out of the B port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |

#### Negative_Current_Droop { #B_Port_Applied_Droop_Setpoints-Negative_Current_Droop }

The droop resistance applied for current flowing in to the B Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 16 | Unsigned | Ohm | 0.01 | 0 |  |  |


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

### Payload description


<a id="DC01_warning"></a>
## DC01_warning { #DC01_warning }


| * | * |
|---|---|
| **Frame ID** | 0x820043 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

DC01 Warning

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|

### Payload description


<a id="DC01_info"></a>
## DC01_info { #DC01_info }


| * | * |
|---|---|
| **Frame ID** | 0x820044 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

DC01 Info

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| BLEEDING_DONE | 1 | Label set |
| parallel | 1 | Label set |
| serial | 1 | Label set |

### Payload description

#### BLEEDING_DONE { #DC01_info-BLEEDING_DONE }

Current limited by power max

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### parallel { #DC01_info-parallel }

Afe are in parallel

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### serial { #DC01_info-serial }

Afe are in series

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |
