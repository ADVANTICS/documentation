### 1. Disable ADVANTICS CSM

ADVANTICS CSM is used manage system-level actions on Charge Controllers. It is designed for development purposes and should be disabled in production.

[ SSH ](charge-controllers/advantics_os/ssh.md) to the controller.

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