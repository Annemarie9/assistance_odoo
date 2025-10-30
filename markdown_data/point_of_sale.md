show-content

:   

show-toc

:   

Point of Sale
=============

With **Odoo Point of Sale**, run your shops and restaurants easily. The
app works on any device with a web browser, even if you are temporarily
offline. Product moves are automatically registered in your stock, you
get real-time statistics, and your data is consolidated across all
shops.

::: {.seealso}
\- [Odoo Tutorials: Point of Sale
Tutorials](https://www.odoo.com/slides/point-of-sale-28) -
`IoT Boxes Documentations </applications/general/iot>`{.interpreted-text
role="doc"}
:::

Start a session {#pos/session-start}
---------------

From the **POS dashboard**, click `New Session`{.interpreted-text
role="guilabel"}, and at the `Opening Cash
Control`{.interpreted-text role="guilabel"} screen, click
`Open Session`{.interpreted-text role="guilabel"} to start a POS
session, or click `Continue
Selling`{.interpreted-text role="guilabel"} if the session is already
opened.

::: {.note}
::: {.title}
Note
:::

`Multiple users <point_of_sale/employee_login>`{.interpreted-text
role="doc"} can be logged into the same session at the same time.
However, the session can only be opened once on the same browser.
:::

Sell products {#pos/sell}
-------------

Click on products to add them to the cart. To change the **quantity**,
click `Qty`{.interpreted-text role="guilabel"} and enter the number of
products using the keypad. To add a **discount** or modify the product
**price**, click respectively `% Disc`{.interpreted-text
role="guilabel"} or `Price`{.interpreted-text role="guilabel"} and enter
the amounts.

Once an order is completed, proceed to checkout by clicking
`Payment`{.interpreted-text role="guilabel"}. Select the **payment
method**, enter the received amount, and click
`Validate`{.interpreted-text role="guilabel"}. Click
`New Order`{.interpreted-text role="guilabel"} to move on to the next
customer.



::: {.tip}
::: {.title}
Tip
:::

\- You can use both [,]{.title-ref} and [.]{.title-ref} on your keyboard
as decimal separators. - **Cash** is selected by default if you enter
the amount without choosing a payment method.
:::

::: {.note}
::: {.title}
Note
:::

The system can only load a limited number of products for effective
opening. Click `Search more`{.interpreted-text role="guilabel"} if the
desired product is not loaded automatically.
:::

Set customers {#pos/customers}
-------------

Registering your customer is necessary to
`collect their loyalty points and grant them rewards
<point_of_sale/pricing/loyalty>`{.interpreted-text role="doc"},
automatically apply the `attributed pricelist
<point_of_sale/pricing/pricelists>`{.interpreted-text role="doc"}, or
`generate and print an invoice
<receipts-invoices/invoices>`{.interpreted-text role="ref"}.

You can create customers from an
`open POS session <pos/session-start>`{.interpreted-text role="ref"} by
clicking `Customer --> Create`{.interpreted-text role="menuselection"},
and filling in the contact information. You can also create customers
from the backend by going to
`Point of Sale --> Orders --> Customers`{.interpreted-text
role="menuselection"} and clicking `New`{.interpreted-text
role="guilabel"}. Then, fill in the information and save.

To set a customer during an order, access the list of customers by
clicking `Customer`{.interpreted-text role="guilabel"} on the POS
interface. You can also set a customer at the payment screen by clicking
`Customer`{.interpreted-text role="guilabel"}.

Customer notes {#pos/customer-notes}
--------------

You can add **customer notes** about specific products directly from an
open `POS session
<pos/session-start>`{.interpreted-text role="ref"}. For instance, to
provide cleaning and maintenance tips. They can also be used to track a
customer\'s particular request, such as not wanting the product to be
assembled for them.

To do so, select a product and click `Customer Note`{.interpreted-text
role="guilabel"} on the pad. Doing so opens a pop-up window in which you
can add or modify content for the note.

::: {.note}
::: {.title}
Note
:::

Product notes from an
`imported SO <point_of_sale/shop/sales_order>`{.interpreted-text
role="doc"} are displayed identically in the cart.
:::



Customer notes appear on customers\' receipts and invoices similarly to
how they appear in the cart, under the related product.



Return and refund products {#pos/refund}
--------------------------

To return and refund a product,

1.  `start a session <pos/session-start>`{.interpreted-text role="ref"}
    from the **POS dashboard**;
2.  click `Refund`{.interpreted-text role="guilabel"} and select the
    corresponding order;
3.  select the product and the quantity to refund using the keypad;
4.  click `Refund`{.interpreted-text role="guilabel"} to go back to the
    previous screen;
5.  once the order is completed, click `Payment`{.interpreted-text
    role="guilabel"} to proceed to the refund;
6.  click `Validate`{.interpreted-text role="guilabel"} and
    `New Order`{.interpreted-text role="guilabel"} to move on to the
    next customer.



::: {.note}
::: {.title}
Note
:::

\- You can filter the **orders list** by
`Receipt Number`{.interpreted-text role="guilabel"},
`Date`{.interpreted-text role="guilabel"} or
`Customer`{.interpreted-text role="guilabel"} using the search bar. -
You can also refund a product by selecting the returned product from an
open session, and setting a negative quantity that equals the number of
returned products. To do so, click `Qty`{.interpreted-text
role="guilabel"} and `+/-`{.interpreted-text role="guilabel"}, followed
by the quantity of returned products.
:::

Once the return payment is validated, Odoo generates the required credit
note, referencing the original receipt or invoice and partially or fully
canceling the document.

Manage the cash register {#pos/cash-register}
------------------------

To add or take out cash from the register, click the **menu icon** in
the upper right corner of your screen and
`Cash In/Out`{.interpreted-text role="guilabel"}.

![Dropdown menu to close a POS session, reach the backend, add or take cash out or check
orders](point_of_sale/menu-button.png)

Doing so opens a pop-up window on which you can select
`Cash In`{.interpreted-text role="guilabel"} or
`Cash Out`{.interpreted-text role="guilabel"}, enter the amount and the
reason, and click `Confirm`{.interpreted-text role="guilabel"}.

Close the POS session {#pos/session-close}
---------------------

To close your session, click the **menu icon** in the upper right corner
of your screen and `Close Session`{.interpreted-text role="guilabel"}.

Doing so opens the `Closing Control`{.interpreted-text role="guilabel"}
pop-up screen. From this screen, you can retrieve various information:

-   the number of orders made and the total amount made during the
    session;
-   the expected amounts grouped by payment method.

Before closing this window, count your cash using the calculator icon.
Doing so opens a pop-up window that computes the total amount in the
cash drawer depending on the coins and bills counted and added manually.
Then, click `Confirm`{.interpreted-text role="guilabel"} or
`Discard`{.interpreted-text role="guilabel"} to close the window. The
computed amount is set in the `Counted`{.interpreted-text
role="guilabel"} column, and the `Money Details`{.interpreted-text
role="guilabel"} are specified in the **Notes** section.



Once you are done controlling the amounts, click
`Close Session`{.interpreted-text role="guilabel"} to close and go back
to the **POS dashboard**.

::: {.note}
::: {.title}
Note
:::

\- To reach the backend without closing the session, click
`Backend`{.interpreted-text role="guilabel"} on the dropdown menu. - To
abort, click `Discard`{.interpreted-text role="guilabel"} on the pop-up
window. - Depending on your setup, you might only be allowed to close a
session if the expected cash revenue equals the counted cash. To close
it anyway, click `Ok`{.interpreted-text role="guilabel"} on the
`Payments Difference`{.interpreted-text role="guilabel"} screen.
:::

::: {.tip}
::: {.title}
Tip
:::

\- It is strongly advised to close your POS session at the end of each
day. - To look at all your previous sessions, go to
`Point of Sale --> Orders -->
Sessions`{.interpreted-text role="menuselection"}.
:::

Analytics {#pos/analytics}
---------

Once you
`close and post the POS session <pos/session-close>`{.interpreted-text
role="ref"}, access the comprehensive report to review all session
activities, including who initiated the session and who handled specific
orders. To access the session\'s report:

1.  Click `fa-ellipsis-v`{.interpreted-text role="icon"}
    (`vertical ellipsis`{.interpreted-text role="guilabel"}) on the POS
    card.
2.  Click `Sessions`{.interpreted-text role="guilabel"} under the
    `View`{.interpreted-text role="guilabel"} section.
3.  From that list view, you can see all the sessions and who initiated
    them under the `Opened By`{.interpreted-text role="guilabel"}
    column.
4.  Select a POS session to open a detailed session report.
5.  Click the `Orders`{.interpreted-text role="guilabel"} smart button
    to display a list of all orders placed during that session.
6.  From that view, you can retrieve the following information:
    -   The `Order Ref`{.interpreted-text role="guilabel"}
    -   The `Date`{.interpreted-text role="guilabel"} of the order.
    -   The `Point of Sale`{.interpreted-text role="guilabel"} where
        that order was made.
    -   The `Receipt Number`{.interpreted-text role="guilabel"}.
    -   The `Customer`{.interpreted-text role="guilabel"}.
    -   The `Employee`{.interpreted-text role="guilabel"} that placed
        this order.
    -   The `Total`{.interpreted-text role="guilabel"} paid amount.
    -   The order `Status`{.interpreted-text role="guilabel"}.

To get an overview of all orders, regardless of the session, click the
vertical ellipsis button (`⋮`{.interpreted-text role="guilabel"}) on the
POS card and select `Orders`{.interpreted-text role="guilabel"} from the
`View`{.interpreted-text role="guilabel"} section.

::: {.toctree titlesonly=""}
point\_of\_sale/configuration point\_of\_sale/employee\_login
point\_of\_sale/receipts\_invoices point\_of\_sale/preparation
point\_of\_sale/self\_order point\_of\_sale/combos point\_of\_sale/shop
point\_of\_sale/restaurant point\_of\_sale/pricing
point\_of\_sale/payment\_methods point\_of\_sale/reporting
:::
