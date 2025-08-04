> [!UPDATE] {docsify-updated}
# CCS

These configuration entries are all under the `[ccs]` section.

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

> [!NOTE]
> Entry named `iso_ed1_priority` was used previously. It is now deprecated.

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

> [!DLIST|label:DC_extended]
> Use the 2 DC pins at the bottom of the combo inlet/pistol.

> [!DLIST|label:DC_core]
> Use what is usually known as the AC pins, but for DC.

Default to `DC_extended`.

> [!NOTE]
> It is not recommended to change this value as in practice all others are seldom, if ever, used.

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

> [!NOTE]
> Only on (special) controllers supporting it.

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

> [!DLIST|label:B1]
> Suitable for NA use. Compatible with SAE J1772 (S3 switch + constant monitoring for e-stop).

> [!DLIST|label:B2]
> Suitable for EU and rest of the world use. Does current coding in AC.

> [!DLIST|label:Any other value]
> PP is ignored.

Default to `B2`.

> [!ATTENTION]
> The controller does the `+V` and `R4` pull-up (330 Ω to 5V) onboard.
>
> Never connect any other detection circuitry on PP. It will disturb the resistance values the
> controller is actively sensing.


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
