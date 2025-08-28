> [!UPDATE] {docsify-updated}
# EVCC Updater
This update should improve the resilience of your EVCC to noisy conditions on the CP line, for both PWM and PLC communications. It is provided as a script for both Windows and Linux to facilitate the process.<br>
This script will update the following things:
* Update the CCS EVCC application to the latest version for EVCC
* Update the SLAC application to the latest version
* Updates the on-board PLC chip firmware
* Improve the attenuation map used by the on-board PLC chip.
* Limit the size of the application logs to prevent them from bloating the system \*.

*\*Note that it will also disable the dumps of the on-board PLC chip. This has been added to protect the filesystem from bloating once used in production. If you are still doing R&D and want to keep the dumps on, please check the Appendix below to re-enable them after running the script.*
<br>

# Instructions
The script provided will look for an EVCC on your lcoal network and automatically update it. To run it in good conditions, please check the following:<br>
*Note: When unspecified, we assume that your EVCC is using the default IP address, which is 192.168.1.49. If you have reconfigured the network settings for your EVCC, changed the IP in the examples below by the one you configured.*
* Connect the PEV to your local network using its Ethernet socket. Make sure that it is reachable from the computer from which you are running the script; you can ping the EVCC at 192.168.1.49.
* Make sure that only one EVCC at a time is connected to the network. This is very important because all your EVCC will use the same IP by default; if multiple of them are connected, the IP conflict will prevent the communications from properly working.
* Start the script:
    * **Windows**: if you are using default IP and password, double-clicking on the script is enough.
    If you need to pass custom parameters, follow the following example syntax:
    ```
    pev-updater.exe --ip 192.168.1.27 --pwd mysecurepassword
    ```
    * **Linux**: open a shell, go the folder in which the script is stored, make the script executable and run it:
        ```
        chmod +x pev-updater
        ./pev-updater
        ```
    You should see the following:
    ```
        ******** ADVANTICS update tool *********

    This utility will probe PEVs on your network and automatically update them.
    To update the PEV, run:
    > /pev-updater

    If you are not using the default IP (192.168.1.49) or the default password, you pass them as:
    > ./pev-updater --ip 192.168.1.27 --pwd mysecurepassword

    When updating multiple boards sequentially, you do not need to restart this utility every time.
    The application will detect new boards every time they are connected and update them automatically.
    Keep an eye on the console and wait for it to display success.
    Then you can unplug the current board and plug the next one, it will be processed automatically.

    To get verbsose output (which will print the standard output from all the commands ran), use:
    > ./pev-updater --verbose
    WARNING: do NOT connect multiple PEVs at once as they all use the same IP; make sure that only 1 PEV with this IP is currently connected.
    If this utility is not detecting your board, try to ping it to make sure it is actually reachable:
    > ping 192.168.1.49 (assuming default IP)
    Also, check that your firewall is not blocking SSH (port 22).

    Once you are done, use Ctrl + C to exit this program.

    Probing pev @IP 192.168.1.49...
    ```
    The script should detect automatically your EVCC and start updating. WHen the update process, you should see ```PEV update success```. You can now safely unplug the Ethernet cable and move to the next EVCC. you do **not** need to restart the script. It will automatically detects and process the next EVCC once you connect it.<br>
Note that the script will produce some logs, which are stored in the same folder.

# Command-line options and flags
```
  ************** ADVANTICS update tool ***************

  Requires to connect the PEV controller ethernet port to your local network
  Can be used from any laptop/computer that has a valid network connection to
  that PEV. Probes the network and looks for a PEV to update at the given
  address, and proceeds to update it.

  If you are not using the default IP or the default password, you can pass
  them as: > pev-updater --ip 192.168.1.27 --pwd mysecurepassword

  When updating multiple boards sequentially, you do not need to restart this
  utility every time. The application will detect new boards every time they
  are connected and update them automatically. Keep an eye on the console and
  wait for it to display success. Then you can unplug the current board and
  plug the next one, it will be processed automatically.

  To get verbsose output (which will print the standard output from all the
  commands ran), use: > pev-updater --verbose WARNING: do NOT connect multiple
  PEVs at once as they all use the same IP; make sure that only 1 PEV with
  this IP is currently connected. If this utility is not detecting your board,
  try to ping it to make sure it is actually reachable: > ping 192.168.1.49
  (assuming default IP) Also, check that your firewall is not blocking SSH
  (port 22).

  Once you are done, use Ctrl + C to exit this program.

Options:
  -v, --verbose   If on, displays stdout from commands executed
  -i, --ip TEXT   Overridee default IP for the target board
  -p, --pwd TEXT  Overrides default password for the target board
  -f, --force     Does not check conditions before running scripts; use that
                  if you want to update even if you already have the latest
                  version
  -o, --one-shot  Stops this script after updating one EVCC. If not passed, by
                  default the script will run continously until it's stopped
                  manually
  --help          Show this message and exit.
```

# Troubleshooting
* If the PEV is not detected, make sure that it is reachable by pinging it and also check your network security policy. The update process is based on SSH, which is using port 22; make sure that this port is not blocked. If you are struggling with your network settings consider hooking a cable directly from your computer to the EVCC, without using a switch.
* If the script fails, it will wait for some input from the user. You can try to rerun it by pressing 'r'. On EVCCs with typical settings this should not happen, if that's the case please contact us.
* MacOs is *not* supported.
* The script has been tested on Ubuntu 20.04 LTS, Windows 10 and Windows 11

> [!WARNING]
> If you have an IPV6 network, access the controller and use the command ifconfig then under eth0 you’ll find the controller’s ipv6.
> Copy it then add the option --ip when you execute the updater script via a cmd:
> ```
> /path/to/updater_script.exe -o --ip ipv6_of_the_controller
> ```
> Don’t forget to change the path, name of the updater script, and the ipv6 in the command above.



# Appendix: re-enabling dumps
To re-enable dumps, follow the procedure in the developer guide to switch the system to writable mode, then open `/srv/run-dumps.sh` on the controller filesystem and remove the line `exit 0` from the file.
