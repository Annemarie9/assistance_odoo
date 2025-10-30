Adyen
=====

Connecting an **Adyen payment terminal** allows you to offer a fluid
payment flow to your customers and ease the work of your cashiers.

::: {.important}
::: {.title}
Important
:::

\- Adyen payment terminals do not require an
`IoT Box </applications/general/iot>`{.interpreted-text role="doc"}. -
Adyen terminals can be used in many countries, but not worldwide. Check
the [List of countries supported by
Adyen](https://docs.adyen.com/point-of-sale/what-we-support/supported-languages/).
- Adyen works only with businesses processing more than **\$10 million
annually** or invoicing a minimum of **1,000 transactions per month**.
:::

::: {.seealso}
\- [List of payment methods supported by
Adyen](https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/)
- [List of Adyen
terminals](https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals/)
:::

Configuration
-------------

Start by creating your Adyen account on [Adyen\'s
website](https://www.adyen.com/). Then, board your terminal following
the steps described on your terminal\'s screen.

::: {.seealso}
[Adyen Docs - Payment terminal quickstart
guides](https://docs.adyen.com/point-of-sale/user-manuals)
:::

### Generate an Adyen API key {#adyen/api}

The **Adyen API key** is used to authenticate requests from your Adyen
terminal. To generate an API key, go to your
`Adyen account --> Developers --> API credentials`{.interpreted-text
role="menuselection"}, and **create** new credentials or select
**existing** ones. Click `Generate an API key`{.interpreted-text
role="guilabel"} and save the key to paste it into the Odoo
`Adyen API key`{.interpreted-text role="guilabel"} field at
`the payment method creation
<adyen/method-creation>`{.interpreted-text role="ref"}.

::: {.seealso}
\- [Adyen Docs - API
credentials](https://docs.adyen.com/development-resources/api-credentials#generate-api-key).
:::

### Locate the Adyen terminal identifier {#adyen/identifier}

The **Adyen Terminal Identifier** is the terminal\'s serial number,
which is used to identify the hardware.

To find this number, go to your
`Adyen account --> Point of Sale --> Terminals`{.interpreted-text
role="menuselection"}, select the terminal to link with, and save its
serial number to paste it into the Odoo
`Adyen Terminal Identifier`{.interpreted-text role="guilabel"} field at
`the payment method creation
<adyen/method-creation>`{.interpreted-text role="ref"}.

### Set the Event URLs

For Odoo to know when a payment is made, you must configure the terminal
**Event URLs**. To do so,

1.  Log in to ;
2.  Go to
    `Adyen's dashboard --> Point of Sale --> Terminals`{.interpreted-text
    role="menuselection"} and select the connected terminal;
3.  From the terminal settings, click `Integrations`{.interpreted-text
    role="guilabel"};
4.  Set the
    `Switch to decrypted mode to edit this setting`{.interpreted-text
    role="guilabel"} field as `Decrypted`{.interpreted-text
    role="guilabel"};
5.  Click the **pencil icon** button and enter your server address,
    followed by [/pos\_adyen/notification]{.title-ref} in the
    `Event URLs`{.interpreted-text role="guilabel"} field;
6.  Click `Save`{.interpreted-text role="guilabel"} at the bottom of the
    screen to save changes.

### Configure the payment method {#adyen/method-creation}

Enable the payment terminal
`in the application settings <configuration/settings>`{.interpreted-text
role="ref"} and
`create the related payment method <../../payment_methods>`{.interpreted-text
role="doc"}. Set the journal type as `Bank`{.interpreted-text
role="guilabel"} and select `Adyen`{.interpreted-text role="guilabel"}
in the `Use a Payment Terminal`{.interpreted-text role="guilabel"}
field.

Finally, fill in the mandatory fields with your
`Adyen API key <adyen/api>`{.interpreted-text role="ref"}, `Adyen
Terminal Identifier <adyen/identifier>`{.interpreted-text role="ref"},
and `Adyen Merchant Account`{.interpreted-text role="guilabel"}.



Once the payment method is created, you can select it in your POS
settings. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"},
click `Edit`{.interpreted-text role="guilabel"}, and add the payment
method under the `Payments`{.interpreted-text role="guilabel"} section.
