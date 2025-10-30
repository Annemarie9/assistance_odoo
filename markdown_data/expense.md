Reinvoice expenses to customers
===============================

While working on a project for a client, employees often have to spend
their own money on various expenses related to the project.

For example, an employee may need to use their own money to pay for a
hotel, while they provide an on-site service for a client. As a company,
this expense should be reinvoiced to the customer. With Odoo, these
kinds of expenses can quickly be reinvoiced to the customer related to
the project.

Expenses application
--------------------

To be able to reinvoice a customer for an expense, the *Expenses*
application **must** be installed.

To install the *Expenses* application, navigate to
`main Odoo dashboard --> Apps`{.interpreted-text role="menuselection"},
and click `Install`{.interpreted-text role="guilabel"} on the *Expenses*
application block. When clicked, Odoo installs the application,
refreshes the page, and returns to the main Odoo dashboard.

Add expenses to sales orders
----------------------------

To begin, have a sales order confirmed in the *Sales* app to which a
reinvoiced expense can be added. Or, create a new sales order from
scratch. To do that, navigate to the `Sales
app --> New`{.interpreted-text role="menuselection"}. Doing so reveals a
blank quotation form.

Then, add a `Customer`{.interpreted-text role="guilabel"}, and add a
product to the `Order Lines`{.interpreted-text role="guilabel"} tab, by
clicking `Add a product`{.interpreted-text role="guilabel"}. Next,
select a product from the drop-down menu.

Lastly, click `Confirm`{.interpreted-text role="guilabel"} to confirm
the sales order.

{.align-center}

With the sales order confirmed, it\'s time to create an expense.

To do that, navigate to the *Expenses* application, by going to
`main Odoo dashboard
--> Expenses`{.interpreted-text role="menuselection"}.

Then, from the *Expenses* dashboard, click `New`{.interpreted-text
role="guilabel"} to reveal a blank expenses form.

{.align-center}

On the expenses form, add a `Description`{.interpreted-text
role="guilabel"} to easily reference the expense.

Then, in the `Category`{.interpreted-text role="guilabel"} field, select
one of the following options from the drop-down menu:

-   `Communication`{.interpreted-text role="guilabel"}: any form of
    communication related to a project/order.
-   `Others`{.interpreted-text role="guilabel"}: expense that doesn\'t
    fit into any other categories.
-   `Meals`{.interpreted-text role="guilabel"}: any form of meal costs
    related to a project/order.
-   `Gifts`{.interpreted-text role="guilabel"}: any form of gift costs
    related to a project/order.
-   `Mileage`{.interpreted-text role="guilabel"}: any form of mileage
    (gas) costs related to project/order.
-   `Travel \& Accommodation`{.interpreted-text role="guilabel"}: any
    travel or accommodation costs related to a project/order.

::: {.tip}
::: {.title}
Tip
:::

New expense categories can be created from an expense form, by clicking
the `Category`{.interpreted-text role="guilabel"} field drop-down menu,
selecting `View All`{.interpreted-text role="guilabel"}, and clicking
`New`{.interpreted-text role="guilabel"} from the
`Search:Category`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}
:::

For this sample workflow, which will reinvoice a customer for a brief
hotel stay, the `Category`{.interpreted-text role="guilabel"} for this
example is `[TRANS \& ACC] Travel \& Accommodation`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The following example requires the *Sales*, *Accounting*, and *Expense*
apps to view/modify all the fields mentioned during the workflow.
:::

Beneath the `Category`{.interpreted-text role="guilabel"} field, enter
in the amount to be expensed in the `Total`{.interpreted-text
role="guilabel"} field.

Next, designate if there are any `Included taxes`{.interpreted-text
role="guilabel"} in the `Total`{.interpreted-text role="guilabel"}. If a
preconfigured tax amount is selected from the
`Included taxes`{.interpreted-text role="guilabel"} field, Odoo
auto-calculates the taxed amount, based on the amount entered in the
`Total`{.interpreted-text role="guilabel"} field.

