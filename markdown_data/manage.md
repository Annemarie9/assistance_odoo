How to list a product?
======================

::: {#ebay-connector/listing}
In order to list a product on eBay and Odoo there are two methods in
Odoo to do so:
:::

1.  (*Preferred method*) Make a product in Odoo and list the item eBay.
    -   Click `List Item on eBay`{.interpreted-text role="guilabel"} in
        the top menu of the product template. The product template can
        be accessed by navigating to
        `Sales app --> Products --> Product`{.interpreted-text
        role="menuselection"} and selecting the individual product.
2.  (*Less preferred method*) List the item on eBay, then create the
    product in Odoo, and finally link product to the item on eBay.
    -   Click `Link With Existing eBay Listing`{.interpreted-text
        role="guilabel"} in the top menu on the product template.The
        product template can be accessed by navigating to
        `Sales app --> Product -->
        Product`{.interpreted-text role="menuselection"} and selecting
        the individual product.

::: {.note}
::: {.title}
Note
:::

If an order comes in and the listing from the order is not linked to a
product, eBay will create a consumable product.product in its place.
These consumables should be altered on the *sales order* while in draft
state to represent a storable product, and then the user can link to the
listing as they come in.
:::

::: {.seealso}
To learn more about the eBay connector visit these pages as well:

-   `setup`{.interpreted-text role="doc"}
-   `linking_listings`{.interpreted-text role="doc"}
-   `troubleshooting`{.interpreted-text role="doc"}
:::

Listing without variation
-------------------------

Access the product template by navigating to
`Sales app --> Products --> Product`{.interpreted-text
role="menuselection"} and selecting the individual product.

In order to list a product, select the `Sell on eBay`{.interpreted-text
role="guilabel"} field on a product template.
`Sell on eBay`{.interpreted-text role="guilabel"} is either in an
`eBay`{.interpreted-text role="guilabel"} tab or under the `Product
name`{.interpreted-text role="guilabel"}. Click `Save`{.interpreted-text
role="guilabel"} if necessary.

{.align-center}

When the `Use Stock Quantity`{.interpreted-text role="guilabel"} field
is checked, the quantity set on eBay is the Odoo *Forecast Quantity*
(Odoo *Inventory* app).

The policies need to be set in order to be able to list on eBay. A value
must be selected for the following fields
`Payment Policy`{.interpreted-text role="guilabel"},
`Return Policy`{.interpreted-text role="guilabel"}, and `Shipping
Policy`{.interpreted-text role="guilabel"}. The options are imported
from the eBay database. If no option appears, they can be imported by
navigating to
`Sales app --> Configuration --> Settings --> eBay`{.interpreted-text
role="menuselection"}, and clicking on the `Policies`{.interpreted-text
role="guilabel"} button in the `Synchronization`{.interpreted-text
role="guilabel"} field. This button **only** appears once the production
and sandbox credentials have been set.

The `Description Template`{.interpreted-text role="guilabel"} allows the
administrator to use templates in listings. The default template only
uses the `eBay Description`{.interpreted-text role="guilabel"} field of
the product. HTML can be used inside the
`Description Template`{.interpreted-text role="guilabel"}, and in the
`eBay Description`{.interpreted-text role="guilabel"} in Odoo 14.
Starting in Odoo 15, the powerbox feature is available to use in the
template and description. Simply type a forward slash [/]{.title-ref} to
reveal a menu with formatting, layout, and text options. To add an
image, type [/image]{.title-ref}.

To use images in the listing, an image needs to be added as one of the
*Attachments* on the product template.

::: {.seealso}
For more information on template configuration in Odoo visit:
`../../../general/companies/email_template`{.interpreted-text
role="doc"}.
:::

Listing with variations
-----------------------

When the `Sell on eBay`{.interpreted-text role="guilabel"} is checked on
a product containing variations with `Fixed Price`{.interpreted-text
role="guilabel"} as `Listing Type`{.interpreted-text role="guilabel"},
the eBay form is slightly different. Go to the
`Variants`{.interpreted-text role="guilabel"} tab to or click
`Configure Variants`{.interpreted-text role="guilabel"} in the top menu
to configure the variant settings. Pricing can be configured for each
variation.

When the `Listing Type`{.interpreted-text role="guilabel"} is changed to
`Fixed Price`{.interpreted-text role="guilabel"}, Odoo presents a
variant table at the bottom of the `eBay`{.interpreted-text
role="guilabel"} tab, in which the `Fixed Price`{.interpreted-text
role="guilabel"} can be entered, and the decision to
`Publish on eBay`{.interpreted-text role="guilabel"} can be made for
specific variants, along with other options.

{.align-center}

Product identifiers
-------------------

Products identifiers such as EAN, UPC, Brand or MPN are required in most
of the eBay categories.

### EAN and UPC identifiers

The module manages the EAN and UPC identifiers with the
`Barcode`{.interpreted-text role="guilabel"} field of the product
variant. If the `Barcode`{.interpreted-text role="guilabel"} field is
empty or is value is not valid, the EAN and UPC values will be set as
\'Does not apply\' as recommended by eBay.

Barcodes can be found on the product template, under the the
`General Information`{.interpreted-text role="guilabel"} tab. Access the
product template, first, by navigating to `Sales app --> Products -->
Product`{.interpreted-text role="menuselection"} and selecting the
individual product.

### Listing with item specifics

In order to add item specifics, one should create a product attribute
with a single value in the `Attributes & Variants`{.interpreted-text
role="guilabel"} tab on the product form. Examples of item specifics
include: [MPN]{.title-ref} or [Brand]{.title-ref}. The Brand and MPN
values are working as item specifics and should be defined in the
`Attributes & Variants`{.interpreted-text role="guilabel"} tab on the
product form. If these values are not set, \'Does not apply\' will be
used for the eBay listing.

Process invoices and payments
-----------------------------

### Posting payment

When eBay orders are placed they are always paid for up front, via the
eBay site. At no point will users pay for items on eBay through Odoo.
Therefore, once orders are synced into Odoo from eBay they are already
paid for. Odoo\'s invoicing and payment functionalities are not
utilized. However, invoices need to be created and marked as Paid to
"close" the *Sales Order*.

Users can opt to mass create and post invoices in batches. To do so,
navigate to Quotations in the list view by going to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}. In the upper right corner, select the list view
icon. Hover over the icons to reveal the name of each. Then check the
boxes on the left that invoices should be made for and go to the
`Action`{.interpreted-text role="guilabel"} menu or ⚙️ \[Gear icon\] .
Click on `Create Invoices`{.interpreted-text role="guilabel"}.

