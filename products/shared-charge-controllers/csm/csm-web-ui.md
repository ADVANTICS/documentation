# ADVANTICS CSM Web UI

Advantics CSM, short for Advantics Controller System Manager, handles all system-level operations. It provides a web interface for monitoring and configuring the system, aiming to minimize the need for manual config file edits and command-line interactions. Users can access logs, manage applications, and perform system updates directly through the interface.

## Connecting to the CSM Web UI

The CSM Web UI is available at the IP address/hostname of the controller on port 80.

<!-- The CSM Web UI is available at the IP address/hostname of the controller on port 80. Check [how to connect to the controller](advos-yocto-system/connecting.md). -->

!!! attention
    The CSM Web UI is designed for development purposes and should be disabled in production when deploying the controller. Even in development, access should be restricted to a secure private network, as there is no authentication mechanism.


## Introduction

The UI is divided into two main sections:

- A collapsible sidebar on the left with links to navigate to different parts of the UI. Common to all pages.
- Main content area where the actual content is displayed

## Status page `/dashboard`

The main content shows:

- Controller Info: Serial number, name of the controller, ethernet mac address, ethernet ipv4 addres, PLC mac address, PLC ipv6 address, and the hostname.
- Controller Status: Shows the state of the applications as well as the uptime.
- Pistol Status: Shows the **enabled** pistols and their voltage, current and power limits that are currently set, as well as the point in the charging sequence that the pistol that is currently charging is in.

{{ figure('./images/csm-ui-index-annotated.png', 'CSM Web UI landing page', size='80%') }}

## Monitoring page `/dashboard/monitoring`

There are two widgets in the monitoring page.

### Live Parameters

This widget shows live parameters of the controller and the ongoing charge session.

{{ figure('./images/csm-ui-monitoring-live-parameters.png', 'CSM Monitoring Live Parameters', size='100%') }}

### Live Charts

"Live Charts" plot shows the stage of the charge and output voltage and current. At the top of the  
plot the user can select which data to display and freeze the plot. Once the plot is frozen, the user can download the data in CSV format.

{{ figure('./images/csm-ui-monitoring-chart.png', 'The Live Charts widget of the monitoring page', alt='CSM Live Charts Monitoring', size='100%') }}

### Meters

Right under the plot, the "Meters" widgets shows the current output voltage, output current and output power.

## Controller configuration page `/dashboard/configuration`

In this page the user can edit the configuration of the controller. It is equivalent to editing the `config.cfg` file.

The configuration header allows to:

- Switch to expert mode: Showing extended configuration options.
- Export config: Downloads the configuration file loaded in the controller.
- Upload config file: Replaces the configuration with a file from your computer, for instance one
  exported before a software update.
- Reset Configuration: Reset the configuration to the factory default values.
- Retrieve Configuration: Overwrites changes that you might have made in the UI with the current configuration that is loaded in the controller.

{{ figure('./images/csm-ui-configuration-header.png', 'The header of the configuration page', size='50%') }}

### The options shown vary with the type of the controller.

The two images below depict the differences between a supply equipment controller and a vehicle controller.

{{ figure('./images/csm-ui-configuration-mevc.png', 'Configuration sections of our MEVC - MCS vehicle controller', size='50%') }}

{{ figure('./images/csm-ui-configuration-spcc.png', 'Configuration sections of our SPCC - MCS supply equipment controller', size='50%') }}

!!! attention
    After successfully modifying the config, the applications should be restarted in order for changes to be taken into account. The CSM Web UI will notify and propose to do so after submitting.


{{ figure('./images/csm-ui-configuration-restart.png', 'Configuration submission prompting to restart', size='50%') }}

## Management page `/dashboard/management`

The **Management** page provides tools for maintaining and updating the system's containers and
controller. Reach it with **System Management** in the left sidebar.

{{ figure('./images/csm-ui-management.png', 'Management section of the CSM web UI', size='80%') }}

!!! note
    Not every card below is shown on every controller. The two container update widgets and the
    certificate sections are always there; _Manage Containers_ and _Manage the Controller_ are
    hidden on the EVCC, and _Sync Time_ is only shown on the vehicle controllers (EVCC and MEVC).

### Update Containers

 Advantics provides a _.tar_ bundle holding one or several application containers, and either of the two
widgets at the top of the page loads it into the controller.

{{ figure('./images/csm-ui-management-update.png', 'The two container update widgets of the management page', size='100%') }}

- **Update containers using a tar bundle from your computer**: drop the file onto the dashed area,
  or click it to browse for the file, then press **Update**.

- **Update containers using a tar bundle from Internet**: paste the URL Advantics gave you, then
  press **Update**.

    !!! tip
        With the _from Internet_ widget the bundle is downloaded by **your browser**, then sent to
        the controller. So it is your computer that needs access to that URL, not the controller.

