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

This mode of operation is suitable for applications where the goal is to obtain a regulation range of 200V to 1500V, using a regulated source with a range of 750V to 950V. The maximum port B voltage is limited to 195% of the port A voltage at all times. This means that, to reach 1500V at port B, a minimum of 770V is required at port A.

In this mode of operation, Port A must be connected to a regulated voltage source to operate properly. An external precharge is required when connecting voltage source to the port A.

When the converter is operating, Port B is actively controlled depending on the user setpoints and the characteristics of the load connected to Port B. A standalone ADB-PC-DC01 operated in ‘Port B control mode’ can not exceed 100kW, or the maximum power capability of Port A, whichever is smaller.

When used as a power supply, the ADB-PC-DC01 can automatically precharge the Port B, without a need for external voltage matching.

In battery-connected systems, Port B is first internally precharged to the actual Port B voltage. This is automatic, and the user doesn't need to do anything specific.

Power delivery towards Port B, in other words, ‘charging’, is possible to achieve by putting a voltage setpoint that is higher than the battery voltage until the desired battery voltage is reached. The converter will operate in constant current (CC) mode until the voltage setpoint is reached, and the current will always be limited by the setpoint defined by the user. Once the target voltage is reached, the operation switches to constant voltage mode (CV). An example CC/CV charging graph is shown below. The voltage and current setpoints in this example are set as 700V and 100A, respectively, when the battery was initially 500V. Charging continues in CC mode until the 700V setpoint is reached, then CV mode takes over until the end of charge.

In other words, the converter behaves like any other lab power supply, with Voltage setpoint and Current limit values benig set over CAN bus.

{{ figure('../assets/cc_cv_charge_session.png', 'An example CC/CV charging session of a battery, charged from 500V to 700V at a maximum 100A') }}

Power delivery towards Port A, in other words, ‘discharging’, is also possible to achieve by appropriate voltage and current setpoints by the user. After connecting Port B to the battery with a precharge sequence, the Port B voltage setpoint should be set lower than the actual battery voltage at port B, along with the user-specified current limit. In this configuration, ADB-PC-DC01 sink power from Port B by discharging the battery at the user-defined current limit. Similar to the charging operation, the discharging follows CC/CV operation.

In summary, ADM-PC-DC01 can charge or discharge a battery connected to Port B in "Port B control mode". If the port B voltage setpoint is higher than the battery voltage connected to port B, power will be delivered to the battery at the current limit defined by the user; if the voltage setpoint is lower than the battery voltage, power will be delivered from the battery at the current limit set by the user.

## Operation Mode 2: Port A Control

This mode of operation is suitable for applications where the goal is to obtain a regulation range of 750V to 950V, using a regulated source with a range of 200V to 1500V. The maximum port B voltage is limited to 195% of the port A voltage at all times. This means that, to reach 750V at port A, the maximum port B voltage can be 1465V. It is recommended to use "Port B control" mode if the regulated voltage source is between 750V and 950V. 

This mode of operation has a limitation in terms of how the initial connections are made. User is responsible for choosing between QP and QS connection before the voltage source is connected to Port B through precharge. 

If the regulated voltage source at port B is less than Vth, a QP connection is required; if the voltage source is greater than Vth, a QS connection is required. Vth is equal to 90% of the minimum expected voltage at port A (e.g., if port A regulation is required between the full range of 750V to 950V, Vth is 90% of 750V, which is 675V. This means that any port B voltage above 675V requires a selection of QS before connecting the voltage source to port B) 

QP connection can not operate at any port B voltage higher than Vth. QS mode, however, can operate at the full range (200V-1500V) with a limited current capability of 110A or 100kW, whichever is smaller.

When used as a power supply, the ADB-PC-DC01 can automatically precharge Port A, without the need for external voltage matching.

In battery-connected systems, Port A is first internally precharged to the actual Port A voltage. This is automatic, and the user doesn't need to do anything specific.

After the startup connections and precharge are completed, respecting the limitations, the user can set a voltage between 750V and 950V at port A, and define the current limit as desired. Similar to 'port B control mode', the power direction is defined by the voltage setpoint. If the port A voltage setpoint is higher than the battery voltage connected to port A, power will be delivered to the battery at the current limit defined by the user; if the voltage setpoint is lower than the battery voltage, power will be delivered from the battery at the current limit set by the user.

## Example application 1: 100kW 3-Phase Bidirectional Charger

An ADB-PC-DC01 can be a building block of a bidirectional battery charging system (e.g., G2V, V2G). The diagram below illustrates the connection diagram of such a system, where a 3-phase grid is connected to ADB-PC-DC01 through ADB-PC-AC01 (Advantics 100kW bidirectional active front end operating in PFC mode). In this system, Port B control mode would be used to regulate the power transfer.

{{ figure('../assets/3-phase-bidir-charger.png', '3-phase bidirectional charger diagram that employs ADB-PC-DC01 and ADB-PC-AC01') }}

Let’s consider that a regulated 800V is connected to Port A of ADB-PC-DC01, and the actual battery voltage is 1100V, and the goal is to charge it to 1500V at the desired current. In this case, the user voltage setpoint will be 1500V, and the current setpoint will be the required charging current, not exceeding the 100kW power envelope. The power module will charge the battery in CC mode until the battery reaches 1500V. Then, the charging will continue in CV mode until the battery is fully charged. Conversely, if the goal is to discharge this battery to 850V, the voltage setpoint will be 850V along with the desired current limit, not exceeding the 100kW power envelope.

 

## Example application 2: 100kW bidirectional Battery-to-Battery charging

When connected as shown below, it is possible to deliver power from one battery pack to another. ADB-PC-DC01 supports charging in both directions, under the condition that the batteries are connected to the unit with a precharge circuit to eliminate high inrush currents to the capacitor banks on Port A and Port B. 

Both control modes support this application.

{{ figure('../assets/battery-to-battery-charging.png', 'Battery-to-battery charging system that employs ADB-PC-DC01') }}

These diagrams are simplified, and don't include precharge, fuses, filtering or contactors. We recommend consulting your system diagram with ADVANTICS before building a complete system.