> [!UPDATE] {docsify-updated}
# Temperature Control

## Concepts

The climate control integrated in `pev-controller` application is taking temperature channels as input and realise actions as output in reaction to the measured temperatures.

The inputs are:
- PTC 1000 analog inputs from the board connectors
- Temperature signals reported over CAN
- System temperatures (CPU and SoM)

The output actions are:
- Add current derating
- Stop the charge
- Monitor (ie. distribute measurements over the charger interface)

To draw the line between an input measurement and an output action, a list of actions can be configured. That list of actions is defined in a "functional" group, that can be associated to various temperature channels.

Example: A temperature channel is associated to a functional group (eg. "cable"). That functional group list the actions that should be invoked for every measurement (1 sample per second) (eg. "cable_current_derate", "charge_stop", "monitor"). Each action implements the reaction it wants and acts on the rest of the system.

## Temperature channels configuration

Temperature channels are configured in the `/srv/config.cfg` file under `[temperature]` section.
<br/><br/>

- `[temperature]` can be a multi-line entry
- Each line has the following format: `<CHANNEL> = <FUNCTION>`
- `<FUNCTION>` has to correspond to another section of the config file named `[temperature:<FUNCTION>]`. Several sensible default functions are already provided (see below).
- `<CHANNEL>` corresponds to a temperature channel available on the controller.

<figcaption>Example temperature channels configuration</figcaption>

```
[temperature]

ptc0 = monitor
ptc1 = cable
ptc2 = monitor
```

## Channel functions configuration

A `[temperature:<FUNCTION>]` section has only one possible entry, the action list.
<br/><br/>

- `actions` can be a multi-line entry of possible `<ACTION>`
- Each `<ACTION>` has to correspond to another section of the config file named `[temperature_action:<ACTION>]`. Several sensible default actions are already provided (see below).

<figcaption>Example temperature function configuration</figcaption>

```
[temperature:cable]
actions =
		cable_derate_current
		cable_stop_threshold
		monitor
```

<br/>
<div class="compact-table">
<span>Default functions provided</span>

|Function|Actions|Purpose|
|--------|-------|-------|
|cable   |cable_derate_current<br/>cable_stop_threshold<br/>monitor|<span class="wrap">Derates the current as temperature goes up. And stop the charge once passed a certain threshold. Also report the temperature over CAN.</span>|
|monitor |monitor|<span class="wrap">Just for reporting a temperature channel over CAN.</span>|

</div>

## Actions configuration

Each `[temperature_action:<ACTION>]` section is providing parameters to actual action classes hard-coded in the `pev-controller` application.
<br/><br/>

- `mode` is the entry corresponding to an actual action class (list below)
- `target` is an entry common to all modes. It defines what the action will act upon. It can also be a comma or space separated list of target.

### Monitor mode

The `monitor` mode is simply storing the value of the measured temperature into the internal datastructure that will be passed on to the charger interface for reporting. It is then up to the charger interface to actually emit the information on its bus according to its own encoding.
<br/><br/>

- `target` parameter can only be `monitor`.

<figcaption>Example (actually, only valid way) of writing a monitor action</figcaption>

```
[temperature_action:monitor]
target = monitor
mode = monitor
```

A default monitor action is already provided (as in the example). And you would most likely just use it as-is as there is nothing particular to configure here.

On the generic interface, these measurements are reported in ` ADM_CS_EVCC_Inputs`.

#### Encoding of temperature signals in the generic CAN interface

All temperature signals in the generic interface (ie. input and output ones) are encoded in the same way:
- Length of 8 bits
- Slope of 1 (ie. 1°C/bit)
- Offset of -40
- Minimum: -40°C (encoded as 0x00)
- Maximum: 215°C (encoded as 0xFF)
- Default value of -40°C means "not provided" or "not connected"

### Threshold mode

The `threshold` mode is triggering its `target` when its configured `limit` is crossed.

