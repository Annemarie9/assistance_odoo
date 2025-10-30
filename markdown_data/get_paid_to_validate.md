Online payment order confirmation
=================================

The Odoo *Sales* application provides customers with the ability to
confirm orders, via an online payment, directly on a sales order. Once
the sales order is electronically paid for by the customer, the
salesperson attached to the sales order is instantly notified that the
order is confirmed.

Activate online payments
------------------------

In order to have customers confirm orders with an online payment, the
*Online Payment* setting **must** be activated.

To activate the *Online Payment* feature, go to
`Sales app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, scroll to the
`Quotations \& Orders`{.interpreted-text role="guilabel"} heading, check
the box next to the `Online Payment`{.interpreted-text role="guilabel"}
feature, and click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

Beneath the `Online Payment`{.interpreted-text role="guilabel"} option
on the *Sales* `Settings`{.interpreted-text role="guilabel"} page,
there\'s a `Default Quotation Validity`{.interpreted-text
role="guilabel"} field. In this field, there\'s the option to add a
specific number of days for quotations to remain valid by default.

To enable this feature on a standard quotation, click the checkbox for
the `Payment`{.interpreted-text role="guilabel"} feature option, located
in the `Online confirmation`{.interpreted-text role="guilabel"} field,
on the `Other Info`{.interpreted-text role="guilabel"} tab.

{.align-center}

To enable this feature on a quotation template, click the checkbox for
the `Payment`{.interpreted-text role="guilabel"} feature option, located
in the `Online confirmation`{.interpreted-text role="guilabel"} field of
the quotation template form.

{.align-center}

Payment providers
-----------------

After activating the `Online Payment`{.interpreted-text role="guilabel"}
feature, a link to configure `Payment
Providers`{.interpreted-text role="guilabel"} appears beneath it.

Clicking that link reveals a separate
`Payment Providers`{.interpreted-text role="guilabel"} page, in which a
large variety of payment providers can be enabled, customized, and
published.

{.align-center}

::: {.seealso}
`../../../finance/payment_providers`{.interpreted-text role="doc"}
:::

Register a payment
------------------

After opening quotations in their customer portal, customers can click
`Accept \& Pay`{.interpreted-text role="guilabel"} to confirm their
order with an online payment.

{.align-center}

After clicking `Accept \& Pay`{.interpreted-text role="guilabel"},
customers are presented with `Validate Order`{.interpreted-text
role="guilabel"} pop-up window containing different options for them to
make online payments, in the `Pay
with`{.interpreted-text role="guilabel"} section.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Odoo will **only** offer payment options on the
`Validate Order`{.interpreted-text role="guilabel"} pop-up window that
have been published and configured on the
`Payment Providers`{.interpreted-text role="guilabel"} page.
:::

Once the customer selects their desired method of payment, they will
click the `Pay`{.interpreted-text role="guilabel"} button on the pop-up
window to confirm the order. Odoo instantly notifies the assigned
salesperson upon order confirmation with an online payment.

{.align-center}

::: {.seealso}
\- `quote_template`{.interpreted-text role="doc"} -
`get_signature_to_validate`{.interpreted-text role="doc"} -
`../../../finance/payment_providers`{.interpreted-text role="doc"}
:::
