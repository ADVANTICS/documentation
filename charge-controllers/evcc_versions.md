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

</div> -->

<!-- ### Snapshots

Snapshots are made when we commit particular changes (eg. bug fix, new function) that are
"up for grab" without waiting that we do a proper major release or even an intermediate container
release.

> [!WARNING]
> These are development releases -->

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
		width: 15%;
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
			<th>Notable differences</th>
			<th>Download</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td class="branch-col">2018-09-25--001</td>
			<td class="date-col">2018-09-25</td>
			<td>ADM-CO-CUI1</td>
			<td>-</td>
		</tr>
		<tr>
			<td class="branch-col">2019-06-11--001</td>
			<td class="date-col">2019-06-11</td>
			<td><a href="https://www.dropbox.com/s/7pxdc6cvobque13/CHANGELOG-PEV--2019-06-11.txt?st=kevsljp0&amp;dl=0">Changelog</a></td>
			<td>
				<a href="https://www.dropbox.com/s/k2f2mfa7v77vrfv/advantics-charge-controller-pev-2019-06-11--001.zip?dl=1">ADM-CS-EVCC (Gen2)</a><br/>
				<a href="https://www.dropbox.com/s/byxmzy5azspqe0m/advantics-charge-controller-generic-pev-2019-06-11--001.zip?st=a6vtspzk&amp;dl=1">ADM-CO-CUI1</a>
			</td>
		</tr>
		<tr>
			<td class="branch-col">2.0.0rc1</td>
			<td class="date-col">2021-02-04</td>
			<td><a href="https://www.dropbox.com/s/gj1pk8s2xjegw09/CHANGELOG-PEV-2.0.0rc1.txt?st=ugwr816z&amp;dl=0">Changelog</a></td>
			<td><a href="https://www.dropbox.com/s/g44jyzotooxmq05/adm-cs-evcc-2.0.0rc1.zip?st=3pq3u0kp&amp;dl=1">ADM-CS-EVCC (Gen3)</a></td>
		</tr>
		<tr>
			<td class="branch-col">2.0.0rc2</td>
			<td class="date-col">2021-06-11</td>
			<td><a href="https://www.dropbox.com/s/jg4o47qyvsu7nf9/CHANGELOG-PEV-2.0.0rc2.txt?st=0vgzjw8c&amp;dl=0">Changelog</a></td>
			<td><a href="https://www.dropbox.com/s/z87kacxmtcos32o/adm-cs-evcc-2.0.0rc2.zip?st=vk9b38yq&amp;dl=1">ADM-CS-EVCC (Gen3)</a></td>
		</tr>
		<tr>
			<td class="branch-col">2.0.0rc3</td>
			<td class="date-col">2022-11-03</td>
			<td>Prefigure rc3</td>
			<td><a href="https://www.dropbox.com/s/oiw76a7lfky3ygu/pev-snapshot-stable--2022-11-02.tar?st=mxnc610w&amp;dl=1">Snapshot</a></td>
		</tr>
		<tr>
			<td class="branch-col">release 1.0</td>
			<td class="date-col">2022-11-25</td>
			<td><a href="https://www.dropbox.com/s/mc65mf3cbnhzuth/CHANGELOG-PEV-2.0.0rc3.txt?st=wyn8zfm8&amp;dl=0">Changelog</a></td>
			<td>-</td>
		</tr>
		<tr>
			<td class="branch-col"><a href="charge-controllers/evcc_bidirectional.md">Bidirectional dev</a></td>
			<td class="date-col">2022-11-17</td>
			<td>ISO 15118-20<br/>Generic CAN interface v2</td>
			<td><a href="https://www.dropbox.com/s/vbex2k6u9mszfut/pev-bidir--2022-11-17.tar?st=mkffbqdx&amp;dl=1">Snapshot</a></td>
		</tr>
		<tr>
			<td class="branch-col"><a href="charge-controllers/evcc_bidirectional.md">Release 2024-10-15</a></td>
			<td class="date-col">2024-10-15</td>
			<td>ISO15118-20 BPT: Use CAN message to dynamically update current limits</td>
			<td><a href="https://drive.google.com/uc?export=download&amp;id=1c0XZHXs2LfjTYAYSp9HNQ0ugLRP0Qmlb">pev-2024-10-15.tar</a></td>
		</tr>
		<tr>
			<td class="branch-col">release 2.0</td>
			<td class="date-col">2025-07-07</td>
			<td>
				New Application:<br/>
				- advantics-csm: Advantics CSM, short for Advantics Controller System Manager, handles all system-level operations.<br/>
				It provides a web interface for monitoring and configuring the system, minimizing the need for manual config file edits and command-line interactions.<br/>
				Users can access logs, manage applications, and perform system updates directly through the interface (<a href="https://advantics.github.io/documentation/#/charge-controllers/advantics_os/csm-web-ui">CSM Web UI</a>).<br/><br/>
				pev-controller 2.2.2:<br/>
				- fix for re-entering emergency state when no_inlet_lock and contactors open CAN message not fast enough<br/>
				ccs-evcc 2.3.2:<br/>
				- Plug and Charge support<br/>
				- Fix calling GC by reset_cache causing nodes disconnection (which also asserts interlock).
			</td>
			<td>
				Download link: <a href="https://drive.google.com/uc?export=download&amp;id=1If2EobawN2vKWnXWWLHdxtfgXnbMNKB7">pev-release-2.0.zip</a><br/>
				Update instructions: (<a href="charge-controllers/sys3_update.md#full-release-update">Full release update</a>)
			</td>
		</tr>
		<tr>
			<td class="branch-col">release 2.1</td>
			<td class="date-col">2025-07-23</td>
			<td>
				pev-controller 2.2.3:<br/>
				- fix PEV temperature: add support for temperature monitoring<br/>
				- allow contactor feedback via CAN bus while contactor control is done via IOs<br/>
				- allow LEDs control via CAN bus interface<br/>
				advantics-csm 1.4.2:<br/>
				- extend config interface<br/>
				- fix bug in SW update process on management interface.
			</td>
			<td>
				Download link: <a href="https://drive.google.com/uc?export=download&amp;id=136dllcmk9AMYky_Nao0IaCV1NHmFTTpm">evcc-23-07-2025.zip</a><br/>
				Update instructions: (<a href="charge-controllers/sys3_update.md#full-release-update">Full release update</a>)
			</td>
		</tr>
		<tr>
			<td class="branch-col">release 2.2</td>
			<td class="date-col">2025-08-04</td>
			<td>
				pev-controller 2.2.4:<br/>
				- New CAN bus signal <a href="charge-controllers/evcc_generic/can_v2.md#EV_Status-HV_Preparing_Hold_Off">HV_Preparing_Hold_Off</a>:<br/>
				Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.<br/>
				- Advantics_Generic_PEV_protocol_v2: Expand energy limits and revise signal slopes accordingly.<br/>
				ccs-evcc 2.3.3:<br/>
				- Allow the vehicle to delay the transition to powered states (starting from the insulation test) until the HV system is ready.
			</td>
			<td>
				Download link: <a href="https://drive.google.com/uc?export=download&amp;id=1eYflFXaEiRZVk_2vr8iMdnCfZEByECmK">evcc-04-08-2025.zip</a><br/>
				Update instructions: (<a href="charge-controllers/sys3_update.md#full-release-update">Full release update</a>)
			</td>
		</tr>
		<tr>
			<td class="branch-col">release 2.3</td>
			<td class="date-col">2025-09-15</td>
			<td>
				pev-controller 2.2.5:<br/>
				New CAN bus message <a href="charge-controllers/evcc_generic/can_v2.md#evcc-mevc-diagnostic-status">EVCC_MEVC_Diagnostic_Status</a>: Diagnostic status of the charge controller:<br/>
				- Shows active faults and errors detected by the charge controller.<br/>
				- Status signals received from the charger over High-Level Communication (HLC).<br/>
				ccs-evcc 2.3.5:<br/>
				- Send HLC error codes and forward charger status signals received over High-Level Communication (HLC).<br/>
				- Fix minor bug in ServiceDiscovery in handling extra services.<br/>
				advantics-csm 1.5.4:<br/>
				- Fix log exporting issue; improve logging page experience (docker socket starvation, app status in colors).<br/>
				- Add export config file in config page.<br/>
				- Add J1939 capabilities; QOL improvements for J1939 logging.<br/>
				- Fix management page for EVCC (official support of EVCC).<br/>
				- Add error stack to monitoring page.<br/>
				- Fix UI typos and descriptions.
			</td>
			<td>
				Download link: <a href="https://drive.google.com/uc?export=download&amp;id=1kNEDyp6DiZuyDF6GrnHkSmdSWe2g0shR">evcc-15-09-2025.zip</a><br/>
				Update instructions: (<a href="charge-controllers/sys3_update.md#full-release-update">Full release update</a>)
			</td>
		</tr>
        <tr>
			<td class="branch-col">release 2.4</td>
			<td class="date-col">2025-12-11</td>
			<td>
                pev-controller 2.3.0:<br/>
                - Add possibility of dynamic target voltage control (configurable)<br/>
                - Report CE and ID state via new message “MCS_Extra_Information” (informational only)<br/>
                - Allow bidirectional cycling at full SOC (configurable)<br/>
                - Disable current deviation check against target current in range mode (dynamic mode)<br/>
                ccs-evcc 2.4.0:<br/>
                - Possibility to disable AC charging (configurable) (only relevant for CCS)<br/>
                - Pause and resume session according to ISO15118-2 and ISO15118-20<br/>
                advantics-csm 1.6.3<br/>
                - Add the possibility to restart CSM when submitting config from the UI<br/>
                - Toggle J1939/CAN monitoring on config change without restarting the whole app<br/>
                - Support both extendend and non-extended IDs for CAN monitoring
			</td>
			<td>
				Download link: <a href="https://drive.google.com/uc?export=download&id=1YJNsdh0bMZ7Wx3zomCCXhH29cs_JgaRN">evcc-11-12-2025.zip</a><br/>
				Update instructions: (<a href="charge-controllers/sys3_update.md#full-release-update">Full release update</a>)
			</td>
		</tr>
	</tbody>
</table>

