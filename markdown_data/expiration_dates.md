# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/product_tracking/expiration_dates.md

Expiration dates
================

::: {#inventory/product_management/product_tracking/expiration_dates}
In Odoo, *expiration dates* can be used to manage and track the
lifecycles of perishable products, from purchase to sale. Using
expiration dates reduces product loss due to unexpected expiry, and
helps to avoid sending expired products to customers.
:::

In Odoo, only products that are tracked using *lots* and *serial
numbers* can be assigned expiration information. Once a lot or serial
number has been assigned, an expiration date can be set. This is
especially helpful for companies (such as food manufacturers) that
consistently, or exclusively, buy and sell perishable products.

::: {.seealso}
\- `../product_tracking/lots`{.interpreted-text role="doc"} -
`../product_tracking/serial_numbers`{.interpreted-text role="doc"}
:::

Enable expiration dates
-----------------------

To enable the use of *expiration dates*, go to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and scroll down to
the `Traceability`{.interpreted-text role="guilabel"} section. Then,
click the checkbox to enable the
`Lots & Serial Numbers`{.interpreted-text role="guilabel"} feature.

Once that feature is activated, a new option will appear to enable
`Expiration Dates`{.interpreted-text role="guilabel"}. Click that
checkbox to enable the feature, and be sure to `Save`{.interpreted-text
role="guilabel"} changes.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Once the `Lots & Serial Numbers`{.interpreted-text role="guilabel"}
feature is activated, additional features appear to
`Display Lots & Serial Numbers on Delivery Slips`{.interpreted-text
role="guilabel"}; to `Display Lots & Serial
Numbers on Invoices`{.interpreted-text role="guilabel"}; and to
`Display Expiration Dates on Delivery Slips`{.interpreted-text
role="guilabel"}. Activating these features helps with end-to-end
traceability, making it easier to manage product recalls, identify
\"bad\" batches of products, and more.
:::

Configure expiration dates on products
--------------------------------------

Once the `Lots & Serial Numbers`{.interpreted-text role="guilabel"} and
`Expiration Dates`{.interpreted-text role="guilabel"} features have been
enabled in the settings of the *Inventory* app, expiration information
can be configured on individual products.

To do so, go to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product to edit. Selecting a product
reveals the product form for that particular item. Once on the product
form, click `Edit`{.interpreted-text role="guilabel"} in the upper-left
corner to make changes.

::: {.important}
::: {.title}
Important
:::

To be tracked using lots or serial numbers, or to configure expiration
information, products *must* have their `Product Type`{.interpreted-text
role="guilabel"} set as `Storable Product`{.interpreted-text
role="guilabel"} under the `General Information`{.interpreted-text
role="guilabel"} tab.
:::

Then, click the `Inventory`{.interpreted-text role="guilabel"} tab, and
scroll down to the `Traceability`{.interpreted-text role="guilabel"}
section. From here, make sure that either
`By Unique Serial Number`{.interpreted-text role="guilabel"} or
`By Lots`{.interpreted-text role="guilabel"} is checked.

Once it is, a new `Expiration Date`{.interpreted-text role="guilabel"}
checkbox appears that must also be clicked. When both are enabled, a new
`Dates`{.interpreted-text role="guilabel"} field appears to the right.

::: {.note}
::: {.title}
Note
:::

If a product has stock on-hand prior to activating tracking by lots or
serial numbers, an inventory adjustment might need to be performed in
order to assign lot numbers to the existing stock.
:::

::: {.tip}
::: {.title}
Tip
:::

For processing large quantities of products on receipts or deliveries,
it is recommended to track using lots, so multiple products can be
traced back to the same lot, if any issues arise.
:::

{.align-center}

Under the `Dates`{.interpreted-text role="guilabel"} field, there are
four categories of expiration information to configure for the product:

-   `Expiration Time`{.interpreted-text role="guilabel"}: the number of
    days after receiving products (either from a vendor or in stock
    after production) in which goods may become dangerous and should not
    be used or consumed.
-   `Best Before Time`{.interpreted-text role="guilabel"}: the number of
    days before the expiration date in which the goods start
    deteriorating, **without** necessarily being dangerous yet.
-   `Removal Time`{.interpreted-text role="guilabel"}: the number of
    days before the expiration date in which the goods should be removed
    from stock.
-   `Alert Time`{.interpreted-text role="guilabel"}: the number of days
    before the expiration date in which an alert should be raised on
    goods in a particular lot or containing a particular serial number.

::: {.note}
::: {.title}
Note
:::

The values entered into these fields automatically compute the
expiration date for goods entered into stock, whether purchased from a
vendor or manufactured in-house.
:::

Once all the expiration information has been configured, click
`Save`{.interpreted-text role="guilabel"} to save all changes.

::: {.tip}
::: {.title}
Tip
:::

If the `Dates`{.interpreted-text role="guilabel"} field is not populated
with any values for expiration information, dates (and lots) can be
manually assigned upon receipts and deliveries in and out of the
warehouse. Even when assigned, they can still be overwritten and changed
manually if needed, as well.
:::

Set expiration dates on receipts with lots & serial numbers
-----------------------------------------------------------

Generating expiration dates for **incoming** goods can be done directly
from the purchase order. To create a purchase order, go to the
`Purchase`{.interpreted-text role="menuselection"} app and click
`Create`{.interpreted-text role="guilabel"} to create a new request for
quotation (RFQ).

Then, fill out the information by adding a `Vendor`{.interpreted-text
role="guilabel"}, and add products to the `Product`{.interpreted-text
role="guilabel"} lines by clicking `Add a product`{.interpreted-text
role="guilabel"}.

Choose the desired quantity to order by changing the number in the
`Quantity`{.interpreted-text role="guilabel"} column, and click
`Confirm Order`{.interpreted-text role="guilabel"}. This converts the
`RFQ (request for quotation)`{.interpreted-text role="abbr"} into a
purchase order.

Click the `Receipt`{.interpreted-text role="guilabel"} smart button at
the top of the purchase order to be taken to the warehouse receipt form.

::: {.note}
::: {.title}
Note
:::

Clicking `Validate`{.interpreted-text role="guilabel"} before assigning
a serial number to the ordered product quantities causes a
`User Error`{.interpreted-text role="guilabel"} popup to appear. The
popup requires entry of a lot or serial number for the ordered products.
The `RFQ (request for quotation)`{.interpreted-text role="abbr"} cannot
be validated without an assigned lot or serial number.

{.align-center}
:::

From here, click the `Additional Options`{.interpreted-text
role="guilabel"} menu (hamburger) icon located on the far-right of the
product line. When clicked, a `Detailed Operations`{.interpreted-text
role="guilabel"} pop-up will appear.

In this pop-up, click `Add a line`{.interpreted-text role="guilabel"},
and assign a lot or serial number under the
`Lot/Serial Number Name`{.interpreted-text role="guilabel"} field.

An expiration date automatically populates, based on the configuration
on the product form (if previously configured).

::: {.tip}
::: {.title}
Tip
:::

If the `Dates`{.interpreted-text role="guilabel"} field on the product
form has not been configured, this date can be manually entered.
:::

After the expiration date has been established, mark the
`Done`{.interpreted-text role="guilabel"} quantities, and click
`Confirm`{.interpreted-text role="guilabel"} to close the pop-up.
Finally, click `Validate`{.interpreted-text role="guilabel"}.

{.align-center}

A `Traceability`{.interpreted-text role="guilabel"} smart button will
appear upon validating the receipt. Click the
`Traceability`{.interpreted-text role="guilabel"} smart button to see
the updated `Traceability Report`{.interpreted-text role="guilabel"},
which includes: a `Reference`{.interpreted-text role="guilabel"}
document; the `Product`{.interpreted-text role="guilabel"} being traced;
the `Lot/Serial #`{.interpreted-text role="guilabel"}; and more.

Set expiration dates on manufactured products
---------------------------------------------

Expiration dates can also be generated for products manufactured
in-house. To assign expiration dates to manufactured products, a
manufacturing order (MO) needs to be completed.

To create a `MO (manufacturing order)`{.interpreted-text role="abbr"},
go to `Manufacturing app --> Operations
--> Manufacturing Orders`{.interpreted-text role="menuselection"}, and
click `Create`{.interpreted-text role="guilabel"}. Choose a product to
manufacture from the `Product`{.interpreted-text role="guilabel"} field
drop-down menu, then select the `Quantity`{.interpreted-text
role="guilabel"} to produce.

{.align-center}

::: {.note}
::: {.title}
Note
:::

To manufacture a product, there must be materials to consume in the
lines in the `Product`{.interpreted-text role="guilabel"} column. This
can be achieved either by creating a `Bill of
Material`{.interpreted-text role="guilabel"} for the
`Product`{.interpreted-text role="guilabel"}, or manually adding
materials to consume by clicking `Add a line`{.interpreted-text
role="guilabel"}.
:::

Once ready, click `Confirm`{.interpreted-text role="guilabel"}.

Next to `Lot/Serial Number`{.interpreted-text role="guilabel"}, either
select an existing lot number from the drop-down menu, or click the
green `+`{.interpreted-text role="guilabel"} sign to automatically
assign a new lot number.

Then, select a number of units for the `Quantity`{.interpreted-text
role="guilabel"} field, and click `Mark as
Done`{.interpreted-text role="guilabel"}.

Click on the `External Link`{.interpreted-text role="guilabel"} icon in
the assigned `Lot/Serial Number`{.interpreted-text role="guilabel"}
field. A pop-up appears, revealing a detail form for that specific
number.

On that pop-up, under the `Dates`{.interpreted-text role="guilabel"}
tab, all expiration information that was previously configured for the
product is displayed. That same information is also available on the
detail form for that specific product, or by going to
`Inventory app --> Products --> Lots/Serial
Numbers`{.interpreted-text role="menuselection"}.

{.align-center}

Sell products with expiration dates
-----------------------------------

Selling perishable products with expiration dates is done the same as
any other type of product. The first step in selling perishable products
is to create a sales order.

To do that, go to `Sales app --> Create`{.interpreted-text
role="menuselection"} to create a new quotation, and fill out the
information on the sales order form.

Add a `Customer`{.interpreted-text role="guilabel"}, click
`Add a product`{.interpreted-text role="guilabel"} to add the desired
products to the `Product`{.interpreted-text role="guilabel"} lines, and
set a `Quantity`{.interpreted-text role="guilabel"} for the products.

Then, click the `Other Info`{.interpreted-text role="guilabel"} tab.
Under the `Delivery`{.interpreted-text role="guilabel"} section, change
the `Delivery Date`{.interpreted-text role="guilabel"} to a date after
the expected date, and click the `green
checkmark`{.interpreted-text role="guilabel"} icon to confirm the date.
Finally, click `Confirm`{.interpreted-text role="guilabel"} to confirm
the sales order.

Next, click the `Delivery`{.interpreted-text role="guilabel"} smart
button at the top of the sales order to see the warehouse receipt form.

On the warehouse receipt form, click `Validate`{.interpreted-text
role="guilabel"}, and then `Apply`{.interpreted-text role="guilabel"} in
the accompanying pop-up window, to automatically process all
`Done`{.interpreted-text role="guilabel"} quantities, and deliver the
products to the customer.

If the products are delivered before the `Alert Date`{.interpreted-text
role="guilabel"} set on the product form, then no alerts will be
created.

::: {.important}
::: {.title}
Important
:::

To sell perishable products with expiration dates, the
`Removal Strategy`{.interpreted-text role="guilabel"} for the
`Location`{.interpreted-text role="guilabel"} the products are stored in
must be set to `FEFO (First Expiry, First
Out)`{.interpreted-text role="abbr"}. If there is not enough stock of
perishable products in one lot, Odoo will automatically take the
remaining quantity required from a second lot with the next-soonest
expiration date. Removal strategies can also be set on
`Product Categories`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
`../../shipping_receiving/removal_strategies`{.interpreted-text
role="doc"}
:::

View expiration dates for lots & serial numbers
-----------------------------------------------

To view (and/or group) all products with expiration dates by lot number,
go to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}.

