> [!UPDATE] {docsify-updated}
# Overview

## General operation

One way to look at the Advantics controllers is to consider them as mere translators between the
communication protocol a vehicle uses and a protocol power modules of the charger uses.
It abstracts away the various types of charge communication standards (eg. CHAdeMO, CCS DIN, CCS
ISO, etc.) as well as their versions.

But it has to also abstract away the complexity of correctly sequencing power modules. Hence,
the generic EVSE CAN interface is a middle ground between two abstraction layers.

```plantuml
left to right direction
skinparam sequenceArrowThickness 2
title Overall context for the generic EVSE CAN interface

node "PEV" {
    [Battery] -d- [BMS]
    [BMS] -d- [EVCC]
    () "Charge port" as Charge_port
    [EVCC] -d- Charge_port
}

node "EVSE" {
    () "Combo plug" as CCS_plug
    () "CHAdeMO plug" as CHAdeMO_plug
    () "Generic CAN\ninterface" as CAN_if
    () "Power bus" as Power

    CHAdeMO_plug -[hidden]l- CCS_plug

    package "Advantics Controller SECC" {
        [CCS DIN/ISO] as CCS_frontend
        [CHAdeMO] as CHAdeMO_frontend
        [Controller] as Controller

        CHAdeMO_frontend -[hidden]l- CCS_frontend

        CCS_plug -d- CCS_frontend
        CHAdeMO_plug -d- CHAdeMO_frontend
        CHAdeMO_frontend -- Controller
        CCS_frontend -r- Controller
        Controller -l- CAN_if
    }

    package "Customer Controller" {
        [DC/DC converter] as DCDC
        [HMI] as HMI
        [Backend] as Backend
        CAN_if -u- DCDC
        CAN_if -u- HMI
        CAN_if -u- Backend
    }

    CHAdeMO_plug -l- CCS_plug
    CCS_plug -l- Power
    Power -d- DCDC
}

Charge_port <|-d- CHAdeMO_plug
Charge_port <|-d- CCS_plug
```

The process of charging a battery is fundamentally driven by what the battery can take at
any given moment. In electric vehicle charging it translates to the BMS requesting voltage and
current setpoints to power electronics capable of deliverying power levels in the order of ten's
to hundreds of kilo Watts.

Communication protocols like CCS and CHAdeMO are here to forward these requests between two
independent entities, a vehicle and a charger, addressing all the challenging aspects it can have
(interoperability, reliability, etc.). They carry other side tasks such as sharing the voltage,
current and power limits of both sides, charge scheduling, authorisation by external payment,
plug'n'charge, etc.

> [!ATTENTION]
> It should always be considered that in this process, the vehicle is a master giving its
> requests to the charger. Actually, CCS took this even further by considering the vehicle is always
> the one initiating every step of the process, much beyond what the main charging loop requires.

The generic EVSE CAN interface reflects this almost one-to-one. Controllers will be requesting
specifc modes and setpoints at the right moments, and the power modules should reports regularly
their status and readouts of voltage and current. But behind, it is the vehicle who is requesting
these. In some ways, you might also consider it is the communication protocol itself which
constrains some aspects of the charging process (eg. isolation tests and precharge steps).

Some steps in the process are long-lasting. Communication protocols adopted different ways for
making these steps cyclic. They generally take the form of loops where the vehicle requests
something, the requests is forwarded to the power modules. Then the readouts of the power modules
are forwarded to the vehicle, and the vehicle decide to continue the loop or not.

In such cyclic steps, with CCS, requests messages are coming regularly to the charger. But the
interval time is up-to the vehicle, and can be as long as 60 seconds. In CHAdeMO, not all steps are
following this cyclic requests model. But controllers will emulate it (possibly following CHAdeMO
CAN frames periodicity of 100 ms).

> [!NOTE]
> Unlike with other typical CAN communications, cyclicity of requests here is not meant to run
> as control loops. The vehicle should have its own, safe, control loop for what the battery can take
> (usually in the BMS directly). The charger should have its own, safe, control loops for the various
> power modes. The cyclicity of these requests is mostly for slowly moving the setpoints, and for
> relatively long time outs in case of problem (unexpected disconnection, failure of some modules,
> power trip on the grid, noise, etc.).

Controllers are hiding all details of the charge process that are not relevant to power modules
(eg. scheduling, authentication, etc.). It will also try its best to capture every possible failure
in the communication with the vehicle in order to properly shut off any active power function
running at that time.

## Workflow of a charge

```plantuml
skinparam sequenceArrowThickness 2
title Typical workflow of a charge

start

:Plug-in;

if (Protocol is) then (CHAdeMO)
    :User push start button;
else (CCS)
endif

partition "Connection negotiation" {
    :Initialisation of communication;

    :Authentication and/or payment;
    note left: Not with all\nprotocols or\nchargers


    :Exchange of charge parameters;
}

partition "Charge preparation" {
    :Plug/Socket locks;
    note left: In some protocols\nit might happen earlier

    :Insulation test;
    note left: Checks charging cable\nis not defective and\npotentially dangerous

    if (Protocol is) then (CCS)
        :Precharge;
        note left: Matches charger output\nvoltage with battery voltage
    else (CHAdeMO)
        note right: CHAdeMO requires an\noutput diode on the\ncharger to avoid arcing\nin vehicle contactors
    endif

    :Contactors close;
}

partition "Charging" {
    while (Any stop conditions?) is (No)
        :Current request;
    endwhile (Yes)
}

partition "Charge closure" {
    :Wait for current lowering;

    :Vehicle does contactors welding detection;
    note left: Can be optional,\nthe vehicle decides

    :Contactors open;

    :Wait for voltage lowering;

    :Plug/Socket unlocks;
}

:Unplug;

stop
```
