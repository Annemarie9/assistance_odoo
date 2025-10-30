# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/revenues_report.md

Revenues report
===============

The Odoo **Events** application creates custom reports, based on
event-related data and analytics. These reports can either be focused on
*Attendees* or *Revenues*.

The following documentation focuses on the reporting options related to
event *Revenues*.

Revenues reporting page
-----------------------

To access the *Attendees* reporting page, navigate to
`Events app --> Reporting -->
Revenues`{.interpreted-text role="menuselection"}.

{.align-center}

By default, the `Revenues`{.interpreted-text role="guilabel"} reporting
page appears as a graph (a `fa-line-chart`{.interpreted-text
role="icon"} `(Line Chart)`{.interpreted-text role="guilabel"} with
`fa-database`{.interpreted-text role="icon"}
`(Stacked)`{.interpreted-text role="guilabel"} data). The default
filters, `Non-free tickets`{.interpreted-text role="guilabel"} and
`Event Start Date: (current year)`{.interpreted-text role="guilabel"},
are present in the search bar.

::: {.tip}
::: {.title}
Tip
:::

To learn more about the various graph views (and graph view options),
refer to the `Graph
views <reporting/using-graph>`{.interpreted-text role="ref"}
documentation.
:::

The `Revenues`{.interpreted-text role="guilabel"} reporting page can
also be viewed as a `pivot table
<reporting/views/pivot>`{.interpreted-text role="ref"}, by clicking the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the upper-right
corner.

### Measures

Choosing specific
`Measures <reporting/choosing-measures>`{.interpreted-text role="ref"}
is a quick way to customize reporting pages.

Regardless of the chosen view, the measures on the
`Revenues`{.interpreted-text role="guilabel"} reporting page are as
follows: `Revenues`{.interpreted-text role="guilabel"},
`Untaxed Revenues`{.interpreted-text role="guilabel"}, and
`Count`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

In the default graph view of the `Revenues`{.interpreted-text
role="guilabel"} reporting page, only the `Revenues`{.interpreted-text
role="guilabel"} option is set in the `Measures`{.interpreted-text
role="guilabel"} drop-down menu.

In graph view, only one of the `Measures`{.interpreted-text
role="guilabel"} can be selected at a time.

When the pivot option is selected, all `Measures`{.interpreted-text
role="guilabel"} options are selected, by default.
:::

-   `Revenues`{.interpreted-text role="guilabel"}: shows the revenues
    generated from events.
-   `Untaxed Revenues`{.interpreted-text role="guilabel"}: shows the
    untaxed revenues generated from events.
-   `Count`{.interpreted-text role="guilabel"}: shows the total amount
    of registrants who attended events.

### Filters and grouping options

To reveal a drop-down menu of filter and grouping options to create
custom reports, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} to the right of the
search bar.

