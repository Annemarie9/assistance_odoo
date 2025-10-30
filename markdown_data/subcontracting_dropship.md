# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_dropship.md

Dropship to subcontractor
=========================

In manufacturing, subcontracting is the process of a company engaging a
third-party manufacturer, or subcontractor, to manufacture products that
are then sold by the contracting company.

In Odoo, the *Dropship Subcontractor on Order* route is used to purchase
the necessary components for a subcontracted product from the vendor,
and have them delivered directly to the subcontractor, each time a
purchase order (PO) for that product is confirmed.

The subcontractor then uses the components to manufacture the desired
product, before shipping it back to the contracting company.

::: {.important}
::: {.title}
Important
:::

It is necessary to understand the differences between the *Dropship* and
*Dropship Subcontractor on Order* routes. While both routes involve
dropshipping, they are used for different purposes.

The *Dropship* route is used to purchase products from a vendor, and
have them shipped directly to the end customer.

The *Dropship Subcontractor on Order* route is used to purchase
components from a vendor, and have them shipped directly to a
subcontractor. By default, finished products are then sent from the
subcontractor back to the contracting company.

However, it is possible to combine both the *Dropship* and *Dropship
Subcontractor on Order* routes so they are used for the same product. In
this workflow, components are dropshipped to the subcontractor, who then
ships the finished product directly to the end customer.

This can be achieved by following steps one through five in the
`workflow section
<manufacturing/workflows/subcontracting-dropship>`{.interpreted-text
role="ref"} of this doc.
:::

Configuration
-------------

To use the *Dropship Subcontractor on Order* route, navigate to
`Manufacturing app
--> Configuration --> Settings`{.interpreted-text role="menuselection"},
and enable the checkbox next to `Subcontracting`{.interpreted-text
role="guilabel"}, under the `Operations`{.interpreted-text
role="guilabel"} heading.

Once the *Subcontracting* setting is enabled, it is also necessary to
properly configure the subcontracted product, the product\'s
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, and the
components listed on the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

### Configure product

To configure a product for the *Dropship Subcontractor on Order* route,
navigate to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product, or create a new one by
clicking `New`{.interpreted-text role="guilabel"}.

Select the `Purchase`{.interpreted-text role="guilabel"} tab, and add
the product\'s subcontractor as a vendor by clicking
`Add a line`{.interpreted-text role="guilabel"}, selecting the
subcontractor in the `Vendor`{.interpreted-text role="guilabel"}
drop-down menu, and entering a price in the `Price`{.interpreted-text
role="guilabel"} field.

Then, click on the `Inventory`{.interpreted-text role="guilabel"} tab to
configure a route that determines what happens to the finished product,
once it has been manufactured by the subcontractor.

If the finished product is shipped back to the contracting company, make
sure that the `Buy`{.interpreted-text role="guilabel"} route is
selected. In addition, select the
`Replenish on Order (MTO)`{.interpreted-text role="guilabel"} route to
automatically create a `PO (Purchase Order)`{.interpreted-text
role="abbr"} for the product upon confirmation of a
`SO (Sales Order)`{.interpreted-text role="abbr"}, unless there is
enough stock on-hand to fulfill the `SO (Sales Order)`{.interpreted-text
role="abbr"}.

If the finished product is shipped directly to the customer by the
subcontractor, make sure that only the `Dropship`{.interpreted-text
role="guilabel"} route is selected.

### Configure bill of materials

To configure a `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
for the *Dropship Subcontractor on Order* route, click the `Bill of
Materials`{.interpreted-text role="guilabel"} smart button on the
product\'s page, and select the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Alternatively, navigate to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}, and select the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} for the
subcontracted product.

::: {.seealso}
For a full overview of `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} configuration, see the `Bill of materials
<../basic_setup/bill_configuration>`{.interpreted-text role="doc"}
documentation.
:::

In the `BoM Type`{.interpreted-text role="guilabel"} field, select the
`Subcontracting`{.interpreted-text role="guilabel"} option. Then, add
one or more subcontractors in the `Subcontractors`{.interpreted-text
role="guilabel"} field that appears below.

{.align-center}

Finally, make sure that all necessary components are specified on the
`Components`{.interpreted-text role="guilabel"} tab. To add a new
component, click `Add a line`{.interpreted-text role="guilabel"}, select
the component in the `Component`{.interpreted-text role="guilabel"}
drop-down menu, and specify the required quantity in the
`Quantity`{.interpreted-text role="guilabel"} field.

### Configure Components

To configure components for the *Dropship Subcontractor on Order* route,
navigate to each component from the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} by selecting
the component\'s name in the `Components`{.interpreted-text
role="guilabel"} tab, and clicking the
`➡️ (right arrow)`{.interpreted-text role="guilabel"} button to the
right of the name.

Alternatively, navigate to each component by going to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and selecting the
component.

