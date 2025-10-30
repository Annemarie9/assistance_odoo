# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation.md

Using inventory valuation
=========================

::: {#inventory/reporting/using_inventory_val}
*Inventory valuation* is a quintessential accounting procedure that
calculates the value of on-hand stock. Once determined, the inventory
valuation amount is then incorporated into a company\'s overall value.
:::

In Odoo, this process can be conducted manually--- by warehouse
employees physically counting the products--- or automatically through
the database.

Automatic inventory valuation
-----------------------------

To use Odoo to automatically generate a trail of inventory valuation
entries, first navigate to the `Product Categories`{.interpreted-text
role="menuselection"} list by going to `Inventory app --> Configuration
--> Product Categories`{.interpreted-text role="menuselection"} and
select the desired product category. On the form, set the
`Inventory Valuation`{.interpreted-text role="guilabel"} as
`Automated`{.interpreted-text role="guilabel"} and the
`Costing Method`{.interpreted-text role="guilabel"} to any of the three
options.

::: {.seealso}
`Set up inventory valuation <inventory_valuation_config>`{.interpreted-text
role="doc"}
:::

In order to understand how moving products in and out of stock affects
the company\'s overall value, consider the following product and stock
moves scenario below.

### Receive a product

To track the value of incoming products, such as a simple *table*,
configure the product category on the the product itself. To get there,
navigate to `Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"} and click the desired
product. On the product form, click the
`➡️ (right arrow)`{.interpreted-text role="guilabel"} icon beside the
`Product Category`{.interpreted-text role="guilabel"} field, which opens
an internal link to edit the product category. Next, set the
`Costing Method`{.interpreted-text role="guilabel"} as
`First In First Out (FIFO)`{.interpreted-text role="guilabel"} and
`Inventory Valuation`{.interpreted-text role="guilabel"} as
`Automated`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Alternatively access the `Product Categories`{.interpreted-text
role="guilabel"} dashboard by navigating to
`Inventory app --> Configuration --> Product Categories`{.interpreted-text
role="menuselection"} and select the desired product category.
:::

Next, assume 10 tables are purchased at a price of \$10.00, each. The
`PO (Purchase Order)`{.interpreted-text role="abbr"} for those tables
will show the subtotal of the purchase as \$100, plus any additional
costs or taxes.

{.align-center}

After selecting `Validate`{.interpreted-text role="guilabel"} on the
`PO (Purchase Order)`{.interpreted-text role="abbr"}, the
`Valuation`{.interpreted-text role="guilabel"} smart button is enabled.
Clicking on this button displays a report showing how the inventory
valuation for the table was affected by this purchase.

::: {.important}
::: {.title}
Important
:::

`Developer mode <developer-mode>`{.interpreted-text role="ref"} **must**
be turned on to see the `Valuation`{.interpreted-text role="guilabel"}
smart button.
:::

::: {.tip}
::: {.title}
Tip
:::

The
`consignment <../../shipping_receiving/daily_operations/owned_stock>`{.interpreted-text
role="doc"} feature allows ownership to items in stock. Thus, products
owned by other companies are not accounted for in the host company\'s
inventory valuation.
:::

{.align-center}

For a comprehensive dashboard that includes the inventory valuation of
all product shipments, inventory adjustments, and warehouse operations,
refer to the `stock valuation report
<inventory/management/reporting/valuation-report>`{.interpreted-text
role="ref"}.

### Deliver a product

In the same logic, when a table is shipped to a customer and leaves the
warehouse, the stock valuation decreases. The
`Valuation`{.interpreted-text role="guilabel"} smart button on the
`DO (Delivery Order)`{.interpreted-text role="abbr"}, likewise, displays
the stock valuation record as it does on a
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

{.align-center}

Inventory valuation report {#inventory/management/reporting/valuation-report}
--------------------------

To view the current value of all products in the warehouse, first turn
on `Developer mode
<developer-mode>`{.interpreted-text role="ref"} and navigate to
`Inventory app --> Reporting --> Valuation`{.interpreted-text
role="menuselection"}. The `Stock Valuation`{.interpreted-text
role="guilabel"} dashboard displays detailed records of products with
the `Date`{.interpreted-text role="guilabel"},
`Quantity`{.interpreted-text role="guilabel"},
`Unit Value`{.interpreted-text role="guilabel"}, and
`Total Value`{.interpreted-text role="guilabel"} of the inventory.

::: {.important}
::: {.title}
Important
:::

`Developer mode <developer-mode>`{.interpreted-text role="ref"} **must**
be enabled to see the `Valuation`{.interpreted-text role="guilabel"}
option under `Reporting`{.interpreted-text role="guilabel"}.
:::

{.align-center}

The `Valuation At Date`{.interpreted-text role="guilabel"} button,
located in the top-left corner of the `Stock
Valuation`{.interpreted-text role="guilabel"} page, reveals a pop-up
window. In this pop-up, the inventory valuation of products available
during a prior specified date can be seen and selected.

::: {.tip}
::: {.title}
Tip
:::

View a detailed record of a product\'s inventory value, stock move, and
on-hand stock by selecting the teal `➡️ (right arrow)`{.interpreted-text
role="guilabel"} button to the right of the
`Reference`{.interpreted-text role="guilabel"} column value.
:::

### Update product unit price

For any company: lead times, supply chain failures, and other risk
factors can contribute to invisible costs. Although Odoo attempts to
accurately represent the stock value, *manual valuation* serves as an
additional tool to update the unit price of products.

::: {.important}
::: {.title}
Important
:::

Manual valuation is intended for products that can be purchased and
received for a cost greater than 0, or have product categories set with
`Costing Method`{.interpreted-text role="guilabel"} set as either
`Average Cost (AVCO)`{.interpreted-text role="guilabel"} or
`First In First Out (FIFO)`{.interpreted-text role="guilabel"}.
:::

{.align-center}

Create manual valuation entries on the
`Stock Valuation`{.interpreted-text role="guilabel"} dashboard by first
navigating to
`Inventory app --> Reporting --> Valuation`{.interpreted-text
role="menuselection"}. Next, to enable the *product revaluation*
feature, select `Group by --> Product`{.interpreted-text
role="menuselection"} to organize all the records by product. Click on
the gray `▶️ (drop-down triangle)`{.interpreted-text role="guilabel"}
icon to reveal stock valuation line items below, as well as a teal
`➕ (plus)`{.interpreted-text role="guilabel"} button on the right.

Click the teal `+ (plus)`{.interpreted-text role="guilabel"} button to
open up the `Product Revaluation`{.interpreted-text role="guilabel"}
form. Here, the inventory valuation for a product can be recalculated,
by increasing or decreasing the unit price of each product.

::: {.note}
::: {.title}
Note
:::

The `▶️ (drop-down triangle)`{.interpreted-text role="guilabel"} and
`➕ (plus)`{.interpreted-text role="guilabel"} buttons are only visible
after grouping entries by product.
:::

{.align-center}

### Inventory valuation journal entries

In Odoo, automatic inventory valuation records are also recorded in the
`Accounting
app --> Accounting --> Journal Entries`{.interpreted-text
role="menuselection"} dashboard. On this comprehensive list of
accounting entries, inventory valuation records are identified by
checking values in the `Journal`{.interpreted-text role="guilabel"}
column, or looking for the `Reference`{.interpreted-text
role="guilabel"} column value which matches the warehouse operation
reference (e.g. [WH/IN/00014]{.title-ref} for receipts).

Clicking on an inventory valuation journal entry opens a *double-entry
accounting* record. These records are generated by Odoo to track the
change of value in inventory valuation as products are moved in and out
of the warehouse.

::: {.example}
To view the inventory valuation of 10 *tables*, costing \$10.00 each,
upon reception from the vendor, go to the
`Journal Entries`{.interpreted-text role="menuselection"} page found in
`Accounting app
--> Accounting --> Journal Entries`{.interpreted-text
role="menuselection"}. Here, click the journal line where the
`Reference`{.interpreted-text role="guilabel"} column value matches the
reference on the receipt, [WH/IN/00014]{.title-ref}.

{.align-center}

[Stock interim]{.title-ref} is a holding account for money intended to
pay vendors for the product. The [stock valuation]{.title-ref} account
stores the value of all on-hand stock.

{.align-center}
:::

::: {.seealso}
[Odoo Tutorial: Inventory
Valuation](https://www.odoo.com/slides/slide/2795/share)
:::
