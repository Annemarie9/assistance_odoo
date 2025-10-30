Down payments
=============

A down payment is a partial payment made by the buyer when a sales
contract is concluded. This implies both parties\' (seller and buyer)
full commitment to honor the contract.

With a down payment, the buyer pays a portion of the total amount owed
while agreeing to pay the remaining amount at a later date. In turn, the
seller provides goods or services to the buyer after accepting the down
payment, trusting that the remaining amount will be paid later on.

Create invoices
---------------

When a sales order is confirmed, the option to create an invoice becomes
available, via the `Create Invoice`{.interpreted-text role="guilabel"}
button, located in the upper-left corner of the sales order form. When
clicked, a `Create invoices`{.interpreted-text role="guilabel"} pop-up
appears.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Invoices are automatically created as drafts, so they can be reviewed
before validation.
:::

On the `Create invoices`{.interpreted-text role="guilabel"} pop-up,
there are 3 options to choose from in the
`Create Invoice`{.interpreted-text role="guilabel"} field:

-   `Regular invoice`{.interpreted-text role="guilabel"}
-   `Down payment (percentage)`{.interpreted-text role="guilabel"}
-   `Down payment (fixed amount)`{.interpreted-text role="guilabel"}

::: {.note}
::: {.title}
Note
:::

If `Regular Invoice`{.interpreted-text role="guilabel"} is selected, the
other fields disappear, as they only pertain to down payment
configurations.
:::

Initial down payment request
----------------------------

On the `Create invoices`{.interpreted-text role="guilabel"} pop-up form,
the down payment options are:

-   `Down payment (percentage)`{.interpreted-text role="guilabel"}
-   `Down payment (fixed amount)`{.interpreted-text role="guilabel"}

Once the desired down payment option is selected in the
`Create Invoice`{.interpreted-text role="guilabel"} field on the pop-up
form, designate the desired amount, either as a percentage or a fixed
amount, in the `Down Payment Amount`{.interpreted-text role="guilabel"}
field.

Then, select the appropriate income account for the down payment (only
the first time a down payment is created) in the
`Income Account`{.interpreted-text role="guilabel"} field.

{.align-center}

Once all fields are filled in with the desired information, click the
`Create Draft
Invoice`{.interpreted-text role="guilabel"} button. Upon clicking this
button, Odoo reveals the `Customer Invoice Draft`{.interpreted-text
role="guilabel"}.

In the `Invoice Lines`{.interpreted-text role="guilabel"} tab of the
`Customer Invoice Draft`{.interpreted-text role="guilabel"}, the down
payment that was just configured in the
`Create invoices`{.interpreted-text role="guilabel"} pop-up form appears
as a `Product`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When the `Down payment`{.interpreted-text role="guilabel"} product in
the `Invoice Lines`{.interpreted-text role="guilabel"} tab is clicked,
Odoo reveals the product form for the down payment.

By default, the `Product Type`{.interpreted-text role="guilabel"} of
down payment products generated for invoices are set as
`Service`{.interpreted-text role="guilabel"}, with the
`Invoicing Policy`{.interpreted-text role="guilabel"} set to
`Prepaid/Fixed
Price`{.interpreted-text role="guilabel"}.

{.align-center}

This product can be edited/modified at any time.
:::

::: {.warning}
::: {.title}
Warning
:::

If `Based on Delivered Quantity (Manual)`{.interpreted-text
role="guilabel"} is chosen as the `Invoicing
Policy`{.interpreted-text role="guilabel"}, an invoice will **not** be
able to be created.
:::

