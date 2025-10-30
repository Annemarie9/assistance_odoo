# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/report.md

Replenishment report
====================

The *replenishment report* is an interactive dashboard that uses
`manual reordering rules
<reordering_rules>`{.interpreted-text role="doc"}, lead times, and
upcoming demands to forecast quantities of products that need
restocking.

Reordering rules used on this dashboard are normal reordering rules, but
the user benefits from a monitoring menu with extra options to manage
suggestions for replenishment.

This enables users to anticipate future needs, keep less products on
hand without the risk of running out, plan and consolidate orders.

To access the replenishment report, go to
`Inventory app --> Operations -->
Replenishment.`{.interpreted-text role="menuselection"}

The fields and features unique to the replenishment dashboard are
displayed below. For definitions of the other fields, go to the
`Create reordering rules section
<inventory/warehouses_storage/rr-fields>`{.interpreted-text role="ref"}.

By default, the quantity in the `To Order`{.interpreted-text
role="guilabel"} field is the quantity required to reach the set
`Max Quantity`{.interpreted-text role="guilabel"}. However, the
`To Order`{.interpreted-text role="guilabel"} quantity can be adjusted
by clicking on the field and changing the value. To replenish a product
manually, click `fa-truck`{.interpreted-text role="icon"}
`Order Once`{.interpreted-text role="guilabel"}.

Clicking `fa-bell-slash`{.interpreted-text role="icon"}
`Snooze`{.interpreted-text role="guilabel"} temporarily deactivates the
reordering rule for the set period, hiding the entry from the
replenishment dashboard, when it is supposed to appear.

::: {.tip}
::: {.title}
Tip
:::

Defining a `Vendor`{.interpreted-text role="guilabel"} allows filtering
or grouping demands by the vendor. This simplifies the process of
identifying products to order and can reduce shipment costs.
:::



::: {.note}
::: {.title}
Note
:::

Automatic reordering rules appear on this menu, too but are hidden by
default.
:::

Replenishment information
-------------------------

In each line of the replenishment report, clicking the
`fa-info-circle`{.interpreted-text role="icon"}
`(info)`{.interpreted-text role="guilabel"} icon opens the
`Replenishment Information`{.interpreted-text role="guilabel"} pop-up
window, which displays the *lead times* and *forecasted date*.

For detailed information on how to use this feature for replenishment,
go to the `Just in time
logic <inventory/warehouses_storage/just-in-time>`{.interpreted-text
role="ref"} section.
