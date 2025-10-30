# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/team_performance.md

Team performance reporting
==========================

The *Team Performance* report in the **Recruitment** app shows how many
applicants each recruiter is managing.

This information is determined by the individuals populating the
`Recruiter
<recruitment/applicant-details>`{.interpreted-text role="ref"} field on
each applicant form.

Open report
-----------

To access the *Team Performance* report, navigate to
`Recruitment app --> Reporting
--> Team Performance`{.interpreted-text role="menuselection"}.

The number of `In Progress`{.interpreted-text role="guilabel"},
`Hired`{.interpreted-text role="guilabel"}, and
`Refused`{.interpreted-text role="guilabel"} applicants for each
recruiter is displayed in the `fa-area-chart`{.interpreted-text
role="icon"} `(Graph)`{.interpreted-text role="guilabel"} view.

The information shown is for the `fa-filter`{.interpreted-text
role="icon"} `Last 365 Days Applicant`{.interpreted-text
role="guilabel"} default filter, as displayed in the search bar.

Hover the cursor over any column to view a popover window, displaying
the specific details for that column.

{.align-center}

### Pivot table view

For a more detailed view of the information in the
`Team Performance`{.interpreted-text role="guilabel"} report, click the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the top-right
corner. This displays all the information in a pivot table.

In this view, the job positions are displayed in the rows, while the
columns display the total number of applicants. The applicants are
further organized by `# Applicant`{.interpreted-text role="guilabel"}
(in process), `# Hired`{.interpreted-text role="guilabel"}, and
`# Refused`{.interpreted-text role="guilabel"}.

The displayed information can be modified, if desired.

In this example, there are 19 total applicants. Out of those 19, eight
have been hired, and three refused.

From the data presented, the `Experienced Developer`{.interpreted-text
role="guilabel"} job position is the most successful. This job position
has the highest number of total applicants, as well as the most hires.
In addition, the `Experienced Developer`{.interpreted-text
role="guilabel"} has the least amount of refused applicants.

This pivot table also shows that the
`Chief Executive Officer`{.interpreted-text role="guilabel"} position is
the hardest to fill, as it has the fewest total applicants.

{.align-center}

Use case: recruiter performance over time
-----------------------------------------

One way to modify this report is to show how recruiters are performing
over time. To show this information, begin with the
`Team Performance`{.interpreted-text role="guilabel"} report in the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} view.

Next, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} in the search bar,
revealing a drop-down menu. Click `Add Custom Group`{.interpreted-text
role="guilabel"} `oi-caret-down`{.interpreted-text role="icon"} at the
bottom of the `oi-group`{.interpreted-text role="icon"}
`Group By`{.interpreted-text role="guilabel"} column, then click
`Recruiter`{.interpreted-text role="guilabel"}. Click away from the
drop-down menu to close it. Now, each row on the table represents a
recruiter.

{.align-center}

To compare the team\'s performance over different time periods, click
the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} in the search bar.
Click `Start Date`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} in the
`fa-filter`{.interpreted-text role="icon"} `Filters`{.interpreted-text
role="guilabel"} column, revealing various time periods to select.

In this example, the desired data is the comparison between the team\'s
performance in the third quarter (June - August) and the second quarter
(April - July). To do so, click `Q3`{.interpreted-text role="guilabel"}.
Once clicked, the current year is also ticked. In this example, it is
`2024`{.interpreted-text role="guilabel"}.

After making this selection, a `fa-adjust`{.interpreted-text
role="icon"} `Comparison`{.interpreted-text role="guilabel"} column
appears. Click `Start Date: Previous Period`{.interpreted-text
role="guilabel"} to compare the third quarter with the second quarter,
for the various recruiters.

{.align-center}

From this report, several things can be extrapolated: the total number
of applicants increased, the number of hired applicants remained the
same, while the number of refused applicants decreased.

Additionally, `Jane Jobs`{.interpreted-text role="guilabel"} had the
highest increase in number of applicants during the third quarter, but
her number of hired applicants went down `67%`{.interpreted-text
role="guilabel"}. The recruiter with the best overall numbers was
`Rose Recruiter`{.interpreted-text role="guilabel"}, who had both their
active applicants and hired applicants, increase in the third quarter,
while their refused applicants went down.
