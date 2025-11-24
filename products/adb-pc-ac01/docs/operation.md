# Theory of Operation

The ADB-PC-AC01 supports multiple operating modes to accommodate various application requirements. Based on the SiC (Silicon Carbide) technology, the module employs a bidirectional topology that operates as a bidirectional active-front-end (AFE), converting single or three-phase AC from the grid into a DC link with high efficiency and almost unity power factor. It performs real-time power factor correction and reactive-power control, while precisely regulating AC current and the DC side voltage. Similarly, the converter can invert DC power back to the AC side, enabling grid support functionalities such as V2G or microgrid operations. Its internal gateway controller facilitates the coordination with multiple modules to increase the power rating to meet megawatt levels.

The control modes, while customizable and flexible, can be divided into two key categories, depending on which side is 'regulated', and which side is 'expected'.
For example, it's not possible (logically) to simultaneously request a certain mains current, and also impose the DC side voltage. Either the control is AC port (mains) centric, or DC port (DC bus) centric.

Which one should you choose? If the ADB-PC-AC01 is used as an PFC, to create a certain DC bus to be used by follow-up stages (whether to push or pull current), the Rectifier Mode is the correct choice. If the DC bus is maintained by external systems (batteries, solar), and it's the AC currents, voltage, or AC power you wish to control, then Inverter Mode is the correct choice.

## Rectifier Mode (AC to DC)

In AC to DC mode, the module receives three-phase AC (208-480V, 50/60Hz) from the grid and performs power factor correction to minimize reactive power and harmonic distortion, achieving a power factor above 0.99 and THD of less than 5%. The SiC switching devices modulate the input current to shape it while actively controlling both amplitude and phase to draw near sinusoidal current from the grid. The module can perform precharge thanks to the built-in circuit that eliminates inrush currents to avoid damage to the converter. An internal soft start algorithm limits the inrush current and avoids grid disturbances. 

The DC link voltage is controlled by the user setpoints within the range of 650V to 950V. Current is regulated bidirectionally within the power envelope of 100kW, allowing for both charging and discharging of the DC link. 

The module includes protection features to eliminate overvoltage, undervoltage, overcurrent, and overtemperature. Hardware interlock and CAN bus control ensure safe operation and coordination with other modules connected in parallel.

**Key Features:**
- Active Power Factor Correction (PFC) maintains PF ≥0.99
- Low Total Harmonic Distortion (THDi ≤5%)
- Programmable DC output voltage (650-950V)
- Current limiting and overcurrent protection
- Anti-islanding detection

## Inverter Mode (DC to AC)

In DC-to-AC mode, the module inverts energy from the DC link back to the AC side, generating a controlled three-phase output synchronized with the grid or microgrid. The modulation stage adjusts amplitude, phase, and frequency to support active and reactive power flow, enabling functions such as grid support, export, and microgrid stabilization. Grid-code integration and mains-side relays manage safe interconnection and disconnection, while real-time current regulation maintains a clean sinusoidal output. Parallel units operate cooperatively through intelligent (and adjustable) droop control, allowing coordinated AC injection and stable multi-module behavior.

The converter supports paralleling up to 120 units, scaling up to megawatt-level power systems. An intelligent droop control algorithm manages the sharing of DC link voltage among the parallel modules, which eliminates the circulating currents and stabilizes the common DC bus without requiring overly complex communication.


**Key Features:**
- Grid-tied or standalone operation
- Reactive power control (±0.9 inductive-capacitive)
- Grid forming and following capabilities
- No Neutral wire used (for pure genset applications, ADVANTICS offers a special variant)

## Bidirectionality

All modes of the ADB-PC-AC01 are inherently bidirectional. This is perfectly fine even in unidirectional applications - as the mains tends to be the only source of energy in such systems. You can however emulate unidirectionality even in battery-based systems, by simply limiting negative current setpoint to a low value. Keep in mind that most systems are bidirectional, even if they don't look that way (AC motors, synchronous PFCs in many products).

## Application Examples

Examples pending.


