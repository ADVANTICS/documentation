# Deployment Checklist for Charge Controllers

Before deploying a charge controller into production, please ensure the following steps are completed:

### 1. Change Default Password

For security reasons, **always change the default root password** before deployment. Using default credentials poses a serious risk. Prioritize using public key authentication for SSH access.

```bash
passwd
```

---

### 2. Enable Log Rotation

Unrestricted log growth can eventually consume all available disk space, leading to system instability or downtime. To prevent this, make sure **log rotation** for Docker. Recent controllers are already configured from factory.

- Ensure `/etc/docker/daemon.json` contains proper log rotation settings.

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "20m",
    "max-file": "10",
    "compress": "true"
  }
}
```

### 3. Disable ADVANTICS CSM

ADVANTICS CSM is used manage system-level actions on Charge Controllers. It is designed for development purposes and should be disabled in production.

[ SSH ](charge-controllers/sys3_user/access.md) to the controller.

Stop and remove all containers:

```
docker container stop $(docker ps -aq)
docker container remove $(docker ps -aq)
```

Edit the file `/etc/init.d/S80vehicle` for the vehicle controller (evcc) and `/etc/init.d/S80charger` for the charge station controller (secc). You can use `nano` or `vi`.

Comment the following lines by adding a `#` at the beginning of each line:

```
    # Start CSM
    /srv/run-advantics-csm.sh start

    # Stop CSM
    /srv/run-advantics-csm.sh stop


    /srv/run-advantics-csm.sh clean
```

Reboot the controller by executing:

```
reboot
```

Please contact us to arrange this preparation before shipping for bulk orders.
