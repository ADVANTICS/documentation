
# Operation

## Operating Modes

The ADB-PC-AC01 supports multiple operating modes to accommodate various application requirements:

### Rectifier Mode (AC to DC)

In rectifier mode, the module converts AC input power to regulated DC output power:


```mermaid
graph LR
    A[AC Grid 208-480V] -->|3-Phase AC| B[ADB-PC-AC01]
    B -->|PFC Control| C[Power Factor Correction]
    C -->|DC Output| D[650-950V DC Bus]
    B -->|CAN Control| E[System Controller]
    
    F[Grid Monitoring] -->|Voltage/Current| C
    G[Temperature Monitoring] -->|Thermal Data| C
```

**Key Features:**
- Active Power Factor Correction (PFC) maintains PF ≥0.99
- Low Total Harmonic Distortion (THDi ≤5%)
- Programmable DC output voltage (650-950V)
- Current limiting and overcurrent protection

### Inverter Mode (DC to AC)

In inverter mode, the module converts DC input power to AC output power:

```mermaid
graph LR
    A[DC Source 650-950V] -->|DC Input| B[ADB-PC-AC01]
    B -->|Inverter Control| C[Grid Synchronization]
    C -->|AC Output| D[208-480V AC Grid]
    B -->|CAN Control| E[System Controller]
    
    F[Grid Monitoring] -->|Sync Data| C
    G[Power Control] -->|Setpoint| C
```


**Key Features:**
- Grid-tied or standalone operation
- Reactive power control (±0.9 inductive-capacitive)
- Grid forming and following capabilities
- Anti-islanding protection

### Bidirectional Mode

In bidirectional mode, the module seamlessly transitions between rectifier and inverter operation:


```mermaid
sequenceDiagram
    participant Grid
    participant ADB
    participant Controller
    participant Load
    
    Grid->>ADB: AC Power Available
    Controller->>ADB: Set Rectifier Mode
    ADB->>Load: DC Power Delivery
    
    Note over Load: Energy Demand Changes
    
    Controller->>ADB: Set Bidirectional Mode
    Load->>ADB: Excess DC Power
    ADB->>Grid: AC Power Injection
    
    Note over Grid: Grid Requirements Change
    
    Controller->>ADB: Set Inverter Mode
    ADB->>Grid: Full Power Export
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
| **Voltage Reference** | 0x102 | 2 bytes | DC voltage setpoint |
| **Status Request** | 0x103 | 0 bytes | Module status query |
| **Fault Reset** | 0x104 | 1 byte | Fault condition reset |

#### Status Messages

| **Message Type** | **CAN ID** | **Update Rate** | **Content** |
|------------------|------------|-----------------|-------------|
| **Operational Status** | 0x200 | 100ms | Mode, state, alarms |
| **Electrical Data** | 0x201 | 50ms | Voltages, currents, power |
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
    participant Grid
    
    PSU->>ADB: 24V Control Power
    ADB->>ADB: Self-Test
    ADB->>Controller: Status: Ready
    
    Controller->>ADB: Initialize Command
    ADB->>ADB: Internal Checks
    ADB->>Controller: Status: Initialized
    
    Grid->>ADB: AC Voltage Present
    ADB->>ADB: Grid Synchronization
    ADB->>Controller: Status: Synchronized
    
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
    Ready --> Synchronized: Grid Detected
    Synchronized --> Operating: Enable Command
    
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

### 4.4.2 Fault Categories

#### Critical Faults (Level 1)
- Ground fault detection
- Overcurrent protection activation
- Overtemperature shutdown
- Hardware interlock activation

#### Serious Faults (Level 2)
- AC overvoltage/undervoltage
- DC overvoltage/undervoltage
- Communication loss timeout
- Grid synchronization loss

#### Minor Faults (Level 3)
- Power derating due to temperature
- Current limiting activation
- Harmonic distortion threshold
- Efficiency below expected

#### Informational (Level 4)
- Maintenance reminders
- Performance warnings
- Configuration mismatches
- Environmental alerts

### Fault Recovery Procedures


**Connection Diagram:**

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
- AC voltage (L1, L2, L3 to neutral and line-to-line)
- AC current (per phase)
- AC power (active, reactive, apparent)
- Power factor and THD
- DC voltage and current
- DC power and efficiency

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