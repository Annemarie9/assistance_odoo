# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/payments/follow_up.md

Follow-up on invoices
=====================

A follow-up message can be sent to customers when a payment is overdue.
Odoo helps you identify late payments and allows you to schedule and
send the appropriate reminders using **follow-up actions** that
automatically trigger one or more actions according to the number of
overdue days. You can send your follow-ups via different means, such as
email, post, or SMS.

::: {.seealso}
\- [Odoo Tutorials: Payment
Follow-up](https://www.odoo.com/slides/slide/payment-follow-up-1682)
:::

Configuration
-------------

To configure a `Follow-Up Action`{.interpreted-text role="guilabel"}, go
to `Accounting --> Configuration -->
Follow-up Levels`{.interpreted-text role="menuselection"}, and select or
create (a) new follow-up level(s). Several follow-up actions are
available by default under the `Notification`{.interpreted-text
role="guilabel"} tab, and the **name** as well as the **number of days**
can be changed. The follow-up `Actions`{.interpreted-text
role="guilabel"} available are:

-   `Send Email`{.interpreted-text role="guilabel"};
-   `Send a Letter <customer_invoices/snailmail>`{.interpreted-text
    role="ref"};
-   `Send an SMS message <pricing/pricing_and_faq>`{.interpreted-text
    role="ref"}.

You can use a pre-filled template for your messages by selecting a
`Content Template`{.interpreted-text role="guilabel"}. To change the
template used, hover over the field and click the
`-->`{.interpreted-text role="guilabel"}. If enabled, SMS messages have
a specific `Sms Template`{.interpreted-text role="guilabel"} field.

It is possible to automatically send a reminder by enabling the
`Automatic`{.interpreted-text role="guilabel"} option, and attaching the
*open* invoice(s) by enabling `Attach Invoices`{.interpreted-text
role="guilabel"}, within a specific follow-up action.

By clicking on the `Activity`{.interpreted-text role="guilabel"} tab,
scheduling activities (tasks) is possible. That way, an activity is
automatically scheduled when the follow-up is triggered. To do so,
enable `Schedule Activity`{.interpreted-text role="guilabel"}, and
select a `Responsible`{.interpreted-text role="guilabel"} person for the
task. Choose an `Activity Type`{.interpreted-text role="guilabel"}, and
enter a `Summary`{.interpreted-text role="guilabel"} on how to handle
the activity, if desired.

::: {.tip}
::: {.title}
Tip
:::

Set a negative number of days to send a reminder before the actual due
date.
:::

Follow-up reports
-----------------

Overdue invoices you need to follow up on are available in
`Accounting --> Customers
--> Follow-up Reports`{.interpreted-text role="menuselection"}. By
default, Odoo filters by `Overdue Invoices`{.interpreted-text
role="guilabel"}, but you can also filter by
`In need of action`{.interpreted-text role="guilabel"} in the
`Filters`{.interpreted-text role="guilabel"} menu.

When selecting an invoice, you can see all of the customer\'s unpaid
invoices (overdue or not), with the due dates of late invoices appearing
in red. You can exclude invoices from a reminder by clicking
`Exclude from Follow-ups`{.interpreted-text role="guilabel"}. You can
set either `Automatic`{.interpreted-text role="guilabel"} or
`Manual`{.interpreted-text role="guilabel"} reminders as well as a
`Responsible`{.interpreted-text role="guilabel"} person for that
customer.

To send reminders, click on `Follow up`{.interpreted-text
role="guilabel"}, and select the action(s) you want to perform from:

-   `Print`{.interpreted-text role="guilabel"};
-   `Email`{.interpreted-text role="guilabel"};
-   `Sms`{.interpreted-text role="guilabel"};
-   `By post`{.interpreted-text role="guilabel"}.

You can `Attach Invoices`{.interpreted-text role="guilabel"} and change
the content templates from this view. When done, click
`Send`{.interpreted-text role="guilabel"} or
`Send & Print`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- The contact information on the invoice or the contact form is used to
send the reminder. - When the reminder is sent, it is documented in the
chatter of the invoice. - If it is not the right time for a reminder,
you can specify the `Next Reminder`{.interpreted-text role="guilabel"}
date. You will get the next report according to the next reminder date
set.
:::

::: {.tip}
::: {.title}
Tip
:::

Reconcile all bank statements right before launching the follow-up
process to avoid sending a reminder to a customer that has already paid.
:::

### Debtor\'s trust level

To know whether a customer usually pays late or not, you can set a trust
level by marking them as `Good Debtor`{.interpreted-text
role="guilabel"}, `Normal Debtor`{.interpreted-text role="guilabel"}, or
`Bad Debtor`{.interpreted-text role="guilabel"} on their follow-up
report. To do so, click on the bullet next to the customer\'s name and
select a trust level.



### Send reminders in batches

You can send reminder emails in batches from the
`Follow-up Reports`{.interpreted-text role="guilabel"} page. To do so,
select all the reports you would like to process, click on the
`Action`{.interpreted-text role="guilabel"} gear icon, and select
`Process follow-ups`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `/applications/essentials/in_app_purchase`{.interpreted-text
role="doc"} -
`/applications/marketing/sms_marketing/pricing_and_faq`{.interpreted-text
role="doc"} - `../customer_invoices/snailmail`{.interpreted-text
role="doc"}
:::
