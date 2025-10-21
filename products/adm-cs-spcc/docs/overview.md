# ADM-CS-SPCC Overview

## Product Overview

The ADM-CS-SPCC (Single Pistol Charge Controller) is a versatile SECC designed for a wide range of electric vehicle charging applications. It supports multiple charging protocols including MCS, CCS (bidirectional), NACS, CHAdeMO (bidirectional), and AC, making it suitable for fast charging stations, Megawatt systems, wallboxes, and rugged installations.

### Applications
- Fast charging stations (DC and AC)
- Megawatt Charging Systems (MCS)
- Compact bidirectional DC wallboxes
- Rugged outdoor charging stations and specialized vehicle applications (e.g., battery-powered gensets, rescue vehicles)

### Key Benefits
- Broad protocol support for future-proof charging solutions
- Compact and flexible mounting options (DIN rail, LCD back, heavy-duty enclosure)
- Advanced communication interfaces (CAN, Ethernet, RS-485, wireless)
- Robust design for harsh conditions
- Native support for modular power integration to accelerate development

## Key Features

| Feature | Details |
|---------|---------|
| Charging Standards | MCS (10BASE-T1S); CCS (DIN SPEC 70121, ISO 15118-2/-20, NACS); CHAdeMO (1.x with V2G); AC (SAE J1772, IEC 61851) |
| Bidirectional Power Transfer (BPT) | V2G capable |
| OCPP Support | 1.6J (2.0.1 coming soon) |
| Plug & Charge | Yes |
| Power Input | 15V–30V (nominal 24V); Typical 5W / Peak 20W |
| Interfaces | CAN 2.0B; Ethernet 100Mbps; RS-485 (Modbus); Wireless (Wi‑Fi 4, Bluetooth 5.2); USB‑C; HDMI (via external conversion from MIPI DSI) |
| User-configurable I/O | 4 digital inputs; 2 digital outputs; 3 LED outputs; 4 × PT1000 temperature sensors |
| Safety | Interlock (current loop); safety circuit opens contactors on fault |
| Mounting | DIN rail; LCD back; Heavy-duty enclosure |
| Environmental | Operating: -40°C to 85°C |

## Technical Specifications

### Charging Standards

| Standard | Support |
|----------|---------|
| MCS | ISO 15118-20, IEC 61851-23-3 |
| CCS | DIN SPEC 70121, ISO 15118-2/-20, NACS SAE J3400, SAE J1772, IEC 61851-1/-23 |
| CHAdeMO | 1.x with V2G extension |
| AC | SAE J1772, IEC 61851-1/-23 |

### Electrical Specifications

| Parameter | Value |
|-----------|-------|
| Input Voltage Range | 15V - 30V |
| Recommended Nominal Voltage | 24V |
| Typical Consumption | 5W |
| Peak Consumption | 20W |
| Temperature Range | -40°C to 85°C |
| Interlock | 20mA current loop, 24V |
| Output Contactor Driver | Contactor enable signal provided, open collector, max 200 mA, max 30V |
| AC cable Locking mechanism | Standard AC inlet locking interface |
| CHAdeMO Inlet Locking mechanism | Solenoid driver |

### Mechanical Specifications

| Parameter | Value |
|-----------|-------|
| Dimensions | 212 x 90 x 58 mm |
| Weight | 350g |
| Connections | pluggable terminal block connectors |
| Mounting Options | DIN rail, LCD back, Heavy duty enclosure |

### Interface Specifications

| Interface | Details |
|-----------|---------|
| 10baseT1S | for MCS (Megawatt Charging System) communication |
| PLC | Power Line Communication for CCS |
| CAN Bus | CAN 2.0B, extended addresses |
| Ethernet | 100Mbps RJ45, Modbus TCP available |
| RS-485 | Modbus-RTU stack available, 5V max 2A |
| Wireless | Dual-Band 2.4/5 GHz Wi-Fi 4 (802.11n), Bluetooth 5.2 |
| USB-C | USB 3.1 Gen 1 |
| Display Serial | IPI DSI + I²C for TP |
| HDMI | Via external conversion from MIPI DSI |
| Configurable Digital Outputs | 2 x 24V push-pull, max 1A (sink/source), Hi-Z |
| Configurable Digital Inputs | 4 x (24V/12V compatible, max 30V) |
| LEDs | 3 x 12V, overcurrent protected |
| Temperature Measurements | 4 x PT1000 inputs |


## Pinout

![Pinout](images/SPCC_pinout3.png "Pinout")

## SPCC Connectors

| Connector | Reference Number |
|-----------|------------------|
| CON 104 | Phoenix Contact 1786882 |
| CON 101 | Phoenix Contact 1786866 |
| CON 102 | Phoenix Contact 1786853 |
| CON 103 | Phoenix Contact 1786895 |
| CON 105 | Phoenix Contact 1786879 |
| CON 106 | Phoenix Contact 1786837 |
| CON 107 | Phoenix Contact 1757475 |

## Typical Use Cases

- [Megawatt charging system](https://advantics.fr/applications/ev-charging/mw-charging-system/)
- [EV DC and AC charging stations](https://advantics.fr/applications/ev-charging/charge-station-controller/)
- [High power EV charging](https://advantics.fr/applications/ev-charging/high-power-ev-charging/)
- [V2G Wallboxes](https://advantics.fr/applications/ev-charging/v2g-wallboxes/)
- [Bi-directional charging](https://advantics.fr/applications/ev-charging/bidirectional-charging/)

For more details on integration and standards, refer to the relevant IEC and SAE specifications.
