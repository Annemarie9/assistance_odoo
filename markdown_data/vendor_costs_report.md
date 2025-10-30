# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/advanced/vendor_costs_report.md

Vendor costs report
===================

With the *Purchase* application, users can track the fluctuation of
vendor costs over time. This allows users to identify the most expensive
vendors, and track seasonal changes.

Create vendor costs reports
---------------------------

To create a vendor costs report, first navigate to
`Purchase app --> Reporting -->
Purchase`{.interpreted-text role="menuselection"} to open the
`Purchase Analysis`{.interpreted-text role="guilabel"} dashboard. By
default, the dashboard displays a line chart overview of the
`Untaxed Total`{.interpreted-text role="guilabel"} of POs (Purchase
Orders) with a `Confirmation Date`{.interpreted-text role="guilabel"}
for the current month, or of RFQs (Requests for Quotation) with a status
of *Draft*, *Sent, or*Cancelled\*.

### Add filters and groups {#purchase/vender-cost-report-filters}

On the top-right, click the `oi-view-pivot`{.interpreted-text
role="icon"} `(pivot)`{.interpreted-text role="guilabel"} icon to switch
to pivot view.

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
date range to use for comparison. The report can be filtered by either
`Order Date`{.interpreted-text role="guilabel"} or
`Confirmation Date`{.interpreted-text role="guilabel"}. Choose one from
the list, and click the `fa-caret-down`{.interpreted-text role="icon"}
`(down)`{.interpreted-text role="guilabel"} icon to specify the date
range, either by month, quarter, or year.

Next, under the `Group by`{.interpreted-text role="guilabel"} column,
select `Vendor`{.interpreted-text role="guilabel"}. Then, select
`Product`{.interpreted-text role="guilabel"}, which is also located in
the `Group By`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

Selecting `Product`{.interpreted-text role="guilabel"} is **not**
required for this report. However, it is recommended, as it provides
additional insight into the performance of individual vendors.
Additional selections can be made under the `Group by`{.interpreted-text
role="guilabel"} heading as well, including `Product
Category`{.interpreted-text role="guilabel"}, `Status`{.interpreted-text
role="guilabel"}, and `Purchase Representative`{.interpreted-text
role="guilabel"}.

To ensure the report is generated correctly, make sure that
`Vendor`{.interpreted-text role="guilabel"} is the **first** selection
made under the `Group By`{.interpreted-text role="guilabel"} column.
:::

Next, make a selection under the `Comparison`{.interpreted-text
role="guilabel"} heading. These options are only available after the
date range is selected under the `Filters`{.interpreted-text
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

By default, the report displays with the following measures:
`Order`{.interpreted-text role="guilabel"}, `Total`{.interpreted-text
role="guilabel"}, `Untaxed Total`{.interpreted-text role="guilabel"},
and `Count`{.interpreted-text role="guilabel"}. Click
`Measures`{.interpreted-text role="guilabel"} at the top-left to open
the drop-down list of available measures. Click
`Average Cost`{.interpreted-text role="guilabel"} to add it to the
report. Select any additional measures to add to the report, or click on
any of the already selected measures to remove them, if desired.

::: {.tip}
::: {.title}
Tip
:::

It is recommended to run the report with at least
`Average Cost`{.interpreted-text role="guilabel"},
`Total`{.interpreted-text role="guilabel"}, or
`Untaxed Total`{.interpreted-text role="guilabel"} selected from the
`Measures`{.interpreted-text role="guilabel"} list. Additional measures,
such as `Days to Receive`{.interpreted-text role="guilabel"}, can be
added to provide additional insights.
:::

View results
------------

After all of the `filters and measures have been selected
<purchase/vender-cost-report-filters>`{.interpreted-text role="ref"},
the report generates in the pivot view. Click
`Insert in Spreadsheet`{.interpreted-text role="guilabel"} to add the
pivot view into an editable spreadsheet format within the *Documents*
app.

::: {.important}
::: {.title}
Important
:::

The `Insert in Spreadsheet`{.interpreted-text role="guilabel"} option is
only available if the *Documents Spreadsheet* module is installed.
:::

{.align-center}

::: {.note}
::: {.title}
Note
:::

The vendor costs report is also available in *graph* view. Click the
`fa-area-chart`{.interpreted-text role="icon"}
`(area chart)`{.interpreted-text role="guilabel"} icon to change to
graph view. Click the corresponding icon at the top of the report to
switch to a `fa-bar-chart`{.interpreted-text role="icon"}
`(bar chart)`{.interpreted-text role="guilabel"},
`fa-line-chart`{.interpreted-text role="icon"}
`(line chart)`{.interpreted-text role="guilabel"}, or
`fa-pie-chart`{.interpreted-text role="icon"}
`(pie chart)`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
To save this report as a *favorite*, see
`search/favorites`{.interpreted-text role="ref"}.
:::
