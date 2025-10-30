# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/fifo.md

FIFO removal
============

The *First In, First Out* (FIFO) removal strategy selects products with
the earliest arrival dates. This method is useful for companies selling
products that have short demand cycles, like clothes, for example. By
using `FIFO (First In, First Out)`{.interpreted-text role="abbr"},
companies can prevent prolonged stock retention of specific styles.

::: {.seealso}
`About removal strategies <../removal_strategies>`{.interpreted-text
role="doc"}
:::

::: {.example}
Various quantities of the product, [T-shirt]{.title-ref}, tracked by lot
numbers, arrive on August 1st and August 25th. For an order made on
September 1st, the `FIFO (First In, First Out)`{.interpreted-text
role="abbr"} removal strategy prioritizes lots that have been in stock
the longest. So, products received on August 1st are selected first for
picking.

{.align-center}
:::

::: {.seealso}
`Lot/serial number setup details <inventory/warehouses_storage/lots-setup>`{.interpreted-text
role="ref"}
:::

Arrival date {#inventory/warehouses_storage/arrival_date}
------------

To see the product lot or serial number that arrived in inventory first,
navigate to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}.

Then, select the `▶️ (right-pointing arrow)`{.interpreted-text
role="guilabel"} icon on the left of a product line, in order to reveal
a list of the product\'s lots or serial numbers that are in stock. The
`Created
On`{.interpreted-text role="guilabel"} field shows the lot/serial number
creation date, which is, essentially, the arrival date.

::: {.example}
Serial number [00000000500]{.title-ref} of the product, [Cabinet with
Doors]{.title-ref}, arrived on December 29th, as displayed in the
`Created On`{.interpreted-text role="guilabel"} field.

{.align-center}
:::

Workflow
--------

To understand how `FIFO (First In, First Out)`{.interpreted-text
role="abbr"} rotates products out, consider the following example,
focusing on three lots of white shirts.

The shirts are from the *All/Clothes* category, where
`FIFO (First In, First Out)`{.interpreted-text role="abbr"} is set as
the `Force Removal Strategy`{.interpreted-text role="guilabel"}.

The white shirts are tracked `By Lots`{.interpreted-text
role="guilabel"} in the `Inventory`{.interpreted-text role="guilabel"}
tab of the product form.

::: {.seealso}
\-
`Set up force removal strategy <inventory/warehouses_storage/removal-config>`{.interpreted-text
role="ref"} -
`Enable lots tracking <inventory/warehouses_storage/lots-setup>`{.interpreted-text
role="ref"}
:::

The following table represents the on-hand stock and lot number details
of white shirts.

                                                                                           LOT1      LOT2      LOT3
  ---------------------------------------------------------------------------------------- --------- --------- -------
  On-hand stock                                                                            5         3         2
  `Created on <inventory/warehouses_storage/arrival_date>`{.interpreted-text role="ref"}   March 1   April 1   May 1

To see the removal strategy in action, create a
`delivery order <inventory/delivery/one-step>`{.interpreted-text
role="ref"} for six white shirts by navigating to the
`Sales app`{.interpreted-text role="menuselection"} and creating a new
quotation.

After clicking `Confirm`{.interpreted-text role="guilabel"} on the sales
order, a delivery order with the oldest lot numbers for shirts are
reserved, using the `FIFO (First In, First Out)`{.interpreted-text
role="abbr"} removal strategy.

To view the detailed pickings, click the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon, located on
the far-right of the white shirt\'s product line in the
`Operations`{.interpreted-text role="guilabel"} tab of the delivery
order. Doing so opens the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window.

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, the `Pick from`{.interpreted-text role="guilabel"} field
displays where the quantities to fulfill the `Demand`{.interpreted-text
role="guilabel"} are picked from. Since the order demanded six shirts,
all five shirts from [LOT1]{.title-ref}, and one shirt from
[LOT2]{.title-ref}, are selected.

{.align-center}
