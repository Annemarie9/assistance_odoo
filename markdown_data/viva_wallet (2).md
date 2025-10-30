Viva Wallet
===========

Connecting a **Viva Wallet**
`payment terminal <../terminals>`{.interpreted-text role="doc"} allows
you to offer a fluid payment flow to your customers and ease the work of
your cashiers.

::: {.note}
::: {.title}
Note
:::

Viva Wallet lets you turn your phone into a mobile card reader: [Tap On
Phone](https://www.vivawallet.com/gb_en/blog-tap-on-phone-gb).
:::

Configuration
-------------

Start by creating your Viva Wallet account on [Viva Wallet\'s
website](https://www.vivawallet.com).

### Locate your Viva Wallet credentials

When configuring Viva Wallet in Point of Sale, you need to use specific
credentials that are available in your Viva Wallet account. These
credentials include your `Merchant ID
<viva_wallet/id-key>`{.interpreted-text role="ref"},
`API key <viva_wallet/id-key>`{.interpreted-text role="ref"},
`POS API credentials
<viva_wallet/pos-api>`{.interpreted-text role="ref"}, and
`Terminal ID <viva_wallet/identifier>`{.interpreted-text role="ref"}
number.

#### Merchant ID and API key {#viva_wallet/id-key}

Locate your [Merchant ID and API key following the Viva
documentation](https://developer.vivawallet.com/getting-started/find-your-account-credentials/merchant-id-and-api-key/).
Then, save the keys and paste them into the Odoo
`Merchant ID`{.interpreted-text role="guilabel"} and
`API Key`{.interpreted-text role="guilabel"} fields
`when creating the payment method <viva_wallet/method-creation>`{.interpreted-text
role="ref"}.



::: {.note}
::: {.title}
Note
:::

These credentials are used for APIs that authenticate with Basic Auth.
:::

#### POS API credentials {#viva_wallet/pos-api}

Locate and generate your [POS API credentials following the Viva
documentation](https://developer.vivawallet.com/getting-started/find-your-account-credentials/pos-api-credentials/).
Then, save the keys and paste them in the Odoo
`Client secret`{.interpreted-text role="guilabel"} and
`Client ID`{.interpreted-text role="guilabel"} fields
`when creating the payment method <viva_wallet/method-creation>`{.interpreted-text
role="ref"}.

::: {.warning}
::: {.title}
Warning
:::

These credentials are only displayed once. Ensure you keep a copy to
secure them.
:::



::: {.note}
::: {.title}
Note
:::

These credentials are used for Android and iOS POS Activation requests,
as well as the Cloud Terminal API.
:::

#### Terminal ID {#viva_wallet/identifier}

Your terminal ID number is used to identify your terminal. To find it:

1.  Go to your Viva Wallet account and select the relevant account.
2.  Go to
    `Sales --> Physical payments --> Card terminals`{.interpreted-text
    role="menuselection"} in the navigation menu.

The terminal ID number is located under the
`Terminal ID (TID)`{.interpreted-text role="guilabel"} column. Save it
to paste it into the `Terminal ID`{.interpreted-text role="guilabel"}
field `when creating the payment method
<viva_wallet/method-creation>`{.interpreted-text role="ref"}.



### Configure the payment method {#viva_wallet/method-creation}

1.  `Activate the POS Viva Wallet module <../../../../general/apps_modules>`{.interpreted-text
    role="doc"} to enable the payment terminal.
2.  `Create the related payment method <../../payment_methods>`{.interpreted-text
    role="doc"} by going to
    `Point of Sale --> Configuration --> Payment Methods`{.interpreted-text
    role="menuselection"} and clicking `New`{.interpreted-text
    role="guilabel"}.
3.  Set the journal type as `Bank`{.interpreted-text role="guilabel"}.
4.  Select `Viva Wallet`{.interpreted-text role="guilabel"} in the
    `Use a Payment Terminal`{.interpreted-text role="guilabel"} field.
5.  Fill in the mandatory fields with your:
    -   `Merchant ID and API key <viva_wallet/ID-key>`{.interpreted-text
        role="ref"}
    -   `Client ID and Client secret <viva_wallet/pos-api>`{.interpreted-text
        role="ref"}
    -   `Terminal ID <viva_wallet/identifier>`{.interpreted-text
        role="ref"}
6.  Save the form and copy the generated webhook URL from the
    `Viva Wallet Webhook
    Endpoint`{.interpreted-text role="guilabel"} field. This URL is
    necessary
    `when configuring the webhook <viva_wallet/webhook>`{.interpreted-text
    role="ref"}.



### Configure the webhook {#viva_wallet/webhook}

Webhooks allow you to receive real-time notifications whenever a
transaction occurs within your Viva Wallet account. Set them up for
[payment transactions following the Viva
documentation](https://developer.vivawallet.com/webhooks-for-payments/transaction-payment-created/).

::: {.seealso}
[Setting up
webhooks](https://developer.viva.com/webhooks-for-payments/#setting-up-webhooks)
:::

### Link the payment method to a POS

You can select the payment method in your POS settings once the payment
method is created. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"}
and add the payment method under the `Payment methods`{.interpreted-text
role="guilabel"} field of the `Payment`{.interpreted-text
role="guilabel"} section.
