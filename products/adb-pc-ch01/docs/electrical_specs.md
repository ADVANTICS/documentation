
# Electrical Specifications

## AC Side (Mains) Specifications

### Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Rated Nominal AC Voltage (L-L)** | 208 - 480 V<sub>rms</sub> | Reduced power below 380 V<sub>rms</sub> |
| **Rated AC Frequency** | 50 / 60 Hz | ±3% tolerance |
| **Maximum AC Current** | ±150 A<sub>rms</sub> per phase | Continuous operation |
| **Power Factor (PF)** | ≥0.99 | At rated power |
| **Total Harmonic Distortion (THDi)** | ≤5% | For loads above 20% |
| **Reactive Power Control** | ±0.9 inductive-capacitive | Full power range |

### Configuration

!!! info "AC Wiring Configuration"
    - **Connection Type**: 3-phase, 3-wire (L1, L2, L3)
    - **Neutral**: Not used
    - **Ground**: PE (protective earth) connection required for safety

### Protection Features

| **Protection Type** | **Description** | **Response** |
|-------------------|----------------|--------------|
| **Overvoltage Protection**  | Monitors input voltage levels | Automatic shutdown |
| **Undervoltage Protection** | Prevents operation below minimum voltage | Automatic shutdown |
| **Overcurrent Protection**  | Current limiting and protection | Automatic current limit |
| **Overtemperature Protection** | Thermal monitoring | Shutdown at overtemperature with warning |

### Startup Characteristics

- **Internal Soft Start**: Controlled ramp-up to prevent inrush current (precharge)
- **Inrush Current**: Less than nominal current during startup
- **Phase to PE Separation**: Basic safety isolation
- **Overvoltage Category**: OVC2 (Overvoltage Category 2)

### Grid Generation Capabilities

The ADB-PC-CH01 supports requires a grid to operate. It it thus a purely grid following inverter.

## DC Side (DC Bus - Bidirectional) Specifications

### Characteristics

| **Parameter** | **Value** | **Conditions** |
|---------------|-----------|----------------|
| **Voltage Range** | 200 - 950 V DC | Minimum depends on mains voltage |
| **Current Range** | ±135 A | Bidirectional, power envelope limited |
| **Maximum Power** | 50 kW | Continuous operation |
| **Current Measurement Accuracy** | ±1% of full-scale | Over full temperature range |
| **Voltage Measurement Accuracy** | ±1% of full-scale | Over full temperature range |

### DC Protection

- **Overvoltage Protection**:  Active monitoring and shutdown
- **Undervoltage Protection**: Active monitoring and shutdown
- **Overcurrent Protection**:  Current limiting and fusing
- **Overtemperature Protection**: Overtemperature shutdown with warning

### Fusing and Contactors

- **DC Fusing**: UL/IEC rated fusing on the positive line
- **Output Contactors**: Not integrated

## Control and Communication Specifications

### Communication Interface

| **Parameter** | **Value** | **Notes** |
|---------------|-----------|-----------|
| **Protocol** | CAN 2.0B | Industry standard |
| **Baud Rate** | Configurable | 500 kbps |
| **Isolation** | Isolated from PE and 24 V | Safety isolation |

### Control Power Supply

| **Parameter** | **Value** | **Tolerance** |
|---------------|-----------|---------------|
| **Nominal Voltage** | 24 V DC | 20 - 28 V |
| **Control Power Consumption** | 50 W | During operation |
| **Standby Power Consumption** | 5 W | Idle state |

### Isolation Concept


**Connection Diagram:**

- **CAN Bus**: Isolated from power electronics and 24V supply
- **Control Power**: 24V isolated from CAN bus and HV, PE referenced
- **HV (AC,DC) side**: Reinforced isolation between AC and DC port. Basic isolation towards PE.


## Safe Operating Area

The ADB-PC-CH01 is engineered to operate reliably within a specific DC voltage range of 200V to 950V.
The module is fundamentally current limited, so the power processing capability scales with AC and DC voltage (the limit is set by whichever side can process less power).
For 480 VAC the available AC power is higher than for 400VAC. A low DC output voltage will lead to the ADB-PC-CH01 to be limited by the DC port output current, instead of the AC port current.
The device needs to be kept in it's operating temperature margins at all time so the cooling system needs
to be dimensioned according to the expected losses.

## Efficiency Characteristics

### Efficiency Performance

- **Peak Efficiency**: 98.5% at optimal operating point
- **Full Load Efficiency**: >97% across wide operating range
- **Partial Load Efficiency**: Maintaining high efficiency down to 10% load

## Power Factor & THDi

The Power Factor (PF) maintains a near-unity value of ≥0.99 for all output loads above 50%, guaranteeing minimal reactive power draw. 
Similarly, Total Harmonic Current Distortion (THDi) remaining below the 5% limit for all loads greater than 25%, fully complying with major harmonic standards. Full load THDi is below 3%.

## Harmonic Spectrum

The ADB-PC-CH01 employs a three-phase active Power Factor Correction (PFC) stage utilizing high-speed Silicon Carbide (SiC) switching technology.
This advanced architecture is designed to draw a near-sinusoidal input current, ensuring near-unity Power Factor (PF).

Due to the fundamental nature of balanced three-phase systems, the PFC action naturally minimizes even-order harmonics (2nd, 4th, etc.).
The remaining distortion is dominated by low-level, odd-order characteristic harmonics (5th, 7th, 11th, etc.)
that originate primarily from switching ripple and slight imbalances in the grid voltage or control loops.

## Parallel Operation Capability

Multiple ADB-PC-CH01 may be operated in parallel, providing a shared DC bus from a common AC grid connection.
The CH01 AC port assumes a stiff grid is present and it's operation will not significantly distort the voltage at it's AC terminals.
The CH01 DC port is configured with a 'virtual resistance' which means the CH01 DC voltage will drop when providing current and rise when absorbing current.
This behaviour allows for multiple CH01 Units to be combined in parallel without needing constant feedback via a separate communications channel.

## Environmental Electrical Specifications

### Operating Conditions

| **Parameter** | **Range** | **Derating** |
|---------------|-----------|--------------|
| **Operating Temperature** | -40°C to +70°C | Power derating applies above 50°C |
| **Storage Temperature** | -50°C to +85°C | No operation |
| **Altitude** | Up to 3000m | |
| **Pollution Degree** | 3 (external) | Sealed IP67 design |

!!! note "Power derating"
    As the liquid cooling system is controlled by the user, the unit will shut off due to overtemperature

### Electromagnetic Compatibility

- **Emissions**: Class A/B with external filter
- **Immunity**: Class A immunity (industrial)
- **Harmonics**: Compliant with IEC 61000-3-2

## Measurement and Monitoring

### Integrated Measurements

- **AC Voltage**: 3-phase voltage measurement
- **AC Current**: 3-phase current measurement with 1% accuracy
- **AC Frequency**: Grid frequency measurement
- **DC Voltage**: High voltage DC bus measurement
- **DC Current**: DC bus current estimation
- **Temperature**: Multiple temperature monitoring points

### Real-time Monitoring

All electrical parameters are continuously monitored and available through the CAN bus interface:

- Instantaneous voltage, current, and power readings
- Harmonic analysis and THD calculations
- Temperature monitoring across critical components
- Fault and status information
