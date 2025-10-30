Lead enrichment
===============

*Lead enrichment* is a service that provides business information for a
contact attached to a lead. Lead enrichment is an In-App Purchase (IAP)
that requires credits to use, and is available for existing leads in an
Odoo database.

The information provided by lead enrichment can include general
information about the business (including full business name and logo),
social media accounts, `Company type`{.interpreted-text
role="guilabel"}, `Founded`{.interpreted-text role="guilabel"}
information, `Sectors`{.interpreted-text role="guilabel"} information,
the number of `Employees`{.interpreted-text role="guilabel"},
`Estimated revenue`{.interpreted-text role="guilabel"},
`Phone`{.interpreted-text role="guilabel"} number,
`Timezone`{.interpreted-text role="guilabel"}, and
`Technologies Used`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Enterprise Odoo users with a valid subscription get free credits to test
`IAP (In-App
Purchase)`{.interpreted-text role="abbr"} features before deciding to
purchase more credits for the database. This includes demo/training
databases, educational databases, and one-app-free databases.
:::

::: {.important}
::: {.title}
Important
:::

The *leads* feature **must** be activated in the *CRM* settings page in
order to use lead enrichment. To access the *CRM* settings, navigate to
`CRM app --> Configuration
--> Settings`{.interpreted-text role="menuselection"}. Under the
`CRM`{.interpreted-text role="guilabel"} section activate the
`Leads`{.interpreted-text role="guilabel"} option and click
`Save`{.interpreted-text role="guilabel"}.
:::

Lead enrichment set up
----------------------

To set up lead enrichment in the *CRM* application, navigate to
`CRM app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Then, under the `Lead Generation`{.interpreted-text role="guilabel"}
section, tick the checkbox next to `Lead Enrichment`{.interpreted-text
role="guilabel"}, and select either
`Enrich leads on demand only`{.interpreted-text role="guilabel"} or
`Enrich all leads automatically`{.interpreted-text role="guilabel"}.
Click the `Save`{.interpreted-text role="guilabel"} button to activate
the changes.

![CRM lead generation settings page, with lead enrichment activation highlighted, and enrich
leads on demand only chosen.](lead_enrichment/lead-enrichment-activate.png){.align-center}

Enrich leads
------------

Enrichment of leads is based on the domain of the email address of the
customer set on the lead. There are two different ways that a lead can
be enriched: *automatically* or *manually*.

### Automatically enrich leads

During set up, if `Enrich all leads automatically`{.interpreted-text
role="guilabel"} was selected on the *CRM* `Settings`{.interpreted-text
role="guilabel"} page, then no action needs to be taken by the user to
enrich the lead. A scheduled action runs automatically, every sixty
minutes, and enrichment occurs on leads, after a remote database is
contacted.

::: {.tip}
::: {.title}
Tip
:::

To access the cron that runs for the automatic lead enrichment, activate
`developer mode
<developer-mode>`{.interpreted-text role="ref"}, and navigate to
`Settings app --> Technical menu --> Automation
section --> Scheduled Actions`{.interpreted-text role="menuselection"}.
In the `Search...`{.interpreted-text role="guilabel"} bar, type in
[CRM]{.title-ref}. Click into the result labeled
`CRM: enrich leads (IAP)`{.interpreted-text role="guilabel"}, and make
any necessary adjustments. In the `Execute Every`{.interpreted-text
role="guilabel"} field, enter a value greater than, or equal to, five
minutes.
:::

::: {.example}
The following is an example of lead enrichment data that has been
autocompleted successfully:

{.align-center}
:::

### Manually enrich leads

If the `Enrich leads on demand only`{.interpreted-text role="guilabel"}
option was selected on the *CRM* `Settings`{.interpreted-text
role="guilabel"} page, when activating
`Lead Enrichment`{.interpreted-text role="guilabel"}, each lead that a
user wishes to enrich **must** be manually enriched. This is achieved by
clicking the `Enrich`{.interpreted-text role="guilabel"} button in the
top menu of the lead.

The same information will be retrieved at the same
`IAP (In-App Puchase)`{.interpreted-text role="abbr"} credit cost (one
per enrichment). This method of enrichment is useful when every lead
does not need to be enriched, or cost is an issue.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Manually enrich leads in bulk using the *list* view. First, navigate to
`CRM app
--> Leads`{.interpreted-text role="menuselection"}, and click the list
view button (`☰ (three horizontal lines)`{.interpreted-text
role="guilabel"} icon). Next, tick the checkboxes for the leads that
should be manually enriched. Finally, click the
`⚙️ Action`{.interpreted-text role="guilabel"} icon, and select
`Enrich`{.interpreted-text role="guilabel"} from the resulting drop-down
menu. This can also be achieved from the *My Pipeline* page. To do so,
simply open the *CRM* app, or navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}. Either route reveals leads and opportunities on
the `Pipeline`{.interpreted-text role="guilabel"} page.
:::

Pricing
-------

Lead enrichment is an In-App Purchase (IAP) feature, and each enriched
lead costs one credit.

::: {.note}
::: {.title}
Note
:::

See here for full pricing information: [Lead Generation by Odoo
IAP](https://iap.odoo.com/iap/in-app-services/273).
:::

To buy credits, navigate to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Lead Generation`{.interpreted-text
role="guilabel"} section, under the `Lead Enrichment`{.interpreted-text
role="guilabel"} feature, click on `Buy Credits`{.interpreted-text
role="guilabel"}.

{.align-center}

Credits and balances may also be purchased by navigating to the
`Settings app`{.interpreted-text role="menuselection"}. In the
`Contacts`{.interpreted-text role="guilabel"} section, under the
`Odoo IAP`{.interpreted-text role="guilabel"} feature, click on `View
My Services`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
`../../../essentials/in_app_purchase`{.interpreted-text role="doc"}
:::

::: {.important}
::: {.title}
Important
:::

When collecting a company\'s contact information, make sure to be aware
of the latest EU regulations. For more information about General Data
Protection Regulation, refer to: .
:::
