# Updating

Updating consists of updating the Linux system and/or the charge controller applications separately.
The "versioning" of the Linux system is done using [ ostree ](https://github.com/ostreedev/ostree). The charge controller applications are managed using [Docker Compose](https://docs.docker.com/compose/).

There are two main ways of doing such tasks:

## Updating using CSM Web UI

Please go to the [ management page ](../advos-yocto-system/csm-web-ui.md#management-page-dashboardmanagement) and you can update the system (Update AdvOS) and the applications (Manage Containers, pull and recreate).

## Updating "manually"

SSH access is required.
Please refer to [ Full release update ](../advos-yocto-system/ssh.md#full-release-update) for updating the charge controller applications and [System Update](../advos-yocto-system/ssh.md#system-update) for updating the Linux system itself.
