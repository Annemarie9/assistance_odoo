# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll/payslips.md

Payslips
========

*Payslips* are created either by the employees themselves or their
managers, and are approved by authorized employees (typically managers).
Then, once payslips are approved, employees are issued payslips and are
paid either by check or direct deposit, depending on how their employee
profile is configured.

The `Payslips`{.interpreted-text role="guilabel"} drop-down header of
the `Payroll`{.interpreted-text role="menuselection"} application
consists of three sections: `To Pay`{.interpreted-text role="guilabel"},
`All Payslips`{.interpreted-text role="guilabel"}, and
`Batches`{.interpreted-text role="guilabel"}.

These three sections provide all the tools needed to create payslips for
employees, including individual payslips, a batch of payslips, or
commission payslips.

{.align-center}

To pay {#payroll/to-pay}
------

Click on `Payroll app --> Payslips --> To Pay`{.interpreted-text
role="menuselection"} to see the payslips that need to be paid. On this
page, Odoo displays the payslips that have not been generated yet, and
can be created from this dashboard.

{.align-center}

Each payslip lists the `Reference`{.interpreted-text role="guilabel"}
number for the individual payslip, the `Employee`{.interpreted-text
role="guilabel"} name, the `Batch Name`{.interpreted-text
role="guilabel"}, the `Company`{.interpreted-text role="guilabel"}, the
`Basic
Wage`{.interpreted-text role="guilabel"}, `Gross Wage`{.interpreted-text
role="guilabel"}, `Net Wage`{.interpreted-text role="guilabel"}, and the
`Status`{.interpreted-text role="guilabel"} of the payslip.

Click on an individual payslip entry to view the details for that
individual payslip.

### Create a new payslip {#payroll/new-payslip}

A new payslip can be created from either the
`Payslips To Pay <payroll/to-pay>`{.interpreted-text role="ref"} page or
the `Employee Payslips <payroll/all-payslips>`{.interpreted-text
role="ref"} page.

Create a new payslip by clicking the `New`{.interpreted-text
role="guilabel"} button in the top-left corner.

A blank payslip form is loaded, where the necessary payslip information
can be entered.

#### Payslip form

On the blank payslip form, several fields are required. Most of the
required fields auto-populate after an employee is selected.

Fill out the following information on the payslip form:

-   `Employee`{.interpreted-text role="guilabel"}: type in the name of
    an employee, or select the desired employee from the drop-down list
    in this field. This field is **required**.

    ::: {.note}
    ::: {.title}
    Note
    :::

    It is recommended to **only** create payslips for employees that are
    already in the database. If there is no current employee record (and
    therefore no employee contract) it is recommended to create the new
    employee in the *Employees* application **before** creating payslips
    for that employee. Refer to the
    `new employee <../employees/new_employee>`{.interpreted-text
    role="doc"} documentation for instructions on how to add an
    employee.
    :::

-   `Period`{.interpreted-text role="guilabel"}: the first day to the
    last day of the *current* month auto-populates the
    `Period`{.interpreted-text role="guilabel"} fields by default. The
    dates can be changed, if desired.

    To change the start date, click on the first date in the
    `Period`{.interpreted-text role="guilabel"} field to reveal a pop-up
    calendar. On this calendar, use the
    `< (less-than)`{.interpreted-text role="guilabel"} and `>
    (greater-than)`{.interpreted-text role="guilabel"} icons to select
    the desired month. Then, click on the desired day to select that
    specific date.

    Repeat this process to modify the end date for the payslip. These
    fields are **required**.

-   `Contract`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the desired contract for the employee. Only the
    available corresponding contracts for the selected employee appear
    as options. This field is **required**.

-   `Batch`{.interpreted-text role="guilabel"}: using the drop-down menu
    in this field, select the batch of payslips this new payslip should
    be added to.

-   `Structure`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the salary structure type. Only the corresponding
    structures associated with the selected contract for the employee
    appear as options.

    If no employee and/or no contract is selected yet, all available
    `Structures`{.interpreted-text role="guilabel"} appear in the list.
    Once an employee and/or contract is selected, any unavailable
    `Structures`{.interpreted-text role="guilabel"} set for that
    employee and/or contract do not appear. This field is **required**.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Typically, after making a selection in the `Employee`{.interpreted-text
role="guilabel"} field, Odoo auto-populates all other required fields
(besides the `Period`{.interpreted-text role="guilabel"} field), but
**only** if that information is already on that employee\'s form in the
*Employees* app.
:::

::: {.important}
::: {.title}
Important
:::

If modifications to auto-populated fields are made, it is recommended to
check with the accounting department to ensure every entry that affects
the *Accounting* application is correct.
:::

##### Worked days & inputs tab {#payroll/worked-days-inputs}

-   `Worked Days`{.interpreted-text role="guilabel"}: the entries under
    `Worked Days`{.interpreted-text role="guilabel"} (including the
    `Type`{.interpreted-text role="guilabel"},
    `Description`{.interpreted-text role="guilabel"},
    `Number of Days`{.interpreted-text role="guilabel"}, `Number of
    Hours`{.interpreted-text role="guilabel"}, and
    `Amount`{.interpreted-text role="guilabel"}) are automatically
    filled in, based on what was entered for the
    `Period`{.interpreted-text role="guilabel"},
    `Contract`{.interpreted-text role="guilabel"}, and
    `Structure`{.interpreted-text role="guilabel"} fields of the payslip
    form.

-   `Other Inputs`{.interpreted-text role="guilabel"}: additional inputs
    affecting the payslip can be entered in this section, such as
    deductions, reimbursements, and expenses.

    Click `Add a line`{.interpreted-text role="guilabel"} to create an
    entry in the `Other Inputs`{.interpreted-text role="guilabel"}
    section.

    Using the drop-down menu in the `Type`{.interpreted-text
    role="guilabel"} column, select a `Type`{.interpreted-text
    role="guilabel"} for the input. Next, enter a
    `Description`{.interpreted-text role="guilabel"}, if desired.
    Lastly, enter the amount in the `Count`{.interpreted-text
    role="guilabel"} field.

{.align-center}

##### Salary computation tab

-   `Salary Computation`{.interpreted-text role="guilabel"}: the
    `Salary Computation`{.interpreted-text role="guilabel"} tab is
    automatically filled in after the `Compute Sheet`{.interpreted-text
    role="guilabel"} button is clicked. Doing so displays the wages,
    deductions, taxes, etc. for the entry.
-   `Has Negative Net To Report`{.interpreted-text role="guilabel"}:
    click the checkbox if the employee has a negative net amount for
    this payslip. This **only** appears if the employee\'s payslip has a
    negative balance.

{.align-center}

##### Other info tab

-   `Payslip Name`{.interpreted-text role="guilabel"}: type in a name
    for the payslip in this field. The name should be short and
    descriptive, such as [(Employee Name) April 2023]{.title-ref}. This
    field is **required**.

-   `Company`{.interpreted-text role="guilabel"}: select the company the
    payslip applies to using the drop-down menu in this field. This
    field is **required**.

-   `Close Date`{.interpreted-text role="guilabel"}: enter the date that
    the payment is made to the employee in this field.

    Click in the field to reveal a calendar pop-up window. Using the
    `< >
    (less-than/greater-than)`{.interpreted-text role="guilabel"} icons,
    navigate to the desired month and year.

    Then, click on the desired date to select it.

-   `Date Account`{.interpreted-text role="guilabel"}: enter the date on
    which the payslip should be posted in this field.

-   `Salary Journal`{.interpreted-text role="guilabel"}: this field
    auto-populates after selecting an existing
    `Employee`{.interpreted-text role="guilabel"}. This field **cannot**
    be edited, as it is linked to the *Accounting* application. This
    field is **required**.

-   `Accounting Entry`{.interpreted-text role="guilabel"}: if
    applicable, this field is automatically populated once the payslip
    is confirmed. This field **cannot** be modified.

-   `Add an Internal Note...`{.interpreted-text role="guilabel"}: any
    note or reference message for the new entry can be typed in this
    field.

{.align-center}

#### Process the new payslip

When all the necessary information on the payslip is entered, click the
`Compute Sheet`{.interpreted-text role="guilabel"} button. Upon doing
so, all the information on the payslip is saved, and the `Salary
Computation`{.interpreted-text role="guilabel"} tab auto-populates,
based on the information on the employee\'s contract or attendance
records.

If any modifications need to be made, first click the
`Cancel`{.interpreted-text role="guilabel"} button, then click the
`Set to Draft`{.interpreted-text role="guilabel"} button. Make any
desired changes, then click the `Compute Sheet`{.interpreted-text
role="guilabel"} button once again, and the changes are reflected in the
`Worked Days`{.interpreted-text role="guilabel"} and
`Salary Computation`{.interpreted-text role="guilabel"} tabs.

Once everything on the payslip form is correct, click the
`Create Draft Entry`{.interpreted-text role="guilabel"} button to create
the payslip.

Then, a confirmation pop-up window appears, asking
`Are you sure you want to proceed?`{.interpreted-text role="guilabel"}.
Click `OK`{.interpreted-text role="guilabel"} to confirm.

The chatter is automatically updated to show the email sent to the
employee, along with a PDF copy of the payslip.

::: {.note}
::: {.title}
Note
:::

The database may need to be refreshed for the payslip and email to
appear.
:::

To print the payslip, click the `Print`{.interpreted-text
role="guilabel"} button. To cancel the payslip, click the
`Cancel`{.interpreted-text role="guilabel"} button.

{.align-center}

Next, the payment must be sent to the employee. To do this, click the
`Register Payment`{.interpreted-text role="guilabel"} button. Doing so
reveals a pop-up form, in which the desired
`Bank Journal`{.interpreted-text role="guilabel"} that the payment
should be made against must be selected from a drop-down menu. Then,
click the `Confirm`{.interpreted-text role="guilabel"} button to confirm
the journal, and return to the payslip.

::: {.important}
::: {.title}
Important
:::

In order for a payslip to be paid, the employee *must* have a bank
account entered in their contact information. If there is no bank
information, a payslip cannot be paid, and an error appears when the
`Make Payment`{.interpreted-text role="guilabel"} button is clicked.
Banking information can be found in the
`Private Information <employees/private-info>`{.interpreted-text
role="ref"} tab on the employee\'s card in the *Employees* app. Edit the
employee card, and add banking information, if it is missing.

{.align-center}
:::

Odoo automatically checks bank account information. If there is an error
with the employee\'s listed bank account, an error appears in a pop-up
window, stating, *The employee bank account is untrusted.* If this error
appears, update the employee\'s bank account information on their
`Employee Form <employees/private-info>`{.interpreted-text role="ref"}.

If a payment needs to be canceled or refunded, click the corresponding
`Cancel`{.interpreted-text role="guilabel"} or
`Refund`{.interpreted-text role="guilabel"} button, located at the
top-left of the screen.

::: {.tip}
::: {.title}
Tip
:::

Before processing payslips, it is best practice to check the *Warnings*
section of the *Payroll* app dashboard. Here, all possible issues
concerning payroll appear.

To view the warnings, navigate to
`Payroll app --> Dashboard`{.interpreted-text role="menuselection"}. The
warnings appear in the top-left corner of the dashboard.

{.align-center}

Warnings are grouped by type, such as [Employees Without Running
Contracts]{.title-ref} or [Employees Without Bank account
Number]{.title-ref}. Click on a warning to view all entries associated
with that specific issue.

If the warnings are not resolved, at any point in the payslip processing
process, an error may occur. Errors appear in a pop-up window, and
provide details for the error, and how to resolve them.

Payslips **cannot** be completed if there are any warnings or issues
associated with the payslip.
:::

All payslips {#payroll/all-payslips}
------------

To view all payslips, regardless of status, go to
`Payroll app --> Payslips --> All
Payslips`{.interpreted-text role="menuselection"}. The
`Employee Payslips`{.interpreted-text role="guilabel"} page loads,
displaying all payslips, organized by batch, in a default nested list
view.

Click on the `▶ (right arrow)`{.interpreted-text role="guilabel"} next
to an individual batch name to view all the payslips in that particular
batch, along with all the payslip details.

The number of payslips in the batch is written in parenthesis after the
batch name. The `Status`{.interpreted-text role="guilabel"} for each
individual payslip appears on the far-right side, indicating one of the
following status options:

-   `Draft`{.interpreted-text role="guilabel"}: the payslip is created,
    and there is still time to make edits, since the amounts are not
    calculated.
-   `Waiting`{.interpreted-text role="guilabel"}: the payslip has been
    calculated, and the salary details can be found in the *Salary
    Computation* tab.
-   `Done`{.interpreted-text role="guilabel"}: the payslip is calculated
    and ready to be paid.
-   `Paid`{.interpreted-text role="guilabel"}: the employee has been
    paid.

{.align-center}

Click on an individual payslip to view the details for that payslip on a
separate page. Using the breadcrumb menu, click
`Employee Payslips`{.interpreted-text role="guilabel"} to go back to the
list view of all payslips.

A new payslip can be created from the
`Employee Payslips`{.interpreted-text role="guilabel"} page, by clicking
the `New`{.interpreted-text role="guilabel"} button in the upper-left
corner. Doing so reveals a separate blank payslip form page. On that
blank payslip form page, enter all the necessary information, as
described in the
`Create new payslips <payroll/new-payslip>`{.interpreted-text
role="ref"} section.

To print PDF versions of payslips from the *Payslips to Pay* or
`Employee Payslips`{.interpreted-text role="guilabel"} pages, first
select the desired payslips by clicking on the individual checkbox to
the left of each payslip to be printed. Or, click the box to the left of
the `Reference`{.interpreted-text role="guilabel"} column title, which
selects all visible payslips on the page. Then, click the
`Print`{.interpreted-text role="guilabel"} button to print the payslips.

Payslips can also be exported to an Excel spreadsheet. To export **all**
payslips, click on the `⚙️ (gear)`{.interpreted-text role="guilabel"}
icon at the end of the words `Employee Payslips`{.interpreted-text
role="guilabel"} in the top-left corner. This reveals a drop-down menu.
Click `Export All`{.interpreted-text role="guilabel"} to export all
payslips to a spreadsheet.

{.align-center}

To export only select payslips, first select the payslips to be exported
from the list. Then, click the checkbox to the left of each individual
payslip to select it. As payslips are selected, a smart button appears
in the top-center of the page, indicating the number of selected
payslips. Then, click the `⚙️ (gear) Actions`{.interpreted-text
role="guilabel"} icon in the top-center of the page, and click
`Export`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Both *To Pay* and *All Payslips* display all the detailed information
for each payslip.
:::

Batches
-------

To view payslips in batches, navigate to
`Payroll app --> Payslips --> Batches`{.interpreted-text
role="menuselection"} to display all the payslip batches that have been
created. These payslip batches are displayed in a list view, by default.

Each batch displays the `Name`{.interpreted-text role="guilabel"},
`Date From`{.interpreted-text role="guilabel"} and
`Date To`{.interpreted-text role="guilabel"} dates, its
`Status`{.interpreted-text role="guilabel"}, the number of payslips in
the batch (`Payslips Count`{.interpreted-text role="guilabel"}), and the
`Company`{.interpreted-text role="guilabel"}.

{.align-center}

### Create a new batch

To create a new batch of payslips from the
`Payslips Batches`{.interpreted-text role="guilabel"} page
(`Payroll app --> Payslips --> Batches`{.interpreted-text
role="menuselection"}), click the `New`{.interpreted-text
role="guilabel"} button in the top-left corner. Doing so reveals a blank
payslip batch form on a separate page.

On the new payslip batch form, enter the `Batch Name`{.interpreted-text
role="guilabel"}.

Next, select the date range to which the batch applies. Click into one
of the `Period`{.interpreted-text role="guilabel"} fields, and a
calendar pop-up window appears. From this calendar pop-up window,
navigate to the correct month, and click on the corresponding day for
both the start and end dates of the batch.

The current company populates the `Company`{.interpreted-text
role="guilabel"} field. If operating in a multi-company environment, it
is **not** possible to modify the `Company`{.interpreted-text
role="guilabel"} from the form. The batch **must** be created while in
the database for the desired company.

{.align-center}

### Process a batch {#payroll/batch-process}

Click on an individual batch to view the details for that batch on a
separate page. On this batch detail page, different options (buttons)
appear at the top, depending on the status of the batch:

-   `New`{.interpreted-text role="guilabel"} status: batches without any
    payslips added to them have a status of `New`{.interpreted-text
    role="guilabel"}. The following button options appear for these
    batches:

    > {.align-center}
    >
    > -   `Add Payslips`{.interpreted-text role="guilabel"}: click the
    >     `Add Payslips`{.interpreted-text role="guilabel"} button to
    >     add payslips to the batch, and an
    >     `Add Payslips`{.interpreted-text role="guilabel"} pop-up
    >     window appears. Only payslips that can be added to the batch
    >     (payslips not currently part of a batch) appear on the list.
    >
    >     Select the desired payslips by clicking the checkbox to the
    >     left of each payslip name, then click the
    >     `Select`{.interpreted-text role="guilabel"} button to add them
    >     to the batch. Once payslips are selected and added to the
    >     batch, the status changes to `Confirmed`{.interpreted-text
    >     role="guilabel"}.
    >
    > -   `Generate Payslips`{.interpreted-text role="guilabel"}: after
    >     payslips have been added to the batch, click the
    >     `Generate Payslips`{.interpreted-text role="guilabel"} button
    >     to process the payslips and create individual payslips in the
    >     database.
    >
    >     A `Generate Payslips`{.interpreted-text role="guilabel"}
    >     pop-up window appears. If only a specific `Salary
    >     Structure`{.interpreted-text role="guilabel"} and/or specific
    >     `Department`{.interpreted-text role="guilabel"} is desired to
    >     make payslips for, select them from the corresponding
    >     drop-down menus. If no selections are made, then all payslips
    >     listed in the pop-up window are processed as usual.
    >
    >     Click the `Generate`{.interpreted-text role="guilabel"} button
    >     to create the payslips. The
    >     `Generate Payslips`{.interpreted-text role="guilabel"} button
    >     changes to a `Create Draft Entry`{.interpreted-text
    >     role="guilabel"} button, and the status changes to
    >     `Confirmed`{.interpreted-text role="guilabel"}.

-   `Confirmed`{.interpreted-text role="guilabel"} status: batches that
    have been created and have payslips in them, but the payslips have
    *not* been processed, have a status of `Confirmed`{.interpreted-text
    role="guilabel"}. The following two button options appear for these
    batches:

    {.align-center}

    -   `Create Draft Entry`{.interpreted-text role="guilabel"}: click
        the `Create Draft Entry`{.interpreted-text role="guilabel"}
        button to confirm the individual payslips (and the batch), and
        create a draft of the payslips. The batch now has a status of
        `Done`{.interpreted-text role="guilabel"}.
    -   `Set to Draft`{.interpreted-text role="guilabel"}: if at any
        point the batch needs to be reverted back to a status of
        `New`{.interpreted-text role="guilabel"}, click the
        `Set to Draft`{.interpreted-text role="guilabel"} button. This
        action does **not** remove any payslips that have already been
        added to the batch.

-   `Done`{.interpreted-text role="guilabel"} status: batches with
    confirmed payslips in them have a status of `Done`{.interpreted-text
    role="guilabel"}. The following button options appear for these
    batches:

    {.align-center}

    -   `Create Payment Report`{.interpreted-text role="guilabel"}:
        click the `Create Payment Report`{.interpreted-text
        role="guilabel"} button, and a
        `Select a bank journal`{.interpreted-text role="guilabel"}
        pop-up window appears. Select the correct bank journal from the
        drop-down menu.

        The batch name appears in the `File name`{.interpreted-text
        role="guilabel"} field, but this can be modified, if desired.
        Finally, click `Confirm`{.interpreted-text role="guilabel"} to
        process the payslips, and pay the employees.

    -   `Mark as paid`{.interpreted-text role="guilabel"}: after the
        payments have been created via the `Create Payment
        Report`{.interpreted-text role="guilabel"} button, the payslips
        need to be marked as paid in the database.

        Click the `Mark as paid`{.interpreted-text role="guilabel"}
        button, and the status of the batch changes to
        `Paid`{.interpreted-text role="guilabel"}.

    -   `Set to Draft`{.interpreted-text role="guilabel"}: if at any
        point the batch needs to be reverted back to a status of
        `New`{.interpreted-text role="guilabel"}, click the
        `Set to Draft`{.interpreted-text role="guilabel"} button. This
        action does **not** remove any payslips that have already been
        added to the batch.

-   `Paid`{.interpreted-text role="guilabel"} status: batches that have
    been completed have a status of `Paid`{.interpreted-text
    role="guilabel"}. No other button options appear for this status.

    {.align-center}

On the batch detail page, the individual payslips in the batch are
accessible, via the `Payslips`{.interpreted-text role="guilabel"} smart
button, located above the batch information, in the center. Click the
`Payslips`{.interpreted-text role="guilabel"} smart button to view a
list of all the individual payslips.

Use the breadcrumb menu to navigate back to the individual batch detail
page, or back to the list of all batches.

### Generate warrant payslips

Commissions are paid to employees in Odoo using *warrant payslips*.

Warrant payslips can be generated directly from the
`Payslips Batches`{.interpreted-text role="guilabel"} page
(`Payroll app --> Payslips --> Batches`{.interpreted-text
role="menuselection"}).

First, select the desired batches by clicking the box to the left of
each batch for which commission payslips should be created. Next, click
the `Generate Warrant Payslips`{.interpreted-text role="guilabel"}
button at the top of the page.

Doing so reveals a `Generate Warrant Payslips`{.interpreted-text
role="guilabel"} pop-up window, in which the necessary information
**must** be filled out.

{.align-center}

In this pop-up window, click on the drop-down menus, located beside the
`Period`{.interpreted-text role="guilabel"} field, to reveal calendar
pop-up windows. On these calendar pop-up windows, select the desired
period for which the payslips are being generated. Using the
`< (left)`{.interpreted-text role="guilabel"} and
`> (right)`{.interpreted-text role="guilabel"} arrow icons, navigate to
the correct month, and click on the date to select it.

In the `Department`{.interpreted-text role="guilabel"} field, select the
desired department from the drop-down menu.

When a department is selected, the employees listed for that department
appear in the `Employee`{.interpreted-text role="guilabel"} section.

Under the `Employee`{.interpreted-text role="guilabel"} section, enter
the `Commission Amount`{.interpreted-text role="guilabel"} for each
employee in the far-right column. To remove an employee, click the
`🗑️ (trash)`{.interpreted-text role="guilabel"} icon to remove the line.

Add a new entry by clicking `Add a Line`{.interpreted-text
role="guilabel"}, and entering the `Employee`{.interpreted-text
role="guilabel"} and the appropriate
`Commission Amount`{.interpreted-text role="guilabel"}.

Click the `Upload your file`{.interpreted-text role="guilabel"} button
to add a file, if necessary. Any file type is accepted.

Once all the commissions are properly entered, click the
`Generate Payslips`{.interpreted-text role="guilabel"} button to create
the warrant payslips in a batch.

`Process the batch <payroll/batch-process>`{.interpreted-text
role="ref"} in the same way as a typical batch to complete the payment
process.
