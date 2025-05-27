# Charger communication simulation

> [!DANGER]
> This feature **is not included in the normal software stack and has to be purchased apart.** Please contact [sales](mailto:sales@advantics.fr) for more information

The primary objective of this software is to emulate a battery and BMS on the vehicle side, allowing users to observe and interact with the system without requiring an actual vehicle.

<!-- This feature is designed to simulate EV behavior in a controlled environment, making it possible to test various scenarios and vehicle responses during a charging session. -->

# UI

Simulation is primarily managed and controlled by the [CSM Web UI](charge-controllers/advantics_os/csm-web-ui.md). [Connect to your controller](charge-controllers/advantics_os/connecting) dashboard and head to `/dashboard/simulation`.

The interface allows real-time enabling the simulator and editing and control of parameters during a simulated session. It is divided into three main sections: **Parameters**, **Control**, and **Command**.

![UI](./vehicle-simulator.png)

## Enabling the simulator

This switch enables or disables the simulation feature.

![Enabling the simulation feature](./enable-simulators.png)

This user interface allows live editing and control of vehicle-side parameters in a simulated charging session. It consists of three main sections: **Parameters**, **Control**, and **Command**.

## Live Editable parameters

### **Parameters (Left Section)**

This section is a **form** where the user can input and adjust various vehicle-related values. These include:

- **Contactors Delay**
- **Departure Time**
- **Charge Speed Multiplier**
- **Energy Requests**: Maximum, Target, Minimum (including V2X-specific)
- **EV Energy Capacity**
- **EV DC Max Charge Current**

Each parameter has:

- A **"Desired Value"** field for user input.
- An **"Actual Value"** field that shows the currently applied value in the system.

Changes are only applied after the user clicks the **“Send”** button at the bottom of the section.

---

### **Control (Middle Section)**

This section contains toggle switches that let the user **enable or disable the sending of specific information** from the simulated vehicle:

- **EV Information**
- **DC Status1**
- **DC Status2**
- **EV Energy Request**
- **EV V2X Energy Request**
- **EV Extra BPT Information**

These toggles apply immediately when switched and determine which data types the simulator sends to the system.

---

### **Command (Right Section)**

This section allows the user to trigger specific **vehicle-side events** using dedicated buttons:

- **Request Normal End Of Charge** – Simulates the vehicle requesting to end the charge normally.
- **Request Emergency Stop** – Simulates an emergency stop request from the vehicle.

Each action is performed by clicking the corresponding **“Stop”** button.

# HOW TO

## Simulating a bidirectional MCS charge session (ISO151180-20) with simulated charger and vehicle, using ADM-CS-SPCC, ADM-CS-MEVC and simulator software stack

