# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [Power_Modules_Status](#Power_Modules_Status) | 0x60010 | 8 | IN | 100 |
| [Power_Modules_Limits](#Power_Modules_Limits) | 0x60011 | 8 | IN |  |
| [Sequence_Control](#Sequence_Control) | 0x60012 | 3 | IN |  |
| [ADM_CS_SECC_Outputs](#ADM_CS_SECC_Outputs) | 0x60013 | 8 | IN | 1000 |
| [New_Charge_Session](#New_Charge_Session) | 0x68001 | 8 | OUT | 100 |
| [Insulation_Test](#Insulation_Test) | 0x68002 | 2 | OUT | 100 |
| [Precharge](#Precharge) | 0x68003 | 4 | OUT | 100 |
| [Charge_Status_Change](#Charge_Status_Change) | 0x68004 | 1 | OUT |  |
| [Charging_Loop](#Charging_Loop) | 0x68005 | 5 | OUT | 100 |
| [Emergency_Stop](#Emergency_Stop) | 0x68006 | 1 | OUT | 100 |
| [Charge_Session_Finished](#Charge_Session_Finished) | 0x68007 | 1 | OUT |  |
| [Advantics_Controller_Status](#Advantics_Controller_Status) | 0x68009 | 1 | OUT | 100 |
| [ADM_CO_CUI1_Inputs](#ADM_CO_CUI1_Inputs) | 0x6800a | 8 | OUT | 1000 |
| [ADM_CS_SECC_Inputs](#ADM_CS_SECC_Inputs) | 0x6800b | 8 | OUT | 1000 |
| [EV_ID_CCS_Part2_DIN](#EV_ID_CCS_Part2_DIN) | 0x6800c | 6 | OUT | 1000 |
| [ADM_CS_SPCC_Inputs](#ADM_CS_SPCC_Inputs) | 0x6800d | 8 | OUT | 1000 |
| [CCS_Extra_Information](#CCS_Extra_Information) | 0x6800e | 8 | OUT | 100 |
| [MCS_Extra_Information](#MCS_Extra_Information) | 0x6800f | 8 | OUT | 100 |


<a id="Power_Modules_Status"></a>
## Power_Modules_Status { #Power_Modules_Status }


| * | * |
|---|---|
| **Frame ID** | 0x60010 |
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


<a id="Power_Modules_Limits"></a>
## Power_Modules_Limits { #Power_Modules_Limits }


| * | * |
|---|---|
| **Frame ID** | 0x60011 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Periodic message reporting the current limits of power modules. This message can be
sent as often as needed (but not faster than 100ms).

Values reported here will be capped by limits statically defined in the config file.
If a value is set to 0, then it means to use default limits from the config file.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Maximum_Voltage | 16 | Unsigned |
| Maximum_Current | 16 | Signed |
| Reserved | 32 | Unsigned |

### Payload description

#### Maximum_Voltage { #Power_Modules_Limits-Maximum_Voltage }

Max output voltage of the charger

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Maximum_Current { #Power_Modules_Limits-Maximum_Current }

Maximum output current of the charger

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Amps | 0.1 | 0 |  |  |

#### Reserved { #Power_Modules_Limits-Reserved }

Reserved bytes for future uses.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="Sequence_Control"></a>
## Sequence_Control { #Sequence_Control }


| * | * |
|---|---|
| **Frame ID** | 0x60012 |
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

Tells when fields in Power_Modules_Limits message can be considered stable and sent to the vehicle.

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
| **Frame ID** | 0x60013 |
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


<a id="New_Charge_Session"></a>
## New_Charge_Session { #New_Charge_Session }


| * | * |
|---|---|
| **Frame ID** | 0x68001 |
| **Length [Bytes]** | 8 |
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
| EV_Maximum_Voltage | 16 | Unsigned |
| EV_Maximum_Current | 16 | Unsigned |
| Battery_Capacity | 8 | Unsigned |
| State_of_Charge | 8 | Unsigned |

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

#### EV_Maximum_Voltage { #New_Charge_Session-EV_Maximum_Voltage }

Maximum battery voltage.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### EV_Maximum_Current { #New_Charge_Session-EV_Maximum_Current }

Maximum battery current (optional, not all communication protocols give it).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |

#### Battery_Capacity { #New_Charge_Session-Battery_Capacity }

Total battery capacity (optional, not all communication protocols give it).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 8 | Unsigned | kWh | 2 | 0 | 0 | 510 |

#### State_of_Charge { #New_Charge_Session-State_of_Charge }

Battery SoC in percent.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 56 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |


<a id="Insulation_Test"></a>
## Insulation_Test { #Insulation_Test }


| * | * |
|---|---|
| **Frame ID** | 0x68002 |
| **Length [Bytes]** | 2 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Test the insulation of the cable by applying a voltage from the charger. The battery
is not connected yet. Power modules report &lt;&lt;Power_Modules_Status.Present_Voltage&gt;&gt;
and &lt;&lt;Power_Modules_Status.Insulation_Resistance&gt;&gt; and the controller decides when
the test passes or fails.

Safety standards require a minimum of 100 Ohms/V insulation resistance. With a
typical test voltage of 500 V, insulation resistance should be &gt;= 50 kOhms.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Test_Voltage | 16 | Unsigned |

### Payload description

#### Test_Voltage { #Insulation_Test-Test_Voltage }

Voltage to apply.

Will be set back to 0 at the end of the test.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |


<a id="Precharge"></a>
## Precharge { #Precharge }


| * | * |
|---|---|
| **Frame ID** | 0x68003 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Precharge procedure, with CCS only. The vehicle decides to consider precharge done
when it senses voltage on its inlet to be close at 20 V to battery voltage.

Charger is expected to match battery voltage at its output while having no load,
apart from the capacitors on the line. When charging this capacitive load, it shall
not output more current than &lt;&lt;Precharge.Maximum_Current&gt;&gt;.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Target_Voltage | 16 | Unsigned |
| Maximum_Current | 16 | Unsigned |

### Payload description

#### Target_Voltage { #Precharge-Target_Voltage }

Voltage to apply.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Maximum_Current { #Precharge-Maximum_Current }

Maximum current allowed by the vehicle (shouldn&#x27;t be more than 2A).

Will be set back to 0 at the end of the precharge procedure.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Amps | 0.1 | 0 |  |  |


<a id="Charge_Status_Change"></a>
## Charge_Status_Change { #Charge_Status_Change }


| * | * |
|---|---|
| **Frame ID** | 0x68004 |
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


<a id="Charging_Loop"></a>
## Charging_Loop { #Charging_Loop }


| * | * |
|---|---|
| **Frame ID** | 0x68005 |
| **Length [Bytes]** | 5 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Sent during the main charging loop. The vehicle is basically requesting current.
Note that while the request is expressed in both voltage and current, it is up to
power modules to determine which control mode they should run (ie. constant current,
constant voltage or constant power).

WARNING: The vehicle might not necessarily ramps up or down its requests.

IMPORTANT: It is also sent at few other moments in the charging process with values
&lt;&lt;Charging_Loop.Target_Voltage&gt;&gt; == 0 and &lt;&lt;Charging_Loop.Target_Current&gt;&gt; == 0.
This has the meaning of telling the power modules to go into a sort of &quot;Standby&quot;
mode. The power modules should turn off any power processing function, while remaning
ready to receive future requests.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Target_Voltage | 16 | Unsigned |
| Target_Current | 16 | Signed |
| State_of_Charge | 8 | Unsigned |

### Payload description

#### Target_Voltage { #Charging_Loop-Target_Voltage }

Voltage to apply.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Volts | 0.1 | 0 |  |  |

#### Target_Current { #Charging_Loop-Target_Current }

Current to provide.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | Amps | 0.1 | 0 |  |  |

#### State_of_Charge { #Charging_Loop-State_of_Charge }

Battery SoC in percent (informative, do not rely on it).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 8 | Unsigned | % | 1 | 0 | 0 | 100 |


<a id="Emergency_Stop"></a>
## Emergency_Stop { #Emergency_Stop }


| * | * |
|---|---|
| **Frame ID** | 0x68006 |
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


<a id="Charge_Session_Finished"></a>
## Charge_Session_Finished { #Charge_Session_Finished }


| * | * |
|---|---|
| **Frame ID** | 0x68007 |
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


<a id="Advantics_Controller_Status"></a>
## Advantics_Controller_Status { #Advantics_Controller_Status }


| * | * |
|---|---|
| **Frame ID** | 0x68009 |
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


<a id="ADM_CO_CUI1_Inputs"></a>
## ADM_CO_CUI1_Inputs { #ADM_CO_CUI1_Inputs }


| * | * |
|---|---|
| **Frame ID** | 0x6800a |
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
| **Frame ID** | 0x6800b |
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


<a id="EV_ID_CCS_Part2_DIN"></a>
## EV_ID_CCS_Part2_DIN { #EV_ID_CCS_Part2_DIN }


| * | * |
|---|---|
| **Frame ID** | 0x6800c |
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


<a id="ADM_CS_SPCC_Inputs"></a>
## ADM_CS_SPCC_Inputs { #ADM_CS_SPCC_Inputs }


| * | * |
|---|---|
| **Frame ID** | 0x6800d |
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
| **Frame ID** | 0x6800e |
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
| **Frame ID** | 0x6800f |
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
