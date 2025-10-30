# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/order_handling.md

Order handling
==============

When a customer orders on your eCommerce, there are **three** record
types required to be handle in Odoo:

-   `Sales orders <handling/sales>`{.interpreted-text role="ref"};
-   `Delivery orders <handling/delivery>`{.interpreted-text role="ref"};
-   `Invoices & legal requirements <handling/legal>`{.interpreted-text
    role="ref"}.

Sales orders {#handling/sales}
------------

### Order and payment status

The first step when a customer adds a product to his cart is the
creation of a quotation. Orders can be managed either from the
**Website** or `Sales </applications/sales/sales>`{.interpreted-text
role="doc"} app. eCommerce orders can automatically be assigned to a
specific sales team by going to `Website
--> Configuration --> Settings`{.interpreted-text role="menuselection"}.
In the **Shop - Checkout Process** section, select a
`Sales Team`{.interpreted-text role="guilabel"} or
`Salesperson`{.interpreted-text role="guilabel"} to handle eCommerce
orders.

{.align-center}

Orders can be found under
`Website --> eCommerce --> Orders/Unpaid Orders`{.interpreted-text
role="menuselection"}. Each order goes through a different status:

-   **Quotation**: a new product is added to the cart, but the customer
    has *not* gone through the checkout process yet;
-   **Quotation sent**: the customer has gone through the checkout
    process and confirmed the order, but the payment is not yet
    confirmed;
-   **Order**: the customer has gone through the checkout process,
    confirmed the order, and the payment is received.

{.align-center}

### Abandoned cart

An **abandoned cart** represents an order for which the customer did
**not finish** the checkout confirmation process. For these orders, it
is possible to send an **email reminder** to the customer automatically.
To enable that feature, go to `Website --> Configuration -->
Settings`{.interpreted-text role="menuselection"} and in the
`Email & Marketing`{.interpreted-text role="guilabel"} section, enable
`Automatically send
abandoned checkout emails`{.interpreted-text role="guilabel"}. Once
enabled, you can set the **time-lapse** after which the email is sent
and customize the **email template** used.

::: {.note}
::: {.title}
Note
:::

For abandoned cart emails, the customer must either have entered their
contact details during the checkout process; or be logged-in when they
added the product to their cart.
:::

Delivery orders {#handling/delivery}
---------------

### Delivery flow

Once a quotation has been confirmed, a delivery order is automatically
created. The next step is to process this delivery.

Packing eCommerce orders usually requires picking the product, preparing
the packaging, printing the shipping label(s) and shipping to the
customer. Depending on the number of orders, strategy, or resources,
those steps can be considered as one or multiple actions in Odoo.

An automatic email can be sent to the customer when the transfer status
in Odoo is "done". To do so, enable the feature in the settings of the
`Inventory </applications/inventory_and_mrp/inventory>`{.interpreted-text
role="doc"} app.

::: {.note}
::: {.title}
Note
:::

If customers are allowed to pay when picking up their order in stores or
by wire transfer, the quotation is **not** be confirmed and the stock is
**not** be reserved. Orders must be confirmed manually to reserve
products in stock.
:::

::: {.seealso}
\-
`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/invoicing`{.interpreted-text
role="doc"} -
`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels`{.interpreted-text
role="doc"} -
`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/multipack`{.interpreted-text
role="doc"}
:::

### Returns and refunds

Customers can only return an order through an online form. It may not be
possible to return products depending on the return strategy or type of
product.

Full refunds can be directly sent to customers from within the order
interface. A refund-compatible payment provider needs to be enabled
first.

::: {.seealso}
\- `/applications/sales/sales/products_prices/returns`{.interpreted-text
role="doc"} -
`/applications/services/helpdesk/advanced/after_sales`{.interpreted-text
role="doc"} -
`/applications/finance/payment_providers`{.interpreted-text role="doc"}
:::

Invoice and legal requirements {#handling/legal}
------------------------------

The final step of an ecommerce order is to generate the invoice and send
it to the customer. Depending on the type of business (B2B or B2C), an
invoice can either be generated automatically (B2B) or on demand of the
customer (B2C). This process can be automated if (and when) the online
payment is `confirmed <handling/sales>`{.interpreted-text role="ref"}.

To automate invoicing, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and in the `Invoicing`{.interpreted-text
role="guilabel"} section, enable `Automatic Invoice`{.interpreted-text
role="guilabel"}.
