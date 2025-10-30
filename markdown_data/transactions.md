# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/bank/transactions.md

Transactions
============

Importing transactions from your bank statements allows keeping track of
bank account transactions and reconciling them with the ones recorded in
your accounting.

`Bank synchronization <bank_synchronization>`{.interpreted-text
role="doc"} automates the process. However, if you do not want to use it
or if your bank is not yet supported, other options exist:

-   `Import bank transactions <transactions/import>`{.interpreted-text
    role="ref"} delivered by your bank;
-   `Register bank transactions <transactions/register>`{.interpreted-text
    role="ref"} manually.

::: {.note}
::: {.title}
Note
:::

`Grouping transactions by statement <transactions/statements>`{.interpreted-text
role="ref"} is optional.
:::

Import transactions {#transactions/import}
-------------------

Odoo supports multiple file formats to import transactions:

-   SEPA recommended Cash Management format (CAMT.053)
-   Comma-separated values (CSV)
-   Open Financial Exchange (OFX)
-   Quicken Interchange Format (QIF)
-   Belgium: Coded Statement of Account (CODA)

To import a file, go to the `Accounting Dashboard`{.interpreted-text
role="guilabel"}, and in the `Bank`{.interpreted-text role="guilabel"}
journal, click on `Import File`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Alternatively, you can also:

-   click the `fa-ellipsis-v`{.interpreted-text role="icon"}
    `(ellipsis)`{.interpreted-text role="guilabel"} icon on the
    `Bank`{.interpreted-text role="guilabel"} journal and select
    `Import file`{.interpreted-text role="guilabel"};
-   or access the transaction list by clicking the
    `fa-ellipsis-v`{.interpreted-text role="icon"}
    `(ellipsis)`{.interpreted-text role="guilabel"} icon on the
    `Bank`{.interpreted-text role="guilabel"} journal and selecting
    `Transactions`{.interpreted-text role="guilabel"}, then click the
    `fa-cog`{.interpreted-text role="icon"} `(gear)`{.interpreted-text
    role="guilabel"} icon and select `Import records`{.interpreted-text
    role="guilabel"}.
:::

Next, select the file and upload it.

After setting the necessary formatting options and mapping the file
columns with their related Odoo fields, you can run a
`Test`{.interpreted-text role="guilabel"} and `Import`{.interpreted-text
role="guilabel"} your bank transactions.

::: {.seealso}
`/applications/essentials/export_import_data`{.interpreted-text
role="doc"}
:::

Register bank transactions manually {#transactions/register}
-----------------------------------

You can also record your bank transactions manually. To do so, go to
`Accounting
Dashboard`{.interpreted-text role="guilabel"}, click on the
`Bank`{.interpreted-text role="guilabel"} journal, and then on
`New`{.interpreted-text role="guilabel"}. Make sure to fill out the
`Partner`{.interpreted-text role="guilabel"} and
`Label`{.interpreted-text role="guilabel"} fields to ease the
reconciliation process.

Statements {#transactions/statements}
----------

A **bank statement** is a document provided by a bank or financial
institution that lists the transactions that have occurred in a
particular bank account over a specified period of time.

In Odoo Accounting, it is optional to group transactions by their
related statement, but depending on your business flow, you may want to
record them for control purposes.

::: {.important}
::: {.title}
Important
:::

If you want to compare the ending balances of your bank statements with
the ending balances of your financial records, *don\'t forget to create
an opening transaction* to record the bank account balance as of the
date you begin synchronizing or importing transactions. This is
necessary to ensure the accuracy of your accounting.
:::

To access a list of existing statements, go to the
`Accounting Dashboard`{.interpreted-text role="guilabel"}, click the
`fa-ellipsis-v`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} icon next to the bank or
cash journal you want to check, then click
`Statements`{.interpreted-text role="guilabel"}.

### Statement creation from the kanban view {#transactions/statement-kanban}

Open the bank reconciliation (kanban) view from the
`Accounting Dashboard`{.interpreted-text role="guilabel"} by clicking on
the name of the bank journal and identify the transaction corresponding
to the last (most recent) transaction of your bank statement. Click on
the `Statement`{.interpreted-text role="guilabel"} button when hovering
on the upper separator line to create a statement from that transaction
down to the oldest transaction that is not yet part of a statement.



In the `Create Statement`{.interpreted-text role="guilabel"} window,
fill out the statement\'s `Reference`{.interpreted-text
role="guilabel"}, verify its `Starting Balance`{.interpreted-text
role="guilabel"} and `Ending Balance`{.interpreted-text
role="guilabel"}, and click `Save`{.interpreted-text role="guilabel"}.

### Statement creation from the list view {#transactions/statement-list}

Open the list of transactions by clicking on the name of the bank
journal and switching to the list view. Select all the transactions
corresponding to the bank statement, and, in the
`Statement`{.interpreted-text role="guilabel"} column, select an
existing statement or create a new one by typing its reference, clicking
on `Create and edit...`{.interpreted-text role="guilabel"}, filling out
the statement\'s details, and saving.

### Statement viewing, editing, and printing {#transactions/view-edit-print}

To view an existing statement, click on the statement amount in the
reconciliation (kanban) view or click on the statement name in the bank
transaction list view. From here, you can edit the
`Reference`{.interpreted-text role="guilabel"},
`Starting Balance`{.interpreted-text role="guilabel"}, or
`Ending Balance`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Manually updating the `Starting Balance`{.interpreted-text
role="guilabel"} automatically updates the `Ending
Balance`{.interpreted-text role="guilabel"} based on the new value of
the `Starting Balance`{.interpreted-text role="guilabel"} and the value
of the statement\'s transactions.
:::

::: {.warning}
::: {.title}
Warning
:::

If the `Starting Balance`{.interpreted-text role="guilabel"} doesn\'t
equal the previous statement\'s `Ending
Balance`{.interpreted-text role="guilabel"}, or if the
`Ending Balance`{.interpreted-text role="guilabel"} doesn\'t equal the
running balance (`Starting Balance`{.interpreted-text role="guilabel"}
plus the statement\'s transactions), a warning appears explaining the
issue. To maintain flexibility, it is still possible to save without
first resolving the issue.
:::

To attach a digital copy (i.e., JPEG, PNG, or PDF) of the bank statement
for enhanced recordkeeping, click the `fa-paperclip`{.interpreted-text
role="icon"} `Attachments`{.interpreted-text role="guilabel"} button and
select the file to attach.

To generate and print a PDF of the bank statement, click the
`Print`{.interpreted-text role="guilabel"} button (if accessed via the
reconciliation view) or click on the `fa-cog`{.interpreted-text
role="icon"}`(gear)`{.interpreted-text role="guilabel"} icon and click
`fa-print`{.interpreted-text role="icon"}`Statement`{.interpreted-text
role="guilabel"} (if accessed via the list view).

::: {.note}
::: {.title}
Note
:::

When a bank statement is generated to be printed, it is automatically
added to the `Attachments`{.interpreted-text role="guilabel"}.
:::
