> [!UPDATE] {docsify-updated}
# Charging station overview
## Wiring considerations
There are many key components making up a charging station. Some of them are essential (like power converters for DC charging), others are required by their respective national standards (like ground fault monitoring devices). A properly designed charging station should be cost-optimized, but safe and compliant. Generally speaking, the lower the power, the fewer additional components would be installed, as they can significantly affect the price.

> [!WARNING]
> Always check national rules and requirements when designing a charging station. Do not rely on the following information to be accurate or even applicable.

### Input (mains) side protection

If the charger is powered from an existing 3-phase industrial power feed, the following equipment should be present in the installation:
- Circuit breakers of appropriate rating. Most likely power modules will have a separate breaker for the 24V supply powering the controllers or fans. Most power module manufacturers will require a separate circuit breaker for each power module.
- Residual-current device (RCD, RCCB, GFCI)
- Dedicated 3-phase mains filter (depending on EMC performance of your station and power modules, required standard limits – residential, industrial)

In case of a direct power grid connection, the situation gets more complicated, as a large high current circuit breaker and high voltage fuses might also be needed.

There is a big difference between AC charging stations and DC charging stations in terms of requirements for residual current monitoring. An AC station will require type B RCCB, unless a special type A RCCB that doesn’t get blinded by DC current is used. RCMB121 from Bender is an example of an RCCB that fulfills this requirement.

For DC charging stations, type A RCCB is sufficient, and additional Ground Fault monitoring is required (due to the isolated nature of DC charging).

### AC charging station residual current monitor
When building an AC charging station, keep in mind that EU rules differ from US rules on the limits.
There are several IEC 61851-1 compliant residual current monitors for AC charging station use, for example:
- Phoenix Contact EV-RCM-C1-AC30-DC6 (part number 1622450)
- Bender RCMB420E

### Power modules

Most power modules on the market will require you to put several units in parallel, to form fast DC charging stations (depending on the required power level). Typically, power modules span from 10 kW for older generation units, to 15-25 kW for most units on the market, to 75 kW per module. So a 150 kW station can have anything from 2 to 15 units in parallel.

The power modules will also vary greatly in additional capabilities. For example ADVANTICS power converters contain onboard ground fault monitoring of the DC output, as well as external voltage sensors, to measure voltage past the contactors or CHAdeMO diodes.

Different cooling concepts are used – they can be separated into following categories:
- Open-frame power supplies, requiring cold air to blow directly through power module components.
- Heatsink-based modules, requiring fresh air only on the main heatsink
- Water-cooled modules, relying on external heat exchangers.

### Ground fault monitoring

Applicable only for DC charging. Ground fault monitoring is performed by injecting low level balanced ground current (intentionally causing a small fault), and measuring impedance from output DC terminals to earth terminal. The limit level for monitored systems is 100 Ohm/V – resulting in the need of at least 50 kOhm of insulation for <500 VDC charging station (there are different requirements in different regions).

If power modules do not come equipped with a built-in ground fault monitor, an external one must be purchased and installed.


<div class="bigger-1000">

![Ground fault monitor installation - Sendyne SIM100MOD sensor](images/IMD.PNG "Ground fault monitor installation - Sendyne SIM100MOD sensor")
</div>
<figcaption style="text-align: center">Figure 8: Ground fault monitor installation - Sendyne SIM100MOD sensor</figcaption>

### Output DC contactors

AC charging stations do not perform power conversion, therefore only AC contactors are needed, and they are essential for operation (as the charger outlet must be de-energized when not connected to a vehicle).

For DC chargers, output contactors are not strictly necessary, provided that the power modules can remove/isolate the output voltage fast enough in case of cable release. Most charging stations will include output contactors.

### CHAdeMO diode

The CHAdeMO standard requires a diode in series with the positive output terminal (for unidirectional chargers). Some power modules come with the diode installed, others require it to be mounted externally. For V2X CHAdeMO, this diode is replaced with a precharge resistor with smaller contactor in series, and main bypass contactor. CCS does require output contactors, as CCS sequence includes smart precharge (voltage matching).

### CCS charging cable

A majority of CCS cables on the market are identical in their wiring. The following wires can be identified at the cable end:
- CP wire.
- PP wire – may not even be present. The PP wire is not used for DC charging, and cables typically have a resistor built-in between the PP and PE (ground) wires.
- PE ground (common high-gauge wire for power and signal ground).
- RTD PT1000 monitoring positive power terminal (2 terminals – one must be grounded).
- RTD PT1000 monitoring negative power terminal (2 terminals – one must be grounded).
- Positive DC high gauge wire (power delivery).
- Negative DC high gauge wire (power delivery).

