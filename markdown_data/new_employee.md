# File: /content/odoo_doc17.0/fr/content/applications/hr/employees/new_employee.md

New employees
=============

When a new employee is hired, the first step is to create a new employee
record. This record is a centralized place where all important
information about the employee is stored, including
`general information <employees/general-info>`{.interpreted-text
role="ref"}, `job history and skills
<employees/resume>`{.interpreted-text role="ref"},
`various work information <employees/work-info-tab>`{.interpreted-text
role="ref"}, `personal
details <employees/private-info>`{.interpreted-text role="ref"},
`documents <employees/docs>`{.interpreted-text role="ref"}, and more.

To begin, open the `Employees`{.interpreted-text role="menuselection"}
app, then click the `New`{.interpreted-text role="guilabel"} button in
the upper-left corner. Doing so reveals a blank employee form.

Proceed to fill out the required information, along with any additional
details.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The current company phone number and name are populated in the
`Work Phone`{.interpreted-text role="guilabel"} and
`Company`{.interpreted-text role="guilabel"} fields. If the *Appraisals*
application is installed, the `Next
Appraisal Date`{.interpreted-text role="guilabel"} field is populated
with a date six months from the current date.
:::

General information {#employees/general-info}
-------------------

The employee form automatically saves as data is entered. However, the
form can be saved manually at any time by clicking the
`Save manually`{.interpreted-text role="guilabel"} option, represented
by a `(cloud with
an upwards arrow)`{.interpreted-text role="guilabel"} icon.

### Required fields

-   `Employee's Name`{.interpreted-text role="guilabel"}: enter the
    employee\'s name.
-   `Company`{.interpreted-text role="guilabel"}: from the drop-down
    menu in this field, select the company the new employee was hired
    by, or create a new company by typing the name in the field, and
    clicking `Create`{.interpreted-text role="guilabel"} or
    `Create and edit...`{.interpreted-text role="guilabel"} from the
    mini drop-down menu that appears.

{.align-center}

### Optional fields

-   `Photo`{.interpreted-text role="guilabel"}: in the top-right image
    box of the employee form, click on the `✏️
    (pencil)`{.interpreted-text role="guilabel"} edit icon to select a
    photo to upload.

-   `Job Position`{.interpreted-text role="guilabel"}: enter the
    employee\'s job title under their name, or select it from the
    `Job Position`{.interpreted-text role="guilabel"} field drop-down
    menu below to have this top field auto-populate. The
    `Job Position`{.interpreted-text role="guilabel"} field under the
    employee name can be modified, and does *not* need to match the
    selection made in the `Job Position`{.interpreted-text
    role="guilabel"} drop-down menu in the field below.

    ::: {.example}
    While it is recommended to have the job positions match, the
    typed-in description in this top field can contain more specific
    information than the selected drop-down `Job
    Position`{.interpreted-text role="guilabel"}, if desired.

    For instance, if someone is hired for a sales representative
    position configured as `Sales Representative`{.interpreted-text
    role="guilabel"} in the *Recruitment* app, that can be selected in
    the drop-down `Job Position`{.interpreted-text role="guilabel"}
    field.

    In the typed-in `Job Position`{.interpreted-text role="guilabel"}
    field beneath the `Employee's Name`{.interpreted-text
    role="guilabel"} field, the position could be more specific, such as
    [Sales Representative - Subscriptions]{.title-ref} if the employee
    is focused solely on subscription sales.

    {.align-center}
    :::

-   `Tags`{.interpreted-text role="guilabel"}: select a tag from the
    drop-down menu to add relevant tags to the employee. Any tag can be
    created in this field by typing it in. Once created, the new tag is
    available for all employee records. There is no limit to the amount
    of tags that can be added.

-   `Work Contact Information`{.interpreted-text role="guilabel"}: enter
    the employee\'s `Work Mobile`{.interpreted-text role="guilabel"},
    `Work Phone`{.interpreted-text role="guilabel"},
    `Work Email`{.interpreted-text role="guilabel"}, and/or
    `Company`{.interpreted-text role="guilabel"} name, if not already
    auto-populated.

-   `Department`{.interpreted-text role="guilabel"}: select the
    employee\'s department from the drop-down menu.

-   `Job Position`{.interpreted-text role="guilabel"}: select the
    employee\'s job position from the drop-down menu. Once a selection
    is made, the `Job Position`{.interpreted-text role="guilabel"} field
    beneath the `Employee's Name`{.interpreted-text role="guilabel"}
    field automatically updates to reflect the currently selected job
    position. These positions are from the
    `Recruitment <../../hr/recruitment/new_job/>`{.interpreted-text
    role="doc"} application, and reflect the currently configured job
    positions.

-   `Manager`{.interpreted-text role="guilabel"}: select the employee\'s
    manager from the drop-down menu.

-   `Coach`{.interpreted-text role="guilabel"}: select the employee\'s
    coach from the drop-down menu.

-   `Next Appraisal Date`{.interpreted-text role="guilabel"}: this field
    is **only** visible if the *Appraisals* application is installed.
    The date automatically populates with a date that is computed
    according to the settings configured in the *Appraisals*
    application. This date can be modified using the calendar selector.

::: {.note}
::: {.title}
Note
:::

After a `Manager`{.interpreted-text role="guilabel"} is selected, if the
`Coach`{.interpreted-text role="guilabel"} field is blank, the selected
manager automatically populates the `Coach`{.interpreted-text
role="guilabel"} field.
:::

::: {.tip}
::: {.title}
Tip
:::

To make edits to the selected `Department`{.interpreted-text
role="guilabel"}, `Manager`{.interpreted-text role="guilabel"},
`Coach`{.interpreted-text role="guilabel"}, or
`Company`{.interpreted-text role="guilabel"}, click the
`Internal Link`{.interpreted-text role="guilabel"} arrow next to the
respective selection. The `Internal Link`{.interpreted-text
role="guilabel"} arrow opens the selected form, allowing for
modifications. Click `Save`{.interpreted-text role="guilabel"} after any
edits are made.
:::

Additional information tabs
---------------------------

### Resumé tab {#employees/resume}

#### Resumé

Next, enter the employee\'s work history in the
`Resumé`{.interpreted-text role="guilabel"} tab. Each resumé line must
be entered individually. When creating an entry for the first time,
click `Create a new
entry`{.interpreted-text role="guilabel"}, and the
`Create Resumé lines`{.interpreted-text role="guilabel"} form appears.
After an entry is added, the `Create a new entry`{.interpreted-text
role="guilabel"} button is replaced with an `Add`{.interpreted-text
role="guilabel"} button. Enter the following information for each entry.

{.align-center}

-   `Title`{.interpreted-text role="guilabel"}: type in the title of the
    previous work experience.
-   `Employee`{.interpreted-text role="guilabel"}: select the employee
    from the drop-down menu.
-   `Type`{.interpreted-text role="guilabel"}: from the drop-down menu,
    select either `Experience`{.interpreted-text role="guilabel"},
    `Education`{.interpreted-text role="guilabel"},
    `Side Projects`{.interpreted-text role="guilabel"},
    `Internal Certification`{.interpreted-text role="guilabel"},
    `Completed Internal Training`{.interpreted-text role="guilabel"}, or
    type in a new entry, then click `Create
    "(Type)"`{.interpreted-text role="guilabel"}.
-   `Display Type`{.interpreted-text role="guilabel"}: from the
    drop-down menu, choose `Classic`{.interpreted-text role="guilabel"}
    for typical work experience, `Certification`{.interpreted-text
    role="guilabel"} for experience gained through a certification, or
    `Course`{.interpreted-text role="guilabel"} for non-certified
    classes.
-   `Duration`{.interpreted-text role="guilabel"}: enter the start and
    end dates for the work experience. To select a date, click the first
    empty field to reveal a calendar pop-up window. Proceed to use the
    `<
    (left arrow)`{.interpreted-text role="guilabel"} and
    `> (right arrow)`{.interpreted-text role="guilabel"} icons to scroll
    to the desired month, then click on the day to select it. Repeat
    this process to locate and select the end date. When the desired
    dates have been selected, click `✔️ Apply`{.interpreted-text
    role="guilabel"}.
-   `Description`{.interpreted-text role="guilabel"}: enter any relevant
    details in this field.

Once all the information is entered, click the
`Save & Close`{.interpreted-text role="guilabel"} button if there is
only one entry to add, or click the `Save & New`{.interpreted-text
role="guilabel"} button to save the current entry and create another
resumé line.

::: {.note}
::: {.title}
Note
:::

After the new employee form is saved, the current position and company
is automatically added to the `Resumé`{.interpreted-text
role="guilabel"} tab, with the end date listed as [current]{.title-ref}.
:::

#### Skills {#employees/skills}

An employee\'s skills can be entered in the `Resumé`{.interpreted-text
role="guilabel"} tab in the same manner that a resumé line is created.

