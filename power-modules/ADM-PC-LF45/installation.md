> [!UPDATE] {docsify-updated}
# Installation

[installation.md](../common/installation_unpacking.md ':include')

## Cooling considerations

For a correct operation, sufficient cooling is needed. **Never run the module without a heatsink attached!** The thermal protection might not react fast enough.
The power modules are designed to be installed on a flat metallic cooling surface. The module can output up to 750 W of heat through the aluminium bar and inductors. This heat needs to be evacuated through the user-supplied metallic plate. It is possible to use either forced aircooled heatsink or a watercooled plate. Consult the details of your implementation with ADVANTICS for cooling design verification. Pre-drilled heatsinks for module verification are also offered for rapid prototyping.
Consult with the Assembly Manual for ADM-PC-LF45 for the list of required materials and the assembly procedure.

## Drawings

The following figures show the main mechanical dimensions four mounting of the module.

![afe top view](images/top_view.png ':size=60%')
<figcaption style="text-align: center">ADM-PC-LF45 top view</figcaption>

![heat flow](images/bottom_view.png ':size=60%')
<figcaption style="text-align: center">ADM-PC-LF45 Bottom view</figcaption>

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

![heat flow](images/accessories.png ':size=50%')
<figcaption style="text-align: center">Recommended accessories</figcaption>


### Process <!-- {docsify-ignore} -->
1. Clean the surface of the cooler (degrease).
2. Place plastic stud (spacer) Thora AB-IA-M5-SW10, AR.N: 100 32 47 into the holes of the cooler.
3. Place the ACC silicone on the top of magnetic components (approx. 5 mm thick).
4. Place thermal paste on the cooling bar on the module.

5. Place the module on the cooler.

6. Place screws with washers into the holes.


7. Apply initial tightening torque on screws. Torque A: 0.5 Nm (Plastic studs), Torque B: 2.5 Nm (Aluminium base)

>[!WARNING] Torque B is necessary to be applied again after the first heat up cycle. Make sure the circuit is off, cooled down and free from any 
residual current, then repeat tightening OF ALL screws.)

[installation.md](../common/installation_cabling.md ':include')


