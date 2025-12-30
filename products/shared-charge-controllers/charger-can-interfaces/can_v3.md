# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [Power_Modules_Status](#Power_Modules_Status) | 0x63000 | 8 | IN | 100 |
| [DC_Power_Parameters](#DC_Power_Parameters) | 0x63001 | 8 | IN |  |
| [Sequence_Control](#Sequence_Control) | 0x63002 | 3 | IN |  |
| [ADM_CS_SECC_Outputs](#ADM_CS_SECC_Outputs) | 0x63201 | 8 | IN | 1000 |
| [Advantics_Controller_Status](#Advantics_Controller_Status) | 0x6b000 | 1 | OUT | 100 |
| [New_Charge_Session](#New_Charge_Session) | 0x6b001 | 2 | OUT | 100 |
| [Charge_Status_Change](#Charge_Status_Change) | 0x6b002 | 1 | OUT |  |
| [DC_Power_Control](#DC_Power_Control) | 0x6b003 | 7 | OUT | 100 |
| [Charge_Session_Finished](#Charge_Session_Finished) | 0x6b004 | 1 | OUT |  |
| [Emergency_Stop](#Emergency_Stop) | 0x6b005 | 1 | OUT | 100 |
| [EV_Information_Battery](#EV_Information_Battery) | 0x6b100 | 6 | OUT |  |
| [EV_Information_Voltages](#EV_Information_Voltages) | 0x6b101 | 6 | OUT |  |
| [EV_Information_Charge_Limits](#EV_Information_Charge_Limits) | 0x6b102 | 8 | OUT |  |
| [EV_Information_Discharge_Limits](#EV_Information_Discharge_Limits) | 0x6b103 | 8 | OUT |  |
| [EV_Information_Energy](#EV_Information_Energy) | 0x6b104 | 6 | OUT |  |
| [EV_ID_CCS_Part2_DIN](#EV_ID_CCS_Part2_DIN) | 0x6b105 | 6 | OUT | 1000 |
| [ADM_CO_CUI1_Inputs](#ADM_CO_CUI1_Inputs) | 0x6b200 | 8 | OUT | 1000 |
| [ADM_CS_SECC_Inputs](#ADM_CS_SECC_Inputs) | 0x6b201 | 8 | OUT | 1000 |
| [ADM_CS_SPCC_Inputs](#ADM_CS_SPCC_Inputs) | 0x6b202 | 8 | OUT | 1000 |
| [CCS_Extra_Information](#CCS_Extra_Information) | 0x6b203 | 8 | OUT | 100 |
| [MCS_Extra_Information](#MCS_Extra_Information) | 0x6b204 | 8 | OUT | 100 |
| [OCPP_Control](#OCPP_Control) | 0x6b300 | 2 | OUT |  |


<a id="Power_Modules_Status"></a>
## Power_Modules_Status { #Power_Modules_Status }


| * | * |
|---|---|
| **Frame ID** | 0x63000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | IN |

### Description

Periodic message reporting the current status of power modules. This message should
be sent all the time when power modules are running.

!!! important
    Controller implements a timeout on the reception of this message. It is used as a
    source of interlock condition. As such, this interlock source is evaluated only in
    states where power modules should be alive.

    Therefore, it is NOT evaluated when waiting for a PEV to plug-in, or when
    negotiating the connection with the PEV.

    Power modules should be alive from the moment &lt;&lt;New_Charge_Session&gt;&gt; is sent, until
    &lt;&lt;Charge_Session_Finished&gt;&gt; is sent. At any other time, power modules are allowed to
    sleep and not send this message.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Present_Voltage | 16 | Unsigned |
| Present_Current | 16 | Signed |
| Power_Modules_Temperature | 8 | Unsigned |
| Enclosure_Temperature | 8 | Unsigned |
| System_Enable | 8 | Label set |
| Insulation_Resistance | 8 | Unsigned |

### Payload description

#### Present_Voltage { #Power_Modules_Status-Present_Voltage }

Voltage measurement at the output of the charger

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Present_Current { #Power_Modules_Status-Present_Current }

Current measurement at the output of the charger

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Amps | 0.1 | 0 |  |  |

#### Power_Modules_Temperature { #Power_Modules_Status-Power_Modules_Temperature }

Top temperature sensed in power modules.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### Enclosure_Temperature { #Power_Modules_Status-Enclosure_Temperature }

Top temperature sensed in the enclosure.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### System_Enable { #Power_Modules_Status-System_Enable }

Tells if charging is allowed.

When &lt;&lt;New_Charge_Session&gt;&gt; is sent, the controller waits for this signal
to be 1 to continue the charge sequence.

If 0 is emitted between &lt;&lt;New_Charge_Session&gt;&gt; and before the charging loop
starts, the charge controller tells the vehicle the charging service is
unavailable.

If 0 is emitted during the charging loop, this is interpreted as an
emergency shutdown requested by power modules.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Allowed | 0 |
| Allowed | 1 |

#### Insulation_Resistance { #Power_Modules_Status-Insulation_Resistance }

Reports the current insulation resistance, in multiple of 2 kOhms.

TIP: If the RCD sensor only gives a boolean value, then 255 correspond to a __Valid__
insulation, and 0 to an __Invalid__ insulation.

IMPORTANT: Whenever a power function is used after the insulation test, if this
signal reports an insulation resistance below the limit of 100 Ohms/V, then this
is considered as an interlock condition and an emergency stop is carried out.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | kOhms | 2 | 0 |  |  |


<a id="DC_Power_Parameters"></a>
## DC_Power_Parameters { #DC_Power_Parameters }


| * | * |
|---|---|
| **Frame ID** | 0x63001 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Message to dynamically set parameters of power transfer (limits, forced setpoints).
This message can be sent as often as needed (but not faster than 100ms).

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Maximum_Voltage | 16 | Unsigned |
| Maximum_Charge_Current | 16 | Unsigned |
| Maximum_Discharge_Current | 16 | Unsigned |
| Range_Target_Current | 16 | Signed |

### Payload description

#### Maximum_Voltage { #DC_Power_Parameters-Maximum_Voltage }

Maximum output voltage of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_voltage` from config file.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Maximum_Charge_Current { #DC_Power_Parameters-Maximum_Charge_Current }

Maximum charge current of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_current` from config file.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### Maximum_Discharge_Current { #DC_Power_Parameters-Maximum_Discharge_Current }

Maximum discharge current of the charger, reported to the vehicle.

Value is capped by limit statically defined in config file.
If set to 0, then it means to use default `max_charger_discharge_current` from
config file.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### Range_Target_Current { #DC_Power_Parameters-Range_Target_Current }

This signal is useful only for chargers using one of the supported power module
interface (ie. we directly control power modules), plus the generic interface
as a mean of external control.

When &lt;&lt;DC_Power_Control.Setpoints_Mode&gt;&gt; == __Range_Mode__, and power modules
are of a kind that cannot decide of the load current by themselves, by default
the maximum of the range will be used.

With this signal, you can set a different target setpoint that will be send to
power modules. Direction of power transfers is chosen with the sign of this
signal. When the sign changes, a switch over will happen.

Values are always capped to the allowed range given in &lt;&lt;DC_Power_Control&gt;&gt;.
Provided values will also be ramped up or down, using ramp slopes defined by
config file entries `current_ramp_up_rate` and `current_ramp_down_rate`.

Note that the actual setpoint sent to power modules is not reflected in
&lt;&lt;DC_Power_Control&gt;&gt; message, as values in this message need to keep
reflecting the full allowed range. Ie. &lt;&lt;DC_Power_Control&gt;&gt; will not emulate
a __Target_Mode__, and it will still show the normal __Range_Mode__.

Note also that while the same functionality could be achieved by changing
&lt;&lt;Power_Transfer_Parameters.Maximum_Charge_Current&gt;&gt;, this Range_Target_Current
signal is actually entirely internal, and the value is never directly reported
to the vehicle. Which mean Maximum_Charge_Current can still reflect the true
maximum charge current advertised to the vehicle.

This signal does nothing in the following situations:
- &lt;&lt;DC_Power_Control.Setpoints_Mode&gt;&gt; == __Target_Mode__.
- Or you only use the generic interface, and manage power modules yourself.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | Amps | 0.1 | 0 |  |  |


<a id="Sequence_Control"></a>
## Sequence_Control { #Sequence_Control }


| * | * |
|---|---|
| **Frame ID** | 0x63002 |
| **Length [Bytes]** | 3 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

This message has most flags controlling the charge sequence (apart from System_Enable).

The first byte is for flags having effect before a charge session starts.
The second byte is for flags having effect during parameters negotiation.
The third byte is for flags having effect during power stages (insulation test,
precharge and charging).

The controller config file should have the entry &quot;use_sequence_flags = true&quot; in the
&quot;[charger]&quot; section in order to take them into account.

To make sure the controller is taking a first message as initialisation of these
flags, send this first message after Advantics_Controller_Status message reports a
State of Waiting_For_PEV (value 1).

All signals default to value 0. Bits that are not used in this version should remain
at 0 to avoid incompatibility with future versions.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Start_Charge_Authorisation | 1 | Label set |
| CHAdeMO_Start_Button | 1 | Label set |
| CCS_Authorisation_Done | 1 | Label set |
| CCS_Authorisation_Valid | 1 | Label set |
| Charge_Parameters_Done | 1 | Label set |
| User_Stop_Button | 1 | Label set |

### Payload description

#### Start_Charge_Authorisation { #Sequence_Control-Start_Charge_Authorisation }

Indicate if the controller should even attempt to start a charge session.
Suitable for external authorisation permit that happens before user is allowed
to plug or start a charge.

Set to 0 to disallow charging, and 1 to allow.

In CCS, it will keep CP PWM to 100%, even when detecting State B (9V).
In CHAdeMO, it will simply ignore the start button.
But in both case, it will register the user intent as wanting to charge. As soon
as this flag allows charging, it will then start the charge session.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Allowed | 0 |
| Allowed | 1 |

#### CHAdeMO_Start_Button { #Sequence_Control-CHAdeMO_Start_Button }

Simulate a press on the CHAdeMO start button. Only acts on change (so you need to cycle it back to 0).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Pressed | 0 |
| Pressed | 1 |

#### CCS_Authorisation_Done { #Sequence_Control-CCS_Authorisation_Done }

Tells if authorisation of vehicle is finished (CCS only)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Done | 0 |
| Done | 1 |

#### CCS_Authorisation_Valid { #Sequence_Control-CCS_Authorisation_Valid }

Tells if authorisation of vehicle is valid (CCS only). Only meaningful when CCS_Authorisation_Done is 1.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Invalid | 0 |
| Valid | 1 |

#### Charge_Parameters_Done { #Sequence_Control-Charge_Parameters_Done }

Tells when fields in Power_Transfer_Parameters message can be considered stable and sent to the vehicle.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Done | 0 |
| Done | 1 |

#### User_Stop_Button { #Sequence_Control-User_Stop_Button }

Simulate a press on the user stop button (for normal charge termination). Only acts on change (so you need to cycle it back to 0).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Not_Pressed | 0 |
| Pressed | 1 |


<a id="ADM_CS_SECC_Outputs"></a>
## ADM_CS_SECC_Outputs { #ADM_CS_SECC_Outputs }


| * | * |
|---|---|
| **Frame ID** | 0x63201 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

Controller (ADM-CS-SECC hardware variant, ie. &quot;DIN rail&quot;) has various outputs that
can be controlled through this message.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Digital_Output1 | 1 | Single bit |
| Digital_Output2 | 1 | Single bit |
| Digital_Output3 | 1 | Single bit |
| Digital_Output4 | 1 | Single bit |
| Reserved | 60 | Unsigned |

### Payload description

#### Digital_Output1 { #ADM_CS_SECC_Outputs-Digital_Output1 }

Sets the logical state of DIG_OUT1 (CONN5, position 1).
Needs to be declared as CAN Controlled in `/srv/config.cfg`:

    [hardware]
    dig_out1 = CAN_Controlled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Output2 { #ADM_CS_SECC_Outputs-Digital_Output2 }

Reports the logical state of DIG_OUT2 (CONN5, position 2).
Needs to be declared as CAN Controlled in `/srv/config.cfg`:

    [hardware]
    dig_out2 = CAN_Controlled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Output3 { #ADM_CS_SECC_Outputs-Digital_Output3 }

Reports the logical state of DIG_OUT3 (CONN5, position 3).
Needs to be declared as CAN Controlled in `/srv/config.cfg`:

    [hardware]
    dig_out3 = CAN_Controlled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Output4 { #ADM_CS_SECC_Outputs-Digital_Output4 }

Reports the logical state of DIG_OUT4 (CONN5, position 4).
Needs to be declared as CAN Controlled in `/srv/config.cfg`:

    [hardware]
    dig_out4 = CAN_Controlled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Reserved { #ADM_CS_SECC_Outputs-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 60 | Unsigned |  | 1 | 0 |  |  |


<a id="Advantics_Controller_Status"></a>
## Advantics_Controller_Status { #Advantics_Controller_Status }


| * | * |
|---|---|
| **Frame ID** | 0x6b000 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Periodic message reporting the current status of the controller. This message is
sent all the time as soon as the application on the controller is running.

IMPORTANT: Power modules should implement a timeout on the reception of this message.
If the controller does not send this message within 200 ms, then power modules
should consider the controller to be in a defective state and stop any power function
as soon as possible.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| State | 8 | Label set |

### Payload description

#### State { #Advantics_Controller_Status-State }

Current internal state. For information only.

- **Initialising**: Controller&#x27;s applications are starting up.
- **Waiting_For_PEV**: Controller is idle and ready for a plug-in.
- **Negotiating_Connection**: Controller is plugged to a car and the connection is
    being initialised. Important charge information are exchanged.
- **Connected_With_Full_Info**: All charge information from the PEV were retrieved
    and a charge session can be considered to be properly open.
- **Insulation_Test**: Insulation of the charge cable is being tested.
- **Precharge**: Charger is matching its output voltage to the present voltage of the
    battery.
- **Waiting_For_Charge**: PEV is about to begin the actual charging.
- **Charging**: Main charging loop going on.
- **Ending_Charge**: A normal charge stop condition happenned and the PEV is exiting
    the charging loop.
- **Welding_Detection**: PEV is testing if its contactors are welded.
- **Closing_Communication**: PEV can unplug and charger is reinitialising in order to
    then go back to __Waiting_For_PEV__.
- **CCS_Authorisation_Process**: Special state in CCS to authorise user.
- **Not_Available**: Controller has been made unavailable by
    __Sequence_Control.Start_Charge_Authorisation__

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Initialising | 0 |
| Waiting_For_PEV | 1 |
| Negotiating_Connection | 2 |
| Connected_With_Full_Info | 3 |
| Insulation_Test | 4 |
| Precharge | 5 |
| Waiting_For_Charge | 6 |
| Charging | 7 |
| Ending_Charge | 8 |
| Welding_Detection | 9 |
| Closing_Communication | 10 |
| CCS_Authorisation_Process | 11 |
| Not_Available | 12 |
| Charge_Pause | 13 |


<a id="New_Charge_Session"></a>
## New_Charge_Session { #New_Charge_Session }


| * | * |
|---|---|
| **Frame ID** | 0x6b001 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Information about an incoming vehicle. Sent periodically from the moment a car is
plugged in and all the information are known. Until power modules send a
&lt;&lt;Power_Modules_Status.System_Enable&gt;&gt; with value  __Allowed__.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Communication_Protocol | 8 | Label set |
| Plug_and_pins | 8 | Label set |

### Payload description

#### Communication_Protocol { #New_Charge_Session-Communication_Protocol }

The charging protocol the car is using.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| CCS_DIN_70121_2012_v2 | 0 |
| CCS_ISO_15118_2010_v1 | 1 |
| CCS_ISO_15118_2013_v2 | 2 |
| CHAdeMO_v0.9 | 3 |
| CHAdeMO_v1.0-v1.1-v1.2 | 4 |
| CHAdeMO_v2.0 | 5 |
| CCS_PWM | 6 |
| CCS_ISO_15118_2022 | 7 |

#### Plug_and_pins { #New_Charge_Session-Plug_and_pins }

Plug type and DC pins selected by the car.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| CCS_DC_Core | 0 |
| CCS_DC_Extended | 1 |
| CHAdeMO | 2 |
| CCS_AC | 3 |
| MCS | 4 |


<a id="Charge_Status_Change"></a>
## Charge_Status_Change { #Charge_Status_Change }


| * | * |
|---|---|
| **Frame ID** | 0x6b002 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Signal a change in the charging procedure. Sent once only when something change.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Vehicle_Ready_for_Charging | 8 | Label set |

### Payload description

#### Vehicle_Ready_for_Charging { #Charge_Status_Change-Vehicle_Ready_for_Charging }

Tells when the vehicle intend to start or stop the charge.

If value is __Charge_Started__, the power modules must be ready for the
charging loop at any moment (with CCS it can still be in several hours).

When value is __Charge_Stopped__, the vehicle stopped the charging process.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Charge_Stopped | 0 |
| Charge_Started | 1 |


<a id="DC_Power_Control"></a>
## DC_Power_Control { #DC_Power_Control }


| * | * |
|---|---|
| **Frame ID** | 0x6b003 |
| **Length [Bytes]** | 7 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Sent during any powered phase of a DC charge session. This message contains the
power function in use, setpoint targets or range, the setpoints mode, the output
contactors and voltage lowering commands.

# Power function

The power function currently in use is given by &lt;&lt;DC_Power_Control.Power_Function&gt;&gt;.
It covers the off state, standby, insulation test, precharge and the actual power
transfer.

During __Standby__, power modules should disable any power processing function (ie.
turn off), but not bleed their output capacitors (ie. leave the output floating) as
a load might be connected at that time, unless otherwise commanded by
&lt;&lt;DC_Power_Control.Lower_Output_Voltage&gt;&gt;.

During __Insulation_Test__, the insulation of the cable is tested by applying a
voltage from the charger. The battery is not connected yet. The test voltage to
apply is given by &lt;&lt;DC_Power_Control.Target_Voltage&gt;&gt;. Power modules report
&lt;&lt;Power_Modules_Status.Present_Voltage&gt;&gt; and &lt;&lt;Power_Modules_Status.Insulation_Resistance&gt;&gt;
and the controller decides when the test passes or fails. Safety standards require a
minimum of 100 Ohms/V insulation resistance. With a typical test voltage of 500 V,
insulation resistance should be &gt;= 50 kOhms. Maximum current to use is not specified.

During __Precharge__ (CCS only), charger is expected to match battery voltage at its
output while having no load, apart from capacitors on the line. When charging this
capacitive load, it shall not output more current than &lt;&lt;DC_Power_Control.Current_Range_Max&gt;&gt;.
The battery voltage to match is given by &lt;&lt;DC_Power_Control.Target_Voltage&gt;&gt;. The
vehicle decides to consider precharge done when it senses on its inlet a voltage that
is +/- 20 V of its battery voltage.

During __Power_Transfer__, actual power is being transfered in one direction or
another. The meaning of setpoints depends on &lt;&lt;DC_Power_Control.Setpoints_Mode&gt;&gt;.
The transfer direction depends on the sign of current setpoints, with positive
meaning power being delivered to the vehicle (ie. charge). And negative meaning
power extracted from the vehicle (ie. discharge).

NOTE: While targets and ranges are expressed in both voltage and current, it is up
to power modules to determine which control mode they should use (ie. constant current,
constant voltage or constant power) depending on the present situation, and the load
attached to their output. Charging protocols do not define it. In a typical situation,
insulation tests and precharge have to be controlled in Constant Voltage. Whereas,
when a battery is connected to the charger output, the vehicle BMS specifies the
maximum current to be delivered to it, or consummed from it. Which makes it a
Constant Current process. But you might also encounter a vehicle with a different
pack voltage (eg. 800 V), and using a DC/DC in between the charger output and its
battery to convert the voltage. In such case, you might have to run into Constant
Voltage mode for instance.

# Setpoints mode

Either the vehicle control the current to be delivered or consummed (that&#x27;s
__Target_Mode__). Or, a range of acceptable values is given, and power modules are
free to operate within that range (that&#x27;s __Range_Mode__).

In the simplest (historical) case, power transfer is unidirectional, with the
vehicle requesting a certain amount of current for a target voltage, and power
modules have to deliver that current. __Target_Mode__ is used in that case.
And both min and max of the range have the same value. If you do less current than
requested, some vehicle might accept it, and some might terminate the charge on a
current deviation error. &lt;&lt;Power_Transfer_Parameters.Maximum_Charge_Current&gt;&gt; offers
a way to dynamically &quot;negotiate&quot; a lower current request properly.

If the vehicle and/or charging protocol wants to use limits instead of targets (eg.
CHAdeMO V2G, or ISO 15118-20 in Dynamic mode), then __Range_Mode__ is used. The min
and max of the range are given, and power modules can choose the actual load and
power transfer direction within that range.

Note however that, if in your application power modules are not able to decide of
the load by themselves, then you can treat the maximum of the range as the target
setpoint (which is why the same signal is used for both target and maximum).

During a power transfer, the setpoint mode does not change between range or target.
However, during the rest of the session, for consistency, during __Insulation_Test__
it will be __Target_Mode__. And during __Precharge__ it will be __Range_Mode__.
During other power functions it is not relevant.

# Bidirectional power transfers

Bidirectional power transfers are only possible when both the vehicle and the charger
supports it (on charger side, `is_bidirectional` has to be set to True in the config
file for that pistol). Bidirectional power transfer can happen either in
__Range_Mode__ (power modules choose when to switch over) or __Target_Mode__ (vehicle
decides when it is time to charge or discharge its battery). Bidirectional in range
mode would typically happen with CHAdeMO V2G, or ISO 15118-20 in Dynamic mode.
Whereas birectional in target mode would happen with ISO 15118-20 in Scheduled mode.

When in range mode, a portion of the range will be in the negative values (or all of
it if only discharge is possible). Note that the positive portion of the range, used
for charging, naturally follows min and max charge current values. Whereas the
negative portion of the range, used for discharging, is mirrored, and its min and
max are logically inverted. Said differently &lt;&lt;DC_Power_Control.Current_Range_Min&gt;&gt;
shows the maximum discharge current, but with a negative sign. And
&lt;&lt;DC_Power_Control.Current_Range_Max&gt;&gt; shows the maximum charge current with a
positive sign.

In the particular situation only discharge is possible, the minimum of the range is
still the maximum discharge current with a negative sign. And the maximum of the
range is then the minimum discharge current, also with a negative sign.

As such, you can see this range as a &quot;continuous slider&quot; on which you can pick an
operating point, moving between the maximum discharge current (the min), and the
maximum charge current (the max). With 0 as a midpoint (but not necessarily
symmetric). If no discharge is possible, then the min is positive. And if no charge
is possible, then the max is negative.

WARNING: The vehicle might not necessarily ramps up or down its requests.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Target_Voltage | 16 | Unsigned |
| Current_Range_Max | 16 | Signed |
| Current_Range_Min | 16 | Signed |
| Power_Function | 4 | Label set |
| Reserved | 1 | Single bit |
| Setpoints_Mode | 1 | Label set |
| Output_Contactors | 1 | Label set |
| Lower_Output_Voltage | 1 | Label set |

### Payload description

#### Target_Voltage { #DC_Power_Control-Target_Voltage }

Voltage setpoint.

In __Insulation_Test__, this is the test voltage, and it should corresponds to
the maximum voltage a charger can theoretically deliver during a charge session.
At the end of the test, this setpoint is set back to 0 V.

In __Precharge__, it usually corresponds to the real battery voltage (unless the
vehicle uses an intermediate DC/DC).

In __Power_Transfer__, it usually corresponds to a voltage significantly higher
than the battery voltage (implying a Constant Current process). However, if the
vehicle uses an intermediate DC/DC, then it corresponds to the input voltage of
that DC/DC.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Current_Range_Max { #DC_Power_Control-Current_Range_Max }

Maximum current to provide (if positive), or minimum current to draw (if negative).

In __Target_Mode__, this signal should be used as the target current setpoint.

In __Insulation_Test__, this signal is not relevant.

In __Precharge__, this signal carries the maximum current the vehicle wants
charger to respect. Usually a value between 0 and 2 A.

In __Power_Transfer__, this signal gives the maximum of the current range to use.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Amps | 0.1 | 0 |  |  |

#### Current_Range_Min { #DC_Power_Control-Current_Range_Min }

Maximum current to draw (if negative), or minimum current to provide (if positive).

In __Target_Mode__, this signal will have the same value than
&lt;&lt;DC_Power_Control.Current_Range_Max&gt;&gt;.

In __Insulation_Test__, this signal is not relevant.

In __Precharge__, this signal is 0 A.

In __Power_Transfer__, this signal gives the minimum of the current range to use.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | Amps | 0.1 | 0 |  |  |

#### Power_Function { #DC_Power_Control-Power_Function }

This signal describes the sort of power function expected from power modules at
a particular point in the process.

__Off__: Power modules turn off any power processing function. And the output of
the charger (exposed on the pistol pins) has ~0 V, floating.

__Standby__: Power modules do not run any power processing function, while
remaining ready to receive future requests. A load might still be connected to
their output. Therefore, unless comanded by &lt;&lt;DC_Power_Control.Lower_Output_Voltage&gt;&gt;,
it should remain floating, with contactors still closed, and no discharge of
their output capacitors should be attempted.

__Insulation_Test__: Power modules (or an external dedicated safety module) apply
high voltage and measure the current leaked through ground. The test voltage
reaches up to the vehicle, but its input contactors are still open.

__Precharge__: Power modules match the requested voltage while limiting their
output current (only some capacitance should be charged during this process).
The purpose is to avoid arcing when vehicle contactors close.
Precharge is specific to CCS. In CHAdeMO you either have a diode at the output
of the charger (unidirectional). Or a custom precharge circuit around the main
output contactors (bidirectionnal, or unidirectional made without diode).

__Power_Transfer__: Main mode of operation, as power is being transfered in one
way or another. See the documentation of &lt;&lt;DC_Power_Control.Setpoints_Mode&gt;&gt; and
others signals of this message for more details.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 4 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Off | 0 |
| Standby | 1 |
| Insulation_Test | 2 |
| Precharge | 4 |
| Power_Transfer | 8 |

#### Reserved { #DC_Power_Control-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 52 | 1 | Single bit |  | 1 | 0 |  |  |

#### Setpoints_Mode { #DC_Power_Control-Setpoints_Mode }

Defines how power modules should follow setpoints.

__Target_Mode__: Power transfer is controlled by the vehicle, and power modules
should follow the given targets. Min and max of the range have the same value.

__Range_Mode__: All parties provide ranges of acceptable limits, and the
controller gives a merged view of that range. Power modules are then free to
provide or draw power within that range.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 53 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Target_Mode | 0 |
| Range_Mode | 1 |

#### Output_Contactors { #DC_Power_Control-Output_Contactors }

Reflects contactors control done using controller&#x27;s onboard relay.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 54 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Open | 0 |
| Close | 1 |

#### Lower_Output_Voltage { #DC_Power_Control-Lower_Output_Voltage }

Tells when charger output voltage should forcibly be lowered to less than or
equal to 20 V. It can be done, for instance, by bleeding the voltage of power
modules output capacitors.

Can only happen in __Standby__ function, with voltage and current setpoints set
to 0.

Output voltage lowering is requested at the following points in the charge
session:

- After insulation test, and before precharge (CCS) or power transfer (CHAdeMO).
  In this case, the controller does not command output contactors to open by
  itself (ie. using its onboard relay) as they would have to reclose shortly
  after. It will however wait that output voltage lower to &lt;= 20 V to comply
  with charging standards.
- After power transfer, when &lt;&lt;Advantics_Controller_Status.State&gt;&gt; is
  __Ending_Charge__, current has lowered to less than 1 A, and after having
  opened output contactors. In this case, the controller does not need to wait
  for voltage to lower. Note that at this point the vehicle battery might still
  be connected to pistol pins (hence why it does not wait on the voltage). Which
  means if your charger does not have output contactors, you should actually
  avoid bleeding output capacitors at this point, and ignore the lowering request.
- When entering &lt;&lt;Advantics_Controller_Status.State&gt;&gt; == __Closing_Communication__
  if output voltage is above 20 V. It could happen after a welding detection
  process from the vehicle in case there are no output contactors and output
  capacitors are still charged (or got recharged during welding detection). This
  lowering request is for safety, in order to avoid exposing high voltages on
  the pistol contacts once it gets unplugged from the vehicle.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 55 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| No_Lowering | 0 |
| Lowering | 1 |


<a id="Charge_Session_Finished"></a>
## Charge_Session_Finished { #Charge_Session_Finished }


| * | * |
|---|---|
| **Frame ID** | 0x6b004 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Charging is over and the vehicle should unplug soon.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| State | 8 | Label set |

### Payload description

#### State { #Charge_Session_Finished-State }

Was the session terminated cleanly or not.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clean_Stop | 0 |
| Rushed_Stop | 1 |


<a id="Emergency_Stop"></a>
## Emergency_Stop { #Emergency_Stop }


| * | * |
|---|---|
| **Frame ID** | 0x6b005 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Sent from the moment an emergency stop has been triggered.

Emergency_Stop are not explicitly rearmable. You either power cycle the whole setup.
Or the emergency condition disappear, and the message will stop being sent once the
controller pass in a state where it reevaluates emergency conditions.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Origin | 8 | Label set |

### Payload description

#### Origin { #Emergency_Stop-Origin }

From which side the emergency stop came from.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| EVSE | 1 |
| PEV | 3 |


<a id="EV_Information_Battery"></a>
## EV_Information_Battery { #EV_Information_Battery }


| * | * |
|---|---|
| **Frame ID** | 0x6b100 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Vehicle battery information.

Sent at least once after first &lt;&lt;New_Charge_Session&gt;&gt; message. As well as every time
vehicle changes these information.

Many of these information can be optional. There default value is 0 if the vehicle
did not sent them.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Battery_Capacity | 16 | Unsigned |
| Present_State_of_Charge | 8 | Unsigned |
| Minimum_State_of_Charge | 8 | Unsigned |
| Target_State_of_Charge | 8 | Unsigned |
| Maximum_State_of_Charge | 8 | Unsigned |

### Payload description

#### Battery_Capacity { #EV_Information_Battery-Battery_Capacity }

Total battery capacity.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | kWh | 1 | 0 |  |  |

#### Present_State_of_Charge { #EV_Information_Battery-Present_State_of_Charge }

Battery SoC, in percent.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |

#### Minimum_State_of_Charge { #EV_Information_Battery-Minimum_State_of_Charge }

Minimum battery SoC vehicle wants, in percent.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |

#### Target_State_of_Charge { #EV_Information_Battery-Target_State_of_Charge }

Target battery SoC vehicle wants, in percent.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |

#### Maximum_State_of_Charge { #EV_Information_Battery-Maximum_State_of_Charge }

Maximum battery SoC vehicle wants, in percent.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |


<a id="EV_Information_Voltages"></a>
## EV_Information_Voltages { #EV_Information_Voltages }


| * | * |
|---|---|
| **Frame ID** | 0x6b101 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Vehicle voltages information.

Sent at least once after first &lt;&lt;New_Charge_Session&gt;&gt; message. As well as every time
vehicle changes these information.

Many of these information can be optional. There default value is 0 if the vehicle
did not sent them.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| EV_Minimum_Voltage | 16 | Unsigned |
| EV_Maximum_Voltage | 16 | Unsigned |
| EV_Present_Voltage | 16 | Unsigned |

### Payload description

#### EV_Minimum_Voltage { #EV_Information_Voltages-EV_Minimum_Voltage }

Minimum vehicle voltage.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### EV_Maximum_Voltage { #EV_Information_Voltages-EV_Maximum_Voltage }

Maximum vehicle voltage.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### EV_Present_Voltage { #EV_Information_Voltages-EV_Present_Voltage }

Present voltage reported by vehicle.

Note: Can be use in Constant Voltage mode to compensate for cable losses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |


<a id="EV_Information_Charge_Limits"></a>
## EV_Information_Charge_Limits { #EV_Information_Charge_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x6b102 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Vehicle information for current and power limits during charging.

Sent at least once after first &lt;&lt;New_Charge_Session&gt;&gt; message. As well as every time
vehicle changes these information.

Many of these information can be optional. There default value is 0 if the vehicle
did not sent them.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| EV_Minimum_Charge_Current | 16 | Unsigned |
| EV_Maximum_Charge_Current | 16 | Unsigned |
| EV_Minimum_Charge_Power | 16 | Unsigned |
| EV_Maximum_Charge_Power | 16 | Unsigned |

### Payload description

#### EV_Minimum_Charge_Current { #EV_Information_Charge_Limits-EV_Minimum_Charge_Current }

Minimum vehicle charge current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### EV_Maximum_Charge_Current { #EV_Information_Charge_Limits-EV_Maximum_Charge_Current }

Maximum vehicle charge current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### EV_Minimum_Charge_Power { #EV_Information_Charge_Limits-EV_Minimum_Charge_Power }

Minimum vehicle charge power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | kW | 1 | 0 |  |  |

#### EV_Maximum_Charge_Power { #EV_Information_Charge_Limits-EV_Maximum_Charge_Power }

Maximum vehicle charge power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned | kW | 1 | 0 |  |  |


<a id="EV_Information_Discharge_Limits"></a>
## EV_Information_Discharge_Limits { #EV_Information_Discharge_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x6b103 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Vehicle information for current and power limits during discharging.

Sent at least once after first &lt;&lt;New_Charge_Session&gt;&gt; message. As well as every time
vehicle changes these information.

Many of these information can be optional. There default value is 0 if the vehicle
did not sent them.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| EV_Minimum_Discharge_Current | 16 | Unsigned |
| EV_Maximum_Discharge_Current | 16 | Unsigned |
| EV_Minimum_Discharge_Power | 16 | Unsigned |
| EV_Maximum_Discharge_Power | 16 | Unsigned |

### Payload description

#### EV_Minimum_Discharge_Current { #EV_Information_Discharge_Limits-EV_Minimum_Discharge_Current }

Minimum vehicle discharge current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### EV_Maximum_Discharge_Current { #EV_Information_Discharge_Limits-EV_Maximum_Discharge_Current }

Maximum vehicle discharge current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### EV_Minimum_Discharge_Power { #EV_Information_Discharge_Limits-EV_Minimum_Discharge_Power }

Minimum vehicle discharge power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | kW | 1 | 0 |  |  |

#### EV_Maximum_Discharge_Power { #EV_Information_Discharge_Limits-EV_Maximum_Discharge_Power }

Maximum vehicle discharge power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Unsigned | kW | 1 | 0 |  |  |


<a id="EV_Information_Energy"></a>
## EV_Information_Energy { #EV_Information_Energy }


| * | * |
|---|---|
| **Frame ID** | 0x6b104 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

Vehicle information for energy.

Sent at least once after first &lt;&lt;New_Charge_Session&gt;&gt; message. As well as every time
vehicle changes these information.

Many of these information can be optional. There default value is 0 if the vehicle
did not sent them.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| EV_Minimum_Energy_Request | 16 | Signed |
| EV_Target_Energy_Request | 16 | Signed |
| EV_Maximum_Energy_Request | 16 | Signed |

### Payload description

#### EV_Minimum_Energy_Request { #EV_Information_Energy-EV_Minimum_Energy_Request }

Minimum (estimated) remaining energy vehicle will consumme (positive value),
or provide (negative value).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | kWh | 1 | 0 |  |  |

#### EV_Target_Energy_Request { #EV_Information_Energy-EV_Target_Energy_Request }

Targeted (estimated) remaining energy vehicle will consumme (positive value),
or provide (negative value).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | kWh | 1 | 0 |  |  |

#### EV_Maximum_Energy_Request { #EV_Information_Energy-EV_Maximum_Energy_Request }

Maximum (estimated) remaining energy vehicle will consumme (positive value),
or provide (negative value).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | kWh | 1 | 0 |  |  |


<a id="EV_ID_CCS_Part2_DIN"></a>
## EV_ID_CCS_Part2_DIN { #EV_ID_CCS_Part2_DIN }


| * | * |
|---|---|
| **Frame ID** | 0x6b105 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The EV ID provided by the vehicle in CCS DIN SPEC 70121 and ISO 15118-2.
EV ID for CCS ISO 15118-20 is not supported by this message.
(the EV ID is defined as a string of max 255 characters in ISO 15118-20)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Byte0 | 8 | Unsigned |
| Byte1 | 8 | Unsigned |
| Byte2 | 8 | Unsigned |
| Byte3 | 8 | Unsigned |
| Byte4 | 8 | Unsigned |
| Byte5 | 8 | Unsigned |

### Payload description

#### Byte0 { #EV_ID_CCS_Part2_DIN-Byte0 }

Byte 0 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Byte1 { #EV_ID_CCS_Part2_DIN-Byte1 }

Byte 1 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Byte2 { #EV_ID_CCS_Part2_DIN-Byte2 }

Byte 2 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Byte3 { #EV_ID_CCS_Part2_DIN-Byte3 }

Byte 3 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Byte4 { #EV_ID_CCS_Part2_DIN-Byte4 }

Byte 4 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned |  | 1 | 0 |  |  |

#### Byte5 { #EV_ID_CCS_Part2_DIN-Byte5 }

Byte 5 of the EV ID.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned |  | 1 | 0 |  |  |


<a id="ADM_CO_CUI1_Inputs"></a>
## ADM_CO_CUI1_Inputs { #ADM_CO_CUI1_Inputs }


| * | * |
|---|---|
| **Frame ID** | 0x6b200 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Controller (ADM-CO-CUI1 hardware variant, ie. &quot;generic/mobile&quot;) is reporting various
information about its inputs. It is sent every seconds (for temperature channels).
Or on change for other digital inputs.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| SWITCH0 | 1 | Single bit |
| SWITCH1 | 1 | Single bit |
| SWITCH2 | 1 | Single bit |
| SWITCH3 | 1 | Single bit |
| SWITCH4 | 1 | Single bit |
| SWITCH5 | 1 | Single bit |
| Reserved | 26 | Unsigned |
| Colibri_Temperature | 8 | Unsigned |
| CPU_Temperature | 8 | Unsigned |
| Pistol_PTC1 | 8 | Unsigned |
| Pistol_PTC2 | 8 | Unsigned |

### Payload description

#### SWITCH0 { #ADM_CO_CUI1_Inputs-SWITCH0 }

Reports the logical state of SWITCH0 (J7, position 1).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch0 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### SWITCH1 { #ADM_CO_CUI1_Inputs-SWITCH1 }

Reports the logical state of SWITCH1 (J7, position 2).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch1 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### SWITCH2 { #ADM_CO_CUI1_Inputs-SWITCH2 }

Reports the logical state of SWITCH2 (J7, position 3).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch2 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### SWITCH3 { #ADM_CO_CUI1_Inputs-SWITCH3 }

Reports the logical state of SWITCH3 (J7, position 4).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch3 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### SWITCH4 { #ADM_CO_CUI1_Inputs-SWITCH4 }

Reports the logical state of SWITCH4 (J7, position 5).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch4 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### SWITCH5 { #ADM_CO_CUI1_Inputs-SWITCH5 }

Reports the logical state of SWITCH5 (J7, position 6).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    switch5 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Reserved { #ADM_CO_CUI1_Inputs-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 26 | Unsigned |  | 1 | 0 |  |  |

#### Colibri_Temperature { #ADM_CO_CUI1_Inputs-Colibri_Temperature }

Temperature measured on the Colibri SoM board of the charge controller.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### CPU_Temperature { #ADM_CO_CUI1_Inputs-CPU_Temperature }

Temperature reported by the CPU chip of the charge controller.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### Pistol_PTC1 { #ADM_CO_CUI1_Inputs-Pistol_PTC1 }

Measured temperature sensor on first PTC channel associated to this pistol.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### Pistol_PTC2 { #ADM_CO_CUI1_Inputs-Pistol_PTC2 }

Measured temperature sensor on second PTC channel associated to this pistol.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |


<a id="ADM_CS_SECC_Inputs"></a>
## ADM_CS_SECC_Inputs { #ADM_CS_SECC_Inputs }


| * | * |
|---|---|
| **Frame ID** | 0x6b201 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Controller (ADM-CS-SECC hardware variant, ie. &quot;DIN rail&quot;) is reporting various
information about its inputs. It is sent every seconds (for temperature channels).
Or on change for other digital inputs.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Digital_Input1 | 1 | Single bit |
| Digital_Input2 | 1 | Single bit |
| Digital_Input3 | 1 | Single bit |
| Digital_Input4 | 1 | Single bit |
| Reserved | 36 | Unsigned |
| CPU_Temperature | 8 | Unsigned |
| Pistol_PTC1 | 8 | Unsigned |
| Pistol_PTC2 | 8 | Unsigned |

### Payload description

#### Digital_Input1 { #ADM_CS_SECC_Inputs-Digital_Input1 }

Reports the logical state of DIG_IN1 (CONN6, position 1).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in1 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input2 { #ADM_CS_SECC_Inputs-Digital_Input2 }

Reports the logical state of DIG_IN2 (CONN6, position 2).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in2 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input3 { #ADM_CS_SECC_Inputs-Digital_Input3 }

Reports the logical state of DIG_IN3 (CONN6, position 3).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in3 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input4 { #ADM_CS_SECC_Inputs-Digital_Input4 }

Reports the logical state of DIG_IN4 (CONN6, position 4).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in4 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Reserved { #ADM_CS_SECC_Inputs-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 36 | Unsigned |  | 1 | 0 |  |  |

#### CPU_Temperature { #ADM_CS_SECC_Inputs-CPU_Temperature }

Temperature reported by the CPU chip of the charge controller.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### Pistol_PTC1 { #ADM_CS_SECC_Inputs-Pistol_PTC1 }

Measured temperature sensor on first PTC channel associated to this pistol.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### Pistol_PTC2 { #ADM_CS_SECC_Inputs-Pistol_PTC2 }

Measured temperature sensor on second PTC channel associated to this pistol.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |


<a id="ADM_CS_SPCC_Inputs"></a>
## ADM_CS_SPCC_Inputs { #ADM_CS_SPCC_Inputs }


| * | * |
|---|---|
| **Frame ID** | 0x6b202 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Controller (ADM-CS-SPCC hardware variant) is reporting various
information about its inputs. It is sent every seconds (for temperature channels).
Or on change for other digital inputs.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Digital_Input1 | 1 | Single bit |
| Digital_Input2 | 1 | Single bit |
| Digital_Input3 | 1 | Single bit |
| Digital_Input4 | 1 | Single bit |
| Reserved | 4 | Unsigned |
| CPU_Temperature0 | 8 | Unsigned |
| CPU_Temperature1 | 8 | Unsigned |
| PT1K_A | 8 | Unsigned |
| PT1K_B | 8 | Unsigned |
| PT1KS_C | 8 | Unsigned |
| PT1KS_D | 8 | Unsigned |

### Payload description

#### Digital_Input1 { #ADM_CS_SPCC_Inputs-Digital_Input1 }

Reports the logical state of DIG_IN1 (CONN6, position 1).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in1 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input2 { #ADM_CS_SPCC_Inputs-Digital_Input2 }

Reports the logical state of DIG_IN2 (CONN6, position 2).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in2 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input3 { #ADM_CS_SPCC_Inputs-Digital_Input3 }

Reports the logical state of DIG_IN3 (CONN6, position 3).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in3 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Digital_Input4 { #ADM_CS_SPCC_Inputs-Digital_Input4 }

Reports the logical state of DIG_IN4 (CONN6, position 4).
Needs to be declared as monitored in `/srv/config.cfg`:

    [hardware]
    dig_in4 = Monitor

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Single bit |  | 1 | 0 | 0 | 1 |

#### Reserved { #ADM_CS_SPCC_Inputs-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 4 | Unsigned |  | 1 | 0 |  |  |

#### CPU_Temperature0 { #ADM_CS_SPCC_Inputs-CPU_Temperature0 }

Temperature reported by the CPU chip of the charge controller.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### CPU_Temperature1 { #ADM_CS_SPCC_Inputs-CPU_Temperature1 }

Temperature reported by the CPU chip of the charge controller.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### PT1K_A { #ADM_CS_SPCC_Inputs-PT1K_A }

This input is used as CHAdeMO pistol solenoid input when the controller is configured for CHAdeMO.
When the controller is configured for MCS, CCS DC or AC, this input can be used as a temperature sensor.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### PT1K_B { #ADM_CS_SPCC_Inputs-PT1K_B }

Measured temperature sensor on PT1K_B input.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### PT1KS_C { #ADM_CS_SPCC_Inputs-PT1KS_C }

Measured temperature sensor on PT1KS_C input.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |

#### PT1KS_D { #ADM_CS_SPCC_Inputs-PT1KS_D }

Measured temperature sensor on PT1KS_D input.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | °C | 1 | -40 | -40 | 215 |


<a id="CCS_Extra_Information"></a>
## CCS_Extra_Information { #CCS_Extra_Information }


| * | * |
|---|---|
| **Frame ID** | 0x6b203 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Extra information from CCS (for information only).
!!! info
        Available since version 4.2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| CP_State | 8 | Label set |
| CP_Duty_Cycle | 16 | Unsigned |
| Reserved | 40 | Unsigned |

### Payload description

#### CP_State { #CCS_Extra_Information-CP_State }

Measured CP state.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| E_or_F | 0 |
| D | 3 |
| C | 6 |
| B | 9 |
| A | 12 |

#### CP_Duty_Cycle { #CCS_Extra_Information-CP_Duty_Cycle }

Measured PWM duty cycle on the CP line.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 16 | Unsigned | % | 0.1 | 0 | 0 | 100 |

#### Reserved { #CCS_Extra_Information-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 40 | Unsigned |  | 1 | 0 |  |  |


<a id="MCS_Extra_Information"></a>
## MCS_Extra_Information { #MCS_Extra_Information }


| * | * |
|---|---|
| **Frame ID** | 0x6b204 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Extra information from MCS (for information only).
!!! info
        Available since version 4.2

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| CE_State | 8 | Label set |
| ID_State | 8 | Label set |
| Reserved | 48 | Unsigned |

### Payload description

#### CE_State { #MCS_Extra_Information-CE_State }

Measured CE state.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Undefined | 0 |
| A | 1 |
| B0 | 2 |
| B0_Aux | 3 |
| B | 4 |
| B_Aux | 5 |
| C | 6 |
| C_Aux | 7 |
| EC | 8 |
| E | 9 |

#### ID_State { #MCS_Extra_Information-ID_State }

Measured ID state.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Unmated | 0 |
| Mated | 1 |
| Mated_EVAux | 2 |
| Mated_EVSEAux | 3 |

#### Reserved { #MCS_Extra_Information-Reserved }

Reserved bits for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 48 | Unsigned |  | 1 | 0 |  |  |


<a id="OCPP_Control"></a>
## OCPP_Control { #OCPP_Control }


| * | * |
|---|---|
| **Frame ID** | 0x6b300 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** |  |
| **Direction** | OUT |

### Description

OCPP information needed for power transfer

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Dynamic_Target_Current | 16 | Signed |

### Payload description

#### Dynamic_Target_Current { #OCPP_Control-Dynamic_Target_Current }

This signal is useful only during power transfer using CCS ISO15118-20 Dynamic mode.
As the charger negociates a current range with the vehicle, a third party needs to specify
the current setpoint within that range.
OCPP1.6J was adapted to provide this inforamtion.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | Amps | 0.1 | 0 |  |  |
