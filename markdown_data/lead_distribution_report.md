Lead distribution report
========================

A *lead distribution report* can be used to see if active leads are
being assigned equitably across sales members. It can also be used to
view the distribution of good or `quality leads
<quality_leads_report>`{.interpreted-text role="doc"}, and see how
frequently each salesperson is receiving (and keeping) leads.

Lead distribution reports can be run each week to help keep salespeople
on track, while providing them with ample good leads. These reports can
also be used to see whether sales members are staying productive, if
good leads are being lost too often by one salesperson, and what
percentage of good leads are being retained overall.

Create lead distribution reports
--------------------------------

To create a lead distribution report, first navigate to
`CRM app --> Reporting -->
Pipeline`{.interpreted-text role="menuselection"}, which reveals the
`Pipeline Analysis`{.interpreted-text role="guilabel"} dashboard.

Remove all the default filters in the search bar at the top of the page.
Doing so displays data related to *all* leads.

`Custom filters <search/custom-filters>`{.interpreted-text role="ref"}
can now be added by clicking the `fa-caret-down`{.interpreted-text
role="icon"} `(down caret)`{.interpreted-text role="guilabel"} icon, to
the right of the search bar, to reveal a drop-down menu of search and
filter options.

Three columns are displayed:
`Filters <search/filters>`{.interpreted-text role="ref"},
`Group By <search/group>`{.interpreted-text role="ref"}, and
`Favorites <search/favorites>`{.interpreted-text role="ref"}. To begin,
navigate to the bottom of the `Filters`{.interpreted-text
role="guilabel"} column, and click `Add Custom Filter`{.interpreted-text
role="guilabel"}. This opens an `Add Custom Filter`{.interpreted-text
role="guilabel"} pop-up window, where the essential filters can be added
one at a time.

### Essential filters {#crm/track_leads/essential-filters}

The following filter conditions are used to create a basic lead
distribution report. Together they gather all leads created within a
certain timespan that have an associated contact method and have been
assigned to a sales team.

#### Lead creation date

Click the first field, under
`Match any of the following rules:`{.interpreted-text role="guilabel"},
that has the value `Country`{.interpreted-text role="guilabel"} in it.
In the popover that appears, type [Created on]{.title-ref} in the search
bar, or scroll to search through the list to locate and select it.

Then, in the second field of that row, select `>=`{.interpreted-text
role="guilabel"} from the drop-down menu. This operator **only**
includes values greater than (or equal to) the value in the third,
rightmost field.

The third field on the `Add Custom Filter`{.interpreted-text
role="guilabel"} pop-up window should contain the earliest date leads
are selected from.

For example, setting [01/01/2024 00:00:00]{.title-ref} only includes
leads created from, and including, the first day of 2024.

{.align-center}

#### Sales team {#crm/track_leads/sales-team}

Click `New rule`{.interpreted-text role="guilabel"} to add another row
to the form, and choose `Sales Team`{.interpreted-text role="guilabel"}
for this rule\'s parameter. Then, click the second field of the new
rule, and select `contains`{.interpreted-text role="guilabel"} from the
drop-down menu. Selecting this operator filters for any records that
contain the words in the third, rightmost field.

::: {.tip}
::: {.title}
Tip
:::

For certain pre-determined, limited choices like a sales team, the
`is in`{.interpreted-text role="guilabel"} operator helps make for an
easier and more accurate selection, via a drop-down menu in the third
field, instead of risking a typo or incorrect value in the text box
field that accompanies the `contains`{.interpreted-text role="guilabel"}
operator.
:::

In this third field, enter the name of the desired sales team(s) that
are to be included in the report. It is important for all
`contains`{.interpreted-text role="guilabel"} argument values to be
specific enough and spelled correctly as they exist in Odoo, otherwise
this risks returning multiple (or zero) values.

{.align-center}

::: {.important}
::: {.title}
Important
:::

By adding more than one rule to the form, a new option emerges at the
top of the pop-up window above all the filters, to specify whether
`any`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} or
`all`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} of the conditions should
match. This distinction is important to set correctly, as it impacts the
driving logic of how the filters return data.
:::

Click the default `any`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} menu item and be sure the
`all`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} option is chosen instead.
This setting will **only** show records that match *all* the rules
contained inside the form.

#### Contact method {#crm/track_leads/phone-number}

::: {.note}
::: {.title}
Note
:::

The instruction below is not necessary, however, it\'s highly
recommended to add a set contact value to the report\'s search criteria.
A lot of spam, duplicate, or low quality leads can easily be screened
out of the report simply by adding either a set
`Phone`{.interpreted-text role="guilabel"} or `Email`{.interpreted-text
role="guilabel"} rule.
:::

