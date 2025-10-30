# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/flutterwave.md

Flutterwave
===========

 is an online payments provider
established in Nigeria and covering several African countries and
payment methods.

Configuration on Flutterwave Dashboard {#payment_providers/flutterwave/configure_dashboard}
--------------------------------------

1.  Log into 
    and go to `Settings --> API`{.interpreted-text
    role="menuselection"}. Copy the values of the
    `Public Key`{.interpreted-text role="guilabel"} and
    `Secret Key`{.interpreted-text role="guilabel"} fields and save them
    for later.

2.  | Go to `Settings --> Webhooks`{.interpreted-text
      role="menuselection"} and enter your Odoo database URL followed by
      [/payment/flutterwave/webhook]{.title-ref} in the
      `URL`{.interpreted-text role="guilabel"} text field.
    | For example:
      [https://yourcompany.odoo.com/payment/flutterwave/webhook]{.title-ref}.

3.  Fill the `Secret hash`{.interpreted-text role="guilabel"} with a
    password that you generate and save its value for later.

4.  Make sure *all* the remaining checkboxes are ticked.

5.  Click on **Save** to finalize the configuration.



Configuration on Odoo {#payment_providers/flutterwave/configure_odoo}
---------------------

1.  `Navigate to the payment provider Flutterwave <payment_providers/add_new>`{.interpreted-text
    role="ref"} and change its state to `Enabled`{.interpreted-text
    role="guilabel"}.

2.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill
    the `Public Key`{.interpreted-text role="guilabel"},
    `Secret Key`{.interpreted-text role="guilabel"}, and
    `Webhook Secret`{.interpreted-text role="guilabel"} with the values
    you saved at the step
    `payment_providers/flutterwave/configure_dashboard`{.interpreted-text
    role="ref"}.

3.  Configure the rest of the options to your liking.

    ::: {.important}
    ::: {.title}
    Important
    :::

    If you choose to allow saving payment methods, it is recommended to
    only enable card payments from Flutterwave dashboard, as only cards
    can be saved as payment tokens. To do so, go to your Flutterwave
    Dashboard and then to
    `Settings --> Account Settings`{.interpreted-text
    role="menuselection"}.
    :::

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::
