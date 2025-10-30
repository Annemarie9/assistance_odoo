# File: /content/odoo_doc17.0/fr/content/applications/finance/fiscal_localizations/united_states.md

United States
=============

The Odoo fiscal localization package for the United States follows the
Generally Acceptable Accounting Principles (GAAP) accounting standards
and rules used to prepare financial statements, as outlined by the
Financial Accounting Standards Board (FASB) and adopted by the
Securities and Exchange Commission (SEC).

::: {.seealso}
\- [Financial Accounting Standards Board
(FASB)](https://asc.fasb.org/Home) - [Securities and Exchange Commission
(SEC)](https://www.sec.gov/)
:::

In addition, a series of videos on the subject of Accounting are
available through Odoo\'s eLearning platform. These videos cover how to
start from scratch, set up configurations, complete common workflows,
and provide in-depth looks at some specific use cases, as well.

::: {.seealso}
\- [Odoo Tutorials: Accounting &
Invoicing](https://www.odoo.com/slides/accounting-and-invoicing-19) -
[Odoo SmartClass:
Accounting](https://www.odoo.com/slides/smartclass-accounting-121)
:::

Configuration
-------------

Below are the available modules in Odoo for accounting use in the United
States.

::: {.note}
::: {.title}
Note
:::

The modules listed below are either for reference only or are optional,
as the core requirements to operate under the US fiscal localization in
Odoo are already included under the default package that came installed
during database initialization.

Verify the default package is in use by navigating to
`Accounting App -->
Settings`{.interpreted-text role="menuselection"} and under the
`Fiscal Localization`{.interpreted-text role="guilabel"} section at the
top, look for the [Generic Chart Template]{.title-ref} selection to be
listed next to the `Package`{.interpreted-text role="guilabel"} field
label. This chart template includes the necessary settings for the US
localization for the Odoo *Accounting* app.

{.align-center}
:::

### Modules installation

`Install <general/install>`{.interpreted-text role="ref"} the following
modules to get all the features of the United States localization:

+-----------------+-----------------+-----------------------------------+
| Name            | Technical name  | Description                       |
+=================+=================+===================================+
| `               | [l10n\_         | Base accounting module for United |
| United States - | us]{.title-ref} | States localization.              |
|  Accounting`{.i |                 |                                   |
| nterpreted-text |                 |                                   |
| r               |                 |                                   |
| ole="guilabel"} |                 |                                   |
+-----------------+-----------------+-----------------------------------+
| `               | [               | Adds United States accounting     |
| US - Accounting | l10n\_us\_repor | reports.                          |
|  Reports <l10n_ | ts]{.title-ref} |                                   |
| us/reports>`{.i |                 |                                   |
| nterpreted-text |                 |                                   |
| role="ref"}     |                 |                                   |
+-----------------+-----------------+-----------------------------------+
| `US Ch          | [l10n\_us       | Enables the printing of payments  |
| ecks Layout`{.i | \_check\_printi | on pre-printed check paper.       |
| nterpreted-text | ng]{.title-ref} | Supports the three most common    |
| r               |                 | check formats and will work out   |
| ole="guilabel"} |                 | of the box with the linked checks |
|                 |                 | from                              |
|                 |                 | [checkde                          |
|                 |                 | pot.net](https://checkdepot.net/c |
|                 |                 | ollections/computer-checks/Odoo). |
|                 |                 |                                   |
|                 |                 | -   [Check on top: Quicken /      |
|                 |                 |     QuickBooks                    |
|                 |                 |     standard](                    |
|                 |                 | https://checkdepot.net/collection |
|                 |                 | s/computer-checks/odoo+top-check) |
|                 |                 | -   [Check on middle: Peachtree   |
|                 |                 |     standard](htt                 |
|                 |                 | ps://checkdepot.net/collections/c |
|                 |                 | omputer-checks/odoo+middle-check) |
|                 |                 | -   [Check on bottom: ADP         |
|                 |                 |     standard](htt                 |
|                 |                 | ps://checkdepot.net/collections/c |
|                 |                 | omputer-checks/odoo+Bottom-Check) |
+-----------------+-----------------+-----------------------------------+
| `NACH           | [l10n\_u        | Export payments as NACHA files    |
| A Payments <l10 | s\_payment\_nac | for use in the United States.     |
| n_us/nacha>`{.i | ha]{.title-ref} |                                   |
| nterpreted-text |                 |                                   |
| role="ref"}     |                 |                                   |
+-----------------+-----------------+-----------------------------------+
| `1099 Repor     | [l10n\_us\_10   | Export 1099 data for e-filing     |
| ting <l10n_us/1 | 99]{.title-ref} | with a 3rd party.                 |
| 099-report>`{.i |                 |                                   |
| nterpreted-text |                 |                                   |
| role="ref"}     |                 |                                   |
+-----------------+-----------------+-----------------------------------+
| `Ava            | [account\_avat  | Module for the                    |
| tax <l10n_us/ta | ax]{.title-ref} | `                                 |
| xes-avatax>`{.i |                 | AvaTax integration <../accounting |
| nterpreted-text |                 | /taxes/avatax>`{.interpreted-text |
| role="ref"}     |                 | role="doc"} with Odoo.            |
+-----------------+-----------------+-----------------------------------+
| `               | [l10n           | Includes the necessary rules for  |
| United States - | \_us\_hr\_payro | United States payroll, including: |
|  Payroll <l10n_ | ll]{.title-ref} |                                   |
| us/payroll>`{.i |                 | -   Employee Details              |
| nterpreted-text |                 | -   Employee Contracts            |
| role="ref"}     |                 | -   Passport-based Contracts      |
|                 |                 | -   Allowances/Deductions         |
|                 |                 | -   Allow Configurations for      |
|                 |                 |     Basic/Gross/Net Salary        |
|                 |                 | -   Employee Payslip              |
|                 |                 | -   Integration with Leaves       |
|                 |                 |     Management                    |
+-----------------+-----------------+-----------------------------------+
| `U              | [l10n\_us\_hr\  | Contains the necessary accounting |
| nited States -  | _payroll\_accou | data for the United States        |
| Payroll with Ac | nt]{.title-ref} | payroll rules.                    |
| counting <l10n_ |                 |                                   |
| us/payroll>`{.i |                 |                                   |
| nterpreted-text |                 |                                   |
| role="ref"}     |                 |                                   |
+-----------------+-----------------+-----------------------------------+
| `United State   | [l10n\_us\      | Export Work Entries to the ADP    |
| s - Payroll - E | _hr\_payroll\_a | payroll software.                 |
| xport to ADP <l | dp]{.title-ref} |                                   |
| 10n_us/adp>`{.i |                 |                                   |
| nterpreted-text |                 |                                   |
| role="ref"}     |                 |                                   |
+-----------------+-----------------+-----------------------------------+

