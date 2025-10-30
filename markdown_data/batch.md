# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/picking_methods/batch.md

Batch picking
=============

::: {#inventory/misc/batch_picking}
*Batch picking* enables a single picker to handle multiple orders at
once, reducing the time needed to navigate to the same location in a
warehouse.
:::

When picking in batches, orders are grouped and consolidated into a
picking list. After the picking, the batch is taken to an output
location, where the products are sorted into their respective delivery
packages.

::: {.seealso}
`Use Barcode app for pickings <inventory/warehouses_storage/barcode_picking>`{.interpreted-text
role="ref"}
:::

Since orders *must* be sorted at the output location after being picked,
this picking method suits businesses with a few products that are
ordered often. Storing high-demand items in easily accessible locations
can increase the number of orders that are fulfilled efficiently.

Configuration
-------------

To activate the batch picking option, begin by going to
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Under the `Operations`{.interpreted-text role="guilabel"} section, check
the `Batch
Transfers`{.interpreted-text role="guilabel"} box.

{.align-center}

Since batch picking is a method to optimize the *pick* operation in
Odoo, the `Storage
Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} options under the
`Warehouse`{.interpreted-text role="guilabel"} heading must also be
checked on this settings page. When finished, click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Lastly, enable the warehouse picking feature, by navigating to the
warehouse settings page, which is accessible from
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}.

From here, select the desired warehouse from the list. Then, from the
radio options available for `Outgoing Shipments`{.interpreted-text
role="guilabel"}, select either the
`Send goods in output and then deliver
(2 steps)`{.interpreted-text role="guilabel"} or
`Pack goods, send goods in output and then deliver (3 steps)`{.interpreted-text
role="guilabel"}.

::: {.seealso}
\-
`Delivery in two steps <../daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"} -
`../daily_operations/delivery_three_steps`{.interpreted-text role="doc"}
:::

{.align-center}

Create batch transfers
----------------------

Manually create batch transfers directly from the
`Inventory app --> Operations -->
Batch Transfers`{.interpreted-text role="menuselection"} page. Click the
`New`{.interpreted-text role="guilabel"} button to begin creating a
batch transfer.

On the batch transfer form, fill the following fields out accordingly:

-   `Responsible`{.interpreted-text role="guilabel"}: employee assigned
    to the picking. Leave this field blank if *any* worker can fulfill
    this picking.
-   `Operation Type`{.interpreted-text role="guilabel"}: from the
    drop-down menu, select the operation type under which the picking is
    categorized.
-   `Scheduled Date`{.interpreted-text role="guilabel"}: specifies the
    date by which the `Responsible`{.interpreted-text role="guilabel"}
    person should complete the transfer to the output location.

Next, in the `Transfers`{.interpreted-text role="guilabel"} list, click
`Add a line`{.interpreted-text role="guilabel"} to open the `Add:
Transfers`{.interpreted-text role="guilabel"} window.

If the `Operation Type`{.interpreted-text role="guilabel"} field was
filled, the list will filter transfer records matching the selected
`Operation Type`{.interpreted-text role="guilabel"}.

Click the `New`{.interpreted-text role="guilabel"} button to create a
new transfer.

Once the transfer records are selected, click
`Confirm`{.interpreted-text role="guilabel"} to confirm the batch
picking.

::: {.example}
A new batch transfer assigned to the `Responsible`{.interpreted-text
role="guilabel"}, [Joel Willis]{.title-ref}, for the [Pick]{.title-ref}
`Operation Type`{.interpreted-text role="guilabel"}. The
`Scheduled Date`{.interpreted-text role="guilabel"} is set to [August
11]{.title-ref}.

{.align-center}

Clicking the `Add a line`{.interpreted-text role="guilabel"} button
opens the `Add:Transfers`{.interpreted-text role="guilabel"} window,
displaying only pickings. This is because the
`Operation Type`{.interpreted-text role="guilabel"} was set to
[Pick]{.title-ref} on the batch transfer form.

Click the checkbox to the left of the transfers,
[WH/PICK/00001]{.title-ref} and [WH/PICK/00002]{.title-ref}, to include
them in the new transfer. Then, click the `Select`{.interpreted-text
role="guilabel"} button to close the `Add:Transfers`{.interpreted-text
role="guilabel"} window.

{.align-center}
:::

### Add batch from transfers list {#inventory/warehouses_storage/add-batch-transfers}

Another method of creating batch transfers is available using the
`Add to batch`{.interpreted-text role="guilabel"} option in a list.
Navigate to the `Inventory app --> Operations`{.interpreted-text
role="menuselection"} drop-down menu, and select any of the
`Transfers`{.interpreted-text role="guilabel"} to open a filtered list
of transfers.

![Show all transfer types in a drop-down menu: Receipts, Deliveries, Internal Transfers,
Manufacturings, Batch Transfers, Dropships.](batch/transfers-drop-down.png){.align-center}

On the transfers list, select the checkbox to the left of the selected
transfers to add in a batch. Next, navigate to the
`Actions ⚙️ (gear)`{.interpreted-text role="guilabel"} button, and click
`Add to batch`{.interpreted-text role="guilabel"} from the resulting
drop-down menu.

{.align-center}

Doing so opens an `Add to batch`{.interpreted-text role="guilabel"}
pop-up window, wherein the employee `Responsible`{.interpreted-text
role="guilabel"} for the picking can be assigned.

Choose from the two radio options to add to
`an existing batch transfer`{.interpreted-text role="guilabel"} or
create `a new batch transfer`{.interpreted-text role="guilabel"}.

To begin with a draft, select the `Draft`{.interpreted-text
role="guilabel"} checkbox.

Conclude the process by clicking `Confirm`{.interpreted-text
role="guilabel"}.

{.align-center}

Process batch transfer
----------------------

Handle batch transfers in the
`Inventory app --> Operations --> Batch Transfers`{.interpreted-text
role="menuselection"} page.

From here, select the intended transfer from the list. Then, on the
batch transfer form, input the `Done`{.interpreted-text role="guilabel"}
quantities for each product, under the
`Detailed Operations`{.interpreted-text role="guilabel"} tab. Finally,
select `Validate`{.interpreted-text role="guilabel"} to complete the
picking.

::: {.tip}
::: {.title}
Tip
:::

Be certain the batch transfer is complete when the
`Validate`{.interpreted-text role="guilabel"} button is highlighted in
purple. If the `Check Availability`{.interpreted-text role="guilabel"}
button is highlighted instead, that means there are items in the batch
that are currently *not* available in-stock.
:::

::: {#inventory/management/batch-transfers-example}
::: {.example}
In a batch transfer involving products from pickings,
[WH/PICK/00001]{.title-ref} and [WH/PICK/00002]{.title-ref}, the
`Detailed Operations`{.interpreted-text role="guilabel"} tab shows that
the product, [Cabinet with Doors]{.title-ref}, has been picked because
the `Done`{.interpreted-text role="guilabel"} column matches the value
in the `Reserved`{.interpreted-text role="guilabel"} column. However,
[0.00]{.title-ref} quantities have been picked for the other product,
[Cable Management Box]{.title-ref}.

{.align-center}
:::
:::

Only in-stock products are visible in the
`Detailed Operations`{.interpreted-text role="guilabel"} tab.

To view the complete product list, switch to the
`Operations`{.interpreted-text role="guilabel"} tab. On this list, the
`Demand`{.interpreted-text role="guilabel"} column indicates the
required quantity for the order. The `Reserved`{.interpreted-text
role="guilabel"} column shows the available stock to fulfill the order.
Lastly, the `Done`{.interpreted-text role="guilabel"} column specifies
the products that have been picked, and are ready for the next step.

::: {.example}
The product, [Desk Pad]{.title-ref}, from the same batch as the
`example above
<inventory/management/batch-transfers-example>`{.interpreted-text
role="ref"}, is only visible in the `Operations`{.interpreted-text
role="guilabel"} tab because there are no `Reserved`{.interpreted-text
role="guilabel"} quantities in-stock to fulfill the batch picking.

Click the `Check Availability`{.interpreted-text role="guilabel"} button
to search the stock again for available products.

{.align-center}
:::

### Create backorder

On the batch transfer form, if the `Done`{.interpreted-text
role="guilabel"} quantity of the product is *less* than the
`Reserved`{.interpreted-text role="guilabel"} quantity, a pop-up window
appears.

This pop-up window provides the option:
`Create Backorder?`{.interpreted-text role="guilabel"}.

Clicking the `Create Backorder`{.interpreted-text role="guilabel"}
button automatically creates a new batch transfer, containing the
remaining products.

Click `No Backorder`{.interpreted-text role="guilabel"} to finish the
picking *without* creating another batch picking.

Click `Discard`{.interpreted-text role="guilabel"} to cancel the
validation, and return to the batch transfer form.

{.align-center}

Process batch transfer: Barcode app {#inventory/warehouses_storage/barcode_picking}
-----------------------------------

Created batch transfers are also listed in the
`Barcode`{.interpreted-text role="menuselection"} app, accessible by
selecting the `Batch Transfers`{.interpreted-text role="guilabel"}
button.

By default, confirmed batch pickings appear on the
`Batch Transfers`{.interpreted-text role="guilabel"} page. On that page,
click on the desired batch transfer to open the detailed list of
products for the picking.

{.align-center}

For the chosen batch transfer, follow the instructions at the top of the
page in the black background. Begin by scanning the product\'s barcode
to record a single product for picking. To record multiple quantities,
click the `✏️ (pencil)`{.interpreted-text role="guilabel"} icon, and
enter the required quantities for the picking.

::: {.note}
::: {.title}
Note
:::

Products from the same order are labeled with the same color on the
left. Completed pickings are highlighted in green.
:::

::: {.example}
In a batch transfer for 2 [Cabinet with Doors]{.title-ref}, 3 [Acoustic
Bloc Screens]{.title-ref}, and 4 [Four Person Desks]{.title-ref}, the
[3/3]{.title-ref} and [4/4]{.title-ref} `Units`{.interpreted-text
role="guilabel"} indicate that the last two product pickings are
complete.

[1/2]{.title-ref} units of the [Cabinet with Doors]{.title-ref} has
already been picked, and after scanning the product barcode for the
second cabinet, Odoo prompts the user to [Scan a serial
number]{.title-ref} to record the unique serial number for
`product tracking <inventory/product_management/configure-lots>`{.interpreted-text
role="ref"}.

{.align-center}
:::

Once all the products have been picked, click on
`Validate`{.interpreted-text role="guilabel"} to mark the batch transfer
as `Done`{.interpreted-text role="guilabel"}.
