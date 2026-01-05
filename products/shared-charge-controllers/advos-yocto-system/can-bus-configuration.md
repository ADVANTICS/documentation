
# CAN Interface System Configuration

## Changing the CAN Bus Bitrate

The CAN interface bitrate is configured using **systemd-networkd**.
In the example below, the interface name is `can0`.

### Configuration File

The CAN interface configuration is located at:

```
/etc/systemd/network/20-can0.network
```

Example content:

```ini
[Match]
Name=can0

[CAN]
BitRate=500000
RestartSec=50ms
```

### Modifying the Bitrate

To change the CAN bus bitrate:

1. Connect to the controller using [SSH access](../advos-yocto-system/ssh.md#ssh-access).

2. Open the configuration file as root:

   ```bash
   sudo nano /etc/systemd/network/20-can0.network
   ```

3. Update the `BitRate` value to the desired baudrate (in bits per second).
   Common values include:

   * `125000`  (125 kbit/s)
   * `250000`  (250 kbit/s)
   * `500000`  (500 kbit/s)
   * `1000000` (1 Mbit/s)

   Example (setting bitrate to 250 kbit/s):

   ```ini
   [CAN]
   BitRate=250000
   RestartSec=50ms
   ```

4. Save the file and restart `systemd-networkd`:

   ```bash
   sudo systemctl restart systemd-networkd
   ```

### Verifying the Bitrate

You can verify the CAN interface configuration with:

```bash
ip -details link show can0
```

The output should show the updated bitrate under the CAN parameters.

### Notes

* All nodes on the CAN bus **must use the same bitrate** to communicate correctly.
* Changing the bitrate will temporarily bring the CAN interface down and back up.
* `RestartSec` defines how long systemd waits before restarting the CAN interface after an error.


## Persistent Virtual CAN Interface Setup Guide (vcan)

This guide details how to create a permanent virtual CAN (vcan) interface, `vcan0`, on a Linux system that uses `systemd-networkd` for network configuration (common in Yocto-based and modern distributions).

Using `systemd-networkd` requires two configuration files:

1. A **`.netdev` file** to define and create the virtual device.
2. A **`.network` file** to match and configure the device (i.e., bring it up).

### 1. Creating the Virtual Device (`.netdev`)

If you need a persistent virtual CAN interface, you must create a systemd netdev configuration file.

To create the `vcan0` virtual CAN interface, use one of the following commands to open the file `/etc/systemd/network/20-vcan0.netdev` with administrative privileges (`sudo`), and then insert the required content:

**Using nano:**

```
sudo nano /etc/systemd/network/20-vcan0.netdev
```

Insert the following content into the editor:

```
# /etc/systemd/network/20-vcan0.netdev
[NetDev]
Name=vcan0
Kind=vcan
```

*This file defines the interface's name (`vcan0`) and its type (`vcan`).*

### 2. Configuring and Bringing up the Interface (`.network`)

The file above only creates the virtual network interface. It still needs to be configured and brought up by the `systemd-networkd` daemon by creating an appropriate `.network` file that matches the name given to the virtual CAN device.

Create the file `/etc/systemd/network/20-vcan0.network` using an editor, and insert the following configuration:

```
[Match]
Name=vcan0

[CAN]

```

*The presence of the `[CAN]` section, even without explicit parameters like `BitRate`, is sufficient in this context to signal `systemd-networkd` to process the virtual CAN link and bring it up.*

### 3. Applying the Configuration and Verification

1. **Reload and Restart:** Once both files are in place, you must reload the `systemd-networkd` daemon to recognize the new configuration:
    
    ```
    sudo systemctl restart systemd-networkd
    ```
    
2. **Verify Status:** You can check whether it works by listing your network interfaces. The `vcan0` link should show an **UP** status.
    
    ```
    ip link show vcan0
    ```
    
    **Expected Output (Example):**
    
    ```
    11: vcan0: <NOARP,UP,LOWER_UP> mtu 72 qdisc noqueue state UNKNOWN group default qlen 1000
        link/can
    
    ```