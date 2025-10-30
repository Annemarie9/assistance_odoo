# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll/work_entries.md

Work entries
============

Work entries are created automatically in the *Payroll* app, based on
the employee\'s `salary
structure type <payroll/structure-types>`{.interpreted-text role="ref"},
and from the *Planning*, *Attendances*, and *Time Off* applications.

The *Work Entries* dashboard of the *Payroll* application provides a
visual overview of the individual work entries for every employee.

To open the dashboard, navigate to
`Payroll app --> Work Entries --> Work Entries`{.interpreted-text
role="menuselection"}.

On the `Work Entry`{.interpreted-text role="guilabel"} dashboard, work
entries appear in alphabetical order, based on the first name of the
employees. The entire month is displayed, with the current day
highlighted in pale yellow.

If any entries have `conflicts <payroll/conflicts>`{.interpreted-text
role="ref"} that need to be resolved, the dashboard defaults to filter
only the `Conflicting`{.interpreted-text role="guilabel"} entries.

To remove the filter from the `Search...`{.interpreted-text
role="guilabel"} bar to view all work entries, click the
`✖️ (remove)`{.interpreted-text role="guilabel"} icon on the
`Conflicting`{.interpreted-text role="guilabel"} filter in the
`Search...`{.interpreted-text role="guilabel"} bar, and all work entries
appear in the list.

{.align-center}

::: {#payroll/adjust-view}
To change the view, so only the entries for a single day, week, or month
are shown, click on `Month`{.interpreted-text role="guilabel"}. A
drop-down menu appears with the options of `Day`{.interpreted-text
role="guilabel"}, `Week`{.interpreted-text role="guilabel"}, or
`Month`{.interpreted-text role="guilabel"}. Click on one of the options
to only display data for that specific selection.
:::

Use the `⬅️ (left arrow)`{.interpreted-text role="guilabel"} and
`➡️ (right arrow)`{.interpreted-text role="guilabel"} icons on the left
and right side of the `Month`{.interpreted-text role="guilabel"} button
to adjust the displayed dates. The arrows adjust the date based on the
type of time selected.

For example, if `Month`{.interpreted-text role="guilabel"} is selected,
the arrows move one month with each click of the arrow. If
`Week`{.interpreted-text role="guilabel"} or `Day`{.interpreted-text
role="guilabel"} is selected, the time moves by either a week or a day
for each click of the arrow, respectively.

At any point, to return to a view containing the current day, click the
`Today`{.interpreted-text role="guilabel"} button.

Add a new work entry {#payroll/new-work-entry}
--------------------

If a work entry is missing and needs to be added, such as sick time, or
if an employee forgot to clock in and out for a shift, click
`New`{.interpreted-text role="guilabel"} on the
`Work Entry`{.interpreted-text role="guilabel"} dashboard, to create a
new work entry.

A `Create`{.interpreted-text role="guilabel"} work entry pop-up form
appears.

Enter the following information on the form:

-   `Description`{.interpreted-text role="guilabel"}: enter a short
    description for the work entry, such as [Sick Time]{.title-ref}. If
    this field is left blank, it automatically populates once an
    employee is selected. The default entry is [Attendance:
    (Employee)]{.title-ref}.

-   `Employee`{.interpreted-text role="guilabel"}: select the employee
    the work entry is for, using the drop-down menu.

-   `Work Entry Type`{.interpreted-text role="guilabel"}: select the
    `work entry type <payroll/work-entries>`{.interpreted-text
    role="ref"} using the drop-down menu.

-   `From`{.interpreted-text role="guilabel"} and `To`{.interpreted-text
    role="guilabel"}: enter the start (`From`{.interpreted-text
    role="guilabel"}) and end (`To`{.interpreted-text role="guilabel"})
    dates and times for the work entry.

    First, click on either the `From`{.interpreted-text role="guilabel"}
    or `To`{.interpreted-text role="guilabel"} line to reveal a calendar
    pop-up window. Select the date by navigating to the correct month
    and year, using the `< (left
    arrow)`{.interpreted-text role="guilabel"} and
    `> (right arrow)`{.interpreted-text role="guilabel"} icons, then
    click on the specific day.

    Next, select the time, by clicking on either the hour or minute
    fields at the bottom of the calendar, and select the desired time
    for both the hour and minutes.

    When the date and time are correct for the entry, click the
    `Apply`{.interpreted-text role="guilabel"} button.

-   `Duration`{.interpreted-text role="guilabel"}: displays the hours
    based on the `To`{.interpreted-text role="guilabel"} and
    `From`{.interpreted-text role="guilabel"} entries. Modifying this
    field modifies the `To`{.interpreted-text role="guilabel"} field
    (the `From`{.interpreted-text role="guilabel"} field does not
    change).

Once the desired information is entered, click
`Save & Close`{.interpreted-text role="guilabel"} to save the entry, and
close the pop-up form.

{.align-center}

Conflicts {#payroll/conflicts}
---------

A conflict appears for any request that has not been approved, such as
sick time or vacation, or if there are any errors on the work entry,
such as required fields being left blank. Conflicts are required to be
resolved before payslips can be generated.

Any work entry that has a conflict to be resolved is indicated on the
main `Work Entry`{.interpreted-text role="guilabel"} dashboard, which
can be accessed by navigating to `Payroll app --> Work Entries -->
Work Entries`{.interpreted-text role="menuselection"}. Only conflicts
needing resolution are shown by default.

Conflicts are indicated with an orange triangle in the top-left corner
of each individual work entry. Click on an individual work entry to see
the date and time for the specific work entry, then click
`Edit`{.interpreted-text role="guilabel"} to view the conflict details
in a pop-up window.

{.align-center}

The conflict is briefly explained in an orange text box in the
`Open`{.interpreted-text role="guilabel"} pop-up window that appears.

The `Description`{.interpreted-text role="guilabel"},
`Employee`{.interpreted-text role="guilabel"}, and
`Work Entry Type`{.interpreted-text role="guilabel"} are listed on the
left side of the pop-up window. The `From`{.interpreted-text
role="guilabel"} and `To`{.interpreted-text role="guilabel"} date and
time range, as well as the total time (in hours) in the
`Duration`{.interpreted-text role="guilabel"} field, appears on the
right side.

If the conflict is due to a time off request that has not been approved
yet, a `Time Off`{.interpreted-text role="guilabel"} field appears on
the left side, with the type of time off requested in the description.

{.align-center}

### Time off conflicts

The most common work entry conflicts are for time off requests that have
been submitted, but not yet approved, which results in duplicate work
entries for that employee (one for time off and another for regular
work).

If there is a conflict because a time off request is in the system for
the same time that a regular work entry already exists, the time off
request is entered in the `Time Off`{.interpreted-text role="guilabel"}
field.

The time off conflict can be resolved either on the work entry pop-up
window, or on a detailed time off request pop-up window.

#### Resolve on work entry

To resolve the time off conflict on this work entry pop-up window, click
the `Approve Time
Off`{.interpreted-text role="guilabel"} button to approve the time off
request, and resolve the work entry conflict.

The `Approve Time Off`{.interpreted-text role="guilabel"} and
`Refuse Time Off`{.interpreted-text role="guilabel"} buttons disappear.
Click the `Save & Close`{.interpreted-text role="guilabel"} button to
close the pop-up window. The conflict disappears from the
`Work Entry`{.interpreted-text role="guilabel"} dashboard, since the
conflict is resolved.

#### Resolve on time off request

To resolve the time off conflict on the detailed time off request pop-up
window, click the `Internal Link`{.interpreted-text role="guilabel"}
button at the end of the `Time Off`{.interpreted-text role="guilabel"}
entry line, and the time off request details appear in a new pop-up
window. The request can be modified, if needed.

Click the `Approve`{.interpreted-text role="guilabel"} button to approve
the request, then click the `Save & Close`{.interpreted-text
role="guilabel"} button to save the changes, and go back to the work
entry conflict pop-up window.

{.align-center}

Now, the `Approve Time Off`{.interpreted-text role="guilabel"} button is
hidden, only the `Refuse Time Off`{.interpreted-text role="guilabel"}
button is visible.

If the approval was a mistake, the request can be refused here, by
clicking the `Refuse
Time Off`{.interpreted-text role="guilabel"} button.

Since the time off was approved in the time off window, click the
`X`{.interpreted-text role="guilabel"} in the top-right corner to close
the window. The conflict disappears from the
`Work Entry`{.interpreted-text role="guilabel"} dashboard, since it has
been resolved.

Regenerate work entries {#payroll/regenerate-work-entries}
-----------------------

When regenerating work entries, any manual changes, such as resolved
conflicts, are overwritten, and work entries are regenerated (or
recreated) from the applications that created them.

This method for correcting a large amount of conflicts is recommended to
keep all records correct. While
`conflicts <payroll/conflicts>`{.interpreted-text role="ref"} *can* be
resolved individually, if the conflicts are caused from another
application, it is best practice to ensure the records in the other
applications are also correct. That is why it is recommended to resolve
these conflicts in the applications that created the conflict.

Another reason this method is recommended is because, when work entries
are regenerated, the conflicts reappear, if the issue in the related
application is **not** resolved.

First, ensure the issues are resolved in the specific applications that
caused the work entry conflicts.

Next, click the `Regenerate Work Entries`{.interpreted-text
role="guilabel"} button at the top of the `Work
Entries`{.interpreted-text role="guilabel"} dashboard, and a
`Work Entry Regeneration`{.interpreted-text role="guilabel"} pop-up
window appears.

Select the `Employees`{.interpreted-text role="guilabel"} to regenerate
work entries for from the drop-down menu, and adjust the
`From`{.interpreted-text role="guilabel"} and `To`{.interpreted-text
role="guilabel"} fields, so the correct date range is displayed.

Click the `Regenerate Work Entries`{.interpreted-text role="guilabel"}
button, and the work entries are recreated. Once finished, the pop-up
window closes.

{.align-center}

::: {.example}
An employee has incorrect work entries generated from the *Planning* app
because they were incorrectly assigned to two work stations
simultaneously. This should be fixed in the *Planning* app, instead of
the *Payroll* app.

To correct this issue, modify the employee\'s schedule in the *Planning*
app, so they are correctly assigned to only one work station. Then, in
the *Payroll* app, regenerate work entries for that employee, for that
specific time period.

The *Payroll* app then pulls the new, corrected data form the *Planning*
app, and recreates the correct work entries for that employee. All
conflicts for that employee are now resolved.
:::

Generating payslips
-------------------

To generate payslips,
`navigate to the time period <payroll/adjust-view>`{.interpreted-text
role="ref"} the payslips should be generated for. Ensure the
`Conflicting`{.interpreted-text role="guilabel"} filter is removed. When
the desired pay period is displayed, click the
`Generate Payslips`{.interpreted-text role="guilabel"} button.

::: {.tip}
::: {.title}
Tip
:::

If the `Generate Payslips`{.interpreted-text role="guilabel"} button is
not active (appears pale purple, instead of dark purple), that indicates
there are conflicts, or the date selected includes dates in the future.
Resolve all conflicts before generating payslips.
:::

When the `Generate Payslips`{.interpreted-text role="guilabel"} button
is clicked, a batch entry appears on a separate page for the time period
selected.

The batch name populates the `Batch Name`{.interpreted-text
role="guilabel"} field in a default [From (date) to (date)]{.title-ref}
format.

The date range to which the payslips apply appears in the
`Period`{.interpreted-text role="guilabel"} field, and the company
appears in the `Company`{.interpreted-text role="guilabel"} field. It is
**not** possible to make changes to this form.

Click the `Create Draft Entry`{.interpreted-text role="guilabel"} button
to create the payslips for the batch.

Click the `Payslips`{.interpreted-text role="guilabel"} smart button at
the top of the page to view all the payslips for the batch.

{.align-center}

### Printing payslips

To print payslips, first view the individual payslips by clicking the
`Payslips`{.interpreted-text role="guilabel"} smart button on the batch
form.

Next, select the payslips to print from the `Payslips`{.interpreted-text
role="guilabel"} list. Click the box next to each payslip to print, or
click the box to the left of the `Reference`{.interpreted-text
role="guilabel"} column title, to select all the payslips in the list at
once.

Click the `Print`{.interpreted-text role="guilabel"} button, and a PDF
file is created with all the specified payslips.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The `Print`{.interpreted-text role="guilabel"} button does **not**
appear until at least one payslip is selected in the list.
:::

Time off to report
------------------

If a time off request is submitted for a time period that was already
processed on a payslip, the time off request appears in the *Time Off*
page in the *Payroll* app, which is accessible by navigating to
`Payroll app --> Work Entries --> Time Off to Report`{.interpreted-text
role="menuselection"}.

On the `Time Off`{.interpreted-text role="guilabel"} page, the request
appears with a status of `To defer to next
payslip`{.interpreted-text role="guilabel"}. This is because the
employee was already paid for that day, and it was logged as time spent
at work, as a typical work day.

In order to keep the employee\'s time off balances correct, the time off
request **must** be applied to the following pay period. This not only
ensures time off request balances are current, it also eliminates the
need to redo work entries, cancel paychecks, and reissue paychecks.

The most common scenario when this situation occurs, is when payslips
are processed a day or two before the pay period ends, and an employee
is unexpectedly sick on one of the last days of the pay period. The
employee puts in a time off request for a day that was already processed
on a payslip as a regular work day. Instead of canceling the payslip,
modifying the work entries, and reissuing the paycheck, Odoo allows for
those time off requests to be applied to the following pay period,
instead.

To view all the time off requests that need to be deferred to the next
payslip, navigate to
`Payroll app --> Work Entries --> Time Off to Report`{.interpreted-text
role="menuselection"}. The default filter for this report is
`To Defer`{.interpreted-text role="guilabel"}.

All time off requests that need to be applied to the following pay
period appear with a `Payslip State`{.interpreted-text role="guilabel"}
of `To defer to next payslip`{.interpreted-text role="guilabel"}.

{.align-center}

### Defer multiple time off entries

To select the work entries to defer, click the box to the left of the
work entry line. To select all work entries in the list, click the box
to the left of the `Employees`{.interpreted-text role="guilabel"} column
title, at the top of the list.

Once any work entry is selected, two buttons appear at the top of the
report: a `(#)
Selected`{.interpreted-text role="guilabel"} button, and an
`Actions`{.interpreted-text role="guilabel"} button. The
`(#) Selected`{.interpreted-text role="guilabel"} button indicates how
many entries are currently selected.

When all the desired work entries are selected, click the
`Actions`{.interpreted-text role="guilabel"} button, and a menu appears
with several choices. Click `Defer to Next Month`{.interpreted-text
role="guilabel"} in the list, and all selected entries are deferred to
the following month.

{.align-center}

### Defer individual time off entries

Time off requests appearing on the
`Time Off to Report`{.interpreted-text role="guilabel"} list can be
deferred individually.

Click on an individual time off request, and the details for that
request load.

The specific details for the time off request appear on the left-hand
side, and all of the employee\'s submitted time off requests appear on
the right-hand side (including the request in the details on the
left-hand side).

To defer the time off request to the next payslip, click the
`Report to Next Month`{.interpreted-text role="guilabel"} button at the
top. Once processed, the `Report to Next Month`{.interpreted-text
role="guilabel"} button disappears, and the
`Payslip State`{.interpreted-text role="guilabel"} changes from
`To defer to next payslip`{.interpreted-text role="guilabel"} to
`Computed
in Current Payslip`{.interpreted-text role="guilabel"}.

To go back to the `Time Off to Report`{.interpreted-text
role="guilabel"} list, click on `Time Off`{.interpreted-text
role="guilabel"} in the breadcrumb menu.

{.align-center}

::: {.seealso}
`Configure work entries <payroll/work-entries-config>`{.interpreted-text
role="ref"}
:::
