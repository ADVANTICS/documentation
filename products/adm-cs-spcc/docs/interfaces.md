# Interfaces

## Power input

The controller expects 24V power. Consult specification sheet for supply requirements.

## MCS interface

The MCS interface consists of 
- TRXP (MCS PHY1), TRXN (MCS PHY2) for 10baseT1S communication.
- CE and ID lines
- temperature sensor inputs.

All of these signals are fully controlled by the communication stack – the user does not have to interact with them in any way. They simply need to be wired properly to the inlet cable.

<div class="bigger-300">

<img src="assets/MCS_inlet.svg" alt="MCS Interface">

</div>
<figcaption style="text-align: center">Figure 4: MCS Interface</figcaption>

## CCS and AC interfaces

The CCS and AC interface consists of CP, PP lines, inlet lock and temperature sensor inputs. All of these signals are fully controlled by the communication stack – the user does not have to interact with them in any way. They simply need to be wired properly to the inlet cable.

!!! tip
    There are many different CCS and AC inlets and cables. Suitable cables are manufactured by typical suppliers such as Phoenix Contact, and are available in a wide price-range. However, beware of potential wiring differences. Consult your choice of cable with ADVANTICS.


## Inlet locking of AC interface

The only real difference between wiring DC CCS and AC charging is in the use of the inlet locking mechanism. The AC locking mechanism consists of a small DC motor, driving a pin in and out of the inlet. This motor prevents removal of the AC cable while charging is in progress. DC CCS always comes with cable built-in the station.
The locking mechanism is only needed when the AC inlet is installed on the station – it does not apply for stations with built-in AC cable directly (as the cable is then not removable, so no lock is needed).

## CHAdeMO interface

Just like the CCS interface, CHAdeMO is under full control of the communication stacks. The interface consists of SEQ1, SEQ2, Solenoid Positive and Negative lines, PROX, PERM lines, and a dedicated CAN bus.

!!! attention
    CHAdeMO cables have even higher variance in wiring than CCS. Datasheets often miss critical information about solenoid control for example. There are two types of CHAdeMO solenoids – bistable ones, requiring having the solenoid wired between SOLENOID_P and SOLENOID_N outputs, and then monostable ones – requiring connection between SOLENOID_P and GROUND.


## Output contactor control

CONTACTOR_ENABLE will be set to logic level 0 on SPCC when the following requirements are met for each pistol:

**For MCS Charging**
- CE_OK: Vehicle sets CE state C (power is allowed)
- HW safety conditions are met: A set of HW safety conditions should be met (defined below)
- Charge application or user requests closing contactors

**For CCS Charging**
- CP_OK: Vehicle sets CP state C (power is allowed)
- HW safety conditions are met: A set of HW safety conditions should be met (defined below)
- Charge application or user requests closing contactors

**For CHAdeMO Charging**
- CHAdeMO_OK (CHAdeMO_PERM_OK): PERM line from the vehicle is True
- HW safety conditions are met: A set of HW safety conditions should be met (defined below)
- Charge application or user requests closing contactors

### HW safety conditions:
All of the following must be met:

- No interlock line trip.
- CLOOP_OUT connected to CLOOP_IN.
- No overtemperature detected (`PT1KS_C` and `PT1KS_D` either: Connected to GND when not in use, or Temperature is below 110°C.)

## User system CAN bus

The charge controller has one dedicated CAN bus for connection to the customer’s systems. For example power modules, voltage and current sensors with CAN bus interface, HMI systems and similar eqiupment. This CAN bus is the main way of communication between ADVANTICS MCS, CCS and CHAdeMO stacks, and the power modules.

!!! tip "CAN bus tip"
    Not all power modules use a CAN bus, some of them might require Ethernet, Modbus or RS-485. Customers can write their own applications running on the charge controller, converting the CAN bus communication into another interface – effectively creating a communications bridge. Typical use would be to listen to ADVANTICS CAN messages, and then convert and send them over RS-485, and vise-versa.

The CAN bus runs at speed of 500kbaud by default. There is no 120 Ohm termination on this bus, but it can be easily enabled by installing a wire jumper between pins CAN_TERM_BRIDGE1 and CAN_TERM_BRIDGE2. A built-in 120 Ohm resistor will then be automatically placed between CAN High and Low.

## Digital inputs and outputs

There are four digital inputs and four digital outputs on the charge controller.
The digital inputs and outputs are fully user-configurable and controllable.

The digital outputs can be configurable via CAN bus. For that refer to the configuration and CAN bus generic interface sections. (not available yet)

For manual GPIO control, please refer to sections [**Manual GPIO control**](charge-controllers/sys3_user/gpios.md#manual_gpio_control) and [**GPIO control in your application**](charge-controllers/sys3_user/gpios.md#gpio_control_in_your_application)

### Digital Inputs
The inputs are 24V tolerant but are also compatible with 12V logic level, the maximum voltage on this pin is about 30V, and have a weak 10 kOhm pulldown.
Transition to ‘1' from 9V sets the input to ON. It will then hold '1’ until the voltage drops under 3V.

### Digital Outputs
The outputs are 24V level logic, with push-pull stage, max. 100 mA (sink or source).

### Temperature Sensors Inputs
The SPCC is equipped with 4 PT1000 inputs. Both the `PT1KS_C` and `PT1KS_D` temperature sensor inputs incorporate a hardware-level safety mechanism that immediately triggers an emergency shutdown when measured temperatures exceed 110°C.

!!! warning
    The `PT1KS_C` and `PT1KS_D` temperature inputs should be connected to GND when not in use.


## LED outputs
LED outputs have 12V output drive, high side driver, with 100mA current limit per channel. They are fully user configurable and controllable, and can also be used to drive other loads besides driving LEDs (as long as limits are not exceeded).

## RS-485
The RS-485 serial interface comes with built-in 120 Ohm termination. The interface is fully user configurable and controllable, including speed and master/slave configuration. A typical application could be a point-to-point connection to a card-reader inside the charger cabinet.

On the Linux system, the serial port is exposed on `/dev/ttyS1`. The kernel has been configured to apply the right settings for it from the start (ie. polarity and the RTS flag).

## Interlock
The interlock line is an open-collector output, with a 4.7 kOhm pull-up to 24V. This signal is bidirectional, allowing sampling as well as assertion from within the controller. It can be used by power modules to signalize failure, or by a door sensor to cause shutdown in case of open door. User systems can assert the interlock by grounding the interlock line.

!!! warning
    The interlock line is hard-wired to the system, and will override the controller’s capability to close the output contactors. When used, it will guarantee the opening of output contactors in case of signaled fault (the protection works irrespective of  software)


## Current loop
The current loop input and output forms a chain of 20mA, that can be monitored and interrupted (door switches, relays). The primary use of this line is E-STOP button on the outside of the charger and cabinet door interlocks. Unlike the interlock line, the E-STOP is not hardwired to the output contactor control like the interlock is, and therefore is the preferred way for cleanly stopping the charging (instead of abruptly interrupting it in case of the interlock line).
