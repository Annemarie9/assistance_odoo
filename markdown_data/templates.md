# File: /content/odoo_doc17.0/fr/content/applications/productivity/spreadsheet/templates.md

Templates
=========

Spreadsheet templates allow you to quickly create spreadsheets without
starting from scratch.

Several pre-built templates are available when creating a new
spreadsheet from the **Documents** app, such as:

-   `budget reports <templates/budget-reports>`{.interpreted-text
    role="ref"},
-   `pipeline revenue reports <templates/pipeline-reports>`{.interpreted-text
    role="ref"}, or
-   `sales commission report <templates/sales-commission>`{.interpreted-text
    role="ref"}.



You can also
`save any spreadsheet as a template <templates/save>`{.interpreted-text
role="ref"} and `manage and edit
existing templates <templates/manage>`{.interpreted-text role="ref"}.

Default templates
-----------------

### Accounting: budget reports {#templates/budget-reports}

Budget reports compare a company\'s actual spending with its budget over
a defined period. Two templates are available: one uses quarterly
intervals (`Budget Report (Quarterly)`{.interpreted-text
role="guilabel"}), while the other uses monthly intervals
(`Budget Report (Monthly)`{.interpreted-text role="guilabel"}).



The cells under the `Actuals`{.interpreted-text role="guilabel"} column
are automatically filled in with the amount of money made and spent over
the corresponding period (month or quarter). The data is taken from
posted journal items under
`income and expense accounts <chart-of-account/type>`{.interpreted-text
role="ref"}.

::: {.warning}
::: {.title}
Warning
:::

Journal items under the `Other Income`{.interpreted-text
role="guilabel"} account type are not considered when collecting data.
:::

To analyze your budget\'s performance, fill the cells under the
`Budget`{.interpreted-text role="guilabel"} column with how much money
you expect to make (`Income`{.interpreted-text role="guilabel"} rows)
and spend (`Expenses`{.interpreted-text role="guilabel"} rows) over the
related period and per account. Then, the performance
(`Perf.`{.interpreted-text role="guilabel"}) column compares
`Actuals`{.interpreted-text role="guilabel"} data to their corresponding
budget, expressed as a percentage.

Lastly, the `Net Profit`{.interpreted-text role="guilabel"} row
represents the total `Income`{.interpreted-text role="guilabel"} minus
the total `Expenses`{.interpreted-text role="guilabel"} for the
`Actuals`{.interpreted-text role="guilabel"} and
`Budget`{.interpreted-text role="guilabel"} columns.

### CRM: pipeline revenue reports {#templates/pipeline-reports}

Two pipeline revenue reports are available. The
`Pipeline Revenue Report (Monthly)`{.interpreted-text role="guilabel"}
is dedicated to one-time revenue
(`NRR (non-recurring revenue)`{.interpreted-text role="abbr"}), while
the `MRR/NRR
Pipeline Revenue Report (Monthly)`{.interpreted-text role="guilabel"}
covers recurring and non-recurring revenue (`MRR (monthly
recurring revenue)`{.interpreted-text role="abbr"}).

::: {.tip}
::: {.title}
Tip
:::

Enable `Recurring Revenues`{.interpreted-text role="guilabel"} by going
to `CRM --> Configuration -->
Settings`{.interpreted-text role="menuselection"}.
:::



The cells under the `Actuals`{.interpreted-text role="guilabel"} column
are automatically filled in with the amount of monthly revenue from
**won** opportunities.

To compute the revenue performance, fill in the monthly revenue targets.

-   For the `Revenue by Team`{.interpreted-text role="guilabel"} sheet,
    fill in the cells under the `Target`{.interpreted-text
    role="guilabel"} columns for each sales team.
-   For the `Revenue by Salesperson`{.interpreted-text role="guilabel"}
    sheet, open the `Targets`{.interpreted-text role="guilabel"} sheet
    and fill in the cells next to each salesperson. Use the
    `Monthly Factor`{.interpreted-text role="guilabel"} table below to
    adapt the main targets depending on the month of the year.

Then, the performance (`Perf.`{.interpreted-text role="guilabel"})
column compares `Actuals`{.interpreted-text role="guilabel"} data to
their related budget, expressed as a percentage.

Lastly, the `Forecasted`{.interpreted-text role="guilabel"} column
gathers the monthly revenue of leads multiplied by their
`Probability`{.interpreted-text role="guilabel"} percentage.

::: {.note}
::: {.title}
Note
:::

For actuals and forecasts:

-   The `Expected Closing`{.interpreted-text role="guilabel"} date found
    on leads is used to assign them to a month.
-   The recurring monthly revenue is used even if the recurring plan\'s
    number of months is set to a different value than 1 month. For
    example, a yearly plan\'s revenue is divided by 12 months.
:::

### Sales: sales commission {#templates/sales-commission}

This report presents the monthly commission earned or due to each
salesperson.



The `Rate`{.interpreted-text role="guilabel"} column is pre-filled with
the percentage rate from the `Rates`{.interpreted-text role="guilabel"}
tab, which can be customized for each product category according to the
company\'s policy. Adjusting the rate for a specific product category
automatically updates the commission amount for that category.

The `Invoiced`{.interpreted-text role="guilabel"} column shows the total
amount of untaxed invoices grouped by salesperson and month.

Lastly, the `Comm.`{.interpreted-text role="guilabel"} column is
computed by multiplying the invoiced amount with the rate percentage.

Save a spreadsheet as a template {#templates/save}
--------------------------------

Any spreadsheet can be saved as a template. From the menu bar, click
`File --> Save
as template`{.interpreted-text role="menuselection"}. Modify the default
`Template Name`{.interpreted-text role="guilabel"} if necessary and
click `Confirm`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Templates are available to all users on the database.
:::

Manage and edit templates {#templates/manage}
-------------------------

Manage templates by going to
`Documents --> Configuration --> Spreadsheet Templates`{.interpreted-text
role="menuselection"}. Remove the `My Templates`{.interpreted-text
role="guilabel"}
`filter <search/preconfigured-filters>`{.interpreted-text role="ref"} to
view all templates in the database.

To edit an existing template, click [✎ Edit]{.title-ref} next to the
desired template. Modifications are automatically saved.

::: {.tip}
::: {.title}
Tip
:::

Use the download button under the `Data`{.interpreted-text
role="guilabel"} column to export a template in JSON format. The file
can be imported into another database.
:::
