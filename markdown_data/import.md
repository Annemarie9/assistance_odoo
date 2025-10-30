Import products
===============

Odoo *Sales* provides a template for importing products with categories
and variants, which can be opened and edited with any spreadsheet
software (Microsoft Excel, OpenOffice, Google Sheets, etc.).

When this spreadsheet is filled out properly, it can be quickly uploaded
to the Odoo database. When uploaded, those products are instantly added,
accessible, and editable in the product catalog.

Import template
---------------

In order to import products with categories and variants, the *Import
Template for Products* **must** be downloaded. Once downloaded, the
template can be adjusted and customized, and then uploaded back into the
Odoo database.

To download the necessary import template, navigate to
`Sales app --> Products -->
Products`{.interpreted-text role="menuselection"}. On the
`Products`{.interpreted-text role="guilabel"} page, click the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon in the upper-left
corner. Doing so reveals a drop-down menu.

From this drop-down menu, select the `Import records`{.interpreted-text
role="guilabel"} option.

{.align-center}

Selecting `Import records`{.interpreted-text role="guilabel"} reveals a
separate page with a link to download the
`Import Template for Products`{.interpreted-text role="guilabel"}. Click
that link to download the template.

{.align-center}

Once the template download is complete, open the spreadsheet file to
customize it.

Customize product import template
---------------------------------

When the import template has been downloaded and opened, it\'s time to
modify its contents. However, before any changes are made, there are a
few elements to keep in mind during the process:

-   Feel free to remove any columns that aren\'t deemed necessary. But,
    it is *strongly* advised that the
    `Internal Reference`{.interpreted-text role="guilabel"} column
    remains.

    While it\'s not mandatory, having a unique identifier (e.g.
    [FURN\_001]{.title-ref}) in the `Internal
    Reference`{.interpreted-text role="guilabel"} column for each
    product can be helpful in many cases. This can even be from previous
    software spreadsheets to ease the transition into Odoo.

    For example, when updating imported products, the same file can be
    imported several times without creating duplicates, thus enhancing
    the efficiency and simplicity of imported product management.

-   Do **not** change the labels of columns that are meant to be
    imported. Otherwise, Odoo won\'t recognize them, forcing the user to
    map them on the import screen manually.

-   Feel free to add new columns to the template spreadsheet, if
    desired. However, to be added, those fields **must** exist in Odoo.
    If Odoo can\'t match the column name with a field, it can be matched
    manually during the import process.

    During the import process of the completed template, Odoo reveals a
    page showcasing all the elements of the newly-configured product
    template spreadsheet, separated by `File
    Column`{.interpreted-text role="guilabel"},
    `Odoo Field`{.interpreted-text role="guilabel"}, and
    `Comments`{.interpreted-text role="guilabel"}.

    To manually match a column name with a field in Odoo, click the
    `Odoo Field`{.interpreted-text role="guilabel"} drop-down menu next
    to the `File Column`{.interpreted-text role="guilabel"} that needs a
    manual adjustment, and select the appropriate field from that
    drop-down menu.

    {.align-center}

Import product template spreadsheet
-----------------------------------

After customizing the product template spreadsheet, return to the Odoo
product import page, where the template download link is found, and
click the `Upload File`{.interpreted-text role="guilabel"} button in the
upper-left corner.

{.align-center}

Then, a pop-up window appears, in which the completed product template
spreadsheet file should be selected and uploaded to Odoo.

After that, Odoo reveals a page showcasing all the elements of the
newly-configured product template spreadsheet, separated by
`File Column`{.interpreted-text role="guilabel"},
`Odoo Field`{.interpreted-text role="guilabel"}, and
`Comments`{.interpreted-text role="guilabel"}.

{.align-center}

From here, the `File Column`{.interpreted-text role="guilabel"} can be
manually assigned to an `Odoo Field`{.interpreted-text role="guilabel"},
if necessary.

To make sure everything is appropriate, and all the columns and fields
are lined up accurately, click the `Test`{.interpreted-text
role="guilabel"} button in the upper-left corner.

If everything is lined up and applied correctly, Odoo reveals a blue
banner at the top of the page, informing the user that
`Everything seems valid`{.interpreted-text role="guilabel"}.

{.align-center}

If there are any errors, Odoo reveals a red banner at the top of the
page, with instructions of where to locate the specific issues, and how
to fix them.

{.align-center}

Once those errors are fixed, click `Test`{.interpreted-text
role="guilabel"} again to ensure all necessary issues have been remedied
appropriately.

If additional product template spreadsheets need to be uploaded, click
the `Load File`{.interpreted-text role="guilabel"} button, select the
desired product template spreadsheet, and repeat the process.

When everything is ready, click the `Import`{.interpreted-text
role="guilabel"} button.

When clicked, Odoo instantly imports those products, and reveals the
main `Products`{.interpreted-text role="guilabel"} page, with a pop-up
message in the upper-right corner. This pop-up message informs the user
how many products were successfully imported.

{.align-center}

At this point, all the newly-imported products are accessible and
editable via the `Products`{.interpreted-text role="guilabel"} page.

Import relation fields, attributes, and variants
------------------------------------------------

It\'s important to note that an Odoo object is always related to many
other objects. For example, a product is linked to product categories,
attributes, vendors, and things of this nature. These links/connections
are known as relations.

::: {.note}
::: {.title}
Note
:::

In order to import product relations, the records of the related object
**must** be imported *first* from their own list menu.
:::

### Relation fields

On product forms in Odoo, there are a number of fields that can be
modified and customized at any time. These fields are found under every
tab on a product form. While these fields are easily editable directly
on the product form, they can also be modified via a product import.

