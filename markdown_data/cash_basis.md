# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/cash_basis.md

Cash basis taxes
================

Cash basis taxes are due when the payment is made, as opposed to
standard taxes that are due when the invoice is confirmed. Reporting
your income and expenses to the government based on the cash basis
method is mandatory in some countries and under some conditions.

::: {.example}
You sell a product in the 1st quarter of your fiscal year, and the
payment is received in the 2nd quarter. Based on the cash basis method,
the tax you must pay is for the 2nd quarter.
:::

Configuration
-------------

Go to `Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and under the `Taxes`{.interpreted-text
role="guilabel"} section, enable `Cash Basis`{.interpreted-text
role="guilabel"}.

Then, define the `Tax Cash Basis Journal`{.interpreted-text
role="guilabel"}. Click on the external link button next to the journal
to update its default properties such as the
`Journal Name`{.interpreted-text role="guilabel"},
`Type`{.interpreted-text role="guilabel"} or
`Short Code`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

By default, the journal entries of the
`Cash Basis Taxes`{.interpreted-text role="guilabel"} journal are named
using the `CABA`{.interpreted-text role="guilabel"} short code.
:::

Once this is done, go to
`Accounting --> Configuration --> Accounting: Taxes`{.interpreted-text
role="menuselection"} to configure your taxes. You can either
`Create`{.interpreted-text role="guilabel"} a new tax or update an
existing one by clicking on it.

The `Account`{.interpreted-text role="guilabel"} column reflects the
proper transitional accounts to post taxes until the payment is
registered.

![Fill in the account column with a transitional accounts where taxes go until the payment
is registered](cash_basis/account_column.png){.align-center}

In the `Advanced Options`{.interpreted-text role="guilabel"} tab, decide
of the `Tax Exigilibity`{.interpreted-text role="guilabel"}. Select
`Based on Payment`{.interpreted-text role="guilabel"}, so the tax is due
when the payment of the invoice is received. You can then also define
the `Cash Basis Transition Account`{.interpreted-text role="guilabel"}
where the tax amount is recorded as long as the original invoice has not
been reconciled.

![Fill in the Cash Basis Transition Account where taxes amounts go until payment
reconciliation.](cash_basis/advanced_options.png){.align-center}

Impact of cash basis taxes on accounting
----------------------------------------

To illustrate the impact of cash basis taxes on accounting transactions,
let\'s take an example with the sales of a product that costs 1,000\$,
with a cash basis tax of 15%.

{.align-center}

The following entries are created in your accounting, and the tax report
is currently empty.

  ---------------------------------------------------------
  **Customer journal (INV)**   
  ---------------------------- ----------------------------
  **Debit**                    **Credit**

  Receivable \$1,150           

                               Income \$1,000

                               Temporary tax account \$150
  ---------------------------------------------------------

When the payment is then received, it is registered as below :

  ---------------------------------------------------------
  **Bank journal (BANK)**      
  ---------------------------- ----------------------------
  **Debit**                    **Credit**

  Bank \$1,150                 

                               Receivable \$1,150
  ---------------------------------------------------------

::: {.note}
::: {.title}
Note
:::

Once the payment is registered, you can use the
`Cash Basis Entries`{.interpreted-text role="guilabel"} smart button on
the invoice to access them directly.
:::

Finally, upon reconciliation of the invoice with the payment, the below
entry is automatically created:

+----------------------------+----------------------------+
| \*\*Tax Cash Basis Journal | ba)\*\*                    |
| (Ca                        |                            |
+============================+============================+
| **Debit**                  | **Credit**                 |
+----------------------------+----------------------------+
| Income account \$1,000     |                            |
+----------------------------+----------------------------+
| Temporary tax account      |                            |
| \$150                      |                            |
+----------------------------+----------------------------+
|                            | > Income account \$1,000   |
+----------------------------+----------------------------+
|                            | Tax Received \$150         |
+----------------------------+----------------------------+

The journal items `Income account`{.interpreted-text role="guilabel"}
vs. `Income account`{.interpreted-text role="guilabel"} are neutral, but
they are needed to ensure correct tax reports in Odoo with accurate base
tax amounts.

Using a default `Base Tax Received Account`{.interpreted-text
role="guilabel"} is recommended so your balance is at zero and your
income account is not polluted by unnecessary accounting movements. To
do so, go to `Configuration --> Settings --> Taxes`{.interpreted-text
role="menuselection"}, and select a
`Base Tax Received Account`{.interpreted-text role="guilabel"} under
`Cash Basis`{.interpreted-text role="guilabel"}.
