# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/sdd.md

SEPA Direct Debit
=================

SEPA (Single Euro Payments Area) is a payment-integration initiative of
the European Union that facilitates standardized and simplified
electronic payments in euros across participating countries.

SEPA Direct Debit (SDD) is a payment provider that allows future
payments to be collected from customers\' bank accounts based on a
signed `SEPA Direct Debit mandate
<accounting/batch_sdd/sdd_mandates>`{.interpreted-text role="ref"}. This
is particularly useful for recurring payments based on a
`subscription </applications/sales/subscriptions>`{.interpreted-text
role="doc"}.

::: {.important}
::: {.title}
Important
:::

To use the SEPA Direct Debit (SDD) payment provider and create
`SEPA Direct Debit mandates
<accounting/batch_sdd/sdd_mandates>`{.interpreted-text role="ref"}:

-   The invoice being paid must be for an amount in euros.
-   The `SEPA Direct Deposit (SDD)`{.interpreted-text role="guilabel"}
    feature must be enabled, and the company\'s
    `Creditor Identifier`{.interpreted-text role="guilabel"} must be
    defined in the `Accounting or Invoicing settings
    <accounting/batch_sdd/sepa-configuration>`{.interpreted-text
    role="ref"}.
:::

Configuration {#sdd/configuration}
-------------

To configure **SEPA Direct Debit**, follow these steps:

1.  `Navigate to the SEPA Direct Debit payment provider <payment_providers/supported_providers>`{.interpreted-text
    role="ref"}.

2.  In the `Configuration`{.interpreted-text role="guilabel"} tab,
    select whether the memo or `Communication`{.interpreted-text
    role="guilabel"} to be displayed alongside the payment instructions
    should be:

    -   `Based on Document Reference`{.interpreted-text
        role="guilabel"}: the sales order or invoice number
    -   `Based on Customer ID`{.interpreted-text role="guilabel"}: the
        customer identifier

3.  Select the `Enable QR codes`{.interpreted-text role="guilabel"}
    check box to activate QR code payments.

    ::: {.note}
    ::: {.title}
    Note
    :::

    `Additional accounting setup <../accounting/customer_invoices/epc_qr_code>`{.interpreted-text
    role="doc"} is required to use QR codes.
    :::

4.  Edit the default payment instructions in the
    `Messages`{.interpreted-text role="guilabel"} tab to include your
    **bank account number**. These instructions are displayed at the end
    of the checkout process on your ecommerce website or on the customer
    portal.

5.  Set the `State`{.interpreted-text role="guilabel"} field to
    `Enabled`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

\- Leave the `Currencies`{.interpreted-text role="guilabel"} field set
to the default `EUR`{.interpreted-text role="guilabel"} tag to ensure
`SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"} is only
available for payments in euros. - The `Bank Account`{.interpreted-text
role="guilabel"} defined for the `Payment Journal`{.interpreted-text
role="guilabel"} must be a valid IBAN.
:::

::: {.tip}
::: {.title}
Tip
:::

You can also test SEPA direct debit payments using the
`payment_providers/test-mode`{.interpreted-text role="ref"}.
:::

::: {.seealso}
`../payment_providers`{.interpreted-text role="doc"}
:::

Online payments with `SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"}
-----------------------------------------------------------------------------

Customers selecting `SDD (SEPA Direct Debit)`{.interpreted-text
role="abbr"} as a payment method are prompted to enter their IBAN to
complete the
`SEPA Direct Debit mandate <accounting/batch_sdd/sdd_mandates>`{.interpreted-text
role="ref"}.

The `SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"} mandate is
then automatically created in `Draft`{.interpreted-text role="guilabel"}
based on the provided IBAN. To validate the information, customers must
confirm each new mandate with a successful bank transfer of the expected
amount **using the specified payment reference (communication)** defined
in the
`SEPA Direct Debit payment provider's form <sdd/configuration>`{.interpreted-text
role="ref"}. Once this initial payment is received and
`reconciled <../accounting/bank/reconciliation>`{.interpreted-text
role="doc"}, the mandate is automatically validated and updated to the
`Active`{.interpreted-text role="guilabel"} status. Once a mandate is
active, it is reused for all subsequent payments made with the
`SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"} payment method.
You can then collect them by
`uploading them to your online banking interface <accounting/batch_sdd/XML>`{.interpreted-text
role="ref"}.

::: {.seealso}
`../accounting/payments/batch_sdd`{.interpreted-text role="doc"}
:::

::: {.note}
::: {.title}
Note
:::

\- Mandates are automatically
`closed <accounting/batch_sdd/close-revoke-mandate>`{.interpreted-text
role="ref"} 36 months after the date of the last collection. -
`SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"} is also
available as a payment method through other providers, such as
`adyen`{.interpreted-text role="doc"}, `buckaroo`{.interpreted-text
role="doc"}, and `stripe`{.interpreted-text role="doc"}. In these cases,
`SDD (SEPA Direct Debit)`{.interpreted-text role="abbr"} mandates are
handled externally by the payment provider.
:::
