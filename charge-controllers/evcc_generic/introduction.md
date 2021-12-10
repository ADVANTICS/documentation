> [!UPDATE] {docsify-updated}
# Introduction

Advantics PEV controllers use a standard ISO-11898 CAN bus for control and status communications
with power modules. While controllers can communicate directly with some specific BMS, it is also
possible to have controllers operate with unsupported BMS.

One way to allow this interoperability is to use the generic PEV CAN interface presented here.
Sequencing through the charging steps are explained in this manual. As well as the specific details
about the different CAN messages and their payload that are part of the communication protocol
between controllers and BMS.

> [!TIP]
> For the purpose of evaluating quickly our solution in a development/prototyping environment,
> their exist a special operating mode in which, under specific conditions, no user code is needed to
> reach a functional DC charge. See [No code mode](charge-controllers/evcc_no_code_mode.md).

## Scope of this manual

This manual focuses mainly on the protocol of the generic PEV CAN interface. It is of interest to people implementing the communication with BMS side.

As it takes place within the whole EV charging topic, important details about other part of the
charging chain will come along side. The charger side of thing as well as the charging communication
protocol themselves are out-of-scope. Nevertheless, details about them are given such that the
reader can contextualise actions happening on the side of the generic PEV CAN interface.

Each message is described together with its payload data. The payload data description, includes the
units of the different variables, the scaling factor and offset, as well as maximum and minimum
limits, where applicable. Some messages require certain periodicity while others can be sent in an on-demand basis.
