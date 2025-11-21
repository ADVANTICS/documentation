# Connectors

## DC Connectors

!!! info "Features"
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
| 0V / GND   | 2 |


