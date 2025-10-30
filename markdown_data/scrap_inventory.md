# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/scrap_inventory.md

Scrap inventory
===============

Sometimes, products in a company\'s warehouse stock might be found to be
damaged or defective, past the point of being reparable. If it is not
possible to repair the product, or return the product to a vendor, it
can be scrapped.

Odoo *Inventory* allows users to scrap inventory, designating goods or
materials that are no longer usable or sellable for disposal (or
recycling).

Scrapping inventory in a database helps stock counts remain accurate, by
removing scrapped products from physical inventory, and placing it in a
virtual scrap location (*Virtual Locations/Scrap*).

::: {.note}
::: {.title}
Note
:::

*Virtual locations* in Odoo are **not** real, physical spaces in a
warehouse. Rather, they are designated locations in a database that
provide tracking of items that shouldn\'t be counted in a physical
inventory.

For more information about virtual locations, see the documentation
about the different types of
`location types <inventory/warehouses_storage/location-type>`{.interpreted-text
role="ref"}.
:::

Scrap from stock
----------------

To create a new scrap order (SP) for an in-stock product, navigate to
`Inventory app
--> Operations --> Scrap`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"}. This opens a new
`SP (Scrap Order)`{.interpreted-text role="abbr"} form.

Click the drop-down menu in the `Product`{.interpreted-text
role="guilabel"} field, and select the product that should be scrapped
from inventory. In the `Quantity`{.interpreted-text role="guilabel"}
field, change the value to the quantity of the product that should be
scrapped (by default, this value is set to [1.00]{.title-ref}).

{.align-center}

The `Source Location`{.interpreted-text role="guilabel"} defaults to the
location where the product is currently stored. The
`Scrap Location`{.interpreted-text role="guilabel"} defaults to the
designated scrap location (`Virtual
Locations/Scrap`{.interpreted-text role="guilabel"}). Either of these
locations can be changed by selecting a different location from their
respective drop-down menus.

If the scrapping is tied to a specific existing operation, specify the
operation in the `Source Document`{.interpreted-text role="guilabel"}
field.

The `Company`{.interpreted-text role="guilabel"} field displays the
company whose warehouse this product belongs to. If a replenishment rule
is set up for the product being scrapped, and if the product should be
replenished, tick the checkbox for
`Replenish Quantities`{.interpreted-text role="guilabel"}.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to
complete the new `SP (Scrap Order)`{.interpreted-text role="abbr"}. Once
validated, a `Product Moves`{.interpreted-text role="guilabel"} smart
button appears at the top of the form. Click the smart button to view
the details of the scrap operation.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To view the all-time total quantities of scrapped items, navigate to
`Inventory
app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}. Click the `x (remove)`{.interpreted-text
role="guilabel"} button on the `Internal`{.interpreted-text
role="guilabel"} filter in the `Search...`{.interpreted-text
role="guilabel"} bar, to display virtual locations.

Select the `Virtual Locations/Scrap`{.interpreted-text role="guilabel"}
location. From the `Scrap`{.interpreted-text role="guilabel"}
location\'s form, click the `Current Stock`{.interpreted-text
role="guilabel"} smart button, at the top of the form.

A list of all scrapped products, and their quantities, is displayed.

{.align-center}
:::

Scrap from an existing operation
--------------------------------

Scrap orders (SPs) can *also* be created from existing operations, such
as receipts, delivery orders, and internal transfers, before they are
entered into, or removed from, stock for an operation.

To scrap a product during an operation, navigate to the
`Inventory app`{.interpreted-text role="menuselection"}. From the
`Inventory Overview`{.interpreted-text role="guilabel"}, click the
`# To Process`{.interpreted-text role="guilabel"} button on an
operation\'s task card (i.e. the `Receipts`{.interpreted-text
role="guilabel"} task card).

{.align-center}

Then, select an operation to process from the resulting list of existing
orders. Doing so opens that operation\'s form.

Click the `fa-cog`{.interpreted-text role="icon"}
`(cog)`{.interpreted-text role="guilabel"} icon, and select
`Scrap`{.interpreted-text role="guilabel"} from the resulting drop-down
menu. This opens a `Scrap Products`{.interpreted-text role="guilabel"}
pop-up window.

{.align-center}

From this pop-up window, click the drop-down menu in the
`Product`{.interpreted-text role="guilabel"} field, and select the
products from the operation that should be scrapped. Adjust the value in
the `Quantity`{.interpreted-text role="guilabel"} field, if necessary.

If the `Product`{.interpreted-text role="guilabel"} selected is tracked
using a lot or serial number, a `Lot/Serial`{.interpreted-text
role="guilabel"} field appears. Specify the tracking number in that
field.

The `Source Location`{.interpreted-text role="guilabel"} and
`Scrap Location`{.interpreted-text role="guilabel"} can be changed, if
needed. If a replenishment rule is set up for the product being
scrapped, and if the product should be replenished, tick the checkbox
for `Replenish Quantities`{.interpreted-text role="guilabel"}.

Once ready, click `Scrap Products`{.interpreted-text role="guilabel"}. A
`Scraps`{.interpreted-text role="guilabel"} smart button appears at the
top of the operation form. Click this smart button to view the details
of all scrap orders created from this specific operation.

{.align-center}
