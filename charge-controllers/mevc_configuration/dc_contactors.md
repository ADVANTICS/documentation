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