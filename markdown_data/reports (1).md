# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/overview/reports.md

Reporting
=========

Reports in Odoo *Helpdesk* provide the opportunity to manage employee
workloads, identify areas for improvement, and confirm if customer
expectations are being met.

Available reports
-----------------

Details about the reports available in Odoo *Helpdesk* can be found
below. To view the different reports, go to
`Helpdesk app --> Reporting`{.interpreted-text role="menuselection"},
and select one of the following: `Tickets Analysis`{.interpreted-text
role="guilabel"}, `SLA Status Analysis`{.interpreted-text
role="guilabel"}, or `Customer Ratings`{.interpreted-text
role="guilabel"}.

### Tickets Analysis

The *Tickets Analysis* report
(`Helpdesk app --> Reporting --> Tickets Analysis`{.interpreted-text
role="menuselection"}) provides an overview of every customer support
ticket in the database.

This report is useful for identifying where teams are spending the most
time, and helps determine if there is an uneven workload distribution
among the support staff. The default report counts the number of tickets
per team and groups them by stage.

{.align-center}

Alternative measures can be selected to track where the most time is
spent at different points in the workflow. To change the measures used
for the report that is currently displayed, or to add more, click the
`Measures`{.interpreted-text role="guilabel"} button, and select one or
more options from the drop-down menu:

-   `Average Hours to Respond`{.interpreted-text role="guilabel"}:
    average number of working hours between a message sent from the
    customer and the response from the support team. *This does not
    include messages sent when the ticket was in a folded stage.*
-   `Hours Open`{.interpreted-text role="guilabel"}: number of hours
    between the date the ticket was created and the closed date. If
    there is no closed date on the ticket, the current date is used.
    **This measure is not specific to working hours.**
-   `Hours Spent`{.interpreted-text role="guilabel"}: number of
    *Timesheet* hours logged on a ticket. *This measure is only
    available if Timesheets are enabled on a team, and the current user
    has the access rights to view them.*
-   `Hours to Assign`{.interpreted-text role="guilabel"}: number of
    working hours between the date the ticket was created and when it
    was assigned to a team member.
-   `Hours to Close`{.interpreted-text role="guilabel"}: number of
    working hours between the date the ticket was created and the date
    it was closed.
-   `Hours to First Response`{.interpreted-text role="guilabel"}: number
    of working hours between the date the ticket was received and the
    date on which the first message was sent. *This does not include
    email sent automatically when a ticket reaches a stage.*
-   `Hours until SLA Deadline`{.interpreted-text role="guilabel"}:
    number of working hours remaining to reach the last
    `SLA (Service Level Agreement)`{.interpreted-text role="abbr"}
    deadline on a ticket.
-   `Rating (/5)`{.interpreted-text role="guilabel"}: number out of five
    to represent customer feedback (Dissatisfied = 1, Okay/Neutral = 3,
    Satisfied = 5).
-   `Remaining Hours on SO`{.interpreted-text role="guilabel"}: hours
    remaining on a linked sales order.
-   `Count`{.interpreted-text role="guilabel"}: number of tickets in
    total.

::: {.note}
::: {.title}
Note
:::

*Working hours* are calculated based on the default working calendar. To
view or change the working calendar, go to the
`Settings`{.interpreted-text role="menuselection"} application and
select `Employees --> Company Working Hours`{.interpreted-text
role="menuselection"}.
:::

### SLA Status Analysis

The *SLA Status Analysis* report
(`Helpdesk app --> Reporting --> SLA Status
Analysis`{.interpreted-text role="menuselection"})
`analyzes the performance <helpdesk/analyze-sla-performance>`{.interpreted-text
role="ref"} of individual SLA (Service Level Agreement) policies.

By default, this report is filtered to show the number of
`SLAs (Service Level Agreements)`{.interpreted-text role="abbr"} failed,
in progress, and the number that have been successful. The results are
grouped by teams.

{.align-center}

To change the measures used for the report that is currently displayed,
or to add more, click the `Measures`{.interpreted-text role="guilabel"}
button, and select one or more options from the drop-down menu:

-   `Number of SLA Failed`{.interpreted-text role="guilabel"}: number of
    tickets that have failed at least one
    `SLA (Service Level Agreement)`{.interpreted-text role="abbr"}.
-   `Rating (/5)`{.interpreted-text role="guilabel"}: number value
    representing customer feedback (Dissatisfied = 1, Okay/Neutral = 3,
    Satisfied = 5).
-   `Remaining Hours on SO`{.interpreted-text role="guilabel"}: hours
    remaining on a linked sales order.
-   `Working Hours to Assign`{.interpreted-text role="guilabel"}: number
    of working hours between the date the ticket was created and when it
    was assigned to a team member.
-   `Working Hours to Close`{.interpreted-text role="guilabel"}: number
    of working hours between the date the ticket was created and the
    date it was closed.
