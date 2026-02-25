# **4.1. Mechanical and Electrical Overview**

## **4.1.1. Content of package**

Please check the content of the package and compare it with the Box Content List, provided with the shipped package. Verify that all components are intact and free from visible damage. In case of any doubt regarding the condition of the items, please contact our Sales Department: [**sales@advantics.fr**](mailto:sales@advantics.fr)

## **4.1.2. Storage Conditions**

When stored outside of the transport box, the module should be kept at temperatures between -30°C and 65°C, with relative humidity between 20% and 80%, without condensation.

## **4.1.3. Form Factor**

{{ figure('../assets/Figure2.png', 'Mechanical view with dimensions of the module') }}

All ADVANTICS power modules share a similar mechanical and electrical form factor. For example, every module fits on a 300 mm wide heat sink and the height is chosen such that a space from the module base to the top of the module is always maximum 70 mm. 

This allows the customer to reuse the same cooling and housing concept for ADVANTICS module power converters. Some of the common features of these converters are: 

* The narrowest X-Y dimension is less than 300 mm   
* The height of the module is less than 70 mm   
* The power inputs and outputs use M5 threaded screw terminals   
* The communication interface uses 8-pin JST CPT connector \- Each power module have at least one (optimally two) communication interface connectors   
* All mounting screws holes for mounting to the heatsink are designed for 5 mm screws   
* 24 V powered

## 

## **4.1.4. Specifications**

Table 1\. Mechanical and Electrical Specifications

|  Parameters |  Values |
| :---- | :---- |
| **Voltage Range** | 500 to 950 V |
| **Voltage Conversion Ratio** | 1:1 |
| **Creepage and Clearance** | IEC 62477-1 and IEC 61851-23 |
| **Overvoltage Category** | OVCII (up to 3000m altitude) |
| **Current Range** | ±60 A |
| **Power** | 50 kW |
| **Power Flow** | Bidirectional |
| **Operating Mode** | 1:1 Voltage Following |
| **Technology** | Silicon Carbide |
| **Efficiency** | 98.7% peak |
| **Assembly** | Flat plate for easy integration |
| **Protection Features** | Overcurrent, overvoltage, overtemperature and external hardware interlock |
| **Voltage and Current Measurement Accuracy** | ±2% (±1% typical) |
| **Cooling** | Air and liquid cooling |
| **Communication Chaining** | Up to 32 devices of the same type |
| **Control Connector** | 8-pin JST CPT |
| **Control System Power** | Max 15 W |
| **Control System Voltage** | 24 V |
| **HV Bus Capacitance** | 80 uF |
| **Weight** | 6.65 kg |
| **Power Density** | 7.52 kW/kg 8.48 kW/L |
| **Operating Heat Sink Temperature Range** | \-20°C to 65°C |
| **Design and Manufacturing** | European Union |

## **4.1.5. Efficiency Measurement**

{{ figure('../assets/1.png', 'Voltage and current envelope') }}

The voltage and current relationship of ADM-PC-BI25 is shown in Figure 4. The envelope is limited by a 50 kW power rating, +-60 A current limit, and 500V-950 V voltage range.

{{ figure('../assets/2.png', 'Efficiency vs Power Rating') }}

{{ figure('../assets/3.png', 'Efficiency vs Power Rating') }}

Efficiency measurements of ADM-PC-BI25 at different bus voltage and power ratings are shown in Figure 5 and 6. Higher bus voltage allows this module to achieve superior efficiency up to 98.7%.


## **4.1.6. Cooling considerations**

For correct operation, sufficient cooling is required. **Never run the module without a heatsink attached\!** The thermal protection might not react fast enough if the transistor bar is not properly cooled. The power modules are designed to be installed on a flat metallic cooling surface. The module can output up to 1250W of heat through the aluminium bar and inductors. This heat needs to be evacuated through the user-supplied metallic plate. It is possible to use either forced air-cooled heatsink or a water-cooled plate to provide cooling. Additionally, please ensure a fan is installed to circulate air over the surface of the board, maintaining uniform temperature and preventing hot spots.

{{ figure('../assets/Figure3.png', 'Module attached to heatsink') }}


!!! tip
    For short tests of the module, the module still needs to be mounted on a heatsink. In this case, please verify the overall temperature of transformers and bars through the CAN message or with ETKA software.

Consult the details of your implementation with ADVANTICS engineering team for cooling design verification. Pre-drilled heatsinks for module verification are also offered for rapid prototyping.

There is only one cooling surface on this module – two bars and a transformer channel is attached to it. This surface should be cooled with a good conducting silicone that cures/solidifies. Consult the Recommended accessories as mentioned in [5.1. Mounting and Assembly procedure](https://documentation.advantics.fr/adm-pc-bi25/6_Setting_up_ADM_PC_BI25/).

## **4.1.7. Functional accessories**

Additionally, users may add the following functional accessories along with the BI25 power module:

* Power supply 24V/3A DC  
* Starter kit for CAN communication and control system power during evaluation and development on MCP-25 power modules can be purchased online: [CAN cable set with 24V power supply](https://store.advantics.fr/adapters/37-can-cable-set-with-24v-power-supply.html)
