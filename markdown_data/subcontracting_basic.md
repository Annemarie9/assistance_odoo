# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_basic.md

Basic subcontracting
====================

In manufacturing, subcontracting is the process of a company engaging a
third-party manufacturer, or subcontractor, to manufacture products that
are then sold by the contracting company.

In basic subcontracting, the subcontractor is responsible for acquiring
the necessary components. This means that the contracting company only
has to worry about what happens to subcontracted products once they are
produced.

The workflow for purchasing a product manufactured using basic
subcontracting is similar to the one used when purchasing a
non-subcontracted product from a vendor. The main differences are the
way that subcontracted products are configured, and the fact that
subcontracted products take longer to be sent from the vendor, since
they must first be manufactured by them.

Configuration
-------------

To use subcontracting in Odoo, navigate to
`Manufacturing app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and tick the checkbox
next to the `Subcontracting`{.interpreted-text role="guilabel"} setting,
under the `Operations`{.interpreted-text role="guilabel"} heading. Then,
click `Save`{.interpreted-text role="guilabel"}.

Once the `Subcontracting`{.interpreted-text role="guilabel"} setting is
enabled, it is also necessary to properly configure the subcontracted
product, and the product\'s `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

### Configure product {#manufacturing/workflows/subcontracting_basic/product-config}

To configure a product for basic subcontracting, navigate to
`Inventory app -->
Products --> Products`{.interpreted-text role="menuselection"}, and
select a product, or create a new one by clicking
`New`{.interpreted-text role="guilabel"}.

On the product form, select the `Purchase`{.interpreted-text
role="guilabel"} tab, and add the product\'s subcontractor as a vendor
by clicking `Add a line`{.interpreted-text role="guilabel"}, selecting
the subcontractor in the `Vendor`{.interpreted-text role="guilabel"}
drop-down menu, and entering a price in the `Price`{.interpreted-text
role="guilabel"} field.

Then, click on the `Inventory`{.interpreted-text role="guilabel"} tab,
and use the `Routes`{.interpreted-text role="guilabel"} field to
configure a route that determines what happens to the finished product
once it has been manufactured by the subcontractor.

If the finished product is shipped back to the contracting company, make
sure the `Buy`{.interpreted-text role="guilabel"} route is selected. In
addition, select the `Replenish on Order (MTO)`{.interpreted-text
role="guilabel"} route to automatically create a
`PO (Purchase Order)`{.interpreted-text role="abbr"} for the product
upon confirmation of a sales order (SO), unless there is enough stock
on-hand to fulfill the `SO (Sales Order)`{.interpreted-text
role="abbr"}.

If the finished product is shipped directly to the customer by the
subcontractor, make sure that **only** the `Dropship`{.interpreted-text
role="guilabel"} route is selected.

### Configure BoM

To configure a `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
for basic subcontracting, click the
`Bill of Materials`{.interpreted-text role="guilabel"} smart button on
the product form, and select the desired
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

Finally, click on the `Miscellaneous`{.interpreted-text role="guilabel"}
tab. In the `Manuf. Lead Time`{.interpreted-text role="guilabel"} field,
enter the number of days it takes the subcontractor to manufacture the
product. This number is factored in when calculating the product\'s
expected arrival date.

::: {.note}
::: {.title}
Note
:::

When using basic subcontracting, there is no need to list components in
the `Components`{.interpreted-text role="guilabel"} tab of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, since the
components required for manufacturing, and the means by which they are
acquired, are handled by the subcontractor.
:::

Basic subcontracting workflow
-----------------------------

The basic subcontracting workflow consists of up to four steps:

1.  Create a sales order (SO) for the subcontracted product; doing so
    creates a `PO (Purchase Order)`{.interpreted-text role="abbr"} to
    purchase the product from the subcontractor.
2.  Confirm the `PO (Purchase Order)`{.interpreted-text role="abbr"}
    created in the previous step, or create a new
    `PO (Purchase Order)`{.interpreted-text role="abbr"}; doing so
    creates a receipt order or a dropship order.
3.  Process the receipt once the subcontractor has finished
    manufacturing the subcontracted product, and shipped it back to the
    contracting company, **OR** process the dropship order to ship the
    product directly to the customer.
4.  If the workflow was started by creating an
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
the *Replenish on Order (MTO)* route is enabled on the product\'s form,
**and** there is not enough stock of the product on-hand to fulfill the
`SO (Sales Order)`{.interpreted-text role="abbr"}.

If there is enough stock on-hand, confirming an
`SO (Sales Order)`{.interpreted-text role="abbr"} for the product
creates a delivery order instead, because Odoo assumes that the
`SO (Sales Order)`{.interpreted-text role="abbr"} is fulfilled using the
stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to
the end customer. In that case, a
`PO (Purchase Order)`{.interpreted-text role="abbr"} is **always**
created, even if there is enough stock on-hand.
:::

### Process PO

If a `PO (Purchase Order)`{.interpreted-text role="abbr"} was created in
the previous step, navigate to it by clicking the
`Purchase`{.interpreted-text role="guilabel"} smart button at the top of
the `SO (Sales Order)`{.interpreted-text role="abbr"}, or by going to
`Purchase app --> Orders --> Purchase
Orders`{.interpreted-text role="guilabel"}, and selecting the
`PO (Purchase Order)`{.interpreted-text role="abbr"}. Then, click
`Confirm Order`{.interpreted-text role="guilabel"} to confirm it, and
move on to the next step.

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
for a product manufactured using basic subcontracting, a receipt or
dropship order is automatically created, and can be accessed from the
corresponding `Receipt`{.interpreted-text role="guilabel"} or
`Dropship`{.interpreted-text role="guilabel"} smart button that appears
at the top of the `PO (Purchase Order)`{.interpreted-text role="abbr"}.

![PO for a basic subcontracting product, with a Receipt smart button at
the top of the
page.](subcontracting_basic/subcontractor-po.png){.align-center}

### Process receipt or dropship order

Once the subcontractor has finished manufacturing the product, they
either ship it to the contracting company, or dropship it to the end
customer, depending on how the product was
`configured <manufacturing/workflows/subcontracting_basic/product-config>`{.interpreted-text
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
product was **not** dropshipped to the customer, but rather delivered to
the contracting company, it is necessary to ship the product to the
customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the
`Sales`{.interpreted-text role="menuselection"} app, and select the
`SO (Sales Order)`{.interpreted-text role="abbr"}. Select the
`Delivery`{.interpreted-text role="guilabel"} smart button at the top of
the page to open the delivery order, and click
`Validate`{.interpreted-text role="guilabel"} on the order to confirm
that the product has been shipped.