In order to add a skill to an employee record, the skill types must be
configured first. If no skill types are configured, a
`Create new Skills`{.interpreted-text role="guilabel"} button appears in
the `Skills`{.interpreted-text role="guilabel"} section of the
`Resumé`{.interpreted-text role="guilabel"} tab.
`Configure the skill types <employees/skill-types>`{.interpreted-text
role="ref"} before adding any skills to the employee record.

If the skill types are configured, a
`Pick a skill from the list`{.interpreted-text role="guilabel"} button
appears instead. Click the
`Pick a skill from the list`{.interpreted-text role="guilabel"} button,
and select the following information for each skill.

{.align-center}

-   `Skill Type`{.interpreted-text role="guilabel"}: select a
    `skill type <employees/skill-types>`{.interpreted-text role="ref"}
    by clicking the radio button next to the skill type.
-   `Skill`{.interpreted-text role="guilabel"}: after selecting a
    `Skill Type`{.interpreted-text role="guilabel"}, the corresponding
    skills associated with that selected `Skill Type`{.interpreted-text
    role="guilabel"} appear in a drop-down menu. For example, selecting
    `Language`{.interpreted-text role="guilabel"} as the
    `Skill Type`{.interpreted-text role="guilabel"} presents a variety
    of languages to select from under the `Skills`{.interpreted-text
    role="guilabel"} field. Select the appropriate pre-configured skill,
    or type in a new skill, then click
    `Create "(new skill)"`{.interpreted-text role="guilabel"}.
