# Installation Guide

## Connector Installation Guidelines

### DC Connector Installation (Port A and Port B)

1. **Polarity Verification**

      * Double-check Port A and port B connections.
      * Connect positive and negative conductors correctly.

2. **Cable Requirements**

      * Use cables rated for 1500V DC operation for Port B and 1000V DC for Port A.
      * Appropriate current rating for ±120A (Port A) and ±220A (Port B) operation.
      * Use appropriate cable gauge for continuous current.
      * Use proper crimping tools for contact termination.

2. **Connection Procedure**

      * Ensure power is disconnected before installation.
      * Connect PE ground conductor first.
      * Mate connectors until positive lock is engaged.
      * Verify proper torque on all connections.

### Control Connector Installation

* **CAN Bus Wiring**
      * Use twisted pair cables for CAN_H and CAN_L.
      * Maintain proper impedance (120Ω characteristic).
      * Install termination resistors at bus ends.

* **Control Power Wiring**
      * Use adequate wire gauge for **3 A current** at **24 VDC**.
      * Include overcurrent protection (fuse) in 24V supply.
      * It is possible to use one 24V power supply for multiple converters. Consult with ADVANTICS beforehand.

## Install the Converter (Mechanical)

This guide covers the physical installation, mounting, and handling of the ADB-PC-DC01 unit.

**Prerequisites:**

   * Use lifting equipment rated for the converter’s weight (recommendation: Scissor-lift table or Hydraulic lift cart).
   * Have the proper mounting hardware (e.g., bolts, washers).
   * In case of a rack installation, make sure the cabinet/rack is equipped with rails or slides.

**Steps:**

   1. **Inspect for Damage:** Visually inspect the unit for any shipping or handling damage before installation.
   2. **Lift the Unit:** lift the unit using the lifting equipment (Recommendation: scissor-lift table or the hydraulic lift cart).
   3. **Position and Mount:** Lift and align the unit in its final position or rack.
   4. **Secure the Unit:** slide the unit inside and fasten the unit’s mounting flanges (if used) with the specified bolts and washers.
   5. **Torque Bolts:** Use a torque wrench to tighten bolts to the specified mechanical values.

## Install the Converter (Electrical)

This guide covers the connection of all high-voltage and low-voltage electrical cables.

!!! WARNING "**RISK OF ELECTRIC SHOCK**"
      This procedure must only be performed by qualified personnel. Ensure all power sources (Port A and Port B) are **de-energized, disconnected, and locked out**.

**Prerequisites:**

   * AC supply and DC load circuits are confirmed **OFF and locked out** (LOTO).
   * Proper **PPE** (insulated gloves, safety glasses, etc.) is used.
   * You are wearing appropriate Personal Protective Equipment (PPE).
   * Multimeter and torque wrench are available and calibrated.
   * All cables are prepared, terminated, and labeled.

**Steps:**

1.  **Connect Protective Earth (PE):**
      - **This must be the first connection made.**
      - Connect the main facility ground to the PE stud on the converter chassis.

2. **Connect DC (Port A):**

      - Confirm polarity and ensure DC load is off.
      - Connect **+ (positive)** and **– (negative)** conductors to Port A.
      - Ensure all Connectors are properly connected and locked.

3. **Connect DC (Port B):**

      - Confirm polarity and ensure DC load is off.
      - Connect **+ (positive)** and **– (negative)** conductors to Port B.
      - Ensure all Connectors are properly connected and locked.

      
4.  **Connect Low-Voltage Control:**

      - Wire the **CAN bus**, **interlock**, and **24 VDC control power** per the provided pinout.
      - Secure connectors to prevent loosening.


## Connect the Cooling System

This section describes the procedure for connecting the **liquid cooling loop** of the converter.

**Prerequisites:**

   * Cooling circuit is flushed and filled with **appropriate coolant** - water/glycol mix with corrosion inhibitors and organic growth inhibitors.
   * The pump is **OFF** before connecting.

**Steps:**

   1. Inspect O-rings on the cooling ports for damage or contamination.
   2. Connect the **Coolant In** hose to the inlet port.
   3. Connect the **Coolant Out** hose to the outlet port.
   4. Tighten all fittings securely (avoid overtightening), or install clamps (in case of barbed fittings).
   5. Start the pump at **low flow rate**.
   6. Purge all air from the circuit according to the chiller’s instructions.
   7. Increase to nominal flow rate and check for **leaks**.


## Set Up a Parallel System

### Parallel Configuration Example

This procedure describes how to interconnect and configure multiple ADB-PC-AC01 units for parallel operation.

<!-- <div style="text-align: center; margin: 4rem 0;">
    <img src="assets/ac01_system_architecture.webp" alt="System Architecture" style="width: auto; height: auto;">
</div> -->


**Prerequisites:**

   * All units are mechanically, electrically, and cooling-system installed.
   * All units are powered off.

**Steps:**

   1. **Connect the Parallel Bus:**
      Connect the dedicated **parallel communication cable** between all converters in the same group.
   2. **Assign Unique IDs:**
      Set a unique **unit ID** for each converter using the **ETKA configuration tool**.
   3. **Configure the Group ID:**
      Assign a **group ID** to define which units operate together.
   4. **Power On:**
      Power on all converters using the standard “Power On” procedure.