Then, choose which `Employee`{.interpreted-text role="guilabel"} was
responsible for the expense, and choose an option in the
`Paid By`{.interpreted-text role="guilabel"} field:
`Employee (to reimburse)`{.interpreted-text role="guilabel"} or
`Company`{.interpreted-text role="guilabel"}.

In this case, our employee paid for the hotel with their own money, so
the `Employee (to
reimburse)`{.interpreted-text role="guilabel"} option is chosen.

On the right-hand side of the expenses form, the option to add a
`Bill Reference`{.interpreted-text role="guilabel"} is available.
Beneath that, the auto-populated `Expense Date`{.interpreted-text
role="guilabel"} and `Account`{.interpreted-text role="guilabel"} fields
are available.

::: {.note}
::: {.title}
Note
:::

The `Expense Date`{.interpreted-text role="guilabel"} and
`Account`{.interpreted-text role="guilabel"} field can be modified, if
needed.
:::

Next, in the `Customer to Reinvoice`{.interpreted-text role="guilabel"}
field, click the blank field to reveal a drop-down menu. From this
drop-down menu, select the appropriate sales order to which this expense
should be attached. This field **must** be filled, in order to reinvoice
a customer for an expense.

Lastly, the option to modify the
`Analytic Distribution`{.interpreted-text role="guilabel"} and
`Company`{.interpreted-text role="guilabel"} fields are available. These
fields are *not* required to complete a reinvoiced expense to a
customer, but are available to modify, if needed.

Also, at the bottom of the expense form, there is a
`Notes...`{.interpreted-text role="guilabel"} section, wherein any notes
related to this expense can be added, if needed.

{.align-center}

At the top of the expense form, there are buttons to
`Attach Receipt`{.interpreted-text role="guilabel"}, `Create
Report`{.interpreted-text role="guilabel"}, and
`Split Expense`{.interpreted-text role="guilabel"}.

If there is a physical or digital receipt that should be attached to the
expense, click `Attach Receipt`{.interpreted-text role="guilabel"}.

If the cost of this expense needs to be split, click
`Split Expense`{.interpreted-text role="guilabel"}. This feature can be
used for a number of reasons (spitting expense with another employee, to
accommodate different tax rates, etc.).

If neither of these options are necessary, click
`Create Report`{.interpreted-text role="guilabel"} to lock in the
expense report that was just configured.

Doing so reveals an `Expense Report Summary`{.interpreted-text
role="guilabel"} for the new expense.

{.align-center}

Here, once the details related to the expense have been confirmed, click
`Submit to
Manager`{.interpreted-text role="guilabel"}. This sends the expense
report to the approving manager, who will review the expense.

The manager in charge of reviewing and approving the expense will
inspect the details related to the expense, and if there are no issues,
they will click the `Approve`{.interpreted-text role="guilabel"} button
--- which *only* appears on the manager\'s view of the
`Expense Report Summary`{.interpreted-text role="guilabel"} that\'s been
submitted to the manager by the employee.

{.align-center}

Once approved, the buttons at the top of the
`Expense Report Summary`{.interpreted-text role="guilabel"} change once
again. At this point, the buttons at the top of the
`Expense Report Summary`{.interpreted-text role="guilabel"} are: `Post
Journal Entries`{.interpreted-text role="guilabel"},
`Report in Next Payslip`{.interpreted-text role="guilabel"},
`Refuse`{.interpreted-text role="guilabel"}, and `Reset to
Draft`{.interpreted-text role="guilabel"}.

{.align-center}

When the manager is satisfied with the
`Expense Report Summary`{.interpreted-text role="guilabel"}, they\'ll
click `Post Journal Entries`{.interpreted-text role="guilabel"}.

Upon clicking `Post Journal Entries`{.interpreted-text role="guilabel"},
that button disappears, and the `Analytic
Distribution`{.interpreted-text role="guilabel"} column in the
`Expense`{.interpreted-text role="guilabel"} tab is filled with the
sales order that was initially configured to the expense in the
`Customer to Reinvoice`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

