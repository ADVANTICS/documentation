# Theory of Operation

The ADB-PC-DC01 is designed to be a building block of bidirectional battery charge/ discharge applications that require reinforced galvanic insulation. 

The ADB-PC-DC01 module operates in four primary modes controlled through CAN bus commands or digital control inputs. Each mode defines the internal power-conversion state and external power-flow behavior. It can be paralleled with other ADB-PC-DC01s to drive loads in the megawatt range by providing user-configurable drooping capability.

The module is able to operate over a very wide range of Port B voltages, reaching up to double the Port A voltage within 200V and 1500V limits.  This is achieved using a novel interconnection strategy that utilizes the galvanic isolation to boost the output voltage above the input voltage, thus reaching the voltages required for Megawatt Charging System (MCS) charging applications.

## Applications

The ADB-PC-DC01 has many use cases, as both reinforced galvanic isolation and full bidirectionality make it very versatile. One of the main applications for which it was designed is as a building block of an MCS. These applications require a very wide voltage range on the vehicle side to allow all kinds of vehicle types to be connected, while expecting a regulated voltage on Port A.
Even though the module is fully bidirectional, port A and port B are not symmetrical. Port B can be reconfigured internally to expand the voltage range of that port, while port A cannot be reconfigured and needs to be within the 750V and 950V range. When used in an MCS charging system, port A would thus be connected to the grid, while port B may be directly connected to the charging pistol. When deploying the DC01, this asymmetry should be kept in mind.

## Module architecture

To achieve the wide output voltage range required by MCS, the ADB-PC-DC01 utilizes two power conversion subsystems that are automatically reconfigured depending on the voltage present at port A and port B. These subsystems are then connected either in a 'Quasi-Parallel (QP)' or in a 'Quasi-Series (QS)’ connection. The particular configuration has an impact on the voltage and current limits of Port B.

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

To prevent the system from switching back and forth between QP and QS connections at the border condition where Port A voltage is equal to Port B voltage, a hysteresis switchover algorithm is utilized. This reconfiguration is done automatically and without requiring any external intervention.

## Operation Mode: Port B control

The ADB-PC-DC01 has a single operational mode (other than 'Idle'), which is 'Port B control'. Port A requires a regulated voltage source for this mode to operate properly. This means that when the converter is operating, the output of Port B is actively controlled depending on the setpoints of the converter and the characteristics of the load connected to Port B. A standalone ADB-PC-DC01 can not exceed 100kW, or the maximum power capability of Port A, whichever is smaller. Thus, an external system is needed to control the voltage on port A while being able to source or sink the required current.

In battery-connected systems, Port B is first precharged to the actual battery voltage. This module achieves this by either measuring the battery voltage in case it is already connected to Port B, or by the requested voltage setpoints sent by the user. The converter operates in QP or QS mode to match the battery voltage and create a soft connection to the battery before the power delivery starts. Then, the user may start power delivery either towards Port B or Port A.

Power delivery towards Port B, in other words, ‘charging’, is possible to achieve by putting a voltage setpoint that is higher than the battery voltage until the desired battery voltage is reached. The converter will operate in constant current (CC) mode until the voltage setpoint is reached, and the current will always be limited by the setpoint defined by the user. Once the target voltage is reached, the operation switches to constant voltage mode (CV). An example CC/CV charging graph is shown below. The voltage and current setpoints in this example are set as 700V and 100A, respectively, when the battery was initially 500V. Charging continues in CC mode until the 700V setpoint is reached, then CV mode takes over until the end of charge.

<!-- ![An example CC/CV charging session of a battery, charged from 500V to 700V at a maximum 100A. ](Theory%20of%20Operation/image.png) -->

{{ figure('../assets/cc_cv_charge_session.png', 'An example CC/CV charging session of a battery, charged from 500V to 700V at a maximum 100A') }}


Power delivery towards Port A, in other words, ‘discharging’, is also possible to achieve by appropriate voltage and current setpoints by the user. After connecting Port B to the battery with a precharge sequence, the Port B setpoint should be put lower than the actual battery voltage, along with a negative current setpoint. In this configuration, ADB-PC-DC01 will try to regulate Port B to the voltage setpoint by discharging the battery at the current limit. Similar to the charging operation, the discharging follows CC/CV operation.

In summary, based on the voltage and current setpoints by the user, the ADM-PC-DC01 is capable of charging and discharging a battery pack after a precharge session.

**Example application 1: 100kW 3-Phase Bidirectional Charger**

An ADB-PC-DC01 can be a building block of a bidirectional battery charging system (e.g., G2V, V2G). The diagram below illustrates the connection diagram of such a system, where a 3-phase grid is connected to ADB-PC-DC01 through ADB-PC-AC01 (Advantics 100kW bidirectional active front end operating in PFC mode). 

<!-- ![3-phase bidirectional charger diagram that employs ADB-PC-DC01 and ADB-PC-AC01](Theory%20of%20Operation/image%201.png) -->

{{ figure('../assets/3-phase-bidir-charger.png', '3-phase bidirectional charger diagram that employs ADB-PC-DC01 and ADB-PC-AC01') }}


Port B control mode can perform charging and discharging operations on a battery pack, as shown in the above diagram.

Let’s consider that a regulated 800V is connected to Port A of ADB-PC-DC01, and the actual battery voltage is 1100V, and the goal is to charge it to 1500V at the desired current. In this case, the user voltage setpoint will be 1500V, and the current setpoint will be the required charging current, not exceeding the 100kW power envelope. The power module will charge the battery in CC mode until the battery reaches 1500V. Then, the charging will continue in CV mode until the battery is fully charged. Conversely, if the goal is to discharge this battery to 850V, the voltage setpoint will be 850V along with the desired negative current setpoint, not exceeding the 100kW power envelope.

 

**Example application 2: 100kW bidirectional Battery-to-Battery charging**

When connected as shown below, it is possible to deliver power from one battery pack to another. ADB-PC-DC01 supports charging in both directions, under the condition that the batteries are connected to the unit with a precharge circuit to eliminate high inrush currents to the capacitor banks on Port A and Port B.

<!-- ![Battery-to-battery charging system that employs ADB-PC-DC01](Theory%20of%20Operation/image%202.png) -->

{{ figure('../assets/battery-to-battery-charging.png', 'Battery-to-battery charging system that employs ADB-PC-DC01') }}
