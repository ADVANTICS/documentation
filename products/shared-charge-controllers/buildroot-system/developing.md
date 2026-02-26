# Developing with the controller

# Platforms

## Hardware

<span>iMX7 systems (ADM-CS-SECC, ADM-CS-EVCC)</span>

| * | * |
|---|--- |
| **Compute module** | Toradex Colibri iMX7 Dual 1GB |
| **Processor** | NXP i.MX 7 |
| **Cores** | 2 * ARM Cortex-A7 + 1 * ARM Cortex-M4F |
| **Clock** | 1 GHz (A7) + 200 MHz (M4) |
| **Instruction sets** | armv7l + half thumb fastmult vfp edsp thumbee neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm |
| **RAM** | 1 GB DDR3 |
| **Flash** | 4 GB eMMC |

<br/>

## Software

| * | * |
|---|--- |
| **Kernel** | Linux LTS branch (5.4 currently), iMX6: Vanilla + ADC patch, iMX7: Toradex + RS485 patch |
| **System** | Advantics 3.x branch, based on Buildroot 2020.11.1 |
| **Container** | Docker CE 19.03 |
| **Python** | 3.12 (system), 3.12 (container) |


## Networking

You can reconfigure networking by editing the file `/etc/network/interfaces`. The syntax of this
file is similar to the Debian's one, which is documented [here](https://wiki.debian.org/NetworkConfiguration).
You are concerned by the `eth0` interface for the ethernet/RJ45 network connector on the controller.

## SD card access

One way of taking files back and forth between a development computer and the controller is to use
the microSD card as a "shuttle". However, that is pretty inconvenient in the long run...

You can plug the SD card while the system is running. Once plugged, do:
```bash
$ mkdir /mnt/sd
$ mount -t auto /dev/mmcblk0p1 /mnt/sd
```
And your files will be accessible in `/mnt/sd`.

To umount the SD card before unplugging it, do:
```bash
$ umount /mnt/sd
$ sync
```
The last `sync` command is to be sure all data have been really written to the SD card before taking it
out.

## Sharing files over network

!!! note
    If you would like to be able to share files using Samba protocol (aka. Windows file sharing protocol), let us know, and we might include it in a future release.


### NFS

NFS is a file sharing protocol quite native for Linux systems. If you already have an NFS server available on your local network, do:
```bash
$ modprobe nfsv4
$ mount -t nfs4 -o port=<SERVER_PORT>,proto=tcp,nolock <SERVER_IP>:/ /mnt/nfs
```
Replace `<SERVER_PORT>` by your server port (usually 2049), and <SERVER_IP> by the address of the server reachable by the controller on its network. Customize options and export path as you need to as well.

If you don't have a NFS server already, but you do have a Linux computer with Docker installed, Advantics can provide you a Dockerfile and a few scripts to easily run a NFS server container.

## Running a custom application at boot

The init system of the controller is based on a very simple and classic approach, well known in the
Linux world. Start and stop scripts are all located in `/etc/init.d` folder. Their name defines their
start and stop order, and must start with `SXX`,  where _XX_ is a number setting the order.
There is no runlevel.

If you wish to add a script to start a custom application, it should have _XX_ >= 80. Knowing that
normal controller applications are actually started by `S80charger` or `S80vehicle`. So, if your
application needs to run after normal controller applications, then _XX_ should be strictly above 80.

Your script should take one argument, a string, which contains either `start` or `stop`, and
implement the corresponding action. Your script should also execute your application in daemon form.
That is, the process must detach from its parent calling process. For simplicity, you can also use
`start-stop-daemon` tool to achieve that.

<figcaption>Template of a start-stop script</figcaption>

