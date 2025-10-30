Returns and refunds
===================

The Odoo *Sales* app provides two different ways to process returns. The
method used depends on whether or not an invoice has been sent.

Before invoicing
----------------

Returns are completed using *Reverse Transfers* when a customer decides
to return a product **before** an invoice has been sent or validated.

::: {.note}
::: {.title}
Note
:::

In order to use *Reverse Transfers*, the *Inventory* app **must** be
installed.
:::

To start a return before invoicing, navigate to the
`Sales`{.interpreted-text role="menuselection"} app, select the desired
sales order, and click on the `Delivery`{.interpreted-text
role="guilabel"} smart button to open the associated delivery order.

{.align-center}

On the validated delivery order, click `Return`{.interpreted-text
role="guilabel"}.

{.align-center}

This opens a `Reverse Transfer`{.interpreted-text role="guilabel"}
pop-up window.

By default, the `Quantity`{.interpreted-text role="guilabel"} matches
the validated quantities from the delivery order. Update the quantities,
if necessary. Click on the `🗑️ (trash)`{.interpreted-text
role="guilabel"} icon next to a line item to remove it from the return.

{.align-center}

Next, click `Return`{.interpreted-text role="guilabel"} to confirm the
return. This generates a new warehouse operation for the incoming
returned product(s).

{.align-center}

Upon receiving the return, the warehouse team validates the warehouse
operation by clicking `Validate`{.interpreted-text role="guilabel"}.
Then, on the original sales order, the `Delivered`{.interpreted-text
role="guilabel"} quantity updates to reflect the difference between the
initial validated quantities and the returned quantities.

{.align-center}

When an invoice is created, the customer receives an invoice **only**
for the products they are keeping, if any.

After invoicing
---------------

Sometimes, customers return an item after they receive and/or pay for
their invoice. In these cases, a return using only *Reverse Transfers*
is insufficient since validated, or sent, invoices cannot be changed.

However, *Reverse Transfers* can be used in conjunction with *Credit
Notes* to complete the customer\'s return.

To start a return after invoicing, navigate to the relevant sales order
in the `Sales`{.interpreted-text role="menuselection"} app.

If there is a payment registered on the sales order, the payment details
appear in the chatter, and the invoice (accessible through the
`Invoices`{.interpreted-text role="guilabel"} smart button) has a green
`In
Payment`{.interpreted-text role="guilabel"} banner.

{.align-center}

From the sales order, click on the `Delivery`{.interpreted-text
role="guilabel"} smart button to view the validated delivery order.
Then, click `Return`{.interpreted-text role="guilabel"} to open the
`Reverse Transfer`{.interpreted-text role="guilabel"} pop-up window.

Next, edit the `Product`{.interpreted-text role="guilabel"} and/or
`Quantity`{.interpreted-text role="guilabel"}, as needed for the return.
Then, click `Return`{.interpreted-text role="guilabel"}. This generates
a new warehouse operation for the incoming returned product(s), which is
validated by the warehouse team once the return is received by clicking
`Validate`{.interpreted-text role="guilabel"}.

Then, on the sales order, the `Delivered`{.interpreted-text
role="guilabel"} quantity updates to reflect the difference between the
initial validated quantities and the returned quantities.

To process a refund, navigate to the relevant invoice (from the sales
order, click on the `Invoices`{.interpreted-text role="guilabel"} smart
button). Then, click the `Credit Note`{.interpreted-text
role="guilabel"} button at the top of the validated invoice.

{.align-center}

Doing so reveals a `Credit Note`{.interpreted-text role="guilabel"}
pop-up form.

{.align-center}

Start by entering a `Reason displayed on Credit Note`{.interpreted-text
role="guilabel"} and a specific `Journal`{.interpreted-text
role="guilabel"} to process the credit. Then, select a specific
`Reversal Date`{.interpreted-text role="guilabel"}.

After the information is filled in, click `Reverse`{.interpreted-text
role="guilabel"} or `Reverse and Create
Invoice`{.interpreted-text role="guilabel"}. Then, edit the draft, if
needed.

Lastly, click `Confirm`{.interpreted-text role="guilabel"} to confirm
the credit note.

When complete, a blue banner reading:
`You have outstanding credits for this customer. You
can allocate them to mark this invoice as paid.`{.interpreted-text
role="guilabel"} appears at the top of the page.

::: {.seealso}
`../../../finance/accounting/customer_invoices/credit_notes`{.interpreted-text
role="doc"}
:::
