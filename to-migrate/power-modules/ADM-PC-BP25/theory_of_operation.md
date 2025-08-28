> [!UPDATE] {docsify-updated}
# Theory of operation

## Topology

The ADM-PC-BP25 is a 3-phase Silicon Carbide bridge, with individual phase chokes. Up to 1000 V DC bus operation is possible (depending on the product variant).


![AFE topology](images/afe_topology.svg ':size=60%')
<figcaption style="text-align: center">ADM-PC-BP25 converter topology</figcaption>

The topology is inherently bidirectional. A DSP (Digital Signal Processor) is used to control the individual transistor pairs directly – allowing for very versatile control modes and strategies. To understand how can the converter be used as a DC/DC, imagine all three phases (L1, L2, L3) being connected in parallel using an external wiring. In case of a DC/DC, all phases will then produce (almost) constant duty cycle, resulting in a controlled boost/buck topology. Each phase is then offset by 120 degrees, for the lowest current and voltage ripple.

## Efficiency

The ADM-PC-BP25 is able to reach an efficiency of 99% across a wide operating range, as shown in the following picture.

![AFE topology](images/afe_efficiency.svg ':size=60%')
<figcaption style="text-align: center">ADM-PC-BP25 efficiency</figcaption>

## Protection mechanisms

#### Overcurrent (L1,L2,L3) protection

The overcurrent protection has three levels. HW, FW and SW. The HW protection is set to +-85 Amps per phase. It is instantaneous, using window comparators and logic, and is fully independent of the digital signal processor firmware. The FW protection is set to +-80 Amps and is verified on low-pass filtered signal with BW of approximately 5 Hz. SW protection works on the same level as FW protection, but is user-adjustable over CAN bus.

#### Overvoltage protection

Similarly there is a three level overvoltage protection on the DC bus. The limit is set to 860 V (VA08 variant) and 1060 V (VA01 variant), is instantaneous, using comparators and logic, and is fully independent of the digital signal processor firmware. A voltage exceeding this level will cause a converter shutdown. Customer should be aware that the module has no means of protecting itself if excessive voltage is presented on its input. Excessive voltage will destroy the switching devices. The L1, L2, L3 voltages only provides SW protection for user’s convenience, as the phase voltages are always lower or equal to the DC bus voltage.

#### Passive high voltage discharge

The module has a slow internal bleeding circuit for capacitor discharge. The purpose of this bleeder is to remove any residual voltage on the terminals when the converter is not operating. This bleeder is not a safety feature meant to protect users from dangerous voltages. It can take more than 4 minutes for the internal bleeder to drop capacitor voltage to a safe level. If safety bleeding is required, it must be implemented externally (for example by using low ohmic power resistor and a DC contactor).

#### Keep Alive feature

Starting from firmware version 2022.2.17, the user can optionally send a 'Keep Alive' message with a periodicity of 1000 ms or less, so that if communication is lost, the module will disable itself after that time.

This feature is disabled by default upon boot-up. To enable it, the user just has to send the **AFE_Keep_Alive** message (ID 0x70060) with bit 0 set to 1. Then, the module will expect to receive this same message constantly with a periodicity of 1000 ms or less. If not received, the module will disable operation. If the module is already disabled and the message does not arrive, nothing happens.

To disable the feature, send the **AFE_Keep_Alive** message with bit 0 cleared to 0. Then, the module will no longer expect to receive the message, and will not disable operation if the message is not received.

For specific information about the message, please check the [CAN database](power-modules/ADM-PC-BP25/can_database.md) section.

## Limits

When talking about similar topologies, there are four main limiting aspects – the voltage, current, power and temperature. Since the converter can be used in many different ways, the way how limits are considered also changes. To make understanding these limits easier, always think of limits per phase (even if they are connected in parallel).

#### Voltage limit

The voltage limit is the simplest to consider. The switching devices have blocking voltage defined (1000 V for VA08 variant, and 1200 V for VA01 variant). The maximum allowed voltage is then derated by 200V for each variant - that is to 800 V and 1000 V respectively. The module will not allow the user to exceed these limits. The absolute value of the voltage will have an impact on the maximum power available – as switching losses increase slightly with the bus voltage. But in general, having higher voltage on both sides of the converter results in higher power available, and higher efficiency.

> [!WARNING]
> The module is equiped with HW protections that will shut down the converter if the limits are exceeded. 
> But the module cannot protect itself against voltages applied on its terminals. Make sure that the applied voltage is within the operational limits


#### Current limit

Always consider current limit in the sense of phase currents. When the module is used as a DC/DC, the total current limit is 100 A for VA01 variant – resulting in maximum phase current of 33 A. When the module is used as a 3-phase power factor correction unit, the phase current is actually an AC current - expressed in Amps RMS. Therefore the phase limit will appear lower (30 A per phase for VA01 variant), as the module has to proccess much higher peak currents (42.5 A).

#### Power limit

