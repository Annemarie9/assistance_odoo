# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps.md

Two-step receipt and delivery
=============================

Depending on a company\'s needs, receiving and shipping products in and
out of the warehouse might require multi-step operations. In Odoo
*Inventory*, this can be done using *Multi-Step Routes*.

In the two-step receipt process, products are received in an input area,
then transferred to stock. This kind of process for incoming shipments
might be beneficial for warehouses with specific storage locations, such
as freezers and refrigerators, secured locked areas, or special aisles
and shelves.

Products can be sorted according to where they are going to be stored,
and employees can stock all the products going to a specific location.
The products are *not* available for further processing, until they are
transferred into stock.

In the two-step delivery process, products are first picked from their
respective location in the warehouse, then transferred to an output
location before being shipped to the customer.

This might be beneficial for companies using a First In, First Out
(FIFO), Last In, First Out (LIFO), or First Expired, First Out (FEFO)
removal strategy.

::: {.tip}
::: {.title}
Tip
:::

Incoming and outgoing shipments do **not** need to be configured with
the same amount of steps.

For example, a warehouse\'s settings can be configured so products can
be received in two steps (input + stock), and delivered in three steps
(pick + pack + ship).
:::

Configuration
-------------

In Odoo *Inventory*, both incoming and outgoing shipments are configured
to process in one step, by default. To change these settings, the
*Multi-Step Routes* feature must be enabled.

To enable *Multi-Step Routes*, navigate to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Under the
`Warehouse`{.interpreted-text role="guilabel"} section, tick the
checkbox next to `Multi-Step
Routes`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}. Doing so also activates the
`Storage Locations`{.interpreted-text role="guilabel"} feature.

{.align-center}

Next, configure a warehouse for two-step receipts and deliveries.
Navigate to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and select a warehouse to edit.

Under the `Warehouse Configuration`{.interpreted-text role="guilabel"}
tab, set `Incoming Shipments`{.interpreted-text role="guilabel"} to
`Receive goods in input and then stock (2 steps)`{.interpreted-text
role="guilabel"}, and set `Outgoing Shipments`{.interpreted-text
role="guilabel"} to
`Send goods in output and then deliver (2 steps)`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Selecting two-step receipts and deliveries automatically creates new
*Input* and *Output* warehouse locations in the database, named
[WH/Input]{.title-ref} and [WH/Output]{.title-ref}, respectively.

To rename or edit these locations, navigate to
`Inventory app --> Configuration
--> Locations`{.interpreted-text role="menuselection"}, and select the
desired location.

On the location\'s form, change the `Location Name`{.interpreted-text
role="guilabel"}, and make any other necessary changes.
:::

Process receipt in two steps (input + stock)
--------------------------------------------

When products are received in two steps, they first move from the vendor
location to an input location. Then, they move from the input location
to warehouse stock in the database, upon validation of a purchase order
(PO), and a subsequent internal transfer.

### Create purchase order

To create a `PO (Purchase Order)`{.interpreted-text role="abbr"},
navigate to the `Purchase app`{.interpreted-text role="menuselection"},
and click `New`{.interpreted-text role="guilabel"}. This opens a blank
`Request for Quotation`{.interpreted-text role="guilabel"} (RfQ) form.

Add a vendor in the `Vendor`{.interpreted-text role="guilabel"} field.
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

::: {.tip}
::: {.title}
Tip
:::

For businesses with multiple warehouses that have different step
configurations, the `Deliver To`{.interpreted-text role="guilabel"}
field on the `PO (Purchase Order)`{.interpreted-text role="abbr"} form
**must** be specified as the correct *input location* connected to the
two-step warehouse.

This can be done by selecting the warehouse from the drop-down menu that
includes the [Receipts]{.title-ref} label at the end of the name.
:::

### Process receipt

From the warehouse receipt form, the products ordered can be received
into the warehouse. To receive the products, click
`Validate`{.interpreted-text role="guilabel"}. Once validated, the
receipt moves to the `Done`{.interpreted-text role="guilabel"} stage,
and the products move to the `WH/Input`{.interpreted-text
role="guilabel"} location.

