# **2. ADM-PC-BI25 Module Overview**

The ADVANTICS module, <font color="#00A89D">**ADM-PC-BI25**</font> is an advanced DC/DC power converter based on Capacitor-Inductor-Inductor-Inductor-Capacitor (CLLLC) topology. It provides reinforced galvanic isolation between its two ports, eliminating the need for a large mains transformer. The converter is fully symmetrical, providing bidirectional power transfer based on Silicon Carbide (SiC) technology. Its reinforced galvanic isolation makes it physically impossible for battery short-circuit currents to propagate through the system in the event of a fault, while also creating a robust electrical barrier that supports effective isolation monitoring in mixed-voltage environments.

{{ figure('../assets/image.png', 'A schematic of the CLLLC topology') }}

The thermal system of this converter is specially built to allow BI25 to rely entirely on conductive heat transfer, enabling the unit to be installed in a sealed enclosure. The integrated control system features overvoltage, overcurrent and overtemperature protection systems to enhance operational safety. The unit is controlled via an industry standard CAN v2.0B bus. All its control signals are published via KCD/DBC files allowing easy integration into a supervisory control system.  Thanks to its compact and robust design, the BI25 power module can operate in mobile applications where traditional transformers would fail.

{{ figure('../assets/Figure1.jpg', 'Physical view of the ADM-PC-BI25 (BI25) power converter') }}