The maximum power at given low side (phase) voltage and low side (phase) current is calculated as max phase current times phase voltage. For very high values of the phase voltage the total transistor dissipation becomes the limiting factor. The maximum power is set to 50 kW. The power envelope is actually much more complicated, as it depends on bus voltage to phase voltage ratio, output current and the duty cycle, as well as on current shape (AC vs DC). Consult the details with ADVANTICS, if you’re not sure your application fits within the power capabilities.

![power envelope va01](images/power_envelope_va01.svg ':size=60%')
<figcaption style="text-align: center">Power envelope of the variant VA01</figcaption>

![power envelope va08](images/power_envelope_va08.svg ':size=60%')
<figcaption style="text-align: center">Power envelope of the variant VA08</figcaption>

#### Thermal limit

There are two temperature sensors installed in the module. The inductor temperature sensor, and the bridge temperature sensor (also call as transistor bar sensor). Both sensors report the current temperature over the CAN bus (in degrees Celsius). The bridge temperature in the module should be maintained at maximum of 70 degrees Celsius for normal operation for long periods. However, it can reach a maximum of 90 degrees Celsius.It is important to note that continuous operation at this maximum temperature can result in damaging the device and reducing the lifetime of the unit. The shutdown temperature of the transistor bar sensor is **90 °C**. The shutdown temperature of the inductor temperature sensor is **130 °C**.

Upon reaching the overheating condition, the converter will stop operating (still reachable via CAN communication) but without tripping the interlock line. This means that other modules chained in the same bus will still continue normal operation.

> [!WARNING]
> Care must be taken to not operate the module near the temperature limits, as it will reduce the lifetime of the unit.

> [!NOTE]
> It is not always practical to implement derating on the module level. In applications where the module is just one of the power stages, derating has no meaning - if the power delivery dropped, the voltage would collapse and downstream power converters would simply attempt to extract power by drawing more current, further collapsing the voltage. Therefore on default the module does not derate – it will simply shut down when maximum temperature is exceeded. A high-level system must implement derating strategy, if such feature is needed by the application.

## Control modes

AFE can operate in many different control modes, which includes both AC and DC applications (buck, boost, rectification, inverting, etc.). Some applications require a proper precharge to be done before connecting sources to the module. This is true whenever voltage source connected to three phases is of higher voltage than the DC link, which is in all applications that include boost and rectifier control modes. Otherwise, a permanent damage to the device might occur which will not be visible at first but it will definitely cause MOSFET failure.

>[!WARNING] Verify if your application requires precharge before appliying any voltage on the module or permanent damage might occur to the module

To start operating the device, please refer to the [Quick Start](power-modules/ADM-PC-BP25/quick_start.md) section. However, it can be summarized in:
1. Power up and clear interlock
2. Select setpoints
3. Select control mode and enable

Setpoints are configured as follows:

- Duty cycle setpoint in **AFE_PWM_Duty_Control** message
- Voltage setpoint in  **AFE_Voltage_Setpoint_Control** message, and Voltage setpoint (2) in **AFE_Rectifier_Setpoint_Control** message
- Current setpoint in **AFE_Current_Setpoint_Control** message, and Current setpoint (2) in **AFE_Rectifier_Setpoint_Control** message
- Frequency setpoint in **AFE_Frequency_Setpoint_Control** message. It cannot be changed once the converter has been started
- Phase setpoint in **AFE_Phase_Setpoint_Control** message. It cannot be changed once the converter has been started

### PWM mode
In this mode, the user selected pwm duty cycles are directly applied in each phase. This is for testing purposes only and should never be used by customers.

>[!WARNING] Do not use this mode unless it is required by Advantics for test purposes

### Neutral mode 
For a given DC link voltage, the AFE will generate an open-loop voltage on L1,L2 and L3 that is 50% of the input. In this mode the three phases must be shorted and the voltage source connected to the DC link. Input side is defined to be the DC link, and output side to be the three phases. 

This control mode is usually used together with other modules operating in the Inverter 3-phase, or in Inverter 1-phase Sync. modes, in order to generate the neutral point.
When the frequency setpoint is configured, this module will generate synchronization pulses used by the other modules in Inverter 1-phase Sync. mode in order to synchronize themselves with respect to the pulse. This process provides great flexibility to generate any type of AC voltage of any frequency, amplitude (within DC link voltage) and phase.

>[!NOTE] The frequency setpoint must be set BEFORE the Neutral mode is enabled.

For more information about possible applications, please refer to the [Application Examples](power-modules/ADM-PC-BP25/application_examples.md) section.

![power envelope va01](images/AFE_neutral-AFE_neutral.svg ':size=50%')
<figcaption style="text-align: center">Simple connection of ADM-PC-BP25 in Neutral mode</figcaption>

### Buck mode
The AFE will act as a Constant Current/Constant Voltage source. For a given DC link voltage, the AFE will generate a closed-loop voltage on L1,L2 and L3 defined by the Voltage Setpoint or will clamp to the current limit set by the user current setpoint. In this mode the three phases must be shorted and the voltage source connected to the DC link. Input side is defined to be the DC link, and output side to be the three phases. Positive current direction is from the input to the output (from DC link to the three phases).

