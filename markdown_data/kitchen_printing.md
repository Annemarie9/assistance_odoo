Orders printing
===============

Integrating printers in a restaurant or bar\'s workflow can enhance
communication and collaboration between the front-of-house and
back-of-house teams, leading to a more streamlined and efficient
service.

Configuration
-------------

### Enable and create printers {#kitchen_printing/enable}

To enable sending orders to a kitchen or bar printer, go to
`Point of Sale -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
scroll down to the `Restaurant & Bar`{.interpreted-text role="guilabel"}
section, and enable `Kitchen Printers`{.interpreted-text
role="guilabel"}. Type in a name for the printer in the
`Printers`{.interpreted-text role="guilabel"} field and click
`Create and edit...`{.interpreted-text role="guilabel"} to open a setup
form.

To get a list of all the printers already created or to modify an
already created printer, click `--> Printers`{.interpreted-text
role="guilabel"} and select the desired printer to open the setup form.

{.align-center}

### Setup form {#kitchen_printing/setup-form}

From the `setup form <kitchen_printing/enable>`{.interpreted-text
role="ref"}, select the `Printer Type`{.interpreted-text
role="guilabel"} according to your installation:

-   If your printer is connected to an IoT system, select
    `Use a printer connected to the
    IoT Box`{.interpreted-text role="guilabel"} and select the device in
    the `IoT Device`{.interpreted-text role="guilabel"} field.
-   If you use an Epson printer that does not require an IoT system,
    select `Use an Epson
    printer`{.interpreted-text role="guilabel"} and enter the printer\'s
    IP address in the `Epson Printer IP Address`{.interpreted-text
    role="guilabel"} field.

::: {.seealso}
\- `/applications/general/iot/connect`{.interpreted-text role="doc"} -
`/applications/general/iot/devices/printer`{.interpreted-text
role="doc"} - `../configuration/epos_ssc`{.interpreted-text role="doc"}
:::

Set your printer to print specific products based on their POS category.
To do so, click `Add a line`{.interpreted-text role="guilabel"} in the
`Printed Product Categories`{.interpreted-text role="guilabel"} field.

{.align-center}

Print orders
------------

From an open session, start taking an order and click
`Order`{.interpreted-text role="guilabel"} to send it to the bar or the
kitchen.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When products can be printed, they appear in green in the cart, and the
order button turns green.
:::
