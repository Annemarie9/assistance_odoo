# File: /content/odoo_doc17.0/fr/content/applications/hr/appraisals/appraisal_analysis.md

Appraisal analysis
==================

The **Appraisals** app has the ability to report on all the appraisals
in the system, including past, present, and future appraisals, and their
respective statuses. This report helps managers track scheduled
appraisals, and identify any overdue or unconfirmed ones.

To access the *Appraisal Analysis* report, navigate to
`Appraisals app --> Reporting
--> Appraisal Analysis`{.interpreted-text role="menuselection"}.

On the `Appraisal Analysis`{.interpreted-text role="guilabel"} page, a
report loads, displaying all the appraisals in the database. Each entry
is highlighted in a different color to represent their status:

  -------------------------------------------------------------------------------------
  Color     Status                               Meaning
  --------- ------------------------------------ --------------------------------------
  Yellow    `Done`{.interpreted-text             The appraisal was completed.
            role="guilabel"}                     

  Orange    `Appraisal Sent`{.interpreted-text   The appraisal was confirmed, but not
            role="guilabel"}                     completed.

  Red       `Cancelled`{.interpreted-text        The appraisal was cancelled.
            role="guilabel"}                     

  Gray      `To Start`{.interpreted-text         The appraisal was scheduled, but not
            role="guilabel"}                     confirmed.
  -------------------------------------------------------------------------------------

::: {.note}
::: {.title}
Note
:::

Appraisals are scheduled automatically (appear in gray), according to
their respective `appraisals/appraisal-plan`{.interpreted-text
role="ref"}.
:::

The report displays the current year, in a default Gantt view, grouped
by department, with the current month highlighted.

To change the period of time that is presented, adjust the date settings
in the top-left corner of the report by clicking the default
`Year`{.interpreted-text role="guilabel"} to reveal a drop-down menu of
options. The options to display are `Day`{.interpreted-text
role="guilabel"}, `Week`{.interpreted-text role="guilabel"},
`Month`{.interpreted-text role="guilabel"}, and `Year`{.interpreted-text
role="guilabel"}. Use the adjacent arrows to move forward or backward in
time.

At any point, click the `Today`{.interpreted-text role="guilabel"}
button to have the Gantt view include today\'s date in the view.

To view the details of any appraisal, click on any appraisal. A pop-over
window appears, displaying the due date for the appraisal. To view more
details, click the `View`{.interpreted-text role="guilabel"} button, and
further details appear in a pop-up window.

The report can have other `filters <search/filters>`{.interpreted-text
role="ref"} and `groupings <search/group>`{.interpreted-text role="ref"}
set in the search bar at the top.

{.align-center}

Group by status {#appraisals/group-status}
---------------

When a company has a large number of employees, the default
`Appraisal Analysis`{.interpreted-text role="guilabel"} report may
display too much information to view easily. In this scenario, viewing
the data by status can be beneficial.

First, remove the default `oi-group`{.interpreted-text role="icon"}
`Department`{.interpreted-text role="guilabel"} grouping from the search
bar. Next, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon in the far-right
of the search bar. Click `Status`{.interpreted-text role="guilabel"} in
the `oi-group`{.interpreted-text role="icon"}
`Group By`{.interpreted-text role="guilabel"} column. Click away from
the drop-down menu to close it.

All the appraisals are now organized by status, in the following order:
`Cancelled`{.interpreted-text role="guilabel"}, `Done`{.interpreted-text
role="guilabel"}, `To Start`{.interpreted-text role="guilabel"}, and
`Appraisal Sent`{.interpreted-text role="guilabel"}.

This view makes it easy to see which appraisals need to be completed,
and when, as well as which appraisals still need to be confirmed.

{.align-center}

Use case: view only the user\'s appraisals
------------------------------------------

When viewing the `Appraisal Analysis`{.interpreted-text role="guilabel"}
report, it can save time to only view the appraisals the signed-in user
is responsible for, and hide the rest.

To only view this data, click the `fa-caret-down`{.interpreted-text
role="icon"} `(down arrow)`{.interpreted-text role="guilabel"} icon in
the far-right of the search bar, revealing a drop-down menu.

::: {.note}
::: {.title}
Note
:::

It is not necessary to remove the default `oi-group`{.interpreted-text
role="icon"} `Department`{.interpreted-text role="guilabel"} grouping.
If it remains active, the results are grouped by department. If it is
removed, the results appear in a list, alphabetically.
:::

Click `Add Custom Filter`{.interpreted-text role="guilabel"} at the
bottom of the `fa-filter`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} column, and a
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window
appears.

Click into the first field, and a pop-over appears with a variety of
options. Click the `fa-chevron-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon after the word
`Employee`{.interpreted-text role="guilabel"}, then scroll down and
click on `Manager`{.interpreted-text role="guilabel"}. Next, set the
middle field to `=`{.interpreted-text role="guilabel"}
`(equal)`{.interpreted-text role="guilabel"}. Last, click the third
field and select the desired user from the list. When all the fields are
set, click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

Now, the only appraisals that appear are the appraisals that the
selected user is responsible for, instead of viewing *all* the
appraisals.

This report can also be
`grouped by status <appraisals/group-status>`{.interpreted-text
role="ref"}.

{.align-center}

::: {.seealso}
\-
`Odoo essentials reporting <../../essentials/reporting>`{.interpreted-text
role="doc"} - `../../essentials/search`{.interpreted-text role="doc"}
:::
