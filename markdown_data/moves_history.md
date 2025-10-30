# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/moves_history.md

Moves history dashboard
=======================

The *Moves History* report in Odoo *Inventory* provides a detailed
record of product movements (containing past and current locations), lot
numbers, and reasons for movement. Reports can be generated for any time
frame, making this report essential for analyzing stock levels,
monitoring inventory turnover, and identifying any discrepancies in
inventory.

::: {.note}
::: {.title}
Note
:::

The reporting feature is only accessible to users with `admin access
<../../../../general/users/access_rights>`{.interpreted-text
role="doc"}.
:::

To access the stock report, go to
`Inventory app --> Reporting --> Moves History`{.interpreted-text
role="menuselection"}.

{.align-center}

Navigate the moves history report {#inventory/warehouses_storage/moves-history-report}
---------------------------------

In the report, the columns represent:

-   `Date`{.interpreted-text role="guilabel"}: calendar date and time of
    the stock move.
-   `Reference`{.interpreted-text role="guilabel"}: description of the
    reason for the stock move or quantity change, such as a receipt
    number (e.g. [WH/IN/00012]{.title-ref}).
-   `Product`{.interpreted-text role="guilabel"}: name of the product
    involved in the move.
-   `Lot/Serial Number`{.interpreted-text role="guilabel"}: specifies
    the lot or serial number of the tracked product being moved.
-   `From`{.interpreted-text role="guilabel"}: source location of the
    moved product.
-   `To`{.interpreted-text role="guilabel"}: destination location of the
    moved product.
-   `Quantity`{.interpreted-text role="guilabel"}: number of products
    moved.
-   `Unit`{.interpreted-text role="guilabel"}: unit of measure of the
    products moved.
-   `Status`{.interpreted-text role="guilabel"}: indicates the move
    status, which can be `Done`{.interpreted-text role="guilabel"},
    `Available`{.interpreted-text role="guilabel"} (ready for action),
    or `Partially Available`{.interpreted-text role="guilabel"}
    (insufficient quantities to complete the operation).

### Search options

Use the following search options to customize the
`Moves History`{.interpreted-text role="guilabel"} report to display
relevant information

::: {.tabs}
::: {.tab}
Filters

The `Filters`{.interpreted-text role="guilabel"} section allows users to
search among pre-made and custom filters to find specific stock records.

-   `To Do`{.interpreted-text role="guilabel"}: show stock move records
    that are in progress. This includes lines with a
    `Status`{.interpreted-text role="guilabel"} column value of
    `Available`{.interpreted-text role="guilabel"} or
    `Partially Available`{.interpreted-text role="guilabel"}.
-   `Done`{.interpreted-text role="guilabel"}: completed stock moves,
    with a `Status`{.interpreted-text role="guilabel"} of
    `Done`{.interpreted-text role="guilabel"}.
-   `Incoming`{.interpreted-text role="guilabel"}: displays move records
    from vendor locations.
-   `Outgoing`{.interpreted-text role="guilabel"}: displays move records
    to customer locations, including customer returns.
-   `Internal`{.interpreted-text role="guilabel"}: displays move records
    from one internal location to another.
-   `Manufacturing`{.interpreted-text role="guilabel"}: shows records
    where products were produced from the virtual, production
    `location <../inventory_management/use_locations>`{.interpreted-text
    role="doc"}.
-   `Date`{.interpreted-text role="guilabel"}: select this drop-down
    menu to access various date filter options and view stock moves from
    a specific month, quarter, or year.
-   `Last 30 Days`{.interpreted-text role="guilabel"}: show records that
    occurred in the last thirty days.
-   `Last 3 Months`{.interpreted-text role="guilabel"}: show records
    from the last three months.
:::

::: {.tab}
Group By

The `Group By`{.interpreted-text role="guilabel"} section allows users
to add pre-made and custom groupings to the search.

-   `Product`{.interpreted-text role="guilabel"}: group records by
    product.
-   `Status`{.interpreted-text role="guilabel"}: group records by the
    three status types: `Done`{.interpreted-text role="guilabel"},
    `Available`{.interpreted-text role="guilabel"}, and
    `Partially Available`{.interpreted-text role="guilabel"}.
-   `Date`{.interpreted-text role="guilabel"}: group records by
    `Year`{.interpreted-text role="guilabel"},
    `Quarter`{.interpreted-text role="guilabel"},
    `Month`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, or `Day`{.interpreted-text role="guilabel"}.
-   `Transfers`{.interpreted-text role="guilabel"}: group records by
    operation number, e.g. [WH/OUT/00012]{.title-ref},
    [WH/MO/00211]{.title-ref}.
-   `Location`{.interpreted-text role="guilabel"}: group records by
    source location (the `From`{.interpreted-text role="guilabel"}
    column in this report).
-   `Category`{.interpreted-text role="guilabel"}: group records by
    product category. To configure these, go to
    `Inventory app --> Configuration --> Products: Product Categories`{.interpreted-text
    role="menuselection"}.
-   `Batch Transfer`{.interpreted-text role="guilabel"}: group records
    by `batch
    <../../shipping_receiving/picking_methods/batch>`{.interpreted-text
    role="doc"}.
:::

::: {.tab}
Favorites

To save the current applied filters and groups, so the same information
can be easily accessed after closing this page, click
`Save current search`{.interpreted-text role="guilabel"}.

Optionally, tick the `Default filter`{.interpreted-text role="guilabel"}
checkbox to make this current view the default filter when opening the
`Moves History`{.interpreted-text role="guilabel"} report. Or tick the
`Shared`{.interpreted-text role="guilabel"} checkbox to make the search
option available to other users.

Lastly, click the `Save`{.interpreted-text role="guilabel"} button.
:::
:::

::: {.seealso}
`../../../../essentials/search`{.interpreted-text role="doc"}
:::
