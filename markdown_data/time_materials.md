Invoicing based on time and materials
=====================================

Invoicing based on time and/or materials is typically used when
accurately estimating the size of a project isn\'t possible, or when the
requirements of a project may change.

This is different from a fixed-price contract, when a customer agrees to
pay a specified total for the fulfillment of the contract\-\--no matter
what needs to be paid to the employees, sub-contractors, vendors,
suppliers, and so on.

The Odoo *Sales* app can invoice for time and various other expenses
(e.g. transport, lodging), as well as purchases needed to fulfill an
order.

App and settings configuration
------------------------------

First, in order to accurately keep track of the progress of a project,
the Odoo *Project* and *Accounting* apps **must** be installed.

To install the *Project* app, navigate to
`Odoo main dashboard --> Apps`{.interpreted-text role="menuselection"}.
Then, on the `Apps`{.interpreted-text role="guilabel"} page, locate the
`Project`{.interpreted-text role="guilabel"} app block, and click
`Activate`{.interpreted-text role="guilabel"}. The page automatically
refreshes and returns to the main Odoo dashboard, where the *Project*
app is now available to access.

Repeat the same process to install the *Accounting* application.

After installation, click the `Accounting`{.interpreted-text
role="guilabel"} app icon from the main Odoo dashboard, and navigate to
`Configuration --> Settings`{.interpreted-text role="menuselection"}. On
the `Settings`{.interpreted-text role="guilabel"} page, scroll down to
the `Analytics`{.interpreted-text role="guilabel"} section, and ensure
the box next to `Analytic
Accounting`{.interpreted-text role="guilabel"} is checked.

{.align-center}

Then, click `Save`{.interpreted-text role="guilabel"} to save all
changes.

