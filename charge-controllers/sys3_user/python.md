> [!UPDATE] {docsify-updated}
# Developing in Python

If you want to write your program running on the controller in Python you have three options:

* Use the Python installed on the system itself.
* Use the Python available in the container `advantics/python:run`.
* Use your own Python container image.

`advantics/python:run` usually contains more recent versions of installed packages.

In any case, because it's Python running on full-featured Linux system, there are pretty much no
difference between a program running on a PC, and a program running on the controller. Therefore,
you could conveniently develop most of your program on a PC and only do final test and integration
on the controller. This is how we do it.

Performance wise, for sure it is not up-to-speed with assembly :). But we found it sufficient for
our own applications (some of which are tightly performance constrained, having to respond to
complex CCS EXI-encoded requests in under 25 ms for instance).

If you use the language correctly you will get decent performances (like for any language). At worst,
you can always optimize part of your code with things like Cython or Nuitka (although it makes for
more complicated compilation steps as it has to target the ARMv7 instruction set).

## Installed packages

Here are the major packages installed on the host system and in container image `advantics/python:run`:

* Python 3.9
* pip
* python-can
* cantools
* click
* pyzmq
* transitions

## Installing other packages

`pip` is available on both the host system as well as inside the `advantics/python:run` container. Therefore, it can be as simple as executing a `pip install <PACKAGE_NAME>` command on the host system (don't forget to switch your system to [writable mode](charge-controllers/sys3_user/read-only.md) beforehand) or in an instantiated container, or as a `RUN` command of a Dockerfile.

## Accessing a CAN bus

You can use the python-can package, which handles using SocketCAN directly. Here is a simple example:

```python
import click
import can
import struct


@click.command()
@click.option('--can-if', default='can0', help='CAN Interface name')
def main(can_if):
    '''Simple example, receive messages, count them and send a CAN message
       on ID 0x123 with the counter value in 8-bytes big-endian integer'''

    can_bus = can.interface.Bus(can_if, bustype='socketcan')
    counter = 0

    while True:
        # Receive
        msg_r = can_bus.recv()
        counter += 1
        print('>>>', counter, msg_r)

        # Send
        data = struct.pack('>Q', counter)
        msg_s = can.Message(arbitration_id=0x123, data=data, extended_id=False)
        can_bus.send(msg_s)
```

> [!TIP]
> We would strongly advise you to look at [cantools](https://pypi.org/project/cantools/) as well.
>
> It handles encoding and decoding of CAN messages according to a CAN database in Kayak or DBC format.
> As such, your chances of having bugs in your CAN implementation are severely reduced.
