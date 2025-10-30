# File: /content/odoo_doc17.0/fr/content/applications/hr/employees/retention_report.md

Employee retention report
=========================

It is possible to determine the retention rate for a company by
modifying an existing report.

First, navigate to
`Employees app --> Reporting --> Contracts`{.interpreted-text
role="menuselection"} to open the `Employee Analysis`{.interpreted-text
role="guilabel"} report. This report shows the number of all employees
for the `Last 365 Days`{.interpreted-text role="guilabel"}, in a default
`fa-line-chart`{.interpreted-text role="icon"}
`Line Chart`{.interpreted-text role="guilabel"}.

{.align-center}

Next, click the `Measures`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} button in the upper-left
corner, revealing a drop-down menu. Click
`# Departure Employee`{.interpreted-text role="guilabel"} in the list,
then click away from the drop-down menu to close it. Now, the report
shows all the employees who were archived for the
`Last 365 Days`{.interpreted-text role="guilabel"}.

To view this information in an easier format, click the
`oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the upper-right
corner, and the data is presented in a pivot table.

The various employees, organized by department, populate the rows. The
columns display the following totals: the monthly
`Wage`{.interpreted-text role="guilabel"}, the
`Fuel Card`{.interpreted-text role="guilabel"} budget, total `Annual
Employee Budget`{.interpreted-text role="guilabel"} (also referred to as
the *annual salary*), the number of `New Employees`{.interpreted-text
role="guilabel"}, as well as the number of
`Departure Employees`{.interpreted-text role="guilabel"} (employees who
left).

{.align-center}

Employee retention rate comparison report
-----------------------------------------

It is possible to compare data only for employees who left, compared to
the total current employees, between two separate time periods. This is
commonly referred to as the *employee retention rate*.

To view these metrics, first open the
`Employee Analysis`{.interpreted-text role="guilabel"} report by
navigating to
`Employees app --> Reporting --> Contracts`{.interpreted-text
role="menuselection"}. Click the `oi-view-pivot`{.interpreted-text
role="icon"} `(Pivot)`{.interpreted-text role="guilabel"} icon in the
upper-right corner to view the information in a pivot table.

Next, click the `Measures`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} button in the upper-left
corner, revealing a drop-down menu. Click
`# New Employees`{.interpreted-text role="guilabel"},
`Annual Employee Budget`{.interpreted-text role="guilabel"},
`Fuel Card`{.interpreted-text role="guilabel"}, and
`Wage`{.interpreted-text role="guilabel"} in the list, to deselect these
metrics and hide them in the table. Then, click
`Count`{.interpreted-text role="guilabel"} at the bottom of the list to
enable that metric.

Click away from the drop-down menu to close it. Now, the report shows
all the employees who left the company
(`# Departure Employee`{.interpreted-text role="guilabel"}), as well as
the total number of employees (`Count`{.interpreted-text
role="guilabel"}), for the `Last 365 Days`{.interpreted-text
role="guilabel"}.

To compare the data for the current year with the previous year, click
the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} in the search bar,
revealing multiple filter and grouping options. Click
`Last 365 Days`{.interpreted-text role="guilabel"} in the
`fa-filter`{.interpreted-text role="icon"} `Filters`{.interpreted-text
role="guilabel"} column, to turn off that filter. Then, click
`Date`{.interpreted-text role="guilabel"}, and click the current year
(in this example, `2024`{.interpreted-text role="guilabel"}) from the
resulting drop-down menu.

Once a selection is made beneath `Date`{.interpreted-text
role="guilabel"} in the `fa-filter`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} column, a
`fa-adjust`{.interpreted-text role="icon"}
`Comparison`{.interpreted-text role="guilabel"} column appears. Click
`Date: Previous
Year`{.interpreted-text role="guilabel"} in the new column, then click
off of the drop-down menu to close it.

::: {.note}
::: {.title}
Note
:::

In Odoo, in order to access the `fa-adjust`{.interpreted-text
role="icon"} `Comparison`{.interpreted-text role="guilabel"} column, a
specific time *other than* `Last 365 Days`{.interpreted-text
role="guilabel"} **must** be selected. If not, the
`fa-adjust`{.interpreted-text role="icon"}
`Comparison`{.interpreted-text role="guilabel"} column is **not**
visible.
:::

Now, the pivot table displays the total number of employees who left the
company (`#
Departure Employee`{.interpreted-text role="guilabel"}), as well as the
total number of employees (`Count`{.interpreted-text role="guilabel"})
in the columns. These are further divided by the two different years,
and also displays the `Variation`{.interpreted-text role="guilabel"}
between the two.

The rows display the departments, and lists each individual employee for
each department, in the rows.

For a more concise view of this report, click
`fa-minus-square-o`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} above the top row of the
departments and employees, to collapse the rows. Now, the table presents
the total number of employees who left the company for both years,
compared to the total number of employees for both years, including the
difference, in a percentage.

::: {.example}
In this example, `3`{.interpreted-text role="guilabel"} employees out of
`83`{.interpreted-text role="guilabel"} left in 2023, and
`8`{.interpreted-text role="guilabel"} employees out of
`202`{.interpreted-text role="guilabel"} left in 2024. There was a
`166.67%`{.interpreted-text role="guilabel"} increase in the employees
who left in 2024 as compared to 2023. Additionally, there was a
`143.37%`{.interpreted-text role="guilabel"} increase in the total
number of employees in 2024 as compared to 2023.

{.align-center}
:::

To view more detailed rates for each department, click
`fa-plus-square`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} in the single row, revealing
a drop-down menu, and click `Department`{.interpreted-text
role="guilabel"}. Click away from the drop-down to close it, and now the
pivot table displays the total number of employees who left
(`# Departure Employee`{.interpreted-text role="guilabel"}), the total
number of employees (`Count`{.interpreted-text role="guilabel"}), and
the `Variation`{.interpreted-text role="guilabel"} (in a percentage) for
both 2023 and 2024, organized by department.

::: {.example}
In this example, it can be determined that the
`Management`{.interpreted-text role="guilabel"} department had the best
retention rate in 2024 as compared to 2023, with a
`Variation`{.interpreted-text role="guilabel"} rate of
`-100%`{.interpreted-text role="guilabel"}. Additionally, it can be
determined that the `Management / Research &
Development`{.interpreted-text role="guilabel"} department had the most
turnover, with a `Variation`{.interpreted-text role="guilabel"} of
`300%`{.interpreted-text role="guilabel"}.

{.align-center}
:::