{.align-center}

Click back to the `PO (Purchase Order)`{.interpreted-text role="abbr"}
(via the breadcrumbs, at the top of the form) to view the
`PO (Purchase Order)`{.interpreted-text role="abbr"} form. On the
product line, the quantity in the `Received`{.interpreted-text
role="guilabel"} column now matches the ordered
`Quantity`{.interpreted-text role="guilabel"}.

### Process internal transfer

Once the receipt is validated, an internal transfer is created and ready
to process.

To view the internal transfer, navigate to the
`Inventory app`{.interpreted-text role="menuselection"}, and locate the
`Internal Transfers`{.interpreted-text role="guilabel"} task card.

Click the `# To Process`{.interpreted-text role="guilabel"} button on
the task card to reveal a list of all internal transfers to process, and
select the transfer associated with the previously validated receipt.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to
complete the transfer, and move the product from
`WH/Input`{.interpreted-text role="guilabel"} to
`WH/Stock`{.interpreted-text role="guilabel"}.

Once the transfer is validated, the products enter inventory, and are
available for customer deliveries or manufacturing orders.

{.align-center}

Process delivery order in two steps (pick + ship) {#inventory/shipping_receiving/two-step-delivery}
-------------------------------------------------

When products are delivered in two steps, they move from warehouse stock
to an output location. Then, they move from the output location to a
customer location in the database, upon validation of a picking order,
and a subsequent delivery order (DO).

### Create sales order

To create a `SO (Sales Order)`{.interpreted-text role="abbr"}, navigate
to the `Sales app`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. This opens a blank sales
quotation form.

Add a customer in the `Customer`{.interpreted-text role="guilabel"}
field. Then, fill out the various fields on the sales quotation form, as
necessary.

{.align-center}

Under the `Order Lines`{.interpreted-text role="guilabel"} tab, click
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

### Process picking

Once the sales order is confirmed, a picking order is generated and
ready to process.

To complete the picking, navigate to the
`Inventory app`{.interpreted-text role="guilabel"}, and locate the
`Pick`{.interpreted-text role="guilabel"} task card on the
`Inventory Overview`{.interpreted-text role="guilabel"} dashboard.
Alternatively, the picking order can also be accessed via the
`Delivery`{.interpreted-text role="guilabel"} smart button at the top of
the sales order form.

From the `Inventory Overview`{.interpreted-text role="guilabel"} page,
click the `# To Process`{.interpreted-text role="guilabel"} button on
the `Pick`{.interpreted-text role="guilabel"} task card. This reveals a
list of all pickings to process.

Click on the picking (WH/PICK) operation associated with the sales order
to reveal the picking order.

{.align-center}

Manually set the quantity by changing the value in the
`Quantity`{.interpreted-text role="guilabel"} column, to match the value
in the `Demand`{.interpreted-text role="guilabel"} column.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to
complete the picking, and move the product from
`WH/Stock`{.interpreted-text role="guilabel"} to
`WH/Output.`{.interpreted-text role="guilabel"}

### Process delivery

Once the picking is validated, a delivery order is created, and ready to
process. Clicking the `Delivery`{.interpreted-text role="guilabel"}
smart button on the sales order form reveals the newly created delivery
order.

Alternatively, to view the delivery order, navigate back to the
`Inventory Overview`{.interpreted-text role="guilabel"} page, via the
breadcrumbs, and locate the `Delivery Orders`{.interpreted-text
role="guilabel"} task card.

Click the `# To Process`{.interpreted-text role="guilabel"} button on
the task card to reveal a list of all delivery orders to process, and
select the order associated with the previously validated picking.

{.align-center}

To deliver the products, change the value in the
`Quantity`{.interpreted-text role="guilabel"} field to match the ordered
quantity in the `Demand`{.interpreted-text role="guilabel"} field.

Once ready, click `Validate`{.interpreted-text role="guilabel"}. Once
validated, the delivery order moves to the `Done`{.interpreted-text
role="guilabel"} stage.

::: {.seealso}
`../daily_operations`{.interpreted-text role="doc"}
:::
