> [!UPDATE] {docsify-updated}
# MEVC Versions

## Hardware

Currently supported hardware are for `ADM-CS-MEVC`.
## Software

### Major releases

<!-- | Branch | Date | Changelog | Download | Docker Hub |
|--------|------|-----------|----------|-------------|
| dev    | 2025-03-26| <ul><li>Initial MEVC Engineering Units release</li><li>MCS support</li><li>Includes [Advantics Controller System Manager](charge-controllers-workspace/Applications/documentation/charge-controllers/advantics_os/csm-web-ui.md)</li></ul> | - | <ul><li>[advantics/pev-controller:2.2.0](https://hub.docker.com/r/advantics/pev-controller/tags)</li><li>[advantics/ccs-evcc:2.3.0](https://hub.docker.com/r/advantics/ccs-evcc/tags)</li><li>[advantics/advantics-csm:1.0.0.dev1](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> |
| Release 2.0    | 2025-07-07| <ul><li><strong>pev-controller 2.2.2</strong><ul><li>Fix for re-entering emergency state when no inlet lock and contactors open CAN message is not fast enough</li><li>ADM-CS-MEVC-PB01-R0B support</li></ul></li><li><strong>ccs-evcc 2.3.2</strong><ul><li>Fix reset_cache causing nodes disconnection</li><li>ADM-CS-MEVC-PB01-R0B support</li><li>Enhanced Logging</li></ul><li><strong>advantics-csm 1.3.6</strong><ul><li>UI/UX improvements</li><li>ADM-CS-MEVC-PB01-R0B support</li></ul></li></ul>  | <li>**Option 1**: Pull from Docker hub following this [Guide](charge-controllers/advantics_os/ssh.md#option-1-requires-internet-pulling-the-update-from-docker-hub)</li><li>**Option 2**: Download .tar here: [Release 2.0](https://drive.google.com/uc?export=download&id=1UbFszaAsMXQeq533L6Q20KhT6ewDkbOw) Update instructions using .tar file here: [Full release update](charge-controllers/advantics_os/ssh.md#full-release-update)</li> | <ul><li>[advantics/pev-controller:2.2.2](https://hub.docker.com/r/advantics/pev-controller/tags)</li><li>[advantics/ccs-evcc:2.3.2](https://hub.docker.com/r/advantics/ccs-evcc/tags)</li><li>[advantics/advantics-csm:1.3.6](https://hub.docker.com/r/advantics/advantics-csm/tags)</li></ul> | -->

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
          <li>Initial MEVC Engineering Units release</li>
          <li>MCS support</li>
          <li>Includes <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/csm-web-ui?id=advantics-csm-web-ui">Advantics Controller System Manager</a></li>
        </ul>
      </td>
      <td>-</td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.2.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.3.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.0.0.dev1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.0</td>
      <td class="date-col">2025-07-07</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.2.2</strong>
            <ul>
              <li>Fix for re-entering emergency state when no inlet lock and contactors open CAN message is not fast enough</li>
              <li>ADM-CS-MEVC-PB01-R0B support</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.3.2</strong>
            <ul>
              <li>Fix reset_cache causing nodes disconnection</li>
              <li>ADM-CS-MEVC-PB01-R0B support</li>
              <li>Enhanced Logging</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.3.6</strong>
            <ul>
              <li>UI/UX improvements</li>
              <li>ADM-CS-MEVC-PB01-R0B support</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1UbFszaAsMXQeq533L6Q20KhT6ewDkbOw">Download .tar (Release 2.0)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.2.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.3.6</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.1</td>
      <td class="date-col">2025-07-23</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.2.3</strong>
            <ul>
              <li>fix PEV temperature: add support for temperature monitoring</li>
              <li>allow contactor feedback via CAN bus while contactor control is done via IOs</li>
              <li>allow LED control via CAN bus interface</li>
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
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1shXzEAFT5bmT5w6k3TfWvUC5RuYSX3C4">Download .tar (Release 2.1)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.2.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.4.2</a></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