On the component product form, select the `Purchase`{.interpreted-text
role="guilabel"} tab, and add a vendor by clicking
`Add a line`{.interpreted-text role="guilabel"}, selecting the vendor in
the `Vendor`{.interpreted-text role="guilabel"} field, and adding the
price they sell the product for in the `Price`{.interpreted-text
role="guilabel"} field. This is the vendor that sends components to the
subcontractor, once they are purchased.

Then, click on the `Inventory`{.interpreted-text role="guilabel"} tab
and select the `Dropship Subcontractor on
Order`{.interpreted-text role="guilabel"} route in the
`Routes`{.interpreted-text role="guilabel"} section.

Repeat the process for every component that must be dropshipped to the
subcontractor.

Dropship subcontractor on order workflow {#manufacturing/workflows/subcontracting-dropship}
----------------------------------------

The dropship subcontractor on order workflow consists of up to six
steps:

1.  Create a sales order (SO) for the subcontracted product; doing so
    creates a *subcontractor* `PO (Purchase Order)`{.interpreted-text
    role="abbr"} to purchase the product from the subcontractor.
2.  Confirm the `PO (Purchase Order)`{.interpreted-text role="abbr"}
    created in the previous step, or create a new
    `PO (Purchase Order)`{.interpreted-text role="abbr"}; doing so
    creates a request for quotation (RfQ) to purchase the components
    from the vendor, as well as a receipt order or a dropship order.
3.  Confirm the `RfQ (Request for Quotation)`{.interpreted-text
    role="abbr"} to turn it into a second
    `PO (Purchase Order)`{.interpreted-text role="abbr"} (*vendor*
    `PO (Purchase Order)`{.interpreted-text role="abbr"}); doing so
    creates a *Dropship Subcontractor* order.
4.  Process the *Dropship Subcontractor* order once the vendor has sent
    the components to the subcontractor.
5.  Process the receipt once the subcontractor has finished
    manufacturing the subcontracted product, and shipped it back to the
    contracting company **OR** process the dropship order to ship the
    product directly to the end customer.
6.  If the workflow was started by creating an
    `SO (Sales Order)`{.interpreted-text role="abbr"}, and the finished
    product is not dropshipped to the end customer, process the delivery
    order once the product has been shipped to the customer.

The specific number of steps depends on the reason that the
subcontracted product is being purchased from the subcontractor.

If the reason is to fulfill a specific customer order, the process
starts with creating an SO, and ends with delivering the product to the
customer, or having the subcontractor dropship it to them.

If the reason is to increase quantity of stock on-hand, the process
starts with creating a PO, and ends with receiving the product into
inventory.

### Create an SO

It is only necessary to complete this step if the product is being
purchased from the subcontractor to fulfill a customer need. If the
product is being purchased to increase the quantity of stock on-hand,
move on to the next step.

To create a new `SO (Sales Order)`{.interpreted-text role="abbr"},
navigate to `Sales app --> Orders --> Orders`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}.

Select the customer in the `Customer`{.interpreted-text role="guilabel"}
drop-down menu. Then, click `Add a
product`{.interpreted-text role="guilabel"} on the
`Order Lines`{.interpreted-text role="guilabel"} tab, select the product
in the `Product`{.interpreted-text role="guilabel"} drop-down menu, and
enter a quantity in the `Quantity`{.interpreted-text role="guilabel"}
field.

Click `Confirm`{.interpreted-text role="guilabel"} to confirm the
`SO (Sales Order)`{.interpreted-text role="abbr"}, at which point a
`Purchase`{.interpreted-text role="guilabel"} smart button appears at
the top of the page. This is the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}, or the
`PO (Purchase Order)`{.interpreted-text role="abbr"} created to purchase
the subcontracted product from the subcontractor.

::: {.note}
::: {.title}
Note
:::

An `SO (Sales Order)`{.interpreted-text role="abbr"} for the product
only creates a *subcontractor* `PO (Purchase Order)`{.interpreted-text
role="abbr"} if the *Replenish on Order (MTO)* route is enabled on the
product\'s page, **and** there is no stock of the product on-hand.

If there is stock on-hand, confirming an
`SO (Sales Order)`{.interpreted-text role="abbr"} for the product will
instead create a delivery order, because Odoo assumes that the
`SO (Sales Order)`{.interpreted-text role="abbr"} is fulfilled using the
stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to
the end customer. In that case, a *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"} is **always**
created, even if there is stock on-hand.
:::

### Process subcontractor PO

