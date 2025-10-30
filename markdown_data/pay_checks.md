# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments/pay_checks.md

Pay by checks
=============

Once you decide to pay a supplier bill, you can select to pay by check.
You can then print all the payments registered by check. Finally, the
bank reconciliation process will match the checks you sent to suppliers
with actual bank statements.

Configuration
-------------

### Activate checks payment methods

To activate the checks payment method, go to
`Accounting --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and scroll down to
the `Vendor Payments`{.interpreted-text role="guilabel"} section. There,
you can activate the payment method as well as set up the
`Check Layout`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- Once the `Checks`{.interpreted-text role="guilabel"} setting is
activated, the **Checks** payment method is automatically set up in the
`Outgoing Payments`{.interpreted-text role="guilabel"} tabs of **bank**
journals. - Some countries require specific modules to print checks;
such modules may be installed by default. For instance, the
`U.S. Checks Layout`{.interpreted-text role="guilabel"} module is
required to print U.S. checks.
:::

Compatible check stationery for printing checks
-----------------------------------------------

### United States

For the United States, Odoo supports by default the check formats of:

-   **Quickbooks & Quicken**: check on top, stubs in the middle and
    bottom;
-   **Peachtree**: check in the middle, stubs on top and bottom;
-   **ADP**: check in the bottom, and stubs on the top.

Pay a supplier bill with a check
--------------------------------

Paying a supplier with a check is done in three steps:

1.  registering a payment
2.  printing checks in batch for all registered payments
3.  reconciling bank statements

### Register a payment by check

To register a payment, open any supplier bill from the menu
`Purchases --> Vendor
Bills`{.interpreted-text role="menuselection"}. Once the supplier bill
is validated, you can register a payment. Set the
`Payment Method`{.interpreted-text role="guilabel"} to
`Checks`{.interpreted-text role="guilabel"} and validate the payment.

### Print checks

On your `Accounting Dashboard`{.interpreted-text role="guilabel"} in the
`Bank`{.interpreted-text role="guilabel"} Journal, you can see the
number of checks registered. By clicking on
`Checks to print`{.interpreted-text role="guilabel"} you have got the
possibility to print the reconciled checks.

To print all checks in batch, select all payments from the list view and
click on `Print`{.interpreted-text role="guilabel"}.
