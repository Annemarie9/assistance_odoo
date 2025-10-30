Rental
======

The Odoo *Rental* application provides comprehensive solutions to
configure and manage rentals.

Send quotations, confirm orders, schedule rentals, register products
when they are picked up and returned, and invoice customers from this
single platform.

::: {.seealso}
\-  - [Odoo
Tutorials: Rental](https://www.odoo.com/slides/rental-48)
:::

Dashboard {#rental/pricing}
---------

Upon opening the *Rental* application, the
`Rental Orders`{.interpreted-text role="guilabel"} dashboard is
revealed.

{.align-center}

In the default kanban view, all rentals are visible. Each rental card
displays the customer name, the price of the rental, the related sales
order number, along with the status of the rental.

::: {.note}
::: {.title}
Note
:::

Rental kanban cards that do **not** display a rental status means those
rentals have confirmed quotations, but have not been picked up yet.
:::

On the left sidebar, the `Rental Status`{.interpreted-text
role="guilabel"} for each rental can be found. Beneath that, the
`Invoice Status`{.interpreted-text role="guilabel"} of the rentals is
accessible. Clicking any option in the left sidebar filters the
displayed rentals on the dashboard.

Settings
--------

To configure additional rental delay costs, availability of rental
items, or minimum time of rental, navigate to
`Rental app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

{.align-center}

In the `Rental`{.interpreted-text role="guilabel"} section, there are
options to configure `Default Delay Costs`{.interpreted-text
role="guilabel"} and `Default Padding Time`{.interpreted-text
role="guilabel"}. There is also the option to activate `Rental
Transfers`{.interpreted-text role="guilabel"} and
`Digital Documents`{.interpreted-text role="guilabel"}.

-   `Default Delay Costs`{.interpreted-text role="guilabel"} are
    additional costs for late returns.

-   `Default Padding Time`{.interpreted-text role="guilabel"} represents
    the minimum amount of time between two rentals.

-   `Rental Transfers`{.interpreted-text role="guilabel"} means stock
    deliveries and receipts can be used for rental orders.

-   

    `Digital Documents`{.interpreted-text role="guilabel"} allows users to upload documents for customers to sign prior to

    :   confirming their rental.

In the `Rent Online`{.interpreted-text role="guilabel"} section, there
are options to configure a `Minimal Rental
Duration`{.interpreted-text role="guilabel"} and designate
`Unavailability days`{.interpreted-text role="guilabel"}, or days during
which pickup and return are not possible.

Rental products
---------------

To view all products that can rented in the database, navigate to
`Rentals app -->
Products`{.interpreted-text role="menuselection"}. By default, the
`Can be Rented`{.interpreted-text role="guilabel"} search filter appears
in the search bar.

Each product kanban card displays that product\'s name, rental price,
and product image (if applicable).

Rental pricing
--------------

To adjust the rental pricing on a product, go to the
`Products`{.interpreted-text role="guilabel"} page in the *Rental* app,
then select the desired product or click `New`{.interpreted-text
role="guilabel"} to create a new product from scratch.

On the product form, ensure the `Can be Rented`{.interpreted-text
role="guilabel"} checkbox is ticked. Then, open the
`Rental prices`{.interpreted-text role="guilabel"} tab.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If creating a rental product outside of the *Rental* app, just ensure
the `Can be
Rented`{.interpreted-text role="guilabel"} checkbox is ticked on the
product form. By default, this checkbox is ticked whenever a product is
created directly in the *Rental* application.
:::

### Pricing

Under the `Pricing`{.interpreted-text role="guilabel"} section of the
`Rental prices`{.interpreted-text role="guilabel"} tab, designate custom
rental prices and rental periods for the product.

To add pricing for a rental, click `Add a price`{.interpreted-text
role="guilabel"}. Then, choose a *pricing period*
(`the unit of duration of the rental`{.interpreted-text role="dfn"}) in
the `Period`{.interpreted-text role="guilabel"} column, or create a new
pricing period by typing in the name and clicking
`Create`{.interpreted-text role="guilabel"}.

Next, decide whether or not to apply this custom rental price to a
specific `Pricelist`{.interpreted-text role="guilabel"}.

Lastly, enter the desired `Price`{.interpreted-text role="guilabel"} for
that specific `Period`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

There is no limit to how many pricing lines can be added. Multiple
pricing options for rental products are typically used to give discounts
for customers who agree to longer rental durations.
:::

To delete any rental pricing option, click the
`🗑️ (trash)`{.interpreted-text role="guilabel"} icon, and that row is
deleted.

### Reservations

Under the `Reservations`{.interpreted-text role="guilabel"} section of
the `Rental prices`{.interpreted-text role="guilabel"} tab, there is the
option to configure additional fines for any
`Extra Hour`{.interpreted-text role="guilabel"} or
`Extra Day`{.interpreted-text role="guilabel"} that the customer takes
to return a rental.

There is also the option to set a `Security Time`{.interpreted-text
role="guilabel"}, expressed in hours, to make the rental product
temporarily unavailable between two rental orders. Such a feature may
prove useful if maintenance or cleaning is required between rentals.

### Price computing

Odoo always uses two rules to compute the price of a product when a
rental order is created:

1.  Only one price line is used.
2.  The cheapest line is selected.

::: {.exercise}
Consider the following rental pricing configuration for a product:

-   1 day: \$100
-   3 days: \$250
-   1 week: \$500

A customer wants to rent this product for eight days. What price will
they pay?

After an order is created, Odoo selects the second line as this is the
cheapest option. The customer has to pay three times \'3 days\' to cover
the rental\'s eight days, for a total of \$750.
:::

Rental orders {#rental/customer-signature}
-------------

To create a rental order in the *Rental* app, navigate to
`Rental app --> Orders -->
Orders`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. Doing so reveals a blank
rental order form to be filled in accordingly.

{.align-center}

Start by adding a `Customer`{.interpreted-text role="guilabel"}, then
configure the desired duration of the rental in the
`Rental period`{.interpreted-text role="guilabel"} field.

To adjust the rental duration, click the first date in the
`Rental period`{.interpreted-text role="guilabel"} field, and select the
range of dates to represent the rental duration from the pop-up calendar
form that appears.

{.align-center}

Once complete, click `Apply`{.interpreted-text role="guilabel"} in the
calendar pop-up form. Following that, the pop-up form disappears, and
the designated time period of the rental is represented in the
`Duration`{.interpreted-text role="guilabel"} field.

Next, add a rental product in the `Order Lines`{.interpreted-text
role="guilabel"} tab, by clicking `Add a
product`{.interpreted-text role="guilabel"}, and selecting the desired
rental product to add to the form.

::: {.note}
::: {.title}
Note
:::

If a rental product is added *before* the
`Rental period`{.interpreted-text role="guilabel"} field has been
properly configured, the user can *still* adjust the
`Rental period`{.interpreted-text role="guilabel"} field accordingly.

Simply select the desired range of dates to represent the duration of
the rental, then click `Update Rental Prices`{.interpreted-text
role="guilabel"} in the `Duration`{.interpreted-text role="guilabel"}
field.

{.align-center}

Doing so reveals a `Confirmation`{.interpreted-text role="guilabel"}
pop-up window. If everything is correct, click `Ok`{.interpreted-text
role="guilabel"}, and Odoo recalculates the rental price accordingly.
:::

Once all the information has been entered correctly on the rental order
form, click the `Send by Email`{.interpreted-text role="guilabel"}
button to send the quotation to the customer, or click the
`Confirm`{.interpreted-text role="guilabel"} button to confirm the
order.

Customer signature
------------------

Upon confirming a rental order, the `Sign Documents`{.interpreted-text
role="guilabel"} button appears. This gives the ability to request the
customer sign a rental agreement, outlining the arrangement between the
company and customer, *before* they pick up the rental product(s).

Such documents can ensure everything is returned on-time and in its
original condition.

::: {.important}
::: {.title}
Important
:::

The `Sign Documents`{.interpreted-text role="guilabel"} button/option
**only** appears if the `Digital
Documents`{.interpreted-text role="guilabel"} feature has been activated
in the *Rental* application settings. To do so, navigate to
`Rental app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, activate `Digital
Documents`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

This feature also requires the
`Sign <../productivity/sign>`{.interpreted-text role="doc"} app. If
necessary, Odoo automatically installs it after activating the
`Digital Documents`{.interpreted-text role="guilabel"} setting.
:::

To request a customer signature on a rental agreement, select a
confirmed rental order, and click the `Sign Documents`{.interpreted-text
role="guilabel"} button to reveal a `Sign Documents`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

From here, select the desired document from the
`Document Template`{.interpreted-text role="guilabel"} field. Then,
click `Sign Document`{.interpreted-text role="guilabel"}. Doing so
reveals a `New Signature Request`{.interpreted-text role="guilabel"}
pop-up window.

{.align-center}

Upon confirming the information in the
`New Signature Request`{.interpreted-text role="guilabel"} pop-up form,
click `Sign Now`{.interpreted-text role="guilabel"} to initiate the
signing process.

A separate page is then revealed, showcasing the document to be signed,
which is accessible to the customer via the customer portal.

Odoo guides the customer through the signing process with clear,
clickable indicators, and allows them to create electronic signatures to
quickly complete the form.

{.align-center}

Once the document has been signed and completed, click the
`Validate & Send Completed
Document`{.interpreted-text role="guilabel"} button at the bottom of the
document.

{.align-center}

Upon clicking the `Validate & Send Completed Document`{.interpreted-text
role="guilabel"} button, Odoo presents the option to download the signed
document for record-keeping purposes, if necessary.

::: {.seealso}

:::

Pickup products {#rental/pickup-return}
---------------

When a customer picks up the product(s), navigate to the appropriate
rental order, click the `Pickup`{.interpreted-text role="guilabel"}
button, and then click `Validate`{.interpreted-text role="guilabel"} in
the `Validate a pickup`{.interpreted-text role="guilabel"} pop-up form
that appears.

Doing so places a `Picked-up`{.interpreted-text role="guilabel"} status
banner on the rental order.

Return products
---------------

When a customer returns the product(s), navigate to the appropriate
rental order, click the `Return`{.interpreted-text role="guilabel"}
button, and validate the return by clicking `Validate`{.interpreted-text
role="guilabel"} in the `Validate a return`{.interpreted-text
role="guilabel"} pop-up form that appears.

Doing so places a `Returned`{.interpreted-text role="guilabel"} status
banner on the rental order.

Print pickup and return receipts
--------------------------------

Pickup and return receipts can be printed for customers when they pick
up and/or return rental products.

To print pickup and/or return receipts, navigate to the appropriate
rental order, click the `⚙️ (gear)`{.interpreted-text role="guilabel"}
icon to reveal a drop-down menu.

{.align-center}

From this drop-down menu, hover over the `Print`{.interpreted-text
role="guilabel"} option to reveal a sub-menu. Then select
`Pickup and Return Receipt`{.interpreted-text role="guilabel"}.

Odoo generates and downloads a PDF, detailing all information about the
current status of the rented item(s).
