# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/barcode/operations/transfers_scratch.md

Create and process transfers with barcodes
==========================================

The *Barcode* app can be used to process internal transfers for all
types of products, including transfers for products tracked using lots
or serial numbers. Transfers can be created from scratch in real time
using an Odoo-compatible barcode scanner or the Odoo mobile app.

For a list of Odoo-compatible barcode mobile scanners, and other
hardware for the *Inventory* app, refer to the [Odoo Inventory •
Hardware page](https://www.odoo.com/app/inventory-hardware).

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

When the page has refreshed, new options are displayed under the
`Barcode Scanner`{.interpreted-text role="guilabel"} feature:
`Barcode Nomenclature`{.interpreted-text role="guilabel"} (with a
corresponding drop-down menu), where either
`Default Nomenclature`{.interpreted-text role="guilabel"} or
`Default GS1 Nomenclature`{.interpreted-text role="guilabel"} can be
selected. The nomenclature selected changes how scanners interpret
barcodes in Odoo.

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

Scan barcodes for internal transfers
------------------------------------

To create and process internal transfers for products in a warehouse,
the `Storage
Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} features **must**
be enabled.

To do so, go to the
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, scroll down to the
`Warehouse`{.interpreted-text role="guilabel"} section, and click the
checkboxes next to `Storage Locations`{.interpreted-text
role="guilabel"} and `Multi-Step Routes`{.interpreted-text
role="guilabel"}.

Then, click `Save`{.interpreted-text role="guilabel"} at the top of the
page to save changes.

### Create an internal transfer

To process existing internal transfers, there first needs to be an
internal transfer created, and an operation to process.

To create an internal transfer, navigate to the
`Inventory app`{.interpreted-text role="menuselection"}. From the
`Inventory Overview`{.interpreted-text role="guilabel"} dashboard,
locate the `Internal Transfers`{.interpreted-text role="guilabel"} card,
and click on the `0 To Process`{.interpreted-text role="guilabel"}
button.

Then, click `Create`{.interpreted-text role="guilabel"} in the top left
of the resulting page. This navigates to a new
`Internal Transfer`{.interpreted-text role="guilabel"} form.

On this blank form, the `Operation Type`{.interpreted-text
role="guilabel"} is automatically listed as `Internal
Transfers`{.interpreted-text role="guilabel"}. Under that field, the
`Source Location`{.interpreted-text role="guilabel"} and
`Destination Location`{.interpreted-text role="guilabel"} are set as
`WH/Stock`{.interpreted-text role="guilabel"} by default, but can be
changed to whichever locations the products are being moved from, and
moved to.

{.align-center}

Once the desired locations have been selected, products can be added to
the transfer. On the `Product`{.interpreted-text role="guilabel"} line
under the `Products`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select the
desired product(s) to add to the transfer.

Once ready, click `Save`{.interpreted-text role="guilabel"} at the top
of the form to save the new internal transfer. Once saved, click the
`Detailed Operations`{.interpreted-text role="guilabel"} icon (four
lines, at the far right of the `Product`{.interpreted-text
role="guilabel"} line) to open the
`Detailed Operations`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

From the pop-up, click `Add a line`{.interpreted-text role="guilabel"}.

Then, in the `To`{.interpreted-text role="guilabel"} column, change the
location from `WH/Stock`{.interpreted-text role="guilabel"} to a
different location, where the products should be moved.

Next, in the `Done`{.interpreted-text role="guilabel"} column, change
the quantity to the desired quantity to transfer. Once ready, click
`Confirm`{.interpreted-text role="guilabel"} to close out the pop-up
window.

### Scan barcodes for internal transfer

To process and scan barcodes for internal transfers, navigate to the
`Barcode app`{.interpreted-text role="menuselection"}.

Once inside the `Barcode app`{.interpreted-text role="guilabel"}, a
`Barcode Scanning`{.interpreted-text role="guilabel"} screen displaying
different options is presented.

To process internal transfers, click on the
`Operations`{.interpreted-text role="guilabel"} button at the bottom of
the screen. This navigates to an `Operations`{.interpreted-text
role="menuselection"} overview page.

{.align-center}

From this page, locate the `Internal Transfers`{.interpreted-text
role="guilabel"} card, and click the `# To
Process`{.interpreted-text role="guilabel"} button to view all
outstanding internal transfers. Then, select the desired operation to
process. This navigates to the barcode transfer screen.

::: {.note}
::: {.title}
Note
:::

When using the *Barcode* app without the *Inventory* app (**only** if
using a barcode scanner or the Odoo mobile app), the barcodes for each
transfer of a corresponding operation type can be scanned to be
processed easily.

Once scanned, the products that are part of an existing transfer can be
scanned, and new products can be added to the transfer, as well. Once
all products have been scanned, validate the transfer to proceed with
the stock moves.
:::

From this screen, an overview of all products to process within that
specific internal transfer (**WH/INT/000XX**) is shown. At the bottom of
the screen, there are options to `Add
Product`{.interpreted-text role="guilabel"} or
`Validate`{.interpreted-text role="guilabel"}, depending on if products
need to be added to the operation, or if the whole operation should be
validated at once.

{.align-center}

Then, scan the barcode of the product to process the internal transfer.

Or, to process and scan each product individually, choose a specific
product line. The `+ 1`{.interpreted-text role="guilabel"} button can be
clicked to add additional quantity of that product to the transfer, or
the `pencil icon`{.interpreted-text role="guilabel"} can be clicked to
open a new screen to edit that product line.

In the product\'s pop-up window, the product and the units to process is
displayed with a number pad. Under the product name, the
`Quantity`{.interpreted-text role="guilabel"} line can be edited. Change
the number in the line to the quantity listed to be transferred on the
internal transfer form.

::: {.example}
In the internal transfer operation [WH/INT/000XX]{.title-ref}, [50
Units]{.title-ref} of the [Transfer Product]{.title-ref} is moved from
[WH/Stock]{.title-ref} to [WH/Stock/Shelf 1]{.title-ref}.
[\[TRANSFER\_PROD\]]{.title-ref} is the `Internal
Reference`{.interpreted-text role="guilabel"} set on the product form.
Scan the barcode of the [Transfer Product]{.title-ref} to receive one
unit. Afterwards, click the `pencil icon`{.interpreted-text
role="guilabel"} to manually enter the transferred quantities.

{.align-center}
:::

Additionally, the `+1`{.interpreted-text role="guilabel"} and
`-1`{.interpreted-text role="guilabel"} buttons can be clicked to add or
subtract quantity of the product, and the number keys can be used to add
quantity, as well.

Below the number keys are the two `location`{.interpreted-text
role="guilabel"} lines, which read whichever locations were previously
specified on the internal transfer form, in this case
[WH/Stock]{.title-ref} and [WH/Stock/Shelf 1]{.title-ref}. Click these
lines to reveal a drop-down menu of additional locations to choose from.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the changes made to the product line.

Then, from the overview page with all products to process within that
transfer (**WH/INT/000XX**), click `Validate`{.interpreted-text
role="guilabel"}. The receipt has now been processed, and the *Barcode*
app can be closed out.

::: {.tip}
::: {.title}
Tip
:::

The *Barcode* app can also be used to scan products in internal
transfers containing unique lot numbers and serial numbers.

From the barcode transfer screen, scan the barcode of a lot or serial
number, and Odoo automatically increases the quantity of the product to
the quantity recorded in the database. If the same lot or serial number
is shared between different products, scan the product barcode first,
then the barcode of the lot/serial number.
:::

Create a transfer from scratch
------------------------------

In addition to processing and scanning barcodes for existing,
previously-created internal transfers, the *Barcode* app can also be
used to create transfers from scratch, simply by scanning a printed
operation type barcode.

::: {.admonition}
Did you know?

Odoo\'s *Barcode* application provides demo data with barcodes to
explore the features of the app. These can be used for testing purposes,
and can be printed from the home screen of the app. To access this demo
data, navigate to the `Barcode app`{.interpreted-text
role="menuselection"} and click `stock
barcodes sheet`{.interpreted-text role="guilabel"} (bolded and
highlighted in blue) in the information pop-up above the scanner.

{.align-center}
:::

To do this, first navigate to the `Barcode app`{.interpreted-text
role="menuselection"}. Once inside the *Barcode* app, a
`Barcode Scanning`{.interpreted-text role="guilabel"} screen displaying
different options is presented.

From this screen, when using a USB or bluetooth barcode scanner,
directly scan the product barcode.

When using a smartphone as the barcode scanner, click the
`Tap to Scan`{.interpreted-text role="guilabel"} button (next to the
camera icon, at the center of the screen). This opens a
`Barcode Scanner`{.interpreted-text role="guilabel"} pop-up screen that
enables the camera of the device being used.

Face the camera toward the printed operation type barcode to scan it.
Doing so processes the barcode, and navigates to a barcode transfer
screen.

From this screen, an overview of all products to process within that
specific internal transfer (**WH/INT/000XX**) is shown. Since this is a
new transfer created from scratch, however, there should not be any
products listed on the page.

To add products, scan the product barcode. If the barcode is not
available, manually enter the product into the system by clicking the
`Add Product`{.interpreted-text role="guilabel"} button at the bottom of
the screen, and add the products and product quantities that should be
transferred.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to
confirm the changes made to the product line.

{.align-center}

Then, from the overview page with all products to process within that
transfer (**WH/INT/000XX**), click `Validate`{.interpreted-text
role="guilabel"}. The internal transfer has now been processed, and the
*Barcode* app can be closed out.
