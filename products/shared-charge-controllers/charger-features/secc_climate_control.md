# Climate control

!!! note
    Only available from version 4.x of the controller system


## Concepts

The climate control integrated in `evse-controller` application is taking temperature channels as input and realise actions as output in reaction to the measured temperatures.

The inputs are:
- PTC 1000 analog inputs from the board connectors
- Temperature signals reported over CAN
- System temperatures (CPU and SoM)

The output actions are:
- Adapt fan speed
- Add current derating
- Stop the charge
- Monitor (ie. distribute measurements over the charger interface)

To draw the line between an input measurement and an output action, a list of actions can be configured. That list of actions is defined in a "functional" group, that can be associated to various temperature channels.

Example: A temperature channel is associated to a functional group (eg. "cable", "power module"). That functional group list the actions that should be invoked for every measurement (1 sample per second) (eg. "cable_current_derate", "power_module_fan", "charge_stop", "monitor"). Each action implements the reaction it wants and acts on the rest of the charging system.

## Temperature channels configuration

Temperature channels are configured in each pistol sections of the `/srv/config.cfg` file.
<br/><br/>

- `temperatures` can be a multi-line entry
- Each line has the following format: `<SOURCE>:<CHANNEL> = <FUNCTION>`
- `<SOURCE>` can be one of `io` or `charger`
- `<FUNCTION>` has to correspond to another section of the config file named `[temperature_function:<FUNCTION>]`. Several sensible default functions are already provided (see below).
- `<CHANNEL>` corresponds to a temperature channel available on the controller you use. See table below.

<figcaption>Example pistol temperature channels configuration</figcaption>

```
[pistol:CCS DC]
temperatures =
    io:pt1k_ch1_a = cable
    io:pt1k_ch2_a = cable
    charger:power_modules_temperature = power_modules_01
    io:cpu_temperature = monitor
```

| Name | Controller | Pistol | Type | Typical application | Input | Note |
|---|---|---|---|---|---|---|
| io:pt1k_a | ADM-CO-CUI1 | Any | PT1000 | Cable | J11, pos. 17 |  |
| io:pt1k_b | ADM-CO-CUI1 | Any | PT1000 | Cable | J11, pos. 16 |  |
| io:pt1k_ch1_a | ADM-CS-SECC | CCS DC | PT1000 | Cable | CONN2, pos. 1 |  |
| io:pt1k_ch2_a | ADM-CS-SECC | CCS DC | PT1000 | Cable | CONN2, pos 3 |  |
| io:pt1k_ch1_b | ADM-CS-SECC | CCS AC | PT1000 | Cable | CONN2, pos 5 |  |
| io:pt1k_ch2_b | ADM-CS-SECC | CCS AC | PT1000 | Cable | CONN2, pos 7 |  |
| io:pt1k_chademo | ADM-CS-SECC | CHAdeMO | PT1000 | Cable | CONN3, pos 1 |  |
| io:cpu_temperature | Any | Any | On-chip | System |  | Not working yet on ADM-CS-SECC |
| io:colibri_temperature | ADM-CO-CUI1 | Any | On-board (SoM) | System |  | Not very reliable |
| charger:power_modules_temperature | Any | Any | CAN source | Power modules | [`0x60010`] `Power_Modules_Status`.`Power_Modules_Temperature` |  |
| charger:enclosure_temperature | Any | Any | CAN source | Charging station | [`0x60010`] `Power_Modules_Status`.`Enclosure_Temperature` |  |
| charger:power_modules_semiconductors | Any | Any | CAN source | Advantics power modules | Semiconductor devices temperature reported by power modules | <span class="wrap">Actually a composite of all semiconductors temperature measurements, of all modules, of all stacks. Only the max value is kept.</span> |
| charger:power_modules_magnetics | Any | Any | CAN source | Advantics power modules | Magnetic devices temperature reported by power modules | <span class="wrap">Actually a composite of all magnetics temperature measurements, of all modules, of all stacks. Only the max value is kept.</span> |

<br/>

Note:
- The typical application of each channel is just a suggestion. You are free to repurpose them for any other hot location.
- The temperature input signals in the generic CAN interface `[0x60010] Power_Modules_Status` message (since version 2.2) are here for you to supply your own measured temperatures to the climate controller, such that it can trigger charging-related actions (ie. charge stop, current derating) or use the fan PWM channels of the charge controller.

