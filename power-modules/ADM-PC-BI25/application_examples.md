> [!UPDATE] {docsify-updated}
# Application examples

Please see the general ADVANTICS application whitepapers for more detailed examples. The following chapter simply presents several typical applications.

## 3-phase bidirectional charger
An advanced 3-phase fully bidirectional charger, capable of charging vehicles with 30 kW power, and extracting power back towards the grid. This configuration consists of ADM-PC-LF45 as a filter stage and inrush limiter, ADM-PC-BP25 as a Power Factor Correction stage, followed by ADM-PC-BI25, as isolated bidirectional DC/DC. In this case, the BI25 works in 'Voltage Follower' mode. The last stage is another ADM-PC-BP25, this time connected as a bidirectional Buck, regulating the 1000 V DC bus of the isolated DC/DC down to required voltage and current for EV charging/discharging.

![3phase bidir charging](images/app_3phase_bidir_charger.svg ':size=200%')
<figcaption style="text-align: center">3-phase bidireecdtional EV charger</figcaption>


## Compact 3-phase bidirectional charger
In this case the configuration consists of ADM-PC-LF45 as a filter stage and inrush limiter, ADM-PC-BP25 as a Power Factor Correction stage, followed by ADM-PC-BI25, as isolated bidirectional DC/DC. The BI25 interfaces directly
with the battery load, and operates in the 'PFC Voltage' control mode.

> [!WARNING] Because in this mode the DAB interfaces directly with the load (the battery), the operating range in this mode is limited and depends mostly on the AFE and DAB variant. Therefore, this mode is only recommended to be used with the VA01 variant of the AFE (1000 V), and with the 2:1 variant of the DAB. This will lead to an output voltage range of about 300 to 500V.

![3phase bidir charging](images/diagrams-compact_bidir_charger.svg ':size=200%')
<figcaption style="text-align: center">3-phase bidireecdtional EV charger</figcaption>