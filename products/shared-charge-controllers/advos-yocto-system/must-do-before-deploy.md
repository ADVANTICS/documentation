### 1. Change the default password

Every controller ships with the same default password (`dev-only`, see [SSH access](ssh.md)). Replace
it with a strong, unique password on each controller.

[ SSH ](ssh.md) to the controller and run:

```
passwd
```

Enter the current password, then the new one twice.

!!! warning
    Keep this password even if you set up SSH keys below: it is still required by `sudo`. Store it
    safely, there is no way to recover it from the controller.

### 2. Harden SSH or disable SSH

Choose one of the two options below:

- **Option A — Harden SSH**: keep SSH access for maintenance, but only with an SSH key. Choose this
  if you need to access the controller remotely after deployment.
- **Option B — Disable SSH**: remove SSH access completely. Choose this if you do not need shell
  access once the controller is deployed: you would then have to rely on the UART console to get a
  prompt.

#### Option A: Harden SSH with public key authentication

Log in with an SSH key instead of a password, then disable password logins so the controller cannot
be accessed by guessing the password.

On **your computer**, generate a key pair if you do not have one yet:

```
ssh-keygen -t ed25519
```

Copy the public key to the controller:

```
ssh-copy-id advantics@adm-cs-<controller-type>-<serial-number>.local
```

!!! tip
    On Windows without `ssh-copy-id`, append the content of your `~/.ssh/id_ed25519.pub` file to
    `/home/advantics/.ssh/authorized_keys` on the controller.

Check that you can log in **without being asked for the password**:

```
ssh advantics@adm-cs-<controller-type>-<serial-number>.local
```

Then, on the controller, disable password logins by editing the SSH server configuration:

```
sudo nano /etc/ssh/sshd_config
```

Set the following options (uncomment them if needed):

```
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin no
```

Restart the SSH server:

```
sudo systemctl restart sshd
```

!!! danger
    Keep your current SSH session open and check that a **new** session can still log in with your
    key before closing it. If the key does not work, you will be locked out of SSH.

#### Option B: Disable SSH

Stop the SSH server and prevent it from starting at boot:

```
sudo systemctl disable --now sshd
```

!!! warning
    Do this **last**, after all the other steps of this checklist: they need SSH. Your current session
    stays open, but no new SSH connection will be accepted, including after a reboot.

!!! danger
    Once SSH is disabled, the only way to get a shell prompt on the controller is the **UART
    console**. With ADVANTICS CSM (step 3) also disabled, there is no remote shell or web access left.
    Make sure you have finished configuring the controller before disabling SSH.

### 3. Disable ADVANTICS CSM

ADVANTICS CSM is used manage system-level actions on Charge Controllers. It is designed for development purposes and should be disabled in production.

[ SSH ](ssh.md) to the controller.

Stop and remove all containers:

```
docker container stop $(docker ps -aq)
docker container remove $(docker ps -aq)
```

Edit the file `/etc/advantics/default/compose.yml`. You can use `nano` or `vim` in the CLI.

```
sudo nano /etc/advantics/default/compose.yml
```

Comment the following lines by adding a `#` at the beginning of each line:

```
  advantics-csm:
    image: ${advantics_csm_registry:-${registry:-}}${advantics_csm_namespace:-${namespace:-advantics}}/advantics-csm:${advantics_csm_version:-${default_tag:-latest}}
    extends:
      file: common.yaml
      service: admin

    volumes:
      - type: bind
        source: ${config_file:-config.cfg}
        target: /app/config.cfg
      - type: bind
        source: /run/dbus/system_bus_socket
        target: /run/dbus/system_bus_socket
        read_only: true
      - type: bind
        source: /etc/advantics/default/simulation_config.cfg
        target: /app/simulation_config.cfg

    cap_add:
      - NET_ADMIN

```

Reboot the controller by executing:

```
sudo reboot
```

Please contact us to arrange this preparation before shipping for bulk orders.