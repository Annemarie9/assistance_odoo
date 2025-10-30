# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_resupply.md

Resupply subcontractor
======================

In manufacturing, subcontracting is the process of a company engaging a
third-party manufacturer, or subcontractor, to manufacture products that
are then sold by the contracting company.

In Odoo, the *Resupply Subcontractor on Order* route is used to deliver
the necessary components for a subcontracted product to the
subcontractor, each time a purchase order (PO) for that product is
confirmed.

The subcontractor then uses the components to manufacture the desired
product, before shipping it back to the contracting company, or
dropshipping it to the end customer.

::: {.important}
::: {.title}
Important
:::

It is necessary to understand the differences between the *Resupply
Subcontractor on Order* and the *Dropship Subcontractor on Order*
routes.

While both routes are used to supply a subcontractor with the components
required for manufacturing a product, they differ in how the components
are sourced.

When using *Resupply Subcontractor on Order*, components are shipped
from the warehouse of the contracting company.

When using *Dropship Subcontractor on Order*, components are purchased
from a vendor and shipped directly to the subcontractor.

The choice of which route to use depends upon the specific requirements
of the subcontracting company and their subcontractors.

See the `subcontracting_dropship`{.interpreted-text role="doc"}
documentation for a full overview of the *Dropship Subcontractor on
Order* route.
:::

Configuration
-------------

To use the *Resupply Subcontractor on Order* route, navigate to
`Manufacturing app
--> Configuration --> Settings`{.interpreted-text role="menuselection"},
and enable the checkbox next to `Subcontracting`{.interpreted-text
role="guilabel"}, under the `Operations`{.interpreted-text
role="guilabel"} heading.

Once the *Subcontracting* setting is enabled, it is also necessary to
properly configure the subcontracted product, the product\'s bill of
materials (BoM), and the components listed on the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

### Configure product {#manufacturing/workflows/subcontracting_resupply/product-config}

To configure a product for the *Resupply Subcontractor on Order* route,
navigate to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product, or create a new one by
clicking `New`{.interpreted-text role="guilabel"}.

