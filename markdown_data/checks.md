# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments/checks.md

Checks
======

There are two ways to handle payments received by checks in Odoo, either
by using `outstanding
accounts <checks/outstanding-account>`{.interpreted-text role="ref"} or
by `bypassing the reconciliation process
<checks/reconciliation-bypass>`{.interpreted-text role="ref"}.

**Using outstanding accounts is recommended**, as your bank account
balance stays accurate by taking into account checks yet to be cashed.

::: {.note}
::: {.title}
Note
:::

Both methods produce the same data in your accounting at the end of the
process. But if you have checks that have not been cashed in, the
**Outstanding Account** method reports these checks in the **Outstanding
Receipts** account. However, funds appear in your bank account whether
or not they are reconciled, as the bank value is reflected at the moment
of the bank statement.
:::

::: {.seealso}
\* `Outstanding accounts <bank/outstanding-accounts>`{.interpreted-text
role="ref"} \*
`Bank reconciliation <accounting/reconciliation>`{.interpreted-text
role="ref"}
:::

Method 1: Outstanding account {#checks/outstanding-account}
-----------------------------

When you receive a check, you
`record a payment <../bank/reconciliation>`{.interpreted-text
role="doc"} by check on the invoice. Then, when your bank account is
credited with the check\'s amount, you reconcile the payment and
statement to move the amount from the **Outstanding Receipt** account to
the **Bank** account.

::: {.tip}
::: {.title}
Tip
:::

You can create a new payment method named *Checks* if you would like to
identify such payments quickly. To do so, go to
`Accounting --> Configuration --> Journals --> Bank`{.interpreted-text
role="menuselection"}, click the `Incoming Payments`{.interpreted-text
role="guilabel"} tab, and `Add a line`{.interpreted-text
role="guilabel"}. As `Payment
Method`{.interpreted-text role="guilabel"}, select
`Manual`{.interpreted-text role="guilabel"}, and enter
[Checks]{.title-ref} as name.
:::

Method 2: Reconciliation bypass {#checks/reconciliation-bypass}
-------------------------------

When you receive a check, you
`record a payment <../bank/reconciliation>`{.interpreted-text
role="doc"} on the related invoice. The amount is then moved from the
**Account Receivable** to the **Bank** account, bypassing the
reconciliation and creating only **one journal entry**.

To do so, you *must* follow the following setup. Go to
`Accounting --> Configuration
--> Journals --> Bank`{.interpreted-text role="menuselection"}. Click
the `Incoming Payments`{.interpreted-text role="guilabel"} tab and then
`Add a line`{.interpreted-text role="guilabel"}, select
`Manual`{.interpreted-text role="guilabel"} as
`Payment Method`{.interpreted-text role="guilabel"}, and enter
[Checks]{.title-ref} as `Name`{.interpreted-text role="guilabel"}. Click
the toggle menu button, tick
`Outstanding Receipts accounts`{.interpreted-text role="guilabel"}, and
in the `Outstanding Receipts accounts`{.interpreted-text
role="guilabel"} column, and set the `Bank`{.interpreted-text
role="guilabel"} account for the **Checks** payment method.



Payment registration
--------------------

::: {.note}
::: {.title}
Note
:::

By default, there are two ways to register payments made by check:

-   **Manual**: for single checks;
-   **Batch**: for multiple checks at once.

This documentation focuses on **single-check** payments. For **batch
deposits**, see `the
batch payments documentation <batch>`{.interpreted-text role="doc"}.
:::

Once you receive a customer check, go to the related invoice
(`Accounting -->
Customer --> Invoices)`{.interpreted-text role="menuselection"}, and
click `Register Payment`{.interpreted-text role="guilabel"}. Fill in the
payment information:

-   `Journal: Bank`{.interpreted-text role="guilabel"};
-   `Payment method`{.interpreted-text role="guilabel"}:
    `Manual`{.interpreted-text role="guilabel"} (or **Checks** if you
    have created a specific payment method);
-   `Memo`{.interpreted-text role="guilabel"}: enter the check number;
-   Click `Create Payment`{.interpreted-text role="guilabel"}.



The generated journal entries are different depending on the payment
registration method chosen.

Journal entries
---------------

### Outstanding account

The invoice is marked as `In Payment`{.interpreted-text role="guilabel"}
as soon as you record the payment. This operation produces the following
**journal entry**:

  ----------------------------------------------------------------
  Account                Statement Match     Debit      Credit
  ---------------------- ------------------- ---------- ----------
  Account Receivable                                    100.00

  Outstanding Receipts                       100.00     
  ----------------------------------------------------------------

Then, once you receive the bank statements, match this statement with
the check of the **Outstanding Receipts** account. This produces the
following **journal entry**:

+---------------------+-------------------+----------+----------+
| Account             | Statement Match   | Debit    | Credit   |
+=====================+===================+==========+==========+
| Outstanding         | > X               |          | 100.00   |
| Receipts            |                   |          |          |
+---------------------+-------------------+----------+----------+
| Bank                |                   | 100.00   |          |
+---------------------+-------------------+----------+----------+

If you use this approach to manage received checks, you get the list of
checks that have not been cashed in the **Outstanding Receipt** account
(accessible, for example, from the general ledger).

### Reconciliation bypass

The invoice is marked as `Paid`{.interpreted-text role="guilabel"} as
soon as you record the check.

With this approach, you bypass the use of **outstanding accounts**,
effectively getting only one journal entry in your books and bypassing
the reconciliation:

  ----------------------------------------------------------------
  Account                Statement Match     Debit      Credit
  ---------------------- ------------------- ---------- ----------
  Account Receivable     X                              100.00

  Bank                                       100.00     
  ----------------------------------------------------------------
