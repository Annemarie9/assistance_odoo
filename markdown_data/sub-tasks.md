# File: /content/odoo_doc17.0/fr/content/applications/services/project/tasks/sub-tasks.md

Sub-tasks
=========

When handling project tasks, you can often benefit from splitting the
workload into smaller **sub-tasks**, making it easier to track progress
and manage the work.

Odoo's sub-task feature is particularly useful in some of the following
cases:

-   The task workload is too big to handle in one record.
-   There's a clear sequence of steps to follow.
-   Some parts of the workload fall under the scope of different
    projects and/or assignees.

The original task to which sub-tasks are linked is referred to as the
**parent task**. The sub-tasks of the parent task are known as **child
tasks**.

Creating sub-tasks
------------------

To create a sub-task:

1.  Open the Project app, then go into your desired project.
2.  Click the task where you want to add the sub-task, then click the
    `Sub-tasks`{.interpreted-text role="guilabel"} tab.
3.  Click `Add a line`{.interpreted-text role="guilabel"}, then fill in
    the `Title`{.interpreted-text role="guilabel"}.
4.  Click the `fa-cloud-upload`{.interpreted-text role="icon"}
    (`save`{.interpreted-text role="guilabel"}) icon to save the task
    manually.

::: {.tip}
::: {.title}
Tip
:::

You can edit several fields of a sub-task directly from the parent
task's sub-task tab without opening the individual sub-task. By default,
those are: `Title`{.interpreted-text role="guilabel"},
`Priority`{.interpreted-text role="guilabel"},
`Status`{.interpreted-text role="guilabel"}, and
`Assignees`{.interpreted-text role="guilabel"}. Use the
`fa-sliders`{.interpreted-text role="icon"} (`sliders`{.interpreted-text
role="guilabel"}) icon to add or remove fields.
:::

Once the new sub-task is created, the following changes occur in the
parent task:

-   A **smart button** displays the total number of sub-tasks, as well
    as the number of closed (**done** or **canceled**) sub-tasks. Click
    the smart button to access the list of the sub-tasks.
-   The `Allocated time`{.interpreted-text role="guilabel"} displays the
    amount of time allocated to the parent task, as well as time
    allocated to the sub-tasks. This can be used to ensure that the time
    allocated to sub-tasks does not exceed time allocated to the parent
    task.
-   The `Timesheets`{.interpreted-text role="guilabel"} tab includes a
    breakdown of time spent on the parent task as well as sub-tasks.

Click `View`{.interpreted-text role="guilabel"} to open the sub-task you
created. The sub-task form is identical to the
`task form <task_creation/task-configuration>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

-   A **smart button** allows to navigate back to the
    `Parent task`{.interpreted-text role="guilabel"}.
-   The `Sub-tasks`{.interpreted-text role="guilabel"} tab allows for
    further creation of sub-tasks.
-   Selecting a `Project`{.interpreted-text role="guilabel"} will
    trigger this sub-task to be displayed in the Kanban view of the
    selected project.
:::
