> [!UPDATE] {docsify-updated}
# Manual GPIO control

> [!NOTE]
> The script to manually control GPIOs is only there for test and development purposes.
> Applications are not using these scripts to control GPIOs.

The GPIO control script is available at `/srv/gpio.sh`.

## Display GPIO list

The GPIO control script can be used to display the GPIO list. The names from this list should be used to manually control the GPIO in the following sections.

```bash
$ /srv/gpio.sh list
```

## GPIO set

The GPIO control script can be used to set a value to an output channel

Usage:
```bash
$ /srv/gpio.sh set IO_NAME [VALUE]
```

For digital output, the value can either be 0 or 1 (default 1).<br/>
For a PWM channel, value is the duty cycle in % (default 100).<br/>
For a LED, the value is the brightness (default max_brightness).<br/>

## GPIO reset

The GPIO control script can be used to reset the value of an output channel (typically turns off)

Usage:
```bash
$ /srv/gpio.sh reset IO_NAME
```

## GPIO get

The GPIO control script can be used to read the value of an input channel

Usage:
```bash
$ /srv/gpio.sh get IO_NAME
```

## GPIO watch

The GPIO control script can be used to Read the value of an input channel in an infinite loop

Usage:
```bash
$ /srv/gpio.sh watch IO_NAME [REFRESH_DELAY]
```
