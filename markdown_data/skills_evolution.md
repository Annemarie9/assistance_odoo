# File: /content/odoo_doc17.0/fr/content/applications/hr/appraisals/skills_evolution.md

Skills evolution
================

In Odoo\'s **Appraisals** app, it is possible to view employee\'s skills
as they progress over time in the
`Skills Evolution <appraisals/identify-skills-evolution>`{.interpreted-text
role="ref"} report, also known as the *Appraisal Skills Report*.

Managers can use this to see who is achieving their various skill goals
set on their appraisals, who is meeting their skill deadlines, who has
the highest performance in terms of skill development, and more.

The *Skills Evolution* report also provides the ability to
`search for employees with specific
skills <appraisals/identify-skills>`{.interpreted-text role="ref"} at
certain levels, which can be helpful for scenarios where specific skills
are required.

Skills evolution report {#appraisals/identify-skills-evolution}
-----------------------

To access this *Skills Evolution* report, navigate to
`Appraisals app --> Reporting
--> Skills Evolution`{.interpreted-text role="menuselection"}.

Doing so reveals the `Appraisal Skills Report`{.interpreted-text
role="guilabel"} page, which displays a report of all skills, grouped by
employee, in alphabetical order, by default.

::: {.note}
::: {.title}
Note
:::

Skill levels are **only** updated after an appraisal is marked as done.
Any skill level changes from ongoing appraisals that have **not** been
finalized are **not** included in this report.
:::

All the `Employee`{.interpreted-text role="guilabel"} lines are
expanded, with all the various skill types nested below. Each individual
skill type is collapsed, by default. To view the individual skills
contained within a skill type, click anywhere on the skill type line to
expand the data.

Each skill has the following information listed:

-   `Employee`{.interpreted-text role="guilabel"}: the name of the
    employee.
-   `Skill Type`{.interpreted-text role="guilabel"}: the category the
    skill falls under.
-   `Skill`{.interpreted-text role="guilabel"}: the specific, individual
    skill.
-   `Previous Skill Level`{.interpreted-text role="guilabel"}: the level
    the employee had previously achieved for the skill.
-   `Previous Skill Progress`{.interpreted-text role="guilabel"}: the
    previous percentage of competency achieved for the skill (based on
    the `Skill Level`{.interpreted-text role="guilabel"}).
-   `Current Skill Level`{.interpreted-text role="guilabel"}: the
    current level the employee has achieved for the skill.
-   `Current Skill Progress`{.interpreted-text role="guilabel"}: the
    current percentage of competency achieved for the skill.
-   `Justification`{.interpreted-text role="guilabel"}: any notes
    entered on the skill, explaining the progress.

The color of the skill text indicates any changes from the previous
appraisal. Skill levels that have increased since the last appraisal
appear in green, as an *Improvement*. Skill levels that have **not**
changed appear in black, as *No Change*. Skills that have regressed
appear in red, as *Regression*.

This report can be modified to find specific information by adjusting
the `filters
<search/filters>`{.interpreted-text role="ref"} and
`groupings <search/group>`{.interpreted-text role="ref"} set in the
search bar at the top.

{.align-center}

Use case: Identify employees with specific skills {#appraisals/identify-skills}
-------------------------------------------------

Since the `Appraisal Skills Report`{.interpreted-text role="guilabel"}
organizes all skills by employee, it can be difficult to find employees
with a specific skill at a specific level. To find these employees, a
custom filter must be used.

In this example, the report is modified to show employees with an expert
level of Javascript knowledge. To view only those employees, first
remove all active filters in the search bar.

Next, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, then click `Add Custom Filter`{.interpreted-text role="guilabel"}
beneath the `fa-filters`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} column to load an
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

Using the drop-down menu in the first field, select
`Skill`{.interpreted-text role="guilabel"}. Then, keep the second field
as-is, and select `Javascript`{.interpreted-text role="guilabel"} from
the third drop-down menu in the third field.

Next, click `New Rule`{.interpreted-text role="guilabel"}, and another
line appears. In this second line, select
`Current Skill Level`{.interpreted-text role="guilabel"} for the first
drop-down field, leave the second field as-is, then select
`Expert`{.interpreted-text role="guilabel"} for the third drop-down
field.

After the `New Rule`{.interpreted-text role="guilabel"} button is
clicked, the word `"any"`{.interpreted-text role="guilabel"} in the
sentence `Match any of the following rules:`{.interpreted-text
role="guilabel"}, changes from plain text into a drop-down menu. Click
the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon after the word
`any`{.interpreted-text role="guilabel"}, and select
`all`{.interpreted-text role="guilabel"}.

Finally, click the `Add`{.interpreted-text role="guilabel"} button.

{.align-center}

Now, only employees that have an `Expert`{.interpreted-text
role="guilabel"} level for the skill `Javascript`{.interpreted-text
role="guilabel"} appear. In this example, only
`Marc Demo`{.interpreted-text role="guilabel"} meets these criteria.

{.align-center}

::: {.seealso}
\-
`Odoo essentials reporting <../../essentials/reporting>`{.interpreted-text
role="doc"} - `../../essentials/search`{.interpreted-text role="doc"}
:::
