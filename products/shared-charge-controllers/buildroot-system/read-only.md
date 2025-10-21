# Read-only file system

In order to ensure the system will not get corrupted by a sudden loss of power, it is running in a non-usual way:

* The base system in the flash memory is only accessed in read-only mode.
* There is a writable overlay in RAM running on top of it.

Anything written to the file system is only written in RAM. It is lost as soon as the power is removed from the controller, or when the controller is rebooted.

When the system boots-up, it switches to this RO+RW[RAM] mode as the first thing right after the Linux kernel is loaded.

You can temporarily access the base file system in writable mode by doing this:
```bash
$ mount -o remount,rw /mnt/old-root
```
And then do your permanent modifications directly in `/mnt/old-root`. Be sure to properly stop the
system with `halt` or `reboot` afterward.

You can also switch the system to permanent writable mode by doing:
```bash
$ mount -o remount,rw /mnt/old-root
$ cd /mnt/old-root/etc
$ cp inittab.no-overlay inittab
$ reboot
```

And if you want to revert to read-only mode (once rebooted in writable mode):
```bash
$ cd /etc
$ cp inittab.overlay inittab
$ reboot
```

## Read-only exception: `/var/lib/docker`

`/var/lib/docker` is a separate partition that is not switched to read-only mode. The reason begin
Docker requires some form of persistency for its meta-data.

The risks of getting the partition corrupted by a sudden loss of power are quite low though:

* Ext4 filesystem is pretty resilient, journalized, and often enough auto-repairable.
* The important part, Docker container images, are provisioned once and not subject to modifications.
* Even if Docker container instances get corrupted, they can be clean-up and recreated from
container images automatically (that is actually how the start-up script does).
* Logs (text outputs and tcpdumps) are stored on this partition. It is not a big deal to have some of
them getting corrupted.
