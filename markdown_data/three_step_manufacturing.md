# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/basic_setup/three_step_manufacturing.md

Three-step manufacturing
========================

Odoo *Manufacturing* allows users to manufacture products using one,
two, or three steps. When using three-step manufacturing, Odoo creates a
pick components transfer, a manufacturing order (MO), and a store
finished products transfer, and updates inventory counts based on the
number of components removed, and finished products created.

::: {.tip}
::: {.title}
Tip
:::

The number of steps used in manufacturing is set at the warehouse level,
allowing for each warehouse to use a different number of steps. To
change the number of steps used for a specific warehouse, begin by
navigating to
`Inventory --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and then select a warehouse from the
`Warehouses`{.interpreted-text role="guilabel"} screen.

On the `Warehouse Configuration`{.interpreted-text role="guilabel"} tab,
find the `Manufacture`{.interpreted-text role="guilabel"} radio input
field, and select one of the three options:
`Manufacture (1 step)`{.interpreted-text role="guilabel"}, `Pick
components and then manufacture (2 steps)`{.interpreted-text
role="guilabel"}, or `Pick components, manufacture and then
store products (3 steps)`{.interpreted-text role="guilabel"}.

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

Products must be properly configured before they can be manufactured in
Odoo. For details on how to do so, see the documentation on how to
`configure a product for manufacturing
<manufacturing/management/configure-manufacturing-product>`{.interpreted-text
role="ref"}.
:::

Create manufacturing order
--------------------------

To manufacture a product in Odoo *Manufacturing*, begin by navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and then click `New`{.interpreted-text
role="guilabel"} to create a new
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

On the new `MO (Manufacturing Order)`{.interpreted-text role="abbr"},
select the product to be produced from the `Product`{.interpreted-text
role="guilabel"} drop-down menu. The
`Bill of Material`{.interpreted-text role="guilabel"} field
auto-populates with the associated Bill of Materials (BoM).

If a product has more than one configured for it, the specific can be
selected in the `Bill of Material`{.interpreted-text role="guilabel"}
field, and the `Product`{.interpreted-text role="guilabel"} field
auto-populates with the associated product.

After a has been selected, the `Components`{.interpreted-text
role="guilabel"} and `Work Orders`{.interpreted-text role="guilabel"}
tabs auto-populate with the components and operations specified on the .
If additional components or operations are required for the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} being
configured, add them to the `Components`{.interpreted-text
role="guilabel"} and `Work Orders`{.interpreted-text role="guilabel"}
tabs by clicking `Add a line`{.interpreted-text role="guilabel"}.

Finally, click `Confirm`{.interpreted-text role="guilabel"} to confirm
the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

Process pick components transfer
--------------------------------

After confirming a three-step
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, a
`Transfers`{.interpreted-text role="guilabel"} smart button appears at
the top of the page. Click it to be taken to the
`Transfers`{.interpreted-text role="guilabel"} page for the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}. The page
lists two transfers: *WH/PC/XXXXX* (the pick components transfer), and
*WH/SFP/XXXXX* (the store finished products transfer).

Select `WH/PC/XXXXX`{.interpreted-text role="guilabel"} to open the pick
components transfer for the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"}. This transfer is used to track the movement of components
from the locations where they are stored to the location where they are
used to manufacture the product.

After transferring the components out of their storage location, click
`Validate`{.interpreted-text role="guilabel"} at the top of the
transfer, followed by `Apply`{.interpreted-text role="guilabel"} on the
`Immediate Transfer?`{.interpreted-text role="guilabel"} pop-up window
that appears. Doing so marks the transfer as `Done`{.interpreted-text
role="guilabel"}, and updates inventory counts to reflect the quantity
of components transferred.

Finally, return to the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} by clicking the `WH/MO/XXXXX`{.interpreted-text
role="guilabel"} breadcrumb at the top of the page.

{.align-center}

Process manufacturing order
---------------------------

An `MO (Manufacturing Order)`{.interpreted-text role="abbr"} is
processed by completing all of the work orders listed under its
`Work Orders`{.interpreted-text role="guilabel"} tab. This can be done
on the `MO (Manufacturing Order)`{.interpreted-text role="abbr"} itself,
or from the work order tablet view.

### Basic workflow

To complete work orders from the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} itself, begin
by navigating to `Manufacturing
--> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and then select a manufacturing order.

On the `MO (Manufacturing Order)`{.interpreted-text role="abbr"} page,
select the `Work Orders`{.interpreted-text role="guilabel"} tab. Once
work begins on the first work order that needs to be completed, click
the `Start`{.interpreted-text role="guilabel"} button for that work
order. Odoo *Manufacturing* then starts a timer that keeps track of how
long the work order takes to complete.

{.align-center}

