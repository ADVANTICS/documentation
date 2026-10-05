---
hide:
  - toc
---

# SPCC Versions

## Hardware

Currently supported hardware are for `ADM-CS-SPCC`.

## Software

### Major releases

Major releases are result of months of development, consolidation, extensive testing and user feedbacks.
They are slow paced because the release process is substantial.


To install a release, follow the [Updating the Software](advos-yocto-system/updating.md) page: [Install a release](advos-yocto-system/updating.md#install-a-release) for a `.zip`, [Install a container bundle](advos-yocto-system/updating.md#install-a-container-bundle) for a `.tar`, or [Pull from Docker Hub](advos-yocto-system/updating.md#pull-from-docker-hub) for the images listed in the _Docker Hub_ column.

<div class="custom-table-wrapper">
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
      <td class="branch-col">Release 4.7.0</td>
      <td class="date-col">2026-09-24</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.9.0</strong>
            <ul>
              <li>Charger error codes, charge-limit status and diagnostics published on the generic EVSE CAN interface (v2 and v3)</li>
              <li>Insulation monitor reading and status published on the generic EVSE CAN interface</li>
              <li>Application version of every container reported on the generic EVSE CAN interface</li>
              <li>Support for the ADVANTICS AC01+DC01 power module</li>
              <li>New options: <code>current_ramp_enabled</code>, <code>clear_error_codes_on_idle</code>, <code>skip_voltage_lowering_after_insulation_test</code>, <code>always_use_dynamic_max_current</code></li>
              <li>Charger voltage and current limits enforced in every control mode, charge parameters refreshed throughout the session</li>
              <li>"Charger powered" now follows the output contactor drive status input, and an abnormal session end is reported as a rushed stop</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.9.0</strong>
            <ul>
              <li>A session setup the vehicle never completes is abandoned after a configurable timeout and reported with a dedicated error code (<code>communication_setup_timeout</code>, 60 s by default)</li>
              <li>MCS: the start of high-level communication can be delayed by up to 10 s (<code>communication_start_delay_s</code>)</li>
              <li>Much richer diagnostics when the charger cannot find the vehicle on the network</li>
              <li>Fixes: starting a session right after an aborted one, unexpected connector-state aborts on fast vehicles, control pilot state reporting, disabling AC charging from the configuration, a closed S3 forcing the current limit to zero, pairing on chargers with several connectors</li>
              <li>Removed the control pilot noise-filtering bypass; <code>invert_pp_b1</code> is deprecated and ignored</li>
            </ul>
          </li>
          <li><strong>slac-evse 2.4.0</strong>
            <ul>
              <li>Reports its application version on the internal bus</li>
              <li>Fix: after a few hundred pairing attempts the service could run out of system resources and restart</li>
              <li>Fix: a pairing timeout could take effect after the message that cancelled it</li>
              <li>Fix: clean exit at start-up when no CCS connector is configured</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.9.0</strong>
            <ul>
              <li>TLS certificate support for the web interface, uploaded or self-signed from the Management page</li>
              <li>Application versions read from the application metadata instead of the Docker image label</li>
              <li>Fixes: navigation sidebar configuration items, per-controller documentation links</li>
            </ul>
          </li>
          <li><strong>chademo-secc 2.0.0</strong>
            <ul>
              <li>CHAdeMO application enabled on the SPCC platform</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/spcc-release-4.7.0.zip">Download .zip</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.9.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.9.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.4.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/chademo-secc/tags">advantics/chademo-secc:2.0.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:2.1.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.9.0</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.5.1</td>
      <td class="date-col">2026-06-05</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.7.1</strong>
            <ul>
              <li>Fix sending CCS/MCS extra info duplicate CAN messages</li>
              <li>Fix CCS PP line initialization</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/spcc-release-4.5.1.zip">Download .zip</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.7.1</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.7.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.3</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.5.0</td>
      <td class="date-col">2026-05-19</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.7.0</strong>
            <ul>
              <li>LED control via CAN bus</li>
              <li>fix: new controllers config parameter retrieval on Bender IMD interface</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.7.0</strong>
            <ul>
              <li>fix: TLS certificate loader</li>
              <li>Add a config option to force EVSE_Ready status in DC_EVSEStatus when charge parameter discovery processing is finished on DIN and ISO-2</li>
            </ul>
          </li>
          <li><strong>advantics-csm 1.7.3</strong>
            <ul>
              <li>Add application version on UI</li>
              <li>Minor bug fixes</li>
            </ul>
          </li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/spcc-release-4.5.0.zip">Download .zip</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.7.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.7.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.3</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.4</td>
      <td class="date-col">2026-04-10</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.6.1</strong>
            <ul>
              <li>Fixed onefile mode folders not getting cleared properly on power cycle</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.6.0</strong>
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
          <li><a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/spcc-release-4.4.zip">Download .zip</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.6.1</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.6.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">Release 4.3</td>
      <td class="date-col">2026-03-13</td>
      <td>
        <ul>
          <li><strong>evse-controller 3.6.0</strong>
            <ul>
              <li>Inputs messages are now suppressed until hardware I/O initialization is fully complete (startup safety)</li>
              <li>Add CAN message ADM_CS_SPCC_Outputs to control the ADM-CS-SPCC outputs</li>
              <li>Temperature median filter window is now configurable (SECC/SPCC)</li>
              <li>Fixed encoding of negative target_voltage values sent by the car</li>
            </ul>
          </li>
          <li><strong>ccs-secc 2.5.0</strong>
            <ul>
              <li>Ignore spurious CE change to B0 when Ss3 is still closed (erroneous measurement during B→C transition)</li>
              <li>Disabled the CP oscillator at end of session</li>
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
          <li><a href="">Download .zip</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.6.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.5.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.7.0</a></li>
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
          <li><a href="https://drive.google.com/uc?export=download&id=1ykdS71tNExKZLM468Rl9SJCZUj5mm7UP">Download .tar</a></li>
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
          <li><a href="https://pub-ec884f5e1c6b4942867b3ac199d79823.r2.dev/spcc/release_4.1.2.tar">Download .tar</a></li>
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
          <li><a href="https://drive.google.com/uc?export=download&id=181-lwnTX-a7RBmUjBx6UnJWfxi2aslbR">Download .tar</a></li>
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
          <li><a href="https://drive.google.com/uc?export=download&id=1BKGBPBxun3zyU2DG1n7415U_D_fKvjNz">Download .tar</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><a href="https://hub.docker.com/r/advantics/evse-controller/tags">advantics/evse-controller:3.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ccs-secc/tags">advantics/ccs-secc:2.3.3</a></li>
          <li><a href="https://hub.docker.com/r/advantics/slac-evse/tags">advantics/slac-evse:2.3.2</a></li>
          <li><a href="https://hub.docker.com/r/advantics/chademo-secc/tags">advantics/chademo-secc:1.5.0</a></li>
          <li><a href="https://hub.docker.com/r/advantics/advantics-csm/tags">advantics/advantics-csm:1.3.6</a></li>
          <li><a href="https://hub.docker.com/r/advantics/ocpp-charge-point/tags">advantics/ocpp-charge-point:1.5.1</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="branch-col">dev</td>
      <td class="date-col">2025-03-26</td>
      <td>
        <ul>
          <li>Initial SPCC Engineering Units release</li>
          <li>MCS support</li>
          <li>Includes <a href="csm/csm-web-ui.html#advantics-csm-web-ui">Advantics Controller System Manager</a></li>
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
</tbody>
</table>
</div>