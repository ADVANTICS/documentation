# Maintenance and Troubleshooting

## Update Firmware

This guide provides the procedure for updating the converter's firmware.

**Prerequisites:**
* You have the new firmware file (`.hex`) provided by the ADVANTICS.
* You have the rovided firmware flashing tool (software) and a CAN-to-USB adapter.
* The converter is powered on and in `STANDBY` mode.

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
- Ground fault detection
- Overcurrent protection activation (Port A or B)
- Overtemperature shutdown
- Hardware interlock activation
- Isolation fault

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

***See Also:***
* `Reference: Fault Code Directory` (for a complete list of all codes)


## Connector Maintenance

### Regular Inspection

- **Visual Inspection**: Check for corrosion, damage, or loose connections.
- **Torque Verification**: Re-torque connections per maintenance schedule.
- **Contact Resistance**: Measure contact resistance during maintenance.
- **Insulation Testing**: Verify insulation integrity.

### Replacement Guidelines

- **Contact Replacement**: Replace contacts showing signs of wear or damage.
- **Seal Replacement**: Replace environmental seals during maintenance.
- **Locking Mechanism**: Verify proper operation of locking features.

## Perform Routine Maintenance

Follow this guide to perform scheduled preventative maintenance to ensure long service life.

**WARNING:** **RISK OF ELECTRIC SHOCK.** The unit must be fully powered off, de-energized, locked-out, and capacitors discharged before performing any maintenance.

**Prerequisites:**
* Unit is fully de-energized (LOTO).
* You have the required spare parts (filters, etc.).

**Procedures:**
* **Monthly:**
    1.  **Inspect Air Inlets (if any):** Check for and clean any dust or debris from air inlet filters.
    2.  **Visual Inspection:** Check for any signs of damage, leaks, or corrosion.
* **Annually:**
    1.  **Replace Coolant Filter:** Power down the cooling loop, replace the external coolant filter, and purge the system.
    2.  **Torque Check:** Re-torque all high-power busbar connections to their specified values.
    3.  **Clean Connections:** Inspect and clean all low-voltage connector pins.

***See Also:***
* `Reference: Maintenance Schedule`
* `Reference: Spare Parts List`


## Documentation and Records

### Installation Records

Maintain records of:
- Installation date and personnel
- Serial numbers and configuration
- Test results and measurements
- As-built drawings and schematics

### Commissioning Reports

Document:
- Startup procedures performed
- Test results and performance data
- Any deviations or issues encountered
- Sign-off by qualified personnel

### Safety Documentation

#### Required Documentation

Maintain current copies of:
- Safety data sheets (SDS).
- Emergency contact lists.
- Safety procedures.
- Training records.
- Incident reports.

#### Safety Records

Keep records of:
- Safety inspections.
- Incident investigations.
- Training activities.
- Safety meetings.
- Corrective actions.