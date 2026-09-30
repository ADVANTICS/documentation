"""Choice values the configuration documentation may show.

Every choice-type entry in `controller-config` lists all its valid values, and some of those are
retired or not meant for customers. The generators show a value only if it is listed here for
that entry; an entry with no key, or an empty list, shows its default only.

Keys are `section.entry`, with shell-style wildcards, optionally prefixed by the controllers they
apply to (`spcc,secc/hardware.dig_in*`). `'*'` in a list means every value, and an entry's default
is always shown. `...` marks a key nobody has reviewed yet: `--check` fails while any is left.
"""

PUBLIC_CHOICES: dict[str, list] = {
    'applications.log_level': ['*'],
    'ccs.preferred_control_mode': ['*'],
    'evcc,mevc/hardware.dig_in*': ['*'],
    'secc,spcc/hardware.dig_in*': [
        'Not_Connected',
        'CHAdeMO_Start',
        'Stop',
        'CCS_DC_Stop',
        'CCS_AC_Stop',
        'CHAdeMO_Stop',
        'Monitor',
        # No handler in evse-controller: IMD_24V, DC_Output_Contactor_Feedback_24V,
        # Aux_Ready_24V, Aux_Warning_24V, Emergency_Stop, Sleep.
    ],
    'secc,spcc/hardware.dig_out*': [
        'Not_Connected',
        'CAN_Controlled',
        'Contactor_Enable',
        # Plugged_In: nothing in evse-controller drives it.
    ],
    'evcc,mevc/hardware.dig_out*': [
        'Not_Connected',
        'Plugged_In',
        'CAN_Controlled',
        # Contactor_Enable: nothing in pev-controller drives it.
    ],
    'secc,spcc/hardware.led*': ['*'],
    'evcc,mevc/hardware.led*': [
        'Not_Connected',
        'Plugged_In',
        'CAN_Controlled',
        # Contactor_Enable: nothing in pev-controller drives it.
    ],
    'hardware.version': [
        'din_controller_v2020-1',
        'din_controller_v2021-1',
        # mobile_charger_controller_v2018-1 is the ADM-CO-CUI1, pev_controller_v2018-1 a vehicle
        # controller the charger board IOs reject.
    ],
    'ocpp.protocol_order': ['*'],
    'pistol:*.charger_type': [
        'Advantics_Generic_DC_v1',
        'Advantics_Generic_DC_v2',
        'Advantics_Generic_DC_v3',
        'Advantics_Generic_AC_v2',
        'Advantics_ADS_PC_UPUD',
        'Advantics_ADS_PC_BPUD',
        'Advantics_ADM_PC_BP25_BoostBuck',
        'PRE_Charger',
        'Maxwell_MXR',
        # Not in the evse-controller charger factory, so rejected at start-up:
        # Advantics_ADS_PC_BPBD, Advantics_ADS_PC_AC01_DC01.
    ],
    'pistol:*.insulation_monitor_address': ['*'],
    'pistol:*.insulation_monitor_baudrate': ['*'],
    'pistol:*.insulation_monitor_parity': ['*'],
    'pistol:*.insulation_monitor_stopbits': ['*'],
    'pistol:*.insulation_monitor_type': ['*'],
    'pistol:*.io_channel': ['*'],
    'secc/pistols.enabled': ['*'],
    'spcc/pistols.enabled': ['*'],
    'temperature_action:cable_stop_threshold.mode': ['*'],
    'temperature_action:cable_stop_threshold.target': ['*'],
    'temperature_action:monitor.mode': ['*'],
    'temperature_action:monitor.target': ['*'],
    'temperature_function:cable.actions': ['*'],
    # Fixed per controller: a charger is a TLS server, a vehicle a client.
    'tls.side': [],
    'tls:*.max_version': ['*'],
    'tls:*.min_version': ['*'],
    'vehicle.can_if': [
        'can0',
        # vcan0 is a virtual interface for simulation.
    ],
    'vehicle.can_sensor_if': ['*'],
    'vehicle.type': [
        'Advantics_Generic_v1',
        'Advantics_Generic_v2',
        # Advantics_Internal is an internal test BMS; EDN_FEX4432A0 and Emus_G1 are
        # customer-specific integrations; VG11BMS has no implementation.
    ],
    'vehicle.use_can_sensor': ['*'],
}