By default, the `Customer to Reinvoice`{.interpreted-text
role="guilabel"} field is enabled for the `[TRANS &
ACC] Travel & Accommodation`{.interpreted-text role="guilabel"},
`[COMM] Communication`{.interpreted-text role="guilabel"},
`[FOOD] Meals`{.interpreted-text role="guilabel"}, and
`[MIL] Mileage`{.interpreted-text role="guilabel"} expense category.

It should be noted that **not** all of the default expense categories
that come installed with the *Expenses* application have reinvoicing
policies activated. The setting may have to be manually activated.

To do that, navigate to
`Expenses app --> Configuration --> Expenses Categories`{.interpreted-text
role="menuselection"} to view a list of all expense categories in the
database.

Look in the `Re-Invoice Expenses`{.interpreted-text role="guilabel"}
column to see which selections have been made for each expense category.

{.align-center}

To modify an expense category, click the
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} in the
`Category`{.interpreted-text role="guilabel"} field, to reveal that
specific expense from.

Under the `Invoicing`{.interpreted-text role="guilabel"} section, in the
`Re-Invoice Expenses`{.interpreted-text role="guilabel"} field, select
either `At cost`{.interpreted-text role="guilabel"} or
`Sales price`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Reinvoice expense
-----------------

With those steps completed, it\'s time to return to the sales order to
complete the reinvoice of the expense to the customer.

To do that, navigate to
`main Odoo dashboard --> Sales app`{.interpreted-text
role="menuselection"}, and select the appropriate sales order that
should be reinvoiced for the expense.

On the sales form, the newly-configured expense is now in the
`Order Lines`{.interpreted-text role="guilabel"} tab, with its
`Delivered`{.interpreted-text role="guilabel"} column filled in, and
ready to be invoiced.

{.align-center}

After confirming the details of the expense, click
`Create Invoice`{.interpreted-text role="guilabel"} at the top of the
sales order. When clicked, a `Create invoices`{.interpreted-text
role="guilabel"} pop-up window appears.

{.align-center}

From this pop-up window, leave the `Create Invoice`{.interpreted-text
role="guilabel"} field on the default
`Regular invoice`{.interpreted-text role="guilabel"} option, and click
`Create Draft Invoice`{.interpreted-text role="guilabel"}.

Doing so reveals a `Customer Invoice Draft`{.interpreted-text
role="guilabel"} showing *only* the expense in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

{.align-center}

If all the information related to the expense is correct, click
`Confirm`{.interpreted-text role="guilabel"} to confirm the invoice.
Doing so moves the status of the invoice from `Draft`{.interpreted-text
role="guilabel"} to `Posted`{.interpreted-text role="guilabel"}.

To send the invoice to the customer, click
`Send \& Print`{.interpreted-text role="guilabel"}. Doing so reveals a
`Send`{.interpreted-text role="guilabel"} pop-up window, with a
preconfigured message and PDF invoice in the body of the message. The
message can be reviewed and modified, if needed.

Once ready, click `Send \& Print`{.interpreted-text role="guilabel"} to
send the invoice to the customer. When clicked, the pop-up window
disappears, and Odoo sends the message/invoice to the customer.
Additionally, a PDF of the invoice is automatically downloaded for
record-keeping and/or printing purposes.

Back on the `Customer Invoice`{.interpreted-text role="guilabel"}, click
the `Register Payment`{.interpreted-text role="guilabel"} button when
the customer pays for the invoiced expense.

{.align-center}

When `Register Payment`{.interpreted-text role="guilabel"} is clicked, a
`Register Payment`{.interpreted-text role="guilabel"} pop-up window
appears. In this pop-up window, the necessary fields are auto-populated
with the correct information. After reviewing the information, click
`Create Payment`{.interpreted-text role="guilabel"}.

{.align-center}

Once `Create Payment`{.interpreted-text role="guilabel"} is clicked, the
pop-up window disappears, and a green `In
Payment`{.interpreted-text role="guilabel"} banner is in the upper-right
corner of the invoice, signifying this invoice is paid for in full.
Thus, completing the workflow.

{.align-center}

::: {.seealso}
\- `invoicing_policy`{.interpreted-text role="doc"} -
`time_materials`{.interpreted-text role="doc"} -
`milestone`{.interpreted-text role="doc"}
:::
