# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.md

Lot numbers
===========

*Lots* are one of the two ways to identify and track products in Odoo.
They typically represent a specific batch of products that were
received, stored, shipped, or manufactured in-house.

Manufacturers assign lot numbers to groups of products sharing common
properties, facilitating end-to-end traceability through their
lifecycles.

Lots are useful for managing large quantities of manufactured or
received products, aiding in tracing items back to their group,
particularly for product recalls or `expiration dates
<expiration_dates>`{.interpreted-text role="doc"}.

::: {.seealso}
`serial_numbers`{.interpreted-text role="doc"}
:::

Enable lots & serial numbers
----------------------------

To track products using lots, enable the *Lots & Serial Numbers*
feature. Go to the
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the
`Traceability`{.interpreted-text role="guilabel"} section, and tick the
checkbox next to `Lots & Serial Numbers`{.interpreted-text
role="guilabel"}. Then, click `Save`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `Tracking expiration dates <expiration_dates>`{.interpreted-text
role="doc"} -
`Print GS1 barcodes for lots and serial numbers <barcode/operations/gs1-lots>`{.interpreted-text
role="ref"}
:::

{.align-center}

Track by lots {#inventory/management/track_products_by_lots}
-------------

Once the `Lots & Serial Numbers`{.interpreted-text role="guilabel"}
feature is activated, configure individual products to be tracked using
lots. To do this, go to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and choose a product to configure.

On the product form, go to the `Inventory`{.interpreted-text
role="guilabel"} tab. In the `Traceability`{.interpreted-text
role="guilabel"} section, select the `By Lots`{.interpreted-text
role="guilabel"} option in the `Tracking`{.interpreted-text
role="guilabel"} field. Now, new or existing lot numbers can be assigned
to newly-received or manufactured batches of this product.

::: {.seealso}
`expiration_dates`{.interpreted-text role="doc"}
:::

::: {.important}
::: {.title}
Important
:::

If a product has stock on-hand prior to activating tracking by lots or
serial numbers, a warning message appears. Use an
`inventory adjustment <reassign>`{.interpreted-text role="doc"} to
assign lot numbers to existing products in stock.
:::

{.align-center}

Assign lots for shipping and receiving
--------------------------------------

Assign new lot numbers to
`incoming goods <inventory/product_management/assign-lots>`{.interpreted-text
role="ref"} on the receipt form. When shipping `outgoing goods
<inventory/product_management/assign-lots-delivery>`{.interpreted-text
role="ref"}, select products with specific lot numbers on the delivery
order form.

### On receipts {#inventory/product_management/assign-lots}

Assigning new or existing lot numbers to incoming goods can be done
directly on receipts.

To begin, go to the `Purchase`{.interpreted-text role="menuselection"}
app to 
a `PO (Purchase Order)`{.interpreted-text role="abbr"} for products
tracked by lot numbers. Then, click the `Receipt`{.interpreted-text
role="guilabel"} smart button that appears at the top of the page to
navigate to the warehouse receipt form.

::: {.note}
::: {.title}
Note
:::

Alternatively, navigate to an existing receipt by going to the
`Inventory`{.interpreted-text role="menuselection"} app, clicking the
`Receipts`{.interpreted-text role="guilabel"} Kanban card, and choosing
the desired receipt.
:::

::: {.important}
::: {.title}
Important
:::

Clicking `Validate`{.interpreted-text role="guilabel"} before assigning
a lot number triggers an error, indicating that a lot number **must** be
assigned before validating the receipt.

{.align-center}
:::

On the receipt form, on the product line in the
`Operations`{.interpreted-text role="guilabel"} tab, select the
`fa-list`{.interpreted-text role="icon"} `(list)`{.interpreted-text
role="guilabel"} icon to the right of the product that is tracked by lot
numbers.

{.align-center}

Doing so opens the `Open: Stock move`{.interpreted-text role="guilabel"}
pop-up window, where the `Lot/Serial
Number`{.interpreted-text role="guilabel"} and
`Quantity`{.interpreted-text role="guilabel"} are assigned.

The two ways to assign lot numbers: **manually** and **importing**.

#### Manual assignment

To manually assign lot numbers, click `Add a line`{.interpreted-text
role="guilabel"}. Input the `Lot/Serial
Number`{.interpreted-text role="guilabel"}, `Store To`{.interpreted-text
role="guilabel"} location for the lot, `Quantity`{.interpreted-text
role="guilabel"}, and `Destination
Package`{.interpreted-text role="guilabel"}, if any.

::: {.note}
::: {.title}
Note
:::

To assign multiple lot numbers, or store to multiple locations, click
`Add a line`{.interpreted-text role="guilabel"}, and type a new
`Lot/Serial Number`{.interpreted-text role="guilabel"} for additional
quantities. Repeat until the total in the `Quantity`{.interpreted-text
role="guilabel"} column matches the `Demand`{.interpreted-text
role="guilabel"} at the top.
:::

{.align-center}

#### Import lots

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, click `Import Serials/Lots`{.interpreted-text role="guilabel"},
then paste the bulk lot numbers, in the
`Lots/Serial numbers`{.interpreted-text role="guilabel"} field.

![List of lot numbers copied on *Google*
spreadsheets.](lots/lots-excel-spreadsheet.png){.align-center}

![Lot numbers pasted to the \"Lots/Serial numbers\" field, in the
**Import Lots** pop-up window.](lots/bulk-sn.png){.align-center}

Tick the `Keep current lines`{.interpreted-text role="guilabel"}
checkbox to generate *additional* lot numbers in the
`Open: Stock move`{.interpreted-text role="guilabel"} pop-up window. To
replace the lot numbers in the list, leave the
`Keep current lines`{.interpreted-text role="guilabel"} option unticked.

Finally, click `Generate`{.interpreted-text role="guilabel"}.

Once all product quantities have been assigned a lot number, click
`Save`{.interpreted-text role="guilabel"} to close the pop-up window.
Then, click `Validate`{.interpreted-text role="guilabel"} on the receipt
form.

::: {.seealso}
`Traceability report for lot numbers <inventory/product_management/lot-traceability>`{.interpreted-text
role="ref"}
:::

### On delivery orders {#inventory/product_management/assign-lots-delivery}

Odoo makes it possible to specify which lot numbers for a product are
chosen for outgoing shipment on a delivery order form.

To begin, create or select an existing quotation from the
`Sales`{.interpreted-text role="menuselection"} app. After confirming
the `SO (Sales Order)`{.interpreted-text role="abbr"}, the
`Delivery`{.interpreted-text role="guilabel"} smart button becomes
available. Click the `Delivery`{.interpreted-text role="guilabel"} smart
button to view the warehouse receipt form for that specific
`SO (Sales Order)`{.interpreted-text role="abbr"}.

::: {.note}
::: {.title}
Note
:::

Alternatively, navigate to delivery orders by going to the
`Inventory`{.interpreted-text role="menuselection"} app, and clicking
the `Delivery Orders`{.interpreted-text role="guilabel"} kanban card.
:::

Clicking the `Delivery`{.interpreted-text role="guilabel"} smart button
opens the the delivery order form, where lot numbers are picked for
delivery. In the `Operations`{.interpreted-text role="guilabel"} tab,
click the `fa-list`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon to the right of the
product that is tracked by lot numbers. Clicking that icon reveals a
`Open: Stock
move`{.interpreted-text role="guilabel"} pop-up window.

In the pop-up window, the chosen lot number and its storage location is
displayed in the `Pick From`{.interpreted-text role="guilabel"} column,
with the with the full `Quantity`{.interpreted-text role="guilabel"}
taken from that specific lot (if there is enough stock in that
particular lot).

If there is insufficient stock in that lot, or if partial quantities of
the `Demand`{.interpreted-text role="guilabel"} should be taken from
multiple lots, change the `Quantity`{.interpreted-text role="guilabel"}
directly.

::: {.note}
::: {.title}
Note
:::

The lot automatically chosen for delivery orders varies, depending on
the selected removal strategy
(`FIFO (First In, First Out)`{.interpreted-text role="abbr"},
`LIFO (Last In, First Out)`{.interpreted-text role="abbr"}, or `FEFO
(First Expiry, First Out)`{.interpreted-text role="abbr"}). It also
depends on the ordered quantity, and whether the lot\'s on-hand quantity
is enough to fulfill the order.
:::

::: {.seealso}
`../../shipping_receiving/removal_strategies`{.interpreted-text
role="doc"}
:::

Repeat the above steps to select enough lots to fulfill the
`Demand`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"} to close the pop-up window.
Lastly, click the `Validate`{.interpreted-text role="guilabel"} button
on the `DO (Delivery Order)`{.interpreted-text role="abbr"} to deliver
the products.

{.align-center}

::: {.seealso}
`Traceability report for lot numbers <inventory/product_management/lot-traceability>`{.interpreted-text
role="ref"}
:::

Lot management
--------------

Manage and view existing lot numbers for products in the
`Lot/Serial Numbers`{.interpreted-text role="guilabel"} dashboard by
going to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}.

