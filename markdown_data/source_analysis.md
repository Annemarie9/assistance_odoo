# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/source_analysis.md

Source analysis reporting
=========================

Reporting is a critical tool used by recruiting departments to gain
insights into the entire recruitment process.

Determining where applicants come from can provide information about
which sources have the best results. This information is determined by
the *Source Analysis* report. With this data, recruitment teams can
better pivot their recruiting strategies to gain better applicants, in
both quantity and quality.

Open report
-----------

To access the *Source Analysis* report, navigate to
`Recruitment app --> Reporting
--> Source Analysis`{.interpreted-text role="menuselection"}.

This presents the data for the `fa-filter`{.interpreted-text
role="icon"} `Last 365 Days Applicant`{.interpreted-text
role="guilabel"}, in a default `fa-area-chart`{.interpreted-text
role="icon"} `(Graph)`{.interpreted-text role="guilabel"} view, showing
the amount of applicants by `Source`{.interpreted-text role="guilabel"},
and further separated by stage (`In Progress`{.interpreted-text
role="guilabel"} and `Hired`{.interpreted-text role="guilabel"})

Hover the cursor over any column to view the specific numbers fort that
column.

{.align-center}

To view more details, view the `Source Analysis`{.interpreted-text
role="guilabel"} report in a pivot table. To do so, click the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the top-right
corner. The data is presented in a pivot table, with rows populated by
job positions, and columns populated stages.

Source effectiveness report
---------------------------

To identify which sources (e.g., job boards, social media, employee
referrals, company website) produce the most hires, the pivot table view
of the `Source Analysis`{.interpreted-text role="guilabel"} report can
be configured to display further details.

To expand this chart to show what specific sources the applicants came
from, click the `fa-plus-square`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} box above the columns, to
reveal a drop-down menu, and click `Source`{.interpreted-text
role="guilabel"}.

Each column is then grouped by the source, such as:
`Search engine`{.interpreted-text role="guilabel"},
`Facebook`{.interpreted-text role="guilabel"},
`Newsletter`{.interpreted-text role="guilabel"}, etc. Each source
displays a separate count for `Applicant`{.interpreted-text
role="guilabel"}, `Hired`{.interpreted-text role="guilabel"}, and
`Refused`{.interpreted-text role="guilabel"}.

This information, as presented, makes it difficult to view the specific
numbers for each source. Click the `fa-exchange`{.interpreted-text
role="icon"} `(Flip axis)`{.interpreted-text role="guilabel"} icon, to
swap the information. After that, the rows represent the source, and the
columns represent the job positions, further divided by stage.

{.align-center}

In this view, the total number of applicants, hired employees, and
refused applicants, are displayed for each source, as well as for each
stage by job position.

### Medium

Viewing the medium for the applicants can be beneficial to see which
specific medium is more successful.

*Mediums* are the specific methods the applicant used to discover and
then apply for job positions, such as organic search, paid search,
social media ad, email, etc.

To further group the results by medium, click into one of the
`fa-plus-square`{.interpreted-text role="icon"}
`[Source]`{.interpreted-text role="guilabel"} rows. Click
`Medium`{.interpreted-text role="guilabel"} in the resulting drop-down
menu. The row presents the specific mediums, relevant to that specific
source.

Once `Medium`{.interpreted-text role="guilabel"} is selected for one
source, clicking into another row automatically reveals the specific
metrics for the mediums for that source.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The only mediums that appear for a source, are mediums that have been
set on an applicant\'s form. If a medium has **not** been set for any
applicants, the medium does not appear in the drop-down rows beneath the
source.

For example, if no applicants applied with the medium *Google Adwords*,
that medium does **not** appear beneath the *Search engine* source row.
:::
