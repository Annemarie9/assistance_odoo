# File: /content/odoo_doc17.0/fr/content/applications/general/iot/devices/measurement_tool.md

Connect a measurement tool
==========================

::: {#iot/devices/measurement-tool}
With Odoo\'s `IoT (Internet of Things)`{.interpreted-text role="abbr"}
box, it is possible to connect measurement tools to the Odoo database
for use in the *Quality app* on a quality control point/quality check,
or for use in a work center during the manufacturing process.
:::

Find the list of supported devices here: [Supported
devices](https://www.odoo.com/page/iot-hardware).

Connect with universal serial bus (USB)
---------------------------------------

To add a device connected by
`USB (Universal Serial Bus)`{.interpreted-text role="abbr"}, plug the
`USB (Universal
Serial Bus)`{.interpreted-text role="abbr"} cable into the
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box, and the
device appears in the Odoo database.

{.align-center}

Connect with bluetooth
----------------------

Activate the Bluetooth functionality on the device (see the device
manual for further explanation), and the
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box
automatically connects to the device.

{.align-center}

Link a measurement tool to a quality control point in the manufacturing process
-------------------------------------------------------------------------------

In the *Quality app*, a device can be set up on a quality control point.
To do that, navigate to
`Quality app --> Quality Control --> Control Points`{.interpreted-text
role="menuselection"}, and open the desired control point to which the
measurement tool should be linked.

From here, edit the control point, by selecting the
`Type`{.interpreted-text role="guilabel"} field, and clicking
`Measure`{.interpreted-text role="guilabel"} from the drop-down menu.
Doing so reveals a field called `Device`{.interpreted-text
role="guilabel"}, where the attached device can be selected.

Additionally, `Norm`{.interpreted-text role="guilabel"} and
`Tolerance`{.interpreted-text role="guilabel"} can be configured.
`Save`{.interpreted-text role="guilabel"} the changes, if required.

At this point, the measurement tool is linked to the chosen quality
control point. The value, which usually needs to be changed manually, is
automatically updated while the tool is being used.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Quality control points can also be accessed by navigating to
`IoT App -->
Devices`{.interpreted-text role="menuselection"}, then select the
device. There is a `Quality Control Points`{.interpreted-text
role="guilabel"} tab, where they can be added with the device.
:::

::: {.note}
::: {.title}
Note
:::

On a quality check detail form, the `Type`{.interpreted-text
role="guilabel"} of check can also be specified to
`Measure`{.interpreted-text role="guilabel"}. Access a new quality check
detail page, by navigating to
`Quality app --> Quality Control --> Quality Checks --> New`{.interpreted-text
role="menuselection"}.
:::

::: {.seealso}
\-
`../../../inventory_and_mrp/quality/quality_management/quality_control_points`{.interpreted-text
role="doc"} -
`../../../inventory_and_mrp/quality/quality_management/quality_alerts`{.interpreted-text
role="doc"}
:::

Link a measurement tool to a work center in the Manufacturing app
-----------------------------------------------------------------

To link a measurement tool to an action, it first needs to be configured
on a work center. To do that, navigate to
`Manufacturing app --> Configuration --> Work Centers`{.interpreted-text
role="menuselection"}. Then, select the desired work center in which the
measurement tool will be used.

On the work center page, add the device in the
`IoT Triggers`{.interpreted-text role="guilabel"} tab, under the
`Device`{.interpreted-text role="guilabel"} column, by selecting
`Add a Line`{.interpreted-text role="guilabel"}. Then, the measurement
tool can be linked to the `Action`{.interpreted-text role="guilabel"}
drop-down menu option labeled `Take Measure`{.interpreted-text
role="guilabel"}. A key can be added to trigger the action.

::: {.important}
::: {.title}
Important
:::

It should be noted that the first listed trigger is chosen first. The
order matters, and these triggers can be dragged into any order.
:::

::: {.note}
::: {.title}
Note
:::

On the `Work Order`{.interpreted-text role="guilabel"} screen, a status
graphic indicates whether the database is correctly connected to the
measurement tool.
:::

::: {.seealso}
`workcenter_iot`{.interpreted-text role="ref"}
:::
