# SSH Access

!!! note
    SSH is not the preferred method to access the device in controllers running AdvOS. Please use the [ CSM Web UI ](../advos-yocto-system/csm-web-ui.md) instead unless SSH is strictly necessary.


Grab the hostname of the controller as documented in [Accessing and interacting with the controller](../advos-yocto-system/connecting.md).

Example:

`ssh advantics@adm-cs-<controller-type>-<serial-number>.local` ie. `ssh advantics@adm-cs-spcc-12345678.local`

!!! tip
    You can also use [ Putty ](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or any SSH client of your choice.


The root login is disabled and the default user is `advantics`. The default password is `dev-only`.

Please change the default password as soon as you log in. Remember that if you need to run privileged commands, you can use `sudo`.

| \*           | \*          |
| ------------ | ----------- |
| **Login**    | _advantics_ |
| **Password** | _dev-only_  |


For controllers meant for series production, the following hardening methods are available.

- Strong, randomized password initialized at first boot of the system after installation.
- SSH key provisioned on the system, and SSH password login restricted.

!!! attention
    For series production, you will have to choose at least one of these methods. ADVANTICS will
    refuse to provide series production orders with system having simple, always the same, default
    password. Even if you don't plan to have the module connected to Internet.


# Copying files to the controller using SCP

Using the Command Line (Linux, macOS, or Windows with WSL/PowerShell).

- Open a terminal (or Command Prompt / PowerShell on Windows if you have scp available).

- Navigate to the folder where your file is located. For example: `cd /path/to/your/file`

- Run the scp command to copy the file:

  ```bash
  scp <filename> <username>@<hostname>:<destination-path>
  ```

  Replace:

  `<filename>` – with the name of the file you want to copy

  `<username>` – with the login user on the remote device **(use `advantics`)**

  `<hostname>` – Grab the hostname of the controller as documented in [Accessing and interacting with the controller](../advos-yocto-system/connecting.md).

  `<destination-path>` – with the target directory on the device **(use `/home/advantics`)**

  Example: `scp myupdate.tar advantics@adm-cs-spcc-12345678:/home/advantics`

- Enter the password for the device when prompted. (the default is _dev-only_)

# System update

1. Make sure this is the content of /etc/ostree/remotes.d/advos.conf

```
[remote "advos"]
url=https://ostree.advos.advantics.com
```

2. Run: `sudo ostree admin upgrade`

# Full release update

## Loading the update

### Option 1 (requires internet): Pulling the update from Docker Hub

In case the controller is connected to the internet, you can easily load the new images using the command:

```bash
/etc/advantics/compose.sh default pull
```

Please note that here we're using the default profile (`default`), more steps might be needed if you're using a different profile or have modified the default one.

**_Then jump to [Common steps](#common-steps)_**

### Option 2 (does not requires internet): Loading the images from a .tar file

This is for updating one or several of the application containers. Advantics provide you a _.tar_
file. The process is to:

1. Copy the update file to the controller following the guide here: [Copying files to the controller using SCP](#copying-files-to-the-controller-using-scp)

2. [Login to the controller](#ssh-access)

3. Load the new images from the .tar file using this command:

```bash
docker load -i /path/to/update.tar
```

(Replace `/path/to/update.tar` by the actual path and name of the .tar file)

### Common steps

- After updating the applications, use the following command to recreate and start new containers:

```bash
/etc/advantics/compose.sh default up -d
```

Please note that here we're using the default profile (`default`), more steps might be needed if you're using a different profile or have modified the default one.

- Then, to clean up and delete the old images, you can use:

```bash
docker image prune
```