-   `Working Hours to Reach SLA`{.interpreted-text role="guilabel"}:
    number of working hours between the date the ticket was created and
    the date the `SLA (Service Level Agreement)`{.interpreted-text
    role="abbr"} was satisfied.
-   `Count`{.interpreted-text role="guilabel"}: number of tickets in
    total.

::: {.seealso}
`Service Level Agreements (SLA) <sla>`{.interpreted-text role="doc"}
:::

### Customer Ratings

The *Customer Ratings* report
(`Helpdesk app--> Reporting --> Customer Ratings`{.interpreted-text
role="menuselection"}) displays an overview of the ratings received on
individual support tickets, as well as any additional comments submitted
with the rating.

{.align-center}

Click on an individual rating to see additional details about the rating
submitted by the customer, including a link to the original ticket.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

On the rating\'s details page, tick the
`Visible Internally Only`{.interpreted-text role="guilabel"} checkbox to
hide the rating from the customer portal.
:::

The *Customer Ratings* report is displayed in a Kanban view by default,
but can also be displayed in graph, list, or pivot view.

::: {.seealso}
`Ratings <ratings>`{.interpreted-text role="doc"}
:::

View and filter options
-----------------------

On any Odoo report, the view and filter options vary, depending on what
data is being analyzed, measured, and grouped. See below for additional
information on the available views for the *Helpdesk* reports.

::: {.note}
::: {.title}
Note
:::

Only one measure may be selected at a time for graphs, but pivot tables
can include multiple measures.
:::

### Pivot view

The *pivot* view presents data in an interactive manner. All three
*Helpdesk* reports are available in pivot view.

The pivot view can be accessed on any report by selecting the
`oi-view-pivot`{.interpreted-text role="icon"}
`(pivot)`{.interpreted-text role="guilabel"} icon at the top-right of
the screen.

{.align-center}

To add a group to a row or column to the pivot view, click the
`fa-plus-square`{.interpreted-text role="icon"}
`(plus)`{.interpreted-text role="guilabel"} icon next to
`Total`{.interpreted-text role="guilabel"}, and then select one of the
groups. To remove one, click the `fa-minus-square-o`{.interpreted-text
role="icon"} `(minus)`{.interpreted-text role="guilabel"} icon, and
de-select the appropriate option.

### Graph view

The *graph* view presents data in either a *bar*, *line*, or *pie*
chart.

Switch to the graph view by selecting the
`fa-area-chart`{.interpreted-text role="icon"}
`(area chart)`{.interpreted-text role="guilabel"} icon at the top-right
of the screen. To switch between the different charts, select the
*related icon* at the top-left of the chart, while in graph view.

::: {.tabs}
::: {.tab}
Bar chart

{.align-center}
:::

::: {.tab}
Line chart

{.align-center}
:::

::: {.tab}
Pie chart

{.align-center}
:::
:::

::: {.tip}
::: {.title}
Tip
:::

Both the *bar chart* and *line chart* can utilize the *stacked* view
option. This presents two or more groups of data on top of each other,
instead of next to each other, making it easier to compare data. While
viewing either a bar chart or line chart, click the
`fa-database`{.interpreted-text role="icon"}
`(stacked)`{.interpreted-text role="guilabel"} icon to toggle the
stacked view option on or off.
:::

### Save and share a favorite search

The *Favorites* feature found on *Helpdesk* reports allows users to save
their most commonly used filters, without having to reconstruct them
every time they are needed.

To create and save a new *Favorites* configuration on a report, follow
the steps below:

1.  Set the necessary parameters using the `Filters`{.interpreted-text
    role="guilabel"}, `Group By`{.interpreted-text role="guilabel"} and
    `Measures`{.interpreted-text role="guilabel"} options.
2.  Click the `fa-caret-down`{.interpreted-text role="icon"}
    `(down)`{.interpreted-text role="guilabel"} icon next to the
    `Search...`{.interpreted-text role="guilabel"} bar to open the
    drop-down menu.
3.  Under the `Favorites`{.interpreted-text role="guilabel"} heading,
    click `Save current search`{.interpreted-text role="guilabel"}.
4.  If desired, enter a new name for the report.
5.  Tick the `Default Filter`{.interpreted-text role="guilabel"}
    checkbox to have these filter settings automatically displayed when
    the report is opened. Otherwise, leave it blank.
6.  Tick the `Shared`{.interpreted-text role="guilabel"} checkbox to
    make this filter configuration available to all other database
    users. If this checkbox is not ticked, only the user who creates the
    filter can access it.
7.  Click `Save`{.interpreted-text role="guilabel"} to preserve the
    configuration for future use.

{.align-center}

::: {.seealso}
\- `Start receiving tickets <receiving_tickets>`{.interpreted-text
role="doc"} -
`Odoo reporting <../../../essentials/reporting>`{.interpreted-text
role="doc"}
:::
