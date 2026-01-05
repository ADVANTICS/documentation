# Controllers IOs on CAN

!!! note
    Only available from version 4.x of the controller system


## Inputs

Digital Inputs can be configured such that their current value is reported over CAN, in message: 

- For ADM-CS-SECC: [ADM_CS_SECC_Inputs](../charger-can-interfaces/can_v3.md#ADM_CS_SECC_Inputs)
- For ADM-CS-SPCC: [ADM_CS_SPCC_Inputs](../charger-can-interfaces/can_v3.md#ADM_CS_SPCC_Inputs)

## Outputs

Digital Outputs can be configured to be controller via the can bus message:

- For ADM-CS-SECC: [ADM_CS_SECC_Outputs](../charger-can-interfaces/can_v3.md#ADM_CS_SECC_Outputs)

- They can be controlled through generic CAN interface (≥ v2.2)
- They also need to be enabled in config file:
    ```
    [hardware]
    dig_out1 = CAN_Controlled
    dig_out2 = CAN_Controlled
    dig_out3 = CAN_Controlled
    dig_out4 = CAN_Controlled
    ```
