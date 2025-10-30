Scheduled actions
=================

*Scheduled actions* are pre-configured processes that allow users to
automate certain tasks within a database, based on a designated schedule
or number of occurrences. These tasks can include sending emails,
generating invoices, data clean-up, and so much more.

In Odoo, some scheduled actions are active, by default, to ensure that
certain functions are triggered automatically, however there are *also*
many scheduled action options that appear in the database that are
**not** activated by default.

In Odoo *Subscriptions*, there are two scheduled actions that initiate
the billing process for active recurring subscriptions, as well as when
billing should stop due to subscription expiration.

They are turned on, by default and can be deactivated at any time in
order to manage subscriptions manually.

Access scheduled actions
------------------------

::: {.important}
::: {.title}
Important
:::

In order to access scheduled actions,
`developer mode <developer-mode>`{.interpreted-text role="ref"} **must**
be activated.
:::

With developer mode activated, navigate to
`Settings app --> Technical --> Scheduled
Actions`{.interpreted-text role="menuselection"}.

{.align-center}

Doing so reveals a dedicated `Scheduled Actions`{.interpreted-text
role="guilabel"} dashboard. On this page, there is a complete list of
scheduled actions for the entire database.

From here, enter [Subscription]{.title-ref} in the search bar. Doing so
provides three subscription-specific results. The following
documentation focuses on the last two results in the list:

-   `Sale Subscription: generate recurring invoices and payments`{.interpreted-text
    role="guilabel"}
-   `Sale Subscription: subscriptions expiration`{.interpreted-text
    role="guilabel"}

{.align-center}

Determine if a scheduled action is active by looking under the
`Active`{.interpreted-text role="guilabel"} column, in the it\'s
corresponding row on the `Scheduled Actions`{.interpreted-text
role="guilabel"} dashboard, for a ticked checkbox; if the checkbox is
green with a check mark, the scheduled action is active.

If a scheduled action needs to be activated, click into the desired
scheduled action from the list.



Then, from the scheduled action form, toggle the switch in the
`Active`{.interpreted-text role="guilabel"} field to the right. Doing so
turns the switch green, indicating that the scheduled action is now
[Active]{.title-ref}.

The ability to set up how often the scheduled action runs is also
available on the scheduled action form, in the
`Execute Every`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

The scheduled action does **not** function correctly if the execution
time is less than five minutes. This is a general rule for all scheduled
actions.

For more information, read the `Frequent Technical Questions
</administration/odoo_sh/advanced/frequent_technical_questions>`{.interpreted-text
role="doc"} documentation.
:::

Generate recurring invoices and payments
----------------------------------------

In order for the
`Sale Subscription: generate recurring invoices and payments`{.interpreted-text
role="guilabel"} scheduled action to properly generate recurring
invoices and payments on subscriptions, the *Deferred Expense* and
*Deferred Revenue* accounts **must** be set up, in order for Odoo to
process various invoices and payments related to subscriptions.