-   `Skill Level`{.interpreted-text role="guilabel"}: pre-defined skill
    levels associated with the selected `Skill
    Type`{.interpreted-text role="guilabel"} appear in a drop-down menu.
    First, select a `Skill Level`{.interpreted-text role="guilabel"},
    then the progress bar automatically displays the pre-defined
    progress for that specific skill level. Skill levels and progress
    can be modified in the `Skill Level`{.interpreted-text
    role="guilabel"} pop-up form, which is accessed via the
    `Internal Link`{.interpreted-text role="guilabel"} arrow next to
    `Skill Level`{.interpreted-text role="guilabel"} field.

Click the `Save & Close`{.interpreted-text role="guilabel"} button if
there is only one skill to add, or click the
`Save & New`{.interpreted-text role="guilabel"} button to save the
current entry and immediately add another skill.

To delete any line from the `Resumé`{.interpreted-text role="guilabel"}
tab, click the `🗑️ (trash can)`{.interpreted-text role="guilabel"} icon
to delete the entry. Add a new line by clicking the
`Add`{.interpreted-text role="guilabel"} button next to the
corresponding section.

::: {.important}
::: {.title}
Important
:::

Only users with `Officer: Manage all employees`{.interpreted-text
role="guilabel"} or `Administrator`{.interpreted-text role="guilabel"}
rights for the *Employees* app can add or edit skills.
:::

##### Skill types {#employees/skill-types}

In order to add a skill to an employee\'s form, the
`Skill Types`{.interpreted-text role="guilabel"} must be configured. Go
to
`Employees app --> Configuration --> Employee: Skill Types`{.interpreted-text
role="menuselection"} to view the currently configured skill types and
create new skill types.

::: {.note}
::: {.title}
Note
:::

The default skill of `Languages`{.interpreted-text role="guilabel"} is
pre-configured as a skill *type*, but there are no specific language
*skills* listed within that skill type. The
`Languages`{.interpreted-text role="guilabel"} skill type must be fully
configured before it can be used.
:::

Click `New`{.interpreted-text role="guilabel"} and a new
`Skill Type`{.interpreted-text role="guilabel"} form appears. Fill out
all the details for the new skill type. Repeat this for all the needed
skill types.

-   `Skill Type`{.interpreted-text role="guilabel"}: enter the name of
    the skill type. This acts as the parent category for more specific
    skills and should be generic.

-   `Skills`{.interpreted-text role="guilabel"}: click
    `Add a line`{.interpreted-text role="guilabel"}, and enter the
    `Name`{.interpreted-text role="guilabel"} for the new skill, then
    repeat for all other needed skills.

-   `Levels`{.interpreted-text role="guilabel"}: click
    `Add a line`{.interpreted-text role="guilabel"}, and enter the
    `Name`{.interpreted-text role="guilabel"} of the level. Next, click
    into the `Progress`{.interpreted-text role="guilabel"} field, and
    enter a percentage (0-100) for that level. Repeat for all additional
    levels, as needed.

