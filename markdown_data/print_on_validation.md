# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/print_on_validation.md

Printable delivery PDFs
=======================

Automatically print delivery-related PDFs documents and labels in Odoo,
containing package recipient details, contents, or handling
instructions.

The following PDFs can be configured to print upon validating an
*Inventory* operation (e.g. receipt, picking, delivery orders, quality
checks):

1.  `Delivery slip <inventory/shipping_receiving/delivery-slip>`{.interpreted-text
    role="ref"}
2.  `Return slip <inventory/shipping_receiving/return-slip>`{.interpreted-text
    role="ref"}
3.  `Product labels of items in the order <inventory/shipping_receiving/product-labels>`{.interpreted-text
    role="ref"}
4.  `Lot and serial number labels <inventory/shipping_receiving/lot-sn-labels>`{.interpreted-text
    role="ref"}
5.  `Carrier labels <inventory/shipping_receiving/carrier-labels>`{.interpreted-text
    role="ref"}
6.  `Export documents <inventory/shipping_receiving/export-doc>`{.interpreted-text
    role="ref"}
7.  `Package content <inventory/shipping_receiving/package-content>`{.interpreted-text
    role="ref"}
8.  `Package label <inventory/shipping_receiving/package-label>`{.interpreted-text
    role="ref"}

