# File: /content/odoo_doc17.0/fr/content/applications/essentials/search.md

Search, filter, and group records
=================================

Odoo allows for the searching, filtering, and grouping of records in a
view to display only the most relevant records. The search bar is
located at the top of the view, start typing to `search for
values <search/values>`{.interpreted-text role="ref"}, or click the
`🔽 (down arrow)`{.interpreted-text role="guilabel"} icon to access the
`Filter
<search/filters>`{.interpreted-text role="ref"},
`Group By <search/group>`{.interpreted-text role="ref"}, and
`Favorites <search/favorites>`{.interpreted-text role="ref"} drop-down
menus.

Search for values {#search/values}
-----------------

Use the search field to quickly look for specific values, and add them
as a filter. Type the value to search for, and select the desired option
from the drop-down menu to apply the search filter.

::: {.example}
Instead of adding a
`custom filter <search/custom-filters>`{.interpreted-text role="ref"} to
select records where *Mitchell Admin* is the salesperson on the *Sales
Analysis* report (`Sales app -->
Reporting --> Sales`{.interpreted-text role="menuselection"}), search
for [Mitch]{.title-ref}, and click the
`⏵ (right arrow)`{.interpreted-text role="guilabel"} next to
`Search Salesperson for: Mitch`{.interpreted-text role="guilabel"}, and
select `Mitchell Admin`{.interpreted-text role="guilabel"}.

{.align-center}
:::

::: {.note}
::: {.title}
Note
:::

Using the search field is equivalent to using the *contains* operator
when adding a `custom
filter <search/custom-filters>`{.interpreted-text role="ref"}. If a
partial value is entered, and the desired field is directly selected
(without selecting the `⏵ (right arrow)`{.interpreted-text
role="guilabel"}), *all* records containing the typed characters for the
selected field are included.
:::

Filters {#search/filters}
-------

Filters are used to select records that meet specific criteria. The
default selection of records is specific to each view, but can be
modified by selecting one (or several) `preconfigured filters
<search/preconfigured-filters>`{.interpreted-text role="ref"}, or by
adding a `custom filter <search/custom-filters>`{.interpreted-text
role="ref"}.

### Preconfigured filters {#search/preconfigured-filters}

Modify the default selection of records by clicking the
`🔽 (down arrow)`{.interpreted-text role="guilabel"} icon from the search
bar, and selecting one (or several) *preconfigured filters* from the
`Filters`{.interpreted-text role="guilabel"} drop-down menu.

::: {.example}
On the *Sales Analysis* report
(`Sales app --> Reporting --> Sales`{.interpreted-text
role="menuselection"}), only records that are at the *sales order*
stage, with an *order date* within the last 365 days, are selected by
default.

To also include records at the *quotation* stage, select
`Quotations`{.interpreted-text role="guilabel"} from the
`Filters`{.interpreted-text role="guilabel"}.

Furthermore, to *only* include sales order and quotation records from a
specific year, like 2024, for example, first remove the existing [Order
Date: Last 365 Days]{.title-ref} filter, by clicking the
`❌ (remove)`{.interpreted-text role="guilabel"} icon, then select
`Order Date --> 2024`{.interpreted-text role="menuselection"}.

{.align-center}
:::

::: {.note}
::: {.title}
Note
:::

The preconfigured `Filters`{.interpreted-text role="guilabel"} are
grouped, and each group is separated by a horizontal line. Selecting
preconfigured filters from the same group allows records to match *any*
of the applied conditions. However, selecting filters from different
groups requires records to match *all* of the applied conditions.
:::

### Custom filters {#search/custom-filters}

If the
`preconfigured filters <search/preconfigured-filters>`{.interpreted-text
role="ref"} are not specific enough, add a custom filter. To do so,
click the `🔽 (down arrow)`{.interpreted-text role="guilabel"} icon in
the search bar, then select
`Filters --> Add Custom Filter`{.interpreted-text role="menuselection"}.

The `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window
displays the matching option, filter rule, and a toggle to
`Include archived`{.interpreted-text role="guilabel"} records.

{.align-center}

The default matching configuration is to
`Match any of the following rules`{.interpreted-text role="guilabel"},
indicating that each filter rule is applied independently. To change the
matching configuration to
`Match all of the following rules`{.interpreted-text role="guilabel"},
at least two filter rules must be added to the custom filter.

-   `Match all 🔽 of the following rules`{.interpreted-text
    role="guilabel"}: **all** of the filter rules must be met.
    Logically, this is an *AND* ([&]{.title-ref}) operation.
-   `Match any 🔽 of the following rules`{.interpreted-text
    role="guilabel"}: **any** of the filter rules can be met. Logically,
    this is an *OR* ([\|]{.title-ref}) operation.

By default, a single filter rule is added to the custom filter. The
following describes the structure of a filter rule:

1.  The first inline field is the *field name* to filter by. Some fields
    have refined parameters that are nested within another field. These
    fields have an `> (arrow)`{.interpreted-text role="guilabel"} icon
    beside them, which can be selected to reveal the nested fields.
2.  The second inline field is the conditional *operator* used to
    compare the field name to the value. The
    `available conditional operators <reference/orm/domains>`{.interpreted-text
    role="ref"} are specific to the field\'s data type.
3.  The third inline field is the variable *value* of the field name.
    The value input may appear as a drop-down menu, a text input, a
    number input, a date/time input, a boolean selector, or it may be
    blank, depending on the operator used and the field\'s data type.

Three inline buttons are also available to the right of the rule\'s
filter criteria:

1.  `➕ (plus sign)`{.interpreted-text role="guilabel"}: adds a new rule
    below the existing rule.

2.  `(Add branch)`{.interpreted-text role="guilabel"}: adds a new group
    of rules below the existing rule, with the `any`{.interpreted-text
    role="guilabel"} and `all`{.interpreted-text role="guilabel"}
    matching options available to define how each rule within this
    branch is applied to the filter. If the matching option is set to
    the same as the parent group, the fields are moved to join the
    parent group.

    ::: {.example}
    If the matching option is set to
    `Match all 🔽 of the following rules`{.interpreted-text
    role="guilabel"}, and a new branch is added with its matching option
    changed from `any 🔽 of`{.interpreted-text role="guilabel"} to `all
    🔽 of`{.interpreted-text role="guilabel"}, the newly-added branch
    disappears, and its group of rules are moved to the parent group.
    :::

3.  `🗑️ (garbage can)`{.interpreted-text role="guilabel"}: deletes the
    node. If a branch node is deleted, all children of that node are
    deleted, as well.

A new filter rule can be added to the custom filter by clicking the
`New Rule`{.interpreted-text role="guilabel"} button.

Once the filter criteria are defined, click `Add`{.interpreted-text
role="guilabel"} to add the custom filter to the view.

::: {.example}
To target all leads and opportunities from the `CRM`{.interpreted-text
role="menuselection"} app that are in the *Won* stage, and have an
expected revenue greater than \$1,000, the following should be entered:

`Match all 🔽 (down arrow) of the following rules:`{.interpreted-text
role="guilabel"}

1.  `Stage`{.interpreted-text role="guilabel"} `is in`{.interpreted-text
    role="guilabel"} `Won`{.interpreted-text role="guilabel"}
2.  `Expected Revenue`{.interpreted-text role="guilabel"}
    `>`{.interpreted-text role="guilabel"} [1,000]{.title-ref}
3.  `any 🔽 (down arrow)`{.interpreted-text role="guilabel"}
    `of:`{.interpreted-text role="guilabel"}
    -   `Type`{.interpreted-text role="guilabel"} `=`{.interpreted-text
        role="guilabel"} `Lead`{.interpreted-text role="guilabel"}
    -   `Type`{.interpreted-text role="guilabel"} `=`{.interpreted-text
        role="guilabel"} `Opportunity`{.interpreted-text
        role="guilabel"}

{.align-center}
:::

::: {.tip}
::: {.title}
Tip
:::

Activate `developer-mode`{.interpreted-text role="ref"} to reveal each
field\'s technical name and data type, as well as the
`# Code editor`{.interpreted-text role="guilabel"} text area below the
filter rules, to view and edit the domain manually.
:::

Group records {#search/group}
-------------

The display of records in a view can be clustered together, according to
one of the *preconfigured groups*. To do so, click the
`🔽 (down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, then select one of the `Group By`{.interpreted-text
role="guilabel"} options from the drop-down menu.

::: {.example}
To group the records by salesperson on the *Sales Analysis* report
(`Sales app -->
Reporting --> Sales`{.interpreted-text role="menuselection"}), click the
`Salesperson`{.interpreted-text role="guilabel"} option from the
`Group By`{.interpreted-text role="guilabel"} drop-down menu. The view
changes to group the records by salesperson, without filtering out any
records.

{.align-center}
:::

It is possible to *customize groups* by using a field present on the
model. To do so, click `Add Custom Group`{.interpreted-text
role="menuselection"}, and select a field from the drop-down menu.

::: {.note}
::: {.title}
Note
:::

Several groups can be used at the same time. The first group that is
selected is the main cluster, the next one that is added further divides
the main group\'s categories, and so on. Furthermore, filters and groups
can be used together to refine the view even more.
:::

Comparison {#search/comparison}
----------

Certain reporting dashboards include a `Comparison`{.interpreted-text
role="guilabel"} section in the drop-down menus of their
`Search...`{.interpreted-text role="guilabel"} bars. This includes the
`Overall Equipment Effectiveness
<../inventory_and_mrp/manufacturing/reporting/oee>`{.interpreted-text
role="doc"} report for the *Manufacturing* app, and the
`Purchase <../inventory_and_mrp/purchase/advanced/analyze>`{.interpreted-text
role="doc"} report for the *Purchase* app, among others.

The options in the `fa-adjust`{.interpreted-text role="icon"}
`Comparison`{.interpreted-text role="guilabel"} section are used to
compare data from two different time periods. There are two comparison
options to choose from: `(Time
Filter): Previous Period`{.interpreted-text role="guilabel"} and
`(Time Filter): Previous Year`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

For some reports, the `Comparison`{.interpreted-text role="guilabel"}
section **only** appears in the `Search...`{.interpreted-text
role="guilabel"} bar drop-down menu if one (or more) time periods have
been selected in the `Filters`{.interpreted-text role="guilabel"}
column. This is because, if no time period is specified, there is
nothing to compare.

Additionally, some reports only allow use of the
`Comparison`{.interpreted-text role="guilabel"} feature when the
`fa-pie-chart`{.interpreted-text role="icon"}
`(pie chart)`{.interpreted-text role="guilabel"} graph type, or the
`oi-view-pivot`{.interpreted-text role="icon"}
`(pivot)`{.interpreted-text role="guilabel"} view, is selected. A
`Comparison`{.interpreted-text role="guilabel"} option can be selected
even if another view is enabled, but doing so does **not** change the
way data is displayed on the report.
:::

{.align-center}

To view data using one of the two comparisons, begin by selecting a time
period in the `Filters`{.interpreted-text role="guilabel"} column of the
`Search...`{.interpreted-text role="guilabel"} bar drop-down menu. Then,
select either `(Time Filter): Previous Period`{.interpreted-text
role="guilabel"} or `(Time Filter): Previous Year`{.interpreted-text
role="guilabel"} in the `Comparison`{.interpreted-text role="guilabel"}
section.

With one of the `Comparison`{.interpreted-text role="guilabel"} options
enabled, the report compares the data for the selected period, with the
data for the same unit of time (month, quarter, year), one period or
year prior. The way the data is displayed depends on the selected view:

-   The `fa-bar-chart`{.interpreted-text role="icon"}
    `(bar chart)`{.interpreted-text role="guilabel"} shows two bars,
    side-by-side, for each unit of time for the selected time period.
    The left bar represents the selected time period, while the right
    bar represents the previous time period.
-   The `fa-line-chart`{.interpreted-text role="icon"}
    `(line chart)`{.interpreted-text role="guilabel"} is displayed with
    two lines, one representing the selected time period, and the other
    representing the previous time period.
-   The `fa-pie-chart`{.interpreted-text role="icon"}
    `(pie chart)`{.interpreted-text role="guilabel"} appears as a large
    circle with a smaller circle inside. The larger circle represents
    the selected time period, while the smaller circle represents the
    previous time period.
-   The `oi-view-pivot`{.interpreted-text role="icon"}
    `(pivot table)`{.interpreted-text role="guilabel"} is displayed with
    each column split into two smaller columns. The right column
    represents the selected time period, while the left column
    represents the previous time period.

::: {.example}
In the `Production Analysis`{.interpreted-text role="guilabel"} report
of the `Manufacturing`{.interpreted-text role="menuselection"} app, data
for the second quarter of 2024 is compared to data for the second
quarter of 2023. `Q2`{.interpreted-text role="guilabel"} is selected in
the `End Date`{.interpreted-text role="guilabel"} filter section of the
`Search...`{.interpreted-text role="guilabel"} bar drop-down menu. In
the `Comparison`{.interpreted-text role="guilabel"} section,
`End Date: Previous Year`{.interpreted-text role="guilabel"} is
selected.

The current year is 2024, so the larger circle shows data for the second
quarter (Q2) of 2024. The smaller circle shows data for the second
quarter (Q2) of 2023, which is the same time period, but one *year*
prior.

If `End Date: Previous Period`{.interpreted-text role="guilabel"} is
selected instead, the smaller circle shows data for the first quarter
(Q1) of 2024, which is the same time period, but one *period* prior.

{.align-center}
:::

Favorites {#search/favorites}
---------

Favorites are a way to save a specific search for future use, or as the
new default filter for the view.

To save the current view as a favorite, click the
`🔽 (down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, then select the `Save current search`{.interpreted-text
role="guilabel"} drop-down menu to display the following options:

-   Filter name: name of the favorited search.
-   `Default filter`{.interpreted-text role="guilabel"}: sets the
    favorited search as the default filter for the view.
-   `Shared`{.interpreted-text role="guilabel"}: makes the favorited
    search available to all users. By default, the favorited search is
    only available to the user who created it.

Once the options are set, click `Save`{.interpreted-text
role="guilabel"} to save the favorited search.

{.align-center}

Saved favorites can be accessed by clicking the
`🔽 (down arrow)`{.interpreted-text role="guilabel"} icon in the search
bar, then selecting the saved filter in the
`Favorites`{.interpreted-text role="guilabel"} drop-down menu. To remove
a saved favorite, click the `🗑️ (garbage can)`{.interpreted-text
role="guilabel"} icon next to the favorited search.

::: {.tip}
::: {.title}
Tip
:::

To view *all* favorited searches, first activate
`developer-mode`{.interpreted-text role="ref"}, and navigate to
`Settings app --> Technical --> User Interface: User-defined Filters`{.interpreted-text
role="menuselection"}. From here, all favorited searches can be viewed,
edited, archived, or deleted.
:::
