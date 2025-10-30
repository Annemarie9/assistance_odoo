# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/locations.md

Locations dashboard
===================

The *Locations* dashboard in the *Inventory* application provides an
overview of on-hand storage locations for company products. Use this
report to see where stock is stored, identify
`misplaced items <inventory/warehouse_storage/stranded>`{.interpreted-text
role="ref"}, or view past inventory to see product locations on specific
dates.

::: {.note}
::: {.title}
Note
:::

The *Reporting* menu in *Inventory* is only accessible to users with
`admin access
<../../../../general/users/access_rights>`{.interpreted-text
role="doc"}.
:::

To access the locations report, the *Storage Locations* feature must be
enabled. To do that, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Warehouse`{.interpreted-text
role="guilabel"} section, tick the checkbox for
`Storage Locations`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}. Then, access the locations
dashboard by navigating to
`Inventory app --> Reporting --> Locations`{.interpreted-text
role="menuselection"}.

Navigate the locations dashboard {#inventory/warehouses_storage/locations-report}
--------------------------------

By default, the `Locations`{.interpreted-text role="guilabel"} dashboard
lists all on-hand products in stock (in the `Product`{.interpreted-text
role="guilabel"} column), along with the following information:

-   `Location`{.interpreted-text role="guilabel"}: current storage
    location. If a product is stored at [Shelf 1]{.title-ref} and [Shelf
    2]{.title-ref}, the product is listed twice, showing quantities at
    each location.
-   `Package`{.interpreted-text role="guilabel"}: the package that the
    product is stored in, if any.
-   `Lot/Serial Number`{.interpreted-text role="guilabel"}: if the
    product has a lot or serial number, it is specified here.
-   `On Hand Quantity`{.interpreted-text role="guilabel"}: current
    quantity of products. Click the `fa-pencil`{.interpreted-text
    role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon to
    `modify the on-hand quantity
    <../inventory_management/count_products>`{.interpreted-text
    role="doc"}.
-   `Reserved Quantity`{.interpreted-text role="guilabel"}: on-hand
    quantity reserved for operations, such as pickings, delivery orders,
    or manufacturings.
-   `Unit`{.interpreted-text role="guilabel"}: the unit of measure of
    the product.

Click the buttons to the right of each row item to access additional
information:

-   `fa-history`{.interpreted-text role="icon"}
    `History`{.interpreted-text role="guilabel"}: access the stock move
    history of the product, displaying information about the quantity
    and description of why the product was moved from one location to
    another.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    View what the product is reserved for, by clicking the
    `fa-history`{.interpreted-text role="icon"}
    `History`{.interpreted-text role="guilabel"} button on the far-right
    of the product line.

    On the `Moves History`{.interpreted-text role="guilabel"} page,
    remove the `fa-filter`{.interpreted-text role="icon"}
    `Done`{.interpreted-text role="guilabel"} filter. Then, click the
    `fa-caret-down`{.interpreted-text role="icon"}
    `(caret down)`{.interpreted-text role="guilabel"} icon to the right
    of the `Search...`{.interpreted-text role="guilabel"} bar to reveal
    filter options, and select the `To Do`{.interpreted-text
    role="guilabel"} filter.

    {.align-center}
    :::

-   `fa-refresh`{.interpreted-text role="icon"}
    `Replenishment`{.interpreted-text role="guilabel"}: access the
    `reordering rules
    <../replenishment/reordering_rules>`{.interpreted-text role="doc"}
    page to replenish products at the specific location.

In the upper-left corner of the page, click the the
`New`{.interpreted-text role="guilabel"} button to make an
`inventory adjustment <../inventory_management/count_products>`{.interpreted-text
role="doc"} to record quantities of a certain product at a specific
`Location`{.interpreted-text role="guilabel"}.

To view products, quantities, and their locations for a specified date,
click the `Inventory At Date`{.interpreted-text role="guilabel"} button
(also located in the upper-left corner of the page). Select a date and
time in the `Inventory at Date`{.interpreted-text role="guilabel"}
field, then click `Confirm`{.interpreted-text role="guilabel"}.

Generate reports
----------------

After learning how to `navigate the locations dashboard
<inventory/warehouses_storage/locations-report>`{.interpreted-text
role="ref"}, it can be used to create and share different reports.

A few common reports that can be created using the
`Locations`{.interpreted-text role="guilabel"} dashboard are detailed
below.

### Dead stock report

To get list of expired items, also referred to as *dead stock*, follow
these steps:

1.  Go to `Inventory app --> Reporting --> Locations`{.interpreted-text
    role="menuselection"}.
2.  Then, click the `fa-caret-down`{.interpreted-text role="icon"}
    `(caret down)`{.interpreted-text role="guilabel"} icon to the right
    of the `Search...`{.interpreted-text role="guilabel"} bar to reveal
    a drop-down list of `Filters`{.interpreted-text role="guilabel"},
    `Group By`{.interpreted-text role="guilabel"}, and
    `Favorite`{.interpreted-text role="guilabel"} options.
3.  Enable the `Internal Locations`{.interpreted-text role="guilabel"}
    and `Expiration Alerts`{.interpreted-text role="guilabel"} option
    under the `Filters`{.interpreted-text role="guilabel"} section.

The report now displays a list of expired products.

::: {.note}
::: {.title}
Note
:::

This report can also be generated from the `Lot and Serials Numbers
<inventory/product_management/expiration-alerts>`{.interpreted-text
role="ref"} page, accessed by going to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}.
:::

{.align-center}

### Stranded inventory report {#inventory/warehouse_storage/stranded}

Businesses using multi-step flows in the *Inventory* or *Manufacturing*
apps, may have *stranded* items, which are products not in their proper
storage locations, due to human error. Use this report to periodically
check transfer locations (e.g. *WH/Input*, *WH/Pre-Processing*) to
ensure items are moved to their intended storage locations, and
accurately recorded in the database.

To get a list of items that might be sitting idly in storage, follow
these steps:

1.  Go to `Inventory app --> Reporting --> Locations`{.interpreted-text
    role="menuselection"}.

2.  In the `Search...`{.interpreted-text role="guilabel"} bar, begin
    typing the name of the location where products are intended to be
    moved to, such as [WH/Input]{.title-ref}, or
    [WH/Packing]{.title-ref}.

3.  Select the `Search Location for:`{.interpreted-text role="guilabel"}
    \[location name\] option from the resulting drop-down menu that
    appears beneath the `Search...`{.interpreted-text role="guilabel"}
    bar.

    {.align-center}

The report now displays a list of products at the transit location.

::: {.example}
Searching [Input]{.title-ref} in `Location`{.interpreted-text
role="guilabel"} shows a list of products at a *WH/Input* location.

The list shows [500]{.title-ref} quantities of [Chicken]{.title-ref},
which is alarming if not refrigerated soon after reception. The stranded
inventory report helps identify items that have been idling in
non-storage locations.

{.align-center}
:::

### Inventory discrepancy report

To generate a report of items that have been moved since the last
`inventory audit
<../inventory_management/cycle_counts>`{.interpreted-text role="doc"},
follow these steps:

1.  Go to `Inventory app --> Reporting --> Locations`{.interpreted-text
    role="menuselection"}.

2.  Then, click the `fa-caret-down`{.interpreted-text role="icon"}
    `(caret down)`{.interpreted-text role="guilabel"} icon to the right
    of the `Search...`{.interpreted-text role="guilabel"} bar to reveal
    a drop-down list of `Filters`{.interpreted-text role="guilabel"},
    `Group By`{.interpreted-text role="guilabel"}, and
    `Favorite`{.interpreted-text role="guilabel"} options.

3.  Enable the `Internal Locations`{.interpreted-text role="guilabel"}
    and `Conflicts`{.interpreted-text role="guilabel"} option from the
    `Filters`{.interpreted-text role="guilabel"} section.

4.  The report now displays items whose quantities have changed since
    the last cycle count.

    {.align-center}

5.  Click the `fa-history`{.interpreted-text role="icon"}
    `History`{.interpreted-text role="guilabel"} button to view
    inventory transfers, including receipts and deliveries, that have
    occurred since the inventory adjustment.

    {.align-center}
