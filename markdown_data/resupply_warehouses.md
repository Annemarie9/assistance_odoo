# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses.md

Inter-warehouse replenishment
=============================

When a business operates multiple locations, such as warehouses, retail
shops, or manufacturing facilities, resupplying stock from a central
warehouse is sometimes necessary. Odoo uses a *Route* configuration that
enables locations to replenish from a central distribution center,
automatically generating *inter-warehouse transfers*. Odoo
`Inventory`{.interpreted-text role="guilabel"} manages these transfers
to keep stores in stock.

This guide explains how to conduct inter-warehouse transfers using two
replenishment strategies:

1.  `Make to order (MTO) <inventory/warehouses_storage/MTO>`{.interpreted-text
    role="ref"}
2.  `Reordering rule <inventory/warehouses_storage/reordering-rule>`{.interpreted-text
    role="ref"}

::: {.seealso}
`Difference between MTO and reordering rules <../replenishment>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

The initial configuration for both replenishment strategies is the same.
First go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Warehouse`{.interpreted-text
role="guilabel"} section, activate `Storage Locations`{.interpreted-text
role="guilabel"}. Then, click `Save`{.interpreted-text role="guilabel"}
to apply the setting.

{.align-center}

### Warehouses

Configure the settings for the central warehouse and connecting storage
locations by going to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}.

::: {.important}
::: {.title}
Important
:::

Each central warehouse and other locations *must* have its own
warehouse. For example, each shop is considered a local warehouse.
:::

Select an existing warehouse, or create a new one to be resupplied from
the central warehouse, by clicking `New`{.interpreted-text
role="guilabel"}. Then, give the warehouse a name and a
`Short Name`{.interpreted-text role="guilabel"}, which will appear on
that warehouse\'s transfers.

In the `Warehouse Configuration`{.interpreted-text role="guilabel"} tab,
locate the `Resupply From`{.interpreted-text role="guilabel"} field.
Check the box next to the central warehouse\'s name. If the warehouse
can be resupplied by more than one warehouse, make sure to check those
warehouses\' boxes too. Now, Odoo knows which warehouses can resupply
this warehouse.

::: {.example}
The central warehouse that will supply the shops is called [Central
warehouse]{.title-ref}. The `Resupply From`{.interpreted-text
role="guilabel"} field is set to this warehouse on the shop\'s warehouse
configuration page.
:::

::: {.seealso}
`../inventory_management/warehouses`{.interpreted-text role="doc"}
:::

{.align-center}

### Set route on a product

Products must also be configured properly in order for them to be
transferred between warehouses.

Go to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"} and select the desired product.

In the `Inventory`{.interpreted-text role="guilabel"} tab, the new route
appears as `X: Supply Product from Y`{.interpreted-text role="guilabel"}
in the `Routes`{.interpreted-text role="guilabel"} section, where \'X\'
is the store\'s warehouse that receives products, and \'Y\' is the
warehouse that sends products.

Tick the `X: Supply Product from Y`{.interpreted-text role="guilabel"}
checkbox, which is intended to be used with the
`MTO (Make to Order)`{.interpreted-text role="abbr"} route or a
reordering rule to replenish stock by moving the product from one
warehouse to another. Proceed to the dedicated sections below to
continue the process.

#### MTO {#inventory/warehouses_storage/MTO}

To replenish products using the make-to-order method, go to the product
form and ensure the
`MTO route is unarchived <inventory/warehouses_storage/unarchive-mto>`{.interpreted-text
role="ref"}, so it appears in the `Routes`{.interpreted-text
role="guilabel"} section of the `Inventory`{.interpreted-text
role="guilabel"} tab.

With the resupply and `MTO (Make to Order)`{.interpreted-text
role="abbr"} routes ticked, jump to the section titled:
`Replenish from another
warehouse <inventory/warehouses_storage/resupply-workflow>`{.interpreted-text
role="ref"}.

::: {.example}
The product, sold at the warehouse, [Store]{.title-ref}, is resupplied
from the central warehouse, named [YourCompany]{.title-ref}. To
replenish the product using `MTO (Make to Order)`{.interpreted-text
role="abbr"}, the following routes are selected:

-   `Store: Supply Product from YourCompany`{.interpreted-text
    role="guilabel"}
-   `Replenish on Order (MTO)`{.interpreted-text role="guilabel"}

{.align-center}
:::

#### Reordering rule {#inventory/warehouses_storage/reordering-rule}

To replenish products using reordering rules, first ensure the
`X: Supply Product from Y`{.interpreted-text role="guilabel"} route is
selected in the `Inventory`{.interpreted-text role="guilabel"} tab of
the product form.

Then, create a reordering rule to automate replenishment by clicking the
`Reordering
Rules`{.interpreted-text role="guilabel"} smart button.

Click `New`{.interpreted-text role="guilabel"}, and set:

-   `Location`{.interpreted-text role="guilabel"}: the stock location of
    the retail store. For example, [SHOP/Stock]{.title-ref}.
-   `Route`{.interpreted-text role="guilabel"}:
    `X: Supply Product from Y`{.interpreted-text role="guilabel"}.
-   `Min Quantity`{.interpreted-text role="guilabel"} and
    `Max Quantity`{.interpreted-text role="guilabel"} to trigger
    automatic stock transfers when inventory falls below the set
    threshold.

::: {.seealso}
`reordering_rules`{.interpreted-text role="doc"}
:::

::: {.example}
A
`0/0 reordering rule <inventory/warehouses_storage/zero-zero>`{.interpreted-text
role="ref"} to replenish the shop\'s warehouse is created, with the
`Location`{.interpreted-text role="guilabel"} set to
[SHOP/Stock]{.title-ref}, and the `Route`{.interpreted-text
role="guilabel"} set to
`Store: Resupply from YourCompany`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Replenish one warehouse from another {#inventory/warehouses_storage/resupply-workflow}
------------------------------------

After completing the setup, trigger replenishment using one of several
methods, such as:

-   Navigate to the product form of the product that is resupplied from
    another warehouse.

    Click the `Replenish`{.interpreted-text role="guilabel"} button on
    the top-left of the product page. In the pop-up window, set the
    warehouse to the retail shop, (e.g. [Store]{.title-ref}), and click
    `Confirm`{.interpreted-text role="guilabel"}.

    {.align-center}

-   Create a quotation, and in the `Other Info`{.interpreted-text
    role="guilabel"} tab, set the `Warehouse`{.interpreted-text
    role="guilabel"} to the retail shop (e.g. [Store]{.title-ref}), when
    selling the product makes the on-hand quantity of the product go
    below the minimum set on the reordering rule.

    {.align-center}

Once triggered, Odoo creates two transfers: One is a *delivery order*
from the central, supplying warehouse, which contains all the necessary
products to the store, and the second is a *receipt* at the shop, from
the main warehouse.

While in transit, the product is located at [Physical
Locations/Inter-warehouse transit]{.title-ref}.

::: {.example}
A sales order for the product at the shop is created. To replenish the
product at the shop and ship it from there, Odoo generates a delivery
order from the central warehouse\'s stock, [WH/Stock]{.title-ref} to the
shop\'s warehouse [SHOP/Stock]{.title-ref}. While the products are
traveling between warehouses, they are in [Physical
Locations/Inter-warehouse transit]{.title-ref}.

The final delivery order is from the shop to the customer\'s delivery
address, and is not pertinent to the workflow in this guide.


:::
