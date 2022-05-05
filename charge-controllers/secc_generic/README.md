> [!UPDATE] {docsify-updated}
# Generic SECC CAN interface

# Introduction

The Advantics EVSE controllers (DIN rail mount version and generic development platform version)
use a standard ISO-11898 CAN bus for control and status communications with power modules. While
controllers can communicate directly with Advantics own power converters, it is also possible to
have controllers operate with power converters from other companies.

One way to allow this interoperability is to use the generic EVSE CAN interface presented here.
Sequencing through the charging steps are explained in this manual. As well as the specific details
about the different CAN messages and their payload that are part of the communication protocol
between controllers and power modules.

Since version 2 of this interface, some of its messages are also used when using Advantics own power
modules. This allow customer implementations to be aware of and act on the charging sequence. This
particular usage will also be described in this manual.

# Scope of this manual

This manual focuses mainly on the protocol of the generic EVSE CAN interface. It is of interest to
people implementing the power modules side, or the client or backend interaction side.

As it takes place within the whole EV charging topic, important details about other part of the
charging chain will come along side. The vehicle side of thing as well as the charging communication
protocol themselves are out-of-scope. Nevertheless, details about them are given such that the
reader can contextualise actions happening on the side of the generic EVSE CAN interface.

Each message is described together with its payload data. The payload data description, includes the
units of the different variables, the scaling factor and offset, as well as maximum and minimum
limits, where applicable. Some messages require certain periodicity while others can be sent in an
on-demand basis.

# Outline
1. [Introduction](#introduction)
1. [Overview](charge-controllers/secc_generic/overview.md)
1. [Sequences of action](charge-controllers/secc_generic/sequences.md)
1. [CAN databases](charge-controllers/secc_generic/databases.md)
1. [CAN messages](charge-controllers/secc_generic/can.md)
1. [Appendix](charge-controllers/secc_generic/appendix-a.md)

# Changelog

<div class="small-table compact-table">

| Since protocol version | Message | Comment |
|:----------------------:|---------|---------|
| 2 | All | 2020-03-02: Update to version 2 of the interface. |
| 1 | All | 2018-10-22: Initial version. |

</div>