Then, navigate to
`Odoo main dashboard --> Project app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. On the
`Settings`{.interpreted-text role="guilabel"} page, in the
`Time Management`{.interpreted-text role="guilabel"} section, ensure the
box beside the `Timesheets`{.interpreted-text role="guilabel"} feature
is checked.

Then, click `Save`{.interpreted-text role="guilabel"} to save all
changes.

{.align-center}

Service product configuration {#sales/invoicing/configured-service-product}
-----------------------------

With the *Timesheets* feature activated in the *Project* app, it is now
possible to invoice for time spent on a project, but **only** when the
following product configurations have been made.

::: {.important}
::: {.title}
Important
:::

Invoicing for time spent on a project is **only** possible with products
that have *Service* set as the *Product Type* on their product form.
:::

To configure a service product, first navigate to
`Sales app --> Products -->
Products`{.interpreted-text role="menuselection"}. On the
`Products`{.interpreted-text role="guilabel"} page, select the desired
service product to be configured, or click `New`{.interpreted-text
role="guilabel"} to create a new product.

From the product form, in the `General Information`{.interpreted-text
role="guilabel"} tab, set the `Product Type`{.interpreted-text
role="guilabel"} to `Service`{.interpreted-text role="guilabel"}. Then,
open the drop-down menu in the `Invoicing Policy`{.interpreted-text
role="guilabel"} field, and select
`Based on Timesheets`{.interpreted-text role="guilabel"}.

Next, from the `Create on Order`{.interpreted-text role="guilabel"}
drop-down menu, select `Project \& Task`{.interpreted-text
role="guilabel"}. That setting indicates that, when a sales order is
created with this specific service product, a new project and task is
created in the *Project* app.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The option `Task`{.interpreted-text role="guilabel"} can be chosen
instead from the `Create on Order`{.interpreted-text role="guilabel"}
drop-down menu. If `Task`{.interpreted-text role="guilabel"} is chosen,
select an existing project that the task will appear in from
`Project`{.interpreted-text role="guilabel"} field, which only appears
if `Task`{.interpreted-text role="guilabel"} is chosen in the
`Create on Order`{.interpreted-text role="guilabel"} field.
:::

Add time spent to sales order
-----------------------------

After properly configuring a service product with the correct *Invoicing
Policy* and *Create on Order* options, it is possible to add time spent
to a sales order.

To see that in action, navigate to `Sales app --> New`{.interpreted-text
role="menuselection"} to open a blank quotation form. Then, proceed to
add a `Customer`{.interpreted-text role="guilabel"}, and in the
`Order Lines`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select the
properly `configured service product
<sales/invoicing/configured-service-product>`{.interpreted-text
role="ref"} from the drop-down menu.

Next, click `Confirm`{.interpreted-text role="guilabel"} to confirm the
order.

After confirming the sales order, two smart buttons appear at the top of
the order form: `Projects`{.interpreted-text role="guilabel"} and
`Tasks`{.interpreted-text role="guilabel"}.

{.align-center}

If the `Projects`{.interpreted-text role="guilabel"} smart button is
clicked, it reveals the specific project related to this sales order. If
the `Tasks`{.interpreted-text role="guilabel"} smart button is clicked,
it reveals the specific project task related to this sales order. Both
are also accessible in the *Project* app.

In order to add time spent on a sales order, click the
`Tasks`{.interpreted-text role="guilabel"} smart button.

On the task form, select the `Timesheets`{.interpreted-text
role="guilabel"} tab. From the `Timesheets`{.interpreted-text
role="guilabel"} tab, employees can be assigned to work on the project,
and the time they spend working on the task can be added by the
employees or by the person who created the sales order.

To add an employee, and the time spent working on the task, click
`Add a line`{.interpreted-text role="guilabel"} in the
`Timesheets`{.interpreted-text role="guilabel"} tab. Then, select the
appropriate `Date`{.interpreted-text role="guilabel"} and
`Employee`{.interpreted-text role="guilabel"}. There is also the option
to add a brief description of the work done during this time in the
`Description`{.interpreted-text role="guilabel"} column, but it\'s not
required.

Lastly, enter the amount of time worked on the task in the
`Hours Spent`{.interpreted-text role="guilabel"} column, and click away
to complete that line in the `Timesheets`{.interpreted-text
role="guilabel"} tab.

::: {.note}
::: {.title}
Note
:::

The time entered in the `Hours Spent`{.interpreted-text role="guilabel"}
column is immediately reflected in the
`Allocated Time`{.interpreted-text role="guilabel"} field (located near
the top of the task form) as a percentage, which reflects how much of
the total allocated work hours have been done so far.

That same information is found as numerical hours in the
`Hours Spent`{.interpreted-text role="guilabel"} and
`Remaining Hours`{.interpreted-text role="guilabel"} fields, located at
the bottom of the `Timesheets`{.interpreted-text role="guilabel"} tab.

{.align-center}
:::

Repeat this process for however many employees and hours have been
worked on the project.

Invoice time spent
------------------

Once all the necessary employees and time spent have been added to the
project task, return to the sales order to invoice the customer for
those hours. To do that, either click the `Sales
Order`{.interpreted-text role="guilabel"} smart button at the top of the
task form, or return to the sales order via the breadcrumb links,
located in the upper-left of the screen.

Back on the sales order form, the time that was added to the task is
reflected in the `Order Lines`{.interpreted-text role="guilabel"} tab
(in the `Delivered`{.interpreted-text role="guilabel"} column) and in
the new `Recorded
Hours`{.interpreted-text role="guilabel"} smart button at the top of the
sales order.

To invoice the customer for time spent on the project, click
`Create Invoice`{.interpreted-text role="guilabel"}, and select
`Regular invoice`{.interpreted-text role="guilabel"} from the
`Create invoices`{.interpreted-text role="guilabel"} pop-up window.
Then, click `Create Draft Invoice`{.interpreted-text role="guilabel"}.

Doing so reveals a `Customer Invoice Draft`{.interpreted-text
role="guilabel"}, clearly showing all the work that\'s been done in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

Pay attention to the `Analytic Distribution`{.interpreted-text
role="guilabel"} column in the `Customer
Invoice`{.interpreted-text role="guilabel"}, as that information is
necessary to ensure other time/material invoicing tasks are completed
properly and accurately.

{.align-center}
:::

Click `Confirm`{.interpreted-text role="guilabel"} to confirm the
invoice and continue with the invoicing process.

::: {.seealso}
`invoicing_policy`{.interpreted-text role="doc"}
:::

Expenses configuration
----------------------

In order to track and invoice expenses related to a sales order, the
Odoo *Expenses* app **must** be installed.

To install the *Expenses* app, navigate to
`Odoo main dashboard --> Apps`{.interpreted-text role="menuselection"}.
Then, on the `Apps`{.interpreted-text role="guilabel"} page, locate the
`Expenses`{.interpreted-text role="guilabel"} app block, and click
`Activate`{.interpreted-text role="guilabel"}.

The page automatically refreshes and returns to the main Odoo dashboard,
where the `Expenses`{.interpreted-text role="guilabel"} app is now
available to access.

Add expenses to sales order {#sales/invoicing/add-expenses-sales-order}
---------------------------

To add an expense to a sales order, first navigate to the
`Expenses`{.interpreted-text role="menuselection"} app. Then, from the
main *Expenses* dashboard, click `New`{.interpreted-text
role="guilabel"}, which reveals a blank expense form.

On the expense form, add a `Description`{.interpreted-text
role="guilabel"} of the expense (e.g. [Hotel Stay]{.title-ref}, [Plane
Ticket]{.title-ref}). Next, in the `Category`{.interpreted-text
role="guilabel"} field, select the appropriate option from the drop-down
menu (e.g. `Meals`{.interpreted-text role="guilabel"},
`Miles`{.interpreted-text role="guilabel"},
`Travel \& Accommodation`{.interpreted-text role="guilabel"}).

::: {.note}
::: {.title}
Note
:::

Expense categories can be added and modified by navigating to
`Expenses app -->
Configuration --> Expense Categories`{.interpreted-text
role="menuselection"}.
:::

Then, enter the total amount of the expense in the
`Total`{.interpreted-text role="guilabel"} field, as well as any
`Included Taxes`{.interpreted-text role="guilabel"} that may apply.
Next, ensure that the correct `Employee`{.interpreted-text
role="guilabel"} is selected, and designate who paid for the expense in
the `Paid By`{.interpreted-text role="guilabel"} field: the
`Employee (to reimburse)`{.interpreted-text role="guilabel"} or the
`Company`{.interpreted-text role="guilabel"}.

Next, in the `Customer to Reinvoice`{.interpreted-text role="guilabel"}
field, select the appropriate sales order from the drop-down menu. Then,
select that same sales order information from the `Analytic
Distribution`{.interpreted-text role="guilabel"} field, as well.

::: {.note}
::: {.title}
Note
:::

The `Analytic Distribution`{.interpreted-text role="guilabel"} field
will **only** have the corresponding sales order as an option if the
sales order contains a service product that is billed based on
*Timesheets*, *Milestones*, or *Delivered Quantities*.
:::

{.align-center}

If there are any receipts that should be uploaded and attached to the
expense, click the `Attach Receipt`{.interpreted-text role="guilabel"}
button, and upload the necessary documents to the expense. This is
**not** required, but it may affect whether or not an expense is
approved.

When all the information has been entered, click
`Create Report`{.interpreted-text role="guilabel"} to create an expense
report detailing all the expense information that was just entered.

{.align-center}

Then, there\'s the option to `Submit to Manager`{.interpreted-text
role="guilabel"} for approval. Once approved, the
`Report in Next Payslip`{.interpreted-text role="guilabel"} appears.

To showcase a complete flow in this example, select
`Submit to Manager`{.interpreted-text role="guilabel"}. Then, the
manager would click `Approve`{.interpreted-text role="guilabel"} to
approve this expense, and click `Post Journal Entries`{.interpreted-text
role="guilabel"} to post this expense to the accounting journal.

Invoice expenses
----------------

To invoice a customer for an `expense on a sales order
<sales/invoicing/add-expenses-sales-order>`{.interpreted-text
role="ref"}, navigate to the related sales order, either from the
`Sales`{.interpreted-text role="menuselection"} app or from the expense
report in the `Expenses`{.interpreted-text role="menuselection"} app.
From the expense report, click the `Sales Orders`{.interpreted-text
role="guilabel"} smart button at the top of the page.

If the expense report was linked to the sales order, the
newly-configured expense now has its own line in the
`Order Lines`{.interpreted-text role="guilabel"} tab, and can be
invoiced to the customer.

{.align-center}

To invoice the customer for the expense on the sales order, click
`Create Invoice`{.interpreted-text role="guilabel"}, select
`Regular Invoice`{.interpreted-text role="guilabel"} from the
`Create invoices`{.interpreted-text role="guilabel"} pop-up window, then
click `Create Draft Invoice`{.interpreted-text role="guilabel"}.

Doing so reveals a `Customer Invoice Draft`{.interpreted-text
role="guilabel"} for the expense. Then, the invoicing process can be
completed as usual.

{.align-center}

Purchase configuration
----------------------

In order to invoice a customer for purchases made on a sales order, the
*Purchase* application **must** be installed.

To install the *Purchase* application, navigate to
`Odoo main dashboard --> Apps`{.interpreted-text role="menuselection"}.
Then, on the `Apps`{.interpreted-text role="guilabel"} page, locate the
`Purchase`{.interpreted-text role="guilabel"} app block, and click
`Activate`{.interpreted-text role="guilabel"}. The page automatically
refreshes and returns to the main Odoo dashboard, where the
`Purchase`{.interpreted-text role="guilabel"} app is now available to
access.

Add purchase to sales order {#sales/invoicing/add-purchase-to-sales-order}
---------------------------

To add a purchase to a sales order, a purchase order must first be
created. To create a purchase order, navigate to
`Purchase app --> New`{.interpreted-text role="menuselection"} to reveal
a blank purchase order form.

First, add a `Vendor`{.interpreted-text role="guilabel"} to the purchase
order. Then, under the `Products`{.interpreted-text role="guilabel"}
tab, click the `extra column options`{.interpreted-text role="guilabel"}
drop-down menu, represented by two horizontal lines with dots on them,
located to the far-right of the column headers. From that drop-down
menu, select `Analytic Distribution`{.interpreted-text role="guilabel"}.

{.align-center}

After adding the `Analytic Distribution`{.interpreted-text
role="guilabel"} column to the headers on the
`Products`{.interpreted-text role="guilabel"} tab of the purchase order
form, proceed to add the product(s) to the purchase order. To do that,
click `Add a product`{.interpreted-text role="guilabel"}, and select the
desired product from the drop-down menu. Repeat for all the products to
add.

::: {.important}
::: {.title}
Important
:::

In order for a purchase to be properly invoiced on a sales order, the
product on the purchase order **must** be marked as
`Can be Expensed`{.interpreted-text role="guilabel"}, have an
`Invoicing Policy`{.interpreted-text role="guilabel"} set to
`Delivered quantities`{.interpreted-text role="guilabel"}, and have the
`At cost`{.interpreted-text role="guilabel"} option selected in the
`Re-Invoice Expenses`{.interpreted-text role="guilabel"} field on its
product form.

{.align-center}
:::

Then, select the appropriate `Analytic Distribution`{.interpreted-text
role="guilabel"} associated with the sales order to which this purchase
order is related. To do that, click the empty
`Analytic Distribution`{.interpreted-text role="guilabel"} field to
reveal an `Analytic`{.interpreted-text role="guilabel"} pop-up window.

Then, from the `Departments`{.interpreted-text role="guilabel"}
drop-down menu, select the analytic distribution associated with the
desired sales order to be invoiced for the purchase.

{.align-center}

Once all the information is entered in the `Products`{.interpreted-text
role="guilabel"} tab of the purchase order, confirm the order by
clicking `Confirm Order`{.interpreted-text role="guilabel"}. Then, click
`Receive Products`{.interpreted-text role="guilabel"} when the products
have been received. This creates a receipt form.

::: {.note}
::: {.title}
Note
:::

If any serial/lot numbers must be entered before validating the receipt
of products, then on the receipt form, click the
`details`{.interpreted-text role="guilabel"} icon represented by four
horizontal lines located to the far-right of the product line.

This reveals a `Detailed Operations`{.interpreted-text role="guilabel"}
tab, in which the necessary `Lot/Serial
Number(s)`{.interpreted-text role="guilabel"} and
`Done`{.interpreted-text role="guilabel"} quantity can be added. When
ready, click `Confirm`{.interpreted-text role="guilabel"} to confirm the
data.
:::

Then, click `Validate`{.interpreted-text role="guilabel"} to validate
the purchase order.

Next, return to the purchase order, via the breadcrumb links at the top
of the page, and click `Create Bill`{.interpreted-text role="guilabel"}
to create a vendor bill that can be invoiced to the customer on the
attached sales order.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Make sure to enter a `Bill Date`{.interpreted-text role="guilabel"} on
the `Vendor Bill Draft`{.interpreted-text role="guilabel"} before
confirming. If a `Bill Date`{.interpreted-text role="guilabel"} is *not*
entered, an error window appears, requesting that information to be
entered before confirmation can occur.
:::

Then, click `Confirm`{.interpreted-text role="guilabel"} to confirm the
vendor bill, which is then automatically added to the sales order, where
it can be invoiced directly to the customer attached to it.

Invoice purchase
----------------

To invoice a customer for a purchase on a sales order, first
`add the purchase to the sales
order <sales/invoicing/add-purchase-to-sales-order>`{.interpreted-text
role="ref"}, then navigate to the desired sales order in the
`Sales`{.interpreted-text role="menuselection"} app.

On the sales order that was attached to the purchase order, the
purchased product now has its own product line under the
`Order Lines`{.interpreted-text role="guilabel"} tab, and it is ready to
be invoiced.

{.align-center}

To invoice the customer for the purchase, simply click
`Create Invoice`{.interpreted-text role="guilabel"}, select
`Regular Invoice`{.interpreted-text role="guilabel"} from the
`Create invoices`{.interpreted-text role="guilabel"} pop-up window, then
click `Create Draft Invoice`{.interpreted-text role="guilabel"}.

Doing so reveals a `Customer Invoice Draft`{.interpreted-text
role="guilabel"} with the newly-added purchase order product in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

{.align-center}

To complete the invoicing process, click `Confirm`{.interpreted-text
role="guilabel"} to confirm the invoice, and then click
`Register Payment`{.interpreted-text role="guilabel"} in the
`Register Payment`{.interpreted-text role="guilabel"} pop-up form.
