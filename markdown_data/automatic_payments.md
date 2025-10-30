Subscriptions and automatic payments
====================================

By default, the **Subscriptions** app will automatically generate
quotations and invoices for customers, but it can also support automatic
payments. Setting up automatic payments requires additional
configuration, including choosing an automatic payment provider and
either setting up a customer portal or an **eCommerce** website. Here\'s
an overview of how to get started.

Setting up a payment processor that supports automatic payments
---------------------------------------------------------------

Setting up automatic recurring payments requires using a payment
provider that supports tokenization. Tokenization lets customers save
their payment details, such as credit card or banking account
information, for automatic billing. The following payment providers
support tokenization:

-   `Adyen <../../finance/payment_providers/adyen>`{.interpreted-text
    role="doc"}
-   `Authorize.net <../../finance/payment_providers/authorize>`{.interpreted-text
    role="doc"}
-   `Flutterwave <../../finance/payment_providers/flutterwave>`{.interpreted-text
    role="doc"}
-   `Razorpay <../../finance/payment_providers/razorpay>`{.interpreted-text
    role="doc"}
-   `Stripe <../../finance/payment_providers/stripe>`{.interpreted-text
    role="doc"}
-   `Xendit <../../finance/payment_providers/xendit>`{.interpreted-text
    role="doc"}

Here are the steps to setting up automatic payments.

1.  Choose a payment provider that supports tokenization.
2.  Follow the provider\'s own setup guide to create an account and
    begin configuring their API credentials in Odoo.
3.  `Enable <payment_providers/add_new>`{.interpreted-text role="ref"}
    the payment provider.
4.  `Configure the payment methods <payment_providers/payment_methods>`{.interpreted-text
    role="ref"} for the chosen payment provider.
5.  `Configure the tokenization <payment_providers/tokenization>`{.interpreted-text
    role="ref"} for the chosen payment provider.

How customers can set up automatic payments
-------------------------------------------

Once these steps are complete, payment providers will be able to create
tokens with customers\' saved payment details during the checkout
process. Saved payment details can then be used for future online or
recurring subscription charges. Customers will also be able to log into
their `customer portal <../../general/users/portal>`{.interpreted-text
role="doc"} and enter their payment information there.

Some payment providers will automatically save customers\' payment
information as part of the checkout process. Others will give them the
option to save their information for future payments. If customers
choose not to save their payment information, they will not be able to
make automatic payments.

::: {.important}
::: {.title}
Important
:::

Building an **eCommerce** website requires the
`Website <../../websites/website>`{.interpreted-text role="doc"} app.
:::

What happens if an automatic payment fails?
-------------------------------------------

When an automatic payment fails, the sales order is updated with:

-   a `Payment Failure`{.interpreted-text role="guilabel"} tag
-   the `Contract in exception`{.interpreted-text role="guilabel"}
    checkbox ticked (in the `Subscription`{.interpreted-text
    role="guilabel"} section of the `Other Info`{.interpreted-text
    role="guilabel"} tab).

Being marked `Contract in exception`{.interpreted-text role="guilabel"}
prevents scheduled actions from running, which keeps the system from
accidentally double-charging the customer if the automatic payment
actually went through. Because the status of the payment failed to
register with the system, users must manually check if the payment has
been made before automatic payments and other scheduled actions can
resume.

To do this, navigate to
`Subscriptions app --> Subscriptions --> Quotations`{.interpreted-text
role="menuselection"}. Click into the desired subscription, then check
the Chatter to see if the payment was made.

If the payment *was not* made, first enter
`developer mode <../../general/developer_mode>`{.interpreted-text
role="doc"}. Then, click the `Other Info`{.interpreted-text
role="guilabel"} tab, and untick the checkbox next to `Contract in
exception`{.interpreted-text role="guilabel"}. Reload the sales order
and confirm that the `Payment Failure`{.interpreted-text
role="guilabel"} tag is gone.

If the payment *was* made, a new invoice must be made and posted
manually. This automatically updates the next invoice date of the
subscription. Once the invoice is created, enter
`developer mode <../../general/developer_mode>`{.interpreted-text
role="doc"} and navigate to the new sales order. Click the
`Other Info`{.interpreted-text role="guilabel"} tab, and untick the
checkbox next to `Contract in exception`{.interpreted-text
role="guilabel"}. Reload the sales order and confirm that the
`Payment Failure`{.interpreted-text role="guilabel"} tag is gone.



The `Contract in exception`{.interpreted-text role="guilabel"} option
selected with the `Payment Failure`{.interpreted-text role="guilabel"}
tag shown.

In both cases, once the `Contract in exception`{.interpreted-text
role="guilabel"} checkbox is no longer ticked, Odoo handles renewals
automatically again. If the subscription remains in
`Payment Failure`{.interpreted-text role="guilabel"}, it is ignored by
Odoo until the sales order is closed.

::: {.seealso}
\- `../../finance/payment_providers`{.interpreted-text role="doc"} -
`../../general/users/portal`{.interpreted-text role="doc"}
:::
