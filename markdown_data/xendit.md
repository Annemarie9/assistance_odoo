# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/xendit.md

Xendit
======

 is an Indonesian-based payment solution
provider that covers several Southeast Asian countries. It allows
businesses to accept credit cards as well as several local payment
methods.

Configuration on the Xendit Dashboard {#payment_providers/xendit/configure_dashboard}
-------------------------------------

1.  [Create a Xendit
    account](https://dashboard.xendit.co/register/1?referral_code=odooid&countr_code=ID)
    if necessary and log in to the [Xendit
    Dashboard](https://dashboard.xendit.co).
2.  Check your account mode in the top left corner of the page. Use the
    `Test Mode`{.interpreted-text role="guilabel"} to try the
    integration without charging your customers. Switch to
    `Live Mode`{.interpreted-text role="guilabel"} once you are ready to
    accept payments.
3.  Navigate to `Configuration: Settings`{.interpreted-text
    role="menuselection"} in the left part of the application page. In
    the `Developers`{.interpreted-text role="guilabel"} section, click
    [API
    Keys](https://dashboard.xendit.co/settings/developers#api-keys).
4.  Click `Generate Secret Key`{.interpreted-text role="guilabel"}. In
    the popup box, enter any `API key name`{.interpreted-text
    role="guilabel"}, select `Write`{.interpreted-text role="guilabel"}
    for the `Money-in Products`{.interpreted-text role="guilabel"}
    permission and `None`{.interpreted-text role="guilabel"} for all
    other permissions then click `Generate key`{.interpreted-text
    role="guilabel"}.
5.  Confirm your password to display your API key. Copy or download the
    key and **save this information securely for later**. This is the
    only time the API key can be viewed or downloaded.
6.  Once completed, scroll down the page to the
    
    section to generate the webhook token.
7.  Under `Webhook verification token`{.interpreted-text
    role="guilabel"}, click
    `View Webhook Verification Token`{.interpreted-text
    role="guilabel"}, then confirm your password to display the token.
    Save it for later.
8.  In the `Webhook URL`{.interpreted-text role="guilabel"} section,
    enter your Odoo database\'s URL, followed by
    [/payment/xendit/webhook]{.title-ref} (e.g.,
    [https://example.odoo.com/payment/xendit/webhook]{.title-ref}) in
    the field `Invoices paid`{.interpreted-text role="guilabel"} and
    click the `Test and save`{.interpreted-text role="guilabel"} button
    next to it.

Configuration on Odoo
---------------------

1.  `Navigate to the payment provider Xendit <payment_providers/add_new>`{.interpreted-text
    role="ref"} and change its state to `Enabled`{.interpreted-text
    role="guilabel"}.
2.  Fill in the `Secret Key`{.interpreted-text role="guilabel"} and
    `Webhook Token`{.interpreted-text role="guilabel"} fields with the
    information saved at the step
    `payment_providers/xendit/configure_dashboard`{.interpreted-text
    role="ref"}.
3.  Configure the rest of the options to your liking.

::: {.seealso}
`../payment_providers`{.interpreted-text role="doc"}
:::
