
# Charger Controller supported insulation monitors

## Bender isoCHA425HV

Our charge controller offers out-of-the-box support for the Bender isoCHA425HV insulation monitoring device via RS485 communication. This seamless integration reduces development time and accelerates time to production for customers, ensuring reliable insulation monitoring and enhanced system safety.

The Bender isoCHA425HV integration is intended for use exclusively with DC charging pistols, such as CCS and CHAdeMO.

You can check how to enable this feature in the configuration section.

### Serial communication configuration

The Bender isoCHA425HV insulation monitor is configured from factory with the following serial communication parameters:

_Section 4.5.4 Configuring interface of the device manual_

- Baudrate: 9600 (1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200)
- Data bits: 8
- Parity: Even
- Stop bits: 1
- Address: 3 (3-90)

`insulation_monitor_stopbits`
You can choose `1` or `2` if the parity is set to `None`. If the parity is set to `Even` or `Odd`, you must select `1`. Section 4.5.4 Configuring interface of the device manual.
