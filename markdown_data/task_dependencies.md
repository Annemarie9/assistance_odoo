# File: /content/odoo_doc17.0/fr/content/applications/services/project/tasks/task_dependencies.md

Task dependencies
=================

Odoo Project allows you to break down projects into tasks and establish
relationships between those tasks to determine the order in which they
are executed. Task dependencies ensure that certain tasks begin only
after the preceding tasks are completed.

To enable task dependencies in projects, go to
`Project --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, enable
`Task Dependencies`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}.

Set task dependencies
---------------------

Task dependencies can be created from the task form or the project\'s
Gantt view by linking the successor task (i.e., the task blocked by
other tasks) to its predecessor task(s) (i.e., the tasks blocking the
successor task).

To create task dependencies from the task form, access the desired task
and, in the `Blocked by`{.interpreted-text role="guilabel"} tab, click
`Add a line`{.interpreted-text role="guilabel"}. Click
`View`{.interpreted-text role="guilabel"} to access the predecessor
task. To access the successor tasks from the predecessor task, click the
`Blocking Tasks`{.interpreted-text role="guilabel"} smart button.

To create a task dependency from the Gantt view, hover your mouse over
the predecessor task, then click one of the dots that appear around it.
Drag and drop the dot onto the successor task. An arrow appears,
indicating the dependency from the predecessor task to the successor.



Odoo automatically manages task progress based on their dependency.
Successor tasks are assigned the `Waiting`{.interpreted-text
role="guilabel"} status and cannot be moved to
`In Progress`{.interpreted-text role="guilabel"} until their predecessor
task(s) are marked as `Approved`{.interpreted-text role="guilabel"},
`Cancelled`{.interpreted-text role="guilabel"}, or
`Done`{.interpreted-text role="guilabel"}.

Remove dependencies
-------------------

To remove a task dependency, proceed as follows:

-   From the task form, go to the **Blocked by** tab and click the
    `fa-times`{.interpreted-text role="icon"} (`times`{.interpreted-text
    role="guilabel"}) button.
-   From the Gantt view, click the red `fa-times`{.interpreted-text
    role="icon"} (`times`{.interpreted-text role="guilabel"}) button
    that appears at the center of the arrow when you hover your mouse
    over it.
