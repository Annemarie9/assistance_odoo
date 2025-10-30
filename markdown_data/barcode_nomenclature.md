# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/barcode/operations/barcode_nomenclature.md

Default barcode nomenclature
============================

*Barcode nomenclatures* define how barcodes are recognized and
categorized. When a barcode is scanned, it is associated to the
**first** rule with a matching pattern. The pattern syntax is described
in Odoo\'s nomenclature list using a regular expression, and a barcode
is successfully read by Odoo if its prefix and/or length matches the one
defined in the barcode\'s rule.

For instance, at a
`Point of Sale <../../../sales/point_of_sale>`{.interpreted-text
role="doc"} station, product weight barcodes in the European Article
Number (EAN) format, which begin with [21]{.title-ref} and have five
digits specifying the weight, are used to weigh products and generate a
barcode depicting the weight and price. The [21]{.title-ref} and
five-digit weight is the barcode pattern used to identify the barcode
and can be customized to ensure Odoo correctly interprets all barcodes
for the business.

::: {.note}
::: {.title}
Note
:::

Barcodes are also commonly used with Odoo\'s **Inventory** and
**Barcode** apps.
:::

Odoo **Barcode** supports
`EAN (European Article Number)`{.interpreted-text role="abbr"},
Universal Product Code (UPC), and
`GS1 <gs1_nomenclature>`{.interpreted-text role="doc"} formats. This
document exclusively focuses on `default rules and patterns in Odoo
<barcode/operations/default-nomenclature-list>`{.interpreted-text
role="ref"}, which use `UPC (Universal Product Code)`{.interpreted-text
role="abbr"} and `EAN (European Article Number)`{.interpreted-text
role="abbr"} encoding.

::: {.important}
::: {.title}
Important
:::

