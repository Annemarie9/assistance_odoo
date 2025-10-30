Quality leads report
====================

A *quality lead* is a lead that is likely to result in a sale. It should
match the characteristics most commonly believed to help salespeople
close a deal, in addition to more precise criteria that is specific to
each organization.

::: {.note}
::: {.title}
Note
:::

The specific criteria that defines a *quality lead* is different for
every organization. For more information, see
`Define a quality lead <track_links/define-a-lead>`{.interpreted-text
role="ref"}.
:::

A quality leads *report* compares how many quality leads each
salesperson has received over a specific amount of time, such as within
the past 30 days. Sales managers can use such a report to make more
informed decisions when assigning new leads to their team

::: {.example}
A sales manager pulls a quality leads report using their company\'s
criteria:

-   Leads must include a phone number and an email address.
-   The email address must be from a professional domain.
-   The source for the lead must be from a live chat conversation or an
    appointment with a salesperson.

After running the report, the manager can see that, although everyone\'s
ability to close a deal has varied, some members of the sales team have
received a higher number of quality leads than others.

{.align-center}

Using this information, the sales manager may decide to assign more
quality leads to the sales people currently on the lower end, to balance
out the distribution of quality leads.
:::

Create a quality leads report {#track_links/create-quality-leads-report}
-----------------------------

To create a quality leads report, first navigate to
`CRM app --> Reporting -->
Pipeline`{.interpreted-text role="menuselection"} to open the
`Pipeline Analysis`{.interpreted-text role="guilabel"} dashboard. Click
into the `Search...`{.interpreted-text role="guilabel"} bar at the top
of the page and remove any active filters.

Click the `🔻(triangle pointed down)`{.interpreted-text role="guilabel"}
icon to the right of the `Search...`{.interpreted-text role="guilabel"}
bar to open the drop-down mega menu that contains
`Filters`{.interpreted-text role="guilabel"},
`Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns. Click
`Add Custom Filter`{.interpreted-text role="guilabel"}. This opens a
`Add
Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

The `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window
allows for the creation of more specific filters.

### Add custom filters

In order to generate a quality leads report, filters need to be created
for the following conditions:

-   `Starting date <quality_leads_report/starting-date>`{.interpreted-text
    role="ref"}: limits results to those created within a specific time
    frame.
-   `Specific sales teams <quality_leads_report/sales-team>`{.interpreted-text
    role="ref"}: limits results to only include leads for one or more
    sales teams. This filter is optional and should not be included if
    the is intended for the entire company.
-   `Exclude unassigned leads <quality_leads_report/unassigned-leads>`{.interpreted-text
    role="ref"}: excludes leads without an assigned salesperson.
-   `Include archived leads <quality_leads_report/archived-leads>`{.interpreted-text
    role="ref"}: ensures that both active and inactive leads are
    included in the results.
-   `Add rules for quality leads <quality_leads_report/add-quality-rules>`{.interpreted-text
    role="ref"}: includes or excludes results based on criteria that is
    specific to a company or sales team.

![An example of the *Custom Filter* pop-up window with all of the
default rules
configured.](quality_leads_report/configured-custom-rules.png){.align-center}

#### Add a starting date filter {#quality_leads_report/starting-date}

Begin by first defining the rule\'s parameter with a date range, by
clicking into the first field, on the left of the row, and typing
[Created On]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, or by scrolling through the menu\'s list to locate
it.

In the rule\'s operator drop-down menu, define the parameter further by
selecting either:

-   `>= (greater than or equal to)`{.interpreted-text role="guilabel"}
    to specify a start date and include all entries *after* that start
    date (as well as the initial value itself); or
-   `is between`{.interpreted-text role="guilabel"} to more sharply
    define a time frame with a clear start and end date. All matching
    entries that fit within the defined start and end dates are included
    in the report.

With either option, use the pop-up calendar\'s day and time pickers, in
the far right field, to define the respective date range. Setting these
values concludes the creation of the first rule.

#### Add a sales team filter {#quality_leads_report/sales-team}

::: {.note}
::: {.title}
Note
:::

This filter is optional. To view results for the entire company, do
**not** add this filter.
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

#### Exclude unassigned leads {#quality_leads_report/unassigned-leads}

Next, add a `New Rule`{.interpreted-text role="guilabel"}. Then, click
into the first field for the new rule, and type
[Salesperson]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, or scroll to search through the list to locate it.

In the rule\'s second field, select `is set`{.interpreted-text
role="guilabel"} from the drop-down menu. Selecting this operator
excludes any leads not assigned to a specific salesperson.

#### Include archived leads {#quality_leads_report/archived-leads}

::: {.tip}
::: {.title}
Tip
:::

This filter is also optional, as it adds archived (inactive) leads to
the report, however it is recommended to include this since it pulls
*all* assigned leads, regardless of status, into the report. This
ensures a more accurate representation of assigned leads is captured.
However, to pull a report that only includes active leads, do **not**
activate this feature.
:::

Next, in the upper-right corner of the
`Add Custom filter`{.interpreted-text role="guilabel"} pop-up window,
move the `Include archived`{.interpreted-text role="guilabel"} toggle to
active.

{.align-center}

Enabling this feature adds archived (inactive) leads to the report.

#### Add rules for quality leads {#quality_leads_report/add-quality-rules}

The filters added in this step vary, based on how an organization
defines a *quality lead*.

##### Define a quality lead {#track_links/define-a-lead}

As defined earlier, a *quality lead* is a lead that is likely to result
in a won opportunity. Although the exact criteria for a quality lead
varies from organization to organization, it is often a combination of
factors commonly attributed to positive sales outcomes, in addition to
factors valued by the specific organization.

In addition to the basic filters and grouping options outlined in the
general `Quality leads
report <track_links/create-quality-leads-report>`{.interpreted-text
role="ref"}, consider the following filters when defining a quality
lead:

-   `Email`{.interpreted-text role="guilabel"} or
    `Phone`{.interpreted-text role="guilabel"}: the information in these
    fields can help determine whether or not a lead is a professional
    contact.
-   `Source`{.interpreted-text role="guilabel"}: this field links to the
    marketing and lead generation efforts from other Odoo applications,
    including *Live Chat*, *Social Marketing*, and *Email Marketing*.
-   `Stage`{.interpreted-text role="guilabel"}: this filter can be used
    to eliminate or target leads that have reached specific stages.
-   `Medium`{.interpreted-text role="guilabel"}: a lead\'s source can
    indicate its quality level, as various channels have different won
    rates and expected revenues.
-   `Campaign`{.interpreted-text role="guilabel"}: adding this filter
    helps track of the success of different marketing efforts to capture
    high quality leads.
-   `Lost Reason`{.interpreted-text role="guilabel"}: exclude leads that
    may appear to be quality based on various criteria, but have been
    marked as *lost* for specified reasons.
-   `Tags`{.interpreted-text role="guilabel"}: include or exclude
    results based on one or more customized tags.

::: {.tip}
::: {.title}
Tip
:::

When adding rules to a custom filter, keep the statements preceding each
rule in mind. The statement above a rule determines whether the search
results must match **all** of the rules below the statement, or **any**
of the rules below the statement.

{.align-center}
:::

View the report
---------------

::: {.important}
::: {.title}
Important
:::

At the top of the `Add Custom Filter`{.interpreted-text role="guilabel"}
form, there is an option to match `any`{.interpreted-text
role="guilabel"} or `all`{.interpreted-text role="guilabel"} of the
rules. In order to properly run the report, only records that match
**all** of the following filters should be included. Before adding the
filters, make sure `all`{.interpreted-text role="guilabel"} is selected
in this field.

{.align-center}
:::

After the filters are configured, click `Add`{.interpreted-text
role="guilabel"}. The default display for the report is a bar graph,
where the leads are grouped by *stage*.

To group the results by salesperson, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar to
open the drop-down mega menu. Under the `Group
By`{.interpreted-text role="guilabel"} heading, select
`Salesperson`{.interpreted-text role="guilabel"}. In the same column,
under the `Group By`{.interpreted-text role="guilabel"} heading, click
`Add a Custom Group`{.interpreted-text role="guilabel"}, then select
`Active`{.interpreted-text role="guilabel"} on the resulting drop-down
menu to layer in lead *status*, under the parent
`Salesperson`{.interpreted-text role="guilabel"} grouping.

The report now displays the total count of *quality leads* each
salesperson has received in the designated time period. Because there
are layered `Group By`{.interpreted-text role="guilabel"} filters, the
grouped leads are also color-coded to identify whether they are *active*
or *marked as lost*.

::: {.tip}
::: {.title}
Tip
:::

To save this search for later, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon next
to the `Search...`{.interpreted-text role="guilabel"} bar to open the
drop-down menu. Under the `Favorites`{.interpreted-text role="guilabel"}
heading, click `Save current search`{.interpreted-text role="guilabel"}.

In the drop-down menu, rename the report from the default
[Pipeline]{.title-ref} label to [Quality Leads]{.title-ref}, and click
`Save`{.interpreted-text role="guilabel"}.
:::
