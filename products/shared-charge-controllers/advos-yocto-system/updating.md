# Updating

Updating consists of updating the Linux system and/or the charge controller applications separately.
The "versioning" of the Linux system is done using [ ostree ](https://github.com/ostreedev/ostree). The charge controller applications are managed using [Docker Compose](https://docs.docker.com/compose/).

There are two main ways of doing such tasks:

## Updating using CSM Web UI

Please go to the [ management page ](./csm-web-ui.md#management-page-dashboardmanagement) and you can update the system (Update AdvOS) and the applications (Manage Containers, pull and recreate).

## Updating "manually"

### System update

1. Make sure this is the content of /etc/ostree/remotes.d/advos.conf

```
[remote "advos"]
url=https://ostree.advos.advantics.com
```

2. Run: `sudo ostree admin upgrade`

### Full release update

#### Loading the update

#### Option 1 (requires internet): Pulling the update from Docker Hub

In case the controller is connected to the internet, you can easily load the new images using the command:

```bash
/etc/advantics/compose.sh default pull
```

Please note that here we're using the default profile (`default`), more steps might be needed if you're using a different profile or have modified the default one.

**_Then jump to [Common steps](#common-steps)_**

#### Option 2 (does not requires internet): Loading the images from a .tar file

This is for updating one or several of the application containers. Advantics provide you a _.tar_
file. The process is to:

1. Copy the update file to the controller following the guide here: [Copying files to the controller using SCP](./ssh.md#copying-files-to-the-controller-using-scp)

2. [Login to the controller](./ssh.md#ssh-access)

3. Load the new images from the .tar file using this command:

```bash
docker load -i /path/to/update.tar
```

(Replace `/path/to/update.tar` by the actual path and name of the .tar file)

#### Common steps

- After updating the applications, use the following command to recreate and start new containers:

```bash
/etc/advantics/compose.sh default up -d
```

Please note that here we're using the default profile (`default`), more steps might be needed if you're using a different profile or have modified the default one.

- Then, to clean up and delete the old images, you can use:

```bash
docker image prune
```