> [!UPDATE] {docsify-updated}
# Theory of operation

## Topology

The ADM-PC-LL25 is a DC/DC multi-resonant LLC isolated converter with:

- 3-phase Silicon Carbide bridge
- Isolation transformer
- Output SiC rectifier bridge
- Output safety discharge
- Ground fault detection.

Up to 1200V DC bus and 500V output operation is possible(depending on the product variant). For more details on the specifications, please check the [ADM-PC-LL25 specifications](power-modules/ADM-PC-LL25/specifications.md).

![LLC topology](images/LLC_topology-LLC_topology.svg ':size=70%')
<figcaption style="text-align: center">ADM-PC-LL25 converter topology</figcaption>

The topology is inherently **unidirectional**. A DSP (Digital Signal Processor) is used to control the individual transistor pairs directly – allowing for very versatile control modes and strategies.

## Allowed load types

The ADM-PC-LL25 is designed to work in battery charging applications, and as such, **only battery loads are allowed**.

>[!ATTENTION] Only connect batteries to the ADM-PC-LL25 output. Connecting other types of loads might result in permanent damage in the module, the load, and represent a safety hazard.

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
Output voltage: up to 500 V

> [!WARNING]
> The module is equiped with HW protections that will shut down the converter if the limits are exceeded. 
> But the module cannot protect itself against voltages applied on its terminals. Make sure that the applied voltage is within the operational limits


#### Current limit

The maximum output current is 65 Amps. 

#### Power limit

The module maximum power is 25 KW. Operation under that level is safe. Contact Advantics if your application requires slightly higher power levels.

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
In this mode, the module will apply short power pulses to slowly charge the battery up to a safe voltage level. Then, the higher-level controller will normally switch to any of the other control modes.

![basic connection](images/LLC_basic_connection-LLC_basic_connection.svg ':size=60%')
<figcaption style="text-align: center">Example connection of ADM-PC-LL25 in pwm, current control, voltage control or precharge modes</figcaption>

### PFC Current control
This mode is equivalent to [Current control](#current-control) mode, but it additionally sends a voltage setpoint to an upstream ADM-PC-BP25 or ADM-PC-UP25 converter working as 3-phase rectifier and power factor correction. Hence, the input voltage of the ADM-PC-LL25 is automatically controlled within a range of 650 to 750 V in this mode, extending the control range.

This mode will allow better and more efficient control of the output.

### PFC Voltage control
This mode is equivalent to [PFC Current control](#pfc-current-control) mode, but acting as a constant current/constant voltage source.


![basic connection](images/app_3phase_charger.svg ':size=80%')
<figcaption style="text-align: center">Example connection of ADM-PC-LL25 in PFC Current control or PFC Voltage control modes</figcaption>
