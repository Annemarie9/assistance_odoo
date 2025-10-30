# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_management/quality_control_points.md

Quality control points
======================

In Odoo, *quality control points* (QCPs), are used to automatically
create `quality checks
<quality_checks>`{.interpreted-text role="doc"} at predetermined
intervals. `QCPs (Quality Control Points)`{.interpreted-text
role="abbr"} can be configured to create quality checks for specific
operations (manufacturing, delivery, etc.), as well as specific products
within those operations.

Using `QCPs (Quality Control Points)`{.interpreted-text role="abbr"}
allows quality teams to ensure products are being regularly inspected
for defects and other issues.

Configure quality control points
--------------------------------

To create a new `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, navigate to
`Quality --> Quality Control --> Control Points`{.interpreted-text
role="menuselection"}, and then click `New`{.interpreted-text
role="guilabel"}.

Begin filling out the new
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} by entering
a unique `Title`{.interpreted-text role="guilabel"} that makes the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} easily
identifiable.

In the `Products`{.interpreted-text role="guilabel"} field, select one
or more products the `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} should apply to. If the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} should
apply to an entire product category, select it in the
`Product Categories`{.interpreted-text role="guilabel"} field.

In the `Operations`{.interpreted-text role="guilabel"} field, select the
operation(s) that should trigger the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}. For
example, selecting the `Manufacturing`{.interpreted-text
role="guilabel"} option in the `Operations`{.interpreted-text
role="guilabel"} field causes a quality check to be created for new
manufacturing orders (MOs).

::: {.note}
::: {.title}
Note
:::

When creating a new `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, at least one operation must be listed in the
`Operations`{.interpreted-text role="guilabel"} field. However, the
`Products`{.interpreted-text role="guilabel"} and
`Product Categories`{.interpreted-text role="guilabel"} fields can be
left blank. If they are left blank, the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} generates
quality checks for every instance of the specified operation(s).
:::

If the `Manufacturing`{.interpreted-text role="guilabel"} operation is
selected in the `Operations`{.interpreted-text role="guilabel"} field, a
new field appears below it, titled
`Work Order Operation`{.interpreted-text role="guilabel"}. From this
field, select a specific work order to generate quality checks for that
operation, rather than the manufacturing operation in general.

For example, a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} could be configured to create quality checks for the
[Assembly]{.title-ref} work order of the [Coffee Table]{.title-ref}
product. Then, if a new is confirmed for a [Coffee Table]{.title-ref},
the `QCP (Quality Control Point)`{.interpreted-text role="abbr"} creates
a quality check specifically for the [Assembly]{.title-ref} operation.

The `Control Per`{.interpreted-text role="guilabel"} field is set to one
of three options that determine *when* a new quality check is created:

-   `Operation`{.interpreted-text role="guilabel"}: one check is
    requested for the specified operation, as a whole.
-   `Product`{.interpreted-text role="guilabel"}: one check is requested
    for each *unique* product included in the specified operation. For
    example, a delivery operation for one table and four chairs would
    generate two checks, since two *unique* products are included in the
    operation.
-   `Quantity`{.interpreted-text role="guilabel"}: a check is requested
    for a certain percentage of items within the specified operation.
    This percentage is set by enabling the
    `Partial Transfer Test`{.interpreted-text role="guilabel"} checkbox,
    and then entering a numerical value in the
    `Percentage`{.interpreted-text role="guilabel"} field that appears
    below. If the checkbox is not enabled, one quality check is created
    for the full quantity.

The `Control Frequency`{.interpreted-text role="guilabel"} field is set
to one of three options that determine *how often* a new quality check
is created:

-   `All`{.interpreted-text role="guilabel"}: a quality check is
    requested every time the conditions of the
    `QCP (Quality Control Point)`{.interpreted-text role="abbr"} are
    met.
-   `Randomly`{.interpreted-text role="guilabel"}: a quality check is
    randomly requested for a certain percentage of operations, which can
    be specified in the `Every #% of Transfers`{.interpreted-text
    role="guilabel"} field that appears below.
-   `Periodically`{.interpreted-text role="guilabel"}: a quality check
    is requested once every set period of time, which is specified by
    entering a numerical value in the field below, and choosing either
    `Days`{.interpreted-text role="guilabel"}, `Weeks`{.interpreted-text
    role="guilabel"}, or `Months`{.interpreted-text role="guilabel"} as
    the desired time interval.

In the `Type`{.interpreted-text role="guilabel"} field, specify the type
of quality check that should be performed. The method for processing
quality checks created by the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} depends
upon the type of quality check selected:

-   `Instructions`{.interpreted-text role="guilabel"} checks provide
    specific instructions for how to complete the quality check.
-   `Take a Picture`{.interpreted-text role="guilabel"} checks require a
    picture of the product be uploaded for later review by the assigned
    quality team.
-   `Register Production`{.interpreted-text role="guilabel"} checks
    prompt manufacturing employees to confirm the quantity of the
    product that was produced during the manufacturing operation.
-   `Pass - Fail`{.interpreted-text role="guilabel"} checks specify a
    criterion that products must meet for the check to pass.
-   `Measure`{.interpreted-text role="guilabel"} checks prompt employees
    to record a measurement of the product that must be within a
    tolerance of a norm value for the check to pass.
-   `Worksheet`{.interpreted-text role="guilabel"} checks provide an
    interactive worksheet that must be filled out by the employee
    processing the check.

::: {.important}
::: {.title}
Important
:::

An *Instructions* check is the same as a step on a work order for an MO.

When a step is added to a work order, Odoo stores it in the Quality app
as a `QCP (Quality Control Point)`{.interpreted-text role="abbr"}. It is
possible to manually create a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} with the
*Instructions* check type, and even assign it to an operation other than
manufacturing, like receipts.

However, when creating a control point specifically for quality control
purposes, using a different check type is probably more effective.
:::

In the `Team`{.interpreted-text role="guilabel"} field, specify the
quality team that is responsible for managing the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, and the
quality checks it creates. If a specific quality team member is
responsible for the `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, select them in the `Responsible`{.interpreted-text
role="guilabel"} field.

The `Step Document`{.interpreted-text role="guilabel"} field has two
options that specify the location of an instructional document detailing
how to complete the quality checks created by the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}.

Select `Specific Page of Operation Worksheet`{.interpreted-text
role="guilabel"} if the document is included with the instructional
worksheet for the work order, then enter the page number in the
`Worksheet
Page`{.interpreted-text role="guilabel"} field that appears below.

Select `Custom`{.interpreted-text role="guilabel"} if the document
should be included in the `Instructions`{.interpreted-text
role="guilabel"} tab at the bottom of the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}.

In the `Instructions`{.interpreted-text role="guilabel"} tab at the
bottom of the form, enter instructions for how to complete the quality
checks created by the `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}.

If the `Custom`{.interpreted-text role="guilabel"} option was selected
in the `Step Document`{.interpreted-text role="guilabel"} field above, a
document can be attached in this tab. To do so, either select the
`Upload your file`{.interpreted-text role="guilabel"} button to open the
device\'s file manager, and then select a file, or add a link to a
Google Slides document in the `Google Slide Link`{.interpreted-text
role="guilabel"} field.

In the `Message If Failure`{.interpreted-text role="guilabel"} tab,
include instructions for what to do if the quality check fails. For
example, instruct the employee processing the quality check to create a
`quality
alert <quality_alerts>`{.interpreted-text role="doc"}.

The `Notes`{.interpreted-text role="guilabel"} tab is used to provide
additional information about the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, like the
reason it was created. The information entered in this tab is **not**
shown to employees processing the quality checks created by the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}.

{.align-center}