1. Enable the [charge station simulator](charge-controllers/charger-simulation#enabling-the-simulator).
2. Enable the [vehicle simulator](charge-controllers/vehicle-simulation#enabling-the-simulator).
3. Make sure ADVANTICS vehicle controller configuration option [No BMS mode](charge-controllers/evcc_configuration/no_bms) is **disabled** (set to false).
4. Set the [relevant configuration entries in the vehicle controller](charge-controllers/evcc_bidirectional?id=relevant-config-entries) and [charge station controller](charge-controllers/secc_generic/secc_bidirectional?id=relevant-config-entries) for ISO151180-20.
5. Enable sending [`DC_Power_Parameters`](charge-controllers/charger-simulation?id=enable_dc_power_parameters-bool), [`Power_Modules_Status`](charge-controllers/charger-simulation?id=enable_power_module_status-bool) and [`Sequence_Flags`](charge-controllers/charger-simulation?id=enable_sequence_flags-bool) in the [ charge controller simulator UI ](charge-controllers/charger-simulation#UI)
6. Enable sending [`EV_Information`](charge-controllers/vehicle-simulation?id=enable_ev_information-bool), [`DC_Status_1`](charge-controllers/vehicle-simulation?id=enable_dc_status_1-bool),[`DC_Status_2`](charge-controllers/vehicle-simulation?id=enable_dc_status_2-bool), [`EV_Energy_Request`](charge-controllers/vehicle-simulation?id=enable_ev_energy_request-bool), [`EV_V2X_Energy_Request`](charge-controllers/vehicle-simulation?id=enable_ev_v2x_energy_request-bool) and [`EV_Extra_BPT_Info`](charge-controllers/vehicle-simulation?id=enable_ev_extra_bpt_info-bool) in the [vehicle simulator UI](charge-controllers/vehicle-simulation#UI).
7. Connect the plug.
8. Head to `dashboard/monitoring` and follow the charge session.

> [!NOTE]
> Please wait at least 30 seconds between sessions

# Simulated EV Configuration Options

These configuration options control how the simulated EV interacts with the charger.

## `contactors_delay` (float)

- **Description:** Time (in seconds) that contactors take to respond to open or close commands.
- **Default:** `0.6`

## `maximum_energy_request` (float)

- **Description:** Maximum State of Charge (SoC) in percentage requested from the charger.
- **Default:** `100`
- **Range:** `0 - 100`

## `target_energy_request` (float)

- **Description:** Target SoC in percentage requested from the charger.
- **Default:** `80`
- **Range:** `0 - 100`

## `minimum_energy_request` (float)

- **Description:** Minimum SoC in percentage requested from the charger.
- **Default:** `30`
- **Range:** `0 - 100`

## `maximum_v2x_energy_request` (float)

- **Description:** Maximum SoC in percentage requested from the charger during a V2X session.
- **Default:** `80`
- **Range:** `0 - 100`

## `minimum_v2x_energy_request` (float)

- **Description:** Minimum SoC in percentage requested from the charger during a V2X session.
- **Default:** `30`
- **Range:** `0 - 100`

## `departure_time` (float)

- **Description:** Departure time of the EV sent to the charger, in seconds.
- **Default:** `86400` (24 hours)

## `charging_speed_multiplier` (float)

- **Description:** Multiplier for the simulated battery charging time, used to accelerate or slow down the simulation for observability.
- **Default:** `1`

  > [!NOTE]
  > When the simulation time multiplier is high, the charger can overshoot for discharge SoC (because time is warped): the solution is to set slopes on EVSE side more agressively so the EVSE can keep up with the faster time multiplier

## `ev_battery_soc` (float)

- **Description:** Initial State of Charge (SoC) in percentage for the simulated battery. The SoC resets to this value between sessions.
- **Default:** `30`
- **Range:** `0 - 100`

## `ev_battery_capacity` (float)

- **Description:** Capacity of the simulated EV battery in kilowatt-hours (kWh).
- **Default:** `75.530`

## `ev_battery_min_voltage` (float)

- **Description:** Minimum voltage (in volts) of the simulated battery at 0% SoC.
- **Default:** `274`

## `ev_battery_max_voltage` (float)

- **Description:** Maximum voltage (in volts) of the simulated battery at 100% SoC.
- **Default:** `400`

## `ev_dc_max_charge_current` (float)

- **Description:** Maximum charging current (in amps) the EV can accept during DC charging sessions.
- **Default:** `120`

## `ev_dc_max_discharge_current` (float)

- **Description:** Maximum discharge current (in amps) the EV can accept during DC discharging sessions.
- **Default:** `120`

---

# Message Enable Flags

These options enable or disable specific EV-related messages sent by the simulator.

## `enable_ev_information` (bool)

- **Description:** Whether to enable the `EV_Information` message from the simulator.
- **Default:** `True`
- Message description: [`ev_information`](charge-controllers/evcc_generic/can_v2?id=ev_information)

## `enable_dc_status_1` (bool)

- **Description:** Whether to enable the `DC_Status1` message from the simulator.
- **Default:** `True`
- Message description: [`dc_status1`](charge-controllers/evcc_generic/can_v2?id=dc_status1)

## `enable_dc_status_2` (bool)

- **Description:** Whether to enable the `DC_Status2` message from the simulator.
- **Default:** `True`
- Message description: [`dc_status2`](charge-controllers/evcc_generic/can_v2?id=dc_status2)

## `enable_ev_energy_request` (bool)

- **Description:** Whether to enable the `EV_Energy_Request` message from the simulator.
- **Default:** `True`
- Message description: [`ev_v2x_energy_request`](charge-controllers/evcc_generic/can_v2?id=ev_energy_request)

## `enable_ev_v2x_energy_request` (bool)

- **Description:** Whether to enable the `EV_V2X_Energy_Request` message from the simulator.
- **Default:** `True`
- Message description: [`ev_v2x_energy_request`](charge-controllers/evcc_generic/can_v2?id=ev_v2x_energy_request)

## `enable_ev_extra_bpt_info` (bool)

- **Description:** Whether to enable the `EV_Extra_BPT_Information` message from the simulator.
- **Default:** `True`
- Message description: [`ev_extra_bpt_information`](charge-controllers/evcc_generic/can_v2?id=ev_extra_bpt_information)
