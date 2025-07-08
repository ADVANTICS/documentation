> [!UPDATE] {docsify-updated}
# Charge Station Controller Versions

## Hardware

Currently supported hardware are for `ADM-CS-SPCC`.

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

| Branch | Date | Changelog | Download | Docker Hub |
|--------|------|-----------|----------|-------------|
| dev    | 2025-03-26| <ul><li>Initial SPCC Engineering Units release</li><li>MCS support</li><li>Includes [Advantics Controller System Manager](/home/amin/Documents/ADVANTICS/charge-controllers-workspace/Applications/documentation/charge-controllers/advantics_os/csm-web-ui.md)</li></ul> | - | <ul><li>[advantics/evse-controller:3.3.0](https://hub.docker.com/r/advantics/evse-controller/tags)</li><li>[advantics/ccs-secc:2.3.0](https://hub.docker.com/r/advantics/ccs-secc/tags)</li><li>[advantics/slac-evse:2.3.0](https://hub.docker.com/r/advantics/slac-evse/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> |
| Release 4.1    | 2025-07-07|  <ul><li><strong>evse-controller 3.3.3</strong><ul><li>Graceful recovery after CAN bus disconnection</li><li>Bender BenderISOCHA425HV Insulation monitor support</li></ul></li><li><strong>ccs-secc 2.3.3</strong><ul><li>Plug and Charge support</li><li>Add basic support for bidirectional scheduled mode</li><li>Comply with CharIN guidelines to simplify ISO15118-20 implementation (mobility needs and generator mode)</li><li>Fix reset_cache causing nodes disconnection (which also asserts interlock)</li><li>MCS: properly transition to waiting unplug when all_nodes_connected and the pistol is inserted</li><li>Enhanced Logging</li></ul></li><li><strong>chademo-secc 1.5.0</strong><ul><li>Enhanced Logging</li></ul></li><li><strong>advantics-csm 1.3.6</strong><ul><li>UI/UX improvements</li></ul><li><strong>ocpp-charge-point</strong></ul>  | <li>**Option 1**: Pull from Docker hub following this [Guide](charge-controllers/advantics_os/ssh.md#option-1-requires-internet-pulling-the-update-from-docker-hub)</li><li>**Option 2**: Download .tar here: [Release 4.1](https://drive.google.com/uc?export=download&id=1BKGBPBxun3zyU2DG1n7415U_D_fKvjNz) Update instructions using .tar file here: [Full release update](charge-controllers/advantics_os/ssh.md#full-release-update)</li> | <ul><li>[advantics/evse-controller:3.3.3](https://hub.docker.com/r/advantics/evse-controller/tags)</li><li>[advantics/ccs-secc:2.3.3](https://hub.docker.com/r/advantics/ccs-secc/tags)</li><li>[advantics/slac-evse:2.3.2](https://hub.docker.com/r/advantics/slac-evse/tags)</li><li>[advantics/chademo-secc:1.5.0](https://hub.docker.com/r/advantics/chademo-secc/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li><li>[advantics/ocpp-charge-point:1.5.1](https://hub.docker.com/r/advantics/ocpp-charge-point/tags)</li></ul> |

