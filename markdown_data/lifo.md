# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/lifo.md

LIFO removal
============

The *Last In, First Out* (LIFO) removal strategy picks the **newest**
products on-hand, based on the date they entered a warehouse\'s stock.

Every time an order is placed for products using the
`LIFO (Last In, First Out)`{.interpreted-text role="abbr"} strategy, a
transfer is created for the lot/serial number that has most recently
entered the stock (the **last** lot/serial number that entered the
warehouse\'s inventory).

::: {.seealso}
`About removal strategies <../removal_strategies>`{.interpreted-text
role="doc"}
:::

::: {.warning}
::: {.title}
Warning
:::

In many countries, the `LIFO (Last In, First Out)`{.interpreted-text
role="abbr"} removal strategy is banned, since it can potentially result
in old, expired, or obsolete products being delivered to customers.
:::

Consider the following example, with the product, [Cinder
Block]{.title-ref}, which is tracked `By
Lots`{.interpreted-text role="guilabel"} in the
`Inventory`{.interpreted-text role="guilabel"} tab of the product form.
The `Force Removal Strategy`{.interpreted-text role="guilabel"} for the
cinder block\'s product category is set to
`Last In, First Out (LIFO)`{.interpreted-text role="guilabel"}.

::: {.seealso}
\-
`Set up force removal strategy <inventory/warehouses_storage/removal-config>`{.interpreted-text
role="ref"} -
`Enable lots tracking <inventory/warehouses_storage/lots-setup>`{.interpreted-text
role="ref"} -
`Check arrival date <inventory/warehouses_storage/arrival_date>`{.interpreted-text
role="ref"}
:::

The following table represents the cinder blocks in stock, and their
various lot number details.

                                                                                           LOT1     LOT2     LOT3
  ---------------------------------------------------------------------------------------- -------- -------- --------
  On-hand stock                                                                            10       10       10
  `Created on <inventory/warehouses_storage/arrival_date>`{.interpreted-text role="ref"}   June 1   June 3   June 6

To see the removal strategy in action, create a
`delivery order <inventory/delivery/one-step>`{.interpreted-text
role="ref"} for seven cinder blocks by navigating to the
`Sales app`{.interpreted-text role="menuselection"} and creating a new
quotation.

`Confirm`{.interpreted-text role="guilabel"} the sales order to create a
delivery order. Doing so reserves the newest lot numbers are using the
`LIFO (Last In, First Out)`{.interpreted-text role="abbr"} removal
strategy.

To view the detailed pickings, click the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon, located on
the far-right of the cinder block\'s product line in the
`Operations`{.interpreted-text role="guilabel"} tab of the delivery
order. Doing so opens the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window.

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, the `Pick from`{.interpreted-text role="guilabel"} field
displays where the quantities to fulfill the `Demand`{.interpreted-text
role="guilabel"} are picked from. Since the order demanded seven cinder
blocks, the newest cinder blocks from [LOT3]{.title-ref} are selected,
using the `LIFO (Last In,
First Out)`{.interpreted-text role="abbr"} removal strategy.

{.align-center}
