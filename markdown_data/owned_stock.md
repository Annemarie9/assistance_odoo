# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/owned_stock.md

Consignment: buy and sell stock without owning it
=================================================

Most of the time, products stored in a company\'s warehouse are either
purchased from suppliers, or are manufactured in-house. However,
suppliers will sometimes let companies store and sell products in the
company\'s warehouse, without having to buy those items up-front. This
is called *consignment*.

Consignment is a useful method for suppliers to launch new products, and
easily deliver to their customers. It\'s also a great way for the
company storing the products (the consignee) to earn something back for
their efforts. Consignees can even charge a fee for the convenience of
storing products they don\'t actually own.

Enable the consignment setting
------------------------------

To receive, store, and sell consignment stock, the feature needs to be
enabled in the settings. To do this, go to
`Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and under the `Traceability`{.interpreted-text
role="guilabel"} section, check the box next to
`Consignment`{.interpreted-text role="guilabel"}, and then click
`Save`{.interpreted-text role="guilabel"} to finish.

{.align-center}

Receive (and store) consignment stock
-------------------------------------

With the feature enabled in Odoo, consignment stock can now be received
into a warehouse. From the main `Inventory`{.interpreted-text
role="menuselection"} dashboard, click into the
`Receipts`{.interpreted-text role="guilabel"} section. Then, click
`Create`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Consignment stock is not actually purchased from the vendor; it is
simply received and stored. Because of this, there are no quotations or
purchase orders involved in receiving consignment stock. So, *every*
receipt of consignment stock will start by creating manual receipts.
:::

Choose a vendor to enter in the `Receive From`{.interpreted-text
role="guilabel"} field, and then choose the same vendor to enter in the
`Assign Owner`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

Since the products received from the vendor will be owned by the same
vendor, the `Receive From`{.interpreted-text role="guilabel"} and
`Assign Owner`{.interpreted-text role="guilabel"} fields must match.
:::

Once the vendor-related fields are set, enter products into the
`Product`{.interpreted-text role="guilabel"} lines, and set the
quantities to be received into the warehouse under the
`Done`{.interpreted-text role="guilabel"} column. If the
`Units of Measure`{.interpreted-text role="guilabel"} feature is
enabled, the `UoM (Units of Measure)`{.interpreted-text role="abbr"} can
be changed, as well. Once all the consignment stock has been received,
`Validate`{.interpreted-text role="guilabel"} the receipt.

{.align-center}

Sell and deliver consignment stock
----------------------------------

Once consignment stock has been received into the warehouse, it can be
sold the same as any other in-stock product that has the
`Can Be Sold`{.interpreted-text role="guilabel"} option enabled on the
product form.

To create a sales order, navigate to the `Sales`{.interpreted-text
role="menuselection"} app, and from the `Quotations`{.interpreted-text
role="guilabel"} overview, click `Create`{.interpreted-text
role="guilabel"}. Next, choose a customer to enter into the
`Customer`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Customer`{.interpreted-text role="guilabel"} *must* be different
from the `Vendor`{.interpreted-text role="guilabel"} that supplied the
consignment stock received (and stored) in the warehouse.
:::

Add the consignment product under the `Product`{.interpreted-text
role="guilabel"} column in the order lines, set the
`Quantity`{.interpreted-text role="guilabel"}, and fill out any other
pertinent product details on the form. Once the quotation is complete,
click `Confirm`{.interpreted-text role="guilabel"}.

{.align-center}

Once the quotation has been confirmed, it becomes a sales order. From
here, the products can be delivered by clicking on the
`Delivery`{.interpreted-text role="guilabel"} smart button, and
selecting `Validate`{.interpreted-text role="guilabel"} to validate the
delivery.

Traceability and reporting of consignment stock
-----------------------------------------------

Although consignment stock is owned by the vendor who supplied it, and
not by the company storing it in their warehouse, consignment products
will *still* appear in certain inventory reports.

To find inventory reports, go to
`Inventory --> Reporting`{.interpreted-text role="menuselection"}, and
choose a report to view.

::: {.note}
::: {.title}
Note
:::

Since the consignee does not actually own consignment stock, these
products are *not* reflected in the `Stock Valuation`{.interpreted-text
role="guilabel"} report, and have no impact on the consignee\'s
inventory valuation.
:::

### Product moves report

To view all information about on-hand stock moves, navigate to the
`Product Moves`{.interpreted-text role="guilabel"} dashboard by going to
`Inventory --> Reporting --> Product Moves`{.interpreted-text
role="menuselection"}. For consignment products, the information in this
report is the same as any other product: the history of its product
moves can be reviewed; the `Quantity Done`{.interpreted-text
role="guilabel"} and `Reference`{.interpreted-text role="guilabel"}
document are available; and its `Locations`{.interpreted-text
role="guilabel"} are available, as well. The consignment stock will
originate from `Partner Location/Vendors`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

To view a consignment product\'s moves by ownership, select the
`Group By`{.interpreted-text role="guilabel"} filter, choose the
`Add Custom Group`{.interpreted-text role="guilabel"} parameter, and
then select `From Owner`{.interpreted-text role="guilabel"}, and
`Apply`{.interpreted-text role="guilabel"} to finish.
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To see forecasted units of consignment stock, go to
`Inventory --> Reporting -->
Forecasted Inventory`{.interpreted-text role="menuselection"}.
:::

### Stock on hand report

View the `Stock On Hand`{.interpreted-text role="guilabel"} dashboard by
navigating to `Inventory -->
Reporting --> Inventory Report`{.interpreted-text role="menuselection"}.
From this report, the `Locations`{.interpreted-text role="guilabel"} of
all stock on-hand are displayed, in addition to the quantities per
location. For consignment products, the `Owner`{.interpreted-text
role="guilabel"} column will be populated with the owner of those
products, or the original vendor who supplied the products in the first
place.
