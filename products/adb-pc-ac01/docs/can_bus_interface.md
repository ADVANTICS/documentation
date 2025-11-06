# CAN Bus Interface Specification

## Message Structure

```
CAN Frame Structure:
- Identifier: 29-bit extended format
- Data Length: 0-8 bytes
- Bit Rate: Configurable (125 kbps to 1 Mbps)
- Frame Type: Data and Remote frames
```

## Control Messages

### Power Control Message (ID: 0x100)
```
Byte 0-1: Active Power Setpoint (W)
Byte 2-3: Reactive Power Setpoint (VAR) - Not applicable for DC/DC, set to 0
Byte 4: Control Flags
    Bit 0: Enable/Disable
    Bit 1: Power Flow Direction (0=Port A to B, 1=Port B to A)
    Bit 2: Reserved
    Bit 3: Emergency Stop
Byte 5-7: Reserved
```

### Mode Control Message (ID: 0x101)
```
Byte 0: Operating Mode
    0x00: Standby
    0x01: Port A to B Conversion
    0x02: Port B to A Conversion
    0x03: Bidirectional Mode
    0x04: Fault
    0x05: Maintenance
Byte 1-7: Reserved
```

## Status Messages

### Operational Status (ID: 0x200)
```
Byte 0: Operating State
    0x00: Off
    0x01: Initialized
    0x02: Ready
    0x03: Operating
    0x04: Fault
    0x05: Maintenance
Byte 1: Fault Flags
Byte 2: Warning Flags
Byte 3: Control Flags
Byte 4-7: Reserved
```

### Electrical Data (ID: 0x201)
```
Byte 0-1: DC Voltage Port A (0.1V resolution)
Byte 2-3: DC Current Port A (0.1A resolution)
Byte 4-5: DC Voltage Port B (0.1V resolution)
Byte 6-7: DC Current Port B (0.1A resolution)
```