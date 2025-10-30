# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/workflows/scrap_manufacturing.md

Scrap during manufacturing
==========================

During the manufacturing process, the need to scrap manufacturing
components or finished products may arise. This can be necessary if a
component or product is damaged, or unusable for any other reason.

By default, scrapping a component or finished product removes it from
physical inventory and places it in a virtual location titled *Virtual
Locations/Scrap*. A virtual location is **not** a physical space, but
rather a designation in Odoo that is used to track items that are no
longer in physical inventory.

::: {.seealso}
For more information, see the documentation about the different types of
`locations
<../../inventory/warehouses_storage/inventory_management>`{.interpreted-text
role="doc"}.
:::

Components can be scrapped from both the *Manufacturing* app and the
*Shop Floor* module, before the associated manufacturing order (MO) is
closed. Finished products can only be scrapped from the *Manufacturing*
app, and only after closing the associated
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

::: {.tip}
::: {.title}
Tip
:::

Scrap orders can be viewed by navigating to
`Inventory --> Operations --> Scrap`{.interpreted-text
role="menuselection"}. Each scrap order shows the date and time the
order was created, along with the product and quantity that was
scrapped.

To view the total quantity of each item scrapped, navigate to
`Inventory -->
Configuration --> Locations`{.interpreted-text role="menuselection"},
then remove the `Internal`{.interpreted-text role="guilabel"} filter
from the `Search...`{.interpreted-text role="guilabel"} bar to display
all virtual locations. From the list, select the
`Virtual Locations/Scrap`{.interpreted-text role="guilabel"} location.
:::

Scrap pop-up window {#manufacturing/management/scrap-window}
-------------------

Scrapping components and finished products is done through the
`Scrap`{.interpreted-text role="guilabel"} pop-up window. The pop-up
window can be accessed from an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} in the
backend, or the *Shop Floor* module.

### Scrap component from Manufacturing

To scrap a component from an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, begin by
navigating to `Manufacturing -->
Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and then select an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}. At the top of
the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, click the
`Scrap`{.interpreted-text role="guilabel"} button to open the
`Scrap`{.interpreted-text role="guilabel"} pop-up window.

### Scrap finished product from Manufacturing

To scrap a finished product from an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, begin by
navigating to `Manufacturing -->
Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}. Select an open
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, and then
click the `Produce
All`{.interpreted-text role="guilabel"} button to close it.

To select an `MO (Manufacturing Order)`{.interpreted-text role="abbr"}
that has already been closed, navigate to `Manufacturing -->
Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, remove the `To Do`{.interpreted-text
role="guilabel"} filter from the `Search...`{.interpreted-text
role="guilabel"} bar, and then select the desired
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

Once closed, click the `Scrap`{.interpreted-text role="guilabel"} button
at the top of the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} to open the `Scrap`{.interpreted-text role="guilabel"}
pop-up window.

### Scrap component from Shop Floor

To scrap a component from the *Shop Floor* module, begin by navigating
to `Shop
Floor`{.interpreted-text role="menuselection"}. Then, either click the
`⋮ (three vertical dots)`{.interpreted-text role="guilabel"} button on
an `MO (Manufacturing Order)`{.interpreted-text role="abbr"} card, or
select a work center from the top navigation, and click the
`⋮ (three vertical dots)`{.interpreted-text role="guilabel"} button on a
work order card.

Either method opens the `What do you want to do?`{.interpreted-text
role="guilabel"} pop-up window. Click the `Scrap`{.interpreted-text
role="guilabel"} button on the window to open the
`Scrap`{.interpreted-text role="guilabel"} pop-up window.

Scrap pop-up window
-------------------

After opening the scrap pop-up window using one of the methods
`detailed above
<manufacturing/management/scrap-window>`{.interpreted-text role="ref"},
select the component or finished product being scrapped, from the
`Product`{.interpreted-text role="guilabel"} drop-down menu.

In the `Quantity`{.interpreted-text role="guilabel"} field, enter the
quantity being scrapped.

By default, the `Source Location`{.interpreted-text role="guilabel"}
field is set to the warehouse\'s pre-production location, while the
`Scrap Location`{.interpreted-text role="guilabel"} field is set to the
`Virtual Locations/Scrap`{.interpreted-text role="guilabel"} location.
If either the source or scrap location should be changed, select a
different location from their respective drop-down menus.

Enable the `Replenish Scrapped Quantities`{.interpreted-text
role="guilabel"} checkbox if a picking order should be created to
replace the scrapped component(s) upon confirmation of the scrap order.
This option should only be enabled for warehouses with
`two-step <../basic_setup/two_step_manufacturing>`{.interpreted-text
role="doc"} or
`three-step <../basic_setup/three_step_manufacturing>`{.interpreted-text
role="doc"} manufacturing enabled, since components are not picked as
part of the
`one-step <../basic_setup/one_step_manufacturing>`{.interpreted-text
role="doc"} manufacturing process.

{.align-center}

Click the `Scrap`{.interpreted-text role="guilabel"} button to scrap the
selected component. After one or more scrap orders have been created, a
`Scraps`{.interpreted-text role="guilabel"} smart button appears at the
top of the screen. Click it to view a list of all scrap orders for the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

If a picking order was automatically created to replenish the scrapped
components, it can be accessed by opening the
`Inventory`{.interpreted-text role="menuselection"} app, clicking the
`# To Process`{.interpreted-text role="guilabel"} button on the
`Pick Components`{.interpreted-text role="guilabel"} card, and selecting
the order.
