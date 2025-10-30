# File: /content/odoo_doc17.0/fr/content/applications/services/planning.md

show-content

:   

Planning
========

**Odoo Planning** allows you to plan your team\'s schedule and manage
shifts and resources.

Handling your team\'s planning comes with specific requirements that may
vary widely depending on your business needs. The following concepts
were introduced in Odoo Planning to meet those needs:

**Shifts** are dispatched to **resources**, which can be either
`human <planning/employees>`{.interpreted-text role="ref"} (employees)
or `material <planning/materials>`{.interpreted-text role="ref"} (e.g.,
equipment). The resources are assigned
`roles <planning/roles>`{.interpreted-text role="ref"}, which allows for
organization of work within the team.

Once the initial configuration is done,
`planning shifts <planning/shifts>`{.interpreted-text role="ref"} can be
done manually or automated by using the
`Auto Plan <planning/open-shifts>`{.interpreted-text role="ref"}
feature.

An integration between the Planning and Sales apps allows the linking of
sold services to roles and shifts in Planning. Additionally, integration
with `Project <project>`{.interpreted-text role="doc"} allows dedicating
shifts, and thus time and resources, to specific projects.

::: {.seealso}

:::

Configuration {#planning/configuration}
-------------

### Roles {#planning/roles}

To define the roles your resources perform (e.g., chef, bartender,
waiter), go to `Planning --> Configuration --> Roles`{.interpreted-text
role="menuselection"}, then click `New`{.interpreted-text
role="guilabel"}, and fill in the `Name`{.interpreted-text
role="guilabel"} (e.g., assistant, receptionist, manager). Then, choose
the `Resources`{.interpreted-text role="guilabel"} that will perform
this role. Resources can be either
`Employees <planning/employees>`{.interpreted-text role="ref"} or
`Materials <planning/materials>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

\- If the Sales app is installed in your database, the
`Services`{.interpreted-text role="guilabel"} field appears, allowing
you to specify which roles are needed to perform services so that the
shifts are dispatched to the right person. - Roles are taken into
account when using the
`Auto Plan feature <planning/open-shifts>`{.interpreted-text
role="ref"}.
:::

#### Property fields and roles

**Property fields** allow you to add custom fields to forms across
several Odoo applications. Planning includes the possibility of adding
property fields linked to roles to shifts.

To create a property field, switch to the list view from any schedule.
From there, click `View`{.interpreted-text role="guilabel"} on the shift
that you wish to edit. If the `Role`{.interpreted-text role="guilabel"}
field is empty, fill it in with the desired role, then click the cog
icon and select `Add Properties`{.interpreted-text role="guilabel"}.
`Configure <../productivity/knowledge/properties>`{.interpreted-text
role="doc"} the new field according to your needs.



The property field is linked to the role and is included in the shift
form of all shifts performed by this role.

::: {.example}
Some of the use cases of role property fields include:

-   **Accreditation**: for roles that require a specific permit (e.g.,
    driving license)
-   **Location**: in companies that operate in multiple locations (e.g.,
    shops or restaurants)
-   **Language**: in a multi-lingual environment (e.g., consulting
    company)
:::

### Employees {#planning/employees}

All employees can be included in the planning and assigned shifts.

To adapt the employee\'s planning settings, go to
`Planning --> Configuration -->
Employees`{.interpreted-text role="menuselection"}, and choose the
employee for whom you want to edit the settings. Then, go to the
`Work Information`{.interpreted-text role="guilabel"} tab.



::: {.tip}
::: {.title}
Tip
:::

You can do the same from the **Employees** app, which is installed by
default along with Planning.
:::

Two sections of the employee\'s `Work Information`{.interpreted-text
role="guilabel"} tab have an impact on Planning:
`Schedule`{.interpreted-text role="guilabel"} (namely, the
`Working Hours`{.interpreted-text role="guilabel"} field) and
`Planning`{.interpreted-text role="guilabel"}.

#### Working hours {#planning/working-hours}

The `Working Hours`{.interpreted-text role="guilabel"} are taken into
account when the `Allocated Time`{.interpreted-text role="guilabel"} and
its percentage is calculated for
`shifts <planning/templates>`{.interpreted-text role="ref"}. If the
`Working Hours`{.interpreted-text role="guilabel"} field is left blank,
the employee is considered to be working flexible hours.

To create individual `Working Hours`{.interpreted-text role="guilabel"},
for example, for employees working part-time, click
`Search more...`{.interpreted-text role="guilabel"}, then
`New`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Working Hours`{.interpreted-text role="guilabel"} and the
`Allocated Time`{.interpreted-text role="guilabel"} in Planning can
impact **Payroll**, if the employee\'s contract is configured to
generate work entries based on shifts.
:::

::: {.seealso}
`Payroll documentation on working schedules <payroll/working-times>`{.interpreted-text
role="ref"}
:::

#### Planning roles

Once an employee has one or more `Roles`{.interpreted-text
role="guilabel"}:

-   When creating a shift for this employee, only the shift templates
    from the roles chosen in this field are displayed.
-   When a schedule is published, the employee is only notified of open
    shifts for the roles that are assigned to them.
-   When auto-assigning open shifts or planning sales orders, the
    employee is only assigned shifts for the roles assigned to them.

Additionally, when a `Default role`{.interpreted-text role="guilabel"}
is defined:

-   When creating a shift for the employee, the default role is
    automatically selected.
-   This role also has precedence over the other roles of the employee
    when auto-assigning open shifts or planning sales orders.

::: {.note}
::: {.title}
Note
:::

If the Planning roles fields are left empty, there are no restrictions
in the shift templates and open shifts shared with the employee.
However, it's not possible to use the **Auto Plan** feature for employee
with no roles.
:::

### Materials {#planning/materials}

**Materials** are resources that can be assigned shifts and working
hours but are not employees. For example, a construction company could
use materials to create shifts for shared machines (e.g., cranes,
forklifts).

Similarly to employees, materials can be assigned roles and working
time.

### Shift templates {#planning/templates}

To create a shift template, click `New`{.interpreted-text
role="guilabel"} on any schedule, then fill in the
`details of the shift <planning/create-shift>`{.interpreted-text
role="ref"}. In order for the shift to be saved as a template, tick
`Save as Template`{.interpreted-text role="guilabel"}.



Alternatively, you can go to
`Planning --> Configuration --> Shift Templates`{.interpreted-text
role="menuselection"}, then click `New`{.interpreted-text
role="guilabel"}. Fill in the `Start Hour`{.interpreted-text
role="guilabel"} and `Shift Duration`{.interpreted-text
role="guilabel"}. The shift's `End Time`{.interpreted-text
role="guilabel"} is then calculated based on the
`Working Hours`{.interpreted-text role="guilabel"}, taking into account
working time as well as breaks.

