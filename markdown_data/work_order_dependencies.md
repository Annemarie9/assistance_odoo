# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies.md

Work order dependencies
=======================

When manufacturing certain products, specific operations may need to be
completed before others can begin. In order to ensure operations are
carried out in the correct order, Odoo *Manufacturing* features a *work
order dependencies* setting. Enabling this setting allows for operations
on a Bill of Materials (BoM) to be *blocked* by other operations that
should occur first.

Configuration
-------------

The *work order dependencies* setting is not enabled by default. To
enable it, begin by navigating to
`Manufacturing --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, enable the `Work
Orders`{.interpreted-text role="guilabel"} setting, if it is not already
active.

After enabling the `Work Orders`{.interpreted-text role="guilabel"}
setting, the `Work Order Dependencies`{.interpreted-text
role="guilabel"} setting appears below it. Enable
`Work Order Dependencies`{.interpreted-text role="guilabel"}, then click
`Save`{.interpreted-text role="guilabel"} to confirm the changes.

Add dependencies to BoM
-----------------------

Work order dependencies are configured on a product\'s
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. To do so,
navigate to
`Manufacturing --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}, then select a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, or create a
new one by clicking `New`{.interpreted-text role="guilabel"}.

::: {.admonition}
Learn more

For a complete guide on how to properly configure a new
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, see the
documentation on
`creating a bill of materials <../basic_setup/bill_configuration>`{.interpreted-text
role="doc"}.
:::

On the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, click
on the `Miscellaneous`{.interpreted-text role="guilabel"} tab, then
enable the `Operation
Dependencies`{.interpreted-text role="guilabel"} checkbox. This makes a
new `Blocked By`{.interpreted-text role="guilabel"} option available in
the settings of the `Operations`{.interpreted-text role="guilabel"} tab.

{.align-center}

Next, click on the `Operations`{.interpreted-text role="guilabel"} tab.
On the top-right of the tab, click on the tab\'s
`settings`{.interpreted-text role="guilabel"} button, then enable the
`Blocked By`{.interpreted-text role="guilabel"} checkbox. This makes a
`Blocked By`{.interpreted-text role="guilabel"} field appear for each
operation on the `Operations`{.interpreted-text role="guilabel"} tab.

{.align-center}

In the line of the operation that should be blocked by another
operation, click the `Blocked By`{.interpreted-text role="guilabel"}
field, and an `Open: Operations`{.interpreted-text role="guilabel"}
pop-up window appears. In the `Blocked By`{.interpreted-text
role="guilabel"} drop-down field on the pop-up window, select the
blocking operation that must be completed *before* the operation that is
blocked.

{.align-center}

Finally, save the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} by clicking `Save`{.interpreted-text role="guilabel"}.

Plan work orders using dependencies
-----------------------------------

Once work order dependencies have been configured on a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, Odoo
*Manufacturing* is able to plan when work orders are scheduled, based on
their dependencies. To plan the work orders for a manufacturing order,
begin by navigating to `Manufacturing --> Operations -->
Manufacturing Orders`{.interpreted-text role="menuselection"}.

Next, select a manufacturing order for a product with work order
dependencies set on its `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, or create a new manufacturing order by clicking
`New`{.interpreted-text role="guilabel"}. If a new manufacturing order
is created, select a `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} configured with work order dependencies from the `Bill of
Material`{.interpreted-text role="guilabel"} drop-down field, then click
`Confirm`{.interpreted-text role="guilabel"}.

After confirming the manufacturing order, select the
`Work Orders`{.interpreted-text role="guilabel"} tab to view the work
orders required to complete it. Any work orders that are *not* blocked
by a different work order display a [Ready]{.title-ref} tag in the
`Status`{.interpreted-text role="guilabel"} section.

Work orders that are blocked by one or more work orders display a
[Waiting for another WO]{.title-ref} tag instead. Once the blocking work
order(s) are completed, the tag updates to [Ready]{.title-ref}.

{.align-center}

To schedule the manufacturing order\'s work orders, click the
`Plan`{.interpreted-text role="guilabel"} button at the top of the page.
After doing so, the `Scheduled Start Date`{.interpreted-text
role="guilabel"} field for each work order on the
`Work Orders`{.interpreted-text role="guilabel"} tab auto-fills with the
scheduled start date and time. A blocked work order is scheduled at the
end of the time period specified in the
`Expected Duration`{.interpreted-text role="guilabel"} field of the work
order that precedes it.

{.align-center}

::: {.example}
A manufacturing order is created for Product A. The manufacturing order
has two operations: Cut and Assemble. Each operation has an expected
duration of 60 minutes, and the Assemble operation is blocked by the Cut
operation.

The `Plan`{.interpreted-text role="guilabel"} button for the
manufacturing order is clicked at 1:30 pm, and the Cut operation is
scheduled to begin immediately. Since the Cut operation has an expected
duration of 60 minutes, the Assemble operation is scheduled to begin at
2:30 pm.
:::

### Planning by workcenter

To see a visual representation of how work orders are planned, navigate
to the `Work
Orders Planning`{.interpreted-text role="guilabel"} page by going to
`Manufacturing --> Planning --> Planning by
Workcenter`{.interpreted-text role="menuselection"}. This page shows a
timeline of all the work orders scheduled for each operation.

If one work order is blocked by the completion of another, the work
order that is blocked is shown as scheduled to start after the work
order blocking it. In addition, an arrow connects the two work orders,
leading from the blocking operation to the blocked operation.

{.align-center}