Voltage setpoint corresponds to the output voltage reference. Current setpoint corresponds to the total output current, where total means the three phases combined.

![power envelope va01](images/AFE_buck-AFE_buck.svg ':size=50%')
<figcaption style="text-align: center">Simple connection of ADM-PC-BP25 in Buck mode</figcaption>

### Boost mode
The AFE will act as a Constant Current/Constant Voltage source. For a given 'low voltage side' voltage, the AFE will generate a closed-loop voltage on the DC link defined by the Voltage Setpoint or will clamp to the current limit set by the user current setpoint. In this mode the three phases must be shorted and the voltage source connected to the three phases. Input side is defined to be the three phases, and output side to be the DC link. Positive current direction is from the input to the output (from three phases to DC link).

Voltage setpoint corresponds to the output voltage reference. Current setpoint corresponds to the total input current, where total means the three phases combined.

>[!WARNING]This application requires precharge to be implemented!

![power envelope va08](images/AFE_boost-AFE_boost.svg ':size=70%')
<figcaption style="text-align: center">Simple connection of ADM-PC-BP25 in Boost mode with precharge</figcaption>

### Boost & Neutral mode
As the name indicates, this mode provides two 'outputs': a boosted DC voltage in the DC link, and a neutral voltage in L3. 

The voltage source is connected to shorted L1-L2 phases. Input side is defined to be the two phases L1-L2, and output side to be the DC link. Positive current direction is from the input to the output.

Neutral is generated in open-loop on phase L3 as 50% of the DC link voltage. This control mode is usually used with another module operating in Inverter 3-phase control mode in order to generate a symmetrical three-phase voltage with neutral from low-voltage DC source.

Voltage setpoint corresponds to the output voltage reference. Current setpoint corresponds to the total input current, where total means the two phases combined.

>[!WARNING]This application requires precharge to be implemented!

