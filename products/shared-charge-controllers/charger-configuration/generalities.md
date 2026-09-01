# Applications, logging, hardware and system

These are the sections that configure the controller itself rather than a charging
connector: which applications log what, what the digital IOs do, and how the web interface
is reached.

## `[applications]`

Here you can change the logging level of the applications running.

    [applications]
    log_level = INFO

- **`log_level`**: Log level applied to every application. `DEBUG`, `INFO`, `WARNING`, `ERROR` or `CRITICAL` (default: `INFO`)
{: #log_level }
- **`persistent_data`**: Directory where applications keep data that must survive a restart (default: `/var/advantics/`)
{: #persistent_data }

## `[logging]`

Configuration for the logging system.

- **`use_legacy_logging`**: If enabled, applications will use the legacy logging system which is based on the Docker log driver. You should only use that if you had 3rd party applications based on ADVANTICS logs on the legacy system, or if you have an existing pipeline based on the Docker JSON driver. If not, the new logging system is recommended as it features better performance and more advanced log management options (default: `true`)
{: #use_legacy_logging }
- **`level`**: Minimum priority level to include in the logs. INFO is recommended for better performances (default: `INFO`)
{: #level }
- **`compress`**: Whether to compress the logs. Highly recommended as without compression the history of logs you can store will be largely smaller (default: `true`)
{: #compress }
- **`use_rotation`**: Whether to use multiple files for logs (default: `true`)
{: #use_rotation }
- **`max_file_size_kb`**: The size at which a log file is rotated, i.e. BEFORE compression. Size AFTER compression is going to be about 5 to 8% of that, depending on compression level (default: `100000`)
{: #max_file_size_kb }
- **`max_total_size_kb`**: Maximum size taken by the logs. Once going beyond that, old logs are deleted (default: `200000`)
{: #max_total_size_kb }
- **`compression_level`**: Compression level for gzip, from 1 to 9 (default: `1`)
{: #compression_level }
- **`verbose`**: Verbose means that the logger will print some info to stdout when compressing and rotating logs. These messages will be shown by `docker logs`, unlike the actual logs (default: `true`)
{: #verbose }
- **`max_lag`**: Maximum time, in seconds, a log line may wait before being written out **advanced** (default: `1.0`)
{: #max_lag }

## `[hardware]`

In this section, you can configure the controller version as well as the
digital inputs and outputs.

!!! note
    Digital inputs and outputs can be interfaced via the generic interface. Check section
    [**Controller IOs on CAN**](../charger-features/secc_can_ios.md#controllers-ios-on-can).

The following is an example:

    [hardware]
    # dig_inX possible values: CHAdeMO_Start, Stop, Monitor, Not_Connected
    dig_in1 = CHAdeMO_Start
    dig_in2 = Stop
    dig_in3 = Monitor
    dig_in4 = Not_Connected

- **`dig_in1`** … **`dig_in4`**: Defines the function controlled by each digital input (default: `Not_Connected`)
{: #dig_in1 }
- **`dig_out1`** … **`dig_out4`**: Defines the function driven on each digital output (default: `Not_Connected`)
{: #dig_out1 }
- **`led1`** … **`led3`**: Defines what each status LED indicates (default: `Not_Connected`)
{: #led1 }
- **`temperature_filter_window`**: Number of samples averaged when filtering a temperature reading **advanced** (default: `5`)
{: #temperature_filter_window }

!!! note "`version` is set at the factory"
    `[hardware] version` identifies the controller model and is provisioned with the unit. It
    is not an integration setting; changing it makes the controller drive the wrong hardware.

## `[system]`

- **`enable_web_interface`**: Makes the administration web interface available (default: `true`)
{: #enable_web_interface }
- **`web_interface_ip`**: IP address for the web interface (default: `0.0.0.0`)
{: #web_interface_ip }
- **`web_interface_port`**: Port for the web interface (default: `80`)
{: #web_interface_port }
