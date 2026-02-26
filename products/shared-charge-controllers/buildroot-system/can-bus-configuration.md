# Virtual CAN buses

You can add virtual CAN buses with the following commands:
```bash
$ ip link add dev vcan0 type vcan
$ ip link set up vcan0
```

You can also add a configuration to the `/etc/network/interfaces` file to have it automatically
set up at boot. It would be written like so:
```
auto vcan0
iface vcan0 inet manual
pre-up /sbin/ip link add dev $IFACE type vcan
up /sbin/ip link set up $IFACE
down /sbin/ip link set down $IFACE
```

If you wish to do this in order to redirect the CAN bus used by Advantics applications to such
virtual bus, then you should also consider simply using the original CAN bus. Indeed, in Linux
SocketCAN implementation, a program can read messages sent on a real CAN bus by another program
despite coming from the same node.

# CAN bus Bitrate

The default CAN bus bitrate is 500 kbit/sec.

!!! note
    The controller should be in writeable mode before applying any modifications.


Some applications might require changing the CAN bus baud rate. You can do that by modifying the file `/etc/network/interfaces`.

Go to the CAN bus section and modify the bitrate. Save the file and reboot the controller.

In the following example we are changing the bitrate to 125 kbit/sec:

```
auto can0
iface can0 inet manual
pre-up /sbin/ip link set $IFACE type can bitrate 125000 restart-ms 50
up /sbin/ifconfig $IFACE up
down /sbin/ifconfig $IFACE down
```
