> [!UPDATE] {docsify-updated}
# Control

This chapter only deals with high-level control. Please consult the ADM-PC-LL25 Communication Manual for the CAN bus addresses and format. The CAN database is distributed in both KCD and DBC formats.

## ETKA

Engineering Toolkit for Advantics (ETKA), available for both Windows and Linux, consists of a series of applications and tools to work with ADVANTICS modules. ETKA is a GUI which together with a PeakCAN USB adapter allows customers to rapidly test and verify modules without writing any code.


![etka](images/etka.png ':size=80%')
<figcaption style="text-align: center">Figure 13: ETKA GUI application</figcaption>

## Wiring connections

The ADM-PC-LL25 is designed to work in conjunction with a ADM-PC-BP25 or ADM-PC-UP25 as upstream 3-phase power factor correction units. At the moment, the ADM-PC-LL25 cannot be used as standalone converter or with other converters than the cited above.

The output terminals of the ADM-PC-BP25 or ADM-PC-UP25 must be connected to the input terminals of the ADM-PC-LL25, and the output terminals of the ADM-PC-LL25 can be connected directly to the battery or through a diode.

## Operating range

The ADM-PC-LL25 is able to provide up to 65 Amps of output current and reach an output voltage of 450V. 
The input voltage can range between 650 and 750V, given by the BP25 or UP25 rectified output capability.
The output voltage must be higher than 200V to prevent too high output currents that would otherwise trip the hardware protections. For cases where output voltages is below 200V, a precharge stage must be done where the power module will provide short power pulses until the voltage raises above 200V. 


## Start procedure

Every module comes with a bootloader which allows firmware update over CAN. The boot process starts once the module has been powered from a 24-V power supply and it takes approximately 5 seconds. After boot the module will start sending periodic status and measurement messages, and is ready to receive control commands.

### Step 1 – Clear interlock

Modules have two types of interlock signals: **internal** which is latched in a locked state until cleared, and **external** formed from combined internal interlock signals from all other modules on the bus. Internal signal is locked when the module goes outside of its operating range (e.g., over-current, over-voltage etc.). If any of the internal and external interlock signals is locked, the module will immediately stop and will not be able to operate.
When the module is power-cycled its internal signal is locked by default for sLLCty reasons. This will also block all other modules on the bus as their external signal will be locked. Interlock state must be cleared for all modules that have their internal signal locked by sending the **Clear_Interlock** in **LLC_Fault_Control** message **exactly once**.
Some older modules cannot separate internal and external interlock signals. When any of these two is locked, they will report both of them locked. This **does not affect** the interlock clear logic.

### Step 2 – Configure setpoints

Each control mode comes with a list of setpoints required for proper operation. This is explained in more details in the **Control modes** section. Here we give a list of messages for setpoint control:
    - LLC_PWM_frequency_Control,
    - LLC_Current_Setpoint_Control
    - LLC_Voltage_Setpoint_Control
Setpoints should be sent only when they need to be updated, i.e., they do not need to be sent periodically.

### Step 3 – Configure control mode

Configure control mode in **LLC_Mode_Control** message. Refer to the Control modes section for mode details on how each control mode works.
The module does not check if more than one control mode has been selected. It will start the first selected control mode from the following list:
    - PWM,
    - CURRENT
    - VOLTAGE (not supported)
    - PRECHARGE
    - PFC_CURRENT
    - PFC_VOLTAGE

### Step 4 – Start converter

Once setpoints and control mode have been configured, the converter can be started by setting **Converter_ON** in **LLC_Mode_Control**. The selected control mode must also be kept active in this message. Alternately, you can combine Step 3 and Step 4 in a single step by sending only one message with **Converter_ON** and selected control mode.
Once started, the converter will perform basic checks which depends on the selected control mode. For example, in the RECTIFIER_3PH control mode it will synchronize to the mains and check mains frequency to be 50 Hz or 60 Hz. Each voltage and current setpoint has associated rate limiter to provide smooth transitions, which is activated once the converter has been started.

### Step 5 – Stop converter

The converter is stopped by one of the following two events: (1) **Converter_ON** in **LLC_Mode_Control** is cleared, or (2) internal or external interlock signal is locked. In case of locked interlock signal, the fault must be cleared by setting **Clear_Interlock** in **LLC_Fault_Control** in order to able to continue operation.

## High voltage discharge

The converter has an internal active voltage discharge (also called bleeding circuit) able to rapidly discharge the output capacitors when the converter is not being used.
The bleeding circuit is activated with any of the two conditions:
    - A trip condition occurs
    - A user 'bleed' request with the **LLC_fault_control** message

