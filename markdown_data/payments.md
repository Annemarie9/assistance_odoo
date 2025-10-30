# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments.md

show-content

:   

Payments
========

In Odoo, payments can either be automatically linked to an invoice or
bill or be stand-alone records for use at a later date:

-   If a payment is **linked to an invoice or bill**, it reduces/settles
    the amount due on the invoice. Multiple payments on the same invoice
    are possible.
-   If a payment is **not linked to an invoice or bill**, the customer
    has an outstanding credit with the company, or the company has an
    outstanding debit with a vendor. Those outstanding amounts
    reduce/settle unpaid invoices/bills.

::: {.seealso}
\- `Internal transfers <payments/internal_transfers>`{.interpreted-text
role="doc"} - `bank/reconciliation`{.interpreted-text role="doc"} -
[Odoo Tutorials: Bank
Configuration](https://www.odoo.com/slides/slide/bank-configuration-6832)
:::

Registering payment from an invoice or bill {#accounting/payments/from-invoice-bill}
-------------------------------------------

Clicking `Register payment`{.interpreted-text role="guilabel"} in a
customer invoice or vendor bill generates a new journal entry and sets
the amount due according to the payment amount. The counterpart is
reflected in an
`outstanding <bank/outstanding-accounts>`{.interpreted-text role="ref"}
**receipts** or **payments** account. At this point, the customer
invoice or vendor bill is marked as `In payment`{.interpreted-text
role="guilabel"} or `Partially paid
<accounting/payments/partial-payment>`{.interpreted-text role="ref"}.
Then, when the outstanding account is reconciled with a bank
transaction, the invoice or vendor bill changes to the
`Paid`{.interpreted-text role="guilabel"} status.

To open the `Journal Entry Info`{.interpreted-text role="guilabel"}
window and display more information about the payment, click the
`fa-info-circle`{.interpreted-text role="icon"}
`(information)`{.interpreted-text role="guilabel"} icon in the footer of
the `Invoice Lines`{.interpreted-text role="guilabel"} tab. To access
additional information, such as the related journal entry, click
`View`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

\- The customer invoice or vendor bill must be in the
`Posted`{.interpreted-text role="guilabel"} status to register the
payment. - If a payment is unreconciled, it still appears in the books
but is no longer linked to the invoice. - If a payment is (un)reconciled
in a different currency, a journal entry is automatically created to
post the currency exchange gains/losses (reversal) amount. - If a
payment is (un)reconciled on an invoice with cash-basis taxes, a journal
entry is automatically created to post the cash-basis tax (reversal)
amount.
:::

::: {.tip}
::: {.title}
Tip
:::

If the main bank account is set as the
`outstanding account <bank/outstanding-accounts>`{.interpreted-text
role="ref"} on the bank journal\'s payment method, registering the full
payment on an invoice or bill moves the invoice/bill directly to the
`Paid`{.interpreted-text role="guilabel"} status without requiring bank
reconciliation.
:::

Registering payments not tied to an invoice or bill {#accounting/payments/not-tied}
---------------------------------------------------

When a new payment is registered via
`Customers / Vendors --> Payments`{.interpreted-text
role="menuselection"}, it is not directly linked to an invoice or bill.
Instead, the account receivable or the account payable is matched with
the **outstanding account** until it is manually matched with its
related invoice or bill. Then,
`reconciling <bank/reconciliation>`{.interpreted-text role="doc"} the
payment with the bank transaction completes the payment workflow.

### Payments matching {#accounting/payments/payments-matching}

::: {.note}
::: {.title}
Note
:::

During the `bank reconciliation <bank/reconciliation>`{.interpreted-text
role="doc"} process, a remaining balance is identified if the total
debits and credits do not match when records are compared with bank
transactions. This balance must either be reconciled later or written
off immediately.
:::

#### For a single invoice or bill {#accounting/payments/matching-invoices-bills}

A blue banner appears when validating a new invoice/bill and an
**outstanding payment** exists for this specific customer or vendor. To
match it with the invoice or bill, click `Add`{.interpreted-text
role="guilabel"} under `Outstanding Credits`{.interpreted-text
role="guilabel"} or `Outstanding Debits`{.interpreted-text
role="guilabel"}.



The invoice or bill is then marked as `In payment`{.interpreted-text
role="guilabel"} until the payment is `reconciled
<bank/reconciliation>`{.interpreted-text role="doc"} with its
corresponding
`bank transaction(s) <bank/transactions>`{.interpreted-text role="doc"}.

#### Matching payments {#accounting/payments/auto-reconcile-tool}

The `Payments matching`{.interpreted-text role="guilabel"} or
`Auto-reconcile`{.interpreted-text role="guilabel"} tool allows
reconciling journal items with each other (i.e., payments with customer
invoices or vendor bills) either individually or in batches. Access the
`Accounting Dashboard`{.interpreted-text role="guilabel"}, click the
`fa-ellipsis-v`{.interpreted-text role="icon"}
(`dropdown menu`{.interpreted-text role="guilabel"}) button from the
`Customer Invoices`{.interpreted-text role="guilabel"} or `Vendor
Bills`{.interpreted-text role="guilabel"} journals, and select
`Payments Matching`{.interpreted-text role="guilabel"}. Alternatively,
go to `Accounting --> Accounting --> Reconcile`{.interpreted-text
role="menuselection"}.

To manually `Reconcile`{.interpreted-text role="guilabel"} journal
items, select the individual items from the list view and click
`Reconcile`{.interpreted-text role="guilabel"}.

##### Auto-Reconcile Feature

To use the `Auto-Reconcile`{.interpreted-text role="guilabel"} feature,
follow these steps:

1.  In the `Journal Items to reconcile`{.interpreted-text
    role="guilabel"} list view, click `Auto-Reconcile`{.interpreted-text
    role="guilabel"} next to the receivable or payable account (or a
    specific contact\'s journal item in that account).
2.  In the `Find Entries to Reconcile Automatically`{.interpreted-text
    role="guilabel"} window, set the `Reconcile`{.interpreted-text
    role="guilabel"} field depending on how you want to match journal
    items:
    -   `Opposite balances one by one`{.interpreted-text
        role="guilabel"}: Each debit journal item will be matched with
        the corresponding credit journal item of the same value.
    -   `Accounts with zero balances`{.interpreted-text
        role="guilabel"}: All reconciled journal items will have the
        same matching number.
3.  Click `Launch`{.interpreted-text role="guilabel"}.

Invoices and bills are automatically matched to their corresponding
payments and marked as `In payment`{.interpreted-text role="guilabel"}
until they are `reconciled <bank/reconciliation>`{.interpreted-text
role="doc"} with their corresponding
`bank transactions <bank/transactions>`{.interpreted-text role="doc"}.

Registering payments on multiple invoices or bills (group payments) {#accounting/payments/group-payments}
-------------------------------------------------------------------

To register payments on multiple invoices/bills, follow these steps:

1.  Go to
    `Accounting --> Customers --> Invoices/Credit Notes`{.interpreted-text
    role="menuselection"} or
    `Accounting --> Vendors --> Bills/Refunds`{.interpreted-text
    role="menuselection"}.
2.  In the list view, select the relevant invoices/credit notes or
    bills/refunds.
3.  Click `fa-cog`{.interpreted-text role="icon"}
    `Actions`{.interpreted-text role="guilabel"} and select
    `Register Payment`{.interpreted-text role="guilabel"}.
4.  In the `Register Payment`{.interpreted-text role="guilabel"} window,
    select the `Journal`{.interpreted-text role="guilabel"}, the
    `Payment Method`{.interpreted-text role="guilabel"}, and the
    `Payment Date`{.interpreted-text role="guilabel"}.
5.  To combine all payments from the same contact into a single payment,
    enable the `Group
    Payments`{.interpreted-text role="guilabel"} option, or leave it
    unchecked to create separate payments.
6.  Click `Create payment`{.interpreted-text role="guilabel"}.

The invoices or bills are then marked as `In payment`{.interpreted-text
role="guilabel"} until the bank transactions are
`reconciled <bank/reconciliation>`{.interpreted-text role="doc"} with
the payments.

Registering a single payment for multiple customers or vendors (batch payments) {#accounting/payments/batch-payments}
-------------------------------------------------------------------------------

Batch payments allow grouping payments from multiple customers to ease
`reconciliation
<bank/reconciliation>`{.interpreted-text role="doc"}. They are also
useful when depositing `checks <payments/checks>`{.interpreted-text
role="doc"} or cash payments to the bank or for generating bank payment
files such as `SEPA
<payments/pay_sepa>`{.interpreted-text role="doc"} or
`NACHA <l10n_us/nacha>`{.interpreted-text role="ref"}.

::: {.seealso}
`payments/batch`{.interpreted-text role="doc"}
:::

Registering a partial payment {#accounting/payments/partial-payment}
-----------------------------

To register a partial payment, click on
`Register Payment`{.interpreted-text role="guilabel"} from the related
invoice or bill. In the case of a partial payment (when the
`Amount`{.interpreted-text role="guilabel"} paid is less than the total
remaining amount on the invoice or the bill), the
`Payment Difference`{.interpreted-text role="guilabel"} field displays
the outstanding balance. There are two options:

-   `Keep open`{.interpreted-text role="guilabel"}: Keep the invoice or
    the bill open and mark it with a `Partial`{.interpreted-text
    role="guilabel"} banner;
-   `Mark as fully paid`{.interpreted-text role="guilabel"}: Select an
    account in the `Post Difference In`{.interpreted-text
    role="guilabel"} field and change the `Label`{.interpreted-text
    role="guilabel"} if needed. A journal entry will be created to
    balance the accounts payable or receivable with the selected
    account.



Reconciling payments with bank transactions {#accounting/payments/reconciling-payments}
-------------------------------------------

Once a payment has been registered, the status of the invoice or bill is
`In payment`{.interpreted-text role="guilabel"}. The next step is
`reconciling <bank/reconciliation>`{.interpreted-text role="doc"} the
payment with the related `bank
transaction <bank/transactions>`{.interpreted-text role="doc"} line to
finalize the payment workflow and mark the invoice or bill as
`Paid`{.interpreted-text role="guilabel"}.

::: {.toctree titlesonly=""}
payments/online payments/checks payments/batch payments/batch\_sdd
payments/follow\_up payments/internal\_transfers payments/pay\_sepa
payments/pay\_checks payments/forecast payments/trusted\_accounts
:::
