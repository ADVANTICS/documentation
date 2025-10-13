
# Appendix

## Technical Specifications Summary

### Electrical Specifications

#### AC Side Specifications
| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Rated AC Voltage (L-L)** | 208 - 480 | V<sub>rms</sub> |
| **Rated AC Frequency** | 50 / 60 | Hz |
| **Maximum AC Current** | ±150 | A<sub>rms</sub> per phase |
| **Power Factor (PF)** | ≥0.99 | - |
| **Total Harmonic Distortion (THDi)** | ≤5 | % |
| **Reactive Power Control** | ±0.9 | inductive-capacitive |

#### DC Side Specifications
| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Voltage Range** | 650 - 950 | V DC |
| **Current** | ±170 | A |
| **Maximum Power** | 100 | kW |
| **Current Measurement Accuracy** | ±1 | % of full-scale |
| **Voltage Measurement Accuracy** | ±1 | % of full-scale |

### Mechanical Specifications

| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Dimensions (L × W × H)** | 700 × 440 × 165 | mm |
| **Weight** | 30 | kg |
| **Mounting** | 4U rack or custom brackets | - |
| **Cooling** | Liquid cooled | - |
| **Ingress Protection** | IP67 | - |

### Environmental Specifications

| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Operating Temperature** | -40 to +70 | °C |
| **Storage Temperature** | -50 to +85 | °C |
| **Altitude** | Up to 3000 | m |
| **Pollution Degree** | 3 | - |

## Connector Pinouts

### AC Connectors (SurLock Plus SLP-HIR-B)

| **Pin** | **Function** | **Wire Color** | **Notes** |
|---------|--------------|----------------|-----------|
| **1** | Phase L1 | Brown | - |
| **2** | Phase L2 | Black | - |
| **3** | Phase L3 | Grey | - |
| **PE** | Protective Earth | Green/Yellow | Safety ground |

### DC Connectors (SurLock Plus SLP-HIR-B)

| **Pin** | **Function** | **Polarity** | **Notes** |
|---------|--------------|--------------|-----------|
| **1** | DC Positive | + | Red marking |
| **2** | DC Negative | - | Black marking |

### CAN Bus Connectors

| **Pin** | **Function** | **Description** |
|---------|--------------|-----------------|
| **1** | CAN_H | CAN High signal |
| **2** | CAN_L | CAN Low signal |
| **3** | GND | Signal ground |
| **4** | SHLD | Cable shield |

### Control Power Connector

| **Pin** | **Function** | **Voltage** | **Current** |
|---------|--------------|-------------|-------------|
| **1** | +24V | 20-28V DC | Up to 3A |
| **2** | GND | 0V | Return |

## CAN Bus Message Specification

### Control Messages

#### Power Control Message (ID: 0x100)
```
Byte 0-1: Active Power Setpoint (W)
Byte 2-3: Reactive Power Setpoint (VAR)
Byte 4: Control Flags
    Bit 0: Enable/Disable
    Bit 1: Mode (0=Rectifier, 1=Inverter)
    Bit 2: Grid Forming/Following
    Bit 3: Emergency Stop
Byte 5-7: Reserved
```

#### Mode Control Message (ID: 0x101)
```
Byte 0: Operating Mode
    0x00: Standby
    0x01: Rectifier Mode
    0x02: Inverter Mode
    0x03: Bidirectional Mode
    0x04: Grid Forming Mode
    0x05: Grid Following Mode
Byte 1-7: Reserved
```

### Status Messages

#### Operational Status (ID: 0x200)
```
Byte 0: Operating State
    0x00: Off
    0x01: Initialized
    0x02: Ready
    0x03: Synchronized
    0x04: Operating
    0x05: Fault
    0x06: Maintenance
Byte 1: Fault Flags
Byte 2: Warning Flags
Byte 3: Control Flags
Byte 4-7: Reserved
```

#### Electrical Data (ID: 0x201)
```
Byte 0-1: AC Voltage L1-L2 (0.1V resolution)
Byte 2-3: AC Voltage L2-L3 (0.1V resolution)
Byte 4-5: AC Voltage L3-L1 (0.1V resolution)
Byte 6-7: AC Current L1 (0.1A resolution)
```

## Fault Codes

### Critical Faults (Level 1)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0001** | Ground Fault | Ground current detected | Immediate shutdown |
| **0x0002** | Overcurrent | Current exceeds limit | Immediate shutdown |
| **0x0003** | Overtemperature | Temperature exceeds limit | Immediate shutdown |
| **0x0004** | Hardware Interlock | Safety interlock activated | Immediate shutdown |

