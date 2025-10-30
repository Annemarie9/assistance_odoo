# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/invoicing.md

Shipping cost invoicing
=======================

Invoicing customers for shipping after delivery ensures accurate charges
based on real-time shipping factors like distance, weight, and method.

In Odoo, shipping costs can be invoiced in two ways:

1.  Agree with the customer on a fixed cost and
    `include it in the sale order.
    <inventory/shipping/invoice-so>`{.interpreted-text role="ref"}
2.  `Invoice shipping costs to the customer post-delivery
    <inventory/shipping/invoice-shipping>`{.interpreted-text
    role="ref"}, reflecting the actual expenses incurred by the
    business.

Configuration
-------------

To set prices to delivery methods, go to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Under the
`Shipping`{.interpreted-text role="guilabel"} section, enable the
`Delivery Methods`{.interpreted-text role="guilabel"} feature. Then,
click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

Add shipping method
-------------------

Next, configure the the price of each delivery method by going to
`Inventory app -->
Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"} and click the `Create`{.interpreted-text
role="guilabel"} button. Doing so opens a form to provide details about
the shipping provider, including:

-   `Shipping Method`{.interpreted-text role="guilabel"} (*required*)
    the name of the delivery method (e.g. [flat-rate
    shipping]{.title-ref}, [same day delivery]{.title-ref}, etc.).

-   `Provider`{.interpreted-text role="guilabel"} (*required*): choose
    the delivery service, like FedEx, if using a third-party carrier
    Ensure the integration with the shipping carrier is properly
    installed and select the provider from the drop-down menu.

    ::: {.seealso}
    `../setup_configuration/third_party_shipper`{.interpreted-text
    role="doc"}
    :::

-   `Company`{.interpreted-text role="guilabel"}: if the shipping method
    should apply to a specific company, select it from the drop-down
    menu. Leave the field blank to apply the method to all companies.

-   `Website`{.interpreted-text role="guilabel"}: configure shipping
    methods for an e-commerce page. Select the applicable website from
    the drop-down menu, or leave it blank to apply the method to all web
    pages.

-   `Delivery Product`{.interpreted-text role="guilabel"} (*required*):
    the product listed on the `sales order line
    <inventory/shipping/invoice-on-so>`{.interpreted-text role="ref"} as
    the delivery charge.

-   `Free if order amount is above`{.interpreted-text role="guilabel"}:
    checking this box enables free shipping if the customer spends above
    the specified amount.

Invoice cost on sales order {#inventory/shipping/invoice-so}
---------------------------

To invoice shipping costs on the sales order, before the item is
delivered, go to the `Sales app`{.interpreted-text role="menuselection"}
and select the desired sales order.

On the sales order, click the `Add Shipping`{.interpreted-text
role="guilabel"} button at the bottom-right corner.

{.align-center}

In the `Add a shipping method`{.interpreted-text role="guilabel"} pop-up
window, choose the intended carrier in the
`Shipping Method`{.interpreted-text role="guilabel"} field.

Then, click the `Get Rate`{.interpreted-text role="guilabel"} button to
the calculate shipping price based on real-time shipping data Odoo\'s
shipping carrier integration.

The `Cost`{.interpreted-text role="guilabel"} is automatically
calculated using the weight of the items in the order. Finally, click
the `Add`{.interpreted-text role="guilabel"} button to close the window.

{.align-center}

::: {#inventory/shipping/invoice-on-so}
On the sales order, the delivery product appears in the
`Order Lines`{.interpreted-text role="guilabel"} tab, with the
`Unit Price`{.interpreted-text role="guilabel"} set as the shipping cost
calculated in the `Add a shipping method`{.interpreted-text
role="guilabel"} pop-up window.
:::

{.align-center}

Finally, after the product is delivered, click the
`Create invoice`{.interpreted-text role="guilabel"} button, and an
invoice is created that includes the shipping cost that was added
earlier.

{.align-center}

Then, click the `Create and View Invoice`{.interpreted-text
role="guilabel"} button, and a draft invoice is generated, with the
shipping cost included in the `Invoice Lines`{.interpreted-text
role="guilabel"} tab.

{.align-center}

Invoice real shipping costs {#inventory/shipping/invoice-shipping}
---------------------------

To modify the invoice to reflect the real cost of shipping, follow the
steps `above
<inventory/shipping/invoice-so>`{.interpreted-text role="ref"} to create
an invoice with a delivery product with a `Unit
Price`{.interpreted-text role="guilabel"} of zero.

Then, on a draft invoice, modify the `Unit Price`{.interpreted-text
role="guilabel"} to reflect the real shipping cost. Finally, invoice the
customer the adjusted shipping cost by clicking
`Confirm`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
\- `../setup_configuration/third_party_shipper`{.interpreted-text
role="doc"} - `../setup_configuration/labels`{.interpreted-text
role="doc"}
:::
