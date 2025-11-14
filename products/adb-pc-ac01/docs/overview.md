# Overview

## Product Description

The **ADB-PC-AC01** is a high-performance 100kW bidirectional AC/DC Active Frontend (PFC) power module designed for demanding industrial applications. Built with advanced Silicon Carbide (SiC) technology, this module delivers exceptional efficiency and power quality in a compact, robust package.

!!! info "Key Features"
    - **Bidirectional Operation**: Supports both AC-to-DC and DC-to-AC power conversion
    - **High Efficiency**: Peak efficiency of 98.5% reduces energy losses and operating costs
    - **Wide Input Range**: Universal AC input from 208-480VAC, 50/60Hz
    - **Advanced Control**: Integrated CAN bus control with hardware interlock
    - **Scalable Design**: Up to 120 units can be paralleled for MW-level applications
    - **Harsh Environment Ready**: IP67 sealed design with liquid cooling

## Applications

The ADB-PC-AC01 is suitable for a wide range of applications requiring bidirectional AC/DC rectification with excellent power factor:

### Electric Vehicle Charging
- DC Fast Charge stations supporting CCS1, CCS2, NACS, MCS, and CHAdeMO standards
- Battery assisted charging systems
- Vehicle-to-Grid (V2G) applications

### Energy Storage Systems
- Grid-tied energy storage systems
- AC and DC microgrids
- Industrial energy management

### Industrial Applications
- Industrial PFC rectifiers
- Laboratory bidirectional power supplies
- EV and charge simulators
- Onboard charging for off-highway and heavy-duty machinery

### Harsh Environments
- Marine and coastal applications
- Mining operations
- Extreme temperature environments (-40°C to +70°C)

## Main Characteristics

| **Characteristic** | **Value** | **Benefit** |
|-------------------|-----------|-------------|
| **Technology** | Silicon Carbide (SiC) | Higher efficiency, reduced losses |
| **Power Rating** | 100kW | Suitable for high-power applications |
| **Efficiency** | 98.5% peak | Energy savings, reduced cooling requirements |
| **Power Factor** | ≥0.99 | Excellent grid compatibility |
| **THDi** | ≤5% | Low harmonic distortion |
| **Cooling** | Liquid cooled | Silent operation, harsh environment capability |
| **Protection** | IP67 | Dust and water resistant |
| **Control** | CAN 2.0B | Industry-standard communication |

## System Architecture

The ADB-PC-AC01 is designed as part of the modular ADB Series system, allowing for flexible configuration and scaling for MW-level power systems.

{{ figure('../assets/ac01_system_architecture.webp', 'System Architecture') }}

### Key Architectural Features:

- **Stackable Design**: Modules can be combined for higher power applications
- **Common DC Bus**: Shared DC link for distributed DC-coupled systems
- **Integrated Gateway**: Enables firmware updates and cybersecurity features
- **Intelligent Droop Technology**: Automatic load sharing in parallel configurations

### Application example: MCS (Megawatt Charging System)

The modular design of ADVANTICS's ADB power modules series allows creating creating megawatt level systems using 1 MW building blocks in 100kW steps.  
**These 1MW building block can be duplicated as much as needed to reach the targeted power level.**  
In our example here, the MCS charger is built using:  

- 1MW AC/DC PFC Building block based on the ADB-PC-AC01 power module.  
- 1MW DC/DC isolated Building block based on the ADB-PC-DC01 power module.  

{{ figure('../assets/ac01_dc01_mcs_example.webp', 'MCS Example') }}

## Compliance and Standards

The ADB-PC-AC01 is designed to meet major international standards:

### Safety Standards
- IEC 61851-1 (Electric vehicle conductive charging system)
- IEC 61851-23 ED2 (DC electric vehicle charging station)
- IEC 62477-1 (Safety requirements for power electronic converter systems)
- UL 2202 (Electric vehicle charging system equipment)
- UL 1741 (Inverters, converters, controllers and interconnection system equipment)

### Grid Codes
- EN50549-1 (Requirements for generating plants to be connected in parallel with distribution networks)
- IEEE 1547 (Standard for interconnecting distributed resources with electric power systems)
- VDE-AR-N 4100 (Technical connection conditions for connecting customers' installations)
- UK G99 (Requirements for the connection of generation equipment in parallel with public distribution networks)
- AS 4777.2 (Grid connection of energy systems via inverters)

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

The ADB-PC-AC01 is designed with environmental considerations:

- High efficiency reduces energy consumption and carbon footprint
- Liquid cooling eliminates fan noise and reduces maintenance
- Sealed design prevents environmental contamination
- Long design life reduces electronic waste
- Recyclable materials used in construction