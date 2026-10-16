# Getting started

Before powering the SPCC and connecting to it for the first time, wire its hardware protections.
These are hard-wired safety conditions: if any of them is not met, the controller will **never close
the output contactors**, whatever the software or the configuration says.

## Wire the hardware protections

!!! warning
    The following inputs must always be connected. Left open, they read as a fault and block
    charging.

| Input | Connector and pins | What to connect | Details |
|---|---|---|---|
| **20 mA current loop** | `CON105`: `CLOOP_IN` (pin 11), `CLOOP_OUT` (pin 12) | Close the loop, through your E-STOP button and door switches if you have them, or with a wire jumper between pins 11 and 12 **for development only** | [Current loop](interfaces.md#current-loop) |
| **`PT1KS_C`** | `CON102`: `PT1KS_C` (pin 5), `GND` (pin 6) | A PT1000 sensor between pins 5 and 6, or **a jumper between pins 5 and 6 (GND)** for development only | [Temperature Sensors Inputs](interfaces.md#temperature-sensors-inputs) |
| **`PT1KS_D`** | `CON102`: `PT1KS_D` (pin 7), `GND` (pin 8) | A PT1000 sensor between pins 7 and 8, or **a jumper between pins 7 and 8 (GND)** for development only | [Temperature Sensors Inputs](interfaces.md#temperature-sensors-inputs) |
| **Interlock** | `CON105`: `PWR_MOD_INTERLOCK` (pin 7) | Leave it released (not pulled to GND), or wire it to the systems that must be able to cut power, such as power module faults | [Interlock](interfaces.md#interlock) |

!!! danger "Jumpers are for development only"
    A jumper bypasses the hardware protection it replaces: a jumpered current loop ignores the E-STOP
    and door switches, and a jumpered `PT1KS_C` or `PT1KS_D` input never detects over-temperature.
    Use jumpers only on a bench or development setup, never on a deployed charger.

`PT1KS_C` and `PT1KS_D` trigger a hardware shutdown above 110 °C. A floating input reads as
over-temperature.

For reference, the power supply (15–30 VDC) goes to `PW_IN` (pin 2) and `GND` (pin 1) of the power
input connector.

The full pinout of every connector is in [Pinout](introduction.md#pinout).

The full list of conditions required to close the contactors is in
[HW safety conditions](interfaces.md#hw-safety-conditions).

## Next steps

1. [Connect to the SPCC](advos-yocto-system/connecting.md) and open the [Web UI](csm/csm-web-ui.md).
2. [Configure](configuration/README.md) your pistols.
3. Follow the [Integration Guide](integration-guide.md) to bring up the complete charger.
