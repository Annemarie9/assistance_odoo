SIX
===

Connecting a SIX payment terminal allows you to offer a fluid payment
flow to your customers and ease the work of your cashiers.

::: {.warning}
::: {.title}
Warning
:::

Even though Worldline has recently acquired SIX Payment Services and
both companies use Yomani payment terminals, the firmware they run is
different. Terminals received from Worldline are therefore not
compatible with this integration.
:::

Configuration
-------------

### Install the POS IoT Six module

To activate the POS IoT Six module, go to `Apps`{.interpreted-text
role="guilabel"}, remove the `Apps`{.interpreted-text role="guilabel"}
filter, and search for **POS IoT Six**. This module adds the necessary
driver and interface to your database to detect Six terminals.

::: {.note}
::: {.title}
Note
:::

This module replaces the **POS Six** module.
:::

### Connect an IoT system

Connecting a Six payment terminal to Odoo is requires
`using an IoT system
</applications/general/iot>`{.interpreted-text role="doc"}.

### Configure the terminal ID

Navigate to the IoT system\'s homepage, where you can find the
`Six payment terminal`{.interpreted-text role="guilabel"} field once
your database server is connected to the IoT system. Click
`Configure`{.interpreted-text role="guilabel"}, fill in the
`Terminal ID`{.interpreted-text role="guilabel"} field with the ID
received from Six, and click `Connect`{.interpreted-text
role="guilabel"}. Your Six terminal ID should appear in the
`Current Terminal Id`{.interpreted-text role="guilabel"} section.



Odoo automatically restarts the IoT system when the Six terminal ID is
configured. If your Six terminal is online, it will be automatically
detected and connected to the database. Check the IoT system\'s homepage
under the `Payments`{.interpreted-text role="guilabel"} section to
confirm the connection.



### Configure the payment method {#six/configure}

Enable the payment terminal
`in the application settings <configuration/settings>`{.interpreted-text
role="ref"} and
`create the related payment method <../../payment_methods>`{.interpreted-text
role="doc"}. Set the journal type as `Bank`{.interpreted-text
role="guilabel"} and select `SIX IOT`{.interpreted-text role="guilabel"}
in the `Use a Payment Terminal`{.interpreted-text role="guilabel"}
field. Then, select your terminal device in the
`Payment Terminal Device`{.interpreted-text role="guilabel"} field.


