# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/demo.md

Demo
====

Odoo\'s **Demo Payment Provider** allows you to test business flows
involving online transactions without requiring real banking
credentials.

Configuration
-------------

::: {.seealso}
`payment_providers/add_new`{.interpreted-text role="ref"}
:::

::: {.important}
::: {.title}
Important
:::

Switch the state to `Test Mode`{.interpreted-text role="guilabel"}.
:::

Payment outcome
---------------

Upon checkout or when paying a bill online, you can choose the payment
outcome when using the demo payment provider. To do so, click on the
`Payment Status`{.interpreted-text role="guilabel"} drop-down menu and
select the desired outcome.

{.align-center}

Transaction state
-----------------

If you selected `Pending`{.interpreted-text role="guilabel"} as
**payment outcome**, you can change the state of the transaction
straight from its form view. To access a transaction\'s form view,
activate the `developer mode <developer-mode>`{.interpreted-text
role="ref"}, and go to `Accounting / Website -->
Configuration --> Payment Transactions`{.interpreted-text
role="menuselection"}. Then, change the status of a transaction by
clicking on the state bar
(`Draft, Pending, Authorized, Confirmed, Canceled, Error`{.interpreted-text
role="guilabel"}).

{.align-center}
