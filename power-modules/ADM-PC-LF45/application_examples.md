> [!UPDATE] {docsify-updated}
# Application examples

Please see the general ADVANTICS application whitepapers for more detailed examples. The following chapter simply presents several typical applications.


## 3-phase unidirectional charger 
A basic 30 kW 3-phase charger, using ADM-PC-LF45 as a filter stage and inrush limiter, ADM-PC-BP25 as a Power Factor Correction stage, and the ADM-PC-LL25 as a unidirectional isolated DC/DC converter.

![3phase charging](images/app_3phase_charger.svg ':size=200%')
<figcaption style="text-align: center">Figure 14: 3-phase unidireecdtional EV charger</figcaption>

## 3-phase bidirectional charger
An advanced 3-phase fully bidirectional charger, capable of charging vehicles with 30 kW power, and extracting power back towards the grid. This configuration consists of ADM-PC-LF45 as a filter stage and inrush limiter, ADM-PC-BP25 as a Power Factor Correction stage, followed by ADM-PC-BI25, an isolated bidirectional DC/DC. The last stage is another ADM-PC-BP25, this time connected as a bidirectional Buck, regulating the 1000 V DC bus of the isolated DC/DC down to required voltage and current for EV charging/discharging.

![3phase bidir charging](images/app_3phase_bidir_charger.svg ':size=200%')
<figcaption style="text-align: center">Figure 15: 3-phase bidireecdtional EV charger</figcaption>
