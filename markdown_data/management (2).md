# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch/management.md

Lunch management
================

In Odoo\'s *Lunch* application, it is required to have someone manage
the orders, vendors, and products. In addition, someone must be
responsible for the orders, and notifying employees when their orders
have arrived. This can be the same person.

Orders can be `canceled <lunch/cancel>`{.interpreted-text role="ref"},
`sent to the vendor <lunch/send-orders>`{.interpreted-text role="ref"},
`confirmed <lunch/confirm-orders>`{.interpreted-text role="ref"} upon
arrival, and `employees can be notified
<lunch/notify>`{.interpreted-text role="ref"}, either from the
`Today's Orders <lunch/todays-orders>`{.interpreted-text role="ref"}
dashboard, or the
`Control Vendors <lunch/control_vendors>`{.interpreted-text role="ref"}
dashboard.

To manage the *Lunch* app, users need the appropriate
`Administrator`{.interpreted-text role="guilabel"} rights. These can be
set by navigating to the `Settings app`{.interpreted-text
role="menuselection"} and selecting `Manage Users`{.interpreted-text
role="guilabel"}. Then, click on the desired user to view their access
rights.

For more information on access rights, refer to the `Access rights
<../../general/users/access_rights/>`{.interpreted-text role="doc"}
documentation.

::: {.note}
::: {.title}
Note
:::

Only users with administration rights are able to view the
`Manager`{.interpreted-text role="guilabel"} and
`Configuration`{.interpreted-text role="guilabel"} menus in the *Lunch*
application.
:::

Today\'s Orders {#lunch/todays-orders}
---------------

To view and manage the orders for the day, navigate to
`Lunch app --> Manager -->
Today's Orders`{.interpreted-text role="menuselection"}. All orders for
the day are presented in a list view on the `Today's
Orders`{.interpreted-text role="guilabel"} dashboard, with a filter for
`Today`{.interpreted-text role="guilabel"}, and grouped by
`Vendor`{.interpreted-text role="guilabel"}, by default.

The following information appears in the list:

-   `Order Date`{.interpreted-text role="guilabel"}: the date the order
    was placed.
-   `Vendor`{.interpreted-text role="guilabel"}: the vendor the product
    is being ordered from.
-   `Product`{.interpreted-text role="guilabel"}: the specific product
    ordered.
-   `Extras`{.interpreted-text role="guilabel"}: any extras selected for
    the product.
-   `Notes`{.interpreted-text role="guilabel"}: any information needed
    to be sent to the vendor.
-   `User`{.interpreted-text role="guilabel"}: the user who ordered the
    product.
-   `Lunch Location`{.interpreted-text role="guilabel"}: where the
    product is set to be delivered.
-   `Price`{.interpreted-text role="guilabel"}: the total price for the
    product, including all extras.
-   `Status`{.interpreted-text role="guilabel"}: the current status of
    the product.
-   `Company`{.interpreted-text role="guilabel"}: the company under
    which the order was placed. This only appears in a multi-company
    database.

![The list that appears in the Today\'s Orders dashboard, with the filters and top column
names highlighted.](management/today.png){.align-center}

### Cancel orders {#lunch/cancel}

All users can cancel an order, not just managers of the *Lunch* app.

To cancel an order from a vendor, individual products **must** be
canceled one at a time.

On the `Today's Orders`{.interpreted-text role="guilabel"} dashboard, a
`✖️ Cancel`{.interpreted-text role="guilabel"} button is shown at the
far-right of each product line that can be canceled. Click the
`✖️ Cancel`{.interpreted-text role="guilabel"} button to cancel the
order for that individual product.

::: {.note}
::: {.title}
Note
:::

Only products with a red `Status`{.interpreted-text role="guilabel"} tag
of `Ordered`{.interpreted-text role="guilabel"} can be canceled.
:::

{.align-center}

### Send orders {#lunch/send-orders}

The first step in managing the *Lunch* app is to send the orders to the
vendors.

When orders are ready to be sent, the manager responsible for sending
orders **must** send the orders to the vendor, outside of the database
(call, online order, etc.).

Once orders have been placed with the vendors, click the
`Send Orders`{.interpreted-text role="guilabel"} button that appears
next to each vendor\'s name and phone number.

Once sent, the `Send Orders`{.interpreted-text role="guilabel"} button
changes to a `Confirm Orders`{.interpreted-text role="guilabel"} button,
and the `Status`{.interpreted-text role="guilabel"} column is updated
from red `Ordered`{.interpreted-text role="guilabel"} tags to blue
`Sent`{.interpreted-text role="guilabel"} tags, indicating the order has
been sent to the vendor. Users who have placed orders in the *Lunch* app
rely on the `Status`{.interpreted-text role="guilabel"} tags to track
their orders.

{.align-center}