## Channel functions configuration

A `[temperature_function:<FUNCTION>]` section has only one possible entry, the action list.
<br/><br/>

- `actions` can be a multi-line entry of possible `<ACTION>`
- Each `<ACTION>` has to correspond to another section of the config file named `[temperature_action:<ACTION>]`. Several sensible default actions are already provided (see below).

<figcaption>Example temperature function configuration</figcaption>

```
[temperature_function:cable]
actions =
		cable_derate_current
		cable_stop_threshold
		monitor
```

<br/>

|Function|Actions|Purpose|Controller|
|--------|-------|-------|----------|
|cable   |cable_derate_current<br/>cable_stop_threshold<br/>monitor|<span class="wrap">Derates the current as temperature goes up. And stop the charge once passed a certain threshold. Also report the temperature over CAN.</span>|Any       |
|power_modules|power_module_fan<br/>power_module_derate_current<br/>power_module_stop_threshold|<span class="wrap">Increase fan speed and derate current as temperature goes up. And stop the charge once passed a certain threshold.</span>|ADM-CO-CUI1|
|power_modules_01|power_module_fan_01<br/>power_module_derate_current<br/>power_module_stop_threshold|<span class="wrap">Same than `power_modules`, but targeting fan PWM channel 1.</span>|ADM-CS-SECC|
|power_modules_02|power_module_fan_02<br/>power_module_derate_current<br/>power_module_stop_threshold|<span class="wrap">Same than `power_modules`, but targeting fan PWM channel 2.</span>|ADM-CS-SECC|
|monitor |monitor|<span class="wrap">Just for reporting a temperature channel over CAN.</span>|Any       |


## Actions configuration

Each `[temperature_action:<ACTION>]` section is providing parameters to actual action classes hard-coded in the `evse-controller` application.
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

On the generic interface (≥ v2.2), these measurements are reported in `ADM_CO_CUI1_Inputs` and `ADM_CS_SECC_Inputs` messages:

<!-- panels:start -->
<!-- div:left-panel -->
<span>[0x6800A] ADM_CO_CUI1_Inputs</span>

| Signal              | Offset (bits) |
|---------------------|---------------|
| Colibri_Temperature | 32            |
| CPU_Temperature     | 40            |
| Pistol_PTC1         | 48            |
| Pistol_PTC2         | 56            |

<!-- div:right-panel -->
<span>[0x6800B] ADM_CS_SECC_Inputs</span>

| Signal          | Offset (bits) |
|-----------------|---------------|
| &nbsp;          |               |
| CPU_Temperature | 40            |
| Pistol_PTC1     | 48            |
| Pistol_PTC2     | 56            |

<!-- panels:end -->

Note that it can only report two PTC channels per pistol. Since each pistol can instantiate a generic interface using a CAN ID offset, here are how they are mapped:

<span>Temperature channels mapping on Generic CAN interface</span>

| Signal      | CCS DC             | CCS AC     | CHAdeMO              |
|-------------|--------------------|------------|----------------------|
| Pistol_PTC1 | PT1K_A, PT1K_CH1_A | PT1K_CH1_B | PT1K_A, PT1K_CHADEMO |
| Pistol_PTC2 | PT1K_B, PT1K_CH2_A | PT1K_CH2_B | PT1K_B               |


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
<br/><br/>

- Currently, the only available `target` is `charge_stop`.
- `limit` is a float.

<figcaption>Example cable temperature action for stopping charge at a threshold (as per CCS standard)</figcaption>

```
[temperature_action:cable_stop_threshold]
target = charge_stop
mode = threshold
limit = 90
```

<br/>

| Action | Target | Limit | Note |
|---|---|---|---|
| cable_stop_threshold | charge_stop | 90 | As per CCS standard |
| power_module_stop_threshold | charge_stop | 85 | Suitable for Silicon Carbide based power modules |

### Interpolate modes

The `interpolate` modes set the result of a linear interpolation function defined by `setpoints` into the `target` parameter. This actually defines a "response curve" in function of the measured temperature.

You cannot instantiate a pure `interpolate` action as the way the result is applied is target-depend. Therefore, two specific interpolate modes are provided, `derate_interpolate` and `pwm_interpolate` (see below).
<br/><br/>

- `setpoints` is a multi-line list of input temperature to output result. An linear interpolation of the output is applied for input temperature values that are in between the setpoints.

