# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/product_tracking/create_sn.md

Assign serial numbers
=====================

Assigning serial numbers to individual products allows the for tracking
of properties, `expiration dates <expiration_dates>`{.interpreted-text
role="doc"}, and location throughout the supply chain, which
particularly benefits manufacturers providing after-sales services.

::: {.seealso}
\- [Odoo Tutorials: Serial
Numbers](https://www.youtube.com/watch?v=ZP-gMz2X5AY) -
`serial_numbers`{.interpreted-text role="doc"}
:::

In Odoo, serial numbers are assigned to products:

-   in the
    `Detailed Operations page <inventory/product_management/detailed-operations>`{.interpreted-text
    role="ref"} on a receipt
-   by clicking the
    `Assign Serial Numbers <inventory/product_management/assign-sn>`{.interpreted-text
    role="ref"} button on a receipt
-   in the
    `Open: Stock move window <inventory/product_management/stock-move-section>`{.interpreted-text
    role="ref"} on a receipt
-   `during a manufacturing order
    <../../../manufacturing/basic_setup/configure_manufacturing_product>`{.interpreted-text
    role="doc"} for a product tracked by lot/serial numbers
-   when making an inventory adjustment

::: {#inventory/product_management/detailed-operations-popup}
![Display the **Detailed Operations** smart button and bulleted list
icon on a receipt.](create_sn/assign-serial-numbers.png){.align-center}
:::

Configuration
-------------

To assign serial numbers to products, activate the
`Lots and Serial Numbers`{.interpreted-text role="guilabel"} feature in
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

Then, in the `Inventory`{.interpreted-text role="guilabel"} tab of an
item\'s product form, set the `Tracking`{.interpreted-text
role="guilabel"} field to `By Unique Serial Number`{.interpreted-text
role="guilabel"}.

::: {.seealso}
\-
`Enable serial numbers <inventory/product_management/enable-lots>`{.interpreted-text
role="ref"} -
`Track products by serial numbers <inventory/product_management/configure-lots>`{.interpreted-text
role="ref"}
:::

::: {#inventory/product_management/configure-new-serials}
Next, enable creating new serial numbers by going to
`Inventory app --> Configuration
--> Operations Types`{.interpreted-text role="menuselection"}.
:::

From the `Operations Types`{.interpreted-text role="guilabel"} page,
select the desired operation type (e.g. `Receipts`{.interpreted-text
role="guilabel"}, `Delivery Orders`{.interpreted-text role="guilabel"},
or `Manufacturing`{.interpreted-text role="guilabel"}), and select the
`Create New`{.interpreted-text role="guilabel"} option in the
`Lots/Serial Numbers`{.interpreted-text role="guilabel"} section of the
operation type\'s configuration page.

{.align-center}

Detailed Operations {#inventory/product_management/detailed-operations}
-------------------

Serial numbers can be assigned to products when entering stock for the
first time, from the `Detailed Operations`{.interpreted-text
role="guilabel"} page on the receipt. Receipts can be accessed by
navigating to
`Inventory app --> Operations --> Receipts`{.interpreted-text
role="menuselection"}.

::: {.important}
::: {.title}
Important
:::

Serial numbers can **not** be assigned to products on a request for
quotation (RfQ) or purchase order (PO) --- **only** on a receipt.

![Screenshot of a \"Purchase Order\" with the \"Receipt\" smart button
at the top.](create_sn/purchase-order-or-receipt.png){.align-center}

To record an item\'s serial number before receiving the item, follow the
steps in the next sections to assign serial numbers, but do **not**
click the receipt\'s `Validate`{.interpreted-text role="guilabel"}
button, until the products are received from the vendor.
:::

Assign a single serial number to a product by clicking the
`Detailed Operations`{.interpreted-text role="guilabel"} smart button on
a receipt.

In the `Lot/Serial Number Name`{.interpreted-text role="guilabel"}
column, manually type in the serial number for a single product.

{.align-center}

When finished, click the receipt\'s breadcrumbs, and the assigned serial
numbers are automatically saved.

Assign serial numbers {#inventory/product_management/assign-sn}
---------------------

To generate new serial numbers in a sequence, click the
`+ (plus)`{.interpreted-text role="guilabel"} icon in the
`product line <inventory/product_management/detailed-operations-popup>`{.interpreted-text
role="ref"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

If the icon is not visible, ensure the `Create New`{.interpreted-text
role="guilabel"} option is selected in the
`receipt's configuration page <inventory/product_management/configure-new-serials>`{.interpreted-text
role="ref"}.
:::

Doing so opens the `Assign Serial Numbers`{.interpreted-text
role="guilabel"} pop-up window. The `Number of SN`{.interpreted-text
role="guilabel"} field is auto-filled based on the product quantity
requiring serial numbers. Manually input the first serial number in the
`First SN`{.interpreted-text role="guilabel"} field, and click
`Assign Serial Numbers`{.interpreted-text role="guilabel"} to generate a
sequence of serial numbers based on the first serial number entered.

{.align-center}

Stock move pop-up window {#inventory/product_management/stock-move-section}
------------------------

For various methods of assigning serial numbers in bulk, click the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon in the
`product line <inventory/product_management/detailed-operations-popup>`{.interpreted-text
role="ref"} of a receipt.

### Add a line

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window that appears, manually input the serial numbers in the
`Lot/Serial Number`{.interpreted-text role="guilabel"} column.

{.align-center}

### Generate Serials

Assign multiple serial numbers at once by clicking the
`Generate Serials/Lots`{.interpreted-text role="guilabel"} button in the
`Open: Stock move`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

Doing so opens the `Generate Serial numbers`{.interpreted-text
role="guilabel"} pop-up window, where the first serial number is entered
in the `First SN`{.interpreted-text role="guilabel"} field to generate a
sequence of serial numbers, based on the first serial number entered.

For more details on how to fill in this pop-up window,
`refer to this section
<inventory/product_management/assign-sn>`{.interpreted-text role="ref"}.

### Import Serials

Assign multiple serial numbers at once by clicking the
`Import Serials/Lots`{.interpreted-text role="guilabel"} button in the
`Open: Stock move`{.interpreted-text role="guilabel"} pop-up window.

::: {.important}
::: {.title}
Important
:::

If the button is not visible, ensure the `Create New`{.interpreted-text
role="guilabel"} option is selected in the
`receipt's configuration page <inventory/product_management/configure-new-serials>`{.interpreted-text
role="ref"}.
:::

Doing so opens the `Import Lots`{.interpreted-text role="guilabel"}
pop-up window. Enter each serial number on a separate line in the
`Lots/Serial numbers`{.interpreted-text role="guilabel"} text field.

::: {.tip}
::: {.title}
Tip
:::

Copy/paste serial numbers from an existing excel spreadsheet and add
them to the `Lots/Serial numbers`{.interpreted-text role="guilabel"}
text field.

{.align-center}
:::

Tick the `Keep current lines`{.interpreted-text role="guilabel"}
checkbox to add serial numbers to the list of products, and serial
numbers in the `Lot/Serial Number`{.interpreted-text role="guilabel"}
table, in the `Open: Stock move`{.interpreted-text role="guilabel"}
pop-up window. To replace the serial numbers in the list, leave the
`Keep current lines`{.interpreted-text role="guilabel"} option
unchecked.

Finally, click `Generate`{.interpreted-text role="guilabel"}.

::: {.example}
For a receipt with a `Demand`{.interpreted-text role="guilabel"} of
[3.00]{.title-ref} products, one product has already been assigned a
serial number in the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window.

So, in the `Import Lots`{.interpreted-text role="guilabel"} pop-up
window, two serial numbers, [124]{.title-ref} and [125]{.title-ref} are
assigned to the remaining products by entering the following in the
`Lots/Serial
numbers`{.interpreted-text role="guilabel"} input field:

``` {.}
124
125
```

The `Keep current lines`{.interpreted-text role="guilabel"} option is
selected to add these two serial numbers **in addition** to the serial
number, [123]{.title-ref}, that has already been assigned.

{.align-center}
:::
