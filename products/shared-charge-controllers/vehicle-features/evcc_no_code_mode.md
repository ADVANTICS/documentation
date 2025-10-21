# No code mode

This is not a particular mode _per se_. But rather a combination of three optional features of
Advantics controller that makes it possible to reach demonstrative working DC charge very quickly
without developing anything. It uses:

* DC contactors drivers embedded in the controller directly (see [DC contactors](charge-controllers/evcc_configuration/dc_contactors.md) config)
* A supported CAN sensor, that Advantics can directly provide you (see [CAN sensor](charge-controllers/evcc_configuration/can_sensor.md) config)
* [No BMS mode](charge-controllers/evcc_configuration/no_bms.md)

With these three features, you don't have to provide any data over CAN bus to the controller, and
you won't have to control any component yourself.

!!! attention
    The same disclaimers than in [No BMS mode](charge-controllers/evcc_configuration/no_bms.md) section apply. Use this only for quick
    demonstration, under a controlled environment, with low, safe and reasonable voltage and current
    values.