-   `Default Level`{.interpreted-text role="guilabel"}: click the toggle
    on the level line to set that level as the default. Typically, the
    lowest level is set as the default, but any level can be chosen. The
    toggle turns green, indicating it is the default level for the
    skill. Only one level can be set as the default.

    ::: {.example}
    To add a math skill set, enter [Math]{.title-ref} in the
    `Name`{.interpreted-text role="guilabel"} field. Next, in the
    `Skills`{.interpreted-text role="guilabel"} field, enter
    [Algebra]{.title-ref}, [Calculus]{.title-ref}, and
    [Trigonometry]{.title-ref}. Last, in the `Levels`{.interpreted-text
    role="guilabel"} field enter [Beginner]{.title-ref},
    [Intermediate]{.title-ref}, and [Expert]{.title-ref}, with the
    `Progress`{.interpreted-text role="guilabel"} listed as
    [25]{.title-ref}, [50]{.title-ref}, and [100]{.title-ref},
    respectively. Last, click `Set
    Default`{.interpreted-text role="guilabel"} on the
    [Beginner]{.title-ref} line to set this as the default skill level.

    {.align-center}
    :::

The `Skill Type`{.interpreted-text role="guilabel"} form automatically
saves as data is entered.

::: {.tip}
::: {.title}
Tip
:::

Once the form is completely filled out, click the
`Save manually`{.interpreted-text role="guilabel"} button, represented
by a `cloud with an upwards arrow`{.interpreted-text role="guilabel"}
icon at the top of the screen, and the `Levels`{.interpreted-text
role="guilabel"} rearrange in descending order, with the highest level
at the top, and the lowest at the bottom, regardless of the default
level and the order they were entered.
:::

### Work information tab {#employees/work-info-tab}

The `Work Information`{.interpreted-text role="guilabel"} tab is where
the employee\'s specific job related information is found. Their working
schedule, various roles, who approves their specific requests (time off,
timesheets, and expenses), their remote work schedule, and specific work
location details are listed here.

Click on the `Work Information`{.interpreted-text role="guilabel"} tab
to access this section, and enter the following information for the new
employee:

-   `Location`{.interpreted-text role="guilabel"}: select the
    `Work Address`{.interpreted-text role="guilabel"} from the drop-down
    menu. To modify the address, hover over the first line (if there are
    multiple lines) of the address to reveal an
    `Internal Link`{.interpreted-text role="guilabel"} arrow. Click the
    `Internal Link`{.interpreted-text role="guilabel"} arrow to open up
    the company form, and make any edits.

    Use the breadcrumb links to navigate back to the new employee form
    when done.

    If a new work address is needed, add the address by typing it in the
    field, then click `Create (new address)`{.interpreted-text
    role="guilabel"} to add the address, or
    `Create and edit...`{.interpreted-text role="guilabel"} to add the
    new address and edit the address form.

-   `Approvers`{.interpreted-text role="guilabel"}: to see this section,
    the user must have either `Administrator`{.interpreted-text
    role="guilabel"} or
    `Officer: Manage all employees`{.interpreted-text role="guilabel"}
    rights set for the *Employees* application. Using the drop-down
    menus, select the users responsible for approving an
    `Expense`{.interpreted-text role="guilabel"}, a
    `Time Off`{.interpreted-text role="guilabel"} request,
    `Timesheet`{.interpreted-text role="guilabel"} entries, and
    `Attendance`{.interpreted-text role="guilabel"} records for the
    employee.

    Hover over any of the selections to reveal the
    `Internal Link`{.interpreted-text role="guilabel"} arrow.

    Click the `Internal Link`{.interpreted-text role="guilabel"} arrow
    to open a form with the approver\'s `Name`{.interpreted-text
    role="guilabel"}, `Email Address`{.interpreted-text
    role="guilabel"}, `Company`{.interpreted-text role="guilabel"},
    `Phone`{.interpreted-text role="guilabel"},
    `Mobile`{.interpreted-text role="guilabel"}, and
    `Default Warehouse`{.interpreted-text role="guilabel"} fields. These
    can be modified, if needed.

    Use the breadcrumb links to navigate back to the new employee form
    when done.

    ::: {.important}
    ::: {.title}
    Important
    :::

    The users that appear in the drop-down menu for the
    `Approvers`{.interpreted-text role="guilabel"} section **must** have
    *Administrator* rights set for the corresponding human resources
    role.

    To check who has these rights, go to
    `Settings app --> Users --> → Manage
    Users`{.interpreted-text role="menuselection"}. Then, click on an
    employee, and check the `Human Resources`{.interpreted-text
    role="guilabel"} section of the `Access Rights`{.interpreted-text
    role="guilabel"} tab.

    -   In order for the user to appear as an approver for
        `Expenses`{.interpreted-text role="guilabel"}, they **must**
        have either `Team Approver`{.interpreted-text role="guilabel"},
        `All Approver`{.interpreted-text role="guilabel"}, or
        `Administrator`{.interpreted-text role="guilabel"} set for the
        `Expenses`{.interpreted-text role="guilabel"} role.
    -   In order for the user to appear as an approver for
        `Time Off`{.interpreted-text role="guilabel"}, they **must**
        have either `Officer:Manage all Requests`{.interpreted-text
        role="guilabel"} or `Administrator`{.interpreted-text
        role="guilabel"} set for the `Time Off`{.interpreted-text
        role="guilabel"} role.
    -   In order for the user to appear as an approver for
        `Timesheets`{.interpreted-text role="guilabel"}, they **must**
        have either `Manager`{.interpreted-text role="guilabel"},
        `Officer:Manage all contracts`{.interpreted-text
        role="guilabel"}, or `Administrator`{.interpreted-text
        role="guilabel"} set for the `Payroll`{.interpreted-text
        role="guilabel"} role.
    :::

