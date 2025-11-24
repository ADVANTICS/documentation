# First-Time Commissioning

### **Introduction**

Welcome to the ADB-PC-AC01! This tutorial is for first-time users, engineers, or technicians.

**Our goal:** To guide you safely from unboxing your new converter to a successful first power-on. This guide provides a simple, direct path to verify that your unit is installed correctly and is operational.

This document is intended only as a simplified introduction to the product. For complete technical specifications and advanced procedures, always refer to the main **Guides** section. This document is not exhaustive. Any safety information included here is provided solely for convenience and in good faith.

You are responsible for ensuring full compliance with all applicable laws, standards, and safety regulations in your country or region. ADVANTICS assumes no liability for any injury, damage, or loss resulting from the installation, operation, or misuse of this equipment.

High-voltage systems must only be handled by trained and qualified personnel. Do not perform any operation unless you are properly certified and fully understand the associated risks.

### **Prerequisites**

Before you begin, make sure you have the following:

**Knowledge & Safety:**  

- You must be a qualified electrical engineer or certified technician.  
- You must be familiar with high-voltage and high-current AC/DC systems.  
- You have read and understood the [Electrical Safety](../safety#electrical-safety) considerations.  

  
***See Also:*** <a href="../safety">General Safety Information</a>

**Tools & Equipment:**  

- Standard mechanics toolset (socket wrench, torque wrench, etc.)
- Digital Multimeter (DMM)
- Personal Protective Equipment (PPE) (high-voltage insulated gloves, safety glasses, etc.)
- lifting equipment rated for the converter’s weight (recommendation: Scissor-lift table or Hydraulic lift cart).
- A CAN bus monitoring tool (e.g., a CAN-to-USB adapter and ETKA software)
- A 3 phase AC connection and a controllable DC load


### **Step 1: Pre-Installation Safety Check**

Safety is the most critical step. Do not proceed until you have verified the following.

1.  **Inspect for Shipping Damage:** Visually inspect the crate and the converter for any signs of damage, such as dents, cracked insulators, or loose components.
2.  **Clear the Workspace:** Ensure the installation area is clean, dry, and free of obstructions.
3.  **Verify Power is OFF:** Confirm that all external AC and DC power sources and loads are completely de-energized, disconnected, and locked out (LOTO).
4.  **Check Environment:** Ensure the ambient temperature and humidity are within the unit's operating range.

### **Step 2: Basic Mechanical & Electrical Installation**

This step covers the essential connections to get the unit running.

1.  **Mount the Unit:**  
    * lift the unit using the lifting equipment (Recommendation: scissor-lift table or the hydraulic lift cart).
    * Align the unit in its final position or rack.
    * Slide the unit inside and fasten the unit’s mounting flanges with the specified bolts and washers.
    * Securely mount it to your rack or chassis using the correct bolt size and type.
    ***See Also:*** [Install the Converter (Mechanical)](../installation#install-the-converter-mechanical)

2.  **Connect Protective Earth (Ground):**
    * **This is the most important connection.** Connect your facility's Protective Earth (PE) ground to the main grounding stud on the converter chassis.
    * Use the specified cable gauge and torque the connection correctly.

3.  **Connect the Cooling System:**
    * Connect the coolant inlet and outlet hoses to the manifold.
    * Ensure there are no leaks. This would be a good moment to perform cooling system test.
  
    ***See Also:*** [Connect the Cooling System](../installation#connect-the-cooling-system)  
    ***See Also:*** [Liquid Cooling](../mechanical_specs#liquid-cooling)


4.  **Connect AC and DC connectors:**
    * **WARNING:** Ensure all sources remain de-energized.
    * Connect the 3 phase AC input to the AC side connectors.
    * Verify the polarity (+ and -) of your busbars or wiring.
    * Connect the DC busbars and cables to the DC converter Connectors.
    * Make sure the connectors are locked (audible click when inserting the Amhpenol connector).
  
    ***See Also:*** [Install the Converter (Electrical)](../installation#how-to-install-the-converter-electrical)  
    ***See Also:*** [Connectors and Interfaces](../mechanical_specs#connectors)

5.  **Connect the Low-Voltage Control Connector:**
    * Connect the main control harness. This includes the connector for CAN bus and the Interlock line.
    * Connect the converter's auxiliary power supply harness (24V supply).

### **Step 3: Power-On Sequence**

1.  **Start the Cooling System:** Turn on your external cooling/chiller system. Verify that coolant is flowing at the correct rate and temperature.
2.  **Apply Auxiliary Power:** Energize the converter's auxiliary power supply.
3.  **Energize AC side** Apply the 3-phase AC voltage input.
4.   **Energize DC Bus:** In case your equipment energizes the DC bus on it's own, it can be performed now. Otherwise, it will get energized during precharge sequence later automatically.


### **Step 4: Establish CAN Communication ("Hello World")**

Now, let's verify the converter is "awake" and communicating.

1.  **Connect Your Monitor:** Connect your CAN bus monitoring tool to the CAN bus lines.
2.  **Set Baud Rate:** Ensure your monitor is set to the correct baud rate (e.g., 500 kbit/s).
    * ***See Also:*** [CAN Bus Communication](../can_bus_interface)
3.  **Look for a Heartbeat:** Open ETKA tool. You should see information about your power module. This indicates the unit is alive and in a `STANDBY` state.

Your control system should be successfully connected at this stage.

!!! tip
    You can communicate with the power converter even without any mains power or DC bus voltage present - just the auxiliary 24V and CAN bus connections are needed. 

### **Step 5: Run a Simple Power Test**

Let's confirm the unit can pass power.

1.  **Set to `STANDBY`:** Use ETKA tool to send the command to place the unit in `STANDBY` mode.
2.  **Set Target Voltage/Current:** Send a simple command, for example, to regulate the DC side at a nominal voltage with a minimal current limit.
3.  **Enable Operation:** Send the CAN command to move from `STANDBY` to `OPERATE`.
4.  **Apply a Small Load:** Using your external DC load, draw a small amount of current (e.g., 10% of the unit's rating).
5.  **Verify Output:** On ETKA tool and your external DMM, confirm that the voltage and current at DC side match your setpoints and that no faults are present.

### **Next Steps**

**Congratulations! Your ADB-PC-AC01 is installed, communicating, and operational.**

You have successfully completed the first-time commissioning. You are now ready to move on to more advanced configuration and integration.

* To perform specific tasks like firmware updates or fault diagnosis, see our **Guides**.
* To understand the theory behind the operating modes or safety systems, see the [**Explanation**](../operation) section.
* For a complete list of all CAN commands, fault codes, and technical specifications, see the [**CAN Bus Communication**](../can_bus_interface) section.