> [!UPDATE] {docsify-updated}

# Quick Start

This chapter only deals with high-level control. Please consult the  [ADM-PC-LF45 CAN database](power-modules/ADM-PC-LF45/can_database.md) section for the CAN bus addresses and format. The CAN database is distributed in both KCD and DBC formats.

[etka.md](../common/etka.md ':include')

## Quick start procedure

### Step 1 – Clear interlock

Modules have two types of interlock signals: **internal** which is latched in a locked state until cleared, and **external** formed from combined internal interlock signals from all other modules on the bus. Internal signal is locked when the module goes outside of its operating range (e.g., over-current, over-voltage etc.). If any of the internal and external interlock signals is locked, the module will immediately stop and will not be able to operate.
When the module is power-cycled its internal signal is locked by default for safety reasons. This will also block all other modules on the bus as their external signal will be locked. Interlock state must be cleared for all modules that have their internal signal locked by sending the **Clear_Interlock** in **Fault_Control** message **exactly once**.
Some older modules cannot separate internal and external interlock signals. When any of these two is locked, they will report both of them locked. This **does not affect** the interlock clear logic.

### Step 2 – Connect

To connect the filter, simply send the **Filter_Relays** message with the **Close_Relays** bit set, and the **Open_Relays** bit unset.

>[!NOTE]**Messages should be sent only when they need to be updated**, i.e., they do not need to be sent periodically.

### Step 3 – Disconnect

The filter is disconnected by one of the following two events:
- **Open_Relays** bit inside **Filter_Relays** message is set.
- Internal or external interlock signal is locked. In case of locked interlock signal, the fault must be cleared by setting **Clear_Interlock** in **Filter_Fault_Control** in order to able to continue operation.