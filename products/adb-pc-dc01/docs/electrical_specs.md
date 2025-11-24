# Electrical Specifications

## Port A (DC Bus Side) specifications

### Characteristics

| **Parameter** | **Value** | **Notes** |
|---------------|-----------|-----------|
| **Voltage** | 750 - 950 V | - |
| **Current** | ±120 A | - |
| **Max Power** | 100 kW | - |
| **Current Measurement Accuracy** | ±1 % | Of full-scale |
| **Voltage Measurement Accuracy** | ±1 % | Of full-scale |
| **Wiring** | DC+, DC- | - |
| **DC Link Capacitance** | 160 uF | - |
| **DC Link Precharge** | No | Must be precharged externally |
| **DC Bus to PE Separation** | Basic safety isolation | - |
| **Protection** | Overvoltage, Undervoltage, Overcurrent, Overtemperature | - |
| **Fusing** | On the positive line | UL/IEC rated |
| **Overvoltage Category** | OVC2 | - |
| **Connectors** | 2x RADSOK Size 8mm Amphenol SurLock Plus (SLP-HIR-B) | - |


### Maximum Power vs Input Voltage

The following graph illustrates the relationship between the maximum achievable power output and the input voltage on the DC Bus Side (Port A). The maximum power is capped at 100 kW, with optimal performance within the specified voltage range of 750-950 V DC. Variations outside this range may result in derating to ensure safe and efficient operation.

{{ figure('../assets/max_power_vs_input_voltage.png', 'Maximum Power vs Input Voltage') }}

## Port B (DC wide control side) specifications

### Characteristics

| **Parameter** | **Value** | **Notes** |
|---------------|-----------|-----------|
| **Voltage Range** | 200 - 1500 V | - |
| **Current** | ±220 A | Bi-directional, limited by power envelope |
| **Max Power** | 100 kW | - |
| **Current Measurement Accuracy** | ±1 % | Of full-scale |
| **Voltage Measurement Accuracy** | ±1 % | Of full-scale |
| **Wiring** | DC+, DC- | - |
| **DC Link Capacitance** | 80 uF | - |
| **Primary-Secondary Separation** | Reinforced Isolation | - |
| **Ripple Voltage/Current** | Fulfills IEC 61851-23-3 | - |
| **Overvoltage Category** | OVC2 | - |
| **Output Contactors** | No | - |
| **Fusing** | No | - |
| **Protection** | Overvoltage, Undervoltage, Overcurrent, Overtemperature | - |
| **Connectors DC** | 2x RADSOK Size 10.3mm Amphenol SurLock Plus (SLP-HIR-C) | - |

### Maximum Power vs DC wide control side Voltage

The following graph illustrates the relationship between the maximum achievable power output and the output voltage on the DC wide control side (Port B). The maximum power is capped at 100 kW, with optimal performance within the specified voltage range of 200-1500 VDC. Variations outside this range may result in derating to ensure safe and efficient operation.

{{ figure('../assets/max_power_vs_output_voltage.png', 'Maximum Power vs Output Voltage') }}


## Safe Operating Area

The Safe Operating Area (SOA) graph provides a V-I plot illustrating the maximum allowable current versus voltage for the 100 kW power envelope. This boundary ensures safe operation without exceeding thermal or electrical limits.

It's important to note that the system is fully bidirectional - graph therefore spans ±220 A.

{{ figure('../assets/soa_outputs.png', 'Safe Operating Area') }}

## Efficiency Characteristics

### Efficiency Performance

- **Peak Efficiency**: 98% at optimal operating point
- **Full Load Efficiency**: >97% across wide operating range
- **Partial Load Efficiency**: Maintained high efficiency down to 10% load

**Efficiency Curve**

The following graph shows the efficiency curve of the ADB-PC-DC01 across various load conditions. It demonstrates the high efficiency maintained from 20% to 100% load, peaking at 98% at the optimal point.

{{ figure('../assets/efficiency_curve.png', 'Efficiency Curve') }}


## Transient Response

### Load Step Response

The ADB-PC-DC01 converter demonstrates robust transient response to load steps, maintaining output voltage stability during rapid load changes. This ensures reliable operation in dynamic environments.

{{ figure('../assets/output_voltage_transient_response_load_step.png', 'Output Voltage Transient Response Load Step') }}

The graph depicts Port B voltage behavior during a load step, highlighting low overshoot and fast recovery to steady-state conditions.


### Output Ripple and Noise

The ADB-PC-DC01 converter maintains low voltage ripple and noise to ensure stable and clean DC power delivery across the full operating range. Ripple is measured as the peak-to-peak variation in output voltage under steady-state conditions.

| **Parameter** | **Value** | **Notes** |
|---------------|-----------|-----------|
| **Output Voltage Ripple (Peak-to-Peak)** | < 1% of nominal voltage | At full load (100 kW), 1500 V output |
| **Output Noise (RMS)** | < 0.1% of nominal voltage | Broadband noise up to 1 MHz |
| **Measurement Conditions** | 1500 V output at 100 kW load | Steady-state, no load transients |

The following graph shows the FFT spectrum of the output voltage ripple for the 1500 V output at 100 kW load, illustrating the low harmonic content and noise levels.

{{ figure('../assets/voltage_ripple_fft_spectrum.png', 'Output Voltage Ripple FFT Spectrum') }}

## Parallel Operation Capability

- **Maximum Units**: Up to 120 modules in parallel
- **Load Sharing**: Intelligent droop technology for automatic load sharing
- **Communication**: Isolated CAN bus for inter-module communication
- **Scalability**: Linear power scaling with additional modules
- **Redundancy**: System continues operation with failed modules

{{ figure('../assets/dc01_system_architecture.webp', 'System Architecture') }}

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


- **CAN Bus**: Isolated from power electronics and 24V supply
- **Control Power**: 24V isolated from CAN bus and HV, PE referenced
- **Primary-Secondary Isolation**: Reinforced isolation between Port A and Port B
- **Port A to PE Isolation**: Basic safety isolation
- **Port B to PE Isolation**: Reinforced safety isolation and basic safety isolation, depending on the voltage

## Environmental Electrical Specifications

### Operating Conditions

| **Parameter** | **Range** | **Derating** |
|---------------|-----------|--------------|
| **Operating Temperature** | -40°C to +70°C | Power derating applies above 50°C |
| **Storage Temperature** | -50°C to +85°C | No operation |
| **Altitude** | Up to 3000m | |
| **Pollution Degree** | 3 (external) | Sealed IP67 design |

### Electromagnetic Compatibility

- **Emissions**: Class A/B with external filter
- **Immunity**: Class A immunity (industrial)
- **Harmonics**: Compliant with IEC 61000-3-2

## Measurement and Monitoring

### Integrated Measurements

- **DC Voltage (Port A)**: DC bus measurement
- **DC Current (Port A)**: Bidirectional current measurement
- **DC Voltage (Port B)**: DC bus measurement
- **DC Current (Port B)**: Bidirectional current measurement
- **Temperature**: Multiple temperature monitoring points

### Real-time Monitoring

All electrical parameters are continuously monitored and available through the CAN bus interface:

- Instantaneous voltage, current, and power readings for both DC ports
- Temperature monitoring across critical components
- Fault and status information