Chart of accounts {#l10n_us/coa}
-----------------

The
`chart of accounts (COA) <../accounting/get_started/chart_of_accounts>`{.interpreted-text
role="doc"} for the United States localization, in Odoo, follows the
standard
`GAAP (Generally Acceptable Accounting Practices)`{.interpreted-text
role="abbr"} structure, with accounts grouped into seven main
categories, with corresponding numeric values that prefix individual
journal entries:

-   **Receivable**: the balance of money (or credit) due to the business
    for goods or services delivered or used, but not yet paid for by
    customers. `AR (Accounts Receivable)`{.interpreted-text role="abbr"}
    is indicated by the journal code labeled (or beginning) with
    `1`{.interpreted-text role="guilabel"}.
-   **Payable**: the business\'s short-term obligations owed to its
    creditors or suppliers, which have not yet been paid.
    `AP (Accounts Payable)`{.interpreted-text role="abbr"} is indicated
    by the journal code labeled (or beginning) with
    `2`{.interpreted-text role="guilabel"}.
-   **Equity**: the amount of money that would be returned to a
    company\'s shareholders if all of the assets were liquidated and all
    of the company\'s debt was paid off in the case of liquidation.
    Equity is indicated by the journal code labeled (or beginning) with
    `3`{.interpreted-text role="guilabel"} or `9`{.interpreted-text
    role="guilabel"}.
-   **Assets**: items listed on the balance sheet that contains economic
    value or have the ability to generate cash flows in the future, such
    as a piece of machinery, a financial security, or a patent. Assets
    are indicated by the journal code labeled (or beginning) with
    `1`{.interpreted-text role="guilabel"}.
-   **Liability**: refers to a company\'s financial debts or obligations
    that arise during the course of business operations. Liabilities are
    indicated by the journal code labeled (or beginning) with
    `2`{.interpreted-text role="guilabel"}.
-   **Income**: synonymous with *net income*, this is the profit a
    company retains after paying off all relevant expenses from sales
    revenue earned. Income is indicated by the journal code labeled (or
    beginning) with `4`{.interpreted-text role="guilabel"} or
    `6`{.interpreted-text role="guilabel"}.
-   **Expenses**: the cost of operations that a company incurs to
    generate revenue. Expenses are indicated by the journal code labeled
    (or beginning) with a `6`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Predefined accounts are included in Odoo, as part of the
`CoA (Chart of Accounts)`{.interpreted-text role="abbr"} that\'s
installed with the US localization package. The accounts listed below
are preconfigured to perform certain operations within Odoo. It is
recommended to **not** delete these accounts; however, if changes are
needed, rename the accounts instead.

+----------------------------------+----------------------------------+
| `Type`{.interpreted-text         | `Account Name`{.interpreted-text |
| role="guilabel"}                 | role="guilabel"}                 |
+==================================+==================================+
| `C                               | | `Bank Sus                      |
| urrent Assets`{.interpreted-text | pense Account`{.interpreted-text |
| role="guilabel"}                 |   role="guilabel"}               |
|                                  | | `Outstan                       |
|                                  | ding Receipts`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Outstan                       |
|                                  | ding Payments`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Liqui                         |
|                                  | dity Transfer`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `St                            |
|                                  | ock Valuation`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Stock Inter                   |
|                                  | im (Received)`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Stock Interi                  |
|                                  | m (Delivered)`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Cost                          |
|                                  | of Production`{.interpreted-text |
|                                  |   role="guilabel"}               |
+----------------------------------+----------------------------------+
| `Income`{.interpreted-text       | | `Foreign                       |
| role="guilabel"}                 | Exchange Gain`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Cash Di                       |
|                                  | fference Gain`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Cash                          |
|                                  | Discount Gain`{.interpreted-text |
|                                  |   role="guilabel"}               |
+----------------------------------+----------------------------------+
| `Expenses`{.interpreted-text     | | `Cash                          |
| role="guilabel"}                 | Discount Loss`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Foreign                       |
|                                  | Exchange Loss`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Cash Di                       |
|                                  | fference Loss`{.interpreted-text |
|                                  |   role="guilabel"}               |
+----------------------------------+----------------------------------+
| `Current                         | `Undistributed P                 |
| Year Earnings`{.interpreted-text | rofits/Losses`{.interpreted-text |
| role="guilabel"}                 | role="guilabel"}                 |
+----------------------------------+----------------------------------+
| `Receivable`{.interpreted-text   | `Accou                           |
| role="guilabel"}                 | nt Receivable`{.interpreted-text |
|                                  | role="guilabel"}                 |
+----------------------------------+----------------------------------+
| `Payable`{.interpreted-text      | `Ac                              |
| role="guilabel"}                 | count Payable`{.interpreted-text |
|                                  | role="guilabel"}                 |
+----------------------------------+----------------------------------+
:::

::: {.seealso}
\- `../accounting/get_started/chart_of_accounts`{.interpreted-text
role="doc"} - `../accounting/get_started/cheat_sheet`{.interpreted-text
role="doc"}
:::

### View, edit, and sort accounts

Access the *Chart of Accounts* dashboard in Odoo by navigating to
`Accounting app
--> Configuration --> Accounting: Chart of Accounts`{.interpreted-text
role="menuselection"}.

From the `Chart of Accounts`{.interpreted-text role="guilabel"}
dashboard, create new accounts by clicking the `New`{.interpreted-text
role="guilabel"} button in the top-left corner of the dashboard and
`filling in the
corresponding form <chart-of-account/create>`{.interpreted-text
role="ref"}. Search and sort through existing accounts by using specific
`Filters`{.interpreted-text role="guilabel"} and
`Group By`{.interpreted-text role="guilabel"} criteria, which are
available in the search drop-down menu.

To filter accounts by category, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(caret down)`{.interpreted-text role="guilabel"} icon to access the
drop-down menu and look under the `Filters`{.interpreted-text
role="guilabel"} column for individual selections. Clicking on a
specific category will only show accounts that match that particular
filter.

