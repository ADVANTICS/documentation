# Charger simulator (simulated EVSE)

<div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This feature is not included in the standard software stack and has to be purchased separately. Please contact <a href="mailto:sales@advantics.fr">sales</a> for more information🚨
</div>

---

The charger simulator turns an ADVANTICS charge station controller into **a complete charger you can
test against**. The whole charge sequence is played out for real — protocol negotiation,
authorisation, cable check, precharge, the current-demand loop, stopping — and only the power stage is
simulated. No power electronics, no high voltage.

## Who this is for

!!! tip "Developing the vehicle side of a charge session? This is the charger you develop against."
    Whether you are building a vehicle, a BMS, a VCU or a vehicle-side communication controller, you
    need a charger to work against long before you can book time on a real one. A charge station
    controller running this simulator **is** that charger: it answers over the standard CCS or MCS
    interface, so you can walk the whole sequence and every branch of it — including the ugly ones —
    from a bench.

| If you are developing | It gives you |
|---|---|
| A vehicle, or its BMS or VCU software | A charger-side partner that runs the complete sequence on demand, so you can validate your implementation and force its error and abort paths |
| A charger, with your own power modules | A stand-in for the power stage you have not built, wired or finished yet, running on your own charge station controller |

## What it does, and does not, prove

**It validates:** the whole sequence and its branches; protocol selection and negotiation;
authorisation, including refusal; cable check and precharge; the current-demand loop and setpoint
following; normal stop, user stop and emergency stop; bidirectional and V2X sequences; and how your
side behaves when an expected message never arrives.

**It does not validate:** anything about real power. Converter dynamics, insulation, EMC, thermal
behaviour and contactor or cable wear are outside what a simulated power stage can tell you. Clean
simulated sessions are what you want *before* HV testing, not instead of it.

## What you need on the bench

- **A charge station controller** with the simulator licensed on it. The licence is tied to the
  controller's serial number.
