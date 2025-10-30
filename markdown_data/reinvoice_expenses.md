# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/reinvoice_expenses.md

Re-invoice expenses
===================

If expenses are tracked on customer projects, they can be automatically
charged back to the customer. This is done by
`creating an expense <expenses/reinvoice-create>`{.interpreted-text
role="ref"}, referencing the sales order the expense is added to, and
then `creating an expense report
<expenses/reinvoice-report>`{.interpreted-text role="ref"}.

Next, managers
`approve the expense report <expenses/reinvoice-approve>`{.interpreted-text
role="ref"}, before the accounting department
`posts the journal entries <expenses/reinvoice-approve>`{.interpreted-text
role="ref"}.

Finally, once the expense report is posted to a journal, the expenses
appears on the specified `SO (Sales Order)`{.interpreted-text
role="abbr"}. The `SO (Sales Order)`{.interpreted-text role="abbr"} is
then `invoiced <expenses/reinvoice>`{.interpreted-text role="ref"}, thus
charging the customer for the expenses.

::: {.important}
::: {.title}
Important
:::

Approving expenses, posting expenses to accounting, and reinvoicing
expenses on `SOs (Sales
Orders)`{.interpreted-text role="abbr"} is **only** possible for users
with the appropriate `access rights
<../../general/users/access_rights>`{.interpreted-text role="doc"}.
:::

::: {.seealso}
This document provides lower-level instructions for the creation,
submission, approval, and posting of expenses. For fully-detailed
instructions for any of these steps, refer to the following
documentation:

-   `Log expenses <../expenses/log_expenses>`{.interpreted-text
    role="doc"}
-   `Expense reports <../expenses/expense_reports>`{.interpreted-text
    role="doc"}
-   `Approving expenses <../expenses/approve_expenses>`{.interpreted-text
    role="doc"}
-   `Posting expenses in accounting <../expenses/post_expenses>`{.interpreted-text
    role="doc"}
:::

Setup
-----

First, specify the invoicing policy for each expense category. Navigate
to `Expenses
app --> Configuration --> Expense Categories`{.interpreted-text
role="menuselection"}. Click on an expense category to view the expense
category form. Under the `INVOICING`{.interpreted-text role="guilabel"}
section, click the radio button next to the desired selection for
`Re-Invoice Expenses`{.interpreted-text role="guilabel"}:

-   `No`{.interpreted-text role="guilabel"}: The expense category cannot
    be re-invoiced.
-   `At cost`{.interpreted-text role="guilabel"}: The expense category
    invoices expenses at the cost set on the expense category form.
-   `Sales price`{.interpreted-text role="guilabel"}: The expense
    category invoices at the sales price set on the expense form.

