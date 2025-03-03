> [!UPDATE] {docsify-updated}
# Interfaces

The ADM-CS-EVCC is an electric vehicle subsystem. It cannot function on its own, but when integrated
in a vehicle, it will provide AC and DC charging abstraction through a simple CAN bus interface.
Thanks to charge inlet monitoring and control, as well as DC contactor control, very little is
required from the vehicle to get the system up and running.

<div class="bigger-1000">

![CINCH ModICE connectors](images/PEV_connector.png "CINCH ModICE connectors")
</div>
<figcaption style="text-align: center">Figure 2: CINCH ModICE connectors</figcaption>

## Power input

The controller expects 12V or 24V power. It is designed to handle the typical environment of
automotive 12/24V systems. For user convenience, it is possible to use for example 12V
contactors/inlets in a 24V system, as the contactor drivers are powered from a separate input.

Consult the specifications sheet for current requirements.

<div class="bigger-300">

![Power section - connector reference next to the pin](images/ADM-CS-EVCC_multipart_power.svg "Power section - connector reference next to the pin")
</div>
<figcaption style="text-align: center">Figure 3: Power section - connector reference next to the pin</figcaption>

## MCS interface

The MCS interface consists of 
- TRXP (MCS PHY1), TRXN (MCS PHY2) for 10baseT1S communication.
- CE and ID lines
- inlet lock.
- temperature sensor inputs.
- MCS Auxiliary Voltage and MCS_CE_Sv4_ext line to request auxilary power fronm the charger (not used for now).
- CAN_H_TEMP_SENSOR, CAN_L_TEMP_SENSOR and CAN_TEMP_SENSOR_GND: Can be used when the MCS inlet is equipped with a CAN bus temperature sensor. (not enabled yet)

All of these signals are fully controlled by the communication stack – the user does not have to
interact with them in any way. They simply need to be wired properly to the inlet cable.

<div class="bigger-300">

![MCS Inlet](images/MCS_inlet.svg "MCS Inlet")
</div>
<figcaption style="text-align: center">Figure 4: MCS Inlet</figcaption>

## Inlet locking

The MCS inlet contains a motorized locking mechanism, designed to prevent removal of the cable during
the charging cycle (when hazardous voltages can be present), and to prevent cable theft. The inlet
lock motor is a simple DC motor, driving a locking pin. For proper operation, 12V (or 24V) is being
applied in different polarities to the DC motor to push pin into the inlet, or to extract it.

> [!TIP|label:Loss of power]
> In the case of power loss or charger/vehicle failure, all inlet locking
> mechanisms come with a manual release lever. This lever is accessible from the inside of the
> vehicle – typically accessed by removing carpet on the side in the trunk. Do not use the manual
> release during operation – only in case of emergencies.

## Temperature monitoring

The MCS inlet comes with integrated PT1000 temperature sensors. They should be directly connected to
the EVCC. During high current charging, it is possible to encounter dangerous temperatures
(especially if the inlet or cable is damaged). The EVCC will shut down the charging cycle in case
limits are exceeded.
Some MCS inlets current sensor communicate over CAN bus, for that you can use the pins: CAN_H_TEMP_SENSOR, CAN_L_TEMP_SENSOR and CAN_TEMP_SENSOR_GND. (not enabled yet)


## DC fast charge contactors control

The charge controller has two independent outputs for controlling the positive and negative fast
charge DC contactors. Also there is an extra digital input for each one of them, for potential
welding detection (provided that the contactors have auxiliary contacts built-in).

The purpose of these contactors is to ‘expose’ the vehicle battery to the charger during fast
charging. Fast charging effectively bypasses the onboard charger in the vehicle, and instead allows
the charging station direct access to the battery. In order for this operation to be safe, a few
conditions must be met. In simple terms, the charger and car will first negotiate required voltage
and current, perform internal tests (like insulation test), followed by a precharge request. During
precharge, the EV requests the charger to supply a voltage matching the battery voltage. The vehicle
will continuously monitor the inlet voltage, and when the charger reaches the requested voltage, the
charge controller will close the DC fast charge contactors.

The last feature of the DC contactor control is external power input. This input needs to be wired
to a power supply (typically a battery) capable of sourcing enough current for the contactors to
operate. In most applications, the CONTACTOR_POWER pin will simply be wired to the same supply as
the main power input. The only reason for it to be wired in a different way is to allow mixed 12V
and 24V operation (24V trucks using 12V contactors, for example).

<div class="bigger-300">

![DC fast charge contactors pinout](images/ADM-CS-EVCC_multipart_contactors.svg "DC fast charge contactors pinout")
</div>
<figcaption style="text-align: center">Figure 7: DC fast charge contactors pinout</figcaption>

