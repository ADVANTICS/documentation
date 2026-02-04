# **3. Applications**

## **3.1. Megawatt Charging System (MCS)**

MCS is emerging as a new, universal charging standard built for high-power applications facilitating more efficient and rapid charging for heavy duty vehicles like trucks and cargo ships.

Combined Charging System (CCS) has been the backbone of EV charging infrastructure for years, but it wasn’t exactly designed with megawatt-level use cases, long cables or harsh environments in mind. CCS relies on PLC for data transmission, a method that’s prone to noise, interference, and environmental disruption, due to its single-ended RF nature.  In contrast, MCS employs 10BASE-T1S, a robust, differential, Ethernet-based communication protocol, which is far less susceptible to noise and interference. This enhanced reliability is crucial for ensuring seamless and uninterrupted charging operations, even in demanding conditions. 

Whether it's high-vibration environments like electric trucks or complex installations on marine vessels, MCS can deliver the robust and reliable data communication that heavy-duty EV infrastructure has long awaited.

## **3.2. Distributed DC Fast Chargers**

Once the power of charging stations reach MW levels, the system architecture cannot be an afterthought anymore. With each building block getting bigger, civil engineering gets intensive, the weight of the overall system becomes heavy, and the distance between the parking spots for vehicles and the power converter increases, becoming an issue for typical charging stations. 

One sustainable way to address the topic of breaking down the large monolith into smaller, more practical, segments is to use DC voltage as an interconnecting link. A sensible split is to have a dedicated rectifier for the total required charging power of the installation, let’s say 3MW, and then use rectified voltage around 850VDC as an input for individual MCS charging stations. However, the challenge quickly becomes evident given the IEC 61851-23 and the corresponding UL standards require reinforced isolation between mains, and between individual charge pistols and stalls. Therefore, each charging station should perform two tasks: isolation of the 850 VDC link, and then provide the output control in the range of 200V to 1250V, and up to 1500 V for rugged MCS applications.

ADVANTICS has developed a power converter solution that achieves just that: a two stage conversion system based on the latest SiC transistors, providing reinforced isolation using high frequency technology, and step down buck conversion stage for voltage and current control. With isolated DC/DC converters being connected in parallel on their input, and series on the output, voltage is effectively doubled. By installing output contactors capable of series/parallel reconnect, we also double our effective current for lower voltage vehicles.

The ADM-PC-BI25 power module enables DC microgrid and fast charging architectures by providing isolated, high-efficiency conversion for megawatt charging stations with galvanic isolation without requiring a large mains transformer.

## **3.3. Uninterruptible Power Supply (UPS) for Data Centres**

The ADM-PC-BI25 module is ideal for modern high-voltage UPS systems in data centers, providing galvanic isolation between high power back-up battery systems and expensive/sensitive compute racks. By isolating the high voltage battery at the source it can be individually monitored for isolation resistance, and therefore improve site safety. Its compact design and high efficiency pair well with side car installations and enable megawatt level racks.
