# File: /content/odoo_doc17.0/fr/content/applications/services/project/project_dashboard.md

Project dashboard
=================

The project dashboard allows you to get a comprehensive overview of your
project\'s status. It displays information such as the total number of
tasks, timesheets, and planned hours linked to the project, as well as
detailed information about project milestones and its costs and
revenues. Within the project dashboard, you can create
`Project updates`{.interpreted-text role="guilabel"}, which allow you to
take a snapshot of the project\'s status at a certain point in time. As
such, it is a crucial tool for effective project management and ensuring
that your project stays on track.

Using the project dashboard
---------------------------

To access the project dashboard, open the **Project** app and hover over
the desired project's card. Then, click the
`fa-vertical-ellipsis`{.interpreted-text role="icon"}
(`vertical ellipsis`{.interpreted-text role="guilabel"}) icon and select
`Dashboard`{.interpreted-text role="guilabel"}.

The left side of the dashboard displays a list of existing
`project updates <project/project-dashboard/updates>`{.interpreted-text
role="ref"}, and the right side provides
`detailed information about records linked to the project
<project/project-dashboard/smart-buttons>`{.interpreted-text
role="ref"}, as well as
`milestones <project/project-dashboard/milestones>`{.interpreted-text
role="ref"},
`profitability <project/project-dashboard/profitability>`{.interpreted-text
role="ref"}, and `budgets
<project/project-dashboard/budgets>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

The information displayed on the project dashboard varies depending on
the applications installed on your database. For example, you will not
see information about **Timesheets**, **Planning**, or **Purchase
Orders** if the corresponding applications are not installed.
:::

### Totals smart buttons {#project/project-dashboard/smart-buttons}

The following smart buttons are displayed on the top left of the project
dashboard:

> -   `Tasks`{.interpreted-text role="guilabel"}: the number of
>     completed (i.e., `Done`{.interpreted-text role="guilabel"} or
>     `Canceled`{.interpreted-text role="guilabel"}
>     `tasks <project/tasks/task_stages_statuses/statuses>`{.interpreted-text
>     role="ref"}) and all tasks, in format completed/all, as well as
>     the entire project\'s completion percentage estimation.
> -   `Timesheets`{.interpreted-text role="guilabel"}: the number of
>     hours or days (depending on the **Timesheets** app configuration)
>     linked to the project. This includes all
>     `timesheets <../timesheets>`{.interpreted-text role="doc"},
>     whether or not they have been validated.
> -   `Planned`{.interpreted-text role="guilabel"}: the number of hours
>     that have been planned for shifts in the **Planning** app. This
>     includes all `planned shifts <../planning>`{.interpreted-text
>     role="doc"}, including past shifts and shifts that have not yet
>     been published.
> -   `Documents`{.interpreted-text role="guilabel"}: number of
>     `documents <../../productivity/documents>`{.interpreted-text
>     role="doc"} in the project's workspace.
> -   `Burndown Chart`{.interpreted-text role="guilabel"}: click the
>     smart button to access a
>     `report </applications/essentials/reporting>`{.interpreted-text
>     role="doc"} on the status of the project's tasks over time.
> -   `Timesheets and Planning`{.interpreted-text role="guilabel"}:
>     click the smart button to access a
>     `report </applications/essentials/reporting>`{.interpreted-text
>     role="doc"} on the project's timesheets and shifts.
> -   **Additional fields**, such as `Sales Orders`{.interpreted-text
>     role="guilabel"}, `Sales Order Items`{.interpreted-text
>     role="guilabel"}, `Purchase Orders`{.interpreted-text
>     role="guilabel"}, and more, represent the number of records linked
>     to the project.

::: {.tip}
::: {.title}
Tip
:::

Use the project dashboard smart buttons to update the project records
easily. Click `Timesheets`{.interpreted-text role="guilabel"} to
validate timesheets, `Planned`{.interpreted-text role="guilabel"} to
create project planning, `Documents`{.interpreted-text role="guilabel"}
to view and validate documents, etc.
:::

### Milestones {#project/project-dashboard/milestones}

This section is only visible if
`milestones </applications/sales/sales/invoicing/milestone>`{.interpreted-text
role="doc"} have been created for this project. Click
`Add Milestone`{.interpreted-text role="guilabel"} to create a new
milestone. Click a milestone in the checklist to edit it, enable its
checkbox to mark it as completed, or click the
`fa-trash`{.interpreted-text role="icon"} (`trash`{.interpreted-text
role="guilabel"}) icon to remove it.

### Profitability {#project/project-dashboard/profitability}

This section only applies to billable projects and provides a breakdown
of project costs and revenues.

### Budgets {#project/project-dashboard/budgets}

If a budget has been set for the project, its status and related details
are displayed in this section. Click `Add Budget`{.interpreted-text
role="guilabel"} to create a new budget for the project.

::: {.note}
::: {.title}
Note
:::

`Analytic accounting </applications/finance/accounting/reporting/analytic_accounting>`{.interpreted-text
role="doc"} must be enabled in your database's **Accounting**
application in order for this section to be displayed.
:::

Project updates {#project/project-dashboard/updates}
---------------

Project updates allow you to take a snapshot of the project's overall
status at a given point in time, for example, during a periodic (weekly,
bi-weekly, or monthly) review. This allows you to compare specific data
points, note any aspects of the project that need improvement, and
estimate if the project is on or off track.

To create a new project update, go to the project dashboard, click
`New`{.interpreted-text role="guilabel"}, and fill in the following
fields:

> -   `Status`{.interpreted-text role="guilabel"}: Choose between
>     `On Track`{.interpreted-text role="guilabel"},
>     `At Risk`{.interpreted-text role="guilabel"}, `Off
>     Track`{.interpreted-text role="guilabel"},
>     `On Hold`{.interpreted-text role="guilabel"}, and
>     `Done`{.interpreted-text role="guilabel"}. Once the status is set,
>     a color-coded dot is displayed on the project's Kanban card,
>     allowing the project manager to easily identify which projects
>     need attention.
> -   `Progress`{.interpreted-text role="guilabel"}: Manually input the
>     completion percentage based on the project\'s progress.
> -   `Date`{.interpreted-text role="guilabel"} and
>     `Author`{.interpreted-text role="guilabel"}: These fields are
>     automatically filled in with appropriate information based on the
>     user who created the update and the current date.
> -   `Description`{.interpreted-text role="guilabel"}: Use this
>     rich-text field to gather notes. Depending on the project
>     configuration (e.g., if the project is billable), this field may
>     be pre-filled with current information on aspects such as
>     profitability, budget, milestones, etc.