Select the `Purchase`{.interpreted-text role="guilabel"} tab, and add
the product\'s subcontractor as a vendor by clicking
`Add a line`{.interpreted-text role="guilabel"}, selecting the
subcontractor in the `Vendor`{.interpreted-text role="guilabel"}
drop-down menu, and entering a price in the `Price`{.interpreted-text
role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The value entered in the `Price`{.interpreted-text role="guilabel"}
field on the `Purchase`{.interpreted-text role="guilabel"} tab of the of
the subcontracted product\'s page is the amount paid to the
subcontractor for the manufacturing of the product.

This does not represent the total cost of the product, which includes
other elements, like the cost of the product\'s components.
:::

Then, click on the `Inventory`{.interpreted-text role="guilabel"} tab to
configure a route that determines what happens to the finished product,
once it has been manufactured by the subcontractor.

If the finished product is shipped back to the contracting company, make
sure that the `Buy`{.interpreted-text role="guilabel"} route is
selected. In addition, select the
`Replenish on Order (MTO)`{.interpreted-text role="guilabel"} route to
automatically create a `PO (Purchase Order)`{.interpreted-text
role="abbr"} for the product upon confirmation of a sales order (SO),
unless there is enough stock on-hand to fulfill the
`SO (Sales Order)`{.interpreted-text role="abbr"}.

If the finished product is shipped directly to the customer by the
subcontractor, make sure that only the `Dropship`{.interpreted-text
role="guilabel"} route is selected.

### Configure BoM

To configure a `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
for the *Resupply Subcontractor on Order* route, click the `Bill of
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

### Configure components

To configure components for the *Resupply Subcontractor on Order* route,
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

On the component product form, click on the
`Inventory`{.interpreted-text role="guilabel"} tab and select the
`Resupply Subcontractor on Order`{.interpreted-text role="guilabel"}
route in the `Routes`{.interpreted-text role="guilabel"} section.

Repeat the process for every component that must be sent to the
subcontractor.

Resupply subcontractor on order workflow
----------------------------------------

The resupply subcontractor on order workflow consists of up to five
steps:

1.  Create an `SO (Sales Order)`{.interpreted-text role="abbr"} for the
    subcontracted product; doing so creates a
    `PO (Purchase Order)`{.interpreted-text role="abbr"} to purchase the
    product from the subcontractor.
2.  Confirm the `PO (Purchase Order)`{.interpreted-text role="abbr"}
    created in the previous step, or create a new
    `PO (Purchase Order)`{.interpreted-text role="abbr"}; doing so
    creates a *Resupply Subcontractor* order, as well as a receipt order
    or a dropship order.
3.  Process the *Resupply Subcontractor* order once components for the
    subcontracted product have been sent to the subcontractor.
4.  Process the receipt once the subcontractor has finished
    manufacturing the subcontracted product, and shipped it back to the
    contracting company **OR** process the dropship order to ship the
    product directly to the customer.
5.  If the workflow was started by creating an
    `SO (Sales Order)`{.interpreted-text role="abbr"}, and the finished
    product is not dropshipped to the end customer, process the delivery
    order once the product is shipped to the customer.

The specific number of steps depends on the reason that the
subcontracted product is being purchased from the subcontractor.

If the reason is to fulfill a specific customer order, the process
starts with creating an `SO (Sales Order)`{.interpreted-text
role="abbr"}, and ends with delivering the product to the customer, or
having the subcontractor dropship it to them.

If the reason is to increase the quantity of stock on-hand, the process
starts with creating a `PO (Purchase Order)`{.interpreted-text
role="abbr"}, and ends with receiving the product into inventory.

::: {.important}
::: {.title}
Important
:::

While the *Resupply Subcontractor on Order* route can be used to
automatically resupply a subcontractor upon confirmation of a
`PO (Purchase Order)`{.interpreted-text role="abbr"}, it is also
possible to create a resupply order manually. This workflow is useful
when it is necessary to resupply the subcontractor without creating a
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

To resupply a subcontractor manually, navigate to the
`Inventory`{.interpreted-text role="menuselection"} app, and click on
the `Resupply Subcontractor`{.interpreted-text role="guilabel"} card.
Create a new *Resupply Subcontractor* order by clicking
`New`{.interpreted-text role="guilabel"}.

In the `Delivery Address`{.interpreted-text role="guilabel"} field,
select the subcontractor to whom the components should be sent.

Then, add each component to the `Operations`{.interpreted-text
role="guilabel"} tab by clicking `Add a line`{.interpreted-text
role="guilabel"}, selecting the component in the
`Product`{.interpreted-text role="guilabel"} drop-down field, and
specifying a quantity in the `Demand`{.interpreted-text role="guilabel"}
field.

Finally, click `Mark as Todo`{.interpreted-text role="guilabel"} to
register the order. Once the components have been sent to the
subcontractor, click `Validate`{.interpreted-text role="guilabel"} to
confirm that the order has been sent.
:::

### Create SO

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
`Order Lines`{.interpreted-text role="guilabel"} tab, select a
subcontracted product in the `Product`{.interpreted-text
role="guilabel"} drop-down menu, and enter a quantity in the
`Quantity`{.interpreted-text role="guilabel"} field.

Click `Confirm`{.interpreted-text role="guilabel"} to confirm the
`SO (Sales Order)`{.interpreted-text role="abbr"}, at which point a
`Purchase`{.interpreted-text role="guilabel"} smart button appears at
the top of the page. This opens the
`PO (Purchase Order)`{.interpreted-text role="abbr"} created to purchase
the subcontracted product from the subcontractor.

::: {.note}
::: {.title}
Note
:::

An `SO (Sales Order)`{.interpreted-text role="abbr"} for the product
only creates a `PO (Purchase Order)`{.interpreted-text role="abbr"} if
the *Replenish on Order (MTO)* route is enabled on the product\'s page,
**and** there is not enough stock of the product on-hand to fulfill the
`SO (Sales Order)`{.interpreted-text role="abbr"}.

If there is enough stock on-hand, confirming an
`SO (Sales Order)`{.interpreted-text role="abbr"} for the product
instead creates a delivery order, because Odoo assumes that the
`SO (Sales Order)`{.interpreted-text role="abbr"} is fulfilled using the
stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to
the end customer. In that case, a
`PO (Purchase Order)`{.interpreted-text role="abbr"} is **always**
created, even if there is enough stock on-hand.
:::

### Process PO

If a `PO (Purchase Order)`{.interpreted-text role="abbr"} was created in
the previous step, navigate to `Purchase app --> Orders -->
Purchase Orders`{.interpreted-text role="guilabel"}, and select the
`PO (Purchase Order)`{.interpreted-text role="abbr"}. Then, click
`Confirm Order`{.interpreted-text role="guilabel"} to confirm it.

If a `PO (Purchase Order)`{.interpreted-text role="abbr"} was not
created in the previous step, do so now by navigating to `Purchase
app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and clicking `New`{.interpreted-text
role="guilabel"}.

Begin filling out the `PO (Purchase Order)`{.interpreted-text
role="abbr"} by selecting a subcontractor from the
`Vendor`{.interpreted-text role="guilabel"} drop-down menu. In the
`Products`{.interpreted-text role="guilabel"} tab, click
`Add a product`{.interpreted-text role="guilabel"} to create a new
product line. Select a subcontracted product in the
`Product`{.interpreted-text role="guilabel"} field, and enter the
quantity in the `Quantity`{.interpreted-text role="guilabel"} field.
Finally, click `Confirm Order`{.interpreted-text role="guilabel"} to
confirm the `PO (Purchase Order)`{.interpreted-text role="abbr"}.

When a `PO (Purchase Order)`{.interpreted-text role="abbr"} is confirmed
for a product that requires resupplying a subcontractor with components,
a receipt or dropship order is automatically created, and can be
accessed from the corresponding `Receipt`{.interpreted-text
role="guilabel"} or `Dropship`{.interpreted-text role="guilabel"} smart
button that appears at the top of the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

In addition, a *Resupply Subcontractor* order is created to ship the
required components to the subcontractor. This order can also be
accessed from the `PO (Purchase Order)`{.interpreted-text role="abbr"},
by clicking the `Resupply`{.interpreted-text role="guilabel"} smart
button at the top of the page.

{.align-center}

### Process Resupply Subcontractor order

Once the subcontracted product\'s components have been sent to the
subcontractor, navigate to
`Purchase app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and select the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

Click the `Resupply`{.interpreted-text role="guilabel"} smart button at
the top of the screen to open the *Resupply Subcontractor* order, and
click `Validate`{.interpreted-text role="guilabel"} to confirm that the
components have been sent to the subcontractor.

Alternatively, navigate to the `Inventory`{.interpreted-text
role="menuselection"} app, click the `# To Process`{.interpreted-text
role="guilabel"} button on the
`Resupply Subcontractor`{.interpreted-text role="guilabel"} card, and
select the *Resupply Subcontractor* order. Then, click
`Validate`{.interpreted-text role="guilabel"} to confirm that the
components have been sent to the subcontractor.

### Process receipt or dropship order

Once the subcontractor has finished manufacturing the product, they
either ship it to the contracting company, or dropship it to the end
customer, depending on how the product was
`configured <manufacturing/workflows/subcontracting_resupply/product-config>`{.interpreted-text
role="ref"}.

#### Process receipt

If the subcontractor ships the finished product to the contracting
company, once it has been received, navigate to
`Purchase app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and select the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

Click the `Receive Products`{.interpreted-text role="guilabel"} button
at the top of the `PO (Purchase Order)`{.interpreted-text role="abbr"},
or the `Receipt`{.interpreted-text role="guilabel"} smart button at the
top of the page, to open the receipt. Then, click
`Validate`{.interpreted-text role="guilabel"} at the top of the receipt
to enter the product into inventory.

#### Process dropship order

If the subcontractor dropships the product, once they have sent it,
navigate to
`Purchase app --> Orders --> Purchase Orders`{.interpreted-text
role="menuselection"}, and select the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

Select the `Dropship`{.interpreted-text role="guilabel"} smart button at
the top of the page to open the dropship order, and click
`Validate`{.interpreted-text role="guilabel"} at the top of the order to
confirm that the product has been sent to the customer.

### Process delivery order

If the subcontracting workflow was started by a customer
`SO (Sales Order)`{.interpreted-text role="abbr"}, and the finished
product was **NOT** dropshipped to the customer, but rather delivered to
the contracting company, it is necessary to ship the product to the
customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the
`Sales`{.interpreted-text role="menuselection"} app, and select the
`SO (Sales Order)`{.interpreted-text role="abbr"}. Select the
`Delivery`{.interpreted-text role="guilabel"} smart button at the top of
the page to open the delivery order, and click
`Validate`{.interpreted-text role="guilabel"} on the order to confirm
that the product has been shipped to the customer.
