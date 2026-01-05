# SPCC Configuration Documentation

The SPCC is configurable via the Web UI. More information can be found [**here**](charge-controllers/advantics_os/csm-web-ui.md)

Alternatively, the configuration can be found in `/etc/advantics/default/config.cfg` file when accessing the controller via [ SSH ](charge-controllers/advantics_os/ssh.md).

## `Pistols` (default: MCS)
As the name suggests, on the single pistol charge controller (the SPCC), only one pistol can be enabled at a time.

<img src="assets/spcc-pistols.png" alt="SPCC pistols">
<figcaption style="text-align: center">SPCC pistols</figcaption>

## CCS DC Pistol

- **`Index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols Used to offset CAN addressing as well (default: `1`)
- **`Use Sequence Flags`**: Tells if flags in Sequence Control message of the Generic CAN interface should be used (default: `True`)
- **`Free Service`**: No description (default: `True`)
- **`Log Signature Details`**: No description (default: `False`)
- **`Skip Cable Check`**: Should not be used in production. (default: `False`)

### CAN Bus

- **`Charger Can Interface`**: No description (default: `can0`)
- **`Charger Type`**: No description (default: `Advantics_Generic DC_v2`)
- **`Charger Can Timeout ms`**: Timeout for reception of Power Modules Status message in generic interface (ms) (default: `500.0`)

### Charge Limits
- **`Min Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `500.0`)
- **`Min Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `120.0`)
- **`Min Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)

### Discharge Limits
- **`Min Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)

### Cable Limits
- **`Max Cable Voltage`**: Maximum voltage rated for the cable (default: `500.0`)
- **`Max Cable Current`**: Maximum current rated for the cable (default: `100.0`)
- **`Max Cable Power`**: Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided (default: `0.0`)
### Bidirectional Charging Extra Parameters
- **`Is Bidirectional`**: Whether this charger supports both charge and discharge (default: `False`)
- **`Limit Non Bidir To Positive Current`**: No description (default: `True`)
- **`Supports Range Mode`**: No description (default: `True`)

### Specific Charger Interface Extra Parameters
- **`Stack Pos`**: Stack position to use when working in conjonction with ADVANTICS power module (default: `0`)
- **`Llc Us External Voltage`**: Only for ADVANTICS power module (default: `0.0`)
- **`do Not Rearm After Fault`**: Only for ADVANTICS power module (default: `False`)

### CCS Params
- **`evse Id`**: identifier of the EVSE as used by OCCP communications (default: `33A51A0001`)
- **`enable Din`**: Whether DIN70121 communications are allowed (default: `True`)
- **`enable Iso Part2`**: Whether ISO15118-2 communications are allowed (default: `True`)
- **`enable Iso Part20`**: Whether ISO15118-20 communications are allowed (default: `False`)
- **`allow No Tls For Iso Part20`**: Whether we should accept communications without TLS on -20This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild (default: `False`)
- **`Current Ripple`**: No description (default: `1.0`)

## CCS AC Pistol

- **`Index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols Used to offset CAN addressing as well (default: `2`)
- **`Ignore PP`**: Ignore the values from Proximity Pilot (default: `True`)
- **`Use Sequence Flags`**: Tells if flags in Sequence Control message of the Generic CAN interface should be used (default: `True`)
- **`Is Ventilated`**: Some vehicles may require (by using CP State D instead of C) to be charging only in a ventilatedarea. If charger is not in a ventilated place, and vehicle requires ventilation, CP PWMgoes to 100%. (default: `True`)

### CAN Bus
- **`Charger Type`**: The type of CAN interfacer to communicate with your charger (default: `Advantics_Generic_AC_v2`)
- **`Charger Can Interface`**: No description (default: `can0`)
- **`Charger Can Timeout Ms`**: Timeout for reception of Power Modules Status message in generic interface (ms) (default: `500.0`)

### Phases, charger limits and cable limits
- **`Number Of Phases`**: Only used in OCPP GetCompositeSchedule (default: `3`)
- **`Max Charger Phase Current`**: The current threshold at which request the charger to cap,for every phase (default: `32.0`)
- **`Max Cable Phase Voltage`**: AC cable limits, per phase (default: `250.0`)
- **`Max Cable Phase Current`**: AC cable limits, per phase (default: `32.0`)
- **`Max Cable Phase Power`**: AC cable limits, per phase (default: `0.0`)

