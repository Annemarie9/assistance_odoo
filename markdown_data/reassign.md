# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/product_tracking/reassign.md

Reassign lot/serial numbers
===========================

Changing a product\'s tracking settings to use lots or serial numbers,
*after* storing products in Odoo without them, can lead to inconsistent
records. Follow this documentation to learn how to use an inventory
adjustment to assign lot or serial numbers to products that were not
originally assigned lots.

{.align-center}

::: {.note}
::: {.title}
Note
:::

This document outlines the process of using two inventory adjustments:
one to remove incorrect records *without* lot numbers, and another to
save the quantities *with* the lot numbers.
:::

::: {.seealso}
\- `Set up and use lot numbers <lots>`{.interpreted-text role="doc"} -
`Set up serial numbers <create_sn>`{.interpreted-text role="doc"} -
`Use serial numbers <serial_numbers>`{.interpreted-text role="doc"}
:::

Change on-hand quantity to zero
-------------------------------

To change the product\'s settings to track by lots or serial numbers,
begin by navigating to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select the intended product.

Next, click the product\'s `On Hand`{.interpreted-text role="guilabel"}
smart button to open the `Update Quantity`{.interpreted-text
role="guilabel"} page. In the `On Hand Quantity`{.interpreted-text
role="guilabel"} column, change the value to zero.

::: {.note}
::: {.title}
Note
:::

If the product is stored in multiple locations, make sure the **total**
on hand quantity at **all** locations is zero.
:::

{.align-center}

Change traceability setting
---------------------------

Return to the product form
(`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}), and switch to the `Inventory`{.interpreted-text
role="guilabel"} tab. In the `Traceability`{.interpreted-text
role="guilabel"} section, change the `Tracking`{.interpreted-text
role="guilabel"} option from `No Tracking`{.interpreted-text
role="guilabel"} to `By Lots`{.interpreted-text role="guilabel"} or `By
Unique Serial Number`{.interpreted-text role="guilabel"}.

::: {.seealso}
`expiration_dates`{.interpreted-text role="doc"}
:::

{.align-center}

Restore on-hand quantity
------------------------

After manually changing the on-hand quantity to zero and changing the
`Tracking`{.interpreted-text role="guilabel"} setting to lots or serial
numbers, restore the quantities by clicking the
`On Hand`{.interpreted-text role="guilabel"} smart button from the
desired product form.

On the `Update Quantity`{.interpreted-text role="guilabel"} page,
because the on-hand quantity had been previously changed to zero, a
`No Stock On Hand`{.interpreted-text role="guilabel"} warning appears on
the page. From here, click the `New`{.interpreted-text role="guilabel"}
button in the top-left corner. Doing so reveals a new, modifiable line
on the `Update Quantity`{.interpreted-text role="guilabel"} page. Then,
input a desired lot number in the `Lot/Serial
Number`{.interpreted-text role="guilabel"} field, and adjust the
`On Hand Quantity`{.interpreted-text role="guilabel"} to its original
value.

::: {.seealso}
`../../warehouses_storage/inventory_management/count_products`{.interpreted-text
role="doc"}
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To find the original quantity, and adjust the
`On Hand Quantity`{.interpreted-text role="guilabel"} accordingly, after
assigning a new lot or serial number, click the
`fa-pencil`{.interpreted-text role="icon"} `(pencil)`{.interpreted-text
role="guilabel"} icon in the `On Hand Quantity`{.interpreted-text
role="guilabel"} column. Then, click the `fa-history`{.interpreted-text
role="icon"} `History`{.interpreted-text role="guilabel"} button on the
far-right.

{.align-center}

The inventory adjustment that changed the on-hand quantity to zero is
displayed in the `Quantity`{.interpreted-text role="guilabel"} field.

> {.align-center}
:::
