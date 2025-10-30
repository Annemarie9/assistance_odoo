# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/retention.md

Withholding taxes
=================

A **withholding tax**, also known as retention tax, mandates the payer
of a customer invoice to deduct a tax from the payment and remit it to
the government. Typically, a tax is included in the subtotal to
calculate the total amount paid, while withholding taxes are directly
subtracted from the payment.

Configuration
-------------

In Odoo, a withholding tax is defined by creating a negative tax. To
create one, go to
`Accounting --> Configuration --> Taxes`{.interpreted-text
role="menuselection"} and, in the `Amount`{.interpreted-text
role="guilabel"} field, enter a negative amount.



Then, go to the `Advanced Options`{.interpreted-text
role="menuselection"} tab and create a retention
`Tax Group`{.interpreted-text role="guilabel"}.



::: {.tip}
::: {.title}
Tip
:::

If the retention is a percentage of a regular tax, create a
`Tax`{.interpreted-text role="guilabel"} with a
`Tax Computation`{.interpreted-text role="guilabel"} as a
`Group of Taxes`{.interpreted-text role="guilabel"}. Then, set both the
regular tax and the retention one in the `Definition`{.interpreted-text
role="guilabel"} tab.
:::

Retention taxes on invoices
---------------------------

Once the retention tax has been created, it can be used on customer
forms, sales orders, and customer invoices. Several taxes can be applied
on a single customer invoice line.



::: {.seealso}
`../taxes`{.interpreted-text role="doc"}
:::
