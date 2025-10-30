# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/razorpay.md

Razorpay
========

 is an online payments provider
established in India that supports more than 100 payment methods.

Create a Razorpay account with Odoo (Indian companies only) {#payment_providers/razorpay/oauth-connection}
-----------------------------------------------------------

::: {.note}
::: {.title}
Note
:::

\- This method is only available for Indian companies. - This flow does
not support the
`test mode <payment_providers/test-mode>`{.interpreted-text role="ref"}.
:::

1.  `Navigate to the Razorpay payment provider <payment_providers/supported_providers>`{.interpreted-text
    role="ref"} and click `Connect`{.interpreted-text role="guilabel"}.

2.  Go through the account creation process and enter the verification
    codes when prompted.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    If you already have a Razorpay account, enter your Razorpay
    credentials, select the account you want to link to your Odoo
    database (if applicable), then click `Continue`{.interpreted-text
    role="guilabel"}.
    :::

3.  At the end of the process, click `Authorize`{.interpreted-text
    role="guilabel"}. If all required information has been submitted,
    you are then redirected to Odoo, and the payment provider is
    `Enabled`{.interpreted-text role="guilabel"}.

Manual credentials and webhook input {#payment_providers/razorpay/manual-connection}
------------------------------------

### Razorpay configuration {#payment_providers/razorpay/configure_dashboard}

1.   if
    necessary and log into the [Razorpay
    Dashboard](https://dashboard.razorpay.com/).

2.  Go to the `Payments`{.interpreted-text role="guilabel"} tab at the
    top of the page.

3.  Toggle the `Test Mode`{.interpreted-text role="guilabel"} switch in
    the left menu to try the integration without charging customers.
    Toggle it off once you are ready to accept real payments.

4.  Click `Account & Settings`{.interpreted-text role="guilabel"} in the
    left menu, then, under `Website and app
    settings`{.interpreted-text role="guilabel"}, select [API
    Keys](https://dashboard.razorpay.com/app/website-app-settings/api-keys).

5.  Copy the values of the `Key Id`{.interpreted-text role="guilabel"}
    and `Secret Key`{.interpreted-text role="guilabel"} fields and save
    them for later.

6.  Click `Account & Settings`{.interpreted-text role="guilabel"} in the
    left menu, then, under `Website and app
    settings`{.interpreted-text role="guilabel"}, select
    .

7.  | Click `Add New Webhook`{.interpreted-text role="guilabel"}, then
      enter your Odoo database URL followed by
      [/payment/razorpay/webhook]{.title-ref} in the
      `Webhook URL`{.interpreted-text role="guilabel"} field.
    | For example:
      [https://example.odoo.com/payment/razorpay/webhook]{.title-ref}.

8.  Fill the `Secret`{.interpreted-text role="guilabel"} field with a
    password of your choice and save it for later.

9.  Enable the following events: `payment.authorized`{.interpreted-text
    role="guilabel"}, `payment.captured`{.interpreted-text
    role="guilabel"}, `payment.failed`{.interpreted-text
    role="guilabel"}, `refund.failed`{.interpreted-text
    role="guilabel"}, and `refund.processed`{.interpreted-text
    role="guilabel"}.

10. Click `Create Webhook`{.interpreted-text role="guilabel"} to
    finalize the configuration.

::: {#payment_providers/razorpay/recurring_payments}
::: {.important}
::: {.title}
Important
:::

The [Recurring
payments](https://razorpay.com/docs/payments/recurring-payments/)
feature must be activated to accept recurring payments. To enable this
feature, submit a request to the [Razorpay Support
team](https://razorpay.com/support/#request).
:::
:::

### Odoo configuration {#payment_providers/razorpay/configure_odoo}

1.  Activate `developer mode <developer-mode>`{.interpreted-text
    role="ref"}.
2.  `Navigate to the Razorpay payment provider <payment_providers/add_new>`{.interpreted-text
    role="ref"}.
3.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill
    the `Key Id`{.interpreted-text role="guilabel"},
    `Key Secret`{.interpreted-text role="guilabel"}, and
    `Webhook Secret`{.interpreted-text role="guilabel"} with the values
    you saved during
    `payment_providers/razorpay/configure_dashboard`{.interpreted-text
    role="ref"}.
4.  Configure the remaining options as needed.
5.  Set the `State`{.interpreted-text role="guilabel"} field to
    `Enabled`{.interpreted-text role="guilabel"} (or
    `Test Mode`{.interpreted-text role="guilabel"} if you are trying
    Razorpay as a `test <payment_providers/test-mode>`{.interpreted-text
    role="ref"}).

::: {.important}
::: {.title}
Important
:::

If you configure Odoo to
`capture amounts manually <payment_providers/manual_capture>`{.interpreted-text
role="ref"}:

-   **Manual voiding** of a transaction is not supported by Razorpay.
-   Transactions that remain uncaptured for more than **five days** are
    automatically **voided**.
:::

::: {.seealso}
`../payment_providers`{.interpreted-text role="doc"}
:::
