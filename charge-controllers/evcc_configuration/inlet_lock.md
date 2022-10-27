> [!UPDATE] {docsify-updated}
# Inlet lock

These configuration entries are all under the `[vehicle]` section.

> [!NOTE]
> See also section [Features/Lock safety](charge-controllers/evcc_lock_safety.md).

## locking_pulse_ms

<figcaption>Example</figcaption>

    locking_pulse_ms = 600

To avoid burning the lock motor, it is driven only for a certain amount of time in one or the other
direction. The length of these driving pulses default to 600 ms as it seems to correspond to most
locking system available on the market. It can be configured to a different value if your lock is
more peculiar.

Default to 600 ms.

> [!NOTE]
> Internally, that value is capped to 2 seconds.

> [!NOTE]
> To avoid damaging lock motors even in the most severe unexpected situations, we used special
> "watchdog" and "crash handler" to ensure the lock is de-energised even in case of a hard crash
> during a locking or unlocking sequence. Also note that de-energising means it will not complete
> the movement, nor unlock it. In such event, the lock will stay where it is, until the controller is
> restarted and user safety can be ensured.

## lock_feedback_r_threshold

<figcaption>Example</figcaption>

    lock_feedback_r_threshold = 100

Threshold, in ohms, between locked and unlocked state.

Default to 100 ohms.

## lock_feedback_low_is_locked

<figcaption>Example</figcaption>

    lock_feedback_low_is_locked = true

Polarity for `lock_feedback_r_threshold` when lock is locked. For instance, `true` means that the
lock is locked when resistance is below the threshold. Whereas `false` means lock is locked when the
resistance is above the threshold.

Default to true.

## no_inlet_lock

<figcaption>Example</figcaption>

    no_inlet_lock = true

If no inlet lock is used. Typical of table test use case, where you don't want to be blocking a
simulated charge test because it cannot detects any lock.

Default to false.

## Inlet lock examples

There are various lock feedback mechanisms existing. Here are examples for two most commonly found
types of inlet locks.

### Normally Open switch

With an NO switch, the lock feedback line will be shorted to ground (ie. R ~= 0 Ohms) when locked.
In such case, the proper configuration is the following (which happens to correspond to default
values):

    lock_feedback_r_threshold = 100
    lock_feedback_low_is_locked = true

### 1k / 11k resistance

With a 1k / 11k lock feedback, when the lock is open (or faulty) a 1 000 Ohms resistance is in the
path to ground. When it is properly locked, that resistance becomes 11 000 Ohms. In such case, the
proper configuration is the following:

    lock_feedback_r_threshold = 5000
    lock_feedback_low_is_locked = false
