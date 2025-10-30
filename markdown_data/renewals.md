Renew subscriptions
===================

The foundation of any subscription business model is recurring payments.
This is when customers reliably pay a regular amount at specific
intervals, in exchange for access to a subscription product or service.

Subscription renewal is the process customers follow when they willingly
choose to continue participating in, and paying for, a subscription
product or service.

Subscribers experience the renewal process at different intervals \--
weekly, monthly, annually, etc. \-- depending on the duration of the
agreed-upon contract.

Most companies that offer subscriptions prefer to automate the renewal
process for customers. However, manual subscription renewals are still
used in some cases.

With the Odoo **Subscriptions** application, a company can manage all of
its subscriptions in one place. Renewals can be processed automatically,
or manually, include additional products or upsells per renewal order,
and be filtered in batch views to quickly locate customers who need to
renew their subscriptions.

Subscription renewals
---------------------

In order to renew a subscription, a quotation with a subscription
product **must** be confirmed, with a configured *Recurring Plan*
selected.

To open a subscription quotation, navigate to
`Subscriptions app --> Subscriptions
--> Quotations`{.interpreted-text role="menuselection"}, and select the
desired quotation from the list. Or, create a new one by clicking
`New`{.interpreted-text role="guilabel"} to open a new quotation form.

::: {.note}
::: {.title}
Note
:::

\- Only a singular product is required. - A subscription service counts
as a product, as it is considered a recurring product.
:::

Subscription quotations **must** be confirmed, and payment from the
customer for the initial subscription **must** be invoiced and
registered in order to successfully open a *Renewal Quotation*.

::: {.seealso}
For more information on the above process of confirming quotations and
invoicing payments, see: -
`../sales/send_quotations/create_quotations`{.interpreted-text
role="doc"} -
`../sales/send_quotations/get_paid_to_validate`{.interpreted-text
role="doc"}
:::

Once the payment from the subscription quotation is confirmed, the
quotation turns into a sales order. An `In Progress`{.interpreted-text
role="guilabel"} tag is applied to the sales order form, and a series of
buttons also appear at the top of the sales order, including a
`Renew`{.interpreted-text role="guilabel"} button.

{.align-center}

When the `Renew`{.interpreted-text role="guilabel"} button is clicked,
Odoo instantly presents a new renewal quotation, complete with a
`Renewal Quotation`{.interpreted-text role="guilabel"} tag.

{.align-center}

From here, a standard sales flow can occur to confirm the quotation.
This typically begins by clicking `Send by Email`{.interpreted-text
role="guilabel"}, which sends a copy of the quotation to the customer,
by email, for them to confirm, and eventually, pay for.

::: {.note}
::: {.title}
Note
:::

In the chatter of the `Renewal Quotation`{.interpreted-text
role="guilabel"}, it is mentioned that this subscription is the renewal
of the subscription from the original sales order.
:::

Once the `Renewal Quotation`{.interpreted-text role="guilabel"} is
confirmed, it becomes a sales order, and a
`Sales History`{.interpreted-text role="guilabel"} smart button appears
at the top of the page.

{.align-center}

When that `Sales History`{.interpreted-text role="guilabel"} smart
button is clicked, Odoo reveals a separate page, showcasing the
different sales orders attached to this subscription, along with their
individual `Subscription Status`{.interpreted-text role="guilabel"}.

{.align-center}

Additionally, once the `Renewal Quotation`{.interpreted-text
role="guilabel"} is confirmed, an `MRR`{.interpreted-text
role="guilabel"} smart button also appears at the top of the sales
order.

{.align-center}

When clicked, Odoo reveals an `MRR Analysis`{.interpreted-text
role="guilabel"} page, detailing the monthly recurring revenue related
to this specific subscription.

::: {.seealso}
\- `../subscriptions`{.interpreted-text role="doc"}
:::
