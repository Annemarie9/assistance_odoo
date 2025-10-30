Forecast report
===============

The *Forecast* report in the *CRM* app allows users to view upcoming
opportunities and build a forecast of potential sales. Opportunities are
grouped by the month of their expected closing date, and can be
dragged-and-dropped to adjust the deadline.

To access the *Forecast* report, navigate to
`CRM app --> Reporting --> Forecast`{.interpreted-text
role="menuselection"}.

Navigate the forecast report
----------------------------

The default `Forecast`{.interpreted-text role="guilabel"} report
includes opportunities assigned to the current user\'s pipeline, and are
expected to close within four months. It also shows opportunities
without an assigned expected closing date. The opportunities are grouped
by month in a `oi-view-kanban`{.interpreted-text role="icon"}
`(Kanban)`{.interpreted-text role="guilabel"} view.

{.align-center}

### Expected closing date

Opportunities are grouped by the date assigned in the *Expected Closing*
field on an opportunity form. To change this date directly from the
`Forecast`{.interpreted-text role="guilabel"} page, select the Kanban
card for the desired opportunity, then click and drag the card to the
desired column.

::: {.note}
::: {.title}
Note
:::

The default time frame for the forecast is *month*. This can be changed
by clicking the `fa-caret-down`{.interpreted-text role="icon"}
`(down)`{.interpreted-text role="guilabel"} icon next to the
`Search...`{.interpreted-text role="guilabel"} bar at the top of the
report. Under the `Group By`{.interpreted-text role="guilabel"} heading
in the resulting drop-down menu, click
`Expected Closing`{.interpreted-text role="guilabel"} to expand the list
of available options, and select a desired amount of time from the list.
:::

After an opportunity is added to a new month, the *Expected Closing*
field on the opportunity form is updated to the *last* date of the new
month.

::: {.tip}
::: {.title}
Tip
:::

The *Expected Closing* field can also be manually updated on the
opportunity card. To do that, click on the Kanban card for an
opportunity on the `Forecast`{.interpreted-text role="guilabel"} page to
open the opportunity\'s detail form. Click in the
`Expected Closing`{.interpreted-text role="guilabel"} field, and use the
calendar popover to select a new closing date.
:::

### Prorated revenue

At the top of the column for each month on the
`Forecast`{.interpreted-text role="guilabel"} reporting page, to the
right of the progress bar, is a sum of the prorated revenue for that
time frame.

The prorated revenue is calculated using the formula below:

$$\text{Expected Revenue} \times \text{Probability} = \text{Prorated Revenue}$$

As opportunities are moved from one column to another, the column\'s
revenue is automatically updated to reflect the change.

::: {.example}
A forecast report for June includes two opportunities:

The first opportunity, [Global Solutions]{.title-ref}, has an expected
revenue of [\$3,800]{.title-ref}, and a probability of
[90%]{.title-ref}. This results in a prorated revenue of
[\$3,420]{.title-ref}.

The second opportunity, [Quote for 600 Chairs]{.title-ref}, has an
expected revenue of [\$22,500]{.title-ref}, and a probability of
[20%]{.title-ref}. This results in a prorated revenue of
[\$4,500]{.title-ref}.

The combined prorated revenue of the opportunities is
[\$7,920]{.title-ref}, which is listed at the top of the column for the
month.

{.align-center}
:::

::: {.seealso}
For more information on how probability is assigned to opportunities,
see `../track_leads/lead_scoring`{.interpreted-text role="doc"}
:::

View results
------------

Click the `fa-area-chart`{.interpreted-text role="icon"}
`(area chart)`{.interpreted-text role="guilabel"} icon to change to
graph view. Then, click the corresponding icon at the top of the report
to switch to a `fa-bar-chart`{.interpreted-text role="icon"} `(bar
chart)`{.interpreted-text role="guilabel"},
`fa-line-chart`{.interpreted-text role="icon"}
`(line chart)`{.interpreted-text role="guilabel"}, or
`fa-pie-chart`{.interpreted-text role="icon"} `(pie
chart)`{.interpreted-text role="guilabel"}.

{.align-center}

Click the `oi-view-pivot`{.interpreted-text role="icon"}
`(pivot)`{.interpreted-text role="guilabel"} icon to change to the pivot
view, or the `oi-view-list`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon to change to the list
view.

::: {.tip}
::: {.title}
Tip
:::

The `pivot view <reporting/using-pivot>`{.interpreted-text role="ref"}
can be used to view and analyze data in a more in-depth manner. Multiple
measures can be selected, and data can be viewed by month, and by
opportunity stage.

{.align-center}
:::

::: {.seealso}
To save this report as a *favorite*, see
`search/favorites`{.interpreted-text role="ref"}.
:::
