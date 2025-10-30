# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/picking_methods/cluster.md

Cluster picking
===============

::: {#inventory/misc/cluster_picking}
Cluster picking is an advanced order fulfillment approach derived from
`batch picking
<inventory/misc/batch_picking>`{.interpreted-text role="ref"}.
:::

In this strategy, pickers load a cart with multiple packages, each
designated for a specific *sales order* (SO). Then, the picker travels
to each storage location, and places the products directly in the
package of the associated order.

This method is most efficient for medium-sized companies, with high
order volumes, and relatively few unique products, since the method
eliminates the need for sorting products into packages for customers
after picking.

However, cluster picking does have some disadvantages. For instance,
urgent orders cannot be prioritized, and optimized batches must be
manually created beforehand. As a result, the picking process can lead
to bottlenecks.

::: {#inventory/misc/cluster_picking/example}
::: {.example}
#\. `SO (Sales Order)`{.interpreted-text role="abbr"} 1 calls for one
apple and orange \#. `SO (Sales Order)`{.interpreted-text role="abbr"} 2
calls for one apple and banana \#. `SO (Sales Order)`{.interpreted-text
role="abbr"} 3 calls for one apple, orange, and banana

Apples are stored in Shelf A, oranges in Shelf B, and bananas in Shelf
C.

To pick products for three orders at once, the cart is loaded with three
empty packages.

Starting at Shelf A, the picker places apples into each package. Next,
the picker navigates to Shelf B, and places oranges in the packages
designated for `SO (Sales Order)`{.interpreted-text role="abbr"} 1 and
`SO (Sales Order)`{.interpreted-text role="abbr"} 3. Finally, the picker
pushes the cart to Shelf C, and loads packages for
`SO (Sales Order)`{.interpreted-text role="abbr"} 2 and
`SO (Sales Order)`{.interpreted-text role="abbr"} 3 with a banana, each.

With the packages for all three `SOs (Sales Orders)`{.interpreted-text
role="abbr"} packed, the picker pushes the cart to the output location,
where the packages are sealed and prepared for shipment.

{.align-center}
:::
:::

Configuration
-------------

To enable cluster picking, begin by navigating to
`Inventory app --> Configuration
--> Settings`{.interpreted-text role="menuselection"}. Under the
`Operations`{.interpreted-text role="guilabel"} heading, activate the
`Packages`{.interpreted-text role="guilabel"} and
`Batch Transfers`{.interpreted-text role="guilabel"} options.

{.align-center}

Since batch picking is used to optimize the *pick* operation in Odoo,
the `Storage
Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} options, under
the `Warehouse`{.interpreted-text role="guilabel"} heading, must also be
checked on this settings page.

*Storage locations* allow products to be stored in specific locations
they can be picked from, while *multi-step routes* enable the picking
operation itself.

When finished, click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

### Packages setup {#inventory/misc/create-package}

After the `Packages`{.interpreted-text role="guilabel"} feature is
enabled, navigate to `Inventory app -->
Products --> Packages`{.interpreted-text role="menuselection"}, and
click the `New`{.interpreted-text role="guilabel"} button to create a
new package.

On the new package form, the `Package Reference`{.interpreted-text
role="guilabel"} is pre-filled with the next available
[PACK]{.title-ref} number in the system. `Pack Date`{.interpreted-text
role="guilabel"} is automatically set to the creation date of the form.

Set the `Package Use`{.interpreted-text role="guilabel"} field to
`Reusable Box`{.interpreted-text role="guilabel"}.

::: {.seealso}
`Packages <../../product_management/configure/package>`{.interpreted-text
role="doc"}
:::

::: {.example}
A package intended for cluster picking is named
[CLUSTER-PACK-3]{.title-ref} for easy identification. For this workflow,
the products are directly packed using their intended shipping boxes, so
`Package Use`{.interpreted-text role="guilabel"} is set to
`Disposable Box`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Create cluster batch
--------------------

To see how cluster picking works in Odoo, navigate to the
`Sales`{.interpreted-text role="menuselection"} app, and create
`SOs (Sales Orders)`{.interpreted-text role="abbr"} that will be
fulfilled together in the same batch. After confirming an
`SO (Sales Order)`{.interpreted-text role="abbr"}, the
`Delivery`{.interpreted-text role="guilabel"} smart button becomes
visible. Displayed inside the icon is a number representing the amount
of steps in the outgoing shipment process.

::: {.example}
Begin by creating three `SOs (Sales Orders)`{.interpreted-text
role="abbr"} for the apples, oranges, and bananas, as shown in the
`example
above <inventory/misc/cluster_picking/example>`{.interpreted-text
role="ref"}.

After confirming the `SO (Sales Order)`{.interpreted-text role="abbr"},
the `Delivery`{.interpreted-text role="guilabel"} smart button displays
the number [2]{.title-ref}, indicating there are two operations to
complete: [Pick]{.title-ref} and [Delivery]{.title-ref}.

{.align-center}
:::

With the `SOs (Sales Orders)`{.interpreted-text role="abbr"} created,
orders now must be grouped into batches. To do so, navigate to the
*Inventory* dashboard and select the operation type card,
`Delivery Orders`{.interpreted-text role="guilabel"} or
`Pick`{.interpreted-text role="guilabel"} (whichever is the first
operation in the delivery flow).

Doing so displays a filtered list of outgoing operations with the
`Ready`{.interpreted-text role="guilabel"} status, indicating that all
the products in the `SO (Sales Order)`{.interpreted-text role="abbr"}
are in stock.

::: {.note}
::: {.title}
Note
:::

Cluster pick batches can be created for outgoing shipments in one, two,
or three steps.
:::

::: {.seealso}
\-
`Delivery in one step <../daily_operations/receipts_delivery_one_step>`{.interpreted-text
role="doc"} -
`Delivery in two steps <../daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"} -
`Delivery in three steps <../daily_operations/delivery_three_steps>`{.interpreted-text
role="doc"}
:::

Click the checkbox to the left of the corresponding outgoing operation
to add them to the batch. With the desired pickings selected, click the
`⚙️ Actions (gear)`{.interpreted-text role="guilabel"} button, and
select the `Add to batch`{.interpreted-text role="guilabel"} option from
the resulting drop-down menu.

::: {.example}
To create a cluster batch, as shown in the `example above
<inventory/misc/cluster_picking/example>`{.interpreted-text role="ref"},
in a warehouse configured with two-step outgoing shipments, the
following pick operations are selected:

-   \`WH/PICK/00007\`: linked to `SO (Sales Order)`{.interpreted-text
    role="abbr"} 88 for one apple and orange.
-   \`WH/PICK/00008\`: linked to `SO (Sales Order)`{.interpreted-text
    role="abbr"} 89 for one apple and banana.
-   \`WH/PICK/00009\`: linked to `SO (Sales Order)`{.interpreted-text
    role="abbr"} 90 for one apple, orange, and banana.

{.align-center}
:::

Doing so opens an `Add to batch`{.interpreted-text role="guilabel"}
pop-up window, wherein the employee `Responsible`{.interpreted-text
role="guilabel"} for the picking can be assigned.

Choose from the two options in the `Add to`{.interpreted-text
role="guilabel"} field to either: add to `an existing
batch transfer`{.interpreted-text role="guilabel"}, or create
`a new batch transfer`{.interpreted-text role="guilabel"}.

To create draft batch pickings to be confirmed at a later date, select
the `Draft`{.interpreted-text role="guilabel"} checkbox.

Conclude the process by clicking `Confirm`{.interpreted-text
role="guilabel"}.

{.align-center}

Process batches
---------------

To process batches, navigate to
`Inventory app --> Operations --> Batch Transfers`{.interpreted-text
role="menuselection"}. Click on a batch to select it.

In the `Detailed Operations`{.interpreted-text role="guilabel"} tab,
products that are to be picked are grouped by location.

Under the `Source Package`{.interpreted-text role="guilabel"} or
`Destination Package`{.interpreted-text role="guilabel"} field, enter
the package used for the picking.

::: {.note}
::: {.title}
Note
:::

Use the `Source Package`{.interpreted-text role="guilabel"} field when
the picking package is configured as *reusable* on the
`package form <inventory/misc/create-package>`{.interpreted-text
role="ref"}. This means the products are temporarily placed in a
container during picking, before getting transferred to their final
shipping box.

Alternatively, use the `Destination Package`{.interpreted-text
role="guilabel"} field when the product is directly placed in its
*disposable* shipping box during picking.
:::

::: {.example}
Process the cluster batch for the three orders of apples, oranges, and
bananas `example
<inventory/misc/cluster_picking/example>`{.interpreted-text role="ref"}
by assigning each picking to a dedicated package.

At the storage location for apples, [WH/Stock/Shelf A]{.title-ref},
assign the apples in all three pickings to one of the three disposable
packages, [CLUSTER-PACK-1]{.title-ref}, [CLUSTER-PACK-2]{.title-ref}, or
[CLUSTER-PACK-3]{.title-ref}.

Record this in Odoo using the `Destination Package`{.interpreted-text
role="guilabel"} field in the `Detailed
Operations`{.interpreted-text role="guilabel"} tab.

{.align-center}
:::

### In Barcode

To process cluster pickings directly from the *Barcode* app, select the
`Batch Transfers`{.interpreted-text role="guilabel"} button from the
*Barcode* dashboard. Then, select the desired batch.

On the batch transfer screen, the products in the picking are grouped by
location, and each line is color-coded to associate products in the same
picking together.

Then, follow the prompt to `Scan the source location`{.interpreted-text
role="guilabel"} barcode for the storage location of the first product.
Then, scan the barcode for the product and package to process the
transfer.

Repeat this for all products, and click the `Validate`{.interpreted-text
role="guilabel"} button.

::: {.note}
::: {.title}
Note
:::

To find the package barcode, navigate to `Inventory app --> Products -->
Packages`{.interpreted-text role="menuselection"}, select the desired
package, click the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon
at the top of the package form, and select the `Print`{.interpreted-text
role="guilabel"} option.

Next, select one of the three print options to generate the package
barcode from the `Package Reference`{.interpreted-text role="guilabel"}
field.

{.align-center}
:::

::: {.example}
Begin processing the cluster picking by going to the first storage
location, [Shelf A]{.title-ref}, and scanning the
`location barcode <barcode/setup/location>`{.interpreted-text
role="ref"}. Doing so highlights all the pickings that need products
from this particular location.

Scan the barcode for the apple, which highlights the picking (labeled in
red) for the product [Apple]{.title-ref}, for the picking,
[WH/PICK/00007]{.title-ref}.

Then, scan the [CLUSTER-PACK-1]{.title-ref} package barcode, and place
the product in the designated package.

{.align-center}
:::

::: {.tip}
::: {.title}
Tip
:::

After creating a batch transfer and assigning a package to a picking,
Odoo suggests the specified package by displaying the name *in italics*
under the product name, ensuring pickers place products into the correct
boxes.
:::
