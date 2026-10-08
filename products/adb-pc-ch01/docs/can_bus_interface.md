# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [Identification](#Identification) | 0x830000 | 8 |  | 1000 |
| [Bootloader_UID](#Bootloader_UID) | 0x830001 | 8 |  | 1000 |
| [Firmware_UID](#Firmware_UID) | 0x830002 | 8 |  | 1000 |
| [CAN_API_Version](#CAN_API_Version) | 0x830003 | 3 |  | 1000 |
| [CH01_Control](#CH01_Control) | 0x830010 | 8 |  |  |
| [CH01_Status](#CH01_Status) | 0x830011 | 8 |  | 1000 |
| [CH01_Latched_Faults](#CH01_Latched_Faults) | 0x830012 | 8 |  | 100 |
| [CH01_DC_Setpoint_Control](#CH01_DC_Setpoint_Control) | 0x830014 | 8 |  |  |
| [CH01_DC_Setpoint_Readback](#CH01_DC_Setpoint_Readback) | 0x830015 | 8 |  | 1000 |
| [CH01_DC_Measurements](#CH01_DC_Measurements) | 0x830020 | 4 |  | 100 |
| [CH01_AC_L1_Measurements](#CH01_AC_L1_Measurements) | 0x830021 | 8 |  | 100 |
| [CH01_AC_L2_Measurements](#CH01_AC_L2_Measurements) | 0x830022 | 8 |  | 100 |
| [CH01_AC_L3_Measurements](#CH01_AC_L3_Measurements) | 0x830023 | 8 |  | 100 |
| [CH01_Temperatures](#CH01_Temperatures) | 0x830024 | 6 |  | 100 |
| [CH01_Internal_DC_Measurements](#CH01_Internal_DC_Measurements) | 0x830025 | 8 |  | 100 |
| [CH01_Grid_Connection_Measurements](#CH01_Grid_Connection_Measurements) | 0x830026 | 8 |  | 100 |
| [Stack_Control](#Stack_Control) | 0x830045 | 6 |  |  |
| [Fault_Control](#Fault_Control) | 0x830050 | 1 |  |  |


<a id="Identification"></a>
## Identification { #Identification }


| * | * |
|---|---|
| **Frame ID** | 0x830000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Contains information about the device sending messages with the corresponding Module type
and stack position as encodede in the arbitration ID.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Type | 8 | Label set |
| Revision | 8 | Label set |
| Variant | 8 | Label set |
| Stack_position | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Type { #Identification-Type }

The module Type. This is the product identifier and appears in bits [23:16] of the arbitration ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| GC01 | 128 |
| AC01 | 129 |
| DC01 | 130 |
| CH01 | 131 |

#### Revision { #Identification-Revision }

The hardware revision number. As the hardware is updated over time this number will change

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| R0 | 0 |
| R1 | 1 |
| R2 | 2 |

#### Variant { #Identification-Variant }

Variants define units that are the same product but with differing specifications (like a higher current variant for example)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| VA00 | 0 |

#### Stack_position { #Identification-Stack_position }

This signal mirrors the stack position that is at bits [15:8] of the CAN arbitration ID.
It used to indicate the configured stack position and changes
when receiving a valid stack control message in which the serial number matched.
In the case in which a matching stack control message is received the new stack position is
written to the EEPROM configuration memory.
The CAN arbitration ID does not change when a stack position update is received, only
this signal changes. The value that determins bits [15:8] of the CAN arbitration ID is
read from eeprom once at boot time and does not change over the runtime of the converter.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### serial_number { #Identification-serial_number }

serial number of the power converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="Bootloader_UID"></a>
## Bootloader_UID { #Bootloader_UID }


| * | * |
|---|---|
| **Frame ID** | 0x830001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Unique identifier of the bootloader firmware used on this module

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID | 64 | Unsigned |

### Payload description

#### UID { #Bootloader_UID-UID }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  |  |


<a id="Firmware_UID"></a>
## Firmware_UID { #Firmware_UID }


| * | * |
|---|---|
| **Frame ID** | 0x830002 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Unique identifier of the application firmware used on this module. This ID allows to identify what exact version of the firmware is running on the converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| UID | 64 | Unsigned |

### Payload description

#### UID { #Firmware_UID-UID }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 64 | Unsigned |  | 1 | 0 |  |  |


<a id="CAN_API_Version"></a>
## CAN_API_Version { #CAN_API_Version }


| * | * |
|---|---|
| **Frame ID** | 0x830003 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

This message declares the version of the CAN API that is provided by the converter.
The numbers follow the semver convention

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Major | 8 | Unsigned |
| Minor | 8 | Unsigned |
| Patch | 8 | Unsigned |

### Payload description

#### Major { #CAN_API_Version-Major }

The Major version number. This number increases if there are changes that break backwards compatibility

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Minor { #CAN_API_Version-Minor }

The Minor version number. This number increases if there are backwards compatible changes, like new messages or the use of previously reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Patch { #CAN_API_Version-Patch }

The Patch number. This number increases when changes to descriptions and documentation/comments are made

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="CH01_Control"></a>
## CH01_Control { #CH01_Control }


| * | * |
|---|---|
| **Frame ID** | 0x830010 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Select the operating mode of the CH01.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Command | 4 | Label set |
| Efficiency_Optimization | 1 | Label set |

### Payload description

#### Command { #CH01_Control-Command }

The command that tells the CH01 what to do. Currently only DC side control
is available.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 4 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Off | 0 |
| DC_Side_Control | 1 |

#### Efficiency_Optimization { #CH01_Control-Efficiency_Optimization }

When optimizing (this signal set to 'enabled') the operation of the CH01 for efficiency, the unit is limited in it's ability
to respond to voltage and current changes. Voltage and current slew rates should be kept below
100V/s and 20A/s respectively.
When this signal is set to 'disabled', the system response is greatly increased, at the cost of a lower conversion
efficiency.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| disabled | 0 |
| enabled | 1 |


<a id="CH01_Status"></a>
## CH01_Status { #CH01_Status }


| * | * |
|---|---|
| **Frame ID** | 0x830011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

The current state of the CH01.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Command_Readback | 4 | Label set |
| State | 8 | Label set |
| Efficiency_Optimizations | 1 | Label set |
| No_AC_Warning | 1 | Label set |
| Incompatible_AC_Warning | 1 | Label set |
| No_Valid_Setpoints_Warning | 1 | Label set |
| SW_forced_Fault | 1 | Label set |
| Hw_Config_Fault | 1 | Label set |
| Hardware_Protection_Fault | 1 | Label set |
| AC_Precharge_Fault | 1 | Label set |
| Overtemperature_Protection_Fault | 1 | Label set |
| Hardware_Overtemperature_Protection_Fault | 1 | Label set |
| Internal_Fault | 1 | Label set |

### Payload description

#### Command_Readback { #CH01_Status-Command_Readback }

The command currently set on the CH01, this is to acknowledge the reception of the command signal

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 4 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Off | 0 |
| DC_Side_Control | 1 |

#### State { #CH01_Status-State }

Current Ch01 operating state.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Init | 0 |
| Idle | 1 |
| Starting | 2 |
| DC_Side_Control | 3 |
| Shutdown | 4 |
| Bleeding | 5 |
| Bleed_done | 6 |
| Fault | 7 |

#### Efficiency_Optimizations { #CH01_Status-Efficiency_Optimizations }

The efficiency optimization is enabled. This limits the slew rate of externally driven
voltages and currents.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| disabled | 0 |
| enabled | 1 |

#### No_AC_Warning { #CH01_Status-No_AC_Warning }

No AC voltage has been detected. The CH01 will refuse to start if no AC voltage
is present

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### Incompatible_AC_Warning { #CH01_Status-Incompatible_AC_Warning }

There Is AC voltage present but it is outside of the region required by the CH01
to operate

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### No_Valid_Setpoints_Warning { #CH01_Status-No_Valid_Setpoints_Warning }

Before operation can commence, setpoints need to be sent to allow operation
This warning says that no setpoints have been sent yet.
The CH01 will not commence power on while this warning is active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### SW_forced_Fault { #CH01_Status-SW_forced_Fault }

The firmware forced a Hardware fault. The sw force trip signal is part of the
Fault_Control Message and can be controlled from there

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hw_Config_Fault { #CH01_Status-Hw_Config_Fault }

The Hardware configuration stored in eeprom is faulty.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hardware_Protection_Fault { #CH01_Status-Hardware_Protection_Fault }

The Hardware interlock is tripped. This fault will stay active until a clear operation
is successful, as it is latched in hardware. This fault should clear upon reception of
the clear command.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### AC_Precharge_Fault { #CH01_Status-AC_Precharge_Fault }

The Internal bus was not sufficiently charged during precharge, possibly indicating wrong wiring or
damaged electronics.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 35 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Overtemperature_Protection_Fault { #CH01_Status-Overtemperature_Protection_Fault }

The overtemperature threshold was reached and caused a the module to cease operations.
Once the module drops below the temp threshold, this fault will clear

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hardware_Overtemperature_Protection_Fault { #CH01_Status-Hardware_Overtemperature_Protection_Fault }

The hardware overtemperature protection faulted and caused a hardware interlock. This fault will
stay latched until it is cleared by the system controller

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 37 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Internal_Fault { #CH01_Status-Internal_Fault }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 38 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |


<a id="CH01_Latched_Faults"></a>
## CH01_Latched_Faults { #CH01_Latched_Faults }


| * | * |
|---|---|
| **Frame ID** | 0x830012 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Faults occurring during operation are latched here. The current state of the fault
is shown in the CH01 Mode Readback message. The faults in this message only clear
if the fault condition has cleared and the command signal is set to the 'clear_fault'
value.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| SW_forced_Fault | 1 | Label set |
| Hw_Config_Fault | 1 | Label set |
| Hardware_Protection_Fault | 1 | Label set |
| AC_Precharge_Fault | 1 | Label set |
| System_Protection_Fault | 1 | Label set |
| Hardware_Overtemperature_Protection_Fault | 1 | Label set |
| Overtemperature_Protection_Fault | 1 | Label set |
| Internal_Fault | 1 | Label set |

### Payload description

#### SW_forced_Fault { #CH01_Latched_Faults-SW_forced_Fault }

The firmware forced a Hardware fault. The sw force trip signal is part of the
Fault_Control Message and can be controlled from there

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hw_Config_Fault { #CH01_Latched_Faults-Hw_Config_Fault }

The Hardware configuration stored in eeprom is faulty.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hardware_Protection_Fault { #CH01_Latched_Faults-Hardware_Protection_Fault }

The Hardware interlock is tripped. This fault will stay active until a clear operation
is successful, as it is latched in hardware. This fault should clear upon reception of
the clear command.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### AC_Precharge_Fault { #CH01_Latched_Faults-AC_Precharge_Fault }

The Internal bus was not sufficiently charged during precharge, possibly indicating wrong wiring or
damaged electronics.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### System_Protection_Fault { #CH01_Latched_Faults-System_Protection_Fault }

The Converter has an interlock line that the system controller can assert to immediately stop
the converter from operation. This is a hardware line that the control system can simply read
and try to reset. This fault will only clear when a clear message is received and the system controller
does not assert this line.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Hardware_Overtemperature_Protection_Fault { #CH01_Latched_Faults-Hardware_Overtemperature_Protection_Fault }

The hardware overtemperature protection faulted and caused a hardware interlock. This fault will
stay latched until it is cleared by the system controller

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Overtemperature_Protection_Fault { #CH01_Latched_Faults-Overtemperature_Protection_Fault }

The configurable overtemperature thresh has been exceeded, resulting in a fault, shutting
off the module.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |

#### Internal_Fault { #CH01_Latched_Faults-Internal_Fault }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Fault | 1 |


<a id="CH01_DC_Setpoint_Control"></a>
## CH01_DC_Setpoint_Control { #CH01_DC_Setpoint_Control }


| * | * |
|---|---|
| **Frame ID** | 0x830014 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set the DC port setpoints

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #CH01_DC_Setpoint_Control-Voltage }

This is the voltage setpoint of the DC Port. The CH01 will try to maintain the voltage set here
as long as the current required for this is within the current limits.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 1 | 0 |  |  |

#### Current { #CH01_DC_Setpoint_Control-Current }

The maxumum currnet (in either direction) that the CH01 will drive.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="CH01_DC_Setpoint_Readback"></a>
## CH01_DC_Setpoint_Readback { #CH01_DC_Setpoint_Readback }


| * | * |
|---|---|
| **Frame ID** | 0x830015 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** |  |

### Description

Setpoints currently applied on the CH01
Signals mirror message 0x12

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #CH01_DC_Setpoint_Readback-Voltage }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 1 | 0 |  |  |

#### Current { #CH01_DC_Setpoint_Readback-Current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="CH01_DC_Measurements"></a>
## CH01_DC_Measurements { #CH01_DC_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830020 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

Measurements on the DC port.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Signed |
| Current | 16 | Signed |

### Payload description

#### Voltage { #CH01_DC_Measurements-Voltage }

DC port voltage.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### Current { #CH01_DC_Measurements-Current }

DC port current. Positive values mean current sourced by the DC port;
negative values mean current sunk by the DC port.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="CH01_AC_L1_Measurements"></a>
## CH01_AC_L1_Measurements { #CH01_AC_L1_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

AC measurements for line 1.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| RMS_Current | 16 | Signed |
| RMS_Voltage | 16 | Signed |

### Payload description

#### RMS_Current { #CH01_AC_L1_Measurements-RMS_Current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.1 | 0 |  |  |

#### RMS_Voltage { #CH01_AC_L1_Measurements-RMS_Voltage }

Line-to-neutral voltage, using a virtual neutral located at the
average of the vector sum of the three phases.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="CH01_AC_L2_Measurements"></a>
## CH01_AC_L2_Measurements { #CH01_AC_L2_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830022 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

AC measurements for line 2.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| RMS_Current | 16 | Signed |
| RMS_Voltage | 16 | Signed |

### Payload description

#### RMS_Current { #CH01_AC_L2_Measurements-RMS_Current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.1 | 0 |  |  |

#### RMS_Voltage { #CH01_AC_L2_Measurements-RMS_Voltage }

Line-to-neutral voltage, using a virtual neutral located at the
average of the vector sum of the three phases.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="CH01_AC_L3_Measurements"></a>
## CH01_AC_L3_Measurements { #CH01_AC_L3_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830023 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

AC measurements for line 3.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| RMS_Current | 16 | Signed |
| RMS_Voltage | 16 | Signed |

### Payload description

#### RMS_Current { #CH01_AC_L3_Measurements-RMS_Current }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | A | 0.1 | 0 |  |  |

#### RMS_Voltage { #CH01_AC_L3_Measurements-RMS_Voltage }

Line-to-neutral voltage, using a virtual neutral located at the
average of the vector sum of the three phases.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V | 0.1 | 0 |  |  |


<a id="CH01_Temperatures"></a>
## CH01_Temperatures { #CH01_Temperatures }


| * | * |
|---|---|
| **Frame ID** | 0x830024 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

The temperatures measured by the CH01. The CH01 has various sensors in critical locations
of the device. This message reports the hottest and coldest spot of the converter
along with the temperature of the coolant entering the Converter.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Max_Temp | 16 | Signed |
| Min_Temp | 16 | Signed |
| Coolant_Temp | 16 | Signed |

### Payload description

#### Max_Temp { #CH01_Temperatures-Max_Temp }

The highest temperature measured in the  converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | C | 0.1 | 0 |  |  |

#### Min_Temp { #CH01_Temperatures-Min_Temp }

The lowest temperature in the converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | C | 0.1 | 0 |  |  |

#### Coolant_Temp { #CH01_Temperatures-Coolant_Temp }

The Temperature of the Coolant

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | C | 0.1 | 0 |  |  |


<a id="CH01_Internal_DC_Measurements"></a>
## CH01_Internal_DC_Measurements { #CH01_Internal_DC_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830025 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

The internal DC Voltages of the two intermediate busses

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| AC_Side_DC_Voltage | 16 | Signed |
| DC_Side_DC_Voltage | 16 | Signed |

### Payload description

#### AC_Side_DC_Voltage { #CH01_Internal_DC_Measurements-AC_Side_DC_Voltage }

The Voltage of the AC side DC bus

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | C | 0.1 | 0 |  |  |

#### DC_Side_DC_Voltage { #CH01_Internal_DC_Measurements-DC_Side_DC_Voltage }

The Voltage od the DC side DC bus

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | C | 0.1 | 0 |  |  |


<a id="CH01_Grid_Connection_Measurements"></a>
## CH01_Grid_Connection_Measurements { #CH01_Grid_Connection_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x830026 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** |  |

### Description

The internal DC Voltages of the two intermediate busses

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Status | 8 | Label set |
| Voltage_RMS | 16 | Unsigned |
| Frequency | 16 | Unsigned |

### Payload description

#### Status { #CH01_Grid_Connection_Measurements-Status }

The state of the grid as determined by the converter. If the grid is 'good' the
converter may start operations

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Bad | 0 |
| Ok | 1 |

#### Voltage_RMS { #CH01_Grid_Connection_Measurements-Voltage_RMS }

The line to neutral equivalent RMS voltage at the grid connection point.
The measurement point lies in front of the
integrated contactors. This way the grid properties can be measured
even without the converter being connected to the grid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 16 | Unsigned | V | 1 | 0 |  |  |

#### Frequency { #CH01_Grid_Connection_Measurements-Frequency }

An estimate of the frequency of the grid
canculated via zero crossing detection.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 16 | Unsigned | Hz | 0.1 | 0 |  |  |


<a id="Stack_Control"></a>
## Stack_Control { #Stack_Control }


| * | * |
|---|---|
| **Frame ID** | 0x830045 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

Set the stack position that the module shall assume on reboot.
The stack position is a way to distinguise multiple modules of the same type
connected to the same bus.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Stack_position | 8 | Unsigned |
| reserved | 8 | Unsigned |
| serial_number | 32 | Unsigned |

### Payload description

#### Stack_position { #Stack_Control-Stack_position }

The new stack position of the module

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### reserved { #Stack_Control-reserved }

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### serial_number { #Stack_Control-serial_number }

The Module serial number to be able to distinguish
a particular module even if it currently shares the same
stack position with another module. The update will only be
applied to the module that has the corresponding serial number

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="Fault_Control"></a>
## Fault_Control { #Fault_Control }


| * | * |
|---|---|
| **Frame ID** | 0x830050 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** |  |

### Description

The Fault Control message is a little bit special. The Clear_Interlock signal in this
message is automatically reset to 0 after a clear attempt so sending multiple identical
messages actually triggers multiple attempts to clear a hardware interlock.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Clear_Interlock | 1 | Single bit |
| Reset_Processor | 1 | Single bit |
| Trip_Interlock | 1 | Single bit |
| Reserved | 5 | Unsigned |

### Payload description

#### Clear_Interlock { #Fault_Control-Clear_Interlock }

Attempts to clear the converter interlock.
If a fault condition is currently active the fault will relatch immediately keeping the module from operating.
In the case where the interlock is already cleared this results in a NoOp.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reset_Processor { #Fault_Control-Reset_Processor }

Reboot the power converter

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 |  |  |

#### Trip_Interlock { #Fault_Control-Trip_Interlock }

When set the Software forces a hardware interlock, needs to be cleared to 0 before
a clear interlock signal will take any effect.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 |  |  |

#### Reserved { #Fault_Control-Reserved }

Reserved space

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 5 | Unsigned |  | 1 | 0 |  |  |
