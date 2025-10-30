# File: /content/odoo_doc17.0/fr/content/applications/hr/employees/departments.md

Departments
===========

All employees in the *Employees* app fall under specific departments
within a company.

Create new departments
----------------------

To make a new department, navigate to
`Employees app --> Departments`{.interpreted-text role="menuselection"},
then click `New`{.interpreted-text role="guilabel"} in the top-left to
reveal a blank department form. Fill out the following information on
the department form:

{.align-center}

-   `Department Name`{.interpreted-text role="guilabel"}: enter a name
    for the department.
-   `Manager`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the department manager.
-   `Parent Department`{.interpreted-text role="guilabel"}: if the new
    department is housed within another department (has a parent
    department), select the parent department using the drop-down menu.
-   `Custom Appraisal Templates`{.interpreted-text role="guilabel"}: if
    employees in this department require a specific appraisal form that
    is different from the default appraisal form, tick the checkbox. If
    this option is activated, an `Appraisal Templates`{.interpreted-text
    role="guilabel"} tab appears below the form. This field **only**
    appears if the *Appraisals* app is installed.
-   `Company`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the company the department is part of.
-   `Appraisal Survey`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the default survey to use for the department
    when requesting feedback from employees. This field **only** appears
    if the *Appraisals* app is installed, **and** the *360 Feedback*
    option is enabled in the settings.
-   `Color`{.interpreted-text role="guilabel"}: select a color for the
    department. Click the default white color box to display all the
    color options. Click on a color to select it.
-   `Appraisal Templates`{.interpreted-text role="guilabel"} tab: this
    tab **only** appears if the `Custom Appraisal
    Templates`{.interpreted-text role="guilabel"} options is activated
    on the form. Make any desired edits to the appraisal form. The
    appraisal form is used for appraisals for all employees within this
    department.

After the form is completed, click the
`fa-cloud-upload`{.interpreted-text role="icon"}
`(cloud upload)`{.interpreted-text role="guilabel"} icon to manually
save the changes. When saved, a
`Department Organization`{.interpreted-text role="guilabel"} chart
appears in the top-right of the department card.

::: {.note}
::: {.title}
Note
:::

The form auto-saves while data is entered, however the
`Department Organization`{.interpreted-text role="guilabel"} chart does
**not** appear until the form is manually saved. If the form is not
saved, the `Department Organization`{.interpreted-text role="guilabel"}
chart is visible upon opening the department card from the
`Departments`{.interpreted-text role="guilabel"} dashboard.
:::

::: {.seealso}
Refer to the `../appraisals`{.interpreted-text role="doc"} documentation
for more information.
:::

Departments dashboard
---------------------

To view the currently configured departments, navigate to
`Employees app -->
Departments`{.interpreted-text role="menuselection"}. All departments
appear in a Kanban view, by default, and are listed in alphabetical
order.

{.align-center}

### Kanban view

Each department has its own Kanban card on the main
`Departments`{.interpreted-text role="guilabel"}
`oi-view-kanban`{.interpreted-text role="icon"}
`(Kanban)`{.interpreted-text role="guilabel"} dashboard view, that can
display the following information:

-   Department name: the name of the department.
-   Company: the company the department is part of.
-   `Employees`{.interpreted-text role="guilabel"}: the number of
    employees within the department.
-   `Appraisals`{.interpreted-text role="guilabel"}: the number of
    appraisals scheduled for employees in the department.
-   `Time Off Requests`{.interpreted-text role="guilabel"}: the number
    of unapproved time off requests for employees in the department
    `awaiting approval <time_off/manage-time-off>`{.interpreted-text
    role="ref"} . This **only** appears if there are requests to
    approve.
-   `Allocation Requests`{.interpreted-text role="guilabel"}: the number
    of unapproved allocation requests for employees in the department
    `awaiting approval <time_off/manage-allocations>`{.interpreted-text
    role="ref"}. This **only** appears if there are requests to approve.
