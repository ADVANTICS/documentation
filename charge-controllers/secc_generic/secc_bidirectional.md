> [!UPDATE] {docsify-updated}
# MCS & BPT (ISO15118-20)

## Introduction

The third version of ADVANTICS generic interface for our charge station controllers (SECC and SPCC) a generic way of handling power transfer fine-tuned for MCS and BPT applications. This API provides new features more in line with bidirectional enabled standards, ISO15118-20 and CHAdeMO V2G in particular.

Based on charger configuration and vehicle parameters, the interface will select the operational mode and provide current limits to meet power transfer requirements.
Version 3 of the interface provides improvements that made it easier to integrate, and are more user-friendly.

> [!NOTE]
> Generic interface v3, CCS ISO 15118-20 and CHAdeMO V2G are available only from version 4.x.dev10 and newer
> of the [development branch](https://www.notion.so/EVSE-Migration-from-3-x-to-4-x-7526d289f055493db054452cbbfeb98f).

## Relevant config entries

- In the pistol section
  - `charger_type`: Use `Advantics_Generic_DC_v3`
  - `is_bidirectional`: Default to `false`. Set it to `true` to enable bidirectionality.
  - `supports_range_mode` (since dev11): Default to `true`. Set it to `false` if your power modules are not in compatible with range mode.
  - `min_charger_voltage`: Default to 0.
  - `max_charger_voltage`: Default to 500. Will be used as the default value in case signal [DC_Power_Parameters.Maximum_Voltage](charge-controllers/secc_generic/can_v3#DC_Power_Parameters-Maximum_Voltage) is 0.
  - `min_charger_current`: Default to 0. For charging direction.
  - `max_charger_current`: Default to 120. For charging direction. Will be used as the default value in case signal [DC_Power_Parameters.Maximum_Charge_Current](charge-controllers/secc_generic/can_v3#DC_Power_Parameters-Maximum_Charge_Current) is 0.
  - `min_charger_power` (since dev11): Default to 0 (meaning computed from `min_charger_voltage` and `min_charger_current`). For charging direction.
  - `max_charger_power`: Default to 0 (meaning computed from `max_charger_voltage` and `max_charger_current`). For charging direction.
  - `min_charger_discharge_current` (since dev11): Default to 0. For discharging direction.
  - `max_charger_discharge_current` (since dev11): Default to 0. For discharging direction. Will be used as the default value in case signal [DC_Power_Parameters.Maximum_Discharge_Current](charge-controllers/secc_generic/can_v3#DC_Power_Parameters-Maximum_Discharge_Current) is 0.
  - `min_charger_discharge_power` (since dev11): Default to 0 (meaning computed from `min_charger_voltage` and `min_charger_discharge_current`). For discharging direction.
  - `max_charger_discharge_power` (since dev11): Default to 0 (meaning computed from `max_charger_voltage` and `max_charger_discharge_current`). For discharging direction.
  - `enable_iso_part20`: Set to `true`
  - `enable_iso_ed1` has been renamed `enable_iso_part2`.

## SECC Generic CAN interface v3:

See [all messages page](charge-controllers/secc_generic/can_v3).

Download CAN DBs:

- [Advantics Generic EVSE protocol v3.2 (Kayak format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.2.kcd ':ignore')
- [Advantics Generic EVSE protocol v3.2 (DBC format)](charge-controllers/secc_generic/Advantics_Generic_EVSE_protocol_v3.2.dbc ':ignore')

### Migration from v2 to v3.2

There are two important concepts introduced with v3:

- It can function with setpoints that either mean targets (as it used to), or limits of a range.
- All preliminary power functions like insulation test and precharge have been merged into a single
  message.

Note that the range mode will only be used with charging protocols supporting it (usually the ones
made for V2X applications).

First of all, there has been a complete CAN message IDs renumbering.

`Charging_Loop` has been renamed to `DC_Power_Control`. We kept the first signal, `Target_Voltage`
as-is. Note that `Target_Current` got renamed `Current_Range_Max`, but still serves grossly the same
function. Ie. in the simplest case you could still charge by using only that value as target current
setpoint. And actually, that's how the target mode function.

The `State_of_Charge` signal was removed. And new signals have been added to give the present power
function, setpoint mode, and output voltage lowering and contactors opening commands.

The new power function signal covers these cases: Off, Standby, Insulation test, Precharge and Power
transfer. Note that the "quirky" behaviour of v2 to use `Charging_Loop` with 0 V and 0 A targets to
mean standby after insulation tests and precharge has been streamlined into a proper `Standby` power
function. For compatibility, the 0 V and 0 A setpoints while in standby have also been kept. And as
now there is a single "power-related" message, it becomes semantically more appropriate to emit it
outside the charging part of the session.

You will however no longer receive the `Insulation_Test` and `Precharge` messages anymore have they
have been entirely removed.

The `Lower_Output_Voltage` and `Output_Contactors` command signals have been added to signal
explicitly when the charger should actively stop presenting an output voltage using one way or
another. You should definitely read [their](DC_Power_Control-Output_Contactors)
[documentations](charge-controllers/secc_generic/can_v3#DC_Power_Control-Lower_Output_Voltage)
as it can be a bit tricky to use correctly.

That was for the "core" part of power related things. Around that, other things changed, notably
around various information vehicle is giving us. In `New_Charge_Session`, signals
`EV_Maximum_Voltage`, `EV_Maximum_Current`, `Battery_Capacity` and `State_of_Charge` have been
removed. Length of that message reduced accordingly. Same thing happened for `State_of_Charge` that
used to be in `Charging_Loop` message.

Instead, vehicle information are provided by a set of new dedicated messages, `EV_Information_Battery`,
`EV_Information_Voltages`, `EV_Information_Charge_Limits`, `EV_Information_Discharge_Limits`. These
will be sent at least once after the first `New_Charge_Session` is emitted, and whenever the vehicle
changes these values. A future iteration of the interface will provide even more information, in
particular for energy, times, identification, and few other things.

Finally, `Power_Modules_Limits` has been renamed `DC_Power_Parameters`. It is also meant to be used
pretty much as the old message was. Ie. the first signal is the same. The second has been renamed
from `Maximum_Current` to `Maximum_Charge_Current` for consistency with the third, new, signal
`Maximum_Discharge_Current`. A fourth signal, `Range_Target_Current` has been added, but is used
only when we control the power modules directly, and the generic interface is used as a way to
externally control some parameters of the charge.

### Migration from v3 to v3.2

If you already migrated from v2 to v3, here are the changes between v3 and v3.1:

- Changed message IDs:
    - `Advantics_Controller_Status`: From 0x68009 to 0x6B000
    - `New_Charge_Session`: From 0x68001 to 0x6B001
    - `Charge_Status_Change`: From 0x68004 to 0x6B002
    - `DC_Power_Control`: From 0x68005 to 0x6B003
    - `Charge_Session_Finished`: From 0x68007 to 0x6B004
    - `Emergency_Stop`: From 0x68006 to 0x6B005
    - `ADM_CO_CUI1_Inputs`: From 0x6800A to 0x6B200
    - `ADM_CS_SECC_Inputs`: From 0x6800B to 0x6B201
    - `Power_Modules_Status`: From 0x60010 to 0x63000
    - `DC_Power_Parameters`: From 0x60011 to 0x63001
    - `Sequence_Control`: From 0x60012 to 0x63002
    - `ADM_CS_SECC_Outputs`: From 0x60013 to 0x63201
- `New_Charge_Session` message:
    - Removed `EV_Maximum_Voltage`, `EV_Maximum_Current`, `Battery_Capacity` and `State_of_Charge`  signals
        - These are now covered by new dedicated messages
        - Consequently, message length changed from 8 to 2 bytes
- `DC_Power_Control`message:
    - `Setpoints_Mode` signal moved from bit 54 to 53
    - Added `Output_Contactors` signal
    - Renamed `Output_Bleed` signal to `Lower_Output_Voltage`, with simplification around how to control contactors
    - Removed `State_of_Charge` signal.
        - Like in case of `New_Charge_Session`, the SoC information is now covered by a new dedicated message.
        - Consequently, message length changed from 8 to 7 bytes.
- Adding new messages:
    - [0x6B100] `EV_Information_Battery` with signals:
        - `Battery_Capacity`
        - `Present_State_of_Charge`
    - [0x6B101] `EV_Information_Voltages` with signals:
        - `EV_Minimum_Voltage`
        - `EV_Maximum_Voltage`
    - [0x6B102] `EV_Information_Charge_Limits` with signals:
        - `EV_Minimum_Charge_Current`
        - `EV_Maximum_Charge_Current`
        - `EV_Minimum_Charge_Power`
        - `EV_Maximum_Charge_Power`
    - [0x6B103] `EV_Information_Discharge_Limits` with signals:
        - `EV_Minimum_Discharge_Current`
        - `EV_Maximum_Discharge_Current`
        - `EV_Minimum_Discharge_Power`
        - `EV_Maximum_Discharge_Power`
    - [0x6B300] `OCPP_Control` with signals:
        - `Dynamic_Target_Current`
    - Side note: expect a future iteration to cover energy and time info as well

## CHAdeMO V2G

ADVANTICS charge controller supports CHAdeMO vehicle to grid application following the CHAdeMO V2G guidelines. The controller needs to be configured as described in the section [Relevant config entries](#Relevant-config-entries).
### Operating Modes

The CHAdeMO Bidirectional application is designed to be compatible with all CHAdeMO protocol versions, including non-bidirectional ones. In cases where a vehicle does not support bidirectionality, the application seamlessly operates in target mode. However, for vehicles that do support bidirectional functionality, the application operates in range mode, allowing customers to select the desired setpoint based on their specific requirements.

### Replacing CHAdeMO Diode with Precharge Stage

In a CHAdeMO bidirectional setup, it is necessary to replace the CHAdeMO diode with a precharge stage in order to allow current to flow in the opposite direction (discharge) while also protecting the contactors. The CHAdeMO protocol does not provide a specific standardized solution for this scenario, so you have the flexibility to either create your own precharge stage or utilize the proposed solution.

To implement this, you will need two relays and one precharge resistance:

![CHAdeMO V2G Precharge Stage](../ADM-CS-SECC/images/chademo_precharge.jpg ':size=200%')
<figcaption style="text-align: center">CHAdeMO V2G Precharge Stage</figcaption>


Precharge Relay and Resistance:
&nbsp;

The precharge relay, controlled by the Digital_OUT1 signal from the CHAdeMO application, is connected in series with the precharge resistance. When the precharge relay is activated, it allows current to pass through the precharge resistance. This stage gradually charges the output capacitors before closing the vehicle contactors.

Main Relay:
&nbsp;

The main relay, which operates in parallel with the precharge relay and precharge resistance, is driven by the CHAdeMO relay on the controller (Relay 3 on the controller). This main relay serves the purpose of controlling the primary current flow within the bidirectional setup.

It is important to consider that the digital outputs, used for relay control are limited to 100mA.

The controller can be configured to use this precharge stage as described above by adding the following config entry to the CHAdeMO section in the config file:

```
chademo_precharge = true
```