Close subscriptions
===================

Odoo *Subscriptions* provides flexibility for businesses to decide
whether customers can self-manage their subscriptions, or restrict that
ability entirely.

Configuration
-------------

Start by navigating to
`Subscriptions app --> Configuration --> Recurring Plans`{.interpreted-text
role="menuselection"}. From there, either create a new plan by clicking
`New`{.interpreted-text role="guilabel"} or select an existing one to
modify it.

Once on the `Recurring Plans`{.interpreted-text role="guilabel"} form,
enable the `Closable`{.interpreted-text role="guilabel"} option, in the
`Self-Service`{.interpreted-text role="guilabel"} section, to allow
customers to close their own subscriptions using the customer portal.

{.align-center}

Close a subscription
--------------------

### Administrator view

After a quotation for a subscription product has been confirmed, it
becomes a sales order, and the subscription status changes to
`In Progress`{.interpreted-text role="guilabel"}.

At that point, the ability to close the subscription becomes available,
via the `Close`{.interpreted-text role="guilabel"} button at the top of
the subscription order, near the row that contains
`In Progress`{.interpreted-text role="guilabel"} and other stages. This
option is also available after the order has been invoiced and the
payment has been registered.

{.align-center}

Clicking the `Close`{.interpreted-text role="guilabel"} button prompts a
`Close Reason`{.interpreted-text role="guilabel"} pop-up window to
appear, allowing administrators to input the reason for closing the
subscription, or choose from the drop-down menu of options in the
`Reason`{.interpreted-text role="guilabel"} field.

{.align-center}

When the desired `Reason`{.interpreted-text role="guilabel"} is entered,
click the `Submit`{.interpreted-text role="guilabel"} button.

Clicking `Submit`{.interpreted-text role="guilabel"} on the
`Close Reason`{.interpreted-text role="guilabel"} pop-up window updates
the subscription sales order to show `Churned`{.interpreted-text
role="guilabel"} status tag, along with the specified `Close
Reason`{.interpreted-text role="guilabel"}.

{.align-center}

That same close reason can be found in the *Chatter* of the sales order,
as well.

{.align-center}

### Customer view

::: {.note}
::: {.title}
Note
:::

As an administrator, the ability to visualize what customers see when
managing their subscriptions is accessible via the
`Preview`{.interpreted-text role="guilabel"} button, located at the top
of the subscription sales order.
:::

From the customer\'s point of view, in the customer portal, the
`Close Subscription`{.interpreted-text role="guilabel"} button is
located on the left side of the sales order.

{.align-center}

When the customer clicks the `Close Subscription`{.interpreted-text
role="guilabel"} button, a `Close Subscription`{.interpreted-text
role="guilabel"} pop-up window appears, in which the customer has to
choose from a select list of reasons why they are choosing to close the
subscription.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Customers can *only* chose a pre-configured reason why the subscription
is being closed. They can *not* enter a custom reason from the customer
portal. These selections can be adjusted by navigating to
`Subscriptions --> Configuration --> Close Reasons`{.interpreted-text
role="menuselection"}.
:::

Once the customer has chosen a close reason, they would click the
`Submit`{.interpreted-text role="guilabel"} button on the pop-up window.

Upon closure, the subscription order in the customer portal is tagged as
`Closed`{.interpreted-text role="guilabel"}.

In addition, the specified `Close Reason`{.interpreted-text
role="guilabel"} appears on the subscription order in the
*Subscriptions* app in the backend (Administrator\'s view).

::: {.seealso}
\- `../subscriptions`{.interpreted-text role="doc"}
:::