### Lock Parameters
- **`No Cable Lock`**: In case cable is detachable from charger side, or for R&D usage (default: `True`)
- **`Lock Feedback R Threshold`**: Threshold, in ohms, between locked and unlocked state (default: `100.0`)
- **`Lock Feedback Low Is Locked`**: There are various lock feedback mechanisms existing. The one provided as default here correspond to a simple Normally Open switch that will short to ground (ie. R~=0) when locked. (default: `True`)
- **`Lock Pulse Duration Ms`**: Time in milliseconds of the locking or unlocking pulses (default: `600.0`)


## CHAdeMO Pistol
- **`Index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols Used to offset CAN addressing as well  (default: `3`)
- **`Chademo Precharge`**: No description (default: `False`)
- **`use Sequence Flags`**: Tells if flags in Sequence Control message of the Generic CAN interface should be used (default: `True`)
- **`Support Welding Detection`**: Whether the charger supports welding detection (default: `True`)

### CAN Bus
- **`Charger Can Interface`**: No description (default: `can0`)
- **`Charger Type`**: No description (default: `Advantics_Generic_DC_v2`)
- **`Charger Can Timeout Ms`**: Timeout for reception of Power Modules Status message in generic interface (ms) (default: `500.0`)

### Charge Limits
- **`Min Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `500.0`)
- **`Min Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `120.0`)
- **`Min Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)

### Discharge Limits
- **`Min Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)

### Cable Limits
- **`Max Cable Voltage`**: Maximum voltage rated for the cable (default: `500.0`)
- **`Max Cable Current`**: Maximum current rated for the cable (default: `100.0`)
- **`Max Cable Power`**: Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided (default: `0.0`)

### Bidirectional Charging Extra Parameters
- **`Is Bidirectional`**: Whether this charger supports both charge and discharge (default: `False`)
- **`Limit Non Bidir To Positive Current`**: No description (default: `True`)
- **`Supports Range Mode`**: No description (default: `True`)

### Specific Charger Interface Extra Parameters
- **`Stack Pos`**: Stack position to use when working in conjonction with ADVANTICS power module (default: `0`)
- **`Llc Us External Voltage`**: Only for ADVANTICS power module (default: `0.0`)
- **`do Not Rearm After Fault`**: Only for ADVANTICS power module (default: `False`)

## MCS Pistol

- **`Index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols Used to offset CAN addressing as well  (default: `1`)
- **`use Sequence Flags`**: Tells if flags in Sequence Control message of the Generic CAN interface should be used (default: `True`)
- **`free Service`**: No description (default: `True`)
- **`Log Signature Details`**: No description (default: `False`)
- **`Skip Cable Check`**: Should not be used in production. (default: `False`)

### CAN Bus
- **`Charger Can Interface`**: No description (default: `can0`)
- **`Charger Type`**: No description (default: `Advantics_Generic DC_v2`)
- **`Charger Can Timeout ms`**: Timeout for reception of Power Modules Status message in generic interface (ms) (default: `500.0`)

### Charge Limits
- **`Min Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Voltage`**: This limit applies to in charge direction (current going to the vehicle) (default: `500.0`)
- **`Min Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Current`**: This limit applies to in charge direction (current going to the vehicle) (default: `120.0`)
- **`Min Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)
- **`Max Charger Power`**: This limit applies to in charge direction (current going to the vehicle) (default: `0.0`)

### Discharge Limits
- **`Min Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Voltage`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Current`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Min Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)
- **`Max Charger Discharge Power`**: This limit applies to the discharge direction (current coming from the vehicle) NB.: Use positive values (default: `0.0`)

### Cable Limits
- **`Max Cable Voltage`**: Maximum voltage rated for the cable (default: `500.0`)
- **`Max Cable Current`**: Maximum current rated for the cable (default: `100.0`)
- **`Max Cable Power`**: Maximum power rated for the cable, can be omitted (0) if max current / max voltage are already provided (default: `0.0`)

### Bidirectional Charging Extra Parameters
- **`Is Bidirectional`**: Whether this charger supports both charge and discharge (default: `False`)
- **`Limit Non Bidir To Positive Current`**: No description (default: `True`)
- **`Supports Range Mode`**: No description (default: `True`)

