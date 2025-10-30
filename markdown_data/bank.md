# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/bank.md

show-content

:   

Bank and cash accounts
======================

You can manage as many bank or cash accounts as needed on your database.
Configuring them well allows you to have all your banking data
up-to-date and ready for `reconciliation
<bank/reconciliation>`{.interpreted-text role="doc"} with your journal
entries.

In Odoo Accounting, each bank account has a dedicated journal set to
post all entries in a dedicated account. Both the journal and the
account are automatically created and configured whenever you add a bank
account.

::: {.note}
::: {.title}
Note
:::

Cash journals and accounts must be configured manually.
:::

Bank journals are displayed by default on the
`Accounting Dashboard`{.interpreted-text role="guilabel"} in the form of
cards which include action buttons.



Manage your bank and cash accounts {#bank_accounts/manage}
----------------------------------

### Connect your bank for automatic synchronization

To connect your bank account to your database, go to
`Accounting --> Configuration
--> Banks: Add a Bank Account`{.interpreted-text role="menuselection"},
select your bank in the list, click on `Connect`{.interpreted-text
role="guilabel"}, and follow the instructions.

::: {.seealso}
`bank/bank_synchronization`{.interpreted-text role="doc"}
:::

### Create a bank account {#bank_accounts/create}

If your banking institution is not available in Odoo, or if you don\'t
want to connect your bank account to your database, you can configure
your bank account manually.

To manually add a bank account, go to
`Accounting --> Configuration --> Banks:
Add a Bank Account`{.interpreted-text role="menuselection"}, click on
`Create it`{.interpreted-text role="guilabel"} (at the bottom right),
and fill out the form.

::: {.note}
::: {.title}
Note
:::

\- Odoo automatically detects the bank account type (e.g., IBAN) and
enables some features accordingly. - A default bank journal is available
and can be used to configure your bank account by going to
`Accounting --> Configuration --> Accounting: Journals --> Bank`{.interpreted-text
role="menuselection"}. Open it and edit the different fields to match
your bank account information.
:::

### Create a cash journal

To create a new cash journal, go to
`Accounting --> Configuration --> Accounting:
Journals`{.interpreted-text role="menuselection"}, click on
`Create`{.interpreted-text role="guilabel"} and select
`Cash`{.interpreted-text role="guilabel"} in the
`Type`{.interpreted-text role="guilabel"} field.

For more information on the accounting information fields, read the
`bank_accounts/configuration`{.interpreted-text role="ref"} section of
this page.

::: {.note}
::: {.title}
Note
:::

A default cash journal is available and can be used straight away. You
can review it by going to
`Accounting --> Configuration --> Accounting: Journals --> Cash`{.interpreted-text
role="menuselection"}.
:::

### Edit an existing bank or cash journal

To edit an existing bank journal, go to
`Accounting --> Configuration --> Accounting:
Journals`{.interpreted-text role="menuselection"} and select the journal
you want to modify.

Configuration {#bank_accounts/configuration}
-------------

You can edit the accounting information and bank account number
according to your needs.



::: {.seealso}
\- `get_started/multi_currency`{.interpreted-text role="doc"} -
`bank/transactions`{.interpreted-text role="doc"}
:::

### Suspense account {#bank_accounts/suspense}

Bank statement transactions are posted on the
`Suspense Account`{.interpreted-text role="guilabel"} until the final
reconciliation allows finding the right account.

### Profit and loss accounts

The `Profit Account`{.interpreted-text role="guilabel"} is used to
register a profit when the ending balance of a cash register differs
from what the system computes, while the
`Loss Account`{.interpreted-text role="guilabel"} is used to register a
loss when the ending balance of a cash register differs from what the
system computes.

### Currency

You can edit the currency used to enter the statements.

::: {.seealso}
`get_started/multi_currency`{.interpreted-text role="doc"}
:::

### Account number {#accounting/bank/account-number}

If you need to **edit your bank account details**, click on the external
link arrow next to your `Account Number`{.interpreted-text
role="guilabel"}. On the new page, click on the external link arrow next
to your `Bank`{.interpreted-text role="guilabel"} and update your bank
information accordingly. These details are used when registering
payments.



### Bank feeds

`Bank Feeds`{.interpreted-text role="guilabel"} defines how the bank
statements are registered. Three options are available:

-   `Undefined yet`{.interpreted-text role="guilabel"}, which should be
    selected when you don't know yet if you will synchronize your bank
    account with your database or not.
-   `Import (CAMT, CODA, CSV, OFX, QIF)`{.interpreted-text
    role="guilabel"}, which should be selected if you want to import
    your bank statement using a different format.
-   `Automated Bank Synchronization`{.interpreted-text role="guilabel"},
    which should be selected if your bank is synchronized with your
    database.

::: {.seealso}
\- `bank/bank_synchronization`{.interpreted-text role="doc"} -
`bank/transactions`{.interpreted-text role="doc"}
:::

Outstanding accounts {#bank/outstanding-accounts}
--------------------

By default, payments are registered through transitory accounts named
**outstanding accounts**, before being recorded in your bank account.

-   An **outstanding payments account** is where outgoing payments are
    posted until they are linked with a withdrawal from your bank
    statement.
-   An **outstanding receipts account** is where incoming payments are
    posted until they are linked with a deposit from your bank
    statement.

These accounts should be of
`type <chart-of-account/type>`{.interpreted-text role="ref"}
`Current Assets`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The movement from an outstanding account to a bank account is done
automatically when you reconcile the bank account with a bank statement.
:::

### Default accounts configuration

The outstanding accounts are defined by default. If necessary, you can
update them by going to
`Accounting --> Configuration --> Settings --> Default Accounts`{.interpreted-text
role="menuselection"} and update your
`Outstanding Receipts Account`{.interpreted-text role="guilabel"} and
`Outstanding Payments Account`{.interpreted-text role="guilabel"}.

### Bank and cash journals configuration

You can also set specific outstanding accounts for any journal with the
`type
<chart-of-account/type>`{.interpreted-text role="ref"}
`Bank`{.interpreted-text role="guilabel"} or `Cash`{.interpreted-text
role="guilabel"}.

From your `Accounting Dashboard`{.interpreted-text role="guilabel"},
click on the menu selection ⋮ of the journal you want to configure, and
click on `Configuration`{.interpreted-text role="guilabel"}, then open
the `Incoming/Outgoing
Payments`{.interpreted-text role="guilabel"} tab. To display the
outstanding accounts column, click on the toggle button and check the
`Outstanding Receipts/Payments accounts`{.interpreted-text
role="guilabel"}, then update the account.

{.align-center}

::: {.note}
::: {.title}
Note
:::

\- If you do not specify an outstanding payments account or an
outstanding receipts account for a specific journal, Odoo uses the
default outstanding accounts. - If your main bank account is added as an
outstanding receipts account or outstanding payments account, when a
payment is registered, the invoice or bill\'s status is directly set to
`Paid`{.interpreted-text role="guilabel"}.
:::

::: {.toctree titlesonly=""}
bank/bank\_synchronization bank/transactions bank/reconciliation
bank/reconciliation\_models bank/foreign\_currency
:::
