# Hardware, applications and system

The sections on this page configure the controller itself rather than a charging session:
what its digital IOs and LEDs do, how much it logs, and how its web interface is reached.

!!! note "Names are what you write in the file"
    These are the option names exactly as `/srv/config.cfg` expects them. The Web UI displays
    them as capitalised labels; writing a label into the file does **not** work -- the option
    is ignored without any error and the built-in default applies.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

## `[hardware]`

The digital inputs, digital outputs and LEDs are assigned a *function* rather than a level.
The same functions are also reachable over the CAN interface -- see
[Controller IOs on CAN](../vehicle-can-interfaces/can_v2.md).

- **`auto_sleep`**: If enabled the EVCC will go to sleep automatically when reaching an IDLE state. It will be woken up on the next pistol plug. This can help reducing 24V power consumption when idle (default: `false`)
{: #auto_sleep }
- **`dig_in1`**: Function assigned to digital input 1. One of `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` (default: `Not_Connected`)
{: #dig_in1 }
- **`dig_in2`**: Function assigned to digital input 2. One of `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` (default: `Not_Connected`)
{: #dig_in2 }
- **`dig_in3`**: Function assigned to digital input 3. One of `Not_Connected`, `Stop`, `Emergency_Stop`, `Sleep`, `Monitor` (default: `Not_Connected`)
{: #dig_in3 }
- **`dig_out1`**: Function assigned to digital output 1. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Plugged_In`)
{: #dig_out1 }
- **`dig_out2`**: Function assigned to digital output 2. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Not_Connected`)
{: #dig_out2 }
- **`dig_out3`**: Function assigned to digital output 3. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Not_Connected`)
{: #dig_out3 }
- **`led1`**: Function assigned to LED 1. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Not_Connected`)
{: #led1 }
- **`led2`**: Function assigned to LED 2. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Not_Connected`)
{: #led2 }
- **`led3`**: Function assigned to LED 3. One of `Not_Connected`, `Plugged_In`, `CAN_Controlled`, `Contactor_Enable` (default: `Not_Connected`)
{: #led3 }
- **`plugged_in_pulse_ms`**: Duration of the Plugged_In output pulse. By default (0) the output configured as Plugged_In latches HIGH on plug-in and stays HIGH for the whole charge session. Set a non-zero value to instead emit a single pulse of this length (in ms) on the plug-in rising edge, then return LOW. This is useful to wake up a vehicle VCU on connection without keeping it powered for the entire session, avoiding LV battery drain during long charges (default: `0` ms)
{: #plugged_in_pulse_ms }
- **`temperature_filter_window`**: Size of the median filter window for temperature readings (default: `5`) **advanced**
{: #temperature_filter_window }

!!! note "`version` is set at the factory"
    `[hardware] version` identifies the controller model and is provisioned with the unit. It
    is not an integration setting; changing it makes the controller drive the wrong hardware.

## `[applications]`

- **`log_level`**: Verbosity of the application logging. One of `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` (default: `INFO`)
{: #log_level }
- **`persistent_data`**: default `/var/advantics/` **advanced**
{: #persistent_data }

## `[system]`

- **`enable_web_interface`**: Makes the administration web interface available (default: `true`)
{: #enable_web_interface }
- **`web_interface_ip`**: IP address the http server for the web interface will be bound to. This is not used to set the IP of the controller itself 0.0.0.0 means it will accept connection to any IP used by the controller, and should be the default unless you know what you are doing (default: `0.0.0.0`) **advanced**
{: #web_interface_ip }
- **`web_interface_port`**: Port for the web interface (default: `80`)
{: #web_interface_port }

## `[ev]`

Identifiers the vehicle presents to the charger. The two are separate because ISO 15118-2 and
ISO 15118-20 do not use the same format.

- **`id`**: default `33A51A0001AA`
{: #id }
- **`id_part20`**: default `VFRVO123456789ABCDEF`
{: #id_part20 }
