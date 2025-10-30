# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/aging.md

Inventory aging report
======================

The inventory aging report evaluates all items in stock, providing
insights into potentially sunken purchase costs and delays in
profitability.

Create customized pivot tables to analyze product, operation types,
month, or company breakdowns. This helps identify products in stock that
are at risk of passing their expiration or viability dates, or instances
of rot/decay for fast-expiring items.

::: {.note}
::: {.title}
Note
:::

The *Reporting* menu in *Inventory* is only accessible to users with
`admin access
<../../../../general/users/access_rights>`{.interpreted-text
role="doc"}.
:::

To access the inventory aging report, go to
`Inventory app --> Reporting -->
Inventory Aging`{.interpreted-text role="menuselection"}.

Navigate the inventory aging report {#inventory/warehouses_storage/aging-report}
-----------------------------------

By default, the `Inventory Aging`{.interpreted-text role="guilabel"}
report displays a pivot table, with the month in columns, and product
category in rows. The default filters, `Incoming`{.interpreted-text
role="guilabel"} and `Has
Remaining Qty`{.interpreted-text role="guilabel"}, show only products
from receipts, and are currently in stock.

`Remaining Qty`{.interpreted-text role="guilabel"} displays the number
of on-hand items, and `Remaining Value`{.interpreted-text
role="guilabel"} displays the total cost of purchasing these items.

Clicking the `fa-plus-square`{.interpreted-text role="icon"}
`(plus)`{.interpreted-text role="guilabel"} icon in each column or row
reveals options to expand the pivot table and show a detailed breakdown
of the `Remaining Qty`{.interpreted-text role="guilabel"} and
`Remaining Value`{.interpreted-text role="guilabel"} by
`Product`{.interpreted-text role="guilabel"},
`Product Category`{.interpreted-text role="guilabel"},
`Date`{.interpreted-text role="guilabel"}, or
`Company`{.interpreted-text role="guilabel"}. Clicking the
`fa-minus-square-o`{.interpreted-text role="icon"}
`(minus)`{.interpreted-text role="guilabel"} icon collapses it back to
its previous state.

![Inventory aging report, showing each **Product** in rows and each
reception **Date** in columns, to better monitor products with fast
expiration dates. Each row shows the the total on-hand quantity and
inventory valuation of items purchased on each
day.](aging/inventory-aging.png){.align-center}

::: {.note}
::: {.title}
Note
:::

Records in the `Inventory Aging`{.interpreted-text role="guilabel"}
report are *stock valuation layers* (SVLs), representing product moves
that impact stock valuation.

Inventory adjustments do **not** create
`SVLs (stock valuation layers)`{.interpreted-text role="abbr"}; only
items purchased from vendors do.
:::

Generate reports
----------------

After learning how to `navigate the inventory aging report
<inventory/warehouses_storage/aging-report>`{.interpreted-text
role="ref"}, it can be used to create and share different reports.

A few common reports that can be created using the
`Inventory Aging`{.interpreted-text role="guilabel"} report are detailed
below.

### Rotating stock report

To create a report to identify items that have been in stock for a
while, follow these steps:

1.  Navigate to
    `Inventory app --> Reporting --> Inventory Aging`{.interpreted-text
    role="menuselection"}.

2.  On the `Inventory Aging`{.interpreted-text role="guilabel"} report,
    click the `fa-caret-down`{.interpreted-text role="icon"} `(caret
    down)`{.interpreted-text role="guilabel"} icon in the
    `Search...`{.interpreted-text role="guilabel"} bar to see a
    drop-down list of `Filters`{.interpreted-text role="guilabel"},
    `Group By`{.interpreted-text role="guilabel"}, and
    `Favorite`{.interpreted-text role="guilabel"} options.

3.  Choose `Product`{.interpreted-text role="guilabel"} under the
    `Group By`{.interpreted-text role="guilabel"} section. Doing so
    expands the pivot table to show a product in each row.

4.  Click the `fa-plus-square`{.interpreted-text role="icon"}
    `(plus)`{.interpreted-text role="guilabel"} icon to the left of the
    date column. Hover over `Date`{.interpreted-text role="guilabel"}
    from the drop-down menu and choose `Year`{.interpreted-text
    role="guilabel"}, `Quarter`{.interpreted-text role="guilabel"},
    `Month`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, or `Day`{.interpreted-text role="guilabel"}. Doing
    so expands the columns to show the `Remaining Qty`{.interpreted-text
    role="guilabel"} and `Remaining Value`{.interpreted-text
    role="guilabel"} by the selected time period.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    For products that have a longer shelf life, choose longer time
    periods such as `Month`{.interpreted-text role="guilabel"} or
    `Quarter`{.interpreted-text role="guilabel"} when expanding columns
    by `Date`{.interpreted-text role="guilabel"}.
    :::

    {.align-center}

5.  The report now displays the on-hand stock of items, and their total
    purchasing cost, for each time period.

    ::: {.example}
    Inventory aging report, with the `Group By`{.interpreted-text
    role="guilabel"}: `Product`{.interpreted-text role="guilabel"}
    option selected, and with the `Date`{.interpreted-text
    role="guilabel"} column set to `Day`{.interpreted-text
    role="guilabel"}. It gives insight into how much raw fish sashimi
    products were purchased on each day, and how much it cost. This
    informs the business owners how much stock is at risk of rotting in
    stock, per day.

    {.align-center}
    :::
