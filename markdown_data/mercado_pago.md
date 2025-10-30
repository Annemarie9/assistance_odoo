Mercado Pago
============

Connecting a payment terminal allows you to offer a fluid payment flow
to your customers and ease the work of your cashiers.

::: {.important}
::: {.title}
Important
:::

Only **Point Smart** payment terminals in Argentina, Brazil, Chile,
Colombia, Mexico, Peru, and Uruguay are supported. They can be purchased
on [Mercado Pago\'s
website](https://www.mercadopago.com.mx/herramientas-para-vender/lectores-point).
:::

::: {.seealso}
[Mercado Pago online
payments](https://www.mercadopago.com.mx/herramientas-para-vender/check-out#benefits-checkout)
:::

Configuration {#pos-mercado-pago-configuration}
-------------

1.  Create a .

2.  Associate your Point Smart terminal with a `store`{.interpreted-text
    role="guilabel"} and a `cash drawer`{.interpreted-text
    role="guilabel"} by following [Mercado Pago\'s
    documentation](https://vendedores.mercadolibre.com.ar/nota/locales-una-herramienta-para-mejorar-la-gestion-de-tus-puntos-de-venta/).

    ::: {.note}
    ::: {.title}
    Note
    :::

    All purchased terminals are automatically displayed on your Mercado
    dashboard.
    :::

3.  Set your Point Smart terminal to the
    `Point of Sale`{.interpreted-text role="guilabel"} operation mode.

    ::: {.warning}
    ::: {.title}
    Warning
    :::

    Odoo does not support the `Standalone`{.interpreted-text
    role="guilabel"} operation mode.
    :::

4.  `Create a Point Smart application <pos-mercado-pago-application>`{.interpreted-text
    role="ref"}.

5.  `Generate your credentials <pos-mercado-pago-credentials>`{.interpreted-text
    role="ref"}.

6.  `Create and configure the related payment method <pos-mercado-pago-method>`{.interpreted-text
    role="ref"}.

### Point Smart application {#pos-mercado-pago-application}

Create a new application from Mercado Pago\'s [developer
panel](https://www.mercadopago.com/developers) by following [Mercado
Pago\'s applications
documentation](https://www.mercadopago.com.mx/ayuda/20152), making sure
you select `In
person Payments`{.interpreted-text role="guilabel"}.

### Credentials {#pos-mercado-pago-credentials}

Once the Point Smart application is created, three credentials are
required:

-   An access token that Odoo uses to call Mercado Pago.
-   A webhook secret key that Odoo uses to authenticate notifications
    sent by Mercado Pago.
-   The **terminal serial number** at the back of your Point Smart
    terminal.

Retrieve the access token and webhook secret key by following [Mercado
Pago\'s credentials
documentation](https://www.mercadopago.com.mx/developers/en/docs/your-integrations/credentials).
Then, copy and paste them into Odoo when creating the payment method.

::: {.important}
::: {.title}
Important
:::

For the webhooks configuration, add the URL of your Odoo database (e.g.,
[https://mycompany.odoo.com]{.title-ref}) followed by
[/pos\_mercado\_pago/notification]{.title-ref} (e.g.,
[https://mycompany.odoo.com/pos\_mercado\_pago/notification]{.title-ref}).


:::

### Payment method {#pos-mercado-pago-method}

1.  `Activate the POS Mercado Pago module <../../../../general/apps_modules>`{.interpreted-text
    role="doc"} to enable the payment terminal.
2.  `Create the related payment method <../../payment_methods>`{.interpreted-text
    role="doc"} by going to
    `Point of Sale --> Configuration --> Payment Methods`{.interpreted-text
    role="menuselection"}.
3.  Set the journal type as `Bank`{.interpreted-text role="guilabel"}
4.  Select `Mercado Pago`{.interpreted-text role="guilabel"} in the
    `Use a Payment Terminal`{.interpreted-text role="guilabel"} field.
5.  Fill in the mandatory fields with the
    `previously generated credentials
    <pos-mercado-pago-credentials>`{.interpreted-text role="ref"}:
    -   Fill in the `Production user token`{.interpreted-text
        role="guilabel"} field using the access token.
    -   Fill in the `Production secret key`{.interpreted-text
        role="guilabel"} field using the webhook secret key.
    -   Fill in the `Terminal S/N`{.interpreted-text role="guilabel"}
        field using the terminal serial number. You can find it at the
        back of your terminal.
    -   Click the `Force PDV`{.interpreted-text role="guilabel"} button
        to activate the Point of Sale mode.



Select the payment method by going to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"}
and adding it to the payment method under the
`Payment Methods`{.interpreted-text role="guilabel"} field of the
`Payment`{.interpreted-text role="guilabel"} section.

::: {.important}
::: {.title}
Important
:::

Any action made on the terminal should trigger a notification on the POS
interface. Ensure the
`webhook secret key <pos-mercado-pago-credentials>`{.interpreted-text
role="ref"} is correctly configured if you are not notified.
:::
