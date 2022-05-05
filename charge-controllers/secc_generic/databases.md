> [!UPDATE] {docsify-updated}
# CAN databases

## Why we need CAN databases
CAN communications define essentially a physical layer and a partial MAC layer. Since in the context of the applications discussed here the physical layer is fully standardized we do not have to worry about that particular asppect and we can simply abstract that away.<br>
When it comes to the MAC layer, you should mainly remember the following:
* Each CAN fram is identified by a unique ID, which has a length of 11  bits, or 29 bits if you are using extended IDs.
* Each CAN frame has a payload of up to 64 bits (8 bytes).
The specifications for the MAC-layer stop right there, unless you are not using a dedicated MAC-level protocol such as CAN IsoTP, which is not the case here. That means that the content and structure of the 64 bits payload is completely user-defined, hence, specific to each application.
To allow two arbitrary systems to communicate properly, we have to define the structure of a payload. This is usually done by defining the so-called CAN databases. Different formats exist, as you will read in the following sections, but there are mainly syntaxic variations to define the same concepts:
* The database define a bunch of frame IDs and should (hopefully) provide some kind of documentation on what the frame ID is associated to.
* The 64 bits payload can be splitted in multiple **signals**. A signal is defined by a length and a position (offset) in the payload. For example, the payload could contain 8 1-byte signals, each containing different types of data. Similarly to frames, signals be named and documented in the database.
* For scalar values, signal payloads can optionally be scaled. *Scaling* simply means that you are applying a linear function to translate the value from the payload into its real value. This is basically important because without scaling  Basically the scaling will determine the resolution of the real value being transmitted.
* For non-scalar values, enumerations can also be defined, which are basically an exhaustive lsit of specific values that are associated to a certain meaning; e.g., if you want to transmit whether a device is ready or not, you might associate 1 to READY and 0 to NOT_READY.
* Optionally, signals can be *multiplexed*, which means that the signal contained at a certain offset of a fram might not be the same everytime. In that case a multiplex index will indicate which of the multiplexed signal is actually present in the current frame. This is typically useful to to aggregate multiple multiple data that do not need to be sent everytime in the same signal. For example, if you have a frame sent twice a second and need to transmit the voltage and current measured once a second, you can alternate between the two signal rather than having them both at the same time.
* ...and a bunch of other features that you can discover in the documentation of the database format reported below.

If you are using ADVANTICS power modules, the CAN databases defining the communication protocol for the backend are already on-board of the controllers so you do not have to do anything specific regarding CAN configuration. If you are using other power modules, you do need to configure them to use ADVANTICS Generic Interface. We provide the `.kcd` and `.dbc` file for the generic interface; you can also find their exported documentation in this chapter.

### CAN databases format used by ADVANTICS
We use two main types of CAN database formats in our projects, Kayak and DBC.

## Kayak format

Kayak is an [open format](https://github.com/julietkilo/kcd) based on XML, and is rather human
readable (more than DBCs...). This is the main format for us. That is, we author the CAN DBs in this
format, and our software and firmware use it directly.

- [Advantics Generic EVSE protocol v2.2](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v2.2.kcd ':ignore')
- [Advantics Generic EVSE protocol v2](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v2.kcd ':ignore')
- [Advantics Generic EVSE protocol v1](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v1.kcd ':ignore')

## DBC format

As a courtesy we also provide our CAN DBs in the more usual DBC format. Note these are automatically
converted from the Kayak ones. Therefore, they are not the reference DBs.

- [Advantics Generic EVSE protocol v2.2](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v2.2.dbc ':ignore')
- [Advantics Generic EVSE protocol v2](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v2.dbc ':ignore')
- [Advantics Generic EVSE protocol v1](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v1.dbc ':ignore')

### ADVANTICS Databases documentation
This document contain an automated export of ADVANTICS CAN databases that you can find [here](charge-controllers/secc_generic/can.md).