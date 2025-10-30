# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/advanced/track_and_bill.md

Track and bill time
===================

Odoo *Helpdesk* provides teams with the ability to track the amount of
hours spent working on a ticket, and to bill a customer for that time.
Through integrations with the *Sales*, *Timesheets*, *Project* and
*Accounting* applications, customers can be charged once the work is
completed, or before it has even begun.

::: {.warning}
::: {.title}
Warning
:::

Since the *Track & Bill Time* features require integration with other
applications, enabling them may result in the installation of additional
modules or applications.

Installing a new application on a *One-App-Free* database triggers a
15-day trial. At the end of the trial, if a paid subscription has not
been added to the database, it will no longer be active or accessible.
:::

Configure track and bill time features
--------------------------------------

Before a customer can be invoiced for support services, the *Track &
Bill Time* features **must** be enabled on each *Helpdesk* team
individually.

### Enable track and bill time on a helpdesk team

To view and enable the *Track & Bill Time* features on a *Helpdesk*
team, first navigate to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}. Then, select a team from the list, or create a
`new one <../../helpdesk>`{.interpreted-text role="doc"}. This reveals a
team\'s settings page.

On the team\'s settings page, scroll to the
`Track & Bill Time`{.interpreted-text role="guilabel"} section. Check
the boxes labeled `Timesheets`{.interpreted-text role="guilabel"} and
`Time Billing`{.interpreted-text role="guilabel"}.

Once the `Timesheets`{.interpreted-text role="guilabel"} box is checked,
a new field appears, labeled `Project`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If this is the first time this feature has been enabled on this
database, the page may need to be manually saved and refreshed before
the `Project`{.interpreted-text role="guilabel"} field appears.
:::

The project selected in this field represents where all the timesheets
for this team\'s tickets are recorded. Click into the
`Project`{.interpreted-text role="guilabel"} drop-down menu to select a
project.

To create a new project where the timesheets are recorded, click into
the `Project`{.interpreted-text role="guilabel"} drop-down menu, type a
name for the project, and then click `Create`{.interpreted-text
role="guilabel"} from the drop-down menu beneath.

{.align-center}

#### Configure service products {#helpdesk/configure-service-products}

When the `Time Billing`{.interpreted-text role="guilabel"} feature is
enabled, a new product is created in the *Sales* app called *Service on
Timesheets*. This product can be found under `Sales app-->
Products --> Products`{.interpreted-text role="menuselection"}. Then,
search for [Service on Timesheets]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar. This is the product
that is used when invoicing for *post-paid support services* **after**
they have been completed.

Select `Service on Timesheets`{.interpreted-text role="guilabel"} from
the product page. This reveals the product detail form. The product is
configured with the `Product Type`{.interpreted-text role="guilabel"}
set to `Service`{.interpreted-text role="guilabel"} and the
`Invoicing Policy`{.interpreted-text role="guilabel"} set to
`Based on Timesheets`{.interpreted-text role="guilabel"}. Make any
necessary changes to the product record, such as the
`Cost`{.interpreted-text role="guilabel"} or
`Sales Price`{.interpreted-text role="guilabel"}.

{.align-center}

In order to invoice for support services **before** the work has been
completed (also known as *prepaid support services*), a separate product
with a different invoicing policy must be created.

To create a new service product, go to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}. This reveals a blank product detail form.

On the new product form, add a `Product Name`{.interpreted-text
role="guilabel"}, and set the `Product Type`{.interpreted-text
role="guilabel"} to `Service`{.interpreted-text role="guilabel"}. Then,
set the `Invoicing Policy`{.interpreted-text role="guilabel"} to
`Prepaid/Fixed Price`{.interpreted-text role="guilabel"}. This means an
invoice can be generated and payment can be received for this product
before any timesheets entries have been recorded for these services.

{.align-center}

Finally, set the `Sales Price`{.interpreted-text role="guilabel"}, and
confirm that the `Unit of Measure`{.interpreted-text role="guilabel"} is
set to `Hours`{.interpreted-text role="guilabel"}.

Invoice prepaid support services
--------------------------------