By default, lot numbers are grouped by product, and selecting the
drop-down menu for each product displays the existing lot numbers.
Select a lot number to `modify or add details
<inventory/product_management/edit-lot>`{.interpreted-text role="ref"}
linked to the lot. Lot numbers can also be `created
<inventory/product_management/create-new-lot>`{.interpreted-text
role="ref"} from this page, by clicking the `New`{.interpreted-text
role="guilabel"} button.

![Display lot numbers, grouped by products, on the **Lot/Serial Number**
dashboard.](lots/lot-dashboard.png){.align-center}

### Modify lot {#inventory/product_management/edit-lot}

Clicking a lot from the `Lot/Serial Number`{.interpreted-text
role="guilabel"} dashboard reveals a separate page where additional
information can be provided about the lot.

::: {.tip}
::: {.title}
Tip
:::

Odoo automatically generates a new `Lot/Serial Number`{.interpreted-text
role="guilabel"} to follow the most recent number. However, it can be
edited, by clicking the line under the
`Lot/Serial Number`{.interpreted-text role="guilabel"} field, and
changing the generated number to any desired one.
:::

On the lot number form, the following fields can be modified:

-   `Lot/Serial Number`{.interpreted-text role="guilabel"}: change the
    lot number linked to the `Product`{.interpreted-text
    role="guilabel"}
