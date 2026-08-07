# Integration Guide

This page is the starting point for integrating the ADM-CS-EVCC into a vehicle. It walks
through **every system the controller talks to**, and for each one lists **all the ways you can
wire it** — a dedicated hardware interface, the CAN bus, or a mix — together with the configuration
entry that selects between them.

Read it once from top to bottom before you wire anything: several choices (who owns the DC
contactors, who measures the inlet voltage) change what you have to build.

!!! info "Who this is for"
    Vehicle integrators of a **CCS** (Combined Charging System) vehicle — typically a car, a van, a
    bus, and etc. It assumes you are responsible for the VCU/BMS side and the wiring harness. For
    the pinout itself see [Interfaces](interfaces.md); this guide tells you *what to connect and
    why*.

## 1. What the controller does, and what it needs from you

The ADM-CS-EVCC owns the charge inlet and the charging protocols (DIN 70121, ISO 15118-2,
ISO 15118-20), and exposes the whole charge process to the rest of the vehicle as CAN bus interface.
It cannot function on its own: the vehicle must supply a few measurements and a small amount of
decision-making.

Everything below is a **choice**. For each system the controller touches you can use its
dedicated hardware interface, or the CAN bus, and one configuration entry decides which:

<!-- | Subsystem | Dedicated hardware interface | Over the CAN bus | Selected by |
|---|---|---|---|
| **DC contactors** ([§4](#4-dc-contactor-control)) | H-bridge outputs, plus feedback inputs | [DC_Control.Close_Contactors](vehicle-can-interfaces/can_v2.md#DC_Control-Close_Contactors) and [DC_Status2.Contactors_Closed](vehicle-can-interfaces/can_v2.md#DC_Status2-Contactors_Closed) | [dc_contactors_use_ios](configuration/dc_contactors.md#dc_contactors_use_ios), [dc_contactors_ios_has_feedback](configuration/dc_contactors.md#dc_contactors_ios_has_feedback) |
| **Inlet & battery voltage, current** ([§5](#5-voltage-and-current-measurement)) | A supported CAN sensor the controller reads itself | [DC_Status1](vehicle-can-interfaces/can_v2.md#dc_status1) / [DC_Status2](vehicle-can-interfaces/can_v2.md#dc_status2) from your BMS | [use_can_sensor](configuration/can_sensor.md), [no_bms](configuration/no_bms.md) |
| **Inlet lock** ([§6](#6-inlet-lock)) | Lock motor drive and resistive feedback | — hardware only | [no_inlet_lock](configuration/inlet_lock.md#no_inlet_lock) disables it for bench tests |
| **Digital inputs** ([§7](#7-digital-inputs-outputs-and-leds)) | `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` on `dig_inN` | Reported in [ADM_CS_EVCC_Inputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_inputs) | `[hardware] dig_inN` |
| **Digital outputs, LEDs** ([§7](#7-digital-inputs-outputs-and-leds)) | `Plugged_In`, `Contactor_Enable` on `dig_outN` / `ledN` | Driven by [ADM_CS_EVCC_MEVC_Outputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_mevc_outputs) | `dig_outN = CAN_Controlled` |
| **Inlet temperature** ([§8](#8-temperature-monitoring)) | PT1000 inputs | Reported in [ADM_CS_EVCC_Inputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_inputs) | Temperature channel configuration |
| **Stopping a charge** ([§10](#10-stopping-a-charge)) | `Stop` input, or loss of CP in hardware | Over the generic interface | `[hardware] dig_inN = Stop` |
| **Diagnostics** ([§9](#9-diagnostics)) | — | [EVCC_MEVC_Diagnostic_Status](vehicle-can-interfaces/can_v2.md#evcc_mevc_diagnostic_status) | Always on |
| **Your BMS dialect** ([§2.3](#23-if-your-vehicle-speaks-j1939)) | — | Generic interface, or **SAE J1939** through the bridge | [type](configuration/generalities.md#type), `enable_j1939_bridge` |

The rest of the page is one section per row, in that order. -->

{{ figure('assets/integration-overview.svg', 'What the ADM-CS-EVCC owns, what you provide, and the interfaces that cross between') }}

Whatever else you choose, these are **always** required:

| You must provide | Why | Where |
|---|---|---|
| 12 V or 24 V supply, plus a contactor supply | The contactor drivers are powered separately so 12 V contactors can be used in a 24 V system | [Power input](interfaces.md#power-input) |
| Inlet harness: CP, PP, lock motor, PT1000 sensors | Fully driven by the communication stack — you only wire it | [CCS and AC interfaces](interfaces.md#ccs-and-ac-interfaces) |
| **Inlet** voltage, battery voltage and charge current | Required by the CCS standards, and by the controller to run precharge and to unlock safely | [§5](#5-voltage-and-current-measurement) |
| A way to open and close the DC contactors | To expose the battery to the charger during DC charging | [§4](#4-dc-contactor-control) |
| Charge parameters limits | The controller limits every request to these; example [`max_current`](configuration/generalities.md#max_current) defaults to 0 A, so charging does nothing until you set it | [Generalities](configuration/generalities.md) |
| [`energy_capacity`](configuration/generalities.md#energy_capacity) | Required to derive energy requests; mandatory when running ISO 15118-20 | [Generalities](configuration/generalities.md) |

!!! warning "Important to know"
    It is **not** sufficient to measure the HV battery voltage. The DC contactors separate the
    battery from the inlet, so battery voltage ≠ inlet voltage. Precharge, contactor closing and
    safe unlocking all depend on the **inlet** reading. See
    [Requirement for inlet monitoring](interfaces.md#requirement-for-inlet-monitoring).

!!! tip "You do not need a real charger to develop against"
    You are integrating a vehicle, so what you need on the bench is **a charger**. An ADVANTICS charge
    station controller (ADM-CS-SPCC) running the [**charger simulator**](https://documentation.advantics.fr/adm-cs-spcc/charger-features/charger-simulation.html) is exactly that:
    it answers your vehicle as a charger would and plays out the whole sequence — negotiation,
    authorisation, cable check, precharge, the current-demand loop, stopping — with the power stage
    simulated. Simulated power is enough to validate the sequence, which is the part that takes the
    time.

    Its parameters exist to let you force the branches you would otherwise wait months to meet:
    authorisation refused, slow negotiation, lazy ramps, poor insulation, a charger weaker than you
    asked for, a stop pressed mid-session, all kinds or emergency stop situations. Test those before HV, not after.

    A **connection box** completes the bench: it powers the charge controller and simulates the inlet
    and the charge pistol with their integrated resistances, so you do not need a real inlet and cable
    to plug into.

    The mirror-image tool, the **[vehicle simulator](vehicle-features/vehicle-simulation.md)**, runs on
    *this* controller and stands in for the VCU/BMS interface you have not written yet. Both let you **switch off
    individual CAN messages**, so the simulator keeps supplying what you have not implemented while
    your own code takes over one message at a time.

    !!! warning "Not part of the standard software stack"
        The simulators are purchased separately — contact
        [sales@advantics.fr](mailto:sales@advantics.fr).

## 2. The vehicle CAN bus — your main integration surface

One CAN bus is dedicated to the vehicle. Everything the controller reports, and everything it needs
from the vehicle, flows over it.

| Property | Value / entry |
|---|---|
| Bit rate | 500 kbaud by default; changing it is described in [CAN Interface System Configuration](buildroot-system/can-bus-configuration.md) |
| Termination | No 120 Ω termination by default — a DIP switch on the PCB enables it. See [Vehicle CAN bus](interfaces.md#vehicle-can-bus) |
| Interface selection | `[vehicle] type = Advantics_Generic_v2` ([type](configuration/generalities.md#type)) |
| Frame IDs | 11-bit where possible; force 29-bit with [force_extended_ids](configuration/generalities.md#force_extended_ids) |
| Loss-of-communication timeout | [can_timeout_ms](configuration/generalities.md#can_timeout_ms) — critical frames missing for longer than this during a powered phase raise a fault |
| Speaking J1939 instead | A bidirectional bridge lets your existing J1939 stack talk to the controller unchanged — see [§2.3](#23-if-your-vehicle-speaks-j1939) |

Direction in the tables below is **from the controller's point of view**: `OUT` is sent by the
controller, `IN` is what the controller expects from the vehicle.

### 2.1 What the controller sends you

| Message | ID | Purpose |
|---|---|---|
| [EVSE_Information](vehicle-can-interfaces/can_v2.md#evse_information) | 0x600 | Charger state and capabilities; carries [Communication_Stage](vehicle-can-interfaces/can_v2.md#EVSE_Information-Communication_Stage), the single most useful signal for your state machine |
| [AC_Control](vehicle-can-interfaces/can_v2.md#ac_control) | 0x601 | Commands to the on-board charger during AC charging |
| [DC_Control](vehicle-can-interfaces/can_v2.md#dc_control) | 0x602 | Commands to the BMS during DC charging, including [Close_Contactors](vehicle-can-interfaces/can_v2.md#DC_Control-Close_Contactors) |
| [CCS_Extra_Information](vehicle-can-interfaces/can_v2.md#ccs_extra_information) | 0x603 | Informational CCS detail |
| [ADM_CS_EVCC_Inputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_inputs) | 0x604 | The controller's own digital inputs and temperature channels |
| [EVCC_MEVC_Diagnostic_Status](vehicle-can-interfaces/can_v2.md#evcc_mevc_diagnostic_status) | 0x605 | Active faults and errors, plus charger status received over HLC — see [§9](#9-diagnostics) |
| [MCS_Extra_Information](vehicle-can-interfaces/can_v2.md#mcs_extra_information) | 0x606 | Informational MCS detail |

### 2.2 What you send the controller

| Message | ID | Needed when | Carries |
|---|---|---|---|
| [EV_Information](vehicle-can-interfaces/can_v2.md#ev_information) | 0x610 | Always | State of charge, energy capacity |
| [AC_Status](vehicle-can-interfaces/can_v2.md#ac_status) | 0x611 | AC charging | On-board charger readiness |
| [DC_Status1](vehicle-can-interfaces/can_v2.md#dc_status1) | 0x612 | DC charging | Current/voltage requests and limits |
| [DC_Status2](vehicle-can-interfaces/can_v2.md#dc_status2) | 0x613 | DC charging | Battery and **inlet** voltage, contactor status, end-of-charge |
| [EV_Status](vehicle-can-interfaces/can_v2.md#ev_status) | 0x618 | On change | Pause/resume, HV readiness hold-off |
| [EV_Energy_Request](vehicle-can-interfaces/can_v2.md#ev_energy_request) | 0x614 | ISO 15118-20 | Target / min / max energy request |
| [EV_V2X_Energy_Request](vehicle-can-interfaces/can_v2.md#ev_v2x_energy_request) | 0x615 | Bidirectional (optional) | Preferred V2X cycling range |
| [EV_Extra_BPT_Information](vehicle-can-interfaces/can_v2.md#ev_extra_bpt_information) | 0x616 | Bidirectional | Departure time and BPT detail |
| [ADM_CS_EVCC_MEVC_Outputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_mevc_outputs) | 0x617 | Only to drive the controller's outputs | See [§7](#7-digital-inputs-outputs-and-leds) |

Some of these can be provided **by the controller instead of by you** — see
[§5](#5-voltage-and-current-measurement).

!!! tip "Read these next"
    [Sequences of action](vehicle-can-interfaces/sequences_v2.md) gives the exact order of events,
    and [Power transfer sequence diagram](vehicle-can-interfaces/power_transfer_sequence_diagram.md)
    shows a full session. The database itself is on
    [CAN databases](vehicle-can-interfaces/databases_v2.md) in `.kcd` and `.dbc` form — import it
    rather than typing signal layouts by hand.

### 2.3 If your vehicle speaks J1939

You do not have to implement the generic interface on your BMS at all. The controller can run a
**J1939 bridge** that translates the generic interface to and from SAE J1939, in both directions, so
your existing J1939 stack talks to the controller unchanged.

Internally nothing changes — the applications keep using the generic interface — the bridge is an
adapter alongside them. The recommended topology therefore moves the generic traffic onto a
**virtual** bus and leaves the physical bus to J1939 only, which avoids ID collisions and noise on
your vehicle bus:

| Setting | Value | Effect |
|---|---|---|
| `[system] enable_j1939_bridge` | `true` | Starts the bridge |
| `[vehicle] can_if` | `vcan0` | Moves the generic interface to the virtual bus, off the physical one |
| [`j1939_can_if`](configuration/j1939.md#j1939_can_if) | `can0` | Where J1939 frames are sent |
| [`device_address`](configuration/j1939.md#device_address) | 0–253 | The controller's J1939 source address |
| Default priority | 0–7 | Priority of the vendor-specific messages |
| Vendor PGN Offset | — | Shifts all vendor IDs if they collide with another device (expert mode) |

Both can also be set from the Web UI's `J1939` and `Vehicle` config tabs. Restart the applications
after changing them.

What you implement against: the bridge **mirrors** each generic message onto a vendor-specific PGN
with the **payload byte-for-byte identical** — only the identifier changes. So every signal layout in
[§2.1](#21-what-the-controller-sends-you) and [§2.2](#22-what-you-send-the-controller) still
applies, and the databases for the mirrored messages are published next to the page:
[Advantics_J1939_vendored.kcd](vehicle-can-interfaces/Advantics_J1939_vendored.kcd) and
[.dbc](vehicle-can-interfaces/Advantics_J1939_vendored.dbc).

!!! warning "Three limits to design around"
    - The bridge works with **generic interface v2 only**.
    - There is **no address claim protocol**. `device_address` is static, defaults to `0`, and you
      must pick one that does not collide with anything else on the bus.
    - Priority is **global**, not per message.

    Translation to *standardised* J1939 PGNs also exists but is a work in progress and not
    considered stable — use the vendor-specific messages exclusively.

Full description, including the bridge's place in the application topology:
[J1939](vehicle-can-interfaces/j1939.md).

## 3. Charging protocols and session behaviour

Unlike an MCS vehicle, a CCS one has a real choice of protocol. Which ones the controller offers to
the charger, and in what order of preference, is configured in the `[ccs]` section — see
[CCS/MCS configuration](configuration/ccs.md).

| Choice | Entry |
|---|---|
| Enable/disable DIN 70121, ISO 15118-2, ISO 15118-20 | [enable_din](configuration/ccs.md#enable_din), [enable_iso_part2](configuration/ccs.md#enable_iso_part2), [enable_iso_part20](configuration/ccs.md#enable_iso_part20) |
| Preference order when a charger supports several | [din_priority](configuration/ccs.md#din_priority), [iso_part2_priority](configuration/ccs.md#iso_part2_priority), [iso_part20_dc_priority](configuration/ccs.md#iso_part20_dc_priority) |
| Proximity Pilot handling (region dependent) | [pp_mode](configuration/ccs.md#pp_mode) — `B2` for EU/RoW, `B1` for North America |
| Charger current-demand timeout | [current_demand_timeout_ms](configuration/ccs.md#current_demand_timeout_ms) |

ISO 15118-20 additionally needs the **v2** generic CAN interface
(`[vehicle] type = Advantics_Generic_v2`): v1 has no messages for energy requests, dynamic limits or
bidirectional signalling.

### 3.1 TLS and Plug & Charge

| Choice | Where | Why |
|---|---|---|
| A decision about TLS | `[tls]`, `[tls:client]` and two `[ccs]` entries — see [TLS](configuration/tls.md) | ISO 15118-20 requires TLS and the vehicle is the TLS **client**. The controller nonetheless **allow disabling TLS** and with the no-TLS relaxations set, so that it charges against the chargers that exist today. Decide deliberately which of the two you are doing. |
| Plug & Charge | [TLS → Plug & Charge](configuration/tls.md#plug-charge) | Implemented for **ISO 15118-2**. It needs the V2G Root CA and your contract as a PKCS#12 file — but no client certificate, since what authenticates the vehicle is the contract |

DIN 70121 does not use TLS at all, and an ISO 15118-2 session that authorises by EIM does not either.
So TLS is a question you only have to answer if you run ISO 15118-20, or Plug & Charge, or both.

### 3.2 How the session is allowed to behave

| Choice | Entry |
|---|---|
| Which -20 control mode to ask for | [`preferred_control_mode`](configuration/ccs.md#preferred_control_mode) — `Dynamic` (default) or `Scheduled` |
| Keep cycling power at 100 % SoC in a bidirectional session | [allow_bpt_at_full_soc](configuration/ccs.md#allow_bpt_at_full_soc) in `[vehicle]` — see [§12](#12-bidirectional-power-transfer-iso-15118-20) |

[`preferred_control_mode`](configuration/ccs.md#preferred_control_mode) represents ISO 15118-20 control modes. The default is
[Dynamic Mode](vehicle-can-interfaces/sequences_v2.md#power-transfer-dynamic-mode),
where the charger decides how much power to push/pull within the limits you publish; the alternative, [Scheduled Mode](vehicle-can-interfaces/sequences_v2.md#power-transfer-scheduled-mode), follows a profile agreed up front.

### 3.3 Holding the session off until your High Voltage system is ready

A vehicle might not have its HV system ready the instant the plug is in — HV
reconnection, a BMS or other components waking from sleep, etc. Rather than have the charger start an insulation
test into a system that is not ready, the controller can hold the session at
`Connected_With_Full_Info`, which is the last stage before the powered ones.

| Choice | Entry |
|---|---|
| Always wait for the BMS before entering powered states. BMS confirms ready state by setting [EV_Status.HV_Preparing_Hold_Off](vehicle-can-interfaces/can_v2.md#EV_Status-HV_Preparing_Hold_Off) | [`hold_off_until_bms_ready`](configuration/ccs.md#hold_off_until_bms_ready) in `[ccs]` — default `false` |
| Ask for the hold dynamically, per session | [EV_Status.HV_Preparing_Hold_Off](vehicle-can-interfaces/can_v2.md#EV_Status-HV_Preparing_Hold_Off) |
| How long the hold may last before the session aborts | [wait_hv_ready_timeout_ms](configuration/ccs.md#wait_hv_ready_timeout_ms) — default 40 s |

The two are different tools. The CAN signal is the normal one: raise it while you are not ready,
clear it when you are. [`hold_off_until_bms_ready`](configuration/ccs.md#hold_off_until_bms_ready) is the belt-and-braces version — with it set, the
controller waits at that stage on *every* session until the BMS starts sending CAN messages *and*
explicitly clears the signal, which is what you want if the controller can boot before your BMS and
the rest of the vehicle does. Either way the wait is bounded by [`wait_hv_ready_timeout_ms`](configuration/ccs.md#wait_hv_ready_timeout_ms), and
hitting that bound aborts the session.

## 4. DC contactor control

This is the decision with the largest impact on your integration. The controller can drive the
contactors itself with its embedded HW interface, or it can tell you when to close and open them and
let the vehicle do it.

Refer to the [contactors interface page](interfaces.md#dc-fast-charge-contactors-control) for information on the driving capabilities and protection.

Two entries in `[vehicle]` select the combination:
[dc_contactors_use_ios](configuration/dc_contactors.md#dc_contactors_use_ios) picks who
**controls**, [dc_contactors_ios_has_feedback](configuration/dc_contactors.md#dc_contactors_ios_has_feedback)
picks where **feedback** comes from.

| [`dc_contactors_use_ios`](configuration/dc_contactors.md#dc_contactors_use_ios) | [`dc_contactors_ios_has_feedback`](configuration/dc_contactors.md#dc_contactors_ios_has_feedback) | Control | Feedback that the contactors are closed |
|---|---|---|---|
| `false` (default) | *not used* | **You** close them, on [DC_Control.Close_Contactors](vehicle-can-interfaces/can_v2.md#DC_Control-Close_Contactors) | **You** report it, in [DC_Status2.Contactors_Closed](vehicle-can-interfaces/can_v2.md#DC_Status2-Contactors_Closed) |
| `true` | `true` (default) | Controller H-bridge outputs | Controller's dedicated feedback inputs (contact to ground when closed) |
| `true` | `false` | Controller H-bridge outputs | **Assumed** after [`dc_contactors_ios_delay`](configuration/dc_contactors.md#dc_contactors_ios_delay) (default 1 s) — there is no way to confirm the real state |

Three things are worth knowing whichever row you are in:

- The controller **always publishes the command** on
  [DC_Control.Close_Contactors](vehicle-can-interfaces/can_v2.md#DC_Control-Close_Contactors), even
  when it is driving its own IOs. You can use it for monitoring without acting on it.
- When feedback comes over CAN, a `DC_Status2` timeout makes the contactor state *unreliable*, which
  is a fault: the controller can no longer prove the contactors are open, so it will refuse to
  unlock (see [§6](#6-inlet-lock)).
- Feedback is not optional. If your contactors have no wireable auxiliary contact you must either
  report the state over CAN, or accept the timer-based assumption of the third row.

### 4.1 Precharge and closing

During precharge the charger raises its output to match the battery. The controller closes the
contactors when the inlet voltage is within **±20 V** of the battery voltage.

Closing contactors may take some time. While waiting for feedback the
controller keeps re-checking the voltage match and re-opens on a mismatch to avoid arcing — which
is a problem when the measured inlet voltage jumps at the moment of closing (typical of a
differential measurement referenced to battery DC−, when the two contactors do not close at exactly
the same instant). [inhibit_precharge_unmatch_t](configuration/generalities.md#inhibit_precharge_unmatch_t)
suppresses re-opening for a moment after the close command for exactly this case.

### 4.2 Emergency opening

On an emergency stop the controller force-opens the contactors immediately when the current
measurement is not reliable (your system stops reporting measurements on the CAN bus interface). That behaviour is tunable — [`disable_e_stop_contactor_force_open_current_not_reliable`](configuration/dc_contactors.md#disable_e_stop_contactor_force_open_current_not_reliable),
[`delay_e_stop_contactor_force_open_current_not_reliable`](configuration/dc_contactors.md#delay_e_stop_contactor_force_open_current_not_reliable) and
[`contactor_force_open_current_not_reliable_delay_ms`](configuration/dc_contactors.md#contactor_force_open_current_not_reliable_delay_ms) in `[vehicle]`.

Independently of software, loss of CP triggers a **hardware-level** disconnect to meet the timing
of IEC 61851-23 — see
[Charge Signal Disconnect Safety](vehicle-features/evcc_safety_functions.md#charge-signal-disconnect-safety).

## 5. Voltage and current measurement

The controller needs inlet voltage, battery voltage and charge current. You have three options.

| Option | What you do | Entry | Use for |
|---|---|---|---|
| **Your own sensing** | Measure in the vehicle and report in `DC_Status1`/`DC_Status2` | — (default) | Production |
| **Supported CAN sensor** | Wire an Isabellenhütte IVT-S; the controller reads it directly and you send nothing | [use_can_sensor](configuration/can_sensor.md) | Production and prototyping |
| **No BMS mode** | Charge at a fixed current up to a fixed voltage, no BMS at all | [no_bms](configuration/no_bms.md) | **Testing and demos only** |

!!! danger "No BMS mode"
    No BMS mode must never be used in normal conditions. It removes the component whose job is to
    keep current and voltage requests safe for the present state of charge. Pick a safe
    `max_charge_voltage` and a low `max_current`, and use a partially discharged pack.

Combining the CAN sensor, the controller's own contactor drivers and No BMS mode gives a working
demonstration charge with **no vehicle-side software at all** — that combination is documented as
[No code mode](vehicle-features/evcc_no_code_mode.md).

## 6. Inlet lock

The inlet lock is a plain DC motor driving a pin, energised in one polarity to lock and the other to
unlock. The controller drives it in **pulses** rather than continuously, so the motor cannot burn.

| Concern | Entry |
|---|---|
| Pulse length | [locking_pulse_ms](configuration/inlet_lock.md#locking_pulse_ms) (default 600 ms, internally capped to 2 s) |
| Locked/unlocked resistance threshold | [lock_feedback_r_threshold](configuration/inlet_lock.md#lock_feedback_r_threshold) |
| Which side of the threshold means locked | [lock_feedback_low_is_locked](configuration/inlet_lock.md#lock_feedback_low_is_locked) |
| No lock fitted (bench testing) | [no_inlet_lock](configuration/inlet_lock.md#no_inlet_lock) |

Two feedback types cover almost everything on the market, and
[Inlet lock examples](configuration/inlet_lock.md#inlet-lock-examples) gives both: a normally-open
switch (shorted to ground when locked — the defaults) and a 1 k/11 k resistive lock
(`lock_feedback_r_threshold = 5000`, `lock_feedback_low_is_locked = false`).

!!! warning "The lock will refuse to open when the controller cannot prove it is safe"
    To command an unlock the controller requires the DC contactors open, inlet voltage ≤ 60 V, and
    **all three of contactor status, current and inlet voltage to be reliable** — received within
    [can_timeout_ms](configuration/generalities.md#can_timeout_ms). A severed or overloaded CAN bus
    therefore keeps the cable locked, by design. Full rules, and what to do about it, are in
    [Lock safety](vehicle-features/evcc_safety_functions.md#lock-safety-avoid-inlet-disconnection-on-load).

## 7. Digital inputs, outputs and LEDs

Inputs and outputs are assigned functions in the `[hardware]` section; the pinout and electrical
limits are in [Digital inputs and outputs](interfaces.md#digital-inputs-and-outputs).

| Assignment | Values |
|---|---|
| [`dig_in1`](configuration/hardware.md#dig_in1) … | `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep` (inverted logic), `Monitor` |
| [`dig_out1`](configuration/hardware.md#dig_out1) …, [`led1`](configuration/hardware.md#led1) … | `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` |

Two details that save a design iteration:

- [`plugged_in_pulse_ms`](configuration/hardware.md#plugged_in_pulse_ms) turns the `Plugged_In` output from a latch (high for the whole session) into
  a single pulse on the plug-in edge. Use it to wake a VCU on connection without keeping it powered
  for a multi-hour charge and draining the LV battery.
- An output set to `CAN_Controlled` is driven by
  [ADM_CS_EVCC_MEVC_Outputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_mevc_outputs), and inputs
  are reported in [ADM_CS_EVCC_Inputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_inputs) — so you
  can use the controller as a small remote IO block without writing an application for it.

For direct access from your own software on the controller, see
[Manual GPIO control](buildroot-system/gpios.md).

## 8. Temperature monitoring

The CCS inlet's integrated PT1000 sensors wire straight to the controller, which terminates the
charge if limits are exceeded — damaged inlets and cables get dangerously hot at high current.

Channels are mapped to functions and then to actions (monitor only, threshold, or derate the
current request by interpolation) as described in
[Temperature Control](vehicle-features/evcc_temperature_control.md). Readings are published in
[ADM_CS_EVCC_Inputs](vehicle-can-interfaces/can_v2.md#adm_cs_evcc_inputs), so the vehicle can log
or display them without its own sensors.

## 9. Diagnostics

| Source | Use |
|---|---|
| [EVCC_MEVC_Diagnostic_Status](vehicle-can-interfaces/can_v2.md#evcc_mevc_diagnostic_status) | Active faults and errors, and charger status forwarded from the HLC layer. The first place to look when a session fails |
| [EVSE_Information.Communication_Stage](vehicle-can-interfaces/can_v2.md#EVSE_Information-Communication_Stage) | Where in the sequence the controller currently is |
| [CCS_Extra_Information](vehicle-can-interfaces/can_v2.md#ccs_extra_information) / [MCS_Extra_Information](vehicle-can-interfaces/can_v2.md#mcs_extra_information) | Protocol-level detail |
| [Debugging](buildroot-system/debugging.md) | Logs on the controller itself |
| [Vehicle simulator](vehicle-features/vehicle-simulation.md) | Run a session with a simulated battery and BMS, and hand messages over to your own code one at a time |

## 10. Stopping a charge

There is more than one way, and they are not equivalent.

| Way | Effect |
|---|---|
| `Stop` digital input | Clean stop, as if the charger had requested a normal stop. Pull the input up to request it. See [Charge stop](interfaces.md#charge-stop) |
| Over CAN | Same, from your software |
| [`max_soc`](configuration/generalities.md#max_soc) reached | Controller triggers a normal stop (DC only). Set to 80 for bulk-only charging |
| `Emergency_Stop` digital input | Emergency path, see [§4.2](#42-emergency-opening) |
| Current deviation | If the charger does not deliver what was asked for longer than allowed — [Current deviation](configuration/current_deviation.md) |
| Loss of CP | Hardware disconnect, independent of software |

## 11. Sleep and wake-up

The controller can sleep between sessions, which matters for LV battery drain.

- `[hardware] auto_sleep = true` sleeps every time the controller returns to `Waiting_For_EVSE`.
- Or assign `Sleep` to a digital input — **inverted logic**, pull it low to request sleep. A request
  during a session is honoured only once the session ends.
- Wake-up comes from `SWITCHED_POWER` going high, or from a charger being plugged in (the controller
  detects the CP voltage rise).
- Budget ~30 s from a cold boot to charge-ready, versus < 1 s from sleep. Keep the controller
  powered while it sleeps or it loses its state and cold-boots.

Details and power figures: [Sleep functions](vehicle-features/evcc_sleep.md).

## 12. Bidirectional power transfer (ISO 15118-20)

CCS sessions can be bidirectional under ISO 15118-20. Set
[is_bidirectional](configuration/generalities.md#is_bidirectional) and then:

- discharge envelope: [`max_discharge_current`](configuration/generalities.md#max_discharge_current), [`max_discharge_power`](configuration/generalities.md#max_discharge_power), [`min_discharge_power`](configuration/generalities.md#min_discharge_power)
- energy request window: [`max_energy_request`](configuration/generalities.md#max_energy_request), [`min_energy_request`](configuration/generalities.md#min_energy_request), and
  [energy_capacity](configuration/generalities.md#energy_capacity), which becomes **required**
- send [EV_Energy_Request](vehicle-can-interfaces/can_v2.md#ev_energy_request) and
  [EV_Extra_BPT_Information](vehicle-can-interfaces/can_v2.md#ev_extra_bpt_information);
  [EV_V2X_Energy_Request](vehicle-can-interfaces/can_v2.md#ev_v2x_energy_request) is optional

The full picture, including what changes in the CAN interface, is in
[BPT (ISO15118-20)](vehicle-features/evcc_bidirectional.md).

<!-- ## 13. Bringing it up, in order

1. Read [Interfaces](interfaces.md) and wire power, the inlet harness and the CAN bus. Check bus
   termination.
2. Edit the config file `/srv/config.cfg` using the web interface or directly via SSH — at minimum
   `max_current`, `max_voltage`, `target_voltage`, `min_voltage`.
3. Run sessions with the [charger simulator](https://documentation.advantics.fr/adm-cs-spcc/charger-features/charger-simulation.html) at low, safe voltage and current. This proves the inlet, lock, contactors and protocol stack.
4. If you're starting in [no_bms](configuration/no_bms.md) mode and without contactors control, replace the demo pieces one at a time — first your own measurements, then your own contactor
   handling, then turn `no_bms` off — watching
   [EVSE_Information.Communication_Stage](vehicle-can-interfaces/can_v2.md#EVSE_Information-Communication_Stage)
   after each step.
5. Exercise the failure paths: charger stop, `Stop` input, emergency stop, CAN dropout mid-session, over-temperature, and a bidirectional cycle if you use one.
6. Work through the [Deployment Checklist](buildroot-system/must-do-before-deploy.md) before
   shipping. -->

## 13. Frequently hit questions

**No power flows when I plug in a charger.** Check [`max_current`](configuration/generalities.md#max_current) — it defaults to 0 A and every
request is capped to it.

**The session never starts, or drops at random.** Check the CP and its return path PE, make sure they are a twisted pair, routed away from any switching noise. Avoid ground loops and unnecessary long paths.

**The cable stays locked and I cannot remove it.** That is deliberate when the controller cannot
prove the situation is safe. See [§6](#6-inlet-lock); do not force it, and never use the manual
release during operation.

**I see no CAN messages.** Bus termination. Two terminations, one at each
end of the chain. Other nodes have to be alive on the same CAN bus network to acknowledge messages and avoid buffer overflow.

**Do I have to implement all the messages?** No. `EV_Information`, `DC_Status1` and `DC_Status2`
(plus `AC_Status` for AC) are the working minimum; the rest are optional or situational, and a CAN
sensor removes some of them entirely.

**Can the vehicle keep control of its own contactors?** Yes — that is the default. See
[§4](#4-dc-contactor-control).
