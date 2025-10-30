# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/inventory_valuation/landed_costs.md

Landed costs
============

When shipping products to customers, the landed cost is the total price
of a product or shipment, including all expenses associated with
shipping the product.

In Odoo, the *Landed Costs* feature is used to take additional costs
into account when calculating the valuation of a product. This includes
the cost of shipment, insurance, customs duties, taxes, and other fees.

Configuration
-------------

To add landed costs to products, the *Landed Costs* feature must first
be enabled. To enable this feature, navigate to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and scroll to the `Valuation`{.interpreted-text
role="guilabel"} section.

Tick the checkbox next to the `Landed Costs`{.interpreted-text
role="guilabel"} option, and click `Save`{.interpreted-text
role="guilabel"} to save changes.

Once the page refreshes, a new `Default Journal`{.interpreted-text
role="guilabel"} field appears below the `Landed
Costs`{.interpreted-text role="guilabel"} feature in the
`Valuation`{.interpreted-text role="guilabel"} section.

Click the `Default Journal`{.interpreted-text role="guilabel"} drop-down
menu to reveal a list of accounting journals. Select a journal for which
all accounting entries related to landed costs should be recorded.



Create landed cost product
--------------------------

For charges that are consistently added as landed costs, a landed cost
product can be created in Odoo. This way, a landed cost product can be
quickly added to a vendor bill as an invoice line, instead of having to
be manually entered every time a new vendor bill is created.

To do this, create a new product by going to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and clicking
`New`{.interpreted-text role="guilabel"}.

Assign a name to the landed cost product in the
`Product Name`{.interpreted-text role="guilabel"} field (i.e.
[International Shipping]{.title-ref}). In the
`Product Type`{.interpreted-text role="guilabel"} field, click the
drop-down menu, and select `Service`{.interpreted-text role="guilabel"}
as the `Product Type`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Landed cost products **must** have their
`Product Type`{.interpreted-text role="guilabel"} set to
`Service`{.interpreted-text role="guilabel"}.
:::

Click the `Purchase`{.interpreted-text role="guilabel"} tab, and tick
the checkbox next to `Is a Landed Cost`{.interpreted-text
role="guilabel"} in the `Vendor Bills`{.interpreted-text
role="guilabel"} section. Once ticked, a new
`Default Split Method`{.interpreted-text role="guilabel"} field appears
below it, prompting a selection. Clicking that drop-down menu reveals
the following options:

-   `Equal`{.interpreted-text role="guilabel"}: splits the cost equally
    across each product included in the receipt, regardless of the
    quantity of each.
-   `By Quantity`{.interpreted-text role="guilabel"}: splits the cost
    across each unit of all products in the receipt.
-   `By Current Cost`{.interpreted-text role="guilabel"}: splits the
    cost according to the cost of each product unit, so a product with a
    higher cost receives a greater share of the landed cost.
-   `By Weight`{.interpreted-text role="guilabel"}: splits the cost,
    according to the weight of the products in the receipt.
-   `By Volume`{.interpreted-text role="guilabel"}: splits the cost,
    according to the volume of the products in the receipt.



When creating new vendor bills, this product can be added as an invoice
line as a landed cost.

::: {.important}
::: {.title}
Important
:::

To apply a landed cost on a vendor bill, products in the original
`PO (Purchase Order)`{.interpreted-text role="abbr"} **must** belong to
a *Product Category* with a *Costing Method* of either
`AVCO (Average Costing)`{.interpreted-text role="abbr"} or
`FIFO (First In First Out)`{.interpreted-text role="abbr"}, and the
valuation method can be
`manual <using_inventory_valuation>`{.interpreted-text role="doc"} or
`automatic
<inventory_valuation_config>`{.interpreted-text role="doc"}.
:::

Create purchase order
---------------------

Navigate to `Purchase app --> New`{.interpreted-text
role="menuselection"} to create a new request for quotation (RfQ). In
the `Vendor`{.interpreted-text role="guilabel"} field, add a vendor to
order products from. Then, click `Add a
product`{.interpreted-text role="guilabel"}, under the
`Products`{.interpreted-text role="guilabel"} tab, to add products to
the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}.

Once ready, click `Confirm Order`{.interpreted-text role="guilabel"} to
confirm the order. Then, click `Receive
Products`{.interpreted-text role="guilabel"} once the products have been
received, followed by `Validate`{.interpreted-text role="guilabel"}.

