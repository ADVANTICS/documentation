# AC Charging

!!! note
    Only available from version 4.x of the controller system


!!! note
    AC charging is only working on `ADM-CS-SECC` (DIN rail variant) controller, as it has a dedicated CCS AC port.


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

```plantuml
@startuml
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

```plantuml
@startuml
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