### Serious Faults (Level 2)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0101** | AC Overvoltage | AC voltage too high | Graceful shutdown |
| **0x0102** | AC Undervoltage | AC voltage too low | Graceful shutdown |
| **0x0103** | DC Overvoltage | DC voltage too high | Graceful shutdown |
| **0x0104** | DC Undervoltage | DC voltage too low | Graceful shutdown |

### Minor Faults (Level 3)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0201** | Temperature Derating | High temperature | Power limiting |
| **0x0202** | Current Limiting | Overcurrent condition | Current limit |
| **0x0203** | High THD | Harmonic distortion high | Power limiting |
| **0x0204** | Low Efficiency | Efficiency below normal | Power limiting |

## Maintenance Schedule

### Routine Maintenance Tasks

| **Frequency** | **Task** | **Procedure** | **Tools Required** |
|---------------|----------|---------------|-------------------|
| **Daily** | Visual Inspection | Check indicators and displays | None |
| **Weekly** | Fault Check | Review fault logs and alarms | CAN interface |
| **Monthly** | Connection Check | Verify torque on connections | Torque wrench |
| **Quarterly** | Performance Check | Test efficiency and operation | Power analyzer |
| **Annually** | Complete Inspection | Comprehensive system check | Full test kit |

### Maintenance Records

Maintain records of:
- Maintenance activities performed
- Test results and measurements
- Parts replaced or repaired
- Observations and recommendations
- Technician signature and date

## Troubleshooting Guide

### Common Issues

#### Module Will Not Start

| **Symptom** | **Possible Cause** | **Solution** |
|-------------|-------------------|--------------|
| No power indication | No control power | Check 24V supply |
| Fault LED on | Critical fault present | Check fault codes |
| Communication error | CAN bus problem | Check CAN connections |

#### Poor Performance

| **Symptom** | **Possible Cause** | **Solution** |
|-------------|-------------------|--------------|
| Low efficiency | High temperature | Check cooling system |
| High THD | Grid conditions | Check AC voltage quality |
| Power limiting | Temperature derating | Improve cooling |

### Diagnostic Procedures

1. **Check Fault Codes**
   - Read fault status via CAN bus
   - Clear non-critical faults
   - Investigate root cause

2. **Verify Electrical Parameters**
   - Measure AC voltages
   - Check DC voltage levels
   - Verify current measurements

3. **Check Environmental Conditions**
   - Verify temperature readings
   - Check cooling system operation
   - Verify airflow and clearances

## Spare Parts List

### Recommended Spare Parts

| **Part Number** | **Description** | **Quantity** | **Lead Time** |
|-----------------|-----------------|--------------|---------------|
| **ADB-CONN-AC** | AC Connector Kit | 1 set | 2 weeks |
| **ADB-CONN-DC** | DC Connector Kit | 1 set | 2 weeks |
| **ADB-CONN-CAN** | CAN Connector Kit | 2 pieces | 1 week |
| **ADB-FUSE-AC** | AC Input Fuse | 3 pieces | 1 week |
| **ADB-FUSE-DC** | DC Output Fuse | 1 piece | 1 week |

### Consumable Parts

| **Part Number** | **Description** | **Replacement Interval** |
|-----------------|-----------------|-------------------------|
| **ADB-COOLANT** | Cooling System Fluid | 5 years or as needed |
| **ADB-FILTER** | Cooling System Filter | Annual |
| **ADB-SEAL-KIT** | Connector Seal Kit | As needed |

## Technical Support

### Contact Information

**Advantics Technical Support**  
Email: support@advantics.fr  
Phone: +33 1 23 45 67 90  
Emergency: +33 1 23 45 67 91

**Hours of Operation**  
Monday - Friday: 8:00 AM - 6:00 PM CET  
Emergency Support: 24/7

### Support Services

- Technical consultation
- Troubleshooting assistance
- Remote diagnostics
- On-site service
- Training programs
- Software updates

## Warranty Information

### Warranty Coverage

- **Standard Warranty**: 24 months from delivery
- **Extended Warranty**: Available upon request
- **Warranty Terms**: See complete warranty document

### Warranty Service

- Return merchandise authorization (RMA) required
- Proper packaging for shipment
- Include detailed problem description
- Follow warranty claim procedures

## Regulatory Compliance

### Standards Compliance

| **Standard** | **Description** | **Compliance** |
|--------------|-----------------|----------------|
| **IEC 61851-1** | EV Charging System | Designed to |
| **IEC 62477-1** | Power Electronics Safety | Designed to |
| **UL 2202** | EV Charging Equipment | Designed to |
| **EMC Class B** | Electromagnetic Compatibility | With filter |

### Certifications

- CE Marking (European Conformity)
- UL Listing (where applicable)
- CSA Certification (where applicable)
- Other regional certifications as required

---

**Document Version**: 1.0  
**Last Updated**: October 2024  
**Next Review**: October 2025