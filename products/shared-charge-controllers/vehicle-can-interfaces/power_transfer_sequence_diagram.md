# Appendix A

```plantuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU

== Initialisation ==
|||

-> EVCC: [User] Power on
note over EVCC
  System boot-up
  ~15 seconds
end note

EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Initialising

|||
== Wait for charger ==
|||

EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Waiting_For_EVSE

|||
== Charge initialisation ==
|||

EVSE -> EVCC: [User] Plug-in
activate EVSE
activate EVCC
EVCC -> VCU: Plugged_In IO goes to HIGH state
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Negotiating_Connection
|||
loop Exchange of information
  |||
  EVCC -> EVSE
  EVCC -> VCU: [0x600] EVSE_Information.Protocol == ...
  EVCC -> VCU: [0x600] EVSE_Information.Pins == ...
  EVCC -> VCU: [0x600] EVSE_Information.Max_Current == ...
  VCU -> EVCC: [0x610] EV_Information.State_of_Charge == ...
  EVSE --> EVCC
  |||
end loop
...
|||

|||
== Connected with full info ==
|||

EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Connected_With_Full_Info
deactivate EVSE
|||
group Check
  EVCC -> EVCC: Inlet lock
  |||
end group
|||
deactivate EVCC
|||
@enduml
```

```plantuml
@startuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU
participant "On-board charger" as Charger

== AC: Start of charge ==
|||

EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Connected_With_Full_Info
EVCC -> VCU: [0x600] EVSE_Information.Pins == CCS_AC*
EVCC -> VCU: [0x600] EVSE_Information.Max_Current == ...

|||
== AC: Charger is ready ==
|||

EVSE -> EVCC: Ready
activate EVSE
activate EVCC
EVCC -> VCU: [0x601] AC_Control.Ready_To_Deliver_Power == Ready
activate VCU

|||
== AC: Vehicle is ready ==
|||

VCU -> VCU: Internal checks
VCU -> EVCC: [0x611] AC_Status.Ready_To_Charge == Ready
deactivate VCU
EVCC -> EVSE: Ready
EVSE -> EVSE: Closes AC relays

|||
== AC: Charging ==
|||


|||
loop Charging
    |||
    EVSE -> Charger: Applies voltage on AC pins
    EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Charging
    activate VCU
    VCU -> Charger: Charge(max_current=...)
    activate Charger
    Charger -> Charger: Draws current
    |||
end loop

...
@enduml
```

```plantuml
@startuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU
participant "On-board charger" as Charger

...
== AC: Charger-initiated end-of-charge ==
...

EVSE -> EVCC: Not ready
activate EVSE
activate EVCC
activate VCU
activate Charger
EVCC -> VCU: [0x601] AC_Control.Ready_To_Deliver_Power == Not_Ready
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Ending_Charge
VCU -> Charger: Stop charge
Charger -> Charger: Stops current\ndraw
Charger -> VCU: Stopped
deactivate Charger
VCU -> EVCC: [0x611] AC_Status.Ready_To_Charge == Not_Ready
deactivate VCU
EVCC -> EVSE: Not ready
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Closing_Communication
EVSE -> EVSE: Opens AC relays
deactivate EVSE
EVCC -> EVCC: Inlet unlock
deactivate EVCC

...
== AC: Vehicle-initiated end-of charge ==
...


VCU -> Charger: Stop charge
activate EVSE
activate EVCC
activate VCU
activate Charger
Charger -> Charger: Stops current\ndraw
Charger -> VCU: Stopped
deactivate Charger
VCU -> EVCC: [0x611] AC_Status.Ready_To_Charge == Not_Ready
deactivate VCU
EVCC -> EVSE: Not ready
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Ending_Charge
EVSE -> EVSE: Opens AC relays
EVCC -> EVCC: Inlet unlock
EVSE -> EVCC: Not ready
deactivate EVSE
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Closing_Communication
deactivate EVCC

...
== AC: Terminating charge session ==
|||

EVCC -> EVSE: [User] Unplug
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Waiting_For_EVSE

|||
@enduml
```

