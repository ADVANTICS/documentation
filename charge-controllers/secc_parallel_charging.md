> [!UPDATE] {docsify-updated}
# Parallel charging

> [!NOTE]
> Only available from version 4.x of the controller system

- Each pistol has its own charger interface instance
- CAN ID "multiplexing" done by offset using pistol index (offset added on last byte of the extended CAN IDs)
- If you want the previous behaviour of non-parallel charging, just set the `Start_Charge_Authorisation` sequence flag to 0 on the other charger interfaces when a charge starts on one (and reenable when done)
- Overall performance of the controllers have yet to be evaluated when doing parallel charging
- Other related config entries to allow declaring a digital input as normal stop for a particular pistol:
    - `Stop` remains a global normal stop. It will stop all pistols currently charging!
    - `CCS_DC_Stop`, `CCS_DC_Stop` and `CHAdeMO_Stop` are pistol specific normal stop inputs
    - Default values on `ADM-CO-CUI1`:

        ```
        [hardware]
        switch1 = Stop
        switch2 = CCS_DC_Stop
        switch3 = CHAdeMO_Stop
        ```

    - Default values on `ADM-CS-SECC`:

        ```
        [hardware]
        dig_in2 = CCS_DC_Stop
        dig_in3 = CCS_AC_Stop
        dig_in4 = CHAdeMO_Stop
        ```
