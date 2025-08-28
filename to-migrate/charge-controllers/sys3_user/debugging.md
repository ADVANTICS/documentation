> [!UPDATE] {docsify-updated}
# Debugging

## Application logs

Please, refer to [EVSE applications control](charge-controllers/sys3_user/applications.md#individual-control) or
[PEV applications control](charge-controllers/sys3_user/applications.md#individual-control-1) to learn how to access text logs of each application.

These might be useful to understand where a blocking point can be. You may also find clues to know
if the problem comes from your side, Advantics side, or the vehicle/charger side.

## CAN buses

Some CAN tools are already installed on the system. Here are a few examples.

<br/>
<div class="compact-table">
<span>Available CAN interfaces</span>

| *CAN_IF* | Decription
| --- | ---
| can0 | Power modules CAN bus
| can1 | CHAdeMO CAN bus
| vcanX | Virtual internal CAN buses. Not activated by default (see [Virtual CAN buses](charge-controllers/sys3_user/developing.md#virtual-can-buses)).

</div>

On Linux, CAN bus interfaces are mapped as network interfaces. You can list all active network
interfaces with `ifconfig`.

<figcaption>Send data on a CAN bus</figcaption>

```bash
$ cansend <CAN_IF> <ID>#<DATA>
```

_ID_ must either be 3 (SFF) or 8 (EFF) hex chars. _DATA_ must be a multiple of 2 hex chars, or
none for empty frame, or _R_ for remote request.

<figcaption>View raw CAN messages with absolute time (CTRL+C to exit)</figcaption>

```bash
$ candump -t a <CAN_IF>
```
<br/>
<figcaption>Filter-in by IDs with mask (`<received_can_id> & mask == can_id & mask`)</figcaption>

```bash
$ candump -t a <CAN_IF>,<can_id>:<can_mask>
```
<br/>
<figcaption>Filter-out by IDs with mask (`<received_can_id> & mask != can_id & mask`)</figcaption>

```bash
$ candump -t a <CAN_IF>,<can_id>~<can_mask>
```
<br/>
<figcaption>Bridge from one CAN bus to another</figcaption>

```bash
$ candump -b <CAN_IF_to> <CAN_IF_from>
```
<br/>
<figcaption>Export CAN dump as you see it to text file</figcaption>

```bash
$ candump -t a <CAN_IF> > a_file.txt
```
<br/>
<figcaption>Export CAN dump in special log format usable by other tools</figcaption>

```bash
$ candump -l <CAN_IF>
```
<br/>
<figcaption>Replay logged CAN dump on the same CAN interface</figcaption>

```bash
$ canplayer -I <LOG_FILE>
```
<br/>

See `candump -h` and `canplayer -h` for more information about their parameters.

> [!TIP]
> You may also install [cantools](https://pypi.org/project/cantools/) to decode CAN frames using a CAN DB file (in either DBC or Kayak format):
> ```bash
> $ candump <CAN_IF> | cantools decode <CAN_DB_FILE>
> ```
>
> You may replace the _candump_ command with a previously exported dump that you pipe to cantools with `cat`:
> ```bash
> $ cat a_file.txt | cantools decode <CAN_DB_FILE>
> ```

## CCS PLC network packet capture

You can capture network packets on the PLC line into a _.pcap_ file like so:
```bash
$ tcpdump -i eth1 -w dump.pcap
```

However, the controller system runs such a packet capture by default already. Dump files are
stored in `/var/lib/docker/dumps`.

You can analyze these packet captures yourself with PCAP compatible software, such as `wireshark`.
However, by default, there is no decoding of the SLAC and CCS EXI packets. And they are pretty much
unreadable by a human... Advantics has a private software to decode, reconstruct and analyze CCS
communications.
