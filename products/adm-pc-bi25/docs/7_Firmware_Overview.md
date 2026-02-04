# **4.2. Firmware Overview**

!!! warning 
    The BI25 module is not able to limit the output current to a low resistance load. Thus, a current limiting device must be installed in series with the BI25 output.

!!! tip 
    We recommend connecting the BP25 in series with the output of the BI25. This will allow for the BI25 to provide an isolated output voltage with the BP25 limiting the output current and providing a large control range for the output voltage.

## 

## **4.2.1. System Configuration**

{{ figure('../assets/Figure14.png', 'Chaining and termination diagram') }}

* Input: A DC voltage source is connected to **the side A of the** BI25.  
* Intermediate Stage: The Output (Side B) is connected to a non isolated DC/DC converter which provides the output current limiting and voltage control range. An ADM-PC-BP25 may be used for this.The output of the non-isolated DC-DC is connected to the load.

!!! note "Startup Condition"
To ensure safe operation and protect the controller, a startup condition is implemented. The voltage following mode will only be enabled when the input DC voltage to the BI25 is **above 500V**. This acts as a protective measure to prevent the controller from starting under potentially unsafe low-voltage conditions.

!!! warning 
    Please take care to not operate the module close to the temperature limits, as it will reduce the lifetime of the unit.

## **4.2.2. Control Modes**

The BI25 module is operated in ‘Voltage-Following’ mode. In ‘Voltage-Following’ the BI25 will provide the same voltage on side B as it sees on side A. In this mode it will also compensate for the voltage drop across the isolation transformer. Side B will appear as a low impedance voltage source.

## **4.2.3. Operational Ranges**

!!! warning 
    Exceeding the recommended range may lead to a deterioration of the device resulting in a shorter operational life span and reduced reliability.

To ensure a long life and reliable operation of the converter, the voltage, current, power and temperature should be within the following ranges during operation:

Table 3\.

| Parameters | Values |
| :---- | :---- |
| **Voltage Range** | Port A: **600 V** to **950 V**  Port B: **600 V** to **950 V** |
| **Current Range** | Bidirectional current range: **60 A** |
| **Thermal Range** | The temperature of the power transistors may not exceed **90°C**. The temperature of the Transformers may not exceed **110°C.** |

## 

## **4.2.4. Protection mechanisms**

### Over-current protection

The BI25 module has an output current protection at 75 A. If a larger current is detected by the control system, the module will cease operation. A further transient protection is set to 95 A. If the BI25 exceeds this current at any point in time operation will cease immediately as this limit is implemented in hardware.

### Over-voltage protection

!!! warning 
    Excessive voltage on the input ports may lead to catastrophic failure of the BI25. It relies on the overall system to prevent these circumstances.


The BI25 module also monitors the voltage on both ports. If a voltage larger than 1050 V is detected by the control system, the module will cease operation. A further transient protection is set to 1150 V. If the BI25 exceeds this voltage at any point in time operation will cease immediately as this limit is implemented with hardware comparators. The BI25 has no means of protecting itself against excessive voltage placed on its ports. Thus, a large voltage spike on either port A or B may destroy the device.

### Over-temperature protection

!!! warning 
    While the protection mechanisms will stop the converter from operating, the communication interface stays active. This will allow re-enabling the converter after conditions have entered nominal ranges. 

If the temperature of the power switches exceeds 90°C or the temperature of the transformers exceeds 110°C the module will cease operations. When detecting the overheating condition, the converter will stop operating but without tripping the interlock line. This means that other modules chained in the same bus will still continue normal operation.

## **4.2.5. Communication Interface**

The BI25 communication interface consists of a CAN 2.0B interface configured at 500 kbit/s with extended address mode and an open collector interlock line (INTLK).

### CAN bus

Please see the module CAN database section for the protocol description. Up to 32 modules of the same type can be connected to the same can bus (daisy chained when using the connectors on the BI25). The limiting factor is the available stack positions, which is used to distinguish multiple BI25 units connected to the same CAN bus.

The module is controlled via ‘signals’. Signals similar to the ‘register’ concept are also often found used on can buses.

### Can Bus Termination

CAN bus termination is necessary for correct operation. To ensure stable communications and good noise margin, no more or less than two termination resistors should be present on the CAN bus, ideally at each end of the chain. If the CAN bus is branched, the termination resistors should be placed at the two points farthest away in the chain, and unterminated branches should be kept at minimum length.

The power module contains an on-board CAN termination resistor per each CPT connector, which can be activated by bridging pins 6 and 3 of the CPT connector with a simple wire (shown on the chaining diagram). The wire used to bridge pins 6 and 3 should be as short as possible to minimize noise pickup, less than 5 cm.

### Interlock Line

The interlock pin on the interface connector is used to put the system in a safe state, independent of the CAN communications, for user safety and in case of faults. The interlock line is normally pulled high by pull-up resistors to \+24 V on each individual module, and any module can pull the line low to put the whole system in a safe state (that is, to trigger the system-wide interlock). Each module has a 4k7 Ω pull-up resistor. Interlock is latching from the module causing it – it will be unlatched by the CPU request (CAN bus request from the user system). Other modules in the system will not latch external interlocks, they will simply act upon them. Interlock is a purely HW-based system, using logic gates and comparators. The CPU cannot overrule the interlock.

!!! tip 
    All modules start with tripped interlock after reset. The user must request interlock clearance over the CAN bus. Otherwise the module cannot be started.

### Interface Power Supply

Control power for the modules is nominally \+24 V DC. Upper and lower limits and maximum current draw are given in the Specification Sheet. Two pins each are used for \+24 V and ground to minimize voltage drop across the wires in installations with a large number of modules and/or long wiring. When planning the communications chain, ensure that no single connector is carrying more than 3 A in total, given the worst-case current requirement of the individual modules. Note that in larger installations, the voltage drop across the wires can be significant, and this will affect the supply voltage of the individual modules.

Voltage drop across the communications ground wires will change the apparent logic levels at each module. Ensure that the voltage drop between any two modules does not exceed 1 volt. The nominal resistance of the recommended wire is 50 mΩ per meter. Two wires are used in parallel for ground, giving a total ground resistance of 25 mΩ per meter.

### Multi-Engineering Toolkit for ADVANTICS 

Multi-Engineering Toolkit for ADVANTICS (ETKA) is available for both Windows and Linux, consisting of stand-alone applications to work with ADVANTICS modules during the development stage. Its user-friendly GUI together with a PeakCAN USB adapter allows customers to rapidly test and verify modules without writing any code.

{{ figure('../assets/Figure15.png', 'ETKA user interface') }}

The user only needs to:

1. Connect to an available CAN bus channel.  
2. Click the tab **open**, and select all the desired modules to be controlled.  
3. Select the slave address of each of the modules to be connected to.  
4. (Optional) The slave address of a module can be modified by opening the **Stack Manager**, next to the **connection** button.

Once the communication is well established and module information is read back, follow the Quick Start procedure to start operating the module.
