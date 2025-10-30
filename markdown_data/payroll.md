# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll.md

show-content

:   

Payroll
=======

Odoo *Payroll* is used to process work entries and create payslips for
employees. *Payroll* works in conjunction with other Odoo apps, such as
*Employees*, *Time Off*, *Attendances*, and *Planning*.

The *Payroll* app helps ensure there are no issues or conflicts when
validating work entries. It also handles country-specific localizations
to ensure payslips follow local rules and taxes, and allows for salary
assignments.

Settings
--------

Configure the *Payroll* app by navigating to
`Payroll app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. The various settings
for accounting, localizations, time off, alerts, and payslips are
specified here.

### Accounting

The accounting section of the configuration menu relates to three
options:

-   `Payroll Entries`{.interpreted-text role="guilabel"}: enable this
    option to post payroll slips in accounting.
-   `Payroll SEPA`{.interpreted-text role="guilabel"}: enable this
    option to create SEPA payments.
-   `Batch Account Move Lines`{.interpreted-text role="guilabel"}:
    enable this option to have a single account move line created from
    all the accounting entries from the same period. This disables the
    generation of single payments.

### Localizations

*Localizations* are country-specific settings pre-configured in Odoo at
the creation of the database, which account for all taxes, fees, and
allowances for that particular country.

The `Localization`{.interpreted-text role="guilabel"} section of the
*Payroll* app `Settings`{.interpreted-text role="guilabel"} page may
include specific settings that need to be set for the specific locality.
This selection also provides a detailed view of all benefits provided to
employees.

The settings and options shown in this section varies, depending on the
localization enabled for the database.

::: {.warning}
::: {.title}
Warning
:::

It is **not** recommended to alter the localization settings, unless
specifically required.
:::

::: {.note}
::: {.title}
Note
:::

Odoo can handle a multi-company configuration. This is generally done
when there is a main company or office location, such as a headquarters,
and there are other offices/branches around the country or globe, that
fall under that main company or headquarters. In Odoo, each company,
including the headquarters, would be set up as their own company/branch
using the multi-company method.

Each individual company can have a different localization setting
configured for that specific company, since company locations can vary
and be located anywhere in the world, where rules and laws differ.

For more information on companies, refer to the
`Companies <../general/companies>`{.interpreted-text role="doc"}
documentation, which covers how to set up companies.
:::

### Time off

-   `Deferred Time Off`{.interpreted-text role="guilabel"}: if time off
    is taken after payslips are validated, the time off needs to be
    applied to the following pay period. Select the person responsible
    for validating these specific time off situations using the
    drop-down menu in the `Responsible`{.interpreted-text
    role="guilabel"} field.

    ::: {.example}
    An employee is paid on the 15th of the month and the last day of the
    month. Payslips are typically processed a day before.

    If an employee\'s payslip is approved and processed on the 30th, but
    that same employee takes an unexpected sick day on the 31st, the
    time off needs to be logged.

    Since the employee is already paid for a regular work day on the
    31st, to keep the time off balances correct, the sick day is
    moved/applied to the 1st of the next month (the next pay period).
    :::

### Payroll

-   `Contract Expiration Notice Period`{.interpreted-text
    role="guilabel"}: enter the number of `Days`{.interpreted-text
    role="guilabel"} before a contract expires, and Odoo notifies the
    responsible person about the upcoming expiration at that time.
-   `Work Permit Expiration Notice Period`{.interpreted-text
    role="guilabel"}: enter the number of `Days`{.interpreted-text
    role="guilabel"} before a work permit expires, and Odoo notifies the
    responsible person about the upcoming expiration at that time.
-   `Payslip PDF Display`{.interpreted-text role="guilabel"}: enable
    this option to have payslips display a PDF file on the payslip form.

Contracts {#payroll/work-entries-config}
---------

In order for an employee to be paid, they **must** have an active
contract for a specific type of employment. Creating and viewing
contract templates, and creating and viewing employment types, is
possible from this section of the configuration header menu.

### Templates {#payroll/contract-templates}

Contract templates are used with the *Recruitment* application when
sending an offer to a candidate. The contract template forms the basis
of an offer, and can be modified for specific candidates or employees,
when necessary. If a contract template is created or modified in the
*Payroll* application, the changes are also reflected in the
*Recruitment* application.

::: {.important}
::: {.title}
Important
:::

To access contract templates, the *Salary Configurator*
([hr\_contract\_salary]{.title-ref}) module **must** be
`installed <general/install>`{.interpreted-text role="ref"}.
:::

To view all the current contract templates in the database, navigate to
`Payroll app
--> Configuration --> Contracts: Templates`{.interpreted-text
role="menuselection"}.

On the `Contract Templates`{.interpreted-text role="guilabel"} page, all
current contract templates appear in a list view. To view the details of
a contract template, click anywhere on the line to open the contract
form. The contract template can be modified from this form. Proceed to
make any desired changes to the contract.

To create a new contract template, click the `New`{.interpreted-text
role="guilabel"} button. Then, enter the following information on the
blank contract template form that appears:

-   `Contract Reference`{.interpreted-text role="guilabel"}: enter a
    brief description for the template. This should be clear and easily
    understood, as this name appears in the *Recruitment* application,
    as well.
-   `Working Schedule`{.interpreted-text role="guilabel"}: select the
    desired working schedule the contract applies to from the drop-down
    menu. If a new working schedule is needed, create a
    `new working schedule
    <payroll/new-working-schedule>`{.interpreted-text role="ref"}.
-   `Work Entry Source`{.interpreted-text role="guilabel"}: select how
    the work entries are generated. Choices are either:
    -   `Working Schedule`{.interpreted-text role="guilabel"}: work
        entries are generated based on the selected working schedule.
    -   `Attendances`{.interpreted-text role="guilabel"}: work entries
        are generated based on the employee\'s attendance, as they are
        logged in the *Attendances* application. Refer to the
        `Attendances
        <attendances/check-in>`{.interpreted-text role="ref"}
        documentation for information on checking in and out.
    -   `Planning`{.interpreted-text role="guilabel"}: work entries are
        generated based on the employee\'s planning in the *Planning*
        application.
-   `Salary Structure Type`{.interpreted-text role="guilabel"}: select
    the `salary structure type
    <payroll/structure-types>`{.interpreted-text role="ref"} from the
    drop-down menu.
-   `Department`{.interpreted-text role="guilabel"}: select the
    department the contract template applies to from the drop-down menu.
    If blank, the template applies to all departments.
-   `Job Position`{.interpreted-text role="guilabel"}: select the
    `job position <payroll/job-positions>`{.interpreted-text role="ref"}
    the contract template applies to from the drop-down menu. If blank,
    the template applies to all job positions.
-   `Wage on Payroll`{.interpreted-text role="guilabel"}: enter the
    monthly wage in the field.
-   `Contract Type`{.interpreted-text role="guilabel"}: select the type
    of contract from the drop-down menu. This list is the same as the
    `Employment Types <payroll/employment-types>`{.interpreted-text
    role="ref"}.
-   `HR Responsible`{.interpreted-text role="guilabel"}: select the
    employee responsible for validating contracts, using this template,
    from the drop-down menu.
-   `New Contract Document Template`{.interpreted-text role="guilabel"}:
    select a default document that a new employee has to sign to accept
    an offer.
-   `Contract Update Document Template`{.interpreted-text
    role="guilabel"}: select a default document that a current employee
    has to sign to update their contract.

{.align-center}

#### Salary information tab

-   `Wage Type`{.interpreted-text role="guilabel"}: select either
    `Fixed Wage`{.interpreted-text role="guilabel"} or
    `Hourly Wage`{.interpreted-text role="guilabel"} from the drop-down
    menu.
-   `Schedule Pay`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select how often the employee is paid. Options
    include `Annually`{.interpreted-text role="guilabel"},
    `Semi-annually`{.interpreted-text role="guilabel"},
    `Quarterly`{.interpreted-text role="guilabel"},
    `Bi-monthly`{.interpreted-text role="guilabel"},
    `Monthly`{.interpreted-text role="guilabel"},
    `Semi-monthly`{.interpreted-text role="guilabel"},
    `Bi-weekly`{.interpreted-text role="guilabel"},
    `Weekly`{.interpreted-text role="guilabel"}, or
    `Daily`{.interpreted-text role="guilabel"}.
-   `Wage`{.interpreted-text role="guilabel"}: enter the gross wage. The
    time period presented in this field is based on what is selected for
    the `Scheduled Pay`{.interpreted-text role="guilabel"} field. It is
    recommended to populate the `Yearly Cost (Real)`{.interpreted-text
    role="guilabel"} field *first*, since that entry updates this field
    automatically.
-   `Yearly Cost (Real)`{.interpreted-text role="guilabel"}: enter the
    total yearly cost the employee costs the employer. When this value
    is entered, the `Monthly Cost (Real)`{.interpreted-text
    role="guilabel"} is automatically updated.
-   `Monthly Cost (Real)`{.interpreted-text role="guilabel"}: this field
    is **not** editable. The value is automatically populated after the
    `Yearly Cost (Real)`{.interpreted-text role="guilabel"} is entered.

::: {.important}
::: {.title}
Important
:::

The `Schedule Pay`{.interpreted-text role="guilabel"},
`Wage`{.interpreted-text role="guilabel"}, and
`Yearly Cost (Real)`{.interpreted-text role="guilabel"} fields are all
linked. If any of these fields are updated, the other two fields
automatically update to reflect the change. It is best practice to check
these three fields if any modifications have been made, to ensure they
are accurate.
:::

{.align-center}

#### Pre-tax benefits and post-tax deductions

Depending on the localization settings set for the company, the entries
presented in this section either vary, or may not appear at all.

For example, some entries may pertain to retirement accounts, health
insurance benefits, and commuter benefits.

Enter the monetary amounts or percentages to specify how much of the
employee\'s salary goes to the various benefits and/or deductions.

### Employment types {#payroll/employment-types}

To view all the pre-configured employment types, navigate to
`Payroll application -->
Configuration --> Contracts: Employment Types`{.interpreted-text
role="menuselection"}.

The employment types are presented in a list view on the
`Employment Types`{.interpreted-text role="guilabel"} page.

The default employment types are `Permanent`{.interpreted-text
role="guilabel"}, `Temporary`{.interpreted-text role="guilabel"},
`Seasonal`{.interpreted-text role="guilabel"},
`Interim`{.interpreted-text role="guilabel"},
`Full-Time`{.interpreted-text role="guilabel"},
`Part-Time`{.interpreted-text role="guilabel"}, and
`Permanent`{.interpreted-text role="guilabel"}.

To make a new employment type, click the `New`{.interpreted-text
role="guilabel"} button in the upper-left corner, and a blank line
appears at the bottom of the `Employment Types`{.interpreted-text
role="guilabel"} page.

On this new blank line, enter the name of the employment type in the
`Name`{.interpreted-text role="guilabel"} column. If the employment type
is country-specific, select the country using the drop-down menu in the
`Country`{.interpreted-text role="guilabel"} column. If a country is
selected, then the employment type is *only* applicable for that
specific country.

To rearrange the order of the employment types, click the
`six small gray boxes`{.interpreted-text role="guilabel"} icon to the
left of the employment type `Name`{.interpreted-text role="guilabel"},
and drag the line to the desired position on the list.

{.align-center}

Work entries {#payroll/work-entries}
------------

A *work entry* is an individual record on an employee\'s timesheet. Work
entries can be configured to account for all types of work and time off,
such as `Attendance`{.interpreted-text role="guilabel"}, `Sick Time
Off`{.interpreted-text role="guilabel"}, `Training`{.interpreted-text
role="guilabel"}, or `Public Holiday`{.interpreted-text
role="guilabel"}.

::: {.seealso}
`Manage work entries <payroll/work_entries>`{.interpreted-text
role="doc"}
:::

### Work entry types

When creating a work entry in the *Payroll* application, or when an
employee enters information in the *Timesheets* application, a
`Work Entry Type`{.interpreted-text role="guilabel"} needs to be
selected. The list of `Work Entry Types`{.interpreted-text
role="guilabel"} is automatically created based on localization settings
set in the database.

To view the current work entry types available, go to
`Payroll app --> Configuration
--> Work Entries --> Work Entry Types`{.interpreted-text
role="menuselection"}.

Each work entry type has a code to aid in the creation of payslips, and
to ensure all taxes and fees are correctly entered.

{.align-center}

#### New work entry type

To create a new `Work Entry Type`{.interpreted-text role="guilabel"},
click the `New`{.interpreted-text role="guilabel"} button, and enter the
information for the following sections on the form.

##### General information section

-   `Work Entry Type Name`{.interpreted-text role="guilabel"}: the name
    should be short and descriptive, such as [Sick Time]{.title-ref} or
    [Public Holiday]{.title-ref}.
-   `Payroll Code`{.interpreted-text role="guilabel"}: this code appears
    with the work entry type on timesheets and payslips. Since the code
    is used in conjunction with the *Accounting* application, it is
    advised to check with the accounting department for a code to use.
-   `DMFA code`{.interpreted-text role="guilabel"}: this code is used to
    identify `DMFA (De Multifunctionele Aangifte)`{.interpreted-text
    role="abbr"} entries on a corresponding
    `DMFA (De Multifunctionele Aangifte)`{.interpreted-text role="abbr"}
    report. The `DMFA
    (De Multifunctionele Aangifte)`{.interpreted-text role="abbr"}
    report is a quarterly report that Belgian-based companies are
    required to submit for social security reporting purposes. This
    report states the work done by the employees during the quarter, as
    well as the salaries paid to those employees.
-   `External Code`{.interpreted-text role="guilabel"}: this code is
    used for exporting data to a third-party payroll service. Check with
    the third-party being used to determine the
    `External Code`{.interpreted-text role="guilabel"} to enter for the
    new work entry type.
-   `SDWorx code`{.interpreted-text role="guilabel"}: this code is only
    for companies that use SDWorx, a payroll service provider.
-   `Color`{.interpreted-text role="guilabel"}: select a color for the
    particular work entry type.

##### Display in payslip section

-   `Rounding`{.interpreted-text role="guilabel"}: the rounding method
    selected determines how quantities on timesheet entries are
    displayed on the payslip.
    -   `No Rounding`{.interpreted-text role="guilabel"}: a timesheet
        entry is not modified.
    -   `Half Day`{.interpreted-text role="guilabel"}: a timesheet entry
        is rounded to the closest half day amount.
    -   `Day`{.interpreted-text role="guilabel"}: a timesheet entry is
        rounded to the closest full day amount.

::: {.example}
If the working time is set to an 8-hour work day (40-hour work week),
and an employee enters a time of 5.5 hours on a timesheet, and
`Rounding`{.interpreted-text role="guilabel"} is set to
`No Rounding`{.interpreted-text role="guilabel"}, the entry remains 5.5
hours. If `Rounding`{.interpreted-text role="guilabel"} is set to
`Half Day`{.interpreted-text role="guilabel"}, the entry is changed to 4
hours. If it is set to `Day`{.interpreted-text role="guilabel"}, it is
changed to 8 hours.
:::

##### Unpaid section

-   `Unpaid in Structures Types`{.interpreted-text role="guilabel"}: if
    the work entry is for work that is not paid, specify which pay
    structure the unpaid work entry applies to from the drop-down menu.
    Some situations where work is logged on a timesheet, but no
    compensation given would be for unpaid internships, unpaid training,
    or volunteer work.

##### Valid for advantages section

-   `Meal Voucher`{.interpreted-text role="guilabel"}: if the work entry
    should count towards a meal voucher, check the box.
-   `Representation Fees`{.interpreted-text role="guilabel"}: if the
    work entry should count towards representation fees, check the box.
-   `Private Car Reimbursement`{.interpreted-text role="guilabel"}: if
    the work entry should count towards a private car reimbursement,
    check the box.

##### Time off options section

-   `Time Off`{.interpreted-text role="guilabel"}: check this box if the
    work entry type can be selected for a time off request, or entry, in
    the *Time Off* application.

    If `Time Off`{.interpreted-text role="guilabel"} is checked, a
    `Time Off Type`{.interpreted-text role="guilabel"} field appears.
    This field has a drop-down menu to select the specific type of time
    off, such as [Paid Time Off]{.title-ref}, [Sick Time
    Off]{.title-ref}, or [Extra Hours]{.title-ref}, for example.

    A new type of time off can be entered in the field, if the listed
    types of time off in the drop-down menu do **not** display the type
    of time off needed.

-   `Keep Time Off Right`{.interpreted-text role="guilabel"}: this is
    for Belgian-specific companies **only**, and does **not** appear for
    other localizations. Check this box if the work entry is for time
    off that affects the time off benefits for the following year.
    Workers are given time off each year, according to the government,
    and in some cases, time off taken during a specific time period can
    affect how much time off the employee receives or accrues the
    following year.

##### Reporting section

-   `Unforeseen Absence`{.interpreted-text role="guilabel"}: if the work
    entry should be visible on the unforeseen absences report, check
    this box.

{.align-center}

### Working schedules {#payroll/working-times}

To view the currently configured working schedules, go to
`Payroll app -->
Configuration --> Work Entries --> Working Schedules`{.interpreted-text
role="menuselection"}. The working schedules that are available for an
employee\'s contracts and work entries are found in this list.

Working schedules are company-specific. Each company **must** identify
each type of working schedule they use. If the database is created for
only one company, the company column is not available.

::: {.example}
An Odoo database containing multiple companies that use a standard
40-hour work week needs to have a separate working schedule entry for
each company that uses the 40-hour standard work week.

A database with five companies that all use a standard 40-hour work week
needs to have five separate 40-hour working schedules configured.
:::

{.align-center}

#### New working schedule {#payroll/new-working-schedule}

To create a new working schedule, click the `New`{.interpreted-text
role="guilabel"} button, and enter the information on the form.

The fields are auto-populated for a regular 40-hour work week but can be
modified. First, change the name of the working time by modifying the
text in the `Name`{.interpreted-text role="guilabel"} field. Next, make
any adjustments to the days and times that apply to the new working
time.

In the `Working Hours`{.interpreted-text role="guilabel"} tab, modify
the `Day of Week`{.interpreted-text role="guilabel"},
`Day Period`{.interpreted-text role="guilabel"}, and
`Work Entry Type`{.interpreted-text role="guilabel"} selections by
clicking on the drop-down menus in each column and making the desired
selection. The `Work From`{.interpreted-text role="guilabel"} and
`Work To`{.interpreted-text role="guilabel"} columns are modified by
typing in the time.

::: {.note}
::: {.title}
Note
:::

The `Work From`{.interpreted-text role="guilabel"} and
`Work To`{.interpreted-text role="guilabel"} times must be in a 24-hour
format. For example, [2:00 PM]{.title-ref} would be entered as
[14:00]{.title-ref}.
:::

If the working time should be in a two-week configuration, click the
`Switch to 2 weeks
calendar`{.interpreted-text role="guilabel"} button in the top-left.
This creates entries for an `Even week`{.interpreted-text
role="guilabel"} and an `Odd week`{.interpreted-text role="guilabel"}.

{.align-center}

Salary
------

### Structure types {#payroll/structure-types}

In Odoo, an employee\'s payslip is based on *structures* and *structure
types*, which both affect how an employee enters timesheets. Each
structure type is an individual set of rules for processing a timesheet
entry, which consists of different structures nested within it.
Structure types define how often an employee gets paid, the working
hours, and if wages are based on a salary (fixed) or how many hours the
employee worked (varied).

For example, a structure type could be [Employee]{.title-ref}, and that
structure type could have two different structures in it: a [Regular
Pay]{.title-ref} structure which includes all the separate rules for
processing regular pay, as well as a structure for an [End of Year
Bonus]{.title-ref} which includes the rules only for the end of year
bonus. Both the [Regular Pay]{.title-ref} structure and [End of Year
Bonus]{.title-ref} structure are structures within the
[Employee]{.title-ref} structure type.

The different `Structure Types`{.interpreted-text role="guilabel"} can
be seen by navigating to `Payroll app
--> Configuration --> Salary: Structure Types`{.interpreted-text
role="menuselection"}.

Two default structure types are configured in Odoo:
`Employee`{.interpreted-text role="guilabel"} and
`Worker`{.interpreted-text role="guilabel"}.

Typically, `Employee`{.interpreted-text role="guilabel"} is used for
salaried employees, which is why the wage type is
`Monthly Fixed Wage`{.interpreted-text role="guilabel"}, and
`Worker`{.interpreted-text role="guilabel"} is typically used for
employees paid by the hour, so the wage type is
`Hourly Wage`{.interpreted-text role="guilabel"}.

{.align-center}

#### New structure type {#payroll/new-structure-type}

To make a new structure type, click the `New`{.interpreted-text
role="guilabel"} button, and a blank structure type form appears.

Proceed to enter information in the fields. Most fields are
pre-populated, but all the fields can be modified.

-   `Structure Type`{.interpreted-text role="guilabel"}: enter the name
    for the new structure type, such as [Employee]{.title-ref} or
    [Worker]{.title-ref}.

-   `Country`{.interpreted-text role="guilabel"}: select the country
    that the new structure type applies to from the drop-down menu.

-   `Wage Type`{.interpreted-text role="guilabel"}: select what type of
    wage the new structure type uses, either
    `Fixed Wage`{.interpreted-text role="guilabel"} or
    `Hourly Wage`{.interpreted-text role="guilabel"}.

    If the type is to be used for salaried employees, who receive the
    same wage every pay period, select `Fixed Wage`{.interpreted-text
    role="guilabel"}.

    If the type is to be used for employees, who receive wages based on
    how many hours they worked during a pay period, select
    `Hourly Wage`{.interpreted-text role="guilabel"}.

-   `Default Scheduled Pay`{.interpreted-text role="guilabel"}: select
    the typical pay schedule for the new structure type from the
    drop-down menu. Options are `Monthly`{.interpreted-text
    role="guilabel"}, `Quarterly`{.interpreted-text role="guilabel"},
    `Semi-annually`{.interpreted-text role="guilabel"},
    `Annually`{.interpreted-text role="guilabel"},
    `Weekly`{.interpreted-text role="guilabel"},
    `Bi-weekly`{.interpreted-text role="guilabel"},
    `Bi-monthly`{.interpreted-text role="guilabel"}. This indicates how
    often this specific type of structure is paid out.

-   `Default Working Hours`{.interpreted-text role="guilabel"}: select
    the default working hours for the new structure type from the
    drop-down menu. All available working hours for the currently
    selected company appear in the drop-down menu. The default working
    hours that are pre-configured in Odoo is the
    `Standard 40 hours/week`{.interpreted-text role="guilabel"} option.
    If the needed working hours do not appear in the list, a
    `new set of default working hours can be created <new-default-working-hours>`{.interpreted-text
    role="ref"}.

-   `Regular Pay Structure`{.interpreted-text role="guilabel"}: type in
    the name for the regular pay structure.

-   `Default Work Entry Type`{.interpreted-text role="guilabel"}: select
    the default type of work entry the new structure type falls under
    from the drop-down menu. The default options include
    `Attendance`{.interpreted-text role="guilabel"},
    `Overtime Hours`{.interpreted-text role="guilabel"},
    `Generic Time Off`{.interpreted-text role="guilabel"},
    `Compensatory Time Off`{.interpreted-text role="guilabel"},
    `Home Working`{.interpreted-text role="guilabel"},
    `Unpaid`{.interpreted-text role="guilabel"},
    `Sick Time Off`{.interpreted-text role="guilabel"}, `Paid Time
    Off`{.interpreted-text role="guilabel"},
    `Out Of Contract`{.interpreted-text role="guilabel"},
    `Extra Hours`{.interpreted-text role="guilabel"}, and
    `Long Term Time Off`{.interpreted-text role="guilabel"}.

    To view all the options for the
    `Default Work Entry Type`{.interpreted-text role="guilabel"}, click
    the `Search
    More..`{.interpreted-text role="guilabel"} button at the bottom of
    the drop-down list.

    Depending on the localization settings, this list may contain more
    options in addition to the default options.

{.align-center}

#### New default working hours

To make new default working hours, type the name for the new working
hours in the `Default
Working Hours`{.interpreted-text role="guilabel"} field on the new
structure type form. Click `Create and edit`{.interpreted-text
role="guilabel"}. A default working hours form pops up. The default
working hours form has two sections, a general information section and a
tab listing out all the individual working hours by day and time. When
the form is completed, click `Save & Close`{.interpreted-text
role="guilabel"}.

-   `Name`{.interpreted-text role="guilabel"}: type in the name for the
    new default working hours. This should be descriptive and clear to
    understand, such as [Standard 20 Hours/Week]{.title-ref}.

-   `Company`{.interpreted-text role="guilabel"}: select the company
    that can use these new default working hours from the drop-down
    menu. Keep in mind, working hours are company-specific, and cannot
    be shared between companies. Each company needs to have their own
    working hours set.

-   `Average Hour Per Day`{.interpreted-text role="guilabel"}: the
    average hours per day field is auto-populated, based on the working
    hours configured in the `Working Hours`{.interpreted-text
    role="guilabel"} tab. This entry affects resource planning, since
    the average daily hours affect what resources can be used, and in
    what quantity, per work day.

-   `Timezone`{.interpreted-text role="guilabel"}: select the time zone
    to be used for the new default working hours from the drop-down
    menu.

-   `Company Full Time`{.interpreted-text role="guilabel"}: enter the
    number of hours per week an employee would need to work to be
    considered a full-time employee. Typically, this is approximately 40
    hours, and this number affects what types of benefits an employee
    can receive, based on their employment status (full-time vs
    part-time).

-   `Work Time Rate`{.interpreted-text role="guilabel"}: this percentage
    is auto-generated based on the entry for the
    `Company Full Time`{.interpreted-text role="guilabel"} and the
    working hours configured in the `Working Hours`{.interpreted-text
    role="guilabel"} tab. This number should be between
    [0.00%]{.title-ref} and [100%]{.title-ref}, so if the percentage is
    above [100%]{.title-ref}, it is an indication that the working times
    and/or `Company Full Time`{.interpreted-text role="guilabel"} hours
    need adjustment.

-   `Working Hours`{.interpreted-text role="guilabel"} Tab: this tab is
    where each day\'s specific working hours are listed. When a new
    default working hour form is created, the
    `Working Hours`{.interpreted-text role="guilabel"} tab is
    pre-populated with a default 40-hour week, with each day divided
    into three timed sections.

    Every day has morning (8:00-12:00), lunch (12:00-13:00), and evening
    (13:00-17:00) hours configured, using a 24 hour time format.

    To adjust any of these hours, click on the specific field to adjust,
    and make the adjustment using the drop-down menus, or in the
    specific case of the times, type in the desired time.

    Keep in mind, working hours are company-specific, and cannot be
    shared between companies. Each company needs to have their own
    working hours set.

    ::: {.note}
    ::: {.title}
    Note
    :::

    If the working hours are not consistent each week, and the hours are
    on a bi-weekly schedule instead, click the
    `Switch to 2 week calendar`{.interpreted-text role="guilabel"}
    button at the top of the new default working hours form. This
    changes the `Working Hours`{.interpreted-text role="guilabel"} tab
    to display two weeks of working times that can be adjusted.
    :::

### Structures

*Salary structures* are the different ways an employee gets paid within
a specific *structure*, and are specifically defined by various rules.

The amount of structures a company needs for each structure type depends
on how many different ways employees are paid, and how their pay is
calculated. For example, a common structure that could be useful to add
may be a [Bonus]{.title-ref}.

To view all the various structures for each structure type, go to
`Payroll app -->
Configuration --> Salary --> Structures`{.interpreted-text
role="menuselection"}.

Each `structure type <payroll/structure-types>`{.interpreted-text
role="ref"} lists the various structures associated with it. Each
structure contains a set of rules that define it.

{.align-center}

Click on a structure to view its `Salary Rules`{.interpreted-text
role="guilabel"}. These rules are what calculate the payslip for the
employee.

{.align-center}

### Rules

Each structure has a set of *salary rules* to follow for accounting
purposes. These rules are configured by the localization, and affect
actions in the *Accounting* application, so modifications to the default
rules, or the creation of new rules, should only be done when necessary.

To view all the rules, go to
`Payroll app --> Configuration --> Salary --> Rules`{.interpreted-text
role="menuselection"}. Click on a structure (such as
`Regular Pay`{.interpreted-text role="guilabel"}) to view all the rules.

To make a new rule, click `New`{.interpreted-text role="guilabel"}. A
new rule form appears. Enter the following information in the fields.

#### Top section

-   `Rule Name`{.interpreted-text role="guilabel"}: enter a name for the
    rule. This field is required.
-   `Category`{.interpreted-text role="guilabel"}: select a category the
    rule applies to from the drop-down menu, or enter a new one. This
    field is required.
-   `Code`{.interpreted-text role="guilabel"}: enter a code to be used
    for this new rule. It is recommended to coordinate with the
    accounting department for a code to use as this affects accounting
    reports and payroll processing. This field is required.
-   `Sequence`{.interpreted-text role="guilabel"}: enter a number
    indicating when this rule is calculated in the sequence of all other
    rules.
-   `Salary Structure`{.interpreted-text role="guilabel"}: select a
    salary structure the rule applies to from the drop-down menu, or
    enter a new one. This field is required.
-   `Active`{.interpreted-text role="guilabel"}: enable this toggle, so
    the rule is available for use. Disable the toggle to hide the rule
    without deleting it in the database.
-   `Appears on payslip`{.interpreted-text role="guilabel"}: tick the
    checkbox to have the rule appear on employee payslips.
-   `View on Employer Cost Dashboard`{.interpreted-text
    role="guilabel"}: tick the checkbox to have the rule appear on the
    `Employer Cost`{.interpreted-text role="guilabel"} report, located
    on the *Payroll* app dashboard.
-   `View on Payroll Reporting`{.interpreted-text role="guilabel"}: tick
    the checkbox to have the rule appear on payroll reports.

{.align-center}

#### General tab

##### Conditions

-   `Condition Based on`{.interpreted-text role="guilabel"}: select from
    the drop-down menu whether the rule is
    `Always True`{.interpreted-text role="guilabel"} (always applies), a
    `Range`{.interpreted-text role="guilabel"} (applies to a specific
    range, which is entered beneath the selection), or a
    `Python Expression`{.interpreted-text role="guilabel"} (the code is
    entered beneath the selection). This field is required.

##### Computation

-   `Amount Type`{.interpreted-text role="guilabel"}: select from the
    drop-down menu whether the amount is a `Fixed
    Amount`{.interpreted-text role="guilabel"}, a
    `Percentage (%)`{.interpreted-text role="guilabel"}, or a
    `Python Code`{.interpreted-text role="guilabel"}. Depending on what
    is selected, the fixed amount, percentage, or Python code needs to
    be entered next. This field is required.

##### Company contribution

-   `Partner`{.interpreted-text role="guilabel"}: if another company
    financially contributes to this rule, select the company from the
    drop-down menu.

#### Description tab

Provide any additional information in this tab to help clarify the rule.
This tab only appears in the rule form.

#### Accounting tab

-   `Debit Account`{.interpreted-text role="guilabel"}: select the debit
    account from the drop-down menu the rule affects.
-   `Credit Account`{.interpreted-text role="guilabel"}: select the
    credit account from the drop-down menu the rule affects.
-   `Not computed in net accountability`{.interpreted-text
    role="guilabel"}: tick the checkbox to delete the value of this rule
    in the [Net Salary]{.title-ref} rule.

### Rule parameters

::: {.note}
::: {.title}
Note
:::

Currently, the `Rule Parameters`{.interpreted-text role="guilabel"}
feature found inside the `Payroll app
--> Configuration --> Salary --> Rule Parameters`{.interpreted-text
role="menuselection"} menu is still in development and only serves a
specific use case for Belgian markets. The documentation will be updated
when this section has matured to more markets.
:::

### Other input types

When creating payslips, it is sometimes necessary to add other entries
for specific circumstances, like expenses, reimbursements, or
deductions. These other inputs can be configured by navigating to
`Payroll app --> Configuration --> Salary --> Other Input Types`{.interpreted-text
role="menuselection"}.

![A list of other input types for payroll that can be selected when creating a new entry for
a payslip.](payroll/other-input.png){.align-center}

To create a new input type, click the `New`{.interpreted-text
role="guilabel"} button. Enter the `Description`{.interpreted-text
role="guilabel"}, the `Code`{.interpreted-text role="guilabel"}, and
which structure it applies to in the
`Availability in Structure`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

The `Code`{.interpreted-text role="guilabel"} is used in the salary
rules to compute payslips. If the
`Availability in Structure`{.interpreted-text role="guilabel"} field is
left blank, it indicates that the new input type is available for all
payslips and is not exclusive to a specific structure.
:::

{.align-center}

Salary package configurator {#payroll/salary-attachment-types}
---------------------------

The various options under the
`Salary Package Configurator`{.interpreted-text role="guilabel"} section
of the
`Payroll app --> Configuration --> Salary Package Configurator`{.interpreted-text
role="menuselection"} menu all affect an employee\'s potential salary.
These sections (`Benefits`{.interpreted-text role="guilabel"},
`Personal Info`{.interpreted-text role="guilabel"}, and
`Resume`{.interpreted-text role="guilabel"}) specify what benefits can
be offered to an employee in their salary package.

Depending on what information an employee enters (such as deductions,
dependents, etc.), their salary is adjusted accordingly. When an
applicant applies for a job on the company website, the sections under
`Salary Package Configurator`{.interpreted-text role="guilabel"}
directly affect what the applicant sees, and what is populated, as the
applicant enters information.

### Benefits

When offering potential employees a position, there can be certain
benefits set in Odoo, in addition to the salary, to make an offer more
appealing (such as extra time off, the use of a company car,
reimbursement for a phone or internet, etc.).

To view the benefits, go to
`Payroll app --> Configuration --> Salary Package
Configurator: Benefits`{.interpreted-text role="menuselection"}.
Benefits are grouped by `Structure type`{.interpreted-text
role="guilabel"}, and the benefit listed for a particular structure type
is only available for that specific structure.

{.align-center}

::: {.example}
A company has two structure types, one labeled
`Employee`{.interpreted-text role="guilabel"}, and another labeled
`Intern`{.interpreted-text role="guilabel"}. The
`Employee`{.interpreted-text role="guilabel"} structure type contains
the benefit of using a company car, while the `Intern`{.interpreted-text
role="guilabel"} structure type has a meal voucher benefit available.

A person hired under the `Employee`{.interpreted-text role="guilabel"}
structure type can use the company car benefit, but cannot have meal
vouchers. A person hired under the `Intern`{.interpreted-text
role="guilabel"} structure type would have meal voucher benefits
available to them, not the use of a company car.
:::

To make a new benefit, click the `New`{.interpreted-text
role="guilabel"} button, and enter the information in the fields on the
blank benefits form.

The various fields for creating a benefit are as follows:

#### General information section

-   `Benefits`{.interpreted-text role="guilabel"}: enter the name for
    the benefit. This field is required.

-   `Benefit Field`{.interpreted-text role="guilabel"}: select from the
    drop-down menu the type of benefit this is.

-   `Cost Field`{.interpreted-text role="guilabel"}: select from the
    drop-down menu the type of cost incurred by the company for this
    specific benefit. The default options are
    `Calendar Changed`{.interpreted-text role="guilabel"}, `Yearly
    Cost (Real)`{.interpreted-text role="guilabel"},
    `Extra Time Off`{.interpreted-text role="guilabel"},
    `Hourly Wage`{.interpreted-text role="guilabel"},
    `Part Time`{.interpreted-text role="guilabel"},
    `Wage`{.interpreted-text role="guilabel"},
    `Wage with Holidays`{.interpreted-text role="guilabel"}, and
    `Work time rate`{.interpreted-text role="guilabel"}. Depending on
    the localization settings, additional options are available.

-   `Related Type`{.interpreted-text role="guilabel"}: select from the
    drop-down menu what type of benefit it is. Select from
    `Monthly Benefit in Kind`{.interpreted-text role="guilabel"},
    `Monthly Benefit in Net`{.interpreted-text role="guilabel"},
    `Monthly
    Benefit in Cash`{.interpreted-text role="guilabel"},
    `Yearly Benefits in Cash`{.interpreted-text role="guilabel"}, or
    `Non Financial Benefits`{.interpreted-text role="guilabel"}. This
    field is required.

-   `Benefit Field`{.interpreted-text role="guilabel"}: select from the
    drop-down menu the specific field on the contract the benefit
    appears.

-   `Cost Field`{.interpreted-text role="guilabel"}: select the specific
    field on the contract that the cost of the benefit is linked to,
    using the drop-down menu. If this field is left blank, the cost of
    the benefit is not computed in the employee budget.

-   `Impacts Net Salary`{.interpreted-text role="guilabel"}: tick the
    checkbox if the benefit should impact the employee\'s net salary.

-   `Requested Documents`{.interpreted-text role="guilabel"}: select any
    document that is required to be submitted for this benefit, from the
    drop-down menu.

-   `Mandatory Benefits`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the benefit that is required in order for
    this specific benefit to be offered to the employee.

    For example, a benefit for car insurance would populate [Company
    Car]{.title-ref} in this field. This would allow the car insurance
    benefit to **only** be displayed if the employee has
    selected/enabled the benefit of a company car.

-   `Salary Structure Type`{.interpreted-text role="guilabel"}: select
    from the drop-down menu which salary structure type this benefit
    applies to. This field is required.

-   `Unit of Measure`{.interpreted-text role="guilabel"}: select the
    metric that the benefit is granted, using the drop-down menu. The
    options are `Days`{.interpreted-text role="guilabel"},
    `Percent`{.interpreted-text role="guilabel"}, or
    `Currency`{.interpreted-text role="guilabel"}.

{.align-center}

#### Display section

-   `Show Name`{.interpreted-text role="guilabel"}: tick the checkbox to
    have the benefit name appear in the salary package configurator.

-   `Display Type`{.interpreted-text role="guilabel"}: select from the
    drop-down menu how this benefit is displayed. The options are
    `Always Selected`{.interpreted-text role="guilabel"},
    `Dropdown`{.interpreted-text role="guilabel"},
    `Dropdown Group`{.interpreted-text role="guilabel"},
    `Slider`{.interpreted-text role="guilabel"},
    `Radio Buttons`{.interpreted-text role="guilabel"},
    `Manual Input`{.interpreted-text role="guilabel"}, or
    `Text`{.interpreted-text role="guilabel"}. This field is required.

    Depending on the selection made, additional configurations need to
    be made. For example, if `Radio Buttons`{.interpreted-text
    role="guilabel"} is selected, the individual radio buttons must be
    entered.

-   `Icon`{.interpreted-text role="guilabel"}: an icon from the [Font
    Awesome 4 library](https://fontawesome.com/v4/icons/) can be visible
    for this benefit. Enter the text code for the icon in this field.
    For example, to display a suitcase icon, the code [fa
    fa-suitcase]{.title-ref} is entered on this line.

-   `Hide Description`{.interpreted-text role="guilabel"}: tick the
    checkbox to hide the benefit description if the benefit is not
    selected by the employee.

-   `Folded`{.interpreted-text role="guilabel"}: if the benefit should
    be folded, or hidden, because it is dependant on another benefit
    selection, tick the checkbox. The following fields appear when this
    is active:

    -   `Fold Label`{.interpreted-text role="guilabel"}: enter a name
        for the folded section of the benefit.
    -   `Fold Res Field`{.interpreted-text role="guilabel"}: select the
        contract field this benefit is tied to using the drop-down menu.
        If this field is selected on the contract, then this benefit
        becomes visible.

#### Activity section

-   `Activity Type`{.interpreted-text role="guilabel"}: from the
    drop-down menu, select the activity type that is automatically
    created when this benefit is selected by the employee.
-   `Activity Creation`{.interpreted-text role="guilabel"}: select when
    the activity is created, either when the
    `Employee signs his contract`{.interpreted-text role="guilabel"}, or
    when the `Contract is countersigned`{.interpreted-text
    role="guilabel"}. Click the radio button next to the desired
    selection.
-   `Activity Creation Type`{.interpreted-text role="guilabel"}: select
    the parameters for when the activity is created, either
    `When the benefit is set`{.interpreted-text role="guilabel"} or
    `When the benefit is modified`{.interpreted-text role="guilabel"}.
    Click the radio button next to the desired selection.
-   `Assigned to`{.interpreted-text role="guilabel"}: select the user
    the activity is automatically assigned to, using the drop-down menu.

#### Sign section

-   `Template to Sign`{.interpreted-text role="guilabel"}: if the
    employee is required to sign a document when selecting this benefit,
    select the document template from the drop-down menu.

    For example, a benefit regarding the use of a company car may
    require the employee to sign a document acknowledging the company\'s
    car policies.

#### Description tab

Provide any additional information in this tab to help clarify the
benefit.

### Personal info

Every employee in Odoo has an *employee card* which is created when a
candidate becomes an employee. This card includes all of their personal
information, resume, work information, and documents.

The personal information is gathered from the salary package
configurator section that a candidate fills out after being offered a
position. This personal information is then transferred to the employee
card when they are hired.

To view an employee\'s card, go to the main
`Employees`{.interpreted-text role="menuselection"} app dashboard, and
click on the employee\'s card.

::: {.note}
::: {.title}
Note
:::

An employee card can be thought of as an employee personnel file.
:::

The `Personal Info`{.interpreted-text role="guilabel"} section lists all
of the fields that are available to enter on the employee\'s card. To
access this section, go to `Payroll app --> Configuration -->
Salary Package Configurator: Personal Info`{.interpreted-text
role="menuselection"}.

{.align-center}

To edit a personal info entry, select an entry from the list on the
`Personal Info`{.interpreted-text role="guilabel"} page, and modify the
personal info on the form that appears.

To create a new personal info entry, click the `New`{.interpreted-text
role="guilabel"} button.

The required fields, aside from entering the
`Information`{.interpreted-text role="guilabel"} name, are `Related
Model`{.interpreted-text role="guilabel"},
`Related Field`{.interpreted-text role="guilabel"}, and
`Category`{.interpreted-text role="guilabel"}.

Select a `Related Model`{.interpreted-text role="guilabel"} from the
drop-down menu. `Employee`{.interpreted-text role="guilabel"} populates
the field by default, but the `Bank Account`{.interpreted-text
role="guilabel"} option is also available if the information is related
to a bank account, instead.

Select a `Related Field`{.interpreted-text role="guilabel"} from the
drop-down menu that best describes what kind of personal information
this entry is, and where it is stored in the backend. Then, select a
`Category`{.interpreted-text role="guilabel"} from the drop-down menu
that the personal information should be under, such as
`Address`{.interpreted-text role="guilabel"} or
`Personal Documents`{.interpreted-text role="guilabel"}.

The two most important fields on the personal info form are
`Is Required`{.interpreted-text role="guilabel"} and
`Display Type`{.interpreted-text role="guilabel"}.

Checking the `Is Required`{.interpreted-text role="guilabel"} box makes
the field mandatory on the employee\'s card. The
`Display Type`{.interpreted-text role="guilabel"} drop-down menu allows
for the information to be entered in a variety of ways, like a
`Text`{.interpreted-text role="guilabel"} box, to a customizable
`Radio`{.interpreted-text role="guilabel"} button, a
`Checkbox`{.interpreted-text role="guilabel"}, a
`Document`{.interpreted-text role="guilabel"}, and more.

{.align-center}

### Resumé

The resumé section, housed within the salary package configurator
section of the settings menu, is how salary information rules are
configured when offering a position to potential employees.

When an offer is sent to a prospective employee, the values for the
offer are computed from these settings, and appear on the offer page.

To configure this section, navigate to
`Payroll app --> Configuration --> Salary
Package Configurator: Resumé`{.interpreted-text role="menuselection"}.

By default, there are three `Salary Structure Types`{.interpreted-text
role="guilabel"} pre-configured in Odoo: `Worker`{.interpreted-text
role="guilabel"}, `Employee`{.interpreted-text role="guilabel"}, and
`None`{.interpreted-text role="guilabel"}.

Each `Salary Structure Type`{.interpreted-text role="guilabel"} has
several rules configured. These affect how an offer is calculated using
that particular `Salary Structure Type`{.interpreted-text
role="guilabel"}.

To create a new rule, click the `New`{.interpreted-text role="guilabel"}
button, and a blank `Contract Salary
Resumé`{.interpreted-text role="guilabel"} form loads.

Enter the following information on the form:

-   `Information`{.interpreted-text role="guilabel"}: type in a name for
    this field.

-   `Category`{.interpreted-text role="guilabel"}: select the category
    this value is housed under, using the drop-down menu. The default
    options are `Monthly Salary`{.interpreted-text role="guilabel"},
    `Monthly Benefits`{.interpreted-text role="guilabel"},
    `Yearly Benefits`{.interpreted-text role="guilabel"}, and
    `Total`{.interpreted-text role="guilabel"}.

    New categories can be made if needed.

    Click the `New`{.interpreted-text role="guilabel"} button, then
    enter the name for the new category in the `Name`{.interpreted-text
    role="guilabel"} field. Next, select the
    `Periodicity`{.interpreted-text role="guilabel"} from the drop-down
    menu, either `Monthly`{.interpreted-text role="guilabel"} or
    `Yearly`{.interpreted-text role="guilabel"}. Last, enter a number
    for the sequence. This corresponds to where this rule appears in the
    `Salary Structure Type`{.interpreted-text role="guilabel"} rule
    list.

    Finally, click `Save & Close`{.interpreted-text role="guilabel"}.

-   `Impacts Monthly Total`{.interpreted-text role="guilabel"}: tick the
    checkbox if this value is added in the monthly total calculation.

-   `Unit of Measure`{.interpreted-text role="guilabel"}: select what
    kind of value this rule is, either `Currency`{.interpreted-text
    role="guilabel"}, `Days`{.interpreted-text role="guilabel"}, or
    `Percent`{.interpreted-text role="guilabel"}.

    `Currency`{.interpreted-text role="guilabel"} is for a set monetary
    value, `Days`{.interpreted-text role="guilabel"} is for compensation
    in the form of time off, and `Percent`{.interpreted-text
    role="guilabel"} is for a monetary value awarded that is based upon
    another metric, such as commissions.

-   `Salary Structure Type`{.interpreted-text role="guilabel"}: select
    which `Salary Structure Type`{.interpreted-text role="guilabel"}
    this rule is nested under, from the drop-down menu.

-   `Value Type`{.interpreted-text role="guilabel"}: select how the
    value is computed, using the drop-down menu. The default options are
    `Fixed Value`{.interpreted-text role="guilabel"},
    `Contract Value`{.interpreted-text role="guilabel"},
    `Payslip Value`{.interpreted-text role="guilabel"},
    `Sum of Benefits Values`{.interpreted-text role="guilabel"}, and
    `Monthly Total`{.interpreted-text role="guilabel"}.

-   `Code`{.interpreted-text role="guilabel"}: select the code this rule
    applies to from the drop-down menu.

{.align-center}

Jobs
----

Since the *Payroll* application is responsible for paying employees for
specific job positions, the complete list of job positions can be found
in both the *Payroll* and *Recruitment* applications.

### Job positions {#payroll/job-positions}

The job positions listed in the *Payroll* application are identical to
the job positions listed in the *Recruitment* application. If a new job
position is added in the *Recruitment* application, it is also visible
in the *Payroll* application, and vice versa.

To view the job positions, navigate to
`Payroll app --> Configuration --> Jobs: Job
Positions`{.interpreted-text role="menuselection"}.

A list of all the job positions appear, along with the corresponding
department, on the `Job Position`{.interpreted-text role="guilabel"}
page.

{.align-center}

To create a new job description, click the `New`{.interpreted-text
role="guilabel"} button and a job form appears.

Enter the information on the form for the new position. The information
is identical as to the information entered when creating a new job
position in the *Recruitment* application.

Refer to the `../hr/recruitment/new_job`{.interpreted-text role="doc"}
documentation for more details on how to fill out this form.

::: {.seealso}
\- `payroll/contracts`{.interpreted-text role="doc"} -
`payroll/work_entries`{.interpreted-text role="doc"} -
`payroll/salary_attachments`{.interpreted-text role="doc"} -
`payroll/payslips`{.interpreted-text role="doc"} -
`payroll/reporting`{.interpreted-text role="doc"} -
`payroll/work_entry_analysis`{.interpreted-text role="doc"} -
`payroll/salary_attachment`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
payroll/contracts payroll/work\_entries payroll/salary\_attachments
payroll/payslips payroll/reporting payroll/work\_entry\_analysis
payroll/salary\_attachment
:::
