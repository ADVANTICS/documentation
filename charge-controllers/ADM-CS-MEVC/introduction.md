> [!UPDATE] {docsify-updated}
# Introduction

## Characteristics

The ADM-CS-EVCC is an EV charge controller for onboard vehicle charging. The main features include:
- Linux system, running on iMX7 ARM platform
- MCS charging IEC 61851-23-3 and ISO 15118-20
- Bidirectional Power Transfer (BPT) Capable
- Plug and Charge (PnC) coming soon
- Automatic deep sleep and wake-up for energy saving
- No code integration with supported BMS
- Compatible with different BMS
- MCS inlet monitoring
- Ethernet (RJ45)
- Drivers for DC fast charging contactors
- CAN bus (for integration into the vehicle)
- Port inlet motor driver
- SD card slot
- Automotive Housing

## Who is this product for?

Manufacturers of electric vehicles (personal, agricultural, buses, trucks), vehicle integrators,
research laboratories, DIY EV enthusiasts looking to integrate MCS charging in their projects,
new EV applications like rescue vehicles, and charge emulation for development purposes.


## Electrical and Mechanical specifications
|       |                                            |                         |
|-----------------------------|-------------------------------------------------|----------------------------------------------------|
| **Charging Standards**      | **MCS**                                          | ISO 15118-20, IEC 61851-23-3                      |
| **Power input**             | **Input voltage**                                | 12 V or 24 V                                      |
|                             | **Input Voltage Range**                          | 11 V to 32 V                                      |
|                             | **Nominal power consumption without peripherals**| 2 W                                               |
| **Interfaces (user side)**  | **CAN bus**                                      | 2x ISO-11898 CAN bus, configurable bitrate (500kbps default)|
|                             | **Digital Outputs**                              | 3 outputs, 24V, push-pull, max. 100 mA (sink or source)|
|                             | **Digital Inputs**                               | 2 inputs, 24V and 12V compatible, Max voltage 30V |
|                             | **LEDs**                                         | 3 LED outputs, 12V, overcurrent protected         |
|                             | **Ethernet**                                     | 100Mbps RJ45.                                     |
|                             | **SD memory card**                               | 16 GB card standard                               |
|                             | **SIM slot**                                     | Micro SIM, user supplied                          |
| **Output Contactor Control**| **Contactors Outputs**                           | 2 Independent outputs                             |
|                             | **Max Current**                                  | Drive up to 5A                                    |
|                             | **Contactors Feedback Inputs**                   | 2 Contactor Feedback inputs                       |
| **MCS interface**           | **Communication wires**                          | PHY1/PHY2 (10BaseT1S), CE (Charge Enable), ID (Insertion Detection)          |
|                             | **Temperature measurements**                     | 3 PT1000 inputs, and 1 dedicated CAN bus          |
|                             | **Inlet locking**                                | Inlet lock motor control                          |
| **Automotive Housing specifications**| **Operating Temperature**               | -40°C to +125°C                                   |
|                             | **Sealing**                                      | IP69K                                             |
|                             | **Shock**                                        | 50 g’s – 20 pulses                                |
|                             | **Dimensions**                                   | 11.43 x 11.68 cm                                  |
|                             | **RoHS Compliant**                               | Yes                                               |

## Software development guide

Please see the Software [Development Guide document](charge-controllers/sys3_user/README.md) for details.

## Typical use case

- [MCS capable vehicles](https://advantics.fr/industries/megawatt-charging/)
- [EV  simulation, development and testing](https://advantics.fr/applications/emobility/eol-tester-ev-fast-charger/)
- [Bidirectional charging](https://advantics.fr/applications/emobility/bidirectional-charging/)

<div class="bigger-1000">

![Functionality overview](images/mevc_functionalities_overview.png "Functionality overview")
</div>
<figcaption style="text-align: center">Figure 1: Functionality overview</figcaption>

## Mechanical housing

The automotive housing is based on the CINCH ModICE platform. In particular the SE variant. The front-facing connectors mate with CINCH P/N:581 01 18 023 (18-way) and 581 01 30 029 (30-way). The terminals for different wire gauge are 425 00 00 872 and 425 00 00 873. Consult the [ModICE brochure](https://www.belfuse.com/product/part-details?partn=5810130043) for the details.
