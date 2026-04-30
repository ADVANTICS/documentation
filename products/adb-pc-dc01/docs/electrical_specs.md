# Electrical Overview

## DC Bus Side (A)

| Parameters | Values |
|------------|--------|
| Voltage range | 750 – 950 V |
| Current | ±120 A |
| Max power | 100 kW |
| Current measurement accuracy | ±1% of full-scale |
| Voltage measurement accuracy | ±1% of full-scale |
| Wiring | DC+, DC- |
| DC link capacitance | 160 µF |
| DC link precharge | No, must be precharged externally |
| DC bus to PE separation | Reinforced isolation |
| Protection | Overvoltage, undervoltage, overcurrent, overtemperature |
| Fusing | On the positive line, UL/IEC rated |
| Connectors | 2x RADSOK size 8 mm, Amphenol SurLock Plus (SLP-HIR-B) |


<!-- ### Maximum Power vs Input Voltage

The following graph illustrates the relationship between the maximum achievable power output and the input voltage on the DC Bus Side (Port A). The maximum power is capped at 100 kW, with optimal performance within the specified voltage range of 750-950 V DC. Variations outside this range may result in derating to ensure safe and efficient operation.

{{ figure('../assets/max_power_vs_input_voltage.png', 'Maximum Power vs Input Voltage') }} -->

## DC Output Side (B)

| Parameters | Values |
|------------|--------|
| Voltage range | 200 – 1500 V |
| Current | ±220 A (bidirectional), limited by power envelope |
| Max power | 100 kW |
| Current measurement accuracy | ±1% of full-scale |
| Voltage measurement accuracy | ±1% of full-scale |
| Wiring | DC+, DC- |
| DC link capacitance | 25.7 µF (QP), 6.4 µF (QS) |
| Primary–secondary separation | Reinforced isolation |
| Ripple voltage/current | Fulfills IEC 61851-23-3 |
| Output contactors | No |
| Protection | Overvoltage, undervoltage, overcurrent, overtemperature |
| Connectors (DC) | 2x RADSOK size 10.3 mm, Amphenol SurLock Plus (SLP-HIR-C) |

<!-- ### Maximum Power vs DC wide control side Voltage

The following graph illustrates the relationship between the maximum achievable power output and the output voltage on the DC wide control side (Port B). The maximum power is capped at 100 kW, with optimal performance within the specified voltage range of 200-1500 VDC. Variations outside this range may result in derating to ensure safe and efficient operation.

{{ figure('../assets/max_power_vs_output_voltage.png', 'Maximum Power vs Output Voltage') }} -->

## Port A and Port B voltage relationship

The module operates within a nominal voltage range of 750–950 V on Port A and 200–1500 V on Port B.

These limits, however, cannot be considered independently. Not all voltage combinations between Port A and Port B are permissible. The allowable Port B voltage range depends on the actual Port A voltage.

{{ figref('fig-vrange') }} illustrates the valid operating region. The enclosed area defines the permitted combinations of Port A and Port B voltages. Operation outside this boundary is not supported and may result in protective limitation or shutdown.

{{ figure('../assets/VoltageRangePortA_PortB.png', 'Permissible Port B voltage range vs. Port A voltage range', id='fig-vrange') }}

As it can be seen in {{ figref('fig-vrange') }}, Port B can not reach 1500V unless Port A voltage is at least ~770V. A closer look at the top left corner of the envelope is shown in {{ figref('fig-vrange-zoomed') }}.

{{ figure('../assets/VoltageRangePortA_PortB_zoomedIn.png', 'Closer look at the top left corner of Figure 4', id='fig-vrange-zoomed') }}

## Maximum power vs. port A voltage

The relationship between the maximum deliverable power and the Port A voltage is shown in {{ figref('fig-maxpower-va') }}. The system output is limited to 100 kW, with a maximum Port A current of 120 A. The effective power ceiling is determined by whichever of these constraints is reached first. Operation beyond this defined envelope will trigger derating to maintain safe performance.

{{ figure('../assets/MaximumOutputPowervsPortAvoltage.png', 'Maximum output power vs. Port A voltage', id='fig-maxpower-va') }}

## Maximum power vs. port B voltage


The maximum power capability is also influenced by the Port B voltage. Output is constrained by the lower of the following limits:

- The maximum power permitted as a function of VA (refer to {{ figref('fig-maxpower-va') }}), or
- Port B current limit of 220 A.

Whichever threshold is reached first defines the allowable operating point.

Startup conditions further shape the power profile of the ADB-PC-DC01. Two startup modes are available: Quasi Parallel (QP) and Quasi Series (QS).

The module dynamically reconfigures its internal connections according to the requested or actual VB, ensuring the highest possible deliverable power. The selected startup mode depends on the ratio between VB and VA:

- If VB is less than 90 % of VA, the unit initializes in QP mode.
- Otherwise, it initializes in QS mode.

To prevent oscillation between configurations, a hysteresis mechanism governs the transition between QP and QS. The switchover behavior is depicted in {{ figref('fig-hysteresis') }}.

{{ figure('../assets/hysteresis.png', 'Hysteresis switchover based on VB/VA ratio', id='fig-hysteresis') }}


**Example:**

Assume VA=900V.

- If the requested VB is below 810 V (90 % of VA), the module starts in QP mode.
- In QP mode, Port B can source or sink up to 220 A between 200V and 855 V.
- At 855 V, the system transitions to QS mode.
- In QS mode, Port B can source or sink up to 110 A between 855 V and 1500 V.

Depending on the application’s operating range, a transition between modes may not occur (see Figure 7).

Because of the hysteresis-controlled switchover, the power curves of the ADB-PC-DC01 vary with startup condition. Representative curves for VA=750, 850 V, and 950 V are shown in the figures below. These plots define the maximum achievable module power for a given startup condition, VA, and VB.

For performance data at a specific VA, contact ADVANTICS helpdesk.

**Port A = 750 V**

{{ figure('../assets/750P.png', 'Maximum Power vs. Port B Voltage (VA = 750V, QP Mode)') }}

{{ figure('../assets/750S.png', 'Maximum Power vs. Port B Voltage (VA = 750V, QS Mode)') }}

**Port A = 850 V**

{{ figure('../assets/850P.png', 'Maximum Power vs. Port B Voltage (VA = 850V, QP Mode)') }}

{{ figure('../assets/850S.png', 'Maximum Power vs. Port B Voltage (VA = 850V, QS Mode)') }}

**Port A = 950 V**

{{ figure('../assets/950P.png', 'Maximum Power vs. Port B Voltage (VA = 950V, QP Mode)') }}

{{ figure('../assets/950S.png', 'Maximum Power vs. Port B Voltage (VA = 950V, QS Mode)') }}


## Safe Operating Area

The Safe Operating Area (SOA) graph provides a V-I plot illustrating the maximum allowable current versus voltage for the 100 kW power envelope. This boundary ensures safe operation without exceeding thermal or electrical limits.

It's important to note that the system is fully bidirectional. The graph shown below therefore spans ±220 A.

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

{{ figure('../assets/dc01_system_architecture.webp', 'System Architecture using ADVANTICS modules') }}

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
| **Operating Temperature** | -40°C to 70°C | Power derating applies above 50°C |
| **Storage Temperature** | -50°C to 85°C | No operation |
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

