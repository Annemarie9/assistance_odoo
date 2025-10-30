# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.md

Inventory adjustments
=====================

In any warehouse management system, the recorded inventory counts in the
database might not always match the actual inventory counts in the
warehouse. The discrepancy between the two counts can be due to damages,
human errors, theft, or other factors. As such, inventory adjustments
must be made to reconcile the differences, and ensure that the recorded
counts in the database match the actual counts in the warehouse.

Inventory Adjustments page {#inventory/inventory-adjustments-page}
--------------------------

To view the *Inventory Adjustments* page, navigate to
`Inventory app --> Operations
--> Physical Inventory`{.interpreted-text role="menuselection"}.



In the `Inventory Adjustments`{.interpreted-text role="guilabel"} table,
all products that are currently in stock are listed, with each product
line containing the following information:

-   `Location`{.interpreted-text role="guilabel"}: the specific location
    in the warehouse where a product is stored. This field needs to be
    enabled my going to
    `Inventory app --> Configuration --> Settings`{.interpreted-text
    role="menuselection"} and ticking the
    `Storage Locations`{.interpreted-text role="guilabel"} checkbox.
-   `Product`{.interpreted-text role="guilabel"}: the product whose
    quantity is listed on the inventory adjustment line.
-   `Lot/Serial Number`{.interpreted-text role="guilabel"}: the tracking
    identifier assigned to the specific product listed. It can contain
    letters, numbers, or a combination of both.
-   `UoM`{.interpreted-text role="guilabel"}: the *unit of measure* in
    which the product is measured. Unless otherwise specified (i.e., in
    `Pounds`{.interpreted-text role="guilabel"} or
    `Ounces`{.interpreted-text role="guilabel"}), the default
    `UoM (Unit of
    Measure)`{.interpreted-text role="abbr"} is
    `Units`{.interpreted-text role="guilabel"}.
-   `Counted Quantity`{.interpreted-text role="guilabel"}: the real
    quantity counted during an inventory count. This field is left blank
    by default but can be changed, depending on if it matches the
    `On Hand
    Quantity`{.interpreted-text role="guilabel"} or not.
-   `Difference`{.interpreted-text role="guilabel"}: the difference
    between the `On Hand Quantity`{.interpreted-text role="guilabel"}
    and `Counted Quantity`{.interpreted-text role="guilabel"}, once an
    inventory adjustment is made. The difference is automatically
    calculated after every inventory adjustment.

::: {.note}
::: {.title}
Note
:::

If a specific product has a quantity of more than [1.00]{.title-ref} in
stock, and more than one serial number (or lot number) is assigned, each
uniquely-identified product is displayed on its own product line with
its own lot/serial number, under the
`Lot/Serial Number`{.interpreted-text role="guilabel"} column.
:::

The fields below are optional and can be made visible by clicking the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(settings)`{.interpreted-text role="guilabel"} icon in the top right of
the `Inventory Adjustments`{.interpreted-text role="guilabel"} page.

-   `Inventory Frequency (Days)`{.interpreted-text role="guilabel"}: the
    frequency, in days, for inventory counts. The default value of this
    field is set to [0]{.title-ref}.
-   `Favorite`{.interpreted-text role="guilabel"}: adds a clickable star
    icon next to each product. Adding a favorite will bring the line
    item to the top of the dashboard.
-   `Product Category`{.interpreted-text role="guilabel"}: the category
    assigned internally to a specific product. Unless otherwise
    specified (i.e., as `Consumable`{.interpreted-text role="guilabel"}
    or `Rental`{.interpreted-text role="guilabel"}), the default
    *Product Category* is set to `All`{.interpreted-text
    role="guilabel"}.
-   `Expiration Date`{.interpreted-text role="guilabel"}: the date a
    product will expire, if it is a perishable good. Only products that
    are tracked using lots and serial numbers can be assigned expiration
    information.
-   `Last Count Date`{.interpreted-text role="guilabel"}: the date on
    which the last inventory count occurred.
-   `Available Quantity`{.interpreted-text role="guilabel"}: the
    quantity of a specific product that is currently available, based on
    any outstanding/uncompleted sales orders, purchase orders, or
    manufacturing orders that might change the available quantity once
    fulfilled.
-   `On Hand Quantity`{.interpreted-text role="guilabel"}: the quantity
    of the product currently recorded in the database.
-   `Accounting Date`{.interpreted-text role="guilabel"}: the date on
    which the adjustments will be accounted for in the Odoo
    **Accounting** app.
-   `Scheduled Date`{.interpreted-text role="guilabel"}: the date at
    which a count should be made. If not otherwise specified, this date
    defaults to the 31st of December of the current year.
-   `User`{.interpreted-text role="guilabel"}: the person assigned to
    the count in the database. This can either be the person physically
    counting the inventory, or applying the count in the database.
-   `Company`{.interpreted-text role="guilabel"}: the company whose
    database these inventory adjustments are being made on. The company
    is listed in the top-right corner of the database, next to the user
    currently logged in.

::: {.tip}
::: {.title}
Tip
:::

Some columns are hidden by default. To reveal these columns, click the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(settings)`{.interpreted-text role="guilabel"} icon to the far right of
the form\'s top row, and select any desired column to reveal by clicking
the checkbox next to that option.
:::

::: {.seealso}
\-
`Product type <../../product_management/configure/type>`{.interpreted-text
role="doc"} - `Tracking with lots, serial numbers, and expiration dates
<../../product_management/product_tracking>`{.interpreted-text
role="doc"}
:::

### Create an inventory adjustment

To create a new inventory adjustment from the `Inventory Adjustments
<inventory/inventory-adjustments-page>`{.interpreted-text role="ref"}
page, click `New`{.interpreted-text role="guilabel"}. Doing so creates a
new, blank inventory adjustment line at the bottom of the page.

On this blank inventory adjustment line, define the
`Location`{.interpreted-text role="guilabel"} where the product is
stored. This is necessary to ensure the accuracy of the inventory
adjustment, as the same product can be stored in multiple locations.

Next, click the drop-down menu under the `Product`{.interpreted-text
role="guilabel"} column, and select a product. If the selected product
is tracked using either lots or serial numbers, the desired lot or
serial number can also be chosen from the drop-down menu under the
`Lot/Serial Number`{.interpreted-text role="guilabel"} column.

Next, set the value in the `Counted Quantity`{.interpreted-text
role="guilabel"} column to the quantity counted for that product during
the inventory adjustment process.

To the right of the `Counted Quantity`{.interpreted-text
role="guilabel"} column, the `Scheduled Date`{.interpreted-text
role="guilabel"} and `User`{.interpreted-text role="guilabel"} can also
be changed via their respective drop-down menus. Changing the
`Scheduled Date`{.interpreted-text role="guilabel"} changes the date
that the inventory adjustment should be processed on, and selecting a
responsible `User`{.interpreted-text role="guilabel"} assigns a user to
the specific inventory adjustment (for traceability purposes).

Once all changes have been made to the new inventory adjustment line,
click away from the line. Doing so saves the adjustment, and moves the
line to the top of the page.

If the `Counted Quantity`{.interpreted-text role="guilabel"} is greater
than the `On Hand Quantity`{.interpreted-text role="guilabel"}, the
value in the `Difference`{.interpreted-text role="guilabel"} column is
**green**. If the `Counted Quantity`{.interpreted-text role="guilabel"}
is less than the `On Hand Quantity`{.interpreted-text role="guilabel"},
the value in the `Difference`{.interpreted-text role="guilabel"} column
is **red**. If the quantities match, and haven\'t been changed at all,
no value appears in the `Difference`{.interpreted-text role="guilabel"}
column.



At this stage, the count (`inventory adjustment`{.interpreted-text
role="dfn"}) is recorded, but not yet applied. This means that the
quantity on hand before the adjustment has not yet been updated to match
the new, real counted quantity.

There are two ways to apply the new inventory adjustment. The first way
is to click the `fa-save`{.interpreted-text role="icon"}
`Apply`{.interpreted-text role="guilabel"} button on the line at the far
right of the page. The second way is to click the checkbox on the far
left of the line. Doing so reveals new button options at the top of the
page, one of which is an `Apply`{.interpreted-text role="guilabel"}
button. Clicking this button instead causes an
`Inventory Adjustment`{.interpreted-text role="guilabel"} pop-up window
to appear.



From this pop-up menu, a reference or reason can be assigned to the
inventory adjustment. By default, the
`Inventory Reason`{.interpreted-text role="guilabel"} field is
pre-populated with the date the adjustment is being made on, but can be
changed to reflect whatever reference or reason is desired.

Once ready, click `Apply`{.interpreted-text role="guilabel"} to apply
the inventory adjustment.

::: {.note}
::: {.title}
Note
:::

Applying an inventory adjustment simultaneously creates a
`stock move line (SML)
<../reporting/moves_history>`{.interpreted-text role="doc"} in the
*Moves History* report for traceability.
:::

::: {.tip}
::: {.title}
Tip
:::

Sometimes products end up in unexpected or incorrect locations. To
quickly move a product to a different storage location, check the box
next to the product, and click the `Relocate`{.interpreted-text
role="guilabel"} button at the top of the
`Inventory Adjustments <inventory/inventory-adjustments-page>`{.interpreted-text
role="ref"} page.
:::

Count products
--------------

Counting products (or stock-taking) is a recurring warehouse process to
verify the physical quantity of items against internal inventory
records. The values recorded on file versus what is actually counted in
real life sometimes do not match, so inventory adjustments can be made
on the *Inventory Adjustments* dashboard.

Once a count is complete, go to
`Inventory app --> Operations --> Physical Inventory`{.interpreted-text
role="menuselection"} to verify and update product
`Count Quantities`{.interpreted-text role="guilabel"}, as it is
necessary to do so.

::: {.tip}
::: {.title}
Tip
:::

To print a PDF of a count sheet, first select the desired product
checkboxes, and then click the `fa-print`{.interpreted-text role="icon"}
`Print`{.interpreted-text role="guilabel"} button that appears at the
top of the dashboard. Then, select the `Count sheet`{.interpreted-text
role="guilabel"} option in the sub-menu, which will download a PDF
detailing the selected products.
:::

On each product line, identify whether the value in the
`On Hand Quantity`{.interpreted-text role="guilabel"} column recorded in
the database matches the newly-counted value. If the recorded value and
the counted value do match, select the product using the checkbox, click
the `Actions`{.interpreted-text role="guilabel"} button, then
`Set to quantity on hand`{.interpreted-text role="guilabel"}.

Doing so copies the value from the `On Hand Quantity`{.interpreted-text
role="guilabel"} column over to the `Counted Quantity`{.interpreted-text
role="guilabel"} column, and sets the value of the
`Difference`{.interpreted-text role="guilabel"} column to
[0.00]{.title-ref}. Subsequently, once applied, an inventory move with
[0.00]{.title-ref} `Quantity Done`{.interpreted-text role="guilabel"} is
recorded in the product\'s inventory adjustment history.



If the newly-counted value for a given product does **not** match the
value in the `On
Hand Quantity`{.interpreted-text role="guilabel"} recorded in the
database, instead of clicking the `Set`{.interpreted-text
role="guilabel"} button, record the real value in the field in the
`Counted Quantity`{.interpreted-text role="guilabel"} column.

To do so, click the field in the `Counted Quantity`{.interpreted-text
role="guilabel"} column on the specific inventory adjustment line for
the product whose count is being changed. This automatically assigns a
`Counted Quantity`{.interpreted-text role="guilabel"} of
[0.00]{.title-ref}.

To change this value, type in a new value that matches the real,
newly-counted value. Then, click away from the line. Doing so saves the
adjustment, and automatically adjusts the value in the
`Difference`{.interpreted-text role="guilabel"} column.

Subsequently, once applied, a move with the difference between the
`On Hand Quantity`{.interpreted-text role="guilabel"} and the
`Counted Quantity`{.interpreted-text role="guilabel"} is recorded in the
product\'s inventory adjustment history.



The `Actions`{.interpreted-text role="guilabel"} menu appears when one
or more products\' checkboxes are selected. The
`Actions`{.interpreted-text role="guilabel"} menu includes the option to
`Set to quantity on hand`{.interpreted-text role="guilabel"}, which sets
the selected products\' `Counted Quantity`{.interpreted-text
role="guilabel"} to the `On Hand Quantity`{.interpreted-text
role="guilabel"}, and `Set to 0`{.interpreted-text role="guilabel"},
which sets the selected products\' `Counted Quantity`{.interpreted-text
role="guilabel"} to zero.



