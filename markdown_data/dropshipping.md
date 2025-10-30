# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping.md

Dropshipping
============

Dropshipping is an order fulfillment strategy that allows sellers to
have items shipped directly from suppliers to customers. Normally, a
seller purchases a product from a supplier, stores it in their
inventory, and ships it to the end customer once an order is placed.
With dropshipping, the supplier is responsible for storing and shipping
the item. This benefits the seller by reducing inventory costs,
including the price of operating warehouses.

Configure products to be dropshipped
------------------------------------

To use dropshipping as a fulfillment strategy, navigate to the
`Purchase`{.interpreted-text role="menuselection"} app and select
`Configuration --> Settings`{.interpreted-text role="menuselection"}.
Under the `Logistics`{.interpreted-text role="guilabel"} heading, click
the `Dropshipping`{.interpreted-text role="guilabel"} checkbox, and
`Save`{.interpreted-text role="guilabel"} to finish.

Next, go to the `Sales`{.interpreted-text role="menuselection"} app,
click `Products --> Products`{.interpreted-text role="menuselection"}
and choose an existing product or select `Create`{.interpreted-text
role="guilabel"} to configure a new one. On the
`Product`{.interpreted-text role="guilabel"} page, make sure that the
`Can be Sold`{.interpreted-text role="guilabel"} and
`Can be Purchased`{.interpreted-text role="guilabel"} checkboxes are
enabled.

{.align-center}

Click on the `Purchase`{.interpreted-text role="guilabel"} tab and
specify a vendor and the price that they sell the product for. Multiple
vendors can be added, but the vendor at the top of the list will be the
one automatically selected for purchase orders.

{.align-center}

Finally, select the `Inventory`{.interpreted-text role="guilabel"} tab
and enable the `Dropship`{.interpreted-text role="guilabel"} checkbox in
the `Routes`{.interpreted-text role="guilabel"} section.

{.align-center}

::: {.note}
::: {.title}
Note
:::

While it is not necessary to enable the `Buy`{.interpreted-text
role="guilabel"} route in addition to the `Dropship`{.interpreted-text
role="guilabel"} route, enabling both provides the option of
dropshipping the product or purchasing it directly.
:::

Fulfill orders using dropshipping
---------------------------------

When a sales order is created for a dropshipped product, an associated
request for quotation (RfQ) is automatically generated to purchase the
product from the vendor. Sales orders can be viewed in the
`Sales`{.interpreted-text role="menuselection"} app by selecting
`Orders --> Orders`{.interpreted-text role="menuselection"}. Click the
`Purchase`{.interpreted-text role="guilabel"} smart button at the top
right of a sales order to view the associated
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"}.

{.align-center}

Once the `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} is
confirmed, it becomes a purchase order, and a dropship receipt is
created and linked to it. The receipt can be viewed by clicking the
`Dropship`{.interpreted-text role="guilabel"} smart button in the
top-right corner of the purchase order form.

{.align-center}

The dropship receipt displays `Partners/Vendors`{.interpreted-text
role="guilabel"} in the `Source Location`{.interpreted-text
role="guilabel"} field, and `Partners/Customers`{.interpreted-text
role="guilabel"} in the `Destination Location`{.interpreted-text
role="guilabel"} field. Upon delivery of the product to the customer,
click on the `Validate`{.interpreted-text role="guilabel"} button at the
top-left of the dropship receipt to confirm the delivered quantity.

{.align-center}

To view all dropship orders, simply navigate to the
`Inventory`{.interpreted-text role="menuselection"}
`Overview`{.interpreted-text role="guilabel"} dashboard and click the
teal `# TO PROCESS`{.interpreted-text role="guilabel"} button on the
`Dropship`{.interpreted-text role="guilabel"} card.

{.align-center}
