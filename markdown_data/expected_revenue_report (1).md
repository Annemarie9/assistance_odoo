Expected revenue report
=======================

*Expected revenue* is the total cash value of leads that are expected to
close by a certain date, usually the end of the current month.

An *expected revenue report* compiles all active leads in a sales
pipeline that have a set expected closing date, and compares how sales
teams are performing in a given time frame.

{.align-center}

By pulling a monthly expected revenue report, sales managers can see
which team members are reaching their goals, and who may need additional
assistance to close valuable deals.

Create an expected revenue report
---------------------------------

To create an expected revenue report, first navigate to
`CRM app --> Reporting -->
Pipeline`{.interpreted-text role="menuselection"}. This opens the
`Pipeline Analysis`{.interpreted-text role="guilabel"} dashboard.

::: {.important}
::: {.title}
Important
:::

The *Pipeline Analysis* dashboard includes several filters in the search
bar by default. Remove these before adding any additional custom
filters.
:::

On the top-left of the report, click `Measures`{.interpreted-text
role="guilabel"}, then select `Expected Revenue`{.interpreted-text
role="guilabel"} from the drop-down menu.

At the top of the page, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar to
open the drop-down menu that contains `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns. Under the
`Filters`{.interpreted-text role="guilabel"} column, click
`Add Custom Filter`{.interpreted-text role="guilabel"}, which opens an
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

### Add custom filters {#expected_revenue_report/custom-filters}

In order to generate an expected revenue report, filters need to be
created for the following conditions:

> -   `Expected closing date <expected_revenue_report/closing-date>`{.interpreted-text
>     role="ref"}: limits results to only include leads expected to
>     close within a specific time frame.
> -   `Exclude unassigned leads <expected_revenue_report/unassigned-leads>`{.interpreted-text
>     role="ref"}: excludes leads without an assigned salesperson.
> -   `Specific sales teams <expected_revenue_report/sales-team>`{.interpreted-text
>     role="ref"}: limits results to only include leads assigned to one
>     or more sales teams. This filter is optional and should not be
>     included if the report is intended for the entire company.

#### Add filter for expected closing date {#expected_revenue_report/closing-date}

On the `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up
window, click into the first field of the new rule. Type [Expected
Closing]{.title-ref} into the `Search...`{.interpreted-text
role="guilabel"} bar, or scroll to select it from the list. Click in the
second field and select `is set`{.interpreted-text role="guilabel"}.
This limits the results to only include leads where an estimated closing
date is listed.

Next, click the `➕ (plus)`{.interpreted-text role="guilabel"} icon to
the right of the rule to duplicate it.

::: {.tip}
::: {.title}
Tip
:::

Using the `➕ (plus)`{.interpreted-text role="guilabel"} icon makes it
easy to add multiple rules based on the same filter.
:::

In the second field of the new rule, select
`is between`{.interpreted-text role="guilabel"} from the drop-down menu.
This creates a set time frame during which the expected closing date
must occur for leads to be included in the results.

Click in each date field, one at a time, and use the calendar popover
window to add both a start and end date to the rule. This is usually the
beginning and ending of the current month, or fiscal quarter.

#### Exclude unassigned leads {#expected_revenue_report/unassigned-leads}

After filtering for the expected closing date, add a
`New Rule`{.interpreted-text role="guilabel"}. Then, click into the new
rule\'s first field, and type [Salesperson]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar, or scroll through
the list to select it. Click in the rule\'s second field and select
`is set`{.interpreted-text role="guilabel"} from the drop-down menu.
This excludes any results without an assigned salesperson.

#### Add a filter for sales teams {#expected_revenue_report/sales-team}

::: {.note}
::: {.title}
Note
:::

This filter is optional. To view results for the entire company, do
**not** add this filter, and continue to
`View results <expected_revenue_report/view-results>`{.interpreted-text
role="ref"}.
:::

To limit the results of the report to one or more sales teams, click
`New Rule`{.interpreted-text role="guilabel"}. Next, click the first
field for the new rule, and type [Sales Team]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar, or scroll to search
through the list to locate it.

In the rule\'s second field, select `is in`{.interpreted-text
role="guilabel"} from the drop-down menu. Selecting this operator limits
results to the sales teams indicated in the next field.

