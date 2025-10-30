Online signatures for order confirmations
=========================================

The Odoo *Sales* application provides customers with the ability to
confirm orders, via an online signature, directly on the sales order.
Once the sales order is electronically signed by the customer, the
salesperson attached to the sales order is instantly notified that the
order is confirmed.

Activate online signatures
--------------------------

In order to have customers confirm orders with an online signature, the
*Online Signature* feature **must** be activated.

To activate the *Online Signature* feature, go to
`Sales app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, scroll to the
`Quotations \& Orders`{.interpreted-text role="guilabel"} heading, and
activate the `Online Signature`{.interpreted-text role="guilabel"}
feature by checking the box beside it.

{.align-center}

Then, click the `Save`{.interpreted-text role="guilabel"} button in the
top-left corner.

::: {.note}
::: {.title}
Note
:::

When making a quotation template, the online signature feature is the
`Signature`{.interpreted-text role="guilabel"} option, located in the
`Online confirmation`{.interpreted-text role="guilabel"} field of the
quotation template form.

{.align-center}

On standard quotations, the online signature feature is the
`Signature`{.interpreted-text role="guilabel"} option, located under the
`Other Info`{.interpreted-text role="guilabel"} tab of the quotation
form.

{.align-center}
:::

Order confirmations with online signatures
------------------------------------------

When clients access quotations online through their customer portal,
there\'s a `Sign \&
Pay`{.interpreted-text role="guilabel"} button directly on the
quotation.

{.align-center}

When clicked, a `Validate Order`{.interpreted-text role="guilabel"}
pop-up window appears. In this pop-up window, the
`Full Name`{.interpreted-text role="guilabel"} field is auto-populated,
based on the contact information in the database.

{.align-center}

Then, customers have the option to enter an online signature with any of
the following options: `Auto`{.interpreted-text role="guilabel"},
`Draw`{.interpreted-text role="guilabel"}, or `Load`{.interpreted-text
role="guilabel"}.

`Auto`{.interpreted-text role="guilabel"} lets Odoo automatically
generate an online signature based on the information in the
`Full Name`{.interpreted-text role="guilabel"} field.
`Draw`{.interpreted-text role="guilabel"} lets the customer use the
cursor to create a custom signature directly on the pop-up window. And
`Load`{.interpreted-text role="guilabel"} lets the customer upload a
previously-created signature file from their computer.

After the customer has chosen any of the three previously mentioned
signature options (`Auto`{.interpreted-text role="guilabel"},
`Draw`{.interpreted-text role="guilabel"}, or `Load`{.interpreted-text
role="guilabel"}), they will click the `Accept \&
Sign`{.interpreted-text role="guilabel"} button.

When `Accept \& Sign`{.interpreted-text role="guilabel"} is clicked, the
various payment method options become available for them to choose from
(if the *online payment* option applies to this quotation).

Then, when the quotation is paid and confirmed, a delivery order is
automatically created (if the Odoo *Inventory* app is installed).

::: {.seealso}
\- `quote_template`{.interpreted-text role="doc"} -
`get_paid_to_validate`{.interpreted-text role="doc"}
:::
