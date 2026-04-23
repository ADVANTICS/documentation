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
    <td class="branch-col">Release 2.2</td>
      <td class="date-col">2025-08-04</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.2.4</strong>
            <ul>
              <li>New CAN bus signal "EV_Status.HV_Preparing_Hold_Off": Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.</li>
              <li>Advantics_Generic_PEV_protocol_v2: Expand energy limits and revise signal slopes accordingly.</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.3.3</strong>
            <ul>
              <li>Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1M8wKx9gKATT6yE24uvH0dJy6aU3MLd5g">Download .tar (Release 2.2)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.2.4</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.3.3</a></li>
        </ul>
      </td>
    </tr>
    <td class="branch-col">Release 2.3</td>
      <td class="date-col">2025-09-15</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.2.5</strong>
            <ul>
              <li>New CAN bus message <a href="https://advantics.github.io/documentation/#/charge-controllers/evcc_generic/can_v2?id=evcc-mevc-diagnostic-status">EVCC_MEVC_Diagnostic_Status</a><br/> Diagnostic status of the charge controller:<br/> - Shows active faults and errors detected by the charge controller.<br/>- Status signals received from the charger over High-Level Communication (HLC).</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.3.5</strong>
            <ul>
              <li>Send HLC error codes and forward charger status signals received over High-Level Communication (HLC).</li>
              <li>Fix minor bug in ServiceDiscovery in handling extra services</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.5.4</strong>
            <ul>
              <li>Fix log exporting issue Improve logging page experience (docker socket starvation, app status in colors)</li>
              <li>Add export config file in config page</li>
              <li>Add j1939 capabilities</li>
              <li>QOL improvements for J1939 logging</li>
              <li>Fix management page for EVCC (official support of EVCC)</li>
              <li>Add error stack to monitoring page</li>
              <li>Fix UI typos and descriptions</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1h_j2vAV_YS2KRCoGGge2JCJGN-YNTATR">Download .tar (Release 2.3)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.2.5</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.3.5</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.5.4</a></li>
        </ul>
      </td>
    </tr>
    <td class="branch-col">Release 2.4</td>
      <td class="date-col">2025-12-11</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.3.0 / ccs-evcc 2.4.0</strong>
            <ul>
              <li>Add possibility of dynamic target voltage control (configurable)</li>
              <li>Report CE and ID state via new message <a href="https://advantics.github.io/documentation/#/charge-controllers/evcc_generic/can_v2?id=mcs-extra-information">MCS_Extra_Information</a> (informational only)</li>
              <li>Add software filtering capability on CE and ID lines (experimental)</li>
              <li>Allow bidirectional cycling at full SOC (configurable)</li>
              <li>Disable current deviation check against target current in range mode (dynamic mode)</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.6.3</strong>
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
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1zBtbxzA0KM8yBtF1vCWaawADOgA-oL1V">Download .tar (Release 2.4)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.3.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.4.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.6.3</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.4.1</td>
      <td class="date-col">2025-12-23</td>
      <td>
        <ul>
          <li><strong>ccs-evcc 2.4.1</strong>
            <ul>
              <li>Bug fix: checking for wrong CP state in session stop state resulting in abnormal session termination in some cases</li>
              <li>CE and ID filtering: enhanced logging</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.6.4</strong>
            <ul>
              <li>fix a minor bug</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Option 1:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>Option 2:</strong> <a href="https://drive.google.com/uc?export=download&id=1k6z6sdHi-K8_FD3yBFHoNis11xjbzsCI">Download .tar (Release 2.4.1)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=full-release-update">Update Instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.4.1</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.6.4</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.5</td>
      <td class="date-col">2026-03-13</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.4.0</strong>
            <ul>
              <li>Fixed checking DC contactors state and DC messages during emergency while AC charging</li>
              <li>Fixed inputs/outputs messages being incorrectly reset between sessions</li>
              <li>Fixed inputs message being sent with wrong values before initialization completes (startup race condition)</li>
              <li>Fixed channel reset and related miscellaneous state issues</li>
              <li>Contactors opening: raised the current-below-limit threshold to 5 A; added a configurable timeout after which contactors open unconditionally if current doesn't drop below limit</li>
              <li>Startup safety: inputs messages are now suppressed until hardware I/O initialization is fully complete</li>
              <li>Temperature: median filter is now applied to temperature sensor inputs</li>
              <li>GC performance: persistent objects are now untracked from the garbage collector to reduce GC overhead</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.5.0</strong>
            <ul>
              <li>Fixed bug where frontend did not send Closing_Communication stage to backend in EmergencyShutdownState</li>
              <li>Improved power permit handling</li>
              <li>Moved CP state reporting to the PLC reading level to eliminate wrong-state reports</li>
              <li>Fixed alarm cancelled more than once on protocol reset (cancel only once per exit)</li>
              <li>bcb_toggle_detected called from unexpected states now handled gracefully (no-op)</li>
              <li>Skip CP filtering while resuming a paused session, to correctly detect the B1→B2 transition</li>
              <li>Allow session resume only when the previous session is fully over</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.7.0</strong>
            <ul>
              <li>Fix logic while exporting logs, server would respond with error code and nothing attached</li>
              <li>Add the ability to generate sample config for every controller</li>
              <li>Fix dynamic voltage meter bar in monitoring and use kW for power metering instead of W</li>
              <li>Remove unused items from navigation side bar</li>
              <li>Minor improvements</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Dockerhub update:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>.zip update:</strong> <a href="">Download .zip (Release 2.5)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-3-does-not-requires-internet-loading-the-images-from-a-zip-file">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.4.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.5.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.0</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.6</td>
      <td class="date-col">2026-04-10</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.5.0</strong>
            <ul>
              <li>Fixed onefile mode folders not getting cleared properly on power cycle</li>
              <li>Added advanced E-stop contactor handling options for unreliable current measurements</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.6.0</strong>
            <ul>
              <li>Fixed onefile mode folders not getting cleared properly on power cycle</li>
              <li>MCS: Improved filtering on the CE line</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.7.1</strong>
            <ul>
              <li>Fix temperature config section</li>
              <li>Bring back controller type to header</li>
              <li>Add CSM version on footer</li>
              <li>Migrate from remix to react router 7</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Dockerhub update:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>.zip update:</strong> <a href="">Download .zip (Release 2.6)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-3-does-not-requires-internet-loading-the-images-from-a-zip-file">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.5.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.6.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.6.1</td>
      <td class="date-col">2026-04-14</td>
      <td>
        <ul>
          <li><strong>ccs-evcc 2.6.1</strong>
            <ul>
              <li>Fixed EVCC ID not read correctly from config file</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Dockerhub update:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>.zip update:</strong> <a href="">Download .zip (Release 2.6.1)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-3-does-not-requires-internet-loading-the-images-from-a-zip-file">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.6.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 2.7.1</td>
      <td class="date-col">2026-04-23</td>
      <td>
        <ul>
          <li><strong>pev-controller 2.6.2</strong>
            <ul>
              <li>Improved MCS sequence: wait for contactors to open at the end of ending charge phase and before setting CE state B</li>
              <li>Introduce a configurable median filter for the lock feedback</li>
              <li>Fixed reading HW variant from EEPROM</li>
              <li>Bidirectional power transfer: more adapted contactors handling</li>
              <li>Fixed race condition during AC ending charge affecting lock state check</li>
            </ul>
          </li>
          <li><strong>ccs-evcc 2.7.0</strong>
            <ul>
              <li>Improved MCS sequence: wait for contactors to open at the end of ending charge phase and before setting CE state B</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.7.2</strong>
            <ul>
              <li>Add the new config parameters</li>
              <li>Add dig_out options in the UI</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><strong>Dockerhub update:</strong> Pull from Docker hub — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-1-requires-internet-pulling-the-update-from-docker-hub">Guide</a></li>
          <li><strong>.zip update:</strong> <a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/mevc/mevc-release-2.7.1.zip">Download .zip (Release 2.7.1)</a> — <a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/ssh?id=option-3-does-not-requires-internet-loading-the-images-from-a-zip-file">Update instructions</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/pev-controller/tags">advantics/pev-controller:2.6.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-evcc/tags">advantics/ccs-evcc:2.7.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.2</a></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
