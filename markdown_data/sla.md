# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/overview/sla.md

Service level agreements (SLA)
==============================

A *service level agreement* (SLA) defines the level of service a
customer can expect from a supplier.
`SLAs (Service Level Agreements)`{.interpreted-text role="abbr"} provide
a timeline that tells customers when they can expect results, and keeps
the support team on target.

::: {.note}
::: {.title}
Note
:::

The *SLA Policies* feature is enabled by default on newly created
*Helpdesk* teams.

To turn off the feature, or edit the working hours, navigate to
`Helpdesk app -->
Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}. Click on a team to open that team\'s
configuration page.

From here, scroll to the `Performance`{.interpreted-text
role="guilabel"} section. To turn off the `SLAs (Service
Level Agreements)`{.interpreted-text role="abbr"} feature for the team,
clear the `SLA Policies`{.interpreted-text role="guilabel"} checkbox.

{.align-center}
:::

Create a new SLA policy
-----------------------

To create a new policy, go to
`Helpdesk app --> Configuration --> SLA Policies`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}.

Alternatively, go to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and click on a team. Then, click the
`SLA Policies`{.interpreted-text role="guilabel"} smart button at the
top of the team\'s settings page, and click `New`{.interpreted-text
role="guilabel"}.

On the blank `SLA (Service Level Agreement)`{.interpreted-text
role="abbr"} policy form, enter a `Title`{.interpreted-text
role="guilabel"} and a `Description`{.interpreted-text role="guilabel"}
for the new policy, and proceed to fill out the form using the steps
below.

### Define the criteria for an SLA policy

The `Criteria`{.interpreted-text role="guilabel"} section is used to
identify which tickets this policy is applied to.

Fill out the following fields to adjust the selection criteria:

::: {.note}
::: {.title}
Note
:::

Unless otherwise indicated, multiple selections can be made for each
field.
:::

-   `Helpdesk Team`{.interpreted-text role="guilabel"}: a policy can
    only be applied to one team. *This field is required.*
-   `Priority`{.interpreted-text role="guilabel"}: the priority level
    for a ticket is identified by selecting one, two, or three of the
    `⭐ (star)`{.interpreted-text role="guilabel"} icons, representing
    the priority level on the Kanban card or on the ticket itself. The
    `SLA (Service Level Agreement)`{.interpreted-text role="abbr"} is
    **only** applied after the priority level has been updated on the
    ticket to match the
    `SLA (Service Level Agreement)`{.interpreted-text role="abbr"}
    criteria. If no selection is made in this field, this policy only
    applies to tickets marked as [Low Priority]{.title-ref}, meaning
    those with zero `⭐ (star)`{.interpreted-text role="guilabel"} icons.
-   `Tags`{.interpreted-text role="guilabel"}: tags are used to indicate
    what the ticket is about. Multiple tags can be applied to a single
    ticket.
-   `Customers`{.interpreted-text role="guilabel"}: individual contacts
    or companies may be selected in this field.
-   `Sales Order Items`{.interpreted-text role="guilabel"}: this field
    is available only if a team has the *Timesheets* app enabled. This
    allows the ticket to link directly to a specific line on a sales
    order, which must be indicated on the ticket in the
    `Sales Order Items`{.interpreted-text role="guilabel"} field.

::: {.example}
A support team needs to address urgent issues for VIP customers within
one business day.

The new policy, titled [8 Hours to close]{.title-ref}, is assigned to
the [VIP Support]{.title-ref} team. It **only** applies to tickets that
are assigned three `⭐ (star)`{.interpreted-text role="guilabel"} icons,
which equates to an [Urgent]{.title-ref} priority level.

At the same time, the tickets can be related to multiple issues, so the
policy applies to tickets with [Repair]{.title-ref},
[Service]{.title-ref}, or [Emergency]{.title-ref} tags.

{.align-center}
:::

### Establish a target for an SLA policy

A *target* is the stage a ticket needs to reach, and the time allotted
to reach that stage, in order to satisfy the
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} policy.
Any stage assigned to a team may be selected for the
`Reach Stage`{.interpreted-text role="guilabel"} field.

Time spent in stages selected in the
`Excluding Stages`{.interpreted-text role="guilabel"} field are **not**
included in the calculation of the
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} deadline.

::: {.example}
An `SLA (Service Level Agreement)`{.interpreted-text role="abbr"} titled
[8 Hours to Close]{.title-ref} tracks the working time before a ticket
is completed, and would have [Solved]{.title-ref} as the
`Reach Stage`{.interpreted-text role="guilabel"}. Simultaneously, an
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} titled [2
Days to Start]{.title-ref} tracks the working time before work on a
ticket has begun, and would have [In Progress]{.title-ref} as the
`Reach Stage`{.interpreted-text role="guilabel"}.
:::

Meet SLA deadlines
------------------

As soon as it is determined that a ticket fits the criteria of an
`SLA (Service Level
Agreement)`{.interpreted-text role="abbr"} policy, a deadline is
calculated. The deadline is based on the creation date of the ticket,
and the targeted working hours.

::: {.note}
::: {.title}
Note
:::

The value indicated next to the `Working Hours`{.interpreted-text
role="guilabel"} field of an `SLA (Service Level
Agreement)`{.interpreted-text role="abbr"} policy is used to determine
the deadline. By default, this is determined by the value set in the
`Company Working Hours`{.interpreted-text role="guilabel"} field under
`Settings app -->
Employees --> Work Organization`{.interpreted-text
role="menuselection"}.
:::

The deadline is then added to the ticket, as well as a tag indicating
the name of the `SLA
(Service Level Agreement)`{.interpreted-text role="abbr"} applied.

{.align-center}

When a ticket satisfies an
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} policy,
the `SLA (Service
Level Agreement)`{.interpreted-text role="abbr"} tag turns green, and
the deadline disappears from view on the ticket.

{.align-center}

::: {.important}
::: {.title}
Important
:::

If a ticket fits the criteria for more than one
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"}, the
earliest occurring deadline is displayed on the ticket. After that
deadline has passed, the next deadline is displayed.
:::

If the `SLA (Service Level Agreement)`{.interpreted-text role="abbr"}
deadline passes and the ticket has not moved to the
`Reach Stage`{.interpreted-text role="guilabel"}, the
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} tag turns
red. After the `SLA (Service Level Agreement)`{.interpreted-text
role="abbr"} has failed, the red tag stays on the ticket, even after the
ticket is moved to the `Reach Stage`{.interpreted-text role="guilabel"}.

{.align-center}

Analyze SLA performance {#helpdesk/analyze-sla-performance}
-----------------------

The `SLA Status Analysis`{.interpreted-text role="guilabel"} report
tracks how quickly an `SLA (Service Level
Agreement)`{.interpreted-text role="abbr"} is fulfilled, as well as the
performance of individual team members. Navigate to the report, and
corresponding pivot table, by going to `Helpdesk app --> Reporting -->
SLA Status Analysis`{.interpreted-text role="menuselection"}.

### Pivot view

By default, the report displays in a `Pivot`{.interpreted-text
role="guilabel"} view. Any `SLA (Service Level
Agreement)`{.interpreted-text role="abbr"} policies in the database with
tickets that failed to fulfill a policy, are in progress, or have
satisfied a policy are listed. By default, they are grouped by team and
ticket count.

![The pivot view aggregates data, which can be manipulated by adding
measures and filters.](sla/sla-status-analysis.png){.align-center}

To change the display, or add additional measurements, click the
`Measures`{.interpreted-text role="guilabel"} button to reveal a
drop-down menu of reporting criteria, and choose from the options
available.

Whenever a measurement is picked, a `✔️ (checkmark)`{.interpreted-text
role="guilabel"} icon appears in the drop-down menu to indicate that the
measurement is included, and a corresponding new column emerges in the
pivot table to show the relevant calculations.

{.align-center}

To add a group to a row or column, click the
`➕ (plus)`{.interpreted-text role="guilabel"} icon next to the policy
name and then select one of the groups. To remove one, click the
`➖ (minus)`{.interpreted-text role="guilabel"} icon next to the policy
name.

{.align-center}

### Graph view

The `SLA Status Analysis`{.interpreted-text role="guilabel"} report can
also be viewed as a `Bar Chart`{.interpreted-text role="guilabel"},
`Line Chart`{.interpreted-text role="guilabel"}, or
`Pie Chart`{.interpreted-text role="guilabel"}. Toggle between these
views by first selecting the `Graph`{.interpreted-text role="guilabel"}
button at the top-right of the dashboard. Then, select the appropriate
chart icon at the top-left of the graph.

::: {.tabs}
::: {.tab}
Bar Chart

![A bar chart can deal with larger data sets and compare data across
several categories.](sla/sla-report-bar.png){.align-center}
:::

::: {.tab}
Line Chart

![A line chart can visualize data trends or changes over
time.](sla/sla-report-line.png){.align-center}
:::

::: {.tab}
Pie Chart

![A pie chart compares data among a small number of
categories.](sla/sla-report-pie.png){.align-center}
:::
:::

::: {.tip}
::: {.title}
Tip
:::

Both the `Bar Chart`{.interpreted-text role="guilabel"} and
`Line Chart`{.interpreted-text role="guilabel"} views can be
`Stacked`{.interpreted-text role="guilabel"} by selecting the
`Stacked`{.interpreted-text role="guilabel"} icon. This displays two or
more groups on top of each other instead of next to each other, making
it easier to compare data.

{.align-center}
:::

### Cohort view

The `Cohort`{.interpreted-text role="guilabel"} view is used to track
the changes in data over a period of time. To display the
`SLA Status Analysis`{.interpreted-text role="guilabel"} report in a
`Cohort`{.interpreted-text role="guilabel"} view, click the
`Cohort`{.interpreted-text role="guilabel"} button, represented by
`(four cascading horizontal lines)`{.interpreted-text role="guilabel"},
in the top-right corner, next to the other view options.

![The cohort view examines the life cycle of data over
time.](sla/sla-report-cohort.png){.align-center}

::: {.seealso}
\- `Reporting views <reporting/views>`{.interpreted-text role="ref"} -
`Allow customers to close their tickets
</applications/services/helpdesk/advanced/close_tickets>`{.interpreted-text
role="doc"}
:::