![power envelope va08](images/AFE_boost_neutral-AFE_boost_neutral.svg ':size=70%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in boost & neutral mode with precharge</figcaption>

### Rectifier 1-phase mode
In this mode, the module can be attached to an existing 1-phase grid to sink or source power from/to it and acting as an active power factor correction unit (PFC) with boost. The module reaches a power factor of 0.96-0.99 depending on the loading.
Supported grid standards are:
- EU grid (50Hz) both line-to-line or line-to-neutral
- US 480V<sub>AC</sub> and 208V<sub>AC</sub> (60Hz)

AC voltage source is connected between phases L2 and L3, either line-to-neutral or line-to-line. Phase L1 is unused in this control mode. Input side is defined to be the two phases L2-L3, and output side to be the DC link. 

Voltage setpoint corresponds to the output voltage reference, and it must be bigger than the peak to peak amplitude of the AC voltage. Current setpoint corresponds to the total input RMS current limit and must be greater than zero, where total means single phase.

>[!WARNING]This application requires precharge to be implemented!

![power envelope va08](images/AFE_rectifier_1ph-AFE_rectifier_1ph.svg ':size=70%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in rectifier 1-phase mode with precharge</figcaption>

### Rectifier 1-phase & Buck mode
This mode is identical to Rectifier 1-phase mode, but it also generates a DC step-down voltage in phase L1. This voltage will always be smaller or equal than the DC link voltage.

AC voltage source is connected between phases L2 and L3, either line-to-neutral or line-to-line.  Input side is defined to be the two phases L2-L3, and output side to be the DC link. 

Voltage setpoint corresponds to the output voltage reference (DC link voltage), and it must be bigger than the peak to peak amplitude of the AC voltage. Current setpoint corresponds to the total input RMS current limit and must be greater than zero, where total means single phase.
Voltage setpoint (2) corresponds to the phase L1 voltage reference. Current setpoint (2) corresponds to the phase L1 current limit, where positive current direction is from the DC link to the phase L1.

>[!WARNING]This application requires precharge to be implemented!

![power envelope va08](images/AFE_rectifier_1ph_buck-AFE_rectifier_1ph_buck.svg ':size=70%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in rectifier 1-phase & Buck mode with precharge</figcaption>

### Rectifier 3-phase mode
In this mode, the module can be attached to an existing 3-phase grid to sink or source power from/to it and acting as an active power factor correction unit (PFC) with boost. The module reaches a power factor of 0.96-0.99 depending on the loading.

Symmetrical three-phase AC voltage source is connected to the three phases. 

Voltage setpoint corresponds to the output voltage reference. Current setpoint corresponds to the total input RMS current limit and must be greater than zero, where total means the three phases combined.

>[!WARNING]This application requires precharge to be implemented!

![power envelope va08](images/AFE_rectifier_3ph-AFE_rectifier_3ph.svg ':size=70%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in Rectifier 3-phase mode with precharge</figcaption>

### Inverter 1-phase mode
In this mode, the module is able to generate an open-loop AC voltage source of the desired frequency, and amplitude within the DC-link limit. 

Voltage source is connected to the DC link. It generates a sine-wave voltage in open-loop on phases L1 and L3 with 180° phase shift, and 50% of the DC link voltage on phase L2 (neutral). Therefore, L1 to L3 voltage will be double of L1 to L2 voltage.

Voltage setpoint corresponds to the phase RMS voltage reference. Current setpoint corresponds to the phase RMS current limit and must be greater than zero. Frequency setpoint corresponds to the sine-wave frequency.

>[!NOTE] The frequency setpoint must be set BEFORE the Inverter 1-phase mode is enabled.

![power envelope va08](images/AFE_inverter_1-ph-AFE_inverter_1ph.svg ':size=60%')
<figcaption style="text-align: center">Simple connection of ADM-PC-BP25 in boost mode with precharge</figcaption>

### Inverter 1-phase & Boost mode
In this mode, the module generates an AC voltage and at the same time, a boosted DC voltage in the DC-link.

Voltage source is connected to the phase L1 and DC-. An AC sine-wave voltage is generated in open-loop on phases L2 and L3 with 180° phase shift.

Voltage setpoint corresponds to the output RMS voltage reference. Current setpoint corresponds to the phase RMS current limit and must be greater than zero. Frequency setpoint corresponds to the sine-wave frequency.
Voltage setpoint (2) corresponds to the DC link voltage reference. Current setpoint (2) corresponds to the phase L1 current limit, where positive current direction is from the phase L1 to the DC link.

![power envelope va08](images/AFE_inverter_1-ph_boost-AFE_inverter_1-ph_boost.svg ':size=70%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in inverter 1-phase mode.</figcaption>

### Inverter 1-phase Sync. mode
In this mode, the module generates a 'floating' AC voltage sine-wave in open loop on the three phases. This control mode is usually used with another module operating in the Neutral control mode which generates a synchronization signal for the specified sine-wave frequency. For more information about possible applications, please refer to the [Application Examples](power-modules/ADM-PC-BP25/application_examples.md) section.

Voltage source is connected to the DC link. The three phases must be shorted. Input side is defined to be the DC link, and output side to be the three phases.

Voltage setpoint corresponds to the output RMS voltage reference. Current setpoint corresponds to the total output RMS current limit and must be greater than zero, where total means all three phases combined. Frequency setpoint corresponds to the sine-wave frequency. Phase setpoint corresponds to the phase shift with respect to the synchronization signal.

>[!NOTE] The frequency and phase setpoints must be set BEFORE the Inverter 1-phase Sync. mode is enabled.


![power envelope va08](images/AFE_inverter_1-ph_sync-AFE_inverter_1-ph_sync.svg ':size=50%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in Inverter 1-phase Sync.mode</figcaption>

### Inverter 3-phase mode
In this mode, the module generates a 3-phase sine-wave voltage in open loop with a 120 degrees phase shift between phases. It is usually used with another module operating in the Boost & Neutral control mode which provides neutral line.

Voltage source is connected to the DC link. Input side is defined to be the DC link, and output side to be the three phases. 

Voltage setpoint corresponds to the output RMS voltage reference. Current setpoint corresponds to the output (per-phase) RMS current limit and must be greater than zero. Frequency setpoint corresponds to the sine-wave frequency.

>[!NOTE] The frequency setpoint must be set BEFORE the Inverter 3-phase mode is enabled.

![power envelope va08](images/AFE_inverter_3ph-AFE_inverter_3ph.svg ':size=50%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in inverter 3-phase mode </figcaption>



### Inverter 1-phase distributed mode
In this mode, the module generates a 'floating' AC voltage sine-wave in open loop on both L1 and L2 (they must be shorted toguether). L3 generates the Neutral. This control mode is usually used with others module that will generate other phases at a user defined phase shift. The master module (in stack position zero) will generate the synchronization signal for the specified sine-wave frequency.

Voltage source is connected to the DC link. Input side is defined to be the DC link

Voltage setpoint corresponds to the output RMS voltage reference. Current setpoint corresponds to the total output RMS current limit and must be greater than zero. Frequency setpoint corresponds to the sine-wave frequency. Phase setpoint corresponds to the phase shift with respect to the synchronization signal. For example, if we have 2 BP25 modules in this mode, we could send a setpoint of 180 degrees to the module with stack position 1, meaning it will generate a phase with oposite polarity to that one generated by the BP25 with stack position 0.

>[!NOTE] The frequency and phase setpoints must be set BEFORE the mode is enabled.

![power envelope va08](images/AFE_inverter_1-ph_distributed.svg ':size=50%')
<figcaption style="text-align: center">Example connection of ADM-PC-BP25 in 1-phase distributed mode </figcaption>


## Setpoint selection
For the module to work as it should, the current and voltage setpoints need to be selected properly depending on the application.

The ADM-PC-BP25 can work in two regimes: **current regulation or voltage regulation**. The switchover from one regime to another is done automatically by the internal logic of the module.

When the output voltage of the module is defined by a battery or any other power module, the module should only work in current regulation regime, meaning that current will reach the desired setpoint, whereas the voltage setpoint will not be reached (because it is defined by an external source).

When the voltage at the output of the module is not defined by a battery or any other power module connected to it, then the module will most likely work in voltage regulation and the voltage setpoint will be reached, unless the current setpoint is reached before.

**The general convention that the user must follow is:**

1. For modules working in **current regulation** (when output voltage is externally defined by a battery or another power module in voltage regulation):

- Choose a positive current setpoint when pushing current towards the output, and a voltage setpoint above the output voltage. For example, if the module output is connected to a 400 V battery, and we want to push 50 A into it, we should use a voltage setpoint of 500 V (any value above 400 by a margin is valid), and a current setpoint of +50 A.

- Choose a negative current setpoint when pulling current from the output, and a voltage setpoint below the output voltage. For example, if the module output is connected to a 400 V battery, and we want to pull 30 A from it, we should use a voltage setpoint of 350 V (any value below 400 by a margin is valid), and a current setpoint of -30 A.

2. For modules working in **voltage regulation** (when the output voltage is not externally defined and current setpoint is not reached before):

- Choose a positive current setpoint which is enough to supply the load by a margin, and whatever desired voltage. Note that even if the current setpoint is possitive, in this case, the module can still sink or source current while maintaining the bus voltage.

>[!NOTE] In DC/DC modes, the current setpoint is referred always to the total phase current, so make sure that the estimated current draw (and the selected current setpoint) is converted to low-voltage side (phase side) current draw by multiplying by the voltage ratio. For example, if we are boosting from 400V to 800V, and the expected current draw in the high-voltage bus is 40A, then, the setpoint has to be actually 80A + margin in the low voltage side.


## Parallel operation in DC/DC modes and AC/DC rectifier mode for voltage regulation

When in a application we need to increase the power, we may need to parallel several modules. 

If the modules to be paralleled are expected to work in **current regulation**, then these modules can be paralleled without further action than just wiring them in parallel. Please, refer to the [Setpoint selection](#Setpoint-selection) section to better understand if/when the modules work in current regulation. For example, if we want to charge a battery with 150 Amps, we need two ADM-PC-BP25 modules in parallel. Assuming that the battery voltage is below the input voltage of the modules, then they would work in Buck mode and since the output voltage is defined by the battery, they must work in current regulation. Therefore, they can be paralleled without further action, and choose the voltage and current setpoints accordingly as explained in previous section.

If the modules to be paralleled are expected to work in **voltage regulation**, then a special procedure must be followed, and the user must read this section and follow the given guidelines. 

#### When can the module be paralleled?
The ADM-PC-BP25 can work in parallel operation for voltage regulation in the following modes:
- Buck (firmware 2021.9.24 or newer)
- Boost (firmware 2021.9.24 or newer)
- Rectifier 3-Phase (firmware 2022.3.9 or newer)

#### Group ID
First of all, let's introduce the concept of **"Group ID"**. The Group ID is an identifier which will be shared by all the modules that will be paralleled. For example, in the case of having 3 modules in parallel to work in Boost operation and keep a constant bus voltage, all of them would share the same Group ID (i.e. Group ID 1). If in the same CAN bus we have 2 more modules that work in parallel in Buck mode to generate a different bus voltage, they would also share a Group ID but different from the previous (i.e. Group ID 2)

Some considerations about the Group ID:
-  The user can modify the Group ID of any device with the **AFE_Group_Control** message,
-  The user can retrieve the current Group ID of a device with the **AFE_Group_Info** message.
- The Group ID can range from 0 to 7. A Group ID of '0' means that the device does NOT share any group with other devices (default configuration)
- The Group ID of a device is **not persistent**, and is set to '0' by default upon reboot/power-up.
- The only limit on the maximum number of modules that belong to a group is impossed by the maximum stack number, 32.

Please, refer to the [CAN database](power-modules/ADM-PC-BP25/can_database.md) for more information about the messages to set/retrieve the group ID.

When one or more ADM-PC-BP25 that belong to a group (different from '0') are enabled and in buck, boost or rectifier 3-Ph operation, they will start publishing system-level messages in the CAN bus called '_AFE_Broadcast' with a periodicity of 50 ms. The message should be disregarded by the user, and are used only by other ADM-PC-BP25 to coordinate their effort.

#### Procedure for parallel operation
For an example case of 2 modules (A and B), the process to enable parallel operation in a boost/buck mode is the following:

1. Power-up modules and make sure that the firmware in all the modules is newer or equal to the 2021.9.24 release.

2. Clear interlocks.

3. Assign the same Group ID only to the desired modules that will work in parallel boost or buck operation (in this case A and B). The group ID should be different from '0' (for example, '1'). 

4. Configure the setpoints for one of the devices in the group (for example, start with module A).

5. Configure control mode to Boost or Buck.

6. Start the converter for 'A' and wait until it reaches steady state.

7. Repeat the process from point 4 to device 'B' and to as many devices as desired.

>[!WARNING]Setpoints and control mode for devices working in parallel must be the same.

>[!WARNING]Do not change the Group ID while the modules are enabled.

>[!NOTE]Even though modules are connected in parallel, one module might be more loaded than others (i.e. perfect sharing of the load is not guaranteed)


#### Examples of parallel operation

**Example 1:** 4 modules are used. Two modules (A and B) work in parallel Boost operation sharing Group ID 1 and with a battery and precharge circuit. The other two modules (C and D) work in parallel Buck sharing Group ID 2, and have their output connected to a generic load. All modules are working in voltage regulation mode and hence, the group ID is needed.

![power envelope va08](images/parallel_boost_buck-parallel_boost_buck.svg ':size=90%')
<figcaption style="text-align: center">Example connection of 2 modules working in parallel Boost operation and 2 modules in parallel Buck </figcaption>

**Example 2:** 4 modules are used. Two modules (A and B) work in parallel Boost operation sharing Group ID 1 and with a battery and precharge circuit. The other two modules (C and D) work in parallel Buck, and have their output connected to a battery. Because the output voltage is defined by the battery, the group ID is not needed, since modules will work in current regulation.

![power envelope va08](images/diagrams-parallel_boost_buck_v2.svg ':size=90%')
<figcaption style="text-align: center">Example connection of 2 modules working in parallel Boost operation (voltage regulation) and 2 modules in parallel Buck (current regulation, group ID not needed)</figcaption>

## Overload handling in AC inverter modes

Starting from firmware version 2023.1.18, the overload (high current) condition is improved and made more flexible with the introduction of a virtual impedance.

>[!WARNING] These overload conditions must always be short in time, and steady state current should always be equal or below the nominal current of the converter (**30/33 Amps RMS per phase** for VA01/VA08 respectively)

When the current (in RMS) is above the current reference defined by the user ('AFE_Current_Setpoint_Control' message), the AC voltage waveform amplitude will drop proportionally to the excess of current, effectively behaving as a series resistor at the output of the converter, but that only actuates above a certain threshold. 

>[!NOTE] For Inverter 3-phase mode, if one phase is more loaded than the other (unbalanced case), the voltage will drop equally in all phases based on the most loaded phase.

The V-I (voltage-current) curve of the converter then looks like the following picture:

![V-I curve](images/inverter_curve.svg ':size=50%')
<figcaption style="text-align: center">V-I curve in inverter modes showing virtual impedance slope and maximum instantaneous current.</figcaption>

The slope (virtual resistance) of the curve is equal to Vref/22. This means that for Vref = 230V, the virtual resistance is ~10.5 Ohm. Although this slope is constant, the user can adjust the threshold when it starts acting by changing the current setpoint.

On top of the virtual impedance, and to prevent interlock trips when capacitive loads, or other very high loads are connected, there is another **faster** mechanism that will use analog window comparators to do peak current control at a fixed high current value of around ~52 Amps RMS. This mechanism will however introduce high frequency distortion in the current and voltage waveform. 

The user can then play and adjust the current setpoint (the threshold at which the virtual impedance will start acting), in order to find a good balance between high current availability and low distortion of the waveform.

For example, if the user is only interested in having the highest current availability, then an unrealisticly high current reference can be used (for example, 200 Amps), so that the virtual impedance never starts acting, and only the fast window comparators will actuate. Obviously, this is only to allow starting high loads (such as motors), but the steady state current should still be equal or below the nominal current of the converter (30/33 Amps RMS depending on the variant).

On the other hand, if the user is more interested in having less high frequency distortion, the user can lower the current reference, so that the virtual impedance will start acting before, and the voltage amplitude will drop, preventing the current to grow too much without introducing high frequency distortion.

>[!TIP] We recommend to start by setting Iref = 30 Amps (90 Amps in the case of Inverter 1-phase + SYNC mode), then checking the behaviour and adjust this value as needed.


## Parallel operation in DC/AC 3-phase Inverter mode  (grid forming)

Starting from firmware 2024.9.25, a new set of features were introduced in the 3-phase inverter mode to allow paralleling of modules for grid forming.

The goal of this set of features is:
- Allow modules to share the load when connected in parallel
- Allow new modules to be connected in parallel while loads are still being suppled (hot plugging)
- Allow transfer of power between modules via power setpoints
- Allow modifying the load sharing via power setpoints
- Allow connection to the grid and exchange power with it via power setpoints
- Allow connection in parallel with other inverters

>[!TIP] Modules should also be able to be paralleled with diesel generators, but experience with this is extremely limited, also due to the big differences between diesel generator specifications (both steady state and transient performance)

To understand how to operate modules in this mode, please read through the following sections of the document.

### Basic operation of 2 or more AFEs in parallel as grid forming
With the new firmware, AFEs can be connected in parallel in AC modes, but only in 3-phase inverter mode. This means that every AFE will generate the 3 phase voltages, and the phases of other AFEs can be paralleled.

To enable a single AFE in ¨Inverter 3-phase¨ mode, set bit number 13 (starting from 0) in the ¨AFE_Mode_Control¨ message (see CAN database for more info).

To start operating, do the following:
1. Select voltage, current and frequency setpoints for all AFEs to be working as voltage sources. All of them have to have the same setpoints. (There are also power setpoints but set them as 0 at start). 
Typical values:
- Voltage setpoint: 120V/230V (RMS phase-to-neutral voltage)
- Current setpoint: 40A 
- Frequency: 50/60 Hz

2. Enable one AFE as NEUTRAL mode (or generate the Neutral from another AFE in Boost+Neutral)

3. Enable one AFE as ¨Inverter 3-phase¨ mode. Step 2 and 3 may be done in any order.

4. Once the voltage has stabilized (may take around 0.5 to 1 second from the moment that the CAN message is sent), then the other 2 AFEs can be enabled as well. At this point, they will be in parallel generating an AC waveform. 

>[!NOTE]When no load is connected, there will be some circulating current, mostly reactive. This is unavoidable, but this small reactive current does not take much of the current budget, as it adds in quadrature to active current. When loads are connected, the AFEs will tend to share the load more or less equally.

### Understanding voltage and frequency droop
In order to enable parallel operation in AC grid forming modes, a droop in voltage and frequency has been implemented. The droop equations are different depending on the impedance of the microgrid. As is usually the case for compatibility with the grid and diesel generators, we have 
assumed a mainly inductive impedance, and with this in mind, the droop equations are as follow:

ΔV = m⋅(Qset−Q)

Δω = n⋅(Pset−P)

Where Pset and Qset are the active and reactive power setpoints,respectively, P and Q are the measured active and reactive powers, and m and n are the voltage and frequency droop gains, respectively.

Let’s start with the simplest case scenario: Pset and Qset are 0 (as this will usually be the case in microgrid operation). When applying the equations above, active power affects the frequency, and reactive power affects the voltage (in reality there is always some coupling). When the active power is increased (due to the connection of a load, for example), the frequency will be reduced, and when reactive power is increased, voltage will be reduced. The amount of reduction depends on the 'm' and 'n' constants. 

Now we can complicate things a bit more: we can play with the Pset and Qset. When they are modified, the modules will try to modify their voltage/frequency to reach a new equilibrium in which they no longer share equally the load. This can be used, for example, to flow energy from one battery to another through the AC microgrid. This is better explained in next section.

### Default droop gains
Upon startup, and if the user does not modify them via CAN, the module will use the following default gains:

**Frequency droop gain:** 40 Hz/MW

**Voltage droop gain:** 630 V/MVAr

### Power sharing
There are several aspects that need to be discussed regarding power delivery and sharing.

First of all, because the modules in grid-forming behave as voltage sources, the delivered current (and therefore, power) is the subproduct of the AC voltage and the load. Therefore, there is no meaning on talking about active/reactive power control of a single AFE because they will only depend on the load.

However, when more than one AFE are connected together (or when they are connected in parallel to the grid or to other inverters), we can modify the power transfet and sharing between the modules. This is done via the Active and Reactive power setpoints. To explain how they work, let's put an example.

Let's say that we have 2 AFEs in grid-forming mode. Their power setpoints (both, active and reactive) should be zero initially. Having a zero power setpoint does NOT mean that the module will not produce power (remember, power just depends on voltage and load). In this condition, the 2 AFEs will reach an equilibrium in which they will share the load, meaning that they both contribute almost the same amount and therefore each AFE will provide roughly half of the total power consumed by the load. Power sharing will never be perfect due to real life uncertainties, impedance mismatch, etc.

In this scenario, modifying the power setpoints refers to modifying the equilibrium point. Therefore, if in this scenario we send an active power setpoint of 2 KW to one of the AFEs, that AFE will try to do 2 more KW than the other AFE, but total amount of power provided to the load will still be the same. 

Some things to point out:
- Having a setpoint of (for example) 2KW in one AFE and a setpoint of 0 KW in the other AFE will produce the same power flow as having a setpoint of 1 KW in one AFE and -1 KW in the other AFE. However, the equilibrium frequency/voltage will be slightly different.

- For the previous reason, we suggest to set the power setpoints in the AFEs such that their sum is always zero (I.e: 1 +(-1) = 0). 

- If a setpoint of +2KW is given to both AFEs, the power sharing will remain the same. But their frequency or voltage will increase according to the droop formulas described in previous section.

### CAN messages for operation
When operating in inverter 3p mode, these are the related CAN messages (for more information, refer directly to the CAN database):

- **ID =** 0x78011, **Message name:** “AFE_AC_Power”, **Description:** contains the measured active and reactive powers (per phase).

- **ID =** 0x70039, **Message name:** “AFE_Power_Setpoint_Control”, **Description:** use this message to send power setpoints to the module.

- **ID =** 0x70051, **Message name:** “AFE_Inverter_Droop_Control”, **Description:** use this message to modify advanced parameters for operation (explained in following section).

### Advanced parameters configuration
When working in Inverter 3-phase mode, there are some extra configuration parameters that the user can modify. (For more information, please check the provided CAN database)

>[!WARNING]**Important:** the modification of these parameters has serious implications on the behavior and stability of the module. If you need assistance, ask Advantics.


The list of (most important) parameters that can be changed over CAN is the following:
- **Frequency droop:** this is the droop slope/gain for the Frequency in Hz/MegaWatt. 
Important: the default value for this gain (40 Hz/MW) is already quite high, and increasing 
it degrades stability. Therefore, we do not recommend increasing it. 
- **Voltage droop:** sets the droop gain/slope for the Voltage in V/MegaWatt. We do not 
recommend increasing or decreasing this gain. Its default value is 630 V/MW.
- **Virtual impedance:** sets the inductive virtual impedance in microhenries (uH). By default 
(i.e: after power cycle), this value is 8000 uH. Important: lowering this value too much will
lead to instability in the power loop. We do not recommend increasing this value.
- **“Disable Harmonic Compensation”:** you can set this flag when harmonic compensation 
needs to be disabled (i.e, when the module is connected in parallel to the utility grid or to a 
diesel generator). Harmonic compensation is enabled by default on startup.
- **“Enable integral action”:** this integral action refers to the Power loop controllers. Enable 
this only if connected to the utility grid or any other 'stiff' AC source. If you go off-grid, this bit must be immediately 
cleared. This is disabled by default on startup. Check the ‘Integral action: operate as 
constant power/current source/sink’ section for more details on when to enable this setting

### Tradeoff between droop grains, virtual impedance, transient performance and stability
In previous section we can see that almost every parameter has serious implications on the stability of the system. In this section, we try to explain a bit more this relationship, and possible combinations of parameters depending on the application.

Let’s start with virtual impedance(inductance). This virtual inductance is needed to make the system behave inductively (remember from previous sections that an inductive behavior was assumed), and also to stabilize the dynamics. **In general, the higher the Frequency droop gain is, the higher virtual impedance is needed.** By default, both frequency and virtual impedance are relatively high, so technically, you could divide them both by a factor of 4 (for example) to maintain stability.

Let’s continue with the frequency droop: in order to improve power sharing between AFEs, the frequency droop gain needs to increase. Therefore, if you decrease the frequency droop gain, power sharing will be slightly worse, but this will allow you to have less virtual inductance, which has a benefit explained next.

A high virtual impedance will worsen the transient performance of the voltage when loads are 
connected/disconnected. To improve transient performance, you will want to lower virtual 
impedance.

Therefore, these 3 aspects are related to each other, and it is not possible to have a high droop gain, low output impedance and good stability and transient performance at the same time. One has to 
choose depending on the application. 

Here we present 2 case scenarios:

**Case scenario 1: AFEs are used only to generate a microgrid**

In this case scenario, the default gains and virtual impedance will work just fine, although transient performance might not be the best. You can decide to operate with default parameters, or you can 
decide to improve transient performance by decreasing both frequency droop and virtual impedance by a factor of 2 or 4, for example. Although power sharing will be slightly worse, but still good enough.

**Case scenario 2: AFEs are used as current sources against the utility grid**

In this case, transient performance is less important as the modules behave as current sources. Therefore the default values can be used without any problem

### Integral action: operate as constant power/current source/sink
In order to behave as a current/power source, you can enable integral action. Integral action adds infinite gain at DC in the power loop, which means that the AFE will increase/decrease its frequency or voltage until its power matches the user selected power setpoints and is perfectly tracked (within the sensors accuracy), therefore behaving as a current/power source.

>[!WARNING]**Important:**  bear in mind that to be able to enable integral action there needs to be at least one or more devices that act as ‘master’ generators, meaning that they do not have integral action or that 
their frequency/voltage is stable, otherwise the whole system would drift in frequency/voltage. For example, it is ok to enable integral action when connected to a diesel generator, or to the utility grid.
But if you only have one AFE generating 3-phase, then you should NOT enable integral action.

>[!WARNING] If the integral action is activated because the AFE is operating in parallel to the utility grid (for example), bbut suddenly the utility grid is disconnected, then the integral action must be deactivated as soon as possible to prevent frequency/voltage drift.

### Overload conditions
The overload capabilities of the AFE is inherently small because its peak current rating is very close to its nominal one. 

While the AFE is loaded above the selected current setpoint (which should be more or less equal to the nominal current), but below ~1.35 times the nominal current, the AFE will heavily lower the output voltage (as explained in section "Overload handling in AC inverter modes"). But also, when the load reaches ~1.35 times the nominal current, the AFE will start 
clipping the current and therefore heavily distorting the voltage waveform to protect itself. This is intentional.

Therefore, the load should not overcome ~1.35 times the nominal current by more than a few milliseconds. If high frequency content appears in the voltage waveform, it means that the peak current protection mechanism is being triggered. This is unavoidable to prevent damage in the AFE without completely stopping operation.