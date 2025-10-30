# File: /content/odoo_doc17.0/fr/content/applications/essentials/in_app_purchase.md

In-app purchases (IAP)
======================

In-app purchases (IAP) are optional services that enhance Odoo
databases. Each service provides its own specific features and
functionality. A full list of services is available on the [Odoo IAP
Catalog](https://iap.odoo.com/iap/all-in-app-services).

{.align-center}

::: {.example}
The `SMS`{.interpreted-text role="guilabel"} service sends text messages
to contacts directly from the database, and the
`Documents Digitization`{.interpreted-text role="guilabel"} service
digitizes scanned or PDF vendor bills, expenses, and resumes with
optical character recognition (OCR) and artificial intelligence (AI).
:::

`IAP (In-app purchases)`{.interpreted-text role="abbr"} services do
**not** need to be configured or set up before use. Odoo users can
simply click on the service in the app to activate it. However, each
service requires its own prepaid credits, and when they run out, users
**must** `buy more <iap/buying_credits>`{.interpreted-text role="ref"}
in order to keep using it.

::: {.note}
::: {.title}
Note
:::

Enterprise Odoo users with a valid subscription get free credits to test
IAP features before deciding to purchase more credits for the database.
This includes demo/training databases, educational databases, and
one-app-free databases.
:::

IAP services {#in_app_purchase/portal}
------------

`IAP (In-app purchases)`{.interpreted-text role="abbr"} services are
provided by Odoo, as well as third-parties, and have a wide range of
uses.

The following `IAP (In-app purchases)`{.interpreted-text role="abbr"}
services are offered by Odoo:

-   `Documents Digitization`{.interpreted-text role="guilabel"}:
    digitizes scanned or PDF vendor bills, expenses, and resumes with
    OCR and AI.
-   `Partner Autocomplete`{.interpreted-text role="guilabel"}:
    automatically populates contact records with corporate data.
-   `SMS`{.interpreted-text role="guilabel"}: sends SMS text messages to
    contacts directly from the database.
-   `Lead Generation`{.interpreted-text role="guilabel"}: generates
    leads based on a set of criteria, and converts web visitors into
    quality leads and opportunities.
-   `Snailmail`{.interpreted-text role="guilabel"}: sends customer
    invoices and follow-up reports by post, worldwide.
-   `Signer identification with itsme®️`{.interpreted-text
    role="guilabel"}: ask document signatories in Odoo *Sign* to provide
    their identity using the *itsme®* identity platform, which is
    available in Belgium and the Netherlands.

For more information on every service currently available (offered from
developers other than Odoo), visit the [Odoo IAP
Catalog](https://iap.odoo.com/iap/all-in-app-services).

### Use IAP services

`IAP (In-app purchases)`{.interpreted-text role="abbr"} services are
automatically integrated with Odoo, and do **not** require users to
configure any settings. To use a service, simply interact with it
wherever it appears in the database.

::: {.example}
The following flow focuses on the *SMS*
`IAP (In-app purchases)`{.interpreted-text role="abbr"} service being
used from a contact\'s record.

This can be done by clicking the `📱 SMS`{.interpreted-text
role="guilabel"} icon within the database.

{.align-center}

One way to utilize the *SMS* `IAP (In-app purchases)`{.interpreted-text
role="abbr"} service with Odoo is showcased in the following steps:

First, navigate to the `Contacts application`{.interpreted-text
role="menuselection"}, and click on a contact with a mobile phone number
entered in either the `Phone`{.interpreted-text role="guilabel"} or
`Mobile`{.interpreted-text role="guilabel"} field of the contact form.

Next, find the `📱 SMS`{.interpreted-text role="guilabel"} icon that
appears to the right of the `Phone`{.interpreted-text role="guilabel"}
or `Mobile`{.interpreted-text role="guilabel"} fields. Click the
`📱 SMS`{.interpreted-text role="guilabel"} icon, and a `Send SMS Text
Message`{.interpreted-text role="guilabel"} pop-up window appears.

Type a message in the `Message`{.interpreted-text role="guilabel"} field
of the pop-up window. Then, click the `Send SMS`{.interpreted-text
role="guilabel"} button. Odoo then sends the message, via SMS, to the
contact, and logs what was sent in the *chatter* of the contact\'s form.

Upon sending the SMS message, the prepaid credits for the *SMS*
`IAP (In-app purchases)`{.interpreted-text role="abbr"} service are
automatically deducted from the existing credits. If there are not
enough credits to send the message, Odoo prompts the user to purchase
more.
:::

::: {.seealso}
For more information on how to use various
`IAP (In-app purchases)`{.interpreted-text role="abbr"} services, and
for more in-depth instructions related to SMS functionality in Odoo,
review the documentation below:

-   `Lead mining <../sales/crm/acquire_leads/lead_mining>`{.interpreted-text
    role="doc"}
-   `Enrich your contacts base with Partner Autocomplete
    <../sales/crm/optimize/partner_autocomplete>`{.interpreted-text
    role="doc"}
-   `SMS Marketing <../marketing/sms_marketing>`{.interpreted-text
    role="doc"}
:::

IAP credits {#in_app_purchase/credits}
-----------

Every time an `IAP (In-app purchases)`{.interpreted-text role="abbr"}
service is used, the prepaid credits for that service are spent. Odoo
prompts the purchase of more credits when there are not enough credits
left to continue using a service. Email alerts can also be set up for
when `credits are low <in_app_purchase/low-credits>`{.interpreted-text
role="ref"}.

Credits are purchased in *Packs* from the [Odoo IAP
Catalog](https://iap.odoo.com/iap/all-in-app-services), and pricing is
specific to each service.

::: {.example}
The  has four
packs available, in denominations of:

-   `Starter Pack`{.interpreted-text role="guilabel"}: 10 credits
-   `Standard Pack`{.interpreted-text role="guilabel"}: 100 credits
-   `Advanced Pack`{.interpreted-text role="guilabel"}: 500 credits
-   `Expert Pack`{.interpreted-text role="guilabel"}: 1,000 credits

{.align-center}

The number of credits consumed depends on the length of the SMS and the
country of destination.

For more information, refer to the `SMS Pricing and FAQ
<../marketing/sms_marketing/pricing_and_faq>`{.interpreted-text
role="doc"} documentation.
:::

### Buy credits {#iap/buying_credits}

If there are not enough credits to perform a task, the database
automatically prompts the purchase of more credits.

Users can check the current balance of credits for each service, and
manually purchase more credits, by navigating to the
`Settings app --> Contacts section`{.interpreted-text
role="menuselection"}, and beneath the `Odoo IAP`{.interpreted-text
role="guilabel"} setting, click `View My Services`{.interpreted-text
role="guilabel"}.

Doing so reveals an `IAP Service`{.interpreted-text role="guilabel"}
page, listing the various `IAP (In-app purchases)`{.interpreted-text
role="abbr"} services in the database. From here, click an
`IAP (In-app purchases)`{.interpreted-text role="abbr"} service to open
its `Account Information`{.interpreted-text role="guilabel"} page, where
additional credits can be purchased.

#### Manually buy credits

To manually buy credits in Odoo, follow these steps:

First, go to the `Settings application`{.interpreted-text
role="menuselection"} and type [IAP]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar. Alternatively users
can scroll down to the `Contacts`{.interpreted-text role="guilabel"}
section. Under the `Contacts`{.interpreted-text role="guilabel"}
section, where it says `Odoo IAP`{.interpreted-text role="guilabel"},
click `View My
Services`{.interpreted-text role="guilabel"}.

{.align-center}

Doing so reveals an `IAP Account`{.interpreted-text role="guilabel"}
page, listing the various `IAP (In-app purchases)`{.interpreted-text
role="abbr"} services in the database. From here, click an
`IAP (In-app purchases)`{.interpreted-text role="abbr"} service to open
its `Account Information`{.interpreted-text role="guilabel"} page, where
additional credits can be purchased.

On the `Account Information`{.interpreted-text role="guilabel"} page,
click the `Buy Credit`{.interpreted-text role="guilabel"} button. Doing
so loads a `Buy Credits for (IAP Account)`{.interpreted-text
role="guilabel"} page in a new tab. From here, click
`Buy`{.interpreted-text role="guilabel"} on the desired pack of credits.
Then, follow the prompts to enter payment details, and confirm the
order.

{.align-center}

Once the transaction is complete, the credits are available for use in
the database.

#### Low-credit notification {#in_app_purchase/low-credits}

It is possible to be notified when credits are low, in order to avoid
running out of credits, while using an
`IAP (In-app purchases)`{.interpreted-text role="abbr"} service. To do
that, follow this process:

Go to the `Settings application`{.interpreted-text
role="menuselection"}, and type [IAP]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar. Under the
`Contacts`{.interpreted-text role="guilabel"} section, where it says
`Odoo IAP`{.interpreted-text role="guilabel"}, click `View My
Services`{.interpreted-text role="guilabel"}.

The available `IAP (In-app purchases)`{.interpreted-text role="abbr"}
accounts appear in a list view on the `IAP Account`{.interpreted-text
role="guilabel"} page. From here, click on the desired
`IAP (In-app purchases)`{.interpreted-text role="abbr"} account to view
that service\'s `Account Information`{.interpreted-text role="guilabel"}
page.

On the `Account Information`{.interpreted-text role="guilabel"} page,
tick the `Warn Me`{.interpreted-text role="guilabel"} checkbox. Doing so
reveals two fields on the form: `Threshold`{.interpreted-text
role="guilabel"} and `Warning Email`{.interpreted-text role="guilabel"}.

In the `Threshold`{.interpreted-text role="guilabel"} field, enter an
amount of credits Odoo should use as the minimum threshold for this
service. In the `Warning Email`{.interpreted-text role="guilabel"}
field, enter the email address that receives the notification.

Odoo sends a low-credit alert to the `Warning Email`{.interpreted-text
role="guilabel"} when the balance of credits falls below the amount
listed as the `Threshold`{.interpreted-text role="guilabel"}.
