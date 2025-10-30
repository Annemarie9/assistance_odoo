# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/product_tracking/serial_numbers.md

Use serial numbers to track products
====================================

*Serial numbers* are one of the two ways to identify and track products
in Odoo. A serial number is a unique identifier assigned incrementally
(or sequentially) to an item or product, used to distinguish it from
other items and products.

Serial numbers can consist of many different types of characters: they
can be strictly numerical, they can contain letters and other
typographical symbols, or they can be a mix of all of the above.

The goal of assigning serial numbers to individual products is to make
sure that every item\'s history is identifiable when it travels through
the supply chain. This can be especially useful for manufacturers that
provide after-sales services to products that they sell and deliver.

::: {.seealso}
`/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots`{.interpreted-text
role="doc"}
:::

Enable lots & serial numbers {#inventory/product_management/enable-lots}
----------------------------

To track products using serial numbers, the
`Lots & Serial Numbers`{.interpreted-text role="guilabel"} feature must
be enabled. To enable this, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the
`Traceability`{.interpreted-text role="guilabel"} section, and click the
box next to `Lots & Serial
Numbers`{.interpreted-text role="guilabel"}. Remember to click the
`Save`{.interpreted-text role="guilabel"} button to save changes.

{.align-center}

Configure serial number tracking on products {#inventory/product_management/configure-lots}
--------------------------------------------

Once the `Lots & Serial Numbers`{.interpreted-text role="guilabel"}
setting has been activated, individual products can now be tracked using
serial numbers. To configure this, go to `Inventory app --> Products
--> Products`{.interpreted-text role="menuselection"}, and choose a
desired product to track.

Once on the product form, click `Edit`{.interpreted-text
role="guilabel"}, and click the `Inventory`{.interpreted-text
role="guilabel"} tab.

Once on the product form, click `Edit`{.interpreted-text
role="guilabel"}, navigate to the `Inventory`{.interpreted-text
role="guilabel"} tab, and scroll to the `Traceability`{.interpreted-text
role="guilabel"} section. Then, select the
`By Unique Serial Number`{.interpreted-text role="guilabel"} option, and
click `Save`{.interpreted-text role="guilabel"} to save the changes.
Existing or new serial numbers can now be selected and assigned to
newly-received or manufactured batches of this product.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

If a product doesn\'t have a serial number assigned to it, a user error
pop-up window will appear. The error message states that the product(s)
in stock have no lot/serial number. However, a lot/serial number can be
assigned to the product by making an inventory adjustment.
:::

### Create new serial numbers for products already in stock

New serial numbers can be created for products already in stock with no
assigned serial number. To do this, go to
`Inventory --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}, and click `Create`{.interpreted-text
role="guilabel"}. Doing so reveals a blank lots/serial numbers form. On
this form, a new `Lot/Serial Number`{.interpreted-text role="guilabel"}
is generated automatically.

::: {.tip}
::: {.title}
Tip
:::

While Odoo automatically generates a new lot/serial number to follow the
most recent number, it can be edited and changed to any desired number,
by clicking the line under the `Lot/Serial Number`{.interpreted-text
role="guilabel"} field, and changing the generated number.
:::

Once the `Lot/Serial Number`{.interpreted-text role="guilabel"} is
generated, click the blank field next to `Product`{.interpreted-text
role="guilabel"} to reveal a drop-down menu. From this menu, select the
product to which this new number will be assigned.

This form also provides the option to adjust the
`Quantity`{.interpreted-text role="guilabel"}, to assign a unique
`Internal Reference`{.interpreted-text role="guilabel"} number (for
traceability purposes), and to assign this specific lot/serial number
configuration to a specific website in the `Website`{.interpreted-text
role="guilabel"} field (if working in a multi-website environment).

A detailed description of this specific lot/serial number can also be
added in the `Description`{.interpreted-text role="guilabel"} tab below.

When all desired configurations are complete, click the
`Save`{.interpreted-text role="guilabel"} button to save all changes.

{.align-center}

After a new serial number has been created, assigned to the desired
product, and saved, navigate back to the product form, by going to
`Products --> Products`{.interpreted-text role="menuselection"}, and
selecting the product that this newly-created serial number was just
assigned to.

On that product\'s detail form, click the
`Lot/Serial Numbers`{.interpreted-text role="guilabel"} smart button to
view the new serial number.

Manage serial numbers for shipping and receiving
------------------------------------------------

Serial numbers can be assigned for both **incoming** and **outgoing**
goods. For incoming goods, serial numbers are assigned directly on the
purchase order form. For outgoing goods, serial numbers are assigned
directly on the sales order form.

### Assign serial numbers to newly received products

Assigning serial numbers to **incoming** goods can be done on the
receipt, by clicking the
`Detailed Operations smart button <inventory/product_management/detailed-operations>`{.interpreted-text
role="ref"} or by clicking the `⦙≣ (bulleted list)`{.interpreted-text
role="guilabel"} icon in the product line.

::: {.seealso}
`create_sn`{.interpreted-text role="doc"}
:::

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

Clicking `Validate`{.interpreted-text role="guilabel"} before assigning
a serial number to received quantities will cause a
`User Error`{.interpreted-text role="guilabel"} pop-up to appear. The
pop-up requires entry of a lot or serial number for the ordered
products. The `RFQ (request for quotation)`{.interpreted-text
role="abbr"} **cannot** be validated without a serial number being
assigned.

{.align-center}
:::

There are multiple ways to do this: manually assigning serial numbers,
automatically assigning serial numbers, and copy/pasting serial numbers
from a spreadsheet.

#### Assign serial numbers automatically

If a large quantity of products need individual serial numbers assigned
to them, Odoo can automatically generate and assign serial numbers to
each of the individual products.

To accomplish this, start with the `First SN`{.interpreted-text
role="guilabel"} field in the `Detailed Operations`{.interpreted-text
role="guilabel"} pop-up window, and type the first serial number in the
desired order to be assigned.

Then, in the `Number of SN`{.interpreted-text role="guilabel"} field,
type the total number of items that need newly-generated unique serial
numbers assigned to them.

Finally, click `Assign Serial Numbers`{.interpreted-text
role="guilabel"}, and a list will populate with new serial numbers
matching the ordered quantity of products.

{.align-center}

#### Copy/paste serial numbers from a spreadsheet

To copy and paste serial numbers from an existing spreadsheet, first
populate a spreadsheet with all of the serial numbers received from the
supplier (or manually chosen upon receipt). Then, copy and paste them in
the `Lot/Serial Number Name`{.interpreted-text role="guilabel"} column.
Odoo will automatically create the necessary number of lines based on
the amount of numbers pasted in the column.

From here, the `To`{.interpreted-text role="guilabel"} locations and
`Done`{.interpreted-text role="guilabel"} quantities can be manually
entered in each of the serial number lines.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For purchase orders that include large quantities of products to
receive, the best method of serial number assignment is to automatically
assign serial numbers using the `Assign
Serial Numbers`{.interpreted-text role="guilabel"} button located on the
`PO (purchase order)`{.interpreted-text role="abbr"}. This prevents any
serial numbers from being reused or duplicated, and improves
traceability reporting.
:::

Once all product quantities have been assigned a serial number, click
the `Confirm`{.interpreted-text role="guilabel"} button to close the
pop-up. Then, click `Validate`{.interpreted-text role="guilabel"}.

A `Traceability`{.interpreted-text role="guilabel"} smart button appears
upon validating the receipt. Click the `Traceability`{.interpreted-text
role="guilabel"} smart button to see the updated
`Traceability Report`{.interpreted-text role="guilabel"}, which
includes: a `Reference`{.interpreted-text role="guilabel"} document, the
`Product`{.interpreted-text role="guilabel"} being traced, the
`Lot/Serial #`{.interpreted-text role="guilabel"}, and more.

Once all product quantities have been assigned a serial number, click
`Confirm`{.interpreted-text role="guilabel"} to close the popup, and
click `Validate`{.interpreted-text role="guilabel"}. A
`Traceability`{.interpreted-text role="guilabel"} smart button will
appear upon validating the receipt. Click the
`Traceability`{.interpreted-text role="guilabel"} smart button to see
the updated `Traceability Report`{.interpreted-text role="guilabel"},
which includes: a `Reference`{.interpreted-text role="guilabel"}
document, the `Product`{.interpreted-text role="guilabel"} being traced,
the `Lot/Serial #`{.interpreted-text role="guilabel"}, and more.

### Manage serial numbers on delivery orders

Assigning serial numbers to **outgoing** goods can be done directly from
the sales order (SO).

To create an `SO (sales order)`{.interpreted-text role="abbr"}, navigate
to the `Sales`{.interpreted-text role="menuselection"} app, and click
the `Create`{.interpreted-text role="guilabel"} button. Doing so reveals
a new, blank quotation form. On this blank quotation form, fill out the
necessary information, by adding a `Customer`{.interpreted-text
role="guilabel"}, and adding products to the `Product`{.interpreted-text
role="guilabel"} lines (in the `Order Lines`{.interpreted-text
role="guilabel"} tab), by clicking `Add a
product`{.interpreted-text role="guilabel"}.

Then, choose the desired quantity to sell by changing the number in the
`Quantity`{.interpreted-text role="guilabel"} column.

Once the quotation has been filled out, click the
`Confirm`{.interpreted-text role="guilabel"} button to confirm the
quotation. When the quotation is confirmed, the quotation becomes an
`SO (sales order)`{.interpreted-text role="abbr"}, and a
`Delivery`{.interpreted-text role="guilabel"} smart button appears.

Click the `Delivery`{.interpreted-text role="guilabel"} smart button to
view the warehouse receipt form for that specific
`SO (sales order)`{.interpreted-text role="abbr"}.

From here, click the `Additional Options`{.interpreted-text
role="guilabel"} menu, represented by a [hamburger]{.title-ref} icon
(four horizontal lines, located to the right of the
`Unit of Measure`{.interpreted-text role="guilabel"} column in the
`Operations`{.interpreted-text role="guilabel"} tab). Clicking that icon
reveals a `Detailed Operations`{.interpreted-text role="guilabel"}
pop-up.

In the pop-up, a `Lot/Serial Number`{.interpreted-text role="guilabel"}
will be chosen by default, with each product of the total
`Reserved`{.interpreted-text role="guilabel"} quantity listed with their
unique serial numbers (most likely listed in sequential order).

To manually change a product\'s serial number, click the drop-down menu
under `Lot/Serial
Number`{.interpreted-text role="guilabel"}, and choose (or type) the
desired serial number. Then, mark the `Done`{.interpreted-text
role="guilabel"} quantities, and click `Confirm`{.interpreted-text
role="guilabel"} to close the pop-up.

Finally, click the `Validate`{.interpreted-text role="guilabel"} button
to deliver the products.

{.align-center}

Upon validating the delivery order, a `Traceability`{.interpreted-text
role="guilabel"} smart button appears. Click the
`Traceability`{.interpreted-text role="guilabel"} smart button to see
the updated `Traceability Report`{.interpreted-text role="guilabel"},
which includes: a `Reference`{.interpreted-text role="guilabel"}
document, the `Product`{.interpreted-text role="guilabel"} being traced,
the `Date`{.interpreted-text role="guilabel"}, and the
`Lot/Serial #`{.interpreted-text role="guilabel"} assigned.

The `Traceability Report`{.interpreted-text role="guilabel"} can also
include a `Reference`{.interpreted-text role="guilabel"} receipt from
the previous purchase order (PO), if any of the product quantities
shared a serial number assigned during receipt of that specific
`PO (purchase order)`{.interpreted-text role="abbr"}.

Manage serial numbers for different operations types
----------------------------------------------------

By default in Odoo, the creation of new serial numbers is only allowed
upon **receiving** products from a purchase order. **Existing** serial
numbers cannot be used. For sales orders, the opposite is true: new
serial numbers cannot be created on the delivery order, only existing
serial numbers can be used.

To change the ability to use new (or existing) serial numbers on any
operation type, go to
`Inventory app --> Configuration --> Operations Types`{.interpreted-text
role="menuselection"}, and select the desired
`Operation Type`{.interpreted-text role="guilabel"}.

For the `Receipts`{.interpreted-text role="guilabel"} operation type,
found on the `Operations Types`{.interpreted-text role="guilabel"} page,
the `Use Existing Lots/Serial Numbers`{.interpreted-text
role="guilabel"} option can be enabled, by selecting
`Receipts`{.interpreted-text role="guilabel"} from the
`Operations Types`{.interpreted-text role="guilabel"} page, clicking
`Edit`{.interpreted-text role="guilabel"}, and then clicking the
checkbox beside the `Use Existing Lots/Serial Numbers`{.interpreted-text
role="guilabel"} option (in the `Traceability`{.interpreted-text
role="guilabel"} section). Lastly, click the `Save`{.interpreted-text
role="guilabel"} button to save the changes.

For the `Delivery Orders`{.interpreted-text role="guilabel"} operation
type, located on the `Operations Types`{.interpreted-text
role="guilabel"} page, the
`Create New Lots/Serial Numbers`{.interpreted-text role="guilabel"}
option can be enabled, by selecting `Delivery Orders`{.interpreted-text
role="guilabel"} from the `Operations Types`{.interpreted-text
role="guilabel"} page, clicking `Edit`{.interpreted-text
role="guilabel"}, and clicking the checkbox beside the
`Create New Lots/Serial Numbers`{.interpreted-text role="guilabel"}
option (in the `Traceability`{.interpreted-text role="guilabel"}
section). Be sure to click `Save`{.interpreted-text role="guilabel"} to
save changes.

{.align-center}

Serial number traceability
--------------------------

Manufacturers and companies can refer to the traceability reports to see
the entire lifecycle of a product: where it came from (and when), where
it was stored, and who it went to.

To see the full traceability of a product, or group by serial numbers,
go to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}. Doing so reveals the
`Lots/Serial Numbers`{.interpreted-text role="guilabel"} dashboard.

From here, products with serial numbers assigned to them will be listed
by default, and can be expanded to show what serial numbers have been
specifically assigned to them.

To group by serial numbers (or lots), first remove any default filters
from the search bar in the upper-right corner. Then, click
`Group By`{.interpreted-text role="guilabel"}, and select
`Add Custom Group`{.interpreted-text role="guilabel"}, which reveals a
mini drop-down menu. From this mini drop-down menu, select
`Lot/Serial Number`{.interpreted-text role="guilabel"}, and click
`Apply`{.interpreted-text role="guilabel"}.

Doing so reveals all existing serial numbers and lots, and can be
expanded to show all quantities of products with that assigned number.
For unique serial numbers that are not reused, there should be just one
product per serial number.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For additional information regarding an individual serial number (or lot
number), click the line item for the serial number to reveal that
specific serial number\'s `Serial Number`{.interpreted-text
role="guilabel"} form. From this form, click the
`Location`{.interpreted-text role="guilabel"} and
`Traceability`{.interpreted-text role="guilabel"} smart buttons to see
all stock on-hand using that serial number, and any operations made
using that serial number.
:::

::: {.seealso}
`../product_tracking`{.interpreted-text role="doc"}
:::
