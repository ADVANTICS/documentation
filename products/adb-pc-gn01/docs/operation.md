# Theory of Operation

The ADB-PC-GN01 supports multiple operating modes to accommodate various application requirements. Based on Silicon Carbide (SiC) technology, the module employs a bidirectional topology that operates as a bidirectional active front-end (AFE), converting single-phase, split-phase, or three-phase AC from the grid into a DC link with high efficiency and near-unity power factor. It performs real-time power factor correction and reactive-power control, while precisely regulating AC current and the DC-side voltage. Similarly, the converter can invert DC power back to the AC side, enabling grid-support functionalities such as V2G or microgrid operations. Its internal gateway controller facilitates coordination with multiple modules to increase the power rating to meet megawatt levels.

The control modes, while customizable and flexible, can be divided into two key categories, depending on which side is "regulated" and which side is "expected".
For example, it is not logically possible to simultaneously request a certain mains current and also impose the DC-side voltage. Either the control is AC-port (mains) centric, or DC-port (DC bus) centric.

Which one should you choose? If the ADB-PC-GN01 is used as a PFC to create a certain DC bus to be used by follow-up stages (whether to push or pull current), the Rectifier Mode is the correct choice. If the DC bus is maintained by external systems (batteries, solar), and it is the AC currents, voltage, or AC power you wish to control, then Inverter Mode is the correct choice.

## Inverter Mode (DC to AC)

In DC-to-AC mode, the module inverts energy from the DC link back to the AC side, generating a controlled single-phase, split-phase, or three-phase output synchronized with the grid or microgrid. The modulation stage adjusts amplitude, phase, and frequency to support active and reactive power flow, enabling functions such as grid support, export, and microgrid stabilization. Grid-code integration and mains-side relays manage safe interconnection and disconnection, while real-time current regulation maintains a clean sinusoidal output. Parallel units operate cooperatively through intelligent (and adjustable) droop control, allowing coordinated AC injection and stable multi-module behavior.

The converter supports paralleling up to 120 units, scaling up to megawatt-level power systems. An intelligent droop control algorithm manages the sharing of the AC bus among the parallel modules, which eliminates circulating currents and stabilizes the common AC network without requiring overly complex communication.

In addition to grid-following operation, the ADB-PC-GN01 can operate in grid-forming mode and generate its own AC grid. In this mode, it defines the AC voltage, frequency, and phase reference, allowing it to power loads in islanded conditions, form a microgrid, or act as the main source in off-grid systems.

## Rectifier Mode (AC to DC)

In AC-to-DC mode, the module receives single-phase, split-phase, or three-phase AC (208–480 V, 50/60 Hz) from the grid and performs power factor correction to minimize reactive power and harmonic distortion, achieving a power factor above 0.99 and THD of less than 5%. The SiC switching devices modulate the input current to shape it while actively controlling both amplitude and phase to draw a near-sinusoidal current from the grid. The module can perform precharge thanks to the built-in circuit that eliminates inrush currents to avoid damage to the converter. An internal soft-start algorithm limits the inrush current and avoids grid disturbances.

The DC link voltage is controlled by user setpoints within the range of 360 V to 950 V. Current is regulated bidirectionally within the power envelope of 93kW (at 400 V/50 Hz).


**Key Features:**

- Active Power Factor Correction (PFC) maintains PF ≥0.99
- Low Total Harmonic Distortion (THDi ≤5%)
- Programmable DC output voltage (650-950V)
- Current limiting and overcurrent protection
- Anti-islanding detection


**Key Features:**

- Grid-tied or standalone operation
- Reactive power control (±0.9 inductive-capacitive)
- Grid forming and following capabilities
- No Neutral wire used (for pure genset applications, ADVANTICS offers a special variant)

## Bidirectionality

All modes of the ADB-PC-GN01 are inherently bidirectional. This is perfectly fine even in unidirectional applications - as the mains tends to be the only source of energy in such systems. You can however emulate unidirectionality even in battery-based systems, by simply limiting negative current setpoint to a low value. Keep in mind that most systems are bidirectional, even if they don't look that way (AC motors, synchronous PFCs in many products).

## Application Examples

Examples pending.


