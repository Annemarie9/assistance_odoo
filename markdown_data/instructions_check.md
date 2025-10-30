# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_check_types/instructions_check.md

Instructions quality check
==========================

In Odoo *Quality*, an *Instructions* check is one of the quality check
types that can be selected when creating a new quality check or quality
control point (QCP). *Instructions* checks consist of a text entry field
that allows the creator to provide instructions for how to complete the
check.

For a full overview of how to configure a quality check or a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, see the
documentation on
`quality checks <quality/quality_management/quality-checks>`{.interpreted-text
role="ref"} and `quality control points
<quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"}.

Process an Instructions quality check
-------------------------------------

There are multiple ways that *Instructions* quality checks can be
processed. If a quality check is assigned to a specific manufacturing,
inventory, or work order, the check can be processed on the order
itself. Alternatively, a check can be processed from the check\'s page.

### Process from the quality check\'s page

To process an *Instructions* quality check from the check\'s page, begin
by navigating to
`Quality --> Quality Control --> Quality Checks`{.interpreted-text
role="menuselection"}, and select a quality check. Follow the
`Instructions`{.interpreted-text role="guilabel"} for how to complete
the check.

If the product passes the check, click the `Pass`{.interpreted-text
role="guilabel"} button above the quality check form. If the product
does not pass the check, click the `Fail`{.interpreted-text
role="guilabel"} button, instead.

### Process quality check on an order

To process an *Instructions* quality check on an order, select a
manufacturing order or inventory order (receipt, delivery, return, etc.)
for which a check is required. Manufacturing orders can be selected by
navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and clicking on an order. Inventory orders can be
selected by navigating to `Inventory`{.interpreted-text
role="menuselection"}, clicking the `# To Process`{.interpreted-text
role="guilabel"} button on an operation card, and selecting an order.

On the selected manufacturing or inventory order, a purple
`Quality Checks`{.interpreted-text role="guilabel"} button appears above
the order. Click the button to open the
`Quality Check`{.interpreted-text role="guilabel"} pop-up window, from
which any quality checks created for the order can be processed.

{.align-center}

To complete an *Instructions* quality check, follow the instructions
detailed in the `Quality Check`{.interpreted-text role="guilabel"}
pop-up window. Finally, click `Validate`{.interpreted-text
role="guilabel"} to confirm that the check has been completed.

If an issue or defect is found during the quality check, a quality alert
may need to be created to notify a quality team. To do so, click the
`Quality Alert`{.interpreted-text role="guilabel"} button that appears
at the top of the manufacturing or inventory order after the check is
validated.

Clicking `Quality Alert`{.interpreted-text role="guilabel"} opens a
quality alert form on a new page. For a complete guide on how to fill
out quality alert forms, view the documentation on `quality alerts
<quality/quality_management/quality-alerts>`{.interpreted-text
role="ref"}.

### Process work order quality check

When configuring a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} that is triggered by a manufacturing order, a specific work
order can also be specified in the
`Work Order Operation`{.interpreted-text role="guilabel"} field on the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form. If a
work order is specified, an *Instructions* quality check is created for
that specific work order, rather than the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} as a whole.

Quality checks configured for work orders **must** be completed from the
*Shop Floor* module. To do so, begin by navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}. Select an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} that includes
a work order for which an *Instructions* quality check is required.

On the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, select
the `Work Orders`{.interpreted-text role="guilabel"} tab, and click the
`Open Work Order
(square with arrow coming out of it)`{.interpreted-text role="guilabel"}
button on the line of the work order to be processed. On the resulting
`Work Orders`{.interpreted-text role="guilabel"} pop-up window, click
the `Open Shop Floor`{.interpreted-text role="guilabel"} button to open
the *Shop Floor* module.

When accessed from a specific work order, the *Shop Floor* module opens
to the page for the work center where the order is configured to be
processed, and isolates the work order\'s card so that no other cards
are shown.

Begin processing the work order\'s steps until the *Instructions*
quality check step is reached. Click on the step to open a pop-up window
that details how to complete the quality check. Once completed, click
the `Next`{.interpreted-text role="guilabel"} button to complete the
check, and move on to the next step.

{.align-center}

Alternatively, an *Instructions* quality check can be completed by
clicking the checkbox that appears on the right side of the step\'s line
on the work order card. When using this method, the quality check
automatically passes, without a pop-up window appearing.

::: {.note}
::: {.title}
Note
:::

For a full guide to the *Shop Floor* module, see the
`Shop Floor overview
<manufacturing/shop_floor/shop_floor_overview>`{.interpreted-text
role="ref"} documentation.
:::
