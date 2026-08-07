# Configuration

This document provides details about the config file sections and entries for ADVANTICS SECC **releases 4.x**.

> Version 4.x of the SW as well as update instructions are available here: [development branch](https://www.notion.so/EVSE-Migration-from-3-x-to-4-x-7526d289f055493db054452cbbfeb98f).

&nbsp;

**For customers using versions 3.x, please consult the actual config file, as it contains all the necessary information on each section.**

> **Note**
>
> Depending on the application the customer can add configuration entries relevant to the specific use case.


In Advantics controller the configuration file is accessible at this path: `/srv/config.cfg`. To edit the file, `nano` and `vi` editors are already installed on the system.

> **Note**
>
> - When modifying the `/srv/config.cfg` file, always remember that
> Advantics charge controllers works in *fake read-writable mode* by
> default. Ie. changes are only written in RAM, and not persisted to the
> actual read-only partition. See section [**Read-only file system**](../advos-yocto-system/updating.md) to
> learn how to temporarily or permanently switch to real writable mode.

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
