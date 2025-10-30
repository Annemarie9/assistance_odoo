# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_management/quality_checks.md

Quality checks
==============

Quality checks are manual inspections conducted by employees, and are
used to ensure the quality of products. In Odoo, a quality check can be
conducted for a single product, or multiple products within the same
inventory operation or manufacturing order.

Using a Quality Control Point (QCP), it is possible to create quality
checks automatically at regular intervals. When quality checks are
created by a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, they appear on a manufacturing or inventory order, where
the employee processing the order will be prompted to complete them. For
a full explanation of how to create and configure a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, see the
documentation on `quality
control points <quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"}.

While quality checks are most commonly created automatically by a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, it is also
possible to manually create a single quality check. Creating a check
manually is useful when an employee wants to schedule a quality check
that will only occur once, or register a quality check that they conduct
unprompted.

Manual quality check
--------------------

To manually create a single quality check, navigate to
`Quality --> Quality Control
--> Quality Checks`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. On the quality check form,
begin by selecting an option from the `Control per`{.interpreted-text
role="guilabel"} drop-down menu:

-   `Operation`{.interpreted-text role="guilabel"} requests a check for
    an entire operation (ex. delivery order) and all products within it.
-   `Product`{.interpreted-text role="guilabel"} requests a check for
    every unit of a product that is part of an operation (ex. every unit
    of a product within a delivery order).
-   `Quantity`{.interpreted-text role="guilabel"} requests a check for
    every quantity of a product that is part of an operation (ex. one
    check for five units of a product within a delivery order).
    Selecting `Quantity`{.interpreted-text role="guilabel"} also causes
    a `Lot/Serial`{.interpreted-text role="guilabel"} drop-down field to
    appear, from which can be selected a specific lot or serial number
    that the quality check should be conducted for.

Next, select an inventory operation from the `Picking`{.interpreted-text
role="guilabel"} drop-down menu or a manufacturing order from the
`Production Order`{.interpreted-text role="guilabel"} drop-down menu.
This is necessary because Odoo needs to know for which operation the
quality check is being conducted.

If the quality check should be assigned to a specific
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, select it
from the `Control
Point`{.interpreted-text role="guilabel"} drop-down menu. This is useful
if the quality check is being created manually, but should still be
recognized as belonging to a specific
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}.

Select a quality check type from the `Type`{.interpreted-text
role="guilabel"} drop-down field:

-   `Instructions`{.interpreted-text role="guilabel"} provides specific
    instructions for how to conduct the quality check.
-   `Take a Picture`{.interpreted-text role="guilabel"} requires a
    picture to be attached to the check before the check can be
    completed.
-   `Print label`{.interpreted-text role="guilabel"} opens a pop-up from
    which labels can be printed. This step can be customized to provide
    instructions about where to add the labels on a product.
-   `Pass - Fail`{.interpreted-text role="guilabel"} is used when the
    product being checked must meet a certain criteria to pass the
    check.
-   Selecting `Measure`{.interpreted-text role="guilabel"} causes a
    `Measure`{.interpreted-text role="guilabel"} input field to appear,
    in which a measurement must be entered before the check can be
    completed.
-   Selecting `Worksheet`{.interpreted-text role="guilabel"} causes a
    `Quality Template`{.interpreted-text role="guilabel"} drop-down
    field to appear. Use it to select a quality worksheet that must be
    filled out to complete the check.

In the `Team`{.interpreted-text role="guilabel"} field, select the
quality team that is responsible for the quality check. In the
`Company`{.interpreted-text role="guilabel"} field, select the company
that owns the product being inspected.

On the `Notes`{.interpreted-text role="guilabel"} tab at the bottom of
the form, enter any relevant instructions in the
`Instructions`{.interpreted-text role="guilabel"} text entry box (ex.
\'Attach a picture of the product\'). In the `Notes`{.interpreted-text
role="guilabel"} text entry box, enter any relevant information about
the quality check (who created it, why it was created, etc.).

Finally, if the check is being processed immediately, click the
`Pass`{.interpreted-text role="guilabel"} button at the top left of the
screen if the check passes, or the `Fail`{.interpreted-text
role="guilabel"} button if the check fails.

{.align-center}

Process quality check
---------------------

Quality checks can be processed directly on the quality check\'s page,
or from a manufacturing or inventory order for which a check is
required. Alternatively, if a quality check is created for a specific
work order operation, the check is processed in the *Shop Floor* module.

::: {.note}
::: {.title}
Note
:::

It is not possible to manually create a single quality check that is
assigned to a specific work order operation. Quality checks for work
order operations can only be created by a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}. See the
documentation on `Quality Control Points
<quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"} for information about how to configure a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} that will
create quality checks for a specific work order operation.
:::