To set up *Deferred Expense* and *Deferred Revenue* accounts, navigate
to `Accounting
app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Both accounts can be configured in the `Default
Accounts`{.interpreted-text role="guilabel"} section.

{.align-center}

Once the correct accounts are entered in the
`Deferred Expense`{.interpreted-text role="guilabel"} and `Deferred
Revenue`{.interpreted-text role="guilabel"} drop-down menu fields, click
`Save`{.interpreted-text role="guilabel"} in the upper-left corner.

### Create invoice

Elements related to the
`Sale Subscription: generate recurring invoices and payments`{.interpreted-text
role="guilabel"} scheduled action can be found on confirmed subscription
sales orders.

To examine these elements, open any confirmed sales order in the
*Subscriptions* application to reveal the subscription sales order form.

On a confirmed subscription sales order form, focus on the
`Recurring Plan`{.interpreted-text role="guilabel"} and
`Date of Next Invoice`{.interpreted-text role="guilabel"} fields.

{.align-center}

The scheduled action creates an invoice when today\'s date is the same
date as the `Date of
Next Invoice`{.interpreted-text role="guilabel"}.

Odoo uses the information in the `Recurring Plan`{.interpreted-text
role="guilabel"} field to update the next invoice date accordingly.

::: {.warning}
::: {.title}
Warning
:::

If the product invoicing policy is set to *Based on Delivered Quantities
(Manual)*, and the delivered quantity is [0]{.title-ref}, Odoo does
**not** create an invoice, and the customer is not charged.

Instead, the subscription is processed as a free recurring product, and
is reflected as such in the *chatter* of the subscription sales order.

When this occurs, the following message appears: [Automatic renewal
succeeded. Free subscription. Next invoice:\[date\]. No email
sent.]{.title-ref}
:::

Once the invoice for the subscription sales order is created, the
invoice can be viewed by clicking the `Invoices`{.interpreted-text
role="guilabel"} smart button that appears at the top of the
subscription sales order.

An email is sent to the customer notifying them of the recurring
subscription charge, *if* there is a `Payment Token`{.interpreted-text
role="guilabel"} on the account.

To check if there is a `Payment Token`{.interpreted-text
role="guilabel"}, open the `Other Info`{.interpreted-text
role="guilabel"} tab, and look at the `Payment Token`{.interpreted-text
role="guilabel"} field, under the `Subscription`{.interpreted-text
role="guilabel"} section.

{.align-center}

If there is no `Payment Token`{.interpreted-text role="guilabel"}, the
invoice is created, and sent to the customer. The payment **must** be
registered manually in this case.

### Closing invoices

The
`Sale Subscription: generate recurring invoices and payments`{.interpreted-text
role="guilabel"} scheduled action also has the ability to close a
subscription, if the following conditions are met:

-   If the subscription has no `Payment Token`{.interpreted-text
    role="guilabel"}, create and post the invoice.

-   If the subscription has a `Payment Token`{.interpreted-text
    role="guilabel"}, try to charge.

    > -   If the charge is successful, create and post the invoice.
    >
    > -   If the charge fails, send reminders periodically.
    >
    >     > -   Close the subscription if it continues to fail for more
    >     >     than fourteen days.

Subscriptions expiration
------------------------

The `Sale Subscription: subscriptions expiration`{.interpreted-text
role="guilabel"} scheduled action checks for all other conditions that
may cause a subscription to close automatically. If certain conditions
are met, the scheduled action closes that subscription.

First, the
`Sale Subscription: subscriptions expiration`{.interpreted-text
role="guilabel"} scheduled action checks to see if the end date has
passed, which is configured on the subscription sales order.

{.align-center}

Then, the
`Sale Subscription: subscriptions expiration`{.interpreted-text
role="guilabel"} scheduled action checks if the invoice has not been
paid within the payment terms deadline.

To access the invoices attached to a subscription, access the sales
order for the subscription product, and click the
`Invoices`{.interpreted-text role="guilabel"} smart button. Then, look
at the `Invoice Date`{.interpreted-text role="guilabel"} column.

{.align-center}

Unpaid subscriptions with an `Invoice Date`{.interpreted-text
role="guilabel"} that are past the determined number of days in the
`Automatic Closing`{.interpreted-text role="guilabel"} field of a
`Recurring Plan`{.interpreted-text role="guilabel"} are automatically
closed by the
`Sale Subscription: subscriptions expiration`{.interpreted-text
role="guilabel"} scheduled action.

{.align-center}

For example, if the next invoice date is July 1st, and the
`Automatic Closing`{.interpreted-text role="guilabel"} is set to \'30
Days\', the scheduled action would close the subscription on August 1st.

::: {.seealso}
\- `../subscriptions`{.interpreted-text role="doc"} -
`automatic_alerts`{.interpreted-text role="doc"}
:::
