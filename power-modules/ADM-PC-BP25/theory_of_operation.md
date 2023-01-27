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

There are two temperature sensors installed in the module. The inductor temperature sensor, and the bridge temperature sensor (also call as transistor bar sensor). Both sensors report the current temperature over the CAN bus (in degrees Celsius). The shutdown temperature of the transistor bar sensor is **90 °C**. The shutdown temperature of the inductor temperature sensor is **130 °C**.

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


## Parallel operation in DC/DC and AC/DC for voltage regulation

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



