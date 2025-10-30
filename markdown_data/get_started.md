# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/get_started.md

show-content

:   

Get started
===========

When you first open your Odoo Accounting app, the
`Accounting Dashboard`{.interpreted-text role="guilabel"} welcomes you
with a step-by-step onboarding banner, a wizard that helps you get
started. This onboarding banner is displayed until you choose to close
it.

The settings visible in the onboarding banner can still be modified
later by going to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Odoo Accounting automatically installs the appropriate **Fiscal
Localization Package** for your company, according to the country
selected at the creation of the database. This way, the right accounts,
reports, and taxes are ready-to-go.
`Click here <fiscal_localizations/packages>`{.interpreted-text
role="ref"} for more information about Fiscal Localization Packages.
:::

Accounting onboarding banner
----------------------------

The step-by-step Accounting onboarding banner is composed of four steps:



1.  `accounting-setup-periods`{.interpreted-text role="ref"}
2.  `accounting-setup-bank`{.interpreted-text role="ref"}
3.  `accounting-setup-taxes`{.interpreted-text role="ref"}
4.  `accounting-setup-chart`{.interpreted-text role="ref"}

### Accounting Periods {#accounting-setup-periods}

Define the **Fiscal Years**' opening and closing dates, which are used
to generate reports automatically, and set your **Tax Return
Periodicity**, along with a reminder to never miss a tax return
deadline.

By default, the opening date is set on the 1st of January and the
closing date on the 31st of December, as this is the most common use.

::: {.note}
::: {.title}
Note
:::

You can also change these settings by going to
`Accounting --> Configuration -->
Settings --> Fiscal Periods`{.interpreted-text role="menuselection"} and
updating the values.
:::

### Bank Account {#accounting-setup-bank}

Connect your bank account to your database and have your bank statements
synced automatically. To do so, find your bank in the list, click
`Connect`{.interpreted-text role="guilabel"}, and follow the
instructions on-screen.

::: {.note}
::: {.title}
Note
:::

`Click here <bank/bank_synchronization>`{.interpreted-text role="doc"}
for more information about this feature.
:::

If your Bank Institution can't be synchronized automatically, or if you
prefer not to sync it with your database, you can also configure your
bank account manually by typing its name, clicking
`Create your Bank Account`{.interpreted-text role="guilabel"}, and
filling out the form.

-   `Name`{.interpreted-text role="guilabel"}: the bank account\'s name,
    as displayed in Odoo.
-   `Account Number`{.interpreted-text role="guilabel"}: your bank
    account number (IBAN in Europe).
-   `Bank`{.interpreted-text role="guilabel"}: click
    `Create and edit`{.interpreted-text role="guilabel"} to configure
    the bank\'s details. Add the bank institution\'s
    `Name`{.interpreted-text role="guilabel"} and its
    `Identifier Code`{.interpreted-text role="guilabel"} (BIC or SWIFT).
-   `Code`{.interpreted-text role="guilabel"}: this code is your
    Journal\'s `Short Code`{.interpreted-text role="guilabel"}, as
    displayed in Odoo. By default, Odoo creates a new Journal with this
    short code.
-   `Journal`{.interpreted-text role="guilabel"}: This field is
    displayed if you have an existing bank journal that is not linked
    yet to a bank account. If so, then select the
    `Journal`{.interpreted-text role="guilabel"} you want to use to
    record the financial transactions linked to this bank account or
    create a new one by clicking `Create and Edit`{.interpreted-text
    role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- You can add as many bank accounts as needed with this tool by going
to
`Accounting --> Configuration --> Add a Bank Account`{.interpreted-text
role="menuselection"}. - `Click here <bank>`{.interpreted-text
role="doc"} for more information about Bank Accounts.
:::

### Taxes {#accounting-setup-taxes}

This menu allows you to create new taxes, (de)activate, or modify
existing taxes. Depending on the
`localization package <../fiscal_localizations>`{.interpreted-text
role="doc"} installed on your database, taxes required for your country
are already configured.

::: {.note}
::: {.title}
Note
:::

`Click here <taxes>`{.interpreted-text role="doc"} for more information
about taxes.
:::

### Chart of Accounts {#accounting-setup-chart}

With this menu, you can add accounts to your **Chart of Accounts** and
indicate their initial opening balances.

Basic settings are displayed on this page to help you review your Chart
of Accounts. To access all the settings of an account, click on the
`Setup`{.interpreted-text role="guilabel"} button at the end of the
line.



::: {.note}
::: {.title}
Note
:::

`Click here <get_started/chart_of_accounts>`{.interpreted-text
role="doc"} for more information on how to configure your Chart of
Accounts.
:::

Invoicing onboarding banner
---------------------------

There is another step-by-step onboarding banner that helps you take
advantage of your Odoo Invoicing and Accounting apps. The Invoicing
onboarding banner is the one that welcomes you if you use the Invoicing
app rather than the Accounting app.

If you have Odoo Accounting installed on your database, you can reach it
by going to `Accounting --> Customers --> Invoices`{.interpreted-text
role="menuselection"}.

The Invoicing onboarding banner consists of four main steps:



1.  `invoicing-setup-company`{.interpreted-text role="ref"}
2.  `invoicing-setup-layout`{.interpreted-text role="ref"}
3.  `invoicing-setup-invoice`{.interpreted-text role="ref"}
4.  `invoicing-setup-payments`{.interpreted-text role="ref"}

### Company Data {#invoicing-setup-company}

Add your company's details, such as the name, address, logo, website,
phone number, email address, and Tax ID or VAT number. These details are
then displayed on your documents, such as invoices.

::: {.note}
::: {.title}
Note
:::

You can also change the company\'s details by going to
`Settings --> General
Settings`{.interpreted-text role="menuselection"}, scrolling down to the
`Companies`{.interpreted-text role="guilabel"} section, and
`Update Info`{.interpreted-text role="guilabel"}.
:::

### Documents Layout {#invoicing-setup-layout}

Customize the
`default invoice layout <studio/pdf-reports/default-layout>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

You can also change the invoice layout by going to `Settings --> General
Settings`{.interpreted-text role="menuselection"}, scrolling down to the
`Companies`{.interpreted-text role="guilabel"} section, and clicking
`Configure
Document Layout`{.interpreted-text role="guilabel"}.
:::

### Create Invoice {#invoicing-setup-invoice}

Create your first invoice.

::: {.tip}
::: {.title}
Tip
:::

Add your **bank account number** and a link to your **General Terms &
Condition** in the footer. This way, your contacts can find the full
content of your GT&C online without having to print them on the invoices
you issue.
:::

### Online Payments {#invoicing-setup-payments}

Get started with Stripe and enable secure integrated credit and debit
card payments within Odoo.

::: {.tip}
::: {.title}
Tip
:::

To use other payment providers, go to
`Invoicing --> Configuration --> Payment Providers`{.interpreted-text
role="guilabel"} and
`enable the desired providers <../payment_providers>`{.interpreted-text
role="doc"}.
:::

::: {.seealso}
\* `bank`{.interpreted-text role="doc"} \*
`get_started/chart_of_accounts`{.interpreted-text role="doc"} \*
`bank/bank_synchronization`{.interpreted-text role="doc"} \*
`../fiscal_localizations`{.interpreted-text role="doc"} \* [Odoo
Tutorials: Accounting and Invoicing - Getting started
\
:::

::: {.toctree titlesonly=""}
get\_started/cheat\_sheet get\_started/chart\_of\_accounts
get\_started/multi\_currency get\_started/avg\_price\_valuation
get\_started/tax\_units
:::