-   `Internal Reference`{.interpreted-text role="guilabel"}: records an
    alternative lot/serial number used within the warehouse that differs
    from the one used by the supplier manufacturer.
-   `Company`{.interpreted-text role="guilabel"}: specify the company
    where the lot number is available.
-   `Description`{.interpreted-text role="guilabel"}: add extra details
    about the lot or serial number in this text field.

::: {.important}
::: {.title}
Important
:::

On existing lots, the `Product`{.interpreted-text role="guilabel"} and
`On Hand Quantity`{.interpreted-text role="guilabel"} fields **cannot**
be modified, as the lot numbers are linked with existing stock moves.
:::

{.align-center}

::: {.seealso}
`Set expiration dates for lots <expiration_dates>`{.interpreted-text
role="doc"}
:::

#### Add property

To add custom fields to lots for enhanced traceability, there are two
methods of adding properties on a lot number form:

1.  Click the `fa-cog`{.interpreted-text role="icon"}
    `(cog)`{.interpreted-text role="guilabel"} icon at the top-left of
    the page, then select `fa-cogs`{.interpreted-text role="icon"}
    `Add Properties`{.interpreted-text role="guilabel"} from the
    drop-down menu.
2.  Click the `fa-plus`{.interpreted-text role="icon"}
    `Add a Property`{.interpreted-text role="guilabel"} button, located
    below the existing fields.

Name and
`configure the new field <../../../../productivity/knowledge/properties>`{.interpreted-text
role="doc"}. Once finished, enter the property value in the new field.

::: {.example}
The new property, [Wood type]{.title-ref}, is added. The value is
recorded as [Cherry wood]{.title-ref}.

{.align-center}
:::

::: {.seealso}
`Configuring custom properties <../../../../productivity/knowledge/properties>`{.interpreted-text
role="doc"}
:::

### Reserve lot number for a product {#inventory/product_management/create-new-lot}