### Confirm orders {#lunch/confirm-orders}

After orders have been sent to the vendor, the next step is to confirm
the orders after they have been delivered.

On the `Today's Orders`{.interpreted-text role="guilabel"} dashboard,
click the `Confirm Orders`{.interpreted-text role="guilabel"} button
that appears next to the vendor\'s name and phone number.

Once confirmed, the `Confirm Orders`{.interpreted-text role="guilabel"}
button disappears, and the `Status`{.interpreted-text role="guilabel"}
column is updated from blue `Sent`{.interpreted-text role="guilabel"}
tags to green `Received`{.interpreted-text role="guilabel"} tags,
indicating the vendor has delivered the orders.

In addition, the `✖️ Cancel`{.interpreted-text role="guilabel"} button
at the end of each product line changes to a
`✉️ Send Notification`{.interpreted-text role="guilabel"} button.

If needed, instead of confirming all of the individual products from a
vendor, individual products can be confirmed one at a time. To confirm
an individual product, click the `✔️ Confirm`{.interpreted-text
role="guilabel"} button at the end of the individual product line. When
confirming individual products with this method, the
`Confirm Orders`{.interpreted-text role="guilabel"} button remains on
the vendor line.

{.align-center}

::: {.example}
A vendor receives an order for three pizzas, and an order of garlic
knots. When the delivery is made to the company, the *Lunch* manager
notices the garlic knots are missing.

The manager first marks the three pizzas as received, by individually
confirming the products with the `✔️ Confirm`{.interpreted-text
role="guilabel"} button at the end of each product line.

Later, when the vendor delivers the garlic knots, the manager can either
click the `✔️
Confirm`{.interpreted-text role="guilabel"} button at the end of the
line for the garlic knots, or click the `Confirm
Orders`{.interpreted-text role="guilabel"} button that appears next to
the vendor\'s name and phone number.
:::

### Notify employees {#lunch/notify}

After products are received, and the orders are confirmed, the employees
**must** be informed that their orders have been delivered, and are
ready to be picked up.

Unlike sending and confirming orders, notifications must be sent
individually, and cannot be sent in a batch.

To notify the user their product has arrived, click the
`✉️ Send Notification`{.interpreted-text role="guilabel"} button at the
end of each product line. An email is sent to the user informing them
their products have been delivered.

Control Vendors {#lunch/control_vendors}
---------------

All orders for all vendors, both past and present, can be found in the
*Control Vendors* dashboard. To access these records, navigate to
`Lunch app --> Manager --> Control Vendors`{.interpreted-text
role="menuselection"}.

All orders appear in a list view, grouped alphabetically by
`Vendor`{.interpreted-text role="guilabel"}. The list loads with all
vendors expanded to show all order lines for every vendor, by default.

The following information appears in the list:

-   `Order Date`{.interpreted-text role="guilabel"}: the date the order
    was placed.
-   `Vendor`{.interpreted-text role="guilabel"}: the vendor the product
    is being ordered from.
-   `Product`{.interpreted-text role="guilabel"}: the specific product
    ordered.
-   `Extras`{.interpreted-text role="guilabel"}: any extras selected for
    the product.
-   `Notes`{.interpreted-text role="guilabel"}: any information needed
    to be sent to the vendor.
-   `User`{.interpreted-text role="guilabel"}: the user who ordered the
    product.
-   `Lunch Location`{.interpreted-text role="guilabel"}: where the
    product is set to be delivered.
-   `Price`{.interpreted-text role="guilabel"}: the total price for the
    product, including all extras.
-   `Status`{.interpreted-text role="guilabel"}: the current status of
    the product.
-   `Company`{.interpreted-text role="guilabel"}: the company under
    which the order was placed. This only appears in a multi-company
    database.

Orders can be `canceled <lunch/cancel>`{.interpreted-text role="ref"},
`sent to the vendor <lunch/send-orders>`{.interpreted-text role="ref"},
`confirmed <lunch/confirm-orders>`{.interpreted-text role="ref"} upon
arrival, and `employees can be notified
<lunch/notify>`{.interpreted-text role="ref"} using the same method as
on the `Today's Orders <lunch/todays-orders>`{.interpreted-text
role="ref"} dashboard.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The difference between the
`Today's Orders <lunch/todays-orders>`{.interpreted-text role="ref"}
dashboard and the
`Control Vendors <lunch/control_vendors>`{.interpreted-text role="ref"}
dashboard is that the *Today\'s Orders* dashboard **only** displays
orders for the current day, while the
`Control Vendors`{.interpreted-text role="guilabel"} dashboard displays
**all** orders made in the *Lunch* app.
:::

::: {.seealso}
\- `../lunch`{.interpreted-text role="doc"} - `orders`{.interpreted-text
role="doc"} - `user-accounts`{.interpreted-text role="doc"}
:::
