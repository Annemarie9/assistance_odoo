# File: /content/odoo_doc17.0/fr/content/applications/marketing/email_marketing/lost_leads_email.md

Lost leads reactivation email
=============================

In Odoo, lost leads are removed from the active *CRM* pipeline, but can
still be targeted with the *Email Marketing* application for strategic
campaign purposes, such as lost leads reactivation.

A lost leads reactivation email looks at the leads that were lost during
a specific period of time, and uses custom filters and lost reasons to
exclude undesirable leads from the mailing list.

Once a lost leads reactivation email is complete, it can be sent as is,
modified and sent to different groups for A/B testing, or saved as a
template for later.

::: {.example}
A warehouse has leftover merchandise from a limited run of items from
last year. To help clear out the excess inventory, the warehouse manager
creates a lost leads email to reach out to old opportunities that were
lost, and inform them that the limited merchandise is back in stock.

The warehouse manager uses the following filters for a lost leads email:

-   `Blacklist`{.interpreted-text role="guilabel"} *is* [not
    set]{.title-ref}
-   `Created on`{.interpreted-text role="guilabel"} *\>=* [01/01/2024
    00:00:01]{.title-ref}
-   `Stage`{.interpreted-text role="guilabel"} *is not in*
    [New]{.title-ref}, [Qualified]{.title-ref}, or [Won]{.title-ref}
-   `Lost Reason`{.interpreted-text role="guilabel"} *is in* [Not enough
    stock]{.title-ref}
-   and either `Active`{.interpreted-text role="guilabel"} *is*
    [set]{.title-ref} or [not set]{.title-ref}

{.align-center}
:::

::: {.tip}
::: {.title}
Tip
:::

As filters are added and removed, pay attention to the
`# record(s)`{.interpreted-text role="guilabel"} value below the
filtering section. This value indicates the total number of records that
match the current criteria.

To view a list of all matching records, click the
`# record(s)`{.interpreted-text role="guilabel"} text.

{.align-center}
:::

Minimum requirements
--------------------

In order to create and deliver a lost leads reactivation email campaign,
the *CRM* and *Email Marketing* applications **must** be
`installed <general/install>`{.interpreted-text role="ref"} and
configured.

Here are the minimum necessary filters that pertain to a lost leads
reactivation mailing campaign:

-   The
    `Recipients <email_marketing/recipients_field>`{.interpreted-text
    role="ref"} field **must** be set to the *Lead/Opportunity* model.
-   A `Blacklist <email_marketing/blacklist_filter>`{.interpreted-text
    role="ref"} filter to exclude unsubscribed recipients.
-   A `Created on <email_marketing/created_on_filter>`{.interpreted-text
    role="ref"} to target leads that were lost during a specific period
    of time.
-   `Stage <email_marketing/stage_filter>`{.interpreted-text role="ref"}
    filter(s) to exclude leads that were already won, or are still
    active in new stages of the sales pipeline (i.e. *New*, *Qualified*,
    etc.). These values will be different per organization; however,
    it\'s minimally viable to exclude all the leads in the *Won* stage.
-   One or more
    `Lost Reason <email_marketing/lost_reason_filter>`{.interpreted-text
    role="ref"} filters to exclude undesired leads, such as duplicate,
    spam, or irrelevant records.
-   A pair of `Active <email_marketing/active_filter>`{.interpreted-text
    role="ref"} filters to target *both* active and inactive leads.

Add the necessary filters
-------------------------

First, navigate to the `Email Marketing`{.interpreted-text
role="menuselection"} app, and on the `Mailings`{.interpreted-text
role="guilabel"} page, click the `New`{.interpreted-text
role="guilabel"} button in the top-left corner.