```plantuml
@startuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU
participant "DC Contactors" as Contactors

== DC: Insulation test ==
|||

EVCC -> EVSE: Start insulation test
activate EVSE
activate EVCC
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Insulation_Test

|||
loop Insulation test
   |||
   EVSE -> Contactors: Applies high voltage
   activate Contactors
   EVSE -> EVSE: Checks
   EVSE -> EVCC: Test status
   EVCC -> EVSE: Continue test
   |||
end loop
...
|||

Contactors -> EVSE: Voltage goes to 0 V
deactivate Contactors
EVSE -> EVCC: Test done
deactivate EVCC
deactivate EVSE

|||
== DC: Precharge ==
|||

VCU --> EVCC: [0x613] DC_Status2.Battery_Voltage == XXX
EVCC -> EVSE: Start precharge with target == XXX
activate EVCC
activate EVSE
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Precharge
activate VCU
|||
loop Waiting for matching voltages
  |||
  EVSE -> Contactors: Applies voltage
  activate Contactors
  VCU --> EVCC: [0x613] DC_Status2.Battery_Voltage == XXX
  VCU --> EVCC: [0x613] DC_Status2.Inlet_Voltage == XXX
  EVSE -> EVCC: Present output voltage == XXX
  EVCC -> EVCC: Check voltages:\nBattery voltage > 20 V\nabs(Inlet voltage - Battery voltage) <= 20 V
  EVCC -> EVSE: Precharge continue with target == XXX
  |||
end loop
...
|||

EVSE -> EVCC: Present output voltage == XXX
EVCC -> VCU: [0x602] DC_Control.Close_Contactors == Close
EVCC --> Contactors: Use controller IOs to drive contactors
EVCC -> EVSE: Precharge continue with target == XXX
Contactors -> Contactors: Closes
VCU --> EVCC: [0x613] DC_Status2.Contactors_Closed == Close
Contactors --> EVCC: Use controller IOs to get contactors feedback
deactivate VCU
EVSE -> EVCC: Present output voltage == XXX
deactivate EVSE
deactivate EVCC

|||
@enduml
```

```plantuml
@startuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU
participant "BMS" as BMS

== DC: Start of charge ==
|||

EVCC -> EVSE: Waiting for charge
activate EVSE
activate EVCC
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Waiting_For_Charge
VCU -> BMS: Charging mode
activate BMS
BMS -> VCU: Current request
VCU -> EVCC: [0x612] DC_Status1
VCU -> EVCC: [0x613] DC_Status2
VCU -> EVCC: [0x610] EV_Information
EVSE -> EVCC: Waiting, ready
deactivate EVCC
deactivate EVSE

== DC: Charging ==

EVCC -> EVSE: Charge at Target Voltage and Current Request
activate EVCC
activate EVSE
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Charging
activate VCU

|||
loop Waiting for any stop conditions
  |||
  BMS -> VCU: Current request
  VCU -> EVCC: [0x612] DC_Status1
  VCU -> EVCC: [0x613] DC_Status2
  VCU -> EVCC: [0x610] EV_Information
  EVSE -> EVCC: Present voltage and current
  EVCC -> EVCC: Capping current request to various limits
  EVCC -> EVSE: Charge at Target Voltage and Current Request
  |||
end loop
|||
@enduml
```

```plantuml
@startuml
hide footbox
skinparam ParticipantPadding 20
skinparam sequenceArrowThickness 2
skinparam roundcorner 20

participant "Charger" as EVSE
participant "Advantics Controller" as EVCC
participant "Customer VCU" as VCU
participant "DC Contactors" as Contactors

== DC: End of charge ==
|||

EVCC -> EVSE: Stopping charge
activate Contactors
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Ending_Charge

|||
== DC: Contactors welding detection ==
|||

EVCC -> EVSE: Welding detection
activate EVCC
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Welding_Detection

|||
loop Waiting for current to lower
  |||
  EVSE -> EVCC: Present voltage == XXX
  VCU --> EVCC: [0x612] DC_Status1.Present_Current == XXX
  EVCC -> EVCC: Check flowing current <= 1 A
  EVCC -> EVSE: Welding detection continue
  |||
end loop
...

EVCC -> VCU: [0x602] DC_Control.Close_Contactors == Open
EVCC --> Contactors: Controller IOs stop driving contactors
Contactors -> Contactors: Opens
deactivate Contactors
VCU --> EVCC: [0x613] DC_Status2.Contactors_Closed == Open
Contactors --> EVCC: Use controller IOs to get contactors feedback

|||
loop Waiting for voltage to lower
  |||
  EVSE -> EVCC: Present voltage == XXX
  VCU --> EVCC: [0x613] DC_Status2.Inlet_Voltage == XXX
  EVCC -> EVCC: Check inlet voltage <= 60 V
  EVCC -> EVSE: Welding detection continue
  |||
end loop
...

EVCC -> EVCC: Inlet unlock
deactivate EVCC

|||
== DC: Terminating charge session ==
|||

EVCC -> EVSE: Charge session finished
EVCC -> VCU: [0x600] EVSE_Information.Communication_Stage == Closing_Communication

|||

EVCC -> EVSE: [User] Unplug
|||
@enduml
```
