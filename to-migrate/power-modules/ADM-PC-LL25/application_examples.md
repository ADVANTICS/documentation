> [!UPDATE] {docsify-updated}
# Application examples


## Unidirectional 3-phase Electric vehicle charger
The typical use of the ADM-PC-LL25 is as electric vehicle unidirectional charger, toghether with an upstream filter ADM-PC-LF45 and a power factor correction ADM-PC-BP25 or ADM-PC-UP25.

In this example, the ADM-PC-LL25 is used in the PFC Voltage control mode. As explained in [Control modes](power-modules/ADM-PC-LL25/theory_of_operation.md#control-modes), the module will command to the upstream PFC a certain input voltage, extending the operating range and improving the efficiency of the converter.


![3phase charging](images/app_3phase_charger2.svg ':size=100%')
<figcaption style="text-align: center">3-phase unidirectional EV charger</figcaption>

## Unidirectional 3-phase Electric vehicle charger with parallel/series connection
Another possibility is to chain two LL25 combos in parallel or series connection either to increase maximum output current or to increase maximum output voltage. The connection could be made as in the picture below, where parallel or series connection is selected by means of relays.

![3phase charging](images/diagrams-BPUD_500V-1000V.svg ':size=100%')
<figcaption style="text-align: center">3-phase unidirectional EV charger with parallel or series connection</figcaption>

