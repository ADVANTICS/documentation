#!/bin/bash

python3 ../../../../Manuals/databases/KCDDoc/main.py -d ../../../../Manuals/databases/db/KCD_Definition.xsd --direction_mask=0x010 ../../../../Manuals/databases/db/Advantics_Generic_PEV_protocol_v1.kcd can.md

sed -i 's/<<No BMS mode>>/[No BMS mode](charge-controllers\/evcc_configuration\/no_bms.md)/' can.md
sed -i 's/<<CAN sensor>>/[CAN sensor](charge-controllers\/evcc_configuration\/can_sensor.md)/' can.md
