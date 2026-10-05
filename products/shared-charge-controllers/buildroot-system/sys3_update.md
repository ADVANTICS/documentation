# Updating the software

The controller runs two layers, updated separately:

- the **applications**, which run in Docker containers;
- the **Linux system** (System 3.x), which is flashed from a microSD card.

## Which procedure to follow

| You have | It updates | Follow |
|---|---|---|
| A release `.zip` from the **Software Releases** page | Applications, start-up scripts, `config.cfg` | [Install a release](#install-a-release) |
| A container bundle (`.tar`) sent by ADVANTICS | Application images | [Install a container bundle](#install-a-container-bundle) |
| A system `.zip` holding `THIS LEVEL IS ROOT OF SD CARD.txt` | Linux system | [Update the Linux system](#update-the-linux-system) |

## Before you start

- Pick a moment with no vehicle connected: the applications are stopped during the update, so the
  controller cannot charge.
- Note the versions installed, shown in the _Controller Status_ table of the Web UI
  [Status page](../csm/csm-web-ui.md#status-page-dashboard).
- Do not power off the controller while an update is running.

## Install a release

A release replaces every application together with its start-up scripts, and installs the default
configuration of the release over your `config.cfg`. It also deletes the application logs.

!!! note "Replace `<release>` in the commands"
    The commands below write `<release>` where the name of your release goes. Replace it with the
    actual name of the release `.zip` you downloaded, without the `.zip` extension.

1. Save your configuration: on the Web UI
   [Configuration page](../csm/csm-web-ui.md#controller-configuration-page-dashboardconfiguration),
   press **Export config**. Without the Web UI, copy the file from your computer instead:  
   `scp root@192.168.1.51:/srv/config.cfg .` (`192.168.1.49` on the EVCC).
   Export the logs as well if you still need them.
2. Copy the release `.zip` to the microSD card, then eject the card as explained in
   [Copying files on the SD card](#copying-files-on-the-sd-card).
3. Insert the card into the controller and [log in](access.md).
4. Mount the card and extract the release onto it:

    ```bash
    $ mkdir -p /mnt/sd
    $ mount -t auto /dev/mmcblk0p1 /mnt/sd
    $ unzip /mnt/sd/<release>.zip -d /mnt/sd
    ```

5. Run the update script of the extracted folder, and wait for it to return to the prompt:

    ```bash
    $ /mnt/sd/<release>/update-controller.sh
    ```

6. Power cycle the controller.
7. Put your settings back: on the Configuration page, press **Upload config file** and select the
   file saved at step 1, then restart the applications when the Web UI proposes it. Without the
   Web UI, copy the file back to `/srv/config.cfg` as explained in
   [Read-only file system](read-only.md).
8. Check the new versions in the _Controller Status_ table of the Status page.

## Install a container bundle

A container bundle is a `.tar` file holding one or several application images. It leaves the
start-up scripts, the configuration and the Linux system unchanged.

### With the Web UI

Upload the bundle from the Management page, as explained in
[Update Containers](../csm/csm-web-ui.md#update-containers). The Web UI installs it and restarts
the applications on its own.

!!! note
    The Web UI is served by the ADVANTICS CSM application, shipped since **release 2.0** on the EVCC
    and **release 4.1** on the SECC. On an older system, use the command line.

### From the command line

#### Copy the bundle with SCP

From a terminal on your computer, in the folder holding the bundle:

```bash
scp update.tar root@192.168.1.51:/tmp
```

Use `192.168.1.49` on the EVCC, or the address you gave the controller. The password is _dev-only_
unless you changed it. Then [log in](access.md) and [load the bundle](#load-the-bundle).

#### Copy the bundle with the SD card

1. Copy the bundle to the microSD card, then eject the card as explained in
   [Copying files on the SD card](#copying-files-on-the-sd-card).
2. Insert the card into the controller, [log in](access.md) and mount the card:

    ```bash
    $ mkdir -p /mnt/sd
    $ mount -t auto /dev/mmcblk0p1 /mnt/sd
    ```

The bundle is then `/mnt/sd/update.tar`. Unmount the card with `umount /mnt/sd` once the bundle is
loaded.

#### Load the bundle

The commands use `S80charger`; on the EVCC, use `S80vehicle` instead.

1. Stop the applications and clear their logs:

    ```bash
    $ /etc/init.d/S80charger stop
    $ /etc/init.d/S80charger clean
    ```

2. Load the bundle and delete the images it replaces. If you copied it with the SD card, the file
   is `/mnt/sd/update.tar` instead:

    ```bash
    $ docker load -i /tmp/update.tar
    $ docker image prune -f
    ```

3. Start the applications:

    ```bash
    $ /etc/init.d/S80charger start
    ```

## Update the Linux system

The Linux system is flashed from a microSD card, automatically at boot.

### What you need

* The charge controller to update, taken out of its casing if it has one (PEV variant)
* The microSD card provided with the controller, or another one of at least 4 GB
* A way to connect the microSD card to your computer (directly if it can, or with a SD card adapter,
or with an external card reader)
* 500 MB of (temporary) disk space

### Preparation

1. Download the ZIP archive of the system ADVANTICS provided you
1. Take the microSD card out of the charge controller
1. Connect it to your computer
1. Erase all files on it, or format it

!!! note
    There is no risk in doing this. The charge controller does not need a SD card present to boot,
    or run.

### Copying files on the SD card

1. Unzip the content of the ZIP archive on the SD card.

    !!! attention
        The ZIP archive holds a file called `THIS LEVEL IS ROOT OF SD CARD.txt`. It marks where the
        files go, in case your ZIP decompressor created an intermediate folder.

2. "Eject" the SD card properly from the computer, then take it out physically.

    !!! warning
        After a large copy, your computer may still be writing to the card in the background
        although the copy looks finished. Wait until it tells you the card can be safely removed,
        or the card may be corrupted.

        In doubt, reconnect the card and run a file system check. In case of error, repair it, or
        reformat the card and start over. On Linux, the `sync` command waits for the writes to end.

### Actual flashing of the controller

1. Insert the microSD card into the charge controller's slot
1. Power up the charge controller
1. Wait for ~3 minutes while flashing and rebooting are happening.

The update is automatic at boot, as long as the system on the SD card is newer than the system
installed on the charge controller. During the update, the system boots up once, does some
initialisation steps, then reboots again.

### Forcing a reflash, or rolling back an update

The automatic updater does nothing when the system on the SD card is not newer than the one
installed. To reflash anyway, ie. to "factory reset" to the system on the SD card or to roll back to
an older version, delete the file the updater reads the installed version from:

1. [Log in to the controller](access.md)
1. Type this command: `mount -o remount,rw /mnt/old-root`
1. Then, type this command: `rm /mnt/old-root/boot/current_version.img`
1. Then reboot, either with a power cycle, or by typing `reboot`
1. Wait ~3 minutes while flashing and rebooting are happening

!!! note
    If you can't log in to the system anymore (if for some reason it got corrupted), ask ADVANTICS
    for the procedure to follow to update from the bootloader of the Colibri module directly.

## Updater tool

The EVCC Updater tool brought EVCC systems up to release 2.0.0rc3 (2022). It does not apply to later
releases: use [Install a release](#install-a-release) instead.
