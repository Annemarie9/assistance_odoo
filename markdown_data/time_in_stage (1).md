# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/time_in_stage.md

Time in stage analysis
======================

The *Time In Stage Analysis* report provides information on how long
applicants stay in each stage of the recruitment process. This is
important, as every job position has specific `process
details <recruitment/new_job_position/edit>`{.interpreted-text
role="ref"} that state the length of time applicants should expect to
wait between specific stages.

Knowing how long applicants remain in each stage can help highlight
possible bottlenecks. Analyzing this data allows the recruitment team to
assess each stage, identify any issues, and pivot their strategies to
move applicants through each stage, within the expected time interval.

Time in stage analysis report
-----------------------------

To access the report, navigate to
`Recruitment app --> Reporting --> Time in Stage
Analysis`{.interpreted-text role="menuselection"}. By default, the
report displays data from all job positions, with the stages populating
the x-axis, and the number of days populating the y-axis, in a
`fa-line-chart`{.interpreted-text role="icon"}
`(Line Chart)`{.interpreted-text role="guilabel"}.

The default filter is `Last 365 Days Applicant`{.interpreted-text
role="guilabel"}, showing information for the last 365 days.

Hover over a stage in the line chart to reveal a popover window listing
all the job positions within it, and the average number of days each job
position sits in each stage.

For a more visually digestible view of the information in the
`Time In Stage Analysis`{.interpreted-text role="guilabel"} report,
click the `fa-bar-chart`{.interpreted-text role="icon"}
`(Bar Chart)`{.interpreted-text role="guilabel"} icon in the upper-left
corner. This displays all the information in a bar chart.

In this view, it is easier to visualize the differences between the job
positions, regarding how long applicants stay in each stage. From this
view, recruiters can more easily determine which job positions have
delays or bottlenecks at certain stages.

{.align-center}

### Use case: comparing times by month

With the `Time In Stage Analysis`{.interpreted-text role="guilabel"}
report, it is possible to see if there are certain months where
applicants take longer to be moved through the pipeline. To view this
data, switch to the `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} view in the upper-right
corner.

This presents the data in a detailed pivot table, with the rows
representing the different job positions, and the columns representing
the stages. The average `Days in Stage`{.interpreted-text
role="guilabel"} populates the various boxes.

::: {.note}
::: {.title}
Note
:::

If a field is empty, it indicates no applicant has been in that stage.
Instead, all applicants moved from a previous stage without being placed
in the stage with an empty field.
:::

{.align-center}

Click `fa-minus-square-o`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} above the job position rows
to collapse the information. Next, click
`fa-plus-square`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} again, revealing a drop-down
menu. Click `Add Custom Group`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} at the bottom of the
list, revealing further grouping options. Click
`Start Date`{.interpreted-text role="guilabel"} from the expanded list.

After doing so, the data presented is grouped with the various months
from the previous 365 days for the rows, leaving the
`Days In Stage`{.interpreted-text role="guilabel"} as the columns.

{.align-center}

In this example, `July 2024`{.interpreted-text role="guilabel"} had the
longest time that applicants spent in each stage, on average. In
addition, the `Contract Proposal`{.interpreted-text role="guilabel"}
stage had the longest wait time in July, with an average of
`31.62`{.interpreted-text role="guilabel"} days in that stage.

While this report does not display the reasons applicants stayed in the
various stages for these lengths of time, it can be helpful to know when
delays occur.

::: {.seealso}
`Essentials reporting documentation <../../essentials/reporting>`{.interpreted-text
role="doc"}
:::
