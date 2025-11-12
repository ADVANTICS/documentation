> [!UPDATE] {docsify-updated}
# EVCC Configuration

In Advantics controller configuration file `/srv/config.cfg`. To edit the file, `nano` and `vi` editors are already installed on the system.

&nbsp;
Options related to the generic interface as well as other controller behaviors reside in the `[vehicle]` section.

> [!NOTE]
> When modifying the `/srv/config.cfg` file, always remember that Advantics charge controllers
> works in __fake read-writable mode__ by default. Ie. changes are only written in RAM, and not
> persisted to the actual read-only partition. See our [Developer Guide](charge-controllers/sys3_user/README.md) to learn how to temporarily or
> permanently switch to real writable mode.

> [!NOTE]
> Depending on the application the customer can add configuration entries relevant to the specific use case.

> [!WARNING]
>  - Any line starting with the "#" sign will be treated as a commented line and will not be taken into account during execution.
> - Remove the “#” at the beginning of every parameter you modify.
> - Leave no white space at the beginning of the line.


</br>

1. [Generalities](charge-controllers/mevc_configuration/generalities.md)
1. [MCS](charge-controllers/mevc_configuration/mcs.md)
1. [Current deviation](charge-controllers/mevc_configuration/current_deviation.md)
1. [Inlet lock](charge-controllers/mevc_configuration/inlet_lock.md)
1. [DC contactors](charge-controllers/mevc_configuration/dc_contactors.md)
1. [CAN sensor](charge-controllers/mevc_configuration/can_sensor.md)
1. [No BMS mode](charge-controllers/mevc_configuration/no_bms.md)