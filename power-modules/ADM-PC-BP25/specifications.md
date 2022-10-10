> [!UPDATE] {docsify-updated}

# Specifications


## Electrical characteristics

<div class="compact-table">

|Field|ADM-PC-BP25 (VA08)|ADM-PC-BP25 (VA01)|
|-----|------------------|------------------|
|**Voltage range**|800 V<sub>DC</sub> bus max |1000 V<sub>DC</sub> bus max|
|**Current range**|DC/DC: 111 A (37 A per phase)  <br /> AC/DC: 111 A<sub>rms</sub> (37 A<sub>rms</sub> per phase)<br />Derating depends on heatsink design, cooling and ambient conditions|DC/DC: 100 A (33 A per phase)  <br /> AC/DC: 90 A<sub>rms</sub> (30 A<sub>rms</sub> per phase) <br />Derating depends on heatsink design, cooling and ambient conditions|
|**Power**|DC/DC: 50 kW max  <br /> AC/DC: 25 kW max|DC/DC: 50 kW max  <br /> AC/DC: 25 kW max|
|**Efficiency**|>99% peak|>99% peak|
|**Power factor**|3-phase mode: >0.995 @ 20 kW, >0.99 @ 4.5 kW  <br />1-phase mode: 0.999 @ 8 kW, >0.99 @ 600 W|3-phase mode: >0.995 @ 20 kW, >0.99 @ 4.5 kW  <br />1-phase mode: 0.999 @ 8 kW, >0.99 @ 600 W|
|**Power flow**|Bidirectional|Bidirectional|
|**Power conversion modes**|Step-down (Buck)<br />Step-up (Boost)<br />Grid attached (Rectification) <br /> AC generation (Inverter) <br />|Step-down (Buck)<br />Step-up (Boost)<br />Grid attached (Rectification) <br /> AC generation (Inverter) <br />|
|**AC mains frequency**|45 - 65 Hz|45 - 65 Hz|
|**AC rated voltage**|400 V<sub>AC</sub>|480 V<sub>AC</sub>|
|**AC 3-phase grid support**|208 V<sub>AC</sub> to 400 V<sub>AC</sub>, neutral wire not used|208 V<sub>AC</sub> to 480 V<sub>AC</sub>, neutral wire not used|
|**AC 1-phase grid support**|110 V<sub>AC</sub> to 480 V<sub>AC</sub>, one phase, split phase (external capacitors required)|110 V<sub>AC</sub> to 480 V<sub>AC</sub>, one phase, split phase (external capacitors required)|
|**Protection features**|Overcurrent<br />Overvoltage<br />Overheating <br /> Common interlock line<br />'Keep alive' periodic message (optional)|Overcurrent<br />Overvoltage<br />Overheating <br /> Common interlock line<br />'Keep alive' periodic message (optional)|
|**Voltage and current accuracy**| +/-2% (+/-1% typical)| +/-2% (+/-1% typical)|
|**Communication protocol**|CAN bus 2.0B, 500kbit/s with extended addressing|CAN bus 2.0B, 500kbit/s with extended addressing|
|**Communication chaining**|Possible. Up to 32 devices of the same type. More if different module types are chained.|Possible. Up to 32 devices of the same type. More if different module types are chained.|
|**Logic interface**| 8 pin JST CPT automotive series|8 pin JST CPT automotive series|
|**Logic power**| 24V nominal (Min: 20V, Max: 28V), max 450 mA current per module|24V nominal (Min: 20V, Max: 28V), max 450 mA current per module|
|**Interlock**| Open collector, hardware interlock|Open collector, hardware interlock|

</div>

## Mechanical characteristics

<div class="compact-table">

|Field|ADM-PC-BP25|
|-----|-----------|
|**Dimensions**| 230 x 60 x 255 mm (without cooling)|
|**Weight**| 4.0 Kg (without cooling)|
|**Power connectors**| Screw terminals, M5 thread|
|**Operating temperature**| -20 to 50 degrees Celsius (ambient)|
|**Storage temperature**| -20 to 75 degrees Celsius|
|**Storage relative humidity**| 20 to 80% without condensation|

</div>