## Vehicle CAN bus

The charge controller has one dedicated CAN bus for the integration with the vehicle. The customer
is expected to provide the controller with the necessary information over CAN bus, for the charging
to work properly. The EVCC will report useful/necessary information about the charge process itself.

The CAN bus runs at a speed of 500 kbaud by default. There is no 120 Ohm termination on this bus by
default, but it can be easily enabled by switching the DIP switch on the PCB into ON position. This
will connect a 120 Ohm termination resistor between CAN high and low. There should only be 2
terminations on the CAN bus – ideally on both end-points of the CAN chain.

![Location of the CAN bus termination enable switch](images/CAN_term.jpg "Location of the CAN bus termination enable switch")
<figcaption style="text-align: center">Figure 8: Location of the CAN bus termination enable switch</figcaption>

> [!TIP|label:CAN bus tip]
> If you don’t see all the CAN messages you were expecting on the bus, the periodicity is wrong, or
> no messages are shown at all, the CAN bus termination could be missing. CAN bus should have two
> terminations, but on the bench will also typically work with just one, or three.

<div class="bigger-300">

![CAN bus, Charge STOP and Ethernet](images/ADM-CS-EVCC_multipart_COMM.svg "CAN bus, Charge STOP and Ethernet")
</div>
<figcaption style="text-align: center">Figure 9: CAN bus, Charge STOP and Ethernet</figcaption>

## Charge stop

The charge stop input allows users to terminate the charging in a clean way – by using a (user
operated) push button for example. It behaves as if the charger side was requesting a normal stop.

The Charge stop input should be pulled up to trigger a stop request

It is also possible to terminate the charge over the CAN bus.

## Digital inputs and outputs

There are two digital inputs and three digital outputs on the charge controller.
The digital inputs and outputs are fully user-configurable and controllable (provided the user
writes an application for their control).

<div class="bigger-300">

![Digital IO](images/ADM-CS-EVCC_multipart_dig.svg "Digital IO")
</div>
<figcaption style="text-align: center">Figure 10: Digital IO</figcaption>

### Digital Outputs
The outputs are push-pull capable, supplied from the input power of the controller (so are either 12V or 24V). Can be used to drive loads up to 100mA.

For GPIO control, please refer to sections [**Manual GPIO control**](charge-controllers/sys3_user/gpios.md#manual_gpio_control) and [**GPIO control in your application**](charge-controllers/sys3_user/gpios.md#gpio_control_in_your_application)

### Digital Inputs
The inputs are 24V tolerant but are also compatible with 12V logic level, the maximum voltage on this pin is about 30V, and have a weak 10 kOhm pulldown.
Transition to ‘1' from 9V sets the input to ON. It will then hold '1’ until the voltage drops under 3V.
## LED outputs

LED outputs are powered from MCS lock power (so they share the same voltage level). A high side
drivers are used, with a current limit of 100mA per channel. LEDs are fully user configurable and
controllable, and can be used for to power other loads (as long as limits are not exceeded).

## Ethernet

During R&D, Ethernet can be used to deploy FW and communicate with the unit. The RJ45 connector is
located on the opposite side from the main connector, and is inaccessible once the box is closed.
Consult the SW Development Manual for how to work with the system over an SSH connection.

# Requirement for inlet monitoring

To be compliant with the MCS standards, the vehicle must contain voltage sensors for monitoring of
the inlet DC pins, a current sensor for measuring the charge current, and a battery voltage monitoring.

> [!WARNING]
> It is not sufficient to just measure the HV battery voltage. The user MUST monitor the inlet
> voltage, as there are DC contactors separating the battery from the inlet when not charging (so
> the battery voltage does not equal inlet voltage!).

For simplicity of wiring, the user can install a combined voltage and current sensor, such as the
Isabellenhutte IVT-S. The sensor should simultaneously monitor the battery voltage, the inlet
voltage as well as charging current. Depending on the target charging current, For example
**IVT-S-300-U3-I-CAN2-12/24** model (300A, 3 voltage sensors, no CAN termination, isolated) can be
used. ADVANTICS supplies the IVT-S-1k-U3-I-CAN2-12/24 model, as the same unit can be used for higher
current applications (like main battery current sensor), and the loss of resolution with higher
current full-scale is not critical in this application.

<div class="bigger-300">

![Isabellenhutte IVT-S current sensor](images/IVT-S.JPG "Isabellenhutte IVT-S current sensor")
</div>
<figcaption style="text-align: center">Figure 11: Isabellenhutte IVT-S current sensor</figcaption>
