# Integration Guide

This page is the single starting point for integrating the ADM-CS-SPCC into a charger. It walks
through **every system the controller talks to** — power modules, output contactors, the vehicle
connector, the insulation monitor, your backend — and for each one lists **all the ways you can wire
it**, together with the configuration entry that selects between them.

Read it once from top to bottom before you wire anything: one choice in particular (which power
module interface you use) decides whether you write any software at all.

!!! info "Who this is for"
    Charger builders using the single-pistol controller — typically an **MCS** charger, though CCS
    DC, CCS AC and CHAdeMO are also supported. It assumes you own the power stage, the cabinet and
    the harness. For the pinout itself see [Interfaces](interfaces.md); this guide tells you *what
    to connect and why*.

!!! note "Which generic interface this guide assumes"
    The message names and IDs below are those of **generic interface v3**. A controller configured
    for v2 (`charger_type` = `Advantics_Generic_DC_v2`) uses the v2 database instead — its own
    reference is under *CAN bus Interfaces → Generic interface v2* in the navigation.

## 1. What the controller does, and what it needs from you

The ADM-CS-SPCC owns the vehicle-facing side of the charger: the connector, the charging protocol
and the charge sequence. It does **not** convert power. It tells your power stage what to produce,
and expects to be told what the power stage is actually doing.

One pistol is active at a time — that is what "single pistol controller" means. See
[Pistols](configuration/pistols.md).

Everything below is a **choice**. For each system the controller touches you can use its
dedicated hardware interface, or the CAN bus, and one configuration entry decides which:

