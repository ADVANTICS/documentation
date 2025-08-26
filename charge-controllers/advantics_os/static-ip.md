> [!UPDATE] {docsify-updated}

<div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This section is only applicable for ADM-CS-SPCC and ADM-CS-MEVC 🚨
</div>

# Set static ip

> [!NOTE]
> We are using NetworkManager to control the primary network connection and other network interfaces.

Please note that this will disable DHCP. Also, if the currently assigned IP address differs from the new static IP, you will lose your connection or remote session.

Once you are connected via [SSH](charge-controllers/advantics_os/ssh.md), you can run the following command:

```bash
nmcli con mod network0 ipv4.addresses <desired_ip_address>/24 \
    ipv4.gateway <desired_gateway> \
    ipv4.dns <desired_dns> \
    ipv4.method manual \
    autoconnect yes

nmcli con down network0 && nmcli con up network0
```
