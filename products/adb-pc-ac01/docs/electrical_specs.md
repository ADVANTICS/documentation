
# Electrical Specifications

## AC Side (Mains) Specifications

### Input Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Rated AC Voltage (L-L)** | 208 - 480 V<sub>rms</sub> | Reduced power below 380 V<sub>rms</sub> |
| **Rated AC Frequency** | 50 / 60 Hz | ±3% tolerance |
| **Maximum AC Current** | ±150 A<sub>rms</sub> per phase | Continuous operation |
| **Power Factor (PF)** | ≥0.99 | At rated power |
| **Total Harmonic Distortion (THDi)** | ≤5% | For loads above 20% |
| **Reactive Power Control** | ±0.9 inductive-capacitive | Full power range |

### Input Configuration

!!! info "AC Wiring Configuration"
    - **Connection Type**: 3-phase, 3-wire (L1, L2, L3)
    - **Neutral**: Not required
    - **Ground**: PE connection required for safety

### Protection Features

| **Protection Type** | **Description** | **Response** |
|-------------------|----------------|--------------|
| **Overvoltage Protection** | Monitors input voltage levels | Automatic shutdown |
| **Undervoltage Protection** | Prevents operation below minimum voltage | Automatic shutdown |
| **Overcurrent Protection** | Current limiting and protection | Automatic current limit |
| **Overtemperature Protection** | Thermal monitoring | Graceful power reduction |

### Startup Characteristics

- **Internal Soft Start**: Controlled ramp-up to prevent inrush current
- **Inrush Current**: Less than nominal current during startup
- **Phase to PE Separation**: Basic isolation for safety
- **Overvoltage Category**: OVC2 (Overvoltage Category 2)

### Grid Generation Capabilities

The ADB-PC-AC01 supports multiple grid operation modes:

- **Grid Forming**: Can create and stabilize a local grid
- **Grid Following**: Synchronizes with existing grid
- **Microgrid Operation**: Seamless transition between grid-tied and island modes

## DC Side (Output - Bidirectional) Specifications

### Output Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Voltage Range** | 650 - 950 V DC | Minimum depends on mains voltage |
| **Current Range** | ±170 A | Bidirectional, power envelope limited |
| **Maximum Power** | 100 kW | Continuous operation |
| **Current Measurement Accuracy** | ±1% of full-scale | Over temperature range |
| **Voltage Measurement Accuracy** | ±1% of full-scale | Over temperature range |

### DC Configuration

!!! warning "Non-Isolated Design"
    The ADB-PC-AC01 features non-isolated primary-secondary separation. Ensure proper system grounding and safety measures are implemented.

### DC Protection

- **Overvoltage Protection**: Active monitoring and shutdown
- **Undervoltage Protection**: Prevents deep discharge
- **Overcurrent Protection**: Current limiting and fusing
- **Overtemperature Protection**: Thermal management system

### Fusing and Contactors

- **DC Fusing**: UL/IEC rated fusing on positive line
- **Output Contactors**: Not integrated (external contactors required)
- **Protection Coordination**: Designed for selective protection

## Control and Communication Specifications

### Communication Interface

| **Parameter** | **Value** | **Notes** |
|---------------|-----------|-----------|
| **Protocol** | CAN 2.0B | Industry standard |
| **Baud Rate** | Configurable | Up to 1 Mbps |
| **Isolation** | Isolated from PE and 24V | Safety isolation |

### Control Power Supply

| **Parameter** | **Value** | **Tolerance** |
|---------------|-----------|---------------|
| **Nominal Voltage** | 24 V DC | 20 - 28 V |
| **Control Power Consumption** | 50 W | During operation |
| **Standby Power Consumption** | 5 W | Idle state |

### Isolation Concept


**Connection Diagram:**

- **CAN Bus Isolation**: Isolated from power electronics and 24V supply
- **Control Power Isolation**: 24V control isolated from power section
- **Safety Isolation**: Basic isolation towards PE, reinforced towards HV

## Paralleling Specifications

### Parallel Operation Capability

- **Maximum Units**: Up to 120 modules in parallel
- **Load Sharing**: Intelligent droop technology for automatic load sharing
- **Communication**: Isolated CAN bus for inter-module communication
- **Scalability**: Linear power scaling with additional modules

### Parallel Configuration

!!! info "Parallel Operation Benefits"
    - **Redundancy**: System continues operation with failed modules
    - **Scalability**: Power can be increased by adding modules
    - **Efficiency**: Optimized operation across wide load ranges
    - **Maintenance**: Hot-swappable capability for service

## Efficiency Characteristics

### Efficiency Performance

- **Peak Efficiency**: 98.5% at optimal operating point
- **Full Load Efficiency**: >97% across wide operating range
- **Partial Load Efficiency**: Maintained high efficiency down to 20% load

### Loss Distribution

| **Component** | **Loss Contribution** | **Optimization** |
|---------------|---------------------|------------------|
| **Power Semiconductors** | ~60% | SiC technology minimizes losses |
| **Magnetics** | ~25% | Optimized core materials |
| **Control Electronics** | ~10% | Efficient power management |
| **Auxiliary Systems** | ~5% | Minimal auxiliary power draw |

## Environmental Electrical Specifications

### Operating Conditions

| **Parameter** | **Range** | **Derating** |
|---------------|-----------|--------------|
| **Operating Temperature** | -40°C to +70°C | Power derating applies above 50°C |
| **Storage Temperature** | -50°C to +85°C | No operation |
| **Altitude** | Up to 3000m | Derating above 2000m |
| **Pollution Degree** | 3 (external) | Sealed design protects internals |

### Electromagnetic Compatibility

- **EMC Class**: Class B with external filter
- **Emissions**: Compliant with CISPR 11/22
- **Immunity**: Compliant with IEC 61000-4 series
- **Harmonics**: Compliant with IEC 61000-3-2

## Measurement and Monitoring

### Integrated Measurements

- **AC Voltage**: 3-phase voltage measurement
- **AC Current**: 3-phase current measurement with 1% accuracy
- **DC Voltage**: High voltage DC bus measurement
- **DC Current**: Bidirectional current measurement
- **Temperature**: Multiple temperature monitoring points

### Real-time Monitoring

All electrical parameters are continuously monitored and available through the CAN bus interface:

- Instantaneous voltage, current, and power readings
- Harmonic analysis and THD calculations
- Temperature monitoring across critical components
- Fault and status information
- Historical data logging capability