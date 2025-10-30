# File: /content/odoo_doc17.0/fr/content/applications/finance/fiscal_localizations/united_kingdom.md

United Kingdom
==============

Configuration {#united-kingdom/modules}
-------------

`Install <general/install>`{.interpreted-text role="ref"} the
`UK - Accounting`{.interpreted-text role="guilabel"} and the
`UK - Accounting
Reports`{.interpreted-text role="guilabel"} modules to get all the
features of the UK localization.

+----------------------+----------------------+----------------------+
| Name                 | Technical name       | Description          |
+======================+======================+======================+
| `UK - Accountin      | [l                   | -   CT600-ready      |
| g`{.interpreted-text | 10n\_uk]{.title-ref} |     chart of         |
| role="guilabel"}     |                      |     accounts         |
|                      |                      | -   VAT100-ready tax |
|                      |                      |     structure        |
|                      |                      | -   Infologic UK     |
|                      |                      |     counties listing |
+----------------------+----------------------+----------------------+
| `UK                  | [l10n\_uk\_          | -   Accounting       |
|  - Accounting Report | reports]{.title-ref} |     reports for the  |
| s`{.interpreted-text |                      |     UK               |
| role="guilabel"}     |                      | -   Allows sending   |
|                      |                      |     the tax report   |
|                      |                      |     via the MTD-VAT  |
|                      |                      |     API to HMRC.     |
+----------------------+----------------------+----------------------+
| `                    | [accoun              | Allows generating    |
| UK BACS Payment File | t\_bacs]{.title-ref} | `unit                |
| s`{.interpreted-text |                      | ed-kingdom/BACS-file |
| role="guilabel"}     |                      | s`{.interpreted-text |
|                      |                      | role="ref"} for bill |
|                      |                      | and invoice payments |
+----------------------+----------------------+----------------------+

::: {.note}
::: {.title}
Note
:::

\- Only UK-based companies can submit reports to HMRC. - Installing the
module `UK - Accounting Reports`{.interpreted-text role="guilabel"}
installs all two modules at once.
:::