- Currently, the available `target` is `charge_stop`.
- `limit` is a float.

<figcaption>Example cable temperature action for stopping charge at a threshold (as per CCS standard)</figcaption>

```
[temperature_action:cable_stop_threshold]
target = charge_stop
mode = threshold
limit = 90
```

<br/>
<div class="compact-table">
<span>Default threshold actions provided</span>

| Action | Target | Limit | Note |
|---|---|---|---|
| cable_stop_threshold | charge_stop | 90 | As per CCS standard |

</div>

### Derate interpolate modes

The `derate_interpolate` mode is suitable to derate the charging current as a measured temperature goes up.

The `derate_interpolate` mode sets the result of a linear interpolation function defined by `setpoints` into the `target` parameter. This actually defines a "response curve" in function of the measured temperature.

<br/><br/>

- `setpoints` is a multi-line list of input temperature to output result. A linear interpolation of the output is applied for input temperature values that are in between the setpoints.

> [!WARNING]
> Because internally the setpoint list ends up being stored in a dictionary data-type, you cannot have duplicated input values in your list. However, the input values are converted to float. So, it is fine to use two different values with a small (eg. 0.1) difference.

> [!TIP]
> The best way to define the behaviour of the response curve at the boundaries (low or high temperatures) is to use the special `-inf` and `+inf` float values.

> [!WARNING]
> When a sensor is disconnected or shorted to ground, it is interpreted as `-inf`.

<!-- panels:start -->
<!-- div:left-panel -->
<figcaption>Example setpoints configuration</figcaption>

```
setpoints =
		-inf = 0%   # For any temperature below 20°C, have a null response
		20   = 0%   # Corner at 20°C to ramp-up
		50   = 40%  # Ramp-up to 40% from 20°C to 50°C
		50.1 = 70%  # Brick wall response, jump from 40% to 70% at 50°C
		70   = 70%  # Plateau at 70% between 50°C and 70°C
		90   = 50%  # Ramp down to 50% up to 90°C
		+inf = 50%  # Flat end of the curve after 90°C
```

<!-- div:right-panel -->
<figcaption>Resulting response curve</figcaption>

```
   Response                                                   
       ^                                                      
  100% |                                                      
       |                                                      
   80% |                                                      
       |                   |---------\                        
   60% |                   |          ---\                    
       |                   |              ----------------    
   40% |                  -|                                  
       |               --/                                    
   20% |            --/                                       
       |         --/                                          
    0% +---+----/--+---+---+---+---+---+---+---+---+---+--> Temperature  
      0°C    20°C    40°C    60°C    80°C    100°C   120°C
```

<!-- panels:end -->

<br/><br/>

- Currently, the only available `target` is `max_charging_current`.
> [!NOTE]
> When several derating are active at the same time on the same target (from different temperature channels and/or accross different actions), the highest derating value is used.

- `setpoints` is the definition of the response curve
> [!NOTE]
> The output quantity expressed by this response curve is the amount of derating applied to the target in percent. Ie. 0% means no derating, and 100% is full derating.


> [!NOTE]
> Therefore, the formula is akin to `target_value *= 1 - max(target_deratings)`

<figcaption>Example of a derate interpolate action</figcaption>

```
[temperature_action:cable_derate_current]
target = max_charging_current
mode = derate_interpolate
setpoints =
    -inf = 0%
    60 = 0%
    90 = 50%
    +inf = 50%
```

<div class="compact-table">
<span>Default derate interpolate actions provided</span>

|Action|Target|Setpoints|Note|Comment|
|---|---|---|---|---|
|cable_derate_current|max_charging_current|-inf = 0%<br/>60 = 0%<br/>90 = 50%<br/>+inf = 50%|Gradual increase of derating from 60°C to 90°C.<br/>Plateau at 50% derating beyond 90°C.|<span class="wrap">To be used with a charge stop threshold action above 90°C.</span>|

</div>