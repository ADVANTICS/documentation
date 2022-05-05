> [!UPDATE] {docsify-updated}
# ADM-CS-SECC hardware manual

> [!FCC]
> This device is considered a sub-assembly, and in accordance with CFR47 part 15.103 is exempted from
> FCC technical standards. The user must follow the installation instructions provided by the manufacturer,
> and the operator of the device shall be required to stop operating the device upon finding that the
> device is causing harmful interference. The integrator is the responsible of the FCC testing of the final product.

1. [Introduction](#introduction)
1. [Interfaces](charge-controllers/ADM-CS-SECC/interfaces.md)
1. [Charge station overview](charge-controllers/ADM-CS-SECC/evse_overview.md)
1. [Examples of use](charge-controllers/ADM-CS-SECC/examples.md)

# Introduction

## Summary

The ADM-CS-SECC is a charge controller for electric vehicle charging stations. The main features include:
- Linux system, running on iMX7 ARM platform
- CCS (Combined Charging System) – DIN SPEC 70121 and ISO 15118
- CHAdeMO interface (1.x)
- AC charging interface (IEC 61851-1, J1772)
- Ethernet (RJ45)
- Extension slot with 4G modem, GPS, Wi-Fi (optional)
- RS-485 (user managed)
- Relays for output contactor control
- CAN bus (for power modules control)
- OCPP interface
- SD card

## Who is this product for?

Manufacturers of stationary and portable charging stations, integrators, research laboratories, new EV applications like rescue vehicles, charging emulation during vehicle development.

## Electrical and mechanical specifications

Please see the specs sheet for ADM-CS-SECC for details.

## Software development guide

Please see the Software Development Guide document for ADM-CS-SECC for details.

## Typical use case

Each EV charging station design is different – requiring a different set of interfaces or equipment. To gain some understanding about the minimum requirements, you can study the following documents:
- Standard IEC 61851-1, Electric vehicle conductive charging system – Part 1: General requirements
- Standard IEC 61851-21-2, Electric vehicle requirements for conductive connection to an AC/DC supply
- CharIN association – [CCS implementation guide](https://www.charinev.org/ccs-at-a-glance/ccs-implementation-guideline/)

<div class="bigger-1000">

![Functionality overview](images/functionalities.jpg "Functionality overview")
</div>
<figcaption style="text-align: center">Figure 1: Functionality overview</figcaption>
