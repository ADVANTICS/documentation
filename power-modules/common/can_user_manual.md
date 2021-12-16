# The CAN Bus protocol in the family of Advantics power converters
The protocol is a lightweight custom implementation over the standard ISO 11898 CAN data link layer, with a variable payload that depends on the frame ID. Each ID is associated with an internal register or a memory area. The ID carries also information about the source node and its position in the stack. The next definitions apply along this document:

- Frame: Is the basic entity defined in the CAN standard. Among other fields, it contains the ID field and the payload.
- Message: It is defined as the combination of the ID field and the payload. A message can have an empty payload.
- Packet: In our context, a packet is a chunk of data which can be complete or partial, and that is carried encapsulated as a payload.

All the messages in the CAN bus are directed, that is, they can be either input or output in relation to the device. __Input__ messages come from the CAN bus into the device (receiver), while __output__ messages are sent from the device towards the bus (transmitter).

Input messages typically contain data whose destination is a memory area, and therefore are called __commands__. Output messages are going to be reffered as __messages__. They typically carry response data from previous __commands__, or periodic readout data (in example, system status register contents).

Each frame can be of the __base__ or the __extended__ type, depending on the ID length (11 or 29 bits). The protocol only uses __extended__ type.

### ID format

A CAN frame ID in our system is formatted as follows:

![CAN_address](../common/images/CAN_address_space.png ':size=60%')
<figcaption style="text-align: center">Figure X: CAN address space</figcaption>

The message ID is divided into fields, accordingly with the ID priority restrictions, carrying node identity data. It comprises four different fields:

#### Register address field [15:0] 
It is a 16bit field allocated that is intended to address a sub-set of the registers 0x0000 to 0x7fff in the base frame (16 identifier bits). The bit 15 is reserved as direction bit. 
#### Device (service) type field [23:16]
 It is an 8bit field allows for up to 256 device types. This field uniquely identifies the addressed device by its type. This filed can be also used by common services running on modules. Typically these are services run temporarily and behave as a "virtual" device, therefore they have device type assigned to them.
#### Position within stack field [28:24]
 It is an 5bit field allows for up to 32 stacked devices. In systems where more than one device is stacked (i.e. paralleled), this field indicates the position of the addressed device in the stack. The position 0 is reserved to the __master__ if __master__ semantics make sense for given stack setup.

![Device type and stack position tree](../common/images/ID_type_stackPosition_master.png ':size=60%')
<figcaption style="text-align: center">Figure X: Device type and stack position tree</figcaption>



Per each device __type__ there can be a master. In general lines, this exploits the ID format in such a way that different device types can be stacked together, sharing the same CAN bus. Each type will __master__ the stack of its same __type__, while the priority is defined also by the device __type__ field value. In example, any critical device will have always the lowest ID, therefore having the lowest __type__ code.

### Addressable space

The addressable space depends on the type of frame, if it is __base__ the dimension of the address space is 7 bits (128 registers), while for the __extended__ type this space is of 7 + 11 = 18 bits (262k).

![Device type and stack position tree](../common/images/protocol_regions.png ':size=60%')
<figcaption style="text-align: center">Figure X: Addressable space division</figcaption>

#### Protocol description

Each message is described using the next notation:

ID Offset:: The ID offset, is a relative address location within the whole ID range for the given CAN packet. It points to an specific location where a register or a service is assigned. The offset is given by the __register address field__.

Payload:: Each CAN packet carries a payload which varies from 0 to 8 bytes (0 to 64 bits). The payload length is always fixed for each message type.

Pyload length:: The payload is always measured in Bytes. The length is specified in octets, and range 0 to 8. Each Byte inside the payload is referred starting at 0 (0 to 7).

### Message description

Each message is described using two main tables. The first table describes the general characteristics of the message:

<div class="small-table compact-table">

|Field|Value|
|--------------|---------|
| **Frame ID** | 0x78000 |
| **Length [Bytes]** | 8 |
| **Periodicity [ms]** | 1000 |
| **Direction** | IN |

</div>


The message direction is always relative to the device, therefore **OUT** messages are messages sent *from* the device to the CAN bus, while **IN** messages
are messages coming *from* the CAN bus to the device.

A second table lists the payload:

<div class="small-table compact-table">

| Signal | Length (bits) | Type |
|--------|---------------|------|
| Device_type | 8 | Label set |
| HW_revision | 8 | Unsigned |
| HW_variant | 8 | Unsigned |
| Stack_position | 8 | Unsigned |
| SN_number | 32 | Unsigned |

</div>

#### Payload description

The payload in a CAN message can be up to 8 bytes, which are used as a flat 64 bit payload organized as the previous table (payload contents index) indicates.

An example description table is as follows:

<div class="small-table compact-table">

| Start bit | Length (bits) | Type | Unit | Scale | Offset | Min | Max |
|-----------|---------------|------|------|-------|--------|-----|-----|
| 0 | 8 | Unsigned | Amps | 0.01 | 0 |   |   |

</div>

Which describes a 16bit element, of type **unsigned**, starting at the payload offset 0.

#### Types

The type field indicates the format of the data in the payload item. Possible types are:

<div class="small-table compact-table">

| Type | Description | Example|
|------|-------------|--------|
| Unsigned | Unsigned integer of the specified length | uint16|
| Signed | Signed integer of the specified length | int16|
| Single | IEEE754 Single precision floating point | float|
| Double | IEEE754 Double precision floating point | double|
| Single bit | A single bit (typically a flag) | bool |

</div>

#### Variables and scale factors

A payload element can be the value of a variable, measured in the units indicated. To obtain the value of the variable from the payload raw value, a first order polynomial is used:

y = x*scale + offset

Where **y** is the value of the variable, and **x** is the payload value. For example:

>Scale = 0.01
>
>Offset = 12
>
>Payload value: x = 140
>
>y = 140*0.01 + 12
>
>y = 13.4

#### Variable limits: minimum and maximum

A variable has a mathematical range, which is the set of values it can take given the internal representation (i.e. uint16), and a valid range.
The valid range refers to the possible values it can take in a given interval, which are constrained by physical, mechanical or electrical conditions of the
process which uses the variable.

The payload can specify the validity limits for a given variable. The limits are specified in the units and scale
of the variable, not in the payload raw value. When only a limit is specified (i.e. maximum), the other limit is assumed to be the absolute minimum or
maximum that the given variable can take (i.e. 0).