> [!TIP]
> Some CCS cable manufacturers are notoriously bad at documenting their cable. If you end up probing with a multimeter, just to find which wire is which, you can always identify the RTD (temperature sensor) by being able to see around 1100 Ohms between them

### CHAdeMO charging cable

CHAdeMO charging cables vary to a much greater degree, mostly because of different ways of solenoid control and different temperature sensing technology. Often, CHAdeMO cable wiring has labeled pins as 1-10 (see  Figure 9: CHAdeMO pinout). The solenoid is not shown on this diagram.


<div class="bigger-1000">

![CHAdeMO pinout](images/Description-of-the-CHAdeMO-connector-pinout-and-schematic.jpg "CHAdeMO pinout")
</div>
<figcaption style="text-align: center">Figure 9: CHAdeMO pinout</figcaption>

### HMI (Human Machine Interface)

Often consisting of displays, indicators, buttons. Depending on the design and size of the charging station, anything from a few LEDs showing basic status, small OLED display, to a large LCD TV screen can be used. Typically, smaller and cheaper stations will opt for simpler interface, while high power public charging stations operators have the option to show advertisement on a large screen.

There are several ways to integrate a screen to the ADVANTICS charge controller. The simplest way is to use an industrial PC with a built-in screen, and communicate with the charge controller over the Ethernet interface. But it is also possible to use much cheaper systems, like a CAN bus capable microprocessor, and OLED display, communicating over CAN bus.

The topic of interface selection is left to the customer. A simple way is to use the provided CAN bus, and parse the interesting messages, like charging status, and display those on the screen.

## Interfaces

The ADM-CS-SECC should be considered as a development platform – experience with Raspberry Pi and similar eco-systems will be very relevant when working with the Charge Controller. Some of the interfaces are directly used by the CCS and CHAdeMO communication stacks, while others are left to customers to utilize.

### Power input

The controller expects 24V power. Consult specification sheet for supply requirements.

<div class="bigger-300">

![Power section - connector reference next to the pin](images/ADM-CS-SECC_multipart_power.svg "Power section - connector reference next to the pin")
</div>
<figcaption style="text-align: center">Figure 2: Power section - connector reference next to the pin</figcaption>

### CCS and AC interfaces

The CCS and AC interface consists of CP, PP lines, inlet lock and temperature sensor inputs. All of these signals are fully controlled by the communication stack – the user does not have to interact with them in any way. They simply need to be wired properly to the inlet cable.

> [!TIP]
> There are many different CCS and AC inlets and cables. Suitable cables are manufactured by typical suppliers such as Phoenix Contact, and are available in a wide price-range. However, beware of potential wiring differences. Consult your choice of cable with ADVANTICS.

<div class="bigger-300">

![CCS A interface - DC charging](images/ADM-CS-SECC_multipart_CCS_A.svg "CCS A interface - DC charging")
<figcaption style="text-align: center">Figure 3: CCS A interface - DC charging</figcaption>

![CCS B interface - AC charging only](images/ADM-CS-SECC_multipart_CCS_B.svg "CCS B interface - AC charging only")
</div>
<figcaption style="text-align: center">Figure 4: CCS B interface - AC charging only</figcaption>

### Inlet locking of AC interface

The only real difference between wiring DC CCS and AC charging is in the use of the inlet locking mechanism. The AC locking mechanism consists of a small DC motor, driving a pin in and out of the inlet. This motor prevents removal of the AC cable while charging is in progress. DC CCS always comes with cable built-in the station.
The locking mechanism is only needed when the AC inlet is installed on the station – it does not apply for stations with built-in AC cable directly (as the cable is then not removable, so no lock is needed).

### CHAdeMO interface

Just like the CCS interface, CHAdeMO is under full control of the communication stacks. The interface consists of SEQ1, SEQ2, Solenoid Positive and Negative lines, PROX, PERM lines, and a dedicated CAN bus.

> [!ATTENTION]
> CHAdeMO cables have even higher variance in wiring than CCS. Datasheets often miss critical information about solenoid control for example. There are two types of CHAdeMO solenoids – bistable ones, requiring having the solenoid wired between SOLENOID_P and SOLENOID_N outputs, and then monostable ones – requiring connection between SOLENOID_P and GROUND.

<div class="bigger-300">

![CHAdeMO interface pinout](images/ADM-CS-SECC_multipart_CHADEMO.svg "CHAdeMO interface pinout")
</div>
<figcaption style="text-align: center">Figure 5:CHAdeMO interface pinout</figcaption>

### Output contactor control

The charge controller has three independent relays, with normally open and common contacts available. Each relay is hard-wired to one interface respectively – AC, CCS and CHAdeMO. These relays provide an additional layer of HW safety – they can only be energized when certain conditions are fulfilled (for example CP state, or PERMIT signals). What the conditions are, depends on the standard.

