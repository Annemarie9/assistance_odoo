# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/configure/uom.md

Units of measure
================

In some cases, handling products in different units of measure is
necessary. For example, a business can buy products from a country that
uses the metric system, and then sell those products in a country that
uses the imperial system. In that case, the business needs to convert
the units.

Another case for unit conversion is when a business buys products in a
big pack from a supplier, and then sells those products in individual
units.

Odoo can be set up to use different *units of measure (UoM)* for one
product.

Configuration
-------------

To use different units of measure in Odoo, first go to
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}, and
under the `Products`{.interpreted-text role="guilabel"} section,
activate the `Units of Measure`{.interpreted-text role="guilabel"}
setting. Then, click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

Units of measure categories
---------------------------

After enabling the *Units of Measure* setting, view the default units of
measure categories in
`Inventory app --> Configuration --> UoM Categories`{.interpreted-text
role="menuselection"}. The category is important for unit conversion;
Odoo can convert a product\'s units from one unit to another **only** if
both units belong to the same category.

{.align-center}

Each units of measure category has a reference unit. The reference unit
is highlighted in blue in the `Uom`{.interpreted-text role="guilabel"}
column of the `Units of Measure Categories`{.interpreted-text
role="guilabel"} page. Odoo uses the reference unit as a base for any
new units.

To create a new unit, first select the correct category from the
`Units of Measure
Categories`{.interpreted-text role="guilabel"} page. For example, to
sell a product in a box of six units, click the `Unit`{.interpreted-text
role="guilabel"} category line. Then, on the category page that appears,
click `Add a line`{.interpreted-text role="guilabel"} in the
`Units of Measure`{.interpreted-text role="guilabel"} tab. Then, in the
`Unit of Measure`{.interpreted-text role="guilabel"} field, title the
new unit, such as [Box of 6]{.title-ref}, then in the
`Type`{.interpreted-text role="guilabel"} field, select the appropriate
size reference, such as
`Bigger than the reference Unit of Measure`{.interpreted-text
role="guilabel"}.

