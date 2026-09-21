# Theory of Operation

The ADB-PC-CH01 is a bidirectional isolated AC/DC converter rated at 50kW for continuous operations. It is based on Silicon Carbide power switches operated at high frequencies allowing for fast transient response and high efficiency.
The ADB-PC-CH01 consists of an active front end AC stage, connected to a high efficiency DC/DC isolation stage followed by a buck stage for a large DC output control range. The ADB-PC-CH01 can be paralleled on the DC port and the AC port
to scale up large DC/AC systems. As it is bidirectional it is able to support V2G systems. 

The ADB-PC-CH01 currently supports DC side control mode. This means that the Voltage and Current on the DC port are actively regulated by the converter.
To enable this control type, the converter sinks/sources AC current as needed, while keeping near unity power factor.

Operating in this mode the ADB-PC-CH01 may also be used as an isolated high current/voltage DC lab power supply. Control and readout are provided via the CAN bus, allowing for integration into test setups or automatic procedures as well as into autonomous systems.

At no point during operation may the DC port voltage exceed the rated DC voltage as this risks damaging the converter.

## DC Port Control

When the operating mode is set to 'DC Port Control' and all requered setpoints (voltage/current) have been sent, the ADB-PC-CH01 starts up and provides a CV/CC controlled DC output. The DC output has a small 0.2 Ohm virtual series impedance that
allows the unit to be paralleled with other dc sources. The working model of the DC port thus becomes essentially identical to a current limited ideal voltage source with a 0.2 Ohm resistor in series. Changing an externally applied voltage from
below the DC port setpoint to above the DC port setpoint naturally reverses current with the magnitude set by either the virtual series resistor or the current limit, whichever is lower. The DC port is fully galvanically isolated towards mains and PE.
This allows the converter to be used in EV charge application, as well. In this case the same mental model of the voltage source with virtual series resistance applies.

In this DC Port Control Mode the ADB-PC-CH01 is grid-following only. It thus expects a Utility grid within the specified ranges to be applied that is expected to be stiff relative to the 50kW power rating of the converter.

### Efficiency Optimizations

If the DC bus voltage does not slew rapidly, by e.g. being connected to a battery, the converter may optimize for efficiency by changing internal conversion parameters, this will improve conversion efficiency slightly, especially at low loads
(as low loads mean the fraction of power lost to the conversion is a larger fraction of the delivered output).

Efficiency optimization trades maximum slew rates for efficiency. If the unit needs to respond to rapidly changing DC voltages/currents (>100V/s) that are imposed by another DC Source or Load, the Efficiency Optimizations must be disabled.
Special attention is needed when an external source raises the DC bus voltage rapidly, as this may damage/destroy the converter. When this option is disabled the slew rates are substantially increased.

## Development

The ADB-PC-CH01 is for the most part a 'software defined converter'. This means that even after purchase the functionality may be expanded to support multiple modes or the behaviour of the unit may be changed to improve thingh like response times, or reliability.
Updates are available over the life of the converter. In case of any custom requirements please reach out to support.
