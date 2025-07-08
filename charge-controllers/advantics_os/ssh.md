> [!UPDATE] {docsify-updated}

<div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This section is only applicable for ADM-CS-SPCC and ADM-CS-MEVC 🚨
</div>

# SSH Access

> [!NOTE]
> SSH is not the preferred method to access the device in controllers running AdvOS. Please use the [ CSM Web UI ](charge-controllers/advantics_os/csm-web-ui.md) instead unless SSH is strictly necessary.

Grab the hostname of the controller as documented in [Accessing and interacting with the controller](charge-controllers/advantics_os/connecting.md).

Example:

`ssh advantics@adm-cs-<controller-type>-<serial-number>.local` ie. `ssh advantics@adm-cs-spcc-12345678.local`

The root login is disabled and the default user is `advantics`. The default password is `dev-only`.

Please change the default password as soon as you log in. Remember that if you need to run privileged commands, you can use `sudo`.

<div class="noheader-table small-table compact-table">

| \*           | \*          |
| ------------ | ----------- |
| **Login**    | _advantics_ |
| **Password** | _dev-only_  |

</div>

For controllers meant for series production, the following hardening methods are available.

- Strong, randomized password initialized at first boot of the system after installation.
- SSH key provisioned on the system, and SSH password login restricted.

> [!ATTENTION]
> For series production, you will have to choose at least one of these methods. ADVANTICS will
> refuse to provide series production orders with system having simple, always the same, default
> password. Even if you don't plan to have the module connected to Internet.


## Copying files to the controller using SCP
Using the Command Line (Linux, macOS, or Windows with WSL/PowerShell).

- Open a terminal (or Command Prompt / PowerShell on Windows if you have scp available).

- Navigate to the folder where your file is located. For example: `cd /path/to/your/file`

- Run the scp command to copy the file:

    `scp <filename> <username>@<hostname>:<destination-path>`

    Replace:

    `<filename>` – with the name of the file you want to copy

    `<username>` – with the login user on the remote device **(use `advantics`)**

    `<hostname>` – Grab the hostname of the controller as documented in [Accessing and interacting with the controller](charge-controllers/advantics_os/connecting.md).

    `<destination-path>` – with the target directory on the device **(use `/home/advantics`)**

    Example: `scp myupdate.tar advantics@adm-cs-spcc-12345678:/home/advantics`

- Enter the password for the device when prompted. (the default is _dev-only_)