### Quality check page

To process a quality check from the check\'s page, begin by navigating
to `Quality -->
Quality Control --> Quality Checks`{.interpreted-text
role="menuselection"}, then select the check to process. Follow the
instructions for how to complete the check, listed in the
`Instructions`{.interpreted-text role="guilabel"} field of the
`Notes`{.interpreted-text role="guilabel"} tab at the bottom of the
page.

If the quality check passes, click the `Pass`{.interpreted-text
role="guilabel"} button at the top of the page. If the check fails,
click the `Fail`{.interpreted-text role="guilabel"} button, instead.

### Quality check on order

To process a quality check on an order, select a manufacturing or
inventory order (receipt, delivery, return, etc.), for which a check is
required. Manufacturing orders can be selected by navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and clicking on an order. Inventory orders can be
selected by navigating to `Inventory`{.interpreted-text
role="menuselection"}, clicking the `# To Process`{.interpreted-text
role="guilabel"} button on an operation card, and selecting an order.

On the selected inventory or manufacturing order, a purple
`Quality Checks`{.interpreted-text role="guilabel"} button appears at
the top of the order. Click the button to open the
`Quality Check`{.interpreted-text role="guilabel"} pop-up window, which
shows all of the quality checks required for that order.

Follow the instructions that appear on the
`Quality Check`{.interpreted-text role="guilabel"} pop-up window. If a
Pass - Fail check is being processed, complete the check by clicking
`Pass`{.interpreted-text role="guilabel"} or `Fail`{.interpreted-text
role="guilabel"} at the bottom of the pop-up window. For all other
quality check types, a `Validate`{.interpreted-text role="guilabel"}
button appears instead. Click it to complete the check.

{.align-center}

### Quality check on work order

To process a quality check for a work order, begin by navigating to
`Manufacturing
--> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}. Select an that includes a work order for which a
quality check is required.

On the , select the `Work Orders`{.interpreted-text role="guilabel"}
tab, and then click the `Open Work Order
(external link icon)`{.interpreted-text role="guilabel"} button on the
line of the work order to be processed. On the resulting
`Work Orders`{.interpreted-text role="guilabel"} pop-up window, click
the `Open Shop Floor`{.interpreted-text role="guilabel"} button to open
the *Shop Floor* module.

::: {.seealso}
For a full guide to the Shop Floor module, see the `Shop Floor overview
<../../manufacturing/shop_floor/shop_floor_overview>`{.interpreted-text
role="doc"} documentation.
:::

When accessed from a specific work order, the *Shop Floor* module opens
to the page for the work center where the order is configured to be
processed, and isolates the work order\'s card so that no other cards
are shown.

Process the work order\'s steps until the quality check step is reached.
Click on the step to open a pop-up window that details how the check
should be completed. After following the instructions, click
`Validate`{.interpreted-text role="guilabel"} to complete the check.
Alternatively, if a *Pass - Fail* check is being processed, click either
the `Pass`{.interpreted-text role="guilabel"} or
`Fail`{.interpreted-text role="guilabel"} button.

It is also possible to complete a quality check by clicking the checkbox
on the right side of the step. Doing so automatically marks the check as
*Passed*.

::: {.note}
::: {.title}
Note
:::

The specific steps for processing a quality check depend upon the type
of check being conducted. For information about processing each type of
quality check, see the associated documentation:

-   `../quality_check_types/instructions_check`{.interpreted-text
    role="doc"}
-   `../quality_check_types/pass_fail_check`{.interpreted-text
    role="doc"}
-   `../quality_check_types/measure_check`{.interpreted-text role="doc"}
-   `../quality_check_types/picture_check`{.interpreted-text role="doc"}
:::
