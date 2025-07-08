> [!UPDATE] {docsify-updated}
# EVCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-MEVC`.
## Software

### Major releases

| Branch | Date | Changelog | Download | Docker Hub |
|--------|------|-----------|----------|-------------|
| dev    | 2025-03-26| <ul><li>Initial MEVC Engineering Units release</li><li>MCS support</li><li>Includes [Advantics Controller System Manager](/home/amin/Documents/ADVANTICS/charge-controllers-workspace/Applications/documentation/charge-controllers/advantics_os/csm-web-ui.md)</li></ul> | - | <ul><li>[advantics/pev-controller:2.2.0](https://hub.docker.com/r/advantics/pev-controller/tags)</li><li>[advantics/ccs-evcc:2.3.0](https://hub.docker.com/r/advantics/ccs-evcc/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> |
| Release 2.0    | 2025-07-07| <ul><li><strong>pev-controller 2.2.2</strong><ul><li>Fix for re-entering emergency state when no inlet lock and contactors open CAN message is not fast enough</li><li>ADM-CS-MEVC-PB01-R0B support</li></ul></li><li><strong>ccs-evcc 2.3.2</strong><ul><li>Fix reset_cache causing nodes disconnection</li><li>ADM-CS-MEVC-PB01-R0B support</li><li>Enhanced Logging</li></ul><li><strong>advantics-csm 1.3.6</strong><ul><li>UI/UX improvements</li><li>ADM-CS-MEVC-PB01-R0B support</li></ul></li></ul>  | <li>**Option 1**: Pull from Docker hub following this [Guide](charge-controllers/advantics_os/ssh.md#option-1-requires-internet-pulling-the-update-from-docker-hub)</li><li>**Option 2**: Download .tar here: [Release 2.0](https://drive.google.com/uc?export=download&id=1UbFszaAsMXQeq533L6Q20KhT6ewDkbOw) Update instructions using .tar file here: [Full release update](charge-controllers/advantics_os/ssh.md#full-release-update)</li> | <ul><li>[advantics/pev-controller:2.2.2](https://hub.docker.com/r/advantics/pev-controller/tags)</li><li>[advantics/ccs-evcc:2.3.2](https://hub.docker.com/r/advantics/ccs-evcc/tags)</li><li>[advantics/advantics-csm:1.3.6](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> |
