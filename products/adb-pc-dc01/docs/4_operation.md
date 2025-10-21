# Operation

## Operating Modes

The ADB-PC-DC01 supports bidirectional power flow between two isolated DC buses, accommodating various application requirements:

### DC/DC Conversion Mode (Port A to Port B)

In this mode, the module converts DC power from Port A (input) to a regulated DC output power on Port B:

```mermaid
graph LR
    A["DC Source (Port A) 750-950V"] -->|DC Power| B["ADB-PC-DC01"]
    B -->|Isolated DC/DC Conversion| C["DC Load (Port B) 200-1500V"]
    B -->|CAN Control| D[System Controller]
    
    E[Voltage Monitoring] -->|Voltage Data| B
    F[Current Monitoring] -->|Current Data| B
```

**Key Features:**
- Programmable DC output voltage (200-1500V).
- Current limiting and overcurrent protection.
- High efficiency (98% peak).
- Reinforced galvanic isolation.

### DC/DC Conversion Mode (Port B to Port A)

In this mode, the module converts DC power from Port B (input) to a regulated DC output power on Port A:

```mermaid
graph LR
    A["DC Source (Port B) 200-1500V"] -->|DC Power| B["ADB-PC-DC01"]
    B -->|Isolated DC/DC Conversion| C["DC Load (Port A) 750-950V"]
    B -->|CAN Control| D[System Controller]
    
    E[Voltage Monitoring] -->|Voltage Data| B
    F[Current Monitoring] -->|Current Data| B
```

**Key Features:**
- Bidirectional power flow for applications like V2G or energy storage.
- Seamless transition between power flow directions.
- Active power management.

### Bidirectional Mode

In bidirectional mode, the module seamlessly transitions between power flow directions based on system demand:

```mermaid
sequenceDiagram
    participant SourceA
    participant ADB
    participant Controller
    participant LoadB
    
    SourceA->>ADB: DC Power Available (Port A)
    Controller->>ADB: Set Power Flow A->B
    ADB->>LoadB: DC Power Delivery (Port B)
    
    Note over LoadB: Energy Demand Changes
    
    Controller->>ADB: Set Power Flow B->A
    LoadB->>ADB: Excess DC Power (Port B)
    ADB->>SourceA: DC Power Injection (Port A)
```

## Control Interface

### CAN Bus Communication

The primary control interface is through CAN 2.0B protocol:

#### Message Structure

```
CAN Frame Structure:
- Identifier: 29-bit extended format
- Data Length: 0-8 bytes
- Bit Rate: Configurable (125 kbps to 1 Mbps)
- Frame Type: Data and Remote frames
```

#### Control Commands

| **Command Type** | **CAN ID** | **Data Bytes** | **Description** |
|------------------|------------|----------------|-----------------|
| **Power Setpoint** | 0x100 | 4 bytes | Active power reference |
| **Mode Control** | 0x101 | 1 byte | Operating mode selection |
| **Voltage Reference** | 0x102 | 2 bytes | DC voltage setpoint for Port B |
| **Status Request** | 0x103 | 0 bytes | Module status query |
| **Fault Reset** | 0x104 | 1 byte | Fault condition reset |

#### Status Messages

| **Message Type** | **CAN ID** | **Update Rate** | **Content** |
|------------------|------------|-----------------|-------------|
| **Operational Status** | 0x200 | 100ms | Mode, state, alarms |
| **Electrical Data** | 0x201 | 50ms | Voltages, currents, power (both ports) |
| **Temperature Data** | 0x202 | 1s | Module temperatures |
| **Fault Status** | 0x203 | Event-driven | Fault codes and details |

### Hardware Interlock

The hardware interlock provides safety-critical control functions:

```mermaid
graph TD
    A[Emergency Stop] -->|Hardwired| B[Interlock Input]
    C[Door Switch] -->|Hardwired| B
    D[Temperature Switch] -->|Hardwired| B
    
    B -->|Immediate| E[Power Shutdown]
    B -->|Status| F[CAN Notification]
    
    G[System Controller] -->|Enable| H[Control Logic]
    H -->|AND| E
```

## Startup Sequence

