# Theory of Operation

The ADB-PC-DC01 is designed to be a building block of bidirectional battery charge/discharge applications, voltage bus conversion systems, power suppliers or similar projects that require reinforced galvanic insulation. This module operates in two primary modes controlled through CAN bus commands or digital control inputs to regulate the voltage at its ports: Port A or Port B. Each mode defines the internal power-conversion state and external power-flow behavior. It can be paralleled with other ADB-PC-DC01s to drive loads in the megawatt range by providing user-configurable drooping capability.

The module is able to operate over a very wide range of Port B voltages between 200V and 1500V, where Port A is kept within 750V and 950V.  This is achieved using a novel interconnection strategy that utilizes the galvanic isolation to boost the output voltage above the input voltage, thus reaching the voltages required for different applications, while maintaining excellent conversion efficiency.

## Applications

The ADB-PC-DC01 is suited for high power electric-vehicle DC charging, covering CCS1, CCS2, NACS, CHAdeMO and MCS. It integrates cleanly with energy-storage systems and supports full V2G operation thanks to it bidirectional topology that is designed to meet stringent reinforced insulation requirements. It can be used in any application that requires a large voltage regulation along with isolated bidirectionality, such as V2G systems. These applications require a wide voltage range to allow all kinds of vehicle types to be connected. Additionally, it functions effectively in EV chargers and charger simulators, DC voltage isolation and conversion aboard ships, mining equipment, or as a laboratory-grade isolated bidirectional power source. The design maintains reliability in harsh locations, including marine, coastal, and mining environments.

Even though the module is fully bidirectional, port A and port B are not symmetrical due to the supported voltage ranges and use cases for each port. When deploying the DC01, this asymmetry should be kept in mind. 

ADB-PC-DC01 can regulate the voltage at either Port A or Port B, but not both at the same time. It is up to the user’s discretion to choose which side needs regulation and make the connections accordingly.

## Module architecture

To achieve the wide output voltage range required by charging standards, the ADB-PC-DC01 utilizes two power conversion subsystems that are automatically reconfigured depending on the voltage present at port A and port B. These subsystems are then connected either in a 'Quasi-Parallel (QP)' or in a 'Quasi-Series (QS)’ connection. The particular configuration has an impact on the voltage and current limits on the ports.

ADB-PC-DC01 is automatically configured to operate in QP mode when the Port A voltage is higher than the Port B voltage. This mode increases the current capability of the converter while respecting the 100kW power limit. 

For applications where Port B voltage is expected to be higher than Port A voltage, the unit reconfigures itself to be connected in QS. This voltage is limited to twice the voltage at Port A or 1500V, whichever is smaller. Again, this mode operates respecting the power envelope of 100kW based on the voltage rating. 

The QP configuration is used when:

$$
V_A > V_B
$$

The QS configuration is used when:

$$
2V_A > V_B > V_A
$$

To prevent the system from switching back and forth between QP and QS connections at the border condition where Port A voltage is equal to Port B voltage, a hysteresis switchover algorithm is utilized. This reconfiguration is done automatically and without requiring any external intervention by the user.

## Operation Mode 1: Port B control

In this mode of operation, Port A must be connected to a regulated voltage source to operate properly. An external precharge is required when connecting voltage source to the port A.

When the converter is operating, Port B is actively controlled depending on the user setpoints and the characteristics of the load connected to Port B. A standalone ADB-PC-DC01 operated in ‘Port B control mode’ can not exceed 100kW, or the maximum power capability of Port A, whichever is smaller.

When used as a power supply, the ADB-PC-DC01 can automatically precharge the Port B, without a need for external voltage matching.

In battery-connected systems, Port B is first internally precharged to the actual Port B voltage. This is automatic, and the user doesn't need to do anything specific.

