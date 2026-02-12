# 5. Installation

!!! warning 
    Please do not place the unit at an angle or rest it on its connectors, as this may damage the 8-pin JST interface. Ensure the module is always supported on a flat, stable surface and properly aligned before mounting.

## 5.1. Mounting and assembly procedure

Recommended accessories are as follows:

* Construction glue (DOWSIL 744\)  
* Thermal paste (AAVID, T-Grease 2500\)  
* Screw ISO 14579 M5 x 60  
* Screws BN 10649 M5 x 6 .. 8  
* Washer DIN 125-A M5  
* Washer DIN 127-A M5  
* Tool: Screwdriver bits ¼”, Torx, Size X25

{{ figure('../assets/Figure4.png', 'Recommend accessories required for mounting and assembly') }}

## 5.2. Step-by-step guide

{{ figure('../assets/Figure5.png', 'Visual overview of steps 1 to 3') }}

1. Clean the surface of the cooler degrease.  
2. Apply the thermal grease lightly on the purple area.  
3. Apply the construction glue on the capacitor (recommended for systems exposed to vibration as implementation on board of vehicles).  

{{ figure('../assets/Figure6.png', 'Visual overview of step 5') }}

4. Place the module on the cooler.

{{ figure('../assets/Figure7.png', 'Visual overview of step 4') }}

5. Place screws with washers into the holes.  

6. Apply initial tightening torque on screws:  
   Torque: 2.5 Nm (Aluminium base)

!!! warning 
    Torque is necessary to be applied again after the first heat up cycle. Make sure the circuit is off, cooled down and free from any residual current. Finally, repeat tightening all the screws. 

{{ figure('../assets/Figure8.png', 'Example of final assembly of power wires and power terminal screws') }}

## 5.3. Power terminals

The power modules use SMD terminals for connecting the power cables or bus bars. The thread is M5, and the maximum length of a screw can be 6 mm, measured from the top of the terminal. Whether a wire or bus bar is used, it is absolutely essential that no constant force sideways is applied on the terminal. Design bus bars with stress reliefs and secure the cables to prevent excessive force or vibrations on the terminals.

{{ figure('../assets/Figure9.png', 'Recommended screws.') }}

Recommended screws: Screw ISO 14583-2011 M5 x 6 mm for one lug, M5 x 8 mm for two lugs.

Recommended tightening: 2 Nm, maximum nominal torque 3 Nm.

Recommended maximum cable cross section: mm²

!!! warning
    If a longer screw is used, it will push against the PCB as it is screwed in, leading to pull the terminal out of the PCB. If this happens, the converter will be destroyed, causing a safety hazard, and warranty voided.

## 5.4. Power wiring

It is recommended to lead the wires by the shortest way out from PCB and avoid crossing and touching the PCB of the source module or any other module.

