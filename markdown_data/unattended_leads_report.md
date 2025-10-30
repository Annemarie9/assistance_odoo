Unattended leads report
=======================

*Unattended leads* are leads that have scheduled activities that are
either due or past due. Whenever an activity is scheduled, Odoo tracks
the due date, and sends email reminders to the users the activity is
assigned to.

An *unattended leads report* compiles all active leads in the pipeline
with due or past due activities, allowing a sales manager to identify
which opportunities require immediate attention.

By pulling a daily unattended leads report, sales managers can remind
their teams to address outstanding activities before they become past
due, helping avoid neglected leads and reinforcing proactive behaviors
in their salespeople.

::: {.example}
A sales manager starts their day by pulling an unattended leads report,
and upon switching to list view, they see the following:

{.align-center}

Their team member, Mitchell, has two leads in the *Proposition* stage
with activities that are due.

The yellow `📞 (phone)`{.interpreted-text role="guilabel"} icon indicates
that the [Modern Open Space]{.title-ref} lead has a phone call activity
scheduled for today. The red `✉️ (envelope)`{.interpreted-text
role="guilabel"} icon indicates that the [5 VP Chairs]{.title-ref} lead
has an email activity scheduled that is past due.

Clicking on the [5 VP Chairs]{.title-ref} lead, the sales manager opens
the record of the lead and reviews the chatter. They see that the email
was scheduled to be sent two days ago, but Mitchell never marked this
activity as done.

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

In order to pull a unattended leads report, sales teams **must** be
regularly utilizing activity in the *CRM* pipeline, on individual lead
and opportunity cards.

It is **not** possible to compile a complete report if the sales people
are not using the *Activities* feature in the *chatter*

For more information, refer to
`Activities <../../../essentials/activities>`{.interpreted-text
role="doc"}
:::

Create an unattended leads report
---------------------------------

To create an unattended leads report, first navigate to
`CRM app --> Reporting -->
Pipeline`{.interpreted-text role="menuselection"} to open the
`Pipeline Analysis`{.interpreted-text role="guilabel"} dashboard. Click
into the `Search...`{.interpreted-text role="guilabel"} bar at the top
of the page, and remove all of the default filters.

::: {.note}
::: {.title}
Note
:::

The `Created on`{.interpreted-text role="guilabel"} filter can remain
active, as this variable may be useful to include in the report.
:::

Next, add custom filters by clicking the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar to
open the drop-down menu that contains `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns. Under the
`Filters`{.interpreted-text role="guilabel"} column, click
`Add Custom Filter`{.interpreted-text role="guilabel"}, which opens an
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

The `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window
allows for the creation of more specific filters.

### Add custom filters

In order to generate an unattended leads report, filters need to be
created for the following conditions:

> -   `Past due activities <unattended_leads_report/past-due>`{.interpreted-text
>     role="ref"}: limits the results to only include leads with an
>     assigned activity where the due date has past. This can be altered
>     to include activities due to occur on the date the report is
>     generated as well.
> -   `Unassigned leads <unattended_leads_report/exclude-unassigned>`{.interpreted-text
>     role="ref"}: excludes leads without an assigned salesperson.
> -   `Specific sales teams <unattended_leads_report/sales-team>`{.interpreted-text
>     role="ref"}: limits results to only include leads assigned to one
>     or more sales teams. This filter is optional and should not be
>     included if the report is intended for the entire company.

#### Add filter for past due activities {#unattended_leads_report/past-due}

Click the first field for the new rule, and type
[Activities]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, or scroll to search through the list to locate it.
Then, next to `Activities`{.interpreted-text role="guilabel"}, click the
`> (greater than sign)`{.interpreted-text role="guilabel"} to open a new
drop-down menu with secondary conditions.

Type [Due Date]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, or scroll to search through the list. Click
`Due Date`{.interpreted-text role="guilabel"} to add it to the rule.

> {.align-center}

Then, click into then next field and select `<=`{.interpreted-text
role="guilabel"} from the drop-down menu. Selecting this operator
includes all activities with a due date up to, and including, the date
selected in the next field.

The third field can be left as today\'s date, or adjusted as needed.

#### Exclude unassigned leads {#unattended_leads_report/exclude-unassigned}

After filtering for activities, add a `New Rule`{.interpreted-text
role="guilabel"}. Then, click into the first field for the new rule, and
type [Salesperson]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, or scroll to search through the list to locate it.

In the rule\'s second field, select `is set`{.interpreted-text
role="guilabel"} from the drop-down menu. Selecting this operator
excludes any leads not assigned to a specific salesperson.

#### Add a Sales team {#unattended_leads_report/sales-team}

::: {.note}
::: {.title}
Note
:::

This filter is optional. To view results for the entire company, do
**not** add this filter, and continue to
`View results <unattended_leads_report/view-results>`{.interpreted-text
role="ref"}
:::

To limit the results of the report to one or more sales teams, click
`New Rule`{.interpreted-text role="guilabel"}. Next, click the first
field for the new rule, and type [Sales Team]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar, or scroll to search
through the list to locate it.

In the rule\'s second field, select `is in`{.interpreted-text
role="guilabel"} from the drop-down menu. Selecting this operator limits
results to the sales teams selected in the next field.

Lastly, in the third field, select the desired sales team from the
drop-down menu. Multiple teams can be added in this field, where each
parameter is treated with an \"or\" (e.g. \"any\") operator in the
search logic.

![An example of the **Add Custom Filter** pop-up window with all of the
rules
configured.](unattended_leads_report/configured-custom-rules.png){.align-center}

View results {#unattended_leads_report/view-results}
------------

At the top of the `Add Custom Filter`{.interpreted-text role="guilabel"}
form, there is an option to match `any`{.interpreted-text
role="guilabel"} or `all`{.interpreted-text role="guilabel"} of the
rules. In order to properly run the report, only records that match
**all** of the following filters should be included. Before adding the
filters, make sure `all`{.interpreted-text role="guilabel"} is selected
in this field.

{.align-center}

After the filters are configured, click `Add`{.interpreted-text
role="guilabel"}. The resulting report displays all leads assigned to a
salesperson where an activity is past due, or is due on the current
date. The default display is a bar graph, where the leads are grouped by
*stage*.

To group the results by salesperson, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar to
open the drop-down menu that contains `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns. Under the
`Group By`{.interpreted-text role="guilabel"} heading, select
`Salesperson`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The option to group by `Sales Team`{.interpreted-text role="guilabel"}
is also available under the `Group By`{.interpreted-text
role="guilabel"} heading.
:::

To change to a *list* view, click the `≣ (list)`{.interpreted-text
role="guilabel"} icon in the top-right corner of the screen.

::: {.tip}
::: {.title}
Tip
:::

Clicking the `(toggle) icon`{.interpreted-text role="guilabel"} opens a
drop-down menu of additional columns that can be added to the report.

Some options that are beneficial for this report include:

-   `Activities`{.interpreted-text role="guilabel"}: the summary of the
    latest activity for this lead.
-   `Expected Closing`{.interpreted-text role="guilabel"}: the estimated
    date on which the lead will be won.
-   `Probability`{.interpreted-text role="guilabel"}: estimated success
    rate based on the stage.

{.align-center}
:::

::: {.seealso}
`Activities <../../../essentials/activities>`{.interpreted-text
role="doc"}
:::
