> [!UPDATE] {docsify-updated}
# Controllers IOs on CAN

> [!NOTE]
> Only available from version 4.x of the controller system

## Inputs

Digital Inputs can be configured such that their current value is reported over CAN, in message [ADM_CS_SECC_Inputs](secc_generic/can#adm_cs_secc_inputs).

## Outputs

Digital Outputs can be configured to be controller via the can bus message [ADM_CS_SECC_Outputs](secc_generic/can#adm_cs_secc_outputs).

- Only for controllers having general purposes IO: `ADM-CS-SECC`
- They can be controlled through generic CAN interface (≥ v2.2)
    - See message [0x60013] ADM_CS_SECC_Outputs
- They also need to be enabled in config file:
    ```
    [hardware]
    dig_out1 = CAN_Controlled
    dig_out2 = CAN_Controlled
    dig_out3 = CAN_Controlled
    dig_out4 = CAN_Controlled
    ```
