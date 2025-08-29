> [!UPDATE] {docsify-updated}

<div style="background-color: teal; color: white; font-weight: bold; padding: 10px; text-align: center;">
    🚨 IMPORTANT: This section is only applicable for ADM-CS-SPCC and ADM-CS-MEVC 🚨
</div>

# Updating

Updating consists of updating the Linux system and/or the charge controller applications separately.
The "versioning" of the Linux system is done using [ ostree ](https://github.com/ostreedev/ostree). The charge controller applications are managed using [Docker Compose](https://docs.docker.com/compose/).

There are two main ways of doing such tasks:

## Updating using CSM Web UI

Please go to the [ management page ](charge-controllers/advantics_os/csm-web-ui?id=management-page-dashboardmanagement) and you can update the system (Update AdvOS) and the applications (Manage Containers, pull and recreate).

## Updating "manually"

SSH access is required.
Please refer to [ Full release update ](charge-controllers/advantics_os/ssh#full-release-update) for updating the charge controller applications and [System Update](charge-controllers/advantics_os/ssh#system-update) for updating the Linux system itself.
