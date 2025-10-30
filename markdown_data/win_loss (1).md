Pipeline Analysis
=================

The *CRM* app manages the sales pipeline as leads/opportunities move
from stage to stage, origination to sale (**Won**) or archival
(**Lost**).

After organizing the pipeline, use the search options and reports
available on the *Pipeline Analysis* page to gain insight into the
effectiveness of the pipeline and its users.

To access the *Pipeline Analysis* page, go to
`CRM app --> Reporting --> Pipeline`{.interpreted-text
role="menuselection"}.

{.align-center}

Navigate the pipeline analysis page {#win_loss/pipeline}
-----------------------------------

Upon accessing the `Pipeline Analysis`{.interpreted-text
role="guilabel"} page, a bar graph showcasing the leads from the past
year automatically populates. The bars represent the number of leads in
each stage of the sales pipeline, color-coded to show the month the lead
reached that stage.

{.align-center}

The interactive elements of the `Pipeline Analysis`{.interpreted-text
role="guilabel"} page manipulate the graph to report different metrics
in several views. From left-to-right, top-to-bottom, the elements
include:

-   `Actions`{.interpreted-text role="guilabel"}: represented by the
    `⚙️ (gear)`{.interpreted-text role="guilabel"} icon, located next to
    the `Pipeline Analysis`{.interpreted-text role="guilabel"} page
    title. When clicked, a drop-down menu appears with three options,
    each with their own sub-menu: `Knowledge`{.interpreted-text
    role="guilabel"}, `Dashboard`{.interpreted-text role="guilabel"},
    `Spreadsheet`{.interpreted-text role="guilabel"}. (See
    `Save and share reports <win_loss/save_reports>`{.interpreted-text
    role="ref"} for more information)
    -   The `Knowledge`{.interpreted-text role="guilabel"} option is for
        linking to or inserting the graph in a *Knowledge* app article.
    -   The `Dashboard`{.interpreted-text role="guilabel"} option is for
        adding the graph to a dashboard in the *Dashboards* app.
    -   The `Spreadsheet`{.interpreted-text role="guilabel"} option is
        for linking the graph in a spreadsheet in the *Documents* app.
-   `Search...`{.interpreted-text role="guilabel"} bar: shows the
    filters and groupings currently being applied to the graph. To add
    new filters/groups, type them into the search bar, or click the
    `⬇️ (down arrow)`{.interpreted-text role="guilabel"} icon, at the
    end of the bar, to open a drop-down menu of options. (See
    `Search Options
    <win_loss/search>`{.interpreted-text role="ref"} for more
    information)

In the upper-right corner, there are view options represented by
different icons. (See `View
Options <win_loss/view>`{.interpreted-text role="ref"} for more
information)

-   `Graph`{.interpreted-text role="guilabel"} view: displays the data
    in a bar graph. This is the default view.
-   `Pivot`{.interpreted-text role="guilabel"} view: displays the data
    in a customizable, categorized metrics table.
-   `Cohort`{.interpreted-text role="guilabel"} view: displays and
    organizes the data, based on their `Created on`{.interpreted-text
    role="guilabel"} and `Closed Date`{.interpreted-text
    role="guilabel"} week (default), day, month, or year.
-   `List`{.interpreted-text role="guilabel"} view: displays the data in
    a list.

Located on the far-left side of the page, beneath the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page title, there
are more configurable filter and view options.

-   `Measures`{.interpreted-text role="guilabel"}: opens a drop-down
    menu of different measurement options that can be seen in the graph,
    pivot, or cohort view. The `Measure`{.interpreted-text
    role="guilabel"} drop-down menu is not available in the list view.
    (See `Measurement Options <win_loss/measure>`{.interpreted-text
    role="ref"} for more information)
-   `Insert in Spreadsheet`{.interpreted-text role="guilabel"}: opens a
    pop-up window with options for adding a graph or pivot table to a
    spreadsheet in the *Documents* app or a dashboard in the
    *Dashboards* app. This option is not available in the cohort or list
    view.

With the graph view selected, the following options are available:

-   `Bar Chart`{.interpreted-text role="guilabel"}: switches the graph
    to a bar chart.
-   `Line Chart`{.interpreted-text role="guilabel"}: switches the graph
    to a line chart.
-   `Pie Chart`{.interpreted-text role="guilabel"}: switches the graph
    to a pie chart.
-   `Stacked`{.interpreted-text role="guilabel"}: when selected, the
    results of each stage of the graph are stacked on top of each other.
    When not selected, the results in each stage are shown as individual
    bars.
-   `Descending`{.interpreted-text role="guilabel"}: re-orders the
    stages in the graph in descending order from left-to-right. Click
    the icon a second time to deselect it. Depending on the search
    criteria, this option may not be available.
-   `Ascending`{.interpreted-text role="guilabel"}: re-orders the stages
    in the graph in ascending order from left-to-right. Click the icon a
    second time to deselect it. Depending on the search criteria, this
    option may not be available.

With the pivot view selected, the following options are available:

-   `Flip Axis`{.interpreted-text role="guilabel"}: flips the X and Y
    axis for the entire table.
-   `Expand All`{.interpreted-text role="guilabel"}: when additional
    groupings are selected using the `➕ (plus
    sign)`{.interpreted-text role="guilabel"} icons, this button opens
    those groupings under every row.
-   `Download xlsx`{.interpreted-text role="guilabel"}: downloads the
    table as an Excel file.

### Search options {#win_loss/search}

The `Pipeline Analysis`{.interpreted-text role="guilabel"} page can be
customized with various filters and grouping options.

To add new search criteria, type the desired criteria into the search
bar, or click the `⬇️ (down arrow)`{.interpreted-text role="guilabel"}
icon, next to the search bar, to open a drop-down menu of all options.
See the sections below for more information on what each option does.

{.align-center}

::: {.tabs}
::: {.tab}
Filters

The `Filters`{.interpreted-text role="guilabel"} section allows users to
add pre-made and custom filters to the search criteria. Multiple filters
can be added to a single search.

-   `My Pipeline`{.interpreted-text role="guilabel"}: show leads
    assigned to the current user.
-   `Opportunities`{.interpreted-text role="guilabel"}: show leads that
    have been qualified as opportunities.
-   `Leads`{.interpreted-text role="guilabel"}: show leads that have yet
    to be qualified as opportunities.
-   `Active`{.interpreted-text role="guilabel"}: show active leads.
-   `Inactive`{.interpreted-text role="guilabel"}: show inactive leads.
-   `Won`{.interpreted-text role="guilabel"}: show leads that have been
    marked **Won**.
-   `Lost`{.interpreted-text role="guilabel"}: show leads that have been
    marked **Lost**.
-   `Created On`{.interpreted-text role="guilabel"}: show leads that
    were created during a specific period of time. By default, this is
    the past year, but it can be adjusted as needed, or removed
    entirely.
-   `Expected Closing`{.interpreted-text role="guilabel"}: show leads
    that are expected to close (marked **Won**) during a specific period
    of time.
-   `Date Closed`{.interpreted-text role="guilabel"}: show leads that
    were closed (marked **Won**) during a specific period of time.
-   `Archived`{.interpreted-text role="guilabel"}: show leads that have
    been archived (marked **Lost**).
-   `Add Custom Filter`{.interpreted-text role="guilabel"}: allows the
    user to create a custom filter with numerous options. (See
    `Add Custom Filters and Groups <win_loss/custom_filters>`{.interpreted-text
    role="ref"} for more information)
:::

::: {.tab}
Group By

The `Group By`{.interpreted-text role="guilabel"} section allows users
to add pre-made and custom groupings to the search results. Multiple
groupings can be added to split results into more manageable chunks.

::: {.important}
::: {.title}
Important
:::

The order that groupings are added affects how the final results are
displayed. Try selecting the same combinations in a different order to
see what works best for each use case.
:::

-   `Salesperson`{.interpreted-text role="guilabel"}: groups the results
    by the Salesperson to whom a lead is assigned.
-   `Sales Team`{.interpreted-text role="guilabel"}: groups the results
    by the Sales Team to whom a lead is assigned.
-   `City`{.interpreted-text role="guilabel"}: groups the results by the
    city from which a lead originated.
-   `Country`{.interpreted-text role="guilabel"}: groups the results by
    the country from which a lead originated.
-   `Company`{.interpreted-text role="guilabel"}: groups the results by
    the company to which a lead belongs (if multiple companies are
    activated in the database).
-   `Stage`{.interpreted-text role="guilabel"}: groups the results by
    the stages of the sales pipeline.
-   `Campaign`{.interpreted-text role="guilabel"}: groups the results by
    the marketing campaign from which a lead originated.
-   `Medium`{.interpreted-text role="guilabel"}: groups the results by
    the medium (Email, Google Adwords, Website, etc.) from which a lead
    originated.
-   `Source`{.interpreted-text role="guilabel"}: groups the results by
    the source (Search engine, Lead Recall, Newsletter, etc.) from which
    a lead originated.
-   `Creation Date`{.interpreted-text role="guilabel"}: groups the
    results by the date a lead was added to the database.
-   `Conversion Date`{.interpreted-text role="guilabel"}: groups the
    results by the date a lead was converted to an opportunity.
-   `Expected Closing`{.interpreted-text role="guilabel"}: groups the
    results by the date a lead is expected to close (marked \"Won\").
-   `Closed Date`{.interpreted-text role="guilabel"}: groups the results
    by the date a lead was closed(marked \"Won\").
-   `Lost Reason`{.interpreted-text role="guilabel"}: groups the results
    by the reason selected when a lead was marked \"Lost.\"
-   `Add Custom Group`{.interpreted-text role="guilabel"}: allows the
    user to create a custom group with numerous options. (See
    `Adding Custom Filters and Groups <win_loss/custom_filters>`{.interpreted-text
    role="ref"} for more information)
:::

::: {.tab}
Comparison

The `Comparison`{.interpreted-text role="guilabel"} section allows users
to add comparisons to the same search criteria over another period of
time.

This option is only available if the search includes time-based filters,
such as `Created On`{.interpreted-text role="guilabel"},
`Expected Closing`{.interpreted-text role="guilabel"}, or
`Date Closed`{.interpreted-text role="guilabel"}. While multiple
time-based filters can be added at once, only one comparison can be
selected at a time.

-   `Previous Period`{.interpreted-text role="guilabel"}: adds a
    comparison to the same search criteria from the previous period.
-   `Previous Year`{.interpreted-text role="guilabel"}: adds a
    comparison to the same search criteria from the previous year.
:::

::: {.tab}
Favorites

The `Favorites`{.interpreted-text role="guilabel"} section allows users
to save a search for later, so it does not need to be recreated every
time.

Multiple searches can be saved, shared with others, or even set as the
default for whenever the `Pipeline Analysis`{.interpreted-text
role="guilabel"} page is opened.

-   `Save current search`{.interpreted-text role="guilabel"}: save the
    current search criteria for later.
    -   `Default filter`{.interpreted-text role="guilabel"}: when saving
        a search, check this box to make it the default search filter
        when the `Pipeline Analysis`{.interpreted-text role="guilabel"}
        page is opened.
    -   `Shared`{.interpreted-text role="guilabel"}: when saving a
        search, check this box to make it available to other users.
:::
:::

#### Add custom filters and groups {#win_loss/custom_filters}

In addition to the pre-made options in the search bar, the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page can also
utilize custom filters and groups.

Custom filters are complex rules that further customize the search
results, while custom groups display the information in a more organized
fashion.

**To add a custom filter:**

1.  On the `Pipeline Analysis`{.interpreted-text role="guilabel"} page,
    click the `down arrow`{.interpreted-text role="guilabel"} icon next
    to the `Search...`{.interpreted-text role="guilabel"} bar.
2.  In the drop-down menu, click `Add Custom Filter`{.interpreted-text
    role="guilabel"}.
3.  The `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up
    window appears with a default rule (`Country
    is in _____`{.interpreted-text role="guilabel"}) comprised of three
    unique fields. These fields can be edited to make a custom rule, and
    multiple rules can be added to a single custom filter.
4.  To edit a rule, start by clicking the first field
    (`Country`{.interpreted-text role="guilabel"}), and select an option
    from the drop-down menu. The first field determines the primary
    subject of the rule.
5.  Next, click the second field, and select an option from the
    drop-down menu. The second field determines the relationship of the
    first and third fields, and is usually an **is** or **is not**
    statement, but can also be **greater than or less than** statements,
    and more.
6.  Finally, click the third field, and select an option from the
    drop-down menu. The third field determines the secondary subject of
    the rule.
7.  With all three fields selected, the rule is complete.
    -   **To add more rules:** click `New Rule`{.interpreted-text
        role="guilabel"} and repeat steps 4-7, as needed.
    -   **To delete a rule:** click the `🗑️ (trash)`{.interpreted-text
        role="guilabel"} icon to the right of the rule.
    -   **To duplicate an existing rule:** click the
        `➕ (plus sign)`{.interpreted-text role="guilabel"} icon to the
        right of the rule.
    -   **To create more complex rules:** click the
        `Add branch`{.interpreted-text role="guilabel"} icon to the
        right of the rule. This adds another modifier below the rule for
        adding an \"all of\" or \"any of\" statement.

{.align-center}

8.  Once all rules have been added, click `Add`{.interpreted-text
    role="guilabel"} to add the custom filter to the search criteria.
    -   **To remove a custom filter:** click the
        `✖️ (x)`{.interpreted-text role="guilabel"} icon beside the
        filter in the search bar.

**To add a custom group:**

1.  On the `Pipeline Analysis`{.interpreted-text role="guilabel"} page,
    click the `down arrow`{.interpreted-text role="guilabel"} icon next
    to the search bar.
2.  In the drop-down menu that appears, click
    `Add Custom Group`{.interpreted-text role="guilabel"}.
3.  Scroll through the options in the drop-down menu, and select one or
    more groups.
    -   **To remove a custom group:** click the
        `✖️ (x)`{.interpreted-text role="guilabel"} icon beside the
        custom group in the search bar.

### Measurement options {#win_loss/measure}

By default, the `Pipeline Analysis`{.interpreted-text role="guilabel"}
page measures the total `Count`{.interpreted-text role="guilabel"} of
leads that match the search criteria, but can be changed to measure
other items of interest.

To change the selected measurement, click the
`Measures`{.interpreted-text role="guilabel"} button on the top-left of
the page, and select one of the following options from the drop-down
menu:

-   `Days to Assign`{.interpreted-text role="guilabel"}: measures the
    number of days it took a lead to be assigned after creation.
-   `Days to Close`{.interpreted-text role="guilabel"}: measures the
    number of days it took a lead to be closed (marked **Won**).
-   `Days to Convert`{.interpreted-text role="guilabel"}: measures the
    number of days it took a lead to be converted to an opportunity.
-   `Exceeded Closing Days`{.interpreted-text role="guilabel"}: measures
    the number of days by which a lead exceeded its Expected Closing
    date.
-   `Expected MRR`{.interpreted-text role="guilabel"}: measures the
    Expected Recurring Revenue of a lead.
-   `Expected Revenue`{.interpreted-text role="guilabel"}: measures the
    Expected Revenue of a lead.
-   `Prorated MRR`{.interpreted-text role="guilabel"}: measures the
    Prorated Monthly Recurring Revenue of a lead.
-   `Prorated Recurring Revenues`{.interpreted-text role="guilabel"}:
    measures the Prorated Recurring Revenues of a lead.
-   `Prorated Revenue`{.interpreted-text role="guilabel"}: measures the
    Prorated Revenue of a lead.
-   `Recurring Revenues`{.interpreted-text role="guilabel"}: measures
    the Recurring Revenue of a lead.
-   `Count`{.interpreted-text role="guilabel"}: measures the total
    amount of leads that match the search criteria.

### View options {#win_loss/view}

After configuring filters, groupings, and measurements, the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page can display
the data in a variety of ways. By default, the page uses the graph view,
but can be changed to a pivot view, cohort view, or list view.

To change the pipeline to a different view, click one of the four view
icons, located in the top-right of the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page.

::: {.tabs}
::: {.tab}
Graph View

The graph view is the default selection for the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page. It displays
the analysis as either a: bar chart, line chart, or pie chart.

This view option is useful for quickly visualizing and comparing simple
relationships, like the `Count`{.interpreted-text role="guilabel"} of
leads in each stage, or the leads assigned to each
`Salesperson`{.interpreted-text role="guilabel"}.

By default, the graph measures the `Count`{.interpreted-text
role="guilabel"} of leads in each group, but this can be changed by
clicking the `Measures`{.interpreted-text role="guilabel"} button, and
`selecting another option
<win_loss/measure>`{.interpreted-text role="ref"} from the resulting
drop-down menu.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

When using a bar chart in this view, consider deselecting the
`Stacked`{.interpreted-text role="guilabel"} option, in order to make
the breakdown of results more legible.
:::
:::

::: {.tab}
Pivot View

The pivot view displays the results of the analysis as a table. By
default, the table groups the results by the stages of the sales
pipeline, and measures `Expected Revenue`{.interpreted-text
role="guilabel"}.

The pivot view is useful for analyzing more detailed numbers than the
graph view can handle, or for adding the data to a spreadsheet, where
custom formulas can be set up, like in an Excel file.

{.align-center}

The three icons at the top-left of the page perform the following
functions:

-   `Flip Axis`{.interpreted-text role="guilabel"}: flips the X and Y
    axis for the entire table.
-   `Expand All`{.interpreted-text role="guilabel"}: when additional
    groupings are selected using the `➕ (plus
    sign)`{.interpreted-text role="guilabel"} icons, this button opens
    those groupings under every row.
-   `Download xlsx`{.interpreted-text role="guilabel"}: downloads the
    table as an Excel file.

::: {.note}
::: {.title}
Note
:::

The `Stage`{.interpreted-text role="guilabel"} grouping cannot be
removed, but the measurement can be changed by clicking the
`Measures`{.interpreted-text role="guilabel"} button, and selecting
another option.
:::
:::

::: {.tab}
Cohort View

The cohort view displays the analysis as periods of time (cohorts) that
can be set to days, weeks, months, or years. By default,
`Week`{.interpreted-text role="guilabel"} is selected.

This view option is useful specifically for comparing how long it has
taken to close leads.

{.align-center}

From left-to-right, top-to-bottom, the columns in the chart represent
the following:

-   `Created On`{.interpreted-text role="guilabel"}: rows in this column
    represent the weeks of the year, in which records matching the
    search criteria exist.
    -   When set to `Week`{.interpreted-text role="guilabel"}, a row
        with the label `W52 2023`{.interpreted-text role="guilabel"}
        means the results occurred in: Week 52 of the Year 2023.
-   `Measures`{.interpreted-text role="guilabel"}: the second column in
    the chart is the measurement of the results. By default, it is set
    to `Count`{.interpreted-text role="guilabel"}, but can be changed by
    clicking the `Measures`{.interpreted-text role="guilabel"} button,
    and selecting an option from the drop-down menu.
-   `Closed Date - By Day/Week/Month/Year`{.interpreted-text
    role="guilabel"}: this column looks at what percentage of the
    measured results were closed in subsequent days/weeks/months/years.
-   `Average`{.interpreted-text role="guilabel"}: this row provides the
    average of all other rows in the column.

The cohort view can also be downloaded as an Excel file, by clicking the
`Download`{.interpreted-text role="guilabel"} icon in the top-left of
the page.
:::

::: {.tab}
List View

The list view displays a single list of all leads matching the search
criteria. Clicking a lead opens the record for closer review. Additional
details such as `Country`{.interpreted-text role="guilabel"},
`Medium`{.interpreted-text role="guilabel"}, and more can be added to
the list, by clicking the `Filters`{.interpreted-text role="guilabel"}
icon in the top-right of the list.

This view option is useful for reviewing many records at once.

{.align-center}

Clicking the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon opens
the Actions drop-down menu, with options for the following:

-   `Import records`{.interpreted-text role="guilabel"}: opens a page
    for uploading a spreadsheet of data, as well as a template
    spreadsheet to easily format that data.
-   `Export All`{.interpreted-text role="guilabel"}: downloads the list
    as an xlsx file for Excel.
-   `Knowledge`{.interpreted-text role="guilabel"}: inserts a view of,
    or link to, the list in an article in the *Knowledge* app.
-   `Dashboard`{.interpreted-text role="guilabel"}: adds the list to *My
    Dashboard* in the *Dashboards* app.
-   `Spreadsheet`{.interpreted-text role="guilabel"}: links to, or
    inserts, the list in a spreadsheet in the *Documents* app.

::: {.note}
::: {.title}
Note
:::

On the list view, clicking `New`{.interpreted-text role="guilabel"}
closes the list, and opens the *New Quotation* page. Clicking
`Generate Leads`{.interpreted-text role="guilabel"} opens a pop-up
window for lead generation. Neither feature is intended to manipulate
the list view.
:::
:::
:::

Create reports {#win_loss/reports}
--------------

After understanding how to
`navigate the pipeline analysis page <win_loss/pipeline>`{.interpreted-text
role="ref"}, the `Pipeline Analysis`{.interpreted-text role="guilabel"}
page can be used to create and share different reports. Between the
pre-made options and custom filter and groupings, almost any combination
is possible.

Once created, reports can be
`saved to favorites, shared with other users, and/or added to
dashboards and spreadsheets <win_loss/save_reports>`{.interpreted-text
role="ref"}.

A few common reports that can be created using the
`Pipeline Analysis`{.interpreted-text role="guilabel"} page are detailed
below.

### Win/Loss reports {#win_loss/win_loss}

Win/Loss is a calculation of active or previously active leads in a
pipeline that were either marked as **Won** or **Lost** over a specific
period of time. By calculating opportunities won over opportunities
lost, teams can clarify key performance indicators (KPIs) that are
converting leads into sales, such as specific teams or team members,
certain marketing mediums or campaigns, and so on.

$$\begin{equation}
Win/Loss Ratio = \frac{Opportunities Won}{Opportunities Lost}
\end{equation}$$

A win/loss report filters the leads from the past year, whether won or
lost, and groups the results by their stage in the pipeline. Creating
this report requires a custom filter, and grouping the results by
`Stage`{.interpreted-text role="guilabel"}.

{.align-center}

Follow the steps below to create a win/loss report:

1.  Navigate to `CRM app --> Reporting --> Pipeline`{.interpreted-text
    role="menuselection"}.

2.  On the `Pipeline Analysis`{.interpreted-text role="guilabel"} page,
    click the `⬇️ (down arrow)`{.interpreted-text role="guilabel"} icon,
    next to the search bar, to open a drop-down menu of filters and
    groupings.

    {.align-center}

3.  In drop-down menu that appears, under the
    `Group By`{.interpreted-text role="guilabel"} heading, click
    `Stage`{.interpreted-text role="guilabel"}.

4.  Under the `Filters`{.interpreted-text role="guilabel"} heading,
    click `Add Custom Filter`{.interpreted-text role="guilabel"} to open
    another pop-up menu.

5.  In the `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up
    menu, click on the first field in the
    `Match any of the following rules:`{.interpreted-text
    role="guilabel"} section. By default, this field displays
    `Country`{.interpreted-text role="guilabel"}.

6.  Clicking that first field reveals a sub-menu with numerous options
    to choose from. From this sub-menu, locate and select the
    `Active`{.interpreted-text role="guilabel"} option. Doing so
    automatically populates the remaining fields.

    The first field reads: `Active`{.interpreted-text role="guilabel"}.
    The second field reads: `is`{.interpreted-text role="guilabel"}. And
    lastly, the third field reads: `set`{.interpreted-text
    role="guilabel"}.

    In total, the rule reads: `Active is set`{.interpreted-text
    role="guilabel"}.

7.  Click `New Rule`{.interpreted-text role="guilabel"}, change the
    first field to `Active`{.interpreted-text role="guilabel"}, and the
    last field to `not set`{.interpreted-text role="guilabel"}. In
    total, the rule reads `Active is not set`{.interpreted-text
    role="guilabel"}.

8.  Click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

The report now displays the total `Count`{.interpreted-text
role="guilabel"} of leads, whether \"Won\" or \"Lost,\" grouped by their
stage in the CRM pipeline. Hover over a section of the report to see the
number of leads in that stage.

{.align-center}

#### Customize win/loss reports

After `creating a win/loss report <win_loss/win_loss>`{.interpreted-text
role="ref"}, consider using the options below to customize the report
for different needs.

::: {.example}
A sales manager might group wins and losses by salesperson, or sales
team, to see who has the best conversion rate. Or, a marketing team
might group by sources, or medium, to determine where their advertising
has been most successful.
:::

::: {.tabs}
::: {.tab}
Filters and groups

To add more filters and groups, click the
`⬇️ (down arrow)`{.interpreted-text role="guilabel"} icon, next to the
search bar, and select one or more options from the drop-down menu.

Some useful options include:

-   `Created on`{.interpreted-text role="guilabel"}: adjusting this
    filter to a different period of time, such as the last 30 days, or
    the last quarter, can provide more timely results.
-   `Add Custom Filter`{.interpreted-text role="guilabel"}: clicking
    this option, and scrolling through the numerous options in the
    drop-down menu, opens up additional search criteria, like `Last
    Stage Update`{.interpreted-text role="guilabel"} or
    `Lost Reason`{.interpreted-text role="guilabel"}.
-   `Add Custom Group > Active`{.interpreted-text role="guilabel"}:
    Clicking `Add Custom Group --> Active`{.interpreted-text
    role="menuselection"} separates the results into **Won**
    (`true`{.interpreted-text role="guilabel"}) or **Lost**
    (`false`{.interpreted-text role="guilabel"}). This shows at what
    stage leads are being marked **Won** or **Lost**.
-   `Multiple Groupings`{.interpreted-text role="guilabel"}: add
    multiple `Group By`{.interpreted-text role="guilabel"} selections to
    split results into more relevant and manageable chunks.
    -   Adding `Salesperson`{.interpreted-text role="guilabel"} or
        `Sales Team`{.interpreted-text role="guilabel"} breaks up the
        total count of leads in each `Stage`{.interpreted-text
        role="guilabel"}.
    -   Adding `Medium`{.interpreted-text role="guilabel"} or
        `Source`{.interpreted-text role="guilabel"} can reveal what
        marketing avenues generate more sales.

{.align-center}
:::

::: {.tab}
Pivot View

By default, pivot view groups win/loss reports by
`Stage`{.interpreted-text role="guilabel"} and measures
`Expected Revenue`{.interpreted-text role="guilabel"}.

To flesh out the table:

1.  Click the `⬇️ (down arrow)`{.interpreted-text role="guilabel"} next
    to the search bar.
2.  In the pop-up menu, replace the `Stage`{.interpreted-text
    role="guilabel"} grouping with something like
    `Salesperson`{.interpreted-text role="guilabel"} or
    `Medium`{.interpreted-text role="guilabel"}.
3.  Click the `Measures`{.interpreted-text role="guilabel"} button and
    click `Count`{.interpreted-text role="guilabel"} to add the number
    of leads back into the report.
    -   Other useful measures for pivot view include
        `Days to Assign`{.interpreted-text role="guilabel"} and
        `Days to Close`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

In pivot view, the `Insert In Spreadsheet`{.interpreted-text
role="guilabel"} button may be greyed out due to the report containing
`duplicate group bys`{.interpreted-text role="guilabel"}. To fix this,
replace the `Stage`{.interpreted-text role="guilabel"} grouping in the
search bar with another option.
:::
:::

::: {.tab}
List View

In list view, a win/loss report displays all leads on a single page.

To better organize the list, click the
`⬇️ (down arrow)`{.interpreted-text role="guilabel"} next to the search
bar, and add more relevant groupings or re-organize the existing ones.
To re-order the nesting, remove all `Group By`{.interpreted-text
role="guilabel"} options and re-add them in the desired order.

To add more columns to the list:

1.  Click the `Filters`{.interpreted-text role="guilabel"} icon in the
    top-right of the page.
2.  Select options from the resulting drop-down menu. Some useful
    filters include:
    -   **Campaign**: Shows the marketing campaign that originated each
        lead.
    -   **Medium**: Shows the marketing medium (Banner, Direct, Email,
        Google Adwords, Phone, Website, etc.) that originated each lead.
    -   **Source**: Shows the source of each lead (Newsletter, Lead
        Recall, Search Engine, etc.).

{.align-center}
:::
:::

Save and share reports {#win_loss/save_reports}
----------------------

After `creating a report <win_loss/reports>`{.interpreted-text
role="ref"}, the search criteria can be saved, so the report does not
need to be created again in the future. Saved searches automatically
update their results every time the report is opened.

Additionally, reports can be shared with others, or added to
spreadsheets/dashboards for greater customization and easier access.

::: {.tabs}
::: {.tab}
Save to Favorites

To save a report for later:

1.  On the `Pipeline Analysis`{.interpreted-text role="guilabel"} page,
    click the `⬇️ (down arrow)`{.interpreted-text role="guilabel"} icon,
    next to the search bar.
2.  In the drop-down menu that appears, under the
    `Favorites`{.interpreted-text role="guilabel"} heading, click
    `Save current search`{.interpreted-text role="guilabel"}.
3.  In the next drop-down menu that appears, enter a name for the
    report.
    -   Checking the `Default filter`{.interpreted-text role="guilabel"}
        box sets this report as the default analysis when the
        `Pipeline Analysis`{.interpreted-text role="guilabel"} page is
        accessed.
    -   Checking the `Shared`{.interpreted-text role="guilabel"} box
        makes this report available to other users.
4.  Finally, click `Save`{.interpreted-text role="guilabel"}. The report
    is now saved under the `Favorites`{.interpreted-text
    role="guilabel"} heading.

{.align-center}
:::

::: {.tab}
Add to a Spreadsheet

Inserting a report into a spreadsheet not only saves a copy of the
report, it allows users to add charts and formulas like in an Excel
file.

To save a report as a spreadsheet:

-   **In Graph or Pivot View**:
    1.  Click the `Insert in spreadsheet`{.interpreted-text
        role="guilabel"} button.
    2.  In the pop-up menu that appears, click
        `Confirm`{.interpreted-text role="guilabel"}.
-   **In Cohort or List View**:
    1.  Click the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon.
    2.  In the drop-down menu that appears, hover over
        `Spreadsheet`{.interpreted-text role="guilabel"}.
    3.  In the next drop-down menu, click either
        `Insert in spreadsheet`{.interpreted-text role="guilabel"} or
        `Link in spreadsheet`{.interpreted-text role="guilabel"}.

Saved reports are viewable in the *Documents* app.

> {.align-center}

::: {.tip}
::: {.title}
Tip
:::

After modifying a spreadsheet and adding additional formulas, consider
then adding the entire spreadsheet to a dashboard. Using this method,
the spreadsheet can be added to a public dashboard instead of only
`My Dashboard`{.interpreted-text role="guilabel"}.

1.  Click `File --> Add to dashboard`{.interpreted-text
    role="menuselection"}.
2.  In the pop-up menu that appears, name the spreadsheet and select a
    `Dashboard
    Section`{.interpreted-text role="guilabel"} to house the report.
3.  Click `Create`{.interpreted-text role="guilabel"}.
:::
:::

::: {.tab}
Add to a Dashboard

Adding a report to a dashboard saves it for later and makes it easy to
view alongside the rest of `My Dashboard`{.interpreted-text
role="guilabel"}.

To add a report to `My dashboard`{.interpreted-text role="guilabel"}:

1.  On the `Pipeline Analysis`{.interpreted-text role="guilabel"} page,
    click the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon.
2.  In the drop-down menu that appears, hover over
    `Dashboard`{.interpreted-text role="guilabel"}.
3.  In the `Add to my dashboard`{.interpreted-text role="guilabel"}
    drop-down menu, enter a name for the report (by default, it is named
    `Pipeline`{.interpreted-text role="guilabel"}).
4.  Click `Add`{.interpreted-text role="guilabel"}.

To view a saved report:

1.  Return to the main apps page, and navigate to `Dashboards app --> My
    Dashboard`{.interpreted-text role="menuselection"}.

{.align-center}
:::
:::

::: {.seealso}
\- `../acquire_leads/convert`{.interpreted-text role="doc"} -
`../acquire_leads/send_quotes`{.interpreted-text role="doc"} -
`../pipeline/lost_opportunities`{.interpreted-text role="doc"}
:::
