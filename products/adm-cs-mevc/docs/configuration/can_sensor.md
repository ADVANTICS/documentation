# CAN sensor

To measure voltages before and after DC contactors (ie. inlet and battery voltages), as well as to
measure the amount of current flowing, Advantics controller can support some particular CAN sensor
available on the market. Advantics even resell some of those as convenience package when ordering a
PEV controller to quickly get started.

The advantage is that you don't have to provide these information yourself through this generic
interface. Which can mean you don't have to implement yourself the reading of such sensors.

These configuration entries are all under the `[vehicle]` section.

## Isabellenhutte IVT-S sensors

To use an Isabellenhutte IVT-S sensor, configure it in the following way:

    use_can_sensor = Isabellenhutte IVT-S

- **`use_can_sensor`**: Which CAN sensor the controller should read the voltages and current from
{: #use_can_sensor }
- **`can_sensor_if`**: CAN interface the sensor is wired to (default: `can0`) **advanced**
{: #can_sensor_if }
- **`ivt_init_timeout_s`**: How long to wait for the sensor to answer during start-up reconfiguration before faulting **advanced**
{: #ivt_init_timeout_s }

It is currently not possible to configure which channel correspond to which voltage, or the current
reading polarity. Here is how you should wire this sensor:

* Battery voltage goes between `REF` (DC -) and `V1` (DC +)
* Inlet voltage is a differential reading of `V2 - V3`
* Current is measured on the return path (DC -)

!!! note
    Upon start-up, Advantics controller WILL reconfigure the sensor as it sees fit.
