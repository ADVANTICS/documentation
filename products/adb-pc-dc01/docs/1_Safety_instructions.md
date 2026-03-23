# Safety instructions

!!! warning 
    Please note that users must read the safety instructions before using this equipment. The most important general safety precautions are summarized     in this preface. Improper connection or operation could result in death, serious injury, fire, or equipment damage. Always read and understand the     full manual before installation and use, and follow all recommended procedures. The ADM-PC-BI25 contains high-voltage capacitors that store energy     and discharge slowly. Even when unplugged, lethal voltages may still be  present. The passive self-bleeding of the converter takes approximately       20 minutes, so always allow sufficient time before handling. Users should always treat the device as energized unless verified otherwise with a        volt meter.

## Qualified personnel only

The instrument may only be operated by personnel capable of recognizing contact hazards and implementing appropriate safety precautions. 

Contact hazards are present anywhere where voltages of greater than 50 V exist. This is very important when the open-ended output signal cable is used or any OEM/PCB version of equipment is operated, tested or else used.

## Avoid working alone

Do not perform measurements involving contact hazards alone; another person must always be present.

## Do Not Operate During Faults

Do not use the equipment in case of sparking, short circuits or other discharge events with attached batteries, module or signal cable.

## Prohibit Use in Damp Conditions

Operation under damp or wet ambient conditions is strictly prohibited.

## Maintain Cable and Lead Integrity

Power and data cables must be kept in flawless condition, with no damage to insulation, plugs, or connectors.

## Remove Unsafe Equipment from Service

If safe operation of the instrument can no longer be assumed, it must be removed from the factory, laboratory and secured against unintentional use. Safe operation can be no longer assumed if: 

- The module, power cables or any cables show visible damage  
- The module no longer functions  
- The module shows very dirty conditions because of dust etc.   
- After lengthy periods of storage under unfavorable conditions  
- After exposure to unusual transport stresses.

## Power disconnection before handling

Maintenance, repair, or internal balancing may only be performed by trained personnel familiar with the dangers involved. As long as the module is connected, conducting parts may be exposed to the voltage. The instrument must be disconnected from all external power sources before performing maintenance and repair work. 

Under the worst conditions (loss of supply voltage), a minimum waiting period of 36 minutes (2147 seconds) must be practiced after the module has been disconnected to allow internal capacitors to discharge to less than 0.5mJ. This duration takes system and component tolerances into account. Even if this time has passed, a voltage absence test is strongly recommended before handling the unit.

# Safety symbols

ADB-PC-DC01 module is equipped with relevant safety labels on the front panel. The explanation of each symbol is provided  below.

### ISO 7010-W001: 2011-05

The ISO 7010-W001: 2011-05 symbol indicates that caution is necessary when operating the device and the current situation needs operator awareness and action to avoid undesirable consequences. 

{{ figure('../assets/General warning.png', 'General safety warning') }}

### ISO 7010-M002: 2011-05

The ISO 7010-M002: 2011-05 symbol signifies that the instruction manual/booklet must be read before operating the module.

{{ figure('../assets/Refer to instruction manualbooklet.png', 'Refer to instruction manual/booklet') }}

### IEC 60417-6042: 2010-11

The IEC 60417-6042: 2010-11 symbol indicates that the equipment has a risk of electric shock.

{{ figure('../assets/Caution, risk of electric shock.png', 'Caution, risk of electric shock') }}

### IEC 60417-5416: 2015-04

The IEC 60417-5416: 2015-04 symbol indicates the required capacitor self-discharge time at fault conditions. 

The discharge time is defined as the duration required for the module to self-discharge its capacitors to 0.5 mJ, starting from the maximum allowable Port A voltage of 950 V, including the component tolerances.

For this unit, the capacitors require 23 minutes to self-discharge at Port A and 36 minutes at Port B. Even though this time has passed, a voltage absence test is strongly recommended before handling the unit.

{{ figure('../assets/Remaining time display; processing.png', 'Capacitor discharge time') }}

### IEC 60417-5041:2002-10

The IEC 60417-5041:2002-10 indicates that the module can be hot and should not be touched without taking care. The cooling surfaces can reach up to the liquid temperature.

{{ figure('../assets/Caution, hot surface.png', 'Caution, hot surface') }}