| Subsystem | Dedicated hardware interface | Over the CAN bus | Selected by |
|---|---|---|---|
| **Power stage** ([§4](#4-power-modules-the-central-choice)) | — | The generic interface you implement, **or** a supported charger interface the controller speaks natively | [`charger_type`](configuration/pistol-mcs.md#charger_type) in the pistol's section |
| **Output contactors** ([§5](#5-output-contactors-and-cabinet-safety)) | `CONTACTOR_ENABLE`, with its conditions enforced in hardware | [DC_Power_Control](charger-can-interfaces/can_v3.md#DC_Power_Control) commands the sequence | — always hardware |
| **Cabinet safety** ([§5](#5-output-contactors-and-cabinet-safety)) | [Interlock](interfaces.md#interlock) line and [current loop](interfaces.md#current-loop) | — hard-wired, overrides software | — always hardware |
| **Insulation resistance** ([§6](#6-insulation-monitoring)) | A supported insulation monitor the controller reads itself | [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance) | The pistol's insulation monitor setting |
| **Present voltage & current** ([§3](#3-the-charger-can-bus)) | — | [Power_Modules_Status](charger-can-interfaces/can_v3.md#Power_Modules_Status) | — always CAN |
| **Digital IO, LEDs** ([§7](#7-digital-io-and-leds)) | Functions on `dig_inN` / `dig_outN` | [ADM_CS_SPCC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Inputs) / [ADM_CS_SPCC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Outputs) | `dig_outN = CAN_Controlled` |
| **Backend** ([§8](#8-backend-connectivity)) | Ethernet | Backend limits arrive as [OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control) | [OCPP configuration](configuration/ocpp.md) |
| **Diagnostics** ([§10](#10-diagnostics)) | — | [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status), [Charge_Status_Change](charger-can-interfaces/can_v3.md#Charge_Status_Change) | Always on |

The rest of the page is one section per row, in that order.

{{ figure('assets/integration-overview.svg', 'What the ADM-CS-SPCC owns, what you provide, and the interfaces that cross between') }}

Whatever else you choose, these are **always** required:

| You must provide | Why | Where |
|---|---|---|
| Supply, and a cabinet | See the specification sheet for current | [Power input](interfaces.md#power-input) |
| Connector harness: CE/ID (MCS) or CP/PP (CCS), lock, temperature, 10BASE-T1S or PLC | Fully driven by the communication stack — you only wire it | [MCS interface](interfaces.md#mcs-interface), [CCS and AC interfaces](interfaces.md#ccs-and-ac-interfaces) |
| Output contactors driven from `CONTACTOR_ENABLE` | Its conditions are hard-wired; software alone cannot close them | [§5](#5-output-contactors-and-cabinet-safety) |
| Power module control — yours or a supported interface | The controller does not convert power | [§4](#4-power-modules-the-central-choice) |
| Present voltage, present current and insulation resistance | The controller runs precharge, the insulation test and the current loop against these | [§4](#4-power-modules-the-central-choice), [§6](#6-insulation-monitoring) |
| Charge and cable limits for the active pistol | Everything the controller advertises to the vehicle comes from these | [Configuration](configuration/README.md) |

!!! tip "You do not need a real vehicle to develop against"
    You are building a charger, so what you need on the bench is **a vehicle**. An ADVANTICS vehicle
    controller (ADM-CS-EVCC for CCS, ADM-CS-MEVC for MCS) running the **vehicle simulator** is exactly that: it
    requests power and follows the sequence as a car's BMS would, against a simulated battery.
    Simulated power is enough to validate the sequence, which is the part that takes the time. It is
    documented on those products' sites, under *Features → Vehicle simulator*.

    Its parameters exist to let you force the branches you would otherwise wait months to meet: a
    nearly full pack, a vehicle asking for more than you can deliver, slow contactors, a
    vehicle-initiated stop, an emergency stop, a whole session compressed into seconds. Test those
    before HV, not after.

    A **connection box** completes the bench: it powers the charge controller and simulates the inlet
    and the charge pistol with their integrated resistances, so you do not need a real inlet and cable
    to plug into.

    The mirror-image tool, the **[charger simulator](charger-features/charger-simulation.md)**, runs on
    *this* controller and stands in for the power stage you have not built or wired yet — switch off
    `Power_Modules_Status`, `DC_Power_Parameters` or `Sequence_Control` one at a time as your own
    software starts sending them. That is the documented way to bring up a partial implementation of
    the generic interface.

    !!! warning "Not part of the standard software stack"
        The simulators are purchased separately — contact
        [sales@advantics.fr](mailto:sales@advantics.fr). When only one side is simulated, make sure the
        real controller on the other side is configured to deliver no power.

## 2. The active pistol

Exactly one pistol is enabled. Each type has its own configuration block, and they are all
documented on one page:

| Pistol | Configuration |
|---|---|
| MCS (default) | [MCS Pistol](configuration/pistol-mcs.md) |
| CCS DC | [CCS DC Pistol](configuration/pistol-ccs-dc.md) |
| CCS AC | [CCS AC Pistol](configuration/pistol-ccs-ac.md) |
| CHAdeMO | [CHAdeMO Pistol](configuration/pistol-chademo.md) |

Each block holds the same families of settings: [`index`](configuration/pistol-mcs.md#index), the **CAN Bus** group (including
[`charger_type`](configuration/pistol-mcs.md#charger_type) and the `Power_Modules_Status` reception timeout), **Charge Limits**, **Discharge
Limits**, **Cable Limits**, **Bidirectional Charging Extra Parameters**, and **Specific Charger
Interface Extra Parameters** — the last being where a supported power module interface is tuned.

Configuration is done through the [Web UI](advos-yocto-system/csm-web-ui.md), or by editing
`/etc/advantics/default/config.cfg` over [SSH](advos-yocto-system/ssh.md).

### 2.1 MCS: CE and ID lines

MCS carries high-level communication over **10BASE-T1S** and uses **CE** (Charge Enable) and **ID**
lines rather than CP and PP. Both are sampled continuously and can be disturbed by noise, so the MCS
pistol exposes filtering:

| Concern | Entry |
|---|---|
| Median filter on CE/ID | [mcs_ce_id_use_median_filter](configuration/pistol-mcs.md#mcs_ce_id_use_median_filter), [mcs_ce_id_filter_buffer_size](configuration/pistol-mcs.md#mcs_ce_id_filter_buffer_size) |
| Debouncing | [mcs_ce_id_use_debouncer](configuration/pistol-mcs.md#mcs_ce_id_use_debouncer), [mcs_ce_id_debouncer_count](configuration/pistol-mcs.md#mcs_ce_id_debouncer_count) |

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
| [ADM_CS_SPCC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Inputs) | 0x6b202 | The controller's own digital inputs and temperature channels |
| [MCS_Extra_Information](charger-can-interfaces/can_v3.md#MCS_Extra_Information) | 0x6b204 | MCS protocol detail, for information |
| [OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control) | 0x6b300 | Backend information needed for power transfer |

### 3.2 What your power stage must send the controller

| Message | ID | Needed when | Carries |
|---|---|---|---|
| [Power_Modules_Status](charger-can-interfaces/can_v3.md#Power_Modules_Status) | 0x63000 | **Always, continuously** | Present voltage and current, insulation resistance, system enable, faults |
| [DC_Power_Parameters](charger-can-interfaces/can_v3.md#DC_Power_Parameters) | 0x63001 | To narrow limits at runtime | Dynamic limits and forced setpoints |
| [Sequence_Control](charger-can-interfaces/can_v3.md#Sequence_Control) | 0x63002 | When [`use_sequence_flags`](configuration/pistol-mcs.md#use_sequence_flags) is on | Flags gating the charge sequence |
| [ADM_CS_SPCC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Outputs) | 0x63202 | Only to drive the controller's outputs | See [§7](#7-digital-io-and-leds) |

`Power_Modules_Status` is the one message you cannot skip: the controller waits for it after
`New_Charge_Session`, its `Present_Voltage`, `Insulation_Resistance` and `System_Enable` signals
drive the insulation test, precharge and the power transfer loop, and losing it for longer than the
pistol's [`charger_can_timeout_ms`](configuration/pistol-mcs.md#charger_can_timeout_ms) is a fault.

!!! tip "Read these next"
    [Sequences of action](charger-can-interfaces/sequences_v3.md) gives the exact order of events and
    [Charge sequence diagram](charger-can-interfaces/charge-sequence-diagram_v3.md) shows a full
    session. The database is on [CAN databases](charger-can-interfaces/databases_v3.md) as `.kcd`
    and `.dbc` — import it rather than typing signal layouts by hand.

## 4. Power modules: the central choice

You can either implement the generic interface above yourself, or select a **pre-defined charger
interface** and let the controller speak your power modules' own protocol. The second option removes
the translation layer you would otherwise have to write and maintain.

| [`charger_type`](configuration/pistol-mcs.md#charger_type) | What it controls | Extra entries |
|---|---|---|
| `Advantics_Generic_DC_v3` | **Your** power stage, over the generic interface of [§3](#3-the-charger-can-bus) | — |
| `Advantics_ADS_PC_BPUD` | ADVANTICS 3-phase unidirectional charger: ADM-PC-LF45 filter + ADM-PC-BP25 PFC + ADM-PC-LL25 DC/DC | [`stack_pos`](configuration/pistol-mcs.md#stack_pos) |
| `Advantics_ADM_PC_BP25_BoostBuck` | ADM-PC-BP25 in boost-buck (or buck-only) bidirectional configuration | `boost_buck_mode`, `boost_buck_max_current`, `precharge_min_current`, [`stack_pos`](configuration/pistol-mcs.md#stack_pos) |
| `Maxwell_MXR` | Maxwell MXR100040 modules | `protocol`, `ptp`, `dest_address`, `src_address`, `group` |

These live in the pistol's **Specific Charger Interface Extra Parameters** group. Parallel stacking is
supported: give [`stack_pos`](configuration/pistol-mcs.md#stack_pos) a comma- or space-separated list, where stack `0` is the one connected
directly to the charger output. Details, wiring diagrams and the stack-position rules are in
[Charger interfaces](charger-features/charger_interfaces.md); the CAN bitrate is set as described in
[CAN Interface System Configuration](advos-yocto-system/can-bus-configuration.md).

!!! warning "Insulation resistance is still yours to provide"
    With the boost-buck and Maxwell interfaces the controller does not read your insulation monitor.
    Feed the measured value into
    [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance)
    or the insulation test cannot pass.

## 5. Output contactors and cabinet safety

`CONTACTOR_ENABLE` goes to logic level 0 only when **all** of the following hold — this is a
hard-wired chain, so software alone can never close the contactors:

1. The protocol says power is allowed: **CE state C** for MCS, **CP state C** for CCS, or the
   **PERM** line for CHAdeMO.
2. The hardware safety conditions are met (below).
3. The charge application, or you, requested closing.

The [hardware safety conditions](interfaces.md#hw-safety-conditions) are:

- no interlock line trip;
- `CLOOP_OUT` connected to `CLOOP_IN`;
- no over-temperature — `PT1KS_C` and `PT1KS_D` must either be **connected to GND when not in use**,
  or read below 110 °C.

!!! tip "A very common bring-up trap"
    Unused PT1K inputs left floating read as over-temperature and silently prevent the contactors
    from closing. Ground them.

| Safety input | Behaviour | Use it for |
|---|---|---|
| [Interlock](interfaces.md#interlock) | Open-collector, 4.7 kΩ pull-up to 24 V, bidirectional. **Hard-wired: it overrides software** and guarantees the output contactors open | Power module fault, cabinet door — anything that must stop power irrespective of software |
| [Current loop](interfaces.md#current-loop) | 20 mA chain that can be monitored and interrupted. **Not** hard-wired to the contactors | External E-STOP button and door switches — the preferred way to stop *cleanly* |

Full detail: [Output contactor control](interfaces.md#output-contactor-control).

## 6. Insulation monitoring

Two ways to satisfy the insulation test:

- **A supported insulation monitor**, named in the pistol's insulation monitor setting, which the
  controller reads directly. Models and wiring are listed in
  [Supported Insulation Monitors](charger-features/evse-supported-insulation-monitors.md).
- **Your own measurement**, reported in
  [Power_Modules_Status.Insulation_Resistance](charger-can-interfaces/can_v3.md#Power_Modules_Status-Insulation_Resistance).

## 7. Digital IO and LEDs

Digital inputs and outputs are assigned functions in
[Hardware](configuration/generalities.md#hardware); the electrical detail is in
[Digital inputs and outputs](interfaces.md#digital-inputs-and-outputs), with
[LED outputs](interfaces.md#led-outputs) and
[Temperature Sensors Inputs](interfaces.md#temperature-sensors-inputs) alongside.

The IO can also be used over the CAN bus: set an output to `CAN_Controlled` and drive it with
[ADM_CS_SPCC_Outputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Outputs), and read inputs from
[ADM_CS_SPCC_Inputs](charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Inputs). See
[IOs on CAN](charger-features/secc_can_ios.md).

[RS-485](interfaces.md#rs-485) is available for serial peripherals such as insulation monitors.

## 8. Backend connectivity

| Need | Where |
|---|---|
| OCPP 1.6J | [OCPP 1.6J](charger-features/ocpp16j.md) |
| OCPP 2.0.1 | [OCPP 2.0.1](charger-features/ocpp201.md) |
| Enable and point at your CSMS | [OCPP configuration](configuration/ocpp.md) — including Core, Local Auth, Reservation and Smart Charging groups |
| Plug & Charge, certificates, TLS | [TLS configuration](configuration/tls.md) for the entries and the certificates to provision; [Plug'n'Charge overview](charger-features/tls_pnc/pnc_primer.md) for what the certificates are and how the roles relate |

Backend-driven limits reach the power stage through
[OCPP_Control](charger-can-interfaces/can_v3.md#OCPP_Control).

## 9. AC charging, and bidirectional

- **AC**: the controller can operate an AC outlet as well — see
  [AC charging](charger-can-interfaces/secc_ac_charging.md) and the
  [CCS AC Pistol](configuration/pistol-ccs-ac.md) settings, which include its own lock
  parameters.
- **Bidirectional / V2G**: see [V2G](charger-can-interfaces/secc_bidirectional.md), the pistol's
  Discharge Limits and Bidirectional Charging Extra Parameters, and the
  `EV_Information_Discharge_Limits` message.
- **Cabinet climate control**: [Climate control](charger-features/secc_climate_control.md) and the
  [Temperature](configuration/temperature.md) settings.

## 10. Diagnostics

| Source | Use |
|---|---|
| [Advantics_Controller_Status](charger-can-interfaces/can_v3.md#Advantics_Controller_Status) | Where the controller is in the sequence — the first thing to watch |
| [Charge_Status_Change](charger-can-interfaces/can_v3.md#Charge_Status_Change) | Why the procedure moved on |
| [EV_Information_*](charger-can-interfaces/can_v3.md#EV_Information_Battery) | What the vehicle actually asked for |
| [Web UI Access](advos-yocto-system/csm-web-ui.md) | Status, logs and configuration from a browser |
| [Connecting to the SPCC](advos-yocto-system/connecting.md) / [SSH access](advos-yocto-system/ssh.md) | Shell access for logs; also available [over 10BASE-T1S](advos-yocto-system/ssh-10base-t1s.md) |
| [Charger simulator](charger-features/charger-simulation.md) | Run a session with a simulated power stack, and hand messages over to your own code one at a time |

## 11. Bringing it up, in order

1. Read [Interfaces](interfaces.md) and wire power, the connector harness, the CAN bus,
   `CONTACTOR_ENABLE`, the interlock and the current loop. **Ground unused PT1K inputs.**
2. Enable and configure the pistol you are using: limits, [`charger_type`](configuration/pistol-mcs.md#charger_type), and the CAN bus group. See
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
7. Work through the [Deployment Checklist](advos-yocto-system/must-do-before-deploy.md) before
   shipping.

## 12. Frequently hit questions

**The output contactors never close.** Work down the chain in [§5](#5-output-contactors-and-cabinet-safety):
unused PT1K inputs left floating, the current loop not closed, the interlock tripped, or the protocol
condition (CE/CP state C, or PERM) not met. Software cannot override any of them.

**The session stops before the insulation test.** The controller is waiting for
`Power_Modules_Status`, or for a plausible `Insulation_Resistance` in it. See
[§4](#4-power-modules-the-central-choice) and [§6](#6-insulation-monitoring).

**The MCS session never starts, or drops at random.** Check the CE and ID lines first, and consider
the median filter and debouncer in [§2.1](#21-mcs-ce-and-id-lines).

**Do I have to write power module software?** Not if your stage is one of the supported
architectures in [§4](#4-power-modules-the-central-choice) — pick the [`charger_type`](configuration/pistol-mcs.md#charger_type) and configure
[`stack_pos`](configuration/pistol-mcs.md#stack_pos).

**Can I run two connectors?** No. The SPCC serves one pistol at a time. A charger with several
outlets needs a multi-pistol charge station controller — ask ADVANTICS which variant fits.

**Interlock or current loop for my E-STOP?** Current loop — it stops the session cleanly. The
interlock is for faults that must bypass software entirely.
