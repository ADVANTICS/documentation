> [!UPDATE] {docsify-updated}
# Update guide

## SD card update

### What you need

You will need the following parts:

* The charge controller to update, taken out of its casing if it has one (PEV variant)
* The microSD card provided with the controller, or another one of at least 4 GB
* A way to connect the microSD card to your computer (directly if it can, or with a SD card adapter,
or with an external card reader)
* 500 MB of (temporary) disk space

### Preparation

1. Download the ZIP archive of the system Advantics provided you
1. Take the microSD card out of the charge controller
1. Connect it to your computer
1. Erase all files on it, or format it

> [!NOTE]
> There are no risk in doing this. The charge controller does not even need a SD card present to boot, or run.

### Copying files on the SD card

<br/>
1. Unzip the content of the ZIP archive on the SD card
<br/>
<br/>

> [!ATTENTION]
> In the ZIP archive there is a file called "THIS LEVEL IS ROOT OF SD CARD.txt".
>
> This is to help you know exactly where to copy them in case your ZIP decompressor created an intermediate folder.

<br/>
2. "Eject" properly the SD card from the computer, and take it out physically
<br/>
<br/>

> [!WARNING]
> Because it is a lot of data copied to the SD card, the copy operation might seems to be done but
> actually in the background your OS is still flushing data to the card.
>
> Waiting for the computer to tell you the SD card can now be safely removed after ejecting it ensures
> the SD card won't become corrupted.
>
> In doubt, reconnect it to the computer and do a file system check. In case of error, you can either
> try to repair them, or reformat the SD card and start over.
>
> If you use Linux, you can type the `sync` command to be sure before removing the SD card
> physically.

### Actual flashing of the controller

1. Insert the microSD card into the charge controller's slot
1. Power up the charge controller

> [!NOTE]
> The update is automatic at boot, as long as the system on the SD card is newer than the system currently installed on the charge controller.

<br/>
3. Wait for ~3 minutes while flashing and rebooting are happening.

During the update, the system will boot up once, do some initialisation steps, then reboot again.

### Forcing a reflash, or rolling back an update

The automatic SD card updater, while convenient when updating to a newer system, will do nothing
for you in case you want to either force a reflash (ie. "Factory reseting" to the version of the
system present on the SD card) or roll back to an older version.

For this you need to delete a special file on the current system. The auto updater uses this file to
know the current version of the system. It will force a full reflash of the system if it does not
find this version file.

1. [Login to the controller](charge-controllers/sys3_user/access.md)
1. First, type this command: `mount -o remount,rw /mnt/old-root`
1. Then, type this command: `rm /mnt/old-root/boot/current_version.img`
1. Then reboot, either with a power cycle, or by typing `reboot`
1. Wait ~3 minutes while flashing and rebooting are happening

> [!NOTE]
> If you can't login to the system anymore (if for some reasons it got corrupted), ask Advantics
> for the procedure to follow to update from the bootloader of the Colibri module directly.

## Patch update

Patch updates are a way to partially update a controller, mostly for bug fixes and rapid iterative
developments. This should only be done when Advantics tells you to do so, and provide you the right
files.

### Application container patch update using SD card

This is for updating one or several of the application containers. Advantics provide you a _.tar_
file. The process is to:
<br/><br/>

1. Copy this file to the SD card
**WARNING:** As with the full system update, pay attention to correctly write all data to the SD card. See note above.
<br/><br/>

2. [Login to the controller](charge-controllers/sys3_user/access.md)

3. Stop and clean all applications
```bash
$ /etc/init.d/S80charger stop
$ /etc/init.d/S80charger clean
```
For EVCC version, uses _S80vehicle_ instead of _S80charger_.

4. Mount the SD card
```bash
$ mkdir /mnt/sd
$ mount -t auto /dev/mmcblk0p1 /mnt/sd
```

5. Apply patch update
```bash
$ docker load -i /mnt/sd/the_file.tar
$ docker image prune -f
```

6. Restart all applications
```bash
$ /etc/init.d/S80charger start
```
For EVCC version, uses _S80vehicle_ instead of _S80charger_.

7. Umount SD card
```bash
$ umount /mnt/sd
```

### Application container patch update using SCP

This is for updating one or several of the application containers. Advantics provide you a _.tar_
file. The process is to:
<br/><br/>

1. Using the Command Line (Linux, macOS, or Windows with WSL/PowerShell).

- Open a terminal (or Command Prompt / PowerShell on Windows).

- Navigate to the folder where your .tar file is located. For example: `cd /path/to/your/myupdate.tar` (Replace `/path/to/your/myupdate.tar` with the actual path to the file on your system.)

- Run the scp command to copy the file:

    `scp <filename> <username>@<ip-address>:<destination-path>`

    Replace:

    `<filename>` – with the name of the .tar file you want to copy

    `<username>` – with the login user on the remote device **(use `root`)**

    `<ip-address>` – Grab the IP address of the controller as documented in [SSH](charge-controllers/sys3_user/access.md#SSH).

    `<destination-path>` – with the target directory on the device **(example: `/root`)**

    Example with the default IP of the SECC: `scp myupdate.tar root@192.168.1.51:/root`

- Enter the password for the device when prompted. (the default is _dev-only_)

2. [Login to the controller](charge-controllers/sys3_user/access.md)

3. Stop and clean all applications
```bash
$ /etc/init.d/S80charger stop
$ /etc/init.d/S80charger clean
```
For EVCC version, uses _S80vehicle_ instead of _S80charger_.


4. Apply patch update
```bash
$ docker load -i /path/to/your/myupdate.tar
$ docker image prune -f
```

5. Restart all applications
```bash
$ /etc/init.d/S80charger start
```
For EVCC version, uses _S80vehicle_ instead of _S80charger_.


## Updater tool

For EVCC, see [EVCC Updater tool](charge-controllers/evcc_updater.md)
