# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/approve_expenses.md

Approve expenses
================

In Odoo, not just anyone can approve expense reports, only users with
the necessary rights (or permissions) can. This means that a user
**must** have at least *Team Approver* rights for the *Expenses* app.
Employees with the necessary rights can review expense reports, approve
or reject them, and provide feedback thanks to the integrated
communication tool.

Please refer to the
`access rights documentation </applications/general/users>`{.interpreted-text
role="doc"} to learn more about managing users and their access rights.

View expense reports
--------------------

Users who are able to approve expense reports, typically managers, can
easily view all expense reports they have access rights to. Go to
`Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}, to view the `All Reports`{.interpreted-text
role="guilabel"} dashboard.

A list of all expense reports with a status of either
`To Submit`{.interpreted-text role="guilabel"},
`Submitted`{.interpreted-text role="guilabel"},
`Approved`{.interpreted-text role="guilabel"},
`Posted`{.interpreted-text role="guilabel"}, or `Done`{.interpreted-text
role="guilabel"} appears. Expense reports with a status of
`Refused`{.interpreted-text role="guilabel"} are hidden, by default.

{.align-center}

Approve expense reports
-----------------------

Expense reports can be approved in two ways:
`individually <expenses/individual>`{.interpreted-text role="ref"} or
`in
bulk <expenses/multiple>`{.interpreted-text role="ref"}.

::: {.important}
::: {.title}
Important
:::

Only reports with a status of `Submitted`{.interpreted-text
role="guilabel"} can be approved.

It is recommended to display only `Submitted`{.interpreted-text
role="guilabel"} reports by ticking the checkbox beside the
`Submitted`{.interpreted-text role="guilabel"} filter, in the left
column, under the `Status`{.interpreted-text role="guilabel"} section.

If a report is **not** able to be approved, the
`Approve Report`{.interpreted-text role="guilabel"} button **does not**
appear on the `All Reports`{.interpreted-text role="guilabel"} page.
:::

### Approve individual reports {#expenses/individual}

To approve an individual report, navigate to
`Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}, and click on an individual report to view the
report form.

From here, several options are presented: `Approve`{.interpreted-text
role="guilabel"}, `Refuse`{.interpreted-text role="guilabel"}, and
`Reset to draft`{.interpreted-text role="guilabel"}.

Click `Approve`{.interpreted-text role="guilabel"} to approve the
report.

### Approve multiple reports {#expenses/multiple}

To approve multiple expense reports at once, first navigate to
`Expenses app -->
Expense Reports`{.interpreted-text role="menuselection"} to view a list
of expense reports. Next, select the reports to approve by ticking the
checkbox next to each report being approved, or tick the checkbox next
to the `Employee`{.interpreted-text role="guilabel"} column title to
select all the reports in the list.

Next, click the `Approve Report`{.interpreted-text role="guilabel"}
button.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

It is possible for team managers to view all the expense reports for
just their team members.

To do so, while on the `All Reports`{.interpreted-text role="guilabel"}
page, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} to the right of the
search bar, then click `My Team`{.interpreted-text role="guilabel"} in
the `fa-filter`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} section.

This presents all the reports for only the manager\'s team.

{.align-center}
:::

Refuse expense reports
----------------------

Expense reports can **only** be refused on the individual expense
report, and **not** from the `All Reports`{.interpreted-text
role="guilabel"} dashboard. To open an individual expense report,
navigate to `Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}, then click on an individual expense report to
view the report form.

If more information is needed, such as a missing receipt, communicate
any necessary information requests in the *chatter* of the report form.
On the individual expense report, click `Send message`{.interpreted-text
role="guilabel"} to open a message text box.

Type in a message, tagging the proper people, and post it to the
*chatter* by clicking `Send`{.interpreted-text role="guilabel"}. The
message is posted in the chatter, and the tagged people are notified,
via email.

::: {.note}
::: {.title}
Note
:::

The only people that can be tagged in a message are *followers* of the
specific report. To see who is a follower, click the
`fa-user-o`{.interpreted-text role="icon"} `(user)`{.interpreted-text
role="guilabel"} icon to display the followers of the expense report.

{.align-center}
:::

To refuse an expense report, click `Refuse`{.interpreted-text
role="guilabel"}, and a `Refuse Expense`{.interpreted-text
role="guilabel"} pop-up window appears. Enter a brief explanation for
the refusal beneath the `REASON TO REFUSE
EXPENSE`{.interpreted-text role="guilabel"} field, then click
`Refuse`{.interpreted-text role="guilabel"}.

{.align-center}

Once the expense report is refused, the status changes to
`Refused`{.interpreted-text role="guilabel"}, and the only button that
appears in the top-left is `Reset to Draft`{.interpreted-text
role="guilabel"}.
