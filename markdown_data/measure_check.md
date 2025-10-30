# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_check_types/measure_check.md

Measure quality check
=====================

In Odoo *Quality*, a *Measure* check is one of the quality check types
that can be selected when creating a new quality check or quality
control point (QCP). *Measure* checks prompt users to measure a certain
aspect of a product and record the measurement in Odoo. For the quality
check to pass, the recorded measurement must be within a certain
*tolerance* of a *norm* value.

Create a Measure quality check
------------------------------

There are two distinct ways that *Measure* quality checks can be
created. A single check can be manually created. Alternatively, a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} can be
configured that automatically creates checks at a predetermined
interval.

This documentation only details the configuration options that are
unique to *Measure* quality checks and
`QCPs (Quality Control Points)`{.interpreted-text role="abbr"}. For a
full overview of all the configuration options available when creating a
single check or a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, see the documentation on `quality checks
<quality/quality_management/quality-checks>`{.interpreted-text
role="ref"} and `quality control points
<quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"}.

### Quality check

To create a single *Measure* quality check, navigate to
`Quality --> Quality Control
--> Quality Checks`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. Fill out the new quality check
form as follows:

-   In the `Type`{.interpreted-text role="guilabel"} drop-down field,
    select the `Measure`{.interpreted-text role="guilabel"} quality
    check type.
-   In the `Team`{.interpreted-text role="guilabel"} drop-down field,
    select the quality team responsible for managing the check.
-   In the `Instructions`{.interpreted-text role="guilabel"} text field
    of the `Notes`{.interpreted-text role="guilabel"} tab, enter
    instructions for how the picture should be taken.

{.align-center}

### Quality control point (QCP)

To create a `QCP (Quality Control Point)`{.interpreted-text role="abbr"}
that generates *Measure* quality checks automatically, navigate to
`Quality --> Quality Control --> Control Points`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}. Fill out the new
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form as
follows:

-   In the `Type`{.interpreted-text role="guilabel"} drop-down field,
    select the `Measure`{.interpreted-text role="guilabel"} quality
    check type. Doing so causes two new fields to appear:
    `Norm`{.interpreted-text role="guilabel"} and
    `Tolerance`{.interpreted-text role="guilabel"}.
    -   Use the first text-entry field of the `Norm`{.interpreted-text
        role="guilabel"} field to record the ideal measurement that the
        product should conform to. Use the second text-entry field to
        specify the unit of measurement that should be used.
    -   The `Tolerance`{.interpreted-text role="guilabel"} field
        features two sub-fields: `from`{.interpreted-text
        role="guilabel"} and `to`{.interpreted-text role="guilabel"}.
        Use the `from`{.interpreted-text role="guilabel"} field to
        specify the minimum acceptable measurement, and the
        `to`{.interpreted-text role="guilabel"} field to specify the
        maximum acceptable measurement.
-   In the `Team`{.interpreted-text role="guilabel"} drop-down field,
    select the quality team responsible for managing the checks created
    by the `QCP (Quality Control Point)`{.interpreted-text role="abbr"}.
-   In the `Instructions`{.interpreted-text role="guilabel"} text field,
    enter instructions for how the measurement should be taken.

{.align-center}

Process a Measure quality check
-------------------------------

Once created, there are multiple ways that *Measure* quality checks can
be processed. If a quality check is assigned to a specific inventory,
manufacturing, or work order, the check can be processed on the order
itself. Alternatively, a check can be processed from the check\'s page.

### From the check\'s page

To process a *Measure* quality check from the check\'s page, begin by
navigating to
`Quality --> Quality Control --> Quality Checks`{.interpreted-text
role="menuselection"}, and select a quality check. Follow the
`Instructions`{.interpreted-text role="guilabel"} for how to take the
measurement.

After taking the measurement, record the value in the
`Measure`{.interpreted-text role="guilabel"} field on the quality check
form. To manually pass or fail the check, click `Pass`{.interpreted-text
role="guilabel"} or `Fail`{.interpreted-text role="guilabel"} at the
top-left corner of the check.

Alternatively, if the quality check is assigned to a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} for which
*norm* and *tolerance* values have been specified, click
`Measure`{.interpreted-text role="guilabel"} at the top-left corner of
the check instead. Doing so automatically marks the check as *Passed* if
the recorded value is within the specified *tolerance*, or *Failed* if
the value is outside of it.

### On an order

To process a *Measure* quality check on an order, select a manufacturing
order or inventory order (receipt, delivery, return, etc.), for which a
check is required. Manufacturing orders can be selected by navigating to
`Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and clicking on an order. Inventory orders can be
selected by navigating to `Inventory`{.interpreted-text
role="menuselection"}, clicking the `# To Process`{.interpreted-text
role="guilabel"} button on an operation card, and selecting an order.

On the selected manufacturing or inventory order, a purple
`Quality Checks`{.interpreted-text role="guilabel"} button appears at
the top of the page. Click the button to open the
`Quality Check`{.interpreted-text role="guilabel"} pop-up window, which
shows all of the quality checks required for that order.

To process a *Measure* quality check, measure the product as instructed,
then enter the value in the `Measure`{.interpreted-text role="guilabel"}
field on the pop-up window. Finally, click `Validate`{.interpreted-text
role="guilabel"} to register the recorded value.

{.align-center}

If the value entered is within the range specified in the
`Tolerance`{.interpreted-text role="guilabel"} section of the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, the
quality check passes and the pop-up window closes. The rest of the
manufacturing or inventory order can then be processed as usual.

