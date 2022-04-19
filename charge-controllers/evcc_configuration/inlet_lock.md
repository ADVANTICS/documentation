> [!UPDATE] {docsify-updated}
# Inlet lock

These configuration entries are all under the `[vehicle]` section.

> [!NOTE]
> For your information, when locking, Advantics controller drives the lock motor (positive lead)
> during 600 ms. When unlocking, it drives it in the other direction (negative lead) during 600 ms as
> well.

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
