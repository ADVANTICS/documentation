# Maintenance and Troubleshooting

The ADB-PC-CH01 is maintenance free.
The connected liquid cooling system needs to be maintained on it's own schedule.

It is recommended that regular inspections of the installation is carried out.
Any visible damage or deformation of the enclosure renders an ADB-PC-CH01 unsafe for operation.

## Firmware update

Even after purchase of the unit, development on the control algorithms and behaviour continues at Advantics
Firmware updates may contain new features or improve regulating behaviour. Updating units in the field
is not mandatory, though updates may improve system performance. Updated firmware is provided free of charge
for the lifetime of the converter unit.

In case of questions regarding the deployment of updates to units in the field please reach out to
Advantics support. We are happy to advise on this matter.

### Firmware update procedure

It is important to note that during the update process, the control/24V power to the ADB-PC-CH01 unit needs to be kept live.

Every firmware released by Advantics carries a unique number that it broadcasts via the `Firmware_UID` Message. This message can
be used to identify the firmware currently running on the converters.

**Prerequisites:**  
* A `adb-pc-ch01-fm01-x.x.x.hex` file (where x.x.x indicates the version of the firmware)
* A Peak Systems CAN-to-USB adapter.  
* the 'afpu' application software provided by advantics

**System State**
* There is no live power on either the AC or DC port of the ADB-PC-CH01
* the 24V power is live and stable
* the unit can be seen on the CAN bus

**Steps:**
  
1. Connect your CAN-to-USB adapter to the CAN bus.
2. Launch 'afpu'
3. the unit should show up in the 'discovered' tab of the application
4. select the `hex` file from earlier in the file browser
5. Initiate the "Flash" or process.  
7. The tool will indicate when the flash is complete and verified.  
8. Power-cycle the unit
9. Verify the new firmware version by comparing the content `Firmware UID` message


## Faults and Warnings

The ADB-PC-CH01 reports faults and warnings via the `CH01_Mode_Readback` message. A Fault will halt system operation
and requires the operator to acknowledge the fault before allowing operations to recommence. Warnings are advisory and
clear automatically as soon as the condition causing the warning is no longer present.


## Regular Inspection

- **Visual Inspection**: Check for corrosion, damage, or loose connections.
- **Torque Verification**: Keep connectors at their declared torque. Retighten if necessary.
- **Contact Resistance**: Measure contact resistance during maintenance.
- **Insulation Testing**: Verify insulation integrity, preferrably run continous ground fault monitoring systems with larger installations.

***See Also:***  
* Reference: [Spare Parts List](../appendix#spare-parts-list)  