::: {#inventory/shipping_receiving/print_setup}
To automatically print these forms, navigate to
`Inventory app --> Configuration -->
Operations Types`{.interpreted-text role="menuselection"}, and select
the desired operation type.
:::

In the `Hardware`{.interpreted-text role="guilabel"} tab, tick each of
the desired options available in the `Print
on Validation`{.interpreted-text role="guilabel"} section to download
the PDF of those selected documents automatically after validating the
`Operation Type`{.interpreted-text role="guilabel"}. For details on what
each of the checkbox options do, jump to the related section.

{.align-center}

Delivery slip {#inventory/shipping_receiving/delivery-slip}
-------------

A *delivery slip* contains recipient and package details, usually placed
inside (or attached to) the package.

::: {.seealso}
\-
`Picking list <inventory/warehouses_storage/barcode_picking>`{.interpreted-text
role="ref"} -
`Tracking label <../setup_configuration/labels>`{.interpreted-text
role="doc"}
:::

After
`enabling the Delivery Slip setting <inventory/shipping_receiving/print_setup>`{.interpreted-text
role="ref"} in the `Hardware`{.interpreted-text role="guilabel"} tab
configuration options, clicking `Validate`{.interpreted-text
role="guilabel"} on the desired operation type downloads a PDF of the
delivery slip.

The delivery slip shows products, quantities, the delivery order
reference number, and the total order weight.

{.align-center}

Return slip {#inventory/shipping_receiving/return-slip}
-----------

Print a *return slip* to include in a delivery for customer return
packages. It identifies the return, links to the sales order, and
includes item details and customer information. It can also include
specific return instructions for the customer.

After
`enabling the Return Slip setting <inventory/shipping_receiving/print_setup>`{.interpreted-text
role="ref"} in the `Hardware`{.interpreted-text role="guilabel"} tab
configuration options, clicking `Validate`{.interpreted-text
role="guilabel"} on the desired operation type downloads a PDF of the
return slip.

The return slip displays the company\'s return address, along with
barcodes for both the order and the return operation.

{.align-center}

Product labels {#inventory/shipping_receiving/product-labels}
--------------

Print *product labels* to affix to items in an order, providing
essential information, such as product name, barcode, and price.

After navigating to the intended operation type
(`Inventory app --> Configuration -->
Operations Types`{.interpreted-text role="menuselection"}), in the
`Hardware`{.interpreted-text role="guilabel"} tab, tick the
`Product Labels`{.interpreted-text role="guilabel"} option.

Doing so makes the `Print label as:`{.interpreted-text role="guilabel"}
drop-down menu visible, where each product label can be printed as:

-   `2 x 7 with price`{.interpreted-text role="guilabel"}: PDF displays
    product name, barcode, and price, fitting two rows and seven columns
    of product labels per page.

    ::: {.spoiler}
    Example 2 x 7

    {.align-center}
    :::

-   `4 x 7 with price`{.interpreted-text role="guilabel"}: displays
    product name, barcode, and price, fitting four rows and seven
    columns of product labels per page.

    ::: {.spoiler}
    Example 4 x 7

    {.align-center}
    :::

-   `4 x 12`{.interpreted-text role="guilabel"}: displays product name
    and barcode. Fits four rows and twelve columns of product labels per
    page.

    ::: {.spoiler}
    Example 4 x 12

    {.align-center}
    :::

-   `4 x 12 with price`{.interpreted-text role="guilabel"}: displays
    product name, barcode, and price. Fits four rows and twelve columns
    of product labels per page.

-   `ZPL Labels`{.interpreted-text role="guilabel"}: prints labels in
    the Zebra Programming Language (ZPL) containing the product name and
    barcode. Readable for Zebra printers to automatically print labels.

-   `ZPL Labels with price`{.interpreted-text role="guilabel"}: prints
    labels in the `ZPL (Zebra Programming Language)`{.interpreted-text
    role="abbr"} containing the product name, barcode, and price.

::: {.note}
::: {.title}
Note
:::

Product labels can be manually printed from any delivery order, by
clicking the `Print
Labels`{.interpreted-text role="guilabel"} button.
:::

Lot/SN Labels {#inventory/shipping_receiving/lot-sn-labels}
-------------

Print *lot/SN labels* to affix to items in an order, providing essential
information, such as product name, lot or serial number, and the
barcode.

To automatically print this PDF, navigate to the intended operation
type\'s options page
(`Inventory app --> Configuration --> Operations Types`{.interpreted-text
role="menuselection"}). Then, in the `Hardware`{.interpreted-text
role="guilabel"} tab, tick the `Lot/SN Labels`{.interpreted-text
role="guilabel"} option.

Doing so makes the `Print label as:`{.interpreted-text role="guilabel"}
drop-down menu visible, where each product label can be printed as:

-   `4 x 12 - One per lot/SN`{.interpreted-text role="guilabel"}: PDF
    with labels for unique lot/serial numbers in the order, including
    product name, lot/serial number, and barcode. Fits four rows and
    twelve columns per page.

    ::: {.spoiler}
    Example 4 x 12 - One per lot/SN

    ![Labels for an order with only one unique set of lot/serial
    numbers.](print_on_validation/four-twelve-lots.png){.align-center}
    :::

-   `4 x 12 - One per unit`{.interpreted-text role="guilabel"}: PDF with
    labels matching the quantity of items, displaying the product name,
    lot/serial number, and barcode. Fits four rows and twelve columns
    per page.

-   `ZPL Labels - One per lot/SN`{.interpreted-text role="guilabel"}:
    prints labels in `ZPL (Zebra Programming
    Language)`{.interpreted-text role="abbr"}, containing the product
    name, lot/serial number, and barcode.

-   `ZPL Labels - One per unit`{.interpreted-text role="guilabel"}:
    prints labels with the quantity of items in `ZPL
    (Zebra Programming Language)`{.interpreted-text role="abbr"},
    containing the product name, lot/serial number, and barcode.

Carrier labels {#inventory/shipping_receiving/carrier-labels}
--------------

To automatically print a *carrier label* with the recipient address,
tracking number, and carrier details for specific third-party shipping
carriers, complete the following setup:

1.  Tick the `Carrier Labels`{.interpreted-text role="guilabel"}
    checkbox in the `operation type settings
    <inventory/shipping_receiving/print_setup>`{.interpreted-text
    role="ref"}.
2.  `Connect a printer <../../../../general/iot/devices/printer>`{.interpreted-text
    role="doc"} to Odoo\'s *IoT* app.
3.  `Assign the carrier label to the printer <inventory/shipping_receiving/assign-printer>`{.interpreted-text
    role="ref"}.
4.  Configure the shipping method\'s
    `label type <inventory/shipping_receiving/label-type>`{.interpreted-text
    role="ref"}.

### Assign printer {#inventory/shipping_receiving/assign-printer}

Refer to the
`Connect a printer <../../../../general/iot/devices/printer>`{.interpreted-text
role="doc"} documentation for details on connecting a printer to Odoo\'s
*IoT* app. Upon completion, assign the carrier label to the printer, by
navigating to `IoT app --> Devices`{.interpreted-text
role="menuselection"}, and selecting the desired printer.

{.align-center}

In the printer configuration form, go to the
`Printer Reports`{.interpreted-text role="guilabel"} tab to configure
the types of documents the printer automatically prints. Click
`Add a line`{.interpreted-text role="guilabel"} to open the
`Add: Reports`{.interpreted-text role="guilabel"} pop-up window. In the
`Search...`{.interpreted-text role="guilabel"} bar, type
[Shipping]{.title-ref}, and select `Shipping Labels`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Shipping Documents`{.interpreted-text role="guilabel"} report is
for `export documents
<inventory/shipping_receiving/export-doc>`{.interpreted-text
role="ref"}.
:::

{.align-center}

After adding the `Shipping Labels`{.interpreted-text role="guilabel"}
report in the `Printer Reports`{.interpreted-text role="guilabel"} tab,
ensure the `Report Type`{.interpreted-text role="guilabel"} matches the
IoT-connected printer\'s type.

-   For laser printers, set the `Report Type`{.interpreted-text
    role="guilabel"} to `PDF`{.interpreted-text role="guilabel"}.
-   For Zebra printers, set the `Report Type`{.interpreted-text
    role="guilabel"} to `Text`{.interpreted-text role="guilabel"}.

### Shipping carrier label type {#inventory/shipping_receiving/label-type}

Next, complete the setup for the `third-party shipping connector
<../setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"}. After that, go to `Inventory app -->
Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}, and select the desired shipping method.

On the shipping method configuration form, in the
`[carrier name] Configuration`{.interpreted-text role="guilabel"} tab,
ensure the `Label Format`{.interpreted-text role="guilabel"} matches the
`report type assigned earlier
<inventory/shipping_receiving/assign-printer>`{.interpreted-text
role="ref"}:

-   For laser printers, set the `Label Format`{.interpreted-text
    role="guilabel"} to `PDF`{.interpreted-text role="guilabel"}.
-   For Zebra printers, set the `Label Format`{.interpreted-text
    role="guilabel"} to `ZPL2`{.interpreted-text role="guilabel"}.

{.align-center}

### Example carrier label

After validating the operation, the carrier label is generated in the
chatter, and printed using the IoT-connected printer.

::: {.spoiler}
Example carrier label

![Carrier label for FedEx, containing the recipient address, tracking
number, barcode, and other shipping
information.](print_on_validation/fedex-carrier-label.png){.align-center}
:::

::: {.seealso}
`Print carrier labels <../setup_configuration/labels>`{.interpreted-text
role="doc"}
:::

Export document {#inventory/shipping_receiving/export-doc}
---------------

An *export document*, required by customs to ship packages from one
country to another, can be automatically printed in Odoo by following
these steps:

1.  Tick the `Export Documents`{.interpreted-text role="guilabel"}
    checkbox in the `operation type settings
    <inventory/shipping_receiving/print_setup>`{.interpreted-text
    role="ref"}.
2.  `Connect a printer <../../../../general/iot/devices/printer>`{.interpreted-text
    role="doc"} to Odoo\'s *IoT* app.
3.  Assign the export document to the printer.

### Assign printer

Similar to the `printer assignment instructions for carrier labels
<inventory/shipping_receiving/assign-printer>`{.interpreted-text
role="ref"}, after connecting a compatible printer to the Odoo *IoT*
app, go to `IoT app --> Devices`{.interpreted-text
role="menuselection"}, and select the desired printer.

In the printer configuration form, go to the
`Printer Reports`{.interpreted-text role="guilabel"} tab, and click
`Add a line`{.interpreted-text role="guilabel"}. In the
`Add: Reports`{.interpreted-text role="guilabel"} pop-up window that
appears, add the `Shipping Documents`{.interpreted-text role="guilabel"}
report to assign the export document to the printer.

::: {.spoiler}
Example export document

![Export document for a shipment from the USA to
Belgium.](print_on_validation/export-doc.png){.align-center}
:::

Package content {#inventory/shipping_receiving/package-content}
---------------

A *package content* PDF includes the package\'s barcode, packed date,
along with a list of contained products and quantities.

To print this form automatically, go to
`Inventory app --> Configuration -->
Operation Types`{.interpreted-text role="menuselection"}, and select the
desired operation type. Then, go to the `Hardware`{.interpreted-text
role="guilabel"} tab, and tick the `Package Contents`{.interpreted-text
role="guilabel"} checkbox.

::: {.important}
::: {.title}
Important
:::

If the option is not available, enable the `Packages
<../../product_management/configure/package>`{.interpreted-text
role="doc"} feature, by going to `Inventory app
--> Configuration --> Settings`{.interpreted-text role="menuselection"},
ticking the `Packages`{.interpreted-text role="guilabel"} checkbox, and
clicking `Save`{.interpreted-text role="guilabel"}.
:::

After enabling the feature in the `Hardware`{.interpreted-text
role="guilabel"} tab, validating the operation prints a PDF of the
package contents.

::: {.spoiler}
Example package content PDF

![Package contents showing the package contents, barcode, and pack
date.](print_on_validation/package-content.png){.align-center}
:::

Package label {#inventory/shipping_receiving/package-label}
-------------

A *package label* that shows the package\'s barcode and pack date can be
configured to print upon clicking the *Put in Pack* button.

::: {.important}
::: {.title}
Important
:::

The `Put in Pack`{.interpreted-text role="guilabel"} button is available
**only** when the `Packages
<../../product_management/configure/package>`{.interpreted-text
role="doc"} feature is enabled in
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

After it is enabled, the `Put in Pack`{.interpreted-text
role="guilabel"} button is available on all inventory operations (e.g.
receipt, pickings, internal transfers, delivery orders, etc.).
:::

To automatically print the package label when the
`Put in Pack`{.interpreted-text role="guilabel"} button is clicked, go
to
`Inventory app --> Configuration --> Operation Types`{.interpreted-text
role="menuselection"}. Select the desired operation type, and tick the
`Package Label`{.interpreted-text role="guilabel"} checkbox in the
`Hardware`{.interpreted-text role="guilabel"} tab. Labels can be printed
in `PDF`{.interpreted-text role="guilabel"} or `ZPL`{.interpreted-text
role="guilabel"} file formats, as defined in the `Print label
as`{.interpreted-text role="guilabel"} field.

::: {.spoiler}
Example of package barcode

{.align-center}
:::
