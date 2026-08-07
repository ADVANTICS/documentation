# Vehicle simulator (simulated PEV)

<div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This feature is not included in the standard software stack and has to be purchased separately. Please contact <a href="mailto:sales@advantics.fr">sales</a> for more information🚨
</div>

---

The vehicle simulator turns an ADVANTICS vehicle charge controller into **a complete vehicle you can
charge**. The whole charge sequence is played out for real — protocol negotiation, authorisation,
cable check, precharge, the current-demand loop, stopping — against a simulated battery and BMS. No
traction battery, no high voltage.

## Who this is for

!!! tip "Developing the charger side of a charge session? This is the vehicle you develop against."
    Whether you are building a charge station or a charger-side communication
    controller, you need a vehicle to charge long before you can risk a real one on your bench. A
    vehicle controller running this simulator **is** that vehicle: it requests power over the standard
    CCS or MCS interface, follows the sequence and reacts as a car's BMS would — repeatedly, at any
    state of charge you like, without charging a real pack.

| If you are developing | It gives you |
|---|---|
| A charge station, or its power-module software | A vehicle-side partner that runs the complete sequence on demand, so you can validate your implementation and force its error and abort paths |
| A vehicle, with your own BMS or VCU software | A stand-in for the vehicle-side software you have not written yet, running on your own vehicle controller |

## What it does, and does not, prove

**It validates:** the whole sequence and its branches; protocol selection and negotiation;
authorisation; cable check and precharge; the current-demand loop and how well your side follows
requests; normal end of charge, and emergency stop from the vehicle; bidirectional and V2X energy
requests; and how your side behaves when an expected message never arrives.

**It does not validate:** anything about real power or a real battery. Cell behaviour, pack impedance,
thermal derating, insulation, EMC and contactor or cable wear are outside what a simulated battery can
tell you. Clean simulated sessions are what you want *before* HV testing, not instead of it.

## What you need on the bench

{{ figure('./emulators.webp', 'A bench with the connection box between the two charge controllers') }}

