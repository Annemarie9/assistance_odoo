# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/stripe.md

Stripe
======

 is a United States-based online payment
solution provider allowing businesses to accept **credit cards** and
other payment methods.

::: {.seealso}
\-  -
[List of payment methods supported by
Stripe](https://stripe.com/payments/payment-methods)
:::

Create your Stripe account with Odoo
------------------------------------

The method to acquire your credentials depends on your hosting type:

::: {.tabs}
.. group-tab:: Odoo Online

1.  `Navigate to the payment provider Stripe <payment_providers/supported_providers>`{.interpreted-text
    role="ref"} and click `Connect Stripe`{.interpreted-text
    role="guilabel"}.
2.  Go through the setup process and confirm your email address when
    Stripe sends you a confirmation email.
3.  At the end of the process, click
    `Agree and submit`{.interpreted-text role="guilabel"}. If all
    requested information has been submitted, you are then redirected to
    Odoo, and your payment provider is enabled.

::: {.group-tab}
Odoo.sh or On-premise
:::

1.  `Navigate to the payment provider Stripe <payment_providers/supported_providers>`{.interpreted-text
    role="ref"} and click `Connect Stripe`{.interpreted-text
    role="guilabel"}.
2.  Go through the setup process and confirm your email address when
    Stripe sends you a confirmation email.
3.  At the end of the process, click
    `Agree and submit`{.interpreted-text role="guilabel"}; you are then
    redirected to the payment provider **Stripe** in Odoo.
4.  `Fill in your credentials <stripe/api_keys>`{.interpreted-text
    role="ref"}.
5.  `Generate a webhook <stripe/webhook>`{.interpreted-text role="ref"}.
6.  Set the `State`{.interpreted-text role="guilabel"} field to
    `Enabled`{.interpreted-text role="guilabel"}.
:::

::: {.tip}
::: {.title}
Tip
:::

\- To use an existing Stripe account,
`activate the Developer mode <developer-mode>`{.interpreted-text
role="ref"} and
`enable Stripe manually <payment_providers/add_new>`{.interpreted-text
role="ref"}. You can then `Fill in your
credentials <stripe/api_keys>`{.interpreted-text role="ref"},
`generate a webhook <stripe/webhook>`{.interpreted-text role="ref"}, and
enable the payment provider. - You can also test Stripe using the
`payment_providers/test-mode`{.interpreted-text role="ref"}. To do so,
first, [log into your Stripe
dashboard](https://dashboard.stripe.com/dashboard) and switch to the
**Test mode**. Then, in Odoo,
`activate the Developer mode <developer-mode>`{.interpreted-text
role="ref"},
`navigate to the payment provider Stripe <payment_providers/supported_providers>`{.interpreted-text
role="ref"},
`fill in your API credentials <stripe/api_keys>`{.interpreted-text
role="ref"} with the test keys, and set the `State`{.interpreted-text
role="guilabel"} field to `Test Mode`{.interpreted-text
role="guilabel"}.
:::

### Fill in your credentials {#stripe/api_keys}

If your **API credentials** are required to connect with your Stripe
account, proceed as follows:

1.  Go to [the API keys page on
    Stripe](https://dashboard.stripe.com/account/apikeys), or log into
    your Stripe dashboard and go to
    `Developers --> API Keys`{.interpreted-text role="menuselection"}.
2.  In the `Standard keys`{.interpreted-text role="guilabel"} section,
    copy the `Publishable key`{.interpreted-text role="guilabel"} and
    the `Secret key`{.interpreted-text role="guilabel"} and save them
    for later.
3.  In Odoo,
    `navigate to the payment provider Stripe <payment_providers/supported_providers>`{.interpreted-text
    role="ref"}.
4.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill in
    the `Publishable Key`{.interpreted-text role="guilabel"} and
    `Secret Key`{.interpreted-text role="guilabel"} fields with the
    values you previously saved.

### Generate a webhook {#stripe/webhook}

If your **Webhook Signing Secret** is required to connect with your
Stripe account, you can create a webhook automatically or manually.

::: {.tabs}
.. tab:: Create the webhook automatically

Make sure your
`Publishable and Secret keys <stripe/api_keys>`{.interpreted-text
role="ref"} are filled in, then click
`Generate your webhook`{.interpreted-text role="guilabel"}.

::: {.tab}
Create the webhook manually
:::

1.  Go to the [Webhooks page on
    Stripe](https://dashboard.stripe.com/webhooks), or log into your
    Stripe dashboard and go to
    `Developers --> Webhooks`{.interpreted-text role="menuselection"}.
2.  In the `Hosted endpoints`{.interpreted-text role="guilabel"}
    section, click `Add endpoint`{.interpreted-text role="guilabel"}.
    Then, in the `Endpoint URL`{.interpreted-text role="guilabel"}
    field, enter your Odoo database\'s URL, followed by
    [/payment/stripe/webhook]{.title-ref}, e.g.,
    [https://yourcompany.odoo.com/payment/stripe/webhook]{.title-ref}.
3.  Click `Select events`{.interpreted-text role="guilabel"} at the
    bottom of the form, then select the following events:
    -   in the `Charge`{.interpreted-text role="guilabel"} section:
        `charge.refunded`{.interpreted-text role="guilabel"} and
        `charge.refund.updated`{.interpreted-text role="guilabel"};
    -   in the `Payment intent`{.interpreted-text role="guilabel"}
        section:
        `payment_intent.amount_capturable_updated`{.interpreted-text
        role="guilabel"},
        `payment_intent.payment_failed`{.interpreted-text
        role="guilabel"}, `payment_intent.processing`{.interpreted-text
        role="guilabel"}, and
        `payment_intent.succeeded`{.interpreted-text role="guilabel"};
    -   in the `Setup intent`{.interpreted-text role="guilabel"}
        section: `setup_intent.succeeded`{.interpreted-text
        role="guilabel"}.
4.  Click `Add events`{.interpreted-text role="guilabel"}.
5.  Click `Add endpoint`{.interpreted-text role="guilabel"}, then click
    `Reveal`{.interpreted-text role="guilabel"} and save your
    `Signing secret`{.interpreted-text role="guilabel"} for later.
6.  In Odoo, `navigate to the payment provider Stripe
    <payment_providers/supported_providers>`{.interpreted-text
    role="ref"}.
7.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill
    the `Webhook Signing Secret`{.interpreted-text role="guilabel"}
    field with the value you previously saved.

::: {.note}
::: {.title}
Note
:::

You can select other events, but they are currently not processed by
Odoo.
:::
:::

Enable Apple Pay
----------------

To allow customers to use the Apple Pay button to pay their eCommerce
orders, go to the `Configuration`{.interpreted-text role="guilabel"}
tab, enable `Allow Express Checkout`{.interpreted-text role="guilabel"},
and click `Enable Apple Pay`{.interpreted-text role="guilabel"}.

::: {.seealso}
\-
`Express checkout and Google Pay <payment_providers/express_checkout>`{.interpreted-text
role="ref"} - `../payment_providers`{.interpreted-text role="doc"} -
`Use Stripe as a payment terminal in Point of Sale <../../sales/point_of_sale/payment_methods/terminals/stripe>`{.interpreted-text
role="doc"}
:::
