# Installing the ADM-PC-LL25

## Unpacking

#### Visual check of parts <!-- {docsify-ignore} -->
Check if all parts look unbroken (intact). In case of doubt, contact the sales department by the e-mail: info@advantics.fr

#### Content of package <!-- {docsify-ignore} -->
Please check the content of the package and compareit against the list attached in the transport box. 

#### Storage conditions outside of the transport box <!-- {docsify-ignore} -->
Temperature: 0 to 45 °C
Relative humidity: 20 – 80 % without condensation

<!--#### Safety and electrical insulation
The module live parts including output/input terminals are of IPXX protected.-->

## Form factor

All the ADVANTICS power modules from the MCP-25 series share a similar mechanical and electrical form factor. For example every module fits on a 300 mm wide heatsink, the height is chosen such that a space from the module base to the top of the module is always maximum 70 mm – allowing the customer to reuse the same cooling and housing concept for every MCP-25 series power converter.
Some of the common features are:

- The narrowest X-Y dimension is less than 300 mm
- The height of the module is less than 70 mm
- The power inputs and outputs use M5 threaded screw terminals
- The communication interface uses 8-pin JST CPT connector
- Each power module have at least one (optimally two) communication interface connectors
- All mounting screws holes for mounting to the heatsink are designed for 5 mm screws
- 24V powered
## Cooling considerations

For a correct operation, sufficient cooling is needed. **Never run the module without a heatsink attached!** The thermal protection might not react fast enough, if the transistor bar is not cooled.
The power modules are designed to be installed on a flat metallic cooling surface. The module can output up to 750 W of heat through the aluminium bar and inductors. This heat needs to be evacuated through the user-supplied metallic plate. It is possible to use either forced aircooled heatsink or a watercooled plate. Consult the details of your implementation with ADVANTICS for cooling design verification. Pre-drilled heatsinks for module verification are also offered for rapid prototyping.
There are three cooling surfaces on this module – a transistor bar, a diode rectifier bar and a transformer block. Check the [Mounting and assembly procedure](#mounting-and-assembly-procedure) section for more information on the recommended mounting material and process.

![3phase charging](assets/heat_path.png){ width="80%" }
<figcaption style="text-align: center">3D view and heat distribution on LLC</figcaption>

## Drawings

The following figures show the main mechanical dimensions for mounting of the module:

![3phase charging](assets/llc_bottom.png){ width="30%" }
<figcaption style="text-align: center">Bottom view</figcaption>

![3phase charging](assets/llc_top.png){ width="40%" }
<figcaption style="text-align: center">Top and side view</figcaption>


## Mounting and assembly procedure

### Recommended accessories <!-- {docsify-ignore} -->

- ACC Silicone AS1803
- Thermal paste
- Screw ISO 14579 M5 x 55			8 pcs
- Screw ISO 14579 M5 x 30			3 pcs
- Washer spring DIN 7980 5 mm		8 pcs	
- Washer plate DIN 433 5.3 mm		11 pcs (19 pcs)
- Tool: Screwdriver bits ¼”, Torx, Size X25

![3phase charging](assets/accessories.png){ width="40%" }
<figcaption style="text-align: center">Recommended accessories</figcaption>


### Process <!-- {docsify-ignore} -->

1. Clean the surface of the cooler (degrease).
2. Place plastic stud (spacer) Thora AB-IA-M5-SW10, AR.N: 100 32 47 in to holes in the cooler.
3. Place thermal paste on the cooling bars and cover of magnetic part on the module.

    ![3phase charging](assets/thermal_paste_areas.png){ width="40%" }
    <figcaption style="text-align: center">Areas to apply thermal paste</figcaption>

4. Place the module on the cooler.

    ![3phase charging](assets/llc_with_cooler.png){ width="40%" }
    <figcaption style="text-align: center">Module on cooler</figcaption>

5. Place screws with washers into the holes. The module is designed for screws M5, but M4 are possible to use as well, if the design of the cooler request it. Apply initial tightening torque on screws of 2.5 Nm. After a thermal cycle, retight all screws to the nominal torque. 

!!! warning
    After applying power and having performed a thermal cycle, make sure the module is turned off, cooled down and free of any remaining current or charge in the capacitors before reapplying the torque.

![3phase charging](assets/assembly_screws_labels.png){ width="40%" }
<figcaption style="text-align: center">Screws insertion</figcaption>
