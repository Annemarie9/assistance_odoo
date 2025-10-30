# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/customer_invoices/snailmail.md

Snailmail {#customer_invoices/snailmail}
=========

Sending direct mail can be an effective strategy for grabbing people\'s
attention, especially when their email inboxes are overflowing. With
Odoo, you have the ability to send invoices and follow-up reports
through postal mail worldwide, all from within your database.

Configuration
-------------

Go to
`Accounting --> Configuration --> Settings --> Customer invoices`{.interpreted-text
role="menuselection"} section to activate `Snailmail`{.interpreted-text
role="guilabel"}.

To make it a by-default feature, select `Send by Post`{.interpreted-text
role="guilabel"} in the `Default Sending
Options`{.interpreted-text role="guilabel"} section.

{.align-center}

Send invoices by post
---------------------

Open your invoice, click on `Send & Print`{.interpreted-text
role="guilabel"} and select `Send by Post`{.interpreted-text
role="guilabel"}. Make sure your customer's address is set correctly,
including the country, before sending the letter.

::: {.important}
::: {.title}
Important
:::

Your document must respect the following rules to pass the validation
before being sent:

-   Margins must be **5 mm** on all sides. As Odoo forces the outer
    margins by filling them with white before sending the snailmail, it
    can results in the user\'s custom being cut off if it protrudes into
    the margins. To check the margins, activate the `developer mode
    <developer-mode>`{.interpreted-text role="ref"}, go to
    `General Settings --> Technical --> Reporting
    section: Paper Format`{.interpreted-text role="menuselection"}.
-   A square of **15mm by 15mm** on the bottom left corner has to stay
    clear.
-   The postage area has to stay clear
    (`download the snailmail PDF template
    <snailmail/snailmail-template.pdf>`{.interpreted-text
    role="download"} for more details).
-   Pingen (Odoo Snailmail service provider) scans the area to process
    the address, so if something gets written outside the area, it is
    not counted as part of the address.
:::

Pricing
-------

Snailmail is an
`/applications/essentials/in_app_purchase`{.interpreted-text role="doc"}
service that requires prepaid stamps (=credits) to work. Sending one
document consumes one stamp.

To buy stamps, go to
`Accounting --> Configuration --> Settings --> Customer
invoices: Snailmail`{.interpreted-text role="menuselection"}, click on
`Buy credits`{.interpreted-text role="guilabel"}, or go to
`Settings --> In-App
Purchases: Odoo IAP`{.interpreted-text role="menuselection"}, and click
on `View my Services`{.interpreted-text role="guilabel"}.

::: {.seealso}

:::
