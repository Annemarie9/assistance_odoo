Enrich contacts with partner autocomplete
=========================================

*Partner autocomplete* enriches the contacts database with corporate
data. In any module, enter the new company name into the
`Customer`{.interpreted-text role="guilabel"} field
([partner\_id]{.title-ref} technical field), and select one of the
companies suggested in the drop-down menu. Instantly get valuable
company information full of hard-to-find data for a desired company.

::: {.important}
::: {.title}
Important
:::

A company **cannot** already be manually entered in the *Contacts*
application prior to enriching it with data.
:::

The information provided by partner autocomplete can include general
information about the business (including full business name and logo),
`Phone`{.interpreted-text role="guilabel"} number,
`Email`{.interpreted-text role="guilabel"}, `Tax ID`{.interpreted-text
role="guilabel"}, address and UNSPSC activities as
`Tags`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

When getting a company\'s contact information make sure to be aware of
the latest EU regulations. For more information about General Data
Protection Regulation refer to: . In
Odoo, individual contact information cannot be searched for with the
partner autocomplete feature.
:::

Configuration
-------------

Go to `Settings app --> Contacts section`{.interpreted-text
role="menuselection"}. Then, activate the `Partner
Autocomplete`{.interpreted-text role="guilabel"} feature, by ticking the
checkbox beside it, and clicking `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

Enrich contacts with corporate data
-----------------------------------

From any module, as the user is typing in the name of a new company
contact, Odoo reveals a large drop-down menu of potential match
suggestions. If any are selected, the contact is then populated with
corporate data related to that specific selection.

For example, after typing [Odoo]{.title-ref}, the following information
populates:

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Partner Autocomplete also works if a
`VAT (value-added tax)`{.interpreted-text role="abbr"} number is entered
instead of company name.
:::

Pricing
-------

*Partner Autocomplete* is an *In-App Purchase (IAP)* service, which
requires prepaid credits to be used. Each request consumes one credit.

To buy credits, go to
`Settings app --> Contacts section`{.interpreted-text
role="menuselection"}. Then, locate either the
`Partner Autocomplete`{.interpreted-text role="guilabel"} feature and
click `Buy credits`{.interpreted-text role="guilabel"}, or locate the
`Odoo IAP`{.interpreted-text role="guilabel"} feature and click
`View My Services`{.interpreted-text role="guilabel"}. From the
resulting page, select a desired package.

::: {.note}
::: {.title}
Note
:::

If the database runs out of credits, the only information populated when
clicking on the suggested company will be the website link and the logo.

Learn about our .
:::

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

::: {.seealso}
`../../../essentials/in_app_purchase`{.interpreted-text role="doc"}
:::
