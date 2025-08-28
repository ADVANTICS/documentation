> [!UPDATE] {docsify-updated}
# Charge Sequence Diagram

```plantuml
hide footbox
title Beginning of charge session
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

...
|||
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

```plantuml
hide footbox
title Insulation test and precharge
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

```plantuml
hide footbox
title Actual charging
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

```plantuml
hide footbox
title End of charge session
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
