# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/expense_reports.md

Expense reports
===============

When expenses are ready to submit (such as, at the end of a business
trip, or once a month), an *expense report* needs to be created. Open
the main `Expenses app`{.interpreted-text role="menuselection"}
dashboard, which displays the `My Expenses`{.interpreted-text
role="guilabel"} dashboard, by default. Alternatively, navigate to
`Expenses app --> My Expenses --> My Expenses`{.interpreted-text
role="menuselection"}.

Expenses are color-coded by status. Any expense with a status of
`To Report`{.interpreted-text role="guilabel"} (expenses that still need
to be added to an expense report) is shown in blue text. All other
statuses (`To Submit`{.interpreted-text role="guilabel"},
`Submitted`{.interpreted-text role="guilabel"}, and
`Approved`{.interpreted-text role="guilabel"}) the text appears in
black.

Create expense reports {#expenses/create_report}
----------------------

First, select each desired expense to be added to the report on the
`My Expenses`{.interpreted-text role="guilabel"} dashboard, by ticking
the checkbox next to each entry, or quickly select all the expenses in
the list by ticking the checkbox next to the
`Expense Date`{.interpreted-text role="guilabel"} column title, if
needed.

Another way to quickly add all expenses that are not on a expense
report, is to click the `Create Report`{.interpreted-text
role="guilabel"} button, *without* selecting any expenses, and Odoo
automatically selects all expenses with a status of
`To Submit`{.interpreted-text role="guilabel"} that are not already on a
report.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Any expense can be selected from the `My Expenses`{.interpreted-text
role="guilabel"} list, except for expenses with a status of
`Approved`{.interpreted-text role="guilabel"}.

The `Create Report`{.interpreted-text role="guilabel"} button is visible
as long as there is a minimum of one expense on the list with a status
of either `To Report`{.interpreted-text role="guilabel"} or
`To Submit`{.interpreted-text role="guilabel"}.

When the `Create Report`{.interpreted-text role="guilabel"} button is
clicked, all expenses with a status of `To
Submit`{.interpreted-text role="guilabel"} that are *not* currently on
another expense report appears in the newly-created expense report.

If all expenses on the `My Expenses`{.interpreted-text role="guilabel"}
report are already associated with another expense report, an
`Invalid Operation`{.interpreted-text role="guilabel"} pop-up window
appears, stating `You have no
expenses to report.`{.interpreted-text role="guilabel"}
:::

Once the expenses have been selected, click the
`Create Report`{.interpreted-text role="guilabel"} button. The new
report appears with all the expenses listed in the
`Expense`{.interpreted-text role="guilabel"} tab. If there is a receipt
attached to an individual expense, a `fa-paperclip`{.interpreted-text
role="icon"} `(paperclip)`{.interpreted-text role="guilabel"} icon
appears between the `Customer to Reinvoice`{.interpreted-text
role="guilabel"} and `Analytic Distribution`{.interpreted-text
role="guilabel"} columns.

When the report is created, the date range for the expenses appears in
the `Expense Report
Summary`{.interpreted-text role="guilabel"} field, by default. It is
recommended to edit this field with a short summary for each report to
help keep expenses organized. Enter a description for the expense
report, such as [Client Trip NYC]{.title-ref}, or [Office Supplies for
Presentation]{.title-ref}, in the
`Expense Report Summary`{.interpreted-text role="guilabel"} field.

The `Employee`{.interpreted-text role="guilabel"},
`Paid By`{.interpreted-text role="guilabel"}, and
`Company`{.interpreted-text role="guilabel"} fields autopoulate with the
information listed on the individual expenses.

Next, select a `Manager`{.interpreted-text role="guilabel"} from the
drop-down menu to assign a manager to review the report. If needed,
update the `Journal`{.interpreted-text role="guilabel"} field, using the
drop-down menu.

{.align-center}

If some expenses are missing from the report, they can still be added
from this report form. To do so, click `Add a line`{.interpreted-text
role="guilabel"} at the bottom of the `Expense`{.interpreted-text
role="guilabel"} tab.

An `Add: Expense Lines`{.interpreted-text role="guilabel"} pop-up window
appears, displaying all the available expenses (with a
`To Submit`{.interpreted-text role="guilabel"} status) that can be added
to the report.

If a new expense needs to be added that does **not** appear on the list,
click `New`{.interpreted-text role="guilabel"} to
`create a new expense <../expenses/log_expenses>`{.interpreted-text
role="doc"} and add it to the report.

Tick the checkbox next to each expense being added, then click
`Select`{.interpreted-text role="guilabel"}.

Doing so removes the pop-up window, and the items now appear on the
report.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Expense reports can be created in one of three places:

1.  Navigate to the main `Expenses app`{.interpreted-text
    role="menuselection"} dashboard (also accessible, via
    `Expenses app --> My Expenses --> My Expenses`{.interpreted-text
    role="menuselection"})
2.  Navigate to
    `Expenses app --> My Expenses --> My Reports`{.interpreted-text
    role="menuselection"}
3.  Navigate to `Expenses app --> Expense Reports`{.interpreted-text
    role="menuselection"}

In any of these views, click `New`{.interpreted-text role="guilabel"} to
create a new expense report.
:::

Submit expense reports {#expenses/submit}
----------------------

When an expense report is completed, the next step is to submit the
report to a manager for approval. To view all expense reports, navigate
to `Expenses app --> My Expenses -->
My Reports`{.interpreted-text role="menuselection"}. Open the specific
report from the list of expense reports.

::: {.note}
::: {.title}
Note
:::

Reports must be individually submitted, and **cannot** be submitted in
batches.
:::

If the list is large, grouping the results by status may be helpful,
since only reports with a `To Submit`{.interpreted-text role="guilabel"}
status need to be submitted; reports with an
`Approved`{.interpreted-text role="guilabel"} or
`Submitted`{.interpreted-text role="guilabel"} status do not.

The `To Submit`{.interpreted-text role="guilabel"} expenses are
identifiable by the `To Submit`{.interpreted-text role="guilabel"}
status, and by the blue text, while all other expense text appears in
black.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The status of each report is shown in the `Status`{.interpreted-text
role="guilabel"} column. If the `Status`{.interpreted-text
role="guilabel"} column is not visible, click the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(additional options)`{.interpreted-text role="guilabel"} icon at the
end of the row, and tick the checkbox beside `Status`{.interpreted-text
role="guilabel"} from the resulting drop-down menu.
:::

Click on a report to open it, then click
`Submit To Manager`{.interpreted-text role="guilabel"}. After submitting
a report, the next step is to wait for the manager to approve it.

::: {.important}
::: {.title}
Important
:::

`Approving <../expenses/approve_expenses>`{.interpreted-text role="doc"}
expenses, `posting
<../expenses/post_expenses>`{.interpreted-text role="doc"} expenses, and
`reimbursing <../expenses/reimburse>`{.interpreted-text role="doc"}
expenses are **only** for users with the appropriate
`access rights documentation
</applications/general/users>`{.interpreted-text role="doc"}.
:::
