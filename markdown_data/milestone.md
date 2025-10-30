Invoice project milestones
==========================

Invoicing based on project milestones can be used for expensive or
large-scale projects. The series of milestones in a project represent a
clear sequence of work that will inevitably result in the completion of
a project and/or contract.

This method of invoicing ensures the company gets a consistent flow of
money throughout the lifetime of the project. Customers can closely
monitor every phase of the project\'s development as it happens, in
addition to paying a large bill in several installments, instead of all
at once.

Create milestone products
-------------------------

In Odoo, each milestone of a project is considered as an individual
product.

To create and/or configure products to work like this, first navigate to
`Sales app
--> Products --> Products`{.interpreted-text role="menuselection"}.
Then, click on a product, or create a new one by clicking
`New`{.interpreted-text role="guilabel"}.

The option to invoice based on milestones is only available for certain
product types.

On the product form, under the `General Information`{.interpreted-text
role="guilabel"} tab, the `Product Type`{.interpreted-text
role="guilabel"} field *must* be set on any of the following options:
`Service`{.interpreted-text role="guilabel"},
`Event Ticket`{.interpreted-text role="guilabel"},
`Event Booth`{.interpreted-text role="guilabel"}, or
`Course`{.interpreted-text role="guilabel"}.

{.align-center}

With any of those `Product Type`{.interpreted-text role="guilabel"}
options selected, choose `Based on Milestones`{.interpreted-text
role="guilabel"} from the `Invoicing Policy`{.interpreted-text
role="guilabel"} drop-down menu.

{.align-center}

Beneath that is the `Create on Order`{.interpreted-text role="guilabel"}
field.

To ensure workflows are as seamless as possible, it is recommended that
an option in the `Create on Order`{.interpreted-text role="guilabel"}
field is selected.

::: {.note}
::: {.title}
Note
:::

Leaving it on the default `Nothing`{.interpreted-text role="guilabel"}
option won\'t negatively affect the desired workflow. However, a project
*must* then be created directly from a sales order form with that
specific product. Once a project is created *then* milestones and tasks
can be created and configured.
:::

When the `Create on Order`{.interpreted-text role="guilabel"} default
option of `Nothing`{.interpreted-text role="guilabel"} is clicked, a
drop-down menu is revealed with the following options:

-   `Task`{.interpreted-text role="guilabel"}: Odoo creates a task
    related to this milestone product in the *Projects* app when this
    specific product is ordered.
-   `Project \& Task`{.interpreted-text role="guilabel"}: Odoo creates a
    project and task related to this milestone product in the *Projects*
    app when this specific product is ordered.
-   `Project`{.interpreted-text role="guilabel"}: Odoo creates a project
    related to this milestone product in the *Projects* app when this
    specific product is ordered.

When `Task`{.interpreted-text role="guilabel"} is selected, a
`Project`{.interpreted-text role="guilabel"} field appears. In this
field, select to which existing project in the *Projects* app this
created task should be connected.

{.align-center}

When `Project \& Task`{.interpreted-text role="guilabel"} or
`Project`{.interpreted-text role="guilabel"} is selected, two new fields
appear: `Project Template`{.interpreted-text role="guilabel"} and
`Workspace Template`{.interpreted-text role="guilabel"}.

{.align-center}

The `Project Template`{.interpreted-text role="guilabel"} field provides
template options to use for the project that will be created when this
specific product is ordered.

The `Workspace Template`{.interpreted-text role="guilabel"} field
provides template options to use for the workspace (for the *Documents*
app, not the *Projects* app) that will be automatically generated for
the project when this specific product is ordered.

::: {.tip}
::: {.title}
Tip
:::

For organizational purposes, click the `Sales`{.interpreted-text
role="guilabel"} tab on the product form, and enter a custom
\'Milestone\' related descriptor in the
`Sales Description`{.interpreted-text role="guilabel"} field. This
information appears in the `Description`{.interpreted-text
role="guilabel"} column on the `Order Lines`{.interpreted-text
role="guilabel"} tab of the sales order.

Or, directly edit/modify the `Description`{.interpreted-text
role="guilabel"} field on the `Order Lines`{.interpreted-text
role="guilabel"} tab of the sales order.

This is *not* a requirement.
:::

Invoice milestones
------------------

::: {.note}
::: {.title}
Note
:::

The following flow features a trio of milestone products that have
`Service`{.interpreted-text role="guilabel"} set as their
`Product Type`{.interpreted-text role="guilabel"}, and
`Task`{.interpreted-text role="guilabel"} set on their
`Create on Order`{.interpreted-text role="guilabel"} field.

{.align-center}

Those tasks are then attached to a pre-existing
`Project`{.interpreted-text role="guilabel"}, which, in this case, is
titled, `Rebranding Projects`{.interpreted-text role="guilabel"}.
:::

To invoice milestones, create a sales order with the milestone
product(s). To do that, go to `Sales app --> New`{.interpreted-text
role="menuselection"}. Doing so reveals a blank quotation form.

