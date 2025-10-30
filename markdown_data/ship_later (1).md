Ship later
==========

The **Ship Later** feature allows you to sell products and schedule
delivery at a later date. It is useful, for example, when a product is
out of stock or so voluminous that it requires to be shipped, or if, for
any reason, the customer needs their order to be shipped later, etc.

Configuration
-------------

`Go to the POS settings <configuration/settings>`{.interpreted-text
role="ref"}, scroll down to the `Inventory`{.interpreted-text
role="guilabel"} section, and enable
`Allow Ship Later`{.interpreted-text role="guilabel"}.



Once activated, you can:

-   Choose the location from where the products are shipped by selecting
    a `Warehouse`{.interpreted-text role="guilabel"}.
-   Define a `Specific route`{.interpreted-text role="guilabel"}, or
    leave this field empty to use the default route.
-   Define the `Shipping Policy`{.interpreted-text role="guilabel"};
    select `As soon as possible`{.interpreted-text role="guilabel"} if
    the products can be delivered separately or
    `When all products are ready`{.interpreted-text role="guilabel"} to
    ship all the products at once.

::: {.seealso}
\-
`../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration`{.interpreted-text
role="doc"} -
`../../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses`{.interpreted-text
role="doc"}
:::

Practical application
---------------------

1.  `Open a session <pos/session-start>`{.interpreted-text role="ref"}
    and make a sale.
2.  On the payment screen, set a customer and select
    `Ship Later`{.interpreted-text role="guilabel"}.
3.  On the popup window, set a shipping date and click
    `Confirm`{.interpreted-text role="guilabel"} to proceed to payment.



The system instantly creates a delivery order from the warehouse to the
shipping address.

::: {.note}
::: {.title}
Note
:::

The selected customer must have referenced an address in the system for
products to be shipped.
:::
