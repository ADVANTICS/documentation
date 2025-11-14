# Installation Guide

## Connector Installation Guidelines

### DC Connector Installation (Port A and Port B)

1. **Polarity Verification**
   - Double-check polarity before connection for both input and output.
   - Use multimeter to verify voltage polarity.
   - Connect positive and negative conductors correctly.

2. **Cable Requirements**
   - Use cables rated for 1500V DC operation for Port B and 1000V DC for Port A.
   - Appropriate current rating for ±120A (Port A) and ±220A (Port B) operation.
   - Use appropriate cable gauge for continuous current.
   - Strip insulation to manufacturer specifications.
   - Use proper crimping tools for contact termination.

3. **Connection Procedure**
   - Ensure power is disconnected before installation.
   - Connect PE ground conductor first.
   - Mate connectors until positive lock is engaged.
   - Verify proper torque on all connections.

### Control Connector Installation

1. **CAN Bus Wiring**
   - Use twisted pair cables for CAN_H and CAN_L.
   - Maintain proper impedance (120Ω characteristic).
   - Install termination resistors at bus ends.

2. **Control Power Wiring**
   - Use adequate wire gauge for 3A current.
   - Include overcurrent protection in 24V supply.

## Install the Converter (Mechanical)

This guide covers the physical installation, mounting, and handling of the ADB-PC-DC01 unit.

**Prerequisites:**  
- You have appropriate lifting equipment rated for the converter's weight.  
- You have the correct mounting hardware (e.g., M12 bolts, washers).  
- The installation site is prepared, clean, and has all required clearances.  

**Steps:**  
1.  **Inspect for Damage:** Visually inspect the unit for any shipping damage before lifting.  
2.  **Lift the Unit:** Attach lifting straps to the designated lifting points on the chassis.  
3.  **Position and Mount:** Carefully lift the unit into its rack or final position.  
4.  **Secure the Unit:** Secure the unit's mounting flanges to the chassis using the specified bolts.  
5.  **Torque Bolts:** Use a torque wrench to tighten all mounting bolts to the specified value.  


## Install the Converter (Electrical)

This guide covers the connection of all high-voltage and low-voltage electrical cables.

!!! WARNING "**RISK OF ELECTRIC SHOCK**"
      This procedure must only be performed by qualified personnel. Ensure all power sources (Port A and Port B) are **de-energized, disconnected, and locked out**.

**Prerequisites:**  
- All power sources are confirmed OFF and locked-out (LOTO).  
- You are wearing appropriate Personal Protective Equipment (PPE).  
- You have a calibrated multimeter and torque wrench.  
- All high-power cables are cut to length, properly terminated with lugs, and clean.  

**Steps:**  
1.  **Connect Protective Earth (PE):**  
   - **This must be the first connection made.**  
   - Connect the main facility ground to the PE stud on the converter chassis.  
   - Verify the connection has low impedance (< 0.1 &#8486;).  
2.  **Connect High-Power DC Busbars (Port A & B):**  
   - Remove the protective covers from the busbar terminals.  
   - Use a multimeter to verify the polarity (+ and -) of your source and load cables one final time.  
   - Connect the positive and negative busbars for Port A.  
   - Connect the positive and negative busbars for Port B.  
   - Ensure busbar surfaces are clean and aligned.  
   - Torque all busbar bolts to the specified value.  
3.  **Connect Low-Voltage Control:**  
   - Wire your control and power harness (CAN, interlock, 24v power, etc...) according to the pinout.  
   - Mate your harness to the control and power connectors and secure it.  


## Connect the Cooling System

This guide covers the procedure for connecting the liquid cooling loop.

**Prerequisites:**  
- Your cooling loop is flushed, and the coolant meets all specifications.  
- The cooling pump is OFF.  

**Steps:**  
1.  Inspect O-rings on the cooling manifold connections for damage or debris.  
2.  Connect the "Coolant In" hose to the inlet port.  
3.  Connect the "Coolant Out" hose to the outlet port.  
4.  Tighten connections to prevent leaks (do not overtighten).  
5.  Start the external cooling pump and set it to a low flow rate.  
6.  Purge the system of all air according to your chiller's instructions.  
7.  Gradually increase to the nominal flow rate and check for any leaks at the connections.  


## Set Up a Parallel System

### Parallel Configuration Example

This procedure describes how to interconnect and configure multiple ADB-PC-DC01 units for parallel operation.

{{ figure('../assets/dc01_system_architecture.webp', 'System Architecture') }}

**Prerequisites:**  
- All units are fully installed (mechanically, electrically, and cooling).  
- All units are powered off.  

**Steps:**  
1.  **Connect Parallel Bus:** Connect the dedicated parallel communication cable between all units in the parallel group.  
2.  **Assign Unique IDs:** Set a unique ID for each unit using ETKA tool.  
3.  **Configure the Group ID:** Configure a group ID using the ETKA tool.  
4.  **Power On:** Power on all units in the group using the standard `Power On` procedure.  
