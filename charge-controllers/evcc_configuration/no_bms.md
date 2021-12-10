> [!UPDATE] {docsify-updated}
# No BMS mode

> [!ATTENTION]
> No BMS mode should NEVER be used in normal conditions.

This is a special mode intended ONLY for testing or prototyping purposes. It allows you to not have
to use a BMS (or not have to develop a bridge between our generic interface and the BMS protocol).
The intended goal of this mode is to help you evaluate our controller and reach a demonstrative
working charge in a short time span.

Normally, a BMS provide safe current request values with respect to the present state of charge of
the battery. No BMS mode works by charging at a specific and static current, and automatically stops
once a certain voltage is reached.

> [!WARNING]
> It is *paramount* that you pick *sane and safe voltage and current settings* for this!
> Charging a battery at too high current and/or above a certain voltage level can result in a
> catastrophic event.

The voltage to not charge over is to be configured with entry `max_charge_voltage`. When reaching
this voltage, charge will be cut-off immediately. This is different from entry [max_voltage](charge-controllers/evcc_configuration/generalities.md#max_voltage) as
that one is for specifying the true maximum voltage of the battery when full (some commercial cars
even use values higher than the actual one). Though, both can have the same value, provided it is a
pretty low and safe one.

The amount of current used will correspond to entry [max_current](charge-controllers/evcc_configuration/generalities.md#max_current). Use a reasonably low value.

> [!TIP]
> Use a partially discharged battery (one with a present voltage well below
> `max_charge_voltage`). This is safer, and will make the demonstrative charge last longer.

Example: For a classic 403 V EV battery pack, a safe maximum charge voltage when not using a BMS
would be 380 V. The current can be something like 20 A.

    no_bms = true
    max_charge_voltage = 380
    max_current = 20

    # Other typical settings (these won't affect the safe charge cut-off voltage)
    max_voltage = 450
    target_voltage = 410

`no_bms` default to false.

`max_charge_voltage` is optional (ie. default to 0) when `no_bms` is false. However, it becomes
required (ie. non-zero value) if `no_bms` is true. Advantics controller also checks that
`max_charge_voltage` is not configured to a value greater than `max_voltage`.
