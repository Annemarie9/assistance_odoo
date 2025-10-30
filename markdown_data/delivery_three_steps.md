# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps.md

Three-step delivery
===================

Some companies process large amounts of deliveries every day, many of
which include multiple products or require special packaging. To make
this efficient, a packing step is needed before shipping out products.
For this, Odoo has a three step process for delivering goods.

In the default three-step delivery process, products that are part of a
delivery order are picked in the warehouse according to their removal
strategy, and brought to a packing zone. After the items have been
packed into the different shipments in the packing zone, they are
brought to an output location before being shipped. These steps can be
modified if they do not fit the needs of the business.

Configuration
-------------

To change delivery settings from
`one step <receipts_delivery_one_step>`{.interpreted-text role="doc"} to
three steps, make sure the *Multi-Step Routes* option is enabled in
`Inventory app --> Configuration
--> Settings --> Warehouse`{.interpreted-text role="menuselection"}.
Note that activating `Multi-Step Routes`{.interpreted-text
role="guilabel"} will also activate *Storage Locations*.

{.align-center}

Next, the warehouse needs to be configured for three step deliveries. To
do this, go to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and click on the `warehouse`{.interpreted-text
role="guilabel"} to edit. Then, select
`Pack goods, send goods in output and then
deliver (3 steps)`{.interpreted-text role="guilabel"} for
`Outgoing Shipments`{.interpreted-text role="guilabel"}.

{.align-center}

Activating three-step receipts and deliveries creates two new internal
locations: a *Packing Zone* (WH/Packing Zone), and *Output* (WH/Output).
To rename these locations, go to
`Inventory app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}, click on the `Location`{.interpreted-text
role="guilabel"} to change, and update the name.

Deliver in three steps (pick + pack + ship)
-------------------------------------------

### Create a sales order

To create a new quote, navigate to
`Sales app --> Create`{.interpreted-text role="menuselection"}, which
reveals a blank quotation form. On the blank quotation form, select a
`Customer`{.interpreted-text role="guilabel"}, add a storable
`Product`{.interpreted-text role="guilabel"}, and click
`Confirm`{.interpreted-text role="guilabel"}.

A `Delivery`{.interpreted-text role="guilabel"} smart button appears in
the top right of the quotation form. Clicking it opens the picking order
to move the ordered product from [WH/Stock]{.title-ref} to [WH/Packing
Zone]{.title-ref}.

![After confirming the sales order, the Delivery smart button appears showing three items
associated with it.](delivery_three_steps/delivery-three-steps-smart-button.png){.align-center}

### Process a picking

The picking order will be created once the sales order is confirmed. To
view the picking, navigate to the `Inventory app`{.interpreted-text
role="menuselection"}, and locate the `Pick`{.interpreted-text
role="guilabel"} task card on the `Inventory Overview`{.interpreted-text
role="guilabel"} dashboard.

Click the `# To Process`{.interpreted-text role="guilabel"} button,
which reveals the picking order generated from the previously confirmed
sales order.

Click on the picking to process. If the product is in stock, Odoo will
automatically reserve the product. Click `Validate`{.interpreted-text
role="guilabel"} to mark the picking as done, and complete the transfer
to the `Packing Zone`{.interpreted-text role="guilabel"}.

{.align-center}

### Process a packing

After validating the picking, the packing order is ready to process.
Click back to the `Inventory Overview`{.interpreted-text
role="guilabel"}, and locate the `Pack`{.interpreted-text
role="guilabel"} task card on the dashboard.

Click the `# To Process`{.interpreted-text role="guilabel"} button (in
this case, `1 To Process`{.interpreted-text role="guilabel"}). This
reveals the packing order generated from the previously confirmed sales
order.

Click on the packing order associated with the sales order, then click
on `Validate`{.interpreted-text role="guilabel"} to complete the
packing.

{.align-center}

Once the packing order is validated, the product leaves the
`WH/Packing Zone`{.interpreted-text role="guilabel"} location and moves
to the `WH/Output`{.interpreted-text role="guilabel"} location. Then,
the status of the document will change to `Done`{.interpreted-text
role="guilabel"}.

### Process a delivery

Once the packing order has been validated, the delivery order is ready
to process. Navigate back to the original sales order to process the
delivery by going to `Sales app`{.interpreted-text
role="menuselection"}, and selecting the sales order created previously.

::: {.tip}
::: {.title}
Tip
:::

Delivery orders can *also* be accessed by going to
`Inventory app --> Operations
--> Deliveries`{.interpreted-text role="menuselection"}.
:::

The `Delivery`{.interpreted-text role="guilabel"} smart button now
indicates there are 3 transfers, instead of one. Clicking the
`Delivery`{.interpreted-text role="guilabel"} smart button shows the
three operations for this sales order: the picking, the packing, and the
delivery.

Click the delivery (WH/OUT) transfer to open the delivery order. Then,
click `Validate`{.interpreted-text role="guilabel"}.

![Click Validate on the delivery order to transfer the product from the output location to
the customer location.](delivery_three_steps/delivery-three-steps-delivery-order.png){.align-center}

Once the delivery order is validated, the product leaves the
`WH/Output`{.interpreted-text role="guilabel"} location and moves to the
`Partners/Customers`{.interpreted-text role="guilabel"} location. Then,
the status of the document will change to `Done`{.interpreted-text
role="guilabel"}.
