# Maintenance and Troubleshooting

## Firmware update

This guide provides the procedure for updating the converter's firmware.

**Prerequisites:**  
  
* You have the new firmware file(s) (`.hex`) provided by the ADVANTICS.  
* You have the provided firmware flashing tool (software) and a Peak Systems CAN-to-USB adapter.  
* The converter is powered on and in `STANDBY` mode.  
* De-energize the HV bus, turn off AC or DC power feeding the units

**Steps:**  
  
1.  Connect your CAN-to-USB adapter to the CAN bus.  
2.  Make sure that your computer and the power converter has a reliable power source during the update process
3.  Launch the firmware flashing tool by running the command "boxupdater.exe -p package_DD.MM.YYYY.zip"
4.  **WARNING:** Do not power off the unit or disconnect the CAN bus during this process.  
5.  The tool will indicate when the flash is 100% complete and verified.  
6.  Power-cycle the unit (see `Power On and Off`).  
7.  Verify the new firmware version by reading the appropriate CAN message.  


## Troubleshooting Faults

This guide provides a step-by-step process for diagnosing and resolving faults.


### Fault Categories

#### Critical (Level 1)

Requires system reboot (contact Advantics support).

- Wrong firmware for internal module  
- Hardware error  

#### Error (Level 2)

Can be cleared using the `Clear_Interlock` signals from the `Fault_Control` message.  
All errors must be cleared before power-on is allowed. If `Enable` is active, the converter will turn on once all faults and warnings are cleared.

When an error occurs, the converter will attempt a graceful shutdown, depending on the severity level.

- DC overvoltage / undervoltage (Port A or B)  
- Overcurrent protection activation (Port A or B)  
- Overtemperature shutdown  
- Communication loss timeout  
- Hardware interlock activation  
- Internal component failure  

#### Warning (Level 3)

Warnings canindicate that a voltage is missing, a voltage is too low, or that operating conditions are suboptimal. All warnings must be cleared before power-on is allowed. If `Enable` is active, the converter will turn on once all faults and warnings are cleared.

When a warning appears during operation, performance may not be met.

- Overtemperature  
- Power derating due to temperature  
- Current limiting activation  
- Too low input voltage  
- Bad setpoints  

#### Info (Level 4)

When an info event appears, the power converter will continue normal operation without any issue.

- Maintenance reminders  
- Performance info  
- Environmental info  


### Troubleshooting

**Procedure:**  
  
1.  **Identify the Fault:** Read the active fault code from the "Fault" CAN message and the "GN01_faults"
2.  **Understand the Cause:**  The notes from the KCD explain the fault
3.  **Take Corrective Action:**  
    * **Example (Over-Voltage):** Check your load. Is it a battery that is already full? Is there another source pushing voltage back?  
    * **Example (Over-Temperature):** Check coolant flow, check for blocked filters, and check ambient temperature.  
    * **Example (CAN Timeout):** Check CAN bus wiring, termination resistors, and your master controller.  
4.  **Resolve the Condition:** Fix the external or internal condition that caused the fault.  
5.  **Clear the Fault:** Once the condition is resolved, send the "Clear Fault" command via CAN. The unit should return to `STANDBY` mode.  
6.  If the fault re-occurs immediately, do not operate the unit and contact technical support.  


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

**Procedures:**  
There are currently no procedures documented. Contact ADVANTICS regarding the maintenance plan.

***See Also:***  
* Reference: [Spare Parts List](../appendix#spare-parts-list)  