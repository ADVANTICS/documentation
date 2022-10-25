> [!UPDATE] {docsify-updated}
# Theory of operation

## Topology

The ADM-PC-LL25 is a DC/DC multi-resonant LLC isolated converter with:

- 3-phase Silicon Carbide bridge
- Isolation transformer
- Output SiC rectifier bridge
- Output safety discharge
- Ground fault detection.

Up to 800V DC bus and 500V output operation is possible. For more details on the specifications, please check the [ADM-PC-LL25 specifications](power-modules/ADM-PC-LL25/specifications.md).

![LLC topology](images/LLC_topology-LLC_topology.svg ':size=70%')
<figcaption style="text-align: center">ADM-PC-LL25 converter topology</figcaption>

The topology is inherently **unidirectional**. A DSP (Digital Signal Processor) is used to control the individual transistor pairs directly – allowing for very versatile control modes and strategies.

## Operating range

The ADM-PC-LL25 operating range is complex to define. The absolute maximum operating range is defined in the picture below:

![LLC absolute range](images/LLC_max_absolute_range.JPG ':size=40%')
<figcaption style="text-align: center">ADM-PC-LL25 absolute maximum operating range</figcaption>

However, the actual reachable operating points will depend on the output current, the input voltage, the output voltage and their ratio. Furthermore, the LLC can be used with other power converters, or with our ADM-PC-BP25 or ADM-PC-UP25 as power factor correction (PFC) unit upstream. This allows the LLC to increase the operation range, as it can automatically adjust the input voltage depending on the needs.

>[!WARNING] Only the last LLC hardware revision (rev. 4), is able to reach 70 Amps as max current. For previous hardware revisions, maximum reachable current is 60 Amps. Heatsink and cooling restrictions must still be taken into account to derate this value.

>[!TIP] **Always ask ADVANTICS** if you are not sure wether the module can operate in a specific operating point or in certain scenarios. 

Therefore, the LLC operating range will be divided in two scenarios: 'single' and 'advantics combo'

### Single DC/DC
In this scenario, the LLC is used as an independent DC/DC isolated converter. The input voltage source can be any other generic power converter, as long as the input voltage to the LLC is within 450-750 Volts.

The normalized operating range is shown below:

![LLC single ratio](images/LLC_single_ratio_range.JPG ':size=40%')
<figcaption style="text-align: center">ADM-PC-LL25 normalized operating range when used in single DC/DC operation</figcaption>

For an operating point to be reachable, it has to fall within the blue areas of both the normalized and the absolute operating range. Notice that for the normalized operating range, there is a darker blue area. The reachable points in this area will depend on the input voltage to the module. For a 450 V input, none of the dark blue area is rachable, wheras for the highest input voltage (750 V), the whole dark blue area is reachable.

