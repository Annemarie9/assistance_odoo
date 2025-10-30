# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/sell_tickets.md

Sell event tickets
==================

Odoo *Events* provides users with the ability to create custom event
tickets (and ticket tiers), with various price points.

It *also* allows them to sell event tickets in two different ways: via
standard sales orders, and online through an integrated website.

Odoo also simplifies the ticket-purchasing process by providing plenty
of payment method options.

::: {.tip}
::: {.title}
Tip
:::

To learn more about how to create custom tickets (and ticket tiers) for
events, check out the `create_events`{.interpreted-text role="doc"}
documentation.
:::

Configuration
-------------

In order to sell event tickets in Odoo, some settings must first be
enabled.

First, navigate to
`Events app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Registration`{.interpreted-text
role="guilabel"} section, there are two different settings:
`Tickets`{.interpreted-text role="guilabel"} and
`Online Ticketing`{.interpreted-text role="guilabel"}.

The `Tickets`{.interpreted-text role="guilabel"} setting allows users to
sell event tickets with standard sales orders.

The `Online Ticketing`{.interpreted-text role="guilabel"} setting allows
users to sell event tickets online through their integrated Odoo
website.

To activate a setting, tick the checkbox beside the desired feature\'s
label, and click `Save`{.interpreted-text role="guilabel"} to finish
enabling it.

::: {.note}
::: {.title}
Note
:::

If these options are *not* enabled, a default
`Register`{.interpreted-text role="guilabel"} button becomes available
for visitors to interact with and procure free registrations to the
event.
:::

{.align-center}

With those settings enabled, Odoo automatically creates a new *Product
Type* called, *Event Ticket*, which is accessible on every product form.
Odoo also creates three event registration products (with the *Product
Type* set to *Event Ticket*) that can be used or modified for event
tickets.

::: {.important}
::: {.title}
Important
:::

When creating a new event registration product, the *Product Type*
**must** be set to *Event Ticket* on the product form, in order for it
to be selected in the *Product* column under the *Tickets* tab on an
event form.

{.align-center}
:::

::: {.note}
::: {.title}
Note
:::

Any event with paid tickets sold, features a
`fa-dollar`{.interpreted-text role="icon"} `Sales`{.interpreted-text
role="guilabel"} smart button at the top of the event form, where the
respective sales orders attributed to those ticket sales become
available.

{.align-center}

Clicking the `fa-dollar`{.interpreted-text role="icon"}
`Sales`{.interpreted-text role="guilabel"} smart button reveals a
separate page, showcasing all the sales orders (standard and/or online)
related to tickets that have been sold for that specific event.
:::

Sell event tickets with the Sales app
-------------------------------------

To sell event tickets with sales orders, start by navigating to the
`Sales`{.interpreted-text role="menuselection"} app. Then, click
`New`{.interpreted-text role="guilabel"} to open a new quotation form.

After filling out the top portion of the form with the appropriate
customer information, click `Add a product`{.interpreted-text
role="guilabel"} in the `Order Lines`{.interpreted-text role="guilabel"}
tab. Then, in the `Product`{.interpreted-text role="guilabel"} column,
select (or create) an event registration product configured with its
`Product
Type`{.interpreted-text role="guilabel"} set to
`Event Ticket`{.interpreted-text role="guilabel"} on its product form.

Once an event registration product is selected, a
`Configure an event`{.interpreted-text role="guilabel"} pop-up window
appears.

{.align-center}

From the `Configure an event`{.interpreted-text role="guilabel"} pop-up
window, select to which event this ticket purchase is related to in the
`Event`{.interpreted-text role="guilabel"} field drop-down menu. Then,
in the `Event Ticket`{.interpreted-text role="guilabel"} drop-down menu,
select which ticket tier the customer wishes to purchase, if there are
multiple tiers configured for that event.

When all the desired configurations are complete, click
`Ok`{.interpreted-text role="guilabel"}. Doing so returns the user to
the sales order, with the event registration ticket product now present
in the `Order
Lines`{.interpreted-text role="guilabel"} tab. The user can proceed to
confirm and close the sale, per the usual process.

::: {.tip}
::: {.title}
Tip
:::

To re-open the *Configure an event* pop-up window, hover over the event
registration product name in the `Order Lines`{.interpreted-text
role="guilabel"} tab, and click on the `fa-pencil`{.interpreted-text
role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon.
:::

Sell event tickets through the Website app
------------------------------------------

When a visitor arrives on the register page of the event website, they
can click the `Register`{.interpreted-text role="guilabel"} button to
purchase a ticket to the event.

::: {.note}
::: {.title}
Note
:::

If the visitor is *not* already on the register page of the event
website, clicking `Register`{.interpreted-text role="guilabel"} on the
event website\'s submenu redirects them to the proper register page.
From there, they can click the `Register`{.interpreted-text
role="guilabel"} button to begin the ticket purchasing process.
:::

If different ticket tiers are configured for the event, the visitor is
presented with a `Tickets`{.interpreted-text role="guilabel"} pop-up
window.

{.align-center}

From here, visitors select which ticket tier they would like to
purchase, along with a quantity, using the numerical drop-down menu
available to the right of their desired ticket. Once the desired
selections have been entered, the visitor then clicks the
`Register`{.interpreted-text role="guilabel"} button.

Then, an `Attendees`{.interpreted-text role="guilabel"} pop-up window
appears, containing all the questions that have been configured in the
*Questions* tab of the event form for this particular event.

{.align-center}

If multiple tickets are being purchased at once, there are numbered
sections for each individual ticket registrant, each containing the same
questions. However, if any question has been configured with the *Ask
once per order* setting, that question is only asked once \-- and
**not** for every attendee making the reservation in the order.

With all necessary information entered, the visitor can then click the
`Go to Payment`{.interpreted-text role="guilabel"} button. Doing so
first takes the visitor to a `Billing`{.interpreted-text
role="guilabel"} confirmation page, followed by a
`Payment`{.interpreted-text role="guilabel"} confirmation page, where
they can utilize any configured payment method set up in the database to
complete the order.

Then, once the purchase is complete on the front-end of the website, the
subsequent sales order is instantly accessible in the back-end of the
database.

::: {.seealso}
`create_events`{.interpreted-text role="doc"}
:::