::: {.important}
::: {.title}
Important
:::

Sometimes a count occurs, but cannot be applied in the database right
away. In the time between the actual count and applying the inventory
adjustment, product moves can occur. In that case, the on-hand quantity
in the database can change and no longer be consistent with the counted
quantity. As an extra precaution, Odoo asks for confirmation before
applying the inventory adjustment.
:::

### Plan inventory counts

To plan inventory counts, such as a full count of everything currently
in stock, first navigate to
`Inventory app --> Operations --> Physical Inventory`{.interpreted-text
role="menuselection"}.

Then, select the desired products to be counted by clicking the checkbox
on the far left of each product line.

::: {.tip}
::: {.title}
Tip
:::

To request a count of **all** products currently in stock, click the
checkbox at the very top of the table, in the header row next to the
`Location`{.interpreted-text role="guilabel"} label. This selects
**all** product lines.
:::

Once all desired products have been selected, click the
`Request a Count`{.interpreted-text role="guilabel"} button at the top
of the page. Doing so opens the `Request a Count`{.interpreted-text
role="guilabel"} pop-up window, where the following information can be
filled:

-   `Inventory Date`{.interpreted-text role="guilabel"}: the planned
    date of the count.
-   `User`{.interpreted-text role="guilabel"}: the user responsible for
    the count.
-   `Accounting Date`{.interpreted-text role="guilabel"}: the date at
    which the inventory adjustment will be accounted.
-   `Count`{.interpreted-text role="guilabel"}: to leave the on-hand
    quantity of each product line blank, select
    `Leave Empty`{.interpreted-text role="guilabel"}. To pre-fill the
    on-hand quantity of each product line with the current value
    recorded in the database, select
    `Set Current Value`{.interpreted-text role="guilabel"}.

Finally, once ready, click `Confirm`{.interpreted-text role="guilabel"}
to request the count.



::: {.important}
::: {.title}
Important
:::

In the Odoo **Barcode** app, users can only view inventory counts that
are assigned to **them**, and are scheduled for **today** or
**earlier**.
:::

::: {.seealso}
`cycle_counts`{.interpreted-text role="doc"}
:::
