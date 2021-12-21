> [!UPDATE] {docsify-updated}
# Application examples


## Unidirectional 3-phase Electric vehicle charger
The typical use of the ADM-PC-LL25 is as electric vehicle unidirectional charger, toghether with an upstream filter ADM-PC-LF45 and a power factor correction ADM-PC-BP25 or ADM-PC-UP25.

In this example, the ADM-PC-LL25 is used in the PFC Voltage control mode. As explained in [Control modes](power-modules/ADM-PC-LL25/theory_of_operation.md#control-modes), the module will command to the upstream PFC a certain input voltage, extending the operating range and improving the efficiency of the converter.

>[!ATTENTION] Only battery loads are allowed. Other usages are not supported at the moment! Connecting a different load may result in permanent damage for the module and the load, as well as representing a safety hazard.

![3phase charging](images/app_3phase_charger.svg ':size=100%')
<figcaption style="text-align: center">3-phase unidirectional EV charger</figcaption>