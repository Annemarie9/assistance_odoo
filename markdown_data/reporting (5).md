# File: /content/odoo_doc17.0/fr/content/applications/essentials/reporting.md

Reporting
=========

You can find several reports under the `Reporting`{.interpreted-text
role="guilabel"} menu of most apps that let you analyze and visualize
the data of your records.

Selecting a view {#reporting/views}
----------------

Depending on the report, Odoo can display the data in various ways.
Sometimes, a unique view fully tailored to the report is available,
while several views are available for others. However, two generic views
are dedicated to reporting: the graph and pivot views.

### Graph view {#reporting/views/graph}

The `graph view <reporting/using-graph>`{.interpreted-text role="ref"}
is used to visualize your records\' data, helping you identify patterns
and trends. The view is often found under the
`Reporting`{.interpreted-text role="guilabel"} menu of apps but can be
found elsewhere. Click the **graph view button** located at the top
right to access it.



### Pivot view {#reporting/views/pivot}

The `pivot view <reporting/using-pivot>`{.interpreted-text role="ref"}
is used to aggregate your records\' data and break it down for analysis.
The view is often found under the `Reporting`{.interpreted-text
role="guilabel"} menu of apps but can be found elsewhere. Click the
**pivot view button** located at the top right to access it.



Choosing measures {#reporting/choosing-measures}
-----------------

After selecting a view, you should ensure only the relevant records are
`filtered <search>`{.interpreted-text role="doc"}. Next, you should
choose what is measured. By default, a measure is always selected. If
you wish to edit it, click `Measures`{.interpreted-text role="guilabel"}
and choose one or, only for pivots, multiple measures.

::: {.note}
::: {.title}
Note
:::

When you select a measure, Odoo aggregates the values recorded on that
field for the filtered records. Only numerical fields
(`integer <studio/fields/simple-fields-integer>`{.interpreted-text
role="ref"},
`decimal <studio/fields/simple-fields-decimal>`{.interpreted-text
role="ref"}, `monetary
<studio/fields/simple-fields-monetary>`{.interpreted-text role="ref"})
can be measured. In addition, the `Count`{.interpreted-text
role="guilabel"} option is used to count the total number of filtered
records.
:::

After choosing what you want to measure, you can define how the data
should be `grouped
<search/group>`{.interpreted-text role="ref"} depending on the dimension
you want to analyze. By default, the data is often grouped by *Date \>
Month*, which is used to analyze the evolution of a measure over the
months.

::: {.tip}
::: {.title}
Tip
:::

When you filter a single time period, the option to compare it against
another one appears.


:::

::: {.example}
::: {.tabs}
::: {.tab}
Select measures

Among other measures, you could add the `Margin`{.interpreted-text
role="guilabel"} and `Count`{.interpreted-text role="guilabel"} measures
to the Sales Analysis report. By default, the
`Untaxed Amount`{.interpreted-text role="guilabel"} measure is selected.


:::

::: {.tab}
Group measures

You could group the measures by `Product Category`{.interpreted-text
role="guilabel"} at the level of rows on the previous Sales Analysis
report example.


:::
:::
:::

Using the pivot view {#reporting/using-pivot}
--------------------

Grouping data is quintessential to the pivot view. It enables drilling
down the data to gain deeper insights. While you can use the
`Group By`{.interpreted-text role="guilabel"} option to quickly add a
group at the level of rows, as shown in the example above, you can also
click the plus button (`➕`{.interpreted-text role="guilabel"}) next to
the `Total`{.interpreted-text role="guilabel"} header at the level of
rows *and* columns, and then select one of the **preconfigured groups**.
To remove one, click the minus button (`➖`{.interpreted-text
role="guilabel"}).

Once you have added a group, you can add new ones on the opposite axis
or the newly created subgroups.

::: {.example}
You could further divide the measures on the previous Sales Analysis
report example by the `Salesperson`{.interpreted-text role="guilabel"}
group at the level of columns and by the
`Order Date > Month`{.interpreted-text role="guilabel"} group on the
`All / Saleable / Office Furniture`{.interpreted-text role="guilabel"}
product category.


:::

::: {.tip}
::: {.title}
Tip
:::

\- Switch the rows and columns\' groups by clicking the flip axis button
(`⇄`{.interpreted-text role="guilabel"}). - Click on a measure\'s label
to sort the values by ascending (⏶) or descending (⏷) order. - Download
a [.xlsx]{.title-ref} version of the pivot by clicking the download
button (`⭳`{.interpreted-text role="guilabel"}).
:::

Using the graph view {#reporting/using-graph}
--------------------

Three graphs are available: the bar, line, and pie charts.

**Bar charts** are used to show the distribution or a comparison of
several categories. They are especially useful as they can deal with
larger data sets.

**Line charts** are useful to show changing time series and trends over
time.

**Pie charts** are used to show the distribution or a comparison of a
small number of categories when they form a meaningful whole.

::: {.tabs}
::: {.tab}
Bar chart


:::

::: {.tab}
Line chart


:::

::: {.tab}
Pie chart


:::
:::

::: {.tip}
::: {.title}
Tip
:::

For **bar** and **line** charts, you can use the stacked option when you
have at least two groups, which then appear on top of each other instead
of next to each other.

::: {.tabs}
::: {.tab}
Stacked bar chart


:::

::: {.tab}
Regular bar chart


:::

::: {.tab}
Stacked line chart


:::

::: {.tab}
Regular line chart


:::
:::

For **line** charts, you can use the cumulative option to sum values,
which is especially useful to show the change in growth over a time
period.

::: {.tabs}
::: {.tab}
Cumulative line chart


:::

::: {.tab}
Regular line chart


:::
:::
:::
