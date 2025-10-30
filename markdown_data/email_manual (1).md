Create leads (from email or manually)
=====================================

Leads can be added to the *CRM* app from custom email aliases, and by
manually creating new records. This is in addition to the leads and
opportunities created in the app through the
`website contact form <opportunities_form>`{.interpreted-text
role="doc"}.

First, ensure the *Leads* feature is enabled in the database by
navigating to `CRM
app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Tick the `Leads`{.interpreted-text
role="guilabel"} checkbox, then click `Save`{.interpreted-text
role="guilabel"}.

Configure email aliases {#crm/configure_email_alias}
-----------------------

Each sales team has the option to create and utilize their own unique
email alias. When messages are sent to this address, a lead (or
opportunity), is created with the information from the message.

To create or update a sales teams\' email alias, navigate to
`CRM app -->
Configuration --> Sales Teams`{.interpreted-text role="menuselection"}.
Click on a team from the list to open the team\'s details page.

{.align-center}

In the `Email Alias`{.interpreted-text role="guilabel"} field, enter a
name for the email alias, or edit the existing name. In the
`Accept Emails From`{.interpreted-text role="guilabel"} field, use the
drop-down menu to choose who is allowed to send messages to this email
alias:

-   `Everyone`{.interpreted-text role="guilabel"}: messages are accepted
    from any email address.
-   `Authenticated Partners`{.interpreted-text role="guilabel"}: only
    accepts messages from email addresses associated with a a partner
    (contact or customer) record.
-   `Followers only`{.interpreted-text role="guilabel"}: only accepts
    messages from those who are following a record related to the team,
    such as a lead or opportunity. Messages are also accepted from team
    members.
-   `Authenticated Employees`{.interpreted-text role="guilabel"}: only
    accepts messages from email addresses that are connected to a record
    in the *Employees* app.

### Leads created from email

Leads created from email alias messages can be viewed by navigating to
`CRM app -->
Leads`{.interpreted-text role="menuselection"}. Click a lead from the
list to open it, and view the details.

The email received by the alias is added to the *chatter* thread for the
lead. The subject line of the message is added to the title field, and
the `Email`{.interpreted-text role="guilabel"} field is updated with the
contact\'s email address.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the *leads* feature is **not** enabled on the database, messages to
the email alias are added to the database as opportunities.
:::

::: {.seealso}
`../../../general/email_communication`{.interpreted-text role="doc"}
:::

Manually create leads
---------------------

Leads can be added directly to the *CRM* app by manually creating a new
record. Navigate to `CRM app --> Leads`{.interpreted-text
role="menuselection"} to view a list of existing leads.

::: {.tip}
::: {.title}
Tip
:::

Leads can also be added via the
`Generate Leads <lead_mining>`{.interpreted-text role="doc"} button.
:::

At the top-left of the list, click `New`{.interpreted-text
role="guilabel"} to open a blank `Leads`{.interpreted-text
role="guilabel"} form.

In the first field of the new form, enter a title for the new lead.
Next, enter a `Contact
Name`{.interpreted-text role="guilabel"}, and a
`Company Name`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If a lead is `converted to an opportunity <convert>`{.interpreted-text
role="doc"}, the `Company Name`{.interpreted-text role="guilabel"} field
is used to either link this opportunity to an existing customer, or to
create a new customer.
:::

### Manually create opportunities

To manually create an opportunity, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}. At the top-left of the page, click
`New`{.interpreted-text role="guilabel"} to create a new opportunity
Kanban card. In the `Organization/Contact`{.interpreted-text
role="guilabel"} field, enter the name of the company the opportunity is
for.

Choose a name, and enter it in the `Opportunity`{.interpreted-text
role="guilabel"} field. *This is a required field.* When manually
creating an opportunity, it is helpful to add a name that relates to the
details of the opportunity.

::: {.example}
In the example below, the opportunity is named [5 VP
Chairs]{.title-ref}. This identifies the product the customer is
interested in, as well as the potential number of products.

{.align-center}
:::

Enter the contact information for the opportunity in the
`Email`{.interpreted-text role="guilabel"} and `Phone`{.interpreted-text
role="guilabel"} fields.

In the `Expected Revenue`{.interpreted-text role="guilabel"} field,
enter an estimated value for the opportunity.

::: {.note}
::: {.title}
Note
:::

The information in the `Expected Revenue`{.interpreted-text
role="guilabel"} and priority fields can be used to track performance
for individual salespeople, and on a team basis. See
`../performance/expected_revenue_report`{.interpreted-text role="doc"}
and `../track_leads/lead_scoring`{.interpreted-text role="doc"} for more
information.
:::

Then, use the `fa-star-o`{.interpreted-text role="icon"}
`(star)`{.interpreted-text role="guilabel"} icons to assign a priority.

-   `fa-star-o`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}: low priority
-   `fa-star`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}: medium priority
-   `fa-star`{.interpreted-text role="icon"} `fa-star`{.interpreted-text
    role="icon"} `fa-star-o`{.interpreted-text role="icon"}: high
    priority
-   `fa-star`{.interpreted-text role="icon"} `fa-star`{.interpreted-text
    role="icon"} `fa-star`{.interpreted-text role="icon"}: very high
    priority

::: {.note}
::: {.title}
Note
:::

Assigning a priority changes the order of leads in Kanban view, with
higher priority leads displayed first.
:::

Once all the necessary information has been entered, click
`Add`{.interpreted-text role="guilabel"}.

{.align-center}
