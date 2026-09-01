# Integration Guide

This page is the single starting point for integrating the ADM-CS-SECC into a charger. It walks
through **every system the controller talks to** — power modules, output contactors, the vehicle
connector, the insulation monitor, your backend — and for each one lists **all the ways you can wire
it**, together with the configuration entry that selects between them.

Read it once from top to bottom before you wire anything: one choice in particular (which power
module interface you use) decides whether you write any software at all.

!!! info "Who this is for"
    Charger builders. It assumes you own the power stage, the cabinet and the harness, and that the
    controller arrives pre-flashed. For the pinout itself see [Interfaces](interfaces.md); this
    guide tells you *what to connect and why*.

## 1. What the controller does, and what it needs from you

The ADM-CS-SECC owns the vehicle-facing side of the charger: the connectors, the charging protocols
(DIN 70121, ISO 15118-2/-20, CHAdeMO) and the charge sequence. It does **not** convert power. It
tells your power stage what to produce, and expects to be told what the power stage is actually
doing.

Everything below is a **choice**. For each system the controller touches you can use its
dedicated hardware interface, or the CAN bus, and one configuration entry decides which:

| Subsystem | Dedicated hardware interface | Over the CAN bus | Selected by |
|---|---|---|---|
| **Power stage** ([§4](#4-power-modules-the-central-choice)) | — | The generic interface you implement, **or** a supported charger interface the controller speaks natively | [`charger_type`](configuration/pistol-ccs-dc.md#charger_type) in the pistol's section |
| **Output contactors** ([§5](#5-output-contactors-and-cabinet-safety)) | Three relays, one per interface, with hard-wired conditions | [DC_Power_Control](charger-can-interfaces/can_v3.md#DC_Power_Control) commands the sequence | — always hardware |
| **Cabinet safety** ([§5](#5-output-contactors-and-cabinet-safety)) | [Interlock](interfaces.md#interlock) line and [current loop](interfaces.md#current-loop) | — hard-wired, overrides software | — always hardware |
| **Insulation resistance** ([§6](#6-insulation-monitoring)) | A supported insulation monitor the controller reads itself | [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance) | [`insulation_monitor_type`](configuration/pistol-ccs-dc.md#insulation_monitor_type) |
| **Present voltage & current** ([§3](#3-the-charger-can-bus)) | — | [Power_Modules_Status](charger-can-interfaces/can_v3.md#Power_Modules_Status) | — always CAN |
| **Digital IO, LEDs, fans** ([§7](#7-digital-io-leds-and-fans)) | Functions on `dig_inN` / `dig_outN` | [ADM_CS_SECC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Inputs) / [ADM_CS_SECC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Outputs) | `dig_outN = CAN_Controlled` |
| **Backend** ([§8](#8-backend-connectivity)) | Ethernet, 4G | Backend limits arrive as [OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control) | `[ocpp] enabled` |
| **Diagnostics** ([§10](#10-diagnostics)) | — | [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status), [Charge_Status_Change](charger-can-interfaces/can_v3.md#Charge_Status_Change) | Always on |

The rest of the page is one section per row, in that order.

{{ figure('assets/integration-overview.svg', 'What the ADM-CS-SECC owns, what you provide, and the interfaces that cross between') }}

Whatever else you choose, these are **always** required:

| You must provide | Why | Where |
|---|---|---|
| Supply, and a cabinet | See the specification sheet for current | [Power input](interfaces.md#power-input) |
| Connector harness: CP, PP, lock, temperature, PLC | Fully driven by the communication stack — you only wire it | [CCS and AC interfaces](interfaces.md#ccs-and-ac-interfaces) |
| Output contactors, driven by the controller's relays | Hard-wired safety layer; they can only be energised when the standard's conditions are met | [§5](#5-output-contactors-and-cabinet-safety) |
| Power module control — yours or a supported interface | The controller does not convert power | [§4](#4-power-modules-the-central-choice) |
| Present voltage, present current and insulation resistance | The controller runs precharge, the insulation test and the current loop against these | [§4](#4-power-modules-the-central-choice), [§6](#6-insulation-monitoring) |
| Per-pistol limits (`min/max_charger_voltage`, `min/max_charger_current`, [`max_charger_power`](configuration/pistol-ccs-dc.md#max_charger_power)) | Everything the controller advertises to the vehicle comes from these | [Configuration → Pistols](configuration/pistols.md) |

!!! tip "You do not need a real vehicle to develop against"
    You are building a charger, so what you need on the bench is **a vehicle**. An ADVANTICS vehicle
    controller (ADM-CS-EVCC for CCS, ADM-CS-MEVC for MCS) running the **[vehicle simulator](https://documentation.advantics.fr/adm-cs-evcc/vehicle-features/vehicle-simulation.html)** is exactly that: it
    requests power and follows the sequence as a car's BMS would, against a simulated battery.
    Simulated power is enough to validate the sequence, which is the part that takes the time.

    Its parameters exist to let you force the branches you would otherwise wait months to meet: a
    nearly full pack, a vehicle asking for more than you can deliver, slow contactors, a
    vehicle-initiated stop, an emergency stop, a whole session compressed into seconds. Test those
    before HV, not after.

    A **connection box** completes the bench: it powers the charge controller and simulates the inlet
    and the charge pistol with their integrated resistances, so you do not need a real inlet and cable
    to plug into.

    The mirror-image tool, the **[charger simulator](charger-features/charger-simulation.md)**, runs on
    *this* controller and stands in for the charger components you have not built or wired yet — switch off
    the CAN messages sent by the simulator one at a time as your own software starts sending them.

    !!! warning "Not part of the standard software stack"
        The simulators are purchased separately — contact
        [sales@advantics.fr](mailto:sales@advantics.fr)

## 2. Pistols: one section per connector

A "pistol" is one vehicle-facing connector. Each gets its own `[pistol:…]` section — for example
`[pistol:CCS DC]` — holding its [`index`](configuration/pistol-ccs-dc.md#index), its electrical limits, its protocol options and **its
power module interface**. A charger with two outlets has two sections.

| Choice | Entry |
|---|---|
| Electrical envelope advertised to the vehicle | [`min_charger_voltage`](configuration/pistol-ccs-dc.md#min_charger_voltage), [`max_charger_voltage`](configuration/pistol-ccs-dc.md#max_charger_voltage), [`min_charger_current`](configuration/pistol-ccs-dc.md#min_charger_current), [`max_charger_current`](configuration/pistol-ccs-dc.md#max_charger_current), [`max_charger_power`](configuration/pistol-ccs-dc.md#max_charger_power) |
| Protocols offered, and their order | [`enable_din`](configuration/pistol-ccs-dc.md#enable_din), [`enable_iso_part2`](configuration/pistol-ccs-dc.md#enable_iso_part2), `protocol_priority_order` |
| Which inlet pins carry DC | `energy_transfer_type` |
| Charge point identity, free vs paid | [`evse_id`](configuration/pistol-ccs-dc.md#evse_id), [`free_service`](configuration/pistol-ccs-dc.md#free_service) |
| Skip the cable check (bench testing) | [`skip_cable_check`](configuration/pistol-ccs-dc.md#skip_cable_check) |
| Insulation monitor model | [`insulation_monitor_type`](configuration/pistol-ccs-dc.md#insulation_monitor_type) — see [§6](#6-insulation-monitoring) |
| Power module interface | [`charger_type`](configuration/pistol-ccs-dc.md#charger_type) — see [§4](#4-power-modules-the-central-choice) |

All of them are described in [Configuration → Pistols](configuration/pistols.md). Applications
to run and hardware assignments live in [Applications](configuration/generalities.md#applications) and
[Hardware](configuration/generalities.md#hardware).

## 3. The charger CAN bus

One CAN bus carries the generic charger interface between the controller and your power stage.
Direction below is **from the controller's point of view**: `OUT` is sent by the controller, `IN` is
what the controller expects from the power modules.

### 3.1 What the controller sends your power stage

| Message | ID | Purpose |
|---|---|---|
| [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status) | 0x6b000 | Where the controller is in the sequence. Sent as soon as the application runs |
| [New_Charge_Session](charger-can-interfaces/can_v3.md#New_Charge_Session) | 0x6b001 | A vehicle is plugged in and its parameters are known — wake the power modules |
| [DC_Power_Control](charger-can-interfaces/can_v3.md#DC_Power_Control) | 0x6b003 | The core of a session: power function, setpoints or ranges, setpoint mode, contactor and voltage-lowering commands |
| [Charge_Status_Change](charger-can-interfaces/can_v3.md#Charge_Status_Change) | 0x6b002 | A step in the charging procedure changed |
| [Charge_Session_Finished](charger-can-interfaces/can_v3.md#Charge_Session_Finished) | 0x6b004 | Session over, the vehicle will unplug |
| [Emergency_Stop](charger-can-interfaces/can_v3.md#Emergency_Stop) | 0x6b005 | Emergency stop is active |
| [EV_Information_*](charger-can-interfaces/can_v3.md#EV_Information_Battery) | 0x6b100–0x6b104 | What the vehicle reported: battery, voltages, charge and discharge limits, energy |
| [ADM_CS_SECC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Inputs) | 0x6b201 | The controller's own digital inputs and temperature channels |
| [CCS_Extra_Information](charger-can-interfaces/can_v3.md#CCS_Extra_Information) | 0x6b203 | Protocol detail, for information |
| [OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control) | 0x6b300 | Backend information needed for power transfer |

### 3.2 What your power stage must send the controller

| Message | ID | Needed when | Carries |
|---|---|---|---|
| [Power_Modules_Status](charger-can-interfaces/can_v3.md#Power_Modules_Status) | 0x63000 | **Always, continuously** | Present voltage and current, insulation resistance, system enable, faults |
| [DC_Power_Parameters](charger-can-interfaces/can_v3.md#DC_Power_Parameters) | 0x63001 | To narrow limits at runtime | Dynamic limits and forced setpoints |
| [Sequence_Control](charger-can-interfaces/can_v3.md#Sequence_Control) | 0x63002 | When [`use_sequence_flags`](configuration/pistol-ccs-dc.md#use_sequence_flags) is on | Flags gating the charge sequence |
| [ADM_CS_SECC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Outputs) | 0x63201 | Only to drive the controller's outputs | See [§7](#7-digital-io-leds-and-fans) |

`Power_Modules_Status` is the one message you cannot skip: the controller waits for it after
`New_Charge_Session`, and its `Present_Voltage`, `Insulation_Resistance` and `System_Enable` signals
drive the insulation test, precharge and the power transfer loop.

!!! tip "Read these next"
    [Sequences of action](charger-can-interfaces/sequences_v3.md) gives the exact order of events and
    [Charge sequence diagram](charger-can-interfaces/charge-sequence-diagram_v3.md) shows a full
    session. The database is on [CAN databases](charger-can-interfaces/databases_v3.md) as `.kcd`
    and `.dbc` — import it rather than typing signal layouts by hand.

## 4. Power modules: the central choice

You can either implement the generic interface above yourself, or select a **pre-defined charger
interface** and let the controller speak your power modules' own protocol. The second option removes
the translation layer you would otherwise have to write and maintain.

| [`charger_type`](configuration/pistol-ccs-dc.md#charger_type) | What it controls | Extra entries |
|---|---|---|
| `Advantics_Generic_DC_v3` | **Your** power stage, over the generic interface of [§3](#3-the-charger-can-bus) | — |
| `Advantics_ADS_PC_BPUD` | ADVANTICS 3-phase unidirectional charger: ADM-PC-LF45 filter + ADM-PC-BP25 PFC + ADM-PC-LL25 DC/DC | [`stack_pos`](configuration/pistol-ccs-dc.md#stack_pos) |
| `Advantics_ADM_PC_BP25_BoostBuck` | ADM-PC-BP25 in boost-buck (or buck-only) bidirectional configuration | `boost_buck_mode`, `boost_buck_max_current`, `precharge_min_current`, [`stack_pos`](configuration/pistol-ccs-dc.md#stack_pos) |
| `Maxwell_MXR` | Maxwell MXR100040 modules | `protocol`, `ptp`, `dest_address`, `src_address`, `group` |

All of them are configured **inside the pistol's section**, not globally. Parallel stacking is
supported: give [`stack_pos`](configuration/pistol-ccs-dc.md#stack_pos) a comma- or space-separated list, where stack `0` is the one connected
directly to the charger output. Details, wiring diagrams and the stack-position rules are in
[Charger interfaces](charger-features/charger_interfaces.md).

!!! warning "Insulation resistance is still yours to provide"
    With the boost-buck and Maxwell interfaces the controller does not read your insulation monitor.
    Feed the measured value into
    [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance)
    or the insulation test cannot pass.

## 5. Output contactors and cabinet safety

Three independent relays (normally-open and common contacts, 5 A / 30 V) are **hard-wired one per
interface** — AC, CCS and CHAdeMO. They are a safety layer, not general-purpose outputs: they can
only be energised when the conditions of the relevant standard are met, such as the CP state for
CCS or the PERMIT signal for CHAdeMO. They cannot be repurposed, and if you do not need them they
can be left unused. See [Output contactor control](interfaces.md#output-contactor-control).

You may wire the relay output through further relays controlled by your power modules for an extra
protection layer, but the interlock line below is the better tool for that.

| Safety input | Behaviour | Use it for |
|---|---|---|
| [Interlock](interfaces.md#interlock) | Open-collector, 4.7 kΩ pull-up to 24 V, bidirectional. **Hard-wired: it overrides software** and guarantees the output contactors open | Power module fault, cabinet door — anything that must stop power irrespective of software |
| [Current loop](interfaces.md#current-loop) | 20 mA chain that can be monitored and interrupted. **Not** hard-wired to the contactors | External E-STOP button and door switches — the preferred way to stop *cleanly* |

!!! tip "Which one for an E-STOP?"
    The current loop. The interlock stops power abruptly; the current loop lets the controller end
    the session in an orderly way. Use the interlock for faults that must not depend on software.

## 6. Insulation monitoring

Two ways to satisfy the insulation test:

- **A supported insulation monitor**, named in the pistol's [`insulation_monitor_type`](configuration/pistol-ccs-dc.md#insulation_monitor_type) (for example
  `BenderISOCHA425HV`), which the controller reads directly. Models and wiring are listed in
  [Supported Insulation Monitors](charger-features/evse-supported-insulation-monitors.md).
- **Your own measurement**, reported in
  [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance).

Set `insulation_monitor_type = Not_Used` when you report the value yourself.

## 7. Digital IO, LEDs and fans

Digital inputs and outputs are assigned functions in
[Hardware](configuration/generalities.md#hardware) — for example `dig_in1 = CHAdeMO_Start`, `dig_in2 = Stop`,
`dig_in3 = Monitor`. The electrical detail is in
[Digital inputs and outputs](interfaces.md#digital-inputs-and-outputs), with
[LED outputs](interfaces.md#led-outputs) and [Fan outputs](interfaces.md#fan-outputs) alongside.

From system version 4.x the IO can be used over the CAN bus instead: set an output to
`CAN_Controlled` and drive it with
[ADM_CS_SECC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Outputs), and read inputs from
[ADM_CS_SECC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SECC_Inputs). See
[IOs on CAN](charger-features/secc_can_ios.md). For direct access from your own software on the
controller, see [Manual GPIO control](buildroot-system/gpios.md).

[RS-485](interfaces.md#rs-485) and [4G connectivity](interfaces.md#4g-network-connectivity) are also
available.

## 8. Backend connectivity

| Need | Where |
|---|---|
| OCPP 1.6J | [OCPP 1.6J](charger-features/ocpp16j.md) |
| OCPP 2.0.1 | [OCPP 2.0.1](charger-features/ocpp201.md) |
| Enable and point at your CSMS | [OCPP Configuration](configuration/ocpp.md) — `enabled`, [`connection_url`](configuration/ocpp.md#connection_url) |
| Plug & Charge, certificates, TLS | [TLS configuration](configuration/tls.md) for the entries and the certificates to provision; [Plug'n'Charge overview](charger-features/tls_pnc/pnc_primer.md) for what the certificates are and how the roles relate |

Backend-driven limits reach the power stage through
[OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control).

## 9. AC charging, and bidirectional

- **AC**: the controller can operate an AC outlet as well — see
  [AC charging](charger-can-interfaces/secc_ac_charging.md).
- **Bidirectional / V2G**: see [V2G](charger-can-interfaces/secc_bidirectional.md), and use the
  discharge limits in the pistol section plus the `EV_Information_Discharge_Limits` message.
- **Climate control** of the cabinet: [Climate control](charger-features/secc_climate_control.md).

## 10. Diagnostics

| Source | Use |
|---|---|
| [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status) | Where the controller is in the sequence — the first thing to watch |
| [Charge_Status_Change](charger-can-interfaces/can_v3.md#Charge_Status_Change) | Why the procedure moved on |
| [EV_Information_*](charger-can-interfaces/can_v3.md#EV_Information_Battery) | What the vehicle actually asked for |
| [Debugging](buildroot-system/debugging.md) | Logs on the controller |
| [Web UI Access](advos-yocto-system/csm-web-ui.md) | Status, logs and configuration from a browser |
| [Charger simulator](charger-features/charger-simulation.md) | Run a session with a simulated power stack, and hand messages over to your own code one at a time |

<!-- ## 11. Bringing it up, in order

1. Read [Interfaces](interfaces.md) and wire power, the connector harness, the CAN bus, the
   contactor relays, the interlock and the current loop.
2. Configure one pistol: limits, protocols, [`evse_id`](configuration/pistol-ccs-dc.md#evse_id), and [`charger_type`](configuration/pistol-ccs-dc.md#charger_type). See
   [Configuration](configuration/README.md).
3. If you are writing the power module side, get `Power_Modules_Status` on the bus **before**
   anything else, then follow [Sequences of action](charger-can-interfaces/sequences_v3.md).
4. Prove the safety chain deliberately: trip the interlock and confirm the contactors open; break
   the current loop and confirm a clean stop.
5. Run a session with the [charger simulator](charger-features/charger-simulation.md) standing in for
   the power stack, then hand its messages over to your own software one at a time, then charge a
   real vehicle — watching
   [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status).
6. Add the backend last: OCPP, then Plug & Charge if you need it.
7. Work through the [Deployment Checklist](buildroot-system/must-do-before-deploy.md) before
   shipping. -->

## 12. Frequently hit questions

**The session stops before the insulation test.** The controller is waiting for
`Power_Modules_Status`. See [§4](#4-power-modules-the-central-choice).

**The output contactors never close.** They are hard-wired: check the interlock line, then the
protocol condition (CP state for CCS, PERMIT for CHAdeMO). Software cannot override either. See
[§5](#5-output-contactors-and-cabinet-safety).

**The CCS session never starts, or drops at random.** Check the CP and its return path PE, make sure they are a twisted pair, routed away from any switching noise. Avoid ground loops and unnecessary long paths.

**Can I run two CCS connectors with one SECC?** No. The SECC serves 1x CCS + 1x CHAdeMO + 1x AC pistol in parallel. 