When support services are billed on a fixed price, an invoice can be
created before any work is completed on the issue. In this case, a
service product with the *Invoicing Policy* set to *Prepaid/Fixed Price*
would be used, just like `the section above
<helpdesk/configure-service-products>`{.interpreted-text role="ref"}.

### Create a sales order with prepaid product

To invoice a customer for prepaid support services, first create a sales
order (SO) with the support services product. To do this, go to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}. Then, click `New`{.interpreted-text
role="guilabel"} to reveal a blank quotation form.

Then, fill out the quotation form with the customer information.

Go to the `Order Lines`{.interpreted-text role="guilabel"} tab of the
quotation and click `Add a Product`{.interpreted-text role="guilabel"}.
Then, select the *prepaid services product* configured in the steps
above. Update the `Quantity`{.interpreted-text role="guilabel"} field
with the number of hours.

After updating any other necessary information,
`Confirm`{.interpreted-text role="guilabel"} the quotation. This
converts the quotation into an `SO (sales order)`{.interpreted-text
role="abbr"}.

### Create and send an invoice for prepaid services

Once the `SO (sales order)`{.interpreted-text role="abbr"} has been
confirmed, click the `Create Invoice`{.interpreted-text role="guilabel"}
button. This opens a `Create invoices`{.interpreted-text
role="guilabel"} pop-up window.

If no down payment is collected, the `Create Invoice`{.interpreted-text
role="guilabel"} type can remain as `Regular Invoice`{.interpreted-text
role="guilabel"}. If a
`down payment <../../../sales/sales/invoicing/down_payment>`{.interpreted-text
role="doc"} is collected, choose between either
`Down payment (percentage)`{.interpreted-text role="guilabel"} or
`Down payment
(fixed amount)`{.interpreted-text role="guilabel"}.

When the necessary information has been entered, click
`Create Draft Invoice`{.interpreted-text role="guilabel"}.

The invoice can then be sent to the customer for payment.

### Create helpdesk ticket for prepaid services

To create a *Helpdesk* ticket for prepaid services, navigate to
`Helpdesk`{.interpreted-text role="menuselection"} and click the
`Tickets`{.interpreted-text role="guilabel"} button to reveal a specific
team\'s pipeline. Click `New`{.interpreted-text role="guilabel"} to
create a new ticket.

On the blank ticket form, create a ticket `Title`{.interpreted-text
role="guilabel"}, and enter the `Customer`{.interpreted-text
role="guilabel"} information.

When the customer name is added, the
`Sales Order Item`{.interpreted-text role="guilabel"} field
automatically populates with the most recent prepaid sales order item
that has time remaining.

### Track hours on helpdesk ticket

Time spent working on a *Helpdesk* ticket is tracked on the *Timesheets*
tab on the specific ticket.

On the ticket detail form, click on the `Timesheets`{.interpreted-text
role="guilabel"} tab and click `Add a line`{.interpreted-text
role="guilabel"}. Choose an `Employee`{.interpreted-text
role="guilabel"}, add a `Description`{.interpreted-text role="guilabel"}
of the task, and enter the number of `Hours Spent`{.interpreted-text
role="guilabel"}.

As new lines are added to `Timesheets`{.interpreted-text
role="guilabel"} tab, the `Remaining Hours on SO`{.interpreted-text
role="guilabel"} field, at the bottom-right of the tab, is automatically
updated.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the number of hours on the `Timesheets`{.interpreted-text
role="guilabel"} tab exceeds the number of hours sold, the
`Remaining Hours of SO`{.interpreted-text role="guilabel"} turns red.
:::

As hours are added to the `Timesheets`{.interpreted-text
role="guilabel"} tab, they are automatically updated in the
`Delivered`{.interpreted-text role="guilabel"} field on the
`SO (sales order)`{.interpreted-text role="abbr"}, as well.

Invoice post-paid support services
----------------------------------

When support services are billed based on the amount of time spent on an
issue, an invoice cannot be created before the total number of hours
required to solve the problem have been entered on a timesheet. In this
case, a service product with the *Invoicing Policy* set to *Based on
Timesheets* would be used, like the one created in `the section above
<helpdesk/configure-service-products>`{.interpreted-text role="ref"}.

