Quotation deadlines
===================

In the Odoo *Sales* application, it is possible to set deadlines on
sales quotations. Doing so encourages customers to act quickly during
sales negotiations, for they might fear for missing out on a good deal.
As well, deadlines also can also act as protection for a company in case
an order has to be fulfilled at a price that is no longer profitable for
the business.

Quotation expiration
--------------------

In Odoo *Sales*, there\'s the option to add an expiration date to a
quotation.

To add an expiration date to a quotation, navigate to
`Sales app`{.interpreted-text role="menuselection"}, and select a
desired quotation, or create a new one by clicking
`New`{.interpreted-text role="guilabel"}.

On the quotation form, click the `Expiration`{.interpreted-text
role="guilabel"} field to reveal a pop-up calendar. From this pop-up
calendar, select the desired month and date as the expiration date for
the quotation.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

By clicking the `Preview`{.interpreted-text role="guilabel"} button on a
quotation, Odoo clearly displays when that specific offer expires.

{.align-center}
:::

Quotation template expiration
-----------------------------

The Odoo *Sales* application also makes it possible to add a deadline
expiration date to quotation templates.

To add a deadline expiration date to a quotation template, navigate to
`Sales app -->
Configuration --> Quotation Templates`{.interpreted-text
role="menuselection"}, and either select the desired quotation template
to which a deadline should be added, or click `New`{.interpreted-text
role="guilabel"} to build a new quotation template from scratch.

On the quotation template form, add a specific number of days to the
`Quotation expires
after`{.interpreted-text role="guilabel"} field, located beneath the
quotation template name. The number of days represents how long the
quotation will be valid for, before it expires.

{.align-center}

Then, whenever that specific quotation template is used in a quote, an
expiration date is automatically calculated, based on the number of days
designated above. However, this date can be overwritten before sending
the quotation to the customer.

::: {.seealso}
`/applications/sales/sales/send_quotations/quote_template`{.interpreted-text
role="doc"}
:::
