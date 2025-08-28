# Advantics charge controllers

Advantics charge controllers act as communications "bridges" between protocols used for charging
(CCS, CHAdeMO) and components of chargers or vehicles (power modules, BMS, contactors, sensors, etc.).
They are however much more than plain bridges. Instead of just giving you more digestible version of
CCS messages or CHAdeMO frames, our controllers translate them into forms and sequences that are
closer to how main components of a charger or vehicle operates.

They run Linux systems on ARM Cortex A7 CPU. They already integrate the communication stacks of the
charging protocols, as well as CAN communications for selected devices. We also provide so-called
"Generic CAN interfaces" for both charger and vehicle controllers that are agnostic of the particular
components you use in your systems, and abstract away some of the complexities of supporting different
charging protocols and charging modes. Customers can also add their own applications to controllers,
for instance to integrate directly with a specific CAN or RJ485 devices, or with a particular cloud
service.

Hardware-wise, each controllers integrate the necessary components for charger-vehicle communications
(PLC modem, CAN transceivers). As well as all output drivers, and analog and digital inputs sensing
to cover the most typical use cases of charging applications (eg. contactors or relays drivers,
pistol temperature sensors, CCS CP PWM generation and sensing, PP sensing, CHAdeMO SEQ1/SEQ2/PERM/PROX
IOs, pistol lock drivers and feedback).

For charging stations, our main product is **ADM-CS-SECC**. It comes in a DIN rail housing and
supports three pistols (CCS DC, CCS AC and CHAdeMO). It has a charger-side CAN bus and RJ485 interface,
relays for output contactors, some general purpose industrial IOs, an ethernet port as well as a
mPCIe slot for cellular or wifi modules.

For vehicles, our main product is **ADM-CS-EVCC**. It comes in an automotive housing and supports
one CCS AC and/or DC inlet. It has a vehicle-side CAN bus, contactors drivers and inlet lock driver.
It also has an ethernet port but it is not exposed outside of the housing and is mainly used for
setup, update or retrieving logs from it.
