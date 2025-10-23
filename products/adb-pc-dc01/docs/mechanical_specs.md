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

### DC Connector Features

!!! info "SurLock Plus Benefits"
    - **Positive Locking**: Prevents accidental disconnection
    - **High Current Capacity**: RADSOK technology for low contact resistance
    - **Environmental Sealing**: IP67 rating when mated
    - **Touch Safe**: Finger-safe design per UL standards
    - **Keying**: Polarized to prevent incorrect connection

### DC Connectors (Port A)

The ADB-PC-DC01 features high-current DC connectors for the input side (Port A), designed for reliable operation with various DC sources:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | High-current contact technology |
| **Manufacturer** | Amphenol | Industry-leading reliability |
| **Series** | SurLock Plus (SLP-HIR-B) | Locking mechanism for safety |
| **Quantity** | 2x Port A | Positive and negative connections |
| **Current Rating** | ±120 A | Bidirectional operation |
| **Voltage Rating** | 1000 V | Suitable for 950V DC operation |


### DC Connectors (Port B )

The DC output side (Port B) features robust bidirectional connectors for the high-voltage DC link:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 10.3mm | Larger size for higher current/voltage |
| **Manufacturer** | Amphenol | SurLock Plus series |
| **Series** | SLP-HIR-C | High-current locking design |
| **Quantity** | 2x Port B | Positive and negative connections |
| **Current Rating** | ±220 A | Bidirectional operation |
| **Voltage Rating** | 1500 V | Suitable for 1500V DC operation |

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

All connectors are designed to resist:
- Industrial chemicals and solvents
- UV radiation exposure
- Ozone and atmospheric contaminants
- Hydraulic fluids and lubricants

## Liquid Cooling

The ADB-PC-XXXX are watercooled power converters.

Each box has 4 ports - two for top plate, two for bottom plate.

The recommended flow of water would look like this. Color indicates the temperature rise, arrows indicate flow direction

![image.png](assets/liquid_cooling_images/image.png)

The render is illustrative - all four fittings are forward facing, but in reality would be oriented differently.

### Flow and temperature rise

The cooling medium is 50/50 water-glycol mix. Probably can be lighter on glycol. This depends on expected environmental conditions.

Glycol also acts as a corrosion protection agent - perhaps we should also consider some drops against bacterial growth. There is some risk of galvanic corrosion. Heatsinks are aluminium, fittings are nickel plated brass. Radiator is probably aluminium. Glycol should ‘save’ us.

Required flow is around 5 liters per minute. (5 l/min). This, together with expected 2kW of heat generation per box, would result in 6.3 degC temperature rise (inlet to outlet). Bigger delta we allow, the smaller the radiator can be.

The reason why the water flows through top plate first and then the bottom, is an attempt to equalize the thermal difference between heatsinks. Heat rises, so the top one should (theoretically) be exposed to higher heat load than the bottom one. 

Another thing to consider is the maximum flow rate. Since these packaged converters are to be used in a parallel loop (cold water pushing into all the boxes at the same time through a manifold), there has to be enough water pressure to spread equally between all converters. If the flow is not restrictive enough per heatsink (or water inlets), we risk that there won’t be enough pressure to feed all units equally.

This goes with pump design - 100 boxes would require 5l/min * 100 = 500 l/min. Already quite a challenging volume of liquid. 

### Port adapter

Each port is coming out of a CNC machined adapter piece - currently the adapter has 3/8” threads, to be used with G3/8 fittings. The adapter has three holes - front, side, top. **The next iteration will use G1/4 thread instead.**

![image.png](assets/liquid_cooling_images/image%201.png)

Michal is suggesting to remove one of the three ports on the adapter. Only keep the forward and upward ones, not the side one. As there boxes go into racks, these holes don’t make that much sense.

### Connector selection

G 1/4” fittings are very common. It’s the go-to standard for PC watercooling, as well as other liquid cooled industries.

![63306_1BGhUnb3cLXA2i_400x400..webp](assets/liquid_cooling_images/63306_1BGhUnb3cLXA2i_400x400..webp)

![1011181_1WajNPTUnGMcWw_400x400..webp](assets/liquid_cooling_images/1011181_1WajNPTUnGMcWw_400x400..webp)

Fitting features an o-ring, which when compressed, provides the seal. Fitting like this provides barbed hose connection, for 3/8” hose (inner diameter of hose 10mm). Unused ports can be capped with plugs.

There also exists G1/4 fittings that attach to the hose using screw-in sleeve, and then bolts directly into the watercooling plate. Both straight and 90deg (including rotating) fittings are available.

![1011165_10umTEVfU9Gzr1_400x400..webp](assets/liquid_cooling_images/1011165_10umTEVfU9Gzr1_400x400..webp)

![1022525_01_400x400..webp](assets/liquid_cooling_images/1022525_01_400x400..webp)

These straight fittings could be perfect for top-bottom heatsink interconnect hose. Alternatively, simply using barbed hose connection with a clamp is also perfectly fine.

Some sample materials for prototyping were ordered at [alphacool.com](http://alphacool.com/)

### No-drop alternatives

For more demanding customers, we could offer CPC EVERIS LQ4 quick disconnect couplings, with no drip disconnect under pressure. These are a lot more expensive, so definitely not something we should offer as default or for free.

![image.png](assets/liquid_cooling_images/image%202.png)

### Cooling channel design optimizations

As the flow rate changed significantly from the initial concept (we were expecting 10-20 l/min), it’s worth reviewing the original flow path and heatsink design.

![image.png](assets/liquid_cooling_images/image%203.png)

The prototype channel might have a few areas of potential improvements:

- Mix of wide and short liquid paths - with only 5l/min, is this still the correct strategy?
- Given the direction of the flow (shown at the top of this page), is the path split functional?
- The heat is concentrated in bars (hard to cool, as screws go through the center of them) and inductors/transformers (easy to cool, no screws above them). How’s the heat moving from the bar?
- Would a longer coolant path perform better? Or a more shallow one?
- Weight concern. The current heatsinks are very heavy. Can we mill them more aggressively? Perhaps also from the ‘inside’ side (module mounting side).
- Channel can’t be direction-sensitive, as what’s an inlet of the top one, becomes the outlet of the bottom one.
- Can we remove some screw holes? At least on the AFE, there are the front screws for the plastic spacers that we don’t use anymore.

![image.png](assets/liquid_cooling_images/262f09a9-54b3-4729-ba6b-ff7a3fba4a54.png)