> [!UPDATE] {docsify-updated}

# Quick Start

This chapter only deals with high-level control. Please consult the ADM-PC-BI25 CAN database section for the CAN bus addresses and format. The CAN database is distributed in both KCD and DBC formats.

[etka.md](../common/etka.md ':include')

## Quick start procedure

### Step 1 – Clear interlock

Modules have two types of interlock signals: **internal** which is latched in a locked state until cleared, and **external** formed from combined internal interlock signals from all other modules on the bus. Internal signal is locked when the module goes outside of its operating range (e.g., over-current, over-voltage etc.). If any of the internal and external interlock signals is locked, the module will immediately stop and will not be able to operate.
When the module is power-cycled its internal signal is locked by default for safety reasons. This will also block all other modules on the bus as their external signal will be locked. Interlock state must be cleared for all modules that have their internal signal locked by sending the **Clear_Interlock** in **AFE_Fault_Control** message **exactly once**.
Some older modules cannot separate internal and external interlock signals. When any of these two is locked, they will report both of them locked. This **does not affect** the interlock clear logic.

>[!TIP] If you use ETKA, simply press the "Rearm Interlock" button to clear the interlock of specific module.

### Step 2 – Configure control mode

Configure control mode in **DAB_Mode_Control** message. Refer to the Control modes section for mode details on how each control mode works.
The module does not check if more than one control mode has been selected. It will start the first selected control mode from the following list:
- PHASE
- VOLTAGE_FOLLOWER

>[!TIP] If you use ETKA, simply select the control mode from the "Feedback mode" combo box.

### Step 3 – Start converter

Once the control mode has been configured, the converter can be started by setting **Converter_ON** in **DAB_Mode_Control**. The selected control mode must also be kept active in this message. Alternately, you can combine Step 3 and Step 4 in a single step by sending only one message with **Converter_ON** and selected control mode.

>[!TIP] If you use ETKA, simply set "State" to "ON" in the combo box, and then click the button "Apply" to send the commands to the module.

### Step 4 – Stop converter

The converter is stopped by one of the following two events:
- **Converter_ON** in **DAB_Mode_Control** is cleared
- Internal or external interlock signal is locked. In case of locked interlock signal, the fault must be cleared by setting **Clear_Interlock** in **DAB_Fault_Control** in order to able to continue operation.

>[!TIP] If you use ETKA, simply set "State" to "OFF" in the combo box, and then click the button "Apply" to send the command to the module.