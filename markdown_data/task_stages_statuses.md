# File: /content/odoo_doc17.0/fr/content/applications/services/project/tasks/task_stages_statuses.md

Task stages and statuses
========================

Task stages
-----------

Task stages are displayed as columns in the project\'s Kanban view, and
allow you to update the progress of its tasks with a drag-and-drop. In
most projects, the stages will be akin to **New**, **In progress**,
**Backlog**, etc.

By default, task stages are project-specific but can be shared across
multiple projects that follow the same workflow.

### Creating task stages

Odoo Project doesn't provide default stages but instead allows you to
create custom stages tailored to your specific business needs. You are
prompted to do so immediately after `creating a new
project <project_management/configuration>`{.interpreted-text
role="ref"}.

To create a stage, type its name into the `Stage...`{.interpreted-text
role="guilabel"} field, then click `Add`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Click `See examples`{.interpreted-text role="guilabel"} to find ideas
for stage names applicable to your line of business.
:::

### Editing task stages

To edit the task stage, click the `fa-cog`{.interpreted-text
role="icon"} (`cog`{.interpreted-text role="guilabel"}) icon next to its
name. From there, click one of the following:

> -   `Fold`{.interpreted-text role="guilabel"}: to hide the task stage
>     and all of the tasks in this stage from the Kanban view.
> -   `Edit`{.interpreted-text role="guilabel"}:
>     -   `Name`{.interpreted-text role="guilabel"}: to change the name
>         of the stage.
>     -   `SMS/Email Template`{.interpreted-text role="guilabel"}: to
>         automatically send an email or SMS notification to the
>         customer when a task reaches this stage.
>     -   `Folded in Kanban`{.interpreted-text role="guilabel"}: to hide
>         the task stage and all of the tasks in this stage from the
>         Kanban view.
>     -   `Projects`{.interpreted-text role="guilabel"}: to share this
>         task stage between several projects.
>     -   `Automations`{.interpreted-text role="guilabel"}: to create
>         `custom rules that trigger automatic actions
>         <../../../studio/automated_actions>`{.interpreted-text
>         role="doc"} (e.g., creating activities, adding followers, or
>         sending webhook notifications). Note that this will activate
>         Studio in your database, which may impact your pricing plan.
> -   `Delete`{.interpreted-text role="guilabel"}: to delete this stage.
> -   `Archive/Unarchive all`{.interpreted-text role="guilabel"}: to
>     archive or unarchive all of the tasks in this stage.

Task statuses {#project/tasks/task_stages_statuses/statuses}
-------------

Task statuses are used to track the status of tasks within the Kanban
stage, as well as to close the task when it's done or canceled. Unlike
Kanban stages, they cannot be customized; five task statuses exist in
Odoo and are used as follows:

> -   `In Progress`{.interpreted-text role="guilabel"}: this is the
>     default state of all tasks, meaning that work required for the
>     task to move to the next Kanban stage is ongoing.
> -   `Changes Requested`{.interpreted-text role="guilabel"}: to
>     highlight that changes, either requested by the customer or
>     internally, are needed before the task is moved to the next Kanban
>     stage.
> -   `Approved`{.interpreted-text role="guilabel"}: to highlight that
>     the task is ready to be moved to the next stage.
> -   `Canceled`{.interpreted-text role="guilabel"}: to cancel the task.
> -   `Done`{.interpreted-text role="guilabel"}: to close the task once
>     it\'s been completed.

::: {.note}
::: {.title}
Note
:::

-   The `Changes Requested`{.interpreted-text role="guilabel"} and
    `Approved`{.interpreted-text role="guilabel"} task statuses are
    cleared as soon as the task is moved to another Kanban stage. The
    task status reverts to the default `In
    Progress`{.interpreted-text role="guilabel"} status so that
    `Changes Requested`{.interpreted-text role="guilabel"} or
    `Approved`{.interpreted-text role="guilabel"} status can be applied
    again once the necessary work has been completed in this Kanban
    stage.
-   The `Done`{.interpreted-text role="guilabel"} and
    `Canceled`{.interpreted-text role="guilabel"} statuses are
    independent from the Kanban stage. Once a task is marked as
    `Done`{.interpreted-text role="guilabel"} or
    `Canceled`{.interpreted-text role="guilabel"}, it is closed. If
    needed, it can be reopened by changing its status.
:::
