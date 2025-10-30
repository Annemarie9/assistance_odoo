# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/payments.md

Payment providers
=================

Odoo supports a multitude of online
`payment providers </applications/finance/payment_providers>`{.interpreted-text
role="doc"} for your website, allowing your customers to pay with their
preferred payment methods.

::: {.seealso}
\-
`/applications/sales/sales/products_prices/ewallets_giftcards`{.interpreted-text
role="doc"} - `checkout`{.interpreted-text role="doc"}
:::

Configuration
-------------

To set up payment providers on the eCommerce app, go to
`Website --> Configuration
--> Payment Providers`{.interpreted-text role="menuselection"}. From
here, `Activate`{.interpreted-text role="guilabel"} the payment
providers you wish to have available on your shop, and configure them
according to your needs.

Alternatively, you can access **payment providers** via
`Website --> Configuration
--> Settings`{.interpreted-text role="menuselection"}. In the
`Shop - Payment`{.interpreted-text role="guilabel"} section, you can
`Configure SEPA Direct
Debit`{.interpreted-text role="guilabel"} if you wish to use it, as well
as `View other providers`{.interpreted-text role="guilabel"}. If you use
the `Authorize.net`{.interpreted-text role="guilabel"} payment provider,
the
`Payment Capture Method <payment_providers/manual_capture>`{.interpreted-text
role="ref"} can be configured in that same menu.

If you are using
`/applications/finance/payment_providers/paypal`{.interpreted-text
role="doc"}, you can also enable and configure it here.

### Checkout payment options

Once activated, customers can choose the payment provider of their
choice during the **checkout process**, at the
`Confirm Order`{.interpreted-text role="guilabel"} step.

{.align-center}

eWallets and gift cards
-----------------------

When checking out, customers can pay with an eWallet or gift cards. To
enable these, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and in the `Shop-Products`{.interpreted-text
role="guilabel"} section, enable
`Discounts, Loyalty & Gift Card`{.interpreted-text
role="menuselection"}.

Once enabled, customers can enter their gift card **code** or pay with
their eWallet at the checkout step.

{.align-center}

::: {.seealso}
`/applications/sales/sales/products_prices/ewallets_giftcards`{.interpreted-text
role="doc"}
:::
