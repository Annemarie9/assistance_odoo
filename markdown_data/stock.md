# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/stock.md

Stock report
============

Use the stock report in Odoo *Inventory* for a detailed list of all
stored products, including those reserved, purchased and in transit, as
well as those delivered to customers.

::: {.note}
::: {.title}
Note
:::

The reporting feature is only accessible to users with `admin access
<../../../../general/users/access_rights>`{.interpreted-text
role="doc"}.
:::

To access the stock report, go to
`Inventory app --> Reporting --> Stock`{.interpreted-text
role="menuselection"}.

{.align-center}

Navigate the stock report
-------------------------

On the stock report, the left sidebar includes several groupings to
narrow down what is being shown. The default groupings are
`Warehouses`{.interpreted-text role="guilabel"}, which filters products
by specific warehouses, and `Category`{.interpreted-text
role="guilabel"}, which shows products within a selected product
category.

::: {.note}
::: {.title}
Note
:::

The `Warehouse`{.interpreted-text role="guilabel"} grouping is only
available when there are multiple warehouses in the database. Refer to
the `../inventory_management/warehouses`{.interpreted-text role="doc"}
documentation for more details.
:::

In the report itself, the columns represent:

-   `Product`{.interpreted-text role="guilabel"}: name of the product.

-   `Unit Cost`{.interpreted-text role="guilabel"}: average inventory
    valuation per unit, adjusted based on the cost to purchase and/or
    manufacture the product.

-   `Total Value`{.interpreted-text role="guilabel"}: Total inventory
    valuation of the product, calculated by multiplying unit cost by
    on-hand quantity.

    ::: {.seealso}
    -   `Compute average cost inventory valuation per unit <inventory/avg_cost/formula>`{.interpreted-text
        role="ref"}

    \- `Inventory valuation methods
    <../../product_management/inventory_valuation/inventory_valuation_config>`{.interpreted-text
    role="doc"}
    :::

-   `On Hand`{.interpreted-text role="guilabel"}: current quantity of
    products. Click the `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon to
    `modify the on-hand quantity
    <../inventory_management/count_products>`{.interpreted-text
    role="doc"}.

-   `Free to Use`{.interpreted-text role="guilabel"}: on-hand quantity
    that are **not** reserved for delivery or manufacturing orders, and
    are available to sell or use.

-   `Incoming`{.interpreted-text role="guilabel"}: items expected to
    arrive at the warehouse. Number of products is based on quantities
    in confirmed purchase orders.

-   `Outgoing`{.interpreted-text role="guilabel"}: items expected to
    leave the warehouse or be consumed in manufacturing orders. Number
    of products is based on quantities in confirmed sales or
    manufacturing orders.

Click the buttons to the right of each row item to access additional
information:

-   `History`{.interpreted-text role="guilabel"}: access the stock move
    history of the product, displaying information about the quantity
    and description of why the product was moved from one location to
    another.
-   `Replenishment`{.interpreted-text role="guilabel"}: access the
    `reordering rules
    <../replenishment/reordering_rules>`{.interpreted-text role="doc"}
    page for the product to create or manage methods of procuring the
    product.
-   `Locations`{.interpreted-text role="guilabel"}: break down of
    on-hand quantity at multiple storage locations. Only available when
    the product is stored in multiple locations.
-   `Forecast`{.interpreted-text role="guilabel"}: access the forecasted
    report to view on-hand, incoming, and outgoing quantities. Report
    also contains links to confirmed purchase, sales, or manufacturing
    orders. Only available when there are confirmed sales, purchase, or
    manufacturing orders for the product.

### Search options

::: {.tabs}
::: {.tab}
Filters

The `Filters`{.interpreted-text role="guilabel"} section allows users to
search among pre-made and custom filters to find specific stock records.

-   `Published`{.interpreted-text role="guilabel"}: display products
    published on the website. Only available with the *Website* app
    installed.

-   `Available in POS`{.interpreted-text role="guilabel"}: display
    products available through the *Point of Sale* app.

-   `Available in Self`{.interpreted-text role="guilabel"}: display
    products available in self order through the *Point of Sale* app.
    Appears in the search because the
    `Available in Self Order`{.interpreted-text role="guilabel"}
    checkbox was ticked in the `Point of Sale`{.interpreted-text
    role="guilabel"} section of a product form\'s
    `Sales`{.interpreted-text role="guilabel"} tab. The option is only
    available when the `Available in POS`{.interpreted-text
    role="guilabel"} checkbox is ticked.

    {.align-center}

-   `Not available in Self`{.interpreted-text role="guilabel"}: display
    products available in *PoS*, but not available in self order.

::: {.seealso}

:::

-   `Can be Sold`{.interpreted-text role="guilabel"}: display products
    that can be sold to customers. Appears in the search because the
    `Can be Sold`{.interpreted-text role="guilabel"} checkbox is ticked
    on the product form.
-   `Can be Purchased`{.interpreted-text role="guilabel"}: display
    products that can be bought from vendors. Appears in the search
    because the `Can be Purchased`{.interpreted-text role="guilabel"}
    checkbox is ticked on the product form.
-   `Can be Recurring`{.interpreted-text role="guilabel"}: show
    subscription products, indicated by ticking the
    `Recurring`{.interpreted-text role="guilabel"} checkbox on the
    product form. Only available with the *Subscription* app activated.
-   `Can be Rented`{.interpreted-text role="guilabel"}: show products
    that can be loaned to customers for a certain time. Appears in the
    search because the `Can be Rented`{.interpreted-text
    role="guilabel"} checkbox was ticked on the product form. Only
    available with the *Rental* app installed.
-   `Can be Subcontracted`{.interpreted-text role="guilabel"}: display
    products that can be produced by a `third-party manufacturer
    <../../../manufacturing/subcontracting/subcontracting_basic>`{.interpreted-text
    role="doc"}. Available only with the *Manufacturing* app installed.
-   `Can be Expensed`{.interpreted-text role="guilabel"}: show items
    that can be expensed. Only available with the *Expenses* app
    installed.

::: {.seealso}
`../../product_management/configure/type`{.interpreted-text role="doc"}
:::
:::

::: {.tab}
Group By

The `Group By`{.interpreted-text role="guilabel"} section allows users
to add pre-made and custom groupings to the search results.

-   `Product Type`{.interpreted-text role="guilabel"}: group items by
    `product type
    <../../product_management/configure/type>`{.interpreted-text
    role="doc"}.
-   `Product Category`{.interpreted-text role="guilabel"}: group items
    by product category. To configure these, go to
    `Inventory app --> Configuration --> Products: Product Categories`{.interpreted-text
    role="menuselection"}.
-   `POS Product Category`{.interpreted-text role="guilabel"}: group
    items by `point of sale product categories
    <../../../../sales/point_of_sale/configuration>`{.interpreted-text
    role="doc"}.
:::

::: {.tab}
Favorites

To save the current applied filters and groupbys, so the same
information can be easily accessed after closing this page, click
`Save current search`{.interpreted-text role="guilabel"}.

Optionally, tick the `Default filter`{.interpreted-text role="guilabel"}
checkbox to make this current view the default filter when opening the
stock report. Or tick the `Shared`{.interpreted-text role="guilabel"}
checkbox to make the search option available to other users.

Lastly, click the `Save`{.interpreted-text role="guilabel"} button.
:::
:::

::: {.seealso}
`../../../../essentials/search`{.interpreted-text role="doc"}
:::
