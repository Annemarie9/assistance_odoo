# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/fefo.md

FEFO removal
============

The *First Expired, First Out* (FEFO) removal strategy targets products
for removal based on their assigned removal dates.

::: {.seealso}
`About removal strategies <../removal_strategies>`{.interpreted-text
role="doc"}
:::

Removal date {#inventory/warehouses_storage/removal-date}
------------

Products **must** be removed from inventory before their *removal date*,
which is set as a certain number of days before the product\'s
*expiration date*.

The user sets this number of days by navigating to the product form\'s
`Inventory`{.interpreted-text role="guilabel"} tab. Under the
`Traceability`{.interpreted-text role="guilabel"} section, ensure the
`Tracking`{.interpreted-text role="guilabel"} field is set to either
`By Lots`{.interpreted-text role="guilabel"} or
`By Unique Serial Number`{.interpreted-text role="guilabel"}.

Next, select the `Expiration Date`{.interpreted-text role="guilabel"}
option, which makes the `Removal Date`{.interpreted-text
role="guilabel"} field (and other date fields) appear.

::: {.important}
::: {.title}
Important
:::

The `Lots and Serial Numbers`{.interpreted-text role="guilabel"} and
`Expiration Dates`{.interpreted-text role="guilabel"} features **must**
be enabled in
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"} to track expiration dates.
:::

The expiration date of a product is determined by adding the date the
product was received to the number of days specified in the
`Expiration Date`{.interpreted-text role="guilabel"} field of the
product form.

The removal date takes this expiration date, and subtracts the number of
days specified in the `Removal Date`{.interpreted-text role="guilabel"}
field of the product form.

::: {.seealso}
`Expiration dates <../../product_management/product_tracking/expiration_dates>`{.interpreted-text
role="doc"}
:::

::: {.example}
In the `Inventory`{.interpreted-text role="guilabel"} tab of the
product, [Egg]{.title-ref}, the following `Dates`{.interpreted-text
role="guilabel"} are set by the user:

-   `Expiration Date`{.interpreted-text role="guilabel"}:
    [30]{.title-ref} days after receipt
-   `Removal Date`{.interpreted-text role="guilabel"}: [15]{.title-ref}
    days before expiration date

{.align-center}

A shipment of Eggs arrive at the warehouse on January 1st. So, the
expiration date of the Eggs is **January 31st** (Jan 1st + 30). By
extension, the removal date is **January 16th** (Jan 31 -15).
:::

::: {#inventory/warehouses_storage/exp-date}
To view the expiration dates of items in stock, navigate to the product
form, and click the `On Hand`{.interpreted-text role="guilabel"} smart
button.
:::

Next, click the additional options icon, located on the far-right, and
select the columns: `Expiration Date`{.interpreted-text role="guilabel"}
and `Removal Date`{.interpreted-text role="guilabel"}.

![Show expiration dates from the inventory adjustments model accessed from the \*On Hand\*
smart button from the product form.](fefo/removal-date.png){.align-center}

Workflow
--------

Using the `FEFO (First Expired, First Out)`{.interpreted-text
role="abbr"} removal strategy ensures that products with the nearest
removal date are picked first.

To understand how this removal strategy works, consider the following
example below about the product, [Carton of eggs]{.title-ref}, which is
a box containing twelve eggs.

The product is tracked `By Lots`{.interpreted-text role="guilabel"}, and
the product category\'s `Force Removal
Strategy`{.interpreted-text role="guilabel"} is set to
`First Expired, First Out (FEFO)`{.interpreted-text role="guilabel"}.

::: {.seealso}
\-
`Set up force removal strategy <inventory/warehouses_storage/removal-config>`{.interpreted-text
role="ref"} -
`Enable lots tracking <inventory/warehouses_storage/lots-setup>`{.interpreted-text
role="ref"} - [Odoo Tutorials: Perishable
Products](https://www.odoo.com/slides/slide/5324/share)
:::

                                                                                         LOT1          LOT2       LOT3
  -------------------------------------------------------------------------------------- ------------- ---------- ----------
  On-hand stock                                                                          5             2          1
  Expiration date                                                                        April 4       April 10   April 15
  `Removal date <inventory/warehouses_storage/exp-date>`{.interpreted-text role="ref"}   February 26   March 4    March 9

To see the removal strategy in action, go to the
`Sales app`{.interpreted-text role="menuselection"} and create a new
quotation.

Clicking `Confirm`{.interpreted-text role="guilabel"} creates a delivery
order for today, December 29th, and the lot numbers with the soonest
expiration dates are reserved, using the
`FEFO (First Expired, First Out)`{.interpreted-text role="abbr"} removal
strategy.

To view the detailed pickings, click the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon, located on
the far-right of the Carton of egg\'s product line, in the
`Operations`{.interpreted-text role="guilabel"} tab of the delivery
order. Doing so opens the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window.

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, the `Pick from`{.interpreted-text role="guilabel"} field
displays where the quantities to fulfill the `Demand`{.interpreted-text
role="guilabel"} are picked from.

Since the order demanded six Cartons of eggs, using the
`FEFO (First Expired, First Out)`{.interpreted-text role="abbr"} removal
strategy, all five Cartons from [LOT1]{.title-ref}, with the removal
date of February 26th, are picked. The remaining Carton is selected from
[LOT2]{.title-ref}, which has a removal date of March 4th.

{.align-center}
