# SPCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-SPCC`.

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.

<style>
  .custom-table-wrapper {
    width: 100%;
    /* no horizontal slider; card layout doesn’t need it */
    overflow-x: hidden;
  }

  /* ===== Card layout (always) ===== */

  /* Hide header row (labels are rendered per-cell via ::before) */
  table.custom-table thead {
    display: none;
  }

  /* Break the table into block-level cards */
  table.custom-table,
  table.custom-table tbody,
  table.custom-table tr,
  table.custom-table td {
    display: block;
    width: 100%;
  }

  table.custom-table {
    border-collapse: collapse;
    font-size: 0.95rem;
    line-height: 1.4;
  }

  /* Each row becomes a "card" */
  table.custom-table tr {
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    margin: 0 0 12px 0;
    background: transparent;
  }

  /* Each cell shows: label | content */
  table.custom-table td {
    border: 0;
    border-bottom: 1px solid #eee;
    padding: 10px 12px;

    display: grid;
    grid-template-columns: minmax(90px, 140px) 1fr;
    gap: 12px;
    align-items: start;

    white-space: normal;
    overflow-wrap: anywhere;
    word-break: normal;
  }

  table.custom-table td:last-child {
    border-bottom: 0;
  }

  table.custom-table td::before {
    font-weight: 600;
    color: #555;
    content: "";
  }

  table.custom-table td:nth-of-type(1)::before { content: "Branch"; }
  table.custom-table td:nth-of-type(2)::before { content: "Date"; }
  table.custom-table td:nth-of-type(3)::before { content: "Changelog"; }
  table.custom-table td:nth-of-type(4)::before { content: "Download"; }
  table.custom-table td:nth-of-type(5)::before { content: "Docker Hub"; }

  table.custom-table ul {
    margin: 0;
    padding-left: 18px;
  }

  table.custom-table a {
    overflow-wrap: anywhere;
    word-break: break-word;
  }

  /* Very narrow screens: stack label above value */
  @media (max-width: 520px) {
    table.custom-table td {
      grid-template-columns: 1fr;
      gap: 6px;
    }
    table.custom-table td::before {
      color: #666;
    }
  }
</style>

<div class="custom-table-wrapper">
<table class="custom-table">
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
          <li><a href="https://hub.docker.com/r/advantics/chademo-secc:1.5.0">advantics/chademo-secc:1.5.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.0.0.dev1</a></li>
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
</div>