Doing so opens a drop-down mega menu of options organized into columns:
`Filters
<search/preconfigured-filters>`{.interpreted-text role="ref"},
`Group By <search/group>`{.interpreted-text role="ref"}, and `Favorites
<search/favorites>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

If a time-related option has been selected from the
`Filters`{.interpreted-text role="guilabel"} column (e.g. the default
`Event Start Date: (year)`{.interpreted-text role="guilabel"} filter), a
`Comparison`{.interpreted-text role="guilabel"} column appears, with
comparison options for the corresponding time-related filter option
selected.

Only **one** selection can be made from the
`Comparison`{.interpreted-text role="guilabel"} column at a time.
:::

::: {.seealso}
`../../essentials/search`{.interpreted-text role="doc"}
:::

#### Filter options

In the `Filters`{.interpreted-text role="guilabel"} column of the
drop-down mega menu, there are various event-related options that can be
utilized to create custom reports, based on a number of specific
criteria.

Multiple options in the `Filters`{.interpreted-text role="guilabel"}
column can be selected at once.

The `Filters`{.interpreted-text role="guilabel"} column has the
following options:

-   `Non-free tickets`{.interpreted-text role="guilabel"}: event
    tickets/registrations that were **not** free.
-   `Free`{.interpreted-text role="guilabel"}: event
    tickets/registrations that *were* free.
-   `Pending payment`{.interpreted-text role="guilabel"}: event
    tickets/registrations that were purchased, but still have payment
    pending.
-   `Sold`{.interpreted-text role="guilabel"}: event
    tickets/registrations that have been successfully sold (and paid
    for).
-   `Registration Date`{.interpreted-text role="guilabel"}: Click the
    `fa-caret-down`{.interpreted-text role="icon"}
    `(down arrow)`{.interpreted-text role="guilabel"} icon to reveal a
    list of month, quarter, and year options. Select any number of these
    options to view a specific periods of time and see how many
    registrations happened during that time.
-   `Upcoming/Running`{.interpreted-text role="guilabel"}: include
    revenue-related information for events that are either currently
    running or are going to happen in the future.
-   `Past Events`{.interpreted-text role="guilabel"}: include
    revenue-related information for events that have already taken
    place.
-   `Event Start Date`{.interpreted-text role="guilabel"}: Click the
    `fa-caret-down`{.interpreted-text role="icon"}
    `(down arrow)`{.interpreted-text role="guilabel"} icon to reveal a
    list of month, quarter, and year options. Select any number of these
    options to designate event start dates to use as filters for
    revenue-related event data.
-   `Event End Date`{.interpreted-text role="guilabel"}: Click the
    `fa-caret-down`{.interpreted-text role="icon"}
    `(down arrow)`{.interpreted-text role="guilabel"} icon to reveal a
    list of month, quarter, and year options. Select any number of these
    options to designate event end dates to use as filters for
    revenue-related event data.
-   `Published Events`{.interpreted-text role="guilabel"}: Select this
    option to show revenue-related data for published events.
-   `Add Custom Filter`{.interpreted-text role="guilabel"}: Create a
    custom filter to analyze event-related revenue data. To learn more,
    refer to the documentation on
    `custom filters <search/custom-filters>`{.interpreted-text
    role="ref"}.

#### Group By options

In the `Group By`{.interpreted-text role="guilabel"} column of the
drop-down mega menu, there are various event-related options to create
custom groupings of data.

Multiple `Group By`{.interpreted-text role="guilabel"} options can be
selected at once.

The `Group By`{.interpreted-text role="guilabel"} column has the
following options:

-   `Event Type`{.interpreted-text role="guilabel"}: Group data based on
    the type of event.
-   `Event`{.interpreted-text role="guilabel"}: Organize data into
    individual groups, separated by events.
-   `Product`{.interpreted-text role="guilabel"}: Group data based on
    the event registration product.
-   `Ticket`{.interpreted-text role="guilabel"}: Group data based on the
    type of event ticket purchased by attendees.
-   `Registration Status`{.interpreted-text role="guilabel"}: Group data
    based on the status of registrations.
-   `Sale Order Status`{.interpreted-text role="guilabel"}: Group data
    based on the status of event-related sales orders.
-   `Customer`{.interpreted-text role="guilabel"}: Group data based on
    customer records.
-   `Add Custom Group`{.interpreted-text role="guilabel"}: Click the
    `fa-caret-down`{.interpreted-text role="icon"}
    `(down arrow)`{.interpreted-text role="guilabel"} icon to reveal a
    drop-down of grouping options. To select one, click on the desired
    option, and Odoo adds it to the `Group By`{.interpreted-text
    role="guilabel"} column. Multiple selections can be made.

Sample report: event ticket analysis (graph)
--------------------------------------------

The following is an example of how various filters and grouping options
can create a useful analytic graph report related to event revenues. In
this case, the configurations present data about sold or free tickets to
published events, with the metrics separated by ticket type and event.

{.align-center}

To create such a report, navigate to
`Events app --> Reporting --> Revenues`{.interpreted-text
role="menuselection"}. Stay in the default graph view, but remove the
default filters from the search bar.

Then, click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} to the right of the
search bar, to reveal the drop-down mega menu of filter and grouping
options.

From here, select `Free`{.interpreted-text role="guilabel"} and
`Sold`{.interpreted-text role="guilabel"} from the
`Filters`{.interpreted-text role="guilabel"} column.

Then, since it is desired to **only** view data related to already
published events, select the `Published Events`{.interpreted-text
role="guilabel"} option in the `Filters`{.interpreted-text
role="guilabel"} column, as well.

Next, in the `Group By`{.interpreted-text role="guilabel"} column,
select the `Event`{.interpreted-text role="guilabel"} and
`Ticket`{.interpreted-text role="guilabel"} options, **in that
sequential order**. Doing so first groups the data by event, *then* by
ticket type, which provides a more useful array of data to analyze.

::: {.important}
::: {.title}
Important
:::

The order in which the options are selected in the
`Group By`{.interpreted-text role="guilabel"} column directly affects
how the data is presented on the report.
:::

From there, additional configurations can be added for more detailed
data, if desired.

If no additional filters or groupings are added, Odoo presents a
graphical representation of data related to all *free* or *sold* tickets
for *published events*, grouped by *event*, and organized by *ticket*
type.

Sample report: event type analysis (pivot table)
------------------------------------------------

The following is an example of how various filters and grouping options
can create a useful analytic pivot table report related to event
revenues. In this case, the configurations present data about how much
revenue different event types have generated, in order to gauge which
events are the most profitable.

{.align-center}

First, navigate to
`Events app --> Reporting --> Revenues`{.interpreted-text
role="menuselection"}, and switch to the pivot table view, by clicking
the `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the upper-right
corner.

Keep the default filters (`Non-free tickets`{.interpreted-text
role="guilabel"} and `Event Start Date: (year)`{.interpreted-text
role="guilabel"}) in the search bar.

Next, open the `Measures`{.interpreted-text role="guilabel"} drop-down
menu, and deselect the option for `Count`{.interpreted-text
role="guilabel"}, because this report is only going to focus on
revenues.

Then, click `fa-plus-square`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} above the column titles, and
select `Event Type`{.interpreted-text role="guilabel"} from the
resulting drop-down menu.

With these configurations in place, all the revenues generated from the
events (and their corresponding registrations) are displayed, organized
by the event type (presented as expandable columns).
