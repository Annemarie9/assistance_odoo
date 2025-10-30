# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/recruitment_analysis.md

Recruitment analysis
====================

The *Recruitment Analysis* report allows recruiting departments to see
which job positions have the most applicants, which have the most
referrals, and how long it takes for applicants to move through the
pipeline.

Knowing how many applicants each specific job position has, along with
statistics about how many are hired and refused, can provide valuable
insights. This information can assist the recruiting team to pivot their
strategies to acquire the most desirable candidates.

Recruitment analysis report
---------------------------

Start by navigating to
`Recruitment app --> Reporting --> Recruitment Analysis`{.interpreted-text
role="menuselection"}. This presents a line chart of all applicants for
the last year.

Three separate color-coded metrics are presented:
`In Progress`{.interpreted-text role="guilabel"},
`Hired`{.interpreted-text role="guilabel"}, and
`Refused`{.interpreted-text role="guilabel"}.

Hover the cursor over a month of the chart, and a pop-up window appears,
displaying the specific numbers for that month.

{.align-center}

### Pivot table view

For a more detailed view of the information in the
`Recruitment Analysis`{.interpreted-text role="guilabel"} report, click
the `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the top-right
corner. This displays all the information in a pivot table.

In this view, the job positions are displayed in the rows, and the
columns display the total numbers of applicants, including how many of
those applicants were hired or refused. The displayed information can be
modified, if desired.

In this example, there are 17 total applicants. Out of that, three have
been hired, and four refused. The
`Experienced Developer`{.interpreted-text role="guilabel"} position has
eight total applicants, two of which were hired, and two were refused.

{.align-center}

#### Use case: applicants with referrals

To get a better understanding of how effective the company\'s
`referral program <../referrals>`{.interpreted-text role="doc"} is, the
`Recruitment Analysis`{.interpreted-text role="guilabel"} report can be
modified to show how many applicants were referred by current employees.

From the `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} view of the
`Recruitment Analysis`{.interpreted-text role="guilabel"} report, first
click the `Measures`{.interpreted-text role="guilabel"} button to reveal
a drop-down menu of options.

Click both `Has Referrer`{.interpreted-text role="guilabel"} and
`Count`{.interpreted-text role="guilabel"}, to activate those two
measures. Then, click `# Applicant`{.interpreted-text role="guilabel"},
`# Hired`{.interpreted-text role="guilabel"}, and
`# Refused`{.interpreted-text role="guilabel"} to deactivate those
default measures.

Now, the column displays the number of applicants that came from a
referral in the `Has
Referrer`{.interpreted-text role="guilabel"} column, and the total
number of applicants in the `Count`{.interpreted-text role="guilabel"}
column.

{.align-center}

In this example, the `Experienced Developer`{.interpreted-text
role="guilabel"} job position has the most applicants from referrals.
Out of the eight applicants, six have applied through a referral from a
current employee. Meanwhile, the
`Marketing and Community Manager`{.interpreted-text role="guilabel"} job
position has the least amount of referrals out of the total applicants,
only one out of six.

##### Hired through referrals

It is possible to modify this report even further to see how many
referred applicants end up being hired.

To view this data, click on a `fa-plus-square`{.interpreted-text
role="icon"} `[job position]`{.interpreted-text role="guilabel"} row,
which reveals a drop-down menu. Then, click `State`{.interpreted-text
role="guilabel"} to show the various states applicants are currently in.

::: {.note}
::: {.title}
Note
:::

Only states that have applicants in them are shown for each job
position. If a state does **not** have any applicants, it does not
appear in the list.
:::

To expand the other rows, and display the various states, click on the
`fa-plus-square`{.interpreted-text role="icon"}
`[job position]`{.interpreted-text role="guilabel"} button.

{.align-center}

In this example, the `Experienced Developer`{.interpreted-text
role="guilabel"} job position is the most successful in terms of
referrals. Both of the hired employees came from internal referrals.
Meanwhile, there have been no hired employees for the
`Chief Executive Officer`{.interpreted-text role="guilabel"} position,
and the only hired employee for the
`Marketing and Community Manager`{.interpreted-text role="guilabel"} was
not referred by an employee.

In this scenario, it is possible to determine that the current software
developers are providing the most referrals, with the highest success
rate.
