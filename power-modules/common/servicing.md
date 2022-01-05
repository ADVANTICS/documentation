# Servicing

## Firmware update
All Advantics MCP-25 family modules have a bootloader that allows the user to update the module firmware through CAN bus, thus, without requiring any additional hardware and cabling.

To check and get the latest firmware release version consult with Advantics.

The firmware of the module can be updated with the Advantics tool **AFPU** (Advantics Flash Programming Utility). It is a very simple command line interface (CLI) program provided by Advantics.

The user just needs to:

1. Navitage to the AFPU folder and open a terminal window
2. Execute the following command:

- For windows:

    .\afpuexe.exe -m **MODULE** -p**X** flash C:\my_firmware_path\firmware_file.hex

- For linux:

    ./afpuexe.exe -m **MODULE** -p**X** flash 'C:\my_firmware_path\firmware_file.hex'

In the commands above, **X** is the stack position of the target device, and **MODULE** can be any module type of the following list:
- FILTER
- PFC
- LLC
- BUCK
- AFE
- ADM-PC-BI25
- ADM-PC-LF45
- ADM-PC-UP25
- ADM-PC-LL25
- ADM-PC-BC25
- ADM-PC-BP25

>[!WARNING]Take close attention to the -m switch. You must use the correct firmware for the correct module. Otherwise you risk to damage the module.

>[!WARNING]Do not disconnect or turn off the module power supply while the flashing process is taking process or permanent damage to the module might occur.

The command above will start the flashing procedure and will show an output similar to this (as an example):

    Putting device on position 0 in reset...
    Interrupting normal boot...
    Found module: AFE
    HW revision: 0x0
    HW variant: 0x0
    Stack position: 0x0
    Serial number: 0x1afdab
    Bootloader firmware info:
    Git revision: 2019.12.12
    Build date: 20191212/1833

>[!NOTE]The Git revision/build date are information about the bootloader itself, NOT the module firmware.

## Manteinance plan

The module does not contain any parts requiring regular maintenance. All the capacitors are either ceramic capacitors (low voltage) or film capacitors (high voltage). There are no electrolytic capacitors prone to drying out, and no cooling fans.

## Serviceability

The module does not contain any user serviceable parts.

## Diagnostics

### Low voltage, control

Diagnostics can be performed over the CAN bus, using ADVANTICS ETKA software. Low level diagnostic include check of low voltage power – measure current on the 24 V supply, to see if it is within the limits. The module contains a number of LEDs – orange ones indicating low voltage power rails, and green ones indicating interlock state and DSP heartbeat (1 Hz). Thermal imagining can also help to discover overheating components.

### Power path

In case of a power converter damage due to high surge currents, optical inspection can be sufficient to discover the failure. Most likely the MOSFET legs will be partially vaporized, and some areas of the board will be covered with metallic dust and carbon buildup from arcing components. If any signs of such damage are discovered, the module is beyond repair. A damage to internal PCB layers is very likely.