::: {.example}
The employee\'s working hours are Monday to Friday, 8 am to 5 pm, with a
break between 12 and 1 pm.

-   Creating a shift template with a start hour of 9 am and a duration
    of 8 hours will result in the end hour being 5 pm, based on the
    working hours and the 1-hour break.
-   Creating a shift template with a start hour of 10 am and a duration
    of 10 hours will result in the end hour of 10 am the following day,
    as the company is closed at 5 pm according to the working hours.
:::

Additionally, for each shift template, you can also configure:

-   `Role`{.interpreted-text role="guilabel"}: to link the shift to this
    specific role.
-   `Project`{.interpreted-text role="guilabel"}: to keep track of
    shifts that are dedicated to work on a project.

Planning shifts {#planning/shifts}
---------------

On opening the Planning app, the users see their own schedule. Users
with admin roles can also see `Schedule by Resource`{.interpreted-text
role="guilabel"}, `Role`{.interpreted-text role="guilabel"},
`Project`{.interpreted-text role="guilabel"}, or
`Sales Order`{.interpreted-text role="guilabel"}, as well as reporting
and configuration menus.

::: {.note}
::: {.title}
Note
:::

The schedule is displayed in the Gantt view, which allows you to edit
(with a drag and drop), resize, split, and duplicate shifts without
having to open them.
:::



The following visual elements are used on the shifts in the schedules:

-   **Full color**: shifts that are planned and published.
-   **Diagonal stripes**: shifts that are planned but have yet to be
    published.
-   **Grayed-out background**: employees that are on time off.
-   **Progress bar**: currently ongoing shifts with timesheets linked to
    them.
-   **Grayed-out shift**: when copying shifts, the copied shifts are
    shown in full color, whereas previously existing shifts are
    temporarily greyed out. The color changes back to full color or
    diagonal stripes on the next refresh of the page or by removing the
    filter.

### Create a shift {#planning/create-shift}

To create a shift, go to any schedule, then click
`New`{.interpreted-text role="guilabel"}. In the pop-up window that
opens, fill in the following details:

-   **Templates**: If there is one or more templates existing in your
    database, they are displayed in the upper section of the pop-up
    window. Once selected, a template prefills the shift form
    accordingly.
-   `Resource`{.interpreted-text role="guilabel"}: Resources can be both
    employees or materials. If this field is left empty, the shift is
    considered an `open shift <planning/open-shifts>`{.interpreted-text
    role="ref"}.
-   `Role`{.interpreted-text role="guilabel"}: Select the role that the
    resource assigned will be performing. This field is used when
    `auto-planning <planning/open-shifts>`{.interpreted-text role="ref"}
    shifts. Once you select a role, the shift templates associated with
    it are displayed in the upper section of the pop-up window.
-   `Project`{.interpreted-text role="guilabel"}: If the Project app is
    installed in your database, this field allows you to link the
    project to the shift is available, allowing you to plan and track
    shifts dedicated to work on the selected project.
-   `Sales Order Item`{.interpreted-text role="guilabel"}: If the Sales
    app is installed in your database, this field allows you to link a
    sales order to the shift.
-   `Repeat`{.interpreted-text role="guilabel"}: Tick the checkbox and
    configure the `Repeat Every`{.interpreted-text role="guilabel"}
    field according to your needs. The following rules apply to
    recurring shifts:
    -   All fields (e.g., `Resource`{.interpreted-text role="guilabel"},
        `Role`{.interpreted-text role="guilabel"},
        `Project`{.interpreted-text role="guilabel"}) are copied from
        the original shift except for the date, which is adjusted
        according to the `Repeat Every`{.interpreted-text
        role="guilabel"} field.
    -   Recurrences are planned but not published.
    -   By default, planned shifts are created six months in advance,
        after which they are created gradually. To change the time
        frame,
        `activate the Developer mode <developer-mode>`{.interpreted-text
        role="ref"}, then go to
        `Planning --> Configuration --> Settings`{.interpreted-text
        role="menuselection"} and edit the
        `Recurring Shifts`{.interpreted-text role="guilabel"}.
-   `Save as Template`{.interpreted-text role="guilabel"}: When this
    option is ticked, a shift template is created with the same
    `Start and End hours`{.interpreted-text role="guilabel"},
    `Allocated time`{.interpreted-text role="guilabel"},
    `Role`{.interpreted-text role="guilabel"}, and
    `Project`{.interpreted-text role="guilabel"}.
-   `Additional note sent to the employee`{.interpreted-text
    role="guilabel"}: Click on the field to add a note.
-   `Date`{.interpreted-text role="guilabel"}: Choose the date and time
    of your shift. This is the only mandatory field when creating a
    shift.
-   `Allocated time`{.interpreted-text role="guilabel"}: Is calculated
    based on the date and the employee's `Working
    Schedule`{.interpreted-text role="guilabel"}. See more in
    `Shift Templates <planning/templates>`{.interpreted-text
    role="ref"}.

Click `Publish & Save`{.interpreted-text role="guilabel"} to confirm the
shift and send the assigned employee their schedule by email.

::: {.note}
::: {.title}
Note
:::

The draft is visible on the admin planning view and can be identified by
diagonal lines. The employee is only notified of the shift once it\'s
published.

Two kinds of notifications are sent to the employees depending on their
account configuration:

-   Employees without user accounts are redirected to a dedicated
    **Planning portal**.
-   Employees with a user account are redirected to the
    `My Planning`{.interpreted-text role="guilabel"} view in the backend
    view of Odoo.
:::

::: {.tip}
::: {.title}
Tip
:::

The **split shifts** tool allows to easily split a long shift into
segments. To do so, hover the mouse over the desired shift and click the
`fa-scissors`{.interpreted-text role="icon"}
(`scissors`{.interpreted-text role="guilabel"}) icon.


:::

### Open shifts and auto planning {#planning/open-shifts}

The `Auto Plan`{.interpreted-text role="guilabel"} button allows you to
assign **Open shifts** (shifts with no resource assigned) and create and
assign shifts linked to sales orders or project.

The following features have an impact on auto planning:

-   **Roles**: Open shifts are only assigned to resources (employees or
    materials) that have the corresponding role assigned. It is not
    possible to use the `Auto Plan`{.interpreted-text role="guilabel"}
    feature for employee with no roles.
-   **Default roles**: The default role assigned to a resource is given
    priority over the other roles they have assigned to them.
-   **Conflicts**: Employees or materials cannot be assigned multiple
    shifts at the same time.
-   **Time off**: The employees' time off is taken into account, as well
    as public holidays.
-   **Working hours**: Are taken into account when assigning shifts to
    employees or materials. It is not possible to use the
    `Auto Plan`{.interpreted-text role="guilabel"} feature for an
    employee who is working
    `flexible hours <planning/working-hours>`{.interpreted-text
    role="ref"}.
-   **Contracts**: If the employee has an active contract, they won\'t
    be assigned shifts that fall outside of their contract period.

Click `Publish`{.interpreted-text role="guilabel"} to confirm the
schedule and notify the employees of their planning.

### Switching shifts and unassignment {#planning/switching-unassignment}

Two features are available to allow employees to make changes to their
schedule: **switching shifts** and **unassignment**.

::: {.note}
::: {.title}
Note
:::

These features are mutually exclusive. Switching shifts is possible by
default and cannot be disabled. However, once the **Allow unassignment**
feature is enabled, it replaces the option to switch shifts.
:::

#### Switching shifts

Once shifts are planned and published, employees receive an email
notification. If an employee wishes to switch a shift, they can click
the unwanted shift and click `Ask to switch`{.interpreted-text
role="guilabel"}.

The shift remains assigned to the original employee, but in the
schedule, a notification informing that the assigned employee would like
to switch shifts is visible on the shift.

The shift is then displayed to other employees who share the same role,
and if they wish to assign it to themselves, they can click the
`I take it`{.interpreted-text role="guilabel"} button.

::: {.note}
::: {.title}
Note
:::

The following rules apply:

-   Only the shifts matching the employee\'s roles are displayed as
    available to them.
-   Switching shifts is not available for shifts in the past.
:::

#### Unassignment

To allow employees to unassign themselves from shifts, go to
`Planning --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, then tick the checkbox
`Allow Unassignment`{.interpreted-text role="guilabel"}. Then, specify
the maximum number of days that the employees can unassign themselves
before the shift.

Once shifts are planned and published, employees receive an email
notification. If shift unassignment is allowed, the employees can click
the `I am unavailable`{.interpreted-text role="guilabel"} button, and
the shift reverts to an open shift.

::: {.note}
::: {.title}
Note
:::

The following rules apply:

-   Only the shifts matching the employee\'s roles are displayed in
    their schedule.
-   Unassigning shifts is not available for shifts in the past.
:::
