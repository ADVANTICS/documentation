# Mechanical Specifications

## Dimentions

| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Dimensions (L × W × H)** | 700 × 440 × 165 | mm |
| **Weight** | 30 | kg |
| **Mounting** | 4U rack or custom brackets | - |
| **Cooling** | Liquid cooled | - |
| **Ingress Protection** | IP67 | - |

## Connectors

### AC Input Connectors

The ADB-PC-AC01 features high-current AC connectors designed for reliable operation in industrial environments:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | High-current contact technology |
| **Manufacturer** | Amphenol | Industry-leading reliability |
| **Series** | SurLock Plus (SLP-HIR-B) | Locking mechanism for safety |
| **Quantity** | 3 connectors | One per phase (L1, L2, L3) |
| **Current Rating** | 150 A<sub>rms</sub> per phase | Continuous operation |
| **Voltage Rating** | 1000 V | Suitable for 480V systems |

### AC Connector Features

!!! info "SurLock Plus Benefits"
    - **Positive Locking**: Prevents accidental disconnection
    - **High Current Capacity**: RADSOK technology for low contact resistance
    - **Environmental Sealing**: IP67 rating when mated
    - **Touch Safe**: Finger-safe design per UL standards
    - **Keying**: Polarized to prevent incorrect connection


### DC Output Connectors

The DC side features bidirectional connectors for the high-voltage DC link:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | Same technology as AC side |
| **Manufacturer** | Amphenol | SurLock Plus series |
| **Series** | SLP-HIR-B | High-current locking design |
| **Quantity** | 2x Port A | Positive and negative connections |
| **Current Rating** | ±170 A | Bidirectional operation |
| **Voltage Rating** | 1000 V | Suitable for 950V DC operation |

### DC Connector Features

!!! info "SurLock Plus Benefits"
    - **Positive Locking**: Prevents accidental disconnection
    - **High Current Capacity**: RADSOK technology for low contact resistance
    - **Environmental Sealing**: IP67 rating when mated
    - **Touch Safe**: Finger-safe design per UL standards
    - **Keying**: Polarized to prevent incorrect connection

### Control and Communication Connectors

#### CAN Bus & Interlock line Connectors

The module includes redundant CAN bus & interlock line connections:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | M12-P5A | Locking connector |
| **Quantity** | 2 | Redundant connections |
| **Isolation** | Isolated interface | Safety isolation |

**Pinout**

<!-- TODO -->

#### 24V Connector

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Function** | 24V Power | Module control supply |
| **Connector Type** | M12-P2T | Locking connector |
| **Voltage Range** | 20-28 V DC | Nominal 24V |
| **Current Draw** | Up to 12A | Peak during startup |
| **Isolation** | Isolated interface | Safety isolation |

**Pinout**

<!-- TODO -->

### Connector Environmental Ratings

#### Environmental Protection

| **Connector Type** | **IP Rating** | **Operating Temperature** | **Corrosion Resistance** |
|-------------------|---------------|-------------------------|------------------------|
| **DC Connectors (Port A)** | IP67 (mated) | -40°C to +125°C | Salt spray resistant |
| **DC Connectors (Port B)** | IP67 (mated) | -40°C to +125°C | Salt spray resistant |
| **Control and power Connectors** | IP65 (mated) | -40°C to +105°C | Industrial grade |

#### Chemical Resistance

All connectors and enclosures are designed to resist:

- Liquids, including salts (coastal areas)
- Industrial chemicals and solvents
- UV radiation exposure
- Ozone and atmospheric contaminants
- Hydraulic fluids and lubricants

## Liquid Cooling

The ADB-PC-XXXX are watercooled power converters.

Each unit has 4 ports - two for top plate, two for bottom plate. To simplify the integration, the units come with the left-side top+bottom ports interconnected from the factory.

The recommended flow of water would look like this. Color indicates the temperature rise, arrows indicate flow direction

{{ figure('../assets/ADB-PC-XXXX_liquid_flow.png', 'Liquid flow') }}

### Heat dissipation

Thermal dissipation of each unit depends on operational conditions - voltage, current, power level. Typical head load can be calculated by multiplying the processed power by the efficiency figure at that operation point.

A typical loss would be: 100 kW * 0.98 = 2 kW
When sizing for the worst case scenario, calculate with 97% efficiency. 100 kW * 0.97 = 3 kW

The system has a very high inertia, thanks to the aluminium heatsink and the liquid loop. That means it can take a long time (20 minutes in some cases) before you see a significant heat buildup.
This can be used to improve noise profile - the heat exchanger (radiator) doesn't need to run at all times. However, **never switch off the coolant flow (pump) during operation.** You don't need to run the pump system if there is no power flowing.

!!! tip

    It is ok to run power converters on a testbench without any cooling at all, for prototyping or (supervised) testing scenarios.
    However monitor the temperatures and don't push the system to it's limits if no cooling is present.


### Flow and temperature rise

The cooling medium is a water-glycol mix. The ratio depends on the environmental conditions (freeze prevention).

Glycol lowers the freezing temperature and acts as a corrosion protection agent, in case of mixed-metal cooling loops. Additional additives could include organic growth inhibitors.

Required flow rate is 5 liters per minute (5 l/min). The flow can be increased, to extend full power operation region in hot climates. Do not exceed 15 l/min.

!!! Example

    With 2kW of heat generation per box, would result in 6.5 &deg;C temperature rise (inlet to outlet).

    Calculating for worst-case scenario, 3 kW, the heat rise would be 9.7 &deg;C (both at 5 l/min).

Since the units are designed to be used in a parallel loop (cold water pushing into all the boxes at the same time through a manifold), there has to be enough water pressure to spread equally between all converters. If the flow is not restrictive enough per heatsink (or water inlets), we risk that there won’t be enough pressure to feed all units equally (especially considering the vertical stacking in a rack).

This goes with pump design - 100 units would require 5 l/min * 100 = 500 l/min. Already quite a challenging flow rate.

### Port adapter

Each port (inlet and outlet) uses G1/4 thread (British Standard Pipe). Unless specified separately by the customer, each unit comes with barbed fittings installed on all ports.
These barbed fittings accept a hose with 3/8" (10 mm) internal tube wall.

<!-- ![image.png](assets/barbed_fitting.png) -->

{{ figure('../assets/barbed_fitting.png', 'Barbed fitting') }}


### No-drip alternatives

There are a number of no-drip fittings that can be installed instead of the straight barbed fitting.
However, given that the hose connects to the manifold (distributor), it makes more sense to place the no-drip fittings there (so the disconnection happens on the manifold side, not on the unit side).