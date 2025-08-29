> [!UPDATE] {docsify-updated}

# Set a different IP address (network configuration)

By default, controllers running Linux 3.x come with the following config:

| Variant         | Static IP    | Submask       | Gateway     |
| --------------- | ------------ | ------------- | ----------- |
| **ADM-CS-SECC** | 192.168.1.51 | 255.255.255.0 | 192.168.1.1 |
| **ADM-CS-EVCC** | 192.168.1.49 | 255.255.255.0 | 192.168.1.1 |

In order to modify this, you need to [SSH](charge-controllers/sys3_user/access#ssh) to the controller.
Then edit using `nano` or `vi` the file `/etc/network/interfaces`:

The configuration you will be interested in is:

```
# Example for ADM-CS-EVCC
address 192.168.1.49
netmask 255.255.255.0
gateway 192.168.1.1
```

After modifying, save the file and reboot the controller.
