show-content

:   

Payment methods
===============

To add a payment method, you first need to create it. Go to
`Point of Sale -->
Configuration --> Payment Methods --> New`{.interpreted-text
role="menuselection"}, and set a name. Check
`Identify Customer`{.interpreted-text role="guilabel"} to allow this
payment method *exclusively* for registered customers.

Then, select the `Journal`{.interpreted-text role="guilabel"}. Choose
`Cash`{.interpreted-text role="guilabel"} to use this payment method for
cash payments, or `Bank`{.interpreted-text role="guilabel"} to use it
for card payments.



::: {.note}
::: {.title}
Note
:::

Selecting a `bank`{.interpreted-text role="guilabel"} journal
automatically adds the `Use a Payment Terminal`{.interpreted-text
role="guilabel"} field in which you can add your
`payment terminal's information
<payment_methods/terminals>`{.interpreted-text role="doc"}.
:::

::: {.seealso}
`payment_methods/terminals`{.interpreted-text role="doc"}.
:::

Once the payment method is created, you can select it in your POS
settings. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"},
click `Edit`{.interpreted-text role="guilabel"}, and add the payment
method under the `Payments`{.interpreted-text role="guilabel"} section.

::: {.toctree titlesonly=""}
payment\_methods/terminals
:::
