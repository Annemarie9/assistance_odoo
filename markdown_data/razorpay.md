Razorpay
========

Connecting a Razorpay payment terminal allows you to offer a fluid
payment flow to your customers and ease the work of your cashiers.

::: {.seealso}
`Use Razorpay as apayment provider. <../../../../finance/payment_providers/razorpay>`{.interpreted-text
role="doc"}
:::

Configuration
-------------

### Locate your Razorpay credentials {#razorpay/credentials}

[Create a Razorpay
account](https://razorpay.com/docs/payments/easy-create-account/) and
set it up on their website.

You need the following credentials to set up the payment method in Odoo:

-   [API
    key](https://razorpay.com/docs/payments/dashboard/account-settings/api-keys/)
-   Razorpay username
-   Razorpay device serial number, which can be found underneath the
    device or on [Razorpay\'s
    dashboard](https://dashboard.razorpay.com/).

### Configure the payment method

1.  `Activate the POS Razorpay module <../../../../general/apps_modules>`{.interpreted-text
    role="doc"} to enable the payment terminal.

2.  `Create the related payment method <../../payment_methods>`{.interpreted-text
    role="doc"} by going to
    `Point of Sale --> Configuration --> Payment Methods`{.interpreted-text
    role="menuselection"}.

    1.  Set the `Journal`{.interpreted-text role="guilabel"} type as
        `Bank`{.interpreted-text role="guilabel"}.
    2.  Select `Razorpay`{.interpreted-text role="guilabel"} in the
        `Use a Payment Terminal`{.interpreted-text role="guilabel"}
        field.
    3.  Enter your username in the `Razorpay Username`{.interpreted-text
        role="guilabel"} field and your device\'s serial number in the
        `Razorpay Device Serial No`{.interpreted-text role="guilabel"}
        field.
    4.  Fill in the `Razorpay API Key`{.interpreted-text
        role="guilabel"} field with the `Razorpay API key
        <razorpay/credentials>`{.interpreted-text role="ref"}.
    5.  Set the `Razorpay Allowed Payment Modes`{.interpreted-text
        role="guilabel"} according to your needs.

    

    ::: {.note}
    ::: {.title}
    Note
    :::

    You can enable the `Razorpay Test Mode`{.interpreted-text
    role="guilabel"} field while testing or keep it unchecked for
    production.
    :::

Once the payment method is created, you can enable it for your POS. To
do so, go to the `POS'
settings <configuration/settings>`{.interpreted-text role="ref"} and add
the payment method under the `Payment`{.interpreted-text
role="guilabel"} section.

::: {.note}
::: {.title}
Note
:::

The terminal must have at least a 10% battery level to use it.
:::
