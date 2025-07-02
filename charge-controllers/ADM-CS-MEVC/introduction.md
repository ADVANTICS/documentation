> [!UPDATE] {docsify-updated}
# Introduction

## Characteristics

The ADM-CS-MEVC is an EV charge controller for onboard vehicle charging. The main features include:
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
|                             | **Temperature measurements**                     | 2 PT1000 inputs, and 1 dedicated CAN bus          |
|                             | **Inlet locking**                                | Inlet lock motor control                          |
| **Automotive Housing specifications**| **Operating Temperature**               | -40°C to +125°C                                   |
|                             | **Sealing**                                      | IP69K                                             |
|                             | **Shock**                                        | 50 g’s – 20 pulses                                |
|                             | **Dimensions**                                   | 11.43 x 11.68 cm                                  |
|                             | **RoHS Compliant**                               | Yes                                               |

## Accessing the controller

Please see the [Accessing and interacting with the controller](charge-controllers/advantics_os/connecting.md) section for details.

## Pinout Table
The reference of the pin is composed of 3 characters:

- The first character is the row number on the connector
- The second character is a letter indicating the column 
- The third character indicates the connector: "1" is the small connector (on the left in figure 2 above) and 2 indicates the big one (the one on the right)

| Name | ![connector 1](images/PEV_connector1.png "connector 1") | ![connector 2](images/PEV_connector2.png "connector 2") |
|------|----|--------|
| [SWITCHED_POWER](#Power_input) | <center> - | <center> 2C2 |
| [PERMANENT_POWER](#Power_input) | <center> - | <center> 3C2 |
| [POWER_GND](#Power_input) | <center> - | <center> 1D2 |
| [TRXP (MCS PHY1)](#MCS_Interface) | <center> - | <center> 1A2 |
| [TRXN (MCS PHY2)](#MCS_Interface) | <center> - | <center> 2A2 |
| [MCS_GND](#MCS_Interface) | <center> - | <center> 3A2 |
| [CE (MCS)](#MCS_Interface) | <center> - | <center> 1H2 |
| [ID (MCS)](#MCS_Interface) | <center> - | <center> 2H2 |
| [MCS_LOCK_POWER](#MCS_Interface) | <center> - | <center> 3B2 |
| [MCS_LOCK+](#MCS_Interface) | <center> - | <center> 1B2 |
| [MCS_LOCK-](#MCS_Interface) | <center> - | <center> 2B2 |
| [MCS_LOCK_FB](#MCS_Interface) | <center> 3E1 | <center> - |
| [PTC0](#Temperature_monitoring) | <center>  2D1 | <center> - |
| [PTC1](#Temperature_monitoring) | <center>  1E1 | <center> - |
| [PTC_GND](#Temperature_monitoring) | <center>  3D1 | <center> - |
| [PTC_GND](#Temperature_monitoring) | <center>  2E1 | <center> - |
| [PTC_GND](#Temperature_monitoring) | <center>  1F1 | <center> - |
| [MCS Auxiliary Voltage](#MCS_Interface) | <center> - | <center> 3G2 |
| [MCS_CE_Sv4_ext](#MCS_Interface) | <center> - | <center> 3H2 |
| [GND](#MCS_Interface) | <center> - | <center> 1J2 |
| [CAN_H_TEMP_SENSOR](#MCS_Interface) | <center>  1B1 | <center> - |
| [CAN_L_TEMP_SENSOR](#MCS_Interface) | <center>  2B1 | <center> - |
| [CAN_TEMP_SENSOR_GND](#MCS_Interface) | <center>  3B1 | <center> - |
| [CONTACTOR_POWER](#DC_fast_charge_contactors_control) | <center> - | <center> 2D2 |
| [CONT_DC+_POS](#DC_fast_charge_contactors_control) | <center> - | <center> 3D2 |
| [CONT_DC+_NEG](#DC_fast_charge_contactors_control) | <center> - | <center> 1E2 |
| [CONT_DC+_FB](#DC_fast_charge_contactors_control) | <center> - | <center> 2E2 |
| [CONT_DC-_POS](#DC_fast_charge_contactors_control) | <center> - | <center> 3E2 |
| [CONT_DC-_NEG](#DC_fast_charge_contactors_control) | <center> - | <center> 1F2 |
| [CONT_DC-_FB](#DC_fast_charge_contactors_control) | <center> - | <center> 2F2 |
| [CHARGE_STOP](#Vehicle_CAN_bus) | <center> - | <center> 3F2 |
| [CAN_H_CONTROL](#Vehicle_CAN_bus) | <center>  1A1 | <center> - |
| [CAN_L_CONTROL](#Vehicle_CAN_bus) | <center>  2A1 | <center> - |
| [CAN_CONTROL_GND](#Vehicle_CAN_bus) | <center>  3A1 | <center> - |
| [UNUSED_GND](#Vehicle_CAN_bus) | <center> - | <center> 1C2 |
| [ETHERNET_RJ45](#Ethernet) | <center>  ETH | <center> ETH |
| [DIGITAL_IN1](#Digital_inputs_and_outputs) | <center> - | <center> 1G2 |
| [DIGITAL_IN2](#Digital_inputs_and_outputs) | <center> - | <center> 2G2 |
| [DIGITAL_OUT1](#Digital_inputs_and_outputs) | <center> - | <center> 1K2 |
| [DIGITAL_OUT2](#Digital_inputs_and_outputs) | <center> - | <center> 2K2 |
| [DIGITAL_OUT3](#Digital_inputs_and_outputs) | <center> - | <center> 3K2 |
| [DIGITAL_GND](#Digital_inputs_and_outputs) | <center> - | <center> 3J2 |

## Typical use case

- [MCS capable vehicles](https://advantics.fr/industries/megawatt-charging/)
- [EV  simulation, development and testing](https://advantics.fr/applications/emobility/eol-tester-ev-fast-charger/)
- [Bidirectional charging](https://advantics.fr/applications/emobility/bidirectional-charging/)

<div class="bigger-1000">

![Functionality overview](images/mevc_functionalities_overview.png "Functionality overview")
</div>
<figcaption style="text-align: center">Figure 1: Functionality overview</figcaption>

## Mechanical housing

The automotive housing is based on the CINCH ModICE platform. In particular the SE variant. The front-facing connectors mate with [CINCH P/N:581 01 18 023](https://www.cinch.com/products/enclosures/connectors/5810118023) (18-way) and [581 01 30 029](https://www.cinch.com/products/enclosures/connectors/5810130029) (30-way). The terminals for different wire gauge are 425 00 00 872 and 425 00 00 873. Consult the [ModICE brochure](https://www.cinch.com/products/enclosures/enclosures/5810130043) for the details.
