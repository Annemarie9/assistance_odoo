# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods/at_confirmation.md

At confirmation reservation
===========================

::: {#inventory/reservation_methods/at-confirmation}
The *at confirmation* reservation method reserves products **only** when
a sales order (SO) is confirmed, **and** if enough stock of the products
included in the `SO (Sales Order)`{.interpreted-text role="abbr"} is
already available.
:::

::: {.seealso}
`About reservation methods <../reservation_methods>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

To set the reservation method to *at confirmation*, navigate to
`Inventory app -->
Configuration --> Operations Types`{.interpreted-text
role="menuselection"}. Then, select the desired
`Operation Type`{.interpreted-text role="guilabel"} to configure, or
create a new one by clicking `New`{.interpreted-text role="guilabel"}.

In the `General`{.interpreted-text role="guilabel"} tab on the operation
type form, locate the `Reservation Method`{.interpreted-text
role="guilabel"} field, and select `At Confirmation`{.interpreted-text
role="guilabel"}.

{.align-center}

Workflow
--------

To see the *at confirmation* reservation method in action, create a new
`SO (Sales Order)`{.interpreted-text role="abbr"} by navigating to
`Sales app --> New`{.interpreted-text role="menuselection"}.

Add a customer in the `Customer`{.interpreted-text role="guilabel"}
field. Then, in the `Order Lines`{.interpreted-text role="guilabel"}
tab, click `Add a product`{.interpreted-text role="guilabel"}, and
select a product to add to the quotation from the drop-down menu.
Finally, in the `Quantity`{.interpreted-text role="guilabel"} column,
adjust the desired quantity of the product to sell.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the sales order.

Click the `📈 (area graph)`{.interpreted-text role="guilabel"} icon on
the product line to reveal the product\'s
`Availability`{.interpreted-text role="guilabel"} tooltip, which reveals
the `Reserved`{.interpreted-text role="guilabel"} number of units for
this order.

::: {.note}
::: {.title}
Note
:::

If there is **not** sufficient quantity of stock for the product
included in the `SO (Sales Order)`{.interpreted-text role="abbr"}, the
`📈 (area graph)`{.interpreted-text role="guilabel"} icon is red, instead
of green.

Instead of revealing the reserved number of units for the order, the
`Availability`{.interpreted-text role="guilabel"} tooltip reads
`Available`{.interpreted-text role="guilabel"}, and reveals the
available number of units (e.g., [0 Units]{.title-ref}).
:::

{.align-center}

::: {.admonition}
Forecasted Report

To see all the factors that affect product reservation, click the
`View Forecast`{.interpreted-text role="guilabel"} internal link arrow
to view the `Forecasted Report`{.interpreted-text role="guilabel"}
dashboard.

The `Forecasted Report`{.interpreted-text role="guilabel"} displays
forecast information about the product(s) included in the sales order;
namely, any live receipts of the product, and any active sales orders,
which are listed in the `Used By`{.interpreted-text role="guilabel"}
column. See how each order is fulfilled in the
`Replenishment`{.interpreted-text role="guilabel"} column.

Additionally, the `Forecasted`{.interpreted-text role="guilabel"}
quantity is calculated at the top of the page, by adding the
`On Hand`{.interpreted-text role="guilabel"} and
`Incoming`{.interpreted-text role="guilabel"} quantity, and subtracting
the `Outgoing`{.interpreted-text role="guilabel"} quantity, as shown
below:

{.align-center}

If one order should be prioritized over another order, click the
`Unreserve`{.interpreted-text role="guilabel"} button on the
corresponding order line in the `Replenishment`{.interpreted-text
role="guilabel"} column.
:::

To deliver the products, click the `Delivery`{.interpreted-text
role="guilabel"} smart button at the top of the sales order form. To
confirm that the reservation worked properly, ensure that the `Product
Availability`{.interpreted-text role="guilabel"} field reads
[Available]{.title-ref} (in green text), and the numbers in the
`Demand`{.interpreted-text role="guilabel"} and
`Quantity`{.interpreted-text role="guilabel"} columns match (in this
case, both should read [100.00]{.title-ref}).

{.align-center}

Once ready, click `Validate`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `Manual reservation <manually>`{.interpreted-text role="doc"} -
`Before scheduled date reservation <before_scheduled_date>`{.interpreted-text
role="doc"}
:::
