> [!UPDATE] {docsify-updated}
# Sequences of actions

Before describing the CAN communication, let's take a detailed look at the sequences of actions,
and what each actor in the charge process does.

See [Appendix A](charge-controllers/secc_generic/appendix-a.md) for the full sequence diagram. Extracts of it will be given here.

## Controller starts-up

When powering up the controller, the operating system starts-up, then a few application processes
start. The main controller process is the first one to start, and will immediately start emitting
the [Advantics_Controller_Status](charge-controllers/secc_generic/can.md#Advantics_Controller_Status) message every 100 ms.

At the begining it reports a state of *Initialising* until all internal processes started-up and
are talking to each other.

Afterwards, if the controller is configured to use the sequence flags, it will report a state of
*Not_Available*. This state is meant for pre-start external charge authorization. Once your
controller/HMI as validated the user, it sends a [Sequence_Control](charge-controllers/secc_generic/can.md#Sequence_Controls) message with signal
[Start_Charge_Authorisation](charge-controllers/secc_generic/can.md#Sequence_Control-Start_Charge_Authorisation) set to `Allowed` (value 1).

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

EVSE->Charger: [0x68009] Advantics_Controller_Status.State == Initialising

|||
== Wait for start authorisation ==
|||

EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Not_Available
...
Charger -> EVSE: [0x60012] Sequence_Control.Start_Charge_Authorisation == Allowed

|||
== Wait for vehicle ==
|||

EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Waiting_For_PEV

|||
```

## Charge initialisation

Once a vehicle plugs-in, a so-called charge session is initialised. It allows for exchange of
important parameters between the vehicle and the charger. Such as voltage, current and power limits.

The content of this initilisation behaves differently from communication protocols. In CHAdeMO it is
rather quick, but requires the user to push a start button on the charger. In CCS it can be a few
tens of seconds, especially if payment authorisation is carried on.

[Advantics_Controller_Status](charge-controllers/secc_generic/can.md#Advantics_Controller_Statuss) message reports a state of *Negotiating_Connection* at first.
Once done with the negotiation, it reports *Connected_With_Full_Info*.

However, in CCS, if the charger is configured to use external authorisation, and configured to use
the sequence flags, you will have an intermediate state *CCS_Authorisation_Process*.
The controller, and the CCS communication itself, will stay in this state as long as the customer
controller does not set the flag [CCS_Authorisation_Done](charge-controllers/secc_generic/can.md#Sequence_Control-CCS_Authorisation_Done) to `Done` (value 1).
Once `Done` is set, the controller checks [CCS_Authorisation_Valid](charge-controllers/secc_generic/can.md#Sequence_Control-CCS_Authorisation_Valid) flag. If set
to `Valid` (value 1), the communication continue. If set to `Invalid` (value 0), the controller
request a stop of communication to the vehicle (and it won't allow the vehicle to "force-through"
the sequence). If not using CCS external authorisation and sequence flags, the controller just
consider user is always authorised and continues directly.

When *Connected_With_Full_Info*, it also sends a [New_Charge_Session](charge-controllers/secc_generic/can.md#New_Charge_Sessions) message containing
relevant information provided by the vehicle. If the controller is configured to use the sequence
flags, it will wait that [Charge_Parameters_Done](charge-controllers/secc_generic/can.md#Sequence_Control-Charge_Parameters_Done) is set to `Done` (value 1) to
continue to the next step (insulation test). Before that, as long as it is `Not_Done` (value 0), the
customer controller can modify the content of the [Power_Modules_Limits](charge-controllers/secc_generic/can.md#Power_Modules_Limitss) message. If not using the
sequence flags then it continues directly with either the static limit values set in the config file,
or whatever as been sent in [Power_Modules_Limits](charge-controllers/secc_generic/can.md#Power_Modules_Limitss) before that.

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
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Negotiating_Connection
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
== [CCS only] External authorisation ==
|||

PEV -> EVSE: [CCS only] Authorised?
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == CCS_Authorisation_Process
activate Charger
...
Charger -> EVSE: [0x60012] Sequence_Control.CCS_Authorisation_Valid == Valid
Charger -> EVSE: [0x60012] Sequence_Control.CCS_Authorisation_Done == Done
EVSE --> PEV: [CCS only] User is valid
deactivate Charger

|||
== Connected with full info ==
|||

EVSE -> Charger: [0x68001] New_Charge_Session
activate Charger
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Connected_With_Full_Info
...
Charger -> EVSE: [0x60011] Power_Modules_Limits
Charger -> EVSE: [0x60012] Sequence_Control.Charge_Parameters_Done == Done
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

By electrical safety standards, the insulation resistance should be of at least 100 Ω/V. For a
500 V test voltage that means an insulation resistance >= 50 kΩ.

At first, the lock of the plug or inlet should be activated by now. Then the vehicle gives its
permit to the charger to apply power. At this point, the Advantics controller has a mechanism to
allow power modules to wake up and be ready for power before doing the actual insulation test.
[New_Charge_Session](charge-controllers/secc_generic/can.md#New_Charge_Sessions) will be sent periodically as long as customer controller is not sending a
message [Power_Modules_Status](charge-controllers/secc_generic/can.md#Power_Modules_Status) with [System_Enable](charge-controllers/secc_generic/can.md#Power_Modules_Status-System_Enable) different from
*Allowed* (value 1).

> [!ATTENTION]
> This [System_Enable](charge-controllers/secc_generic/can.md#Power_Modules_Status-System_Enable) flag will be used even when the controller is
> configured to NOT use the sequence flags.

> [!TIP]
> This allows power modules to be in sleep mode, only waking up on incoming [New_Charge_Session](charge-controllers/secc_generic/can.md#New_Charge_Sessions)
> messages, and gives it some times to initialise. Internally, the controller manages to make the
> vehicle wait for cable insulation test while power modules wakes up and set
> [System_Enable](charge-controllers/secc_generic/can.md#Power_Modules_Status-System_Enable) to *Allowed*. Therefore, you still have a limited time to
> wake-up as communication protocols may have long timeouts on these states (in the order of a few
> tens of seconds).

> [!NOTE]
> Notice also that once power modules signal they are ready, the controller emits one
> [Target_Voltage](charge-controllers/secc_generic/can.md#Charging_Loop>> message with Charging_Loop-Target_Voltage) == 0 V and
> [Target_Current](charge-controllers/secc_generic/can.md#Charging_Loop-Target_Current) == 0 A. Such [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) message is used by the controller
> multiple times through the whole charging process to signify a sort of "Standby" mode. It is
> expected from the power electronics to just be ready for any future request while not processing any
> power.

Once ready for power, the controller will emit [Insulation_Test](charge-controllers/secc_generic/can.md#Insulation_Tests) messages periodically. Customer
controller should be returning a meaningful value in [Insulation_Resistance](charge-controllers/secc_generic/can.md#Power_Modules_Status-Insulation_Resistance)
of [Power_Modules_Status](charge-controllers/secc_generic/can.md#Power_Modules_Statuss) message. The controller will wait for the present voltage to be at least
90% of the requested test voltage. It then waits for the insulation resistance to be above the
100 Ohms/V limit for at least 10 iterations of the [Insulation_Test](charge-controllers/secc_generic/can.md#Insulation_Tests) message. This number of 10 is
an arbitrary choice from us, which we might change in the future if necessary.

In case this criterion is not met (ie. there is an electrical defect somewhere), the insulation test
state will timeout after 30 seconds. The malfunction is reported to the vehicle, and the whole
charging process stops.

When terminating the insulation test sequence, first the controller emits [Insulation_Test](charge-controllers/secc_generic/can.md#Insulation_Tests)
messages with [Test_Voltage](charge-controllers/secc_generic/can.md#Insulation_Test-Test_Voltage) of 0, as well as [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) messages with
[Target_Voltage](charge-controllers/secc_generic/can.md#Charging_Loop-Target_Voltage) == 0 V and [Target_Current](charge-controllers/secc_generic/can.md#Charging_Loop-Target_Current) == 0 A meaning
"standby". It will emit those messages periodically as long as the present voltage reported by power
modules is above 20 V. It then reports to the vehicle the insulation test is finished and the
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

group CCS only
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
  EVSE -> Charger: [0x68001] New_Charge_Session
  activate Charger
  |||
end loop
...
Charger -> EVSE: [0x60010] Power_Modules_Status.System_Enable == Allowed
deactivate Charger
EVSE -> Charger: [0x68005] Charging_Loop (0 V, 0 A)

|||
== Ready for power ==
|||

EVSE->Charger: [0x68009] Advantics_Controller_Status.State == Insulation_Test
|||
loop Waiting for Power_Modules_Status.Insulation_Resistance >= 100 Ω/V over 50 iterations
  |||
  PEV -> EVSE: [CCS only] Insulation test continue
note left of Charger
  Typical test voltage: 500 V
end note
  EVSE -> Charger: [0x68002] Insulation_Test.Test_Voltage == XXX
  activate Charger
  Charger -> EVSE: [0x60010] Power_Modules_Status.Insulation_Resistance == XXX
  EVSE --> PEV: [CCS only] Insulation test ongoing
  |||
end loop
...
|||

loop Waiting for Power_Modules_Status.Present_Voltage <= 20 V
  |||
  PEV -> EVSE: [CCS only] Insulation test continue
  EVSE -> Charger: [0x68002] Insulation_Test.Test_Voltage == 0
  deactivate Charger
  EVSE -> Charger: [0x68005] Charging_Loop (0 V, 0 A)
  Charger -> EVSE: [0x60010] Power_Modules_Status.Present_Voltage == XXX
  EVSE --> PEV: [CCS only] Insulation test ongoing
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

### Precharge (CCS only)

When the vehicle closes its contactors, the battery voltage is applied up to the charger power
electronics output (or charger's own output contactors if it uses some) which could be at a
potential close to 0 V at this moment. This can create arcing in the contactors if some current is
allowed to flow, and severely deteriote contactors.

To handle this situation, CHAdeMO chose to require chargers to have an output diode. While CCS
adopted the precharge process, which consists in having the charger match the battery voltage to
about 20 V prior to the vehicle closing its contactors.

With CCS, the controller will start emitting [Precharge](charge-controllers/secc_generic/can.md#Precharges) messages periodically when the vehicle
tells it to. These messages contains the target voltage corresponding to the present battery voltage.
It also gives a maximum current limit to comply with (bear in mind some capacitors are still being
charged in the process).

Once the vehicle decide the voltage is right (which it should do by its own measurements before its
contactors), it closes its contactors and continue with the charging sequence. While CCS does not
explicitely tell when the vehicle is ending the precharge process, the controller is using the fact
that the vehicle starts to send requests other than precharge to determine the end of precharge.
At that point, the controller emits a single [Precharge](charge-controllers/secc_generic/can.md#Precharge) message with [Maximum_Current](charge-controllers/secc_generic/can.md#Precharge-Maximum_Current)
set to 0. It also emits a [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loop) message with [Target_Voltage](charge-controllers/secc_generic/can.md#Charging_Loop-Target_Voltage) == 0 V and
[Target_Current](charge-controllers/secc_generic/can.md#Charging_Loop-Target_Current) == 0 A meaning "standby". However, bear in mind that, as the
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

== Precharge [CCS only] ==
|||

PEV -> EVSE: Start precharge
activate PEV
activate EVSE
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Precharge
|||
loop Waiting for abs(Plug voltage - Battery voltage) <= 20 V
  |||
  PEV -> EVSE: Precharge continue
  EVSE -> Charger: [0x68003] Precharge
  activate Charger
  EVSE --> PEV: Present voltage
  Charger -> EVSE: [0x60010] Power_Modules_Status.Present_Voltage == XXX
  |||
end loop
...
|||

PEV -> PEV: Close contactors
|||

PEV -> EVSE: Other request than precharge
deactivate PEV
EVSE -> Charger: [0x68003] Precharge.Maximum_Current == 0
deactivate Charger
EVSE -> Charger: [0x68005] Charging_Loop (0 V, 0 A)
deactivate EVSE
|||
```

### Start of charge

The start of charge state is here to signal the charge is *about* to start. This is to accomodate
for the *Power Delivery* request in CCS which requires the charger to be ready to charge, while the
actual charge might be starting in several hours. It happens if the user of the vehicle configured a
delayed charge or if there have been a negotiation of the charging schedule between the vehicle, the
charger and the electricity provider (only in complex scenario of CCS ISO).

The [Charge_Status_Change](charge-controllers/secc_generic/can.md#Charge_Status_Changes) and [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) messages are sent only once.

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Start of charge ==
|||

PEV -> EVSE: About to start charge
activate PEV
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Waiting_For_Charge
EVSE -> Charger: [0x68004] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Started
EVSE -> Charger: [0x68005] Charging_Loop (0 V, 0 A)

|||
...
note over PEV, Charger
  Delayed charging: Potentially very long delay, up to several hours
end note
...
|||
```

### Charging

This happens as soon as the vehicle and the charger enter the actual charging loop. The process is
very simple: the vehicle send its voltage and current requests to the controller, the controller
forward them to the customer controller, which forward them to power modules. The power modules
should follow and not deviate from the vehicle requests, otherwise the vehicle could stop the charge
abruptly.

While the vehicle can use its own voltage and current measurements, it is also required that the
charger reports its own readings. Therefore, customer controller should update frequently the
readings in [Power_Modules_Status](charge-controllers/secc_generic/can.md#Power_Modules_Statuss) message.

However, the communication protocols are very demanding in terms of charger performances during this
charging loop (CHAdeMO: 100 ms, CCS: 25 ms). In order to comply with these requirements (which
otherwise could trigger a premature end of charge), the controller is not waiting on the power
modules to get the most recent readings. It will use the last ones it has at this moment instead. As
the loops are short, it should not create much lag anyway.

> [!NOTE]
> A note about the periodicity at which the [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) messages are emitted. In CHAdeMO
> they should be sent about every 100 ms. However, in CCS, the vehicle sets the pace, and the standards
> allows for periodicity of up to 60 s (afterwards it is considered a timeout and the charge stops).

About the behaviour of voltage and current changes, this is mostly unspecified (or specified too
differently accross various communication standards). Therefore, you should expect for the worst:
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

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Charging ==

|||
loop Waiting for any stop conditions
  |||
  PEV -> EVSE: Current request
  activate EVSE
  EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Charging
  EVSE -> Charger: [0x68005] Charging_Loop
  activate Charger
  EVSE --> PEV: Present voltage and current
  Charger -> EVSE: [0x60010] Power_Modules_Status
  note over PEV,EVSE
    Not waiting for customer controller latest
    readouts in order to ensure timing constraints.
  end note
  |||
end loop
|||
```

### End of charge

This sequence comes at the end of a charge, when the charge has not been aborpted irregularly. The
[Charge_Status_Change](charge-controllers/secc_generic/can.md#Charge_Status_Changes) and [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) messages are sent only once.

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
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Ending_Charge
EVSE -> Charger: [0x68004] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Stopped
EVSE -> Charger: [0x68005] Charging_Loop (0 V, 0 A)
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

### Contactors welding detection (optional)

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
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Welding_Detection

|||
loop
  |||
  Charger -> EVSE: [0x60010] Power_Modules_Status.Present_Voltage == XXX
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

### Terminating charge session

When the charge session is over, the vehicle opens its contactors. Then, whoever owns the lock of
plug/inlet waits for the voltage to lower to a safe level before unlocking the connector.

The controller then emits [Charge_Session_Finished](charge-controllers/secc_generic/can.md#Charge_Session_Finisheds) as a formal way to tell customer controller
charging is done for now.

However, state of [Advantics_Controller_Status](charge-controllers/secc_generic/can.md#Advantics_Controller_Statuss) will continue to report *Closing_Communication*
for some seconds as some communication protocols require to wait a bit before the charger becomes
available again. Once that delay is passed, the controller goes back to *Waiting_For_PEV* state in
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
    Charger -> EVSE: [0x60010] Power_Modules_Status.Present_Voltage == XXX
    |||
  end loop
  |||
  EVSE -> EVSE: Unlock connector
  |||
end group
|||
group CCS only
  |||
  PEV -> PEV: Wait for low voltage
  PEV -> PEV: Unlock connector
  |||
end group
|||

PEV -> EVSE: Charge session finished
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Closing_Communication
EVSE -> Charger: [0x68007] Charge_Session_Finished

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
using the [User_Stop_Button](charge-controllers/secc_generic/can.md#Sequence_Control-User_Stop_Button) flag in [Sequence_Control](charge-controllers/secc_generic/can.md#Sequence_Control) message.

In practice, this only signals to the vehicle that the charger wants to do a normal charge stop.
Vehicle should honor the request quickly. If the request happens during charging, it will behave
like a normal charge termination.
