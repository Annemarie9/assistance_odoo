# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/mercado_pago.md

Mercado Pago
============

 is an online payment
provider covering several countries, currencies and payment methods in
Latin America.

Configuration on Mercado Pago Dashboard {#payment_providers/mercado_pago/configure_dashboard}
---------------------------------------

1.  Log into the [Mercado Pago
    Dashboard](https://www.mercadopago.com.mx/developers/panel) and
    select your application or create a new one.
2.  Select `Credenciales de producción`{.interpreted-text
    role="guilabel"} in the left part of the application page, then
    select the industry, optionally enter your domain, and click
    `Activar credenciales
    de producción`{.interpreted-text role="guilabel"}.
3.  Copy the `Access token`{.interpreted-text role="guilabel"} and save
    it for later.

::: {.tip}
::: {.title}
Tip
:::

If you are trying Mercado Pago as a test, select
`Credienciales de prueba`{.interpreted-text role="guilabel"} in the left
part of the application page, then copy the test
`Access token`{.interpreted-text role="guilabel"}.
:::



Configuration on Odoo {#payment_providers/mercado_pago/configure_odoo}
---------------------

1.  `Navigate to the payment provider Mercado Pago <payment_providers/add_new>`{.interpreted-text
    role="ref"} and change its state to `Enabled`{.interpreted-text
    role="guilabel"}.
2.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill in
    the `Access Token`{.interpreted-text role="guilabel"} with the value
    you saved at the
    `payment_providers/mercado_pago/configure_dashboard`{.interpreted-text
    role="ref"} step.
3.  Configure the rest of the options to your liking.

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"} - [Mercado Pago
Odoo webinar](https://www.youtube.com/watch?v=CX8vPHMb1ic)
:::