-   `Remote Work`{.interpreted-text role="guilabel"}: use the drop-down
    menu to select the default location the employee works from each day
    of the week. The default options are `Home`{.interpreted-text
    role="guilabel"}, `Office`{.interpreted-text role="guilabel"}, or
    `Other`{.interpreted-text role="guilabel"}.

    A new location can be typed into the field, then click either
    `Create (new location)`{.interpreted-text role="guilabel"} to add
    the location, or `Create and edit...`{.interpreted-text
    role="guilabel"} to add the new location and edit the form.

    After edits are done, click `Save & Close`{.interpreted-text
    role="guilabel"}, and the new location is added, and populates the
    field.

    Leave the field blank (`Unspecified`{.interpreted-text
    role="guilabel"}) for non-working days like Saturday and Sunday.

    ::: {.note}
    ::: {.title}
    Note
    :::

    It is also possible to add or modify work locations by navigating to
    `Employees
    app --> Configuration --> Employee: Work Locations`{.interpreted-text
    role="menuselection"}. To modify a location, click on an existing
    location, then make any changes on the form.

    Click `New`{.interpreted-text role="guilabel"} to create a new
    location, then enter the following information on the form. All
    fields are **required**.

    -   `Work Location`{.interpreted-text role="guilabel"}: enter the
        name for the location. This can be as general or as specific, as
        needed, such as [Home]{.title-ref} or [Building 1, Second
        Floor]{.title-ref}, respectfully.
    -   `Work Address`{.interpreted-text role="guilabel"}: using the
        drop-down menu, select the address for the location.
    -   `Cover Image`{.interpreted-text role="guilabel"}: click on the
        icon to select it for the `Cover Image`{.interpreted-text
        role="guilabel"}. Options are a `house`{.interpreted-text
        role="guilabel"} icon, an `office building`{.interpreted-text
        role="guilabel"} icon, and a
        `GPS location marker`{.interpreted-text role="guilabel"} icon.
    -   `Company`{.interpreted-text role="guilabel"}: using the
        drop-down menu, select the company the location applies to. The
        current company populates this field, by default.

    {.align-center}
    :::

-   `Schedule`{.interpreted-text role="guilabel"}: select the
    `Working Hours`{.interpreted-text role="guilabel"} and
    `Timezone`{.interpreted-text role="guilabel"} for the employee. The
    `Internal Link`{.interpreted-text role="guilabel"} arrow opens a
    detailed view of the specific daily working hours. Working hours can
    be modified or deleted here.

    ::: {.note}
    ::: {.title}
    Note
    :::

    `Working Hours`{.interpreted-text role="guilabel"} are related to a
    company\'s working schedules, and an Employee **cannot** have
    working hours that are outside of a company\'s working schedule.

    Each individual working schedule is company-specific. So, for
    multi-company databases, each company needs to have its own working
    schedules set.

    If an employee\'s working hours are not configured as a working
    schedule for the company, new working schedules can be added, or
    existing working schedules can be modified.

    Working hours can be modified in the *Payroll* application, where
    they are referred to as `Working Schedules`{.interpreted-text
    role="guilabel"}.

    For more information on how to create or modify
    `Working Schedules`{.interpreted-text role="guilabel"} in the
    *Payroll* application, refer to the
    `../../hr/payroll`{.interpreted-text role="doc"} documentation.
    :::

