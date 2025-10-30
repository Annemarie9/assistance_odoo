Customer display
================

The **customer display** feature provides customers with real-time
checkout updates on a secondary display.



Configuration
-------------

Depending on your POS setup, the feature can be displayed
`locally on a secondary screen
<customer_display/local>`{.interpreted-text role="ref"} or on
`another monitor connected to an IoT Box
<customer_display/iot>`{.interpreted-text role="ref"}.

To activate the feature, go to the POS settings, scroll down to the
`Connected Devices`{.interpreted-text role="guilabel"} section, and tick
the `Customer Display`{.interpreted-text role="guilabel"} checkbox.



### Local {#customer_display/local}

Connect a second screen to your POS and
`open a POS session <pos/session-start>`{.interpreted-text role="ref"}.
Then, click `Customer Screen`{.interpreted-text role="guilabel"} to open
a new window to drag and drop onto the second screen.

### IoT system {#customer_display/iot}

Connect an IoT box to your database and the second screen to the IoT
box. Then, go to
`Point of Sale --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the
`Connected Devices`{.interpreted-text role="guilabel"} section, tick the
`IoT Box`{.interpreted-text role="guilabel"} checkbox, and select the
second monitor in the `Customer Display`{.interpreted-text
role="guilabel"} field.



::: {.note}
::: {.title}
Note
:::

Both devices need to be connected to the same local network.
:::

::: {.seealso}
`../configuration/pos_iot`{.interpreted-text role="doc"}
:::
