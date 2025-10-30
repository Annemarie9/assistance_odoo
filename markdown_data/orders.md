# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch/orders.md

show-content

:   

Orders
======

When the *Lunch* application is opened, the
`Order Your Lunch`{.interpreted-text role="guilabel"} dashboard loads.
This view is also accessed by navigating to
`Lunch app --> My Lunch --> New Order`{.interpreted-text
role="menuselection"}.

The `Order Your Lunch`{.interpreted-text role="guilabel"} dashboard
provides a summary of lunch offerings, the user\'s account information,
and the current day\'s orders, along with their statuses.

Order Your Lunch
----------------

On the main `Order Your Lunch`{.interpreted-text role="guilabel"}
dashboard, all the necessary information needed to place an order is
visible. The default filter for the products is
`Available Today`{.interpreted-text role="guilabel"}, which is present
in the `Search...`{.interpreted-text role="guilabel"} bar. This filter
shows only products that can be purchased that day, based on the
`vendor's availability <lunch/availability>`{.interpreted-text
role="ref"}.

The left-side of the dashboard displays the various
`Categories`{.interpreted-text role="guilabel"} of products available,
along with the `Vendors`{.interpreted-text role="guilabel"} supplying
the products. To the right of each line is a number, which indicates how
many products are associated with that respective category or vendor.

To filter the products by categories or vendors, tick the checkbox next
to the desired category or vendor to only view items related to those
selections. Multiple selections can be made in each section.

::: {.note}
::: {.title}
Note
:::

If multiple selections are made, **only** products that fall under
**all** the selected options are shown.
:::

The top portion of the dashboard, which serves as an order summary,
displays the user\'s account information, and the order details for
today, if any orders have been placed.

The main section, beneath the user\'s information, displays all the
products in a default Kanban view. Each product card displays the name,
cost, vendor, photo, and description of the product. If the product is
configured as new, it also displays a `New`{.interpreted-text
role="guilabel"} tag.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Anywhere a vendor\'s name is listed in the *Lunch* app, such as on
Kanban product cards, their phone number is listed, as well.
:::

The products can also be displayed in a list view, by clicking the
`≣ (four parallel
lines)`{.interpreted-text role="guilabel"} icon in the top-right corner
of the dashboard.

Placing orders
--------------

To place a lunch order, navigate to the main
`Order Your Lunch`{.interpreted-text role="guilabel"} dashboard, by
either opening the *Lunch* app, or by navigating to
`Lunch app --> My Lunch --> New Order`{.interpreted-text
role="menuselection"}.

### Add products to an order

From the `Order Your Lunch`{.interpreted-text role="guilabel"}
dashboard, click on a desired product to add to an order, and the
product appears in a `Configure Your Order`{.interpreted-text
role="guilabel"} pop-up window.

At the top of the pop-up window is the product image, name, and price.
Beneath that, there is a potential `Extras`{.interpreted-text
role="guilabel"} field, showcasing any
`extra items or options <lunch/extras>`{.interpreted-text role="ref"}.
Tick the checkbox next to any desired extras present in the
`Extras`{.interpreted-text role="guilabel"} field to add them to the
order.

Each extra option is organized by a category, complete with its name and
price. As extras are selected, the displayed price at the top of the
pop-up window updates to reflect all current selections.

Beneath the `Extras`{.interpreted-text role="guilabel"} field is the
`Description`{.interpreted-text role="guilabel"} of the product,
followed by a `Notes`{.interpreted-text role="guilabel"} field. The
`Notes`{.interpreted-text role="guilabel"} field is used to enter any
vital information, which is then sent to the vendor regarding the order,
such as any special requests or food allergies.

When all selections for the product have been made, click the
`Add To Cart`{.interpreted-text role="guilabel"} button in the
lower-left of the pop-up window. To cancel the order, click the
`Discard`{.interpreted-text role="guilabel"} button.

{.align-center}

#### Errors