-   `New Applicants`{.interpreted-text role="guilabel"}: the number of
    `new applicants <recruitment/new>`{.interpreted-text role="ref"} for
    a position in this department. This **only** appears if there are
    new applicants.
-   `Expense Reports`{.interpreted-text role="guilabel"}: the number of
    employees in the department with `open expense
    reports to approve <../../finance/expenses/approve_expenses>`{.interpreted-text
    role="doc"}. This **only** appears if there are any expense reports
    waiting for approval.
-   `Absence`{.interpreted-text role="guilabel"}: the number of absences
    for the current day.
-   Color bar: the selected color for the department appears as a
    vertical bar on the left side of the department card.

::: {.note}
::: {.title}
Note
:::

Click on an alert in a department card, such as
`Time Off Requests`{.interpreted-text role="guilabel"}, to reveal a list
view of the requests to approve. This list includes **all** open
requests to approve, not just from the specific department.
:::

The default view for the `Departments`{.interpreted-text
role="guilabel"} dashboard is a Kanban view. It is possible to view the
departments in two other forms: a list view and a hierarchy view.

### List view

To view the departments in a list view, click the
`fa-align-justify`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon in the top-right
corner. The departments appear in a list view, which displays the
`Department Name`{.interpreted-text role="guilabel"},
`Company`{.interpreted-text role="guilabel"},
`Manager`{.interpreted-text role="guilabel"},
`Employees`{.interpreted-text role="guilabel"},
`Parent Department`{.interpreted-text role="guilabel"}, and
`Color`{.interpreted-text role="guilabel"} for each department.

The departments are sorted alphabetically by
`Department Name`{.interpreted-text role="guilabel"}, by default.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

When in list view, departments can be managed in batch by selecting one
or multiple record\'s checkbox, then select the
`fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
role="guilabel"} button to reveal a drop-down menu of actions.
:::

### Hierarchy view

To view the departments in a hierarchy view, click the
`fa-share-alt fa-rotate-90`{.interpreted-text role="icon"}
`(hierarchy)`{.interpreted-text role="guilabel"} icon in the top-right
corner. The departments appear in an organizational chart format, with
the highest-level department at the top (typically
`Management`{.interpreted-text role="guilabel"}), and all other
departments beneath it. All child departments of the first-level child
departments are folded.

Each department card displays the `Department Name`{.interpreted-text
role="guilabel"}, the `Manager`{.interpreted-text role="guilabel"} (and
their profile image), the `Number of Employees`{.interpreted-text
role="guilabel"} in the department, and the ability to expand the
department (`Unfold`{.interpreted-text role="guilabel"}) if there are
child departments beneath it.

Click the `Unfold`{.interpreted-text role="guilabel"} button on a
department card to expand it. Once expanded, the
`Unfold`{.interpreted-text role="guilabel"} button changes to a
`Fold`{.interpreted-text role="guilabel"} button. To collapse the
department, click the `Fold`{.interpreted-text role="guilabel"} button.
Only **one** department *per row* can be unfolded at a time.

Click anywhere on a department card to open the department form. Click
the `(#) Employees`{.interpreted-text role="guilabel"} smart button to
view a list of all the employees in that department, including all
employees in the child departments beneath it, organized by individual
department.

::: {.example}
In the hierarchy view, if the `(2) Employees`{.interpreted-text
role="guilabel"} button on the `Management`{.interpreted-text
role="guilabel"} card is clicked (the highest-level department card),
**all** employees appear in a list view, grouped by department. This is
because **all** departments are children of the
`Management`{.interpreted-text role="guilabel"} department.

If the `(3) Employees`{.interpreted-text role="guilabel"} button in the
`Sales`{.interpreted-text role="guilabel"} department card is clicked,
the employees from the `Sales`{.interpreted-text role="guilabel"}
department, as well as its two child departments
(`East Coast Territory`{.interpreted-text role="guilabel"} and
`West Coat Territory`{.interpreted-text role="guilabel"}), appear in the
list.

{.align-center}

![The list view of employees for the department that was clicked, including all child
departments.](departments/employee-list.png){.align-center}
:::
