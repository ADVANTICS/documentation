# OCPP

Advantics charge controllers can provide OCPP functionality. Please refer to the [**OCPP documentation**](../charger-features/ocpp16j.md) for more details on the application.
&nbsp;

By default, OCPP is disabled. To enable it, you need to at least set the `enabled`
and `connection_url` in the `ocpp` section of the config file.

    [ocpp]
    enabled = true
    connection_url = ws://your-ocpp-endpoint.example.com/your/ocpp/path/charge-point-id                  

-   In `connection_url` replace `charge-point-id` with the id this
    charge point should identify as.

OCPP Options that are specified in the OCPP standard (e.g.
`AuthorizationCacheEnabled`) are grouped in config sections according to
the OCPP feature profile they belong to (e.g.
`AuthorizationCacheEnabled` is used as part of the core feature profile
and is thus configured in section `ocpp:1.6_core`). Names for OCPP
options are case-sensitive. Some examples include

    [ocpp:1.6_core]
    AuthorizationCacheEnabled = true
    ...

    [ocpp:1.6_local_auth]
    LocalAuthListEnabled = false
    ...

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

## `[ocpp]`

The connection to the central system, and whether OCPP runs at all.

- **`connection_retry_delay`**: Only when `enabled` = `true` (default: `60.0`)
{: #connection_retry_delay }
- **`connection_timeout`**: Timeout for websocket, do not confuse with ConnectionTimeout. Only when `enabled` = `true` (default: `30.0` s)
{: #connection_timeout }
- **`connection_url`**: Endpoint URL of the OCPP server. Only when `enabled` = `true` (default: *(empty)*)
{: #connection_url }
- **`enable_test_rpc`**: Enables a tiny OCPP RPC simulator that can be used from the web interface. WARNING: do not enable this if you have your own RPC, as they would likely collide (default: `false`)
{: #enable_test_rpc }
- **`enabled`**: Enables support for OCPP on this controller (default: `false`)
{: #enabled }
- **`ignore_sequence_flags_for_ocpp_availability`**: Only when `enabled` = `true` (default: `false`)
{: #ignore_sequence_flags_for_ocpp_availability }
- **`inoperative_pistols`**: Persistent data about inoperative pistols. Only when `enabled` = `true` (default: *(empty)*)
{: #inoperative_pistols }
- **`management_dealer_endpoint`**: Dealer endpoint for the management RPC (default: `tcp://*:60501`) **advanced**
{: #management_dealer_endpoint }
- **`management_router_endpoint`**: Router endpoint for the management RPC (default: `tcp://*:60500`) **advanced**
{: #management_router_endpoint }
- **`ping_timeout`**: Only when `enabled` = `true` (default: `20.0` s)
{: #ping_timeout }
- **`protocol_order`**: List of targeted OCPP versions in preference order. Used as the `subprotocols` in the websockets communications. The central server should respect the order, if supported, according to RFC 6455. Examples: Using [2.0.1, 1.6] will ask to use preferrably 2.0.1 but accept to downgrade to 1.6. Using [1.6] will refuse to use 2.0.1 even if the central server supports it. One of `1.6`, `2.0.1`. Only when `enabled` = `true` (default: `['1.6']`)
{: #protocol_order }
- **`resend_ev_needs_on_limits_changed`**: (OCPP 2.0.1 only). Whether NotifyEVNeeds should be resent when EV updates its limits in the middle of a transaction. NotifyEVNeeds is always sent at the beginning of a transaction for dynamic charging, and can be re-triggered while being in the transaction if the limits change depending on this parameter. This is required by the standard and should be the default. However, when managing schedule on the CSMS side (i.e. CSMS sends a new schedule on each new setpoint), if the EV incorporates the charger side limit in its own reported limit, you can get an infinite feedback loop where the CSMS keeps re-adjusting its own setpoints. In that case, you might consider using this. Only when `enabled` = `true` (default: `true`)
{: #resend_ev_needs_on_limits_changed }
- **`server_uses_self_signed_certificate`**: Whether we should accept self-signed certificates for TLS. Self-signed certificates are useful for testing, however, using this in production might create a security risk. Only when `enabled` = `true` (default: `false`)
{: #server_uses_self_signed_certificate }

## `[ocpp:1.6_core]`

The OCPP 1.6 Core profile keys. Names are the ones from the OCPP specification and are case-sensitive.

- **`AuthorizationCacheEnabled`**: default `true`
{: #AuthorizationCacheEnabled }
- **`AuthorizeRemoteTxRequests`**: default `false`
{: #AuthorizeRemoteTxRequests }
- **`BootNotificationOverwriteChargePointFirmwareVersion`**: default *(empty)* **advanced**
{: #BootNotificationOverwriteChargePointFirmwareVersion }
- **`BootNotificationOverwriteChargePointModel`**: default *(empty)* **advanced**
{: #BootNotificationOverwriteChargePointModel }
- **`BootNotificationOverwriteChargePointSerialNumber`**: default *(empty)* **advanced**
{: #BootNotificationOverwriteChargePointSerialNumber }
- **`BootNotificationOverwriteChargePointVendor`**: default *(empty)* **advanced**
{: #BootNotificationOverwriteChargePointVendor }
- **`ClockAlignedDataInterval`**: default `900.0` ms
{: #ClockAlignedDataInterval }
- **`ConnectionTimeOut`**: default `300.0` ms
{: #ConnectionTimeOut }
- **`ConnectorPhaseRotation`**: default `0.Unknown,1.NotApplicable,2.Unknown,3.NotApplicable`
{: #ConnectorPhaseRotation }
- **`GetConfigurationMaxKeys`**: default `1000`
{: #GetConfigurationMaxKeys }
- **`HeartbeatInterval`**: default `86400` ms **advanced**
{: #HeartbeatInterval }
- **`MessageTimeout`**: default `30.0` s **advanced**
{: #MessageTimeout }
- **`MeterValueSampleInterval`**: default `300.0`
{: #MeterValueSampleInterval }
- **`MeterValuesAlignedData`**: default `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC`
{: #MeterValuesAlignedData }
- **`MeterValuesSampledData`**: default `Current.Import,Current.Offered,Energy.Active.Import.Register,Power.Active.Import,Power.Offered,SoC`
{: #MeterValuesSampledData }
- **`NumberOfConnectors`**: default `3`
{: #NumberOfConnectors }
- **`ResetRetries`**: default `0`
{: #ResetRetries }
- **`StopTransactionOnEVSideDisconnect`**: default `true`
{: #StopTransactionOnEVSideDisconnect }
- **`StopTransactionOnInvalidId`**: default `true`
{: #StopTransactionOnInvalidId }
- **`SupportedFeatureProfiles`**: default `Core,LocalAuthListManagement,Reservation` **advanced**
{: #SupportedFeatureProfiles }
- **`TransactionMessageAttempts`**: default `3` **advanced**
{: #TransactionMessageAttempts }
- **`TransactionMessageRetryInterval`**: default `10.0` s **advanced**
{: #TransactionMessageRetryInterval }
- **`UnlockConnectorOnEVSideDisconnect`**: default `false`
{: #UnlockConnectorOnEVSideDisconnect }
- **`WebSocketPingInterval`**: default `20.0` s **advanced**
{: #WebSocketPingInterval }

## `[ocpp:1.6_local_auth]`

Local authorisation list management.

- **`LocalAuthListEnabled`**: default `false`
{: #LocalAuthListEnabled }
- **`LocalAuthListMaxLength`**: default `1000`
{: #LocalAuthListMaxLength }
- **`SendLocalListMaxLength`**: default `1000`
{: #SendLocalListMaxLength }

## `[ocpp:1.6_reservation]`

Reservation profile.

- **`ReserveConnectorZeroSupported`**: default `false`
{: #ReserveConnectorZeroSupported }

## `[ocpp:1.6_smart_charging]`

Smart charging profile.

- **`ChargeProfileMaxStackLevel`**: default `100`
{: #ChargeProfileMaxStackLevel }
- **`ChargingScheduleAllowedChargingRateUnit`**: default `Current,Power`
{: #ChargingScheduleAllowedChargingRateUnit }
- **`ChargingScheduleMaxPeriods`**: default `1000.0`
{: #ChargingScheduleMaxPeriods }
- **`ConnectorSwitch3to1PhaseSupported`**: default `false`
{: #ConnectorSwitch3to1PhaseSupported }
- **`MaxChargingProfilesInstalled`**: default `1000`
{: #MaxChargingProfilesInstalled }
- **`TargetCurrent`**: default `0.0` A
{: #TargetCurrent }
- **`allow_limiting_to_zero`**: default `false`
{: #allow_limiting_to_zero }
- **`update_interval`**: default `30.0` s
{: #update_interval }

## `[ocpp:tls]`

TLS towards the central system. This is separate from the TLS used with vehicles, which is on the [TLS page](tls.md).

- **`check_hostname`**: Whether the charge point should check hostname of the CA file. Should only be disabled for local testing (default: `false`)
{: #check_hostname }
