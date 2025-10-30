# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/barcode/operations/gs1_nomenclature.md

GS1 barcode nomenclature
========================

::: {#barcode/operations/gs1}
 consolidates various product
and supply chain data into a single barcode. Odoo takes in [unique
Global Trade Item Numbers](https://www.gs1.org/standards/get-barcodes)
(GTIN), purchased by businesses, to enable global shipping, sales, and
eCommerce product listing.
:::

Configure GS1 nomenclature to scan barcodes of sealed boxes and identify
essential product information, such as
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"}, lot
number, quantity information, and more.

::: {.important}
::: {.title}
Important
:::

`GTINs (Global Trade Item Numbers)`{.interpreted-text role="abbr"} are
unique product identification that **must** be [purchased from
GS1](https://www.gs1.org/standards/get-barcodes) to use GS1 barcodes.
:::

::: {.seealso}
\- [All GS1
barcodes](https://www.gs1.org/standards/barcodes/application-identifiers)
-
`Odoo's default GS1 rules <barcode/operations/default-gs1-nomenclature-list>`{.interpreted-text
role="ref"} -
`Why's my barcode not working? <barcode/operations/troubleshooting>`{.interpreted-text
role="ref"}
:::

Set up barcode nomenclature {#barcode/operations/set-up-barcode-nomenclature}
---------------------------

To use GS1 nomenclature, navigate to the
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Then under the
`Barcode`{.interpreted-text role="guilabel"} section, check the
`Barcode Scanner`{.interpreted-text role="guilabel"} box. Next, select
`Barcode Nomenclature --> Default GS1 Nomenclature`{.interpreted-text
role="menuselection"} from the default barcode nomenclature options.

{.align-center}

The list of GS1 *rules* and *barcode patterns* Odoo supports by default
is accessible by clicking the `➡️ (arrow)`{.interpreted-text
role="guilabel"} icon to the right of the
`Barcode Nomenclature`{.interpreted-text role="guilabel"} selection.

In the `Open: Nomenclature`{.interpreted-text role="guilabel"} pop-up
table, view and edit the GS1 `Rule Names`{.interpreted-text
role="guilabel"} available in Odoo. The table contains all the
information that can be condensed with a GS1 barcode, along with the
corresponding `Barcode Pattern`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

After setting GS1 as the barcode nomenclature, the
`Barcode Nomenclatures`{.interpreted-text role="menuselection"} settings
can also be accessed by a hidden menu that\'s discoverable after
enabling `developer
mode <developer-mode>`{.interpreted-text role="ref"}. Once enabled,
navigate to the `Inventory app -->
Configuration --> Barcode Nomenclatures`{.interpreted-text
role="menuselection"} menu and finally, select `Default GS1
Nomenclature`{.interpreted-text role="guilabel"}.
:::

Use GS1 barcodes in Odoo {#barcode/operations/create-GS1-barcode}
------------------------

For product identification using GS1 barcodes in Odoo, businesses obtain
a  as an
internationally distinct product identifier purchased from GS1. This
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"} is
combined with specific product details following GS1\'s designated
*barcode pattern*. The barcode pattern\'s arrangement of numbers and
letters must adhere to GS1 conventions for accurate interpretation by
global systems along the supply chain.

Every barcode starts with a 2-4 digit [application
identifier](https://www.gs1.org/standards/barcodes/application-identifiers)
(A.I.). This required prefix universally indicates what kind of
information the barcode contains. Odoo follows GS1 rules for identifying
information, as detailed in the `default GS1 rules list
<barcode/operations/default-gs1-nomenclature-list>`{.interpreted-text
role="ref"}. Including the relevant
`A.I. (Application Identifier)`{.interpreted-text role="abbr"} from the
list enables Odoo to correctly interpret GS1 barcodes. While most
barcode patterns have a fixed length requirement, certain ones, such as
lots and serial numbers, have flexible length.

::: {.tip}
::: {.title}
Tip
:::

For flexible-length barcode patterns not placed at the end of the GS1
barcode, use the FNC1 separator ([x1D]{.title-ref}) to end the barcode.

Example: The barcode pattern for lot numbers is 20 characters long.
Instead of creating a 20-character lot number barcode, like
[LOT00000000000000001]{.title-ref}, use the FNC1 separator to make it
shorter: [LOT001x1D]{.title-ref}.
:::

Refer to the
`GS1 nomenclature list <barcode/operations/default-gs1-nomenclature-list>`{.interpreted-text
role="ref"} to see a comprehensive list of all barcode patterns and
rules to follow. Otherwise, refer to `this
GS1 usage doc <barcode/operations/gs1_usage>`{.interpreted-text
role="ref"} for specific examples of combining
`GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"} to
product information and configuring the workflow.

::: {.seealso}
\- `Lots workflow <barcode/operations/gs1-lots>`{.interpreted-text
role="ref"} -
`Non-unit quantities workflow <barcode/operations/quantity-ex>`{.interpreted-text
role="ref"}
:::

### Create rules {#barcode/operations/create-new-rules}

GS1 rules are a specific format of information contained in the barcode,
beginning with an `A.I. (Application Identifier)`{.interpreted-text
role="abbr"} and containing a defined length of characters. Scanning GS1
barcodes from the `default GS1 list
<barcode/operations/default-gs1-nomenclature-list>`{.interpreted-text
role="ref"} auto-fills corresponding data in the Odoo database.

Adding GS1 barcode rules in Odoo ensures accurate interpretation of
unique, non-standard GS1 formats.

To do so, begin by turning on
`developer mode <developer-mode>`{.interpreted-text role="ref"} and
navigating to the `Barcode Nomenclatures`{.interpreted-text
role="guilabel"} list in `Inventory app --> Configuration -->
Barcode Nomenclatures`{.interpreted-text role="menuselection"}. Then,
select the `Default GS1 Nomenclature`{.interpreted-text role="guilabel"}
list item.

On the `Default GS1 Nomenclature`{.interpreted-text role="guilabel"}
page, select `Add a line`{.interpreted-text role="guilabel"} at the
bottom of the table, which opens a window to create a new rule. The
`Rule Name`{.interpreted-text role="guilabel"} field is used internally
to identify what the barcode represents. The barcode
`Types`{.interpreted-text role="guilabel"} are different classifications
of information that can be understood by the system (e.g. product,
quantity, best before date, package, coupon). The
`Sequence`{.interpreted-text role="guilabel"} represents the priority of
the rule; this means the smaller the value, the higher the rule appears
on the table. Odoo follows the sequential order of this table and will
use the first rule it matches based on the sequence. The `Barcode
Pattern`{.interpreted-text role="guilabel"} is how the sequence of
letters or numbers is recognized by the system to contain information
about the product.

After filling in the information, click the
`Save & New`{.interpreted-text role="guilabel"} button to make another
rule or click `Save & Close`{.interpreted-text role="guilabel"} to save
and return to the table of rules.

Barcode troubleshooting {#barcode/operations/troubleshooting}
-----------------------

Since GS1 barcodes are challenging to work with, here are some checks to
try when the barcodes are not working as expected:

1.  Ensure that the `Barcode Nomenclature`{.interpreted-text
    role="guilabel"} setting is set as `Default GS1
    Nomenclature`{.interpreted-text role="menuselection"}. Jump to the
    `nomenclature setup section
    <barcode/operations/set-up-barcode-nomenclature>`{.interpreted-text
    role="ref"} for more details.

2.  Ensure that the fields scanned in the barcode are enabled in Odoo.
    For example, to scan a barcode containing lots and serial numbers,
    make sure the `Lots & Serial Numbers`{.interpreted-text
    role="guilabel"} feature is enabled in
    `Odoo's settings <barcode/operations/lot-setup>`{.interpreted-text
    role="ref"} and `on the product
    <barcode/operations/lot-setup-on-product>`{.interpreted-text
    role="ref"}.

3.  Omit punctuation such as parentheses [()]{.title-ref} or brackets
    [\[\]]{.title-ref} between the `A.I. (Application
    Identifier)`{.interpreted-text role="abbr"} and the barcode
    sequence. These are typically used in examples for ease of reading
    and should **not** be included in the final barcode. For more
    details on building GS1 barcodes, go to
    `this section <barcode/operations/create-GS1-barcode>`{.interpreted-text
    role="ref"}.

4.  When a single barcode contains multiple encoded fields, Odoo
    requires all rules to be listed in the barcode nomenclature for Odoo
    to read the barcode. `This section
    <barcode/operations/create-new-rules>`{.interpreted-text role="ref"}
    details how to add new rules in the barcode nomenclature.

5.  Test barcodes containing multiple encoded fields, piece by piece, to
    figure out which field is causing the issue.

    ::: {.example}
    When testing a barcode containing the
    `GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"},
    lot number, and quantity, start by scanning the
    `GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"}
    alone. Then, test the
    `GTIN (Global Trade Item Number)`{.interpreted-text role="abbr"}
    with the lot number, and finally, try scanning the whole barcode.
    :::

6.  After diagnosing the encoded field is unknown, `add new rules
    <barcode/operations/create-new-rules>`{.interpreted-text role="ref"}
    to Odoo\'s default list to recognize GS1 barcodes with unique
    specifications.

    ::: {.important}
    ::: {.title}
    Important
    :::

    While the new field will be read, the information won\'t link to an
    existing field in Odoo without developer customizations. However,
    adding new rules is necessary to ensure the rest of the fields in
    the barcode are interpreted correctly.
    :::

GS1 nomenclature list {#barcode/operations/default-gs1-nomenclature-list}
---------------------

The table below contains Odoo\'s default list of GS1 rules. Barcode
patterns are written in regular expressions. Only the first three rules
require a [check
digit](https://www.gs1.org/services/check-digit-calculator) as the final
character.

  ---------------------------------------------------------------------------------------------------------------------
  Rule Name              Type          Barcode Pattern                    GS1 Content     Odoo field
                                                                          Type            
  ---------------------- ------------- ---------------------------------- --------------- -----------------------------
  Serial Shipping        Package       (00)(\\d{18})                      Numeric         Package name
  Container Code                                                          identifier      

  Global Trade Item      Unit Product  (01)(\\d{14})                      Numeric         `Barcode`{.interpreted-text
  Number (GTIN)                                                           identifier      role="guilabel"} field on
                                                                                          product form

  GTIN of contained      Unit Product  (02)(\\d{14})                      Numeric         Packaging
  trade items                                                             identifier      

  Ship to / Deliver to   Destination   (410)(\\d{13})                     Numeric         Destination location
  global location        location                                         identifier      

  Ship / Deliver for     Destination   (413)(\\d{13})                     Numeric         Source location
  forward                location                                         identifier      

  I.D. of a physical     Location      (414)(\\d{13})                     Numeric         Location
  location                                                                identifier      

  Batch or lot number    Lot           \(10\)                             Alpha-numeric   Lot
                                       (\[!\"%-/0-9:-?A-Z\_a-z\]{0,20})   name            

  Serial number          Lot           \(21\)                             Alpha-numeric   Serial number
                                       (\[!\"%-/0-9:-?A-Z\_a-z\]{0,20})   name            

  Packaging date         Packaging     (13)(\\d{6})                       Date            Pack date
  (YYMMDD)               Date                                                             

  Best before date       Best before   (15)(\\d{6})                       Date            Best before date
  (YYMMDD)               Date                                                             

  Expiration date        Expiration    (17)(\\d{6})                       Date            Expiry date
  (YYMMDD)               Date                                                             

  Variable count of      Quantity      (30)(\\d{0,8})                     Measure         UoM: Units
  items                                                                                   

  Count of trade items   Quantity      (37)(\\d{0,8})                     Measure         Qty in units for containers
                                                                                          (AI 02)

  Net weight: kilograms  Quantity      (310\[0-5\])(\\d{6})               Measure         Qty in kg
  (kg)                                                                                    

  Length in meters (m)   Quantity      (311\[0-5\])(\\d{6})               Measure         Qty in m

  Net volume: liters (L) Quantity      (315\[0-5\])(\\d{6})               Measure         Qty in L

  Net volume: cubic      Quantity      (316\[0-5\])(\\d{6})               Measure         Qty in m^3^
  meters (m^3^)                                                                           

  Length in inches (in)  Quantity      (321\[0-5\])(\\d{6})               Measure         Qty in inches

  Net weight/volume:     Quantity      (357\[0-5\])(\\d{6})               Measure         Qty in oz
  ounces (oz)                                                                             

  Net volume: cubic feet Quantity      (365\[0-5\])(\\d{6})               Measure         Qty in ft^3^
  (ft^3^)                                                                                 

  Packaging type         Packaging     \(91\)                             Alpha-numeric   Package type
                         Type          (\[!\"%-/0-9:-?A-Z\_a-z\]{0,90})   name            
  ---------------------------------------------------------------------------------------------------------------------
