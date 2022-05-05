# Advantics charge controllers

Welcome to the charge controller documentation !If you are taking your first steps into the EV industry, you should have a look to the [overview](#what_are_charge_controllers_for) section below as well as the linked resources in [additional documentation](#additional_documentation). There are a lot of acronyms in EV charging, so a quick look at the [terminology](#a_first_introduction_to_ev_terminology) might be helpful to follow along. You can navigate in the sections below to discover them. <br>
* [Products](#products)
* [What are charge controllers for ?](#what-are-charge-controllers-for-)
* [A first introduction to EV Terminology](#a-first-introduction-to-ev-terminology)
* [Additional resources](#additional-resources)

If you feel confident in your knowledge of this type of products, you can move to the next chapters.<br>
If you have already received your charge controller, the [Quick Start](#quick_start) chapter will help you getting your brand new charge controller running. 
If you are facing issues that the technical manual does not address while developing on your charge controller, please check [Common Issues](#common_issues). There are recurrent mistakes that can happen when developing a charging system, and there are good chances that you issue is already covered there. 


## Products
ADVANTICS charge controllers are a family of products that are designed to meet the needs of the electric vehicle industry:
* [ADM-CS-SECC](#adm_cs_secc): Charge Controller for Supply Equipments
* [ADM-CS-EVCC](#adm_cs_evcc): Charge Controller for Plug-in Electric Vehicles
* [ADM-CS-CUI](#adm_cs_cui): Universal Charge Controller for R&D applications on both Electric Vehicles and Supply Equipment
![Pictures of controllers](images/controllers_images.svg)

### Main features
All our controllers provide the following major features:
* **CCS** (CharIN)  (Combined Charging System) * DIN SPEC 70121 and ISO 15118* and **ChadeMo** support* 
* Linux system on iMx7 ARM platform, open for custom user applications
* AC charging interface (IEC 61851-1, J1772)
* Ethernet (RJ45) access
* Extension slot with 4G modem, GPS, Wi-Fi (optional)
* RS-485 (user managed)
* CAN bus to both backend and frontend (*see diagram below*)
* Open Charge Point Protocol (OCPP) interface
* SD card

For charging stations, our main product is **ADM-CS-SECC**. It comes in a DIN rail housing and
supports three pistols (CCS DC, CCS AC and CHAdeMO). It has a charger-side CAN bus and RJ485 interface,
relays for output contactors, some general purpose industrial IOs, an ethernet port as well as a
mPCIe slot for cellular or wifi modules.<br>
For vehicles, our main product is **ADM-CS-EVCC**. It comes in an automotive housing and supports
one CCS AC and/or DC inlet. It has a vehicle-side CAN bus, contactors drivers and inlet lock driver.
It also has an ethernet port but it is not exposed outside of the housing and is mainly used for
setup, update or retrieving logs from it.<br>
For pure R&D applications or more compact designs, **ADM-CS-CUI1** is the ideal solution. It does not come with industrial housing and has a more limited set of input/outputs compared to the products above, but it is universal, which means it can be used for both Electric Vehicle and Charging Station Side.

## What are charge controllers for ?

Advantics charge controllers act as communication bridges between protocols used for charging
(CCS, CHAdeMO) and components of chargers or vehicles (power modules, BMS, contactors, sensors, etc.). If you are not familiar with the existing charging protocols, the section below givshould give an overview of the main components of a charging system.

### Basic principles of EV charging
First, there are obviously two parties in a charging session:
* The charger, also called Supply Equipment (SE)
* The vehicle, also called *(Plug-in)* Electric Vehicle (EV / *P*EV).

Charging requires more than simply blindly transmitting power through a cable. There are indeed multiple parameters that the two parties have to manage:
* The **safety** of the process. Considering the significant power delivered by the process, it is crucial to prevent customers and operators from being event when facing errors or hardware damages.
* The **physical parameters** of the transaction: this includes for example the voltage at which the charger and battery operate, the current that they can deliver or handle.
* The **high-level aspects** of the transaction, such as vehicle identification, automatic payment, etc.<br><br>

![Block diagram of a typical EV charging system](images/block_diagram.svg)<br>

In the diagram above, starting from the charger side (*left*) the power modules are in charge of delivering the horse power for the charging process. They can be controlled over CAN; this is the first task handled by the charge controller, which is also defined as the charger *backend* in this documentation. The charge controller needs indeed to communicate the voltage and current requested (among other things) to the pwoer modules; to do that, it has to communicate with the other party, which is known as the *frontend*. The nature of the communication depends on the charging protocol used:
* For CCS, the **pistol** connecting the charger to the vehicle has a Control Pilot (CP) line, which actually carries two communications channel:
    * A PWM-based channel, also known as the *Low-Frequency Communications* (LFC) channel: it is mainly intended to communicate the current state of the charging process and can only take 5 different values (from A to E), defined by the PWM duty cycle.
    * A Power Line Communications (PLC) channel on top of the LFC, also known as the High-Frequency Communications (HFC) channel: it has a much higher data rate it is mainly intended to communicate transaction parameters and high-level data during the charging process.
* For Chademo, the pistol hosts a CAN bus that is used to by the two parties to communicate over a standardized interface.
If we now look at the vehicle side, the *frontend* has a similar role, which is to handle the communications from the vehicle backend to the charger. The vehicle *backend* designate the part that is in contact with the *Battery Management System* (BMS), typically handled over CAN, which transmits the physical parameter requested by the battery during the charging process.

### Overview of AVANTICS Charge Controllers
Although their primary goal is to act as communication bridges between the respective backends of the charger and the vehicle, ADVANTICS charge controllers are more than that. Instead of simply providing a more digestible version of
CCS messages or CHAdeMO frames, the **ADM-CS-\*** family of charge controllers translate them into forms and sequences that are
closer to how main components of a charger or vehicle operates.<br>
Hardware-wise, each controllers integrate the necessary components for charger-vehicle communications
(PLC modem, CAN transceivers). As well as all output drivers, and analog and digital inputs sensing
to cover the most typical use cases of charging applications (eg. contactors or relays drivers,
pistol temperature sensors, CCS CP PWM generation and sensing, PP sensing, CHAdeMO SEQ1/SEQ2/PERM/PROX
IOs, pistol lock drivers and feedback).

## A first introduction to EV Terminology
Here is a brief introduction on the most common acronyms that you may encounter in EV-related content. The list below is mainly intended to help you in your first walkthrough and is by no means exhaustive; you can find a more exhaustive terminology [here](#terminology).
* **Back-end**: In the context of EV charging, *backend* refers to the part of a system that is independant from the nature of the protocol between the Electric vehicle and the charging (i.e., the part that is *behind* the frton-end, which is defined below). For a supply equipment, *backend* refers the power modules; for an electric vehicle, to the battery management system.
* **BMS**: Battery Management System; Lithium-ion batteries require specific regulation of the charging process to (1), guarantee their safety, and (2), maximize their longevity. The BMS is **not** included in the Electric Vehicle Charge Controller, however, the charge controller is interacting with the on-board BMS when charging.
* **EV**: Electric Vehicle
* **EVCC** Electric Vehicles Charge Controller. This refers directly to the product discussed in this section: the charge controller is responsible for handling the communications with the supply equipment and interfacing with the Battery Management System (BMS).
* **Front-end**: In the context of the interaction between a Supply Equipment and an Electric Vehicle,*front-end* refers the part of the system that interacts with (i.e., that is *facing*) the other party. In other words, the front-end englobes all the communications and protocols between the EV and the supply equipment.
* **PEV**: Plug-in Electric Vehicle. Electric vehicles that are not *plugged-in** are typically hybrid vehicles in which the battery is solely charged by the internal combustion engine. Since these vehicles are by their nature out of the scope of this document, you can consider *EV* and *PEV* as interchangable in this documentation.
* **SE**: Supply Equipment, a broad term to designate charging stations.
* **SECC**: Supply Equipment Charge Controller; it manages the communications with the Electric Vehicles and controls the power modules. 

## Additional Resources
Here are a few useful links if you are getting started in the field of EV charging:
* [CharIn official website](https://www.charin.global/)
* [Chademo Official website](https://www.chademo.com/)
* [Design Guide for Combined Charging System](https://tesla.o.auroraobjects.eu/Design_Guide_Combined_Charging_System_V3_1_1.pdf)
* [Chademo Brochure](https://www.chademo.com/wp2016/wp-content/uploads/2018/06/CHAdeMO_Brochure_spring18.pdf)-