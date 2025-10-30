# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/barcode/operations/receipts_deliveries.md

Process receipts and deliveries with barcodes
=============================================

::: {#barcode/operations/intro}
The *Barcode* app can be used to process receipts, deliveries, and other
types of operations in real time using a barcode scanner or the Odoo
mobile app.
:::

This makes it possible to process operations on the warehouse floor when
they happen, instead of having to wait to validate transfers from a
computer. Processing operations this way can help to properly attribute
barcodes to the appropriate products, pickings, locations, and more.

Enable Barcode app
------------------

To use the *Barcode* app to process transfers, it must be installed by
enabling the feature from the settings of the *Inventory* app.

To do so, go to the
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, scroll down to the
`Barcode`{.interpreted-text role="guilabel"} section, and click the
checkbox next to the `Barcode Scanner`{.interpreted-text
role="guilabel"} feature.

Once the checkbox is ticked, click `Save`{.interpreted-text
role="guilabel"} at the top of the page to save changes.

Once the page has refreshed, new options will be displayed under the
`Barcode Scanner`{.interpreted-text role="guilabel"} feature:
`Barcode Nomenclature`{.interpreted-text role="guilabel"} (with a
corresponding drop-down menu), where either
`Default Nomenclature`{.interpreted-text role="guilabel"} or
`Default GS1 Nomenclature`{.interpreted-text role="guilabel"} can be
selected.

There is also a `Configure Product Barcodes`{.interpreted-text
role="guilabel"} internal link arrow, and a set of
`Print`{.interpreted-text role="guilabel"} buttons for printing barcode
commands and a barcode demo sheet.

{.align-center}

For more on setting up and configuring the `Barcode`{.interpreted-text
role="guilabel"} app, refer to the `Set up your
barcode scanner <../setup/hardware>`{.interpreted-text role="doc"} and
`Activate the Barcodes in Odoo <../setup/software>`{.interpreted-text
role="doc"} documentation pages.

Scan barcodes for receipts {#barcode/operations/scan-received-products}
--------------------------

To process warehouse receipts for incoming products, there first needs
to be a purchase order (PO) created, and a receipt operation to process.

To create a `PO (purchase order)`{.interpreted-text role="abbr"},
navigate to the `Purchase app --> Create`{.interpreted-text
role="menuselection"} to create a new request for quotation (RFQ).

From the blank `RFQ (request for quotation)`{.interpreted-text
role="abbr"} form, click the drop-down menu next to the
`Vendor`{.interpreted-text role="guilabel"} field to add a vendor. Then,
on the `Product`{.interpreted-text role="guilabel"} line under the
`Products`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select the
desired product(s) to add to the quotation.

Once ready, click `Save`{.interpreted-text role="guilabel"} at the top
of the form, then click `Confirm Order`{.interpreted-text
role="guilabel"} to confirm the
`RFQ (request for quotation)`{.interpreted-text role="abbr"} to a
`PO (purchase order)`{.interpreted-text role="abbr"}.

{.align-center}

To process and scan barcodes for warehouse receipts, navigate to the
`Barcode app`{.interpreted-text role="menuselection"}.

Once inside the `Barcode app`{.interpreted-text role="guilabel"}, a
`Barcode Scanning`{.interpreted-text role="guilabel"} screen displaying
different options is presented. To process receipts, click on the
`Operations`{.interpreted-text role="guilabel"} button at the bottom of
the screen. This navigates to an `Operations`{.interpreted-text
role="menuselection"} overview page.

{.align-center}

From this page, locate the `Receipts`{.interpreted-text role="guilabel"}
card, and click the `# To Process`{.interpreted-text role="guilabel"}
button to view all outstanding receipts. Then, select the desired
receipt operation to process. This navigates to the barcode transfer
screen.

::: {.note}
::: {.title}
Note
:::

If *only* using a barcode scanner or the Odoo mobile app, the barcodes
for each transfer of a corresponding operation type can be scanned to be
processed easily. Once scanned, the products that are part of an
existing transfer can be scanned, and new products can be added to the
transfer, as well. Once all products have been scanned, validate the
transfer to proceed with the stock moves.
:::

From this screen, an overview of all receipts to process within that
transfer (**WH/IN/000XX**) is shown. At the bottom of the screen, there
are options to `Add Product`{.interpreted-text role="guilabel"} or
`Validate`{.interpreted-text role="guilabel"}, depending on if products
need to be added to the operation, or if the whole operation should be
validated at once.

{.align-center}

To process and scan each product individually, choose a specific product
line. The `+#`{.interpreted-text role="guilabel"} button (in this case,
`+10`{.interpreted-text role="guilabel"}) can be clicked to indicate
receipt of that product, or the `pencil`{.interpreted-text
role="guilabel"} icon can be clicked to open a new screen to edit that
product line.

From this screen, the product that\'s being received is listed. Under
the product name, the `Quantity`{.interpreted-text role="guilabel"} line
can be edited. Either change the [0]{.title-ref} in the line to the
desired quantity, or click the `/# Units`{.interpreted-text
role="guilabel"} button (in this case, `/10 Units`{.interpreted-text
role="guilabel"}) to automatically fill the quantity ordered from the
`PO (purchase order)`{.interpreted-text role="abbr"}.

::: {.example}
In the reception operation [WH/IN/00019]{.title-ref}, [10
Units]{.title-ref} of the [Barcode Product]{.title-ref} is expected to
be received. [\[BARCODE\_PROD\]]{.title-ref} is the
`Internal Reference`{.interpreted-text role="guilabel"} set on the
product form. Scan the barcode of the [Barcode Product]{.title-ref} to
receive one unit. Afterwards, click the `pencil`{.interpreted-text
role="guilabel"} icon to manually enter the received quantities.

{.align-center}
:::

Additionally, the `+1`{.interpreted-text role="guilabel"} and
`-1`{.interpreted-text role="guilabel"} buttons can be clicked to add or
subtract quantity of the product, and the
`number keys`{.interpreted-text role="guilabel"} can be used to add
quantity, as well.

Below the `number keys`{.interpreted-text role="guilabel"} is the
`location`{.interpreted-text role="guilabel"} line, which reads
[WH/Stock]{.title-ref} by default, unless another *location* is listed
on the product itself. Click this line to reveal a drop-down menu of
additional locations to choose from.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the changes made to the product line.

Then, from the overview page with all receipts to process within that
transfer (**WH/IN/000XX**), click the `+#`{.interpreted-text
role="guilabel"} button on the product line for the products being
received, and click `Validate`{.interpreted-text role="guilabel"}. The
receipt has now been processed, and the `Barcode app`{.interpreted-text
role="guilabel"} can be closed out.

{.align-center}

Scan barcodes for delivery orders
---------------------------------

To process warehouse deliveries for outgoing products, there first needs
to be a sales order (SO) created, and a delivery operation to process.

To create a `SO (sales order)`{.interpreted-text role="abbr"}, navigate
to the `Sales app --> Create`{.interpreted-text role="menuselection"} to
create a new quotation.

From the blank quotation form, click the drop-down menu next to the
`Customer`{.interpreted-text role="guilabel"} field to add a customer.
Then, on the `Product`{.interpreted-text role="guilabel"} line under the
`Order Lines`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select the
desired product(s) to add to the quotation.

Once ready, click `Save`{.interpreted-text role="guilabel"} at the top
of the form, and click `Confirm Order`{.interpreted-text
role="guilabel"} to confirm the quotation to a
`SO (sales order)`{.interpreted-text role="abbr"}.

{.align-center}

To process and scan barcodes for warehouse deliveries, navigate to the
`Barcode app`{.interpreted-text role="menuselection"}.

Once inside the `Barcode app`{.interpreted-text role="guilabel"}, a
`Barcode Scanning`{.interpreted-text role="guilabel"} screen displaying
different options is presented. To process deliveries, click on the
`Operations`{.interpreted-text role="guilabel"} button at the bottom of
the screen. This navigates to an `Operations`{.interpreted-text
role="guilabel"} overview page.

From this page, locate the `Delivery Orders`{.interpreted-text
role="guilabel"} card, and click the `# To Process`{.interpreted-text
role="guilabel"} button to view all outstanding deliveries. Then, select
the desired delivery order to process. This navigates to the barcode
transfer screen.

{.align-center}

From this screen, an overview of all deliveries to process within that
transfer (**WH/OUT/000XX**) is shown. At the bottom of the screen, there
are options to `Add Product`{.interpreted-text role="guilabel"} or
`Validate`{.interpreted-text role="guilabel"}, depending on if products
need to be added to the operation, or if the whole operation should be
validated at once.

To process and scan each product individually, choose a specific product
line. The `+1`{.interpreted-text role="guilabel"} button can be clicked
to indicate delivery of that product, or the
`pencil icon`{.interpreted-text role="guilabel"} can be clicked to open
a new screen to edit that product line.

From this screen, the product that\'s being delivered is listed. Under
the product name, the `Quantity`{.interpreted-text role="guilabel"} line
can be edited. Either change the [0]{.title-ref} in the line to the
desired quantity, or click the `/# Units`{.interpreted-text
role="guilabel"} button (in this case, `/10 Units`{.interpreted-text
role="guilabel"}) to automatically fill the quantity ordered from the
`SO (sales order)`{.interpreted-text role="abbr"}.

Additionally, the `+1`{.interpreted-text role="guilabel"} and
`-1`{.interpreted-text role="guilabel"} buttons can be clicked to add or
subtract quantity of the product, and the
`number keys`{.interpreted-text role="guilabel"} can be used to add
quantity, as well.

Below the `number keys`{.interpreted-text role="guilabel"} is the
`location`{.interpreted-text role="guilabel"} line, which reads
[WH/Stock]{.title-ref} by default, unless another location is listed on
the product itself.

This is the location that the product is being pulled from for delivery.
Click this line to reveal a drop-down menu of additional locations to
choose from (if this product is stored in multiple locations in the
warehouse).

::: {.tip}
::: {.title}
Tip
:::

For warehouses that have multiple different storage locations, putaway
rules, and removal strategies, additional steps can be added for various
operation types, while using the *Barcode* app.
:::

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the changes made to the product line.

Then, from the overview page with all receipts to process within that
transfer (**WH/OUT/000XX**), click the `+#`{.interpreted-text
role="guilabel"} button on the product line for the products being
received, and click `Validate`{.interpreted-text role="guilabel"}. The
delivery has now been processed, and the *Barcode* app can be closed
out.

{.align-center}
