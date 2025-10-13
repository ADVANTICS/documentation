# Appendix

## Technical Specifications Summary

### Electrical Specifications

#### DC Bus Side (Port A) Specifications
| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Voltage Range** | 750 - 950 | V DC |
| **Current** | ±120 | A |
| **Maximum Power** | 100 | kW |
| **Current Measurement Accuracy** | ±1 | % of full-scale |
| **Voltage Measurement Accuracy** | ±1 | % of full-scale |

#### DC Output Side (Port B) Specifications
| **Parameter** | **Value** | **Unit** |
|---------------|-----------|----------|
| **Voltage Range** | 200 - 1500 | V DC |
| **Current** | ±220 | A |
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

### DC Connectors (Port A - SurLock Plus SLP-HIR-B)

| **Pin** | **Function** | **Polarity** | **Notes** |
|---------|--------------|--------------|-----------|
| **1** | DC Positive | + | Red marking |
| **2** | DC Negative | - | Black marking |

### DC Connectors (Port B - SurLock Plus SLP-HIR-C)

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
Byte 2-3: Reactive Power Setpoint (VAR) - Not applicable for DC/DC, set to 0
Byte 4: Control Flags
    Bit 0: Enable/Disable
    Bit 1: Power Flow Direction (0=Port A to B, 1=Port B to A)
    Bit 2: Reserved
    Bit 3: Emergency Stop
Byte 5-7: Reserved
```

#### Mode Control Message (ID: 0x101)
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

### Status Messages

#### Operational Status (ID: 0x200)
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

#### Electrical Data (ID: 0x201)
```
Byte 0-1: DC Voltage Port A (0.1V resolution)
Byte 2-3: DC Current Port A (0.1A resolution)
Byte 4-5: DC Voltage Port B (0.1V resolution)
Byte 6-7: DC Current Port B (0.1A resolution)
```

## Fault Codes

### Critical Faults (Level 1)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0001** | Ground Fault | Ground current detected | Immediate shutdown |
| **0x0002** | Overcurrent (Port A) | Current exceeds limit on Port A | Immediate shutdown |
| **0x0003** | Overcurrent (Port B) | Current exceeds limit on Port B | Immediate shutdown |
| **0x0004** | Overtemperature | Temperature exceeds limit | Immediate shutdown |
| **0x0005** | Hardware Interlock | Safety interlock activated | Immediate shutdown |
| **0x0006** | Isolation Fault | Loss of reinforced isolation | Immediate shutdown |

### Serious Faults (Level 2)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0101** | DC Overvoltage (Port A) | DC voltage too high on Port A | Graceful shutdown |
| **0x0102** | DC Undervoltage (Port A) | DC voltage too low on Port A | Graceful shutdown |
| **0x0103** | DC Overvoltage (Port B) | DC voltage too high on Port B | Graceful shutdown |
| **0x0104** | DC Undervoltage (Port B) | DC voltage too low on Port B | Graceful shutdown |
| **0x0105** | Communication Loss | CAN bus communication lost | Graceful shutdown |

### Minor Faults (Level 3)

| **Code** | **Description** | **Cause** | **Action** |
|----------|-----------------|-----------|------------|
| **0x0201** | Temperature Derating | High temperature | Power limiting |
| **0x0202** | Current Limiting | Overcurrent condition | Current limit |
| **0x0203** | Low Efficiency | Efficiency below normal | Power limiting |

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
| Power limiting | Temperature derating | Improve cooling |

### Diagnostic Procedures

1. **Check Fault Codes**
   - Read fault status via CAN bus
   - Clear non-critical faults
   - Investigate root cause

2. **Verify Electrical Parameters**
   - Measure DC voltages on both Port A and Port B
   - Verify current measurements on both Port A and Port B

3. **Check Environmental Conditions**
   - Verify temperature readings
   - Check cooling system operation
   - Verify airflow and clearances

## Spare Parts List

### Recommended Spare Parts

| **Part Number** | **Description** | **Quantity** | **Lead Time** |
|-----------------|-----------------|--------------|---------------|
| **ADB-CONN-DCA** | DC Connector Kit (Port A) | 1 set | 2 weeks |
| **ADB-CONN-DCB** | DC Connector Kit (Port B) | 1 set | 2 weeks |
| **ADB-CONN-CAN** | CAN Connector Kit | 2 pieces | 1 week |
| **ADB-FUSE-DCB** | DC Output Fuse (Port B) | 1 piece | 1 week |

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
| **IEC 61851-23** | DC EV Charging Station | Designed to |
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
**Last Updated**: October 2025  
**Next Review**: October 2026