Add another `New rule`{.interpreted-text role="guilabel"} to the form
and set the first field to the first field to `Phone`{.interpreted-text
role="guilabel"}. Then, select `is set`{.interpreted-text
role="guilabel"} from the drop-down menu in the second field. Selecting
this operator **only** filters for records that have a phone number
associated with the lead.

Alternatively (or in addition to the above rule), click
`New rule`{.interpreted-text role="guilabel"} and set the first field to
`Email`{.interpreted-text role="guilabel"}. Then, select
`is set`{.interpreted-text role="guilabel"} from the drop-down menu in
the second field.

These rules add only leads with an associated contact method to the
report.

#### Active status {#crm/track_leads/active-status}

Click the `fa-sitemap`{.interpreted-text role="icon"}
`(Add branch)`{.interpreted-text role="guilabel"} icon to the right of
the [Phone is set]{.title-ref} line, to add a new rule that branches
from the rules above.

Two horizontal sets of fields appear below a line showing
`any`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} `of:`{.interpreted-text
role="guilabel"} option. This setting filters for records that match
**any** of the rules contained inside. This uses the same logic as an OR
([\|]{.title-ref}) logical operator.

Set the first field to `Active`{.interpreted-text role="guilabel"}.
Then, select `is set`{.interpreted-text role="guilabel"} in the next
field.

Next, click the `fa-plus`{.interpreted-text role="icon"}
`(Add New Rule)`{.interpreted-text role="guilabel"} button next to
`Active is set`{.interpreted-text role="guilabel"} to create a new line
of fields beneath it.

Set the first field to `Active`{.interpreted-text role="guilabel"}.
Then, select `is not set`{.interpreted-text role="guilabel"} in the next
field.

{.align-center}

This rule adds the activity status of the lead to the report.

::: {.note}
::: {.title}
Note
:::

Active status is an important filter to include when creating a lead
distribution report because it includes **all** leads regardless of
won/lost or active/inactive status in the report. This provides a
comprehensive view of all the leads assigned to each sales member.
:::

#### Group by

Once all filters are set, click the `Add`{.interpreted-text
role="guilabel"} button to add these filters to the search bar. To have
the report grouped appropriately, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(down caret)`{.interpreted-text role="guilabel"} icon, to the right of
the search bar, and click `Salesperson`{.interpreted-text
role="guilabel"} in the `Group
By`{.interpreted-text role="guilabel"} section. All results are now
grouped by the salesperson assigned to each lead.

Once the rules for the filter are set, click the purple
`Confirm`{.interpreted-text role="guilabel"} button at the bottom of the
pop-up menu to save the custom filter and close the pop-up menu.

The `Pipeline Analysis`{.interpreted-text role="guilabel"} dashboard is
now displayed again with each filter rule in the search bar.

Click the `fa-area-chart`{.interpreted-text role="icon"}
`(Graph)`{.interpreted-text role="guilabel"} icon, to the right of the
search bar, to view the report as a bar chart. Alternatively, click the
`oi-view-list`{.interpreted-text role="icon"} `(List)`{.interpreted-text
role="guilabel"} icon to view leads in a grouped list.

::: {.tip}
::: {.title}
Tip
:::

To save the filter so it can easily be re-applied, click the
`Save current search`{.interpreted-text role="guilabel"} button in the
`Favorites`{.interpreted-text role="guilabel"} section of the search bar
drop-down menu.

Next, type a name for the filter in the text box below. Check the
`Shared`{.interpreted-text role="guilabel"} checkbox to have the filter
shared with any user with access to the pipeline. Finally, click the
purple `Save`{.interpreted-text role="guilabel"} button below to save
the filter.

The filter will now appear with the name it was given under the
`Favorites`{.interpreted-text role="guilabel"} section of the drop-down
menu and can be re-applied by clicking on it.
:::

### Filter for quality leads

The following additional conditions are provided as an example of a
*good*, but *not comprehensive*, set of rules for finding quality leads.
These filters should be applied on top of the
`crm/track_leads/essential-filters`{.interpreted-text role="ref"} in the
order specified to achieve a heavily-detailed filter.

-   **Referred-by:** Filter for referrals, such as by appointment or
    sales member.
-   **Source:** Filter for specific source UTMs, such as Facebook or
    LinkedIn.
-   **Notes:** Filter for internal notes.
-   **Tags:** Filter for categorical tags.
-   **Email:** Filter for specific email domains, such as gmail.com or
    yahoo.com.
-   **Salesperson:** Filter for leads associated with certain sales
    members.

These conditions can be added, removed, or modified to best fit the
desired information in the report.

::: {.seealso}
\- `quality_leads_report/add-quality-rules`{.interpreted-text
role="ref"} - `../../../essentials/search`{.interpreted-text role="doc"}
:::
