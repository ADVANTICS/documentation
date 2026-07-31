---
hide:
  - toc
---

<!-- > [!UPDATE] {docsify-updated} -->
# EVCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-EVCC` units of "Gen3" variant
(using Vertexcom PLC chipset and Toradex Colibri iMX7 SoM). This generation had 4 hardware revisions so far.

Past hardware variants (no longer supported) were based firstly on the versatile `ADM-CO-CUI1` unit,
then on the first version of the `ADM-CO-EVCC` unit, both being "Gen2" variants (ie. using Qualcomm
PLC chipset and Toradex Colibri iMX6 SoM).

## Software

### Releases

<!-- Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

<div class="small-table compact-table">

| Version | Release date | Changelog | Full system image ([doc](buildroot-system/sys3_update.md#sd-card-update)) | Updater tool ([doc](vehicle-features/evcc_updater.md)) | Notes |
|---------|--------------|-----------|-------------------|--------------|-------|
| 2.0.0rc3.post1 | 2022-11-25 | [Changelog](https://www.dropbox.com/s/mc65mf3cbnhzuth/CHANGELOG-PEV-2.0.0rc3.txt?st=wyn8zfm8&dl=0) | - | Normal versions:<br/> [Windows](https://www.dropbox.com/s/1o0fyykhw6ye19c/pev-updater-2.0.0rc3.post1.exe?st=gomhg1o9&dl=1) \| [Linux](https://www.dropbox.com/s/4bqmhtoak7fmydq/pev-updater-2.0.0rc3.post1?st=vh1xvrw7&dl=1) <br/>Versions for pistol update:<br/>[Windows](https://www.dropbox.com/s/z69588amdecowox/pev-plc-updater-2.0.0rc3.post1.exe?dl=1) \| [Linux](https://www.dropbox.com/s/cgpt1pc9qqae10y/pev-plc-updater-2.0.0rc3.post1?st=rk6j58el&dl=1) | <b>- The update tool must be applied on a system that is at least in 2.0.0rc2. If not, update first to 2.0.0rc2.</b><br/><br/>- post1 version fixes a minor missing file in the updater tool. |
| 2.0.0rc2 | 2021-06-11 | [Changelog](https://www.dropbox.com/s/jg4o47qyvsu7nf9/CHANGELOG-PEV-2.0.0rc2.txt?st=0vgzjw8c&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/z87kacxmtcos32o/adm-cs-evcc-2.0.0rc2.zip?st=vk9b38yq&dl=1) | - | - |
| 2.0.0rc1 | 2021-02-04 | [Changelog](https://www.dropbox.com/s/gj1pk8s2xjegw09/CHANGELOG-PEV-2.0.0rc1.txt?st=ugwr816z&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/g44jyzotooxmq05/adm-cs-evcc-2.0.0rc1.zip?st=3pq3u0kp&dl=1) | - | - |
| 2019-06-11--001 | 2019-06-11 | [Changelog](https://www.dropbox.com/s/7pxdc6cvobque13/CHANGELOG-PEV--2019-06-11.txt?st=kevsljp0&dl=0) | [ADM-CS-EVCC (Gen2)](https://www.dropbox.com/s/k2f2mfa7v77vrfv/advantics-charge-controller-pev-2019-06-11--001.zip?dl=1)<br/>[ADM-CO-CUI1](https://www.dropbox.com/s/byxmzy5azspqe0m/advantics-charge-controller-generic-pev-2019-06-11--001.zip?st=a6vtspzk&dl=1) | - | - |
| 2018-09-25--001 | 2018-09-25 | - | [ADM-CO-CUI1](https://www.dropbox.com/s/fet0k009bf7r7b4/advantics-charge-controller-pev-2018.09.25--001.zip?st=l6zjcz21&dl=1) | - | - |

</div>

### Intermediate container releases

Intermediate container releases can be generated to make so-called [patch update](buildroot-system/sys3_update.md#patch-update).
These are "partial releases" that are internally tagged (and hence follow reproducible build). They
are a bit more tested than snapshots. But not as much as for major releases.

!!! note
    This table is purged when a new major release is published.

    The following updates are to be applied **on top of major release 2.0.0rc3.post1**.

<div class="small-table compact-table">

| Date | Comment | pev-controller | ccs-evcc | slac-pev |
|------|---------|----------------|----------|----------|
| 2023-01-05 | Fixes constant unlocking attempt when in AC_Ending_Charge for a long time | [2.0.6](https://www.dropbox.com/s/s6b4jq2ofwwyzq8/pev-controller-2.0.6.tar?st=y6sk06sl&dl=1) | - | - |

</div> -->

<!-- ### Snapshots

Snapshots are made when we commit particular changes (eg. bug fix, new function) that are
"up for grab" without waiting that we do a proper major release or even an intermediate container
release.

!!! warning
    These are development releases -->
<div class="release-table" markdown="1">

| Branch | Date | Notable differences | Download |
|---|---|---|---|
| 2018-09-25--001 | 2018-09-25 | ADM-CO-CUI1 | - |
| 2019-06-11--001 | 2019-06-11 | [Changelog](https://www.dropbox.com/s/7pxdc6cvobque13/CHANGELOG-PEV--2019-06-11.txt?st=kevsljp0&dl=0) | [ADM-CS-EVCC (Gen2)](https://www.dropbox.com/s/k2f2mfa7v77vrfv/advantics-charge-controller-pev-2019-06-11--001.zip?dl=1)<br/>[ADM-CO-CUI1](https://www.dropbox.com/s/byxmzy5azspqe0m/advantics-charge-controller-generic-pev-2019-06-11--001.zip?st=a6vtspzk&dl=1) |
| 2.0.0rc1 | 2021-02-04 | [Changelog](https://www.dropbox.com/s/gj1pk8s2xjegw09/CHANGELOG-PEV-2.0.0rc1.txt?st=ugwr816z&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/g44jyzotooxmq05/adm-cs-evcc-2.0.0rc1.zip?st=3pq3u0kp&dl=1) |
| 2.0.0rc2 | 2021-06-11 | [Changelog](https://www.dropbox.com/s/jg4o47qyvsu7nf9/CHANGELOG-PEV-2.0.0rc2.txt?st=0vgzjw8c&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/z87kacxmtcos32o/adm-cs-evcc-2.0.0rc2.zip?st=vk9b38yq&dl=1) |
| 2.0.0rc3 | 2022-11-03 | Prefigure rc3 | [Snapshot](https://www.dropbox.com/s/oiw76a7lfky3ygu/pev-snapshot-stable--2022-11-02.tar?st=mxnc610w&dl=1) |
| release 1.0 | 2022-11-25 | [Changelog](https://www.dropbox.com/s/mc65mf3cbnhzuth/CHANGELOG-PEV-2.0.0rc3.txt?st=wyn8zfm8&dl=0) | - |
| [Bidirectional dev](vehicle-features/evcc_bidirectional.md) | 2022-11-17 | ISO 15118-20<br/>Generic CAN interface v2 | [Snapshot](https://www.dropbox.com/s/vbex2k6u9mszfut/pev-bidir--2022-11-17.tar?st=mkffbqdx&dl=1) |
| [Release 2024-10-15](vehicle-features/evcc_bidirectional.md) | 2024-10-15 | ISO15118-20 BPT: Use CAN message to dynamically update current limits | [pev-2024-10-15.tar](https://drive.google.com/uc?export=download&id=1c0XZHXs2LfjTYAYSp9HNQ0ugLRP0Qmlb) |
| release 2.0 | 2025-07-07 | <ul><li>New Application:<ul><li>advantics-csm: Advantics CSM, short for Advantics Controller System Manager, handles all system-level operations.<br/>It provides a web interface for monitoring and configuring the system, minimizing the need for manual config file edits and command-line interactions.<br/>Users can access logs, manage applications, and perform system updates directly through the interface ([CSM Web UI](advos-yocto-system/csm-web-ui.md)).</li></ul></li><li><strong>pev-controller 2.2.2</strong><ul><li>fix for re-entering emergency state when no_inlet_lock and contactors open CAN message not fast enough</li></ul></li><li><strong>ccs-evcc 2.3.2</strong><ul><li>Plug and Charge support</li><li>Fix calling GC by reset_cache causing nodes disconnection (which also asserts interlock).</li></ul></li></ul> | Download link: [pev-release-2.0.zip](https://drive.google.com/uc?export=download&id=1If2EobawN2vKWnXWWLHdxtfgXnbMNKB7)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.1 | 2025-07-23 | <ul><li><strong>pev-controller 2.2.3</strong><ul><li>fix PEV temperature: add support for temperature monitoring</li><li>allow contactor feedback via CAN bus while contactor control is done via IOs</li><li>allow LEDs control via CAN bus interface</li></ul></li><li><strong>advantics-csm 1.4.2</strong><ul><li>extend config interface</li><li>fix bug in SW update process on management interface.</li></ul></li></ul> | Download link: [evcc-23-07-2025.zip](https://drive.google.com/uc?export=download&id=136dllcmk9AMYky_Nao0IaCV1NHmFTTpm)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.2 | 2025-08-04 | <ul><li><strong>pev-controller 2.2.4</strong><ul><li>New CAN bus signal [HV_Preparing_Hold_Off](vehicle-can-interfaces/can_v2.md#EV_Status-HV_Preparing_Hold_Off):<br/>Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.</li><li>Advantics_Generic_PEV_protocol_v2: Expand energy limits and revise signal slopes accordingly.</li></ul></li><li><strong>ccs-evcc 2.3.3</strong><ul><li>Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.</li></ul></li></ul> | Download link: [evcc-04-08-2025.zip](https://drive.google.com/uc?export=download&id=1eYflFXaEiRZVk_2vr8iMdnCfZEByECmK)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.3 | 2025-09-15 | <ul><li><strong>pev-controller 2.2.5</strong><br/>New CAN bus message [EVCC_MEVC_Diagnostic_Status](vehicle-can-interfaces/can_v2.md#evcc-mevc-diagnostic-status): Diagnostic status of the charge controller:<ul><li>Shows active faults and errors detected by the charge controller.</li><li>Status signals received from the charger over High-Level Communication (HLC).</li></ul></li><li><strong>ccs-evcc 2.3.5</strong><ul><li>Send HLC error codes and forward charger status signals received over High-Level Communication (HLC).</li><li>Fix minor bug in ServiceDiscovery in handling extra services.</li></ul></li><li><strong>advantics-csm 1.5.4</strong><ul><li>Fix log exporting issue; improve logging page experience (docker socket starvation, app status in colors).</li><li>Add export config file in config page.</li><li>Add J1939 capabilities; QOL improvements for J1939 logging.</li><li>Fix management page for EVCC (official support of EVCC).</li><li>Add error stack to monitoring page.</li><li>Fix UI typos and descriptions.</li></ul></li></ul> | Download link: [evcc-15-09-2025.zip](https://drive.google.com/uc?export=download&id=1kNEDyp6DiZuyDF6GrnHkSmdSWe2g0shR)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.4 | 2025-12-11 | <ul><li><strong>pev-controller 2.3.0</strong><ul><li>Add possibility of dynamic target voltage control (configurable)</li><li>Allow bidirectional cycling at full SOC (configurable)</li><li>Disable current deviation check against target current in range mode (dynamic mode)</li></ul></li><li><strong>ccs-evcc 2.4.0</strong><ul><li>Possibility to disable AC charging (configurable) (only relevant for CCS)</li><li>Pause and resume session according to ISO15118-2 and ISO15118-20</li></ul></li><li><strong>advantics-csm 1.6.3</strong><ul><li>Add the possibility to restart CSM when submitting config from the UI</li><li>Toggle J1939/CAN monitoring on config change without restarting the whole app</li><li>Support both extendend and non-extended IDs for CAN monitoring</li></ul></li></ul> | Download link: [evcc-11-12-2025.zip](https://drive.google.com/uc?export=download&id=1YJNsdh0bMZ7Wx3zomCCXhH29cs_JgaRN)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.4.1 | 2025-12-23 | <ul><li><strong>ccs-evcc 2.4.1</strong><ul><li>Bug fix: checking for wrong CP state in session stop state resulting in abnormal session termination in some cases</li></ul></li><li><strong>advantics-csm 1.6.4</strong><ul><li>fix a minor bug</li></ul></li></ul> | Download link: [evcc-23-12-2025.zip](https://drive.google.com/uc?export=download&id=1P94tjWQfFQqn-2JCfV5JVXagRMNqQ8CT)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.5 | 2026-03-13 | <ul><li><strong>pev-controller 2.4.0</strong><ul><li>Fixed checking DC contactors state and DC messages during emergency while AC charging</li><li>Fixed inputs message being sent with wrong values before initialization completes (startup race condition)</li><li>Contactors opening: raised the current-below-limit threshold to 5 A; added a configurable timeout after which contactors open unconditionally if current doesn't drop below limit</li><li>Startup safety: inputs messages are now suppressed until hardware I/O initialization is fully complete</li><li>Temperature: median filter is now applied to temperature sensor inputs</li><li>GC performance: persistent objects are now untracked from the garbage collector to reduce GC overhead</li></ul></li><li><strong>ccs-evcc 2.5.0</strong><ul><li>Fixed bug where frontend did not send Closing_Communication stage to backend in EmergencyShutdownState</li><li>Moved CP state reporting to the PLC reading level to eliminate wrong-state reports</li><li>Fixed alarm cancelled more than once on protocol reset (cancel only once per exit)</li><li>bcb_toggle_detected called from unexpected states now handled gracefully (no-op)</li><li>Skip CP filtering while resuming a paused session, to correctly detect the B1→B2 transition</li><li>Allow session resume only when the previous session is fully over</li></ul></li><li><strong>advantics-csm 1.7.0</strong><ul><li>Fix logic while exporting logs, server would respond with error code and nothing attached</li><li>Add the ability to generate sample config for every controller</li><li>Fix dynamic voltage meter bar in monitoring and use kW for power metering instead of W</li><li>Remove unused items from navigation side bar</li><li>Minor improvements</li></ul></li></ul> | Download link: [evcc-release-2.5.zip]()<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.6 | 2026-04-10 | <ul><li><strong>pev-controller 2.5.0</strong><ul><li>Fixed onefile mode folders not getting cleared properly on power cycle</li><li>Added advanced E-stop contactor handling options for unreliable current measurements</li></ul></li><li><strong>ccs-evcc 2.6.0</strong><ul><li>Fixed onefile mode folders not getting cleared properly on power cycle</li></ul></li><li><strong>advantics-csm 1.7.1</strong><ul><li>Fix temperature config section</li><li>Bring back controller type to header</li><li>Add CSM version on footer</li><li>Migrate from remix to react router 7</li></ul></li></ul> | Download link: [evcc-release-2.6.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.6.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.6.1 | 2026-04-14 | <ul><li><strong>ccs-evcc 2.6.1</strong><ul><li>Fixed EVCC ID not read correctly from config file</li></ul></li></ul> | Download link: [evcc-release-2.6.1.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.6.1.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.7.1 | 2026-04-23 | <ul><li><strong>pev-controller 2.6.2</strong><ul><li>Introduce a configurable median filter for the lock feedback</li><li>Fixed reading HW variant from EEPROM</li><li>Bidirectional power transfer: more adapted contactors handling</li><li>Fixed race condition during AC ending charge affecting lock state check</li></ul></li><li><strong>ccs-evcc 2.7.0</strong><ul><li>Improved MCS sequence: wait for contactors to open at the end of ending charge phase and before setting CE state B</li></ul></li><li><strong>advantics-csm 1.7.2</strong><ul><li>Add the new config parameters</li><li>Add dig_out options in the UI</li></ul></li></ul> | Download link: [evcc-release-2.7.1.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.7.1.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.7.2 | 2026-04-30 | <ul><li><strong>advantics-csm 1.7.3</strong><ul><li>Fix configuration issue with J1939 interface</li></ul></li></ul> | Download link: [evcc-release-2.7.2.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.7.2.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.7.2.post1 | 2026-06-01 | <ul><li>Fix system services update</li></ul> | Download link: [evcc-release-2.7.2.post1.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.7.2.post1.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.7.3 | 2026-06-05 | <ul><li><strong>advantics-csm 1.7.4</strong><ul><li>Fix docker client issue that was leading to blocking behavior on image discovery</li></ul></li></ul> | Download link: [evcc-release-2.7.3.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.7.3.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |
| release 2.8.0 | 2026-06-26 | <ul><li><strong>pev-controller 2.7.0</strong><ul><li>ISO15118-20: cap energy requests based on config params</li><li>Always report the state of the digital inputs over CAN bus regardless of their configuration</li><li>Add possibility to use different CAN bus interfaces for IVT and Generic CAN interface using `can_sensor_if` config entry</li><li>Retry IVT sensor configuration until it powers up after init/sleep. Capped by configured timeout `ivt_init_timeout_s`</li><li>Add possibility to assert HV hold-off until the BMS reports ready using config entry `hold_off_until_bms_ready`</li><li>Enable current derate function based on temperature</li></ul></li><li><strong>pev-slac 2.4.0</strong><ul><li>fix: In multi-EVSE, duplicate CM_SLAC_MATCH.CNF lingers in buffer causing cm_set_key to hard-fail</li></ul></li><li><strong>advantics-csm 1.7.6</strong><ul><li>TLS certificates management</li><li>New configuration entries added</li></ul></li></ul> | Download link: [evcc-release-2.8.0.zip](https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/evcc/evcc-release-2.8.0.zip)<br/>Update instructions: ([Full release update](buildroot-system/sys3_update.md#full-release-update)) |

</div>
