Electronic shelf labels
=======================

Electronic shelf labels allow you to display product information like
prices and barcodes on store shelves and to synchronize them remotely
from the backend. This removes the need to print new labels when product
information changes.



::: {.note}
::: {.title}
Note
:::

Odoo uses electronic labels from .
:::

Configuration
-------------

### Pricer setup

1.   to create
    and configure your Pricer account.

2.  Create your stores: one pricer store equates to one physical store.

3.  Link as many transceivers as needed to the Pricer store(s).

4.  Create the following variables to share product information between
    your Odoo database system and Pricer. These variables act like
    placeholders on the label template.

    -   \`itemId\`: this holds the unique internal identifier assigned
        to each product
    -   \`itemName\`: the actual name of the product
    -   \`price\`: the selling price of the product, including any
        applicable taxes
    -   \`presentation\`: the template name used in Pricer for
        displaying the product information on the label
    -   \`currency\`: the currency of your company (e.g., USD, EUR)
    -   \`barcode\`: the barcode number associated with each product

    ::: {.important}
    ::: {.title}
    Important
    :::

    The names for these variables must be **identical** in your Pricer
    database.
    :::

5.  Create a template named [NORMAL]{.title-ref}. This template is used
    to display information on your digital tags.

Once your account, stores, variables, and template are configured on
Pricer, you can proceed with the setup of your Odoo database.

::: {.important}
::: {.title}
Important
:::

The account associated with your Pricer store must have access to send
API requests to Pricer.
:::

### Odoo setup

As a pre-requisite, `activate <general/install>`{.interpreted-text
role="ref"} the `POS Pricer`{.interpreted-text role="guilabel"} module
*(technical name: pos\_pricer)* to have all the required features to use
Pricer electronic tags.



Once the module is activated, configure your
`pricer stores <pricer_tags/stores>`{.interpreted-text role="ref"} and
associate `Pricer tags <pricer_tags/tags>`{.interpreted-text role="ref"}
with your products.

#### Pricer stores {#pricer_tags/stores}

Similarly to the configuration in Pricer, you need to create one pricer
store per physical location. To do so, go to
`Point of Sale --> Configuration --> Pricer Stores`{.interpreted-text
role="menuselection"}, click `New`{.interpreted-text role="guilabel"},
and fill in the line with the required information:

-   `Store Name`{.interpreted-text role="guilabel"}: you can put any
    name of your liking.
-   `Pricer Tenant Name`{.interpreted-text role="guilabel"}: the name of
    your company account in Pricer, usually followed by
    [-country\_code]{.title-ref}. This value is provided by Pricer.
-   `Pricer Login`{.interpreted-text role="guilabel"}: the login of your
    Pricer account.
-   `Pricer Password`{.interpreted-text role="guilabel"}: the password
    of your Pricer account.
-   `Pricer Store ID`{.interpreted-text role="guilabel"}: the ID of the
    related Pricer store as defined on your Pricer database.



::: {.note}
::: {.title}
Note
:::

\- The `Pricer Tags`{.interpreted-text role="guilabel"} column is
updated automatically when a label is linked to a product. - The
`Last Update`{.interpreted-text role="guilabel"} and
`Last Update Status`{.interpreted-text role="guilabel"} columns are
updated automatically when the tags are updated.
:::

#### Pricer tags {#pricer_tags/tags}

For a label to display specific product information, the label needs to
be associated with the product. To do so:

1.  Open the product form by going to
    `Point of Sale --> Products --> Products`{.interpreted-text
    role="menuselection"} and clicking `New`{.interpreted-text
    role="guilabel"} or selecting an existing product.

    ::: {.note}
    ::: {.title}
    Note
    :::

    If you are creating a new product, configure and save it before
    associating any Pricer tags.
    :::

2.  Go to the `Sales`{.interpreted-text role="guilabel"} tab, scroll to
    the `Pricer`{.interpreted-text role="guilabel"} section, and select
    the corresponding `Pricer Store`{.interpreted-text role="guilabel"}.

    

3.  Fill in the `Pricer tags ids`{.interpreted-text role="guilabel"}
    field by copying the label\'s ID from the label itself or scanning
    its barcode.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Pricer tag IDs are composed of a letter followed by 16 digits.
    :::

::: {.tip}
::: {.title}
Tip
:::

\- We recommended using a barcode scanner to speed up the encoding
process. - When setting up Pricer with Odoo for the first time, it is
recommended that you configure only one product first. Before
configuring more products, ensure you can display their information on a
Pricer tag.
:::

Now that you have a product associated with a Pricer tag, we can send
its information to Pricer.

### Practical application

Odoo automatically sends requests to Pricer to synchronize the tags
every 12 hours if you make any modifications to:

> -   Product name, price, barcode, or customer taxes
> -   Currency
> -   Associated Pricer store or Pricer tags

To force the update, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}. Then:

1.  Go to
    `Point of Sale --> Configuration --> Pricer Store`{.interpreted-text
    role="menuselection"}.
2.  Select the desired store(s).
3.  Click `Update tags`{.interpreted-text role="guilabel"} to update all
    tags affected by changes to:
    -   Product name, price, barcode, or customer taxes
    -   Currency
    -   Associated Pricer store or Pricer tags

Alternatively, click `Update all tags`{.interpreted-text
role="guilabel"} to force the update of every tag, regardless of whether
changes were made.



If Pricer has processed and accepted the request, the status field shows
`Update
successfully sent to Pricer`{.interpreted-text role="guilabel"}. If
there is any issue, the system displays an error message.

::: {.warning}
::: {.title}
Warning
:::

If a request sent to Pricer fails, Odoo still considers that the product
has been updated. In that case, we recommend forcing the update of all
tags.
:::
