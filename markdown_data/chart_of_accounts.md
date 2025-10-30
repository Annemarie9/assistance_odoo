# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/get_started/chart_of_accounts.md

Chart of accounts
=================

The **chart of accounts (COA)** is the list of all the accounts used to
record financial transactions in the general ledger of an organization.
The chart of accounts can be found under
`Accounting --> Configuration --> Chart of Accounts`{.interpreted-text
role="menuselection"}.

When browsing your chart of accounts, you can sort the accounts by
`Code`{.interpreted-text role="guilabel"},
`Account Name`{.interpreted-text role="guilabel"}, or
`Type`{.interpreted-text role="guilabel"}, but other options are
available in the drop-down menu





Configuration of an account {#chart-of-account/create}
---------------------------

The country you select during the creation of your database (or
additional company in your database) determines which
`fiscal localization package <../../fiscal_localizations>`{.interpreted-text
role="doc"} is installed by default. This package includes a standard
chart of accounts already configured according to the country\'s
regulations. You can use it directly or set it according to your
company\'s needs.

To create a new account, go to
`Accounting --> Configuration --> Chart of Accounts`{.interpreted-text
role="menuselection"}, click `Create`{.interpreted-text
role="guilabel"}, and fill in (at the minimum) the required fields
(`Code, Account Name, Type`{.interpreted-text role="guilabel"}).

::: {.warning}
::: {.title}
Warning
:::

It is not possible to modify the **fiscal localization** of a company
once a journal entry has been posted.
:::

### Code and name

Each account is identified by its `Code`{.interpreted-text
role="guilabel"} and `Name`{.interpreted-text role="guilabel"}, which
also indicate the account\'s purpose.

### Type {#chart-of-account/type}

Correctly configuring the **account type** is critical as it serves
multiple purposes:

-   Information on the account\'s purpose and behavior
-   Generate country-specific legal and financial reports
-   Set the rules to close a fiscal year
-   Generate opening entries

To configure an account type, open the `Type`{.interpreted-text
role="guilabel"} field\'s drop-down selector and select the
corresponding type from the following list:

+---------------+--------------+-------------------------+
| Report        | Category     | Account Types           |
+===============+==============+=========================+
| Balance Sheet | > Assets     | > Receivable            |
|               | >            |                         |
| > -           | > :   -      | \-\-                    |
| > -           | >     -      | \-\-\-\-\-\-\-\-\-\-\-\ |
|               | >     -      | -\-\-\-\-\-\-\-\-\-\--+ |
|               | >     -      |                         |
|               | >     -      | :   Bank and Cash       |
|               |              |                         |
|               | \-\-         | \-\-                    |
|               | \-\-\-\-\-\- | \-\-\-\-\-\-\-\-\-\-\-\ |
|               | \-\-\-\-\--+ | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               | :            | :   Current Assets      |
|               |              |                         |
|               |              | \-\-                    |
|               |  Liabilities | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |     :   -    |                         |
|               |         -    | :   Non-current Assets  |
|               |         -    |                         |
|               |              | \-\-                    |
|               | \-\-         | \-\-\-\-\-\-\-\-\-\-\-\ |
|               | \-\-\-\-\-\- | -\-\-\-\-\-\-\-\-\-\--+ |
|               | \-\-\-\-\--+ |                         |
|               |              | :   Prepayments         |
|               | :            |                         |
|               |              | \-\-                    |
|               |     Equity   | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |     :   -    |                         |
|               |              | :   Fixed Assets        |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Payable             |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Credit Card         |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Current Liabilities |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Non-current         |
|               |              |     Liabilities         |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Equity              |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Current Year        |
|               |              |     Earnings            |
+---------------+--------------+-------------------------+
| Profit & Loss | > Income     | > Income                |
|               | >            |                         |
| > -           | > :   -      | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               | \-\-         | -\-\-\-\-\-\-\-\-\-\--+ |
|               | \-\-\-\-\-\- |                         |
|               | \-\-\-\-\--+ | :   Other Income        |
|               |              |                         |
|               | :            | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |     Expense  | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |     :   -    | :   Expense             |
|               |         -    |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Depreciation        |
|               |              |                         |
|               |              | \-\-                    |
|               |              | \-\-\-\-\-\-\-\-\-\-\-\ |
|               |              | -\-\-\-\-\-\-\-\-\-\--+ |
|               |              |                         |
|               |              | :   Cost of Revenue     |
+---------------+--------------+-------------------------+
| Other         | Other        | Off-Balance Sheet       |
+---------------+--------------+-------------------------+

#### Assets

Some **account types** can **automate** the creation of
`asset <assets-automation>`{.interpreted-text role="ref"} entries. To
**automate** entries, click `View`{.interpreted-text role="guilabel"} on
an account line and go to the `Automation`{.interpreted-text
role="guilabel"} tab.

You have three choices for the `Automation`{.interpreted-text
role="guilabel"} tab:

1.  `No`{.interpreted-text role="guilabel"}: this is the default value.
    Nothing happens.
2.  `Create in draft`{.interpreted-text role="guilabel"}: whenever a
    transaction is posted on the account, a draft entry is created but
    not validated. You must first fill out the corresponding form.
3.  `Create and validate`{.interpreted-text role="guilabel"}: you must
    also select a `Deferred Expense Model`{.interpreted-text
    role="guilabel"}. Whenever a transaction is posted on the account,
    an entry is created and immediately validated.

### Default taxes

In the `View`{.interpreted-text role="guilabel"} menu of an account,
select a **default tax** to be applied when this account is chosen for a
product sale or purchase.

### Tags

Some accounting reports require **tags** to be set on the relevant
accounts. To add a tag, under `View`{.interpreted-text role="guilabel"},
click the `Tags`{.interpreted-text role="guilabel"} field and select an
existing tag or `Create`{.interpreted-text role="guilabel"} a new one.

### Account groups

**Account groups** are useful to list multiple accounts as
*sub-accounts* of a bigger account and thus consolidate reports such as
the **Trial Balance**. By default, groups are handled automatically
based on the code of the group. For example, a new account
[131200]{.title-ref} is going to be part of the group
[131000]{.title-ref}. You can attribute a specific group to an account
in the `Group`{.interpreted-text role="guilabel"} field under
`View`{.interpreted-text role="guilabel"}.

#### Create account groups manually

::: {.note}
::: {.title}
Note
:::

Regular users should not need to create account groups manually. The
following section is only intended for rare and advanced use cases.
:::

To create a new account group, activate
`developer mode <developer-mode>`{.interpreted-text role="ref"} and head
to `Accounting --> Configuration --> Account Groups`{.interpreted-text
role="menuselection"}. Here, create a new group and enter the
`name, code prefix, and company`{.interpreted-text role="guilabel"} to
which that group account should be available. Note that you must enter
the same code prefix in both `From`{.interpreted-text role="guilabel"}
and `to`{.interpreted-text role="guilabel"} fields.



To display your **Trial Balance** report with your account groups, go to
`Accounting --> Reporting --> Trial Balance`{.interpreted-text
role="menuselection"}, then open the `Options`{.interpreted-text
role="guilabel"} menu and select
`Hierarchy and Subtotals`{.interpreted-text role="guilabel"}.



### Allow reconciliation

Some accounts, such as accounts made to record the transactions of a
payment method, can be used for the reconciliation of journal entries.

For example, an invoice paid with a credit card can be marked as
`paid`{.interpreted-text role="guilabel"} if reconciled with its
payment. Therefore, the account used to record credit card payments
needs to be configured as **allowing reconciliation**.

To do so, check the `Allow Reconciliation`{.interpreted-text
role="guilabel"} box in the account\'s settings, and
`Save`{.interpreted-text role="guilabel"}; or enable the button from the
chart of accounts view.



### Deprecated

It is not possible to delete an account once a transaction has been
recorded on it. You can make them unusable by using the **Deprecated**
feature: check the `Deprecated`{.interpreted-text role="guilabel"} box
in the account\'s settings, and `Save`{.interpreted-text
role="guilabel"}.

::: {.seealso}
\* `cheat_sheet`{.interpreted-text role="doc"} \*
`../vendor_bills/assets`{.interpreted-text role="doc"} \*
`../vendor_bills/deferred_expenses`{.interpreted-text role="doc"} \*
`../customer_invoices/deferred_revenues`{.interpreted-text role="doc"}
\* `../../fiscal_localizations`{.interpreted-text role="doc"} \* [Odoo
Tutorials: Chart of
accounts](https://www.odoo.com/slides/slide/chart-of-accounts-6834) \*
[Odoo Tutorials: Update your chart of
accounts](https://www.odoo.com/slides/slide/update-your-chart-of-accounts-6391)
:::
