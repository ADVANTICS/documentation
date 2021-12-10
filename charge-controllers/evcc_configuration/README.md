> [!UPDATE] {docsify-updated}
# EVCC Configuration

In Advantics controller configuration file `/srv/config.cfg`, options related to this generic
interface as well as other controller behaviours reside in the `[vehicle]` section.

> [!NOTE]
> When modifying the `/srv/config.cfg` file, always remember that Advantics charge controllers
> works in __fake read-writable mode__ by default. Ie. changes are only written in RAM, and not
> persisted to the actual read-only partition. See our Developer Guide to learn how to temporarily or
> permanently switch to real writable mode.

</br>

1. [Generalities](charge-controllers/evcc_configuration/generalities.md)
1. [Current deviation](charge-controllers/evcc_configuration/current_deviation.md)
1. [Inlet lock](charge-controllers/evcc_configuration/inlet_lock.md)
1. [DC contactors](charge-controllers/evcc_configuration/dc_contactors.md)
1. [CAN sensor](charge-controllers/evcc_configuration/can_sensor.md)
1. [No BMS mode](charge-controllers/evcc_configuration/no_bms.md)
