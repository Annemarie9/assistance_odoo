# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments/batch.md

Batch payments
==============

Batch payments allow grouping payments from multiple customers or
vendors into a single batch and generating a detailed deposit slip or
payment file with a batch reference. This reference can be used during
`reconciliation <../bank/reconciliation>`{.interpreted-text role="doc"}
to match bank transactions with the corresponding payments. This feature
is particularly useful for submitting `SEPA Direct Debit
payments <batch_sdd>`{.interpreted-text role="doc"}, depositing cash
payments or `checks <checks>`{.interpreted-text role="doc"}, or
generating outgoing payment files, such as
`SEPA <pay_sepa>`{.interpreted-text role="doc"} or
`NACHA <l10n_us/nacha>`{.interpreted-text role="ref"}.

Configuration
-------------

To enable batch payments, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the
`Customer Payments`{.interpreted-text role="guilabel"} section, and
enable `Batch Payments`{.interpreted-text role="guilabel"}.

Batch creation {#accounting/batch/creation}
--------------

To create a batch payment, follow these steps:

1.  Make sure all payments to be included in the batch have been
    `registered
    <accounting/payments/from-invoice-bill>`{.interpreted-text
    role="ref"}.

2.  Go to `Accounting --> Customers --> Payments`{.interpreted-text
    role="menuselection"}.

3.  Select the payments to include in the batch.

    ::: {.note}
    ::: {.title}
    Note
    :::

    All payments in the batch must use the same payment method. If
    needed, payments can be grouped using the
    `Payment Method Line`{.interpreted-text role="guilabel"}.
    :::

4.  Click `Create batch`{.interpreted-text role="guilabel"} or click
    `fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
    role="guilabel"} and select `Create batch payment`{.interpreted-text
    role="guilabel"}.

5.  In the batch payment form, review the selected payments. If any
    individual payments were missed, click
    `Add a line`{.interpreted-text role="guilabel"} and select the
    missing payments to be included in the batch.

6.  Once all relevant payments are included, click
    `Validate`{.interpreted-text role="guilabel"} to finalize the batch.

::: {.note}
::: {.title}
Note
:::

Once validated, no additional payments can be added to a batch.
:::

::: {.tip}
::: {.title}
Tip
:::

\- Click `Print`{.interpreted-text role="guilabel"} to download a list
of the included payments. - To view existing batch payments, go to
`Accounting --> Customers --> Batch
Payments`{.interpreted-text role="menuselection"}.
:::

### Bank reconciliation

Once the bank transactions
`have been created <../bank/transactions>`{.interpreted-text role="doc"}
in your database, you can
`reconcile them with the batch payment <reconciliation/batch-payments>`{.interpreted-text
role="ref"}.



::: {.note}
::: {.title}
Note
:::

If a specific payment could not be processed by the bank or is missing,
remove the related line from the resulting entry section of the
reconciliation view using the `fa-trash`{.interpreted-text role="icon"}
(`delete`{.interpreted-text role="guilabel"}) button before validating
the reconciliation.
:::

::: {.seealso}
\- `../payments`{.interpreted-text role="doc"} -
`batch_sdd`{.interpreted-text role="doc"}
:::
