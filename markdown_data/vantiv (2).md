Vantiv
======

Connecting a Vantiv payment terminal allows you to offer a fluid payment
flow to your customers and ease the work of your cashiers.

::: {.note}
::: {.title}
Note
:::

Please note MercuryPay only operates with US and Canadian banks, making
this procedure only suitable for North American businesses.
:::

::: {.warning}
::: {.title}
Warning
:::

Vantiv card readers should be purchased exclusively from Vantiv, as
certain Vantiv terminals bought on Amazon do not include the correct
encryption needed to be used with an Odoo database.
:::

Configuration
-------------

### Configure the payment method

Enable the payment terminal in the `Payment Terminals`{.interpreted-text
role="guilabel"} section `of the application
settings <configuration/settings>`{.interpreted-text role="ref"}.

Then, go to
`Point of Sale --> Configuration --> Payment Methods`{.interpreted-text
role="menuselection"}, and `create
the related payment method <../../payment_methods>`{.interpreted-text
role="doc"}. Set the journal type as `Bank`{.interpreted-text
role="guilabel"} and select `Vantiv`{.interpreted-text role="guilabel"}
in the `Use a Payment Terminal`{.interpreted-text role="guilabel"}
field.

Type the name you want to give to your
`Vantiv Credentials`{.interpreted-text role="guilabel"} and click
`Create
and edit`{.interpreted-text role="guilabel"}. Enter your
`Merchant ID`{.interpreted-text role="guilabel"} and
`Merchant Password`{.interpreted-text role="guilabel"}, then click
`Save & Close`{.interpreted-text role="guilabel"}.



Once the payment method is created, you can select it in your POS
settings. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"}
and add the payment method under the `Payment`{.interpreted-text
role="guilabel"} section.