### Create a sales order with a time-tracked product

To invoice a customer for post-paid support services, first create a
sales order (SO) with the *support services product*. To do this, go to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}. Then, click `New`{.interpreted-text
role="guilabel"} to reveal a blank quotation form.

Fill out the quotation with the customer information.

On the `Order Lines`{.interpreted-text role="guilabel"} tab, click
`Add a Product`{.interpreted-text role="guilabel"}. Select the post-paid
services product configured in the steps above. After updating any other
necessary information, `Confirm`{.interpreted-text role="guilabel"} the
quotation.

::: {.important}
::: {.title}
Important
:::

Unlike with the prepaid services quotation, Odoo does **not** allow an
invoice to be created at this time. That is because no services have
been performed; in other words, nothing has been delivered, therefore,
there is nothing to invoice.
:::

### Create a helpdesk ticket for time-tracked services

To record a *Timesheet* entry for time-tracker services, go to the
`Helpdesk`{.interpreted-text role="menuselection"} app, and select the
appropriate team for which these services apply.

If there is already an existing ticket for this issue, select it from
the Kanban view. This opens the ticket details form. If there is no
existing ticket for this customer issue, click `New`{.interpreted-text
role="guilabel"} to create a new ticket and enter the necessary customer
information on the blank ticket details form.

After selecting or creating a ticket, go to the
`Sales Order Item`{.interpreted-text role="guilabel"} drop-down menu.
Select the `SO (sales order)`{.interpreted-text role="abbr"} created in
the previous step.

### Track support hours on a ticket

In order to create an invoice for a product based on timesheets, hours
need to be tracked and recorded. At this point, the service is
considered *delivered*. To record hours for this support service, click
on the `Timesheets`{.interpreted-text role="guilabel"} tab of the
ticket.

Click `Add a Line`{.interpreted-text role="guilabel"} to record a new
entry. Select an `Employee`{.interpreted-text role="guilabel"} from the
drop-down menu, and record the time spent in the
`Hours Spent`{.interpreted-text role="guilabel"} column.

Repeat these steps as needed until all time spent on the issues has been
recorded.

{.align-center}

### Create an invoice for hours tracked on a ticket

After the customer\'s issue has been solved, and it is determined no new
timesheet entries need to be made, an invoice can be created, and the
customer can be billed.

To do this, return to the `SO (sales order)`{.interpreted-text
role="abbr"} by clicking on the `Sales Order`{.interpreted-text
role="guilabel"} smart button at the top of the ticket.

Before creating the invoice, confirm that the number in the
`Delivered`{.interpreted-text role="guilabel"} column matches the total
number of `Hours Spent`{.interpreted-text role="guilabel"} listed in the
`Timesheets`{.interpreted-text role="guilabel"} tab on the ticket.

{.align-center}

Then, click `Create Invoice`{.interpreted-text role="guilabel"}. This
opens a `Create invoice(s)`{.interpreted-text role="guilabel"} pop-up
window.

If no down payment is collected, the `Create Invoice`{.interpreted-text
role="guilabel"} type can remain as `Regular Invoice`{.interpreted-text
role="guilabel"}. If a down payment is collected, choose between either
`Down
payment (percentage)`{.interpreted-text role="guilabel"} or
`Down payment (fixed amount)`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Use the `Timesheets Period`{.interpreted-text role="guilabel"} field if
this invoice should **only** include timesheets from a certain time
period. If this field is left blank, **all** applicable timesheets that
have not yet been invoiced will be included.
:::

{.align-center}

When the necessary information has been entered, click
`Create Draft`{.interpreted-text role="guilabel"}. The invoice can then
be reviewed, edited, and sent to the customer for payment.

::: {.seealso}
\-
`../../../inventory_and_mrp/inventory/product_management/configure/uom`{.interpreted-text
role="doc"} -
`../../../sales/sales/invoicing/down_payment`{.interpreted-text
role="doc"}
:::