-   `Planning`{.interpreted-text role="guilabel"}: select a role from
    the drop-down menu for both the `Roles`{.interpreted-text
    role="guilabel"} and the `Default Role`{.interpreted-text
    role="guilabel"} fields. If the `Default Role`{.interpreted-text
    role="guilabel"} is selected as a role, it is automatically added to
    the list of `Roles`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

The users that appear in the drop-down menu for the
`Approvers`{.interpreted-text role="guilabel"} section **must** have
*Administrator* rights set for the corresponding human resources role.

To check who has these rights, go to
`Settings app --> Users --> → Manage Users`{.interpreted-text
role="menuselection"}. Click on an employee, and check the
`Human Resources`{.interpreted-text role="guilabel"} section of the
`Access
Rights`{.interpreted-text role="guilabel"} tab.

-   In order for the user to appear as an approver for
    `Expenses`{.interpreted-text role="guilabel"}, they **must** have
    either `Team Approver`{.interpreted-text role="guilabel"},
    `All Approver`{.interpreted-text role="guilabel"}, or
    `Administrator`{.interpreted-text role="guilabel"} set for the
    `Expenses`{.interpreted-text role="guilabel"} role.
-   In order for the user to appear as an approver for
    `Time Off`{.interpreted-text role="guilabel"}, they **must** have
    either `Officer`{.interpreted-text role="guilabel"} or
    `Administrator`{.interpreted-text role="guilabel"} set for the
    `Time Off`{.interpreted-text role="guilabel"} role.
-   In order for the user to appear as an approver for
    `Timesheets`{.interpreted-text role="guilabel"}, they **must** have
    either `Manager`{.interpreted-text role="guilabel"},
    `Officer`{.interpreted-text role="guilabel"}, or
    `Administrator`{.interpreted-text role="guilabel"} set for the
    `Payroll`{.interpreted-text role="guilabel"} role.
:::

::: {.note}
::: {.title}
Note
:::

`Working Hours`{.interpreted-text role="guilabel"} are related to a
company\'s working times, and an employee **cannot** have working hours
that are outside of a company\'s working times.

Each individual working time is company-specific. So, for multi-company
databases, each company **must** have its own working hours set.

If an employee\'s working hours are not configured as a working time for
the company, new working times can be added, or existing working times
can be modified.

To add or modify a working time, go to the
`Payroll app --> Configuration -->
Working Schedules`{.interpreted-text role="menuselection"}. Then, either
add a new working time by clicking `New`{.interpreted-text
role="guilabel"}, or edit an existing one by selecting a
`Working Time`{.interpreted-text role="guilabel"} from the list to
modify it.

Refer to the
`Working schedules <payroll/working-times>`{.interpreted-text
role="ref"} section of the payroll documentation for specific details on
creating and editing working schedules.

After the new working time is created, or an existing one is modified,
the `Working
Hours`{.interpreted-text role="guilabel"} can be set on the employee
form. In the `Schedule`{.interpreted-text role="guilabel"} section of
the `Work Information`{.interpreted-text role="guilabel"} tab, select
the employee\'s working hours using the drop-down menu.
:::

### Private information tab {#employees/private-info}

No information in the `Private Information`{.interpreted-text
role="guilabel"} tab is required to create an employee, however, some
information in this section may be critical for the company\'s payroll
department. In order to properly process payslips and ensure all
deductions are accounted for, the employee\'s personal information
should be entered.

Here, the employee\'s `Private Contact`{.interpreted-text
role="guilabel"}, `Family Status`{.interpreted-text role="guilabel"},
`Emergency`{.interpreted-text role="guilabel"} contact,
`Education`{.interpreted-text role="guilabel"},
`Work Permit`{.interpreted-text role="guilabel"}, and
`Citizenship`{.interpreted-text role="guilabel"} information is entered.
Fields are entered either using a drop-down menu, ticking a checkbox, or
typing in the information.