When the work order is completed, click the `Done`{.interpreted-text
role="guilabel"} button for that work order. Repeat the same process for
each work order listed on the `Work Orders`{.interpreted-text
role="guilabel"} tab.

{.align-center}

After completing all of the work orders, click
`Produce All`{.interpreted-text role="guilabel"} at the top of the
screen to mark the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} as `Done`{.interpreted-text role="guilabel"}, and register
the manufactured product(s) into inventory.

### Shop Floor workflow

To complete the work orders for an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} using the
*Shop Floor* module, begin by navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and then select an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

On the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, click
on the `Work Orders`{.interpreted-text role="guilabel"} tab, and then
select the `↗️ (square
with arrow coming out of it)`{.interpreted-text role="guilabel"} button
on the line of the first work order to be processed. Doing so opens a
`Work Orders`{.interpreted-text role="guilabel"} pop-up window, with
details and processing options for the work order.

On the pop-up window, select the `Open Shop Floor`{.interpreted-text
role="guilabel"} button at the top-left of the window to open the *Shop
Floor* module.

{.align-center}

When accessed directly from a specific work order within an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, *Shop Floor*
defaults to the page for the work center where the work order is
configured to be carried out. The page shows a card for the work order
that displays the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} number, the product and number of units to be produced, and
the steps required to complete the work order.

{.align-center}

A work order is processed by completing each step listed on its card.
This can be done by clicking on a step, and following the instructions
listed on the pop-up window that appears. Once the step is completed,
click `Next`{.interpreted-text role="guilabel"} to move on to the next
step, if any are required.

Alternatively, work order steps can be completed by clicking the
checkbox that appears on the right side of the step\'s line on the work
order card. When using this method, the step is automatically marked as
completed, without a pop-up window appearing.

The final step on a work order card is titled *Register Production*.
This step is used to register the number of product units that were
produced. If the number produced is equal to the number that the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} was created
for, click the `# Units`{.interpreted-text role="guilabel"} button on
the right side of the line to automatically register that number as the
quantity produced.

If a different number must be entered, click the
`Register Production`{.interpreted-text role="guilabel"} step to open a
pop-up window. Enter the number of units produced in the
`Units`{.interpreted-text role="guilabel"} field, and then click
`Validate`{.interpreted-text role="guilabel"} to register that number.

::: {.note}
::: {.title}
Note
:::

The *Register Production* step appears on every work order card. It must
be completed for the first work order that is processed. After doing so,
the step appears as already completed for each remaining work order in
the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.
:::

After completing all of the steps for a work order, a button appears on
the footer of the work order card. If any other work orders must be
completed before the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} can be closed, the button is titled
`Mark as Done`{.interpreted-text role="guilabel"}. If there are no
additional work orders to complete, the button is titled
`Close Production`{.interpreted-text role="guilabel"}.

Clicking `Mark as Done`{.interpreted-text role="guilabel"} causes the
work order card to fade away. Once it disappears completely, the work
order\'s status is marked as *Finished* on the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, and the next
work order appears in the *Shop Floor* module, on the page of the work
center where it is configured to be carried out. Any additional work
orders can be processed using the instructions detailed in this section.

Clicking `Close Production`{.interpreted-text role="guilabel"} causes
the work order card to fade away. Once it disappears, the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} is marked as
*Done*, and the units of the product that were produced are entered into
inventory.

After clicking `Mark as Done`{.interpreted-text role="guilabel"} or
`Close Production`{.interpreted-text role="guilabel"}, each button is
replaced by an `Undo`{.interpreted-text role="guilabel"} button. Click
the `Undo`{.interpreted-text role="guilabel"} button before the work
order card fades away to keep the work order open.

::: {.tip}
::: {.title}
Tip
:::

This section details the basic workflow for processing an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} in the *Shop
Floor* module. For a more in-depth explanation of the module and all of
its features, please see the `Shop Floor
overview <manufacturing/shop_floor/shop_floor_overview>`{.interpreted-text
role="ref"} documentation.
:::

Process finished product transfer
---------------------------------

After completing the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"}, return to the order\'s `Transfers`{.interpreted-text
role="guilabel"} page by clicking the `Transfers`{.interpreted-text
role="guilabel"} button at the top of the order. This time, select
`WH/SFP/XXXXX`{.interpreted-text role="guilabel"} to open the store
finished products transfer. This transfer is used to track the movement
of finished products from the location where they were manufactured to
the location where they are stored.

After transferring the finished products to their storage location,
click `Validate`{.interpreted-text role="guilabel"} at the top of the
transfer, followed by `Apply`{.interpreted-text role="guilabel"} on the
`Immediate Transfer?`{.interpreted-text role="guilabel"} pop-up window
that appears. Doing so marks the transfer as `Done`{.interpreted-text
role="guilabel"}, and updates inventory counts to reflect the quantity
of finished products transferred.
