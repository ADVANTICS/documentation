# CAN messages

## Message index

| Name | ID | Length | Direction | Cycle time |
|------|----|--------|-----------|------------|
| [DC_Ports_Setpoints](#DC_Ports_Setpoints) | 0x850020 | 6 | IN | 1000 |
| [DC_Port_Applied_Setpoints](#DC_Port_Applied_Setpoints) | 0x850021 | 8 | OUT | 1000 |
| [DC_Port_Droop_Setpoints](#DC_Port_Droop_Setpoints) | 0x850022 | 8 | IN |  |
| [DC_Port_Applied_Droop_Setpoints](#DC_Port_Applied_Droop_Setpoints) | 0x850023 | 8 | OUT | 1000 |
| [DC_Port_Measurements](#DC_Port_Measurements) | 0x850024 | 4 | OUT | 100 |
| [AC_Port_Setpoints](#AC_Port_Setpoints) | 0x850030 | 8 | IN |  |
| [AC_Port_Applied_Setpoints](#AC_Port_Applied_Setpoints) | 0x850031 | 8 | OUT | 1000 |
| [AC_Port_Droop_Setpoints](#AC_Port_Droop_Setpoints) | 0x850032 | 8 | IN |  |
| [AC_Port_Applied_Droop_Setpoints](#AC_Port_Applied_Droop_Setpoints) | 0x850033 | 8 | OUT | 1000 |
| [AC_Port_Measurements](#AC_Port_Measurements) | 0x850034 | 8 | OUT | 1000 |
| [L1_Measurements](#L1_Measurements) | 0x850035 | 8 | OUT | 100 |
| [L2_Measurements](#L2_Measurements) | 0x850036 | 8 | OUT | 100 |
| [L3_Measurements](#L3_Measurements) | 0x850037 | 8 | OUT | 100 |
| [N_Measurements](#N_Measurements) | 0x850038 | 8 | OUT | 100 |
| [ac_custom_Setpoints_Control](#ac_custom_Setpoints_Control) | 0x850039 | 8 | IN |  |
| [ac_custom_Setpoints_Applied](#ac_custom_Setpoints_Applied) | 0x85003a | 8 | OUT | 1000 |
| [ac_adjustments_Control](#ac_adjustments_Control) | 0x85003b | 8 | IN |  |
| [ac_adjustments_Applied](#ac_adjustments_Applied) | 0x85003c | 8 | OUT | 200 |
| [GN01_Mode_Set](#GN01_Mode_Set) | 0x850040 | 1 | IN |  |
| [GN01_Mode_Applied](#GN01_Mode_Applied) | 0x850041 | 1 | OUT | 1000 |
| [GN01_faults](#GN01_faults) | 0x850042 | 8 | OUT | 1000 |
| [GN01_warning](#GN01_warning) | 0x850043 | 8 | OUT | 1000 |
| [GN01_info](#GN01_info) | 0x850044 | 8 | OUT | 1000 |


<a id="DC_Ports_Setpoints"></a>
## DC_Ports_Setpoints { #DC_Ports_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850020 |
| **Length [Bytes]** | 6 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

### Description

The setpoints control the behaviour of the DC Port of the GN01. The GN01 operates this port in CVCC mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Positive_Current_Limit | 16 | Signed |
| Negative_Current_Limit | 16 | Signed |

### Payload description

#### Voltage { #DC_Ports_Setpoints-Voltage }

Control the target dc side voltage. This voltage will be maintained as long as the current required to do so is smaller than the current limits specified in this message

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Positive_Current_Limit { #DC_Ports_Setpoints-Positive_Current_Limit }

The maximum current that the GN01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### Negative_Current_Limit { #DC_Ports_Setpoints-Negative_Current_Limit }

The maximum current that the GN01 will sink into the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="DC_Port_Applied_Setpoints"></a>
## DC_Port_Applied_Setpoints { #DC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850021 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

The setpoints that are currently used by the GN01. This message allows to validate that the setpoints have been properly applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Positive_Current_Limit | 16 | Signed |
| Negative_Current_Limit | 16 | Signed |

### Payload description

#### Voltage { #DC_Port_Applied_Setpoints-Voltage }

The voltage target of the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Positive_Current_Limit { #DC_Port_Applied_Setpoints-Positive_Current_Limit }

The maximum current that the GN01 will source on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### Negative_Current_Limit { #DC_Port_Applied_Setpoints-Negative_Current_Limit }

The maximum amount of current that the GN01 will sink into the DC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="DC_Port_Droop_Setpoints"></a>
## DC_Port_Droop_Setpoints { #DC_Port_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850022 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints for applying Droop on the DC Port. Droop is needed for paralleling multiple GN01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |
| Reserved | 31 | Unsigned |

### Payload description

#### Positive_Current_Droop { #DC_Port_Droop_Setpoints-Positive_Current_Droop }

The droop resistance to apply for current flowing out of the DC port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Negative_Current_Droop { #DC_Port_Droop_Setpoints-Negative_Current_Droop }

The droop resistance to apply for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Enable { #DC_Port_Droop_Setpoints-Enable }

Enable DC Droop. If this feature is enabled the output voltage of the DC port varies with output current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #DC_Port_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 33 | 31 | Unsigned |  | 1 | 0 |  |  |


<a id="DC_Port_Applied_Droop_Setpoints"></a>
## DC_Port_Applied_Droop_Setpoints { #DC_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850023 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Droop setpoints that are applied by the GN01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Positive_Current_Droop | 16 | Unsigned |
| Negative_Current_Droop | 16 | Unsigned |
| Enable | 1 | Label set |

### Payload description

#### Positive_Current_Droop { #DC_Port_Applied_Droop_Setpoints-Positive_Current_Droop }

The droop resistance applied for current flowing out of the DC port (DC current is positive)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Negative_Current_Droop { #DC_Port_Applied_Droop_Setpoints-Negative_Current_Droop }

The droop resistance applied for current flowing in to the DC Port (DC current is negative)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | Ohm | 0.001 | 0 |  |  |

#### Enable { #DC_Port_Applied_Droop_Setpoints-Enable }

Show is DC Droop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |


<a id="DC_Port_Measurements"></a>
## DC_Port_Measurements { #DC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850024 |
| **Length [Bytes]** | 4 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements of the DC Bus

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Voltage | 16 | Unsigned |
| Current | 16 | Signed |

### Payload description

#### Voltage { #DC_Port_Measurements-Voltage }

Voltage on the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Current { #DC_Port_Measurements-Current }

Current through the DC Port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="AC_Port_Setpoints"></a>
## AC_Port_Setpoints { #AC_Port_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850030 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints to apply to the AC Port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| phase_config | 8 | Label set |
| grid_standard | 8 | Label set |
| Q | 16 | Signed |
| RMS_Phase_Current_Limit | 16 | Unsigned |

### Payload description

#### phase_config { #AC_Port_Setpoints-phase_config }

FOLLOW_N        (0): follow phase + neutral
SINGLE_PHASE_N  (1): 1-phase + neutral
THREE_PHASE     (2): 3-phase, no neutral (delta load)
THREE_PHASE_N   (3): 3-phase + neutral (star load)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| FOLLOW_N | 0 |
| SINGLE_PHASE_N | 1 |
| THREE_PHASE | 2 |
| THREE_PHASE_N | 3 |
| SPLIT_PHASE | 4 |

#### grid_standard { #AC_Port_Setpoints-grid_standard }

Grid voltage and frequency standard

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| FOLLOW | 0 |
| EU_230V_50HZ | 1 |
| US_277V_60HZ | 2 |
| US_120V_60HZ | 3 |
| CUSTOM | 7 |

#### Q { #AC_Port_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the GN01 to behave inductively, negative values cause the GN01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | VAR | 10 | 0 |  |  |

#### RMS_Phase_Current_Limit { #AC_Port_Setpoints-RMS_Phase_Current_Limit }

The maximum RMS current that the GN01 will supply at its AC terminals.
                This value limits the the magnitute of the AC current and applies
                symmetrically to both source and sink currents. This limit applies to
                the current carried by a single phase.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  |  |


<a id="AC_Port_Applied_Setpoints"></a>
## AC_Port_Applied_Setpoints { #AC_Port_Applied_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850031 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Setpoints that are currently being applied to the the AC Port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| phase_config | 8 | Label set |
| grid_standard | 8 | Label set |
| Q | 16 | Signed |
| RMS_Phase_Current_Limit | 16 | Unsigned |

### Payload description

#### phase_config { #AC_Port_Applied_Setpoints-phase_config }

SINGLE_PHASE_N  (1): 1-phase + neutral
THREE_PHASE     (2): 3-phase, no neutral (delta load)
THREE_PHASE_N   (3): 3-phase + neutral (star load)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| FOLLOW_N | 0 |
| SINGLE_PHASE_N | 1 |
| THREE_PHASE | 2 |
| THREE_PHASE_N | 3 |

#### grid_standard { #AC_Port_Applied_Setpoints-grid_standard }

Grid voltage and frequency standard

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| FOLLOW | 0 |
| EU_230V_50HZ | 1 |
| US_277V_60HZ | 2 |
| US_120V_60HZ | 3 |
| CUSTOM | 7 |

#### Q { #AC_Port_Applied_Setpoints-Q }

Reactive Power of the AC port. Positive values cause the GN01 to behave inductively, negative values cause the GN01 to behave capacitively

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | VAR | 10 | 0 |  |  |

#### RMS_Phase_Current_Limit { #AC_Port_Applied_Setpoints-RMS_Phase_Current_Limit }

The maximum RMS current that the GN01 will supply at its AC terminals.
                This value limits the the magnitute of the AC current and applies
                symmetrically to both source and sink currents. This limit applies to
                the current carried by a single phase.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Unsigned | A | 0.1 | 0 |  |  |


<a id="AC_Port_Droop_Setpoints"></a>
## AC_Port_Droop_Setpoints { #AC_Port_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850032 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Setpoints for applying Droop on the DC Port. Droop is needed for paralleling multiple AC01

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Freq_droop_nominal | 16 | Signed |
| Volt_droop_nominal | 16 | Signed |
| Virtual_Impedance | 16 | Signed |
| Enable | 1 | Label set |
| Disable_Harmonic_Compensation | 1 | Label set |
| Enable_Integral_Action | 1 | Label set |
| Reserved | 13 | Unsigned |

### Payload description

#### Freq_droop_nominal { #AC_Port_Droop_Setpoints-Freq_droop_nominal }

Sets the nominal droop slope for the Frequency in Hz/MW. By default
                   (i.e: after power cycle), this value is 40 Hz/MW

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | Hz/MW | 0.01 | 0 |  |  |

#### Volt_droop_nominal { #AC_Port_Droop_Setpoints-Volt_droop_nominal }

Sets the nominal droop slope for the Voltage in V/MVAr. By default
                   (i.e: after power cycle), this value is 630 V/MVAr

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V/MVAr | 0.1 | 0 |  |  |

#### Virtual_Impedance { #AC_Port_Droop_Setpoints-Virtual_Impedance }

Sets the inductive virtual impedance in microhenries (uH). By default
                   (i.e: after power cycle), this value is 8000 uH

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | uH | 1 | 0 |  |  |

#### Enable { #AC_Port_Droop_Setpoints-Enable }

Enable AC Droop. If this feature is enabled the output voltage of the AC port varies with output current.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Disable_Harmonic_Compensation { #AC_Port_Droop_Setpoints-Disable_Harmonic_Compensation }

Set this flag when harmonic compensation needs to be disabled (i.e, when
               the ADB is connected in parallel to the grid or to other diesel generators).
               Harmonic compensation is enabled by default on startup.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 49 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Enabled | 0 |
| Disabled | 1 |

#### Enable_Integral_Action { #AC_Port_Droop_Setpoints-Enable_Integral_Action }

Enable integral action for the Power loops. Enable this only if connected
               to the utility grid. If you go off-grid, this bit must be immediately cleared.
               This is disabled by default on startup.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 50 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #AC_Port_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 51 | 13 | Unsigned |  | 1 | 0 |  |  |


<a id="AC_Port_Applied_Droop_Setpoints"></a>
## AC_Port_Applied_Droop_Setpoints { #AC_Port_Applied_Droop_Setpoints }


| * | * |
|---|---|
| **Frame ID** | 0x850033 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Droop setpoints currently applied by the AC01.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Freq_droop_nominal | 16 | Signed |
| Volt_droop_nominal | 16 | Signed |
| Virtual_Impedance | 16 | Signed |
| Enable | 1 | Label set |
| Disable_Harmonic_Compensation | 1 | Label set |
| Enable_Integral_Action | 1 | Label set |
| Reserved | 13 | Unsigned |

### Payload description

#### Freq_droop_nominal { #AC_Port_Applied_Droop_Setpoints-Freq_droop_nominal }

The applied nominal frequency droop slope in Hz/MW.
The value represents the frequency variation per megawatt of active power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | Hz/MW | 0.01 | 0 |  |  |

#### Volt_droop_nominal { #AC_Port_Applied_Droop_Setpoints-Volt_droop_nominal }

The applied nominal voltage droop slope in V/MVAr.
The value represents the voltage variation per MVAr of reactive power.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | V/MVAr | 0.1 | 0 |  |  |

#### Virtual_Impedance { #AC_Port_Applied_Droop_Setpoints-Virtual_Impedance }

The applied inductive virtual impedance in microhenries (uH).

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | uH | 1 | 0 |  |  |

#### Enable { #AC_Port_Applied_Droop_Setpoints-Enable }

Indicates whether AC droop is enabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Disable_Harmonic_Compensation { #AC_Port_Applied_Droop_Setpoints-Disable_Harmonic_Compensation }

Indicates whether harmonic compensation is disabled.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 49 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Enabled | 0 |
| Disabled | 1 |

#### Enable_Integral_Action { #AC_Port_Applied_Droop_Setpoints-Enable_Integral_Action }

Indicates whether integral action for the power loops is enabled.
This should only be enabled when connected to the utility grid.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 50 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Disabled | 0 |
| Enabled | 1 |

#### Reserved { #AC_Port_Applied_Droop_Setpoints-Reserved }

This space is reserved. This region should contain only '0's.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 51 | 13 | Unsigned |  | 1 | 0 |  |  |


<a id="AC_Port_Measurements"></a>
## AC_Port_Measurements { #AC_Port_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850034 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Mesured values of the Grid connection

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency | 16 | Unsigned |
| Voltage | 16 | Unsigned |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency { #AC_Port_Measurements-Frequency }

Nominal frequency of the grid being formed by the GN01

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |

#### Voltage { #AC_Port_Measurements-Voltage }

Average RMS Line to Line voltage at the AC port

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Reserved { #AC_Port_Measurements-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="L1_Measurements"></a>
## L1_Measurements { #L1_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850035 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements for L1 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L1_Measurements-U }

RMS Voltage of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L1_Measurements-I }

RMS Current of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L1_Measurements-P }

Active power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L1_Measurements-Q }

Reactive power of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="L2_Measurements"></a>
## L2_Measurements { #L2_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850036 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements for L2 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L2_Measurements-U }

RMS Voltage of L1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L2_Measurements-I }

RMS Current of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L2_Measurements-P }

Active power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L2_Measurements-Q }

Reactive power of L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="L3_Measurements"></a>
## L3_Measurements { #L3_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850037 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements for L3 of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| U | 16 | Signed |
| I | 16 | Signed |
| P | 16 | Signed |
| Q | 16 | Signed |

### Payload description

#### U { #L3_Measurements-U }

RMS Voltage of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #L3_Measurements-I }

RMS Current of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |

#### P { #L3_Measurements-P }

Active power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 16 | Signed | W | 0.1 | 0 |  |  |

#### Q { #L3_Measurements-Q }

Reactive power of L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 48 | 16 | Signed | VAR | 0.1 | 0 |  |  |


<a id="N_Measurements"></a>
## N_Measurements { #N_Measurements }


| * | * |
|---|---|
| **Frame ID** | 0x850038 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 100 |
| **Direction** | OUT |

### Description

Measurements for Neutral of the AC port

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| reserved | 16 | Signed |
| I | 16 | Signed |

### Payload description

#### reserved { #N_Measurements-reserved }

reserved

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | V | 0.1 | 0 |  |  |

#### I { #N_Measurements-I }

RMS current via the neutral line.

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | A | 0.1 | 0 |  |  |


<a id="ac_custom_Setpoints_Control"></a>
## ac_custom_Setpoints_Control { #ac_custom_Setpoints_Control }


| * | * |
|---|---|
| **Frame ID** | 0x850039 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Custom Setpoints control

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency | 16 | Unsigned |
| Voltage | 16 | Unsigned |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency { #ac_custom_Setpoints_Control-Frequency }

Target Frequency

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |

#### Voltage { #ac_custom_Setpoints_Control-Voltage }

Target RMS voltage of the grid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Reserved { #ac_custom_Setpoints_Control-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="ac_custom_Setpoints_Applied"></a>
## ac_custom_Setpoints_Applied { #ac_custom_Setpoints_Applied }


| * | * |
|---|---|
| **Frame ID** | 0x85003a |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Custom Setpoints applied.

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency | 16 | Unsigned |
| Voltage | 16 | Unsigned |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency { #ac_custom_Setpoints_Applied-Frequency }

Target Frequency

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Unsigned | Hz | 0.01 | 0 |  |  |

#### Voltage { #ac_custom_Setpoints_Applied-Voltage }

Target RMS voltage of the grid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Unsigned | V | 0.1 | 0 |  |  |

#### Reserved { #ac_custom_Setpoints_Applied-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="ac_adjustments_Control"></a>
## ac_adjustments_Control { #ac_adjustments_Control }


| * | * |
|---|---|
| **Frame ID** | 0x85003b |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Ac adjustment control , usefull to sync with another grid

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency_shift | 16 | Signed |
| Voltage_shift | 16 | Signed |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency_shift { #ac_adjustments_Control-Frequency_shift }

Shift target Frequency by x percent (±2Hz)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | % | 0.001 | 0 |  |  |

#### Voltage_shift { #ac_adjustments_Control-Voltage_shift }

Shift target RMS voltage by x percent (±20V)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | % | 0.01 | 0 |  |  |

#### Reserved { #ac_adjustments_Control-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="ac_adjustments_Applied"></a>
## ac_adjustments_Applied { #ac_adjustments_Applied }


| * | * |
|---|---|
| **Frame ID** | 0x85003c |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 200 |
| **Direction** | OUT |

### Description

Shift target Frequency by x percent

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Frequency_shift | 16 | Signed |
| Voltage_shift | 16 | Signed |
| Reserved | 32 | Unsigned |

### Payload description

#### Frequency_shift { #ac_adjustments_Applied-Frequency_shift }

Target Frequency

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 16 | Signed | % | 0.001 | 0 |  |  |

#### Voltage_shift { #ac_adjustments_Applied-Voltage_shift }

Shift target RMS voltage by x percent

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 16 | Signed | % | 0.01 | 0 |  |  |

#### Reserved { #ac_adjustments_Applied-Reserved }

This space is reserved. This region contains only '0's

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 32 | Unsigned |  | 1 | 0 |  |  |


<a id="GN01_Mode_Set"></a>
## GN01_Mode_Set { #GN01_Mode_Set }


| * | * |
|---|---|
| **Frame ID** | 0x850040 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** |  |
| **Direction** | IN |

### Description

Configure GN01 operating mode

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #GN01_Mode_Set-mode }

Requested operating mode

            DC_Controlled (0): DC side voltage controlled to setpoint, requires AC side input present
            AC_Controlled (1): AC side voltage controlled, will generate AC if not present
            Bleeding (2): Discharge internal capacitors/remaining charge

            changing mode can only be done when the power converter is not "Enable"

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| DC_Controlled | 0 |
| AC_Controlled | 1 |
| Bleeding | 2 |


<a id="GN01_Mode_Applied"></a>
## GN01_Mode_Applied { #GN01_Mode_Applied }


| * | * |
|---|---|
| **Frame ID** | 0x850041 |
| **Length [Bytes]** | 1 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

GN01 actual operating mode (readback)

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| mode | 8 | Label set |

### Payload description

#### mode { #GN01_Mode_Applied-mode }

Currently applied operating mode

                changing mode can only be done when the power converter is not "Enable"

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| DC_Controlled | 0 |
| AC_Controlled | 1 |
| Bleeding | 2 |


<a id="GN01_faults"></a>
## GN01_faults { #GN01_faults }


| * | * |
|---|---|
| **Frame ID** | 0x850042 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

GN01 Critical and error conditions

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| CABLE_1_2_L1 | 1 | Label set |
| CABLE_1_3_L1 | 1 | Label set |
| CABLE_1_2_L2 | 1 | Label set |
| CABLE_1_3_L2 | 1 | Label set |
| CABLE_1_2_L3 | 1 | Label set |
| CABLE_1_3_L3 | 1 | Label set |
| CABLE_4_5_L1 | 1 | Label set |
| CABLE_7_L1_L2 | 1 | Label set |
| CABLE_4_5_L2 | 1 | Label set |
| CABLE_7_L2_L3 | 1 | Label set |
| CABLE_4_5_L3 | 1 | Label set |
| CABLE_1_4_L1 | 1 | Label set |
| CABLE_1_4_L2 | 1 | Label set |
| CABLE_1_4_L3 | 1 | Label set |
| CABLE_2_3_DC | 1 | Label set |
| CABLE_3_5_DC | 1 | Label set |
| MODULE_1_RUNNING | 1 | Label set |
| MODULE_2_RUNNING | 1 | Label set |
| MODULE_3_RUNNING | 1 | Label set |
| MODULE_4_RUNNING | 1 | Label set |
| MODULE_5_RUNNING | 1 | Label set |
| MODULE_7_RUNNING | 1 | Label set |
| reserved_1 | 1 | Label set |
| reserved_2 | 1 | Label set |
| reserved_3 | 1 | Label set |
| reserved_4 | 1 | Label set |
| PRECHARGE_FAILED | 1 | Label set |
| Main_Contactors_failed | 1 | Label set |
| FILTER_NOT_RUNNING | 1 | Label set |
| RECTIFIER_3P_NOT_RUNNING | 1 | Label set |
| AFE_NOT_OFF | 1 | Label set |
| FILTER_STOP_RUNNING | 1 | Label set |
| RECTIFIER_3P_STOP_RUNNING | 1 | Label set |
| AFE_PWM_NOT_RUNNING | 1 | Label set |
| AFE_PWM_STOP_RUNNING | 1 | Label set |
| BLEEDING_FAILED | 1 | Label set |
| FILTER_NOT_OFF | 1 | Label set |
| INVERTER_3P_NOT_RUNNING | 1 | Label set |
| INVERTER_3P_STOP_RUNNING | 1 | Label set |
| NEUTRAL_NOT_RUNNING | 1 | Label set |
| NEUTRAL_STOP_RUNNING | 1 | Label set |

### Payload description

#### CABLE_1_2_L1 { #GN01_faults-CABLE_1_2_L1 }

Critical: Phase mismatch between DMF1(1).L1 and BP25(2).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L1 { #GN01_faults-CABLE_1_3_L1 }

Critical: Phase mismatch between DMF1(1).L1 and BP25(3).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L2 { #GN01_faults-CABLE_1_2_L2 }

Critical: Phase mismatch between DMF1(1).L2 and BP25(2).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L2 { #GN01_faults-CABLE_1_3_L2 }

Critical: Phase mismatch between DMF1(1).L2 and BP25(3).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_2_L3 { #GN01_faults-CABLE_1_2_L3 }

Critical: Phase mismatch between DMF1(1).L3 and BP25(2).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_3_L3 { #GN01_faults-CABLE_1_3_L3 }

Critical: Phase mismatch between DMF1(1).L3 and BP25(3).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L1 { #GN01_faults-CABLE_4_5_L1 }

Critical: Phase mismatch between DMF1(4).L1 and BP25(5).U

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 6 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_7_L1_L2 { #GN01_faults-CABLE_7_L1_L2 }

Critical: Phase mismatch between BP25(7).U and BP25(7).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 7 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L2 { #GN01_faults-CABLE_4_5_L2 }

Critical: Phase mismatch between DMF1(4).L2 and BP25(5).V

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 8 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_7_L2_L3 { #GN01_faults-CABLE_7_L2_L3 }

Critical: Phase mismatch between BP25(7).V and BP25(7).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 9 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_4_5_L3 { #GN01_faults-CABLE_4_5_L3 }

Critical: Phase mismatch between DMF1(4).L3 and BP25(5).W

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 10 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L1 { #GN01_faults-CABLE_1_4_L1 }

Critical: Grid L1 mismatch between DMF1(1).IN and DMF1(4).IN

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 12 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L2 { #GN01_faults-CABLE_1_4_L2 }

Critical: Phase mismatch between DMF1(1).L2 and DMF1(4).L2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 13 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_1_4_L3 { #GN01_faults-CABLE_1_4_L3 }

Critical: Phase mismatch between DMF1(1).L3 and DMF1(4).L3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 14 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_2_3_DC { #GN01_faults-CABLE_2_3_DC }

Critical: DC mismatch between BP25(2) and BP25(3)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### CABLE_3_5_DC { #GN01_faults-CABLE_3_5_DC }

Critical: DC mismatch between BP25(3) and BP25(5)

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Critical | 1 |

#### MODULE_1_RUNNING { #GN01_faults-MODULE_1_RUNNING }

Error: Module 1 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_2_RUNNING { #GN01_faults-MODULE_2_RUNNING }

Error: Module 2 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_3_RUNNING { #GN01_faults-MODULE_3_RUNNING }

Error: Module 3 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_4_RUNNING { #GN01_faults-MODULE_4_RUNNING }

Error: Module 4 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 21 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_5_RUNNING { #GN01_faults-MODULE_5_RUNNING }

Error: Module 5 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 22 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### MODULE_7_RUNNING { #GN01_faults-MODULE_7_RUNNING }

Error: Module 7 is running, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 23 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_1 { #GN01_faults-reserved_1 }

reserved_1

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 24 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_2 { #GN01_faults-reserved_2 }

reserved_2

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 25 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_3 { #GN01_faults-reserved_3 }

reserved_3

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 26 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### reserved_4 { #GN01_faults-reserved_4 }

reserved_4

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 27 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### PRECHARGE_FAILED { #GN01_faults-PRECHARGE_FAILED }

Error: Precharge failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 28 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### Main_Contactors_failed { #GN01_faults-Main_Contactors_failed }

Error: Main contactors did not closed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 29 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_RUNNING { #GN01_faults-FILTER_NOT_RUNNING }

Error: Filter is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 30 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_NOT_RUNNING { #GN01_faults-RECTIFIER_3P_NOT_RUNNING }

Error: Three-phase rectifier is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 31 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_NOT_OFF { #GN01_faults-AFE_NOT_OFF }

Error: AFE is not off, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 32 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_STOP_RUNNING { #GN01_faults-FILTER_STOP_RUNNING }

Error: Filter stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 34 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### RECTIFIER_3P_STOP_RUNNING { #GN01_faults-RECTIFIER_3P_STOP_RUNNING }

Error: Rectifier stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 35 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_NOT_RUNNING { #GN01_faults-AFE_PWM_NOT_RUNNING }

Error: BLEEDING is not running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 36 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### AFE_PWM_STOP_RUNNING { #GN01_faults-AFE_PWM_STOP_RUNNING }

Error: Bleeding stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 37 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### BLEEDING_FAILED { #GN01_faults-BLEEDING_FAILED }

Error: Bleeding process failed

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 38 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### FILTER_NOT_OFF { #GN01_faults-FILTER_NOT_OFF }

Error: Filter is not off, but it should be off

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 39 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### INVERTER_3P_NOT_RUNNING { #GN01_faults-INVERTER_3P_NOT_RUNNING }

Error: Three-phase inverter is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 40 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### INVERTER_3P_STOP_RUNNING { #GN01_faults-INVERTER_3P_STOP_RUNNING }

Error: Three-phase inverter stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 41 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### NEUTRAL_NOT_RUNNING { #GN01_faults-NEUTRAL_NOT_RUNNING }

Error: neutral is not running, but it should be active

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 42 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |

#### NEUTRAL_STOP_RUNNING { #GN01_faults-NEUTRAL_STOP_RUNNING }

Error: neutral stop running

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 43 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Error | 1 |


<a id="GN01_warning"></a>
## GN01_warning { #GN01_warning }


| * | * |
|---|---|
| **Frame ID** | 0x850043 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

GN01 warning flags, it need to be cleared to "Enable" the power converter

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| grid_not_supported | 1 | Label set |
| grid_not_existing | 1 | Label set |
| grid_selection_wrong | 1 | Label set |
| reserved_3 | 1 | Label set |
| V_SET_DC_BELOW_AC | 1 | Label set |
| V_DC_BELOW_AC | 1 | Label set |
| AFE_DROOP_NOT_ENABLE | 1 | Label set |
| MODE_NOT_SUPPORTED | 1 | Label set |
| V_A_LOW | 1 | Label set |
| V_A_HIGH | 1 | Label set |
| V_B_LOW | 1 | Label set |
| V_B_HIGH | 1 | Label set |

### Payload description

#### grid_not_supported { #GN01_warning-grid_not_supported }

Warning: Grid is not supported

            3-Phase 230V (line-to-neutral) / 400V (line-to-line), 50Hz
            3-Phase 277V (line-to-neutral) / 480V (line-to-line), 60Hz
            3-Phase 120V (line-to-neutral) / 208V (line-to-line), 60Hz

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### grid_not_existing { #GN01_warning-grid_not_existing }

Warning: The converter is not connected to existing grid

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### grid_selection_wrong { #GN01_warning-grid_selection_wrong }

Warning: grid selection is wrong

              converter see an existing grid and the selected grid mode is different

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### reserved_3 { #GN01_warning-reserved_3 }

reserved

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_SET_DC_BELOW_AC { #GN01_warning-V_SET_DC_BELOW_AC }

Warning: DC voltage setpoint is lower than the measured AC voltage

                It needs to follow this equation::
                      Vset DC &gt; VAC rms * sqrt(2) * 2 + 20

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_DC_BELOW_AC { #GN01_warning-V_DC_BELOW_AC }

Warning: DC voltage measured is too low to generate AC voltage

                It needs to follow this equation::
                      Vset DC &gt; VAC rms * sqrt(2) * 2 + 20

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### AFE_DROOP_NOT_ENABLE { #GN01_warning-AFE_DROOP_NOT_ENABLE }

Warning: AFE droop control is disabled but expected to be enabled

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 15 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### MODE_NOT_SUPPORTED { #GN01_warning-MODE_NOT_SUPPORTED }

Warning: The selected operating mode is not supported

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 16 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_LOW { #GN01_warning-V_A_LOW }

Warning: Port A voltage is below the minimum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 17 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_A_HIGH { #GN01_warning-V_A_HIGH }

Warning: Port A voltage exceeds the maximum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 18 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_B_LOW { #GN01_warning-V_B_LOW }

Warning: Port A voltage is below the minimum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 19 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |

#### V_B_HIGH { #GN01_warning-V_B_HIGH }

Warning: Port A voltage exceeds the maximum operating threshold

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 20 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Warning | 1 |


<a id="GN01_info"></a>
## GN01_info { #GN01_info }


| * | * |
|---|---|
| **Frame ID** | 0x850044 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | OUT |

### Description

Info: Informational status and operating conditions

### Payload

| Signal | Length (bits) | Type |
|--------|---------------|------|
| BLEEDING_DONE | 1 | Label set |
| CURRENT_LIMIT | 1 | Label set |
| CURRENT_LIMITED_BY_POWER | 1 | Label set |
| VB_LIMITED_BY_VA | 1 | Label set |
| PHASE_SWAPPED | 1 | Label set |

### Payload description

#### BLEEDING_DONE { #GN01_info-BLEEDING_DONE }

Info: Bleeding process completed successfully

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 1 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CURRENT_LIMIT { #GN01_info-CURRENT_LIMIT }

Info: Current limit has been reached

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 2 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### CURRENT_LIMITED_BY_POWER { #GN01_info-CURRENT_LIMITED_BY_POWER }

Info: Output current is limited because the maximum power is reached

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 3 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### VB_LIMITED_BY_VA { #GN01_info-VB_LIMITED_BY_VA }

Info: Output voltage VB is limited because input voltage VA is insufficient

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 4 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |

#### PHASE_SWAPPED { #GN01_info-PHASE_SWAPPED }

Info: input phase are swapped

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 5 | 1 | Label set |  | 1 | 0 |  |  |

| Label name | Value |
|------------|-------|
| Clear | 0 |
| Info | 1 |
