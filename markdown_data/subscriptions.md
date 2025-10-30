show-content

:   

hide-toc

:   

Subscriptions
=============

The Odoo **Subscriptions** app is designed to manage recurring revenue
through subscription-based products or services. It supports automated
invoicing, renewal management, and customer lifecycle tracking.

Subscriptions can be created manually or automatically through online
sales, with varying options for recurring billing. The app integrates
with other Odoo modules such as **Invoicing**, **CRM**, **Sales**, and
**Helpdesk** to support end-to-end subscription workflows.

::: {.cards}
::: {.card target="subscriptions/renewals" large=""}
Renew a subscription

Understand the core management activity for subscriptions
:::

::: {.card target="subscriptions/upselling" large=""}
Upsell a subscription

Offer more value for current subscribers on the same sales order
:::

::: {.card target="subscriptions/closing" large=""}
Close a subscription

Customize subscription plan templates tailored to various product
offerings
:::

::: {.card target="subscriptions/ecommerce" large=""}
eCommerce integration

Offer subscription products through your Odoo eCommerce store
:::
:::

::: {.seealso}
\- [Odoo Tutorials:
Subscriptions](https://www.odoo.com/slides/subscription-20)
:::

Set up recurring plans
----------------------

To get started with subscription products in Odoo, *recurring plans*
(previously known as *recurrence periods*) must first be configured.

Recurring plans are the time windows in which subscriptions are active
before they renew again. While a subscription is active, customers
receive products or services, and may also have access to additional
benefits such as support desk triage. In terms of payment, these
recurring plans designate how often the customer is charged in order to
maintain the benefits of their subscription.

To configure recurring plans, go to
`Subscriptions app --> Configuration -->
Recurring Plans`{.interpreted-text role="menuselection"}.

By default, the **Subscriptions** app includes a number of common
recurring plans already available, such as `Monthly`{.interpreted-text
role="guilabel"} and `Yearly`{.interpreted-text role="guilabel"}.

Create a new recurring plan by clicking `New`{.interpreted-text
role="guilabel"} on the `Recurring Plans`{.interpreted-text
role="guilabel"} dashboard, to reveal a blank form where the plan
`Name`{.interpreted-text role="guilabel"}, `DETAILS`{.interpreted-text
role="guilabel"}, `SELF-SERVICE`{.interpreted-text role="guilabel"} and
`Pricing`{.interpreted-text role="guilabel"} field values are specified.



::: {.important}
::: {.title}
Important
:::

The [Days]{.title-ref} unit of measure *cannot* be used as a
`Billing Period`{.interpreted-text role="guilabel"} for subscription
products. The daily recurrence period in Odoo is designated for rentals,
and **cannot** be added to subscription-based sales orders.

This limitation is there to avoid sales orders that would generate daily
invoices.
:::

### DETAILS section

After giving the recurring plan a suitable `Name`{.interpreted-text
role="guilabel"} (e.g. [Monthly]{.title-ref}, [Bi-weekly]{.title-ref},
[Quarterly]{.title-ref}, etc.), proceed to the form\'s
`DETAILS`{.interpreted-text role="guilabel"} section to fill out the
following configuration fields:

-   `Billing Period`{.interpreted-text role="guilabel"}: determines the
    recurrence period of the recurring plan. Set the numerical value in
    the text field and contextualize the quantity with a unit of time in
    the corresponding drop-down menu, in `Weeks`{.interpreted-text
    role="guilabel"}, `Months`{.interpreted-text role="guilabel"}, or
    `Years`{.interpreted-text role="guilabel"}.

-   `Automatic Closing`{.interpreted-text role="guilabel"}: a numerical
    value, in days, where the subscription is set to close automatically
    if payment is not made.

    ::: {.example}
    If a subscription is set to renew on the 1st of every month, and the
    `Automatic
    Closing`{.interpreted-text role="guilabel"} value is set to
    [15]{.title-ref} `Days`{.interpreted-text role="guilabel"}, then the
    subscription will close on the 16th of that month if payment is not
    received.
    :::

-   `Company`{.interpreted-text role="guilabel"}: optional assignment,
    if the database has `Multi-company
    <../general/companies/multi_company>`{.interpreted-text role="doc"}
    functionality enabled. Assigning this value will make the recurring
    plan available for that company\'s location, specifically.

-   `Invoice Email Template`{.interpreted-text role="guilabel"}: assigns
    a specific email template to be used in subscriptions invoicing
    communications. The default assignment here is [Invoice:
    Sending]{.title-ref} which contains various dynamic fields that
    autopopulate specific variables across the
    `Subject`{.interpreted-text role="guilabel"} field and
    `Content`{.interpreted-text role="guilabel"} tab, such as the
    customer\'s name, invoice number, total amount invoiced, etc.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Although this field is optional, it is recommended to use it since
    this type of communication fulfills good business practices around
    price transparency, regular customer communication (especially as it
    relates to charged amounts), and helps build contextual financial
    documentation around recurring revenues.

    ![The [Invoice: Sending]{.title-ref} email template is accessible by
    clicking the `fa-arrow-right`{.interpreted-text role="icon"}
    (`Internal link`{.interpreted-text role="guilabel"}) that appears
    after hovering over the `Invoice Email
    Template`{.interpreted-text role="guilabel"} drop-down field in the
    `Recurring Plans`{.interpreted-text role="guilabel"}
    form.](subscriptions/subscriptions-invoice-email-template.png)
    :::

### SELF-SERVICE section

The following optional fields enable customers to take administrative
actions on their own subscriptions. Enabling any of these options may
decrease customer service request volume or increase customer lifetime
value (LTV).

-   `Closable`{.interpreted-text role="guilabel"}: checking this box
    will give customers the power to close their own subscriptions.
    Consider enabling this option to reduce customer service requests
    and improve the overall customer experience; customers that can
    manage their own subscriptions in this way helps offload tedious
    tasks for sales and support teams, and reduces the likelihood of
    negative reviews.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Although this option is generally advisable to enable, sales teams
    with strong customer offboarding processes may consider leaving this
    option unchecked in order to force an interaction that might save
    the subscription or a different form of recurring revenue (such as
    in the case of a lesser subscription or a new trial period with an
    alternative plan).
    :::

-   `Add Products`{.interpreted-text role="guilabel"}: allows customers
    to add new products or edit existing product quantities to their
    recurring sales orders, thereby enabling customer-driven upselling.
    When enabled,
    `Upsell quotations <subscriptions/upselling>`{.interpreted-text
    role="doc"} are generated in Odoo whenever a customer performs a
    quantitative adjustment on their sales order product lines.

-   `Renew`{.interpreted-text role="guilabel"}: enabling this allows
    customers to manually create a `Renewal quotation
    <subscriptions/renewals>`{.interpreted-text role="doc"} for their
    subscription.

-   `Optional Plans`{.interpreted-text role="guilabel"}: adding values
    here from the drop-down field menu enables customers to switch their
    subscription plans, in which case a new subscription quotation or
    renewal quote is created to accommodate the change request.

### Pricing tab

Make product-specific pricing adjustments, as part of the recurring
plan, by adding them to the `Pricing`{.interpreted-text role="guilabel"}
tab order lines. Sequentially add the `Products`{.interpreted-text
role="guilabel"}, along with any respective
`Product Variants`{.interpreted-text role="guilabel"}, and then assign a
`Pricelist`{.interpreted-text role="guilabel"} (if available) and a
`Recurring Price`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Price rules that are added here take precedent over the default pricing
information on the subscription product\'s form. This is meant to
accommodate deals, discounts, and similar pricing adjustment strategies
that would incentivize customers to purchase the recurring plan.
:::

Product form configuration
--------------------------

With recurring plans set up, create a subscription product by navigating
to `Subscriptions app --> Products --> Products`{.interpreted-text
role="menuselection"}, and click either an existing product to edit, or
make a new one by clicking `New`{.interpreted-text role="guilabel"} to
open up the subscription product\'s form.

::: {.note}
::: {.title}
Note
:::

By default, the `Recurring`{.interpreted-text role="guilabel"} option is
already enabled, prompting Odoo to recognize it as a subscription
product. Be sure to leave the `Recurring`{.interpreted-text
role="guilabel"} and `Can be Sold`{.interpreted-text role="guilabel"}
options enabled.
:::



On the product form, configure the following items in the
`General Information`{.interpreted-text role="guilabel"} tab so the
subscription product will function correctly:

-   `Product type`{.interpreted-text role="guilabel"}: this value is
    typically set to a `Service`{.interpreted-text role="guilabel"},
    however other product types may be used depending on the purpose of
    the subscription (e.g., physical product box subscriptions,
    eLearning course, etc.).
-   `Invoicing policy <sales/invoicing/invoicing_policy>`{.interpreted-text
    role="doc"}: set this value to when the customer should be charged
    for their subscription.
-   `Unit of Measure`{.interpreted-text role="guilabel"}: how the
    product should be counted in Odoo, for stock purposes. For most
    subscriptions, the `UoM (Unit of Measure)`{.interpreted-text
    role="abbr"} will be `Units`{.interpreted-text role="guilabel"}.
-   `Sales Price`{.interpreted-text role="guilabel"}: enter the
    recurring cost of the subscription that the customer will pay per
    recurrence period.

::: {.important}
::: {.title}
Important
:::

When creating a subscription for a physical good, selecting the wrong
`Invoicing
Policy`{.interpreted-text role="guilabel"} will lead to errors when
creating invoices. Physical products must be set to
`Ordered quantities`{.interpreted-text role="guilabel"}.
:::

Optionally set up information on the `Attributes & Variants
<sales/products_prices/products/variants>`{.interpreted-text role="doc"}
tab if the subscription contains multiple choices for customers (i.e.
food delivery, tailored fashion boxes, etc.).

In the `Recurring Prices`{.interpreted-text role="guilabel"} tab,
clarify the pricing options for the subscription. For each option
available, click `Add a price rule`{.interpreted-text role="guilabel"}
to add a new row.

::: {.tip}
::: {.title}
Tip
:::

Longer time `Recurring Plan`{.interpreted-text role="guilabel"} time
periods are typically incentivized with cost savings. Consider dropping
the total `Recurring Price`{.interpreted-text role="guilabel"} values to
offer customers a discount while supporting the business\'s financial
runway.
:::

Last, if the subscription is meant to be purchased on the **eCommerce**
website, click the `fa-globe`{.interpreted-text role="icon"}
`Go To Website`{.interpreted-text role="menuselection"} smart button and
in the product page header, click the gray slider from
`Unpublished`{.interpreted-text role="guilabel"} to the green
`Published`{.interpreted-text role="guilabel"} status.

Create a subscriptions quotation {#subscriptions/quotations}
--------------------------------

Manually create a new customer subscription by navigating to either the
`Sales`{.interpreted-text role="menuselection"} or
`Subscriptions`{.interpreted-text role="menuselection"} app dashboards,
and then clicking `New`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Products that have been marked as `Recurring`{.interpreted-text
role="guilabel"} on their product forms, and are also sold on the
**eCommerce** website will *automatically* create and confirm
subscription quotations in the backend of Odoo.
:::

::: {.important}
::: {.title}
Important
:::

Sales orders with a defined recurring plan automatically become
subscriptions.
:::

On the quotation form, fill in the necessary fields such as
`Customer`{.interpreted-text role="guilabel"} and
`Recurring Plan`{.interpreted-text role="guilabel"}, as well as the
`Order Lines`{.interpreted-text role="guilabel"} tab.

Optionally, specify a:

-   `Quotation Template <sales/send_quotations/quote_template>`{.interpreted-text
    role="doc"}, if one is readily available to help populate the form
    fields.

-   `Expiration`{.interpreted-text role="guilabel"} date, to indicate
    when the subscription offer is no longer valid.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Expiration dates pair well with
    `discounts <sales/products_prices/discounts>`{.interpreted-text
    role="ref"} to incentivize faster purchases, since the discount will
    expire with the quotation if it\'s not turned into a sales order
    within the specified date range.
    :::

-   `Pricelist <sales/product_prices/pricelist>`{.interpreted-text
    role="ref"}, if one is available and appropriate to use (i.e.,
    summer sale discount, VIP customer, etc.).

-   `Payment Terms`{.interpreted-text role="guilabel"}, to set a
    specified time window for when the subscription must be paid. This
    is not to be confused for when the quotation is *confirmed* and
    becomes a sales order, to where, payment may then be obtained
    immediately or within a certain amount of days, weeks, months, etc.



::: {.tip}
::: {.title}
Tip
:::

Define different invoice and delivery addresses by enabling the
`Customer Addresses
</applications/finance/accounting/customer_invoices/customer_addresses>`{.interpreted-text
role="doc"} feature.
:::

Confirmation {#subscriptions/confirmation}
------------

Send the quotation to the customer for confirmation by clicking on
`Send By Email`{.interpreted-text role="guilabel"}, or confirm it
immediately by clicking on `Confirm`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Click on `Preview`{.interpreted-text role="guilabel"} to preview the
customer portal where the customer can view their quotation, sign and
pay it, and communicate with you.
:::

If an `Online signature`{.interpreted-text role="guilabel"} or
`Online payment`{.interpreted-text role="guilabel"} is required to
confirm the quotation, set the checkboxes next to either (or both) of
these labels in the `Other Info`{.interpreted-text role="guilabel"} tab,
under the :`SALES`{.interpreted-text role="guilabel"} section.

::: {.seealso}
\- `/applications/finance/accounting/payments/online`{.interpreted-text
role="doc"} -
`Payment providers and payment methods </applications/finance/payment_providers>`{.interpreted-text
role="doc"}
:::

::: {.toctree titlesonly=""}
subscriptions/ecommerce subscriptions/upselling subscriptions/renewals
subscriptions/closing subscriptions/automatic\_alerts
subscriptions/scheduled\_actions subscriptions/reports
subscriptions/automatic\_payments
:::