### Power-On Sequence

```mermaid
sequenceDiagram
    participant PSU
    participant ADB
    participant Controller
    
    PSU->>ADB: 24V Control Power
    ADB->>ADB: Self-Test
    ADB->>Controller: Status: Ready
    
    Controller->>ADB: Initialize Command
    ADB->>ADB: Internal Checks
    ADB->>Controller: Status: Initialized
    
    Controller->>ADB: Enable Operation
    ADB->>ADB: Soft Start Sequence
    ADB->>Controller: Status: Operating
```

### Operating State Machine

```mermaid
stateDiagram-v2
    [*] --> Off
    Off --> Initialized: Power On
    Initialized --> Ready: Self Test Pass
    Ready --> Operating: Enable Command
    
    Operating --> Fault: Fault Condition
    Operating --> Standby: Disable Command
    
    Standby --> Operating: Enable Command
    Fault --> Initialized: Fault Reset
    
    Operating --> [*]: Power Off
```

## Protection and Fault Handling

### Protection Levels

| **Protection Level** | **Response Time** | **Action** | **Recovery** |
|---------------------|-------------------|------------|--------------|
| **Level 1** | <1ms | Immediate shutdown | Manual reset required |
| **Level 2** | <10ms | Graceful shutdown | Automatic retry after delay |
| **Level 3** | <100ms | Power limiting | Automatic recovery |
| **Level 4** | <1s | Warning/alarm | No action required |

### Fault Categories

#### Critical Faults (Level 1)
- Ground fault detection
- Overcurrent protection activation (Port A or B)
- Overtemperature shutdown
- Hardware interlock activation
- Isolation fault

#### Serious Faults (Level 2)
- DC overvoltage/undervoltage (Port A or B)
- Communication loss timeout
- Internal component failure

#### Minor Faults (Level 3)
- Power derating due to temperature
- Current limiting activation
- Efficiency below expected

#### Informational (Level 4)
- Maintenance reminders
- Performance warnings
- Configuration mismatches
- Environmental alerts

### Fault Recovery Procedures

- **Fault Detection** *(Level 2)* → **Graceful Shutdown**
- **Fault Detection** *(Level 3)* → **Power Limiting**
- **Fault Detection** *(Level 4)* → **Alarm Only**
- **Immediate Shutdown** → **Fault Latch**
- **Graceful Shutdown** → **Auto Retry Timer**
- **Power Limiting** → **Monitor Recovery**
- **Alarm Only** → **Log Event**
- **Fault Latch** *(Manual Reset)* → **Restart Sequence**
- **Auto Retry Timer** *(Timer Expired)* → **Automatic Restart**
- **Monitor Recovery** *(Condition Cleared)* → **Normal Operation**
- **Log Event** → **Continue Operation**

## Performance Monitoring

### Real-time Monitoring

The module continuously monitors and reports:

#### Electrical Parameters
- DC voltage (Port A and Port B)
- DC current (Port A and Port B)
- DC power (Port A and Port B)
- Efficiency

#### Thermal Parameters
- Heat sink temperature
- Ambient temperature
- Cooling system temperature
- Power semiconductor temperature

#### Operational Parameters
- Operating mode and state
- Fault status and history
- Maintenance counters
- Runtime statistics

### Data Logging

Historical data is maintained for:
- Energy production/consumption
- Operating hours and cycles
- Fault events and timestamps
- Performance trends and analysis

## Maintenance Operations

### Routine Maintenance

!!! info "Maintenance Schedule"
    - **Daily**: Visual inspection of indicators and displays
    - **Weekly**: Check for fault codes and alarms
    - **Monthly**: Verify electrical connections and torque
    - **Quarterly**: Comprehensive performance check
    - **Annually**: Complete system inspection and testing

### Diagnostic Functions

The module provides built-in diagnostic capabilities:
- Self-test routines
- Component health monitoring
- Performance degradation analysis
- Predictive maintenance alerts

### Firmware Updates

Firmware updates can be performed through the integrated gateway:
- Secure update process with verification
- Rollback capability in case of issues
- Update scheduling to minimize downtime
- Compatibility checking before installation