ADVANTICS recommends RADOX® cables from the company HUBER+SUHNER. Guidelines on which cable to use can be visited online: [Current carrying capacity of RADOX® 125 single core and multi core cables](http://www.beichang.cn/pdf/RADOX%20CURRENT%20CARRYING%20CAPACITY.pdf).

The assembly engineer needs to take into account the final number, position, cover of cables and ambient temperature to choose the correct cross-section. These rules are recommended for cables longer than 5 cm. Shorter cables can be used with smaller cross sections due to the cooling effect of the M5 SMD power terminals.

## 5.5. Communication terminal and wiring

{{ figure('../assets/Figure10.png', 'Pintout of the CPT-connector pins 1-8') }}


{{ figure('../assets/Figure11.jpeg', 'JST CPT crimping tool WC-CPT021') }}


All ADVANTICS modules have a common interface for control and readout. The interface consists of a CAN bus for control and status reporting, and an interlock line (INTLK) for safety. Additionally, the interface connectors also include power distribution for the control section of the modules. Each module is provided with two interface connectors that are completely identical in pinout, allowing chaining of the modules without using branched cables or a distribution hub.

The interface connector mounted on every power converter is an 8-pin CPT series automotive connector with a latch, manufactured by JST.

The modules use the SM08B-CPTK male connector, and the mating female connector is model number 08CPT-B-2A. The pins used for the female connector are part number SCPT-A021GF-0.5, which can be crimped using the WC-CPT021 crimping tool. These terminals are made for use with 22 AWG (0.3 mm2) wire with an outer diameter of 1.4 mm. The wires for each connector should be bundled tightly together, to reduce the amount of electrical noise picked up from the environment. Unshielded communications cables should not be near the power wiring. CAN bus High and Low should be twisted (form a twisted pair). JST CPT product page can be visited online: [CPT Connector](https://www.jst-mfg.com/product/index.php?series=477).

Table 3. Pinout of the CPT connector

| JST CPT pin | Name | Description |
| :---: | :---: | :---: |
| 1 | \+24V power | Interface and control power |
| 2 | Interlock | Open collector, 24V pullup |
| 3 | Termination | See CAN bus termination |
| 4 | Signal ground | Interface ground |
| 5 | \+24V power | Interface and control power |
| 6 | CAN HIGH | Twisted pair between 6,7 |
| 7 | CAN LOW | Twisted pair between 6,7 |
| 8 | Signal ground | Interface ground |

> **Note:** ADVANTICS has the mating CPT connector in stock, already crimped and ready for use. Please contact us for purchase information.

## 5.6. Module Chaining

{{ figure('../assets/Figure12.jpeg', 'An example of a 1:1 chaining cable') }}


{{ figure('../assets/Figure13.png', 'Chaining and termination diagram') }}

The total end-to-end wire length of the network should not exceed 10 m with multiple power modules installed. The CAN standard specifies up to 100 m end-to-end cable length, but in an environment with high noise and multiple connection stubs, this value is too high. In larger systems, it can be beneficial or even necessary to split up the modules into several separate CAN networks.

If you are planning to deploy a large network of more than 24 nodes, consult with ADVANTICS engineering team for special assistance.

## 5.7. Firmware setup

### Step 1 – Clear interlock

Modules have two types of interlock signals: internal which is latched in a locked state until manually cleared. The external interlock is formed by combining the internal interlock signal with those from all other modules on the bus. The internal interlock is latched when the module goes outside of its operating range (e.g., over-current, over-voltage etc.). If any of the internal and external interlock signals is latched, the module will immediately stop operation and will not be able to operate until the interlock is cleared. When the module is power-cycled its internal interlock is latched  by default to avoid spurious operation. As all interlock signals of modules on the same bus are tied together, this will also inhibit all other modules on the bus from operating as their external signal will be asserted. Interlock state must be cleared for all modules that have their internal signal latched by setting the Clear\_Interlock signal in the BI25\_Fault\_Control message exactly once and sending this frame once.

### Step 2 – Configure operating mode

<font color="#00A89D">**PWM Mode**</font> is designated for normal user operation and should be used for standard system configuration. This mode operates in open loop with a user-defined frequency, which should be set to 300 kHz. As this mode does not compensate for voltage drops, there can be up to a 20 V difference between Side A and Side B at full load. Incorrect selection of frequency may result in irreversible damage to the module. If in doubt, please contact us for guidance.

The other modes, Voltage Follower Mode and Gain Mode, are under development. We do not recommend using this mode at this stage.

### Step 3 – Start converter

Once setpoints and operating mode have been configured, the converter can be started by setting Converter\_ON in BI25\_Mode\_Control. The selected control mode must also be kept active in this message. Alternatively, you can combine Step 2 and Step 3 in a single step by sending only one message with Converter\_ON and selected control mode.

### Step 4 – Stop converter

The converter is stopped by one of the following two events:

* Converter\_ON in BI25\_Mode\_Control is cleared  
* Internal or external interlock signals are locked. In case of locked interlock signal, the fault must be cleared by setting Clear\_Interlock in BI25\_Fault\_Control in order to be able to continue operation.
