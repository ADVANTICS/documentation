> [!UPDATE] {docsify-updated}
# Introduction

## Summary

The ADM-CS-EVCC is an EV charge controller for onboard vehicle charging. The main features include:
- Linux system, running on iMX7 ARM platform
- CCS (Combined Charging System) – DIN SPEC 70121 and ISO 15118
- AC charging interface (IEC 61851-1, J1772)
- CCS inlet monitoring
- Ethernet (RJ45)
- Drivers for DC fast charging contactors
- CAN bus (for integration into the vehicle)
- Port inlet motor driver
- SD card slot

## Who is this product for?

Manufacturers of electric vehicles (personal, agricultural, buses, trucks), vehicle integrators,
research laboratories, DIY EV enthusiasts looking to integrate CCS charging in their projects,
new EV applications like rescue vehicles, and charge emulation for development purposes.

## Electrical and mechanical specifications

Please see the Specification Sheet for ADM-CS-EVCC for details.

## Software development guide

Please see the software development guide document for ADM-CS-EVCC for details.

## Typical use case

Every electric vehicle project is different – requiring different subset of interfaces or equipment. To gain some understanding about minimal requirements, the following documents can be studied:
- Standard IEC 61851-1, Electric vehicle conductive charging system – Part 1: General requirements
- Standard IEC 61851-21-2, Electric vehicle requirements for conductive connection to an AC/DC supply
- CharIN association – [CCS implementation guide](https://www.charinev.org/ccs-at-a-glance/ccs-implementation-guideline/)

![Functionality overview](images/functionalities.jpg "Functionality overview")
<figcaption style="text-align: center">Figure 1: Functionality overview</figcaption>

## Mechanical housing

The automotive housing is based on the CINCH ModICE platform. In particular the SE variant. The front-facing connectors mate with CINCH P/N:581 01 18 023 (18-way) and 581 01 30 029 (30-way). The terminals for different wire gauge are 425 00 00 872 and 425 00 00 873. Consult the [ModICE brochure](https://www.belfuse.com/product-detail/modice-modice-le-enclosures) for the details.
