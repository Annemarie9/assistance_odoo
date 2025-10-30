# File: /content/odoo_doc17.0/fr/content/applications/general/companies/digest_emails.md

Digest emails
=============

*Digest Emails* are periodic snapshots sent via email to users in an
organization that include high-level information about how the business
is performing.

To start sending digest emails, begin by navigating to
`Settings app --> Statistics
section`{.interpreted-text role="menuselection"}, activate the
`Digest Emails`{.interpreted-text role="guilabel"} feature, and click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

A variety of settings can be configured for digest emails, such as:

-   Deciding which `KPIs (key performance indicators)`{.interpreted-text
    role="abbr"} are shared in the digest emails
-   Determining how often digest emails are sent
-   Choosing who in the organization receives digest emails
-   Creating custom digest email templates
-   Adding additional
    `KPIs (key performance indicators)`{.interpreted-text role="abbr"}
    (*Studio* app required)

::: {.note}
::: {.title}
Note
:::

By default, the `Digest Email`{.interpreted-text role="guilabel"}
feature is enabled. `Your Odoo Periodic
Digest`{.interpreted-text role="guilabel"} serves as the primary
template, which includes all `KPI (key performance
indicator)`{.interpreted-text role="abbr"} measurements across the Odoo
database, and is sent daily to administrators.
:::

::: {.warning}
::: {.title}
Warning
:::

When creating duplicates of databases that have sending capabilities
(not testing-mode), the digest emails continue to send from the
duplicate database, unless deactivated.

To deactivate the digest email, navigate to
`Settings --> Statistics section`{.interpreted-text
role="menuselection"}. Then, deactivate the
`Digest Emails`{.interpreted-text role="guilabel"} feature, by
un-ticking the checkbox, and clicking `Save`{.interpreted-text
role="guilabel"}. See the section on
`digest-emails/deactivate`{.interpreted-text role="ref"}.
:::

