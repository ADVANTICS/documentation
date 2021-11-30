> [!UPDATE] {docsify-updated}
# Managing charging applications

## Applications are in containers

We chose to run our applications in Linux containers with Docker for various reasons:

* It simplifies updates for just one application.
* The layering of containers file system makes for lightweight updates.
* Containers use system tools and libs that are independent of the host Buildroot system (which is
more constrained and potentially less up-to-date for some packages).
* Benefit from process and network isolations to further minimize security risks.
* Resources of the system can be limited for each application in case one misbehaves.
* Docker itself can monitor for processes heartbeat and restart them if they fail.

Users are free to use containers or not. If they do, they are also free to use the base images they
want.

Advantics provides base images for Python environment (installed by default). These images are themselves based on Debian 10 (Buster) arm32v7 images provided
directly by Docker, Inc.

## EVSE applications

### Start and stop all

There is a central script for managing all applications at once:
```bash
$ /etc/init.d/S80charger <COMMAND>
```

This script takes one parameter _COMMAND_ which correspond to the following actions:

| **_COMMAND_** | Description |
|---|---|
| start | Start all applications. |
| stop | Stop all applications. |
| restart | Stop and start again all applications. |
| clean | Clean all application logs. Must be done when all applications are stopped. |
| restart-clean | Stop all applications, then clean their logs, then restart them. |

### Individual control

Each application has its own managing script:

<figcaption>Main controller</figcaption>

```bash
$ /srv/run-evse-controller.sh <COMMAND>
```
<br/>
<figcaption>CCS SECC frontend</figcaption>

```bash
$ /srv/run-ccs-secc.sh <COMMAND>
```
<br/>
<figcaption>CCS SLAC frontend</figcaption>

```bash
$ /srv/run-slac-evse.sh <COMMAND>
```

They all takes the same _COMMAND_ parameter:

| **_COMMAND_** | Description |
|---|---|
| setup | Prepare the application for running. Automatically called by _start_. |
| start | Start the application. |
| stop | Stop the application. |
| clean | Clean application logs and unprepare it. Must be done when application is stopped. |
| status | Print out the status of the application. |
| logs | Print out the logs and keep following them. Do _CTRL+C_ to exit the log. |
| exportlogs | Takes one exta parameter to give the file name where the logs will be exported to. |

## PEV applications

### Start and stop all

There is a central script for managing all applications at once:
```bash
$ /etc/init.d/S80vehicle <COMMAND>
```

This script takes one parameter _COMMAND_ which correspond to the following actions:

| **_COMMAND_** | Description |
|---|---|
| start | Start all applications.
| stop | Stop all applications.
| restart | Stop and start again all applications.
| clean | Clean all application logs. Must be done when all applications are stopped.
| restart-clean | Stop all applications, then clean their logs, then restart them.

### Individual control

Each application has its own managing script:

<figcaption>Main controller</figcaption>

```bash
$ /srv/run-pev-controller.sh <COMMAND>
```
<br/>
<figcaption>CCS EVCC frontend</figcaption>

```bash
$ /srv/run-ccs-evcc.sh <COMMAND>
```
<br/>
<figcaption>CCS SLAC frontend</figcaption>

```bash
$ /srv/run-slac-pev.sh <COMMAND>
```

They all takes the same _COMMAND_ parameter:

| **_COMMAND_** | Description |
|---|---|
| setup | Prepare the application for running. Automatically called by _start_.
| start | Start the application.
| stop | Stop the application.
| clean | Clean application logs and unprepare it. Must be done when application is stopped.
| status | Print out the status of the application.
| logs | Print out the logs and keep following them. Do _CTRL+C_ to exit the log.
| exportlogs | Takes one exta parameter to give the file name where the logs will be exported to.

### Export and copy Logs

After exporting the logs of an application with exportlogs command as shown in the following example :

```bash
$ /srv/run-evse-controller.sh exportlogs evselogsname
```

You can download the logs to your system by doing:

```bash
$ scp root@<controllerIPAddress>:<LogsPath> <DestinationPath>
```
You should replace <controllerIPAddress> with the IP address of the controller, <LogsPath> with the logs path on the controller, and <DestinationPath> with the destination folder on your system. The following is an example:
```bash
$ scp root@192.168.1.51:/root/evselogsname .
```