::: {#email_marketing/recipients_field}
On the new `Mailings`{.interpreted-text role="guilabel"} form, enter an
appropriate `Subject`{.interpreted-text role="guilabel"} line for the
email in the corresponding field. Then, in the
`Recipients`{.interpreted-text role="guilabel"} field, choose the
`Lead/Opportunity`{.interpreted-text role="guilabel"} model from the
drop-down menu.
:::

::: {#email_marketing/blacklist_filter}
In the rules section, located beneath the `Recipients`{.interpreted-text
role="guilabel"} field, click the modify filter
(`▶ (triangle pointing right)`{.interpreted-text role="guilabel"}) icon
to expand the filter rules. Leave the default
`Blacklist`{.interpreted-text role="guilabel"} rule in place.
:::

### Created on {#email_marketing/created_on_filter}

Begin by clicking `New Rule`{.interpreted-text role="guilabel"} beneath
the default `Blacklist`{.interpreted-text role="guilabel"} rule. Then,
click the first field of the new rule that appears, and select the
`Created on`{.interpreted-text role="guilabel"} parameter from the
drop-down menu. With that in place, a specific time period during which
the targeted leads were lost can be designated (e.g. 30 days prior, 90
days prior, previous year, etc.).

Then, in the second field, select
`<= (less than or equal to)`{.interpreted-text role="guilabel"},
`>= (greater
than or equal to)`{.interpreted-text role="guilabel"}, or
`is between`{.interpreted-text role="guilabel"} as a date operator, in
order to frame the time selection chosen in the third field.

In the third field, use the calendar popover window to select dates, and
click `Apply`{.interpreted-text role="guilabel"} to lock in the time
range.

{.align-center}

::: {.important}
::: {.title}
Important
:::

When there is more than one rule applied, make sure the statement at the
top of the `Recipients`{.interpreted-text role="guilabel"} filter list
reads: `Match all of the following rules`{.interpreted-text
role="guilabel"}. If it does not, click on the statement, and select
`all`{.interpreted-text role="guilabel"} from the drop-down menu (as
opposed to `any`{.interpreted-text role="guilabel"}).

{.align-center}
:::

### Stage {#email_marketing/stage_filter}

Now, add the `Stage`{.interpreted-text role="guilabel"} filter to
exclude leads that are in the *New*, *Qualified*, and *Won* stages of
the sales pipeline.

::: {.note}
::: {.title}
Note
:::

This step assumes that the *New*, *Qualified*, and *Won* stages exist in
the CRM pipeline; however, stage names may differ from business to
business. Refer to the database\'s actual stage names in the *CRM*
app\'s pipeline to complete this step, accordingly.
:::

Begin again by clicking `New Rule`{.interpreted-text role="guilabel"}
and select `Stage`{.interpreted-text role="guilabel"} from the first
field\'s drop-down menu. In the second field, select the
`is not in`{.interpreted-text role="guilabel"} operator, and in the
third field, select the `New`{.interpreted-text role="guilabel"},
`Qualified`{.interpreted-text role="guilabel"} and
`Won`{.interpreted-text role="guilabel"} stages to define the rule\'s
parameters.

When the rule is added in this way, the logic in the third field renders
as `OR` ([\|]{.title-ref}) statements.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Another way to add *Stage* rules, is to do so on a one-rule-per-row
basis using the `contains`{.interpreted-text role="guilabel"} or
`does not contain`{.interpreted-text role="guilabel"} operators, and
manually typing out the defining characters in each stage name. This
method, however, only allows for one selection at a time, which can be
useful for quickly turning on/off filters in the
`Search...`{.interpreted-text role="guilabel"} bar.

{.align-center}
:::

### Lost Reason {#email_marketing/lost_reason_filter}

Next, add one or more `Lost Reason`{.interpreted-text role="guilabel"}
rules to exclude leads that should **not** be targeted for specific
`lost reasons <../../sales/crm/pipeline/lost_opportunities>`{.interpreted-text
role="doc"}.

To do that, create another `New Rule`{.interpreted-text
role="guilabel"}, once again. Then, in the rule\'s first field, select
`Lost Reason`{.interpreted-text role="guilabel"} from the drop-down
menu. For the operator, choose either `is not
in`{.interpreted-text role="guilabel"} or
`does not contain`{.interpreted-text role="guilabel"} from the drop-down
menu. With either selection, use the third field to enter a lost reason
(or multiple lost reasons, depending on your operator choice) to include
in the rule.

If choosing the `does not contain`{.interpreted-text role="guilabel"}
operator, then repeat the preceding steps to add more lost reasons, as
needed, where each lost reason occupies one rule row at a time.

For more information, refer to the section below outlining how to
`select appropriate lost
reasons <email_marketing/select_lost_reasons>`{.interpreted-text
role="ref"}.

{.align-center}

### Active {#email_marketing/active_filter}

Finally, add a pair of `Active`{.interpreted-text role="guilabel"}
filters to include both active and inactive leads for the campaign.

::: {.important}
::: {.title}
Important
:::

Adding both active *and* inactive lead records is necessary to capture
the full scope of lost leads in the database. Doing one without the
other greatly impacts the number of targetable records for the email
campaign, and does **not** include a complete or accurate lost leads
audience.
:::

First, click the `(Add Branch)`{.interpreted-text role="guilabel"} icon
on the most recently created rule (e.g. `Lost Reason`{.interpreted-text
role="guilabel"}), which is the middle of three icons located to the
right of the rule row. Doing so adds a pair of
`any of`{.interpreted-text role="guilabel"} rules. Then, in the top
rule\'s first field of the newly-created branch, select the
`Active`{.interpreted-text role="guilabel"} parameter from the drop-down
menu. The rule then automatically fills out to read:
`Active`{.interpreted-text role="guilabel"} *is* [set]{.title-ref}.

For the first field of the bottom rule of the branch, select
`Active`{.interpreted-text role="guilabel"} from the drop-down menu
again. However, this time, select `is not`{.interpreted-text
role="guilabel"} from the operator drop-down menu in the second field.
The rule should then read: `Active`{.interpreted-text role="guilabel"}
*is not* [set]{.title-ref}.

{.align-center}

Add body content
----------------

Now, with the domain section of the email campaign complete, create the
body content of the email using any of the premade stylized templates,
or choose between the `Plain Text`{.interpreted-text role="guilabel"} or
`Start From Scratch`{.interpreted-text role="guilabel"} options for more
granular control. For more information, refer to the *Email Marketing*
`documentation on how to create an email <email_marketing/create_email>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To save the set of filters for later use, click
`Save as Favorite Filter 💾 (floppy
disk)`{.interpreted-text role="guilabel"}, enter a name (such as [Lost
Leads]{.title-ref}), and click `Add`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Send or schedule
----------------

Once all the components of the email campaign are complete, either:

-   click the purple `Send`{.interpreted-text role="guilabel"} button at
    the top-left of the form to immediately send the email; or
-   click the gray `Schedule`{.interpreted-text role="guilabel"} button,
    located to the right of the `Send`{.interpreted-text
    role="guilabel"} button, to send the email at a future date and
    time.

::: {.tip}
::: {.title}
Tip
:::

Consider using *A/B Testing* to send an alternate version of the email
to a percentage of the target leads. This can help determine what
subject lines and body content produce the best click-through rates,
before sending a final version to the remaining leads.

To do so, open the `A/B Tests`{.interpreted-text role="guilabel"} tab on
the mailing form and check the box next to
`Allow A/B Testing`{.interpreted-text role="guilabel"}. Then, adjust the
parameters as needed, and click `Create
an Alternative Version`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Select appropriate lost reasons {#email_marketing/select_lost_reasons}
-------------------------------

When a lead is marked as lost, Odoo recommends selecting a *Lost Reason*
to indicate why the opportunity did not result in a sale. Doing so keeps
the pipeline organized and reporting data accurate, and generates
potential to follow up with the lead in the future.

If an existing *Lost Reason* is not applicable, users with the necessary
permissions can create new ones, which means the lost reasons in a
database can vary from organization to organization, and from pipeline
to pipeline.

For more information on *Lost Reasons*, including the creation of them,
refer to `../../sales/crm/pipeline/lost_opportunities`{.interpreted-text
role="doc"}.

By default, Odoo includes a few common *Lost Reasons*, such as:

-   *Too expensive*
-   *We don\'t have people/skills*
-   *Not enough stock*

When determining which reasons to include in a lost leads reactivation
email, consider what the email is advertising, in order pinpoint one or
more relevant lost reasons. Then, add a rule stating,
`Lost Reason`{.interpreted-text role="guilabel"} *does not contain*
[\_\_\_\_\_]{.title-ref} for every reason in the database, **except**
for the relevant one(s).

::: {.example}
If the email advertises a selection of previously-limited merchandise
that is now back in stock, it makes sense to target leads with the lost
reason: *not enough stock*.

{.align-center}

If the email advertises a price reduction, it makes sense to target
leads with the lost reason: *too expensive*.

{.align-center}
:::

Analyze the results
-------------------

After sending a lost leads reactivation email, marketing teams can use
the smart buttons along the top of the email to analyze the results, and
determine follow-up actions.

Clicking on any of the smart buttons opens a list of records matching
that button\'s specific criteria.

{.align-center}

The smart buttons include:

-   `Sent`{.interpreted-text role="guilabel"}: total number of emails
    sent.
-   `Opened`{.interpreted-text role="guilabel"}: percentage of
    recipients that opened the email.
-   `Replied`{.interpreted-text role="guilabel"}: percentage of
    recipients that replied to the email.
-   `Clicked`{.interpreted-text role="guilabel"}: click-through rate (%)
    of recipients that clicked on a link in the email.
-   `Leads/Opportunities`{.interpreted-text role="guilabel"}: number of
    leads (or opportunities) that have been created in the *CRM*
    pipeline, as a result of the email campaign.
-   `Quotations`{.interpreted-text role="guilabel"}: number of
    quotations that have been created in the *Sales* application, as a
    result of the email.
-   `Invoiced`{.interpreted-text role="guilabel"}: total revenues
    generated, as a result of the email campaign, via invoices sent to,
    and paid by, customers. These values are recorded in either the
    *Invoicing* or *Accounting* application, depending on which app is
    installed in the database.
-   `Received`{.interpreted-text role="guilabel"}: percentage of
    recipients that received the email.
-   `Bounced`{.interpreted-text role="guilabel"}: percentage of emails
    that bounced (`not delivered`{.interpreted-text role="dfn"}).
-   `Ignored`{.interpreted-text role="guilabel"}: the number of
    recipients that received the email, but have not interacted with it
    in a meaningful way (i.e. opened, clicked, etc.).

Email nurturing
---------------

*Email nurturing* (sometimes referred to as *lead nurturing*) is the
process of sending a series of timely and relevant \"nudge\" emails to
connect with a lead, build a deeper relationship, and ultimately convert
the lead into a sale.

The point of nurturing is to keep the email campaign \"visible\" or at
the top of a lead\'s inbox, until they are ready to buy.

There are many approaches to effective lead nurturing, but they often
involve:

-   Sending an initial email (such as, a lost leads reactivation email).
-   Sending a follow-up email each week (or according to specific
    triggers) for the duration of the campaign.
-   Continuously analyzing results to learn what approaches have
    resulted in sales.
-   Continuously adjusting the approach to remain \"visible\" at the top
    of the lead\'s inbox, and hopefully, get a meaningful response from
    the lead.

As a campaign progresses, a marketing team may send different follow-up
emails depending on how a lead responded the previous week.

::: {.example}
A marketing team wants to advertise a restocking of limited-run
merchandise to all leads with a lost reason of *not enough stock*. They
develop the following three-week long lead nurturing campaign.

-   **Week 1:** the marketing team sends an initial email, with the
    subject line: *"Limited run merchandise is back in stock! Act now!"*
-   **Week 2:** the marketing team sends two different emails, depending
    on how a lead responded.
    -   If a lead ignored the Week 1 email: *"Stock is almost out, did
        you get yours?"*
    -   If a lead clicked on the Week 1 email: *\"You still have time to
        add this to your collection\"*
-   **Week 3:** the marketing team sends a final email to all leads who
    have not been converted stating: *"20% off, don\'t miss your last
    chance to get these items before they\'re gone!"*

Throughout the campaign, the marketing team continuously refers to the
smart buttons along the top of the mailing page to see what percentages
of leads are opening, clicking on, or ignoring the emails. They also
regularly analyze reports on how many opportunities, quotations, and
invoices have been generated by the campaign.
:::

::: {.seealso}
\- `../email_marketing`{.interpreted-text role="doc"} -
`unsubscriptions`{.interpreted-text role="doc"} -
`../marketing_automation`{.interpreted-text role="doc"}
:::
