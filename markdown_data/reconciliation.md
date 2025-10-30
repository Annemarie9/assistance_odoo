# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/bank/reconciliation.md

Bank reconciliation
===================

**Bank reconciliation** is the process of matching your
`bank transactions <transactions>`{.interpreted-text role="doc"} with
your business records, such as
`customer invoices <../customer_invoices>`{.interpreted-text
role="doc"}, `vendor bills
<../vendor_bills>`{.interpreted-text role="doc"}, and
`payments <../payments>`{.interpreted-text role="doc"}. Not only is this
compulsory for most businesses, but it also offers several benefits,
such as reduced risk of errors in financial reports, detection of
fraudulent activities, and improved cash flow management.

Thanks to the bank
`reconciliation models <reconciliation_models>`{.interpreted-text
role="doc"}, Odoo pre-selects the matching entries automatically.

::: {.seealso}
\- [Odoo Tutorials: Bank
reconciliation](https://www.odoo.com/slides/slide/bank-reconciliation-6562)
- `bank_synchronization`{.interpreted-text role="doc"} -
`transactions`{.interpreted-text role="doc"}
:::

Bank reconciliation view {#accounting/reconciliation/access}
------------------------

To access a bank journal\'s **reconciliation view**, go to your
`Accounting Dashboard`{.interpreted-text role="guilabel"} and either:

-   click the journal name (e.g., `Bank`{.interpreted-text
    role="guilabel"}) to display all transactions, including those
    previously reconciled or
-   click the `Reconcile items`{.interpreted-text role="guilabel"}
    button to display all transactions Odoo pre-selected for
    reconciliation. You can remove the `Not Matched`{.interpreted-text
    role="guilabel"} filter from the search bar to include previously
    reconciled transactions.



The bank reconciliation view is structured into three distinct sections:
transactions, counterpart entries, and resulting entry.



Transactions

:   The transactions section on the left shows all bank transactions,
    with the newest displayed first. Click a transaction to select it.

Counterpart entries

:   The counterpart entries section on the bottom right displays the
    options to match the selected bank transaction. Multiple tabs are
    available, including
    `reconciliation/existing-entries`{.interpreted-text role="ref"},
    `reconciliation/batch-payments`{.interpreted-text role="ref"},
    `reconciliation/manual-operations`{.interpreted-text role="ref"},
    and `Discuss`{.interpreted-text role="guilabel"}, which contains the
    chatter for the selected bank transaction.

Resulting entry

:   The resulting entry section on the top right displays the selected
    bank transaction matched with the counterpart entries and includes
    any remaining debits or credits. In this section, you can validate
    the reconciliation or mark it as `To Check`{.interpreted-text
    role="guilabel"}. Any `reconciliation model
    buttons <reconciliation/button>`{.interpreted-text role="ref"} are
    also available in the resulting entry section.

Reconcile transactions {#accounting/reconciliation/reconcile}
----------------------

Transactions can be matched automatically with the use of
`reconciliation models
<reconciliation_models>`{.interpreted-text role="doc"}, or they can be
matched with `existing entries
<reconciliation/existing-entries>`{.interpreted-text role="ref"},
`batch payments <reconciliation/batch-payments>`{.interpreted-text
role="ref"},
`manual operations <reconciliation/manual-operations>`{.interpreted-text
role="ref"}, and `reconciliation model buttons
<reconciliation/button>`{.interpreted-text role="ref"}.

1.  Select a transaction among unmatched bank transactions.
2.  Define the counterpart. There are several options for defining a
    counterpart, including
    `matching existing entries <reconciliation/existing-entries>`{.interpreted-text
    role="ref"}, `manual operations
    <reconciliation/manual-operations>`{.interpreted-text role="ref"},
    `batch payments <reconciliation/batch-payments>`{.interpreted-text
    role="ref"}, and
    `reconciliation model buttons <reconciliation/button>`{.interpreted-text
    role="ref"}.
3.  If the resulting entry is not fully balanced, balance it by adding
    another existing counterpart entry or writing it off with a
    `manual operation <reconciliation/manual-operations>`{.interpreted-text
    role="ref"}.
4.  Click the `Validate`{.interpreted-text role="guilabel"} button to
    confirm the reconciliation and move to the next transaction.

::: {.tip}
::: {.title}
Tip
:::

If you are not sure how to reconcile a particular transaction and would
like to deal with it later, use the `To Check`{.interpreted-text
role="guilabel"} button instead. All transactions marked as `To
Check`{.interpreted-text role="guilabel"} can be displayed using the
`To Check`{.interpreted-text role="guilabel"} filter.
:::

::: {.note}
::: {.title}
Note
:::

Bank transactions are posted on the **journal\'s suspense account**
until reconciliation. At this point, reconciliation modifies the
transaction journal entry by replacing the bank suspense account with
the corresponding receivable, payable, or outstanding account.
:::

### Match existing entries {#reconciliation/existing-entries}

This tab contains matching entries Odoo automatically pre-selects
according to the reconciliation models. The entry order is based on
`reconciliation models <reconciliation_models>`{.interpreted-text
role="doc"}, with suggested entries appearing first.

::: {.tip}
::: {.title}
Tip
:::

The search bar within the `Match Existing Entries`{.interpreted-text
role="guilabel"} tab allows you to search for specific journal items.
:::

### Batch payments {#reconciliation/batch-payments}

`Batch payments <../payments/batch>`{.interpreted-text role="doc"} allow
you to group different payments to ease reconciliation. Use the
`Batch Payments`{.interpreted-text role="guilabel"} tab to find batch
payments for customers and vendors. Similarly to the
`Match Existing Entries`{.interpreted-text role="guilabel"} tab, the
`Batch Payments`{.interpreted-text role="guilabel"} tab has a search bar
that allows you to search for specific batch payments.

### Manual operations {#reconciliation/manual-operations}

If there is not an existing entry to match the selected transaction, you
may instead wish to reconcile the transaction manually by choosing the
correct account and amount. Then, complete any of the relevant optional
fields.

::: {.tip}
::: {.title}
Tip
:::

You can use the `fully paid`{.interpreted-text role="guilabel"} option
to reconcile a payment, even in cases where only a partial payment is
received. A new line appears in the resulting entry section to reflect
the open balance registered on the Account Receivable by default. You
can choose another account by clicking on the new line in the resulting
entry section and selecting the `Account`{.interpreted-text
role="guilabel"} to record the open balance.
:::

::: {.note}
::: {.title}
Note
:::

Lines are silently reconciled unless a write-off entry is required,
which launches a reconciliation wizard.


:::

### Reconciliation model buttons {#reconciliation/button}

Use a `reconciliation model <reconciliation_models>`{.interpreted-text
role="doc"} button for manual operations that are frequently used. These
custom buttons allow you to quickly reconcile bank transactions manually
and can also be used in combination with existing entries.
