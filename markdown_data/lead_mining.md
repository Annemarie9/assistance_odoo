Lead mining
===========

*Lead mining* is a feature that allows *CRM* users to generate new leads
directly into their Odoo database. To ensure lead qualification, lead
mining output is determined by a variety of filtering criteria, such as
the country, the company size, and the industry.

Configuration
-------------

To get started, go to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the `Lead Mining`{.interpreted-text
role="guilabel"} checkbox to activate the feature. Then, click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Generate leads
--------------

After the *Lead Mining* setting is activated, a new button called
*Generate Leads* is available to use in the upper-left corner of the
*CRM* *Pipeline* (`CRM app --> Sales --> My
Pipeline`{.interpreted-text role="menuselection"}).

Lead mining requests are also available through
`CRM app --> Configuration --> Lead
Mining Requests`{.interpreted-text role="menuselection"}, or through
`CRM app --> Leads --> Leads`{.interpreted-text role="menuselection"},
where the `Generate Leads`{.interpreted-text role="guilabel"} button is
also available.

{.align-center}

Click the `Generate Leads`{.interpreted-text role="guilabel"} button,
and a pop-up window appears, offering a variety of criteria by which to
generate leads.

{.align-center}

Choose to generate leads for `Companies`{.interpreted-text
role="guilabel"} to get company information only, or choose
`Companies and their Contacts`{.interpreted-text role="guilabel"} to get
company information and individual employee contact information.

::: {.note}
::: {.title}
Note
:::

When targeting `Companies and their Contacts`{.interpreted-text
role="guilabel"}, additional options are available to filter contacts
based on `Role`{.interpreted-text role="guilabel"} or
`Seniority`{.interpreted-text role="guilabel"}.
:::

Additional filtering options include the following:

-   `Countries`{.interpreted-text role="guilabel"}: filter leads based
    on the country (or countries) they are located in.
-   `States`{.interpreted-text role="guilabel"}: further filter leads
    based on the state in which they are located, if applicable.
-   `Industries`{.interpreted-text role="guilabel"}: filter leads based
    on the specific industry they work in.
-   `Filter on Size`{.interpreted-text role="guilabel"}: tick this
    checkbox to specify the number of employees at the company. This
    generates a field labeled `Size`{.interpreted-text role="guilabel"}.
    Fill in the blanks to create a range for the desired company size.
-   `Sales Team`{.interpreted-text role="guilabel"}: choose which Sales
    Team the leads will be assigned to.
-   `Salesperson`{.interpreted-text role="guilabel"}: choose which
    member of the Sales Team the leads will be assigned to.
-   `Default Tags`{.interpreted-text role="guilabel"}: choose which tags
    are applied directly to the leads once found.

::: {.important}
::: {.title}
Important
:::

Make sure to be aware of the latest EU regulations when receiving
contact information. Get more information about the General Data
Protection Regulation on .
:::

### View leads

After leads are generated, they are assigned to the designated
salesperson and team. To view additional information regarding the lead,
select one from the list, and click to open it.

In the chatter thread for the lead, additional information is provided.
This can include the number of employees, the technology used by the
company, the timezone, and direct contact information.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If `Leads`{.interpreted-text role="guilabel"} are **not** enabled for
the database, then leads are generated as *opportunities*, and added to
the pipeline for the designated salesperson.

To enable the `Leads`{.interpreted-text role="guilabel"} feature,
navigate to `CRM app --> Configuration
--> Settings`{.interpreted-text role="menuselection"}, and tick the
`Leads`{.interpreted-text role="guilabel"} checkbox. Then, click
`Save`{.interpreted-text role="guilabel"}.
:::

Pricing
-------

Lead mining is an *In-App Purchase* feature, and each generated lead
costs one `credit
<in_app_purchase/credits>`{.interpreted-text role="ref"}.

::: {.important}
::: {.title}
Important
:::

Generating `Companies and their Contacts`{.interpreted-text
role="guilabel"} costs one additional credit for each contact generated.
See here for complete pricing information: [Lead Generation by Odoo
IAP](https://iap.odoo.com/iap/in-app-services/167?).
:::

To buy credits, navigate to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Lead Generation`{.interpreted-text
role="guilabel"} section, under the `Lead Mining`{.interpreted-text
role="guilabel"} feature, click `Buy
Credits`{.interpreted-text role="guilabel"}.

Credits may also be purchased by navigating to the
`Settings app`{.interpreted-text role="menuselection"}. In the
`Contacts`{.interpreted-text role="guilabel"} section, under the
`Odoo IAP`{.interpreted-text role="guilabel"} feature, click `View My
Services`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Enterprise Odoo users with a valid subscription get free credits to test
`IAP (In-App Purchase)`{.interpreted-text role="abbr"} features before
purchasing more credits for the database. This includes demo/training
databases, educational databases, and one-app-free databases.
:::

::: {.seealso}
`/applications/essentials/in_app_purchase`{.interpreted-text role="doc"}
:::
