# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments/internal_transfers.md

Internal transfers
==================

Internal money transfers can be handled in Odoo. At least two bank
accounts are needed to make internal transfers.

::: {.seealso}
`How to add an additional bank account <../bank>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

An internal transfer account is automatically created on your database
based on your company\'s localization and depending on your country's
legislation. To modify the default `Internal
transfer account`{.interpreted-text role="guilabel"}, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and scroll down to the
`Default Accounts`{.interpreted-text role="guilabel"} section.

Register an internal transfer from one bank to another
------------------------------------------------------

If you want to transfer money from one bank to another, access the
Accounting Dashboard, click the drop-down selection button
(`⋮`{.interpreted-text role="guilabel"}) on the bank from which you want
to make the transfer, then click `Payments`{.interpreted-text
role="guilabel"}. Select or create a payment, tick the
`Internal Transfer`{.interpreted-text role="guilabel"} checkbox, and
select a `Destination Journal`{.interpreted-text role="guilabel"} before
you `Confirm`{.interpreted-text role="guilabel"} the internal transfer.

The money is now booked in the transfer account and another payment is
automatically created in the destination journal.

::: {.example}
-   Bank journal (Bank A)

      **Account**                     **Debit**     **Credit**
      ------------------------------- ------------- ------------
      Outstanding Payments account                  \$1,000
      **Internal transfer account**   **\$1,000**   

-   Bank journal (Bank B)

      **Account**                     **Debit**   **Credit**
      ------------------------------- ----------- -------------
      Outstanding Receipts account    \$1,000     
      **Internal transfer account**               **\$1,000**

There is **one outstanding payment** and **one outstanding receipt**
pending in your two bank account journals because the bank statement
confirming the sending and receiving of the money has not been booked
yet.
:::

Once this is done, you can book and reconcile your bank statement lines
as usual.

::: {.seealso}
`../bank/reconciliation`{.interpreted-text role="doc"}
:::
