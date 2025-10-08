> [!UPDATE] {docsify-updated}
# Charge Station Controller Versions

## Hardware

Currently supported hardware are for `ADM-CS-SECC` (using Vertexcom PLC chipset and Toradex Colibri iMX7 SoM).

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

<div class="small-table compact-table">

| Version | Release date | Changelog | Full system image | Notes |
|---------|--------------|-----------|-------------------|-------|
| Release 3.0           | 2020-12-18 | - | - | - |
| 4.x.dev1 - 4.x.dev15 | 2021-2024  | [Changelog](https://www.notion.so/EVSE-Migration-from-3-x-to-4-0-7526d289f055493db054452cbbfeb98f?pvs=4#4c68cd39adaf4465a34b912686f97dd2)  | [4.x.dev branch](https://www.notion.so/EVSE-Migration-from-3-x-to-4-0-7526d289f055493db054452cbbfeb98f) | releases 4.x was the development branch of 2021-2024|
| Release 4.0           | 2024-12-20 | [Changelog](https://www.notion.so/evse-4-0-dev15-18a424f0ef998087863bfd83360cc6c2) | [Release 4.0](https://www.notion.so/evse-4-0-dev15-18a424f0ef998087863bfd83360cc6c2) | |
| Release 4.1 | 2025-07-07 | New Application:<br/>- advantics-csm: Advantics CSM, short for Advantics Controller System Manager, handles all system-level operations.<br/>It provides a web interface for monitoring and configuring the system, minimizing the need for manual config file edits and command-line interactions.<br/>Users can access logs, manage applications, and perform system updates directly through the interface ([CSM Web UI](https://advantics.github.io/documentation/#/charge-controllers/advantics_os/csm-web-ui)).<br/><br/>evse-controller 3.3.3:<br/>- graceful recovery after CAN bus disconnection<br/>- Bender BenderISOCHA425HV Insulation monitor support<br/><br/>ccs-secc 2.3.3:<br/>- Plug and Charge according to ISO15118-2 support<br/>- Add basic support for bidirectional scheduled mode<br/>- comply with charin guidelines to simplify ISO15118-20 implementation (mobility needs and generator mode mainly)<br/>- Fix calling GC by reset_cache causing nodes disconnection (which also asserts interlock).<br/>- MCS: properly transition to waiting unlug when all_nodes_connected and the pistol is inserted<br/>- Enhanced Logging<br/><br/>chademo-secc 1.5.0:<br/>- Enhanced Logging | [Release 4.1](https://drive.google.com/file/d/1ewuEgluU2LCU00oVsK9CbdyYwer9T8wB/view?usp=drive_link) | Update instructions here ([Full release update](charge-controllers/sys3_update.md#full-release-update)). |
| Release 4.1.1 | 2025-10-06 | - advantics-csm 1.5.4:<br/>- Fix log exporting issue; improve logging page experience (docker socket starvation, app status in colors).<br/>- Add export config file in config page.<br/>- Fix UI typos and descriptions. | [Release 4.1.1](https://drive.google.com/uc?export=download&id=1mBCwU_lgQI7f7dWBv-10lnNPL-nmP4gf) | Update instructions here ([Full release update](charge-controllers/sys3_update.md#full-release-update)). |


</div>
