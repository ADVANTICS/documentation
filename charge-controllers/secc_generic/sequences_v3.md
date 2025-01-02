> [!UPDATE] {docsify-updated}

# Sequences of actions (EVSE Generic Interface v3)

> [!NOTE]
> The EVSE Generic interface version 3 supports all the charging standards, both unidirectional and bidirectional (DIN SPEC 70121 and ISO 15118-2/-20 (CCS and MCS), NACS and CHAdeMO).

Before describing the CAN communication, let's take a detailed look at the sequences of actions,
and what each actor in the charge process does.

See the [Power transfer sequence diagram](charge-controllers/secc_generic/power_transfer_sequence_diagram.md) for the full sequence. Extracts of it will be
given here.

## Controller starts-up

When powering up the controller, the operating system starts-up, then a few application processes
start. The main controller process is the first one to start, and will immediately start emitting
the [Advantics_Controller_Status](charge-controllers/secc_generic/can_v3.md#Advantics_Controller_Status) message every
100 ms.

At the beginning it reports a state of *Initialising* until all internal processes started-up and
are talking to each other.

Afterwards, if the controller is configured to use the sequence flags, it will report a state of
*Not_Available*. This state is meant for pre-start external charge authorisation. Once your
controller/HMI has validated the user, it sends
a [Sequence_Control](charge-controllers/secc_generic/can_v3.md#Sequence_Controls) message with signal
[Start_Charge_Authorisation](charge-controllers/secc_generic/can_v3.md#Sequence_Control-Start_Charge_Authorisation) set
to `Allowed` (value 1).

Afterwards, or if the controller is configured to not use the sequence flags, it reports a state of
*Waiting_For_PEV*.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Initialisation ==
|||

-> EVSE: [User] Power on
note over EVSE
  System boot-up
  ~15 seconds
end note

EVSE->Charger: [0x6B000] Advantics_Controller_Status.State == Initialising

|||
== Wait for start authorisation ==
|||

EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Not_Available
...
Charger -> EVSE: [0x63002] Sequence_Control.Start_Charge_Authorisation == Allowed

|||
== Wait for vehicle ==
|||

EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Waiting_For_PEV

|||
```

## Charge initialisation

Once a vehicle plugs-in, a so-called charge session is initialised. It allows for exchange of
important parameters between the vehicle and the charger. Such as voltage, current and power limits.

The content of this initialisation behaves differently from communication protocols. In CHAdeMO it is
rather quick, but requires the user to push a start button on the charger. In CCS it can be a few
tens of seconds, especially if payment authorisation is carried on.

[Advantics_Controller_Status](charge-controllers/secc_generic/can_v3.md#Advantics_Controller_Status) message reports a
state of *Negotiating_Connection* at first.
Once done with the negotiation, it reports *Connected_With_Full_Info*.

However, in CCS, if the charger is configured to use external authorisation, and configured to use
the sequence flags, you will have an intermediate state *CCS_Authorisation_Process*.
The controller, and the CCS communication itself, will stay in this state as long as the customer
controller does not set the
flag [CCS_Authorisation_Done](charge-controllers/secc_generic/can_v3.md#Sequence_Control-CCS_Authorisation_Done) to
`Done` (value 1).
Once `Done` is set, the controller
checks [CCS_Authorisation_Valid](charge-controllers/secc_generic/can_v3.md#Sequence_Control-CCS_Authorisation_Valid)
flag. If set
to `Valid` (value 1), the communication continue. If set to `Invalid` (value 0), the controller
request a stop of communication to the vehicle (and it won't allow the vehicle to "force-through"
the sequence). If not using CCS external authorisation and sequence flags, the controller just
consider user is always authorised and continues directly.

When *Connected_With_Full_Info*, it also sends
a [New_Charge_Session](charge-controllers/secc_generic/can_v3.md#New_Charge_Sessions) message alongside the other
messages carrying
relevant information provided by the vehicle. If the controller is configured to use the sequence
flags, it will wait
that [Charge_Parameters_Done](charge-controllers/secc_generic/can_v3.md#Sequence_Control-Charge_Parameters_Done) is set
to `Done` (value 1) to
continue to the next step (insulation test). Before that, as long as it is `Not_Done` (value 0), the
customer controller can modify the content of
the [DC_Power_Parameters](charge-controllers/secc_generic/can_v3.md#DC_Power_Parameters) message. If not using the
sequence flags then it continues directly with either the static limit values set in the config file,
or whatever has been sent in [DC_Power_Parameters](charge-controllers/secc_generic/can_v3.md#DC_Power_Parameters) before
that.

> [!TIP]
> This allows the customer controller to adapt the advertised max current and voltage in relation
> to the vehicle capabilities. For instance, this is useful for chargers using an internal battery as
> power source.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Charge initialisation ==
|||

PEV -> EVSE: [User] Plug-in
-> EVSE: [User, CHAdeMO only] Start button
activate PEV
activate EVSE
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Negotiating_Connection
|||
loop Exchange of information
  |||
  PEV -> EVSE
  |||
  EVSE --> PEV
  |||
end loop
|||

|||
== [only for CCS & MCS] External authorisation ==
|||

PEV -> EVSE: [only for CCS & MCS] Authorised?
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == CCS_Authorisation_Process
activate Charger
...
Charger -> EVSE: [0x63002] Sequence_Control.CCS_Authorisation_Valid == Valid
Charger -> EVSE: [0x63002] Sequence_Control.CCS_Authorisation_Done == Done
EVSE --> PEV: [only for CCS & MCS] User is valid
deactivate Charger

|||
== Connected with full info ==
|||

EVSE -> Charger: [0x6B001] New_Charge_Session
activate Charger
EVSE -> Charger: [0x6B100] EV_Information_Battery
EVSE -> Charger: [0x6B101] EV_Information_Voltages
EVSE -> Charger: [0x6B102] EV_Information_Charge_Limits
EVSE -> Charger: [0x6B103] EV_Information_Discharge_Limits
Charger -> EVSE: [0x63001] DC_Power_Parameters
Charger -> EVSE: [0x63002] Sequence_Control.Charge_Parameters_Done == Done
...
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Connected_With_Full_Info
deactivate Charger
EVSE --> PEV: Charge parameters
deactivate PEV
deactivate EVSE
|||
```

### Insulation test

Insulation test is a step meant to verify the charging cable is not damaged in a way it could be a
safety hazard for the user. It consists in the charger applying a test voltage (normally, the
maximum and riskier voltage that the charger would be applying across a whole charge, typically
500 V). It then measures the output current and deduce the insulation resistance.

The insulation resistance should be of at least 100 kΩ for CCS according to IEC 61851-23:2023, and at least 125 kΩ according to IEC 61851-23-3 for MCS.

At first, the lock of the plug or inlet should be activated by now. Then the vehicle gives its
permit to the charger to apply power. At this point, the Advantics controller has a mechanism to
allow power modules to wake up and be ready for power before doing the actual insulation test.
[New_Charge_Session](charge-controllers/secc_generic/can_v3.md#New_Charge_Sessions) will be sent periodically as long as
customer controller is not sending a
message [Power_Modules_Status](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status)
with [System_Enable](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status-System_Enable) different from
*Allowed* (value 1).

> [!ATTENTION]
> This [System_Enable](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status-System_Enable) flag will be used
> even when the controller is
> configured to NOT use the sequence flags.

> [!TIP]
> This allows power modules to be in sleep mode, only waking up on
> incoming [New_Charge_Session](charge-controllers/secc_generic/can_v3.md#New_Charge_Session) messages, and gives it
> some time to initialise. Internally, the controller manages to make the vehicle wait for cable insulation test while
> power modules wake up and
> set [System_Enable](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status-System_Enable) to *Allowed*.
> Therefore, you still have a limited time to wake-up as communication protocols may have long timeouts on these
> states (in the order of a few tens of seconds).

> [!NOTE]
> Please note that once the power modules signal that they are ready, the controller emits one
> [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control)
> message with [Target_Voltage](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Target_Voltage) == 0 V,
> [Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) == 0 A,
> [Current_Range_Min](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Min) == 0 A,
> [Power_Function](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Power_Function) == `Standby`.
> This signifies a request for a "Standby", it will be used for this purpose across the charging session.
> When emitted, it's expected from the power electronics to be ready for any future request while not processing any
> power.

Once ready for power, the controller will
emit [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control)
with insulation target voltage
as [Target_Voltage](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Target_Voltage)
and [Power_Function](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Power_Function) == Insulation_Test.
Customer controller should be returning a meaningful value
in [Insulation_Resistance](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status-Insulation_Resistance)
of [Power_Modules_Status](charge-controllers/secc_generic/can_v3.md#Power_Modules_Status) message. The controller will
wait for the present voltage to be at least 90% of the requested test voltage. It then waits for the insulation resistance to be above the valid insulation resistance threshold (100 kΩ for CCS and 125 kΩ for MCS) for at least 10 iterations of the [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) message. This number of 10 is
an arbitrary choice from us, which we might change in the future if necessary.

In case this criterion is not met (i.e. there is an electrical defect somewhere), the insulation test fails and the session will be terminated. The malfunction is reported to the vehicle.

After successful insulation test and the sequence can proceed to the next stage, the controller will emit standby
messages ([DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control)
message with [Target_Voltage](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Target_Voltage) == 0 V,
[Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) == 0 A,
[Power_Function](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Power_Function) == Standby) as long as the
present voltage reported by power modules is above 20 V. It then reports to the vehicle the insulation test is finished and the
charging process can continue to the next step.

In case of CHAdeMO, the vehicle contactors are closed right after a successful insulation test.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Insulation test ==
|||

group CHAdeMO only
  |||
  EVSE -> EVSE: Lock connector
  |||
end group

group only for CCS & MCS
  |||
  PEV -> PEV: Lock connector
  |||
end group
|||

PEV -> EVSE: Start insulation test
activate PEV
activate EVSE

|||
== Not ready for power ==
|||

loop Waiting for Power_Modules_Status.System_Enable == Allowed
  |||
  EVSE -> Charger: [0x6B001] New_Charge_Session
  activate Charger
  |||
end loop
...
Charger -> EVSE: [0x63000] Power_Modules_Status.System_Enable == Allowed
deactivate Charger
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby)

|||
== Ready for power ==
|||

EVSE->Charger: [0x6B000] Advantics_Controller_Status.State == Insulation_Test
|||
loop Waiting for Power_Modules_Status.Insulation_Resistance >= 100 kΩ (125 kΩ for MCS) over 50 iterations
  |||
  PEV -> EVSE: [only for CCS & MCS] Insulation test continue
  EVSE -> Charger: [0x6B003] DC_Power_Control (XXX V, 0 A, Insulation_Test)
  activate Charger
  Charger -> EVSE: [0x63000] Power_Modules_Status.Insulation_Resistance == XXX
  EVSE --> PEV: [only for CCS & MCS] Insulation test ongoing
  |||
end loop
...
|||

loop Waiting for Power_Modules_Status.Present_Voltage <= 20 V
  |||
  PEV -> EVSE: [only for CCS & MCS] Insulation test continue
  EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby)
  Charger -> EVSE: [0x63000] Power_Modules_Status.Present_Voltage == XXX
  deactivate Charger
  EVSE --> PEV: [only for CCS & MCS] Insulation test ongoing
  |||
end loop
...
|||

EVSE --> PEV: Insulation test done
deactivate EVSE
deactivate PEV

|||
group CHAdeMO only
  |||
  PEV -> PEV: Close contactors
  |||
end group
|||
```

### Precharge (only for CCS & MCS)

When the vehicle closes its contactors, the battery voltage is applied up to the charger power
electronics output (or charger's own output contactors if it uses some) which could be at a
potential close to 0 V at this moment. This can create arcing in the contactors if some current is
allowed to flow, and severely deteriorate contactors.

To handle this situation, CHAdeMO chose to require chargers to have an output diode. While CCS
adopted the precharge process, which consists in having the charger match the battery voltage to
about 20 V prior to the vehicle closing its contactors.

With CCS and MCS, the controller will start
emitting [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control)
messages with [Target_Voltage](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Target_Voltage) == XXX V
(battery voltage), [Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) ==
0 A,
[Power_Function](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Power_Function) == "Precharge" when the
vehicle
tells it to. These messages contain the target voltage corresponding to the present battery voltage. It also gives a
maximum current limit to comply with (bear in mind some capacitors are still being charged in the process).

Once the vehicle decide the voltage is right (which it should do by its own measurements before closing its contactors),
it closes its contactors and continue with the charging sequence. While CCS and MCS does not explicitly tell when the vehicle is
ending the precharge process, the controller is using the fact that the vehicle starts sending requests other than
precharge to determine the end of precharge. At that point, the controller
emits [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) standby message
with [Target_Voltage](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Target_Voltage) == 0 V,
[Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) == 0 A
and [Power_Function](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Power_Function) == "Standby". However,
bear in mind that, as the
battery voltage is now applied up to the charger output, the voltage will not go down, and the power
electronics should not try to take the voltage to 0!

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Precharge [CCS & MCS Only] ==
|||

PEV -> EVSE: Start precharge
activate PEV
activate EVSE
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Precharge
|||
loop Waiting for abs(Plug voltage - Battery voltage) <= 20 V
  |||
  PEV -> EVSE: Precharge continue
  EVSE -> Charger: [0x6B003] DC_Power_Control (XXX V, X A, 0 A, Precharge)
  activate Charger
  EVSE --> PEV: Present voltage
  Charger -> EVSE: [0x63000] Power_Modules_Status.Present_Voltage == XXX
  |||
end loop
...
|||

PEV -> PEV: Close contactors
|||

PEV -> EVSE: Other request than precharge
deactivate PEV
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby)
deactivate Charger
deactivate EVSE
|||
```

### Start of charge

The start of charge state is here to signal the charge is *about* to start. This is to accommodate
for the *Power Delivery* request in CCS and MCS which requires the charger to be ready to charge, while the
actual charge might be starting in several hours. It happens if the user of the vehicle configured a
delayed charge or if there have been a negotiation of the charging schedule between the vehicle, the
charger and the electricity provider (only in complex scenario of ISO).

The [Charge_Status_Change](charge-controllers/secc_generic/can_v3.md#Charge_Status_Changes)
and [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) messages are sent only once.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Start of power transfer ==
|||

PEV -> EVSE: About to start charge
activate PEV
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Waiting_For_Charge
EVSE -> Charger: [0x6B002] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Started
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby)

|||
...
note over PEV, Charger
  Delayed charging: Potentially very long delay, up to several hours
end note
...
|||
```

## Power Transfer

This happens as soon as the vehicle and the charger enter the actual power transfer phase. The process is
very simple: the vehicle send its requests and limits to the controller, the controller
forwards them to the customer controller, which can then send voltage and current setpoint to the power modules depending on
 the [Setpoints_Mode](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Setpoints_Mode) and power transfer direction specified by the car or the charger (determining the power transfer direction is explained later in this document).

While the vehicle can use its own voltage and current measurements, it is also required that the
charger reports its own readings. Therefore, customer controller should update frequently the
readings in [Power_Modules_Status](charge-controllers/secc_generic/can_v3.md#Power_Modules_Statuss) message.

However, the communication protocols are very demanding in terms of charger performances during this
power transfer (CHAdeMO: 100 ms, ISO15118: 25 ms). In order to comply with these requirements (which
otherwise could trigger a premature end of charge), the controller is not waiting on the power
modules to get the most recent readings. It will use the last ones it has at this moment instead. As
the loops are short, it should not create much lag anyway.

> [!NOTE]
> A note about the periodicity at which
> the [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control)
> messages are emitted. In CHAdeMO they should be sent about every 100 ms. However, in CCS and MCS, the vehicle sets the pace,
> and the standards allows for periodicity of up to 60 s (afterwards it is considered a timeout and the charge stops).

About the behaviour of voltage and current changes, this is mostly unspecified (or specified too
differently across various communication standards). Therefore, you should expect for the worst:
sudden change in voltage and current without proper ramping (especially at charge start and end).
The protocols give enough slack for the power modules to implement their own ramping.

Also, the various control modes during a battery charging (constant current, constant power and
constant voltage) are not something of a concern to communication protocols. Power modules should be
able to determine it by themselves. In addition, vehicles have various ways of requesting the free
parameters. For instance, in constant current phase of charging, some vehicles might request a
voltage corresponding to either the present voltage of the battery, the present voltage plus a few
more volts, the real maximum voltage of the battery, or even a voltage much higher than the real
maximum voltage.

Some vehicle might decide to stop the charge early (for instance, when bulk charging is reached).
Some might decide to squeeze as much juice as possible until any of the limits is reached (max.
voltage, min. current or min. power).

### Power Transfer with Target Mode

> [!NOTE]
> Used for Unidirectional charging and some cases of Bidirectional power transfer.

This can be the normal EV charging process where the EV owner is only interested in charging the vehile or if the charger or the vehicle do not support bidirectional power transfer (ISO 15118-20 or CHAdeMO V2G).

This mode covers as well the scenario when the power transfer session is following a pre-negociated schedule where the charger and the vehicle agreed to charge and discharge at specific power rates on specific time frames during the session if supported by both parties. The target voltage and current are predefined and known in this case.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Target Mode & Unidirectional charging ==

|||
loop Waiting for any stop conditions
  |||
  PEV -> EVSE: Current request
  activate EVSE
  EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Charging
  EVSE -> Charger: [0x6B003] DC_Power_Control (XXX V, XX A, XX A, Power_Transfer, __**Target_Mode**__)
  activate Charger
  EVSE -> Charger: [0x6B100] EV_Information_Battery
  EVSE --> PEV: Present voltage and current
  Charger -> EVSE: [0x63000] Power_Modules_Status
  note over PEV,EVSE
    Not waiting for customer controller latest
    readouts in order to ensure timing constraints.
  end note
  |||
end loop
|||
```

In this case, the voltage and current setpoints are defined by the vehicle, they are then sent to the charge controller which forwards them to the customer controller (taking into account the charger and cable limits), which sends them to power modules. The power modules should follow and not deviate from these requests, otherwise the vehicle could stop the charge abruptly.

In this scenario, the controller sets [Setpoints_Mode](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Setpoints_Mode) to `Target_Mode` in the message [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) and provides the voltage and current setpoints. Both [Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) and [Current_Range_Min](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Min) signals will have the same value in `Target_Mode`

### Power Transfer with Range Mode

In this mode, the vehicle exposes its battery to the charger during the power transfer stage. The charger can then draw or push power within the limits negotiated with the vehicle (these limits can be dynamically updated).
This power transfer mode is used when the vehicle does not specify target power requests to the charger. Instead, the charger receives a target energy request that the vehicle aims to achieve by its departure time, along with charge/discharge current limits that must be respected throughout the session.

The charger in this scenario has the liberty to cycle between charging and discharging the vehicle's battery within the provided limits depending on the application, as long as the target energy request of the vehicle is reached by the departure time. The power transfer direction and the power setpoints are determined by a third-party system, such as a Central System Management System (CSMS) via OCPP or a local control system on the charger. This decision-making process considers factors like real-time electricity pricing and grid requirements.

In this scenario, the controller sets [Setpoints_Mode](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Setpoints_Mode) to Range_Mode in the message [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) and provides the voltage and current limits.

The OCPP CSMS can define the power transfer direction and the charge/discharge current to be used within the limits of the current range.
If this information is provided by the OCPP CSMS to the charge station, the generic interface forwards you this information over CAN bus via the signal [OCPP_Control](charge-controllers/secc_generic/can_v3.md#OCPP_Control-Dynamic_Target_Current) to be used as a current setpoint for the power modules.

> [!NOTE]
> A normal unidirectional power transfer process can be implemented in range mode by using the upper limit of the current range as a target current setpoint.

> [More information about bidirectionality on EVSE](charge-controllers/secc_generic/secc_bidirectional)  
> [More information about the Setpoints_Mode signal in DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Setpoints_Mode)

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Power Transfer with Range Mode ==

|||
loop Waiting for any stop conditions
  |||
  PEV -> EVSE: Current request
  activate EVSE
  EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Charging
  EVSE -> Charger: [0x6B003] DC_Power_Control (XXX V, XX A, X A, Power_Transfer, __**Range_Mode**__)
  activate Charger
  EVSE -> Charger: [0x6B100] EV_Information_Battery
  EVSE --> PEV: Present voltage and current
  group In case of OCPP central bidirectional charge control
    |||
    EVSE -> Charger: OCPP_Control.Dynamic_Target_Current == X A (or -X A) within range
    |||
  end group
  group In case of 3rd party/internal bidirectional charge control
    |||
    Charger -> Charger: Setting current to X A (or -X A) within range
    |||
  end group
  Charger -> EVSE: [0x63000] Power_Modules_Status
  note over PEV,EVSE
    Not waiting for customer controller latest
    readouts in order to ensure timing constraints.
  end note
  |||
end loop
|||
```

In this scenario, the controller sets [Setpoints_Mode](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Setpoints_Mode) to `Range_Mode` in the message [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) and provides the voltage and current limits in the signals [Current_Range_Max](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Max) and [Current_Range_Min](charge-controllers/secc_generic/can_v3.md#DC_Power_Control-Current_Range_Min).


## End of charge

This sequence comes at the end of a charge, when the charge has not been aborted irregularly. The
[Charge_Status_Change](charge-controllers/secc_generic/can_v3.md#Charge_Status_Change) message is sent only once.
Then three different [DC_Power_Control](charge-controllers/secc_generic/can_v3.md#DC_Power_Control) messages are
being sent: First to stop the power output from the charger, then open the contactors, then lower the charger side
output actively.

Before continuing the process, the vehicle will wait for the current flowing into its battery to
lower to reasonably safe values (5 A in CHAdeMO, and 1 A in CCS).

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== End of charge ==
|||

PEV -> EVSE: Stopping charge
deactivate PEV
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Ending_Charge
EVSE -> Charger: [0x6B002] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Stopped
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby, Contactors Close, No_Lowering)
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby, Contactors Open, No_Lowering)
EVSE -> Charger: [0x6B003] DC_Power_Control (0 V, 0 A, 0 A, Standby, Contactors Open, Lowering)
deactivate EVSE
deactivate Charger
|||
loop Waiting for current to lower
  |||
  PEV -> PEV
  note right: [CHAdeMO] <= 5A\n[CCS] <= 1A
  |||
end loop
...
|||
```

## Contactors welding detection (optional)

Depending on the communication protocol used, as well as on the vehicle willingness to do it, there
might be an optional step of contactor welding detection. The vehicle will open and close its
positive and negative contactors in a particular sequence that allows it to detect if one of the
contactors got welded during the charging.

During this test, the charger is not involved, apart from reporting regularly its present output
voltage.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Contactors welding detection (optional) ==
|||

PEV -> EVSE: Welding detection
activate PEV
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Welding_Detection

|||
loop
  |||
  Charger -> EVSE: [0x63000] Power_Modules_Status.Present_Voltage == XXX
  PEV -> EVSE: Welding detection continue
  activate EVSE
  EVSE --> PEV: Present voltage
  deactivate EVSE
  deactivate PEV
  |||
end loop
...
|||
```

## Terminating charge session

When the charge session is over, the vehicle opens its contactors. Then, whoever owns the lock of plug/inlet waits for
the voltage to lower to a safe level before unlocking the connector.

The controller then emits [Charge_Session_Finished](charge-controllers/secc_generic/can_v3.md#Charge_Session_Finisheds)
as a formal way to tell customer controller charging is done for now.

However, state of [Advantics_Controller_Status](charge-controllers/secc_generic/can_v3.md#Advantics_Controller_Statuss)
will continue to report *Closing_Communication* for some seconds as some communication protocols require to wait a bit
before the charger becomes available again. Once that delay is passed, the controller goes back to *Waiting_For_PEV*
state in
[Controller starts-up](#Controller starts-up).

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Terminating charge session ==

|||
PEV -> PEV: Open contactors

|||
group CHAdeMO only
  loop Waiting for voltage on plug <= 10V
    |||
    Charger -> EVSE: [0x63000] Power_Modules_Status.Present_Voltage == XXX
    |||
  end loop
  |||
  EVSE -> EVSE: Unlock connector
  |||
end group
|||
group only for CCS & MCS
  |||
  PEV -> PEV: Wait for low voltage
  PEV -> PEV: Unlock connector
  |||
end group
|||

PEV -> EVSE: Charge session finished
EVSE -> Charger: [0x6B000] Advantics_Controller_Status.State == Closing_Communication
EVSE -> Charger: [0x6B004] Charge_Session_Finished

|||

EVSE -> PEV: [User] Unplug
|||
```

### User-initiated normal stop of charge

It is possible for a user to decide to stop the charge before its battery is full. User can either
use the vehicle own charge stop method. Or it can use a charge stop button on the charger.

If this button is physical, then it can be wired to a free digital input on the Advantics controller.
In that case, you should configure it in the charger config file.

If this button is on an HMI screen, the customer controller can emulate the physical button input
using the [User_Stop_Button](charge-controllers/secc_generic/can_v3.md#Sequence_Control-User_Stop_Button) flag
in [Sequence_Control](charge-controllers/secc_generic/can_v3.md#Sequence_Control) message.

In practice, this only signals to the vehicle that the charger wants to do a normal charge stop.
Vehicle should honor the request quickly. If the request happens during charging, it will behave
like a normal charge termination.
