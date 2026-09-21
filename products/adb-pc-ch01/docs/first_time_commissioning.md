# First-Time Commissioning

### **Introduction**

This section guides you through the first time set up of the Module from taking the module from the shipping box, to a ADB-PC-CH01 operational on the bench.

You are responsible for ensuring full compliance with all applicable laws, standards, and safety regulations in your country or region.
ADVANTICS assumes no liability for any injury, damage, or loss resulting from the installation, operation, or misuse of this equipment.

High-voltage systems must only be handled by trained and qualified personnel.
Do not perform any operation unless you are properly certified and fully understand the associated risks.

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
- A 24 V power supply rated at or above 50W. If using a laboratory power supply, ensure the current limit and overcurrent protection are set high enought.
- A 3 phase AC connection and a controllable DC load


### **Step 1: Pre-Installation Safety Check**

Safety is the most critical step. Do not proceed until you have verified the following.

1.  **Inspect for Shipping Damage:** Visually inspect the crate and the converter for any signs of damage, such as dents, cracked insulators, or loose components.
2.  **Clear the Workspace:** Ensure the installation area is clean, dry, and free of obstructions.

### **Control power-up on the bench**

Here we get the 

1. lift the unit using the lifting equipment and place it on the bench (Recommendation: scissor-lift table or the hydraulic lift cart).
2. Connect the 24V control power to the Top of the M12 connectors on the left hand side of the front panel.
3. Connect the CAN-to-USB adapter to the unit and start a PEAK-Can View.
4. Verify that there are messages being sent by the converter. For the CH01 the bits [23:16] should read as 0x83, identifying it as a ADB-PC-CH01 on the can bus.

### **Grid Connection**

1. Now that the unit is live and communicating It is time to start up ETKA on your laptop. It should autodetect the ADB-PC-CH01 and bring up an overview window
2. Check the `CH01_Mode_Readback`, it should be either reporting `Init` (if the box has just been powered on), or `Idle` at this point.
3. Given that nothing should be connected at this point, The `Status` signal in the `CH01_Grid_Connection_Measurements` should report `0`.
4. Connect the grid Lines to the converter. It is important to connect the phases with their corresponding connector on the front panel. Misaligned phases will
   prevent the CH01 from starting up.
5. Energize the grid lines. The `Status` in the `CH01_Grid_Connection_Measurements` should now report `1` as well as showing the `Voltage_RMS` as well as the `Frequency` of the lines.

### **Starting up the Converter**

1. With the grid connected and `Voltage_RMS`, `Status` and `Frequency` showing the expected values we can continue to power up the converter.
2. Before enabling the converter, the output setpoints for the DC port need to be sent. If they have not been sent at least once after a power
   up the `No_Valid_Setpoints_Warning` signal should be set to `1`. Sending a setpiont message clears this flag and acknowledges the
   applied setpoints via the `CH01_DC_Setpoints_Readback` message. For a starting point it is recommended to set the `Voltage` signal of the `CH01_DC_Setpoint_Control` message to `750` in ETKA and the `Current` to `10`. The CH01 operates in CV/CC mode on the DC output so the `Current` signal sets both the sink and source current limits. When in CC mode the voltage on the input is no longer controlled by the CH01.
3. With the setpoints sent, the `No_Valid_Setpoints_Warning` flag clear and the `CH01_DC_Setpoints_Readback` message acknowledging the setpoints send a
   `CH01_Mode_Control` message with the `Mode` signal set to `DC_Side_Control`. The converter should start to report the `Starting` State. You should hear contactors clicking inside the box and once the CH01 enters the `Running` state you should see `750` volts on the output. Congrats, the unit is up and runnign and can start to be loaded.

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

### **Step 3: Establish CAN Communication **

Now, let's verify the converter is "awake" and communicating.

1.  **Apply Auxiliary Power:** Energize the converter's auxiliary 24 V power supply.
2.  **Connect Your Monitor:** Connect your CAN bus monitoring tool to the CAN bus lines.
3.  **Set Baud Rate:** Ensure your monitor is set to 500kbit/s on a Linux machine `sudo ip link set can0 up type can bitrate 500000` should do the trick.
    * ***See Also:*** [CAN Bus Communication](../can_bus_interface)
4.  **Look for a Heartbeat:** Open ETKA tool. You should 

Your control system should be successfully connected at this stage.

!!! tip
    You can communicate with the power converter even without any mains power or DC bus voltage present - just the auxiliary 24V and CAN bus connections are needed. 

### **Step 4: Power-On Sequence**

1.  **Start the Cooling System:** Turn on your external cooling/chiller system. Verify that coolant is flowing at the correct rate and temperature.
2.  **Apply Auxiliary Power:** Energize the converter's auxiliary 24 V power supply.
3.  **Energize AC side** Apply the 3-phase AC voltage input.
4.   **Energize DC Bus:** In case your equipment energizes the DC bus on it's own, it can be performed now. Otherwise, it will get energized during precharge sequence later automatically.

### **Step 5: Run a Simple Power Test**

Let's confirm the unit can process power.

1.  **check `STANDBY`:** Use ETKA tool make sure that the unit is `STANDBY` mode. If the unit is in `ERROR` mode, make sure that no emergency stop is active. If the unit is in `CRITICAL` mode, please contact Advantics support.

    !!! tip
        Errors can be cleared using `Clear_Interlock` signals from the `Fault_Control` message.

2.  **Set operating Mode:** Send command to `AC01_Mode_Set` , to choose the  operating mode 
    !!! tip
        Requested operating mode :

            - DC_Controlled (0): DC side voltage controlled to setpoint, requires AC side input present
            - AC_Controlled (1): AC side voltage controlled, will generate AC if not present
            - Bleeding (2): Discharge internal capacitors/remaining charge


        Changing mode can only be done when the power converter is not "Enable"


2.  **Set Target Voltage/Current:** Send a simple command, for example, to regulate the DC side at a nominal voltage with a minimal current limit.
3.  **Enable Operation:** Send the CAN command to move from `STANDBY` to `OPERATE`.
4.  **Apply a Small Load:** Using your external DC load, draw a small amount of current (e.g., 10% of the unit's rating).
5.  **Verify Output:** On ETKA tool and your external DMM, confirm that the voltage and current at DC side match your setpoints and that no faults are present.