Once there, remove any default search filters from the
`Search...`{.interpreted-text role="guilabel"} bar. Then, click
`Group By`{.interpreted-text role="guilabel"}, choose
`Add Custom Group`{.interpreted-text role="guilabel"}, and select the
`Expiration
Date`{.interpreted-text role="guilabel"} parameter from the drop-down
menu. Finally, click `Apply`{.interpreted-text role="guilabel"} to apply
the filter.

Doing so breaks down all perishable products, their expiration dates,
and the assigned lot number.

{.align-center}

### Expiration alerts {#inventory/product_management/expiration-alerts}

To see expiration alerts, go to
`Inventory app --> Products --> Lots/Serial Numbers`{.interpreted-text
role="menuselection"}.

Then, click into a `Lot/Serial Number`{.interpreted-text
role="guilabel"} with perishable products. Doing so reveals the serial
number detail form. On the serial number detail form, click the
`Dates`{.interpreted-text role="guilabel"} tab to see all expiration
information related to the products.

To edit the form, click `Edit`{.interpreted-text role="guilabel"} in the
upper-left corner of the form, then change the
`Expiration Date`{.interpreted-text role="guilabel"} to today\'s date
(or earlier), and click `Save`{.interpreted-text role="guilabel"} to
save changes.

After saving, the lot number form displays a red
`Expiration Alert`{.interpreted-text role="guilabel"} at the top of the
form to indicate that the products in this lot are either expired or
expiring soon. From here, click back to the
`Lots/Serial Numbers`{.interpreted-text role="guilabel"} page (via the
breadcrumbs).