> [!WARNING]
> When the bleeder circuit is activated, it heats up and subsequent bleeding cycles will not perform properly if sufficient time has not passed to cooldown the circuit.


## Periodic messages

The converter periodically sends status and measurement messages, with periodicity specified in the CAN database in milliseconds as **interval** parameter. Some of the messages are multiplexed, where **multiplex count** must also be used to decode the message.
All messages that start with an **underscore** are system-level messages and should be disregarded. Here is a list of system-level messages:

    - _LLC_Voltages_Currents_Raw
    - _LLC_Ground_Fault_Raw
    - _LLC_External_Raw
    - _LLC_Calibration_Offset_Update
    - _LLC_Calibration_Scale_Update
    - _LLC_Calibration_Adc_Scale
    - _LLC_Calibration_Adc_Fs

### LLC_Identification [1000 ms]
Contains identification information for the device such as (1) device type, (2) stack position, (3) unique serial number, (4) hardware revision, and (5) hardware variant.

### LLC_FwInfo [1000 ms] – muxed
Module firmware revision and date-code information.

### Boot_FW_info_mux [1000 ms] – muxed
Bootloader firmware revision and date-code information.

### LLC_Debug [1000 ms]
Obsolete.
### LLC_Status [100 ms]
Indicates if converter is running and which control mode is currently active. Some of the bit fields are obsolete. Here is the list of **obsolete bit fields**:

    - Master
    - Slave


### LLC_Debug [1000 ms]
Not implemented
### LLC_Faults [100 ms]
Indicates module fault source.
Some modules cannot separate internal and external interlock signals. When any of the two is locked, both of them are reported as being locked. This does not affect interlock clear logic.
### LLC_Phase_Current_U_V_W [100 ms]
Rectified peak phase current measurements for all three phases.
Measurements are heavily filtered at 5 Hz cut-off frequency.
### LLC_Voltages_Currents [100 ms]
Input and output currents and voltages readout. Realtime readouts of the sensed variables. The voltage is measured at the input and output of the converter, while the current is measured at the output only.
Measurements are heavily filtered at 5 Hz cut-off frequency.
### LLC_Temperatures [100 ms]
Transistor Bridge, rectifier and transformer temperature.
### LLC_Setpoints [100 ms]
Setpoints for PWM frequency, current and voltage.
### LLC_Voltages_External [100 ms]
Output external voltage channels readout. The voltage is measured at the two external voltage sensors (EXT1,EXT2), with reference to output DC-.
### LLC_Ground_Fault [100 ms]
Ground fault measurement. It tells the insulation resistance between output terminals and ground.

## Other control messages
Some of the control messages are system-level messages or obsolete. Here is a list of messages:

    - LLC_Stack_Control
    - _LLC_ADC_Calibration_mode
    - _LLC_ADC_Calibration_setpoint
    - _LLC_Calibration_offset_update
    - _LCC_Calibration_scale_update
    
### LLC_Voltage_Limits
Used to set custom voltage limits for three phases and DC link. This is software protection and is usually much slower than the hardware protection which is always active.
### LLC_Current_Limits
Used to set custom current limits for three phases. This is software protection and is usually much slower than the hardware protection which is always active.

## Control modes

LLC can operate in a few control modes. Setpoints are configured as follows:

    - PWM frequency setpoint in LLC_frequency_control message
    - Voltage setpoint in  LLC_Voltage_Setpoint_Control message
    - Current setpoint in LLC_Current_Setpoint_Control message

### PWM
Directly sets the frequency of the PWM for all phases. This is for testing purposes only and should never be used by customers!

### Current
The LLC will act as a current source.

### Precharge
The LLC will apply short power pulses until the output voltage reaches the setpoint.

### PFC Current
The LLC will act as a current source sourcing the current specified in the setpoint. In this mode, the LLC will send voltage commands to the upstream PFC (either ADM-PC-BP25 or ADM-PC-UP25) in order to provide the optimum input voltage. Both modules must have the same slave address.

### PFC Voltage
The LLC will act as a current source with the given current setpoint until the voltage reaches the voltage setpoint, where it will act as a voltage source. In this mode, the LLC will send voltage commands to the upstream PFC (either ADM-PC-BP25 or ADM-PC-UP25) in order to provide the optimum input voltage. Both modules must have the same slave address.
> [!TIP]
> If output voltage is lower than 200V, the module will first go thorough a **precharge stage**, where short power pulses are applied until the voltage reaches a safe level.