To create a lot number for a product, begin by going to
`Inventory app --> Products
--> Lot/Serial Numbers`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Creating a lot number reserves it for a product but **does not** assign
it. To assign lot numbers, refer to the section on
`assigning lot numbers on receipts
<inventory/product_management/assign-lots>`{.interpreted-text
role="ref"}.
:::

::: {.tip}
::: {.title}
Tip
:::

While Odoo automatically generates a new
`Lot/Serial Number`{.interpreted-text role="guilabel"} to follow the
most recent number, it can be edited and changed to any desired number,
by clicking the line under the `Lot/Serial Number`{.interpreted-text
role="guilabel"} field on the lot form, and changing the generated
number.
:::

Once the new `Lot/Serial Number`{.interpreted-text role="guilabel"} is
generated, click the blank field next to `Product`{.interpreted-text
role="guilabel"} to reveal a drop-down menu. From this menu, select the
product to which this new number will be assigned.

::: {.example}
The lot number, [000001]{.title-ref}, is created for the product,
[Drawer Black]{.title-ref}.

{.align-center}
:::

After a new lot number has been created, saved, and assigned to the
desired product, the lot number is saved as an existing lot number
linked to the product, and can be selected when `assigning
lot numbers to products on a receipt <inventory/product_management/assign-lots>`{.interpreted-text
role="ref"}, or when making an inventory adjustment.

::: {.example}
After creating the lot number, [000001]{.title-ref} appears as an option
for [Drawer Black]{.title-ref} when assigning lot numbers on the
`Inventory Adjustment`{.interpreted-text role="guilabel"} page.

{.align-center}
:::

Manage lots for different operations types
------------------------------------------

By default, new lots can only be created when receiving products, and
existing lot numbers cannot be used. For sales orders, only existing lot
numbers can be utilized, and new ones cannot be created on the delivery
order.

To change the ability to use new (or existing) lot numbers on any
operation type, go to the
`Inventory app --> Configuration --> Operations Types`{.interpreted-text
role="menuselection"}, and select the desired operation type.

On the operation type form, under the
`Lots/Serial Numbers`{.interpreted-text role="guilabel"} section, tick
the `Create New`{.interpreted-text role="guilabel"} checkbox to enable
new lot numbers to be created during this operation type. Choose
`Use Existing ones`{.interpreted-text role="guilabel"} if only existing
lot numbers can be selected.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For inter-warehouse transfers involving products tracked by lots, it can
be useful to enable the
`Use Existing Lots/Serial Numbers`{.interpreted-text role="guilabel"}
option for warehouse receipts.
:::

Traceability {#inventory/product_management/lot-traceability}
------------

Manufacturers and companies can refer to traceability reports to see the
entire lifecycle of a product: where it came from, when it arrived,
where it was stored, who it went to (and when).

To see the full traceability of a product, or group by lots, go to the
`Inventory app
--> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}. Doing so reveals the
`Lots/Serial Numbers`{.interpreted-text role="menuselection"} dashboard.

From here, products with lot numbers assigned to them will be listed by
default, and can be expanded to show the lot numbers those products have
assigned to them.

To group by lots, begin by removing any filters in the
`Search...`{.interpreted-text role="guilabel"} bar. Then, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(caret down)`{.interpreted-text role="guilabel"} icon to open a
drop-down menu of `Filters`{.interpreted-text role="guilabel"},
`Group By`{.interpreted-text role="guilabel"} options, and
`Favorites`{.interpreted-text role="guilabel"}. Under the
`Group By`{.interpreted-text role="guilabel"} section, click the
`Add Custom Group`{.interpreted-text role="guilabel"} option, and select
`Lot/Serial Number`{.interpreted-text role="guilabel"} from the
drop-down menu.

Doing so reorganizes all the records on the page to display all existing
lots and serial numbers, and can be expanded to show all quantities of
products with that assigned number.

{.align-center}

### Traceability report

To view a full stock moves report for a lot number, select the lot
number line from the `Lots/Serial Number`{.interpreted-text
role="guilabel"} dashboard. On the lot number form, click the
`Traceability`{.interpreted-text role="guilabel"} smart button.

{.align-center}

::: {.seealso}
`../product_tracking`{.interpreted-text role="doc"}
:::
