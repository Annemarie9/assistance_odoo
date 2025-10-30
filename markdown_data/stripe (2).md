Stripe
======

Connecting a payment terminal allows you to offer a fluid payment flow
to your customers and ease the work of your cashiers.

::: {.important}
::: {.title}
Important
:::

\- Stripe payment terminals do not require an
`IoT Box </applications/general/iot>`{.interpreted-text role="doc"} -
Stripe terminals can be used in many countries, but not worldwide. Check
the [global availability for Stripe
Terminal](https://support.stripe.com/questions/global-availability-for-stripe-terminal).
- Stripe\'s integration works with [Stripe Terminal smart
readers](https://docs.stripe.com/terminal/smart-readers)
:::

::: {.seealso}
\-
`Stripe as payment provider <../../../../finance/payment_providers/stripe>`{.interpreted-text
role="doc"} - [List of payment methods supported by
Stripe](https://stripe.com/payments/payment-methods)
:::

Configuration
-------------

### Configure the payment method

Activate **Stripe** in the settings by going to
`Point of Sale --> Configuration -->
Settings --> Payment Terminals`{.interpreted-text role="menuselection"}
and enabling `Stripe`{.interpreted-text role="guilabel"}.

Then, create the payment method:

-   Go to
    `Point of Sale --> Configuration --> Payment Methods`{.interpreted-text
    role="menuselection"}, click `Create`{.interpreted-text
    role="guilabel"}, and complete the `Method`{.interpreted-text
    role="guilabel"} field with your payment method\'s name;
-   Set the `Journal`{.interpreted-text role="guilabel"} field as
    `Bank`{.interpreted-text role="guilabel"} and the
    `Use a Payment Terminal`{.interpreted-text role="guilabel"} field as
    `Stripe`{.interpreted-text role="guilabel"};
-   Enter your payment terminal serial number in the
    `Stripe Serial Number`{.interpreted-text role="guilabel"} field;
-   Click
    `Don't forget to complete Stripe connect before using this payment method.`{.interpreted-text
    role="guilabel"}

{.align-center}

::: {.note}
::: {.title}
Note
:::

\- Click `Identify Customer`{.interpreted-text role="guilabel"} to allow
this payment method **exclusively** for identified customers. For any
unidentified customers to be able to pay with Stripe, leave the
`Identify Customer`{.interpreted-text role="guilabel"} field unchecked.
- The `Outstanding Account`{.interpreted-text role="guilabel"} and the
`Intermediary Account`{.interpreted-text role="guilabel"} can stay empty
to use the default accounts. - Find your payment terminal serial number
under the device or on [Stripe\'s
dashboard](https://dashboard.stripe.com).
:::

### Connect Stripe to Odoo

Click `Connect Stripe`{.interpreted-text role="guilabel"}. Doing so
redirects you automatically to a configuration page. Fill in all the
information to create your Stripe account and link it with Odoo. Once
the forms are completed, the API keys
(`Publishable Key`{.interpreted-text role="guilabel"} and
`Secret Key`{.interpreted-text role="guilabel"}) can be retrieved on
**Stripe\'s** website. To do so, click
`Get your Secret and Publishable keys`{.interpreted-text
role="guilabel"}, click the keys to copy them, and paste them into the
corresponding fields in Odoo. Your terminal is ready to be configured in
a POS.

{.align-center}

::: {.note}
::: {.title}
Note
:::

\- When you use **Stripe** exclusively in Point of Sale, you only need
the **Secret Key** to use your terminal. - When you use Stripe as
**payment provider**, the `State`{.interpreted-text role="guilabel"} can
stay set as `Disabled`{.interpreted-text role="guilabel"}. - For
databases hosted **On-Premise**, the `Connect Stripe`{.interpreted-text
role="guilabel"} button does not work. To retrieve the API keys
manually, log in to your [Stripe
dashboard](https://dashboard.stripe.com), type [API]{.title-ref} in the
search bar, and click `Developers > API`{.interpreted-text
role="guilabel"}.
:::

### Configure the payment terminal

Swipe right on your payment terminal, click `Settings`{.interpreted-text
role="guilabel"}, enter the admin PIN code, validate and select your
network.

::: {.note}
::: {.title}
Note
:::

\- The user\'s device and the terminal must share the same network. - In
case of a Wi-Fi connection, the network must be secured. - You must
enter the admin PIN code to access your payment terminal settings. By
default, this code is [07139]{.title-ref}.
:::

### Link the payment method to a POS

To add a **payment method** to your point of sale, go to
`Point of Sale -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Select the POS, scroll down to the `Payments`{.interpreted-text
role="guilabel"} section, and add your payment method for **Stripe** in
the `Payment Methods`{.interpreted-text role="guilabel"} field.

Troubleshooting
---------------

### Payment terminal unavailable in your Stripe account

If the payment terminal is unavailable in your Stripe account, you must
add it manually:

1.  Log into your 
    and go to
    `Stripe dashboard --> Payments --> Readers --> Locations`{.interpreted-text
    role="menuselection"};
2.  Add a location by clicking the `+ New`{.interpreted-text
    role="guilabel"} button or selecting an already created location;
3.  Click the `+ New`{.interpreted-text role="guilabel"} button in the
    `Readers`{.interpreted-text role="guilabel"} box and fill in the
    required information.

::: {.note}
::: {.title}
Note
:::

You must provide a **registration code**. To retrieve that code, swipe
right on your device, enter the admin PIN code (by default:
[07139]{.title-ref}), validate, and click `Generate a
registration code`{.interpreted-text role="guilabel"}.
:::