```bash
#!/bin/sh

DESC="YourApplication"
NAME=yourapp # Name used for extra files
EXECUTABLE=yourapp # Name of the executable alone (no path, no options)
YOURAPP_OPTS=  # Options for your executable
DAEMON=/usr/bin/$EXECUTABLE # Full path toward the executable

YOURAPP_PIDFILE=/var/run/$EXECUTABLE.pid # Will contain the PID of your running program
YOURAPP_LOGFILE=/var/log/$EXECUTABLE.log # Will contain the outputs of your program

# This is to load a config file and add extra bash variables for the rest of the script
if [ -r /etc/default/$BASE ] # Only if it exists, otherwise it is not loaded
then
  . /etc/default/$BASE
fi

test -x $DAEMON || exit 1

start() {
    if [ "$(id -u)" != '0' ]; then
        echo "$DESC must be run as root"
        exit 1
    fi

    echo -n "Starting $DESC: "
    start-stop-daemon --quiet -S \
        --background --exec "$DAEMON" \
        --pidfile "$YOURAPP_PIDFILE" --make-pidfile \
        -- $YOURAPP_OPTS >> "$YOURAPP_LOGFILE" 2>&1

    [ $? = 0 ] && echo "OK" || echo "FAIL"
}

stop() {
    if [ "$(id -u)" != '0' ]; then
        echo "$DESC must be run as root"
        exit 1
    fi

    if [ -f "$YOURAPP_PIDFILE" ]; then
        echo -n "Stopping $DESC: "
        start-stop-daemon --quiet -K --pidfile "$YOURAPP_PIDFILE"
        [ $? = 0 ] && echo "OK" || echo "FAIL"
    else
        echo "$DESC already stopped - file $YOURAPP_PIDFILE not found."
    fi
}

case "$1" in
  start)
    start
    ;;

  stop)
    stop
    ;;

  *)
    echo "Usage: $0 {start|stop}" >&2
    exit 1
    ;;

esac

exit 0
```

## Developing in Python

If you want to write your program running on the controller in Python you have three options:

* Use the Python installed on the system itself.
* Use the Python available in the container `advantics/python:run`.
* Use your own Python container image.

`advantics/python:run` usually contains more recent versions of installed packages.

In any case, because it's Python running on full-featured Linux system, there are pretty much no
difference between a program running on a PC, and a program running on the controller. Therefore,
you could conveniently develop most of your program on a PC and only do final test and integration
on the controller. This is how we do it.

Performance wise, for sure it is not up-to-speed with assembly :). But we found it sufficient for
our own applications (some of which are tightly performance constrained, having to respond to
complex CCS EXI-encoded requests in under 25 ms for instance).

If you use the language correctly you will get decent performances (like for any language). At worst,
you can always optimize part of your code with things like Cython or Nuitka (although it makes for
more complicated compilation steps as it has to target the ARMv7 instruction set).

### Installed packages

Here are the major packages installed on the host system and in container image `advantics/python:run`:

* Python 3.9
* pip
* python-can
* cantools
* click
* pyzmq
* transitions

### Installing other packages

`pip` is available on both the host system as well as inside the `advantics/python:run` container. Therefore, it can be as simple as executing a `pip install <PACKAGE_NAME>` command on the host system (don't forget to switch your system to [writable mode](charge-controllers/sys3_user/read-only.md) beforehand) or in an instantiated container, or as a `RUN` command of a Dockerfile.

### Accessing a CAN bus

You can use the python-can package, which handles using SocketCAN directly. Here is a simple example:

```python
import click
import can
import struct


@click.command()
@click.option('--can-if', default='can0', help='CAN Interface name')
def main(can_if):
    '''Simple example, receive messages, count them and send a CAN message
       on ID 0x123 with the counter value in 8-bytes big-endian integer'''

    can_bus = can.interface.Bus(can_if, bustype='socketcan')
    counter = 0

    while True:
        # Receive
        msg_r = can_bus.recv()
        counter += 1
        print('>>>', counter, msg_r)

        # Send
        data = struct.pack('>Q', counter)
        msg_s = can.Message(arbitration_id=0x123, data=data, extended_id=False)
        can_bus.send(msg_s)
```

!!! tip
    We would strongly advise you to look at [cantools](https://pypi.org/project/cantools/) as well.

>
> It handles encoding and decoding of CAN messages according to a CAN database in Kayak or DBC format.
> As such, your chances of having bugs in your CAN implementation are severely reduced.