!!! warning
    Because internally the setpoint list ends up being stored in a dictionary data-type, you cannot have duplicated input values in your list. However, the input values are converted to float. So, it is fine to use two different values with a small (eg. 0.1) difference.


!!! tip
    The best way to define the behaviour of the response curve at the boundaries (low or high temperatures) is to use the special `-inf` and `+inf` float values.


!!! warning
    When a sensor is disconnected or shorted to ground, it is interpreted as `-inf`.


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

#### Derate interpolate mode

The `derate_interpolate` mode is suitable to derate the charging current as a measured temperature goes up.
<br/><br/>

- Currently, the only available `target` are `max_charger_current` and `max_cable_current`.
!!! note
    When several derating are active at the same time on the same target (from different temperature channels and/or accross different actions), the highest derating value is used.


- `setpoints` is the definition of the response curve
!!! note
    The output quantity expressed by this response curve is the amount of derating applied to the target in percent. Ie. 0% means no derating, and 100% is full derating.



!!! note
    Therefore, the formula is akin to `target_value *= 1 - max(target_deratings)`


<figcaption>Example of a derate interpolate action</figcaption>

```
[temperature_action:cable_derate_current]
target = max_cable_current
mode = derate_interpolate
setpoints =
    -inf = 0%
    60 = 0%
    90 = 50%
    +inf = 50%
```

<span>Default derate interpolate actions provided</span>

|Action|Target|Setpoints|Note|Comment|
|---|---|---|---|---|
|cable_derate_current|max_cable_current|-inf = 0%<br/>60 = 0%<br/>90 = 50%<br/>+inf = 50%|Gradual increase of derating from 60°C to 90°C.<br/>Plateau at 50% derating beyond 90°C.|<span class="wrap">To be used with a charge stop threshold action above 90°C.</span>|
|power_module_derate_current|max_charger_current|-inf = 0%<br/>75 = 0%<br/>85 = 50%<br/>+inf = 50%|Sharp increase of derating from 75°C to 85°C.<br/>Plateau at 50% derating beyond 85°C.|<span class="wrap">Suitable for Silicon Carbide based power modules. To be used with a charge stop threshold action above 85°C.</span>|


#### PWM interpolate mode

The `pwm_interpolate` mode is suitable to control a fan speed in function of a measured temperature.
<br/><br/>

- `target` has to be a PWM channel of the controller (see table below). It can also be a comma or space separated lists of PWM channels.
- `frequency` sets the base frequency of the PWM signal (for a fan, typically 25 kHz)
- `setpoints` is the definition of the response curve

<figcaption>Example of a PWM interpolate action</figcaption>

```
[temperature_action:power_module_fan]
target = fan_pwm
mode = pwm_interpolate
frequency = 25000
setpoints =
    -inf = 0%
    39.9 = 0%
    40 = 20%
    65 = 100%
    +inf = 100%
```


| Name | Controller | Output |
|---|---|---|
| fan_pwm | ADM-CO-CUI1 | "J5, J8 and J9, position 2 (same channel on all three connectors)" |
| fan1_pwm | ADM-CS-SECC | "CONN6, position 10" |
| fan2_pwm | ADM-CS-SECC | "CONN6, position 9" |


|Action|Target|Frequency|Setpoints|Controller|Note|
|---|---|---|---|---|---|
|power_module_fan|fan_pwm|25000|-inf = 0%<br/>39.9 = 0%<br/>40 = 20%<br/>65 = 100%<br/>+inf = 100%|ADM-CO-CUI1|<span class="wrap">Fan is off below 40°C.<br/>At 40°C, fan start with a base speed of 20% duty cycle.<br/>Between 40°C and 65°C, fan speed progressively increase to 100%.<br/>Above 65°C, fan is at max speed.</span>|
|power_module_fan_01|fan1_pwm|25000|inf = 0%<br/>39.9 = 0%<br/>40 = 20%<br/>65 = 100%<br/>+inf = 100%|ADM-CS-SECC|<span class="wrap">Same than `power_module_fan`, but targetting only fan1_pwm channel.</span>|
|power_module_fan_02|fan2_pwm|25000|inf = 0%<br/>39.9 = 0%<br/>40 = 20%<br/>65 = 100%<br/>inf = 100%|ADM-CS-SECC|<span class="wrap">Same than `power_module_fan`, but targetting only fan1_pwm channel.</span>|

