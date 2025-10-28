# First-Time Commissioning

### **Introduction**

Welcome to the ADB-PC-DC01! This tutorial is for first-time users, engineers, or technicians.

**Our goal:** To guide you safely from unboxing your new converter to a successful first power-on. This guide provides a simple, direct path to verify that your unit is installed correctly and is operational.

This guide simplifies the process. For detailed technical data and advanced procedures, it will link you to the main **How-To Guides** and **Reference** sections.

### **Prerequisites**

Before you begin, make sure you have the following:

**Knowledge & Safety:**
* You must be a qualified electrical engineer or certified technician.
* You must be familiar with high-voltage and high-current DC systems.
* You have read and understood the conceptual safety warnings.
    * ***See Also:*** [General Safety Information](docs/6_safety_and_warnings.md#general-safety-information)

**Tools & Equipment:**
* Standard mechanics toolset (socket wrench, torque wrench, etc.)
* Digital Multimeter (DMM) rated for 1500V DC
* Personal Protective Equipment (PPE) (high-voltage insulated gloves, safety glasses, etc.)
* Lifting equipment (the unit is heavy)
* A CAN bus monitoring tool (e.g., a CAN-to-USB adapter and monitoring software)
* A controllable DC source (Port A) and a controllable DC load (Port B)


### **Step 1: Pre-Installation Safety Check**

Safety is the most critical step. Do not proceed until you have verified the following.

1.  **Inspect for Shipping Damage:** Visually inspect the crate and the converter for any signs of damage, such as dents, cracked insulators, or loose components.
2.  **Clear the Workspace:** Ensure the installation area is clean, dry, and free of obstructions.
3.  **Verify Power is OFF:** Confirm that all external DC power sources and loads are completely de-energized, disconnected, and locked out (LOTO).
4.  **Check Environment:** Ensure the ambient temperature and humidity are within the unit's operating range.
    * ***See Also:*** [Environmental Specifications](docs/7_appendix.md#environmental-specifications)


### **Step 2: Basic Mechanical & Electrical Installation**

This step covers the essential connections to get the unit running.

1.  **Mount the Unit:**
    * Lift the converter using the designated lifting points.
    * Securely mount it to your rack or chassis using the correct bolt size and type.
    * Ensure all mechanical clearances for airflow are met.
    ***See Also:*** [Install the Converter (Mechanical)](#how-to-install-the-converter-mechanical)

2.  **Connect Protective Earth (Ground):**
    * **This is the most important connection.** Connect your facility's Protective Earth (PE) ground to the main grounding stud on the converter chassis.
    * Use the specified cable gauge and torque the connection correctly.

3.  **Connect the Cooling System:**
    * Connect the coolant inlet and outlet hoses to the manifold.
    * Ensure there are no leaks.
    ***See Also:*** [Connect the Cooling System](#how-to-connect-the-cooling-system)

4.  **Connect DC Power (Port A & Port B):**
    * **WARNING:** Ensure all sources remain locked out.
    * Use your DMM to verify the polarity (+ and -) of your incoming and outgoing busbars.
    * Connect the DC busbars (Port A and Port B) to the converter terminals. Ensure correct polarity.
    * Torque the bolts to the specified value.
    ***See Also:*** [Install the Converter (Electrical)](#how-to-install-the-converter-electrical)
    * ***See Also:*** [Connectors and Interfaces](docs/3_connectors_and_interfaces.md#connectors-and-interfaces)

5.  **Connect the Low-Voltage Control Connector:**
    * Connect the main control harness. This includes the connector for CAN bus and the "Enable" signal.
    * Ensure the hardware "Enable" signal is initially set to OFF (disabled).


### **Step 3: Power-On Sequence**

1.  **Start the Cooling System:** Turn on your external cooling/chiller system. Verify that coolant is flowing at the correct rate and temperature.
2.  **Apply Auxiliary Power:** Energize the converter's auxiliary power supply (if separate from the main DC bus).
3.  **Energize DC Busses:** Remove the lock-out and energize the main DC source (Port A) and the DC load/source (Port B) so that voltage is present at the terminals.
4.  **Enable the Converter:** Apply the hardware "Enable" signal. You should hear the unit start up (e.g., internal contactors closing, fans spinning).


### **Step 4: Establish CAN Communication ("Hello World")**

Now, let's verify the converter is "awake" and communicating.

1.  **Connect Your Monitor:** Connect your CAN bus monitoring tool to the CAN bus lines.
2.  **Set Baud Rate:** Ensure your monitor is set to the correct baud rate (e.g., 250 kbit/s).
    * ***See Also:*** [CAN Bus Communication](docs/4_operation.md#can-bus-communication)
3.  **Look for a Heartbeat:** Open your CAN monitoring software. You should see a "heartbeat" message  being broadcast by the converter every 1-2 seconds. This message indicates the unit is alive and in a `STANDBY` state.

If you see this message, your control system is successfully connected.


### **Step 5: Run a Simple Power Test**

Let's confirm the unit can pass power.

1.  **Set to `STANDBY`:** Use your CAN tool to send the command to place the unit in `STANDBY` mode.
2.  **Set Target Voltage/Current:** Send a simple command, for example, to regulate the output (Port B) at a nominal voltage with a 0A current limit.
3.  **Enable Operation:** Send the CAN command to move from `STANDBY` to `OPERATE`.
4.  **Apply a Small Load:** Using your external DC load, draw a small amount of current (e.g., 10% of the unit's rating).
5.  **Verify Output:** On your monitoring tool and your external DMM, confirm that the voltage and current at Port B match your setpoints and that no faults are present.

### **Next Steps**

**Congratulations! Your ADB-PC-DC01 is installed, communicating, and operational.**

You have successfully completed the first-time commissioning. You are now ready to move on to more advanced configuration and integration.

* To perform specific tasks like firmware updates or fault diagnosis, see our **`How-To Guides`**.
* To understand the theory behind the operating modes or safety systems, see the **`Explanation`** section.
* For a complete list of all CAN commands, fault codes, and technical specifications, see the **`Reference`** section.