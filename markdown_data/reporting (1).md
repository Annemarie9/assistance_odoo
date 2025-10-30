# File: /content/odoo_doc17.0/fr/content/applications/hr/referrals/reporting.md

Reporting
=========

The reporting function in the **Referrals** app helps recruiters and
managers learn where applicants are applying from, when referred by a
current employee. Additionally, the reporting feature shows the number
of applicants hired, refused, and still in the recruitment pipeline, for
each medium.

::: {.important}
::: {.title}
Important
:::

Only users with *Administrator* rights for the **Recruitment** app have
access to the reporting feature in the **Referrals** app.
:::

Employees referral analysis report
----------------------------------

To access the *Employees Referral Analysis* report, navigate to
`Referrals app -->
Reporting`{.interpreted-text role="menuselection"}. This loads the
`Employees Referral Analysis`{.interpreted-text role="guilabel"} report,
in a default `fa-bar-chart`{.interpreted-text role="icon"}
`Bar Chart`{.interpreted-text role="guilabel"}.

The graph is presented in a `fa-database`{.interpreted-text role="icon"}
`Stacked`{.interpreted-text role="guilabel"} view, with the number of
referrals on the y-axis, and the source, referred to as the
`Medium`{.interpreted-text role="guilabel"}, of the applicant (e.g.:
*Facebook*, *LinkedIn*, *Email*, etc.) on the x-axis. If a medium does
**not** appear on the report, that indicates there are no referrals from
that particular medium.

Referral amounts for all stages are displayed, including
`Not Hired`{.interpreted-text role="guilabel"} (refused),
`In Progress`{.interpreted-text role="guilabel"}, and
`Hired`{.interpreted-text role="guilabel"}. The default filter is set to
the current month.

Hover over any bar to view a popover containing specific data for that
particular bar.

In this view, it is easy to see which `Medium`{.interpreted-text
role="guilabel"} is the most successful.

::: {.example}
In this example, both `Email`{.interpreted-text role="guilabel"} and
`LinkedIn`{.interpreted-text role="guilabel"} are the mediums with the
most referrals, but `Email`{.interpreted-text role="guilabel"} has the
most referrals that were hired.

{.align-center}
:::

### Use case: hired referrals

One way to use the reporting feature is to assess which employees are
referring the highest quality applicants. This is done by examining how
many of their referrals go on to become employees.

In this example, data is examined to determined which employee has the
highest number of hired referrals for the current year.

To view this information, first click the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the upper-right
corner. Next, remove the current filter in the search bar.

Click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} in the search bar to
reveal a drop-down menu. Click `Date`{.interpreted-text role="guilabel"}
in the `fa-filter`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} column, revealing a
drop-down menu of available time periods, and click the current year (in
this example, `2024`{.interpreted-text role="guilabel"}).

Next, click `Measures`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"}, then deselect
`Earned Points`{.interpreted-text role="guilabel"} and
`Employee Referral Refused`{.interpreted-text role="guilabel"} to hide
those metrics. Click anywhere on the screen to close the drop-down menu.

The information displayed shows how many total applicants each employee
referred, and how many of those applicants were hired, for the current
year.

In this example, it can be determined that
`Bob Wilson`{.interpreted-text role="guilabel"} is the most successful
referrer, with three hired referrals, and nine total referred
applicants. Additionally, `Mitchell
Admin`{.interpreted-text role="guilabel"} has the lowest performance in
terms of referrals, as he has only one applicant, and no hires.

This information can be helpful to the recruitment team, so they can
determine the most active referrers in the company, and who is the most
successful in terms of hires.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

The pivot table can be inserted into a new or existing `spreadsheet
<../../productivity/spreadsheet/insert>`{.interpreted-text role="doc"},
if desired.

To do so, click the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button right above the chart. A pop-up window appears,
asking which spreadsheet to insert the pivot chart into. Select the
desired spreadsheet or dashboard from the presented options.
Alternatively, select `Blank
Spreadsheet`{.interpreted-text role="guilabel"} to create a new one.

Click `Confirm`{.interpreted-text role="guilabel"}, and the selected
spreadsheet loads, with the new table in it.

The spreadsheet is stored in the *Documents* application. This
application **must** be installed to use the
`Insert in Spreadsheet`{.interpreted-text role="guilabel"} option.
:::
