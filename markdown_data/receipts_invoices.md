Receipts and invoices
=====================

Receipts
--------

Set up receipts by going to
`Point of Sale --> Configuration --> Point of Sale`{.interpreted-text
role="menuselection"}, selecting a POS, and scrolling down to the
`Bills & Receipts`{.interpreted-text role="guilabel"} section.

To **customize** the **header** and **footer**, activate
`Header & Footer`{.interpreted-text role="guilabel"} and fill in both
fields with the information to be printed on the receipts.

To **print receipts** automatically once the payment is registered,
enable the `Automatic
Receipt Printing`{.interpreted-text role="guilabel"} setting.



::: {.seealso}
\- `restaurant/bill_printing`{.interpreted-text role="doc"} -
`configuration/epos_printers`{.interpreted-text role="doc"}
:::

### Reprint a receipt

From the POS interface, click `Orders`{.interpreted-text
role="guilabel"}, open the dropdown selection menu next to the search
bar, and change the default `All active orders`{.interpreted-text
role="guilabel"} filter to `Paid`{.interpreted-text role="guilabel"}.
Then, select the corresponding order and click
`Print Receipt`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

You can filter the list of orders using the search bar. Type in your
reference and click `Receipt Number`{.interpreted-text role="guilabel"},
`Date`{.interpreted-text role="guilabel"}, or
`Customer`{.interpreted-text role="guilabel"}.
:::

Invoices {#receipts-invoices/invoices}
--------

Point of Sale allows you to issue and print invoices for
`registered customers <pos/customers>`{.interpreted-text role="ref"}
upon payment and retrieve all past invoiced orders.

::: {.note}
::: {.title}
Note
:::

An invoice created in a POS creates an entry into the corresponding
`accounting journal
<cheat_sheet/journals>`{.interpreted-text role="ref"}, previously
`set up <receipts_invoices/invoice_configuration>`{.interpreted-text
role="ref"}.
:::

### Configuration {#receipts_invoices/invoice_configuration}

To define what journals will be used for a specific POS, go to the
`POS' settings
<configuration/settings>`{.interpreted-text role="ref"} and scroll down
to the accounting section. Then, you can determine the accounting
journals used by default for orders and invoices in the
`Default Journals`{.interpreted-text role="guilabel"} section.



### Invoice a customer

Upon processing a payment, click `Invoice`{.interpreted-text
role="guilabel"} underneath the customer\'s name to issue an invoice for
that order.

Select the payment method and click `Validate`{.interpreted-text
role="guilabel"}. The **invoice** is automatically issued and ready to
be downloaded and/or printed.

::: {.note}
::: {.title}
Note
:::

To be able to issue an invoice, a
`customer <pos/customers>`{.interpreted-text role="ref"} must be
selected.
:::

### Retrieve invoices

To retrieve invoices from the **POS dashboard**,

1.  access all orders made through your POS by going to
    `Point of Sale --> Orders -->
    Orders`{.interpreted-text role="menuselection"};
2.  to access an order\'s invoice, open the **order form** by selecting
    the order, then click `Invoice`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

\- **Invoiced orders** can be identified by the
`Invoiced`{.interpreted-text role="guilabel"} status in the
`Status`{.interpreted-text role="guilabel"} column. - You can filter the
list of orders to invoiced orders by clicking
`Filters`{.interpreted-text role="guilabel"} and
`Invoiced`{.interpreted-text role="guilabel"}.
:::

### QR codes to generate invoices

Customers can also request an invoice by scanning the **QR code**
printed on their receipt. Upon scanning, they must fill in a form with
their billing information and click `Get my
invoice`{.interpreted-text role="guilabel"}. On the one hand, doing so
generates an invoice available for download. On the other hand, the
order status goes from `Paid`{.interpreted-text role="guilabel"} or
`Posted`{.interpreted-text role="guilabel"} to
`Invoiced`{.interpreted-text role="guilabel"} in the Odoo backend.



To use this feature, you have to enable QR codes on receipts by going to
`Point of
Sale --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, select the POS in the
`Point of Sale`{.interpreted-text role="guilabel"} field, scroll down to
the `Bills & Receipts`{.interpreted-text role="guilabel"} section and
enable `Use QR code on
ticket`{.interpreted-text role="guilabel"}.
