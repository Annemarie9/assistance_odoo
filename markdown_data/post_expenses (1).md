# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/post_expenses.md

Post expenses
=============

Once an expense report is
`approved <../expenses/approve_expenses>`{.interpreted-text role="doc"},
the next step is to post the expense report to the proper accounting
journal.

::: {.important}
::: {.title}
Important
:::

To post expense reports to an accounting journal, the user **must** have
the following
`access rights <../../general/users/access_rights>`{.interpreted-text
role="doc"}:

-   Accounting: *Accountant* or *Adviser*
-   Expenses: *Manager*
:::

Only expense reports with an *Approved* status can post the expenses to
a journal. To view all expense reports, navigate to
`Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}. Next, to view **only** approved expense reports
that need to be posted, adjust the filters on the left side, so only the
`Approved`{.interpreted-text role="guilabel"} checkbox is ticked.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The default `All Reports`{.interpreted-text role="guilabel"} dashboard
displays all expense reports, except reports with a status of
`Refused`{.interpreted-text role="guilabel"}.
:::

Expense reports can be posted to accounting journals in two ways:
`individually
<expenses/individual-reports>`{.interpreted-text role="ref"} or
`in bulk <expenses/multiple-reports>`{.interpreted-text role="ref"}.

Post individual reports {#expenses/individual-reports}
-----------------------

To post an individual report, navigate to
`Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}, and click on an individual report with a
`Status`{.interpreted-text role="guilabel"} of
`Approved`{.interpreted-text role="guilabel"}, to view the report form.
In this view, several options are presented:
`Post Journal Entries`{.interpreted-text role="guilabel"},
`Report In Next Payslip`{.interpreted-text role="guilabel"},
`Refuse`{.interpreted-text role="guilabel"}, or
`Reset to Draft`{.interpreted-text role="guilabel"}.

Click `Post Journal Entries`{.interpreted-text role="guilabel"} to post
the report.

The accounting journal the expenses are posted to is listed in the
`Journal`{.interpreted-text role="guilabel"} field of the expense
report.

After posting the expenses to an accounting journal, a
`Journal Entry`{.interpreted-text role="guilabel"} smart button appears
at the top of the screen. Click the `Journal Entry`{.interpreted-text
role="guilabel"} smart button, and the details for the journal entry
appear, with a status of `Posted`{.interpreted-text role="guilabel"}.

Post multiple reports {#expenses/multiple-reports}
---------------------

To post multiple expense reports at once, navigate to
`Expenses app --> Expense
Reports`{.interpreted-text role="menuselection"} to view a list of
expense reports. Next, select the reports to approve by ticking the
checkbox next to each report being approved.

::: {.note}
::: {.title}
Note
:::

Only expense reports with a status of `Approved`{.interpreted-text
role="guilabel"} are able to post the expenses to an accounting journal.
If an expense report is selected that **cannot** be posted, such as an
unapproved report, or the report has already been posted to a journal,
the `Post
Entries`{.interpreted-text role="guilabel"} button is **not** visible.
:::

::: {.tip}
::: {.title}
Tip
:::

To select **only** approved expense reports, adjust the filters on the
left side, so that only the `Approved`{.interpreted-text
role="guilabel"} checkbox is ticked. Next, tick the checkbox next to the
`Employee`{.interpreted-text role="guilabel"} column title to select
**all** the `Approved`{.interpreted-text role="guilabel"} reports in the
list at once.
:::

Next, click the `Post Entries`{.interpreted-text role="guilabel"}
button.

{.align-center}
