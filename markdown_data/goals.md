# File: /content/odoo_doc17.0/fr/content/applications/hr/appraisals/goals.md

Goals
=====

The Odoo *Appraisals* application allows managers to set goals for their
employees. That way, employees know what to work toward before their
next review.

To view all goals, navigate to
`Appraisals app --> Goals`{.interpreted-text role="menuselection"}. This
presents all the goals for every employee, in a default Kanban view.

::: {#appraisals/goal-card}
Each goal card contains the following information:
:::

-   `Goal`{.interpreted-text role="guilabel"}: the name of the goal.
-   `Employee`{.interpreted-text role="guilabel"}: the employee the goal
    is assigned to.
-   `fa-clock-o`{.interpreted-text role="icon"}
    `(clock)`{.interpreted-text role="guilabel"} icon: displays the
    corresponding `activity icon
    <../../essentials/activities>`{.interpreted-text role="doc"} for the
    record. If no activities are scheduled, the default icon is the
    `fa-clock-o`{.interpreted-text role="icon"}
    `(clock)`{.interpreted-text role="guilabel"}. If any activities have
    been scheduled, the icon represents the activity scheduled soonest.
-   `Deadline`{.interpreted-text role="guilabel"}: the due date for the
    goal.
-   `Progress`{.interpreted-text role="guilabel"}: the percentage of
    competency set for the goal. The options are `0%`{.interpreted-text
    role="guilabel"}, `25%`{.interpreted-text role="guilabel"},
    `50%`{.interpreted-text role="guilabel"}, `75%`{.interpreted-text
    role="guilabel"}, or `100%`{.interpreted-text role="guilabel"}.
-   `Employee Icon`{.interpreted-text role="guilabel"}: the profile icon
    of the employee the goal is assigned to.

If a goal is completed, a `Done`{.interpreted-text role="guilabel"}
banner appears in the top-right corner of the goal card.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Every individual goal requires its own record for each employee. If
multiple employees have the same goal, a goal card for each employee
appears on the list.

For example, if Bob and Sara have the same goal of [Typing]{.title-ref},
two cards appear in the Kanban view: one [Typing]{.title-ref} goal for
Bob, and another [Typing]{.title-ref} goal for Sara.
:::

New goal
--------

To create a new goal, navigate to
`Appraisals app --> Goals`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"} top-left corner to open a
blank goal form.

Input the `Goal`{.interpreted-text role="guilabel"},
`Employee`{.interpreted-text role="guilabel"},
`Progress`{.interpreted-text role="guilabel"}, and
`Deadline`{.interpreted-text role="guilabel"}, information on the goal
card, as discussed in the
`goal card <appraisals/goal-card>`{.interpreted-text role="ref"} section
of this document.

The information requested is all the same information that appears on
the goal card in the Kanban view, with the addition of a
`Tags`{.interpreted-text role="guilabel"} field and a
`Description`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

The *Appraisals* application does **not** have any pre-configured tags,
so all tags need to be added. To add a tag, enter the name of the tag on
the line, then click `Create
"(tag)"`{.interpreted-text role="guilabel"}. Repeat this for all tags
that need to be added.
:::

The current user populates the `Employee`{.interpreted-text
role="guilabel"} field, by default, and the `Manager`{.interpreted-text
role="guilabel"} field populates with the manager set on the employee
profile.

Make any necessary changes to the form, and add any notes that might be
useful to clarify the goal in the `Description`{.interpreted-text
role="guilabel"} tab.

{.align-center}

Completed goals
---------------

When a goal has been met, it is important to update the record. A goal
can be marked as [Done]{.title-ref} in one of two ways: from the main
`Goals`{.interpreted-text role="guilabel"} dashboard, or from the
individual goal card.

To mark a goal as [Done]{.title-ref} from the main
`Goals`{.interpreted-text role="guilabel"} dashboard, click on the
`fa-ellipsis-v`{.interpreted-text role="icon"}
`(vertical ellipsis)`{.interpreted-text role="guilabel"} icon in the
top-right of a goal card.

::: {.note}
::: {.title}
Note
:::

The `fa-ellipsis-v`{.interpreted-text role="icon"}
`(vertical ellipsis)`{.interpreted-text role="guilabel"} icon **only**
appears when the mouse hovers over the top-right corner of a goal card.
:::

Then, click `Mark as Done`{.interpreted-text role="guilabel"} from the
resulting drop-down menu. A green `Done`{.interpreted-text
role="guilabel"} banner appears in the top-right corner of the goal
card.

To mark a goal as [Done]{.title-ref} from the goal card itself, click on
a goal card to open that goal\'s form. Then, click the
`Mark as Done`{.interpreted-text role="guilabel"} button in the top-left
of the form. When clicked, a green `Done`{.interpreted-text
role="guilabel"} banner appears in the top-right corner of the goal
form.