A pop-up will appear and click on the
`Create and view invoice`{.interpreted-text role="guilabel"} button. A
new screen will populate with the newly created invoices. Next, select
all of them by clicking on the box icon next to
`Number`{.interpreted-text role="guilabel"} in the header row of the
list, this will select all the records. Then navigate to the
`Action`{.interpreted-text role="guilabel"} menu and click
`Post entries`{.interpreted-text role="guilabel"}. Following this step,
a pop-up will appear and click on
`Post journal entries`{.interpreted-text role="guilabel"}. This will
take the invoices out of *draft* and set them to *posted*.

### Reconciling payments

Users typically utilize PayPal to receive payment from eBay, and then
send lump sums from PayPal into their bank account. To reconcile this
income, users can reconcile the one PayPal transfer with all related
invoices.

First navigate to the `Accounting Dashboard`{.interpreted-text
role="guilabel"} by going to the `Accounting
app --> Dashboard --> Bank`{.interpreted-text role="menuselection"}.
`Create`{.interpreted-text role="guilabel"} a new transaction and enter
the `Label`{.interpreted-text role="guilabel"} as [eBay
Sales]{.title-ref}. Fill out the `Amount`{.interpreted-text
role="guilabel"} and enter a `Statement`{.interpreted-text
role="guilabel"} date in. Click on `Create and edit`{.interpreted-text
role="guilabel"}.

For the `Ending Balance`{.interpreted-text role="guilabel"} field, enter
the same account that was entered for the `Amount`{.interpreted-text
role="guilabel"} above. Click on `Save`{.interpreted-text
role="guilabel"}. Next, open the new balance that needs to be
reconciled. Under the tab marked:
`Match Existing Entries`{.interpreted-text role="guilabel"} select the
entries that are included in this balance.

After adding all the necessary entries, click
`Validate`{.interpreted-text role="guilabel"} to complete the
reconciliation. To verify the payment, navigate to
`Customers --> Invoices`{.interpreted-text role="menuselection"} and
select the desired customer invoice. The *Paid* label should appear
under the `Payment Status`{.interpreted-text role="guilabel"} column.

::: {.seealso}
\-
`/applications/sales/sales/ebay_connector/troubleshooting`{.interpreted-text
role="doc"} -
`/applications/sales/sales/ebay_connector/linking_listings`{.interpreted-text
role="doc"} -
`/applications/sales/sales/ebay_connector/setup`{.interpreted-text
role="doc"}
:::
