# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_management/quality_alerts.md

Quality alerts
==============

In the Odoo *Quality* app, *quality alerts* are used to notify quality
teams of product defects or other issues. Quality alerts can be created
from a manufacturing or inventory order, from a work order in the *Shop
Floor* module, or directly within the *Quality* app.

Create quality alerts
---------------------

There are multiple ways to create a new quality alert:

-   **From the Quality app itself**, by to
    `Quality -->  Quality Control --> Quality
    Alerts`{.interpreted-text role="menuselection"}, and then click
    `New`{.interpreted-text role="guilabel"} to open a quality alert
    form.

-   Navigate to
    `Manufacturing --> Operations --> Manufacturing Orders`{.interpreted-text
    role="menuselection"}, and then select an . Click the
    `Quality Alert`{.interpreted-text role="guilabel"} button at the top
    of the to open a quality alert form in a new page.

    ::: {.important}
    ::: {.title}
    Important
    :::

    This method can only be used if a quality check has been requested
    for the . The `Quality Alert`{.interpreted-text role="guilabel"}
    button will not appear otherwise.
    :::

-   Open the `Inventory`{.interpreted-text role="menuselection"} app,
    click the `# To Process`{.interpreted-text role="guilabel"} button
    on an inventory order type card (Receipts, Delivery Orders, etc.),
    and then select an order. Click the
    `Quality Alert`{.interpreted-text role="guilabel"} button at the top
    of the order to open a quality alert form in a new page.

    ::: {.important}
    ::: {.title}
    Important
    :::

    This method can only be used if a quality check has been requested
    for the inventory order. The `Quality Alert`{.interpreted-text
    role="guilabel"} button will not appear otherwise. If the button
    does not appear, a quality alert can also be created by clicking the
    `⚙️ (gear)`{.interpreted-text role="guilabel"} icon at the top of
    the page and selecting the `Quality Alert`{.interpreted-text
    role="guilabel"} option from the resulting menu.
    :::

-   Open the `Shop Floor`{.interpreted-text role="menuselection"}
    module, and then select a work center from the navigation bar at the
    top of the page. Then, click the
    `⋮ (three vertical dots)`{.interpreted-text role="guilabel"} button
    at the bottom-right of a work order card to open the
    `What do you want to do?`{.interpreted-text role="guilabel"} menu.
    Select the `Create a Quality Alert`{.interpreted-text
    role="guilabel"} option from this menu to open a quality alert in a
    pop-up window.

::: {.note}
::: {.title}
Note
:::

Depending on how a new quality alert form is opened, certain fields on
the form may already be filled in. For example, if a quality alert is
created from a work order card in the *Shop Floor* module, the
`Product`{.interpreted-text role="guilabel"} and
`Work Center`{.interpreted-text role="guilabel"} are pre-filled.
:::

### Quality alerts form

After opening a new quality alert form, begin by giving it a short
`Title`{.interpreted-text role="guilabel"} that summarizes the issue
with the product.

Then, if the quality alert is referencing:

-   **A specific product or product variant**, select it from the
    `Product`{.interpreted-text role="guilabel"} or
    `Product Variant`{.interpreted-text role="guilabel"} drop-down
    menus.
-   **A specific work center**, select it from the
    `Work Center`{.interpreted-text role="guilabel"} drop-down menu.
-   **A specific picking order**, select it from the
    `Picking`{.interpreted-text role="guilabel"} drop-down menu.

Next in the `Team`{.interpreted-text role="guilabel"} field, select the
quality team that is responsible for managing the quality alert. If a
specific employee should be responsible for the quality alert, select
them from the `Responsible`{.interpreted-text role="guilabel"} drop-down
menu.

In the `Tags`{.interpreted-text role="guilabel"} field, select any tags
relevant to the quality alert from the drop-down menu.

Use the `Root Cause`{.interpreted-text role="guilabel"} field to select
the cause of the quality issue, if known.

Lastly, choose a `Priority`{.interpreted-text role="guilabel"} level by
selecting a `⭐ (star)`{.interpreted-text role="guilabel"} number between
one and three. Quality alerts with higher priorities appear at the top
of the `Quality Alerts`{.interpreted-text role="guilabel"} Kanban board
in the *Quality* app.

At the bottom of the quality alert form are four tabs which aid in
adding supplemental information or actions to be taken for the quality
alert. They can be filled out as follows:

-   In the `Description`{.interpreted-text role="guilabel"} tab, enter a
    description of the quality issue.
-   Use the `Corrective Actions`{.interpreted-text role="guilabel"} tab
    to detail the steps that should be taken to fix the issue.
-   Use the `Preventive Actions`{.interpreted-text role="guilabel"} tab
    to detail what should be done to prevent the issue from occurring in
    the future.
-   In the `Miscellaneous`{.interpreted-text role="guilabel"} tab,
    select the `Vendor`{.interpreted-text role="guilabel"} of the
    product. If using an Odoo database which manages multiple companies,
    select the relevant company in the `Company`{.interpreted-text
    role="guilabel"} field. Finally, specify when the alert was assigned
    to a quality team in the `Date Assigned`{.interpreted-text
    role="guilabel"} field.

{.align-center}

Manage quality alerts
---------------------

To view all existing quality alerts, navigate to
`Quality --> Quality Control -->
Quality Alerts`{.interpreted-text role="menuselection"}. By default,
alerts are displayed in a Kanban board view, which organizes them into
different stages based on where they are in the review process.

To move an alert to a different stage, simply drag and drop it on the
desired stage. Alternatively, select a quality alert to open it, and
then click the desired stage above the top-right corner of the quality
alert form.

To create a new alert within a specific stage, click the
`+ (plus)`{.interpreted-text role="guilabel"} button to the right of the
stage name. In the new alert card that appears below the stage title,
enter the `Title`{.interpreted-text role="guilabel"} of the alert, and
then click `Add`{.interpreted-text role="guilabel"}. To configure the
rest of the alert, select the alert card to open its form.

{.align-center}
