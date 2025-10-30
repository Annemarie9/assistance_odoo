# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/barcode/operations/gs1_usage.md

GS1 barcode usage
=================

::: {#barcode/operations/gs1_usage}
GS1 barcodes provide a standardized format that barcode scanners can
interpret. They encode information in a
`specific structure recognized globally <barcode/operations/gs1>`{.interpreted-text
role="ref"}, allowing scanners to understand and process supply chain
data consistently.
:::

Odoo *Barcode* interprets and prints GS1 barcodes, automating product
identification and tracking in warehouse operations such as receiving,
picking, and shipping.

The following sections contain examples of how Odoo uses GS1 barcodes
provided by the business to identify common warehouse items and automate
certain warehouse workflows.

::: {.important}
::: {.title}
Important
:::

Odoo **does not** create GS1 barcodes. Businesses must purchase a unique
Global Trade Item Number (GTIN) from GS1. Then, they can combine their
existing GS1 barcodes with product and supply chain information (also
provided by GS1) to create barcodes in Odoo.
:::

::: {.seealso}
\-  -
`GS1 nomenclature <barcode/operations/gs1>`{.interpreted-text
role="ref"}
:::

Configure barcodes for product, quantity, and lots {#barcode/operations/gs1-lots}
--------------------------------------------------

To build a GS1 barcode that contains information about a product, its
quantities, and the lot number, the following barcode patterns and
Application Identifiers (A.I.) are used:

  ------------------------------------------------------------------------------------------------------
  Name       Rule Name       A.I.   Barcode Pattern                        Field in Odoo
  ---------- --------------- ------ -------------------------------------- -----------------------------
  Product    Global Trade    01     (01)(\\d{14})                          `Barcode`{.interpreted-text
             Item Number                                                   role="guilabel"} field on
             (GTIN)                                                        product form

  Quantity   Variable count  30     (30)(\\d{0,8})                         `Units`{.interpreted-text
             of items                                                      role="guilabel"} field on
                                                                           transfer form

  Lot Number Batch or lot    10     (10)(\[!\"%-/0-9:-?A-Z\_a-z\]{0,20})   `Lot`{.interpreted-text
             number                                                        role="guilabel"} on Detailed
                                                                           Operations pop-up
  ------------------------------------------------------------------------------------------------------

### Configuration {#barcode/operations/lot-setup}

First,
`enable product tracking using lots <inventory/management/track_products_by_lots>`{.interpreted-text
role="ref"} by navigating to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and checking the box for
`Lots & Serial Numbers`{.interpreted-text role="guilabel"} under the
`Traceability`{.interpreted-text role="guilabel"} heading.

Then, set up the product barcode by navigating to the intended product
form in `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"} and selecting the product. On the product form,
click `Edit`{.interpreted-text role="guilabel"}. Then, in the
`General Information`{.interpreted-text role="guilabel"} tab, fill in
the `Barcode`{.interpreted-text role="guilabel"} field with the unique
14-digit [Global Trade Item Number
(GTIN)](https://www.gs1.org/standards/get-barcodes), which is a
universally recognized identifying number that is provided by GS1.

::: {.important}
::: {.title}
Important
:::

On the product form, omit the
`A.I. (Application Identifier)`{.interpreted-text role="abbr"}
[01]{.title-ref} for `GTIN (Global Trade Item Number)`{.interpreted-text
role="abbr"} product barcode pattern, as it is only used to encode
multiple barcodes into a single barcode that contains detailed
information about the package contents.
:::

::: {.example}
To record the GS1 barcode for the product, [Fuji Apple]{.title-ref},
enter the 14-digit `GTIN (Global Trade Item Number)`{.interpreted-text
role="abbr"} [20611628936004]{.title-ref} in the
`Barcode`{.interpreted-text role="guilabel"} field on the product form.

{.align-center}
:::

::: {.tip}
::: {.title}
Tip
:::

To view a list of *all* products and their corresponding barcodes in the
Odoo database, navigate to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Barcode`{.interpreted-text
role="guilabel"} heading, click on the
`Configure Product Barcodes`{.interpreted-text role="guilabel"} button
under the `Barcode
Scanner`{.interpreted-text role="guilabel"} section. Enter the 14-digit
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"} into
the `Barcode`{.interpreted-text role="guilabel"} column, then click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}
:::

::: {#barcode/operations/lot-setup-on-product}
After activating tracking by lots and serial numbers from the settings
page, specify that this feature is to be applied on each product by
navigating to the `Inventory`{.interpreted-text role="guilabel"} tab on
the product form. Under `Tracking`{.interpreted-text role="guilabel"},
choose the `By Lots`{.interpreted-text role="guilabel"} radio button.
:::

{.align-center}

### Scan barcode on receipt

To ensure accurate lot interpretation in Odoo on product barcodes
scanned during a receipt operation, navigate to the
`Barcode`{.interpreted-text role="menuselection"} app to manage the
`receipt picking process
<barcode/operations/scan-received-products>`{.interpreted-text
role="ref"}.

From the `Barcode Scanning`{.interpreted-text role="guilabel"}
dashboard, click the `Operations`{.interpreted-text role="guilabel"}
button, then the `Receipts`{.interpreted-text role="guilabel"} button to
view the list of vendor receipts to process. Receipts generated from
`POs (Purchase Orders)`{.interpreted-text role="abbr"} are listed, but
new receipt operations can also be created directly through the
`Barcode`{.interpreted-text role="menuselection"} app using the
`Create`{.interpreted-text role="guilabel"} button.

On the list of receipts, click on the warehouse operation
([WH/IN]{.title-ref}) and scan product barcodes and lot numbers with a
barcode scanner. The scanned product then appears on the list. Use the
`✏️ (pencil)`{.interpreted-text role="guilabel"} button to open a window
and manually enter quantities for specific lot numbers.

::: {.example}
After placing a `PO (Purchase Order)`{.interpreted-text role="abbr"} for
fifty apples, navigate to the associated receipt in the *Barcode* app.

Scan the barcode containing the
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"},
quantity, and lot number. For testing with a barcode scanner, below is
an example barcode for the fifty Fuji apples in Lot 2.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  50 Fuji apples in Lot0002                           
  --------------------------------------------------- ---------------------------------------------------------------------------------------------------------------
  2D Matrix                                           

  `A.I. (Application Identifier)`{.interpreted-text   01
  role="abbr"} (product)                              

  GS1 Barcode (product)                               20611628936004

  `A.I. (Application Identifier)`{.interpreted-text   30
  role="abbr"} (quantity)                             

  GS1 Barcode (quantity)                              00000050

  `A.I. (Application Identifier)`{.interpreted-text   10
  role="abbr"} (lot)                                  

  GS1 Barcode (lot \#)                                LOT0002

  Full GS1 barcode                                    0120611628936004 3000000050 10LOT0002
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

`If the configuration is correct <barcode/operations/troubleshooting>`{.interpreted-text
role="ref"}, [50/50]{.title-ref} `Units`{.interpreted-text
role="guilabel"} processed will be displayed and the
`Validate`{.interpreted-text role="guilabel"} button turns green. Click
the `Validate`{.interpreted-text role="guilabel"} button to complete the
reception.

{.align-center}
:::

Configure barcode for product and non-unit quantity {#barcode/operations/quantity-ex}
---------------------------------------------------

To build a GS1 barcode that contains products measured in a non-unit
quantity, like kilograms, for example, the following barcode patterns
are used:

  ------------------------------------------------------------------------------------------------
  Name        Rule Name          A.I.         Barcode Pattern        Field in Odoo
  ----------- ------------------ ------------ ---------------------- -----------------------------
  Product     Global Trade Item  01           (01)(\\d{14})          `Barcode`{.interpreted-text
              Number (GTIN)                                          role="guilabel"} field on
                                                                     product form

  Quantity in Variable count of  310\[0-5\]   (310\[0-5\])(\\d{6})   `Units`{.interpreted-text
  kilograms   items                                                  role="guilabel"} field on
                                                                     transfer form
  ------------------------------------------------------------------------------------------------

### Scan barcode on receipt

To confirm that quantities are correctly interpreted in Odoo, place an
order in the *Purchase* app using the appropriate unit of measure
(`UoM`{.interpreted-text role="guilabel"}) for the quantity of products
to be purchased.

::: {.seealso}
`Simplify vendor unit conversions with UoMs
<inventory/product_replenishment/unit-conversion>`{.interpreted-text
role="ref"}
:::

After the order is placed, navigate to the `Barcode`{.interpreted-text
role="menuselection"} app to `receive the vendor
shipment <barcode/operations/scan-received-products>`{.interpreted-text
role="ref"}.

::: {.example}
On the receipt in the *Barcode* app, receive an order for [52.1
kg]{.title-ref} of peaches by scanning the barcode containing the
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"} and
quantity of peaches in kilograms.

  ---------------------------------------------------------------------------------------------------------------------------------------
  52.1 kg of Peaches                                  
  --------------------------------------------------- -----------------------------------------------------------------------------------
  2D Matrix                                           

  `A.I. (Application Identifier)`{.interpreted-text   01
  role="abbr"} (product)                              

  GS1 Barcode (product)                               00614141000012

  `A.I. (Application Identifier)`{.interpreted-text   3101
  role="abbr"} (kg, 1 decimal point)                  

  GS1 Barcode (quantity)                              000521

  Full GS1 barcode                                    0100614141000012 3101000521
  ---------------------------------------------------------------------------------------------------------------------------------------

`If the configuration is correct <barcode/operations/troubleshooting>`{.interpreted-text
role="ref"}, [52.1 / 52.1]{.title-ref} `kg`{.interpreted-text
role="guilabel"} will be displayed and the `Validate`{.interpreted-text
role="guilabel"} button turns green. Finally, press
`Validate`{.interpreted-text role="guilabel"} to complete the
validation.

{.align-center}
:::

Verify product moves
--------------------

For additional verification, the quantities of received products are
also recorded on the `Product Moves`{.interpreted-text role="guilabel"}
report, accessible by navigating to `Inventory app -->
Reporting --> Product Moves`{.interpreted-text role="menuselection"}.

The items on the `Product Moves`{.interpreted-text role="guilabel"}
report are grouped by product by default. To confirm the received
quantities, click on a product line to open its collapsible drop-down
menu, which displays a list of *stock move lines* for the product. The
latest stock move matches the warehouse reception reference number (e.g.
[WH/IN/00013]{.title-ref}) and quantity processed in the barcode scan,
demonstrating that the records processed in the *Barcode* app were
properly stored in *Inventory*.

{.align-center}
