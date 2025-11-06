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