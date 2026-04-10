> [!UPDATE] {docsify-updated}
# DC contactors

Advantics controller can control DC contactors directly with its embedded H-Bridge driver. Or, if
you use special types of contactors and/or want to add addition checks before closing/opening
contactors, this generic interface will tell you when to close or open them. In such case, you have
to provide feedback on their status.

These configuration entries are all under the `[vehicle]` section.

## dc_contactors_use_ios

<figcaption>Example</figcaption>

    dc_contactors_use_ios = false

Specify if DC contactors control is done with the dedicated controller IOs or through the vehicle
communication interface. If set to false, it means the communication interface is used. Otherwise,
if set to true, the corresponding message in the communication interface are ignored.

Default to false.

## dc_contactors_ios_has_feedback

<figcaption>Example</figcaption>

    dc_contactors_ios_has_feedback = true

Some contactors don't have any feedback wireable on Advantics controller dedicated digital input
(it has to contact to ground when closed).

Default to true.

## disable_e_stop_contactor_force_open_current_not_reliable

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    disable_e_stop_contactor_force_open_current_not_reliable = false

Disables force opening the contactors during E-stop when the current measurement is not reliable
(e.g. due to a CAN reporting failure).

By default, when the current measurement is not reliable during an E-stop, the contactors are
immediately force-opened to ensure safety. Setting this to `true` disables that behaviour.

Default to false.

## delay_e_stop_contactor_force_open_current_not_reliable

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    delay_e_stop_contactor_force_open_current_not_reliable = false

Instead of immediately force-opening the contactors when the current measurement is not reliable
during an E-stop, this option introduces a configurable delay to give time for the system to
stabilize before opening.

Only effective if `disable_e_stop_contactor_force_open_current_not_reliable` is set to `false`.

Default to false.

## contactor_force_open_current_not_reliable_delay_ms

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    contactor_force_open_current_not_reliable_delay_ms = 60000

Delay in milliseconds before force-opening the contactors during E-stop when the current
measurement is not reliable.

Only effective if `delay_e_stop_contactor_force_open_current_not_reliable` is set to `true` and
`disable_e_stop_contactor_force_open_current_not_reliable` is set to `false`.

Default to 60000 ms (60 s).

## enable_e_stop_contactor_force_open_timeout

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    enable_e_stop_contactor_force_open_timeout = false

Enables a timeout after which the contactors are force-opened during E-stop even if the current is
still above 5 A. This is a last-resort measure if the current does not drop after E-stop.

By default, the contactors are not force-opened while current is still flowing, to avoid damaging
them.

Default to false.

## contactor_force_open_timeout_ms

> [!NOTE]
> This is an advanced configuration option.

<figcaption>Example</figcaption>

    contactor_force_open_timeout_ms = 60000

Timeout in milliseconds after which the contactors are force-opened during E-stop while current is
still flowing (above 5 A).

Only effective if `enable_e_stop_contactor_force_open_timeout` is set to `true`.

Default to 60000 ms (60 s).

# Possible Configurations

<style>
  table.custom-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed; /* ensure fixed column widths */
  }
  table.custom-table th,
  table.custom-table td {
    border: 1px solid #ccc;
    padding: 8px;
    vertical-align: top;
    box-sizing: border-box;
    overflow-wrap: break-word;
    word-break: break-word;
  }
  /* Make first column wider; second and third columns equal */
  table.custom-table col:nth-child(1) { width: 20%; }
  table.custom-table col:nth-child(2),
  table.custom-table col:nth-child(3) { width: 40%; }
</style>

<table class="custom-table">
  <colgroup>
    <col>
    <col>
    <col>
  </colgroup>
    <thead>
        <tr>
            <th></th>
            <th><code>dc_contactors_ios_has_feedback == False</code></th>
            <th><code>dc_contactors_ios_has_feedback == True</code> (default)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong><code>dc_contactors_use_ios == False</code> (default)</strong></td>
            <td>
                <ul>
                    <li>Contactors control via CAN bus</li>
                    <li>Contactors Feedback via CAN bus</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>Contactors control via IO interface</li>
                    <li>Contactors Feedback via CAN bus</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><strong><code>dc_contactors_use_ios == True</code></strong></td>
            <td>
                <ul>
                    <li>Contactors control via IO interface</li>
                    <li>Contactors Feedback set to True automatically by the controller after a configurable delay (Contactors don't have feedback which means there's no way to confirm their closed state)</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>Contactors control via IO interface</li>
                    <li>Contactors Feedback via IO interface</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>