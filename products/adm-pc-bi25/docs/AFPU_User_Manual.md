# ADVANTICS Flash Programming Utility (AFPU) User Manual

## Before starting

Before getting started, make sure that CAN communications are working properly on your device:

- **On Windows**, you can use *PCAN-Viewer*  ([https://www.peak-system.com/PCAN-View.242.0.html?&L=2](https://www.peak-system.com/PCAN-View.242.0.html?&L=2)) to peek at the CAN messages on your bus. You can use to verify that you can connect to your CAN interface properly and receive messages on it.
- **On Linux,** you can use `can-utils` package, which contains among other things `candump`. Run `candump -ta your-interface-name` to show the CAN communications in your terminal. You will need to setup your CAN interface prior to that as explained in the socketcan documentation: [https://docs.kernel.org/networking/can.html](https://docs.kernel.org/networking/can.html)

# Introduction

`afpu` can run as a pure command-line application or as a TUI (Terminal User Interface). Calling `afpu` without argument (or double-clicking on the application) will open the TUI directly. Passing any argument will use the command-line interface instead.

## CLI Overview

You get the manual for afpu using `afpu --help`. Here is a snapshot:

```jsx
Usage: afpu [OPTIONS] COMMAND [ARGS]...

  Main entrypoint for the command-line utility

Options:
  -l, --level [CRITICAL|FATAL|ERROR|WARN|WARNING|INFO|DEBUG|NOTSET]
  -in, --inline                   Runs the TUI in inline mode
  --help                          Show this message and exit.

Commands:
  check-firmware-updates  Checks what firmware update are available for...
  download-firmware
  erase-memory            Wipes the sectors in flash memory pointed by...
  flash                   flashin
  interrupt-boot          Prevents the bootloader from automatically...
  make-virgin             Erases the device's EEPROM.
  probe                   Probes the MCP25 devices present on the CAN bus
  read-eeprom             Reads the current values programmed in the...
  read-fw-info            Extracts firmware version and datecode
  reset                   Restarts the target's device CPU.
  resume-boot             Requests to exit the bootloader and boot the...
  set-serial-number       Reprograms the serial number in the target...
  web                     Runs afpu in the browser
  write-eeprom            Writes a value to the bootloader's EEPROM.
```

You can get also get individual subcommands manual by calling `afpu {subcommand} --help`, for example: `afpu read-eeprom --help` :

```jsx
╭──────────────────────────────────────────────────────╮                                                                                                                                       
│  --- Advantics Flash Programming Utility (AFPU) ---  │                                                                                                                                       
╰──────────────────────────────────────────────────────╯                                                                                                                                       
Usage: afpu read-eeprom [OPTIONS]

  Reads the current values programmed in the module's EEPROM

Options:
  -c, --can-channel TEXT
  -p, --stack-position INTEGER
  -t, --module-type [CONTROLLER|FILTER|PFC|LLC|BUCK|GENERIC|AFE|BI25|SFRA_Float|DLOG|LOG|ID_STEALER|BOOTLOADER|VG11_AC|VG11_DC|VG11]
  --help                          Show this message and exit.
```

## TUI Overview

After opening the application, you should get the following menu:

{{ figure('../assets/hompage_annotated.drawio.png', 'AFPU menu') }}

The main actions buttons are shown in **(1);** they all have keyboard shortcuts, which are indicated in the bottom bar **(2).** 

The first thing you should do is connecting to your CAN devices; to do that, click ‘Connect’ or press **c**. AFPU will probe the bus for about 3 seconds, and the detected devices will be displayed in the top-right panel. Here is an example, with one AFE and one LLC on the bus:

{{ figure('../assets/after_conn.png', 'AFPU example with one AFE and one LLC on the bus') }}

## Reading the EEPROM

To check the content of your module’s EEPROM, press `r` or click the `Read EEPROM` button. EEPROM values should get populated in the left menu:

{{ figure('../assets/after_read_eeprom.png', 'AFPU populated EEPROM values') }}

## Flashing

### From an official release

After connecting to a unit, the link to the latest release for that unit should get populated in the URL placeholder on the right. You can apply the update directly by clicking `Flash` or pressing `f`.

### From local storage

If you would rather like to use a local file, you may use the file browser on the right side to flash a local *.hex* file (firmware.hex in this example):

{{ figure('../assets/file_browser.png', 'AFPU file browser') }}

Click on the file and press `f` or click the `Flash` button.