Power delivery towards Port B, in other words, ‘charging’, is possible to achieve by putting a voltage setpoint that is higher than the battery voltage until the desired battery voltage is reached. The converter will operate in constant current (CC) mode until the voltage setpoint is reached, and the current will always be limited by the setpoint defined by the user. Once the target voltage is reached, the operation switches to constant voltage mode (CV). An example CC/CV charging graph is shown below. The voltage and current setpoints in this example are set as 700V and 100A, respectively, when the battery was initially 500V. Charging continues in CC mode until the 700V setpoint is reached, then CV mode takes over until the end of charge.

In other words, the converter behaves like any other lab power supply, with Voltage setpoint and Current limit values beig set over CAN bus.

{{ figure('../assets/cc_cv_charge_session.png', 'An example CC/CV charging session of a battery, charged from 500V to 700V at a maximum 100A') }}

Power delivery towards Port A, in other words, ‘discharging’, is also possible to achieve by appropriate voltage and current setpoints by the user. After connecting Port B to the battery with a precharge sequence, the Port B voltage setpoint should be set lower than the actual battery voltage, along with a negative current setpoint. In this configuration, ADB-PC-DC01 will try to regulate Port B by discharging the battery at the user-defined current limit. Similar to the charging operation, the discharging follows CC/CV operation.

In summary, based on the voltage and current setpoints by the user, the ADM-PC-DC01 is capable of charging and discharging a battery pack after a precharge session.

## Operation Mode 2: Port A Control

In this mode of operation, Port B requires a regulated voltage source to operate properly. When the converter is operating, Port A is actively controlled depending on the setpoints of the converter and the characteristics of the load connected to Port A within a 750V-950V range. This mode is particularly interesting when the source voltage is above 950V (maximum voltage supported by Port A), and regulation is required on the other side of the converter. A standalone ADB-PC-DC01 operated in ‘Port A control mode’ can not exceed 100kW, or the maximum power capability of Port B, whichever is smaller. Thus, an external system is needed to control the voltage on port A while being able to source or sink the required power, on top of the minimal power losses on ADB-PC-DC01.

The principle of operation is identical to ‘Port B control mode’, while the only difference is the Port that is regulated by ADB-PC-DC01. 

When connecting the voltage source to Port B, the user must make sure that it is done via a precharge circuit since connecting a battery directly to the terminals will cause a high inrush current. After the successful precharge session, ADB-PC-DC01 can regulate voltage and power at Port A.

## Example application 1: 100kW 3-Phase Bidirectional Charger

An ADB-PC-DC01 can be a building block of a bidirectional battery charging system (e.g., G2V, V2G). The diagram below illustrates the connection diagram of such a system, where a 3-phase grid is connected to ADB-PC-DC01 through ADB-PC-AC01 (Advantics 100kW bidirectional active front end operating in PFC mode). In this system, Port B control mode would be used to regulate the power transfer.

{{ figure('../assets/3-phase-bidir-charger.png', '3-phase bidirectional charger diagram that employs ADB-PC-DC01 and ADB-PC-AC01') }}

Let’s consider that a regulated 800V is connected to Port A of ADB-PC-DC01, and the actual battery voltage is 1100V, and the goal is to charge it to 1500V at the desired current. In this case, the user voltage setpoint will be 1500V, and the current setpoint will be the required charging current, not exceeding the 100kW power envelope. The power module will charge the battery in CC mode until the battery reaches 1500V. Then, the charging will continue in CV mode until the battery is fully charged. Conversely, if the goal is to discharge this battery to 850V, the voltage setpoint will be 850V along with the desired negative current setpoint, not exceeding the 100kW power envelope.

 

## Example application 2: 100kW bidirectional Battery-to-Battery charging

When connected as shown below, it is possible to deliver power from one battery pack to another. ADB-PC-DC01 supports charging in both directions, under the condition that the batteries are connected to the unit with a precharge circuit to eliminate high inrush currents to the capacitor banks on Port A and Port B. 

Both control modes support this application.

{{ figure('../assets/battery-to-battery-charging.png', 'Battery-to-battery charging system that employs ADB-PC-DC01') }}

These diagrams are simplified, and don't include precharge, fuses, filtering or contactors. We recommend consulting your system diagram with ADVANTICS before building a complete system.