Lastly, click into the third field, and either: make a selection from
the complete list revealed in the popover menu, or type the first few
characters of the specific sales team\'s title to quickly find and
select it as a parameter.

::: {.tip}
::: {.title}
Tip
:::

Multiple teams can be added to the [Sales Team]{.title-ref} rule, where
each parameter is treated with an \"or\" (e.g. \"any\") operator in the
search logic.
:::

![Add Custom Filters pop-up window with custom filters configured for expected revenue
report.](expected_revenue_report/custom-filters.png){.align-center}

View results {#expected_revenue_report/view-results}
------------

At the top of the `Add Custom Filter`{.interpreted-text role="guilabel"}
form, there is an option to match `any`{.interpreted-text
role="guilabel"} or `all`{.interpreted-text role="guilabel"} of the
rules. In order to properly run the report, only records that match
**all** of the following filters should be included. Before adding the
filters, make sure `all`{.interpreted-text role="guilabel"} is selected
in this field.

{.align-center}

At the bottom of the `Add Custom Filter`{.interpreted-text
role="guilabel"} form, click `Add`{.interpreted-text role="guilabel"}.

### View options

The expected revenue report benefits from utilizing multiple views. The
default graph view can be used to identify which salespeople are
expected to bring in the most revenue, while the list view and pivot
view provide more detail on specific deals.

::: {.tabs}
::: {.tab}
Graph view

The *graph view* is used to visualize data, and is beneficial in
identifying patterns and trends.

*Bar charts* are used to show the distribution of data across several
categories or among several salespeople.

*Line charts* are useful to show changing trends over a period of time.

*Pie charts* are useful to show the distribution, or comparison, of data
among a small number of categories or salespeople, specifically how they
form the meaningful part of a whole picture.

The default view for the expected revenue report is the bar chart,
stacked. To change to a different graph view, click one of the icons at
the top-left of the report. While both the line chart and bar chart are
available in stacked view, the pie chart is not.

![Graph view icons in order: bar chart, line chart, pie chart,
stacked.](expected_revenue_report/graph-view-icons.png){.align-center}
:::

::: {.tab}
List view

The *list view* provides a list of all leads that are expected to close
by the designated date. Clicking on a lead in list view opens the record
for detailed analysis, but many insights can be gleaned from the basic
view.

To switch to the list view, click the `≣ (list)`{.interpreted-text
role="guilabel"} icon at the top-right of the report.

{.align-center}

To add additional metrics to the report, click the *additional options
menu* indicated by the `toggle`{.interpreted-text role="guilabel"} icon
at the top-right of the list.

![Clicking the toggle icon in *list view* opens the *additional options
menu*.](expected_revenue_report/toggle-icon.png){.align-center}

Select any additional metrics from the drop-down menu to add them to the
list view. Some options that may be useful are
`Expected Closing`{.interpreted-text role="guilabel"} and
`Probability`{.interpreted-text role="guilabel"}.
:::

::: {.tab}
Pivot view

The *pivot view* arranges all leads that are expected to close by the
designated date into a dynamic table.

To switch to the pivot view, click the `Pivot`{.interpreted-text
role="guilabel"} icon at the top-right of the report.

{.align-center}

When the pivot view is selected for this report, the X-axis lists the
stages in the pipeline, while the Y-axis defaults to group the results
by their creation date. To switch these groupings, click the flip access
icon (`⇄`{.interpreted-text role="guilabel"}) at the top of the report.

To add additional measures to the report, click the
`Measures`{.interpreted-text role="guilabel"} button at the top-left of
the report. Select any additional metrics from the drop-down menu.

To add a group to a row or column to the pivot view, click the
`➕ (plus sign)`{.interpreted-text role="guilabel"} next to
`Total`{.interpreted-text role="guilabel"}, and then select one of the
groups. To remove one, click the `➖ (minus sign)`{.interpreted-text
role="guilabel"} and de-select the appropriate option.

Click `Insert in Spreadsheet`{.interpreted-text role="guilabel"} to add
the pivot view into an editable spreadsheet format within the
*Dashboards* app. If the Odoo *Documents* app is installed, the report
can be inserted into a blank or existing spreadsheet, and exported.
:::
:::
