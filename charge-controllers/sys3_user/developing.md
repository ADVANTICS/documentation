> [!UPDATE] {docsify-updated}
# Developing with the controller

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

> [!NOTE]
> If you would like to be able to share files using Samba protocol (aka. Windows file sharing protocol), let us know, and we might include it in a future release.

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

## Virtual CAN buses

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

## CAN bus Bitrate

The default CAN bus bitrate is 500 kbit/sec.

> [!NOTE]
> The controller should be in writeable mode before applying any modifications.

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
