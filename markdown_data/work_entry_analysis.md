# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll/work_entry_analysis.md

Work entry analysis
===================

The default *Work Entries Analysis* report provides an overview of the
validated work entries for the current month. To view this report,
navigate to `Payroll app --> Reporting -->
Work Entry Analysis`{.interpreted-text role="menuselection"}.

The work entries appear in a pivot table, with the default filters of
`Current month:
(Month)(Year)`{.interpreted-text role="guilabel"} and
`Validated`{.interpreted-text role="guilabel"}. The various types of
`work_entries`{.interpreted-text role="doc"} populate the rows, while
the `Total`{.interpreted-text role="guilabel"} values populate the only
visible column.

To change the displayed information, click
`fa-plus-square`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} above the main column,
revealing a drop-down menu of available metrics. Click on one of the
available groupings, and the data is further organized by that selected
metric. The default options are `Work
Entry Type`{.interpreted-text role="guilabel"},
`Employee`{.interpreted-text role="guilabel"}, and
`Department`{.interpreted-text role="guilabel"}. If in a multi-company
database, a `Company`{.interpreted-text role="guilabel"} option also
appears.

Work entry analysis comparison
------------------------------

It is possible to compare the work entries from one time period to a
previous time period. To view this comparison, first navigate to
`Payroll app --> Reporting --> Work Entry
Analysis`{.interpreted-text role="menuselection"}.

Next, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, revealing a drop-down menu. Under the `fa-adjust`{.interpreted-text
role="icon"} `Comparison`{.interpreted-text role="guilabel"} section,
click on either `Current Month: Previous Period`{.interpreted-text
role="guilabel"} or `Current Month: Previous Year`{.interpreted-text
role="guilabel"}.

The report updates and displays the data for the current time period,
data for the selected previous time period, as well as the
`Variation`{.interpreted-text role="guilabel"} between the two, in a
percentage.



::: {.note}
::: {.title}
Note
:::

If no work entries for a specific
`work entry type <payroll/work-entries>`{.interpreted-text role="ref"}
are logged for the time period, it does **not** appear on the report.
That does **not** mean the work entry type does not exist, or is not
configured.

Additionally, if the default
`Current month: (Month)(Year)`{.interpreted-text role="guilabel"} filter
is removed from the search bar, the `Comparison`{.interpreted-text
role="guilabel"} column does **not** appear; there must be a time-frame
selected to view the `Comparison`{.interpreted-text role="guilabel"}
column.
:::

Use case: overtime report comparison
------------------------------------

It is possible to alter the *Work Entries Analysis* report to show a
comparison of only overtime work entries, grouped by employee, for a
specific time period. To view this data, first navigate to the default
*Work entry analysis* report by going to `Payroll app --> Reporting -->
Work Entry Analysis`{.interpreted-text role="menuselection"}.

Next, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, revealing a drop-down menu. Under the `fa-filter`{.interpreted-text
role="icon"} `Filters`{.interpreted-text role="guilabel"} column, click
`Add Custom
Filter`{.interpreted-text role="guilabel"}, and a
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window
appears.

Using the drop-down menu, select `Work Entry Type`{.interpreted-text
role="guilabel"} for the first field, leave the middle field as-is (with
`is in`{.interpreted-text role="guilabel"} populating the field), and
select `Overtime Hours`{.interpreted-text role="guilabel"} for the last
field. Click `Add`{.interpreted-text role="guilabel"}, and all other
work entry types disappear, and `Overtime Hours`{.interpreted-text
role="guilabel"} appear in the sole row.

To compare overtime from the current month to the previous month, to see
which month had more overtime logged, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon again in the
search bar. Under the `fa-adjust`{.interpreted-text role="icon"}
`Comparison`{.interpreted-text role="guilabel"} section, click
`Current Month:
Previous Period`{.interpreted-text role="guilabel"}. Click away from the
drop-down menu to close it.

Now, the report displays the `Overtime Hours`{.interpreted-text
role="guilabel"} for the current month and the previous month, along
with the `Variation`{.interpreted-text role="guilabel"}, in a
percentage.

To view which employees received the most overtime, click
`fa-plus-square`{.interpreted-text role="icon"} `Overtime
Hours`{.interpreted-text role="guilabel"}, revealing a drop-down menu of
options. Click `Employee`{.interpreted-text role="guilabel"}, and all
employees with overtime work entries for either the current or previous
month appears.

In this example, it can be determined that `Marc Demo`{.interpreted-text
role="guilabel"} worked the most overtime in
`August 2024`{.interpreted-text role="guilabel"}, whereas
`Beth Evans`{.interpreted-text role="guilabel"} worked the most overtime
hours in `September 2024`{.interpreted-text role="guilabel"}.
Additionally, `Mitchell Admin`{.interpreted-text role="guilabel"} had
the largest variation change, with a `-100%`{.interpreted-text
role="guilabel"} change from `August 2024`{.interpreted-text
role="guilabel"} to `September 2024`{.interpreted-text role="guilabel"}.


