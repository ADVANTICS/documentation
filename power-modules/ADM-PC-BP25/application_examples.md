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

## Bidirectional Buck
Step down bidirectional DC/DC. The left side voltage must always be higher than the right side voltage for the application to work. Overlapping voltages (like charging 400V battery from a 400V battery) are not possible.

![Bidirectional buck](images/app_bidir_buck.svg ':size=70%')
<figcaption style="text-align: center">Figure 16: Bidirectional buck</figcaption>

## Bidirectional Boost-Buck
Step up, followed by a Step down DC/DC. Removes the limitation of a simple Bidirectional Buck, as now the voltage regions can overlap. The first stage (no matter from which direction) is always a Step up. Then this voltage is stepped down to provide the Voltage and Current regulation.

![Bidirectional boost buck](images/app_bidir_boost_buck.svg ':size=200%')
<figcaption style="text-align: center">Figure 17: Bidirectional boost-buck</figcaption>

## Parallel 150kW bidirectional Buck
It is also possible to use modules in parallel, to increase the total power.

![150kW Bidirectional buck](images/app_150kw_bidir_buck.svg ':size=70%')
<figcaption style="text-align: center">Figure 18: 150kW Bidirectional buck</figcaption>

## 3-phase portable battery powered inverter/charger
An example of a much more complex system, control-wise. Two ADM-PC-BP25 modules are used, with one always providing boost on two phases, and third phase is used to generate Neutral wire (50% duty cycle). The second ADM-PC-BP25 is then used to generate L1, L2, and L3 phases. This configuration then allows for several modes of operation - 3-phase+Neutral power inverter, 1-phase charger (to refill the built-in battery), and a 3-phase charger. The following diagram illustrates these three modes.

![portable inverter charger](images/app_portable_inverter_charger.svg ':size=90%')
<figcaption style="text-align: center">Figure 19: Portable inverter/charger</figcaption>
