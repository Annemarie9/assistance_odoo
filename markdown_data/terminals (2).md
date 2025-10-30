show-content

:   

Payment terminals
=================

Connecting and integrating a payment terminal with your POS system
allows you to accept multiple payment options, including credit and
debit cards, making the payment process more efficient.

Configuration {#terminals/configuration}
-------------

Go to the
`application settings <configuration/settings>`{.interpreted-text
role="ref"}, scroll down to the `Payment Terminals`{.interpreted-text
role="guilabel"} section, and tick your terminal\'s checkbox.



Then, follow the corresponding documentation to configure your device:

-   `Adyen configuration <terminals/adyen>`{.interpreted-text
    role="doc"}
-   `Ingenico configuration <terminals/ingenico>`{.interpreted-text
    role="doc"}
-   `Mercado Pago configuration <terminals/mercado_pago>`{.interpreted-text
    role="doc"}
-   `Razorpay configuration <terminals/razorpay>`{.interpreted-text
    role="doc"}
-   `SIX configuration <terminals/six>`{.interpreted-text role="doc"}
-   `Stripe configuration <terminals/stripe>`{.interpreted-text
    role="doc"}
-   `Vantiv configuration <terminals/vantiv>`{.interpreted-text
    role="doc"}
-   `Viva Wallet configuration <terminals/viva_wallet>`{.interpreted-text
    role="doc"}
-   `Worldline configuration <terminals/worldline>`{.interpreted-text
    role="doc"}

Once the terminal is configured, you can
`create the corresponding payment method and add it to
the POS <../payment_methods>`{.interpreted-text role="doc"}.

Pay with a payment terminal
---------------------------

When processing a payment, select the terminal\'s payment method. Check
the amount and click on `Send`{.interpreted-text role="guilabel"}. Once
the payment is successful, the status changes to `Payment
Successful`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- \| In case of connection issues between Odoo and the payment
terminal, force the payment by clicking on
`Force Done`{.interpreted-text role="guilabel"}, which allows you to
validate the order. \| This option is only available after receiving an
error message informing you that the connection failed. - To cancel the
payment request, click on `Cancel`{.interpreted-text role="guilabel"}.
:::

::: {.toctree titlesonly=""}
terminals/adyen terminals/ingenico terminals/mercado\_pago
terminals/razorpay terminals/six terminals/stripe terminals/vantiv
terminals/viva\_wallet terminals/worldline
:::
