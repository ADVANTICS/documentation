> [!UPDATE] {docsify-updated}
# MCS

These configuration entries are all under the `[ccs]` section.

## full_soc

<figcaption>Example</figcaption>

    full_soc = 100

Value in percent we consider to be a full state of charge.

Default to 100 %.

## bulk_soc

<figcaption>Example</figcaption>

    bulk_soc = 80

Value in percent we consider to be a bulk state of charge.

Default to 80 %.

## cabin_conditioning

<figcaption>Example</figcaption>

    cabin_conditioning = true

Tells charger if the energy it provides is also used for cabin cabin conditioning.

Default to false.

## ress_conditioning

<figcaption>Example</figcaption>

    ress_conditioning = true

Tells charger if the energy it provides is also used for battery conditioning.

Default to false.

## allow_dynamic_power_limits

<figcaption>Example</figcaption>

    allow_dynamic_power_limits = true

Allows charger to change its power limits (including max current) while charging, without going
through a charge parameters renegotiation phase.

Default to true.

## current_demand_timeout_ms

<figcaption>Example</figcaption>

    current_demand_timeout_ms = 2000

Set the current demand timeout in milliseconds. When triggered, the charge is stopped.

MCS standards specify it should be 250 ms. However, we believe it is needlessly too strict, and some
chargers can actually fail it from time to time. Heavy noise conditions can also make this timeout
trigger spuriously. Hence, we rather default to 2 seconds instead of 250 ms.

Default to 2000 ms.