# ADVANTICS CSM Web UI

<!-- <div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This interface is currently supported only for ADM-CS-SPCC and ADM-CS-MEVC 🚨
</div> -->

Advantics CSM, short for Advantics Controller System Manager, handles all system-level operations. It provides a web interface for monitoring and configuring the system, aiming to minimize the need for manual config file edits and command-line interactions. Users can access logs, manage applications, and perform system updates directly through the interface.

## Connecting to the CSM Web UI

The CSM Web UI is available at the IP address/hostname of the controller on port 80. Check [how to connect to the controller](advos-yocto-system/connecting.md).

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

![CSM Web UI landing page](./images/csm-ui-index-annotated.png ":size=80%")

<figcaption style="text-align: center">CSM Web UI landing page</figcaption>

## Monitoring page `/dashboard/monitoring`

There are two widgets in the monitoring page.

### Live Parameters

This widget shows live parameters of the controller and the ongoing charge session.
![CSM Monitoring Live Parameters](./images/csm-ui-monitoring-live-parameters.png ":size=100%")

<figcaption style="text-align: center">CSM Monitoring Live Parameters</figcaption>

### Live Charts

"Live Charts" plot shows the stage of the charge and output voltage and current. At the top of the  
plot the user can select which data to display and freeze the plot. Once the plot is frozen, the user can download the data in CSV format.

![CSM Live Charts Monitoring](./images/csm-ui-monitoring-chart.png "width=100%")

<figcaption style="text-align: center">CSM Live Charts</figcaption>

### Meters

Right under the plot, the "Meters" widgets shows the current output voltage, output current and output power.

## Controller configuration page `/dashboard/configuration`

In this page the user can edit the configuration of the controller. It is equivalent to editing the `config.cfg` file.

The configuration header allows to:

- Switch to expert mode: Showing extended configuration options.
- Reset Configuration: Reset the configuration to the factory default values.
- Retrieve Configuration: Overwrites changes that you might have made in the UI with the current configuration that is loaded in the controller.

![Configuration header](./images/csm-ui-configuration-header.png ":size=50%")

### The options shown vary with the type of the controller.

The two images below depict the differences between a supply equipment controller and a vehicle controller.

![Configuration sections a vehicle controller](./images/csm-ui-configuration-mevc.png ":size=50%")

<figcaption style="text-align: center">Configuration sections a vehicle controller</figcaption>

![Configuration sections a charger side controller](./images/csm-ui-configuration-spcc.png ":size=50%")

<figcaption style="text-align: center">Configuration sections a charger side controller</figcaption>

!!! attention
    After successfully modifying the config, the applications should be restarted in order for changes to be taken into account. The CSM Web UI will notify and propose to do so after submitting.


![Configuration submission prompting to restart](./images/csm-ui-configuration-restart.png ":size=50%")

## Management page `/dashboard/management`

The **Management** page provides tools for maintaining and updating the system’s containers and controller.

![Management section of the CSM web UI](./images/csm-ui-management.png ":size=80%")

<figcaption style="text-align: center">Management section of the CSM web UI</figcaption>

### Update Containers

- **From Internet**: Enter a URL to a `.tar` bundle containing application artifacts.
- **From Computer**: Upload a `.tar` bundle directly from your local machine.

### Manage Containers

- **Pull images**: Fetches the latest container images for the selected profile without restarting or updating running containers.
- **Recreate containers**: Stops, removes, recreates, and restarts containers. The UI may become temporarily unresponsive until the CSM container is back online.

### Manage the Controller

- **Reboot Controller**: Restarts the controller system.
- **Update AdvOS**: Updates the underlying **AdvOS** Linux system using `ostree`.

This interface centralizes system updates and container lifecycle management in one place.

## Logging page `/dashboard/logs`

Real-time logs of the docker applications. The user can filter which applications to display, enable/disable auto-scroll and showing all logs in the same widget.

Refresh the page if the logs are not loading properly.

> [!INFO]
> The log stream is exclusive to the most recent user. If a new user connects to the Web UI and initiates a log stream, the previous stream will be closed to optimize system resources.

Export the logs will generate a zip file with the logs of the controller and a copy of the config file.

![CSM Logging](./images/csm-ui-logging.png ":size=80%")

<figcaption style="text-align: center">CSM Logging page of a vehicle controller</figcaption>