- **The connection box.** It powers the charge controller and simulates the inlet and the charge
  pistol, including their integrated resistances — so the controller sees a plausible plug without a
  real inlet, cable or vehicle connector on the bench. Its pinouts, should you want to wire your own
  hardware to one side of it, are in [Hardware wiring](#hardware-wiring).
- **Network access** to the controller's [Web UI](../advos-yocto-system/csm-web-ui.md), which is how
  the simulator is driven.

!!! warning "One simulated side means the other side must not deliver power"
    When you run the simulator on one side only, make sure the **real** controller on the other side
    is configured so that no power is actually delivered. A simulated charger reports current that no
    hardware is producing.

## Driving the simulator

Everything happens in the [Web UI](../advos-yocto-system/csm-web-ui.md):
[connect to the controller](../advos-yocto-system/connecting.md) and open `/dashboard/simulation`.
The simulator can be enabled, disabled and re-parameterised **while a session is running**.

{{ figure('./charger-simulator.png', 'The simulation page of the Web UI, where the charger simulator is driven') }}

### Enabling the simulator

This switch enables or disables the simulation feature.

{{ figure('./enable-simulators.png', 'Enabling the simulation feature') }}

### Parameters (left section)

Charge-session and power-module values. Each has a **desired value** you edit and an **actual value**
showing what is live. Nothing takes effect until you press **Send**.

- **Session** — CCS authorisation duration, and whether authorisation succeeds.
- **PowerModules** — voltages, currents, insulation resistance, module response time.
- **Simulator** — voltage and current ramp slopes.

This is what lets one simulator behave like many different chargers: a slow authoriser, a lazy
ramper, a charger that refuses, a charger with poor insulation.

### Control (middle section)

Toggles that **stop the simulator sending a specific CAN message**, handing that message over to
whatever you are developing. This is the intended way to bring up a **partial** implementation of the
EVSE generic interface: start with the simulator supplying everything, then switch off one message at
a time as your own software starts sending it.

- **Enable Sending DC Power Parameters**: [DC_Power_Parameters](../charger-can-interfaces/can_v3.md#DC_Power_Parameters)
- **Enable Sending Power Modules Status**: [Power_Modules_Status](../charger-can-interfaces/can_v3.md#Power_Modules_Status)
- **Enable Sending Sequence Flags**: [Sequence_Control](../charger-can-interfaces/can_v3.md#Sequence_Control)

Toggling takes effect immediately.

### Command (right section)

Manual actions, each with its own button:

- **Current Setpoint** — enter a value and click **Apply**. Available only in
  [Range_Mode](../charger-can-interfaces/sequences_v3.md#power-transfer-with-range-mode)
  bidirectional transfers. The setpoint is always clamped to the system limits: maximum
  charge/discharge current, cable limits, and the EV's own current limits.
- **User Stop Button Pressed** — simulates a user pressing the stop button on the charger.

## Exercising the paths that matter

A sequence that works when everything goes well is the easy half. These are the branches worth forcing
deliberately, and how to force each one:

| Path to test | How to produce it |
|---|---|
| Authorisation refused | `ccs_authorisation_success` = `false` |
| Slow authorisation, and your timeouts | raise `ccs_authorisation_duration` |
| Slow charge-parameter negotiation | raise `charge_params_negotiation_duration` |
| Modules slow to wake up | raise `power_modules_wake_up_duration`, `power_modules_dead_time` |
| Gentle or aggressive ramps | `voltage_ramp_up_slope`, `voltage_ramp_down_slope`, `current_ramp_up_slope`, `current_ramp_down_slope` |
| Insulation fault before precharge | drop `insulation_resistance` below your threshold |
| A charger weaker than the vehicle asks for | lower `maximum_voltage`, `maximum_charge_current` |
| Charger-initiated stop mid-session | **User Stop Button Pressed** in *Command* |
| Session that ends on its own | `charge_duration` (set it before the `Charging` state) |
| Your implementation only sends some messages | switch the matching toggles off in *Control* |
| Bidirectional / V2X setpoint following | *Current Setpoint* in *Command*, in `Range_Mode` |
| A message that stops arriving mid-session | switch its toggle off during the session |

Follow the session at `/dashboard/monitoring` while you do it.

{{ figure('./charger-monitor.png', 'Following a simulated session on the monitoring page') }}

!!! note
    After a session ends, wait for the controllers to return to idle before plugging in again.

## If you have controllers on both sides

With an ADVANTICS controller on each side you can run a fully simulated session end to end — useful
for demonstrations, and for telling "my side is wrong" apart from "the other side is wrong". To run a
bidirectional MCS session (ISO 15118-20) with a simulated charger and a simulated vehicle:

1. Configure both controllers for bidirectional power transfer — see
   [Relevant Config Entries](../charger-can-interfaces/secc_bidirectional.md#relevant-config-entries).
2. [Enable the charger simulator](#enabling-the-simulator) with all CAN messages enabled. The default
   configuration is a good starting point.
3. Enable the vehicle simulator on the vehicle-side controller — documented on the ADM-CS-EVCC (CCS)
   and ADM-CS-MEVC (MCS) sites, under *Features → Vehicle simulator*.
4. Connect the plug.
5. Follow the session at `/dashboard/monitoring`.

## Hardware wiring

To wire your own hardware to one side of the connection box:

### Power connector

| Number | Label | Color |
|--------|-------|-------|
| 1 | 24V | Red |
| 2 | GND | Black |

### CAN bus connector

| Number | Label | Color |
|--------|-------|-------|
| 1 | CAN H | Brown |
| 2 | CAN L | Blue |
| 3 | CAN GND | Black |

### MCS connector

| Number | Label | Color |
|--------|-------|-------|
| 1 | CE | Orange |
| 2 | ID | White |
| 3 | PHY1 | Purple |
| 4 | PHY2 | Green |
| 5 | PE | Yellow/Green |

## Configuration reference

The configuration is edited in the web interface at `/dashboard/simulation/config`.

!!! note
    The configuration entries and most of the live parameters are the same values. The configuration
    entry sets the **default** applied when the controller restarts, and changing it requires the
    charge controller applications to restart. The live parameters can be changed at any time —
    typically between sessions, to try a different behaviour without making it permanent.

### `pistol_index` (int)

- **Description:** Pistol index used by the simulated charger. Ensure it matches the index configured for your target pistol.
- **Default:** `1`
- **Range:** `1 - 16`
- **Note:** CCS DC defaults to index `1`.

### `ccs_authorisation_duration` (float)

- **Description:** Duration (in seconds) the simulated charger waits before proceeding with CCS authorization.
- **Default:** `3`

### `ccs_authorisation_success` (bool)

- **Description:** Whether the simulated charger should grant CCS authorization at the end of the authorisation duration. This should be enabled to reach the charging state.
- **Default:** `True`

### `charge_params_negotiation_duration` (float)

- **Description:** Duration (in seconds) taken to negotiate charge parameters.
- **Default:** `1.5`

### `power_modules_wake_up_duration` (float)

- **Description:** Time (in seconds) for power modules to wake up.
- **Default:** `1`

### `power_modules_dead_time` (float)

- **Description:** Dead time (in seconds) before power modules start operating.
- **Default:** `1`

### `voltage_ramp_up_slope` (float)

- **Description:** Voltage ramp-up rate in volts per second.
- **Default:** `200`

### `voltage_ramp_down_slope` (float)

- **Description:** Voltage ramp-down rate in volts per second.
- **Default:** `100`

### `current_ramp_up_slope` (float)

- **Description:** Current ramp-up rate in amps per second, once actual charging starts. Determines how quickly the current increases from 0 to the target value.
- **Default:** `20`

### `current_ramp_down_slope` (float)

- **Description:** Current ramp-down rate in amps per second, when charging ends. Determines how quickly the current decreases from the target value to 0.
- **Default:** `20`

### `charge_duration` (float)

- **Description:** Charge session will be stopped automatically after this duration (in seconds). It must be set **before** the `Charging` state, the changes made during `Charging` state will be taken into account for the next charge session.
- **Default:** `10`

### `maximum_voltage` (float)

- **Description:** Maximum voltage accepted by this simulated charger (in volts).
- **Default:** `500`

### `maximum_charge_current` (float)

- **Description:** Maximum output charge current deliverable by the simulated charger (in amps).
- **Default:** `120`

### `maximum_discharge_current` (float)

- **Description:** Maximum output discharge current that the simulated charger can sink (in amps).
- **Default:** `120`

### `insulation_resistance` (float)

- **Description:** Insulation resistance (in ohms) reported after insulation test.
- **Default:** `100`

### `enable_dc_power_parameters` (bool)

- **Description:** Whether the `DC_Power_Parameters` message sent by the simulator should be enabled.
- **Default:** `True`
- Message description: [`dc_power_parameters`](../charger-can-interfaces/can_v3.md#DC_Power_Parameters)

### `enable_power_module_status` (bool)

- **Description:** Whether the `Power_Modules_Status` message sent by the simulator should be enabled.
- **Default:** `True`
- Message description: [`power_modules_status`](../charger-can-interfaces/can_v3.md#Power_Modules_Status)

### `enable_sequence_control` (bool)

- **Description:** Whether the `Sequence_Control` message sent by the simulator should be enabled.
- **Default:** `True`
- Message description: [`sequence_control`](../charger-can-interfaces/can_v3.md#Sequence_Control)
