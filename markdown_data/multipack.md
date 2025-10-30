# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/multipack.md

Multi-package shipments
=======================

In some cases, a delivery order with multiple items may need to be
shipped in more than one package. This may be necessary if the items are
too large to ship in a single package, or if certain items cannot be
packaged together. Shipping a single delivery order in multiple packages
provides flexibility for how each item is packaged, without the need to
create multiple delivery orders.

Configuration
-------------

In order to split a delivery order across multiple packages, the
*Packages* setting must be enabled. To do so, navigate to
`Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, then enable the checkbox next to
`Packages`{.interpreted-text role="guilabel"}. Click
`Save`{.interpreted-text role="guilabel"} to confirm the change.

{.align-center}

Ship items in multiple packages {#inventory/shipping/multiple-packages}
-------------------------------

To split items in the same delivery order across multiple packages,
begin by navigating to `Inventory --> Delivery Orders`{.interpreted-text
role="menuselection"}, then select a delivery order that has multiple
items, a multiple quantity of the same item, or both.

On the `Operations`{.interpreted-text role="guilabel"} tab, select the
`⁞≣ (menu)`{.interpreted-text role="guilabel"} icon in the line of the
product that will be shipped in the first package.

{.align-center}

This makes a `Detailed Operations`{.interpreted-text role="guilabel"}
pop-up window appear. In the table at the bottom of the pop-up window,
the `Reserved`{.interpreted-text role="guilabel"} column shows the total
quantity of the product included in the delivery order.

If the full quantity will be shipped in the first package, enter the
number from the `Done`{.interpreted-text role="guilabel"} column in the
`Reserved`{.interpreted-text role="guilabel"} column. If less than the
full quantity will be shipped in the first package, enter a smaller
number than the one that appears in the `Reserved`{.interpreted-text
role="guilabel"} column. Click `Confirm`{.interpreted-text
role="guilabel"} to confirm the `Done`{.interpreted-text
role="guilabel"} quantities and close the pop-up.

{.align-center}

Repeat the same steps for every item quantity that is included in the
first package. Then, click `Put In Pack`{.interpreted-text
role="guilabel"} to create a package with all of the selected items.

{.align-center}

For the next package, follow the same steps as detailed above, marking
the quantity of each item to be included in the package as
`Done`{.interpreted-text role="guilabel"} before clicking
`Put In Pack`{.interpreted-text role="guilabel"} on the delivery order.
Continue doing so until the full quantity of all items are added to a
package.

Finally, after all of the packages have been shipped, click
`Validate`{.interpreted-text role="guilabel"} to confirm that the
delivery order has been completed.

::: {.tip}
::: {.title}
Tip
:::

After one or more packages are created, a `Packages`{.interpreted-text
role="guilabel"} smart button appears in the top-right corner of the
delivery order. Click the `Packages`{.interpreted-text role="guilabel"}
smart button to go to the `Packages`{.interpreted-text role="guilabel"}
page for the delivery order, where each package can be selected to view
all of the items included in it.

{.align-center}
:::

Create a backorder for items to be shipped later
------------------------------------------------

If some items will be shipped at a later date than others, there is no
need to put them in a package until they are ready to be shipped.
Instead, create a backorder for the items being shipped later.

Begin by shipping the items that will be shipped immediately. If they
will be shipped in multiple packages, follow the
`steps above <inventory/shipping/multiple-packages>`{.interpreted-text
role="ref"} to package them as required. If they will be shipped in a
single package, simply mark in the `Done`{.interpreted-text
role="guilabel"} column the quantity of each item being shipped, but
**do not** click the `Put In Pack`{.interpreted-text role="guilabel"}
button.

After all quantities being shipped immediately are marked as
`Done`{.interpreted-text role="guilabel"}, click the
`Validate`{.interpreted-text role="guilabel"} button, and a
`Create Backorder?`{.interpreted-text role="guilabel"} pop-up window
appears. Then, click the `Create Backorder`{.interpreted-text
role="guilabel"} button. Doing so confirms the items being shipped
immediately and creates a new delivery order for the items that will be
shipped later.

{.align-center}

The backorder delivery order will be listed in the chatter of the
original delivery order in a message that reads
`The backorder WH/OUT/XXXXX has been created.`{.interpreted-text
role="guilabel"}. Click on `WH/OUT/XXXXX`{.interpreted-text
role="guilabel"} in the message to view the backorder delivery order.

{.align-center}

The backorder delivery order can also be accessed by navigating to
`Inventory`{.interpreted-text role="menuselection"}, clicking the
`# Back Orders`{.interpreted-text role="guilabel"} button on the
`Delivery Orders`{.interpreted-text role="guilabel"} card, and selecting
the delivery order.

{.align-center}

Once the remaining items are ready to be shipped, navigate to the
backorder delivery order. The items can be shipped in a single package
by clicking `Validate`{.interpreted-text role="guilabel"} and selecting
`Apply`{.interpreted-text role="guilabel"} on the
`Immediate Transfer?`{.interpreted-text role="guilabel"} pop-up window
that appears, or shipped in multiple packages by following the steps
detailed in the section above.

It is also possible to ship out some of the items while creating another
backorder for the rest. To do so, simply follow the same steps used to
create the first backorder.
