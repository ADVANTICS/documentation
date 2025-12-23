> [!UPDATE] {docsify-updated}

# SPCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-SPCC`.

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

<!-- | Branch | Date | Changelog | Download | Docker Hub |
|--------|------|-----------|----------|-------------|
| dev    | 2025-03-26| <ul><li>Initial SPCC Engineering Units release</li><li>MCS support</li><li>Includes [Advantics Controller System Manager](charge-controllers-workspace/Applications/documentation/charge-controllers/advantics_os/csm-web-ui.md)</li></ul> | - | <ul><li>[advantics/evse-controller:3.3.0](https://hub.docker.com/r/advantics/evse-controller/tags)</li><li>[advantics/ccs-secc:2.3.0](https://hub.docker.com/r/advantics/ccs-secc/tags)</li><li>[advantics/slac-evse:2.3.0](https://hub.docker.com/r/advantics/slac-evse/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> |
| Release 4.1    | 2025-07-07|  <ul><li><strong>evse-controller 3.3.3</strong><ul><li>Graceful recovery after CAN bus disconnection</li><li>Bender BenderISOCHA425HV Insulation monitor support</li></ul></li><li><strong>ccs-secc 2.3.3</strong><ul><li>Plug and Charge support</li><li>Add basic support for bidirectional scheduled mode</li><li>Comply with CharIN guidelines to simplify ISO15118-20 implementation (mobility needs and generator mode)</li><li>Fix reset_cache causing nodes disconnection (which also asserts interlock)</li><li>MCS: properly transition to waiting unplug when all_nodes_connected and the pistol is inserted</li><li>Enhanced Logging</li></ul></li><li><strong>chademo-secc 1.5.0</strong><ul><li>Enhanced Logging</li></ul></li><li><strong>advantics-csm 1.3.6</strong><ul><li>UI/UX improvements</li></ul><li><strong>ocpp-charge-point</strong></ul>  | <li>**Option 1**: Pull from Docker hub following this [Guide](charge-controllers/advantics_os/ssh.md#option-1-requires-internet-pulling-the-update-from-docker-hub)</li><li>**Option 2**: Download .tar here: [Release 4.1](https://drive.google.com/uc?export=download&id=1BKGBPBxun3zyU2DG1n7415U_D_fKvjNz) Update instructions using .tar file here: [Full release update](charge-controllers/advantics_os/ssh.md#full-release-update)</li> | <ul><li>[advantics/evse-controller:3.3.3](https://hub.docker.com/r/advantics/evse-controller/tags)</li><li>[advantics/ccs-secc:2.3.3](https://hub.docker.com/r/advantics/ccs-secc/tags)</li><li>[advantics/slac-evse:2.3.2](https://hub.docker.com/r/advantics/slac-evse/tags)</li><li>[advantics/chademo-secc:1.5.0](https://hub.docker.com/r/advantics/chademo-secc/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li><li>[advantics/ocpp-charge-point:1.5.1](https://hub.docker.com/r/advantics/ocpp-charge-point/tags)</li></ul> |
 -->

<style>
  table.custom-table {
    width: 100%;
    border-collapse: collapse;
  }
  table.custom-table th,
  table.custom-table td {
    border: 1px solid #ccc;
    padding: 8px;
    vertical-align: top;
  }
  table.custom-table th.branch-col,
  table.custom-table td.branch-col {
    width: 12%;
    white-space: nowrap;
  }
  table.custom-table th.date-col,
  table.custom-table td.date-col {
    width: 12%;
    white-space: nowrap;
  }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th class="branch-col">Branch</th>
      <th class="date-col">Date</th>
      <th>Changelog</th>
      <th>Download</th>
      <th>Docker Hub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="branch-col">dev</td>
      <td class="date-col">2025-03-26</td>
      <td>
        <ul>
          <li>Initial SPCC Engineering Units release</li>
          <li>MCS support</li>
          <li>Includes <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/csm-web-ui?id=advantics-csm-web-ui">Advantics Controller System Manager</a></li>
        </ul>
      </td>
      <td>-</td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.3.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.3.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.0.0.dev1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.1</td>
      <td class="date-col">2025-07-07</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.3.3</strong>
            <ul>
              <li>Graceful recovery after CAN bus disconnection</li>
              <li>Bender BenderISOCHA425HV Insulation monitor support</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.3.3</strong>
            <ul>
              <li>Plug and Charge support</li>
              <li>Add basic support for bidirectional scheduled mode</li>
              <li>Comply with CharIN guidelines for ISO15118-20 implementation</li>
              <li>Fix reset_cache issue causing node disconnection</li>
              <li>MCS: transition to waiting unplug when pistol inserted</li>
              <li>Enhanced Logging</li>
            </ul>
          </li>
          <li><strong>chademo-secc 1.5.0</strong>
            <ul><li>Enhanced Logging</li></ul>
          </li>
          <li><strong>advantics-csm 1.3.6</strong>
            <ul><li>UI/UX improvements</li></ul>
          </li>
          <li><strong>ocpp-charge-point</strong></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker Hub - <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1BKGBPBxun3zyU2DG1n7415U_D_fKvjNz">Download .tar</a> + <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.3.6</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:1.5.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.1.1</td>
      <td class="date-col">2025-07-23</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.3.4</strong>
            <ul>
              <li>Add SPCC ADM_CS_SPCC_Inputs message to generic v2 and v3</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.4.2</strong>
            <ul>
              <li>UI/UX improvements</li>
              <li>extend config interface</li>
              <li>fix bug in SW update process on management interface</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker Hub - <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=181-lwnTX-a7RBmUjBx6UnJWfxi2aslbR">Download .tar</a> + <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.3.4</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.4.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:1.5.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.1.2</td>
      <td class="date-col">2025-11-05</td>
      <td>
        <ul>
          <li><strong>advantics-csm 1.5.7 (from 1.4.2)</strong>
            <ul>
              <li>UI/UX improvements in logging page</li>
              <li>fix log export</li>
              <li>add unit annotations to config props</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker Hub - <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/release_4.1.2.tar">Download .tar</a> + <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.3.4</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.5.7</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:1.5.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.2</td>
      <td class="date-col">2025-12-23</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.4.0</strong>
            <ul>
              <li>Support for Pause/Resume functionality according to ISO15118-2 and ISO15118-20</li>
              <li>Allow restarting a new charge session when B-C-B toggle is detected (CCS)</li>
              <li>Add CCS and MCS extra info messages reporting CP, duty cycle / CE, ID</li>
              <li>Change default current ramp up/down rates</li>
              <li>Fix EV ID sending over CAN bus interface</li>
              <li>Boost-Buck interface: Force boost to always have a 200V offset over buck voltage</li>
              <li>Boost-Buck interface: Perform precharge using all the stacks</li>
              <li>Boost-Buck interface: Turn off bucks in standby</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.4.0</strong>
            <ul>
              <li>Support for Pause/Resume functionality according to ISO15118-2 and ISO15118-20</li>
              <li>MCS: Add configurable software filtering on CE and ID lines</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.6.4</strong>
            <ul>
              <li>Add the possibility to restart CSM when submitting config from the UI</li>
              <li>Toggle J1939/CAN monitoring on config change without restarting the whole app</li>
              <li>Support both extended and non-extended IDs for CAN monitoring</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker Hub - <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1ykdS71tNExKZLM468Rl9SJCZUj5mm7UP">Download .tar</a> + <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.4.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.4.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.6.4</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:1.5.1</a></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