-   `Private Contact`{.interpreted-text role="guilabel"}: enter the
    `Private Address`{.interpreted-text role="guilabel"},
    `Email`{.interpreted-text role="guilabel"}, and
    `Phone`{.interpreted-text role="guilabel"} for the employee. Then,
    enter the employee\'s `Bank Account Number`{.interpreted-text
    role="guilabel"} using the drop-down menu.

    If the bank is not already configured (the typical situation when
    creating a new employee), enter the bank account number, and click
    `Create and edit..`{.interpreted-text role="guilabel"}. A
    `Create Bank Account
    Number`{.interpreted-text role="guilabel"} form loads. Fill in the
    necessary information, then click `Save & Close`{.interpreted-text
    role="guilabel"}.

    Next, select the employee\'s preferred `Language`{.interpreted-text
    role="guilabel"} from the drop-down menu. Then enter the
    `Home-Work Distance`{.interpreted-text role="guilabel"} in the
    field. This field is only necessary if the employee is receiving any
    type of commuter benefits.

    Lastly, enter the employee\'s license plate information in the
    `Private Car Plate`{.interpreted-text role="guilabel"} field.

-   `Family Status`{.interpreted-text role="guilabel"}: select the
    current `Marital Status`{.interpreted-text role="guilabel"} using
    the drop-down menu, either `Single`{.interpreted-text
    role="guilabel"}, `Married`{.interpreted-text role="guilabel"},
    `Legal Cohabitant`{.interpreted-text role="guilabel"},
    `Widower`{.interpreted-text role="guilabel"}, or
    `Divorced`{.interpreted-text role="guilabel"}. If the employee has
    any dependent children, enter the `Number
    of Dependent Children`{.interpreted-text role="guilabel"} in the
    field.

-   `Emergency`{.interpreted-text role="guilabel"}: type in the
    `Contact Name`{.interpreted-text role="guilabel"} and
    `Contact Phone`{.interpreted-text role="guilabel"} number of the
    employee\'s emergency contact in the respective fields.

-   `Education`{.interpreted-text role="guilabel"}: select the highest
    level of education completed by the employee from the
    `Certificate Level`{.interpreted-text role="guilabel"} drop-down
    menu. Default options include `Graduate`{.interpreted-text
    role="guilabel"}, `Bachelor`{.interpreted-text role="guilabel"},
    `Master`{.interpreted-text role="guilabel"},
    `Doctor`{.interpreted-text role="guilabel"}, or
    `Other`{.interpreted-text role="guilabel"}.

    Type in the `Field of Study`{.interpreted-text role="guilabel"}, and
    the name of the `School`{.interpreted-text role="guilabel"} in the
    respective fields.

-   `Work Permit`{.interpreted-text role="guilabel"}: if the employee
    has a work permit, enter the information in this section. Type in
    the `Visa No`{.interpreted-text role="guilabel"} (visa number),
    and/or `Work Permit No`{.interpreted-text role="guilabel"} (work
    permit number) in the corresponding fields.

    Using the calendar selector, select the
    `Visa Expiration Date`{.interpreted-text role="guilabel"}, and/or
    the `Work Permit Expiration Date`{.interpreted-text
    role="guilabel"}, to enter the expiration date(s).

    If available, upload a digital copy of the
    `Work Permit`{.interpreted-text role="guilabel"} document. Click
    `Upload your file`{.interpreted-text role="guilabel"}, navigate to
    the work permit file in the file explorer, and click
    `Open`{.interpreted-text role="guilabel"}.

-   `Citizenship`{.interpreted-text role="guilabel"}: this section
    contains all the information relevant to the citizenship of the
    employee. Some fields use a drop-down menu, as the
    `Nationality (Country)`{.interpreted-text role="guilabel"},
    `Gender`{.interpreted-text role="guilabel"}, and
    `Country of Birth`{.interpreted-text role="guilabel"} fields do.

    The `Date of Birth`{.interpreted-text role="guilabel"} uses a
    calendar selector to select the date. First, click on the name of
    the month, then the year, to access the year ranges. Use the
    `< (left)`{.interpreted-text role="guilabel"} and
    `> (right)`{.interpreted-text role="guilabel"} arrow icons, navigate
    to the correct year range, and click on the year. Next, click on the
    month. Last, click on the day to select the date.

    Type in the information for the
    `Identification No`{.interpreted-text role="guilabel"}
    (identification number), `Passport No`{.interpreted-text
    role="guilabel"} (passport number), and
    `Place of Birth`{.interpreted-text role="guilabel"} fields.

    Lastly, if the employee is **not** a resident of the country they
    are working in, activate the checkbox next to the
    `Non-resident`{.interpreted-text role="guilabel"} field.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Depending on the localization setting, other fields may be present.
    For example, for the United States, a `SSN No`{.interpreted-text
    role="guilabel"} (Social Security Number) field is present.
    :::

### HR settings tab {#employees/hr-settings}

This tab provides various fields for different information, depending on
the country the company is located. Different fields are configured for
different locations, however some sections appear regardless.

