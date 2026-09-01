# Configuration

This document provides details about the configuration of the SECC.

## Configuration via the web UI

Please access the [web UI](../buildroot-system/access.md#web-ui) and navigate to the configuration section.

## Configuration via SSH access

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

1. [Pistols](pistols.md)
1. [CCS DC pistol](pistol-ccs-dc.md)
1. [CCS AC pistol](pistol-ccs-ac.md)
1. [CHAdeMO pistol](pistol-chademo.md)
1. [TLS](tls.md)
1. [OCPP](ocpp.md)
1. [Temperature](temperature.md)
1. [Applications, logging, hardware and system](generalities.md)
