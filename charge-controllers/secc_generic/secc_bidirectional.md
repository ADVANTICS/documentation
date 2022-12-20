> [!UPDATE] {docsify-updated}
# SECC Bidirectionality

## Introduction

The third version of ADVANTICS generic interface for SECC introduces an even more generic way of handling power transfer. This extended API provides new features more in line with bidirectional enabled standards, ISO15118-20 and CHAdeMO V2G in particular.

Based on charger configuration and vehicle parameters, the interface will select the operational mode and provide current limits to meet power transfer requirements.
Version 3 of the interface provides improvements that made it easier to integrate, and are more user-friendly while keeping changes minimal to facilitate the migration.

> [!NOTE]
> Generic interface v3, CCS ISO 15118-20 and CHAdeMO V2G are available only from version 4.x.dev10
> of the [development branch](https://www.notion.so/EVSE-Migration-from-3-x-to-4-x-7526d289f055493db054452cbbfeb98f).

## Relevant config entries

- In the pistol section
  - `charger_type`: Use `Advantics_Generic_DC_v3`
  - `is_bidirectional`: Set to `true`
  - `max_charger_voltage`: will be used as the default value in case signal [DC_Power_Parameters.Maximum_Voltage](#DC_Power_Parameters-Maximum_Voltage) is 0.
  - `max_charger_current`: will be used as the default value in case signal [DC_Power_Parameters.Maximum_Charge_Current](#DC_Power_Parameters-Maximum_Charge_Current) is 0.
  - `max_charger_discharge_current`: will be used as the default value in case signal [DC_Power_Parameters.Maximum_Discharge_Current](#DC_Power_Parameters-Maximum_Discharge_Current) is 0.
  - `enable_iso_part20`: Set to `true`
  - `enable_iso_ed1` has been renamed `enable_iso_part2`.


## Changes in the SECC Generic CAN interface v3:

<div class="compact-table">

| Name | ID | Length | Direction | Cycle time | Difference | Note |
|------|----|--------|-----------|------------| ----------- |-----|
| [DC_Power_Control](#DC_Power_Control) | 0x68005 | 8 | IN | 100 | New message | - |
| [Charging_Loop](charge-controllers/secc_generic/can.md#Charging_Loops) | 0x68005 | - | - | - | Removed | Replaced by [DC_Power_Control](#DC_Power_Control)
| [Insulation_Test](charge-controllers/secc_generic/can.md#Insulation_Tests) | 0x68002 | - | - | - | Removed | Merged into [DC_Power_Control](#DC_Power_Control)
| [Precharge](charge-controllers/secc_generic/can.md#Precharge) | 0x68003 | - | - | - | Removed | Merged into [DC_Power_Control](#DC_Power_Control)
| [DC_Power_Parameters](#DC_Power_Parameters) | 0x60011 | 8 | IN | 100 | New message | - |
| [Power_Modules_Limits](#Power_Modules_Limits) | 0x60011 | - | - | - | Removed | Replaced by [DC_Power_Parameters](#DC_Power_Parameters)

</div>

Download CAN DBs:

- [Advantics Generic EVSE protocol v3 (Kayak format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.kcd ':ignore')
- [Advantics Generic EVSE protocol v3 (DBC format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.dbc ':ignore')

### Migration from v2

There are two important concepts introduced with v3:

- It can function with setpoints that either mean targets (as it used to), or limits of a range.
- All preliminary power functions like insulation test and precharge have been merged into a single
  message.

Note that the range mode will only be used with charging protocols supporting it (usually the ones
made for V2X applications).

`Charging_Loop` has been renamed to `DC_Power_Control`. We kept the first signal, `Target_Voltage`
as-is. Note that `Target_Current` got renamed `Current_Range_Max`, but still serves grossly the same
function. Ie. in the simplest case you could still charge by using only that value as target current
setpoint. And actually, that's how the target mode function.

The `State_of_Charge` signal moved to the end of the message to make space for new signals that give
the present power function, setpoint mode, and output bleeding command.

The new power function signal covers these cases: Off, Standby, Insulation test, Precharge and Power
transfer. Note that the "quircky" behaviour of v2 to use `Charging_Loop` with 0 V and 0 A targets to
mean standby after insulation tests and precharge has been streamlined into a proper `Standby` power
function. For compatibility, the 0 V and 0 A setpoints while in standby have also been kept. And as
now there is a single "power-related" message, it becomes sementically more appropriate to emit it
outside of the charging part of the session.

You will however no longer receive the `Insulation_Test` and `Precharge` messages anymore have they
have been entirely removed.

The `Output_Bleed` command signal has been added to signal explicitly when the charger should
actively stop presenting an output voltage. You should definitly read its [documentation](#DC_Power_Control-Output_Bleed)
as it can be a bit tricky to use correctly. Note however that it might still change a little bit in
the future for further clarity (like splitting the command with one for output contactors and one
for power modules bleeding).

Finally, `Power_Modules_Limits` has been renamed `DC_Power_Parameters`. It is also meant to be used
pretty much as the old message was. Ie. the first signal is the same. The second has been renamed
from `Maximum_Current` to `Maximum_Charge_Current` for consistency with the third, new, signal
`Maximum_Discharge_Current`. A fourth signal, `Range_Target_Current` has been added, but is used
only when we control the power modules directly, and the generic interface is used as a way to
externally control some parameters of the charge.

## DC_Power_Control

<div class="noheader-table small-table compact-table">

| * | * |
|---|---|
| **Frame ID** | 0x68005 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

</div>

### Description


Sent during any powered phase of a DC charge session. This message contains the
power function in use, setpoint targets or range, the setpoints mode, the output
bleeding command, and the present vehicle SoC.

#### Power function

The power function currently in use is given by [Power_Function](#DC_Power_Control-Power_Function).
It covers the off state, standby, insulation test, precharge and the actual power
transfer.

During *Standby*, power modules should disable any power processing function (ie.
turn off), but not bleed their output capacitors (ie. leave the output floating) as
a load might be connected at that time.

During *Insulation_Test*, the insulation of the cable is tested by applying a
voltage from the charger. The battery is not connected yet. The test voltage to
apply is given by [Target_Voltage](#DC_Power_Control-Target_Voltage). Power modules report
[Present_Voltage](charge-controllers/secc_generic/can.md#Power_Modules_Status-Present_Voltage) and [Insulation_Resistance](charge-controllers/secc_generic/can.md#Power_Modules_Status-Insulation_Resistance)
and the controller decides when the test passes or fails. Safety standards require a
minimum of 100 Ohms/V insulation resistance. With a typical test voltage of 500 V,
insulation resistance should be >= 50 kOhms. Maximum current to use is not specified.

During *Precharge* (CCS only), charger is expected to match battery voltage at its
output while having no load, apart from capacitors on the line. When charging this
capacitive load, it shall not output more current than [Current_Range_Max](#DC_Power_Control-Current_Range_Max).
The battery voltage to match is given by [Target_Voltage](#DC_Power_Control-Target_Voltage). The
vehicle decides to consider precharge done when it senses on its inlet a voltage that
is +/- 20 V of its battery voltage.

During *Power_Transfer*, actual power is being transfered in one direction or
another. The meaning of setpoints depends on [Setpoints_Mode](#DC_Power_Control-Setpoints_Mode).
The transfer direction depends on the sign of current setpoints, with positive
meaning power being delivered to the vehicle (ie. charge). And negative meaning
power extracted from the vehicle (ie. discharge).

> [!NOTE]
> While targets and ranges are expressed in both voltage and current, it is up
> to power modules to determine which control mode they should use (ie. constant current,
> constant voltage or constant power) depending on the present situation, and the load
> attached to their output. Charging protocols do not define it. In a typical situation,
> insulation tests and precharge have to be controlled in Constant Voltage. Whereas,
> when a battery is connected to the charger output, the vehicle BMS specifies the
> maximum current to be delivered to it, or consummed from it. Which makes it a
> Constant Current process. But you might also encounter a vehicle with a different
> pack voltage (eg. 800 V), and using a DC/DC in between the charger output and its
> battery to convert the voltage. In such case, you might have to run into Constant
> Voltage mode for instance.


#### Setpoints mode

Either the vehicle control the current to be delivered or consummed (that's
*Target_Mode*). Or, a range of acceptable values is given, and power modules are
free to operate within that range (that's *Range_Mode*).

In the simplest (historical) case, power transfer is unidirectional, with the
vehicle requesting a certain amount of current for a target voltage, and power
modules have to deliver that current. *Target_Mode* is used in that case.
And both min and max of the range have the same value. If you do less current than
requested, some vehicle might accept it, and some might terminate the charge on a
current deviation error. [Maximum_Charge_Current](#Power_Transfer_Parameters-Maximum_Charge_Current) offers
a way to dynamically "negotiate" a lower current request properly.

If the vehicle and/or charging protocol wants to use limits instead of targets (eg.
CHAdeMO V2G, or ISO 15118-20 in Dynamic mode), then *Range_Mode* is used. The min
and max of the range are given, and power modules can choose the actual load and
power transfer direction within that range.

Note however that, if in your application power modules are not able to decide of
the load by themselves, then you can treat the maximum of the range as the target
setpoint (which is why the same signal is used for both target and maximum).

During a power transfer, the setpoint mode does not change between range or target.
However, during the rest of the session, for consistency, during *Insulation_Test*
it will be *Target_Mode*. And during *Precharge* it will be *Range_Mode*.
During other power functions it is not relevant.

#### Bidirectional power transfers

Bidirectional power transfers are only possible when both the vehicle and the charger
supports it (on charger side, `is_bidirectional` has to be set to True in the config
file for that pistol). Bidirectional power transfer can happen either in
*Range_Mode* (power modules choose when to switch over) or *Target_Mode* (vehicle
decides when it is time to charge or discharge its battery). Bidirectional in range
mode would typically happen with CHAdeMO V2G, or ISO 15118-20 in Dynamic mode.
Whereas birectional in target mode would happen with ISO 15118-20 in Scheduled mode.

When in range mode, a portion of the range will be in the negative values (or all of
it if only discharge is possible). Note that the positive portion of the range, used
for charging, naturally follows min and max charge current values. Whereas the
negative portion of the range, used for discharging, is mirrored, and its min and
max are logically inverted. Said differently [Current_Range_Min](#DC_Power_Control-Current_Range_Min)
shows the maximum discharge current, but with a negative sign. And
[Current_Range_Max](#DC_Power_Control-Current_Range_Max) shows the maximum charge current with a
positive sign.

In the particular situation only discharge is possible, the minimum of the range is
still the maximum discharge current with a negative sign. And the maximum of the
range is then the minimum discharge current, also with a negative sign.

As such, you can see this range as a "continuous slider" on which you can pick an
operating point, moving between the maximum discharge current (the min), and the
maximum charge current (the max). With 0 as a midpoint (but not necessarily
symmetric). If no discharge is possible, then the min is positive. And if no charge
is possible, then the max is negative.

> [!WARNING]
> The vehicle might not necessarily ramps up or down its requests.




### Payload


<div class="small-table compact-table">

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Target_Voltage | 16 | Unsigned |
| Current_Range_Max | 16 | Signed |
| Current_Range_Min | 16 | Signed |
| Power_Function | 4 | Label set |
| Reserved | 2 | Unsigned |
| Setpoints_Mode | 1 | Single bit |
| Output_Bleed | 1 | Single bit |
| State_of_Charge | 8 | Unsigned |

</div>


### Payload description

#### Target_Voltage :id=DC_Power_Control-Target_Voltage


Voltage setpoint.

In *Insulation_Test*, this is the test voltage, and it should corresponds to
the maximum voltage a charger can theoretically deliver during a charge session.
At the end of the test, this setpoint is set back to 0 V.

In *Precharge*, it usually corresponds to the real battery voltage (unless the
vehicle uses an intermediate DC/DC).

In *Power_Transfer*, it usually corresponds to a voltage significantly higher
than the battery voltage (implying a Constant Current process). However, if the
vehicle uses an intermediate DC/DC, then it corresponds to the input voltage of
that DC/DC.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |   |   |

</div>

#### Current_Range_Max :id=DC_Power_Control-Current_Range_Max


Maximum current to provide (if positive), or minimum current to draw (if negative).

In *Target_Mode*, this signal should be used as the target current setpoint.

In *Insulation_Test*, this signal is not relevant.

In *Precharge*, this signal carries the maximum current the vehicle wants
charger to respect. Usually a value between 0 and 2 A.

In *Power_Transfer*, this signal gives the maximum of the current range to use.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Amps | 0.1 | 0 |   |   |

</div>

#### Current_Range_Min :id=DC_Power_Control-Current_Range_Min


Maximum current to draw (if negative), or minimum current to provide (if positive).

In *Target_Mode*, this signal will have the same value than
[Current_Range_Max](#DC_Power_Control-Current_Range_Max).

In *Insulation_Test*, this signal is not relevant.

In *Precharge*, this signal is 0 A.

In *Power_Transfer*, this signal gives the minimum of the current range to use.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | Amps | 0.1 | 0 |   |   |

</div>

#### Power_Function :id=DC_Power_Control-Power_Function


This signal describes the sort of power function expected from power modules at
a particular point in the process.

*Off*: Power modules turn off any power processing function. And the output of
the charger (exposed on the pistol pins) has ~0 V, floating.

*Standby*: Power modules do not run any power processing function, while
remaining ready to receive future requests. A load might still be connected to
their output. Therefore, unless comanded by [Output_Bleed](#DC_Power_Control-Output_Bleed),
it should remain floating, with contactors still closed, and no discharge of
their output capacitors should be attempted.

*Insulation_Test*: Power modules (or an external dedicated safety module) apply
high voltage and measure the current leaked through ground. The test voltage
reaches up to the vehicle, but its input contactors are still open.

*Precharge*: Power modules match the requested voltage while limiting their
output current (only some capacitance should be charged during this process).
The purpose is to avoid arcing when vehicle contactors close.
Precharge is specific to CCS. In CHAdeMO you either have a diode at the output
of the charger (unidirectional). Or a custom precharge circuit around the main
output contactors (bidirectionnal, or unidirectional made without diode).

*Power_Transfer*: Main mode of operation, as power is being transfered in one
way or another. See the documentation of [Setpoints_Mode](#DC_Power_Control-Setpoints_Mode) and
others signals of this message for more details.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 4 | Label set |   | 1 | 0 |   |   |

</div>


<div class="small-table compact-table">

| Label name | Value |
|------------|-------|
| Off | 0 |
| Standby | 1 |
| Insulation_Test | 2 |
| Precharge | 4 |
| Power_Transfer | 8 |

</div>

#### Reserved :id=DC_Power_Control-Reserved

Reserved bits for future uses.


<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 52 | 2 | Unsigned |   | 1 | 0 |   |   |

</div>

#### Setpoints_Mode :id=DC_Power_Control-Setpoints_Mode


Defines how power modules should follow setpoints.

*Target_Mode*: Power transfer is controlled by the vehicle, and power modules
should follow the given targets. Min and max of the range have the same value.

*Range_Mode*: All parties provide ranges of acceptable limits, and the
controller gives a merged view of that range. Power modules are then free to
provide or draw power within that range.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 54 | Single bit | Single bit |   | 1 | 0 |   |   |

</div>


<div class="small-table compact-table">

| Label name | Value |
|------------|-------|
| Target_Mode | 0 |
| Range_Mode | 1 |

</div>

#### Output_Bleed :id=DC_Power_Control-Output_Bleed


Tells when charger output should forcibly be lowered to less than or equal to
20 V. It can be done by opening output contactors and/or bleed the voltage of
power modules output capacitors.

Note that how you lower the output voltage depends on when the bleed is requested
and for which purpose. As well as if you have output contactors or solely rely
on capacitor bleeding.

Can only happen in *Standby* function, with voltage and current setpoints set
to 0.

Output bleed is requested at the following points in the charge session:

- After insulation test, and before precharge (CCS) or power transfer (CHAdeMO).
  In this case, the controller does not command output contactors to open by
  itself (ie. using its onboard relay) as they would have to reclose shortly
  after. It will however wait that output voltage lower to <= 20 V to comply
  with charging standards. Therefore, this one is more about bleeding output
  capacitors before continuing to next step.
- After power transfer, when [State](charge-controllers/secc_generic/can.md#Advantics_Controller_Status-State) is
  *Ending_Charge*, current has lowered to less than 1 A, and after having
  opened output contactors (using controller own relay). In this case, the
  controller does not need to wait for voltage to lower. Note that at this point
  the vehicle battery might still be connected to charger output (hence why it
  does not wait on the voltage). Which means if your charger does not have output
  contactors, you should actually avoid bleeding output capacitors at this point,
  and ignore the bleed request.
- When entering [State](charge-controllers/secc_generic/can.md#Advantics_Controller_Status-State) == *Closing_Communication*
  if output voltage is above 20 V. It could happen after a welding detection
  process from the vehicle in case there are no output contactors and output
  capacitors are still charged (or got recharged during welding detection). This
  bleed request is for safety, in order to avoid exposing high voltages on the
  pistol contacts once it gets unplugged from the vehicle.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 55 | Single bit | Single bit |   | 1 | 0 |   |   |

</div>


<div class="small-table compact-table">

| Label name | Value |
|------------|-------|
| No_Bleed | 0 |
| Bleed | 1 |

</div>

#### State_of_Charge :id=DC_Power_Control-State_of_Charge

Battery SoC in percent (informative, do not rely on it).


<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |

</div>

| 56 | 8 | Unsigned | kOhms | 2 | 0 |   |   |

</div>



## DC_Power_Parameters

<div class="noheader-table small-table compact-table">

| * | * |
|---|---|
| **Frame ID** | 0x60011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | NA |
| **Direction** | OUT |

</div>

### Description


Message to dynamically set parameters of power transfer (limits, forced setpoints).
This message can be sent as often as needed (but not faster than 100ms).



### Payload


<div class="small-table compact-table">

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Maximum_Voltage | 16 | Unsigned |
| Maximum_Charge_Current | 16 | Unsigned |
| Maximum_Discharge_Current | 16 | Unsigned |
| Range_Target_Current | 16 | Signed |

</div>


### Payload description

#### Maximum_Voltage :id=DC_Power_Parameters-Maximum_Voltage


Maximum output voltage of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_voltage` from config file.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |   |   |

</div>

#### Maximum_Charge_Current :id=DC_Power_Parameters-Maximum_Charge_Current


Maximum charge current of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_current` from config file.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Amps | 0.1 | 0 |   |   |

</div>

#### Maximum_Discharge_Current :id=DC_Power_Parameters-Maximum_Discharge_Current


Maximum discharge current of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_discharge_current` from
config file.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Amps | 0.1 | 0 |   |   |

</div>

#### Range_Target_Current :id=DC_Power_Parameters-Range_Target_Current


This signal is useful only for chargers using one of the supported power module
interface (ie. we directly control power modules), plus the generic interface
as a mean of external control.

When [Setpoints_Mode](#DC_Power_Control-Setpoints_Mode) == *Range_Mode*, and power modules
are of a kind that cannot decide of the load current by themselves, by default
the maximum of the range will be used.

With this signal, you can set a different target setpoint that will be send to
power modules. Direction of power transfers is chosen with the sign of this
signal. When the sign changes, a switch over will happen.

Values are always capped to the allowed range given in [DC_Power_Control](#DC_Power_Control).
Provided values will also be ramped up or down, using ramp slopes defined by
config file entries `current_ramp_up_rate` and `current_ramp_down_rate`.

Note that the actual setpoint sent to power modules is not reflected in
[DC_Power_Control](#DC_Power_Control) message, as values in this message need to keep
reflecting the full allowed range. Ie. [DC_Power_Control](#DC_Power_Control) will not emulate
a *Target_Mode*, and it will still show the normal *Range_Mode*.

Note also that while the same functionality could be achieved by changing
[Maximum_Charge_Current](#Power_Transfer_Parameters-Maximum_Charge_Current), this Range_Target_Current
signal is actually entirely internal, and the value is never directly reported
to the vehicle. Which mean Maximum_Charge_Current can still reflect the true
maximum charge current advertised to the vehicle.

This signal does nothing in the following situations:
- [Setpoints_Mode](#DC_Power_Control-Setpoints_Mode) == *Target_Mode*.
- Or you only use the generic interface, and manage power modules yourself.



<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | Amps | 0.1 | 0 |   |   |

</div>