To use `UPC (Universal Product Code)`{.interpreted-text role="abbr"} and
`EAN (European Article Number)`{.interpreted-text role="abbr"} barcodes
for uniquely identifying products across the entire supply chain, they
**must** be [purchased from
GS1](https://www.gs1.org/standards/get-barcodes).

In Odoo, custom barcode patterns can be defined to recognize barcodes
specific to the company. Barcodes do not need to be purchased if used
only within the company, such as in the
`example <barcode/operations/product-weight>`{.interpreted-text
role="ref"} where the barcode is written in the
`EAN (European Article Number)`{.interpreted-text role="abbr"} format.
:::

Configuration
-------------

To use default nomenclature, navigate to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Under the
`Barcode`{.interpreted-text role="guilabel"} section, tick the
`Barcode Scanner`{.interpreted-text role="guilabel"} checkbox. Doing so
installs the **Barcode** app in the database.

Next, in the `Barcode Nomenclature`{.interpreted-text role="guilabel"}
field, ensure `Default Nomenclature`{.interpreted-text role="guilabel"}
is selected. Then, click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

With the **Barcode** module installed, and the
`Default Nomenclature`{.interpreted-text role="guilabel"} selected, the
barcode actions using `UPC (Universal Product Code)`{.interpreted-text
role="abbr"} and `EAN (European Article Number)`{.interpreted-text
role="abbr"}, detailed in the `default nomenclature list
<barcode/operations/default-nomenclature-list>`{.interpreted-text
role="ref"}, are available for use. And, by default, Odoo automatically
handles `UPC (Universal Product Code)`{.interpreted-text
role="abbr"}/`EAN (European Article Number)`{.interpreted-text
role="abbr"} conversion.

Example: product weight barcode {#barcode/operations/product-weight}
-------------------------------

To better understand how barcode nomenclature is used to identify
products in Odoo, this example where product weight barcodes in
`EAN (European Article Number)`{.interpreted-text role="abbr"} format
are used to allow a `Point of Sale
<../../../sales/point_of_sale>`{.interpreted-text role="doc"} business
to automatically print barcodes, and calculate the price using the
weight of the item.

To set up barcodes for weighted products, the following rule is used:

  Rule Name                      Barcode Pattern    Field in Odoo
  ------------------------------ ------------------ --------------------------------------------------------------------
  Weighted Barcodes 3 Decimals   (21)\....{NNDDD}   `Barcode`{.interpreted-text role="guilabel"} field on product form

::: {.example}
To better understand the barcode pattern for weighted products, consider
the barcode, \`2112345000008\`:

-   \`21\`: code that identifies this a barcode for weighted products.
-   \`12345\`: five digits (denoted by [\.....]{.title-ref} in the table
    above) that identify the product.
-   \`00000\`: five digits (denoted by [{NNDDD}]{.title-ref} in the
    table) representing the weight of the product. On the product form,
    the five weight values **must** be [00000]{.title-ref}. The first
    two digits are whole number values, and the last three digits are
    decimal values. For example, \"13.5 grams\" in the
    [{NNDDD}]{.title-ref} format is [13500]{.title-ref}.
-   \`8\`: [check
    digit](https://www.gs1.org/services/check-digit-calculator) for
    [211234500000]{.title-ref}.

Together, these components make up a 13-character
`EAN (European Article Number)`{.interpreted-text role="abbr"} - 13
barcode.
:::

To configure the product barcode for [Pasta Bolognese]{.title-ref}, the
`EAN (European Article Number)`{.interpreted-text role="abbr"} barcode
for weighted products, [2112345000008]{.title-ref}, is entered in the
`Barcode`{.interpreted-text role="guilabel"} field on the product form
(accessible by going to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and selecting the desired product). In addition,
the `Unit of Measure`{.interpreted-text role="guilabel"} is set to
`kg`{.interpreted-text role="guilabel"}.

{.align-center}

Next, a customer\'s bowl of pasta is weighed to be [1.5]{.title-ref}
kilograms. This generates a new barcode for the pasta, according to the
weight: [211234501500]{.title-ref}, which has a check digit of
[2]{.title-ref}. The new barcode is [2112345015002]{.title-ref}.

{.align-center}

Ensure the products scan properly, by navigating to the
`Barcode app --> Operations`{.interpreted-text role="menuselection"}.
Next, click any operation type, such as `Receipts`{.interpreted-text
role="guilabel"}. Then, click the `New`{.interpreted-text
role="guilabel"} button to create a draft stock move. Scan the product
weight barcode, such as [2112345015002]{.title-ref}, and if the intended
product appears, the barcode setup is correct.

{.align-center}

Create rules
------------

::: {.important}
::: {.title}
Important
:::

Adding new rules is necessary for
`UPC (Universal Product Code)`{.interpreted-text role="abbr"} and
`EAN (European Article Number)`{.interpreted-text role="abbr"} formats
that are **not** in Odoo\'s default list, since barcodes cannot be read
successfully if there are unknown fields.

While new rules can be created, Odoo fields do **not** auto-populate
with information from these rules. [Custom
development](https://www.odoo.com/appointment/132) is required for this
functionality.
:::

To create a rule, first enable
`developer mode <developer-mode>`{.interpreted-text role="ref"}. Then,
navigate to
`Inventory app --> Configuration --> Barcode Nomenclatures`{.interpreted-text
role="menuselection"}, and select
`Default Nomenclature`{.interpreted-text role="guilabel"}.

On this page, configure the following optional fields:

-   `UPC/EAN Conversion`{.interpreted-text role="guilabel"}: determines
    if a `UPC (Universal Product Code)`{.interpreted-text
    role="abbr"}/`EAN (European Article Number)`{.interpreted-text
    role="abbr"} barcode should be automatically converted when matching
    a rule with another encoding. Options include
    `Always`{.interpreted-text role="guilabel"} (the default option),
    `Never`{.interpreted-text role="guilabel"},
    `EAN-13 to UPC-A`{.interpreted-text role="guilabel"}, and
    `UPC-A to EAN-13`{.interpreted-text role="guilabel"}.
-   `Is GS1 Nomenclature`{.interpreted-text role="guilabel"}: ensure
    this checkbox is **not** ticked, as the
    `Default Nomenclature`{.interpreted-text role="guilabel"} uses
    `UPC (Universal Product Code)`{.interpreted-text role="abbr"} and
    `EAN (European Article Number)`{.interpreted-text role="abbr"}
    encoding, *not* GS1 encoding.

{.align-center}

On the `Default Nomenclature`{.interpreted-text role="guilabel"} page,
click `Add a line`{.interpreted-text role="guilabel"} at the bottom of
the table, which opens a `Create Rules`{.interpreted-text
role="guilabel"} pop-up window to create a new rule.

The `Rule Name`{.interpreted-text role="guilabel"} field is used
internally to identify what the barcode represents.

The `Sequence`{.interpreted-text role="guilabel"} field represents the
priority of the rule; meaning the smaller the value, the higher the rule
appears on the table.

The barcode `Type`{.interpreted-text role="guilabel"} field represents
different classifications of information that can be understood by the
system (e.g., `Package`{.interpreted-text role="guilabel"},
`Lot`{.interpreted-text role="guilabel"}, `Location`{.interpreted-text
role="guilabel"}, `Coupon`{.interpreted-text role="guilabel"}, etc.).

The `Encoding`{.interpreted-text role="guilabel"} field specifies which
encoding the barcode uses. This rule **only** applies if the barcode
uses this specific encoding. The available `Encoding`{.interpreted-text
role="guilabel"} options are: `EAN-13`{.interpreted-text
role="guilabel"}, `EAN-8`{.interpreted-text role="guilabel"},
`UPC-A`{.interpreted-text role="guilabel"}, and
`GS1-28`{.interpreted-text role="guilabel"}.

The `Barcode Pattern`{.interpreted-text role="guilabel"} field
represents how the sequence of letters or numbers is recognized by the
system to contain information about the product. Sometimes, when a
certain amount of digits are required, the number of [.]{.title-ref} is
shown. [N]{.title-ref} represents whole number digits, and
[D]{.title-ref} represent decimal digits.

::: {.example}
[1\...]{.title-ref} represents any 4-digit number that starts with 1.
[NNDD]{.title-ref} represents a two digit number with two decimal
points. For example, [14.25]{.title-ref} is 1425.
:::

After filling in the information, click the
`Save & New`{.interpreted-text role="guilabel"} button to save the rule,
and instantly start creating another rule. Or, click
`Save & Close`{.interpreted-text role="guilabel"} to save the rule, and
return to the table of rules.

Default nomenclature list {#barcode/operations/default-nomenclature-list}
-------------------------

The table below contains Odoo\'s list of
`Default Nomenclature`{.interpreted-text role="guilabel"} rules. Barcode
patterns are written in regular expressions.

  Rule Name                     Type                 Encoding   Barcode Pattern
  ----------------------------- -------------------- ---------- -----------------
  Price Barcodes 2 Decimals     Priced Product       EAN-13     23\.....{NNNDD}
  Discount Barcodes             Discounted Product   Any        22{NN}
  Weight Barcodes 3 Decimals    Weighted Product     EAN-13     21\.....{NNDDD}
  Customer Barcodes             Client               Any        042
  Coupon & Gift Card Barcodes   Coupon               Any        043\|044
  Cashier Barcodes              Cashier              Any        041
  Location barcodes             Location             Any        414
  Package barcodes              Package              Any        PACK
  Lot barcodes                  Lot                  Any        10
  Magnetic Credit Card          Credit Card          Any        %.\*
  Product Barcodes              Unit Product         Any        .\*

::: {.note}
::: {.title}
Note
:::

When the `Barcode Pattern`{.interpreted-text role="guilabel"} contains
[.\*]{.title-ref}, it means it can contain any number or type of
characters.
:::

::: {.seealso}
`gs1_nomenclature`{.interpreted-text role="doc"}
:::