To operate the LLC, use the 'Voltage control' mode. For more information, please refer to the [Control Modes](power-modules/ADM-PC-LL25/ADM-PC-LL25.md#control_modes) subsection.

### Advantics combo for AC/DC conversion (BP25 + LL25 or UP25 + LL25)
In this scenario, the LLC is used together with a BP25 or a UP25 Advantics module. The BP25 or UP25 is used as AC/DC power converter with power factor correction, whereas the LLC is used as DC/DC isolated converter. The LLC will automatically manipulate the BP25 or UP25 for optimal operation. For this reason, the **reachable operating range is equal to the absolute maximum operating range**:

![LLC absolute range](images/LLC_max_absolute_range.JPG ':size=40%')
<figcaption style="text-align: center">ADM-PC-LL25 absolute maximum operating range</figcaption>

>[!NOTE] **The BP25 or the UP25 must have the same stack address as the LLC to work** properly.

>[!WARNING] When used with the UP25 module, the maximum output current should NOT be above 52 Amps. This is due to UP25 limitations.

To operate the LLC with the Advantics combo, use the 'PPFC Voltage control' mode. For more information, please refer to the [Control Modes](power-modules/ADM-PC-LL25/ADM-PC-LL25.md#control_modes) subsection.

## Allowed load types 
The ADM-PC-LL25 is designed and optimized to work in battery charging applications. However, starting with firmware 2022.10.19, the LLC can be used as a generic DC/DC isolated converter to power other loads as well, such as resistive loads.

>[!NOTE] **If a resistive load is present at the output, then, the minimum resistance of the load must be 4 Ohms**. Reachable operating range above still applies.

>[!WARNING] The module is not able to generate an open circuit voltage. Thus, the module has to be enabled always under a load (either a battery or a resistive load), or it has to be precharged at the output with the 'precharge' operation mode.


## Protection mechanisms

#### Overcurrent (L1,L2,L3) protection

The overcurrent protection has three levels. HW, FW and SW. The HW protection is set to +-65 Amps per phase, refered to the peak phase current. It is instantaneous, using window comparators and logic, and is fully independent of the digital signal processor firmware. The FW protection is set to +-60 Amps and is verified on low-pass filtered signal with BW of approximately 5 Hz. SW protection works on the same level as FW protection, but is user-adjustable over CAN bus.

#### Overvoltage protection

Similarly there is a three level overvoltage protection on the DC bus. The limit is set to 860 V (VA08 variant) and 1060 V (VA01 variant), is instantaneous, using comparators and logic, and is fully independent of the digital signal processor firmware. A voltage exceeding this level will cause a converter shutdown. Customer should be aware that the module has no means of protecting itself if excessive voltage is presented on its input. Excessive voltage will destroy the switching devices. The L1, L2, L3 voltages only provides SW protection for user’s convenience, as the phase voltages are always lower or equal to the DC bus voltage.

#### Active high voltage discharge

The module has a fast internal bleeding circuit for capacitor discharge. The purpose of this bleeder is to remove any residual voltage on the terminals when the converter is not operating. 

The bleeding circuit is enabled in any of the following two cases:
- If the interlock line is tripped either manually or due to overcurrent/overvoltage.
- If the user sends a "bleed" command over CAN. Refer to the [CAN messages](power-modules/ADM-PC-LL25/ADM-PC-LL25.md#llc_fault_control) for more information on the message to send.

#### Safety ground fault protection

The module constantly monitors the insulation resistance between the negative output terminal of the module and the safety ground connection. This ground insulation resistance is reported over CAN bus.


## Limits

When talking about similar topologies, there are four main limiting aspects – the voltage, current, power and temperature. Since the converter can be used in many different ways, the way how limits are considered also changes. To make understanding these limits easier, always think of limits per phase (even if they are connected in parallel).

#### Voltage limit

Input voltage: up to 800 V
Output voltage: from 200 to 500 V

> [!WARNING]
> The module is equiped with HW protections that will shut down the converter if the limits are exceeded. 
> But the module cannot protect itself against voltages applied on its terminals. Make sure that the applied voltage is within the operational limits


#### Current limit

The maximum output current is 70 Amps for hardware revision 4. For earlier versions, current limit is 60 Amps. If you are using a UP25 as PFC unit, then the maximum current limit is 52 Amps. 

#### Power limit

The module maximum power is 30 KW for hardware revision 4. For earlier versions, power limit is 25 KW. Operation under that level is safe. Contact Advantics if your application requires slightly higher power levels.

#### Thermal limit

There are two temperature sensors (diode rectifier and mosfet bridge) installed in the module plus an optional transformer temperature sensor. 

Both sensors report the current temperature over the CAN bus (in degrees Celsius). The shutdown temperature of the mosfet bridge, the diode rectifier and transformer is **85 °C**.

Upon reaching the overheating condition, the converter will stop operating (still reachable via CAN communication) but without tripping the interlock line. This means that other modules chained in the same bus will still continue normal operation.

> [!WARNING]
> Care must be taken to not operate the module near the temperature limits, as it will reduce the lifetime of the unit.

> [!NOTE]
> It is not always practical to implement derating on the module level. In applications where the module is just one of the power stages, derating has no meaning - if the power delivery dropped, the voltage would collapse and downstream power converters would simply attempt to extract power by drawing more current, further collapsing the voltage. Therefore on default the module does not derate – it will simply shut down when maximum temperature is exceeded. A high-level system must implement derating strategy, if such feature is needed by the application.

## Control modes

The ADM-PC-LL25 can operate in a few control modes. 

To start operating the device, please refer to the [Quick Start](power-modules/ADM-PC-LL25/quick_start.md) section. However, it can be summarized in:
1. Power up and clear interlock
2. Select setpoints
3. Select control mode and enable

Setpoints are configured as follows:

- Frequency setpoint in **LLC_PWM_Frequency_Control** message
- Voltage setpoint in  **LLC_Voltage_Setpoint_Control** message
- Current setpoint in **LLC_Current_Setpoint_Control** message

>[!TIP] Refer to [Application examples](power-modules/ADM-PC-LL25/application_examples.md) to see typical circuit applications and connection diagrams. 

### PWM mode
In this mode, the user selected pwm frequency is directly applied in each phase. This is for testing purposes only and should never be used by customers.

>[!WARNING] Do not use this mode unless it is required by Advantics for test purposes

### Current control
In this mode, the module behaves as a constant current source, pushing the current selected by the user.

### Voltage control
In this mode, the module behaves as a constant current/constant voltage (CC/CV) source, where the module will provide a constant voltage unless the current limit has been reached, in which case a constant current will be applied.

### Precharge
In this mode, the module will apply short power pulses to slowly charge the output capacitor up to a safe voltage level. Then, the higher-level controller will normally switch to any of the other control modes.

![basic connection](images/LLC_basic_connection-LLC_basic_connection.svg ':size=60%')
<figcaption style="text-align: center">Example connection of ADM-PC-LL25 in pwm, current control, voltage control or precharge modes</figcaption>

### PFC Current control
This mode is equivalent to [Current control](#current-control) mode, but it additionally sends a voltage setpoint to an upstream ADM-PC-BP25 or ADM-PC-UP25 converter working as 3-phase rectifier and power factor correction. Hence, the input voltage of the ADM-PC-LL25 is automatically controlled within a range of 650 to 750 V in this mode, extending the control range.

This mode will allow better and more efficient control of the output.

### PFC Voltage control
This mode is equivalent to [PFC Current control](#pfc-current-control) mode, but acting as a constant current/constant voltage source.


![basic connection](images/app_3phase_charger.svg ':size=80%')
<figcaption style="text-align: center">Example connection of ADM-PC-LL25 in PFC Current control or PFC Voltage control modes</figcaption>
