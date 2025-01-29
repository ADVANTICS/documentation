> [!UPDATE] {docsify-updated}
# EVCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-EVCC` units of "Gen3" variant
(using Vertexcom PLC chipset and Toradex Colibri iMX7 SoM). This generation had 4 hardware revisions so far.

Past hardware variants (no longer supported) were based firstly on the versatile `ADM-CO-CUI1` unit,
then on the first version of the `ADM-CO-EVCC` unit, both being "Gen2" variants (ie. using Qualcomm
PLC chipset and Toradex Colibri iMX6 SoM).

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

<div class="small-table compact-table">

| Version | Release date | Changelog | Full system image ([doc](charge-controllers/sys3_update.md#sd-card-update)) | Updater tool ([doc](charge-controllers/evcc_updater.md)) | Notes |
|---------|--------------|-----------|-------------------|--------------|-------|
| 2.0.0rc3.post1 | 2022-11-25 | [Changelog](https://www.dropbox.com/s/mc65mf3cbnhzuth/CHANGELOG-PEV-2.0.0rc3.txt?st=wyn8zfm8&dl=0) | - | Normal versions:<br/> [Windows](https://www.dropbox.com/s/1o0fyykhw6ye19c/pev-updater-2.0.0rc3.post1.exe?st=gomhg1o9&dl=1) \| [Linux](https://www.dropbox.com/s/4bqmhtoak7fmydq/pev-updater-2.0.0rc3.post1?st=vh1xvrw7&dl=1) <br/>Versions for pistol update:<br/>[Windows](https://www.dropbox.com/s/z69588amdecowox/pev-plc-updater-2.0.0rc3.post1.exe?dl=1) \| [Linux](https://www.dropbox.com/s/cgpt1pc9qqae10y/pev-plc-updater-2.0.0rc3.post1?st=rk6j58el&dl=1) | <b>- The update tool must be applied on a system that is at least in 2.0.0rc2. If not, update first to 2.0.0rc2.</b><br/><br/>- post1 version fixes a minor missing file in the updater tool. |
| 2.0.0rc2 | 2021-06-11 | [Changelog](https://www.dropbox.com/s/jg4o47qyvsu7nf9/CHANGELOG-PEV-2.0.0rc2.txt?st=0vgzjw8c&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/z87kacxmtcos32o/adm-cs-evcc-2.0.0rc2.zip?st=vk9b38yq&dl=1) | - | - |
| 2.0.0rc1 | 2021-02-04 | [Changelog](https://www.dropbox.com/s/gj1pk8s2xjegw09/CHANGELOG-PEV-2.0.0rc1.txt?st=ugwr816z&dl=0) | [ADM-CS-EVCC (Gen3)](https://www.dropbox.com/s/g44jyzotooxmq05/adm-cs-evcc-2.0.0rc1.zip?st=3pq3u0kp&dl=1) | - | - |
| 2019-06-11--001 | 2019-06-11 | [Changelog](https://www.dropbox.com/s/7pxdc6cvobque13/CHANGELOG-PEV--2019-06-11.txt?st=kevsljp0&dl=0) | [ADM-CS-EVCC (Gen2)](https://www.dropbox.com/s/k2f2mfa7v77vrfv/advantics-charge-controller-pev-2019-06-11--001.zip?dl=1)<br/>[ADM-CO-CUI1](https://www.dropbox.com/s/byxmzy5azspqe0m/advantics-charge-controller-generic-pev-2019-06-11--001.zip?st=a6vtspzk&dl=1) | - | - |
| 2018-09-25--001 | 2018-09-25 | - | [ADM-CO-CUI1](https://www.dropbox.com/s/fet0k009bf7r7b4/advantics-charge-controller-pev-2018.09.25--001.zip?st=l6zjcz21&dl=1) | - | - |

</div>

### Intermediate container releases

Intermediate container releases can be generated to make so-called [patch update](charge-controllers/sys3_update.md#patch-update).
These are "partial releases" that are internally tagged (and hence follow reproducible build). They
are a bit more tested than snapshots. But not as much as for major releases.

> [!NOTE]
> This table is purged when a new major release is published.
>
> The following updates are to be applied **on top of major release 2.0.0rc3.post1**.

<div class="small-table compact-table">

| Date | Comment | pev-controller | ccs-evcc | slac-pev |
|------|---------|----------------|----------|----------|
| 2023-01-05 | Fixes constant unlocking attempt when in AC_Ending_Charge for a long time | [2.0.6](https://www.dropbox.com/s/s6b4jq2ofwwyzq8/pev-controller-2.0.6.tar?st=y6sk06sl&dl=1) | - | - |

</div>

### Snapshots

Snapshots are made when we commit particular changes (eg. bug fix, new function) that are
"up for grab" without waiting that we do a proper major release or even an intermediate container
release.

> [!WARNING]
> These are development releases

<div class="small-table compact-table">

| Branch | Date | Notable differences | Download |
|--------|------|---------------------|----------|
| Stable | 2022-11-03 | Prefigure rc3 | [Snapshot](https://www.dropbox.com/s/oiw76a7lfky3ygu/pev-snapshot-stable--2022-11-02.tar?st=mxnc610w&dl=1) |
| [Bidirectional](charge-controllers/evcc_bidirectional.md) | 2022-11-17 | ISO 15118-20<br/>Generic CAN interface v2 | [Snapshot](https://www.dropbox.com/s/vbex2k6u9mszfut/pev-bidir--2022-11-17.tar?st=mkffbqdx&dl=1) |
| [Bidirectional 2024-10-15](charge-controllers/evcc_bidirectional.md) | 2024-10-15 | ISO15118-20 BPT: Use CAN message to dynamically update current limits | [pev-bidir--2024-10-15.tar](https://drive.google.com/uc?export=download&id=1c0XZHXs2LfjTYAYSp9HNQ0ugLRP0Qmlb) |


</div>
