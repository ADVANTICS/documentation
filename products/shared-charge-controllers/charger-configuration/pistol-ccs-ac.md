# CCS AC pistol

These configuration entries are all under the `[pistol:CCS AC]` section.

!!! note "Names are what you write in the file"
    These are the option names exactly as the configuration file expects them. The Web UI
    displays them as capitalised labels ("Charger Type"); writing that label into the file
    does **not** work -- the option is ignored without an error and the default applies.

Entries marked **advanced** are hidden in the Web UI until you switch to expert mode.

### CAN BUS
- **`charger_can_if`**: default `can0` **advanced**
{: #charger_can_if }
- **`charger_can_timeout_ms`**: Timeout for reception of Power_Modules_Status message in generic interface (ms) (default: `500.0` ms) **advanced**
{: #charger_can_timeout_ms }
- **`charger_type`**: The type of CAN interfacer to communicate with your charger. One of `Advantics_Generic_AC_v2` (default: `Advantics_Generic_AC_v2`)
{: #charger_type }

### Lock Parameters
- **`lock_feedback_low_is_locked`**: There are various lock feedback mechanisms existing. The one provided as default here correspond to a simple Normally Open switch that will short to ground (ie. R~=0) when locked. For a 1K/11K lock feedback, you would have to change the R threshold (eg. 5000) as well as inverse the polarity option by setting it to false (default: `true`)
{: #lock_feedback_low_is_locked }
- **`lock_feedback_r_threshold`**: Threshold, in ohms, between locked and unlocked state (default: `100.0`)
{: #lock_feedback_r_threshold }
- **`lock_pulse_ms`**: Time in milliseconds of the locking or unlocking pulses (default: `600.0` ms)
{: #lock_pulse_ms }
- **`no_cable_lock`**: In case cable is detachable from charger side, or for R&D usage (default: `true`)
{: #no_cable_lock }

### Phases, charger limits and cable limits
- **`max_cable_phase_current`**: AC cable limits, per phase Max current rated for the cable, in A (default: `32.0` A)
{: #max_cable_phase_current }
- **`max_cable_phase_power`**: AC cable limits, per phase Max current rated for the cable, in A. Can be ommitted if a current limit is set (default: `0.0` W)
{: #max_cable_phase_power }
- **`max_cable_phase_voltage`**: AC cable limits, per phase Max voltage rated for the cable, in V (default: `250.0` V)
{: #max_cable_phase_voltage }
- **`max_charger_phase_current`**: The current threshold at which request the charger to cap,for every phase (default: `32.0` A)
{: #max_charger_phase_current }
- **`number_of_phases`**: Only used in OCPP GetCompositeSchedule (default: `3`) **advanced**
{: #number_of_phases }

### General
- **`ignore_pp`**: Ignore the values from Proximity Pilot (default: `true`) **advanced**
{: #ignore_pp }
- **`index`**: Pistol index. Must be a non-zero positive integer unique with respect to other pistols. Used to offset CAN addressing as well. One of `1` to `16` (default: `2`)
{: #index }
- **`is_cable_detachable`**: default `false`
{: #is_cable_detachable }
- **`is_ventilated`**: Some vehicles may require (by using CP State D instead of C) to be charging only in a ventilatedarea. If charger is not in a ventilated place, and vehicle requires ventilation, CP PWMgoes to 100% (default: `true`) **advanced**
{: #is_ventilated }
- **`use_sequence_flags`**: Tells if flags in Sequence_Control message of the Generic CAN interface should be used (default: `true`)
{: #use_sequence_flags }
