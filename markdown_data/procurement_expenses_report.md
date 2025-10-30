# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/advanced/procurement_expenses_report.md

Procurement expenses report
===========================

With the *Purchase* application, users can monitor procurement expenses
over time. This report helps companies track and analyze spending,
identify cost-saving opportunities, and ensure efficient budget
management.

Create procurement expenses report
----------------------------------

To create a procurement expenses report, first navigate to
`Purchase app --> Reporting --> Purchase`{.interpreted-text
role="menuselection"} to open the `Purchase Analysis`{.interpreted-text
role="guilabel"} dashboard.

By default, the dashboard displays a line chart overview of the
`Untaxed Total`{.interpreted-text role="guilabel"} of
`Purchase Orders`{.interpreted-text role="guilabel"} (POs) with a
`Confirmation Date`{.interpreted-text role="guilabel"} for the current
month, or of Requests for Quotation (RFQs) with a status of *Draft*,
*Sent*, or *Cancelled*.

### Add filters and groups

On the top-right, click the `oi-view-pivot`{.interpreted-text
role="icon"} `(pivot)`{.interpreted-text role="guilabel"} icon to switch
to pivot view.

::: {.tip}
::: {.title}
Tip
:::

While the procurement expenses report can also be
`viewed <purchase/view-results>`{.interpreted-text role="ref"} as a
`fa-bar-chart`{.interpreted-text role="icon"}
`(bar chart)`{.interpreted-text role="guilabel"},
`fa-line-chart`{.interpreted-text role="icon"}
`(line chart)`{.interpreted-text role="guilabel"}, or
`fa-pie-chart`{.interpreted-text role="icon"}
`(pie chart)`{.interpreted-text role="guilabel"}, the pivot view
provides the most detailed view of the data, and is the recommended
starting point.
:::

Remove any default filters from the `Search...`{.interpreted-text
role="guilabel"} bar. Then, click the `fa-caret-down`{.interpreted-text
role="icon"} `(down)`{.interpreted-text role="guilabel"} icon to open
the drop-down menu that contains the `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns.

::: {.note}
::: {.title}
Note
:::

Unless otherwise specified, the report displays data from both
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} and
`POs (Purchase Orders)`{.interpreted-text role="abbr"}. This can be
changed by selecting either `Requests for Quotation`{.interpreted-text
role="guilabel"} or `Purchase Orders`{.interpreted-text role="guilabel"}
under the `Filters`{.interpreted-text role="guilabel"} column.
:::

Under the `Filters`{.interpreted-text role="guilabel"} column, select a
time frame to use for comparison. The report can be filtered by either
`Order Date`{.interpreted-text role="guilabel"} or
`Confirmation Date`{.interpreted-text role="guilabel"}. Choose one from
the list, and click the `fa-caret-down`{.interpreted-text role="icon"}
`(down)`{.interpreted-text role="guilabel"} icon to specify the date
range, either by month, quarter, or year.

Next, under the `Group by`{.interpreted-text role="guilabel"} column,
select `Vendor`{.interpreted-text role="guilabel"}. Then, select
`Product Category`{.interpreted-text role="guilabel"}, which is also
located in the `Group By`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

The selections under the `Group By`{.interpreted-text role="guilabel"}
heading can be altered, depending on the needs of the individual
company. For example, selecting `Product`{.interpreted-text
role="guilabel"}, instead of `Product
Category`{.interpreted-text role="guilabel"}, provides a more in depth
look at the performance of specific items, in place of an entire
category.
:::

Next, make a selection under the `Comparison`{.interpreted-text
role="guilabel"} heading that appears. These options are only available
after the date range is selected under the `Filters`{.interpreted-text
role="guilabel"} column, and vary based on that range.
`Previous Period`{.interpreted-text role="guilabel"} adds a comparison
to the previous period, such as the last month or quarter.
`Previous Year`{.interpreted-text role="guilabel"} compares the same
time period from the previous year.

::: {.note}
::: {.title}
Note
:::

While multiple time-based filters can be added at once, only one
comparison can be selected at a time.
:::

{.align-center}

### Add measures

After selecting the `Filters`{.interpreted-text role="guilabel"},
`Group by`{.interpreted-text role="guilabel"}, and
`Comparison`{.interpreted-text role="guilabel"} settings, click out of
the drop-down menu.

By default, the report displays data with the following measures:
`Order`{.interpreted-text role="guilabel"}, `Total`{.interpreted-text
role="guilabel"}, `Untaxed Total`{.interpreted-text role="guilabel"},
and `Count`{.interpreted-text role="guilabel"}. Click
`Measures`{.interpreted-text role="guilabel"} at the top-left to open
the drop-down list of available measures.

Click the following specific measures to include additional columns for
the procurement expenses report:

-   `Total`{.interpreted-text role="guilabel"} and
    `Untaxed Total`{.interpreted-text role="guilabel"}: can include one
    or both measures. These are included for overall spending analysis.
-   `Average Cost`{.interpreted-text role="guilabel"}: included to
    evaluate cost efficiency.
-   `Days to Confirm`{.interpreted-text role="guilabel"} and
    `Days to Receive`{.interpreted-text role="guilabel"}: used to assess
    supplier performance.
-   `Qty Ordered`{.interpreted-text role="guilabel"} and
    `Qty Received`{.interpreted-text role="guilabel"}: used to
    understand order efficiency.
-   `Qty Billed`{.interpreted-text role="guilabel"} and
    `Qty to be Billed`{.interpreted-text role="guilabel"}: used to track
    order accuracy.

::: {.tip}
::: {.title}
Tip
:::

Additional measures can be included in the report, if desired, to
provide additional insights. For example,
`Gross Weight`{.interpreted-text role="guilabel"} and
`Volume`{.interpreted-text role="guilabel"} may be included for further
logistics and management analysis.
:::

After selecting all necessary measures, click out of the drop-down menu.

View results {#purchase/view-results}
------------

After all of the filters and measures have been selected, the report
generates in the selected view.

{.align-center}

Click `Insert in Spreadsheet`{.interpreted-text role="guilabel"} to add
the pivot view into an editable spreadsheet format within the
*Documents* app.

::: {.important}
::: {.title}
Important
:::

The `Insert in Spreadsheet`{.interpreted-text role="guilabel"} option is
**only** available if the *Documents Spreadsheet* module is installed.
:::

::: {.note}
::: {.title}
Note
:::

The procurement expenses report is also available in graph view. Click
the `fa-area-chart`{.interpreted-text role="icon"} `(area
chart)`{.interpreted-text role="guilabel"} icon to change to graph view.
Click the corresponding icon at the top of the report to switch to a
`fa-bar-chart`{.interpreted-text role="icon"}
`(bar chart)`{.interpreted-text role="guilabel"},
`fa-line-chart`{.interpreted-text role="icon"} `(line
chart)`{.interpreted-text role="guilabel"}, or
`fa-pie-chart`{.interpreted-text role="icon"}
`(pie chart)`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
To save this report as a *favorite*, see
`search/favorites`{.interpreted-text role="ref"}.
:::
