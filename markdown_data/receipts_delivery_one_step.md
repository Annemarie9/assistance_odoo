# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.md

One-step receipt and delivery
=============================

In Odoo *Inventory*, both incoming and outgoing shipments are configured
to process in one step, by default. This means purchases will be
received directly into stock, and deliveries will be moved directly from
stock to customers.

::: {.tip}
::: {.title}
Tip
:::

Incoming and outgoing shipments do **not** need to be configured with
the same amount of steps.

For example, a warehouse\'s settings can be configured so products can
be received directly in one step, and delivered in three steps (pick +
pack + ship).
:::

Configuration
-------------

To configure one-step receipts and deliveries for a warehouse, navigate
to `Inventory
app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and select a warehouse to edit.

Under the `Warehouse Configuration`{.interpreted-text role="guilabel"}
tab, set `Incoming Shipments`{.interpreted-text role="guilabel"} to
`Receive goods directly (1 step)`{.interpreted-text role="guilabel"},
and set `Outgoing Shipments`{.interpreted-text role="guilabel"} to
`Deliver goods directly (1 step)`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Since one-step receipt and delivery is the default for incoming and
outgoing shipments in Odoo, the *Multi-Step Routes* feature is *not*
required.

However, for the `Shipments`{.interpreted-text role="guilabel"} settings
to appear on a warehouse form, the feature **must** be enabled.

To enable *Multi-Step Routes*, navigate to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Under the
`Warehouse`{.interpreted-text role="guilabel"} section, tick the
checkbox next to `Multi-Step Routes`{.interpreted-text role="guilabel"},
and click `Save`{.interpreted-text role="guilabel"}. Doing so also
activates the `Storage Locations`{.interpreted-text role="guilabel"}
feature.
:::

Receive goods directly (1 step) {#inventory/receipts_delivery_one_step/wh}
-------------------------------

When products are received in one step, they will move from the vendor
location to warehouse stock in the database immediately upon validation
of a purchase order (PO).

### Create purchase order

To create a `PO (Purchase Order)`{.interpreted-text role="abbr"},
navigate to the `Purchase app`{.interpreted-text role="menuselection"},
and click `New`{.interpreted-text role="guilabel"}. This opens a blank
`Request for Quotation`{.interpreted-text role="guilabel"} (RfQ) form.

Add a vendor in the `Supplier`{.interpreted-text role="guilabel"} field.
Then, fill out the various fields on the
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, as
necessary.

{.align-center}

Under the `Products`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select a product
to add to the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"}.

Once ready, click `Confirm Order`{.interpreted-text role="guilabel"}.
This moves the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} to the `Purchase Order`{.interpreted-text role="guilabel"}
stage.

Once the `PO (Purchase Order)`{.interpreted-text role="abbr"} is
confirmed, a `Receipt`{.interpreted-text role="guilabel"} smart button
appears at the top of the form. Clicking the smart button opens the
warehouse receipt (WH/IN) form.

{.align-center}

### Process receipt

From the warehouse receipt form, the products ordered can be received
into the warehouse. To receive the products, click
`Validate`{.interpreted-text role="guilabel"}. Once validated, the
receipt moves to the `Done`{.interpreted-text role="guilabel"} stage.

{.align-center}

Click back to the `PO (Purchase Order)`{.interpreted-text role="abbr"}
(via the breadcrumbs, at the top of the form) to view the
`PO (Purchase Order)`{.interpreted-text role="abbr"} form. On the
product line, the quantity in the `Received`{.interpreted-text
role="guilabel"} column now matches the ordered
`Quantity`{.interpreted-text role="guilabel"}.

Deliver goods directly (1 step) {#inventory/delivery/one-step}
-------------------------------

When products are delivered in one step, they will move from warehouse
stock to the customer location in the database immediately upon
validation of a sales order (SO).

### Create sales order

To create a `SO (Sales Order)`{.interpreted-text role="abbr"}, navigate
to the `Sales app`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. This opens a blank sales
quotation form.

Add a customer in the `Customer`{.interpreted-text role="guilabel"}
field. Then, fill out the various fields on the sales quotation form, as
necessary.

{.align-center}

Under the `Product`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"}, and select a product
to add to the sales order quotation.

Once ready, click `Confirm`{.interpreted-text role="guilabel"}. This
moves the quotation to the `Sales Order`{.interpreted-text
role="guilabel"} stage.

Once the `SO (Sales Order)`{.interpreted-text role="abbr"} is confirmed,
a `Delivery`{.interpreted-text role="guilabel"} smart button appears at
the top of the form. Clicking the smart button opens the warehouse
delivery (WH/OUT) form.

{.align-center}

### Process delivery

From the warehouse delivery form, the products ordered by the customer
can be delivered from the warehouse. To deliver the products, change the
value in the `Quantity`{.interpreted-text role="guilabel"} field to
match the ordered quantity in the `Demand`{.interpreted-text
role="guilabel"} field.

Once ready, click `Validate`{.interpreted-text role="guilabel"}. Once
validated, the delivery order moves to the `Done`{.interpreted-text
role="guilabel"} stage.

{.align-center}

Click back to the `SO (Sales Order)`{.interpreted-text role="abbr"} (via
the breadcrumbs, at the top of the form) to view the
`SO (Sales Order)`{.interpreted-text role="abbr"} form. On the product
line, the quantity in the `Delivered`{.interpreted-text role="guilabel"}
column now matches the ordered `Quantity`{.interpreted-text
role="guilabel"}.

::: {.seealso}
`../daily_operations`{.interpreted-text role="doc"}
:::