To view all the available account types, remove all of the filters in
the search bar, and then click the `fa-caret-down`{.interpreted-text
role="icon"} `(caret down)`{.interpreted-text role="guilabel"} icon to
access the drop-down menu. From there, select
`Account Type`{.interpreted-text role="guilabel"} under the
`Group By`{.interpreted-text role="guilabel"} column heading to list all
of the account types in the table.

{.align-center}

Besides structure, there are other key differences in the chart of
accounts in the United States, compared to other countries:

-   **Specificity**: US
    `GAAP (Generally Acceptable Accounting Practices)`{.interpreted-text
    role="abbr"} often requires more detailed accounts compared to some
    other countries. This can include separate accounts for various
    types of revenue, expenses, and assets, providing more granular
    information in financial reports.
-   **Regulatory Requirements**: In the United States, there are
    specific regulatory requirements set by bodies such as the
    `SEC (Securities and Exchange Commission)`{.interpreted-text
    role="abbr"} for publicly traded companies. These requirements may
    influence the structure and content of the
    `CoA (Chart of Accounts)`{.interpreted-text role="abbr"} to ensure
    compliance with reporting standards.
-   **Industry Practices**: Certain industries in the United States may
    have unique accounting requirements or specialized
    `CoA (Chart of Accounts)`{.interpreted-text role="abbr"} structures.
    For example, financial institutions often have specific accounts
    related to loans, investments, and interest income.
-   **Tax Considerations**: The
    `CoA (Chart of Accounts)`{.interpreted-text role="abbr"} may also
    reflect tax considerations, such as accounts for deductible
    expenses, deferred tax assets, and liabilities, to ensure compliance
    with tax laws and facilitate tax reporting.

These differences, ultimately, should be reflected in the
`CoA (Chart of Accounts)`{.interpreted-text role="abbr"} structure
itself, with the addition of new accounts, as needed, in order to meet
the demands of US accounting reporting requirements.

::: {.seealso}
\- `Create a new account <chart-of-account/create>`{.interpreted-text
role="ref"} - `../../essentials/search`{.interpreted-text role="doc"}
:::

Taxes {#l10n_us/taxes}
-----

In the United States, tax rates and what is considered taxable vary by
jurisdiction. Default *Sales* and *Purchase* taxes are created
automatically when the Odoo *Accounting* application is installed. To
manage existing or configure additional taxes, navigate to
`Accounting -->
Configuration --> Taxes`{.interpreted-text role="menuselection"}.

### AvaTax {#l10n_us/taxes-avatax}

**Avalara AvaTax** is a cloud-based tax calculation and compliance
software that integrates with Odoo for several localizations.
Integrating AvaTax with Odoo provides real-time and region-specific tax
calculations when items are sold, purchased, and invoiced in the
database.

::: {.important}
::: {.title}
Important
:::

AvaTax is available for integration with databases/companies that have
locations in the United States and Canada. Reference the
`avatax/fiscal_country`{.interpreted-text role="ref"} documentation for
more information.
:::

::: {.seealso}
Refer to the documentation articles below to integrate and configure an
AvaTax account with an Odoo database:

-   `AvaTax integration <../accounting/taxes/avatax>`{.interpreted-text
    role="doc"}
-   `Avalara management portal <../accounting/taxes/avatax/avalara_portal>`{.interpreted-text
    role="doc"}
-   `Calculate taxes with AvaTax <../accounting/taxes/avatax/avatax_use>`{.interpreted-text
    role="doc"}
-   [US Tax Compliance: AvaTax elearning
    video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)
-   Avalara\'s support documents: [About
    AvaTax](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=dqa1657870670369_dqa1657870670369&topicId=About_AvaTax.html&_LANG=enus)
