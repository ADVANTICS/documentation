> [!UPDATE] {docsify-updated}
# Sleep functions

There are two ways you can make use of the sleep functions: an automatic one, or one were an digital
input is used as a sleep request.

Note that the sleeping and waking-up events are themselves pretty "snappy", so they don't introduce
any appreciable delays from the user point-of-view.

## Automatic sleep

In the configuration file, under the `[hardware]` section, you have an option named `auto_sleep`.
By default it is false. Set it to `true` to enable it.

When enabled, every time the controller is cycling back to the `Waiting_For_EVSE` idle state
(including on the first start), it will immediately go to sleep.

## Sleep request IO

You can assign a digital input to serve as a sleep request. In the configuration file, under the
`[hardware]` section, set one of the input (eg. `dig_in1`) to the value `Sleep`.

This work on inverted logic, so you need to set it low to request a sleep. Note that it has effect
only when the controller is in (or enter) `Waiting_For_EVSE` idle state. If you request the controller
to sleep during charging (and keep the request on), it will not go into sleep immediately but rather
wait that the charge session finishes.

You can also keep it low all the time, as it will not prevent a wake-up event to happen and trigger
a new charge session. You could even permanently wire it to ground, though at this point you will be
better off using the `auto_sleep` function described above, as it will have the exact same effect.

## Wake-up events

When the controller is asleep it will not respond to any event on the CAN bus or ethernet port. The
controller can be woken-up in either by:

- Setting `2C2 - SWITCHED_POWER` terminal high.
- Plugging-in an active charger, as we detect the rise in voltage on the CP line.
