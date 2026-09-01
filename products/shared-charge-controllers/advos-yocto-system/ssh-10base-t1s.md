This guide shows how to establish a remote shell on the ADM-CS-SPCC via SSH using a 10base-T1S connection.
The 10base-T1S interface used is EVB-LAN8670-USB from Microchip.

## SSH From Windows 11

Download the drivers [ from the official webpage ](https://www.microchip.com/en-us/development-tool/ev08l38a)

{{ figure('./images/download.png', 'Downloading the EVB-LAN8670-USB drivers from Microchip') }}

Extract the downloaded zip file by right clicking the downloaded file and choosing Extract all.

{{ figure('./images/extract-1.png', 'Extracting the driver archive with "Extract all"') }}

{{ figure('./images/extract.webp', 'Choosing where to extract the driver archive') }}

Execute the installer.

{{ figure('./images/start-install.png', 'Starting the driver installer') }}

Follow the instructions of the installer.

{{ figure('./images/install-1.webp', 'Driver installer, first step') }}

Recommendation: Use the default path for the installation.

{{ figure('./images/install-2.webp', 'Driver installer, installation path -- keep the default') }}

{{ figure('./images/install-3.webp', 'Driver installer, installation complete') }}

Go to Network Connections and check that there is a new interface type 10base-T1S.

{{ figure('./images/interfaces.png', 'The new 10base-T1S interface in Windows Network Connections') }}

Open a new command prompt and ping your controller using its mDNS hostname. You can find it [here](./connecting.md). It should work without further action.

{{ figure('./images/cmd.png', 'Opening a Windows command prompt') }}

{{ figure('./images/ping.webp', 'Pinging the controller by its mDNS hostname') }}

If the ping was successful, you should be able to ssh in the controller. The default password can be found [here](./connecting.md).

{{ figure('./images/ssh.webp', 'Logging in to the controller over SSH') }}

## SSH From Linux

There is no need to install any driver on Linux. Just connect the controller to your computer using the usb 10base-T1S interface and ping the controller using its mDNS hostname. You can find it [here](./connecting.md). It should work without further action.