Depending on how the various
`extras <lunch/configure-extras>`{.interpreted-text role="ref"} are
configured for a vendor, it is possible to receive an error when
attempting to add products to the cart.

An error can occur when a configured product **requires** the user to
select an option in the `Extras`{.interpreted-text role="guilabel"}
field, but the user neglects to make one.

When this occurs, a `Validation Error`{.interpreted-text
role="guilabel"} pop-up window appears. The error is briefly explained
in the pop-up window. Click `Close`{.interpreted-text role="guilabel"}
to close the window, and make any necessary changes to the
`Configure Your Order`{.interpreted-text role="guilabel"} pop-up window.

::: {.example}
The vendor, The Pizza Palace, provides a free beverage with any
purchase. Their products are configured so that a beverage selection is
**required** in the `Extras`{.interpreted-text role="guilabel"} field
*before* adding one of their products to the cart.

If a selection is **not** made, an error occurs. The message that
appears is [You have to order one and only one Free Beverage with
Purchase]{.title-ref}.

![The :guilabel:\`Validation Error\` pop-up window with the specific error for the free
beverage displayed.](orders/error.png){.align-center}
:::

### Your Order summary

When at least one item is added to an order, the items appear at the top
of the dashboard in the `Your Order`{.interpreted-text role="guilabel"}
summary. In addition to the products, users can view the account
information, in addition to all the information related to orders placed
during the current calendar day.

As products are added to an order, they appear at the top center of the
summary box. Each product is listed beneath the words
`Your Order`{.interpreted-text role="guilabel"}, with the product name,
quantity, and a status tag.

The available tags that can be displayed for each item are:

-   `To Order`{.interpreted-text role="guilabel"}: the product has been
    added to the cart, but has not been purchased yet by the user.
-   `Ordered`{.interpreted-text role="guilabel"}: the product has been
    purchased by the user, and is waiting to be sent to the vendor by a
    *Lunch* app manager.
-   `Sent`{.interpreted-text role="guilabel"}: the order for the product
    has been sent to the vendor by a *Lunch* app manager.
-   `Received`{.interpreted-text role="guilabel"}: the product has been
    delivered by the vendor to the user\'s location, and has been
    verified as received by a *Lunch* app manager.

Product quantities can be adjusted by clicking the
`➕ (plus sign)`{.interpreted-text role="guilabel"} or `➖ (minus
sign)`{.interpreted-text role="guilabel"} to the left of the listed
product. The product price adjusts in real-time to display the cost for
the currently selected quantity of the product.

The right side of the `Your Order`{.interpreted-text role="guilabel"}
summary displays the purchasing information. The
`Total`{.interpreted-text role="guilabel"} amount for the entire day\'s
lunch order is displayed. The `Already Paid`{.interpreted-text
role="guilabel"} field indicates how much has been paid that day towards
the `Total`{.interpreted-text role="guilabel"} amount. The
`To Pay`{.interpreted-text role="guilabel"} field displays how much of
the remaining `Total`{.interpreted-text role="guilabel"} amount must be
paid, in order to place the currently configured order.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Users can place multiple orders throughout the day, and are not
restricted to only placing one lunch order each day. Multiple orders
might need to be placed, due to users forgetting to add items to an
order, or if there are multiple meals that are available to be purchased
for the office ()not just lunch), and so on.

Depending on the various vendors, and how the vendors and products are
configured, it is possible to order breakfast, lunch, dinner, coffee,
and/or snacks.
:::

### Submit an order

To place the order, click the `Order Now`{.interpreted-text
role="guilabel"} button on the right-side of the `Your
Order`{.interpreted-text role="guilabel"} summary. The user is charged
the amount that is displayed in the `To Pay`{.interpreted-text
role="guilabel"} field, and the cost is deducted from their *Lunch*
account balance.

Once the order is placed, the tags for the items just purchased in the
`Your Order`{.interpreted-text role="guilabel"} field change from orange
`To Order`{.interpreted-text role="guilabel"} tags to red
`Ordered`{.interpreted-text role="guilabel"} tags.

### Track an order

When orders have been sent to the vendors, the tags for the items in the
`Your Order`{.interpreted-text role="guilabel"} summary change from red
`Ordered`{.interpreted-text role="guilabel"} tags to blue
`Sent`{.interpreted-text role="guilabel"} tags.

Once orders have been received and verified, the tags change from blue
`Sent`{.interpreted-text role="guilabel"} tags to green
`Received`{.interpreted-text role="guilabel"} tags.

### Receive an order

When orders are received at the delivery location, they are confirmed by
a *Lunch* app manager, and a notification is sent to the employee who
ordered the food.

My Orders
---------

To view a full list of all orders placed in the *Lunch* app for the
currently signed-in user, navigate to
`Lunch app --> My Lunch --> My Order History`{.interpreted-text
role="menuselection"}. This navigates to the
`My Orders`{.interpreted-text role="guilabel"} dashboard. The data is
filtered by `My Orders`{.interpreted-text role="guilabel"} and grouped
by `Order Date: Day`{.interpreted-text role="guilabel"}, by default,
both of which are located in the `Search...`{.interpreted-text
role="guilabel"} bar.

All products appear in a list view, organized by date. The list displays
the `Order Date`{.interpreted-text role="guilabel"},
`Vendor`{.interpreted-text role="guilabel"}, `Product`{.interpreted-text
role="guilabel"}, `Extras`{.interpreted-text role="guilabel"},
`Notes`{.interpreted-text role="guilabel"}, `User`{.interpreted-text
role="guilabel"}, `Lunch Location`{.interpreted-text role="guilabel"},
`Price`{.interpreted-text role="guilabel"}, and
`Status`{.interpreted-text role="guilabel"} information. If in a
multi-company database, a `Company`{.interpreted-text role="guilabel"}
column also appears.

The total cost for each order is displayed on the line containing the
order date. At the bottom of the list, beneath all the lines, the
overall total amount paid for all the orders appears, under the
`Price`{.interpreted-text role="guilabel"} column.

At the end of each product line with a status of
`Ordered`{.interpreted-text role="guilabel"} or `Sent`{.interpreted-text
role="guilabel"}, an `X Cancel`{.interpreted-text role="guilabel"}
button appears. Click `X Cancel`{.interpreted-text role="guilabel"} to
cancel that product order. Once a product order has been canceled, the
money paid for that product is refunded, and appears in the user\'s
account.

At the end of each product line with a status of
`Received`{.interpreted-text role="guilabel"}, a
`Re-order`{.interpreted-text role="guilabel"} button appears. Click
`Re-order`{.interpreted-text role="guilabel"} to instantly reorder that
same product, with the same extras, if applicable. The new order appears
in the list, under the current date, and the product is paid for, with
money deducted from the user\'s account.

{.align-center}

My Account
----------

To view a summary of all transactions in the user\'s account, navigate
to `Lunch app
--> My Lunch --> My Account History`{.interpreted-text
role="menuselection"}. Doing so reveals the
`My Account`{.interpreted-text role="guilabel"} dashboard.

The default presentation of the `My Account`{.interpreted-text
role="guilabel"} dashboard displays all entries, from newest to oldest.
The `Date`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and
`Amount`{.interpreted-text role="guilabel"} are the only fields
displayed in the list.

Entries with a negative figure listed in the `Amount`{.interpreted-text
role="guilabel"} column represent products purchased in the *Lunch* app.
These appear in a [\$-XX.XX]{.title-ref} format.

Entries with a positive balance either represent funds added to the
user\'s lunch account, or canceled orders that were eventually refunded
to the user. These appear in a [\$XX.XX]{.title-ref} format.

![The My Account dashboard with the entry for adding funds to the user\'s lunch account
highlighted.](orders/my-account.png){.align-center}
