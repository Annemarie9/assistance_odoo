# File: /content/odoo_doc17.0/fr/content/applications/productivity/spreadsheet/insert.md

Link Odoo data
==============

You can insert and link several elements from your database in your
spreadsheets, namely:

-   pivots,
-   graphs,
-   lists, and
-   links to menus (i.e., a clickable link to a view of a specific
    model).

Before inserting `pivots <reporting/views/pivot>`{.interpreted-text
role="ref"}, `graphs <reporting/views/graph>`{.interpreted-text
role="ref"}, or lists, ensure they are tailored to your needs, as some
elements are more quickly - or only -configurable in their respective
view.

-   To insert pivots and graphs, click
    `Insert in spreadsheet`{.interpreted-text role="guilabel"} from any
    pivot or graph view.
-   To insert lists, click
    `Favorites --> Insert list in spreadsheet`{.interpreted-text
    role="menuselection"} from any list view.
-   To insert links to menus, click
    `Favorites --> Link menu in spreadsheet`{.interpreted-text
    role="menuselection"} from any view.

In the pop-up box, either create a new spreadsheet by selecting
`Blank spreadsheet`{.interpreted-text role="guilabel"} or insert it in
an existing one by selecting it and clicking `Confirm`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

By default, new spreadsheets are saved under the
`Spreadsheet`{.interpreted-text role="guilabel"} workspace of the
Documents app.
:::

Updating data {#insert/update}
-------------

Once inserted in a spreadsheet, your data is kept up-to-date, reflecting
any changes made to your database. Reopening the spreadsheet reloads the
linked data.

::: {.note}
::: {.title}
Note
:::

To update pivots and lists data without reopening a spreadsheet, go to
the menu bar and click `Data --> Refresh all data`{.interpreted-text
role="menuselection"}.
:::

### Pivot data

Using `Refresh all data`{.interpreted-text role="guilabel"} only updates
existing pivot cells. If new cells need to be added, go to the menu bar
and click `Data --> Re-insert pivot`{.interpreted-text
role="menuselection"} to fully update the pivot. Alternatively, click
`Insert pivot`{.interpreted-text role="guilabel"}, select the pivot, and
tick `Display missing
cells only`{.interpreted-text role="guilabel"} to preview first the
missing data.

> {.align-center}

To change which records are
`used by the pivot <search/preconfigured-filters>`{.interpreted-text
role="ref"}, right-click on a pivot cell, select
`See pivot properties`{.interpreted-text role="guilabel"}, and click
`Edit domain`{.interpreted-text role="guilabel"}.