::: {.seealso}
\- [HM Revenue &
Customs](https://www.gov.uk/government/organisations/hm-revenue-customs/)
- [Overview of Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/)
:::

Chart of accounts
-----------------

The UK chart of accounts is included in the
`UK - Accounting`{.interpreted-text role="guilabel"} module. Go to
`Accounting --> Configuration --> Accounting: Chart of Accounts`{.interpreted-text
role="menuselection"} to access it.

Setup your `CoA (chart of accounts)`{.interpreted-text role="abbr"} by
going to `Accounting --> Configuration
--> Settings --> Accounting Import section`{.interpreted-text
role="menuselection"} and choose to `Review Manually`{.interpreted-text
role="guilabel"} or `Import (recommended)`{.interpreted-text
role="guilabel"} your initial balances.

Taxes
-----

As part of the localization module, UK taxes are created automatically
with their related financial accounts and configuration.

Go to
`Accounting --> Configuration --> Settings --> Taxes`{.interpreted-text
role="menuselection"} to update the `Default Taxes`{.interpreted-text
role="guilabel"}, the `Tax Return Periodicity`{.interpreted-text
role="guilabel"} or to `Configure your
tax accounts`{.interpreted-text role="guilabel"}.

To edit existing taxes or to `Create`{.interpreted-text role="guilabel"}
a new tax, go to `Accounting -->
Configuration --> Accounting: Taxes`{.interpreted-text
role="menuselection"}.

::: {.seealso}
\- `taxes <../accounting/taxes>`{.interpreted-text role="doc"} -
Tutorial: [Tax report and
return](https://www.odoo.com/slides/slide/tax-report-and-return-1719?fullscreen=1).
:::

### Making Tax Digital (MTD)

In the UK, all VAT-registered businesses have to follow the MTD rules by
using software to submit their VAT returns.

The **UK - Accounting Reports** module enables you to comply with the
[HM Revenue &
Customs](https://www.gov.uk/government/organisations/hm-revenue-customs/)
requirements regarding [Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/).

::: {.important}
::: {.title}
Important
:::

If your periodic submission is more than three months late, it is no
longer possible to submit it through Odoo, as Odoo only retrieves open
bonds from the last three months. Your submission has to be done
manually by contacting HMRC.
:::

#### Register your company to HMRC before the first submission {#uk_localization/hmrc-registration}

Go to `Accounting --> Reporting --> Tax report`{.interpreted-text
role="menuselection"} and click on `Connect to HMRC`{.interpreted-text
role="guilabel"}. Enter your company information on the HMRC platform.
You only need to do it once.

#### Periodic submission to HMRC

Import your obligations HMRC, filter on the period you want to submit,
and send your tax report by clicking `Send to HMRC`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

You can use dummy credentials to demo the HMRC flow. To do so, activate
the `developer mode <developer-mode>`{.interpreted-text role="ref"} and
go to `General Settings -->
Technical --> System Parameters`{.interpreted-text
role="menuselection"}. From here, search for
[l10n\_uk\_reports.hmrc\_mode]{.title-ref} and change the value line to
[demo]{.title-ref}. You can get such credentials from the [HMRC
Developer Hub](https://developer.service.hmrc.gov.uk/api-test-user).
:::

#### Periodic submission to HMRC for multi-company

Only one company and one user can connect to HMRC simultaneously. If
several UK-based companies are on the same database, the user who
submits the HMRC report must follow these instructions before each
submission:

1.  Log into the company for which the submission has to be done.
2.  Go to `General Settings`{.interpreted-text role="guilabel"}, and in
    the `Users`{.interpreted-text role="guilabel"} section, click
    `Manage Users`{.interpreted-text role="guilabel"}. Select the user
    who is connected to HMRC.
3.  Go to the `UK HMRC Integration`{.interpreted-text role="guilabel"}
    tab and click `Reset Authentication
    Credentials`{.interpreted-text role="guilabel"} or
    `Remove Authentication Credentials`{.interpreted-text
    role="guilabel"} button.
4.  You can now
    `register your company to HMRC <uk_localization/hmrc-registration>`{.interpreted-text
    role="ref"} and submit the tax report for this company.
5.  Repeat the steps for other companies\' HMRC submissions.

::: {.note}
::: {.title}
Note
:::

During this process, the `Connect to HMRC`{.interpreted-text
role="guilabel"} button no longer appears for other UK-based companies.
:::

Bacs files {#united-kingdom/BACS-files}
----------

`Bacs (Bankers' Automated Clearing Services)`{.interpreted-text
role="abbr"} files are electronic files used in the UK to process
payments and transfers between bank accounts.

To enable the use of Bacs files, make sure the
`UK BACS Payment Files <united-kingdom/modules>`{.interpreted-text
role="ref"} module is installed, then:

1.  Configure your Bacs Service User Number:
    1.  Go to
        `Accounting --> Configuration --> Settings`{.interpreted-text
        role="menuselection"} and scroll down to the
        `Customer Payments`{.interpreted-text role="guilabel"} section.
    2.  Enter your `Service User Number`{.interpreted-text
        role="guilabel"} under `BACS`{.interpreted-text role="guilabel"}
        and manually save.
2.  Configure your **bank** journal:
    1.  Go to
        `Accounting --> Configuration --> Journals`{.interpreted-text
        role="menuselection"} and select your **bank** journal.
    2.  In the `Journal Entries`{.interpreted-text role="guilabel"} tab,
        configure the `Account Number`{.interpreted-text
        role="guilabel"} and `Bank`{.interpreted-text role="guilabel"}
        fields.
    3.  In the `Incoming Payments`{.interpreted-text role="guilabel"}
        and `Outgoing Payments`{.interpreted-text role="guilabel"} tabs,
        make sure the `BACS Direct Debit`{.interpreted-text
        role="guilabel"} payment method is enabled.
3.  Configure the contacts for whom you wish to use Bacs files: Access
    the contact form and, in the `Accounting`{.interpreted-text
    role="guilabel"} tab, click `Add a line`{.interpreted-text
    role="guilabel"} and fill in the `Account Number`{.interpreted-text
    role="guilabel"} and `Bank`{.interpreted-text role="guilabel"}
    fields.

### Bill payments

To generate Bacs files for bill payments, set the
`Payment Method`{.interpreted-text role="guilabel"} to
`BACS Direct Debit`{.interpreted-text role="guilabel"} when
`registering vendor payments <../accounting/payments>`{.interpreted-text
role="doc"}.

Then, create a vendor batch payment:

1.  Go to `Accounting --> Vendors --> Batch Payments`{.interpreted-text
    role="menuselection"}, and click `New`{.interpreted-text
    role="guilabel"}.
2.  Select the bank journal in the `Bank`{.interpreted-text
    role="guilabel"} field, set the `Payment Method`{.interpreted-text
    role="guilabel"} to `BACS Direct Credit`{.interpreted-text
    role="guilabel"}, and select a
    `BACS Processing Date`{.interpreted-text role="guilabel"}.
3.  Optionally, you can also:
    -   select a `BACS Expiry Date`{.interpreted-text role="guilabel"};
    -   enable `BACS Multi Mode`{.interpreted-text role="guilabel"} to
        process the payments on their individual date.
4.  Click `Add a line`{.interpreted-text role="guilabel"}, select the
    payments you want to include, click `Select`{.interpreted-text
    role="guilabel"}, then `Validate`{.interpreted-text
    role="guilabel"}.

Once validated, the Bacs file is available in the chatter. You can also
`Re-generate
Export File`{.interpreted-text role="guilabel"} if you need a new Bacs
file for that batch payment.



::: {.seealso}
`../accounting/payments/batch`{.interpreted-text role="doc"}
:::

### Invoice payments

Before generating Bacs files for invoice payments, you must first create
a **BACS Direct Debit Instruction**: Go to
`Accounting --> Customers --> BACS Direct Debit Instructions`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text
role="guilabel"}. Select a `Customer`{.interpreted-text
role="guilabel"}, their `IBAN`{.interpreted-text role="guilabel"}, and
the `Journal`{.interpreted-text role="guilabel"} you wish to use.

To generate Bacs files for invoice payments, set the
`Payment Method`{.interpreted-text role="guilabel"} to
`BACS Direct Debit`{.interpreted-text role="guilabel"} when
`registering invoice payments <../accounting/payments>`{.interpreted-text
role="doc"}.

::: {.tip}
::: {.title}
Tip
:::

If you register the payment for an invoice linked to a subscription or
via `Accounting --> Customers --> Payments`{.interpreted-text
role="menuselection"}, you can select the `BACS
Payment Type`{.interpreted-text role="guilabel"}:

-   `Direct debit-first collection of a series`{.interpreted-text
    role="guilabel"};
-   `Direct debit single collection`{.interpreted-text role="guilabel"};
-   `Direct debit repeating collection in a series`{.interpreted-text
    role="guilabel"};
-   `Direct debit-final collection of a series`{.interpreted-text
    role="guilabel"}.
:::

Then, create a customer batch payment:

1.  Go to
    `Accounting --> Customers --> Batch Payments`{.interpreted-text
    role="menuselection"}, and click `New`{.interpreted-text
    role="guilabel"}.
2.  Select the bank journal in the `Bank`{.interpreted-text
    role="guilabel"} field, set the `Payment Method`{.interpreted-text
    role="guilabel"} to `BACS Direct Credit`{.interpreted-text
    role="guilabel"}, and select a
    `BACS Processing Date`{.interpreted-text role="guilabel"}.
3.  Optionally, you can also:
    -   select a `BACS Expiry Date`{.interpreted-text role="guilabel"};
    -   enable `BACS Multi Mode`{.interpreted-text role="guilabel"} to
        process the payments on their individual date.
4.  Click `Add a line`{.interpreted-text role="guilabel"}, select the
    payments you want to include, click `Select`{.interpreted-text
    role="guilabel"}, then `Validate`{.interpreted-text
    role="guilabel"}.

Once validated, the Bacs file is available in the chatter. You can also
`Re-generate
Export File`{.interpreted-text role="guilabel"} if you need a new Bacs
file for that batch payment.
