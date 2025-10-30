# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps.md

Three-step receipt
==================

Some companies require a quality control process before receiving goods
from suppliers. To accomplish this, Odoo has a three-step process for
receiving goods.

In the three-step receipt process, products are received in an input
area, then transferred to a quality area for inspection. Products that
pass the quality inspection are then transferred into stock. The
products are not available for further processing until they are
transferred out of the quality area and into stock.

Configuration
-------------

Odoo is configured by default to `receive and deliver goods in one step
<receipts_delivery_one_step>`{.interpreted-text role="doc"}, so the
settings need to be changed in order to utilize three-step receipts.
First, make sure the *Multi-Step Routes* option is enabled in `Inventory
--> Configuration --> Settings --> Warehouse`{.interpreted-text
role="menuselection"}. Note that activating
`Multi-Step Routes`{.interpreted-text role="guilabel"} will also
activate *Storage Locations*.

{.align-center}

Next, the warehouse needs to be configured for three-step receipts. To
do that, go to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and select the desired warehouse to be edited.
Doing so reveals the detail form for that specific warehouse.

On that `Warehouse`{.interpreted-text role="guilabel"} detail form page,
select `Receive goods in input, then
quality and then stock (3 steps)`{.interpreted-text role="guilabel"} for
`Incoming Shipments`{.interpreted-text role="guilabel"}.

{.align-center}

Activating three-step receipts and deliveries creates two new internal
locations: *Input* (WH/Input), and *Quality Control* (WH/Quality
Control). To rename these locations, go to
`Inventory app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}, then click on the desired location to change (or
update) the name.

Receive in three steps (input + quality + stock)
------------------------------------------------

### Create a purchase order

To create a new `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"}, navigate to `Purchase app -->
New`{.interpreted-text role="menuselection"}, which reveals a blank
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} form page.
On this page, select a `Vendor`{.interpreted-text role="guilabel"}, add
a storable `Product`{.interpreted-text role="guilabel"}, and click
`Confirm Order`{.interpreted-text role="guilabel"}.

A `Receipt`{.interpreted-text role="guilabel"} smart button will appear
in the top right, and the receipt will be associated with the purchase
order. Clicking on the `Receipt`{.interpreted-text role="guilabel"}
smart button will show the receipt order.

{.align-center}

### Process a receipt

Once the purchase order (PO) is confirmed, a receipt
([WH/IN]{.title-ref}) operation is generated and ready to process.

The receipt can be confirmed from the original purchase order form, or
it can be accessed by navigating to the
`Inventory app`{.interpreted-text role="menuselection"}, and locating
the `Receipts`{.interpreted-text role="guilabel"} task card.

Click the `# To Process`{.interpreted-text role="guilabel"} button to
reveal all incoming receipts to process. Click the receipt associated
with the previous purchase order.

Click `Validate`{.interpreted-text role="guilabel"} to validate the
receipt, and move the product to the destination location,
`WH/Input`{.interpreted-text role="guilabel"}.

{.align-center}

### Process a transfer to Quality Control

Once the receipt has been validated, an internal transfer operation to
move the product to quality control is ready to process.

Click `Inventory Overview`{.interpreted-text role="guilabel"} in the
breadcrumbs to navigate back to the dashboard, and locate the
`Internal Transfers`{.interpreted-text role="guilabel"} task card.

Select the `# To Process`{.interpreted-text role="guilabel"} button to
reveal all internal transfers to process. Then, choose the internal
transfer associated with the validated receipt.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to
complete the transfer, and move the product from
`WH/Input`{.interpreted-text role="guilabel"} to
`WH/Quality Control`{.interpreted-text role="guilabel"}.

{.align-center}

Process a transfer to stock
---------------------------

Once the internal transfer to move the product to quality control has
been validated, another internal transfer operation to move the product
into warehouse stock is ready to process.

Click `YourCompany: Internal Transfers`{.interpreted-text
role="guilabel"} in the breadcrumbs to reveal the list of all internal
transfers to process. Then, select the new internal transfer to move the
product from [WH/Quality Control]{.title-ref} to [WH/Stock]{.title-ref}.

Once ready, click `Validate`{.interpreted-text role="guilabel"} to
complete the transfer, and move the product from
`WH/Quality Control`{.interpreted-text role="guilabel"} to
`WH/Stock`{.interpreted-text role="guilabel"}.

{.align-center}
