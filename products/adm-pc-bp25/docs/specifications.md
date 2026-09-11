# Electrical and Mechanical Overview


## Electrical characteristics

The ADM-PC-BP25 ships in 4 variants. They differ only in the 4 ratings below; everything else is common to all of them.

### Variant-specific ratings

|Field|VA08|VA01|VA04|VA03|
|-----|----|----|----|----|
|**Voltage range**|800 V<sub>DC</sub> bus max|950 V<sub>DC</sub> bus max|950 V<sub>DC</sub> bus max|950 V<sub>DC</sub> bus max|
|**Current range**|DC/DC: 111 A (37 A per phase)  <br /> AC/DC: 111 A<sub>rms</sub> (37 A<sub>rms</sub> per phase)<br />Derating depends on heatsink design, cooling and ambient conditions|DC/DC: 100 A (33 A per phase)  <br /> AC/DC: 90 A<sub>rms</sub> (30 A<sub>rms</sub> per phase) <br />Derating depends on heatsink design, cooling and ambient conditions|DC/DC: 111 A (37 A per phase)  <br /> AC/DC: 111 A<sub>rms</sub> (37 A<sub>rms</sub> per phase)<br />Derating depends on heatsink design, cooling and ambient conditions|DC/DC: 135 A (45 A per phase)  <br /> AC/DC: 135 A<sub>rms</sub> (45 A<sub>rms</sub> per phase)<br />Derating depends on heatsink design, cooling and ambient conditions|
|**AC rated voltage**|400 V<sub>AC</sub>|480 V<sub>AC</sub>|480 V<sub>AC</sub>|480 V<sub>AC</sub>|
|**AC 3-phase operating voltage range**|208 V<sub>AC</sub> to 400 V<sub>AC</sub>, neutral wire not used|208 V<sub>AC</sub> to 480 V<sub>AC</sub>, neutral wire not used|208 V<sub>AC</sub> to 480 V<sub>AC</sub>, neutral wire not used|208 V<sub>AC</sub> to 480 V<sub>AC</sub>, neutral wire not used|

### Common to all variants

|Field|Value|
|-----|-----|
|**Power**|DC/DC: 50 kW max  <br /> AC/DC: 25 kW max|
|**Efficiency**|>99% peak|
|**Power factor**|3-phase mode: >0.995 @ 20 kW, >0.99 @ 9 kW  <br />1-phase mode: 0.997 @ 8 kW, >0.99 @ 2500 W|
|**Power flow**|Bidirectional|
|**Power conversion modes**|Step-down (Buck)<br />Step-up (Boost)<br />AC attached (Rectification) <br /> AC generation (Inverter) <br />|
|**AC mains frequency**|45 - 65 Hz|
|**AC 1-phase operating voltage range**|110 V<sub>AC</sub> to 480 V<sub>AC</sub>, one phase, split phase (external capacitors required)|
|**Protection features**|Overcurrent<br />Overvoltage<br />Overheating <br /> Common interlock line<br />'Keep alive' periodic message (optional)|
|**Voltage and current accuracy**|+/-2% (+/-1% typical)|
|**Communication protocol**|CAN bus 2.0B, 500kbit/s with extended addressing|
|**Communication chaining**|Possible. Up to 32 devices of the same type. More if different module types are chained.|
|**Logic interface**|8 pin JST CPT automotive series|
|**Logic power**|24V nominal (Min: 20V, Max: 28V), max 450 mA current per module|
|**Interlock**|Open collector, hardware interlock|

!!! note "AC operating ranges"
    The AC voltage and frequency ranges above describe the electrical operating capability of the
    power stage. They cover the common European and North American nominal AC voltages and
    frequencies. Certification and listing of the finished equipment, including to UL 1741,
    IEEE 1547 or EN 50549-1 where applicable, are determined at system level. See
    [Integration requirements](#integration-requirements).

## Mechanical characteristics

|Field|ADM-PC-BP25|
|-----|-----------|
|**Dimensions**| 230 x 60 x 255 mm (without cooling)|
|**Weight**| 4.0 Kg (without cooling)|
|**Power connectors**| Screw terminals, M5 thread|
|**Operating temperature**| -20 to 50 degrees Celsius (ambient)|
|**Storage temperature**| -20 to 75 degrees Celsius|
|**Storage relative humidity**| 20 to 80% without condensation|

### 3D models

3D models are available for each mechanical variant (see [Drawings of BP25-VA01 and BP25-VA08](installation.md#drawings-of-bp25-va01-and-bp25-va08) and [Drawings of BP25-VA03 and BP25-VA04](installation.md#drawings-of-bp25-va03-and-bp25-va04) in the Installation Guide for the corresponding mechanical drawings):

|Variant|3D model|
|-------|--------|
|VA01 & VA08|[BP25-VA01 3D model](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/3d-models/adm-pc-bp25/ADM-PC-BP25-VA01-R10%20Bidirectional%203phase%20conv.%20AFE.zip)|
|VA03|[BP25-VA03 3D model](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/3d-models/adm-pc-bp25/ADM-PC-BP25-VA03-R10%20Bidirectional%203phase%20conv.%20AFE.zip)|
|VA04|[BP25-VA04 3D model](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/3d-models/adm-pc-bp25/ADM-PC-BP25-VA04-R09%20Bidirectional%203phase%20conv.%20AFE.zip)|

## Connectors and interfaces

The table below lists every electrical interface on ADM-PC-BP25 as supplied.

|Interface|Connector|Function|
|---------|---------|--------|
|DC bus +/-|M5 screw terminal|DC power|
|AC / DC output, 3 phases|M5 screw terminal|AC or DC power|
|CAN 2.0B|8 pin JST CPT, 2 off|Control, status, diagnostics, firmware update|
|INTLK|8 pin JST CPT (shared)|Hardware safety interlock|
|+24 V / GND|8 pin JST CPT (shared)|Control-section supply|

The CPT pinout is given in
[Communication terminal and wiring](installation.md#communication-terminal-and-wiring).

## Integration requirements

ADM-PC-BP25 is supplied as an OEM power-conversion subassembly for integration into equipment built
by the system integrator. It contains the power stage, its control and its own protection; the
functions below belong to the finished equipment and must be provided by the integrator.

|Function|Provided by|
|--------|-----------|
|AC precharge circuit and main AC contactors|Integrator — available as ADM-PC-LF46|
|AC-side EMC filtering|Integrator — available as ADM-PC-LF46|
|AC disconnect and AC overcurrent protection|Integrator|
|Galvanic isolation, where required|Integrator — available as ADM-PC-BI25 or ADM-PC-LL25|
|Grid voltage and frequency trip, anti-islanding, cease-to-energize, reconnect|Integrator|
|Utility or DER communications, where required|Integrator|
|Supervisory control|Integrator|
|Enclosure, cooling, grounding and bonding|Integrator|

Precharge, main AC contactors and AC-side EMC filtering are required for every AC operating mode of
the module, in every product variant.
