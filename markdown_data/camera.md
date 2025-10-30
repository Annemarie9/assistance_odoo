# File: /content/odoo_doc17.0/fr/content/applications/general/iot/devices/camera.md

Connect a camera
================

A camera can be connected to an
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box with an
Odoo database in just a few steps. Once a camera is connected to an
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box, it can be
used in a manufacturing process, or it can be linked to a quality
control point/quality check. Doing so allows for the taking of pictures
when a chosen quality control point/check has been reached, or when a
specific key is pressed during manufacturing.

Connection
----------

To connect a camera to an `IoT (Internet of Things)`{.interpreted-text
role="abbr"} box, simply connect the two via cable. This is usually done
with a `USB (Universal Serial Bus)`{.interpreted-text role="abbr"} cable
of some sort.

If the camera is ,
there is no need to set up anything, as it\'ll be detected as soon as
it\'s connected.

{.align-center}

Link camera to quality control point in manufacturing process
-------------------------------------------------------------

In the `Quality app`{.interpreted-text role="menuselection"}, a device
can be set up on a `Quality Control Point`{.interpreted-text
role="guilabel"}. To do that, navigate to the
`Quality app --> Quality Control --> Control Points`{.interpreted-text
role="menuselection"} and open the desired
`Control Point`{.interpreted-text role="guilabel"} that\'ll be linked to
the camera.

On the control point form, edit the control point by selecting the
`Type`{.interpreted-text role="guilabel"} field, and clicking on
`Take a Picture`{.interpreted-text role="guilabel"} from the drop-down
menu. Doing so reveals a field called `Device`{.interpreted-text
role="guilabel"}, wherein the attached *device* can be selected.
`Save`{.interpreted-text role="guilabel"} the changes, if required.

{.align-center}

The camera is now useable with the selected quality control point. When
the quality control point is reached during the manufacturing process,
the database prompts the operator to take a picture.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Quality control points can also be accessed by navigating to
`IoT App -->
Devices`{.interpreted-text role="menuselection"}. From here, select the
device. There is a `Quality Control Points`{.interpreted-text
role="guilabel"} tab, where they can be added with the device.
:::

::: {.tip}
::: {.title}
Tip
:::

On a quality check form, the `Type`{.interpreted-text role="guilabel"}
of check can also be specified to `Take a
Picture`{.interpreted-text role="guilabel"}. Navigate to
`Quality app --> Quality Control --> Quality Checks --> New`{.interpreted-text
role="menuselection"} to create a new quality check from the
`Quality Checks`{.interpreted-text role="guilabel"} page.
:::

::: {.seealso}
\-
`/applications/inventory_and_mrp/quality/quality_management/quality_control_points`{.interpreted-text
role="doc"} -
`/applications/inventory_and_mrp/quality/quality_management/quality_alerts`{.interpreted-text
role="doc"}
:::

Link camera to a work center in the Manufacturing app
-----------------------------------------------------

To link a camera to an action, it first needs to be configured on a work
center. Navigate to
`Manufacturing app --> Configuration --> Work Centers`{.interpreted-text
role="menuselection"}. Next, go to the desired
`Work Center`{.interpreted-text role="guilabel"} in which a camera will
be used to reveal that specific work center\'s detail form. From here,
add the device in the `IoT Triggers`{.interpreted-text role="guilabel"}
tab, in the `Device`{.interpreted-text role="guilabel"} column, by
clicking `Add a Line`{.interpreted-text role="guilabel"}.

Now, the camera device can be linked to the `Action`{.interpreted-text
role="guilabel"} column drop-down option labeled
`Take a Picture`{.interpreted-text role="guilabel"}. A key can also be
added to trigger the action.

::: {.important}
::: {.title}
Important
:::

The first trigger listed is chosen first. The order of triggers matters,
and they can be dragged into any desired order.
:::

::: {.note}
::: {.title}
Note
:::

On the `Work Order`{.interpreted-text role="guilabel"} screen, a status
graphic indicates whether the database is correctly connected to the
camera.
:::

::: {.seealso}
`workcenter_iot`{.interpreted-text role="ref"}
:::
