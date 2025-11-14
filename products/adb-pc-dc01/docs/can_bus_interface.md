# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [DC01_Setpoints](#DC01_Setpoints) | 0x820009 | 6 | OUT | 1000 |
| [DC01_Current_Setpoint_Control](#DC01_Current_Setpoint_Control) | 0x820043 | 2 | IN | 1000 |
| [DC01_Voltage_Setpoint_Control](#DC01_Voltage_Setpoint_Control) | 0x820044 | 2 | IN | 1000 |
| [DC01_DC_Bus_current](#DC01_DC_Bus_current) | 0x820051 | 2 | OUT | 100 |
| [DC01_Currents](#DC01_Currents) | 0x820053 | 6 | OUT | 100 |
| [DC01_Voltages](#DC01_Voltages) | 0x820054 | 8 | OUT | 100 |


<a id="DC01_Setpoints"></a>
## DC01_Setpoints { #DC01_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x820009 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_setpoint | 16 | Signed |
| Voltage_setpoint | 16 | Unsigned |
| Reserved | 16 | Unsigned |

### Payload description

#### Current_setpoint { #DC01_Setpoints-Current_setpoint }

The actual current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Voltage_setpoint { #DC01_Setpoints-Voltage_setpoint }

The actual voltage setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Reserved { #DC01_Setpoints-Reserved }

Reserved bits for future uses

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned |  | 1 | 0 |  |  |


<a id="DC01_Current_Setpoint_Control"></a>
## DC01_Current_Setpoint_Control { #DC01_Current_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x820043 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Current setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Current_setpoint | 16 | Signed |

### Payload description

#### Current_setpoint { #DC01_Current_Setpoint_Control-Current_setpoint }

Sets the output current setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 | -220 | 220 |


<a id="DC01_Voltage_Setpoint_Control"></a>
## DC01_Voltage_Setpoint_Control { #DC01_Voltage_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x820044 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Voltage setpoint control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage_setpoint | 16 | Unsigned |

### Payload description

#### Voltage_setpoint { #DC01_Voltage_Setpoint_Control-Voltage_setpoint }

Sets the output voltage setpoint

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 | 0 | 1500 |


<a id="DC01_DC_Bus_current"></a>
## DC01_DC_Bus_current { #DC01_DC_Bus_current }


| * | * |
|---|---|
| **Frame ID** | 0x820051 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Current of the DC Bus. This is a calculated value using the phase currents and voltage difference across the converter.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Bus_current | 16 | Signed |

### Payload description

#### Bus_current { #DC01_DC_Bus_current-Bus_current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="DC01_Currents"></a>
## DC01_Currents { #DC01_Currents }


| * | * |
|---|---|
| **Frame ID** | 0x820053 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Current of flowing in U/L1, V/L2, W/L3

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |

### Payload description

#### Phase_U { #DC01_Currents-Phase_U }

Phase U current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_V { #DC01_Currents-Phase_V }

Phase V current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.01 | 0 |  |  |

#### Phase_W { #DC01_Currents-Phase_W }

Phase W current

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.01 | 0 |  |  |


<a id="DC01_Voltages"></a>
## DC01_Voltages { #DC01_Voltages }


| * | * |
|---|---|
| **Frame ID** | 0x820054 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description



### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Phase_U | 16 | Signed |
| Phase_V | 16 | Signed |
| Phase_W | 16 | Signed |
| DC | 16 | Signed |

### Payload description

#### Phase_U { #DC01_Voltages-Phase_U }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Phase_V { #DC01_Voltages-Phase_V }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Phase_W { #DC01_Voltages-Phase_W }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | V | 0.1 | 0 |  |  |

#### DC { #DC01_Voltages-DC }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | V | 0.1 | 0 |  |  |
