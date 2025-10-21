# Charge station overview

There are many key components making up a charging station. Some of them are essential (like power converters for DC charging), others are required by their respective national standards (like ground fault monitoring devices). A properly designed charging station should be cost-optimized, but safe and compliant. Generally speaking, the lower the power, the fewer additional components would be installed, as they can significantly affect the price.

!!! warning
    Always check national rules and requirements when designing a charging station. Do not rely on the following information to be accurate or even applicable.


## Input (mains) side protection

If the charger is powered from an existing 3-phase industrial power feed, the following equipment should be present in the installation:
- Circuit breakers of appropriate rating. Most likely power modules will have a separate breaker for the 24V supply powering the controllers or fans. Most power module manufacturers will require a separate circuit breaker for each power module.
- Residual-current device (RCD, RCCB, GFCI)
- Dedicated 3-phase mains filter (depending on EMC performance of your station and power modules, required standard limits – residential, industrial)

In case of a direct power grid connection, the situation gets more complicated, as a large high current circuit breaker and high voltage fuses might also be needed.

There is a big difference between AC charging stations and DC charging stations in terms of requirements for residual current monitoring. An AC station will require type B RCCB, unless a special type A RCCB that doesn’t get blinded by DC current is used. RCMB121 from Bender is an example of an RCCB that fulfills this requirement.

For DC charging stations, type A RCCB is sufficient, and additional Ground Fault monitoring is required (due to the isolated nature of DC charging).

## AC charging station residual current monitor
When building an AC charging station, keep in mind that EU rules differ from US rules on the limits.
There are several IEC 61851-1 compliant residual current monitors for AC charging station use, for example:
- Phoenix Contact EV-RCM-C1-AC30-DC6 (part number 1622450)
- Bender RCMB420E

## Power modules

Most power modules on the market will require you to put several units in parallel, to form fast DC charging stations (depending on the required power level). Typically, power modules span from 10 kW for older generation units, to 15-25 kW for most units on the market, to 75 kW per module. So a 150 kW station can have anything from 2 to 15 units in parallel.

The power modules will also vary greatly in additional capabilities. For example ADVANTICS power converters contain onboard ground fault monitoring of the DC output, as well as external voltage sensors, to measure voltage past the contactors or CHAdeMO diodes.

Different cooling concepts are used – they can be separated into following categories:
- Open-frame power supplies, requiring cold air to blow directly through power module components.
- Heatsink-based modules, requiring fresh air only on the main heatsink
- Water-cooled modules, relying on external heat exchangers.

## Ground fault monitoring

Applicable only for DC charging. Ground fault monitoring is performed by injecting low level balanced ground current (intentionally causing a small fault), and measuring impedance from output DC terminals to earth terminal. The limit level for monitored systems is 100 Ohm/V – resulting in the need of at least 50 kOhm of insulation for <500 VDC charging station (there are different requirements in different regions).

If power modules do not come equipped with a built-in ground fault monitor, an external one must be purchased and installed.


<div class="bigger-1000">

![Ground fault monitor installation - Sendyne SIM100MOD sensor](images/IMD.PNG "Ground fault monitor installation - Sendyne SIM100MOD sensor")
</div>
<figcaption style="text-align: center">Figure 8: Ground fault monitor installation - Sendyne SIM100MOD sensor</figcaption>

## Output DC contactors

AC charging stations do not perform power conversion, therefore only AC contactors are needed, and they are essential for operation (as the charger outlet must be de-energized when not connected to a vehicle).

For DC chargers, output contactors are not strictly necessary, provided that the power modules can remove/isolate the output voltage fast enough in case of cable release. Most charging stations will include output contactors.

## CHAdeMO diode

The CHAdeMO standard requires a diode in series with the positive output terminal (for unidirectional chargers). Some power modules come with the diode installed, others require it to be mounted externally. For V2X CHAdeMO, this diode is replaced with a precharge resistor with smaller contactor in series, and main bypass contactor. CCS does require output contactors, as CCS sequence includes smart precharge (voltage matching).

## CCS charging cable

A majority of CCS cables on the market are identical in their wiring. The following wires can be identified at the cable end:
- CP wire.
- PP wire – may not even be present. The PP wire is not used for DC charging, and cables typically have a resistor built-in between the PP and PE (ground) wires.
- PE ground (common high-gauge wire for power and signal ground).
- RTD PT1000 monitoring positive power terminal (2 terminals – one must be grounded).
- RTD PT1000 monitoring negative power terminal (2 terminals – one must be grounded).
- Positive DC high gauge wire (power delivery).
- Negative DC high gauge wire (power delivery).

!!! tip
    Some CCS cable manufacturers are notoriously bad at documenting their cable. If you end up probing with a multimeter, just to find which wire is which, you can always identify the RTD (temperature sensor) by being able to see around 1100 Ohms between them


## CHAdeMO charging cable

CHAdeMO charging cables vary to a much greater degree, mostly because of different ways of solenoid control and different temperature sensing technology. Often, CHAdeMO cable wiring has labeled pins as 1-10 (see  Figure 9: CHAdeMO pinout). The solenoid is not shown on this diagram.


<div class="bigger-1000">

![CHAdeMO pinout](images/Description-of-the-CHAdeMO-connector-pinout-and-schematic.jpg "CHAdeMO pinout")
</div>
<figcaption style="text-align: center">Figure 9: CHAdeMO pinout</figcaption>

## HMI (Human Machine Interface)

Often consisting of displays, indicators, buttons. Depending on the design and size of the charging station, anything from a few LEDs showing basic status, small OLED display, to a large LCD TV screen can be used. Typically, smaller and cheaper stations will opt for simpler interface, while high power public charging stations operators have the option to show advertisement on a large screen.

There are several ways to integrate a screen to the ADVANTICS charge controller. The simplest way is to use an industrial PC with a built-in screen, and communicate with the charge controller over the Ethernet interface. But it is also possible to use much cheaper systems, like a CAN bus capable microprocessor, and OLED display, communicating over CAN bus.

The topic of interface selection is left to the customer. A simple way is to use the provided CAN bus, and parse the interesting messages, like charging status, and display those on the screen.