### Specific Charger Interface Extra Parameters
- **`Stack Pos`**: Stack position to use when working in conjonction with ADVANTICS power module (default: `0`)
- **`Llc Us External Voltage`**: Only for ADVANTICS power module (default: `0.0`)
- **`do Not Rearm After Fault`**: Only for ADVANTICS power module (default: `False`)

### MCS Params
- **`evse Id`**: identifier of the EVSE as used by OCCP communications (default: `33A51A0001`)
- **`allow No Tls For Iso Part20`**: Whether we should accept communications without TLS on -20This is prohibited by the standard, yet you should not expect this to be wideliy applied in the wild (default: `False`)
- **`Current Ripple`**: No description (default: `1.0`)






- **`System`** (`SystemConfig`): No description (default: `SystemConfig(update Index Path='/app/updates/update Index.json', staging Index Path='/app/updates/staging Index.json', artefact Folder='/app/updates/artefacts', enable Web Interface=True, web Interface Ip='0.0.0.0', web Interface Port=80, bundle Path='csm-front/build/client', update Script=UpdateScriptsConfig(ccs Secc='/srv/run-ccs-secc.sh update', ocpp Charge Point='/srv/run-ccs-secc.sh update'))`)



## `Logging`
  Configuration for the logging system.

- **`Use legacy logging`**: If enabled, applications will use the legacy logging system which is based on Docker log driver.. You should only use that if you had 3rd party applications based on ADVANTICS logs on the legacy system, or if you have an existing pipeline based Docker JSON driver.. If not, the new logging system is recommended as it features better performance and more advanced log management options
- **`Level`**: Minimum priority level to include in the logs. INFO is recommended for better performances (default: `INFO`)
- **`Compress`**: Whether to compress the logs. Highly recommended as without compression the history of logs you can store will be largely smaller (default: `True`)
- **`Use Rotation`**: Whether to use multiple files for logs. (default: `True`)
- **`Max File Size kb`**: max File Size if the size at which we should rotate, i.e., BEFORE compression. Size AFTER compression is going to be about 5 to 8% of that, depending on compression level (default: `100000`)
- **`Max Total Size kb`**: Maximum size taken by the logs. Once going beyond that, old logs are deleted (default: `200000`)
- **`Compression Level`**: Compression level for gzip, from 1 to 9. (default: `1`)
- **`Verbose`**: Verbose means that the logger will print some info to stdout when compressing and rotating logs. These messages will be shown by docker log, unlike the actual logs. (default: `True`)

## `Hardware`
Allows configuration of the controller IOs.

- **`Digital Input 1`**: Defines the function controlled by digital input 1 (default: `Not Connected`)
- **`Digital Input 2`**: Defines the function controlled by digital input 2 (default: `Not Connected`)
- **`Digital Input 3`**: Defines the function controlled by digital input 3 (default: `Not Connected`)
- **`Digital Input 4`**: Defines the function controlled by digital input 4 (default: `Not Connected`)
- **`Digital Output 1`**: Defines the function controlled by digital output 1 (default: `Not Connected`)
- **`Digital Output 2`**: Defines the function controlled by digital output 2 (default: `Not Connected`)
- **`Digital Output 3`**: Defines the function controlled by digital output 3 (default: `Not Connected`)
- **`Digital Output 4`**: Defines the function controlled by digital output 4 (default: `Not Connected`)


## `System`
- **`enable Web Interface`**: Makes the administration web interface available (default: `True`)
- **`web Interface Ip`**: IP address for the web interface (default: `0.0.0.0`)
- **`web Interface Port`**: Port for the web interface (default: `80`)

## `OCPP`
- **`enabled`**: Enables support for OCPP on this controller (default: `False`)
- **`Connection Url`**: No description (default: ``)
- **`version`**: No description (default: `1.6`)
- **`Server Uses Self Signed Certificate`**: Whether we should accept self-signed certificates for TLS. Self-signed certificates are useful for testing, however, using this in production might create a security risk (default: `False`)
- **`ping Timeout`**: No description (default: `20.0`)
- **`Connection Timeout`**: Timeout for websocket, do not confuse with ConnectionTimeout (default: `30.0`)
- **`Connection Retry Delay`**: No description (default: `60.0`)
### `Core`
    Core parameters for OCPP

