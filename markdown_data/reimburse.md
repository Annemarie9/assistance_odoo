# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/reimburse.md

Reimburse employees
===================

After an expense report is
`posted to an accounting journal <../expenses/post_expenses>`{.interpreted-text
role="doc"}, the next step is to reimburse the employee. Just like
approving and posting expenses, employees can be reimbursed in two ways:
with cash, check, or direct deposit (`individually
<expenses/reimburse-single>`{.interpreted-text role="ref"} or
`in bulk <expenses/reimburse-bulk>`{.interpreted-text role="ref"}), or
`reimbursed in a
payslip <expenses/reimburse-payslip>`{.interpreted-text role="ref"}.

Settings
--------

Reimbursements can be paid via paycheck, check, cash, or bank transfer.
To set up payment options, first configure the various settings by
navigating to `Expenses app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

To reimburse employees for expenses
`in their paychecks <expenses/reimburse-payslip>`{.interpreted-text
role="ref"}, tick the checkbox beside the
`Reimburse in Payslip`{.interpreted-text role="guilabel"} option in the
`Expenses`{.interpreted-text role="guilabel"} section.

Next, set how payments are made in the `Accounting`{.interpreted-text
role="guilabel"} section. Click the drop-down menu under
`Payment Methods`{.interpreted-text role="guilabel"}, and select the
desired payment option. Default options include paying by
`Manual (Cash)`{.interpreted-text role="guilabel"},
`Checks (Bank)`{.interpreted-text role="guilabel"},
`NACHA (Bank)`{.interpreted-text role="guilabel"}, and others. Leaving
this field blank allows for **all** available payment options to be
used.

When all desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"} to activate the settings.

Reimburse individually {#expenses/reimburse-single}
----------------------

To reimburse an individual expense report, first navigate to
`Expenses app -->
Expense Reports`{.interpreted-text role="menuselection"}. All expense
reports are presented in a default list view. Click on the expense
report being reimbursed to view the report details.

::: {.important}
::: {.title}
Important
:::

**Only** expense reports with a status of `Posted`{.interpreted-text
role="guilabel"} can be reimbursed.
:::

Click the `Register Payment`{.interpreted-text role="guilabel"} button
in the top-left corner of the expense report, and a
`Register Payment`{.interpreted-text role="guilabel"} pop-up window
appears. Enter the following information in the pop-up window:

-   `Journal`{.interpreted-text role="guilabel"}: Select the accounting
    journal to post the payment to using the drop-down menu. The default
    options are `Bank`{.interpreted-text role="guilabel"} or
    `Cash`{.interpreted-text role="guilabel"}.
-   `Payment Method`{.interpreted-text role="guilabel"}: Select how the
    payment is made using the drop-down menu. If
    `Cash`{.interpreted-text role="guilabel"} is selected for the
    `Journal`{.interpreted-text role="guilabel"}, the only option
    available is `Manual`{.interpreted-text role="guilabel"}. If
    `Bank`{.interpreted-text role="guilabel"} is selected for the
    `Journal`{.interpreted-text role="guilabel"}, the default options
    are `Manual`{.interpreted-text role="guilabel"} or
    `Checks`{.interpreted-text role="guilabel"}.
-   `Recipient Bank Account`{.interpreted-text role="guilabel"}: Select
    the employee\'s bank account the payment is being sent to. If the
    employee has a bank account on file in the `Private Information tab
    <employees/private-info>`{.interpreted-text role="ref"} of their
    employee form in the **Employees** app, that bank account populates
    this field, by default.
-   `Amount`{.interpreted-text role="guilabel"}: The total amount being
    reimbursed populates this field, by default. The currency, located
    to the right of the field, can be modified using the drop-down menu.
-   `Payment Date`{.interpreted-text role="guilabel"}: Enter the date
    the payments are issued in this field. The current date populates
    this field, by default.
-   `Memo`{.interpreted-text role="guilabel"}: The text entered in the
    `Expense Report Summary
    <../expenses/expense_reports>`{.interpreted-text role="doc"} field
    of the expense report populates this field, by default.

![The Register Payment pop-up window filled out for an individual expense report
reimbursement.](reimburse/payment.png){.align-center}

When the fields of the pop-up window are completed, click the
`Create Payment`{.interpreted-text role="guilabel"} button to register
the payment, and reimburse the employee.

Reimburse in bulk {#expenses/reimburse-bulk}
-----------------

To reimburse multiple expense reports at once, navigate to
`Expenses app --> Expense
Reports`{.interpreted-text role="menuselection"} to view all expense
reports in a list view. Next, adjust the `STATUS`{.interpreted-text
role="guilabel"} filters on the left side to only present expense
reports with a status of `Posted`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Adjusting the `STATUS`{.interpreted-text role="guilabel"} filters to
only show `Posted`{.interpreted-text role="guilabel"} expense reports is
not necessary, but removes the step of selecting each individual report
in the list.
:::

Tick the checkbox next to the `Employee`{.interpreted-text
role="guilabel"} column title to select all the reports in the list.
Once ticked, the number of selected expense reports appears at the top
of the page (`(#) Selected`{.interpreted-text role="guilabel"}).
Additionally, a `Register Payment`{.interpreted-text role="guilabel"}
button also appears in the upper-left corner.

{.align-center}

Click the `Register Payment`{.interpreted-text role="guilabel"} button,
and a `Register Payment`{.interpreted-text role="guilabel"} pop-up
window appears. Enter the following information in the pop-up window:

-   `Journal`{.interpreted-text role="guilabel"}: Select the accounting
    journal the payment should be posted to, using the drop-down menu.
    The default options are `Bank`{.interpreted-text role="guilabel"} or
    `Cash`{.interpreted-text role="guilabel"}.
-   `Payment Method`{.interpreted-text role="guilabel"}: Select how the
    payment is made using the drop-down menu. If
    `Cash`{.interpreted-text role="guilabel"} is selected for the
    `Journal`{.interpreted-text role="guilabel"}, the only option
    available is `Manual`{.interpreted-text role="guilabel"}. If
    `Bank`{.interpreted-text role="guilabel"} is selected for the
    `Journal`{.interpreted-text role="guilabel"}, the default options
    are `Manual`{.interpreted-text role="guilabel"} or
    `Checks`{.interpreted-text role="guilabel"}.
-   `Group Payments`{.interpreted-text role="guilabel"}: When multiple
    expense reports are selected for the same employee, this option
    appears. Tick the checkbox to have only one payment made, rather
    than issuing multiple payments to the same employee.
-   `Payment Date`{.interpreted-text role="guilabel"}: Enter the date
    the payments are issued. The current date populates this field, by
    default.

{.align-center}

When the fields on the pop-up window are completed, click the
`Create Payments`{.interpreted-text role="guilabel"} button to register
the payments, and reimburse the employees.

Report in next payslip {#expenses/reimburse-payslip}
----------------------

If the *Reimburse in Payslip* option is activated on the *Settings*
page, payments can be added to their next payslip, instead of issued
manually.

::: {.important}
::: {.title}
Important
:::

Reimbursing expenses on payslips can **only** be done individually, on
an expense report with a status of *Approved*. Once an expense report
has a status of *Posted*, the option to reimburse in the following
payslip does **not** appear.
:::

Navigate to `Expenses app --> Expense Reports`{.interpreted-text
role="menuselection"}, and click on the individual expense report being
reimbursed on the following paycheck. Click the
`Report in Next Payslip`{.interpreted-text role="guilabel"} smart
button, and the expenses are added to the next payslip issued for that
employee. Additionally, a message is logged in the chatter stating the
expense is added to the following payslip.

{.align-center}

The status for the expense report remains `Approved`{.interpreted-text
role="guilabel"}. The status only changes to `Posted`{.interpreted-text
role="guilabel"} (and then `Done`{.interpreted-text role="guilabel"}),
when the paycheck is processed.

::: {.seealso}
Refer to the `Payslips <../../hr/payroll/payslips>`{.interpreted-text
role="doc"} documentation for more information about processing
paychecks.
:::
