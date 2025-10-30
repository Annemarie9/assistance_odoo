# File: /content/odoo_doc17.0/fr/content/applications/hr/attendances.md

show-content

:   

Attendances
===========

Odoo\'s *Attendances* application functions as a time clock. Employees
are able to check in and out of work using a dedicated device in kiosk
mode, while users are also able to check in and out of work directly
from the database. Managers can quickly see who is available at any
given time, create reports to see everyone\'s hours, and gain insights
on which employees are working overtime, or checking out of work earlier
than expected.

Access rights {#attendances/access-rights}
-------------

It is important to understand how the different access rights affect
what options and features users can access in the *Attendances*
application.

Every user in the database is able to check in and out directly from the
database, without needing access to the *Attendances* application.
Additionally, all users can access their own attendance records from
their employee form in the *Employees* app.

Access to both the *Attendances* application, and the various features
within the application is determined by access rights.

To see what access rights a user has, navigate to the
`Settings app --> Users &
Companies: Users`{.interpreted-text role="menuselection"}, and click on
an individual user. The `Access Rights`{.interpreted-text
role="guilabel"} tab is visible by default. Scroll down to the
`Human Resources`{.interpreted-text role="guilabel"} section to see the
setting. For the `Attendances`{.interpreted-text role="guilabel"} field,
the options are either to leave the field blank or select
`Administrator`{.interpreted-text role="guilabel"}.

If the `Administrator`{.interpreted-text role="guilabel"} option is
selected, the user has full access to the entire *Attendances*
application, with no restrictions. They can view all employee attendance
records, enter *Kiosk mMode* from the application, access all reporting
metrics, and make modifications to the settings. If left blank, the user
does **not** have access to the *Attendances* application.

### Approvers {#attendances/approvers}

The **only** other scenario where different information may be
accessible in the *Attendances* application is for approvers. If a user
does *not* have administrative rights for the *Attendances* application,
but they are set as an employee\'s approver for the *Attendances*
application, that user is able to view the attendance records for that
specific employee, as well as make modifications to that employee\'s
attendance records, if necessary. This applies to all employees for whom
the user is listed as the *Attendances* application approver. Approvers
are typically managers, though this is not required.

To see who the attendance approver is for an employee, navigate to the
`Employees
application`{.interpreted-text role="menuselection"} and click on the
specific employee. Click on the `Work Information`{.interpreted-text
role="guilabel"} tab, scroll to the `Approvers`{.interpreted-text
role="guilabel"} section, and check the `Attendance`{.interpreted-text
role="guilabel"} field. The person selected is able to view that
employees\' attendance records, both on the *Attendances* application
dashboard as well as in the attendance reports, and make modifications
to their records.

Configuration
-------------

Few configurations are needed in the *Attendances* application.
Determining how employees check in and out, defining how the kiosks
function, and determining how extra hours are computed are all set in
the Configuration menu. Navigate to the `Attendances application -->
Configuration`{.interpreted-text role="menuselection"} to access the
configuration menu.

### Modes

-   `Attendances from Backend`{.interpreted-text role="guilabel"}:
    activate this selection to allow users to check in and out directly
    from the Odoo database. If this is not activated, users must use a
    kiosk to check in and out of work.

### Extra hours

This section specifies how extra time is calculated, including when
extra time is counted and what time is not logged.

-   `Count of Extra Hours`{.interpreted-text role="guilabel"}: enable
    this box to allow employees to log extra hours beyond their set
    working hours (sometimes referred to as *overtime*). Activating this
    selection displays the following settings as well. If this is not
    activated, no other configurations appear.
    -   `Start From`{.interpreted-text role="guilabel"}: the current
        date is automatically entered in this field. If desired, click
        on this field and use the calendar selector to modify the start
        date on which extra hours are logged.

    -   `Tolerance Time In Favor Of Company`{.interpreted-text
        role="guilabel"}: enter the amount of time, in minutes, that is
        **not** counted towards an employee\'s overtime. When an
        employee checks out, and the extra time logged is below the
        specified minutes, the extra time is **not** counted as overtime
        for the employee.

    -   `Tolerance Time In Favor Of Employee`{.interpreted-text
        role="guilabel"}: enter the amount of time, in minutes, that an
        employee is given, that does **not** adversely affect their
        attendance if they log less time than their working hours. When
        an employee checks out, and the total time logged for the day is
        less than their specified working hours and less than this
        specified grace period, they are **not** penalized for their
        reduced hours.

        ::: {.example}
        A company sets both of the `Tolerance`{.interpreted-text
        role="guilabel"} fields to [15]{.title-ref} minutes, and the
        working hours for the entire company are set from 9:00 AM to
        5:00 PM.

        If an employee checks in at 9:00 AM, and checks out at 5:14 PM,
        the extra 14 minutes are **not** counted towards their overtime.

        If an employee checks in at 9:05 AM, and checks out at 4:55 PM,
        even though they logged a total of 10 minutes less than their
        full working hours, they are **not** penalized for this
        discrepancy.
        :::

    -   `Display Extra Hours`{.interpreted-text role="guilabel"}:
        activate this box to display the extra hours logged by an
        employee when they check out with a kiosk, or when a user checks
        out in the database.

::: {.note}
::: {.title}
Note
:::

Employees are still able to log overtime hours even if the
`Count of Extra Hours`{.interpreted-text role="guilabel"} option is not
activated. The difference is that when
`Count of Extra Hours`{.interpreted-text role="guilabel"} is activated,
the extra hours can be `deducted from an approved time off request
<time_off/deduct-extra-hours>`{.interpreted-text role="ref"}.
:::

Overview
--------

When entering the *Attendances* application, the
`Overview`{.interpreted-text role="guilabel"} dashboard is presented,
containing all the check in and check out information for the signed in
user. If the user has specific
`access rights <attendances/access-rights>`{.interpreted-text
role="ref"} and/or are `approvers
<attendances/approvers>`{.interpreted-text role="ref"} for specific
employees, then those additional employee\'s check in and check out
information is also visible on the `Overview`{.interpreted-text
role="guilabel"} dashboard.

### Views

To change the view from the default Gantt chart to a list view, click
the `List`{.interpreted-text role="guilabel"} icon in the top right of
the dashboard, beneath the user\'s photo. To switch back to the Gantt
chart, click the `Gantt`{.interpreted-text role="guilabel"} button,
located next to the `List`{.interpreted-text role="guilabel"} button.

The default view presents the current day\'s information. To present the
information for the `Week`{.interpreted-text role="guilabel"},
`Month`{.interpreted-text role="guilabel"}, or `Year`{.interpreted-text
role="guilabel"}, click on the `Day`{.interpreted-text role="guilabel"}
button to reveal a drop-down, displaying those other options. Select the
desired view, and the dashboard updates, presenting the selected
information. To change the `Day`{.interpreted-text role="guilabel"},
`Week`{.interpreted-text role="guilabel"}, `Month`{.interpreted-text
role="guilabel"}, or `Year`{.interpreted-text role="guilabel"}
presented, click the `← (left arrow)`{.interpreted-text role="guilabel"}
or `→ (right arrow)`{.interpreted-text role="guilabel"} buttons on
either side of the drop-down menu. To jump back to a view containing the
current day, click the `Today`{.interpreted-text role="guilabel"}
button. This refreshes the dashboard, presenting information containing
the current day\'s information.

In the `Day`{.interpreted-text role="guilabel"} view, the column for the
current hour is highlighted in yellow. If the `Week`{.interpreted-text
role="guilabel"} or `Month`{.interpreted-text role="guilabel"} view is
selected, the column for the current day is highlighted. If the
`Year`{.interpreted-text role="guilabel"} view is selected, the current
month is highlighted.

![The overview dashboard presenting the information for the week, with the current day
highlighted.](attendances/overview.png){.align-center}

Any entries that have errors appear in red, indicating they need to be
resolved by a user with the proper
`access rights <attendances/access-rights>`{.interpreted-text
role="ref"} and/or are `approvers
<attendances/approvers>`{.interpreted-text role="ref"} for the
employee(s) with the errors.

### Filters and groups {#attendances/filters-groups}

To filter the results in the overview dashboard, or to present different
groups of information, click the
`🔻 (triangle drop down)`{.interpreted-text role="guilabel"} button in
the right side of the `Search`{.interpreted-text role="guilabel"} bar
above the dashboard, and select one of the available
`Filters`{.interpreted-text role="guilabel"} or
`Group By`{.interpreted-text role="guilabel"} options. There are several
pre-configured filters and groups to choose from, as well as an option
to create custom ones.

#### Filters

The default filters that can be selected are:

-   `My Attendances`{.interpreted-text role="guilabel"}: this filter
    only presents the user\'s attendance data.
-   `My Team`{.interpreted-text role="guilabel"}: this filter presents
    the attendance data for the user\'s team.
-   `At Work`{.interpreted-text role="guilabel"}: this filter displays
    the attendance data for everyone currently checked in.
-   `Errors`{.interpreted-text role="guilabel"}: this filter displays
    any entries with `errors <attendances/errors>`{.interpreted-text
    role="ref"} that need to be resolved.
-   `Check In`{.interpreted-text role="guilabel"}: this filter has a
    drop-down to further select a specific time period. Select the
    desired time period from the options presented, a specific month,
    quarter, or year.
-   `Last 7 days`{.interpreted-text role="guilabel"}: this filter
    presents the attendance data for the last seven days.
-   `Add Custom Filter`{.interpreted-text role="guilabel"}: create a
    custom filter using the pop-up that appears when this is selected.

#### Groups

The default groups that can be selected are:

-   `Check In`{.interpreted-text role="guilabel"}: this grouping
    presents a drop-down menu containing the following time period
    options: `Year`{.interpreted-text role="guilabel"},
    `Quarter`{.interpreted-text role="guilabel"},
    `Month`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, and `Day`{.interpreted-text role="guilabel"}.
    Selected the time period to display all the check-in information,
    grouped by the selected time period.
-   `Employee`{.interpreted-text role="guilabel"}: this group presents
    the attendance data organized by employee.
-   `Check Out`{.interpreted-text role="guilabel"}: this grouping
    presents a drop-down menu containing the following time period
    options: `Year`{.interpreted-text role="guilabel"},
    `Quarter`{.interpreted-text role="guilabel"},
    `Month`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, and `Day`{.interpreted-text role="guilabel"}.
    Selected the time period to display all the check-out information,
    grouped by the selected time period.
-   `Add Custom Group`{.interpreted-text role="guilabel"}: this option
    displays a drop-down menu with a variety of options to group the
    attendance data by, including `City`{.interpreted-text
    role="guilabel"}, `Country`{.interpreted-text role="guilabel"},
    `Mode`{.interpreted-text role="guilabel"}, and
    `IP Address`{.interpreted-text role="guilabel"}.

### Attendance log details {#attendances/errors}

Odoo captures various time and location details when a user checks in
and out. The specific details provided are determined by the method the
user checked in and out.

To view the specific check in and/or check out details for an employee,
click on an individual entry in the overview dashboard.

A detailed attendance log for the user appears in a pop-up window. To
close the detailed attendance log, click the
`Save & Close`{.interpreted-text role="guilabel"} button in the
bottom-left corner of the form.

The detailed attendance log contains the following information:

#### Main details

-   `Employee`{.interpreted-text role="guilabel"}: the name of the
    employee.
-   `Check In`{.interpreted-text role="guilabel"}: the date and time the
    employee checked in.
-   `Check Out`{.interpreted-text role="guilabel"}: the date and time
    the employee checked out. This only appears if the employee has
    checked out.
-   `Worked Hours`{.interpreted-text role="guilabel"}: the total amount
    of time the employee logged for the day, in an hour and minute
    format (HH:MM). This value calculates all the checks in and check
    outs for the day, if the employee checked in and out multiple times.
-   `Extra Hours`{.interpreted-text role="guilabel"}: any extra hours
    the employee logged that is beyond their expected working hours.

#### Check in/check out details

The following information appears for both the
`Check In`{.interpreted-text role="guilabel"} and
`Check Out`{.interpreted-text role="guilabel"} sections.

-   `Mode`{.interpreted-text role="guilabel"}: the method with which the
    attendance information was gathered. `Systray`{.interpreted-text
    role="guilabel"} is displayed if the employee logged in and out
    `directly from the
    database <attendances/check-in>`{.interpreted-text role="ref"},
    `Manual`{.interpreted-text role="guilabel"} is displayed if the
    employee logged in and out
    `using an attendance kiosk <attendances/kiosk-mode-entry>`{.interpreted-text
    role="ref"}.
-   `IP Address`{.interpreted-text role="guilabel"}: the IP address for
    the computer the employee used to log in or out.
-   `Browser`{.interpreted-text role="guilabel"}: the web browser the
    employee used to log in or out.
-   `Localization`{.interpreted-text role="guilabel"}: the city and
    country associated with the computer\'s IP address.
-   `GPS Coordinates`{.interpreted-text role="guilabel"}: the specific
    coordinates when the user logged in or out. To view the specific
    coordinates on a map, click the `→ View on Maps`{.interpreted-text
    role="guilabel"} button beneath the
    `GPS Coordinates`{.interpreted-text role="guilabel"}. This opens a
    map in a new browser tab, with the specific location pointed out.

{.align-center}

### Errors

Entries that contain an error appear on the overview dashboard in red.
In the `Gantt
view`{.interpreted-text role="guilabel"}, the entry appears with a red
background. If in the `List view`{.interpreted-text role="guilabel"},
the entry text appears in red.

An error typically occurs when an employee has checked in but has not
checked out within the last 24 hours, or when an employee has a check in
and check out period spanning over 16 hours.

To fix the error, the attendance entry must be modified or deleted.
Click on the entry to reveal a pop-up containing the details for that
particular entry. To modify the `Check In`{.interpreted-text
role="guilabel"} and/or `Check Out`{.interpreted-text role="guilabel"}
information, click on the `Check In`{.interpreted-text role="guilabel"}
or `Check Out`{.interpreted-text role="guilabel"} field and a calendar
selector appears. Click on the desired date, then use the time selector
beneath the calendar to select the specific time for the entry. When the
information is correct, click `Apply.`{.interpreted-text
role="guilabel"}

![The pop-up that allows for modifications to an attendance entry with an error. The calendar
selector is shown, and the time selector is highlighted.](attendances/errors.png){.align-center}

When all the information on the pop-up is correct, click
`Save & Close`{.interpreted-text role="guilabel"}. When the entry no
longer has an error, the entry appears in gray instead of red.

To delete an entry, click `Remove`{.interpreted-text role="guilabel"} on
the pop-up instead of making modifications to the entry.

Reporting
---------

To view attendance reports, click `Reporting`{.interpreted-text
role="guilabel"} in the top menu. The default report displays each
employee\'s attendance information for the past 3 months, in a
`Line Chart`{.interpreted-text role="guilabel"}.

The default view is a `Graph`{.interpreted-text role="guilabel"}. To
view the data in a pivot table, click the
`Pivot Table`{.interpreted-text role="guilabel"} button on the top right
of the report. To switch back to the graph view, click the
`Graph`{.interpreted-text role="guilabel"} button, located next to the
`Pivot Table`{.interpreted-text role="guilabel"} button.

To present different information, adjust the
`filters and groups <attendances/filters-groups>`{.interpreted-text
role="ref"} in the same way as in the `Overview`{.interpreted-text
role="guilabel"} dashboard.

The data can be presented in either a `Bar Chart`{.interpreted-text
role="guilabel"}, `Line Chart`{.interpreted-text role="guilabel"}, `Pie
Chart`{.interpreted-text role="guilabel"}, `Stacked`{.interpreted-text
role="guilabel"} chart, or in `Descending`{.interpreted-text
role="guilabel"} or `Ascending`{.interpreted-text role="guilabel"}
order. To change the view to any of these charts, click the
corresponding button above the displayed chart.

To change the `Measures`{.interpreted-text role="guilabel"}, click the
`Measures`{.interpreted-text role="guilabel"} button and select the
desired measure from the drop-down menu.

The report can also be inserted into a spreadsheet. Click the
`Insert in Spreadsheet`{.interpreted-text role="guilabel"} button and a
pop-up appears. Select the desired spreadsheet, and click
`Confirm`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
\- `attendances/check_in_check_out`{.interpreted-text role="doc"} -
`attendances/kiosks`{.interpreted-text role="doc"} -
`attendances/hardware`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
attendances/check\_in\_check\_out attendances/kiosks
attendances/hardware
:::
