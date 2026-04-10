> [!UPDATE] {docsify-updated}

# MCS

These configuration entries are all under the `[ccs]` section.
MCS requires using [Generic EVCC CAN Interface 2](charge-controllers/evcc_generic/README_v2) in [vehicle type](charge-controllers/evcc_configuration/generalities).

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

## wait_hv_ready_timeout_ms

<figcaption>Example</figcaption>

    wait_hv_ready_timeout_ms = 40000

Timeout (milliseconds) for waiting for high-voltage system readiness. If exceeded, the session will abort.

## dynamic_target_voltage

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    dynamic_target_voltage = false

When enabled, the target voltage sent to the charger during the current delivery loop is updated
dynamically from the vehicle CAN interface (e.g. from a BMS signal), rather than using the static
`target_voltage` config value. This allows the charger setpoint to track the actual battery voltage
as the state of charge evolves, which can be useful for Constant Voltage phases or more sophisticated
charge profiles.

Default to false.

## allow_bpt_at_full_soc

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    allow_bpt_at_full_soc = false

When enabled, a bidirectional power transfer (BPT / V2G) session will not be terminated solely
because the state of charge has reached 100 %. This allows the vehicle to keep cycling power
(discharge followed by recharge) until the user or the charger explicitly stops the session.

Only relevant when `is_bidirectional` is set to `true`.

Default to false.

## mcs_ce_id_use_median_filter

> [!WARNING]
> Using the median filter and the debouncer simultaneously, setting a large `mcs_ce_id_filter_buffer_size`,
> or setting a high `mcs_ce_id_debouncer_count` will increase the latency of CE and ID state change
> detection. This can cause the MCS state machine to miss time-sensitive transitions, potentially
> triggering sequence timeouts and abnormal session terminations. Tune these parameters conservatively.

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_use_median_filter = false

Enables a median filter on the CE and ID line readings. The median filter smooths
out short glitches or noise spikes by returning the median value over a rolling window of samples,
rather than acting on every raw reading immediately. The window size is controlled by
`mcs_ce_id_filter_buffer_size`.

Default to false.

## mcs_ce_id_filter_buffer_size

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_filter_buffer_size = 5

Number of samples in the rolling window used by the median filter on CE and ID line readings.
A larger window provides stronger noise rejection at the cost of a slightly slower response to
genuine state changes. Only effective when `mcs_ce_id_use_median_filter` is set to `true`.

Default to 5.

## mcs_ce_id_use_debouncer

> [!WARNING]
> Using the median filter and the debouncer simultaneously, setting a large `mcs_ce_id_filter_buffer_size`,
> or setting a high `mcs_ce_id_debouncer_count` will increase the latency of CE and ID state change
> detection. This can cause the MCS state machine to miss time-sensitive transitions, potentially
> triggering sequence timeouts and abnormal session terminations. Tune these parameters conservatively.


> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_use_debouncer = false

Enables a debouncer on the CE and ID line readings. Instead of accepting a new state on the first
observation, the debouncer requires the same value to be seen a configurable number of times
consecutively (see `mcs_ce_id_debouncer_count`) before the state change is accepted. This helps
reject transient noise or bouncing on the physical lines.

Default to false.

## mcs_ce_id_debouncer_count

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_debouncer_count = 3

Number of consecutive identical readings required before the debouncer accepts a CE or ID state
change. A higher value makes the debouncer more conservative and resistant to noise, but also
increases the latency before a genuine transition is acted upon. Only effective when
`mcs_ce_id_use_debouncer` is set to `true`.

Default to 3.
