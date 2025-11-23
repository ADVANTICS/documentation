# Connectors

Each power converter comes with a unique front panel, with some identical elements, and some function-specific elements.
Common elements include:

- 24V input power connector (M12 industrial connector)
- 2x CAN bus communication connector (M12 industrial connector)

The specific elements include power connectors for AC or DC ports. As different converters require different current and power levels,
a combination of different connectors is often selected. This helps to limit a chance of incorrect installation through the use of colour, size and keying features.

## AC Connectors

The ADB-PC-AC01 features high-current Amphenol Surlok Plus connectors designed for reliable operation in industrial and automotive environments:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | High-current contact technology |
| **Manufacturer** | Amphenol | Industry-leading reliability |
| **Series** | SurLock Plus (SLP-HIR-B) | Locking mechanism for safety |
| **Quantity** | 3 connectors | One per phase (L1, L2, L3) |
| **Colour and Keyway** | Orange | 20&deg; |
| **Connector Current Rating** | 200 A | Continuous operation |
| **Connector Voltage Rating** | 1500 VDC | |

## DC Connectors

The DC side features bidirectional connectors for the high-voltage DC link:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | Same technology as AC side |
| **Manufacturer** | Amphenol | SurLok Plus series |
| **Series** | SLP-HIR-B | High-current locking design |
| **Quantity** | 2x Port A | Positive and negative connections |
 **Colour and Keyway** | Red, Black | 20&deg; (Red), 30&deg; (Black) |
| **Connector Current Rating** | 200 A | Continuous operation |
| **Connector Voltage Rating** | 1500 VDC | |

## Selection of connector part numbers

Depending on the current and insulation material rating (PVC vs XLPE for example),
cross section of the cable has to be selected. For higher quality insulation materials (eg. not 70 &deg;C PVC), a lower cross section can be selected.

That means for L1, L2, L3 and also DC+ and DC-, a 35 mm2 cross section is suitable.
Here's a table showing the individual connector part numbers, taking into consideration the connector keying, colour as well as cross section:

| **Connector label** | **Cable cross section** | **Part number** | **Notes** |
|---------------------|-------------------------|-----------------|-----------|
| **L1** | 35 mm2 | SLPHPB35BSO1 | Orange, 20&deg;, IP rated |
| **L2** | 35 mm2 | SLPHPB35BSO1 | Orange, 20&deg;, IP rated |
| **L3** | 35 mm2 | SLPHPB35BSO1 | Orange, 20&deg;, IP rated |
| **DC+** | 35 mm2 | SLPHPB35BSR1 | Red, 20&deg;, IP rated |
| **DC-** | 35 mm2 | SLPHPB35BSB2 | Black, 30&deg;, IP rated |

This table can be modified for a larger cross section, following the same keying, pin diameter and color coding.
Please refer to Amphenol brochure for more details: [Amphenol](https://www.amphenol-industrial.de/en/products/xev-connectors/surlok)

## Control and Communication Connectors

### CAN Bus & Interlock line Connectors

The module includes redundant CAN bus & interlock line connections:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | M12-P5A | Locking connector |
| **Quantity** | 2 | Redundant connections |
| **Isolation** | Isolated interface | Safety isolation |

{{ figure('../assets/control_connector.png', 'CAN Bus & Interlock line Connectors') }}

**Pinout**

| Name              | Pin | Description                                                                 |
|-------------------|-----|-----------------------------------------------------------------------------|
| Interlock         | 1   | Interlock input/output                                                      |
| CAN_GND           | 2   | Ground                                                                      |
| CAN_L             | 3   | CAN bus low (differential)                                                  |
| CAN_H             | 4   | CAN bus high (differential)                                                 |
| CAN Termination   | 5   | Connect to CAN_H to provide the 120 Ω CAN bus termination when required |


!!! warning "CAN Bus Termination"
    - Enable termination only at the physical ends of the CAN bus (two terminations in total).
    - Do not fit termination on intermediate nodes; multiple terminations cause bus impedance mismatch and communication errors.
    - If using the optional termination pin (Pin 5), connect it to CAN_H only on end nodes; leave it unconnected on intermediate modules.


### 24V Connector

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Function** | 24V Power | Module control supply |
| **Connector Type** | M12-P2T | Locking connector |
| **Voltage Range** | 20-28 V DC | Nominal 24V |
| **Current Draw** | Up to 12A | Peak during startup |
| **Isolation** | Isolated interface | Safety isolation |

{{ figure('../assets/power_connector.png', '24V Connector') }}

**Pinout**

| Name   | Pin |
|--------|-----|
| 24V_DC (+) | 1 |
| 0V / GND   | 2 |