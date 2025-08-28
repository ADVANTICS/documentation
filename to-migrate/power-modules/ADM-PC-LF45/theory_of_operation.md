> [!UPDATE] {docsify-updated}
# Theory of operation

## Topology

The ADM-PC-LF45 is a 3-phase line filter and precharge with:

- 3-phase filter
- Smart precharge
- Phase loss detection

For more details on the specifications, please check the [ADM-PC-LF45 specifications](power-modules/ADM-PC-LF45/specifications.md).

![filter topology](images/Filter_topology-filter_topology.svg ':size=70%')
<figcaption style="text-align: center">ADM-PC-LF45 simplified topology</figcaption>


## Enabling sequence

The ADM-PC-LF45 module has a smart precharge and filter connection sequence, which follows this state diagram:

![filter topology](images/filter_sequence.svg ':size=50%')
<figcaption style="text-align: center">ADM-PC-LF45 simplified topology</figcaption>

To connect the module, the user just needs to set the **Close relays** bit in the **Filter_relays** message. For more information, please refer to the [ADM-PC-LF45 CAN database](power-modules/ADM-PC-LF45/can_database.md) and also to the [Quick Start](power-modules/ADM-PC-LF45/quick_start.md) section.