- **A vehicle charge controller** with the simulator licensed on it.
- **The connection box.** It powers the charge controller and simulates the inlet and the charge
  pistol, including their integrated resistances — so the controller sees a plausible plug without a
  real inlet, cable or connector on the bench. Its pinouts, should you want to wire your own hardware
  to one side of it, are in [Hardware wiring](#hardware-wiring).
- **Network access** to the controller's Web UI, which is how the simulator is driven.

!!! warning "Simulated power delivery -- Real charge sequence"
    A simulated vehicle asks for current that no battery is going to absorb.
    So the charger side should support a simulated power flow.

## Driving the simulator

Everything happens in the [Web UI](../advos-yocto-system/csm-web-ui.md):
[connect to the controller](../advos-yocto-system/connecting.md) and open `/dashboard/simulation`.
The simulator can be enabled, disabled and re-parameterised **while a session is running**.

{{ figure('./vehicle-simulator.png', 'The simulation page of the Web UI, where the vehicle simulator is driven') }}

### Enabling the simulator

This switch enables or disables the simulation feature.

{{ figure('./enable-simulators.png', 'Enabling the simulation feature') }}

### Parameters (left section)

Vehicle and battery values. Each has a field you edit and an **actual value** showing what is currently
applied. Nothing takes effect until you press **Send**.

Between them these decide what kind of vehicle turns up: how full it is, how much energy it wants, how
fast it can take current, and how quickly its contactors respond. Every one of them is listed in the
[configuration reference](#configuration-reference) below.

### Control (middle section)

Toggles that **stop the simulator sending a specific CAN message**, handing that message over to
whatever you are developing. This is the intended way to bring up a **partial** implementation of the
PEV generic interface: start with the simulator supplying everything, then switch off one message at a
time as your own software starts sending it.

- **EV Information**: [EV_Information](../vehicle-can-interfaces/can_v2.md#ev_information)
- **DC Status1**: [DC_Status1](../vehicle-can-interfaces/can_v2.md#dc_status1)
- **DC Status2**: [DC_Status2](../vehicle-can-interfaces/can_v2.md#dc_status2)
- **EV Energy Request**: [EV_Energy_Request](../vehicle-can-interfaces/can_v2.md#ev_energy_request)
- **EV V2X Energy Request**: [EV_V2X_Energy_Request](../vehicle-can-interfaces/can_v2.md#ev_v2x_energy_request)
- **EV Extra BPT Information**: [EV_Extra_BPT_Information](../vehicle-can-interfaces/can_v2.md#ev_extra_bpt_information)

Toggling takes effect immediately.

### Command (right section)

Vehicle-side events, each triggered by its own button:

- **Request Normal End Of Charge** — the vehicle asks to end the charge normally.
- **Request Emergency Stop** — the vehicle raises an emergency stop.

## Exercising the paths that matter

A sequence that works when everything goes well is the easy half. These are the branches worth forcing
deliberately, and how to force each one:

| Path to test | How to produce it |
|---|---|
| A nearly empty, or nearly full, vehicle | `ev_battery_soc` |
| Charge that terminates on reaching target SoC | `target_energy_request` below `maximum_energy_request` |
| A vehicle that wants more than your charger can give | raise `ev_dc_max_charge_current`, `ev_battery_max_voltage` |
| A vehicle that asks for very little | lower `ev_dc_max_charge_current` |
| Slow contactors, and your precharge timeouts | raise `contactors_delay` |
| A full session in a fraction of the time | `charging_speed_multiplier` |
| Vehicle-initiated normal stop mid-session | **Request Normal End Of Charge** in *Command* |
| Vehicle-initiated emergency stop | **Request Emergency Stop** in *Command* |
| Your implementation only sends some messages | switch the matching toggles off in *Control* |
| Bidirectional / V2X energy windows | `maximum_v2x_energy_request`, `minimum_v2x_energy_request`, `departure_time` |
| A message that stops arriving mid-session | switch its toggle off during the session |
| Changing limits in ISO15118-20 Dynamic mode | Select Dynamic mode in the configuration page and update limits dynamically |
| Constant Voltage / Constant Current in ISO15118-20 Scheduled mode mode | Select Scheduled mode in the configuration page and control the current, voltage or switch between both depending on the vehicle's needs |

Follow the session at `/dashboard/monitoring` while you do it.

{{ figure('./mcs_charge.png', 'Following a simulated (MCS) charge session on the monitoring page') }}

{{ figure('./mcs_discharge.png', 'Following a simulated (MCS) discharge session on the monitoring page') }}

!!! note
    After a session ends, wait for the controllers to return to idle before plugging in again.


## Hardware wiring

To wire your own hardware to one side of the connection box:

### Power connector
<div class="small-table compact-table" markdown="1">

| Number | Label | Color |
|--------|-------|-------|
| 1 | 24V | Red |
| 2 | GND | Black |

</div>

### CAN bus connector
<div class="small-table compact-table" markdown="1">

| Number | Label | Color |
|--------|-------|-------|
| 1 | CAN H | Brown |
| 2 | CAN L | Blue |
| 3 | CAN GND | Black |

</div>

### MCS connector
<div class="small-table compact-table" markdown="1">

| Number | Label | Color |
|--------|-------|-------|
| 1 | CE | Orange |
| 2 | ID | White |
| 3 | PHY1 | Purple |
| 4 | PHY2 | Green |
| 5 | PE | Yellow/Green |

</div>

## Configuration reference

These options control how the simulated vehicle behaves. A configuration entry sets the value applied
when the controller restarts; the matching live parameter in the Web UI can be changed at any time.

### `contactors_delay` (float)

- **Description:** Time (in seconds) that contactors take to respond to open or close commands.
- **Default:** `0.6`

### `maximum_energy_request` (float)

- **Description:** Maximum State of Charge (SoC) in percentage requested from the charger.
- **Default:** `100`
- **Range:** `0 - 100`

### `target_energy_request` (float)

- **Description:** Target SoC in percentage requested from the charger.
- **Default:** `80`
- **Range:** `0 - 100`

### `minimum_energy_request` (float)

- **Description:** Minimum SoC in percentage requested from the charger.
- **Default:** `30`
- **Range:** `0 - 100`

### `maximum_v2x_energy_request` (float)

- **Description:** Maximum SoC in percentage requested from the charger during a V2X session.
- **Default:** `80`
- **Range:** `0 - 100`

### `minimum_v2x_energy_request` (float)

- **Description:** Minimum SoC in percentage requested from the charger during a V2X session.
- **Default:** `30`
- **Range:** `0 - 100`

### `departure_time` (float)

- **Description:** Departure time of the EV sent to the charger, in seconds.
- **Default:** `86400` (24 hours)

### `charging_speed_multiplier` (float)

- **Description:** Multiplier for the simulated battery charging time, used to accelerate or slow down the simulation for observability. This parameter allows user to run the simulated charge session faster than real time. If this value set to 100, the simulated battery will charge 100 times faster. The elapsed time for the simulated session is indicated in the same page. When the charge speed multiplier is high, the charger can overshoot for discharge SoC because the time is faster for the battery and charger might not be able to reach that fast.
- **Default:** `1`

### `ev_battery_soc` (float)

- **Description:** Initial State of Charge (SoC) in percentage for the simulated battery. The SoC resets to this value between sessions.
- **Default:** `30`
- **Range:** `0 - 100`

### `ev_battery_capacity` (float)

- **Description:** Capacity of the simulated EV battery in kilowatt-hours (kWh).
- **Default:** `75.530`

### `ev_battery_min_voltage` (float)

- **Description:** Minimum voltage (in volts) of the simulated battery at 0% SoC.
- **Default:** `274`

### `ev_battery_max_voltage` (float)

- **Description:** Maximum voltage (in volts) of the simulated battery at 100% SoC.
- **Default:** `400`

### `ev_dc_max_charge_current` (float)

- **Description:** Maximum charging current (in amps) the EV can accept during DC charging sessions.
- **Default:** `120`

### `ev_dc_max_discharge_current` (float)

- **Description:** Maximum discharge current (in amps) the EV can accept during DC discharging sessions.
- **Default:** `120`

---

## Message enable flags

These options enable or disable specific EV-related messages sent by the simulator. They are the
persistent form of the *Control* toggles above.

### `enable_ev_information` (bool)

- **Description:** Whether to enable the `EV_Information` message from the simulator.
- **Default:** `True`
- Message description: [`ev_information`](../vehicle-can-interfaces/can_v2.md#ev_information)

### `enable_dc_status_1` (bool)

- **Description:** Whether to enable the `DC_Status1` message from the simulator.
- **Default:** `True`
- Message description: [`dc_status1`](../vehicle-can-interfaces/can_v2.md#dc_status1)

### `enable_dc_status_2` (bool)

- **Description:** Whether to enable the `DC_Status2` message from the simulator.
- **Default:** `True`
- Message description: [`dc_status2`](../vehicle-can-interfaces/can_v2.md#dc_status2)

### `enable_ev_energy_request` (bool)

- **Description:** Whether to enable the `EV_Energy_Request` message from the simulator.
- **Default:** `True`
- Message description: [`ev_energy_request`](../vehicle-can-interfaces/can_v2.md#ev_energy_request)

### `enable_ev_v2x_energy_request` (bool)

- **Description:** Whether to enable the `EV_V2X_Energy_Request` message from the simulator.
- **Default:** `True`
- Message description: [`ev_v2x_energy_request`](../vehicle-can-interfaces/can_v2.md#ev_v2x_energy_request)

### `enable_ev_extra_bpt_info` (bool)

- **Description:** Whether to enable the `EV_Extra_BPT_Information` message from the simulator.
- **Default:** `True`
- Message description: [`ev_extra_bpt_information`](../vehicle-can-interfaces/can_v2.md#ev_extra_bpt_information)
