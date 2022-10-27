> [!UPDATE] {docsify-updated}
# Generalities

These configuration entries are all under the `[vehicle]` section.

## type

<figcaption>Example</figcaption>

    type = Advantics_Generic_v1

This entry specify which vehicle interface type is to be used. For this Generic Interface, the valid
values are:

> [!DLIST|label:Advantics_Generic_v1]
> The first version of this interface

## can_timeout_ms

<figcaption>Example</figcaption>

    can_timeout_ms = 500

Timeout in milliseconds for receiving critical frames during powered phases, before triggering a fault.

Default to 500 ms.

## force_extended_ids

<figcaption>Example</figcaption>

    force_extended_ids = true

If we should send 29-bits extended frame IDs even if the ID fits on the 11 bits of a simple frame ID.

Default to false.

## max_voltage

<figcaption>Example</figcaption>

    max_voltage = 500

Absolute maximum voltage EV systems (inlet, wires, contactors, battery, etc.) can safely accept.

Default to 500 V.

## max_current

<figcaption>Example</figcaption>

    max_current = 120

Absolute maximum current EV systems (inlet, wires, contactors, battery, etc.) can safely accept.

Default to 0 A.

> [!ATTENTION]
> You MUST edit this entry for charging to work. Otherwise all current requests will just
> be limited to 0 A.

## max_power

<figcaption>Example</figcaption>

    max_power = 150000

Absolute maximum power EV systems (inlet, wires, contactors, battery, etc.) can safely accept. This
specifies a power envelop used to determine capping of current requests depending on the present
battery voltage. A value of 0 means no maximum power is configured and it will not be used to limit
current requests.

Default to 0 W (ie. not used).

## min_voltage

<figcaption>Example</figcaption>

    min_voltage = 200

Minimum voltage that battery could reach at lowest possible state of charge (used for compatibility
checks with charger capabilities).

Default to 200 V.

## min_current

<figcaption>Example</figcaption>

    min_current = 0

Minimum current we want the charger to deliver (only relevant for CCS ISO AC).

Default to 0 A.

## target_voltage

<figcaption>Example</figcaption>

    target_voltage = 450

The target voltage sent to EVSE during the current delivery loop.

Default to 450 V.

> [!NOTE]
> This is a Constant Current charging process. Target voltage should be higher than the battery
> voltage will ever reach at maximum state of charge.

## energy_capacity

<figcaption>Example</figcaption>

    energy_capacity = 0

Energy capacity of the battery, in Wh. Optional but recommended. Used for various informational
calculations (SoC, remaining time, etc.).

Default to 0 Wh.

## max_soc

<figcaption>Example</figcaption>

    max_soc = 80

Maximum state of charge above which Advantics controller will trigger a normal stop. Only valid for
DC charging. Set it to 80 to only do bulk charging.

Default to 99 %.

## inhibit_precharge_unmatch_t

<figcaption>Example</figcaption>

    inhibit_precharge_unmatch_t = 1

When charging DC, in precharge the controller is actively checking the voltage at the inlet is
within ±20 V of the battery voltage. When the inlet voltage match this range, the contactors are
commanded to close.

Contactors do not necessarily close immediately. In situations where contactors are actually managed
by the vehicle and not the charge controller, the vehicle could be "preparing" for a few seconds
before actually closing the contactors. While the controller waits to receive feedback that the
contactors are closed, it will keep checking the inlet voltage is matching. If it no longer does for
whatever reason, the controller considers it is an unmatch, and commands the contactors to reopen in
order to avoid arcing.

However in other situations, the moment contactors are actually closing, the reading of the inlet
voltage could vary widely, by a few hundreds volt. This is particularly the case when using a [CAN
sensor](charge-controllers/evcc_configuration/can_sensor.md) that measures the inlet voltage as a
difference of two channels, themselves referenced to the battery DC-. If both contactors do not
close exactly at the same time, the measured then calculated inlet voltage is invalid for a short
amount of time. This config entry is here to prevent reopening the contactors for a specified amount
of time after commanding them to close, in case there is a voltage unmatch.

Default to 1 s.

## current_ramp

<figcaption>Example</figcaption>

    current_ramp = 20

Maximum current ramp-up rate, in A/s. Will be used to limit current requests sent to charger.

Default to 20 A/s.

NOTE: The ramp uses a linear interpolation, such that the current increase between two requests
does not exceed this rate. For instance, between two requests spaced by 100ms, with a ramp-up rate
limit of 20 A/s, the current request can only increase by 2 A in that time period.