To see the new expiration alert, or any expiration alerts for products
that are expired (or will expire soon), remove all of the search filters
from the `Search...`{.interpreted-text role="guilabel"} bar on the
`Lots/Serial Numbers`{.interpreted-text role="guilabel"} dashboard.

Then, click `Filters`{.interpreted-text role="guilabel"}, and choose
`Expiration Alerts`{.interpreted-text role="guilabel"}.

{.align-center}

### Expiration notifications

Users can be notified when the expiration date for a product has passed.
This can help keep specific employees up to date on the status of items
under their purview.

To configure a notification, navigate to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}. Select a product configured with lot/serial
numbers and expiration date tracking. Navigate to the
`Inventory`{.interpreted-text role="guilabel"} tab. Under the
`Logistics`{.interpreted-text role="guilabel"} section, select a user in
the `Responsible`{.interpreted-text role="guilabel"} field.

When the expiation date passes for a lot/serial number for this product,
a notification is sent to the user in this field.

::: {.note}
::: {.title}
Note
:::

Once the expiration date is due, expiration alerts are created on the
form view of the lot/serial number of the product.

To customize these alerts, turn on
`developer mode <developer-mode>`{.interpreted-text role="ref"}, go to
`Settings app --> Technical --> Activity Types`{.interpreted-text
role="menuselection"}, and select the `Alert
Date Reached`{.interpreted-text role="guilabel"} alert.

The `Default User`{.interpreted-text role="guilabel"} assigned will be
notified once the expiration date is reached. If no default user is
configured, the activity will be assigned to the
`Responsible`{.interpreted-text role="guilabel"} user selected on the
product\'s `Inventory`{.interpreted-text role="guilabel"} tab.
:::