Example: request 50% down payment {#sales/invoicing/50-percent-down-payments}
---------------------------------

::: {.note}
::: {.title}
Note
:::

The following example involves a 50% amount down payment on a product
(`Cabinet with
Doors`{.interpreted-text role="guilabel"}) with
`Ordered quantities`{.interpreted-text role="guilabel"} as the
`Invoicing Policy`{.interpreted-text role="guilabel"}.

{.align-center}
:::

::: {.seealso}
`invoicing_policy`{.interpreted-text role="doc"}
:::

First, navigate to `Sales app --> New`{.interpreted-text
role="menuselection"}, and add a `Customer`{.interpreted-text
role="guilabel"} to the quotation.

Then, click `Add a product`{.interpreted-text role="guilabel"} in the
`Order Lines`{.interpreted-text role="guilabel"} tab, and select the
`Cabinet with Doors`{.interpreted-text role="guilabel"} product.

When the order is confirmed (via the `Confirm`{.interpreted-text
role="guilabel"} button), the quotation turns into a sales order. Once
this occurs, create and view the invoice by clicking
`Create Invoice`{.interpreted-text role="guilabel"}.

{.align-center}

Next, on the `Create invoices`{.interpreted-text role="guilabel"} pop-up
window that appears, select `Down payment
(percentage)`{.interpreted-text role="guilabel"}, and type
[50]{.title-ref} in the `Down Payment Amount`{.interpreted-text
role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Income Account`{.interpreted-text role="guilabel"} field is *not* a
required field, and it does *not* appear if it has already been
preconfigured in previous down payment requests.

For more information, check out the documentation on
`income account modification on down
payments <sales/invoicing/income-account-modification>`{.interpreted-text
role="ref"}.
:::

Lastly, click `Create Draft Invoice`{.interpreted-text role="guilabel"}
to create and view the invoice draft.

Clicking `Create Draft Invoice`{.interpreted-text role="guilabel"}
reveals the draft invoice, which includes the down payment as a
`Product`{.interpreted-text role="guilabel"} in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

From there, the invoice can be confirmed and posted by clicking
`Confirm`{.interpreted-text role="guilabel"}. Confirming the invoice
changes the status from `Draft`{.interpreted-text role="guilabel"} to
`Posted`{.interpreted-text role="guilabel"}. It also reveals a new
series of buttons at the top of the page.

{.align-center}

From those buttons, the payment can be registered by clicking
`Register Payment`{.interpreted-text role="guilabel"}.

{.align-center}

Doing so reveals a `Register Payment`{.interpreted-text role="guilabel"}
pop-up form, which is auto-populated with the necessary information.
Confirm the information provided is correct, and make any necessary
adjustments. When ready, click the `Create Payment`{.interpreted-text
role="guilabel"} button.

{.align-center}

After clicking `Create Payment`{.interpreted-text role="guilabel"}, Odoo
reveals the customer invoice, now with a green
`In Payment`{.interpreted-text role="guilabel"} banner in the
upper-right corner.

{.align-center}

Now, when the customer wants to pay the remaining amount of the order,
another invoice must be created. To do that, return to the sales order,
via the breadcrumb links.

Back on the sales order, a new `Down Payments`{.interpreted-text
role="guilabel"} section is present in the `Order
Lines`{.interpreted-text role="guilabel"} tab, along with the down
payment that was just invoiced and posted.

{.align-center}

Next, click the `Create Invoice`{.interpreted-text role="guilabel"}
button.

On the `Create invoices`{.interpreted-text role="guilabel"} pop-up
window that appears, there are two new fields:
`Already invoiced`{.interpreted-text role="guilabel"} and
`Amount to invoice`{.interpreted-text role="guilabel"}.

{.align-center}

If the remaining amount is ready to be paid, select the
`Regular Invoice`{.interpreted-text role="guilabel"} option. Odoo will
create an invoice for the exact amount needed to complete the total
payment, as indicated in the `Amount to invoice`{.interpreted-text
role="guilabel"} field.

Once ready, click `Create Draft Invoice`{.interpreted-text
role="guilabel"}.

Doing so reveals another `Customer Invoice Draft`{.interpreted-text
role="guilabel"} page, listing *all* the invoices for that specific
sales order in the `Invoice Lines`{.interpreted-text role="guilabel"}
tab. Each invoice line item displays all the necessary information
related to each invoice.

To complete the flow, click `Confirm`{.interpreted-text
role="guilabel"}, which changes the status of the invoice from
`Draft`{.interpreted-text role="guilabel"} to `Posted`{.interpreted-text
role="guilabel"}. Then, click `Register Payment`{.interpreted-text
role="guilabel"}.

Once again, the `Register Payment`{.interpreted-text role="guilabel"}
appears, with all fields auto-populated with the necessary information,
including the remaining amount left to be paid on the order.

{.align-center}

After confirming that information, click
`Create Payment`{.interpreted-text role="guilabel"}. Doing so reveals
the final `Customer Invoice`{.interpreted-text role="guilabel"} with a
green `In Payment`{.interpreted-text role="guilabel"} banner in the
upper-right corner. Also, both down payments are present in the
`Invoice Lines`{.interpreted-text role="guilabel"} tab.

{.align-center}

At this point, the flow is now complete.

::: {.note}
::: {.title}
Note
:::

This flow is also possible with the `Fixed amount`{.interpreted-text
role="guilabel"} down payment option.
:::

::: {.important}
::: {.title}
Important
:::

If a down payment is used with a product that has a
`Delivered quantities`{.interpreted-text role="guilabel"} invoicing
policy, and the cost of the product *exceeds* the 50% down payment (as
in most cases), a regular invoice is created.

However, for products that cost *less* than the 50% down payment, the
down payments will **not** be able to be deducted when it comes time to
invoice the customer.

This is because the product(s) would have to be delivered *before*
creating the final invoice due to Odoo not allowing negative totals for
invoices.

If nothing has been delivered, a `Credit Note`{.interpreted-text
role="guilabel"} is created, which cancels the draft invoice that was
created after the down payment.

To utilize the `Credit Note`{.interpreted-text role="guilabel"} option,
the *Inventory* application must be installed, in order to confirm the
delivery. Otherwise, the delivered quantity can be entered manually
directly on the sales order.
:::

Example: request 100% down payment {#sales/invoicing/100-percent-down-payments}
----------------------------------

The process of requesting a 100% down payment is similar to the process
of setting up a `50%
down payment <sales/invoicing/50-percent-down-payments>`{.interpreted-text
role="ref"}, but with fewer steps.

::: {.note}
::: {.title}
Note
:::

A 100% down payment is **not** the same as a full payment of the sales
order.

A sales order paid through the regular invoice process will not allow
any additional invoices to be generated, and **will not** display the
*Create Invoice* button on the Sales Order.

Following this example **will** cause the *Create Invoice* button to be
displayed on the Sales Order. This is because Odoo expects another
invoice to be created after the down payment to complete payment of the
sales order.
:::

The *Solar Panel Installation* product is being used in this example.

To configure a 100% down payment, begin by navigating to
`Sales app --> New`{.interpreted-text role="menuselection"}, and add a
`Customer`{.interpreted-text role="guilabel"} to the quote.

Next, click `Add a product`{.interpreted-text role="guilabel"} in the
`Order Lines`{.interpreted-text role="guilabel"} tab, and select the
[Solar Panel Installation]{.title-ref} product.

Upon clicking the `Confirm`{.interpreted-text role="guilabel"} button,
the quotation turns into a sales order. At that point, an invoice can
now be created by clicking `Create Invoice`{.interpreted-text
role="guilabel"} in the top-left corner.

On the `Create invoices`{.interpreted-text role="guilabel"} pop-up
window that appears, select `Down payment
(percentage)`{.interpreted-text role="guilabel"}, and type
[100]{.title-ref} in the `Down Payment Amount`{.interpreted-text
role="guilabel"} field. Then, if desired, select an
`Income Account`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Income Account`{.interpreted-text role="guilabel"} and
`Customer Taxes`{.interpreted-text role="guilabel"} fields are *not*
required fields, and they will *not* appear if they\'ve already been
preconfigured in previous down payment requests.

For more information, check out the documentation on
`income account modification on down
payments <sales/invoicing/income-account-modification>`{.interpreted-text
role="ref"}.
:::

{.align-center}

Next, click `Create Draft Invoice`{.interpreted-text role="guilabel"} to
create an invoice draft. This will also bring the draft invoice into
view, which includes the `Down payment`{.interpreted-text
role="guilabel"} as a `Product`{.interpreted-text role="guilabel"} in
the `Invoice Lines`{.interpreted-text role="guilabel"} tab. The taxes on
the down payment invoices are broken down in proportion of the sales
order lines taxes.

The invoice can now be confirmed and posted by clicking
`Confirm`{.interpreted-text role="guilabel"}. Confirming the invoice
changes the status from `Draft`{.interpreted-text role="guilabel"} to
`Posted`{.interpreted-text role="guilabel"}. It also reveals a new
series of buttons at the top of the page.

The payment can be registered by clicking the
`Register Payment`{.interpreted-text role="guilabel"} button.

Doing so reveals a `Register Payment`{.interpreted-text role="guilabel"}
pop-up form, which is auto-populated with the necessary information.
Confirm the information provided is correct and make any necessary
adjustments. When ready, click the `Create Payment`{.interpreted-text
role="guilabel"} button.

After clicking `Create Payment`{.interpreted-text role="guilabel"}, Odoo
reveals the customer invoice, now with a green
`In Payment`{.interpreted-text role="guilabel"} banner in the
upper-right corner.

{.align-center}

The process is now complete, and the 100% down payment has been
successfully applied.

Income account modification on down payments {#sales/invoicing/income-account-modification}
--------------------------------------------

To change or adjust the income account attached to the
`Down Payment`{.interpreted-text role="guilabel"} product page, the
*Accounting* app **must** be installed.

Navigate to the `Products`{.interpreted-text role="guilabel"} page
(`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"}), search for the [Down Payment]{.title-ref}
product in the search bar, and select it to reveal the product detail
page.

With the *Accounting* app installed, the `Accounting`{.interpreted-text
role="guilabel"} tab becomes available on the product page.

In the `Accounting`{.interpreted-text role="guilabel"} tab, the income
account can be changed in the `Income
Account`{.interpreted-text role="guilabel"} field, located in the
`Receivables`{.interpreted-text role="guilabel"} section.

{.align-center}

::: {.seealso}
`invoicing_policy`{.interpreted-text role="doc"}
:::