- **`authorization Cach Enabled`**: No description (default: `True`)
- **`authorize Remote Tx Requests`**: No description (default: `False`)
- **`Clock Aligned Data Interval`**: No description (default: `900.0`)
- **`Connection Time Out`**: No description (default: `300.0`)
- **`get Configuration Max_keys`**: No description (default: `1000`)
- **`heartbeat Interval`**: No description (default: `86400`)
- **`Meter Values Aligned Data`**: No description (default: `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC`)
- **`Meter Values Sampled Data`**: No description (default: `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC`)
- **`Meter Value Sample Interval`**: No description (default: `300.0`)
- **`Number Of Connectors`**: No description (default: `3`)
- **`Stop Transaction On Invalid Id`**: No description (default: `True`)
- **`web Socket Ping Interval`**: No description (default: `20.0`)
- **`Message Timeout`**: No description (default: `30.0`)
- **`Connector Phase Rotation`**: No description (default: `0.Unknown,1.NotApplicable,2.Unknown,3.NotApplicable`)
- **`reset Retries`**: No description (default: `0`)
- **`Stop Transaction O E V Side Disconnect`**: No description (default: `True`)
- **`unlock Connector O E V Side Disconnect`**: No description (default: `False`)
- **`Supported Feature Profiles`**: No description (default: `Core,LocalAuthListManagement,Reservation`)
- **`transaction Message Attempts`**: No description (default: `3`)
- **`transaction Message Retry Interval`**: No description (default: `10.0`)

### `Local Auth`
    Authentication related parameters

- **`Local Auth Lis Enabled`**: No description (default: `False`)
- **`Local Auth List Max Length`**: No description (default: `1000`)
- **`Send Local List Max Length`**: No description (default: `1000`)

### `Reservation`
    Reservation related parameters

- **`reserve Connector_zero Supported`**: No description (default: `False`)

### `OcppV16SmartCharging`
    Smart charging parameters

- **`Charge Profile Max Stack Level`**: No description (default: `100`)
- **`Charging Schedule Allowed Charging Rate Unit`**: No description (default: `Current,Power`)
- **`Charging Schedule Max Periods`**: No description (default: `1000.0`)
- **`Connector Switch_3 To_1 Phase Supported`**: No description (default: `False`)
- **`Max Charging Profiles Installed`**: No description (default: `1000`)
- **`target Current`**: No description (default: `0.0`)
- **`allow Limiting To_zero`**: No description (default: `False`)
- **`update Interval`**: No description (default: `30.0`)
- **`Ignore Sequence Flags For Ocpp Availability`**: No description (default: `False`)
- **`Inoperative Pistols`** : Persistent data about inoperative pistols (default: `[]`)

## `TLS`

  - **`enabled`**: Whether TLS is enabled. (default: `True`)
  - **`allow No Cert`**: Allow no certificate verification. (default: `True`)
  - **`allow Iso_20 Without Tls`**: Allow ISO 20 communication without TLS. (default: `True`)

### `Server`
- **`Ca File`**: Path to the CA certificate file. (default: `/app/certs/CA.pem`)
- **`keyfile`**: Path to the server key file. (default: `/app/certs/server.key`)
- **`Server Certificate`**: Path to the server certificate file. (default: `/app/certs/server.pem`)
- **`Server Certificate Chain`**: Path to the server certificate chain (default: ``)
- **`keyfile Passphrase`**: Passphrase for your server certificate, if any (default: ``)

## `Temperature`
Derate charge current option will apply a default profile for decreasing the output current depending on the temperature. The default profile can be found [**here**](charge-controllers/secc_climate_control.md#interpolate-modes) . Stop charge temp threshold will stop the charge session if the temperature raises above the given threshold.

### Mode
3 possible temperature monitoring functions can be enabled:
- Cable derate current: Derate charge current option will apply a default profile for decreasing the output current depending on the temperature.
- Cable stop threshold: Stop charge temp threshold will stop the charge session if the temperature raises above the given threshold
- Monitor: allows monitoring of the temperature readings via CAN bus