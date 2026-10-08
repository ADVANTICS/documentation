# Installation Guide for ADB-PC-CH01

This section provides guidance for installing the unit in a permanent location. 

## Position the converter in its intended location

This section covers the physical installation of the **ADB-PC-CH01** unit.

**Prerequisites:**

* Use lifting equipment rated for the converter’s weight. It is recommended to use a scissor-lift table or hydraulic lift cart.
* To mound a uint in a rack, mounting flanges need to be installed on either side of the rack to place the unit on. When selecting
  the flanges, ensure that they are rated to carry the weight of the converter.
* In case of a rack installation, make sure the cabinet/rack is equipped with rails or slides.

**Steps:**

1. **Inspect for Damage:** Visually inspect the unit for any shipping or handling damage before installation.
2. **Lift the Unit:** lift the unit using the lifting equipment (Recommendation: scissor-lift table or the hydraulic lift cart).
3. **Position and Mount:** align the unit in its final position or rack.
4. **Secure the Unit:** slide the unit inside and fasten the unit’s mounting flanges (if used) with the specified bolts and washers.
5. **Torque Bolts:** Use a torque wrench to tighten bolts to the specified mechanical values.



## Wiring the converter

!!! WARNING "**RISK OF ELECTRIC SHOCK**"
      This procedure must only be performed by qualified personnel. Ensure all power sources (Port A and Port B) are **de-energized, disconnected, and locked out**.

The power connectors, their keying and the full list of mating part numbers are described on the [Connectors](connectors.md) page.
For the current class of the ADB-PC-CH01 (up to 75 A<sub>rms</sub> per phase on the AC port, up to 60 A on the DC port) the following
mating connectors and cables are required:

| **Connector label** | **Mating connector** | **Cable** | **Notes** |
|---------------------|----------------------|-----------|-----------|
| **L1, L2, L3** | 3x SLPHPA25BSO1 | 35 mm2, rated for 480 V<sub>rms</sub> L-L | Orange, 20&deg; |
| **DC+** | 1x SLPHPB35BSR1 | 35 mm2, rated for 950 V DC | Red, 20&deg; |
| **DC-** | 1x SLPHPB35BSB2 | 35 mm2, rated for 950 V DC | Black, 30&deg; |
| **PE** | Ring lug for M8 thread | min. 16 mm2 | Front panel, tightened to 6 N.m |

The cross section assumes standard 70 &deg;C PVC insulation. With higher rated insulation (e.g. XLPE) a smaller cross section may be
possible, see [Selection of connector part numbers](connectors.md#selection-of-connector-part-numbers).

The unit is controlled via CAN. the two 'Link' connectors are internally shorted together, allowing multiple units to be connected
to the same physical can bus, without needing to splice cables or add T-junctions. To allow for reliable control systems in
electrically noisy environments, ensure that the cables have a characteristic impedance of 120 Ohms and the ends of the bus are
properly terminated. The external wiring may also be done in such a way as to have two independent cables carry control signals
to each unit, allowing for a physically redundant control path.

The 24V power runs the converter controls, as well as auxiliary devices inside the converter. The power draw for a single converter is
up to 3A continuous, with load spikes. It is possible to power multiple units from the same supply. In this case the supply needs
to be able to support the load. On large installations it is important to consider the voltage drop accross a long cable. It is
recommended to include overcurrent protection at the power supply output. Consult with ADVANTICS for larger installations.

### Connect power wiring

1. **Cable Check**
      * ensure that you have the correct wire cross sections, all the connectors are firmly attached to the cables and all
        connectors are clean, check that all cables have the required connectors listed above.

2. **Lock out Tag Out**
      * ensure the system that the ADB-PC-CH01 is deenergized and can't be energized accidentally during installation.

2. **Connect Cables**
      * attach PE first: a protective earth conductor of at least 16 mm2 to the M8 thread on the front panel, tightened to 6 N.m.
      * Verify the Phase ploarity and attach the phases to the specified connectors on the front panel(L1, L2, L3)
      * Connect DC+ and DC- cables. Ensure that all Surelock connectors are latched to the front panel.

### Connect control wiring

1. **Control wire connection**
      * screw the M12 connector into one of the 'Link' ports. Check the cable and the connector for the mating tab and align them
        before inserting.
      * check for proper mating of the connectors. the screw shroud should be close to the font panel.
2. **Control power connection**
      * Ensure that the power supply is turned off
      * Align the tabs in the cable and the connector. the power wire tab is in the center of the connector
      * screw the cable on and check a proper fit.

## Connect the Cooling System

This section describes the procedure for connecting the **liquid cooling loop** of the converter.

**Prerequisites:**

   * Cooling circuit is flushed and filled with **appropriate coolant** - water/glycol mix with corrosion inhibitors and organic growth inhibitors.
   * The pump is **OFF** before connecting.

**Steps:**

   1. Inspect O-rings on the cooling ports for damage or contamination.
   2. Connect the **Coolant In** hose to the inlet port.
   3. Connect the **Coolant Out** hose to the outlet port.
   4. Tighten all fittings securely (avoid overtightening), or install clamps (in case of barbed fittings).
   5. Start the pump at **low flow rate**.
   6. Purge all air from the circuit according to the chiller’s instructions.
   7. Increase to nominal flow rate and check for **leaks**.