However, if the value entered is outside of the specified range, a new
pop-up window appears, titled `Quality Check Failed`{.interpreted-text
role="guilabel"}. The body of the pop-up shows a warning message that
states,
`You measured # units and it should be between # units and # units.`{.interpreted-text
role="guilabel"}, as well as the instructions entered in the
`Message If Failure`{.interpreted-text role="guilabel"} tab of the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}. At the
bottom of the pop-up, two buttons appear:
`Correct Measure`{.interpreted-text role="guilabel"} and
`Confirm Measure`{.interpreted-text role="guilabel"}.

{.align-center}

If the measurement was not entered correctly and should be changed,
select `Correct
Measure`{.interpreted-text role="guilabel"}. Doing so re-opens the
`Quality Check`{.interpreted-text role="guilabel"} pop-up window. Enter
the corrected measurement in the `Measure`{.interpreted-text
role="guilabel"} field, and then click `Validate`{.interpreted-text
role="guilabel"} to complete the check.

If the measurement was entered correctly, click
`Confirm Measure`{.interpreted-text role="guilabel"} instead, and the
quality check fails. Follow any instructions that were listed on the
`Quality Check Failed`{.interpreted-text role="guilabel"} pop-up window.

If a quality alert must be created, click the
`Quality Alert`{.interpreted-text role="guilabel"} button that appears
at the top of the manufacturing or inventory order after the check
fails. Clicking `Quality
Alert`{.interpreted-text role="guilabel"} opens a quality alert form on
a new page.

::: {.seealso}
For a complete guide on how to fill out the quality alert form, view the
documentation on
`quality alerts <../quality_management/quality_alerts>`{.interpreted-text
role="doc"}.
:::

### On a work order

When configuring a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} that is triggered during manufacturing, a specific work
order can also be specified in the
`Work Order Operation`{.interpreted-text role="guilabel"} field on the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form. If a
work order is specified, a *Measure* quality check is created for that
specific work order, rather than the manufacturing order as a whole.

*Measure* quality checks configured for work orders **must** be
completed from the *Shop Floor* module. To do so, begin by navigating to
`Manufacturing --> Operations -->
Manufacturing Orders`{.interpreted-text role="menuselection"}. Select an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} that includes
a work order for which a *Measure* quality check is required.

On the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, select
the `Work Orders`{.interpreted-text role="guilabel"} tab, and click the
`Open Work Order
(external link icon)`{.interpreted-text role="guilabel"} button on the
line of the work order to be processed. On the resulting
`Work Orders`{.interpreted-text role="guilabel"} pop-up window, click
the `Open Shop Floor`{.interpreted-text role="guilabel"} button to open
the *Shop Floor* module.

When accessed from a specific work order, the *Shop Floor* module opens
to the page for the work center where the order is configured to be
processed, and isolates the work order\'s card, so no other cards are
shown.

Process the work order\'s steps until the *Measure* quality check step
is reached. Click on the step to open a pop-up window that includes
instructions for how the measurement should be taken. After taking the
measurement, enter it in the `Measure`{.interpreted-text
role="guilabel"} field of the pop-up window, and then click
`Validate`{.interpreted-text role="guilabel"}.

{.align-center}

If the measurement entered is within the range specified in the
`Tolerance`{.interpreted-text role="guilabel"} section of the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, the
quality check passes, and the pop-up window moves on to the next step of
the work order. However, if the measurement entered is outside of the
specified range, a new pop-up window appears, titled
`Quality Check Failed`{.interpreted-text role="guilabel"}.

The body of the `Quality Check Failed`{.interpreted-text
role="guilabel"} pop-up window shows a message that states,
`You measured # units and it should be between # units and # units`{.interpreted-text
role="guilabel"}, as well as the instructions entered in the
`Message If Failure`{.interpreted-text role="guilabel"} tab of the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}. At the
bottom of the pop-up window, two buttons appear:
`Correct Measure`{.interpreted-text role="guilabel"} and
`Confirm Measure`{.interpreted-text role="guilabel"}.

{.align-center}

If the measurement was not entered correctly, and should be changed,
select `Correct
Measure`{.interpreted-text role="guilabel"}. Doing so opens a new pop-up
window, titled `Quality Check`{.interpreted-text role="guilabel"}. Enter
the corrected measure in the `Measure`{.interpreted-text
role="guilabel"} field, and then click `Validate`{.interpreted-text
role="guilabel"} to complete the check and close the pop-up window.

If the measurement was entered correctly, click
`Confirm Measure`{.interpreted-text role="guilabel"} instead, and the
quality check fails. Follow any instructions that were listed on the
`Quality Check Failed`{.interpreted-text role="guilabel"} pop-up window.

If a quality alert must be created, exit the pop-up window by clicking
the `X (close)`{.interpreted-text role="guilabel"} button in the
top-right corner.

Then, click the `⋮ (three vertical dots)`{.interpreted-text
role="guilabel"} button on the bottom-right corner of the work order
card to open the `What do you want to do?`{.interpreted-text
role="guilabel"} pop-up window.

On the `What do you want to do?`{.interpreted-text role="guilabel"}
pop-up window, select the `Create a Quality
Alert`{.interpreted-text role="guilabel"} button. Doing so opens a blank
quality alert form in a new `Quality Alerts`{.interpreted-text
role="guilabel"} pop-up window.

::: {.seealso}
For a complete guide on how to fill out quality alert forms, view the
documentation on
`quality alerts <../quality_management/quality_alerts>`{.interpreted-text
role="doc"}.
:::