### Create vendor bill

Once the vendor fulfills the `PO (Purchase Order)`{.interpreted-text
role="abbr"} and sends a bill, a vendor bill can be created from the
`PO (Purchase Order)`{.interpreted-text role="abbr"} in Odoo.

Navigate to the `Purchase app`{.interpreted-text role="menuselection"},
and click into the `PO (Purchase Order)`{.interpreted-text role="abbr"}
for which a vendor bill should be created. Then, click
`Create Bill`{.interpreted-text role="guilabel"}. This opens a new
`Vendor Bill`{.interpreted-text role="guilabel"} in the
`Draft`{.interpreted-text role="guilabel"} stage.

In the `Bill Date`{.interpreted-text role="guilabel"} field, click the
line to open a calendar popover menu, and select the date on which this
draft bill should be billed.

Then, under the `Invoice Lines`{.interpreted-text role="guilabel"} tab,
click `Add a line`{.interpreted-text role="guilabel"}, and click the
drop-down menu in the `Product`{.interpreted-text role="guilabel"}
column to select the previously-created landed cost product. Click the
`fa-cloud-upload`{.interpreted-text role="icon"}
`(cloud with arrow)`{.interpreted-text role="guilabel"} icon to manually
save and update the draft bill.



In the `Landed Costs`{.interpreted-text role="guilabel"} column, the
product ordered from the vendor does **not** have its checkbox ticked,
while the landed cost product\'s checkbox **is** ticked. This
differentiates landed costs from all other costs displayed on the bill.

Additionally, at the top of the form, a
`Create Landed Costs`{.interpreted-text role="guilabel"} button appears.



Add landed cost
---------------

Once a landed cost is added to the vendor bill, click
`Create Landed Costs`{.interpreted-text role="guilabel"} at the top of
the vendor bill.

Doing so automatically creates a landed cost record, with a set landed
cost pre-filled in the product line in the
`Additional Costs`{.interpreted-text role="guilabel"} tab.

From the `Landed Cost`{.interpreted-text role="guilabel"} form, click
the `Transfers`{.interpreted-text role="guilabel"} drop-down menu, and
select which transfer the landed cost belongs to.



::: {.tip}
::: {.title}
Tip
:::

In addition to creating landed costs directly from a vendor bill, landed
cost records can *also* be created by navigating to
`Inventory app --> Operations --> Landed Costs`{.interpreted-text
role="menuselection"}, and clicking `New`{.interpreted-text
role="guilabel"}.
:::

After setting the picking from the `Transfers`{.interpreted-text
role="guilabel"} drop-down menu, click `Compute`{.interpreted-text
role="guilabel"} (at the bottom of the form, under the
`Total:`{.interpreted-text role="guilabel"} cost).

Click the `Valuation Adjustments`{.interpreted-text role="guilabel"} tab
to see the impact of the landed costs. The
`Original Value`{.interpreted-text role="guilabel"} column lists the
original price of the `PO (Purchase Order)`{.interpreted-text
role="abbr"}, the `Additional
Landed Cost`{.interpreted-text role="guilabel"} column displays the
landed cost, and the `New Value`{.interpreted-text role="guilabel"}
displays the sum of the two, for the total cost of the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to post
the landed cost entry to the accounting journal.

This causes a `Valuation`{.interpreted-text role="guilabel"} smart
button to appear at the top of the form. Click the
`Valuation`{.interpreted-text role="guilabel"} smart button to open a
`Stock Valuation`{.interpreted-text role="guilabel"} page, with the
product\'s updated valuation listed.

::: {.note}
::: {.title}
Note
:::

For a `Valuation`{.interpreted-text role="guilabel"} smart button to
appear upon validation, the product\'s `Product Type`{.interpreted-text
role="guilabel"} **must** be set to `Storable`{.interpreted-text
role="guilabel"}.
:::

To view the valuation of *every* product, including landed costs,
navigate to
`Inventory app --> Reporting --> Valuation`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Each journal entry created for a landed cost on a vendor bill can be
viewed in the *Accounting* app.

To locate these journal entries, navigate to
`Accounting app --> Accounting -->
Journal Entries`{.interpreted-text role="menuselection"}, and locate the
correct entry, by number (i.e. [PBNK1/2024/XXXXX]{.title-ref}).

Click into the journal entry to view the
`Journal Items`{.interpreted-text role="guilabel"}, and other
information about the entry.


:::
