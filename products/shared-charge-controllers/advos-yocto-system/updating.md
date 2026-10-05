# Updating the software

The controller runs two layers, updated separately:

- the **applications**, which run in Docker containers managed with
  [Docker Compose](https://docs.docker.com/compose/);
- the **Linux system**, AdvOS, versioned with [ostree](https://github.com/ostreedev/ostree).

## Which procedure to follow

| You have | It updates | Follow |
|---|---|---|
| A release `.zip` from the **Software Releases** page | Applications | [Install a release](#install-a-release) |
| A container bundle (`.tar`) sent by ADVANTICS | Applications in the bundle | [Install a container bundle](#install-a-container-bundle) |
| A controller connected to the Internet | Applications, from Docker Hub | [Pull from Docker Hub](#pull-from-docker-hub) |
| A new AdvOS version | Linux system | [Update the Linux system](#update-the-linux-system) |

## Before you start

- Pick a moment with no vehicle connected: the applications are stopped during the update, so the
  controller cannot charge. Installing a release takes about 10 minutes.
- Note the versions installed, shown in the _Controller Status_ table of the Web UI
  [Status page](../csm/csm-web-ui.md#status-page-dashboard).
- The release script and the commands on this page work on the `default` Docker Compose profile. If
  your controller uses another profile, or a modified default one, ask ADVANTICS before updating.
- Do not power off the controller while an update is running.

## Install a release

!!! note "Replace `<release>` and `<hostname>` in the commands"
    The commands below write `<release>` where the name of your release goes. Replace it with the
    actual name of the release `.zip` you downloaded, without the `.zip` extension. Replace
    `<hostname>` with the hostname of your controller, as found in
    [Connecting to the controller](connecting.md).

1. Extract the release `.zip` on your computer. It holds one folder with the same name as the
   `.zip`. Do not extract the `.tar` or `.tar.gz` archive inside it: the controller reads it as
   it is.
2. Copy that folder to the home folder of the controller, as explained in
   [Copying files to the controller using SCP](ssh.md#copying-files-to-the-controller-using-scp):

    ```bash
    scp -r <release> advantics@<hostname>:/home/advantics/
    ```

    Do not copy it to `/tmp`: it is a small memory-based area, too small for a release.

3. [Log in to the controller](ssh.md#ssh-access) and run the update script:

    ```bash
    cd /home/advantics/<release>
    chmod +x update-controller.sh
    ./update-controller.sh
    ```

4. Wait for the script to print `=> All applications updated and old versions cleared.` It
   restarts the applications itself, so no power cycle is needed.
5. Check the new versions in the _Controller Status_ table of the Status page, or with `docker ps`.

!!! tip "If the script stops before the end"
    The applications may be left stopped: read the error, then run the script again. If the error
    is `No space left on device`, first free the images no longer used with
    `docker image prune -a -f`.

## Install a container bundle

A container bundle is a `.tar` file holding one or several application images.

### With the Web UI

Upload the bundle from the Management page, as explained in
[Update Containers](../csm/csm-web-ui.md#update-containers). The Web UI installs it and restarts
the applications on its own.

### From the command line

1. Copy the bundle to `/home/advantics`, as explained in
   [Copying files to the controller using SCP](ssh.md#copying-files-to-the-controller-using-scp).
2. [Log in to the controller](ssh.md#ssh-access) and load the bundle:

    ```bash
    docker load -i /home/advantics/update.tar
    ```

3. [Start the new containers](#start-the-new-containers).

## Pull from Docker Hub

The controller downloads the images itself, so it needs access to the Internet.

- **With the Web UI**: on the Management page, under
  [Manage Containers](../csm/csm-web-ui.md#manage-containers-secc-spcc-and-mevc), press
  **Pull images**, then **Recreate containers**.
- **From the command line**: [log in to the controller](ssh.md#ssh-access), pull the images, then
  [start the new containers](#start-the-new-containers):

    ```bash
    /etc/advantics/compose.sh default pull
    ```

## Start the new containers

After loading or pulling images from the command line, recreate the containers, then delete the
images they no longer use:

```bash
/etc/advantics/compose.sh default up -d
docker image prune -f
```

## Update the Linux system

A new AdvOS version is used from the next boot of the controller.

- **With the Web UI**: on the Management page, under
  [Manage the Controller](../csm/csm-web-ui.md#manage-the-controller-secc-spcc-and-mevc), press
  **Update AdvOS**.
- **From the command line**: [log in to the controller](ssh.md#ssh-access), then:

    1. Make sure this is the content of `/etc/ostree/remotes.d/advos.conf`:

        ```
        [remote "advos"]
        url=https://ostree.advos.advantics.com
        ```

    2. Run `sudo ostree admin upgrade`, then reboot with `sudo reboot`.
