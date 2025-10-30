# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_check_types/picture_check.md

Take a Picture quality check
============================

In Odoo *Quality*, a *Take a Picture* check is one of the quality check
types that can be selected when creating a new quality check or quality
control point (QCP). *Take a Picture* checks require a picture to be
attached to the check, which can then be reviewed by a quality team.

Create a Take a Picture quality check
-------------------------------------

There are two distinct ways that *Take a Picture* quality checks can be
created. A single check can be manually created. Alternatively, a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} can be
configured that automatically creates checks at a predetermined
interval.

This documentation only details the configuration options that are
unique to *Take a Picture* quality checks and
`QCP (Quality Control Points)`{.interpreted-text role="abbr"}. For a
full overview of all the configuration options available when creating a
single check or a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, see the documentation on `quality checks
<quality/quality_management/quality-checks>`{.interpreted-text
role="ref"} and `quality control points
<quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"}.

### Quality check

To create a single *Take a Picture* quality check, navigate to
`Quality --> Quality
Control --> Quality Checks`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"}. Fill out the new quality
check form as follows:

-   In the `Type`{.interpreted-text role="guilabel"} drop-down field,
    select the `Take a Picture`{.interpreted-text role="guilabel"}
    quality check type.
-   In the `Team`{.interpreted-text role="guilabel"} drop-down field,
    select the quality team responsible for managing the check.
-   In the `Instructions`{.interpreted-text role="guilabel"} text field
    of the `Notes`{.interpreted-text role="guilabel"} tab, enter
    instructions for how the picture should be taken.

{.align-center}

### Quality control point

To create a `QCP (Quality Control Point)`{.interpreted-text role="abbr"}
that generates *Take a Picture* quality checks automatically, navigate
to `Quality --> Quality Control --> Control Points`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}. Fill out the new
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form as
follows:

-   In the `Type`{.interpreted-text role="guilabel"} drop-down field,
    select the `Take a Picture`{.interpreted-text role="guilabel"}
    quality check type.
-   If the *Maintenance* app is installed, a `Device`{.interpreted-text
    role="guilabel"} field appears after selecting the *Take a Picture*
    check type. Use this field to specify a device that should be used
    to take quality check pictures. For information about managing
    devices in the *Maintenance* app, see the documentation on
    `adding new equipment <maintenance/equipment_management/add_new_equipment>`{.interpreted-text
    role="ref"}.
-   In the `Team`{.interpreted-text role="guilabel"} drop-down field,
    select the quality team responsible for managing the checks created
    by the `QCP (Quality Control Point)`{.interpreted-text role="abbr"}.
-   In the `Instructions`{.interpreted-text role="guilabel"} text field,
    enter instructions for how the picture should be taken.

{.align-center}

Process a Take a Picture quality check
--------------------------------------

Once created, there are multiple ways that *Take a Picture* quality
checks can be processed. If a quality check is assigned to a specific
inventory, manufacturing, or work order, the check can be processed on
the order itself. Alternatively, a check can be processed from the
check\'s page.

### From the check\'s page

To process a *Take a Picture* quality check from the check\'s page,
begin by navigating to
`Quality --> Quality Control --> Quality Checks`{.interpreted-text
role="menuselection"}, and then select a quality check. Follow the
`Instructions`{.interpreted-text role="guilabel"} for how to take the
picture.

After taking the picture, make sure it is stored on the device being
used to process the quality check (computer, tablet, etc.). Then, click
the `✏️ (pencil)`{.interpreted-text role="guilabel"} button in the
`Picture`{.interpreted-text role="guilabel"} section to open the
device\'s file manager. In the file manager, navigate to the picture,
select it, and click `Open`{.interpreted-text role="guilabel"} to attach
it.

{.align-center}

### On an order

To process a *Take a Picture* quality check on an order, select a
manufacturing order or inventory order (receipt, delivery, return,
etc.), for which a check is required. Manufacturing orders can be
selected by navigating to
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

Follow the instructions detailing how to take the picture, which are
shown on the `Quality
Check`{.interpreted-text role="guilabel"} pop-up window. After taking
the picture, make sure it is stored on the device being used to process
the quality check (computer, tablet, etc.).

Then, click the `Take a Picture`{.interpreted-text role="guilabel"}
button in the `Picture`{.interpreted-text role="guilabel"} section to
open the device\'s file manager. In the file manager, navigate to the
picture, select it, and click `Open`{.interpreted-text role="guilabel"}
to attach it. Finally, click `Validate`{.interpreted-text
role="guilabel"} on the `Quality Check`{.interpreted-text
role="guilabel"} pop-up window to complete the quality check.

{.align-center}

If a quality alert must be created, click the
`Quality Alert`{.interpreted-text role="guilabel"} button that appears
at the top of the manufacturing or inventory order after the check is
validated. Clicking `Quality Alert`{.interpreted-text role="guilabel"}
opens a quality alert form on a new page. For a complete guide on how to
fill out quality alert forms, view the documentation on `quality alerts
<quality/quality_management/quality-alerts>`{.interpreted-text
role="ref"}.

### On a work order

When configuring a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} that is triggered during manufacturing, a specific work
order can also be specified in the
`Work Order Operation`{.interpreted-text role="guilabel"} field on the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form. If a
work order is specified, a *Take a Picture* quality check is created for
that specific work order, rather than the manufacturing order as a
whole.

*Take a Picture* quality checks configured for work orders **must** be
completed from the *Shop Floor* module. To do so, begin by navigating to
`Manufacturing --> Operations -->
Manufacturing Orders`{.interpreted-text role="menuselection"}. Then,
select an `MO (Manufacturing Order)`{.interpreted-text role="abbr"} that
includes a work order for which a *Take a Picture* quality check is
required.

On the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, select
the `Work Orders`{.interpreted-text role="guilabel"} tab, and then click
the `Open Work Order
(external link icon)`{.interpreted-text role="guilabel"} button on the
line of the work order to be processed. On the resulting
`Work Orders`{.interpreted-text role="guilabel"} pop-up window, click
the `Open Shop Floor`{.interpreted-text role="guilabel"} button to open
the *Shop Floor* module.

When accessed from a specific work order, the *Shop Floor* module opens
to the page for the work center where the order is configured to be
processed, and isolates the work order\'s card, so no other cards are
shown.

Process the work order\'s steps until the *Take a Picture* quality check
step is reached. Click on the step to open a pop-up window that includes
instructions for how the picture should be taken. After taking the
picture, make sure it is stored on the device being used to process the
quality check (computer, tablet, etc.).

Then, click the `Take a Picture`{.interpreted-text role="guilabel"}
button on the pop-up window to open the device\'s file manager. In the
file manager, navigate to the picture, select it, and click
`Open`{.interpreted-text role="guilabel"} to attach it.

Finally, click `Validate`{.interpreted-text role="guilabel"} at the
bottom of the pop-up window to complete the quality check. The pop-up
window then moves on to the next step of the work order.

{.align-center}

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

Review picture attached to quality check
----------------------------------------

After a picture has been attached to a check, it can then be reviewed by
quality team members or other users. To do so, navigate to
`Quality --> Quality Control --> Quality Checks`{.interpreted-text
role="menuselection"}, and select a quality check to review.

The attached picture appears in the `Picture`{.interpreted-text
role="guilabel"} section of the quality check form. After reviewing the
picture, click the `Pass`{.interpreted-text role="guilabel"} button if
the check passes, or the `Fail`{.interpreted-text role="guilabel"}
button if the check fails.

{.align-center}