:::

Reports {#l10n_us/reports}
-------

A number of
`report selections <../accounting/reporting>`{.interpreted-text
role="doc"} are readily available for the US localization, under the
`Accounting app --> Reporting`{.interpreted-text role="menuselection"}
drop-down menu:

-   `Balance Sheet <accounting/reporting/balance-sheet>`{.interpreted-text
    role="ref"}: a \"snapshot\" of a company\'s financial position at a
    specific point in time, which contains an overview of a company\'s
    assets, liabilities, and equity.
-   `Profit & Loss <accounting/reporting/balance-sheet>`{.interpreted-text
    role="ref"}: otherwise known as a *P&L statement* or *income
    statement*, provides a summary of a company\'s revenues, expenses,
    and profits/losses over a given period of time.
-   `Cash Flow Statement <l10n_us/cash-flow-statement>`{.interpreted-text
    role="ref"}: shows how much cash and cash equivalents a company has
    received and spent in a given period.
-   `Executive Summary <accounting/reporting/executive-summary>`{.interpreted-text
    role="ref"}: an overview report that covers the key performance
    indicators of a company\'s financial position, such as revenue,
    profit, and debt.
-   `Tax Report <accounting/reporting/tax-report>`{.interpreted-text
    role="ref"}: an official form filed for a tax authority that reports
    income, expenses, and other pertinent tax information. Tax reports
    allow taxpayers to calculate their tax liability, schedule tax
    payments, or request refunds for the overpayment of taxes. In Odoo,
    the tax report can be made monthly, every two months, quarterly,
    every 4 months, semi-annually, and annually.
-   `Check Register`{.interpreted-text role="guilabel"}: a report that
    displays cash transactions (regardless of the journal) with their
    running balance after the transaction. Only visible with the *US -
    Accounting Reports* ([l10n\_us\_reports]{.title-ref}) module
    installed.
-   `1099 Report <l10n_us/1099-report>`{.interpreted-text role="ref"}: a
    CSV download of payments made to non-employees in a period to file
    electronically in a third-party service. Only visible with the *1099
    Reporting* ([l10n\_us\_1099]{.title-ref}) module installed.

::: {#l10n_us/report-filters}
Depending on the type of report, certain filters are available at the
top of the dashboard:
:::

-   a *date* filter, indicated by a `fa-calendar`{.interpreted-text
    role="icon"} `(calendar)`{.interpreted-text role="guilabel"} icon
    that precedes a date in *MM/DD/YYYY* format. Use this to select a
    specific date or date range for the report.
-   a `fa-bar-chart`{.interpreted-text role="icon"}
    `Comparison`{.interpreted-text role="guilabel"} filter, to compare
    reporting periods against each other
-   a *journal* filter, as indicated by a `fa-book`{.interpreted-text
    role="icon"} `(book)`{.interpreted-text role="guilabel"} icon and
    the default setting of `All Journals`{.interpreted-text
    role="guilabel"}. Use this filter to specify which journals should
    be included in the report.
-   an *entries type* filter, as indicated by a
    `fa-filter`{.interpreted-text role="icon"}
    `(filter)`{.interpreted-text role="guilabel"} icon, with the default
    setting of `Posted Entries Only, Accrual Basis`{.interpreted-text
    role="guilabel"}. Use this filter to determine which type of journal
    entries should be included in the report (e.g. posted or draft),
    along with the type of accounting method (e.g. accrual or cash
    basis).
    -   There are view options in this filter, as well, one that will
        `Hide lines at 0`{.interpreted-text role="guilabel"} for more
        relevant viewing, along with a
        `Split Horizontally`{.interpreted-text role="guilabel"} option
        to keep the report above the screen\'s fold, removing the need
        to scroll.

        {.align-center}
-   a *decimal* filter, that by default, includes figures with cents, as
    indicated by the `In .$`{.interpreted-text role="guilabel"} setting.
    Use the other options in the drop-down menu to change figures in the
    report to whole numbers (`In $`{.interpreted-text role="guilabel"}),
    thousands (`In K$`{.interpreted-text role="guilabel"}), or millions
    (`In M$`{.interpreted-text role="guilabel"}) formats.
-   a report *customization* filter, indicated by the
    `fa-cogs`{.interpreted-text role="icon"} `(gears)`{.interpreted-text
    role="guilabel"} icon. Use this filter to customize the current
    report\'s sections and line items, or build new reports, as desired.

::: {.seealso}
\- `Accounting reporting <../accounting/reporting>`{.interpreted-text
role="doc"} - `../../essentials/search`{.interpreted-text role="doc"}
:::

### 1099 report {#l10n_us/1099-report}

The 1099 report, available by
`installing <general/install>`{.interpreted-text role="ref"} the *1099
Reporting* ([l10n\_us\_1099]{.title-ref}) module, includes payments that
are made to non-employees across a given reporting period. Use the
available CSV download from the report in Odoo to file 1099 payments
electronically via a third-party service.

To generate a 1099 report, navigate to
`Accounting app --> Reporting --> Management:
1099 Report`{.interpreted-text role="menuselection"} to open a
`1099 Report`{.interpreted-text role="guilabel"} wizard.

First, enter the date range of the transactions to report in the
`Start Date`{.interpreted-text role="guilabel"} and
`End Date`{.interpreted-text role="guilabel"} fields.

Then, edit the journal items that appear on the wizard. Click
`Add a line`{.interpreted-text role="guilabel"} to add any items that
are missing. Be sure to remove any items that should not be included in
the report by clicking `fa-times`{.interpreted-text role="icon"}
`(delete)`{.interpreted-text role="guilabel"} on the row.

Finally, once all necessary items are included in the 1099 report, click
on the `Generate`{.interpreted-text role="guilabel"} button. Doing so
downloads a CSV file that groups transactions by the partner that
received the payments.

### Cash flow statement {#l10n_us/cash-flow-statement}

Navigate to the *Cash Flow Statement* (CFS) dashboard by going to
`Accounting app -->
Reporting --> Statement Reports: Cash Flow Statement`{.interpreted-text
role="menuselection"}. From here,
`CFS (Cash Flow Statement)`{.interpreted-text role="abbr"} reports can
be generated using the various
`filters <l10n_us/report-filters>`{.interpreted-text role="ref"} that
are available at the top of the dashboard.

Odoo uses the *direct* cash flow method to compile cash flow statements,
which measures actual cash inflows and outflows from the company\'s
operations, such as when cash is received from customers or when cash
payments are made to suppliers.

By default, an account labeled with any of the three default
`Tags`{.interpreted-text role="guilabel"} on the
`Chart of Accounts`{.interpreted-text role="guilabel"} dashboard will be
included in the report, which includes:
`Operating Activities`{.interpreted-text role="guilabel"},
`Financing Activities`{.interpreted-text role="guilabel"}, and
`Investing &
Extraordinary Activities`{.interpreted-text role="guilabel"}.

{.align-center}

Additionally, the cash flow statement in Odoo:

-   is limited to the *Bank* and *Cash* journals to reflect money coming
    in or out; and
-   also contains *Expenses* accounts, to show the counterpart
    transactions versus *Bank* or *Cash* journal entries, while
    excluding `AR (Accounts Receivable)`{.interpreted-text role="abbr"}
    and `AP (Accounts Payable)`{.interpreted-text role="abbr"} activity.

::: {.example}
Create a vendor bill for \$100, as an operating expense (not
`AP (Accounts Payable)`{.interpreted-text role="abbr"}). Doing so will
**not** reflect a transaction on the cash flow statement. However,
register a corresponding payment for \$100, and the transaction **will**
reflect on the cash flow statement as `Cash paid for
operating activities`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Cash discount {#l10n_us/cash-discount}
-------------

Cash discounts can be configured from
`Accounting app --> Payment Terms`{.interpreted-text
role="menuselection"}. Each payment term can be set up with a cash
discount and reduced tax.

::: {.seealso}
`../accounting/customer_invoices/cash_discounts`{.interpreted-text
role="doc"}
:::

Writing checks {#l10n_us/writing-checks}
--------------

Using checks is still a common payment practice in the US. Be sure the
*US Checks Layout* ([l10n\_us\_check\_printing]{.title-ref}) module for
the US localization is `installed <general/install>`{.interpreted-text
role="ref"}.

To enable check printing from Odoo, navigate to
`Accounting --> Configuration -->
Settings`{.interpreted-text role="menuselection"} and find the
`Vendor Payments`{.interpreted-text role="guilabel"} section. From here,
tick the `Checks`{.interpreted-text role="guilabel"} checkbox to reveal
several fields for check configuration.

Select a `Check Layout`{.interpreted-text role="guilabel"} from the
drop-down menu:

-   `Print Check (Top) - US`{.interpreted-text role="guilabel"}
-   `Print Check (Middle) - US`{.interpreted-text role="guilabel"}
-   `Print Check (Bottom) - US`{.interpreted-text role="guilabel"}

Next, choose whether or not to enable the
`Multi-Pages Check Stub`{.interpreted-text role="guilabel"} checkbox.

Optionally set a `Check Top Margin`{.interpreted-text role="guilabel"}
and `Check Left Margin`{.interpreted-text role="guilabel"}, if required.

Once all check configurations are complete, `Save`{.interpreted-text
role="guilabel"} the settings.

::: {.tip}
::: {.title}
Tip
:::

Some of the check formats may require pre-printed paper from a third
party vendor, <https://checkdepot.net/collections/odoo-checks> is
recommended.
:::

::: {.seealso}
`../accounting/payments/pay_checks`{.interpreted-text role="doc"}
:::

Payroll {#l10n_us/payroll}
-------

The *Payroll* application is responsible for calculating an employee\'s
pay, taking into account all work, vacation, and sick time, benefits,
and deductions. The *Payroll* app pulls information from the
*Attendances*, *Timesheets*, *Time Off*, *Employees* and *Expenses*
applications, to calculate the worked hours and compensation for each
employee.

When using an external payroll provider, such as *ADP*, it is necessary
to export the various payroll-related data, such as work entries,
repayment of expenses, taxes, commissions, and any other relevant data,
so the data can be uploaded into the payroll provider, who then issues
the actual paychecks or directly deposits the funds into an employee\'s
bank account.

In order to export the payroll data, the work entries must first be
validated and correct. Refer to the
`work entries <../../hr/payroll/work_entries>`{.interpreted-text
role="doc"} documentation for more information regarding validating work
entries.

Once work entries are validated, the information can be
`exported to ADP <l10n_us/adp>`{.interpreted-text role="ref"}.

After payments have been issued to employees, payslips can be processed
into batches, validated, and posted to the corresponding accounting
journals to keep all financial records in Odoo current.

### Required information

It is important to have the *Employees* application installed, and all
employee information populated. Several fields in both the
`employee records <l10n_us/payroll-employee-records>`{.interpreted-text
role="ref"}, as well as in an
`employee contracts <l10n_us/payroll-employee-contracts>`{.interpreted-text
role="ref"}, are necessary to properly process the employee\'s pay.
Ensure the following fields are filled out in their respective places.

#### Employee records {#l10n_us/payroll-employee-records}

In each employee record, there is various information the *Payroll*
application requires to properly process payslips, including various
banking, tax, and work information.

Navigate to the `Employees app`{.interpreted-text role="menuselection"}
and select an employee record to view the sections of the employee form
that directly affect *Payroll*:

-   `Work Information`{.interpreted-text role="guilabel"} tab:
    -   `Work Address`{.interpreted-text role="guilabel"}: indicates
        where the employee is located, including the state, which
        affects the tax calculations.
    -   `Working Hours`{.interpreted-text role="guilabel"}: determines
        how pay is calculated, and determines if an employee earns
        overtime.
-   `Private Information`{.interpreted-text role="guilabel"} tab:
    -   `SSN No`{.interpreted-text role="guilabel"}: the last four
        digits of the employee\'s Social Security Number (SSN) appears
        on payslips.
    -   `Bank Account Number`{.interpreted-text role="guilabel"}: the
        bank account associated with the NACHA payment file.
-   `HR Settings`{.interpreted-text role="guilabel"} tab:
    -   `Federal Tax Filing Status`{.interpreted-text role="guilabel"}:
        the tax status an employee uses for Payroll tax calculations,
        which can be different from their state status.
    -   `State Tax Filing Status`{.interpreted-text role="guilabel"}:
        the tax status an employee uses for their state portion of the
        Payroll tax calculation.
    -   `W-2 Form`{.interpreted-text role="guilabel"}: a US tax form
        indicating the summary of wages, taxes, and benefits paid to an
        employee during a tax period (typically one year).
    -   `W-4 Form`{.interpreted-text role="guilabel"}: an IRS form that
        helps outline the amount of federal taxes to withhold for an
        employee, which is paid to the IRS by the company.

#### Employee contracts {#l10n_us/payroll-employee-contracts}

Additionally, there is information that is found in an employee contract
that also affects the *Payroll* application.

Navigate to the
`Employees app --> Employees --> Contracts`{.interpreted-text
role="menuselection"} and select a contract record to view the sections
of a contract that directly affect *Payroll*:

-   `General Information`{.interpreted-text role="guilabel"}:
    -   `Salary Structure Type: United States: Employee`{.interpreted-text
        role="guilabel"}: defines when the employee is paid, their
        working schedule, and the work entry type.
    -   `Work Entry source`{.interpreted-text role="guilabel"}:
        determines how work entries are calculated.
-   `Salary Information`{.interpreted-text role="guilabel"} tab:
    -   `SSN No`{.interpreted-text role="guilabel"}: the last four
        digits of the employee\'s Social Security Number (SSN) appears
        on payslips.
    -   `Wage type`{.interpreted-text role="guilabel"}: determines how
        the employee is paid, wether a Fixed wage (salary) or Hourly
        wage.
    -   `Schedule Pay`{.interpreted-text role="guilabel"}: defines how
        often the employee is paid, either `Annually`{.interpreted-text
        role="guilabel"}, `Semi-annually`{.interpreted-text
        role="guilabel"}, `Quarterly`{.interpreted-text
        role="guilabel"}, `Bi-monthly`{.interpreted-text
        role="guilabel"}, `Monthly`{.interpreted-text role="guilabel"},
        `Semi-monthly`{.interpreted-text role="guilabel"},
        `Bi-weekly`{.interpreted-text role="guilabel"},
        `Weekly`{.interpreted-text role="guilabel"}, or
        `Daily`{.interpreted-text role="guilabel"}. In the US,
        Semi-monthly (24 payments a year) or bi-weekly (26 payments a
        year) are the most common.
    -   `Wage, Yearly, and Monthly cost`{.interpreted-text
        role="guilabel"}: used to show the total cost of an employee. It
        is recommended to populate the `Yearly`{.interpreted-text
        role="guilabel"} wage first, as it auto-populates the other
        fields.
    -   `Pre-tax benefits`{.interpreted-text role="guilabel"}: populate
        this section according to the employee\'s selections. Pre-tax
        benefits decrease the gross wage, which lowers the base amount
        that is taxed. These are displayed at the beginning of the
        payslip.
    -   `Post-tax benefits`{.interpreted-text role="guilabel"}: these
        benefits are deductions made *after* taxes are calculated. These
        appear towards the end of the payslip before the net amount is
        displayed.

::: {.seealso}
`Employees documentation <../../hr/employees/new_employee>`{.interpreted-text
role="doc"}
:::

### Export work entries to ADP {#l10n_us/adp}

#### Requirements

In order to create a report that can be uploaded to ADP, there are some
initial configuration steps that must be completed first.

First, ensure the *United States - Payroll - Export to ADP*
([l10n\_us\_hr\_payroll\_adp]{.title-ref}) module is
`installed <general/install>`{.interpreted-text role="ref"}.

Then, the company **must** have an *ADP Code* entered in the company
settings. To do so, navigate to
`Payroll app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Enter the `ADP Code`{.interpreted-text
role="guilabel"} in the `US Localization`{.interpreted-text
role="guilabel"} section.

Next, work entry types **must** have the correct ADP code listed in the
*External Code* field for each work entry type that is being referenced.

Lastly, every employee **must** have an *ADP Code* entered on their
employee form. To do so, navigate to `Employees app`{.interpreted-text
role="menuselection"}, select an employee record, and open the `HR
Settings`{.interpreted-text role="guilabel"} tab. Enter the
`ADP Code`{.interpreted-text role="guilabel"} in the
`ADP Information`{.interpreted-text role="guilabel"} section.

The `ADP Code`{.interpreted-text role="guilabel"} code is how ADP
identifies that particular employee, and is typically a six-digit
number.

::: {.seealso}
\- `payroll/new-work-entry`{.interpreted-text role="ref"} -
`../../hr/employees/new_employee`{.interpreted-text role="doc"}
:::

#### Export data

Once `work entries <../../hr/payroll/work_entries>`{.interpreted-text
role="doc"} have been verified, the information can be exported to a CSV
file, which can then be uploaded into ADP.

To export the data, navigate to
`Payroll app --> Reporting --> United States: ADP
Export`{.interpreted-text role="menuselection"}, then click
`New`{.interpreted-text role="guilabel"}. Next, enter the
`Start Date`{.interpreted-text role="guilabel"} and
`End Date`{.interpreted-text role="guilabel"} for the work entries using
the calendar pop-over.

Then, enter a `Batch ID`{.interpreted-text role="guilabel"} in the
corresponding field. The recommendation for this field is to enter the
date in a [YY-MM-DD]{.title-ref} format, followed by any other
characters to distinguish that specific batch, such as a department
name, or any other defining characteristics for the batch.

Enter a `Batch Description`{.interpreted-text role="guilabel"} in the
corresponding field. This should be short and descriptive, but distinct
from the `Batch Name`{.interpreted-text role="guilabel"}.

Ensure the correct company populates the `Company`{.interpreted-text
role="guilabel"} field. Change the selected company with the drop-down
menu, if needed.

Lastly, add the employee\'s work entry information to the list. Click
`Add a line`{.interpreted-text role="guilabel"} and an
`Add: Employee`{.interpreted-text role="guilabel"} pop-up window loads.
The list can be `filtered
<../../essentials/search>`{.interpreted-text role="doc"} to more easily
find the employees to add to the list.

::: {.tip}
::: {.title}
Tip
:::

Process the data export in multiple groups instead of in one large group
that contains all employees. This helps to meaningfully differentiate
the batches and makes processing more tenable, overall. The most common
ways to group employees is by department, or by wage type (hourly or
salaried).
:::

Select the employees to add to the list by ticking the box to the left
of their name. Once all desired employees have been selected, click the
`Select`{.interpreted-text role="guilabel"} button in the lower-left
corner, and the employees appear in the list.

To create the CSV file, click the `Generate`{.interpreted-text
role="guilabel"} button in the top-left corner.

ACH - electronic transfers {#l10n_us/ach-electronic-transfers}
--------------------------

Automated Clearing House (ACH) payments are a modern way to transfer
funds electronically between bank accounts, replacing traditional
paper-based methods. `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} payments are commonly used for direct deposits, bill
payments, and business transactions.

### Receive ACH payments: payment provider integration

`ACH (Automated Clearing House)`{.interpreted-text role="abbr"} payments
are supported by *Authorize.net* and *Stripe* payment integrations in
Odoo.

::: {.seealso}
\-
`Setting up Authorize.net for ACH payments (Odoo) <authorize/ach_payments>`{.interpreted-text
role="ref"} - [Authorize.net\'s ACH payment processing for small
businesses
documentation](https://www.authorize.net/resources/blog/2021/ach-payments-for-small-businesses.html)
-
`Setting up Stripe for ACH payments (Odoo) <../payment_providers/stripe>`{.interpreted-text
role="doc"} - [Stripe\'s ACH Direct Debit
documentation](https://docs.stripe.com/payments/ach-debit)
:::

### Send payments: NACHA files {#l10n_us/nacha}

Odoo can generate a National Automated Clearing House Association
(NACHA) compatible `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} file to send to a company\'s bank. For each individual
*Bank* journal that the company wishes to pay vendors with, a
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} configuration section needs to be filled out on the Odoo
database.

#### Configuration

First, navigate to the
`Accounting app --> Configuration --> Journals`{.interpreted-text
role="menuselection"}. Open the bank journal and click into the
`Outgoing Payments`{.interpreted-text role="guilabel"} tab.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The following
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} configuration information is normally provided by the
company\'s financial institution once they have been approved to send
payments via their account.
:::

Under the section labeled, `NACHA configuration`{.interpreted-text
role="guilabel"} are the fields required to generate a
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} compatible
`ACH (Automated Clearing House)`{.interpreted-text role="abbr"} file to
send to a company\'s bank. First, enter the routing number of the
financial institution in the field labeled,
`Immediate Destination`{.interpreted-text role="guilabel"}. This
information is widely available on the Internet and generally varies by
bank location. This number is usually provided during the initial
account setup.

Next, enter the registered name of the financial institution in the
field called, `Destination`{.interpreted-text role="guilabel"}. This
information will be provided by the bank or credit union.

Following the `Destination`{.interpreted-text role="guilabel"} field is
the `Immediate Origin`{.interpreted-text role="guilabel"} field. Enter
the 9-digit company ID or Employer Identification Number (EIN) into this
field. This information is provided by the financial institution.

Next, enter the `Company Identification`{.interpreted-text
role="guilabel"} number, which is a 10-digit number made from combining
the 9-digit company ID or Employer Identification Number (EIN), along
with an additional number at the start of the sequence. This number is
often a [1]{.title-ref}. Check with the financial institution should
this first number differ to verify that it is correct, as this number is
provided for `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} approved accounts.

Enter the `Originating DFI Identification`{.interpreted-text
role="guilabel"} number next, which should contain an assigned 8-digit
number from the financial institution.

::: {.important}
::: {.title}
Important
:::

Enter the numerical values in this section *exactly* as the company\'s
financial institution (e.g. bank or credit union) has provided them,
otherwise risk failing a successful
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} configuration in Odoo.
:::

{.align-center}

There are two options for the next field:
`Standard Entry Class Code`{.interpreted-text role="guilabel"}. Select
the drop-down menu to the right of the field and pick either
`Corporate Credit or Debit (CCD)`{.interpreted-text role="guilabel"} or
`Prearranged Payment and Deposit (PPD)`{.interpreted-text
role="guilabel"}. Again, this information will be provided by the
financial institution. By default
`Corporate Credit or Debit (CCD)`{.interpreted-text role="guilabel"} is
selected.

Finally, the last option is for
`Generated Balanced Files`{.interpreted-text role="guilabel"}. Tick the
checkbox to the right of the field to enable
`Generated Balanced Files`{.interpreted-text role="guilabel"}. Consult
the company\'s accountant or financial advisor to make an informed
decision for this field.

Manually save the configuration by clicking the
`fa-cloud-upload`{.interpreted-text role="icon"}
`(cloud upload)`{.interpreted-text role="guilabel"} icon, or navigate
away from this screen to auto-save. The configuration is now complete.

#### Create batch payment {#l10n_us/batch-payment}

Now, record each payment in Odoo using the
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} payment method.

::: {.seealso}
`Register Payments in Odoo <accounting/payments/from-invoice-bill>`{.interpreted-text
role="ref"}
:::

::: {.important}
::: {.title}
Important
:::

Be aware of the cut-off time for same-day payments. Either the file
needs to have a future date associated with each payment or the file
needs to be sent prior to the cut-off, if the dates included in it match
today\'s date. Consult the financial institution for the exact cut-off
time for their processing of same-day payments.
:::

Once all the payments to be included in the
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} file have been made, a batch payment needs to be made from
the `fa-cog`{.interpreted-text role="icon"} `Action`{.interpreted-text
role="guilabel"} menu.

To create the batch payments, access the payments page, by navigating to
`Accounting
--> Vendors --> Payments`{.interpreted-text role="menuselection"}.
Select all the payments that should be included in the
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} file, by ticking the checkboxes to the far-left of the
rows.

![On the payments screen, the action menu is highlighted with create a batch payment
selected.](united_states/us-l10n-create-batch-payments.png){.align-center}

::: {.important}
::: {.title}
Important
:::

All payments in the batch **must** share the same
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} payment method.
:::

Next, navigate to the batched payment
(`Accounting --> Vendors --> Batch Payments`{.interpreted-text
role="menuselection"}). Click into the payment just created and then
click into the `Exported File`{.interpreted-text role="guilabel"} tab.
The generated file is listed with the
`Generation Date`{.interpreted-text role="guilabel"}. Click the
`fa-download`{.interpreted-text role="icon"}
`(download)`{.interpreted-text role="guilabel"} button to download the
file.

{.align-center}

If any adjustments need to be made, click the
`Re-generate Export File`{.interpreted-text role="guilabel"} button to
recreate a new
`NACHA (National Automated Clearing House Association)`{.interpreted-text
role="abbr"} `ACH (Automated Clearing House)`{.interpreted-text
role="abbr"} file.

::: {.seealso}
\- `../accounting/payments/batch`{.interpreted-text role="doc"} -
`Europe's direct debiting <../accounting/payments/batch_sdd>`{.interpreted-text
role="doc"}
:::
