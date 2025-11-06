
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