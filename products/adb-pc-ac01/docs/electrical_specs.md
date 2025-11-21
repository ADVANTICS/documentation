
# Electrical Specifications

## AC Side (Mains) Specifications

### Input Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Rated Nominal AC Voltage (L-L)** | 208 - 480 V<sub>rms</sub> | Reduced power below 380 V<sub>rms</sub> |
| **Rated AC Frequency** | 50 / 60 Hz | ±3% tolerance |
| **Maximum AC Current** | ±150 A<sub>rms</sub> per phase | Continuous operation |
| **Power Factor (PF)** | ≥0.99 | At rated power |
| **Total Harmonic Distortion (THDi)** | ≤5% | For loads above 20% |
| **Reactive Power Control** | ±0.9 inductive-capacitive | Full power range |

### Input Configuration

!!! info "AC Wiring Configuration"
    - **Connection Type**: 3-phase, 3-wire (L1, L2, L3)
    - **Neutral**: Not used
    - **Ground**: PE (protective earth) connection required for safety

### Protection Features

| **Protection Type** | **Description** | **Response** |
|-------------------|----------------|--------------|
| **Overvoltage Protection** | Monitors input voltage levels | Automatic shutdown |
| **Undervoltage Protection** | Prevents operation below minimum voltage | Automatic shutdown |
| **Overcurrent Protection** | Current limiting and protection | Automatic current limit |
| **Overtemperature Protection** | Thermal monitoring | Gradual power reduction |

### Startup Characteristics

- **Internal Soft Start**: Controlled ramp-up to prevent inrush current (precharge)
- **Inrush Current**: Less than nominal current during startup
- **Phase to PE Separation**: Basic safety isolation
- **Overvoltage Category**: OVC2 (Overvoltage Category 2)

### Grid Generation Capabilities

The ADB-PC-AC01 supports multiple grid operation modes:

- **Grid Forming**: Can create and stabilize a local grid
- **Grid Following**: Synchronizes with existing grid
- **Microgrid Operation**: Seamless transition between grid-tied and island modes

!!! note "Grid Forming / AC microgrids"
    While the ADB-PC-AC01 supports AC microgrid and grid forming operation, **the primary purpose of this unit is grid following**.
    In case you want to build a genset or an AC microgrid system, please use ADB-PC-GN01 (genset module) instead. 
    ADB-PC-GN01 also contains Neutral wire (needed for unbalanced operations and 1-phase loads), and has higher overload capability.

## DC Side (DC Bus - Bidirectional) Specifications

### Output Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Voltage Range** | 650 - 950 V DC | Minimum depends on mains voltage |
| **Current Range** | ±170 A | Bidirectional, power envelope limited |
| **Maximum Power** | 100 kW | Continuous operation |
| **Current Measurement Accuracy** | ±1% of full-scale | Over temperature range |
| **Voltage Measurement Accuracy** | ±1% of full-scale | Over temperature range |

### DC Configuration

!!! warning "Non-Isolated PFC"
    The ADB-PC-AC01 is a non-isolated PFC. If your system requires isolation, it needs to be handled by a DC/DC converter or a mains transformer.

### DC Protection

- **Overvoltage Protection**: Active monitoring and shutdown
- **Undervoltage Protection**: Active monitoring and shutdown
- **Overcurrent Protection**: Current limiting and fusing
- **Overtemperature Protection**: Thermal management system

### Fusing and Contactors

- **DC Fusing**: UL/IEC rated fusing on positive line
- **Output Contactors**: Not integrated (external contactors required)

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


## Safe Operating Area

The ADB-PC-AC01 is engineered to operate reliably within a specific DC voltage range of $650 \text{ V}$ to $950 \text{ V}$.The module's maximum output is always controlled by its $100 \text{ kW}$ power rating. This means that as the voltage gets lower (closer to $650 \text{ V}$), the current the module can handle automatically increases to maintain that $100 \text{ kW}$ limit.  
For long-term reliability, especially in high-temperature environments, we recommend keeping the operating point slightly inside these limits.

{{ figure('../assets/afe_soa_plot.webp', 'Safe Operating Area') }}

## Efficiency Characteristics

### Efficiency Performance

- **Peak Efficiency**: 98.5% at optimal operating point
- **Full Load Efficiency**: >97% across wide operating range
- **Partial Load Efficiency**: Maintained high efficiency down to 20% load

**Efficiency Curve**

The ADB-PC-AC01 Active Frontend achieves its peak of 98.5% at full load (100 kW) when using the highest input voltage (480 V). The unit maintains strong performance across the operational range as illustraited in the following efficiency curve:

{{ figure('../assets/afe_efficiency_plot.webp', 'Efficiency Curve') }}

## Power Factor & THDi

The Power Factor (PF) maintains a near-unity value of $\ge 0.99$ for all output loads above 50%, guaranteeing minimal reactive power draw. Similarly, Total Harmonic Distortion of Current (THDi) is aggressively managed, remaining below the stringent $5\%$ limit for all loads greater than $25\%$, fully complying with major harmonic standards.

{{ figure('../assets/afe_pf_thdi_plots.webp', 'Power Factor & THDi vs Load') }}

## Harmonic Spectrum

The ADB-PC-AC01 employs a three-phase active Power Factor Correction (PFC) stage utilizing high-speed Silicon Carbide (SiC) switching technology. This advanced architecture is designed to draw a near-sinusoidal input current, ensuring near-unity Power Factor (PF) across most of the operating range.  

Due to the fundamental nature of balanced three-phase systems, the PFC action naturally minimizes even-order harmonics (2nd, 4th, etc.). The remaining distortion is dominated by low-level, odd-order characteristic harmonics (5th, 7th, 11th, etc.) that originate primarily from switching ripple and slight imbalances in the grid voltage or control loops. As confirmed by the plot, the overall harmonic content is maintained well below industry standards (e.g., IEEE 519), with THDi typically remaining $\le 5\%$ at full power.

{{ figure('../assets/afe_harmonic_spectrum.webp', 'Harmonic Spectrum') }}


## Parallel Operation Capability

- **Maximum Units**: Up to 120 modules in parallel
- **Load Sharing**: Intelligent droop technology for automatic load sharing
- **Communication**: Isolated CAN bus for inter-module communication
- **Scalability**: Linear power scaling with additional modules
- **Redundancy**: System continues operation with failed modules
- **Maintenance**: Hot-swappable capability for service

{{ figure('../assets/ac01_system_architecture.webp', 'Parallel System') }}

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