-   `Status`{.interpreted-text role="guilabel"}: select an
    `Employee Type`{.interpreted-text role="guilabel"} and, if
    applicable, a `Related
    User`{.interpreted-text role="guilabel"}, with the drop-down menus.
    The `Employee Type`{.interpreted-text role="guilabel"} options
    include `Employee`{.interpreted-text role="guilabel"},
    `Student`{.interpreted-text role="guilabel"},
    `Trainee`{.interpreted-text role="guilabel"},
    `Contractor`{.interpreted-text role="guilabel"}, or
    `Freelancer`{.interpreted-text role="guilabel"}.

    ::: {.important}
    ::: {.title}
    Important
    :::

    Employees do **not** also need to be users. *Employees* do **not**
    count towards the Odoo subscription billing, while *Users* **do**
    count towards billing. If the new employee should also be a user,
    the user **must** be created.

    After the employee is created, click the
    `⚙️ (gear)`{.interpreted-text role="guilabel"} icon, then click
    `Create User`{.interpreted-text role="guilabel"}. A
    `Create User`{.interpreted-text role="guilabel"} form appears.

    Type in the `Name`{.interpreted-text role="guilabel"} and
    `Email Address`{.interpreted-text role="guilabel"}. Next, select the
    `Company`{.interpreted-text role="guilabel"} from the drop-down
    menu.

    Then, enter the `Phone`{.interpreted-text role="guilabel"} and
    `Mobile`{.interpreted-text role="guilabel"} numbers in the
    respective fields.

    If a photo is available, click the `Edit`{.interpreted-text
    role="guilabel"} icon (which appears as a `✏️
    (pencil)`{.interpreted-text role="guilabel"} icon) in the lower-left
    corner of the image box, which is located in the top-right corner of
    the form.

    A file explorer pops up. Navigate to the file, then click
    `Open`{.interpreted-text role="guilabel"} to select it. Finally,
    click `Save`{.interpreted-text role="guilabel"} after all the
    information is entered, and the employee record is automatically
    updated with the newly-created user populating the `Related User
    field`{.interpreted-text role="guilabel"}.

    Users can also be created manually. For more information on how to
    manually add a user, refer to the
    `../../general/users/`{.interpreted-text role="doc"} document.
    :::

-   `Attendance/Point of Sale/Manufacturing`{.interpreted-text
    role="guilabel"}: the employee\'s `PIN Code`{.interpreted-text
    role="guilabel"} and `Badge ID`{.interpreted-text role="guilabel"}
    can be entered here, if the employee needs/has one. Click
    `Generate`{.interpreted-text role="guilabel"} next to the
    `Badge ID`{.interpreted-text role="guilabel"} to create a badge ID.

    The `PIN Code`{.interpreted-text role="guilabel"} is used to sign in
    and out of the *Attendance* app kiosk, and a
    `POS (Point Of Sale)`{.interpreted-text role="abbr"} system.

-   `Payroll`{.interpreted-text role="guilabel"}: if applicable, enter
    the `Registration Number of the Employee`{.interpreted-text
    role="guilabel"} in this section.

    Depending on the localization setting, the other items that appear
    in this field vary based on location. In addition, other sections
    may appear in this tab based on location. It is recommended to check
    with the payroll and/or accounting departments to ensure this
    section, as well as any other sections relating to payroll that may
    appear, are filled in correctly.

-   `Application Settings`{.interpreted-text role="guilabel"}: enter the
    employee\'s `Billing Time Target`{.interpreted-text role="guilabel"}
    for the billing rate leader board in the *Timesheets* application.
    Next, enter the `Hourly Cost`{.interpreted-text role="guilabel"} in
    a XX.XX format. This is factored in when the employee is working at
    a `work center
    <../../inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers>`{.interpreted-text
    role="doc"}.

    If applicable, enter the `Fleet Mobility Card`{.interpreted-text
    role="guilabel"} number.

::: {.note}
::: {.title}
Note
:::

Manufacturing costs are added to the costs for producing a product, if
the value of the manufactured product is **not** a fixed amount. This
cost does **not** affect the *Payroll* application.
:::

{.align-center}

Documents {#employees/docs}
---------

All employee-related documents are stored in the *Documents* app. The
number of associated documents is displayed in the
`Documents`{.interpreted-text role="guilabel"} smart button above the
employee record. Click on the smart button to access all documents.

Refer to
`documentation <../../productivity/documents>`{.interpreted-text
role="doc"} on the *Documents* app for more information.

{.align-center}
