# Overview

## Product Description

The **ADB-PC-DC01** is a high-performance 100kW 1500V DC/DC Isolated Power Converter, part of the ADVANTICS ADB Series. This modular and stackable power module is specifically designed for demanding applications such as DC Fast Charge stations supporting CCS, NACS, and MCS charging standards, as well as various energy storage systems and industrial power systems. Its robust, fully sealed, and liquid-cooled design ensures exceptional reliability across diverse operating environments, from corrosive coastal regions to extreme temperatures.

!!! info "Key Features"
    - **Bidirectional DC/DC**: Supports power flow in both directions between two DC buses.
    - **High Voltage Output**: Wide output range from 200V to 1500V, compatible with MCS (Megawatt Charging System) requirements.
    - **High Efficiency**: Peak efficiency of 98% across a wide power range, minimizing energy losses.
    - **SiC Technology**: Utilizes advanced Silicon Carbide technology for superior performance and efficiency.
    - **Integrated Isolation**: Reinforced galvanic isolation between input and output for enhanced safety.
    - **Scalable Design**: Up to 120 units can be paralleled for MW-level applications (up to 6MW).
    - **Harsh Environment Ready**: IP67 sealed design with liquid cooling, eliminating the need for air circulation.
    - **Advanced Control**: Integrated CAN bus control with hardware interlock for precise management and safety.
    - **Integrated Gateway**: Facilitates easy firmware updates and cybersecurity features.

## Applications

The ADB-PC-DC01 is suitable for a wide range of applications requiring isolated bidirectional DC/DC conversion:

### Electric Vehicle Charging
- DC Fast Charge stations supporting CCS1, CCS2, NACS, MCS, and CHAdeMO standards.
- Battery-assisted charging systems.
- Vehicle-to-Grid (V2G) systems.
- Onboard charging for off-highway and heavy-duty machinery.
- EV and charge simulators.

### Energy Storage Systems
- Grid-tied and off-grid energy storage systems.
- AC and DC microgrids.
- Industrial energy management.

### Industrial Applications
- Laboratory bidirectional power supplies.
- High-power DC bus management.
- Industrial power systems requiring galvanic isolation.

### Harsh Environments
- Marine and coastal applications.
- Mining operations.
- Extreme temperature environments (-40°C to +70°C).

## Main Characteristics

| **Characteristic** | **Value** | **Benefit** |
|-------------------|-----------|-------------|
| **Technology** | Silicon Carbide (SiC) | Higher efficiency, reduced losses, compact design |
| **Power Rating** | 100kW | Suitable for high-power applications |
| **Efficiency** | 98% peak | Energy savings, reduced cooling requirements |
| **Isolation** | Reinforced galvanic | Enhanced safety and system integrity |
| **Input Voltage** | 750 - 950 V DC | Flexible integration with various DC sources |
| **Output Voltage** | 200 - 1500 V DC | MCS compliant, wide application range |
| **Cooling** | Liquid cooled | Silent operation, harsh environment capability |
| **Protection** | IP67 | Dust and water resistant, robust for outdoor use |
| **Control** | CAN 2.0B | Industry-standard communication, precise control |

## System Architecture

The ADB-PC-DC01 is designed as part of the modular ADB Series system, allowing for flexible configuration and scaling for MW-level power systems.

<div style="text-align: center; margin: 4rem 0;">
    <img src="assets/dc01_system_architecture.svg" alt="System Architecture" style="width: auto; height: auto;">
</div>

### Key Architectural Features:

- **Stackable Design**: Modules can be combined for higher power applications, up to 6MW.
- **Common DC Bus**: Shared DC link for distributed DC-coupled systems.
- **Integrated Gateway**: Enables firmware updates and cybersecurity features.
- **Intelligent Droop Technology**: Automatic load sharing in parallel configurations.

### Application example: MCS (Megawatt Charging System)

The modular design of ADVANTICS's ADB power modules series allows creating creating megawatt level systems using 1 MW building blocks in 100kW steps.  
**These 1MW building block can be duplicated as much as needed to reach the targeted power level.**  
In our example here, the MCS charger is built using:
- 1MW AC/DC PFC Building block based on the ADB-PC-AC01 power module.
- 1MW DC/DC isolated Building block based on the ADB-PC-DC01 power module.

<div style="text-align: center; margin: 4rem 0;">
    <img src="assets/ac01_dc01_mcs_example.png" alt="System Architecture" style="width: auto; height: auto;">
</div>

## Compliance and Standards

The ADB-PC-DC01 is designed to meet major international standards for EV charging and power conversion:

### Safety Standards
- IEC 61851-1 (Electric vehicle conductive charging system)
- IEC 61851-23 ED2 (DC electric vehicle charging station)
- IEC 62477-1 (Safety requirements for power electronic converter systems)
- UL 2202 (Electric vehicle charging system equipment)
- UL 1741 (Inverters, converters, controllers and interconnection system equipment)

### Charging Standards
- MCS (Megawatt Charging System) compliant (200V-1500V output range)
- CCS1, CCS2, NACS, CHAdeMO compatible

### Electromagnetic Compatibility
- EMC Class B with external filter

## Design Philosophy

As a vertically integrated company, Advantics maintains complete control over the design and manufacturing process:

!!! note "Vertical Integration Benefits"
    - No reliance on third-party "black boxes"
    - Full customer control over system configuration
    - Rapid customization and optimization
    - Comprehensive technical support
    - Long-term product availability

All Advantics products are proudly designed and manufactured in the European Union, ensuring high quality standards and supply chain reliability.

## Environmental Responsibility

The ADB-PC-DC01 is designed with environmental considerations:

- High efficiency reduces energy consumption and carbon footprint.
- Liquid cooling eliminates fan noise and reduces maintenance.
- Sealed design prevents environmental contamination.
- Long design life reduces electronic waste.
- Recyclable materials used in construction.