As mentioned, relation fields of this nature can **only** be imported
for products if they already exist in the database. For example, if a
user attempts to import a product with a *Product Type*, it can only be
one of the preconfigured product types existing in the database (e.g.
*Storable Product*, *Consumable*, etc.).

To import information for a relation field on a product import template
spreadsheet, add the name of the field as a column name/title on the
spreadsheet. Then, on the appropriate product line, add the desired
relation field option.

When all desired relation field information has been entered, save the
spreadsheet, and import it to the database, per the process mentioned
above (`Sales app --> Products -->
Products --> ⚙️ (gear) icon --> Import records --> Upload File`{.interpreted-text
role="menuselection"}).

Once the spreadsheet with the newly-configured relation field
information has been uploaded, click `Import`{.interpreted-text
role="guilabel"}, and Odoo returns to the `Products`{.interpreted-text
role="guilabel"} page.

When the newly-changed/modified products, complete with the new relation
field information, has been imported and uploaded, that new information
can be found on the `Products`{.interpreted-text role="guilabel"} page.

### Attributes and values

Odoo also allows users to import product attributes and values that can
be used for products that already exist in the database, and/or with
imported products.

To import attributes and values, a separate spreadsheet or CSV file
dedicated to attributes and values **must** be imported and uploaded
before they can be used for other products.

The column names/titles of the attributes and values spreadsheet should
be as follows: `Attribute`{.interpreted-text role="guilabel"},
`Display Type`{.interpreted-text role="guilabel"},
`Variant Creation Mode`{.interpreted-text role="guilabel"}, and
`Values / Value`{.interpreted-text role="guilabel"}.

{.align-center}

-   `Attribute`{.interpreted-text role="guilabel"}: name of the
    attribute (e.g. [Size]{.title-ref}).
-   `Display Type`{.interpreted-text role="guilabel"}: display type used
    in the product configurator. There are three display type options:
    -   `Radio`{.interpreted-text role="guilabel"}: values displayed as
        radio buttons
    -   `Selection`{.interpreted-text role="guilabel"}: values displayed
        in a selection list
    -   `Color`{.interpreted-text role="guilabel"}: values denoted as a
        color selection
-   `Variant Creation Mode`{.interpreted-text role="guilabel"}: how the
    variants are created when applied to a product. There are three
    variant creation mode options:
    -   `Instantly`{.interpreted-text role="guilabel"}: all possible
        variants are created as soon as the attribute, and its values,
        are added to a product

    -   `Dynamically`{.interpreted-text role="guilabel"}: each variant
        is created **only** when its corresponding attributes and values
        are added to a sales order

    -   `Never`{.interpreted-text role="guilabel"}: variants are
        **never** created for the attribute

        ::: {.note}
        ::: {.title}
        Note
        :::

        The `Variants Creation Mode`{.interpreted-text role="guilabel"}
        **cannot** be changed once the attribute is used on at least one
        product.
        :::
-   `Values/Value`{.interpreted-text role="guilabel"}: values pertaining
    to the corresponding attribute. If there are multiple values for the
    same attribute, the values need to be in individual lines on the
    spreadsheet.

Once the desired attributes and values have been entered and saved in
the spreadsheet, it\'s time to import and upload it into Odoo. To do
that, navigate to `Sales app --> Configuration
--> Attributes --> ⚙️ (gear) icon --> Import records --> Upload File`{.interpreted-text
role="menuselection"}.

Once the spreadsheet with the newly-configured attributes and values has
been uploaded, click `Import`{.interpreted-text role="guilabel"}, and
Odoo returns to the `Attributes`{.interpreted-text role="guilabel"}
page. That\'s where those newly-added attributes and values can be found
and edited, if necessary.

As mentioned previously, when attributes and values have been added to
the Odoo database, they can be used for existing or imported products.

### Product variants

When product attributes and values are configured in the database, they
can be used on product import spreadsheets to add more information and
detail to products being imported.

To import products with product attributes and values, the product
import template spreadsheet must be configured with specific
`Product Attributes / Attribute`{.interpreted-text role="guilabel"},
`Product
Attributes / Values`{.interpreted-text role="guilabel"}, and
`Name`{.interpreted-text role="guilabel"} columns.

There can be other columns, as well, but these columns are **required**
in order to properly import products with specific variants.

{.align-center}

-   `Name`{.interpreted-text role="guilabel"}: product name
-   `Product Attributes / Attribute`{.interpreted-text role="guilabel"}:
    name of attribute
-   `Product Attributes / Values`{.interpreted-text role="guilabel"}:
    values pertaining to the corresponding attribute

::: {.tip}
::: {.title}
Tip
:::

To import multiple values, separate them by *just* a comma, **not** a
comma followed by a space, in the product import template spreadsheet
(e.g. [furniture,couch,home]{.title-ref}).
:::

When the desired products and product variants have been entered and
saved in the spreadsheet, it\'s time to import and upload them into
Odoo. To do that, navigate to `Sales app -->
Products --> Products --> ⚙️ (gear) icon --> Import records --> Upload File`{.interpreted-text
role="menuselection"}.

Once the spreadsheet with the newly-configured products and product
variants has been uploaded, click `Import`{.interpreted-text
role="guilabel"}, and Odoo returns to the `Products`{.interpreted-text
role="guilabel"} page. That\'s where the newly-added products can be
found.

To view and modify the attributes and variants on any products, select
the desired product from the `Products`{.interpreted-text
role="guilabel"} page, and click the
`Attributes \& Variants`{.interpreted-text role="guilabel"} tab.

::: {.seealso}
`variants`{.interpreted-text role="doc"}
:::
