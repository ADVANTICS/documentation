# Charger interfaces

The charger interfaces page in the documentation provides information about the available power module interfaces that can be selected via the charge controller configuration. These interfaces facilitate communication and control between the charge controller and the power modules efficiently and seamlessly.

By utilizing these pre-defined charger interfaces, the customer can avoid the need for developing a custom translation stage between the power module CAN bus interface and the charge controllers' generic interface.

These charger interfaces are available for a selected number of charger architectures composed of ADVANTICS power modules as well as third-party power modules.

The ADVANTICS charge controller supports parallel stacking of power modules, enabling the creation of higher power chargers by combining their capabilities. Refer to the specific charger interface section for more details.

All charger interfaces should be configured in the section corresponding to the enabled pistol being configured (example [pistol:CCS DC]).

## ADVANTICS AC/DC charger Interface

ADVANTICS charge controller offers a complete AC/DC charger interface.

The BPUD interface is designed for the [3-phase unidirectional charger](../power-modules/ADM-PC-BP25/application_examples.md#3-phase-unidirectional-charger). It incorporates the ADM-PC-LF45 (filter stage and inrush limiter), the ADM-PC-BP25 as a Power Factor Correction (PFC) stage, and ADM-PC-LL25 (unidirectional isolated DC/DC converter).

![BPUD charger](../power-modules/ADM-PC-BP25/images/app_3phase_charger.svg ':size=200%')
<figcaption style="text-align: center">BPUD charger</figcaption>

### power modules configuration

Configure the power modules stack position numbers to be the same for each stack.
You can do that by Using ADVANTICS engineering toolkit
ETKA or by manually sending the CAN messages to configure the stack position to the AFE.

### Controller configuration

The config entries available for this charger interface are the following:

```
charger_type: The charger type should be "Advantics_ADS_PC_BPUD".
```

```
stack_pos: the stack position number configured for all 3 power modules. In case multiple BPUD chargers are stacked in parallel, provide the stack position number of all the stacks comma or space separated.
```

## ADVANTICS BIDIRECTIONAL BOOST-BUCK Interface

Step-up, followed by a Step-down DC/DC. Removes the limitation of a simple Bidirectional Buck, as now the
voltage regions can overlap. The first stage (no matter from which direction) is always a Step up. Then this
voltage is stepped down to provide the Voltage and Current regulation.

This interface can be also used to control only one AFE as a Buck.


> Insolation resistance value measured via your insulation monitor should be provided to the charge controller using the [CAN bus generic interface](charge-controllers/secc_generic/can.md) signal [Power_Modules_Status](charge-controllers/secc_generic/can.md#Power_Modules_Status).[Insulation_Resistance](charge-controllers/secc_generic/can.md#Insulation_Resistance)


![BOOST-BUCK charger](ADM-CS-SECC/images/ADM-CS-SECC_boost_buck.svg ':size=200%')
<figcaption style="text-align: center">BOOST-BUCK charger</figcaption>


### AFEs configuration

> This interface can control Boost-Buck or Buck only stacks of ADM-PC-BP25 power modules.

Configure the boost and buck stack position numbers to be consecutive such as the boost stack
position number = buck stack position number + 1.
You can do that by Using ADVANTICS engineering toolkit
ETKA or by manually sending the CAN messages to configure the stack position to the AFE.

### Controller configuration

The config entries available for this charger interface are the following:

```
charger_type: The charger type should be "Advantics_ADM_PC_BP25_BoostBuck".
```
```
boost_buck_mode: This boolean parameter can be used to select between Boost-Buck mode or Buck-only mode.
```
```
boost_buck_max_current: This float parameter can be used to set the maximum current for Boost-Buck mode. The default value is 110 Amps.
```

```
precharge_min_current: Specifies the minimum current required during precharge to ensure successful voltage rise and prevent precharge failures caused by low current requests from the vehicle. The default is 3 Amps
```

```
stack_pos: stack position of the Buck. The controller assumes that the stack position of the Boost will be "buck stack position number" + 1.
```

### Parallel Stacking

The charge controller can be configured to control a set of Boost-Buck chargers stacked in parallel. The stack position number of the Boost-Buck sets can be provided to the controller using the "stack_pos" config entry comma or space separated.

If the system is configured in Buck-only mode (```boost_buck_mode``` is set to ```false```), ```stack_pos``` config entry should be the stack position of the Bucks comma or space separated.

The power modules stack with the stack position number ```0``` should correspond to the stack connected directly to the output of the charger.

## MAXWELL MXR MXR100040

This interface applies to Maxwell power MXR100040 modules from MXR Series.

> If you need to modify the CAN bus bitrate, you can refer to [CAN bus Bitrate](charge-controllers/sys3_user/developing.md#can-bus-bitrate)

> Insolation resistance value measured via your insulation monitor should be provided to the charge controller using the [CAN bus generic interface](charge-controllers/secc_generic/can.md) signal [Power_Modules_Status](charge-controllers/secc_generic/can.md#Power_Modules_Status).[Insulation_Resistance](charge-controllers/secc_generic/can.md#Insulation_Resistance)

### Controller configuration

The config entries available for this charger interface are the following:
```
charger_type: The charger type should be "Maxwell_MXR".
```

The power module frame identifier is composed of the following parameters:

![MXR Frame Identifier](ADM-CS-SECC/images/MXR_frame_id.svg ':size=200%')
<figcaption style="text-align: center">MXR Frame Identifier</figcaption>

```
protocol: corresponds to PROTNO.
```
```
ptp: corresonds to PTP.
```
```
dest_address: corresponds to the power module DSTADDR. It can be a list of addresses if multiple MXR units are stacked in parallel.
```
```
src_address: corresponds to SRCADDR.
```
```
group: corresponds to Group.
```


The following default parameters will be applied. If your MXR power module
has a different Frame Identifier configuration, you need to add and modify these entries:
```
protocol = 0x60
ptp = 1
dest_address = 0x00
src_address = 0xF0
group = 0
```