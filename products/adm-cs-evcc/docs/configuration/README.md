# EVCC Configuration

In Advantics controller configuration file `/srv/config.cfg`. To edit the file, `nano` and `vi` editors are already installed on the system.

&nbsp;
Options related to the generic interface as well as other controller behaviors reside in the `[vehicle]` section.

!!! note
    When modifying the `/srv/config.cfg` file, always remember that Advantics charge controllers
    works in __fake read-writable mode__ by default. Ie. changes are only written in RAM, and not
    persisted to the actual read-only partition. See our [Developer Guide](../buildroot-system/README.md) to learn how to temporarily or
    permanently switch to real writable mode.

!!! note
    Depending on the application the customer can add configuration entries relevant to the specific use case.

!!! warning
     - Any line starting with the "#" sign will be treated as a commented line and will not be taken into account during execution.
    - Remove the “#” at the beginning of every parameter you modify.
    - Leave no white space at the beginning of the line.


</br>

1. [Generalities](generalities.md)
1. [Current deviation](current_deviation.md)
1. [Inlet lock](inlet_lock.md)
1. [DC contactors](dc_contactors.md)
1. [CAN sensor](can_sensor.md)
1. [No BMS mode](no_bms.md)
1. [Hardware, applications and system](hardware.md)
1. [SAE J1939](j1939.md)
1. [CCS](ccs.md)
1. [TLS](tls.md)
