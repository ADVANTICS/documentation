> [!UPDATE] {docsify-updated}
# DC contactors

Advantics controller can control DC contactors directly with its embedded H-Bridge driver. Or, if
you use special types of contactors and/or want to add addition checks before closing/opening
contactors, this generic interface will tell you when to close or open them. In such case, you have
to provide feedback on their status.

## dc_contactors_use_ios

<figcaption>Example</figcaption>

    dc_contactors_use_ios = true

Specify if DC contactors control is done with the dedicated controller IOs or through the vehicle
communication interface. If set to false, it means the communication interface is used. Otherwise,
if set to true, the corresponding message in the communication interface are ignored.

Default to false.

## dc_contactors_ios_has_feedback

<figcaption>Example</figcaption>

    dc_contactors_ios_has_feedback = true

Some contactors don't have any feedback wireable on Advantics controller dedicated digital input
(it has to contact to ground when closed). In such case, set this option to false. Only matters if
`dc_contactors_use_ios` is true.

Default to true.
