# Mechanical Specifications

## Dimentions

{{ figure('../assets/ADB-PC-AC01_3D.png', 'ADB-PC-AC01 3D model') }}

| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Dimensions (L × W × H)** | 720 × 440 × 175 | mm |
| **Weight** | 40 | kg |
| **Mounting** | 4U rack or custom brackets | - |
| **Cooling** | Liquid cooled | - |
| **Ingress Protection** | IP67 | - |

## Liquid Cooling

The ADB-PC-XXXX are watercooled power converters.

Each unit has 4 ports - two for top plate, two for bottom plate. To simplify the integration, the units come with the left-side top+bottom ports interconnected from the factory.

The recommended flow of water would look like this. Color indicates the temperature rise, arrows indicate flow direction

{{ figure('../assets/ADB-PC-XXXX_liquid_flow.png', 'Liquid flow') }}

### Heat dissipation

Thermal dissipation of each unit depends on operational conditions - voltage, current, power level. Typical head load can be calculated by multiplying the processed power by the efficiency figure at that operation point.

A typical loss would be: 100 kW * 0.98 = 2 kW
For the exact loss for a specific setpoint, please consult the efficiency map.
2kW of heat generation per converter would result in 6.5 &deg;C temperature rise (inlet to outlet, 5 l/min).

The system has a very high inertia, thanks to the aluminium heatsink and the liquid loop. That means it can take a long time (>10 minutes in some cases) before you see a significant heat buildup.
This can be used to improve noise profile - the heat exchanger (radiator) doesn't need to have its fan run at all times. However, **never switch off the coolant flow (pump) during operation.** You don't need to run the pump system if there is no power flowing.

!!! tip
    It is ok to run power converters on a test bench without any cooling at all, for prototyping or (supervised) testing scenarios.
    However monitor the temperatures and don't push the system to very high power if no cooling fluid is present.


### Flow and temperature rise

The cooling medium is a water-glycol mix. The ratio depends on the environmental conditions (freeze prevention).
Glycol mixture lowers the freezing temperature and acts as a corrosion protection agent, in case of mixed-metal cooling loops. Additional additives could include organic growth inhibitors.

!!! warning
    It is important to use the correct coolant formulation. The heatsinks are made out of aluminium, distribution manifolds tends to be made out of stainless steel, 
    fittings tends to be made out of nickel-plated brass, pipes in the heat exchangers tends to be made ouf of copper.
    To limit the galvanic corrosion and organic growth in the coolant loop, use only glycol-based coolant fluids formulated for mixed metal loops containing aluminium, with organic growth inhibitors.
    Do not use tap water or distilled water in the loop. Consult a coolant manufacturer before commissioning.
    
    Failure to follow this can result in clogged pumps, limited cooling performance, and in the worst case, damaged fittings and leaks.

Required flow rate is 5 liters per minute (5 l/min). The flow can be increased, to extend full power operation region in hot climates. Do not exceed 15 l/min.

Since the units are designed to be used in a parallel loop (cold water pushing into all the boxes at the same time through a manifold), there has to be enough water pressure to spread equally between all converters. If the flow is not restrictive enough per heatsink (or water inlets), there is a risk there won’t be enough pressure to feed all units equally (especially considering the vertical stacking in a rack).
One way to test how well the fluid is distributed is to (temporarily) install flow indicators on every high pressure port on the first rack you build.

### Port adapter

Each port (inlet and outlet) uses G1/4" thread (British Standard Pipe). Unless specified separately by the customer, each unit comes with barbed fittings installed on all ports.
These barbed fittings accept a hose with 3/8" (10 mm) internal tube wall.

<!-- ![image.png](assets/barbed_fitting.png) -->

{{ figure('../assets/barbed_fitting.png', 'Barbed fitting') }}

The bottom-to-top cooling plate interconnect is handled by a pre-installed hose on the left side.

### No-drip alternatives

There are a number of no-drip fittings that can be installed instead of the straight barbed fitting.
However, given that the hose connects to the manifold (distributor), it makes more sense to place the no-drip fittings there (so the disconnection happens on the manifold side, not on the converter side).