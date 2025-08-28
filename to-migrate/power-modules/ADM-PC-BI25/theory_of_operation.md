> [!UPDATE] {docsify-updated}
# Theory of operation

## Topology

The ADM-PC-BI25 is a Dual Active Silicon Carbide Bridge (DAB) with up to 1000 V DC bus, 30 amps and 30 KW.


![AFE topology](images/diagrams-DAB_topology.svg ':size=60%')
<figcaption style="text-align: center">ADM-PC-BI25 converter topology</figcaption>

The topology is inherently bidirectional. A DSP (Digital Signal Processor) is used to control the individual transistor pairs directly – allowing for very versatile control.

## Efficiency


## Protection mechanisms

#### Overcurrent protection

The overcurrent protection has three levels. HW, FW and SW. The HW protection is set to +-85 Amps per phase. It is instantaneous, using window comparators and logic, and is fully independent of the digital signal processor firmware. The FW protection is set to +-80 Amps and is verified on low-pass filtered signal with BW of approximately 5 Hz. SW protection works on the same level as FW protection, but is user-adjustable over CAN bus.

#### Overvoltage protection

Similarly there is a three level overvoltage protection on the DC bus. The limit is set to 1050 V, it is instantaneous, using comparators and logic, and is fully independent of the digital signal processor firmware. A voltage exceeding this level will cause a converter shutdown. Customer should be aware that the module has no means of protecting itself if excessive voltage is presented on its input. Excessive voltage will destroy the switching devices. 

#### Keep Alive feature

The user can optionally send a 'Keep Alive' message with a periodicity of 1000 ms or less, so that if communication is lost, the module will disable itself after that time.

This feature is disabled by default upon boot-up. To enable it, the user just has to send the **DAB_Keep_Alive** message (ID 0x80060) with bit 0 set to 1. Then, the module will expect to receive this same message constantly with a periodicity of 1000 ms or less. If not received, the module will disable operation. If the module is already disabled and the message does not arrive, nothing happens.

To disable the feature, send the **DAB_Keep_Alive** message with bit 0 cleared to 0. Then, the module will no longer expect to receive the message, and will not disable operation if the message is not received.

For specific information about the message, please check the [CAN database](power-modules/ADM-PC-BI25/can_database.md) section.

## Limits

#### Voltage limit

The voltage limit is the simplest to consider. The switching devices have blocking voltage defined (1200 V). The maximum allowed voltage is then derated by 200V (that is to 1000 V). The module will not allow the user to exceed these limits. Having higher voltage on both sides of the converter results in higher power available, and higher efficiency.

> [!WARNING]
> The module is equiped with HW protections that will shut down the converter if the limits are exceeded. 
> But the module cannot protect itself against voltages applied on its terminals. Make sure that the applied voltage is within the operational limits


#### Current limit

The current limit of the converter is 30 amps under any voltage level. Therefore, maximum power can only be reached at maximum voltage.

#### Power limit

The maximum power is set to 30 kW. Consult the details with ADVANTICS, if you’re not sure your application fits within the power capabilities.

#### Thermal limit

There are two temperature sensors installed in the module. The inductor temperature sensor, and the bridge temperature sensor (also call as transistor bar sensor). Both sensors report the current temperature over the CAN bus (in degrees Celsius). The shutdown temperature of the transistor bar sensor is **90 °C**. The shutdown temperature of the inductor temperature sensor is **130 °C**.

Upon reaching the overheating condition, the converter will stop operating (still reachable via CAN communication) but without tripping the interlock line. This means that other modules chained in the same bus will still continue normal operation.

> [!WARNING]
> Care must be taken to not operate the module near the temperature limits, as it will reduce the lifetime of the unit.

> [!NOTE]
> It is not always practical to implement derating on the module level. In applications where the module is just one of the power stages, derating has no meaning - if the power delivery dropped, the voltage would collapse and downstream power converters would simply attempt to extract power by drawing more current, further collapsing the voltage. Therefore on default the module does not derate – it will simply shut down when maximum temperature is exceeded. A high-level system must implement derating strategy, if such feature is needed by the application.

## Control modes

The DAB can operate in different control modes explained in this section.

To start operating the device, please refer to the [Quick Start](power-modules/ADM-PC-BI25/quick_start.md) section. However, it can be summarized in:
1. Power up and clear interlock
2. Select setpoints (if applicable), depending on the control mode)
3. Select control mode and enable

Setpoints are configured as follows:

- Phase shift setpoint in **DAB_Phase_Control** message
- Voltage setpoint in  **DAB_Voltage_Setpoint_Control** message
- Current setpoint in **DAB_Current_Setpoint_Control** message

### Phase shift mode
In this mode, the user selects the amount of phase shift between primary and secondary bridge. This is for testing purposes only and **should never be used by customers**.

>[!WARNING] Do not use this mode unless it is required by Advantics for test purposes

### Voltage follower mode 
In this mode, port A is considered "input" port and port B is considered "output" port. Voltage source must be connected to port A, and when the DAB is enabled, port B will be controlled to have a voltage similar to port A (for a 1:1 transformer ratio), leading to increased efficiency. 

This control mode does not need any user setpoint, since voltage will simply try to follow the input voltage, and current will be defined by downstream converters and loads.

This control mode is usually used with a 1000V DC bus voltage followed by a ADM-PC-BP25 (AFE) working as DC/DC step-down converter to adapt the high voltage to the required levels by the load.

For more information on possible applications, please refer to the [Application Examples](power-modules/ADM-PC-BI25/application_examples.md) section.

### PFC Voltage
In this mode, the DAB is preceded (connected to port A) by a ADM-PC-BP25 (AFE) working as AC/DC power factor correction unit. At the output, the battery is directly connected. 

User must select the DAB voltage and current setpoints:
- When charging the battery, voltage setpoint must be above battery voltage and current setpoint must be possitive.
- When discharging the battery, voltage setpoint must be below battery voltage and current setpoint must be negative.

The DAB and the AFE must have the same stack address number, as the DAB will autonomously send voltage setpoints to the upstream AFE to operate in the highest efficiency point when charging the battery.

>[!WARNING] Because in this mode the DAB interfaces directly with the load (the battery), the operating range in this mode is highly limited and depends mostly on the AFE and DAB variant. Therefore, this mode is only recommended to be used with the VA01 variant of the AFE (1000 V), and with the 2:1 variant of the DAB. This will lead to an output voltage range of about 300 to 500V.

For more information on possible applications, please refer to the [Application Examples](power-modules/ADM-PC-BI25/application_examples.md) section.


