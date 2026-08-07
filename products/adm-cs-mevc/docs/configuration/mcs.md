# MCS

These configuration entries are under the `[ccs]` section — the MCS stack reuses the CCS
configuration section, so there is no `[mcs]` section. The two exceptions are marked as such below.

MCS requires using [Generic EVCC CAN Interface 2](../vehicle-can-interfaces/README_v2.md) in [vehicle type](generalities.md).

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

!!! warning "This entry is in the `[vehicle]` section"
    Despite being documented here with the rest of the charge-session settings, this entry belongs to
    `[vehicle]`, not `[ccs]`. Put it under `[ccs]` and it is silently ignored.

!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    dynamic_target_voltage = false

When enabled, the target voltage sent to the charger during the current delivery loop is updated
dynamically from the vehicle CAN interface (e.g. from a BMS signal), rather than using the static
`target_voltage` config value. This allows the charger setpoint to track the actual battery voltage
as the state of charge evolves, which can be useful for Constant Voltage phases or more sophisticated
charge profiles.

Default to false.

## allow_bpt_at_full_soc

!!! warning "This entry is in the `[vehicle]` section"
    Despite being documented here with the rest of the charge-session settings, this entry belongs to
    `[vehicle]`, not `[ccs]`. Put it under `[ccs]` and it is silently ignored.

!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    allow_bpt_at_full_soc = false

When enabled, a bidirectional power transfer (BPT / V2G) session will not be terminated solely
because the state of charge has reached 100 %. This allows the vehicle to keep cycling power
(discharge followed by recharge) until the user or the charger explicitly stops the session.

Only relevant when `is_bidirectional` is set to `true`.

Default to false.

## mcs_ce_id_use_median_filter

!!! warning
    Using the median filter and the debouncer simultaneously, setting a large `mcs_ce_id_filter_buffer_size`,
    or setting a high `mcs_ce_id_debouncer_count` will increase the latency of CE and ID state change
    detection. This can cause the MCS state machine to miss time-sensitive transitions, potentially
    triggering sequence timeouts and abnormal session terminations. Tune these parameters conservatively.

!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_use_median_filter = false

Enables a median filter on the CE and ID line readings. The median filter smooths
out short glitches or noise spikes by returning the median value over a rolling window of samples,
rather than acting on every raw reading immediately. The window size is controlled by
`mcs_ce_id_filter_buffer_size`.

Default to false.

## mcs_ce_id_filter_buffer_size

!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_filter_buffer_size = 5

Number of samples in the rolling window used by the median filter on CE and ID line readings.
A larger window provides stronger noise rejection at the cost of a slightly slower response to
genuine state changes. Only effective when `mcs_ce_id_use_median_filter` is set to `true`.

Default to 5.

## mcs_ce_id_use_debouncer

!!! warning
    Using the median filter and the debouncer simultaneously, setting a large `mcs_ce_id_filter_buffer_size`,
    or setting a high `mcs_ce_id_debouncer_count` will increase the latency of CE and ID state change
    detection. This can cause the MCS state machine to miss time-sensitive transitions, potentially
    triggering sequence timeouts and abnormal session terminations. Tune these parameters conservatively.


!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_use_debouncer = false

Enables a debouncer on the CE and ID line readings. Instead of accepting a new state on the first
observation, the debouncer requires the same value to be seen a configurable number of times
consecutively (see `mcs_ce_id_debouncer_count`) before the state change is accepted. This helps
reject transient noise or bouncing on the physical lines.

Default to false.

## mcs_ce_id_debouncer_count

!!! note
    This is an advanced configuration option.

<figcaption>Example</figcaption>

    mcs_ce_id_debouncer_count = 3

Number of consecutive identical readings required before the debouncer accepts a CE or ID state
change. A higher value makes the debouncer more conservative and resistant to noise, but also
increases the latency before a genuine transition is acted upon. Only effective when
`mcs_ce_id_use_debouncer` is set to `true`.

Default to 3.

## `[t1s_driver]`

On controllers fitted with a 10BASE-T1S interface, this section configures it.

- **`mac_address`**: default `advantics-serial` **advanced**
{: #mac_address }

## Other entries

The rest of the `[ccs]` section, generated from the controller software so that names,
defaults and units cannot drift from it. Most of these are protocol timeouts you will not
need to touch; they exist for interoperability work against a stubborn vehicle or charger.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

- **`ac_enabled`**: Whether the AC charging interface is allowed to operate (default: `true`)
{: #ac_enabled }
- **`authorization_setup_timeout_ms`**: default `2000` ms **advanced**
{: #authorization_setup_timeout_ms }
- **`authorization_timeout_ms`**: default `2000` ms **advanced**
{: #authorization_timeout_ms }
- **`cable_check_process_timeout_s`**: default `40` s **advanced**
{: #cable_check_process_timeout_s }
- **`communication_setup_timeout_s`**: default `20` s **advanced**
{: #communication_setup_timeout_s }
- **`enable_pnc`**: Whether Plug and Charge (PnC) should be enabled (default: `false`) **advanced**
{: #enable_pnc }
- **`hold_off_until_bms_ready`**: When True, the session will always be held off at Connected_With_Full_Info stage until the vehicle BMS starts sending CAN messages and explicitly clears the hold-off signal (using EV_Status message). This prevents proceeding to the powered states before the vehicle internal equipment has finished preparing/waking up after init/sleep. The wait is bounded by wait_hv_ready_timeout_ms (default: `false`) **advanced**
{: #hold_off_until_bms_ready }
- **`ignore_id_change`**: Whether to ignore changes in the ID line (which can be caused by noise) only for testing purposes. Supported only for MCS (default: `false`) **advanced**
{: #ignore_id_change }
- **`log_signature_details`**: default `false` **advanced**
{: #log_signature_details }
- **`mcs_ce_id_enable_extended_logging`**: Whether to enable extended logging for CE ID readings (default: `false`) **advanced**
{: #mcs_ce_id_enable_extended_logging }
- **`payment_details_timeout_ms`**: default `5000` ms **advanced**
{: #payment_details_timeout_ms }
- **`pnc_contract_p12`**: default *(empty)* **advanced**
{: #pnc_contract_p12 }
- **`pnc_contract_p12_passphrase`**: default *(empty)* **advanced**
{: #pnc_contract_p12_passphrase }
- **`precharge_process_timeout_s`**: default `7` s **advanced**
{: #precharge_process_timeout_s }
- **`preferred_control_mode`**: One of `Dynamic`, `Scheduled` (default: `Dynamic`) **advanced**
{: #preferred_control_mode }
- **`service_detail_timeout_ms`**: default `5000` ms **advanced**
{: #service_detail_timeout_ms }
- **`service_discovery_timeout_ms`**: default `2000` ms **advanced**
{: #service_discovery_timeout_ms }
- **`service_selection_timeout_ms`**: default `2000` ms **advanced**
{: #service_selection_timeout_ms }
- **`session_setup_timeout_ms`**: default `2000` ms **advanced**
{: #session_setup_timeout_ms }
- **`supported_app_protocol_timeout_ms`**: default `2000` ms **advanced**
{: #supported_app_protocol_timeout_ms }
