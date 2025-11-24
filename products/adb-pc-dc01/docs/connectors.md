# Connectors

Each power converter comes with a unique front panel, with some identical elements, and some function-specific elements.
Common elements include:

- 24V input power connector (M12 industrial connector)
- 2x CAN bus communication connector (M12 industrial connector)

The specific elements include power connectors for AC or DC ports. As different converters require different current and power levels,
a combination of different connectors is often selected. This helps to limit a chance of incorrect installation through the use of colour, size and keying features.

### DC Connectors (Port A)

The ADB-PC-DC01 features high-current Amphenol Surlok Plus connectors designed for reliable operation in industrial and automotive environments:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 8mm | High-current contact technology |
| **Manufacturer** | Amphenol | Industry-leading reliability |
| **Series** | SurLock Plus (SLP-HIR-B) | Locking mechanism for safety |
| **Quantity** | 2 | Positive and negative connections |
| **Connector Current Rating** | 200 A | Continuous operation |
| **Connector Voltage Rating** | 1500 VDC | |

### DC Connectors (Port B)

The DC wide control side (Port B) features robust bidirectional connectors for the high voltage DC:

| **Specification** | **Value** | **Notes** |
|-------------------|-----------|-----------|
| **Connector Type** | RADSOK Size 10.3mm | Larger size for higher current |
| **Manufacturer** | Amphenol | SurLock Plus series |
| **Series** | SLP-HIR-C | High-current locking design |
| **Quantity** | 2 | Positive and negative connections |
| **Connector Current Rating** | 350 A | Continuous operation |
| **Connector Voltage Rating** | 1500 VDC | |

## Selection of connector part numbers

Depending on the current and insulation material rating (PVC vs XLPE for example),
cross section of the cable has to be selected. For higher quality insulation materials (eg. not 70 &deg;C PVC), a lower cross section can be selected.

That means for Port A DC+ and DC-, a 35 mm2 cross section is suitable.
The Port B DC+ and DC- requires higher cross section - 70 mm2. There is no risk of incorrectly wiring polarity, because of the keying and colour encoding, and since Port A and Port B have different connector diameter, they cannot be swapped either.

Here's a table showing the individual connector part numbers, taking into consideration the connector keying, colour as well as cross section:

| **Connector label** | **Cable cross section** | **Part number** | **Notes** |
|---------------------|-------------------------|-----------------|-----------|
| **Port A DC+** | 35 mm2 | SLPHPB35BSR1 | Red, 20&deg;, IP rated |
| **Port A DC-** | 35 mm2 | SLPHPB35BSB2 | Black, 30&deg;, IP rated |
| **Port B DC+** | 70 mm2 | SLPHPC70BSR1 | Red, 20&deg;, IP rated |
| **Port B DC-** | 70 mm2 | SLPHPC70BSB2 | Black, 30&deg;, IP rated |

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
    - Enable termination only at the physical ends of the CAN bus.
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
| 0V / GND   | 3 |


