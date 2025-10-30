# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/configure/packaging.md

Packaging
=========

In Odoo *Inventory*, *packaging* refers to disposable containers holding
multiple units of a specific product.

For example, different packages for cans of soda, such as a 6-pack, a
12-pack, or a case of 36, **must** be configured on the individual
product form. This is because packagings are product specific, not
generic.

::: {.tip}
::: {.title}
Tip
:::

Packaging can be used in conjunction with Odoo
`Barcode <inventory/barcode/software>`{.interpreted-text role="ref"}.
When receiving products from suppliers, scanning the packaging barcode
automatically adds the number of units in the packaging to the internal
count of the product.
:::

Configuration
-------------

To use packagings, navigate to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, under the `Products`{.interpreted-text
role="guilabel"} heading, enable the
`Product Packagings`{.interpreted-text role="guilabel"} feature, and
click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

Create packaging {#inventory/product_management/packaging-setup}
----------------

Packagings can be created directly on the product form, or from the
`Product Packagings`{.interpreted-text role="guilabel"} page.

### From product form

Create packagings on a product form by going to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and select the
desired product.

Under the `Inventory`{.interpreted-text role="guilabel"} tab, scroll
down to the `Packaging`{.interpreted-text role="guilabel"} section, and
click `Add a line`{.interpreted-text role="guilabel"}. In the table,
fill out the following fields:

-   `Packaging`{.interpreted-text role="guilabel"} (required): name of
    packaging that appears on sales/purchase orders as a packaging
    option for the product.
-   `Contained quantity`{.interpreted-text role="guilabel"} (required):
    amount of product in the packaging.
-   `Unit of Measure`{.interpreted-text role="guilabel"} (required):
    measurement unit for quantifying the product.
-   `Sales`{.interpreted-text role="guilabel"}: check this option for
    packagings intended for use on sales orders.
-   `Purchase`{.interpreted-text role="guilabel"}: check this option for
    packagings intended for use on purchase orders.

::: {.note}
::: {.title}
Note
:::

Access additional fields in the `Packaging`{.interpreted-text
role="guilabel"} table below by clicking the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(additional options)`{.interpreted-text role="guilabel"} icon to the
far-right of the column titles in the `Packaging`{.interpreted-text
role="guilabel"} section, and selecting the desired options from the
drop-down menu that appears.
:::

-   `Barcode`{.interpreted-text role="guilabel"}: identifier for tracing
    packaging in stock moves or pickings, using the
    `Barcode app <barcode/operations/intro>`{.interpreted-text
    role="ref"}. Leave blank if not in use.
-   `Company`{.interpreted-text role="guilabel"}: indicates the
    packaging is only available at the selected company. Leave blank to
    make the packaging available across all companies.

::: {.example}
To create a packaging type for six units of the product, [Grape
Soda]{.title-ref}, begin by clicking `Add a line`{.interpreted-text
role="guilabel"}. In the line, name the `Packaging`{.interpreted-text
role="guilabel"} [6-pack]{.title-ref}, and set the
`Contained quantity`{.interpreted-text role="guilabel"} to
[6]{.title-ref}. Repeat this process for additional packagings.

{.align-center}
:::

### From product packagings page

To view all packagings that have been created, go to
`Inventory app --> Configuration
--> Product Packagings`{.interpreted-text role="menuselection"}. Doing
so reveals the `Product Packagings`{.interpreted-text role="guilabel"}
page with a complete list of all packagings that have been created for
all products. Create new packagings by clicking `New`{.interpreted-text
role="guilabel"}.

::: {.example}
Two soda products, [Grape Soda]{.title-ref} and [Diet Coke]{.title-ref},
have three types of packagings configured. On the
`Product Packagings`{.interpreted-text role="guilabel"} page, each
product can be sold as a [6-Pack]{.title-ref} that contains 6 products,
as a [12-Pack]{.title-ref} of 12 products, or as a [Case]{.title-ref} of
32 products.

{.align-center}
:::

### Partial reservation

After
`completing the packaging setup <inventory/product_management/packaging-setup>`{.interpreted-text
role="ref"}, packagings can be reserved in full or partial quantities
for outgoing shipments. Partial packaging flexibility expedites order
fulfillment by allowing the immediate shipment of available items, while
awaiting the rest.

To configure packaging reservation methods, go to
`Inventory app --> Configuration
--> Product Categories`{.interpreted-text role="menuselection"}. Then,
click `New`{.interpreted-text role="guilabel"}, or select the desired
product category.

On the product category\'s form, in the `Logistics`{.interpreted-text
role="guilabel"} section, `Reserve Packagings`{.interpreted-text
role="guilabel"} can be set to
`Reserve Only Full Packagings`{.interpreted-text role="guilabel"} or
`Reserve Partial Packagings`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

To see the `Reserve Packaging`{.interpreted-text role="guilabel"} field,
the `Product Packaging`{.interpreted-text role="guilabel"} feature
**must** be enabled. To enable this feature, go to `Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
scroll to the `Products`{.interpreted-text role="guilabel"} section,
tick the `Product Packagings`{.interpreted-text role="guilabel"}
checkbox, and click `Save`{.interpreted-text role="guilabel"}.
:::

{.align-center}

::: {.example}
To better evaluate the options based on business needs, consider the
following example:

-   a product is sold in twelve units per packaging.
-   an order demands two packagings.
-   there are only twenty-two units in stock.

When `Reserve Only Full Packagings`{.interpreted-text role="guilabel"}
is selected, only twelve units are reserved for the order.

Conversely, when `Reserve Partial Packagings`{.interpreted-text
role="guilabel"} is selected, twenty-two units are reserved for the
order.
:::

Apply packagings
----------------

When creating a sales order in the `Sales`{.interpreted-text
role="menuselection"} app, specify the packagings that should be used
for the product. The chosen packaging is displayed on the
`SO (Sales Order)`{.interpreted-text role="abbr"} under the
`Packaging`{.interpreted-text role="guilabel"} field.

::: {.example}
18 cans of the product, [Grape Soda]{.title-ref}, is packed using three
6-pack packagings.

{.align-center}
:::

Routes for packaging {#inventory/product_management/packaging-route}
--------------------

When receiving packagings, by default, they follow the warehouse\'s
`configured reception route
<../../shipping_receiving/daily_operations>`{.interpreted-text
role="doc"}. To **optionally** set up a packaging-specific route, go to
`Inventory app --> Configuration --> Routes`{.interpreted-text
role="menuselection"}.

::: {.important}
::: {.title}
Important
:::

The *Product Packagings*, *Storage Locations*, and *Multi-Step Routes*
features (found by going to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}) **must** be activated, and saved.
:::

::: {.seealso}
`../../shipping_receiving/daily_operations/use_routes`{.interpreted-text
role="doc"}
:::

### Create route

On the `Routes`{.interpreted-text role="guilabel"} page, click
`New`{.interpreted-text role="guilabel"}, or select a route that is
**not** for a warehouse. Next, in the `Applicable on`{.interpreted-text
role="guilabel"} section, tick the `Packagings`{.interpreted-text
role="guilabel"} checkbox.

![Route with \"Packagings\" selected, with \"Products\" and
\"Warehouses\" not selected.](packaging/route.png){.align-center}

### Apply route on packaging {#inventory/product_management/route-on-packaging}

Then, to apply the route, go to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select the product that uses packaging.

In the product form, switch to the `Inventory`{.interpreted-text
role="guilabel"} tab. In the `Packaging`{.interpreted-text
role="guilabel"} section that contains
`configured packagings <inventory/product_management/packaging-setup>`{.interpreted-text
role="ref"}, click the `oi-settings-adjust`{.interpreted-text
role="icon"} `(additional options)`{.interpreted-text role="guilabel"}
icon. Tick the `Routes`{.interpreted-text role="guilabel"} checkbox to
make the column visible in the `Packaging`{.interpreted-text
role="guilabel"} table.

In the `Routes`{.interpreted-text role="guilabel"} field, select the
packaging-specific route. Repeat these steps for all packaging intended
to use the route.

{.align-center}