Customize default digest email {#digest-emails/customize-digest}
------------------------------

To customize the default digest email (*Your Odoo Periodic Digest*), go
to `Settings
app --> Statistics section --> Digest Email field`{.interpreted-text
role="menuselection"}. Then, select `Your Odoo Periodic
Digest`{.interpreted-text role="guilabel"}, and click on the
`↗️ (External link)`{.interpreted-text role="guilabel"} icon, next to
the drop-down menu selection.

A pop-up window appears, and presents a variety of editable settings,
which include:

-   `Digest Name`{.interpreted-text role="guilabel"}: the name of the
    digest email.
-   `Periodicity`{.interpreted-text role="guilabel"}: control how often
    digest emails are sent (`Daily`{.interpreted-text role="guilabel"},
    `Weekly`{.interpreted-text role="guilabel"},
    `Monthly`{.interpreted-text role="guilabel"}, or
    `Quarterly`{.interpreted-text role="guilabel"}).
-   `Next Send Date`{.interpreted-text role="guilabel"}: the date on
    which the digest email will be sent again.
-   `KPIs`{.interpreted-text role="guilabel"} tab: check/uncheck each
    calculated `KPI (key performance indicator)`{.interpreted-text
    role="abbr"} that appears in digest emails. A ticked box indicates
    an active `KPI (key performance indicator)`{.interpreted-text
    role="abbr"} in the digest email. See the section on
    `digest-emails/kpis`{.interpreted-text role="ref"}.
-   `Recipients`{.interpreted-text role="guilabel"} tab: add/remove
    users who receive the digest emails. See the section on
    `digest-emails/recipients`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

The `KPIs (key performance indicators)`{.interpreted-text role="abbr"}
can be customized using Odoo *Studio*. Additional costs to the database
subscription are incurred should *Studio* need to be installed. See this
section on `digest-emails/custom-kpi`{.interpreted-text role="ref"}.
:::

{.align-center}

Deactivate digest email {#digest-emails/deactivate}
-----------------------

To manually deactivate an individual digest email, first navigate to
`Settings app
--> Statistics section`{.interpreted-text role="menuselection"}, and
click `Configure Digest Emails`{.interpreted-text role="guilabel"}.
Then, select the desired digest email from the list that should be
deactivated.

Next, click `DEACTIVATE FOR EVERYONE`{.interpreted-text role="guilabel"}
to deactivate the digest email for everyone, or
`UNSUBSCRIBE ME`{.interpreted-text role="guilabel"} to remove the logged
in user from the mailing list. These buttons are located in the top
menu, just above the `Digest Name`{.interpreted-text role="guilabel"}.

Manually send digest email
--------------------------

To manually send a digest email, first navigate to
`Settings app --> Statistics
section`{.interpreted-text role="menuselection"}, and click
`Configure Digest Emails`{.interpreted-text role="guilabel"}. Then,
select the desired digest email, and click `SEND NOW`{.interpreted-text
role="guilabel"}. This button is located in the top menu, just above the
`Digest
Name`{.interpreted-text role="guilabel"}.

KPIs {#digest-emails/kpis}
----

Pre-configured `KPIs (key performance indicators)`{.interpreted-text
role="abbr"} can be added to the digest email from the
`KPIs`{.interpreted-text role="guilabel"} tab of the digest email
template form.

First, navigate to
`Settings app --> Statistics section`{.interpreted-text
role="menuselection"}, and click
`Configure Digest Emails`{.interpreted-text role="guilabel"}.

Then, select the desired digest email, and open the
`KPIs`{.interpreted-text role="guilabel"} tab.

To add a `KPI (key performance indicator)`{.interpreted-text
role="abbr"} to the digest email, tick the checkbox next to the desired
`KPI (key performance indicator)`{.interpreted-text role="abbr"}. After
all `KPIs (key performance indicators)`{.interpreted-text role="abbr"}
are added (or deselected), click `Save`{.interpreted-text
role="guilabel"}.

The following `KPIs (key performance indicators)`{.interpreted-text
role="abbr"} are available in the `KPIs`{.interpreted-text
role="guilabel"} tab on a digest email template form out-of-box in Odoo:

{.align-right}

`General`{.interpreted-text role="guilabel"}

:   -   `Connected Users`{.interpreted-text role="guilabel"}
    -   `Messages`{.interpreted-text role="guilabel"}

`Project`{.interpreted-text role="guilabel"}

:   -   `Open Tasks`{.interpreted-text role="guilabel"}

`Recruitment`{.interpreted-text role="guilabel"}

:   -   `Employees`{.interpreted-text role="guilabel"}

`CRM`{.interpreted-text role="guilabel"}

:   -   `New Leads/Opportunities`{.interpreted-text role="guilabel"}
    -   `Opportunities Won`{.interpreted-text role="guilabel"}

`Sales`{.interpreted-text role="guilabel"}

:   -   `All Sales`{.interpreted-text role="guilabel"}
    -   `eCommerce Sales`{.interpreted-text role="guilabel"}

`Point of Sale`{.interpreted-text role="guilabel"}

:   -   `POS Sales`{.interpreted-text role="guilabel"}

`Live Chat`{.interpreted-text role="guilabel"}

:   -   `% of Happiness`{.interpreted-text role="guilabel"}
    -   `Conversations handled`{.interpreted-text role="guilabel"}
    -   `Time to answer (sec)`{.interpreted-text role="guilabel"}

`Helpdesk`{.interpreted-text role="guilabel"}

:   -   `Tickets Closed`{.interpreted-text role="guilabel"}

`Invoicing`{.interpreted-text role="guilabel"}

:   -   `Revenue`{.interpreted-text role="guilabel"}
    -   `Banks and Cash Moves`{.interpreted-text role="guilabel"}

Recipients {#digest-emails/recipients}
----------

Digest email recipients are added from the
`Recipients`{.interpreted-text role="guilabel"} tab of the digest email
template form.

To add a recipient, navigate to
`Settings app --> Statistics section`{.interpreted-text
role="menuselection"}, and click
`Configure Digest Emails`{.interpreted-text role="guilabel"}. Then,
select the desired digest email, and open the
`Recipients`{.interpreted-text role="guilabel"} tab.

To add a recipient, click `Add a line`{.interpreted-text
role="guilabel"}, and an `Add Recipients`{.interpreted-text
role="guilabel"} pop-up window appears, with all available users to add
as recipients.

From the pop-up window, tick the checkbox next to the
`Name`{.interpreted-text role="guilabel"} of the user(s), and click the
`Select`{.interpreted-text role="guilabel"} button.

To remove a user as a recipient, click the
`❌ (remove)`{.interpreted-text role="guilabel"} icon to the far-right of
the user listed in the `Recipients`{.interpreted-text role="guilabel"}
tab.

Click `Save`{.interpreted-text role="guilabel"} to implement the
changes.

Create digest emails {#digest-emails/custom-emails}
--------------------

To create a new digest email, navigate to
`Settings app --> Statistics section`{.interpreted-text
role="menuselection"}, and click
`Configure Digest Emails`{.interpreted-text role="guilabel"}. Then,
click `Create`{.interpreted-text role="guilabel"} to create a new digest
email.

A separate page, with a blank digest email template appears, and
presents a variety of editable settings, including:

-   `Digest Name`{.interpreted-text role="guilabel"}: the name of the
    digest email.
-   `Periodicity`{.interpreted-text role="guilabel"}: control how often
    digest emails are sent (`Daily`{.interpreted-text role="guilabel"},
    `Weekly`{.interpreted-text role="guilabel"},
    `Monthly`{.interpreted-text role="guilabel"}, or
    `Quarterly`{.interpreted-text role="guilabel"}).
-   `Next Send Date`{.interpreted-text role="guilabel"}: the date on
    which the digest email will be sent again.
-   `KPIs`{.interpreted-text role="guilabel"} tab: check/uncheck each
    calculated `KPI (key performance indicator)`{.interpreted-text
    role="abbr"} that appears in digest emails. A ticked box indicates
    an active `KPI (key performance indicator)`{.interpreted-text
    role="abbr"} in the digest email. See the section on
    `digest-emails/kpis`{.interpreted-text role="ref"}.
-   `Recipients`{.interpreted-text role="guilabel"} tab: add/remove
    users who receive the digest emails. See the section on
    `digest-emails/recipients`{.interpreted-text role="ref"}.

From there, give the digest email a `Digest Name`{.interpreted-text
role="guilabel"}, specify `Periodicity`{.interpreted-text
role="guilabel"}, choose the desired
`KPIs (key performance indicators)`{.interpreted-text role="abbr"}, and
add `Recipients`{.interpreted-text role="guilabel"}, as needed.

After clicking `Save`{.interpreted-text role="guilabel"}, the new custom
digest email is available as a selection in the
`Digest Email`{.interpreted-text role="guilabel"} field, located in the
`Settings app --> Statistics section`{.interpreted-text
role="menuselection"}.

Custom KPIs with Odoo Studio {#digest-emails/custom-kpi}
----------------------------

The `KPIs (key performance indicators)`{.interpreted-text role="abbr"}
on a digest email template form, in the `KPIs`{.interpreted-text
role="guilabel"} tab, can be customized using Odoo *Studio*.

::: {.warning}
::: {.title}
Warning
:::

Additional costs to the database subscription are incurred, should Odoo
*Studio* need to be installed.
:::

To begin, click the `🛠️ (tools)`{.interpreted-text role="guilabel"} icon
in the top-right of the screen. This is the link to the Odoo *Studio*
application.

In order to create additional fields, create two fields on the digest
object:

1.  Create a boolean field called [kpi\_myfield]{.title-ref}, and
    display it in the `KPIs`{.interpreted-text role="guilabel"} tab.
2.  Create a computed field called [kpi\_myfield\_value]{.title-ref}
    that computes the customized `KPI (key
    performance indicator)`{.interpreted-text role="abbr"}.
3.  Select the `KPIs (key performance indicators)`{.interpreted-text
    role="abbr"} in the `KPIs`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

Here is the [source
code](https://github.com/odoo/odoo/blob/15.0/addons/digest/models/digest.py)
for the [digest.py]{.title-ref} file, which guides the programmer in the
coding of the computed field.
:::

::: {.seealso}
Users can also click the `Recipients`{.interpreted-text role="guilabel"}
tab, and then the vertical three-dot `(kebab)`{.interpreted-text
role="guilabel"} menu to edit this view. Either click
`EDIT LIST VIEW`{.interpreted-text role="guilabel"} or
`EDIT FORM VIEW`{.interpreted-text role="guilabel"} to modify this tab.
:::

### Computed values reference table

  ------------------------------------------------------------------------------------
  LABEL                   VALUE
  ----------------------- ------------------------------------------------------------
  Connected Users         [kpi\_res\_users\_connected\_value]{.title-ref}

  Messages Sent           [kpi\_mail\_message\_total\_value]{.title-ref}

  New Leads               [kpi\_crm\_lead\_created\_value]{.title-ref}

  Opportunities Won       [kpi\_crm\_opportunities\_won\_value]{.title-ref}

  Open Tasks              [kpi\_project\_task\_opened\_value]{.title-ref}

  Tickets Closed          [kpi\_helpdesk\_tickets\_closed\_value]{.title-ref}

  \% of Happiness         [kpi\_livechat\_rating\_value]{.title-ref}

  Conversations handled   [kpi\_livechat\_conversations\_value]{.title-ref}

  Time to answer (sec)    [kpi\_livechat\_response\_value]{.title-ref}

  All Sales               [kpi\_all\_sale\_total\_value]{.title-ref}

  eCommerce Sales         [kpi\_website\_sale\_total\_value]{.title-ref}

  Revenue                 [kpi\_account\_total\_revenue\_value]{.title-ref}

  Bank & Cash Moves       [kpi\_account\_bank\_cash\_value]{.title-ref}

  POS Sales               [kpi\_pos\_total\_value]{.title-ref}

  New Employees           [kpi\_hr\_recruitment\_new\_colleagues\_value]{.title-ref}
  ------------------------------------------------------------------------------------