Create an expense {#expenses/reinvoice-create}
-----------------

First, when
`creating a new expense <../expenses/log_expenses>`{.interpreted-text
role="doc"}, the correct information needs to be entered to re-invoice
the expense to a customer. Using the drop-down menu, select the
`SO (Sales Order)`{.interpreted-text role="abbr"} to add the expense to
in the `Customer to Reinvoice`{.interpreted-text role="guilabel"} field.

Next, select the `Analytic Distribution`{.interpreted-text
role="guilabel"} the expense is posted to. Multiple accounts can be
selected, if desired.

To add another `Analytic Distribution`{.interpreted-text
role="guilabel"}, click on the line to reveal the
`Analytic`{.interpreted-text role="guilabel"} pop-over window. Click
`Add a line`{.interpreted-text role="guilabel"}, then select the desired
`Analytic Distribution`{.interpreted-text role="guilabel"} from the
drop-down field. If selecting more than one
`Analytic Distribution`{.interpreted-text role="guilabel"}, the
`Percentage`{.interpreted-text role="guilabel"} fields **must** be
modified. By default, both fields are populated with [100%]{.title-ref}.
Adjust the percentages for all the fields, so the total of all selected
accounts equals [100%]{.title-ref}.

::: {.example}
A painting company agrees to paint an office building that houses two
different companies. During the estimate, a meeting is held at the
office location to discuss the project.

Both companies agree to pay for the travel expenses for the painting
company employees. When creating the expenses for the mileage and
hotels, **both companies** are listed in the
`Analytic Distribution`{.interpreted-text role="guilabel"} line, for 50%
each.
:::

Create an expense report {#expenses/reinvoice-report}
------------------------

After the expenses are created, the expense report must be
`created <expenses/create_report>`{.interpreted-text role="ref"} and
`submitted <expenses/submit>`{.interpreted-text role="ref"}, in the same
manner as all other expenses.

Once the expense report is submitted, a `fa-money`{.interpreted-text
role="icon"} `Sales Orders`{.interpreted-text role="guilabel"} smart
button appears at the top-center of both the expense report, and each
individual expense record being reinvoiced.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Selecting the proper `SO (Sales Order)`{.interpreted-text role="abbr"}
in the `Customer to Reinvoice`{.interpreted-text role="guilabel"} field
is **critical**, since this is how expenses are automatically invoiced
after an expense report is approved.

The `Customer to Reinvoice`{.interpreted-text role="guilabel"} field can
be modified *only* until an expense report is **approved**. After an
expense report is approved, the
`Customer to Reinvoice`{.interpreted-text role="guilabel"} field is no
longer able to be modified.
:::

Approve and post expenses {#expenses/reinvoice-approve}
-------------------------

Before
`approving an expense report <../expenses/approve_expenses>`{.interpreted-text
role="doc"}, ensure the `Analytic Distribution`{.interpreted-text
role="guilabel"} section is populated for every expense line.

If an `Analytic Distribution`{.interpreted-text role="guilabel"} entry
is missing, assign the correct accounts from the drop-down menu, then
click `Approve`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The `Approve`{.interpreted-text role="guilabel"} button **only** appears
after an expense report has been `submitted
<expenses/submit>`{.interpreted-text role="ref"}.
:::

The accounting department is typically responsible for
`posting journal entries
<../expenses/post_expenses>`{.interpreted-text role="doc"}. To post
expenses to an accounting journal, click `Post
Journal Entries`{.interpreted-text role="guilabel"}. Once an expense
report is approved, it can then be posted.

The `SO (Sales Order)`{.interpreted-text role="abbr"} is **only**
updated *after* the journal entries are posted. Once the journal entries
are posted, the expenses now appear on the referenced
`SO (Sales Order)`{.interpreted-text role="abbr"}.

Invoice expenses {#expenses/reinvoice}
----------------

After the expense report has been approved, and the journal entries have
been posted, the `SO
(Sales Order)`{.interpreted-text role="abbr"} is updated, and the
customer can be invoiced.

Select the expense report, and click the `fa-money`{.interpreted-text
role="icon"} `Sales Orders`{.interpreted-text role="guilabel"} smart
button to open the `SO (Sales Order)`{.interpreted-text role="abbr"}.
The expenses to be re-invoiced now appear on the `SO (Sales
Order)`{.interpreted-text role="abbr"}.

::: {.note}
::: {.title}
Note
:::

More than one `SO (Sales Order)`{.interpreted-text role="abbr"} can be
referenced on an expense report. If more than one
`SO (Sales Order)`{.interpreted-text role="abbr"} is referenced,
clicking the `Sales Orders`{.interpreted-text role="guilabel"} smart
button opens a list displaying all the
`SOs (Sales Order)`{.interpreted-text role="abbr"} associated with that
expense report. Click on a `SO (Sales Order)`{.interpreted-text
role="abbr"} to open the individual `SO (Sales Order)`{.interpreted-text
role="abbr"} details.
:::

The expenses are listed in the `SO (Sales Order)`{.interpreted-text
role="abbr"} `Order Lines`{.interpreted-text role="guilabel"} tab.

{.align-center}

Next, click `Create Invoice`{.interpreted-text role="guilabel"}, and a
`Create invoices`{.interpreted-text role="guilabel"} pop-up window
appears. Select if the invoice is a `Regular invoice`{.interpreted-text
role="guilabel"}, a `Down payment (percentage)`{.interpreted-text
role="guilabel"}, or a `Down payment (fixed amount)`{.interpreted-text
role="guilabel"}. Then, click `Create Draft Invoice`{.interpreted-text
role="guilabel"}. Doing so creates a draft invoice for the customer.
Click `Confirm`{.interpreted-text role="guilabel"} to confirm the
invoice, and the customer is invoiced for the expenses.
