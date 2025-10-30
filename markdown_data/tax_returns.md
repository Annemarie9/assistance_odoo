# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/tax_returns.md

Tax return (VAT declaration)
============================

Companies with a registered `VAT (Value Added Tax)`{.interpreted-text
role="abbr"} number must submit a **tax return** on a monthly or
quarterly basis, depending on their turnover and the registration
regulation. A tax return - or VAT return - gives the tax authorities
information about the taxable transactions made by the company. The
**output tax** is charged on the number of goods and services sold by a
business, while the **input tax** is the tax added to the price when
goods or services are purchased. Based on these values, the company can
calculate the tax amount they have to pay or be refunded.

::: {.note}
::: {.title}
Note
:::

You can find additional information about VAT and its mechanism on this
page from the European Commission: [\"What is
VAT?\"](https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en).
:::

Prerequisites {#tax-returns/prerequisites}
-------------

### Tax Return Periodicity {#tax-returns/periodicity}

The configuration of the **Tax Return Periodicity** allows Odoo to
compute your tax return correctly and also to send you a reminder to
never miss a tax return deadline.

To do so, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the
`Tax Return Periodicity`{.interpreted-text role="guilabel"}, you can
set:

-   `Periodicity`{.interpreted-text role="guilabel"}: define here
    whether you submit your tax return on a monthly or quarterly basis;
-   `Reminder`{.interpreted-text role="guilabel"}: define when Odoo
    should remind you to submit your tax return;
-   `Journal`{.interpreted-text role="guilabel"}: select the journal in
    which to record the tax return.

{.align-center}

::: {.note}
::: {.title}
Note
:::

This is usually configured during the
`app's initial set up <../get_started>`{.interpreted-text role="doc"}.
:::

### Tax Grids {#tax-returns/tax-grids}

Odoo generates tax reports based on the `Tax Grids`{.interpreted-text
role="guilabel"} settings that are configured on your taxes. Therefore,
it is crucial to make sure that all recorded transactions use the right
taxes. You can see the `Tax Grids`{.interpreted-text role="guilabel"} by
opening the `Journal Items`{.interpreted-text role="guilabel"} tab of
any invoice and bill.

{.align-center}

To configure your tax grids, go to
`Accounting --> Configuration --> Taxes`{.interpreted-text
role="menuselection"}, and open the tax you want to modify. There, you
can edit your tax settings, along with the tax grids that are used to
record invoices or credit notes.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Taxes and reports are usually already pre-configured in Odoo: a
`fiscal localization package
<fiscal_localizations/packages>`{.interpreted-text role="ref"} is
installed according to the country you select at the creation of your
database.
:::

Close a tax period {#tax-returns/close}
------------------

### Tax Lock Date {#tax-returns/lock-date}

Any new transaction whose accounting date prior to the
`Tax Lock Date`{.interpreted-text role="guilabel"} has its tax values
moved to the next open tax period. This is useful to make sure that no
change can be made to a report once its period is closed.

Therefore, we recommend locking your tax date before working on your
`Closing Journal Entry`{.interpreted-text role="guilabel"}. This way,
other users cannot modify or add transactions that would have an impact
on the `Closing Journal Entry`{.interpreted-text role="guilabel"}, which
can help you avoid some tax declaration errors.

To check the current `Tax Lock Date`{.interpreted-text role="guilabel"},
or to edit it, go to
`Accounting --> Accounting --> Actions: Lock Dates`{.interpreted-text
role="menuselection"}.

{.align-center}

### Tax Report {#tax-returns/report}

Once all the transactions involving taxes have been posted for the
period you want to report, open the `Tax Report`{.interpreted-text
role="guilabel"} by going to
`Accounting --> Reporting --> Tax Report`{.interpreted-text
role="menuselection"}. Select the period you want to declare using the
date filter to have an overview of the tax report. From the report,
click `PDF`{.interpreted-text role="guilabel"} or
`XLSX`{.interpreted-text role="guilabel"} to download the desired format
of the tax report. To save the report to the Documents app, click the
`fa-caret-down`{.interpreted-text role="icon"} (`down
arrow`{.interpreted-text role="guilabel"}) icon, then click
`Save`{.interpreted-text role="guilabel"}. Select the format to
`Export to`{.interpreted-text role="guilabel"}, the
`Documents Name`{.interpreted-text role="guilabel"}, the
`Folder`{.interpreted-text role="guilabel"} to store it in, and add any
`Tags`{.interpreted-text role="guilabel"}.

The report includes all the values to report to the tax authorities,
along with the amount to be paid or refunded.



::: {.note}
::: {.title}
Note
:::

If you forgot to lock your tax date before clicking on
`Closing Journal Entry`{.interpreted-text role="guilabel"}, then Odoo
automatically locks your fiscal period on the same date as the
accounting date of your entry. This safety mechanism can prevent some
fiscal errors, but it is advised to lock your tax date manually before,
as described above.
:::

::: {.important}
::: {.title}
Important
:::

\- Once the tax report for a period has been generated but not yet
posted, additional invoices or bills from that same period can still be
posted and included in the closing entry. To do so, click
`oi-arrow-right`{.interpreted-text role="icon"}
`Refresh`{.interpreted-text role="guilabel"} in the
`Proposition of tax closing
journal entry`{.interpreted-text role="guilabel"}, or click
`Closing Entry`{.interpreted-text role="guilabel"} again from the tax
report. - After the tax report has been posted for a period, Odoo locks
the period and prevents the creation of new journal entries involving
VAT. Any corrections to customer invoices or vendor bills must then be
recorded in the following period.
:::

::: {.seealso}
\* `../taxes`{.interpreted-text role="doc"} \*
`../get_started`{.interpreted-text role="doc"} \*
`../../fiscal_localizations`{.interpreted-text role="doc"}
:::
