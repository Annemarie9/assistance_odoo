# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods/before_scheduled_date.md

Before scheduled date reservation
=================================

::: {#inventory/reservation_methods/before-scheduled-date}
The *Before scheduled date* reservation method allows users to select a
specific number of days that act as the maximum number of days
**before** a scheduled delivery date, when products included in a sales
order (SO) should be reserved.
:::

::: {.seealso}
`About reservation methods <../reservation_methods>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

To set the reservation method to *Before scheduled date*, navigate to
`Inventory app
--> Configuration --> Operations Types`{.interpreted-text
role="menuselection"}. Then, select the desired
`Operation Type`{.interpreted-text role="guilabel"} to configure, or
create a new one by clicking `New`{.interpreted-text role="guilabel"}.

In the `General`{.interpreted-text role="guilabel"} tab, locate the
`Reservation Method`{.interpreted-text role="guilabel"} field, and
select `Before scheduled date`{.interpreted-text role="guilabel"}.

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

Once selected, a new `Reserve before scheduled date`{.interpreted-text
role="guilabel"} field appears below. From this field, the number of
`days before`{.interpreted-text role="guilabel"} and
`days before when starred`{.interpreted-text role="guilabel"} can be
changed from the default [0]{.title-ref}.

Changing the `days before`{.interpreted-text role="guilabel"} value
changes the maximum number of days before a scheduled date that products
should be reserved.

Changing the `days before when starred`{.interpreted-text
role="guilabel"} value changes the maximum number of days before a
scheduled date that products should be reserved if the transfers are
starred (favorited).

::: {.example}
Here, the `days before`{.interpreted-text role="guilabel"} value is set
to [2]{.title-ref} days before, and the `days before
when starred`{.interpreted-text role="guilabel"} value is set to
[3]{.title-ref}.

This means products are reserved two days before the scheduled delivery
date for normal orders, and three days before the scheduled delivery
date for starred (favorited) transfers.

{.align-center}

This is the configuration applied for the following workflow found
below.
:::

### Edit product form

Before the *Before scheduled date* reservation method can be used,
ensure that a *customer lead time* is added to products that plan to be
sold with this method.

To do that, navigate to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select the desired product to configure.

On the product form, click the `Inventory`{.interpreted-text
role="guilabel"} tab, and under the `Logistics`{.interpreted-text
role="guilabel"} section, change the value in the
`Customer Lead Time`{.interpreted-text role="guilabel"} field.

For this example workflow, change it to [5]{.title-ref} days.

This sets the scheduled delivery date for this specific product to five
days after the creation date of the sales order.

{.align-center}

Workflow
--------

To see the *Before scheduled date* reservation method in action, create
a new `SO (Sales Order)`{.interpreted-text role="abbr"} by navigating to
`Sales app --> New`{.interpreted-text role="menuselection"}.

Add a customer in the `Customer`{.interpreted-text role="guilabel"}
field, then, in the `Order Lines`{.interpreted-text role="guilabel"}
tab, click `Add a product`{.interpreted-text role="guilabel"}, and
select a product from the drop-down menu that has a configured *customer
lead time*, to add to the quotation form.

Finally, in the `Quantity`{.interpreted-text role="guilabel"} column,
adjust the desired quantity of the product to sell.

For this sample workflow, set the `Quantity`{.interpreted-text
role="guilabel"} to [10]{.title-ref}.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the sales order.

Click the green `📈 (area graph)`{.interpreted-text role="guilabel"} icon
on the product line to reveal the product\'s
`Availability`{.interpreted-text role="guilabel"} tooltip. This tooltip
reveals the reserved number of units for this order. Because the
reservation method is set to *Before scheduled date*, the
`Reserved`{.interpreted-text role="guilabel"} quantity reads [0
Units]{.title-ref}.

However, below that quantity reads [Available in stock]{.title-ref}.
This is because the quantity is available, but the scheduled date, for
this example workflow, is five days from the order date.

Since reservation is not until two days before the scheduled delivery,
it will not reserve the products until then.

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

Click the `Delivery`{.interpreted-text role="guilabel"} smart button to
see the delivery order form.

On the delivery order form, the status in the
`Product Availability`{.interpreted-text role="guilabel"} field is
listed as [Available]{.title-ref}, in yellow text, instead of green.
This is because there is sufficient stock on-hand for this order, but no
quantity has been reserved yet.

Note the `Scheduled Date`{.interpreted-text role="guilabel"} field,
above the `Product Availability`{.interpreted-text role="guilabel"}
field, displays the date five days from the order creation date. This
indicates that the products are not reserved until three days from
today\'s date (two days before the scheduled delivery date).

{.align-center}

In the `Operations`{.interpreted-text role="guilabel"} tab on the
`Product`{.interpreted-text role="guilabel"} line, the numbers in the
`Demand`{.interpreted-text role="guilabel"} column and the
`Quantity`{.interpreted-text role="guilabel"} column do not match (in
this case, the `Demand`{.interpreted-text role="guilabel"} column lists
[10.00]{.title-ref}, while the `Quantity`{.interpreted-text
role="guilabel"} column lists [0]{.title-ref}).

The `Quantity`{.interpreted-text role="guilabel"} column lists
[0]{.title-ref} because the products aren\'t reserved until two days
*before* their delivery date. Odoo automatically reserves the products
once the scheduled date arrives, at which point the
`Demand`{.interpreted-text role="guilabel"} and
`Quantity`{.interpreted-text role="guilabel"} columns will match.

::: {.tip}
::: {.title}
Tip
:::

If the products in the `SO (Sales Order)`{.interpreted-text role="abbr"}
should be reserved *sooner* than the scheduled reservation date, the
reservation can be manually overridden. To manually reserve the products
sooner than scheduled, click `Check Availability`{.interpreted-text
role="guilabel"} at the top of the form.

This turns the [Available]{.title-ref} status in the
`Product Availability`{.interpreted-text role="guilabel"} field green,
and changes the number in the `Quantity`{.interpreted-text
role="guilabel"} column to match the `Demand`{.interpreted-text
role="guilabel"} column.

Once ready, click `Validate`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
\- `Manual reservation <manually>`{.interpreted-text role="doc"} -
`At confirmation reservation <at_confirmation>`{.interpreted-text
role="doc"}
:::
