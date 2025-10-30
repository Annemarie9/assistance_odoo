# File: /content/odoo_doc17.0/fr/content/applications/services/project/tasks/recurring_tasks.md

Recurring tasks
===============

When handling a project, the same task often needs to be performed
several times: for example, weekly meetings or status reports. The
**recurring tasks** feature allows you to automate the creation of those
tasks.

::: {.seealso}
[Odoo Tutorials: Recurring
tasks](https://www.odoo.com/slides/slide/recurring-tasks-6958)
:::

Configuration
-------------

To enable recurring tasks, go to
`Project --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, then activate `Recurring Tasks`{.interpreted-text
role="guilabel"}, and press `Save`{.interpreted-text role="guilabel"}.

### Set up task recurrence

In an existing task, click the `fa-repeat`{.interpreted-text
role="icon"} (`Recurrent`{.interpreted-text role="guilabel"}) button
next to the `Deadline`{.interpreted-text role="guilabel"} field. Then,
configure the `Repeat Every`{.interpreted-text role="guilabel"} field
according to your needs.

A new task in recurrence will be created once the status of the previous
task is set to `Done`{.interpreted-text role="guilabel"} or
`Canceled`{.interpreted-text role="guilabel"}.

The new task is created on the project dashboard with the following
configuration:

-   `Stage`{.interpreted-text role="guilabel"}: is set to the first
    stage of the project dashboard (`New`{.interpreted-text
    role="guilabel"} or equivalent);
-   `Name`{.interpreted-text role="guilabel"},
    `Description`{.interpreted-text role="guilabel"},
    `Project`{.interpreted-text role="guilabel"},
    `Assignees`{.interpreted-text role="guilabel"},
    `Customer`{.interpreted-text role="guilabel"},
    `Tags`{.interpreted-text role="guilabel"}: are copied from the
    original task;
-   `Deadline`{.interpreted-text role="guilabel"}: is updated based on
    the `Repeat Every`{.interpreted-text role="guilabel"} field (e.g.,
    if the task is set to repeat once a week, 7 days will be added to
    the deadline);
-   `Milestones`{.interpreted-text role="guilabel"},
    `Timesheets`{.interpreted-text role="guilabel"},
    `Chatter`{.interpreted-text role="guilabel"},
    `Activities`{.interpreted-text role="guilabel"},
    `Subtasks`{.interpreted-text role="guilabel"}: are **not** copied
    from the original task.

Once a recurrence is configured, a **smart button** on the task displays
the total number of existing recurrences.

### Edit or stop task recurrence

**To edit** the recurrence, open the last task in recurrence. Any
changes made on the task will be applied to the tasks that will be
created in the future.

**To stop** the recurrence, open the last task in recurrence and press
the `Recurrent`{.interpreted-text role="guilabel"} button next to the
`Planned date`{.interpreted-text role="guilabel"}.
