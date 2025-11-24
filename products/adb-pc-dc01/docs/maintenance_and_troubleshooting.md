# Maintenance and Troubleshooting

## Firmware update

This guide provides the procedure for updating the converter's firmware.

**Prerequisites:**  
  
* You have the new firmware file(s) (`.hex`) provided by the ADVANTICS.  
* You have the provided firmware flashing tool (software) and a Peak Systems CAN-to-USB adapter.  
* The converter is powered on and in `STANDBY` mode.  
* De-energize the HV bus, turn off AC or DC power feeding the units.  

**Steps:**  
  
1.  Connect your CAN-to-USB adapter to the CAN bus.  
2.  Launch the firmware flashing tool.  
3.  Use the tool to "discover" the converter on the bus.  
4.  Load the new firmware file into the tool.  
5.  Initiate the "Flash" or "Update" process.  
6.  **WARNING:** Do not power off the unit or disconnect the CAN bus during this process.  
7.  The tool will indicate when the flash is 100% complete and verified.  
8.  Power-cycle the unit (see `Power On and Off`).  
9.  Verify the new firmware version by reading the appropriate CAN message.  


## Troubleshooting Faults

This guide provides a step-by-step process for diagnosing and resolving faults.

### Protection Levels

| **Protection Level** | **Response Time** | **Action** | **Recovery** |
|---------------------|-------------------|------------|--------------|
| **Level 1** | <1ms | Immediate shutdown | Manual reset required |
| **Level 2** | <10ms | Graceful shutdown | Automatic retry after delay |
| **Level 3** | <100ms | Power limiting | Automatic recovery |
| **Level 4** | <1s | Warning/alarm | No action required |

### Fault Categories

#### Critical Faults (Level 1)
- Overcurrent protection activation (Port A or B)
- Overtemperature shutdown
- Hardware interlock activation

#### Serious Faults (Level 2)
- DC overvoltage/undervoltage (Port A or B)
- Communication loss timeout
- Internal component failure

#### Minor Faults (Level 3)
- Power derating due to temperature
- Current limiting activation
- Efficiency below expected

#### Informational (Level 4)
- Maintenance reminders
- Performance warnings
- Configuration mismatches
- Environmental alerts

### Fault Recovery Procedures

- **Fault Detection** *(Level 2)* → **Graceful Shutdown**
- **Fault Detection** *(Level 3)* → **Power Limiting**
- **Fault Detection** *(Level 4)* → **Alarm Only**
- **Immediate Shutdown** → **Fault Latch**
- **Graceful Shutdown** → **Auto Retry Timer**
- **Power Limiting** → **Monitor Recovery**
- **Alarm Only** → **Log Event**
- **Fault Latch** *(Manual Reset)* → **Restart Sequence**
- **Auto Retry Timer** *(Timer Expired)* → **Automatic Restart**
- **Monitor Recovery** *(Condition Cleared)* → **Normal Operation**
- **Log Event** → **Continue Operation**

### Troubleshooting

**Procedure:**  
  
1.  **Identify the Fault:** Read the active fault code from the "Fault" CAN message.  
2.  **Look Up the Code:** Find the code in the `Reference: Fault Code Directory`.  
3.  **Understand the Cause:** The directory will state the cause (e.g., "Output Over-Voltage").  
4.  **Take Corrective Action:**  
    * **Example (Over-Voltage):** Check your load. Is it a battery that is already full? Is there another source pushing voltage back?  
    * **Example (Over-Temperature):** Check coolant flow, check for blocked filters, and check ambient temperature.  
    * **Example (CAN Timeout):** Check CAN bus wiring, termination resistors, and your master controller.  
5.  **Resolve the Condition:** Fix the external or internal condition that caused the fault.  
6.  **Clear the Fault:** Once the condition is resolved, send the "Clear Fault" command via CAN. The unit should return to `STANDBY` mode.  
7.  If the fault re-occurs immediately, do not operate the unit and contact technical support.  

<!-- ***See Also:*** `Reference: Fault Code Directory` (for a complete list of all codes) -->


## Connector Maintenance

### Regular Inspection

- **Visual Inspection**: Check for corrosion, damage, or loose connections.
- **Torque Verification**: Re-torque connections per maintenance schedule.
- **Contact Resistance**: Measure contact resistance during maintenance.
- **Insulation Testing**: Verify insulation integrity.


### Replacement Guidelines

- **Contact Replacement**: Replace contacts or cables showing signs of wear or damage.
- **Liquid cooling**: Inspect liquid cooled components (fittings, manifolds, pumps) - replace as needed.
- **Coolant replacement**: Flush and fill new coolant (follow coolant manufacturer's recommnendations for intervals).
- **Fluid filters**: If the coolant system contains filters, replace them as instructed by the manufacturer.

## Perform Routine Maintenance

Follow this guide to perform scheduled preventative maintenance to ensure long service life.

**WARNING:** **RISK OF ELECTRIC SHOCK.** The unit must be fully powered off, de-energized, locked-out, and capacitors discharged before performing any maintenance. Wait at least 15 minutes after powering down the equipment.


**Prerequisites:**  
- Unit is fully de-energized.  
- You have the required spare parts (filters, etc.).  

There are currently no procedures documented. Contact ADVANTICS regarding the maintenance plan.

***See Also:***  
* Reference: [Spare Parts List](../appendix#spare-parts-list)  \ No newline at end of file