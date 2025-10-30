# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods/manually.md

Manual reservation
==================

::: {#inventory/reservation_methods/manually}
Unlike the *At Confirmation* reservation method, the *Manually*
reservation method does **not** reserve products automatically.
:::

Instead, once a sales order (SO) is confirmed, product availability
**must** be checked manually, and the required quantity **must** be
reserved manually.

::: {.seealso}
`About reservation methods <../reservation_methods>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

To set the reservation method to *Manually*, navigate to
`Inventory app -->
Configuration --> Operations Types`{.interpreted-text
role="menuselection"}. Then, select the desired
`Operation Type`{.interpreted-text role="guilabel"} to be configured, or
create a new one by clicking `New`{.interpreted-text role="guilabel"}.

In the `General`{.interpreted-text role="guilabel"} tab, locate the
`Reservation Method`{.interpreted-text role="guilabel"} field, and
select `Manually`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When the `Type of Operation`{.interpreted-text role="guilabel"} is
changed to `Receipt`{.interpreted-text role="guilabel"} on an
`Operations Type`{.interpreted-text role="guilabel"} form, reservation
methods are **not** available.
:::

Workflow
--------

To see the *Manually* reservation method in action, create a new
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

Click the green `📈 (area graph)`{.interpreted-text role="guilabel"} icon
on the product line to reveal the product\'s
`Availability`{.interpreted-text role="guilabel"} tooltip. This tooltip
reveals the reserved number of units for this order. Because the
reservation method is set to *Manually*, the
`Reserved`{.interpreted-text role="guilabel"} quantity reads [0
Units]{.title-ref}.

However, below that quantity reads [Available in stock]{.title-ref}.
This is because the quantity is available, but must be manually
reserved.

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
`Reserved`{.interpreted-text role="guilabel"}, and reveals the available
number of units (e.g., [0 Units]{.title-ref}).

Additionally, unless there is a set replenishment or a live receipt, it
also reads `No
future availability`{.interpreted-text role="guilabel"}, in red text.
:::

{.align-center}

Once the `SO (Sales Order)`{.interpreted-text role="abbr"} is confirmed,
navigate to the `Inventory app`{.interpreted-text role="menuselection"},
and locate the `Delivery Orders`{.interpreted-text role="guilabel"} card
on the `Inventory Overview`{.interpreted-text role="guilabel"} page.

The `Delivery Orders`{.interpreted-text role="guilabel"} card displays
the current status of live orders, including those with a
`Waiting`{.interpreted-text role="guilabel"} status. Orders with this
status indicate that the products in those orders have either not been
reserved yet, or are not in stock at all.

{.align-center}

To see the `SO (Sales Order)`{.interpreted-text role="abbr"} created
previously, click the `(#) Waiting`{.interpreted-text role="guilabel"}
button on the card (in this case, [8 Waiting]{.title-ref}).

Locate the delivery order (DO) tied to the
`SO (Sales Order)`{.interpreted-text role="abbr"} that was previously
created, and click the line to view it.

On the `Delivery Order`{.interpreted-text role="guilabel"} form, the
status in the `Product Availability`{.interpreted-text role="guilabel"}
field is listed as [Available]{.title-ref}, in yellow text, instead of
green. This is because there is sufficient stock on hand for this order,
but no quantity has been reserved yet.

In the `Operations`{.interpreted-text role="guilabel"} tab, on the
`Product`{.interpreted-text role="guilabel"} line, the numbers in the
`Demand`{.interpreted-text role="guilabel"} column and the
`Quantity`{.interpreted-text role="guilabel"} column do *not* match.

In this case, the `Demand`{.interpreted-text role="guilabel"} column
lists [10.00]{.title-ref}, while the `Quantity`{.interpreted-text
role="guilabel"} column lists [0]{.title-ref}.

{.align-center}

To manually reserve the specified quantity of the product for this
order, click the `Check Availability`{.interpreted-text role="guilabel"}
button at the top of the form. Doing so turns the
[Available]{.title-ref} status in the
`Product Availability`{.interpreted-text role="guilabel"} field green,
and changes the number in the `Quantity`{.interpreted-text
role="guilabel"} column to match the `Demand`{.interpreted-text
role="guilabel"} column.

This is because there is sufficient quantity in stock to reserve for the
order.

Once ready, click `Validate`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Multiple orders with a *Waiting* status can be manually reserved at the
same time, and set to *Ready* status.

To do that, open the `Inventory`{.interpreted-text role="menuselection"}
app, which reveals the `Inventory
Overview`{.interpreted-text role="guilabel"} page. The
`Inventory Overview`{.interpreted-text role="guilabel"} page is also
accessible by navigating to
`Inventory app --> Overview`{.interpreted-text role="menuselection"}.

From the `Inventory Overview`{.interpreted-text role="guilabel"} page,
click the `(#) Waiting`{.interpreted-text role="guilabel"} button on the
`Delivery Orders`{.interpreted-text role="guilabel"} card.

Then, tick the checkboxes to the left of each desired order, or tick the
checkbox in the header row, to the far-left, to select all orders on the
page at once.

Then, click the `Check Availability`{.interpreted-text role="guilabel"}
button at the top of the page.

If the products included in every selected order have enough stock
on-hand, this reserves the products, and moves the order into
`Ready`{.interpreted-text role="guilabel"} status. Upon receiving a
`Ready`{.interpreted-text role="guilabel"} status, the order disappears
from the `Waiting`{.interpreted-text role="guilabel"} list.

If there is *not* enough stock on-hand, the order retains its current
status, and remains on the list.

{.align-center}
:::

::: {.seealso}
\- `At confirmation reservation <at_confirmation>`{.interpreted-text
role="doc"} -
`Before scheduled date reservation <before_scheduled_date>`{.interpreted-text
role="doc"}
:::