From this quotation form, add a `Customer`{.interpreted-text
role="guilabel"}. Then, click `Add a product`{.interpreted-text
role="guilabel"} in the `Order Lines`{.interpreted-text role="guilabel"}
tab. Next, add the milestone product(s) to the
`Order Lines`{.interpreted-text role="guilabel"} tab.

Once the corresponding milestone product(s) have been added, click
`Confirm`{.interpreted-text role="guilabel"} to confirm the order, which
turns the quotation into a sales order.

When the order is confirmed, new smart buttons appear at the top of the
sales order based on what was selected in the
`Create on Order`{.interpreted-text role="guilabel"} field on the
product form.

From the sales order, click the `Milestones`{.interpreted-text
role="guilabel"} smart button. Doing so reveals a blank
`Milestones`{.interpreted-text role="guilabel"} page. Click
`New`{.interpreted-text role="guilabel"} to add milestones.

{.align-center}

Enter a `Name`{.interpreted-text role="guilabel"} for the milestone.
Next, apply it to the corresponding `Sales
Order Item`{.interpreted-text role="guilabel"}. Lastly, assign a
`Deadline`{.interpreted-text role="guilabel"} to the milestone, if
desired.

Repeat that process for all milestone sales order items.

Then, return to the sales order, via the breadcrumbs. From the sales
order, click the `Tasks`{.interpreted-text role="guilabel"} smart
button. Doing so reveals a `Tasks`{.interpreted-text role="guilabel"}
page with a task for each sales order item with that option designated
in the `Create on Order`{.interpreted-text role="guilabel"} field.

{.align-center}

To manually assign a configured milestone to a task, click the desired
task, which reveals the task form. On the task form, select the
appropriate milestone to which this task should be connected, in the
`Milestone`{.interpreted-text role="guilabel"} field.

{.align-center}

Repeat this process for all milestone tasks.

With those tasks properly configured, employees log in their progress as
they work on the task, in addition to adding any notes related to the
task.

Then, when that task is complete, that means that milestone has been
reached. At that point, it is time to invoice that milestone.

To invoice a milestone, first return to the sales order --- either via
the breadcrumb links, or by navigating to
`Sales app --> Orders --> Orders`{.interpreted-text
role="menuselection"} and picking the appropriate sales order.

Back on the sales order form, click the `Milestones`{.interpreted-text
role="guilabel"} smart button, and check the box in the
`Reached`{.interpreted-text role="guilabel"} column for that particular
task.

{.align-center}

Next, return to the sales order --- either by clicking
`View Sales Order`{.interpreted-text role="guilabel"} on the
`Milestones`{.interpreted-text role="guilabel"} page, or via the
breadcrumb links.

Back on the sales order, the line item for the milestone that\'s been
reached has its `Delivered`{.interpreted-text role="guilabel"} column
filled. That\'s because the milestone has been reached, and therefore
delivered.

{.align-center}

Click `Create Invoice`{.interpreted-text role="guilabel"} in the
upper-left corner. Doing so reveals a `Create
invoices`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

On the `Create invoices`{.interpreted-text role="guilabel"} pop-up
window, leave the `Create Invoice`{.interpreted-text role="guilabel"}
option on the default `Regular Invoice`{.interpreted-text
role="guilabel"} selection, and click the
`Create Draft Invoice`{.interpreted-text role="guilabel"} button.

Upon clicking `Create Draft Invoice`{.interpreted-text role="guilabel"},
Odoo reveals the `Customer Invoice Draft`{.interpreted-text
role="guilabel"}, *only* showing that reached milestone in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

{.align-center}

From this invoice page, click the `Confirm`{.interpreted-text
role="guilabel"} button to confirm the invoice. Then, when the customer
has paid for this milestone, click `Register Payment`{.interpreted-text
role="guilabel"}.

When `Register Payment`{.interpreted-text role="guilabel"} is clicked, a
`Register Payment`{.interpreted-text role="guilabel"} pop-up window
appears.

{.align-center}

On this pop-up window, confirm the accuracy of the auto-populated
fields, then click `Create Payment`{.interpreted-text role="guilabel"}.

When clicked, the pop-up window disappears, and Odoo returns to the
invoice for that milestone, which now has a green
`In Payment`{.interpreted-text role="guilabel"} banner in the
upper-right corner. This banner signifies the invoice has been paid.

{.align-center}

Then, return to the sales order, via the breadcrumb links. Back on the
sales order, in the `Order Lines`{.interpreted-text role="guilabel"}
tab, the reached milestone that\'s been invoiced and paid for, now has
its `Invoiced`{.interpreted-text role="guilabel"} column filled.

{.align-center}

There is also a new `Invoices`{.interpreted-text role="guilabel"} smart
button at the top of the sales order. Clicking that reveals all the
invoices that are connected to this sales order.

{.align-center}

Simply repeat the above process for each milestone as it is worked on,
and subsequently, completed.

Continue that process until the entire project has been completed, each
milestone has been invoiced, and the entire order has been paid for in
full.

::: {.seealso}
\- `time_materials`{.interpreted-text role="doc"} -
`proforma`{.interpreted-text role="doc"} -
`invoicing_policy`{.interpreted-text role="doc"}
:::