Once the bundle is uploaded, a confirmation message is shown and the update is installed as soon as
the controller is idle. Installing loads the new images, prunes the images they replace, then
restarts the charging applications on its own: there is no command to type afterwards, and no power
cycle needed. Back on the Status page, the _Controller Status_ table then shows the new version of
each application.

!!! attention
    An update is never applied in the middle of a charge session. If one is ongoing, the update
    stays pending until it ends.

!!! warning
    Do not power off the controller while the update is being applied.

### Manage Containers (SECC, SPCC and MEVC)

- **Pull images**: Fetches the latest container images for the selected profile without restarting or updating running containers.
- **Recreate containers**: Stops, removes, recreates, and restarts containers. The UI may become temporarily unresponsive until the CSM container is back online.

### Manage the Controller (SECC, SPCC and MEVC)

- **Reboot Controller**: Restarts the controller system.
- **Update AdvOS**: Updates the underlying **AdvOS** Linux system using `ostree`. This card is only
  relevant to controllers running AdvOS; the Linux system of a controller running System 3.x is
  updated from a SD card instead.

### Sync Time

Syncs the system time with a NTP server, falling back on the time of your own computer if no server
can be reached.

### Web Interface Certificate

By default this web interface is served over plain **HTTP** on port 80. The **Web Interface
Certificate** section, at the bottom of the Management page, serves it over **HTTPS** instead:
either with a certificate you own, or with a self-signed one generated by the controller.

{{ figure('./images/csm-ui-management-web-certificate.png', 'The Web Interface Certificate section of the management page', size='100%') }}

!!! note
    This certificate only protects the browsing of this web interface. It has nothing to do with
    the TLS certificates of the charging protocols, which are handled by the _TLS Certificates_
    section right below it.

#### Uploading your own certificate and key

1. In **Upload Web Interface Certificate**, drop your certificate file onto the dashed area, or
   click it to browse for the file, then press **Upload**.
2. Do the same in **Upload Web Interface Certificate Key** with the matching private key.
3. Open the [Configuration page](#controller-configuration-page-dashboardconfiguration), go to
   the **System** section, **Web Interface** category, and set:

    - **`web_interface_certificate`**: the file name of the certificate you uploaded, for
      instance `my-charger.pem`.
    - **`web_interface_certificate_key`**: the file name of the private key you uploaded, for
      instance `my-charger-key.pem`.

    Then submit the configuration.

4. Restart the applications, CSM included, when the UI proposes it after the submission.

!!! attention "Uploading the files is not enough"
    The two files are only copied into the certificates folder of the controller. It is the
    configuration that tells the admin service which of them to serve the web interface with, so
    the web interface stays on plain HTTP until step 3 is done and the applications are restarted.

{{ figure('./images/csm-ui-configuration-web-certificate.png', 'The two web interface certificate options in the System section of the configuration page', size='100%') }}

Both files are expected in **PEM** format. Give each file a name you will recognise in the
configuration, as that name is what you type there. Uploading a file again under the same name
overwrites the previous one, which is how a certificate is renewed: upload the new pair under the
same names, then restart the applications, with no configuration change needed.

#### Generating a self-signed certificate

**Generate** creates a certificate and its private key directly on the controller, for its
hostname, its IP address and `localhost`. The UI then shows what the certificate covers and until
when it is valid, and proposes to serve this web interface with it; accepting fills the two
configuration options above for you, so there is nothing to edit in the Configuration page. The
applications still have to be restarted, which the UI proposes as well.

!!! warning
    A self-signed certificate is not issued by an authority your browser knows, so every browser
    warns about it and the connection has to be accepted manually. It encrypts the traffic, but it
    does not prove the identity of the controller. Use one for a private commissioning network,
    and a certificate issued for your own domain in any other case.

#### Reaching the UI once HTTPS is on

Once the applications have restarted, the web interface is only reachable over `https://`:

- If `web_interface_port` was left at its default of `80`, the interface moves to the standard
  HTTPS port, **443**: reach it at `https://<controller-ip>/`, without a port.
- If it was set to any other value, that port is kept, and the interface is reached at
  `https://<controller-ip>:<port>/`.

Clearing `web_interface_certificate` in the configuration and restarting the `advantics-csm` application brings
the interface back on plain HTTP.

### TLS Certificates

The last section of the page holds the TLS certificates used by the charging protocols. Uploaded charging certificates are staged until **Validate and Commit** is
pressed. 

## Logging page `/dashboard/logs`

Real-time logs of the docker applications. The user can filter which applications to display, enable/disable auto-scroll and showing all logs in the same widget.

Refresh the page if the logs are not loading properly.

!!! info
    The log stream is exclusive to the most recent user. If a new user connects to the Web UI and initiates a log stream, the previous stream will be closed to optimize system resources.


Export the logs will generate a zip file with the logs of the controller and a copy of the config file.

{{ figure('./images/csm-ui-logging.png', 'CSM Logging page of a vehicle controller', alt='CSM Logging', size='80%') }}