If applicable, enter a `UNSPSC Category`{.interpreted-text
role="guilabel"}, which is a globally recognized [code managed by
GS1](https://www.unspsc.org/), that **must** be purchased in order to
use.

In the `Ratio`{.interpreted-text role="guilabel"} field, enter how many
individual units are in the new
`UoM (Unit of Measure)`{.interpreted-text role="abbr"}, such as
[6.00000]{.title-ref} when using the example of the [6-Pack]{.title-ref}
(since a box of six is six times *bigger* than the reference unit,
[1.00000]{.title-ref}).

{.align-center}

Specify a product\'s units of measure
-------------------------------------

To set units of measure on a product, first go to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"} and select a product
to open its product form page.

In the `General Information`{.interpreted-text role="guilabel"} tab,
edit the `Unit of Measure`{.interpreted-text role="guilabel"} field to
specify the unit of measure that the product is sold in. The specified
unit is also the unit used to keep track of the product\'s inventory and
internal transfers.

Edit the `Purchase UoM`{.interpreted-text role="guilabel"} field to
specify the unit of measure that the product is purchased in.

Unit conversion {#inventory/product_replenishment/unit-conversion}
---------------

Odoo automatically converts unit measurements when products have
different `UoMs (Units of
Measure)`{.interpreted-text role="abbr"} and purchase
`UoMs (Units of Measure)`{.interpreted-text role="abbr"}.

This occurs in various scenarios, including:

1.  `Vendor orders <inventory/product_replenishment/buy-in-uom>`{.interpreted-text
    role="ref"}: purchase `UoM (Unit of Measure)`{.interpreted-text
    role="abbr"} on purchase orders (POs) converts to
    `UoM (Unit of Measure)`{.interpreted-text role="abbr"} on internal
    warehouse documents
2.  `Automatic replenishment <inventory/product_replenishment/replenish>`{.interpreted-text
    role="ref"}: generates `POs (Purchase Orders)`{.interpreted-text
    role="abbr"} when the stock levels of a product (tracked in
    `UoM (Unit of Measure)`{.interpreted-text role="abbr"}) dips below a
    certain level. But, the `POs (Purchase Orders)`{.interpreted-text
    role="abbr"} are created using the purchase
    `UoM (Unit of Measure)`{.interpreted-text role="abbr"}
3.  `Sell products <inventory/product_replenishment/sell-in-uom>`{.interpreted-text
    role="ref"}: if a different
    `UoM (Unit of Measure)`{.interpreted-text role="abbr"} is used on
    the sales order (SO), the quantity is converted to the warehouse\'s
    preferred `UoM (Unit of Measure)`{.interpreted-text role="abbr"} on
    the delivery order

### Buy products in the purchase UoM {#inventory/product_replenishment/buy-in-uom}

When creating a new request for quotation (RFQ) in the *Purchase* app,
Odoo automatically uses the product\'s specified purchase unit of
measure. If needed, manually edit the `UoM`{.interpreted-text
role="guilabel"} value on the
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"}.

After the `RFQ (Request for Quotation)`{.interpreted-text role="abbr"}
is confirmed into a `PO (Purchase Order)`{.interpreted-text
role="abbr"}, click the `Receipt`{.interpreted-text role="guilabel"}
smart button at the top of the `PO (Purchase Order)`{.interpreted-text
role="abbr"}.

Odoo automatically converts the purchase unit of measure into the
product\'s sales/inventory unit of measure, so the
`Demand`{.interpreted-text role="guilabel"} column of the delivery
receipt shows the converted quantity.

::: {.example}
When the product\'s purchase `UoM`{.interpreted-text role="guilabel"} is
[Box of 6]{.title-ref}, and its sales/inventory unit of measure is
[Units]{.title-ref}, the `PO (Purchase Order)`{.interpreted-text
role="abbr"} shows the quantity in boxes of six, and the receipt (and
other internal warehouse documents) shows the quantity in units.

![An order of three quantities is placed using the purchase \"UoM\":
{.align-center}

![Upon warehouse receipt, the recorded quantities are in the internal
\"Unit of Measure\":
{.align-center}
:::

### Replenishment {#inventory/product_replenishment/replenish}

A request for quotation for a product can also be generated directly
from the product form using the `Replenish`{.interpreted-text
role="guilabel"} button.

After clicking `Replenish`{.interpreted-text role="guilabel"}, a
replenish assistant box pops up. The purchase unit of measure can be
manually edited in the `Quantity`{.interpreted-text role="guilabel"}
field, if needed. Then, click `Confirm`{.interpreted-text
role="guilabel"} to create the
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"}.

::: {.important}
::: {.title}
Important
:::

A `PO (Purchase Order)`{.interpreted-text role="abbr"} can **only** be
automatically generated if at least **one** vendor is listed in the
product form\'s `Purchase`{.interpreted-text role="guilabel"} tab.
:::

{.align-center}

Navigate to the created `PO (Purchase Order)`{.interpreted-text
role="abbr"} by clicking the `Forecasted`{.interpreted-text
role="guilabel"} smart button on the product form. Scroll down to the
`Forecasted Inventory`{.interpreted-text role="guilabel"} section, and
in the `Requests
for quotation`{.interpreted-text role="guilabel"} line, click the
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"} reference
number to open the draft `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"}. If necessary, the purchase
`UoM (Unit of Measure)`{.interpreted-text role="abbr"} can be edited
directly on the `PO (Purchase Order)`{.interpreted-text role="abbr"}.

### Sell in a different UoM {#inventory/product_replenishment/sell-in-uom}

When creating a new quotation in the *Sales* app, Odoo automatically
uses the product\'s specified unit of measure. If needed, the
`UoM`{.interpreted-text role="guilabel"} can be manually edited on the
quotation.

After the quotation is sent to the customer, and confirmed into a sales
order (SO), click the `Delivery`{.interpreted-text role="guilabel"}
smart button at the top of the `SO (Sales Order)`{.interpreted-text
role="abbr"}. Odoo automatically converts the unit of measure into the
product\'s inventory unit of measure, so the `Demand`{.interpreted-text
role="guilabel"} column of the delivery shows the converted quantity.

For example, if the product\'s `UoM (Unit of Measure)`{.interpreted-text
role="abbr"} on the `SO (Sales Order)`{.interpreted-text role="abbr"}
was changed to [Box of 6]{.title-ref}, but its inventory unit of measure
is [Units]{.title-ref}, the `SO (Sales Order)`{.interpreted-text
role="abbr"} shows the quantity in boxes of six, and the delivery shows
the quantity in units.
