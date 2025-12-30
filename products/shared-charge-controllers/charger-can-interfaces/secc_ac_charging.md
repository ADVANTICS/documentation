# AC Charging

!!! note
    Only available from version 4.x of the controller system


## CAN interface

The CAN interface to control AC charging is currently based on the generic v2 interface originally meant for DC. It is only re-using some messages:

- `New_Charge_Session` (irrelevant signals will be left at 0)
- `Charge_Status_Change`, when vehicle change between CP state B and C/D
- `Charge_Session_Finished`
- `Emergency_Stop`
- `Advantics_Controller_Status` (only valid states are `Initialising`, `Waiting_For_PEV`, `Negotiating_Connection`, `Connected_With_Full_Info`, `Charging`, `Ending_Charge` and `Closing_Communication`.
- `Power_Modules_Status`, notably for `System_Enable` flag that will pretty much control CP PWM being on or off. Other signals will be ignored (except the ones related to temperature).
- `Power_Modules_Limits`, for changing CP PWM duty cycle with `Maximum_Current` signal (other signal ignored)
- `Sequence_Control`, for `Start_Charge_Authorisation` and `User_Stop_Button`signals

!!! warning
    We expect to control the 3 phases relays with the relay 2 output of the controller


## Flowcharts

### Start of charge

```puml
@startuml
!define ADVANTICS_GREEN #00A99D
!define ADVANTICS_DARK_BLUE #1a365d
!define ADVANTICS_LIGHT_BLUE #2d5aa0
!define ADVANTICS_GRAY #4a5568
!define ADVANTICS_LIGHT_GRAY #e2e8f0

' General diagram style
skinparam backgroundColor ADVANTICS_LIGHT_GRAY
skinparam shadowing false

' Fonts
skinparam defaultFontName Roboto
skinparam defaultFontSize 13
skinparam defaultTextAlignment center

' Lines and borders
skinparam ArrowColor ADVANTICS_DARK_BLUE
skinparam ArrowThickness 2

' Participants, classes, and boxes
skinparam participant {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

skinparam sequence {
  LifeLineBorderColor ADVANTICS_GREEN
  LifeLineBackgroundColor ADVANTICS_LIGHT_GRAY
  ParticipantBorderThickness 1
  BoxLineColor ADVANTICS_GREEN
}

' Notes
skinparam note {
  BackgroundColor #f7fafc
  BorderColor ADVANTICS_LIGHT_BLUE
  FontColor ADVANTICS_GRAY
}

' Titles and headers
skinparam title {
  FontColor ADVANTICS_DARK_BLUE
  FontSize 16
  FontStyle bold
}

' Groups and frames
skinparam package {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

' Legends and text
skinparam legend {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_GRAY
}

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
@enduml
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

!!! tip
    This allows the customer controller to adapt the advertised max current and voltage in relation
    to the vehicle capabilities. For instance, this is useful for chargers using an internal battery as
    power source.


```puml
@startuml
!define ADVANTICS_GREEN #00A99D
!define ADVANTICS_DARK_BLUE #1a365d
!define ADVANTICS_LIGHT_BLUE #2d5aa0
!define ADVANTICS_GRAY #4a5568
!define ADVANTICS_LIGHT_GRAY #e2e8f0

' General diagram style
skinparam backgroundColor ADVANTICS_LIGHT_GRAY
skinparam shadowing false

' Fonts
skinparam defaultFontName Roboto
skinparam defaultFontSize 13
skinparam defaultTextAlignment center

' Lines and borders
skinparam ArrowColor ADVANTICS_DARK_BLUE
skinparam ArrowThickness 2

' Participants, classes, and boxes
skinparam participant {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

skinparam sequence {
  LifeLineBorderColor ADVANTICS_GREEN
  LifeLineBackgroundColor ADVANTICS_LIGHT_GRAY
  ParticipantBorderThickness 1
  BoxLineColor ADVANTICS_GREEN
}

' Notes
skinparam note {
  BackgroundColor #f7fafc
  BorderColor ADVANTICS_LIGHT_BLUE
  FontColor ADVANTICS_GRAY
}

' Titles and headers
skinparam title {
  FontColor ADVANTICS_DARK_BLUE
  FontSize 16
  FontStyle bold
}

' Groups and frames
skinparam package {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

' Legends and text
skinparam legend {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_GRAY
}


hide footbox
title CCS AC charge session over Basic Signaling (ie. PWM)
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
EVSE -> PEV: CP PWM 100% (State A1)

...
|||
== Charge initialisation ==
|||

-> EVSE: [User] Plug-in
PEV -> EVSE: CP 9V (State B1)
activate PEV
activate EVSE
EVSE -> Charger: [0x68001] New_Charge_Session
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Connected_With_Full_Info

|||
== Charger readiness ==
|||

loop Waiting for Power_Modules_Status.System_Enable != Allowed
  |||
  EVSE -> Charger: [0x68001] New_Charge_Session
  activate Charger
  |||
end loop
...
Charger -> EVSE: [0x60010] Power_Modules_Status.System_Enable == Allowed
deactivate Charger
EVSE -> PEV: CP PWM 10..96% (State B2)

|||
== Start of charge ==
|||


PEV -> EVSE: CP 6V or 3V (State C2 or D2)
EVSE -> EVSE: Closing CCS B contactors
EVSE -> Charger: [0x68004] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Started
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Charging
activate Charger
Charger -> Charger: AC supply turns\non within 3s
PEV -> PEV: Starts AC current draw

|||
== Charging ==
|||

loop Every 1s
  |||
  EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Charging
  |||
end loop

...
@enduml
```

### End of charge

```puml
@startuml
!define ADVANTICS_GREEN #00A99D
!define ADVANTICS_DARK_BLUE #1a365d
!define ADVANTICS_LIGHT_BLUE #2d5aa0
!define ADVANTICS_GRAY #4a5568
!define ADVANTICS_LIGHT_GRAY #e2e8f0

' General diagram style
skinparam backgroundColor ADVANTICS_LIGHT_GRAY
skinparam shadowing false

' Fonts
skinparam defaultFontName Roboto
skinparam defaultFontSize 13
skinparam defaultTextAlignment center

' Lines and borders
skinparam ArrowColor ADVANTICS_DARK_BLUE
skinparam ArrowThickness 2

' Participants, classes, and boxes
skinparam participant {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

skinparam sequence {
  LifeLineBorderColor ADVANTICS_GREEN
  LifeLineBackgroundColor ADVANTICS_LIGHT_GRAY
  ParticipantBorderThickness 1
  BoxLineColor ADVANTICS_GREEN
}

' Notes
skinparam note {
  BackgroundColor #f7fafc
  BorderColor ADVANTICS_LIGHT_BLUE
  FontColor ADVANTICS_GRAY
}

' Titles and headers
skinparam title {
  FontColor ADVANTICS_DARK_BLUE
  FontSize 16
  FontStyle bold
}

' Groups and frames
skinparam package {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_DARK_BLUE
}

' Legends and text
skinparam legend {
  BackgroundColor #ffffff
  BorderColor ADVANTICS_GREEN
  FontColor ADVANTICS_GRAY
}

hide footbox
title CCS AC charge session over Basic Signaling (ie. PWM)
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Vehicle" as PEV
participant "Advantics Controller" as EVSE
participant "Customer Controller" as Charger

== Charger-initiated end-of-charge ==
|||

activate PEV
activate EVSE
activate Charger
...

Charger -> EVSE: [0x60010] Power_Modules_Status.System_Enable == Not_Allowed
note over Charger
  or
end note
Charger -> EVSE: [0x60012] Sequence_Control.User_Stop_Button == Pressed

EVSE -> PEV: CP PWM 100% (State C1 or D1)
PEV -> PEV: Stops AC current draw within 3s
PEV -> EVSE: CP 9V (State B1)
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Ending_Charge
Charger -> Charger: AC supply turns\noff within 100ms
deactivate Charger
EVSE -> Charger: [0x68004] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Stopped
EVSE -> EVSE: Opening CCS B contactors
deactivate PEV
deactivate EVSE

...
|||
== Vehicle-initiated end-of charge ==
|||

PEV -> PEV: Stops AC current draw
activate PEV
activate EVSE
activate Charger

PEV -> EVSE: CP 9V (State B2)
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Ending_Charge
Charger -> Charger: AC supply turns\noff within 100ms
deactivate Charger
EVSE -> Charger: [0x68004] Charge_Status_Change.Vehicle_Ready_for_Charging == Charge_Stopped
EVSE -> EVSE: Opening CCS B contactors
EVSE -> PEV: CP 100% (State B1)

...
== Terminating charge session ==
|||

-> EVSE: [User] Unplug
PEV -> EVSE: CP 12V (State A1)
EVSE -> Charger: [0x68007] Charge_Session_Finished
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Closing_Communication
deactivate PEV
...
EVSE -> Charger: [0x68009] Advantics_Controller_Status.State == Waiting_For_PEV
deactivate EVSE

|||
@enduml
```
