> [!UPDATE] {docsify-updated}
# Servicing

## Manteinance plan

The module does not contain any parts requiring regular maintenance. All the capacitors are either ceramic capacitors (low voltage) or film capacitors (high voltage). There are no electrolytic capacitors prone to drying out, and no cooling fans.

## Serviceability

The module does not contain any user serviceable parts.

## Diagnostics

### Low voltage, control

Diagnostics can be performed over the CAN bus, using ADVANTICS ETKA software. Low level diagnostic include check of low voltage power – measure current on the 24 V supply, to see if it is within the limits. The module contains a number of LEDs – orange ones indicating low voltage power rails, and green ones indicating interlock state and DSP heartbeat (1 Hz). Thermal imagining can also help to discover overheating components.

### Power path

In case of a power converter damage due to high surge currents, optical inspection can be sufficient to discover the failure. Most likely the MOSFET legs will be partially vaporized, and some areas of the board will be covered with metallic dust and carbon buildup from arcing components. If any signs of such damage are discovered, the module is beyond repair. A damage to internal PCB layers is very likely.