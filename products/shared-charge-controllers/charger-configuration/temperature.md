# Temperature
Derate charge current option will apply a default profile for decreasing the output current depending on the temperature. The default profile can be found [**here**](../charger-features/secc_climate_control.md#interpolate-modes) . Stop charge temp threshold will stop the charge session if the temperature raises above the given threshold.

### Mode
3 possible temperature monitoring functions can be enabled:

- Cable derate current: Derate charge current option will apply a default profile for decreasing the output current depending on the temperature.
- Cable stop threshold: Stop charge temp threshold will stop the charge session if the temperature raises above the given threshold
- Monitor: allows monitoring of the temperature readings via CAN bus
