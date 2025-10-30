# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/repairs/repair_orders.md

Process repair orders
=====================

Sometimes, products delivered to customers can break or be damaged in
transit, and need to be returned for a refund, delivery of a replacement
product, or repairs.

In Odoo, repairs for products returned by customers can be tracked in
the *Repairs* app. Once repaired, products can be redelivered to the
customer.

The return and repair process for damaged products typically follows the
below steps:

1.  `Process return order for damaged product <repairs/repair_orders/return-order>`{.interpreted-text
    role="ref"}
2.  `Create repair order for returned product <repairs/repair_orders/repair>`{.interpreted-text
    role="ref"}
3.  `Return repaired product to customer <repairs/repair_orders/return-customer>`{.interpreted-text
    role="ref"}

Return order {#repairs/repair_orders/return-order}
------------

Returns can be processed in Odoo via *reverse transfers*, created
directly from a sales order (SO) once products have been delivered to a
customer.

To create a return, navigate to the `Sales app`{.interpreted-text
role="menuselection"}, and click into an
`SO (Sales Order)`{.interpreted-text role="abbr"} from which a product
should be returned. Then, from the `SO (Sales Order)`{.interpreted-text
role="abbr"} form, click the `Delivery`{.interpreted-text
role="guilabel"} smart button. Doing so opens the delivery order (DO)
form.

From this form, click `Return`{.interpreted-text role="guilabel"}. This
opens a `Reverse Transfer`{.interpreted-text role="guilabel"} pop-up
window.

{.align-center}

This pop-up lists the `Product`{.interpreted-text role="guilabel"}
included in the order, the `Quantity`{.interpreted-text role="guilabel"}
delivered to the customer, and the `Unit of Measure`{.interpreted-text
role="guilabel"} the product was in.

Click the value in the `Quantity`{.interpreted-text role="guilabel"}
field to change the quantity of the product to be returned, if
necessary.

Click the `🗑️ (trash)`{.interpreted-text role="guilabel"} icon at the
far-right of the product line to remove it from the return, if
necessary.

Once ready, click `Return`{.interpreted-text role="guilabel"} to confirm
the return. This creates a new receipt for the returned products.

Once the product has been returned to the warehouse, receipt of the
return can be registered in the database by clicking
`Validate`{.interpreted-text role="guilabel"} from the reverse transfer
form.

::: {.tip}
::: {.title}
Tip
:::

Once a reverse transfer for a return is validated, the value in the
`Delivered`{.interpreted-text role="guilabel"} column on the original
`SO (Sales Order)`{.interpreted-text role="abbr"} updates to reflect the
difference between the original `Quantity`{.interpreted-text
role="guilabel"} ordered, and the `Quantity`{.interpreted-text
role="guilabel"} returned by the customer.

{.align-center}
:::

Create repair order {#repairs/repair_orders/repair}
-------------------

Once products have been returned, their repairs can be tracked by
creating a repair order (RO).

To create a new `RO (Repair Order)`{.interpreted-text role="abbr"},
navigate to `Repairs app`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"}. This opens a blank
`RO (Repair Order)`{.interpreted-text role="abbr"} form.

{.align-center}

On this form, begin by selecting a `Customer`{.interpreted-text
role="guilabel"}. The customer selected should be for whom the order
will be invoiced and delivered.

In the `Product to Repair`{.interpreted-text role="guilabel"} field,
click the drop-down menu to select the product that needs repair. If
necessary, click `Search More...`{.interpreted-text role="guilabel"} to
open a `Search: Product to
Repair`{.interpreted-text role="guilabel"} pop-up window, and browse all
products in the database.

Once a `Product to Repair`{.interpreted-text role="guilabel"} is
selected, a new `Product Quantity`{.interpreted-text role="guilabel"}
field appears below it. In that field, enter the quantity (in a
[0.00]{.title-ref} format) of the product that requires repair.

To the right of that value, click the drop-down list to select the unit
of measure (UoM) for the product.

In the `Return`{.interpreted-text role="guilabel"} field, click the
drop-down menu and select the return order from which the product to be
repaired comes from.

Tick the `Under Warranty`{.interpreted-text role="guilabel"} checkbox,
if the product being repaired is covered by a warranty. If ticked, the
`Customer`{.interpreted-text role="guilabel"} is not charged for all the
parts used in the repair order.

In the `Scheduled Date`{.interpreted-text role="guilabel"} field, click
the date to reveal a calendar popover window. From this calendar, select
a date for the repair, and click `Apply`{.interpreted-text
role="guilabel"}.

{.align-center}

In the `Responsible`{.interpreted-text role="guilabel"} field, click the
drop-down menu and select the user who should be responsible for the
repair.

In the `Company`{.interpreted-text role="guilabel"} field, if in a
multi-company environment, select which company this
`RO (Repair Order)`{.interpreted-text role="abbr"} belongs to.

In the `Tags`{.interpreted-text role="guilabel"} field, click the
drop-down menu and select which tags should be applied to this
`RO (Repair Order)`{.interpreted-text role="abbr"}.

### Parts tab

Add, remove, or recycle parts in the `Parts`{.interpreted-text
role="guilabel"} tab. To do so, click `Add a line`{.interpreted-text
role="guilabel"} at the bottom of the form.

In the `Type`{.interpreted-text role="guilabel"} column, click the box
to reveal three options to choose from: `Add`{.interpreted-text
role="guilabel"} (selected by default), `Remove`{.interpreted-text
role="guilabel"}, and `Recycle`{.interpreted-text role="guilabel"}.

{.align-center}

Choosing `Add`{.interpreted-text role="guilabel"} adds this part to the
`RO (Repair Order)`{.interpreted-text role="abbr"}. Adding parts lists
components for use in the repair. If the components are used, the user
completing the repair can record they were used. If they were not used,
the user can indicate that, too, and the components can be saved for
another use.

Choosing `Remove`{.interpreted-text role="guilabel"} removes this part
from the `RO (Repair Order)`{.interpreted-text role="abbr"}. Removing
parts lists components that should be removed from the product being
repaired during the repair process. If the parts are removed, the user
completing the repair can indicate they were removed.

Choosing `Recycle`{.interpreted-text role="guilabel"} recycles this part
from the `RO (Repair Order)`{.interpreted-text role="abbr"}, designating
it for later use or to be repurposed for another use in the warehouse.

In the `Product`{.interpreted-text role="guilabel"} column, select which
product (part) should be added, removed, or recycled. In the
`Demand`{.interpreted-text role="guilabel"} column, change the quantity,
if necessary, to indicate what quantity of this part should be used in
the repair process.

In the `Done`{.interpreted-text role="guilabel"} column, change the
value (in a [0.00]{.title-ref} format) once the part has been
successfully added, removed, or recycled.

In the `Unit of Measure`{.interpreted-text role="guilabel"} column,
select the `UoM (Unit of Measure)`{.interpreted-text role="abbr"} for
the part.

Finally, in the `Used`{.interpreted-text role="guilabel"} column, tick
the checkbox once the part has been used in the repair process.

To add additional columns to the line, click the
`(optional columns drop-down)`{.interpreted-text role="guilabel"} icon,
at the far-right of the header row. Select the desired options to add to
the line.

{.align-center}

### Repair Notes and Miscellaneous tabs

Click the `Repair Notes`{.interpreted-text role="guilabel"} tab to add
internal notes about this specific `RO (Repair Order)`{.interpreted-text
role="abbr"}, and anything the user performing the repair might need to
know.

Click the blank text field to begin writing notes.

Click the `Miscellaneous`{.interpreted-text role="guilabel"} tab to see
the `Operation Type`{.interpreted-text role="guilabel"} for this repair.
By default, this is set to `YourCompany: Repairs`{.interpreted-text
role="guilabel"}, indicating this is a repair type operation.

Once all desired configurations have been made on the
`RO (Repair Order)`{.interpreted-text role="abbr"} form, click
`Confirm Repair`{.interpreted-text role="guilabel"}. This moves the
`RO (Repair Order)`{.interpreted-text role="abbr"} to the
`Confirmed`{.interpreted-text role="guilabel"} stage, and reserves the
necessary components needed for the repair.

A new `Forecasted`{.interpreted-text role="guilabel"} column appears on
the product lines under the `Parts`{.interpreted-text role="guilabel"}
tab, displaying the availability of all components needed for the
repair.

Once ready, click `Start Repair`{.interpreted-text role="guilabel"}.
This moves the `RO (Repair Order)`{.interpreted-text role="abbr"} to the
`Under Repair`{.interpreted-text role="guilabel"} stage (in the
upper-right corner). If the `RO (Repair Order)`{.interpreted-text
role="abbr"} should be canceled, click `Cancel Repair`{.interpreted-text
role="guilabel"}.

Once all products have been successfully repaired, the
`RO (Repair Order)`{.interpreted-text role="abbr"} is completed. To
register this in the database, click `End Repair`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If all parts added to the `RO (Repair Order)`{.interpreted-text
role="abbr"} were not used, clicking `End Repair`{.interpreted-text
role="guilabel"} causes an `Uncomplete Move(s)`{.interpreted-text
role="guilabel"} pop-up window to appear.

{.align-center}

The pop-up window informs the user that there is a difference between
the initial demand and the actual quantity used for the order.

If the `Used`{.interpreted-text role="guilabel"} quantity should be
changed, click `Discard`{.interpreted-text role="guilabel"} or close the
pop-up window. If the order should be confirmed, click
`Validate`{.interpreted-text role="guilabel"}.
:::

This moves the `RO (Repair Order)`{.interpreted-text role="abbr"} to the
`Repaired`{.interpreted-text role="guilabel"} stage. A
`Product Moves`{.interpreted-text role="guilabel"} smart button also
appears above the form.

Click the `Product Moves`{.interpreted-text role="guilabel"} smart
button to view the product\'s moves history during and after the repair
process.

{.align-center}

### Return product to customer {#repairs/repair_orders/return-customer}

#### Product is under warranty

Once the product has been successfully repaired, it can be returned to
the customer.

#### Product is not under warranty

If the product is not under warranty, or should the customer bear the
repair costs, click `Create Quotation`{.interpreted-text
role="guilabel"}. This opens a new `SO (Sales Order)`{.interpreted-text
role="abbr"} form, pre-populated with the parts used in the
`RO (Repair Order)`{.interpreted-text role="abbr"}, with the total cost
of the repair calculated.

{.align-center}

If this `SO (Sales Order)`{.interpreted-text role="abbr"} should be sent
to the customer, click `Confirm`{.interpreted-text role="guilabel"}, and
proceed to invoice the customer for the repair.

::: {.tip}
::: {.title}
Tip
:::

If the customer should be charged for a repair service, a service type
product can be created and added to the
`SO (Sales Order)`{.interpreted-text role="abbr"} for a repaired
product.
:::

To return the product to the customer, navigate to the
`Sales app`{.interpreted-text role="menuselection"}, and select the
original `SO (Sales Order)`{.interpreted-text role="abbr"} from which
the initial return was processed. Then, click the
`Delivery`{.interpreted-text role="guilabel"} smart button.

From the resulting list of operations, click the reverse transfer,
indicated by the `Source Document`{.interpreted-text role="guilabel"},
which should read [Return of WH/OUT/XXXXX]{.title-ref}.

This opens the return form. At the top of this form, a
`Repair Orders`{.interpreted-text role="guilabel"} smart button now
appears, linking this return to the completed
`RO (Repair Order)`{.interpreted-text role="abbr"}.

Click `Return`{.interpreted-text role="guilabel"} at the top of the
form. This opens a `Reverse Transfer`{.interpreted-text role="guilabel"}
pop-up window.

{.align-center}

This pop-up lists the `Product`{.interpreted-text role="guilabel"}
included in the order, the `Quantity`{.interpreted-text role="guilabel"}
delivered to the customer, and the `Unit of Measure`{.interpreted-text
role="guilabel"} the product was in.

Click the value in the `Quantity`{.interpreted-text role="guilabel"}
field to change the quantity of the product to be returned, if
necessary.

Click the `🗑️ (trash)`{.interpreted-text role="guilabel"} icon at the
far-right of the product line to remove it from the return, if
necessary.

Once ready, click `Return`{.interpreted-text role="guilabel"} to confirm
the return. This creates a new delivery for the returned products.

When the delivery has been processed and the product has been returned
to the customer, click `Validate`{.interpreted-text role="guilabel"} to
validate the delivery.

::: {.seealso}
`../../sales/sales/products_prices/returns`{.interpreted-text
role="doc"}
:::
