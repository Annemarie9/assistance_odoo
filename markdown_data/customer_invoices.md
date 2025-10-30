# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/customer_invoices.md

show-content

:   

Customer invoices
=================

A customer invoice is a document issued by a company for products and/or
services sold to a customer. It records receivables as they are sent to
customers. Customer invoices can include amounts due for the goods
and/or services provided, applicable sales taxes, shipping and handling
fees, and other charges. Odoo supports multiple invoicing and payment
workflows.

::: {.seealso}
`/applications/finance/accounting/customer_invoices/overview`{.interpreted-text
role="doc"}
:::

From draft invoice to profit and loss report, the process involves
several steps once the goods (or services) have been ordered/shipped (or
rendered) to a customer, depending on the invoicing policy:

-   `accounting/invoice/creation`{.interpreted-text role="ref"}
-   `accounting/invoice/confirmation`{.interpreted-text role="ref"}
-   `accounting/invoice/sending`{.interpreted-text role="ref"}
-   `accounting/invoice/paymentandreconciliation`{.interpreted-text
    role="ref"}
-   `accounting/invoice/followup`{.interpreted-text role="ref"}
-   `accounting/invoice/reporting`{.interpreted-text role="ref"}

Invoice creation {#accounting/invoice/creation}
----------------

Draft invoices can be created directly from documents like sales orders
or purchase orders or manually from the
`Customer Invoices`{.interpreted-text role="guilabel"} journal in the
`Accounting Dashboard`{.interpreted-text role="guilabel"}.

An invoice must include the required information to enable the customer
to pay promptly for their goods and services. Make sure the following
fields are appropriately completed:

-   `Customer`{.interpreted-text role="guilabel"}: When a customer is
    selected, Odoo automatically pulls information from the customer
    record like the invoice address,
    `preferred payment terms <customer_invoices/payment_terms>`{.interpreted-text
    role="doc"},
    `fiscal positions <taxes/fiscal_positions>`{.interpreted-text
    role="doc"}, receivable account, and more onto the invoice. To
    change these values for this specific invoice, edit them directly on
    the invoice. To change them for future invoices, change the values
    on the contact record.
-   `Invoice Date`{.interpreted-text role="guilabel"}: If not set
    manually, this field is automatically set as the current date upon
    confirmation.
-   `Due Date`{.interpreted-text role="guilabel"} or
    `payment terms <customer_invoices/payment_terms>`{.interpreted-text
    role="doc"}: To specify when the customer has to pay the invoice.
-   `Journal`{.interpreted-text role="guilabel"}: Is automatically set
    and can be changed if needed.
-   `Currency <get_started/multi_currency>`{.interpreted-text
    role="doc"}
-   `Product`{.interpreted-text role="guilabel"}: Click
    `Add a line`{.interpreted-text role="guilabel"} to add a product.
-   `Quantity`{.interpreted-text role="guilabel"}
-   `Price`{.interpreted-text role="guilabel"}
-   `Taxes <taxes>`{.interpreted-text role="doc"} (if applicable)

::: {.tip}
::: {.title}
Tip
:::

To display the total amount of the invoice in words, go to
`Accounting -->
Configuration --> Settings`{.interpreted-text role="menuselection"} and
activate the `Total amount of invoice in letters`{.interpreted-text
role="guilabel"} option.
:::

The `Journal Items`{.interpreted-text role="guilabel"} tab displays the
accounting entries created. Additional invoice information such as the
`Customer Reference`{.interpreted-text role="guilabel"},
`Fiscal Positions
<taxes/fiscal_positions>`{.interpreted-text role="doc"},
`Incoterms <customer_invoices/incoterms>`{.interpreted-text role="doc"},
and more can be added or modified in the `Other Info`{.interpreted-text
role="guilabel"} tab.

::: {.note}
::: {.title}
Note
:::

Odoo initially creates invoices in `Draft`{.interpreted-text
role="guilabel"} status. Draft invoices have no accounting impact until
they are `confirmed <accounting/invoice/confirmation>`{.interpreted-text
role="ref"}.
:::

::: {.seealso}
`/applications/sales/sales/invoicing/proforma`{.interpreted-text
role="doc"}
:::

Invoice confirmation {#accounting/invoice/confirmation}
--------------------

Click `Confirm`{.interpreted-text role="guilabel"} when the document is
completed. The document\'s status changes to `Posted`{.interpreted-text
role="guilabel"}, and a journal entry is generated based on the invoice
configuration. On confirmation, Odoo assigns each invoice a unique
number from a defined
`sequence <customer_invoices/sequence>`{.interpreted-text role="doc"}.

::: {.note}
::: {.title}
Note
:::

\- Once confirmed, an invoice can no longer be updated. Click
`Reset to draft`{.interpreted-text role="guilabel"} if changes are
needed. - If required, invoices and other journal entries can be locked
once posted using the
`Lock posted entries with hash <data-inalterability/lock>`{.interpreted-text
role="ref"} feature.
:::

Invoice sending {#accounting/invoice/sending}
---------------

To send the invoice to the customer, click
`Send & Print`{.interpreted-text role="guilabel"}. A `Configure your
document layout`{.interpreted-text role="guilabel"} pop-up window will
appear if a `default invoice layout
<studio/pdf-reports/default-layout>`{.interpreted-text role="ref"}
hasn\'t been customized. Then, select how to send this invoice to the
customer in the `Send`{.interpreted-text role="guilabel"} window.

To send and print multiple invoices, go to
`Accounting --> Customers --> Invoices`{.interpreted-text
role="menuselection"} and select them. Then click the
`fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
role="guilabel"} menu and select `Send & Print`{.interpreted-text
role="guilabel"}. A banner will appear on the selected invoices to
indicate they are part of an ongoing send and print batch. This helps
prevent the process from being triggered manually again, as it may take
some time to complete for exceptionally large batches.

Payment and reconciliation {#accounting/invoice/paymentandreconciliation}
--------------------------

In Odoo, an invoice is considered `Paid`{.interpreted-text
role="guilabel"} when the associated accounting entry has been
reconciled with a corresponding bank transaction.

::: {.seealso}
\- `payments`{.interpreted-text role="doc"} -
`bank/reconciliation`{.interpreted-text role="doc"}
:::

Payment follow-up {#accounting/invoice/followup}
-----------------

Odoo\'s `follow-up actions <payments/follow_up>`{.interpreted-text
role="doc"} help companies follow up on customer invoices. Different
actions can be set up to remind customers to pay their outstanding
invoices, depending on how much the customer is overdue. These actions
are bundled into follow-up levels that trigger when an invoice is
overdue by a certain number of days. If there are multiple overdue
invoices for the same customer, the actions are performed on the most
overdue invoice.

Reporting {#accounting/invoice/reporting}
---------

### Partner reports {#accounting/invoice/partner-reports}

#### Partner Ledger {#accounting/invoices/partner-ledger}

The `Partner Ledger`{.interpreted-text role="guilabel"} report shows the
balance of customers and suppliers. To access it, go to
`Accounting --> Reporting --> Partner Ledger`{.interpreted-text
role="menuselection"}.

#### Aged Receivable {#accounting/invoices/aging-report}

To review outstanding customer invoices and their related due dates, use
the
`Aged Receivable <accounting/reporting/aged-receivable>`{.interpreted-text
role="ref"} report. To access it, go to
`Accounting --> Reporting --> Aged Receivable`{.interpreted-text
role="menuselection"}.

#### Aged Payable {#accounting/invoices/aged-payable}

To review outstanding vendor bills and their related due dates, use the
`Aged Payable <accounting/reporting/aged-payable>`{.interpreted-text
role="ref"} report. To access it, go to
`Accounting --> Reporting --> Aged Payable`{.interpreted-text
role="menuselection"}.

### Profit and Loss {#accounting/invoices/profit-and-loss}

The
`Profit and Loss <accounting/reporting/profit-and-loss>`{.interpreted-text
role="ref"} statement shows details of income and expenses.

### Balance sheet {#accounting/invoices/balance-sheet}

The
`Balance Sheet <accounting/reporting/balance-sheet>`{.interpreted-text
role="ref"} summarizes the company\'s assets, liabilities, and equity at
a specific time.

::: {.toctree titlesonly=""}
customer\_invoices/overview customer\_invoices/customer\_addresses
customer\_invoices/payment\_terms customer\_invoices/terms\_conditions
customer\_invoices/cash\_discounts customer\_invoices/credit\_notes
customer\_invoices/cash\_rounding customer\_invoices/deferred\_revenues
customer\_invoices/electronic\_invoicing customer\_invoices/sequence
customer\_invoices/snailmail customer\_invoices/epc\_qr\_code
customer\_invoices/incoterms
:::
