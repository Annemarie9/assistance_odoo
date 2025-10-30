Convert leads into opportunities
================================

*Leads* act as a qualifying step before an opportunity is created. This
provides additional time to review its potential, and gauge its
viability, before the opportunity is assigned to a salesperson.

Configuration
-------------

To activate the *Leads* setting, navigate to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and check the box labeled,
`Leads`{.interpreted-text role="guilabel"}. Then, click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Activating this feature adds a new menu option,
`Leads`{.interpreted-text role="guilabel"}, to the header bar, located
along the top of the screen.

{.align-center}

Once the *Leads* setting has been activated, it applies to all sales
teams by default. To turn off leads for a specific team, navigate to
`CRM app --> Configuration --> Sales Teams`{.interpreted-text
role="menuselection"}. Then, select a team from the list to open that
team\'s configuration page. Clear the `Leads`{.interpreted-text
role="guilabel"} checkbox, located beneath the
`Sales Team`{.interpreted-text role="guilabel"} field, then click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Convert a lead into an opportunity
----------------------------------

To convert a lead into an *opportunity*, navigate to
`CRM app --> Leads`{.interpreted-text role="menuselection"}, and click
on a lead from the list to open it.

::: {.warning}
::: {.title}
Warning
:::

If a `Similar Leads`{.interpreted-text role="guilabel"} smart button
appears at the top of the page for the lead, it indicates a similar lead
or opportunity already exists in the database. Before converting this
lead, click the smart button to confirm if the lead should be merged.

{.align-center}
:::

Click the `Convert to Opportunity`{.interpreted-text role="guilabel"}
button, located at the top-left of the page.

{.align-center}

This opens a `Convert to opportunity`{.interpreted-text role="guilabel"}
pop-up modal. Here, in the `Conversion
Action`{.interpreted-text role="guilabel"} field, select the
`Convert to opportunity`{.interpreted-text role="guilabel"} option.

::: {.note}
::: {.title}
Note
:::

To merge this lead with an existing similar lead or opportunity, select
`Merge with
existing opportunities`{.interpreted-text role="guilabel"} in the
`Conversion Action`{.interpreted-text role="guilabel"} field. This
generates a list of the similar leads/opportunities to be merged.

When merging, Odoo gives priority to whichever lead/opportunity was
created in the system first, merging the information into the first
created lead/opportunity. However, if a lead and an opportunity are
being merged, the resulting record is referred to as an opportunity,
regardless of which record was created first.
:::

Then, select a `Salesperson`{.interpreted-text role="guilabel"} and a
`Sales Team`{.interpreted-text role="guilabel"} to which the opportunity
should be assigned. Neither field is required, though if a selection is
made in the `Salesperson`{.interpreted-text role="guilabel"} field, the
`Sales Team`{.interpreted-text role="guilabel"} field is populated
automatically, based on the salesperson\'s team assignments.

If the lead has already been assigned to a salesperson or a team, these
fields automatically populate with that information.

{.align-center}

Under the `Customer`{.interpreted-text role="guilabel"} heading, choose
from the following options:

-   `Create a new customer`{.interpreted-text role="guilabel"}: choose
    this option to use the information in the lead to create a new
    customer record.
-   `Link to an existing customer`{.interpreted-text role="guilabel"}:
    choose this option, then select a customer from the resulting
    drop-down menu, to link this opportunity to an existing customer
    record.
-   `Do not link to a customer`{.interpreted-text role="guilabel"}:
    choose this option to convert the lead, but not link it to a new or
    existing customer.

Lastly, when all configurations are complete, click
`Create Opportunity`{.interpreted-text role="guilabel"}.

To view the newly created opportunity, navigate to
`CRM app --> My Pipeline`{.interpreted-text role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Some filters may need to be removed from the
`Search...`{.interpreted-text role="guilabel"} bar on the top
`Pipeline`{.interpreted-text role="guilabel"} page to view all
opportunities.
:::