These relays cannot be repurposed for other application – their sole purpose is to control output DC (or AC) contactors. In case this functionality is not required, they do not have to be used.

The customer can also use the output of these relays, and add an additional protection layer by wiring it through relays controlled by for example the power modules or other controllers (to potentially prevent the controller from successfully closing the output contactors). But such measures are not necessary, only optional. It’s much better to use the provided interlock line (see below).

### User system CAN bus

The charge controller has one dedicated CAN bus for connection to the customer’s systems. For example power modules, voltage and current sensors with CAN bus interface, HMI systems and similar eqiupment. This CAN bus is the main way of communication between ADVANTICS CCS and CHAdeMO stacks, and the power modules.

> [!TIP|label:CAN bus tip]
> Not all power modules use a CAN bus, some of them might require Ethernet, Modbus or RS-485. Customers can write their own applications running on the charge controller, converting the CAN bus communication into another interface – effectively creating a communications bridge. Typical use would be to listen to ADVANTICS CAN messages, and then convert and send them over RS-485, and vise-versa.

The CAN bus runs at speed of 500kbaud by default. There is no 120 Ohm termination on this bus, but it can be easily enabled by installing a wire jumper between pins CAN_TERM_BRIDGE1 and CAN_TERM_BRIDGE2. A built-in 120 Ohm resistor will then be automatically placed between CAN High and Low.

<div class="bigger-300">

![Communication pinout - CAN, RS485, Interlock, Current Loop, Ethernet, Antenna](images/ADM-CS-SECC_multipart_COMM.svg "Communication pinout - CAN, RS485, Interlock, Current Loop, Ethernet, Antenna")
</div>
<figcaption style="text-align: center">Figure 6: Communication pinout - CAN, RS485, Interlock, Current Loop, Ethernet, Antenna</figcaption>

### Digital inputs and outputs

There are four digital inputs and four digital outputs on the charge controller. Consult the specs sheet for levels. The outputs are 24V level logic, with push-pull stage. Inputs are 24V tolerant, but can be used also with 12V logic.
The digital inputs and outputs are fully user-configurable and controllable.

<div class="bigger-300">

![Digital input/output pinout and fans](images/ADM-CS-SECC_multipart_dig_IO.svg "Digital input/output pinout and fans")
</div>
<figcaption style="text-align: center">Figure 7: Digital input/output pinout and fans</figcaption>

### LED outputs

LED outputs have 12V output drive, high side driver, with 100mA current limit per channel. They are fully user configurable and controllable, and can also be used to drive other loads besides driving LEDs (as long as limits are not exceeded).


### Fan outputs

The two fan outputs are meant to be used with four pin fans – with dedicated PWM speed control. The interface expects open collector fan PWM input. The voltage or power of the fan does not play a role (both 12V and 24V fans can be used), as they are externally powered, and only controlled by the controller.
Currently, these outputs are user configurable and controllable. We are in process of adding automatic fan control as a SW configuration option.

### RS-485

The RS-485 serial interface comes with built-in 120 Ohm termination. The interface is fully user configurable and controllable, including speed and master/slave configuration. A typical application could be a point-to-point connection to a card-reader inside the charger cabinet.

### Interlock

The interlock line is an open-collector output, with a 4.7 kOhm pull-up to 24V. This signal is bidirectional, allowing sampling as well as assertion from within the controller. It can be used by power modules to signalize failure, or by a door sensor to cause shutdown in case of open door. User systems can assert the interlock by grounding the interlock line.

> [!WARNING]
> The interlock line is hard-wired to the system, and will override the controller’s capability to close the output contactors. When used, it will guarantee the opening of output contactors in case of signaled fault (the protection works irrespective of  software)

### Current loop

The current loop input and output forms a chain of 20mA, that can be monitored and interrupted (door switches, relays). The primary use of this line is E-STOP button on the outside of the charger and cabinet door interlocks. Unlike the interlock line, the E-STOP is not hardwired to the output contactor control like the interlock is, and therefore is the preferred way for cleanly stopping the charging (instead of abruptly interrupting it in case of the interlock line).

### 4G network connectivity

The ADM-CS-SECC can be fit with a standard mPCIe SIMCOM 4G module (7600E series). The Mini-PCI Express slot on the charge controller only implements the USB interface (which provides sufficient functionality for most types of wireless mPCIe cards). Consult ADVANTICS before using alternative brands or models of cards, as compatibility cannot be guaranteed.

The charge controller does not require any connectivity for normal operation. Therefore the configuration of the network is left completely to the user. The typical use case would be connection over OCPP to the cloud, or internet distribution (forwarding a 4G connection to the Ethernet interface on the charge controller).
