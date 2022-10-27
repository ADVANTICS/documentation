> [!UPDATE] {docsify-updated}
# Lock safety

The lock of the inlet is here to prevent exposing users to dangerous electrical potentials.

When the charge controller is managing an inlet lock, in abnormal situations it might decide to keep
it locked if it sees the situation is dangerous, OR if it has no way of assessing if the situation
is dangerous or not.

While these is for safety sake, it can also lead to user frustration. In such event, an inlet lock
should be manually unlocked only either by technicians able to assess the situation and the risks.
Or in case of remote assistance, the user should be guided by a remote technician in such a way it
can assess the situation remotely.

A restart/power cycle of the charge controller might also automatically resolve the issue. But only
if the controller is able to assess the situation by itself.

## Safe conditions

Fundamentally, the controller needs the following conditions to command an unlock:

- DC contactors must be open. This itself implies the reported flowing current is less than or equal
  to 1 A.
- The reported inlet voltage is less than or equal to 60 V.
- The information about contactor status, flowing current and inlet voltage are all reliable. That
  means it should have received them within the last
  [can_timeout_ms](charge-controllers/evcc_configuration/generalities.md#can_timeout_ms) milliseconds.

During an abnormal event that persists outside of a normal communication session with a charger, the
controller spawns an "emergency monitor" and will stay in that state until the situation resolves.
Part of the emergency monitor is to look for these above conditions, and command the contactors and
inlet lock as needed.

Usually, a lock would remain locked when:

- The charger keeps producing voltage or current despite all the "emergency stop" signaling.
- The contactors are not opening (eg. they could be welded, or their control is inoperative).
- The CAN bus is in a bad state (eg. disconnected, physically severed, overloaded, too noisy).
- The lock control is inoperative.
- Unrecoverable crash of the controller applications.

> [!NOTE]
> Upon restart, power cycle, or any cycling back to `Waiting_For_EVSE` state, if the controller sees
> the lock feedback tells it is locked, it will assess the situation before commanding an unlock.
>
> Ie. If after a reboot the abnormal situation is resolved, the lock will be released. But if it is
> not (ie. still high voltage at the inlet), or if the controller is "blind" (eg. CAN bus is in a
> bad state) then it will not unlock.
