# Theory of Operation

The ADB-PC-AC01 supports multiple operating modes to accommodate various application requirements:

## Rectifier Mode (AC to DC)

In rectifier mode, the module converts AC input power to regulated DC output power:


```mermaid
graph LR
    A["AC Grid 208-480V"] -->|3-Phase AC| B["ADB-PC-AC01"]
    B -->|PFC Control| C[Power Factor Correction]
    C -->|DC Output| D["650-950V DC Bus"]
    B -->|CAN Control| E[System Controller]
    
    F[Grid Monitoring] -->|Voltage/Current| C
    G[Temperature Monitoring] -->|Thermal Data| C
```

**Key Features:**
- Active Power Factor Correction (PFC) maintains PF ≥0.99
- Low Total Harmonic Distortion (THDi ≤5%)
- Programmable DC output voltage (650-950V)
- Current limiting and overcurrent protection

## Inverter Mode (DC to AC)

In inverter mode, the module converts DC input power to AC output power:

```mermaid
graph LR
    A["DC Source 650-950V"] -->|DC Input| B["ADB-PC-AC01"]
    B -->|Inverter Control| C[Grid Synchronization]
    C -->|AC Output| D["208-480V AC Grid"]
    B -->|CAN Control| E[System Controller]
    
    F[Grid Monitoring] -->|Sync Data| C
    G[Power Control] -->|Setpoint| C
```


**Key Features:**
- Grid-tied or standalone operation
- Reactive power control (±0.9 inductive-capacitive)
- Grid forming and following capabilities
- Anti-islanding protection

## Bidirectional Mode

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
