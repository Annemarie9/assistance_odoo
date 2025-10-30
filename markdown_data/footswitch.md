# File: /content/odoo_doc17.0/fr/content/applications/general/iot/devices/footswitch.md

Connect a footswitch
====================

When working in a manufacturing environment, it\'s always better for an
operator to have both hands available at all times. Odoo\'s
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box makes this
possible when using a footswitch.

In fact, with a footswitch, the operator is able to go from one screen
to another, and perform actions using their foot. This can be configured
in just a few steps on the work center in the *Manufacturing* app.

Connection
----------

To connect a footswitch to the
`IoT (Internet of Things)`{.interpreted-text role="abbr"} box, connect
the two devices via cable. More often than not, this is done with a
`USB (Universal Serial Bus)`{.interpreted-text role="abbr"} cable.

If the footswitch is a [supported
device](https://www.odoo.com/page/iot-hardware), there is no need to
take further action, since it\'ll be automatically detected when
connected.

{.align-center}

Link a footswitch to a work center in the Odoo Manufacturing app
----------------------------------------------------------------

To link a footswitch to an action, it first needs to be configured on a
work center. Navigate to
`Manufacturing app --> Configuration --> Work Centers`{.interpreted-text
role="menuselection"}. From here, go to the desired
`Work Center`{.interpreted-text role="guilabel"} in which the footswitch
will be used, and add the device in the `IoT Triggers`{.interpreted-text
role="guilabel"} tab, under the `Device`{.interpreted-text
role="guilabel"} column, by selecting `Add a
Line`{.interpreted-text role="guilabel"}. Doing so means the footswitch
can be linked to an option in the `Action`{.interpreted-text
role="guilabel"} column drop-down, and optionally, a key can be added to
trigger it. An example of an `Action`{.interpreted-text role="guilabel"}
in the *Manufacturing app* could be the `Validate`{.interpreted-text
role="guilabel"} or `Mark as Done`{.interpreted-text role="guilabel"}
buttons on a manufacturing work order.

{.align-center}

::: {.important}
::: {.title}
Important
:::

It should be noted that the first listed trigger is chosen first. So,
the order matters, and these triggers can be dragged into any order. In
the picture above, using the footswitch automatically skips the part of
the process that\'s currently being worked on.
:::

::: {.note}
::: {.title}
Note
:::

On the `Work Order`{.interpreted-text role="guilabel"} screen, a status
graphic indicates whether the database is correctly connected to the
footswitch.
:::

::: {.seealso}
`workcenter_iot`{.interpreted-text role="ref"}
:::
