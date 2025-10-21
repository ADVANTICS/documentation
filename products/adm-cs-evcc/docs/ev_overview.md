# Electric vehicle overview

There are many key components to make an electric vehicle. Most of them do not interact with the
charging process directly (like the drive system for example), but might be linked indirectly
(preventing the user from driving away with a charge plug still connected).

!!! attention
    Always check national rules and requirements when designing a charging system of an electric
    vehicle. Do not rely on the following information to be accurate or even applicable.


## AC vs DC charging

AC charging and DC charging are abstracted away by the charge controller. The information about what
standard or charging connector has been plugged in is sent over the CAN bus. Sequences then look
approximately like this:

### AC charging

- The user plugs the charging cable into the car
- The EVCC announces the cable connection on the CAN bus
- The EVCC measures the CP line duty cycle to know how much current is available
- The EVCC measures the resistance on the PP line to know the current rating of the cable
- The EVCC commands the inlet to lock the charging cable
- The EVCC commands the EVSE to close the AC contactors
- The EVCC forwards the available current to the OBC over CAN
- The EVSE closes the charging contactors, making power available on the OBC input
- The OBC starts the power delivery process, staying within the EVSE and battery limits.
- The EVCC periodically monitors the charging inlet temperature during charging
- Charging continues until the user or the BMS requests to terminate the process
- The EVCC signals to the EVSE that the charging process is terminated
- The EVSE opens the AC contactors
- The EVCC commands the inlet to release the charging cable

### DC charging

- The user plugs the charging cable into the car
- The EVCC announces the cable connection on the CAN bus
- The EVCC measures CP line duty cycle, 5% signals digital communication on the CP line
- The EVCC commands the inlet to lock the charging cable
- The EVCC requests a list of capabilities from the EVSE (protocol version, voltage, current)
- The EVCC signals that the car is ready for the isolation check
- The EVCC requests the charging station to perform the isolation check
- The EVCC transmits the battery terminal voltage to the EVSE for the precharge sequence
- The EVSE attempts to match the car battery voltage on its output
- The EVCC monitors the inlet voltage, and closes the charging contactors once the voltages  are close enough to safely do so.
- The EVCC goes into power delivery mode, forwarding current and voltage setpoints from the BMS to the EVSE periodically
- The EVCC supervises the charging process by comparing voltage and current measurements to the requested values, connector temperatures are also monitored
- Charging continues until the user or the car requests to terminate the process
- At the end-of-charge, the EVCC commands the EVSE to stop power delivery
- The EVCC opens the charging contactor
- The EVCC monitors the charge port voltage, and opens the contactors once the voltage is at a safe level (below 60 V)
- The EVCC releases the inlet lock, allowing the user to unplug the charging cable.

## CCS inlet assembly

Majority of the CCS inlets are identical in their wiring. The following wires can be identified at
the cable end:

- CP wire.
- PP wire.
- PE ground (identical high-gauge wire for power and signal ground, to be connected to the vehicle chassis).
- RTD PT1000 monitoring positive power terminal (2 terminals – one must be grounded).
- RTD PT1000 monitoring negative power terminal (2 terminals – one must be grounded).
- Potentially more thermistors, monitoring for example AC pins
- Positive DC high gauge wire (actual power delivery).
- Negative DC high gauge wire (actual power delivery).
- Depending on the type of the connector, 1 to 3 phase connections (2-4 power wires).
- Inlet motor interface (Positive and negative motor drive, position switch, ground)

!!! tip
    Some CCS inlet manufacturers are notoriously bad at documenting their cable. If you end up probing
    with a multimeter, just to find which wire is which, you can always identify the RTD (temperature
    sensor) by being able to see around 1100 Ohms between them.


## HMI (Human Machine Interface)

Consists of displays, indicators, buttons. Depending on the use case, anything from a few LEDs
showing basic status, small OLED display, to a large LCD TV screen to schedule charging can be used.
The communication for configuration and readout of the charge status is always done over the CAN bus.

This topic is left on the customer. A simplest way is to use the provided CAN bus, and parse the
interesting messages, like charging status, and display those on the screen, and add control for
limiting current, if desired.