If a *subcontractor* `PO (Purchase Order)`{.interpreted-text
role="abbr"} was not created in the previous step, do so now by
navigating to
`Purchase app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and clicking `New`{.interpreted-text
role="guilabel"}.

Begin filling out the `PO (Purchase Order)`{.interpreted-text
role="abbr"} by selecting a subcontractor from the
`Vendor`{.interpreted-text role="guilabel"} drop-down menu.

In the `Products`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"} to create a new
product line. Select a product produced by the subcontractor in the
`Product`{.interpreted-text role="guilabel"} field, and enter the
quantity in the `Quantity`{.interpreted-text role="guilabel"} field.

Finally, click `Confirm Order`{.interpreted-text role="guilabel"} to
confirm the *subcontractor* `PO (Purchase Order)`{.interpreted-text
role="abbr"}.

When a `PO (Purchase Order)`{.interpreted-text role="abbr"} is confirmed
for a product that requires dropshipping components to a subcontractor,
a receipt or dropship order is automatically created, and can be
accessed from the corresponding `Receipt`{.interpreted-text
role="guilabel"} or `Dropship`{.interpreted-text role="guilabel"} smart
button that appears at the top of the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

![A subcontractor PO for a \*Dropship Subcontractor on Order\* product, with a Receipt smart
button at the top of the page.](subcontracting_dropship/subcontractor-po.png){.align-center}

In addition, an `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} is created for the components that are purchased from the
vendor and sent to the subcontractor. However, the
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} **IS NOT**
automatically linked to the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

Once the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} is
confirmed and becomes a *vendor* `PO (Purchase Order)`{.interpreted-text
role="abbr"}, a *Dropship Subcontractor* order is created. This order is
linked to both the *vendor* `PO (Purchase Order)`{.interpreted-text
role="abbr"} and the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

### Confirm vendor RfQ

To access the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} created by confirming the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}, navigate to
`Purchase app --> Orders --> Requests for Quotation`{.interpreted-text
role="menuselection"}. Select the
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} that lists
the correct vendor in the `Vendor`{.interpreted-text role="guilabel"}
field, and the reference number of the receipt that was created after
confirming *subcontractor* `PO (Purchase Order)`{.interpreted-text
role="abbr"}, in the `Source Document`{.interpreted-text
role="guilabel"} field.

On the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, the
`Deliver To`{.interpreted-text role="guilabel"} field reads
`Dropship Subcontractor`{.interpreted-text role="guilabel"}, and the
`Dropship Address`{.interpreted-text role="guilabel"} field shows the
name of the subcontractor to whom components are being dropshipped.

Click `Confirm Order`{.interpreted-text role="guilabel"} to turn the
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} into a
*vendor* `PO (Purchase Order)`{.interpreted-text role="abbr"}, and
confirm the purchase of components from the vendor. After doing so, a
`Dropship`{.interpreted-text role="guilabel"} smart button appears at
the top of the *vendor* `PO (Purchase Order)`{.interpreted-text
role="abbr"}, and a `Resupply`{.interpreted-text role="guilabel"} smart
button appears at the top of the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

![A vendor PO for the components of a \*Dropship Subcontractor on Order\* product, with a
Dropship smart button at the top of the page.](subcontracting_dropship/vendor-po.png){.align-center}

### Process Dropship Subcontractor order

Once the components have been delivered to the subcontractor, navigate
to `Purchase
app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and select the *vendor*
`PO (Purchase Order)`{.interpreted-text role="abbr"} or the
*subcontractor* `PO (Purchase Order)`{.interpreted-text role="abbr"}.
Then, click the `Dropship`{.interpreted-text role="guilabel"} smart
button or the `Resupply`{.interpreted-text role="guilabel"} smart
button, respectively.

Clicking either button opens the *Dropship Subcontractor* order. Click
the `Validate`{.interpreted-text role="guilabel"} button at the top of
the order to confirm that the subcontractor has received the components.

### Process receipt or dropship order

Once the subcontractor has manufactured the finished product, navigate
to `Purchase
app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and select the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

If the subcontracted product should be received into inventory, once the
product arrives, click the `Receive Products`{.interpreted-text
role="guilabel"} button at the top of the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"} to open the
receipt. Then, click `Validate`{.interpreted-text role="guilabel"} at
the top of the receipt to register the product into inventory.

Alternatively, select the `Receipt`{.interpreted-text role="guilabel"}
smart button at the top of the *subcontractor*
`PO (Purchase Order)`{.interpreted-text role="abbr"}, and click
`Validate`{.interpreted-text role="guilabel"} at the top of the receipt.

If the subcontracted product should be dropshipped, select the
`Dropship`{.interpreted-text role="guilabel"} button at the top of the
page to open the dropship order, and click `Validate`{.interpreted-text
role="guilabel"} once the subcontractor has sent the product to the
customer.

### Process delivery order

If the subcontracting workflow was started by a customer
`SO (Sales Order)`{.interpreted-text role="abbr"}, and the finished
product was **not** dropshipped to the customer, but rather delivered to
the contracting company, it is necessary to ship the product to the
customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the
`Sales`{.interpreted-text role="menuselection"} app, and select the
`SO (Sales Order)`{.interpreted-text role="abbr"}. Select the
`Delivery`{.interpreted-text role="guilabel"} smart button at the top of
the page to open the delivery order, and click
`Validate`{.interpreted-text role="guilabel"} to confirm that the
product has been shipped to the customer.
