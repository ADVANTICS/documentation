# CCS/MCS

These configuration entries are under the `[ccs]` section. The two exceptions are marked as such
below.

## enable_din

<figcaption>Example</figcaption>

    enable_din = true

Loads support for DIN SPEC 70121.

Default to true.

## enable_iso_part2

<figcaption>Example</figcaption>

    enable_iso_part2 = true

Loads support for ISO 15118-2.

Default to true.

## enable_iso_part20

<figcaption>Example</figcaption>

    enable_iso_part20 = true

Loads support for ISO 15118-20.

Default to true.

## din_priority

<figcaption>Example</figcaption>

    din_priority = 3

Sets the priority used in AppProtocol for DIN SPEC 70121 schema.

Default to 3.

## iso_part2_priority

<figcaption>Example</figcaption>

    iso_part2_priority = 2

Sets the priority used in AppProtocol for ISO 15118-2 schema.

Default to 2.

!!! note
    Entry named `iso_ed1_priority` was used previously. It is now deprecated.

## iso_part20_dc_priority

<figcaption>Example</figcaption>

    iso_part20_dc_priority = 1

Sets the priority used in AppProtocol for ISO 15118-20 DC schema.

Default to 1.

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

## energy_transfer_type

<figcaption>Example</figcaption>

    energy_transfer_type = DC_extended

Defines which pins on the inlet/pistol are used in DC charging. Possible values are:

!!! note "DC extended"
    Use the 2 DC pins at the bottom of the combo inlet/pistol.

!!! note "DC core"
    Use what is usually known as the AC pins, but for DC.

Default to `DC_extended`.

!!! note
    It is not recommended to change this value as in practice all others are seldom, if ever, used.

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

## ventilation_required

<figcaption>Example</figcaption>

    ventilation_required = true

Tells if ventilation is required during charging (ie. use CP State D).

Default to false.

!!! note
    Only on (special) controllers supporting it.

## allow_dynamic_power_limits

<figcaption>Example</figcaption>

    allow_dynamic_power_limits = true

Allows charger to change its power limits (including max current) while charging, without going
through a charge parameters renegotiation phase.

Default to true.

## pp_mode

<figcaption>Example</figcaption>

    pp_mode = B2

Sets which mode to use for PP (Proximity Pilot) handling. Modes are defined by IEC 61851-1, Annex B.
Possible values are:

!!! note "B1"
    Suitable for NA use. Compatible with SAE J1772 (S3 switch + constant monitoring for e-stop).

!!! note "B2"
    Suitable for EU and rest of the world use. Does current coding in AC.

!!! note "Any other value"
    PP is ignored.

Default to `B2`.

!!! attention
    The controller does the `+V` and `R4` pull-up (330 Ω to 5V) onboard.

    Never connect any other detection circuitry on PP. It will disturb the resistance values the
    controller is actively sensing.


## wait_hv_ready_timeout_ms

<figcaption>Example</figcaption>

    wait_hv_ready_timeout_ms = 40000

Timeout (milliseconds) for waiting for high-voltage system readiness. If exceeded, the session will abort.


## current_demand_timeout_ms

<figcaption>Example</figcaption>

    current_demand_timeout_ms = 2000

Set the current demand timeout in milliseconds. When triggered, the charge is stopped.

CCS standards specify it should be 250 ms. However, we believe it is needlessly too strict, and some
chargers can actually fail it from time to time. Heavy noise conditions can also make this timeout
trigger spuriously. Hence, we rather default to 2 seconds instead of 250 ms.

Default to 2000 ms.


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

## Other expert settings

Here are other expert settings with their default values. Someone with knowledge of the standards
can understand them.

<figcaption>Expert knowable settings</figcaption>

    # SLAC
    slac_nb_msound_threshold = 1

    # Process timeouts, in seconds
    precharge_process_timeout_s = 7

    # Message timeouts
    supported_app_protocol_timeout_ms = 2000
    session_setup_timeout_ms = 2000
    service_discovery_timeout_ms = 2000
    service_detail_timeout_ms = 5000
    payment_service_selection_timeout_ms = 2000
    payment_details_timeout_ms = 5000
    authorization_timeout_ms = 2000
    charge_parameter_discovery_timeout_ms = 2000
    charging_status_timeout_ms = 2000
    wait_locked_timeout_ms = 2000
    metering_receipt_timeout_ms = 2000
    cable_check_timeout_ms = 2000
    precharge_timeout_ms = 2000
    # We can distinguish between the power delivery at the beginning of the charge and the one at the end
    power_delivery_begin_timeout_ms = 5000
    # Current Demand timeout has a special place above
    power_delivery_end_timeout_ms = 5000
    welding_detection_timeout_ms = 2000
    session_stop_timeout_ms = 2000
    certificate_installation_timeout_ms = 5000
    certificate_update_timeout_ms = 5000

## Other entries

The rest of the `[ccs]` section, generated from the controller software so that names,
defaults and units cannot drift from it. Most of these are protocol timeouts you will not
need to touch; they exist for interoperability work against a stubborn vehicle or charger.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

- **`ac_enabled`**: Whether the AC charging interface is allowed to operate (default: `true`)
{: #ac_enabled }
- **`allow_tls_for_din`**: Whether TLS should be allowed for DIN charging (default: `false`) **advanced**
{: #allow_tls_for_din }
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
- **`invert_pp_b1`**: default `false` **advanced**
{: #invert_pp_b1 }
- **`iso_ed1_priority`**: Priority of the different protocols. The priority is used to determine which protocol is used to charge the EV, among DIN, ISO 15118-2 and ISO15118-20. Protocols with the lowest priority value gets picked first whenever possible (default: `2`)
{: #iso_ed1_priority }
- **`log_signature_details`**: default `false` **advanced**
{: #log_signature_details }
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
