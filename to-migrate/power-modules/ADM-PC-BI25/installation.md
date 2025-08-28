> [!UPDATE] {docsify-updated}
# Installation

[installation.md](../common/installation_unpacking.md ':include')


## Cooling considerations

For a correct operation, sufficient cooling is needed. **Never run the module without a heatsink attached!** The thermal protection might not react fast enough, if the transistor bar is not cooled.
The power modules are designed to be installed on a flat metallic cooling surface. The module can output up to 750 W of heat through the aluminium bar and inductors. This heat needs to be evacuated through the user-supplied metallic plate. It is possible to use either forced aircooled heatsink or a watercooled plate. Consult the details of your implementation with ADVANTICS for cooling design verification. Pre-drilled heatsinks for module verification are also offered for rapid prototyping.

There are four cooling surfaces on this module – three inductors and one transistor bar. Inductors should be cooled with a good conducting silicone that cures/solidifies. The transistor bar should be cooled with a thermal paste. Consult with the [Recommended accessories](#recommended-accessories) subsection for the list of recommended materials. 

>[!TIP] For a short tests of the module, cooling the inductors may not be needed, but the module still needs to be mounted on a heatsink. In this case, please verify the temperature of inductors through the CAN message or with ETKA software. 

<div class="bigger-300">

![heat flow](images/heat_flow.png "heat flow")
</div>
<figcaption style="text-align: center">Module attached to heatsink with silicone under inductors</figcaption>

## Drawings

The following figures show the main mechanical dimensions four mounting of the module.


## Mounting and assembly procedure

### Recommended accessories <!-- {docsify-ignore} -->
- ACC Silicone AS1803
- Thermal paste
- Screw ISO 14579 M5 x 55
- Screw BN 10649 M5 x 8
- Plastic stud (spacer) Thora AB-IA-M5-SW10, AR.N: 100 32 47
- Washer DIN 7980 5 mm
- Washer DIN 433 5.3 mm
- Tool: Screwdriver bits ¼”, Torx, Size X25

![heat flow](images/recommended_accesories.png ':size=50%')
<figcaption style="text-align: center">Recommended accesories</figcaption>


### Process <!-- {docsify-ignore} -->


[installation.md](../common/installation_cabling.md ':include')

