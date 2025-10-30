# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.md

Lead times
==========

Accurately forecasting delivery dates is vital for fulfilling customer
expectations. In Odoo, the **Inventory** app allows for comprehensive
lead time configuration, allowing coordination and planning of
manufacturing orders, deliveries, and receipts.

Lead time types
---------------

Different lead times for different operations can impact various stages
of the order fulfillment process. Here\'s a summary of the types of lead
times in Odoo:



-   `Customer lead time <inventory/warehouses_storage/customer-lt>`{.interpreted-text
    role="ref"}: default time frame for fulfilling customer orders. The
    customer lead time is the number of days from the date the sales
    order (SO) is confirmed to the date the products are shipped from
    the warehouse. This is also known as *delivery lead time*.
-   `Sales security lead time <inventory/warehouses_storage/sales-security-lt>`{.interpreted-text
    role="ref"}: moves the *scheduled delivery date* forward by a
    specified number of days. This serves as a buffer to allow ample
    time to prepare the outgoing shipment earlier, considering the
    possibility of delays in the fulfillment process.
-   `Purchase lead time <inventory/warehouses_storage/purchase-lt>`{.interpreted-text
    role="ref"}: number of days from the confirmation of a purchase
    order (PO) to the receipt of products. It provides insight on the
    time it takes for products to arrive at the warehouse, facilitating
    effective scheduling and planning of supplier deliveries.
-   `Purchase security lead time <inventory/warehouses_storage/purchase-security-lt>`{.interpreted-text
    role="ref"}: advances the order deadline on a
    `PO (Purchase Order)`{.interpreted-text role="abbr"} by a specified
    number of days. This proactive approach of placing orders earlier
    mitigates the risk of vendor or shipping delays. Thus, for products
    that are set to replenish to order, the need appears on the
    *Replenishment report* earlier, according to the specified number of
    days.
-   `Days to Purchase <inventory/warehouses_storage/days-to-purchase>`{.interpreted-text
    role="ref"}: days needed for the vendor to receive a request for
    quotation (RFQ) and confirm it. It advances the deadline to schedule
    a `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} by a
    specified number of days.
-   `Manufacturing lead time <inventory/warehouses_storage/manuf-lt>`{.interpreted-text
    role="ref"}: number of days needed to complete a manufacturing order
    (MO) from the date of confirmation. This lead time includes weekends
    (non-working hours in Odoo), and is used to forecast an approximate
    production date for a finished good.
-   `Days to prepare manufacturing order
    <inventory/warehouses_storage/prepare-manufacturing-order>`{.interpreted-text
    role="ref"}: number of days needed to replenish components, or
    manufacture sub-assemblies of the product. Either set one directly
    on the bill of materials (BoM), or click *Compute* to sum up
    purchase and manufacturing lead times of components in the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.
-   `Manufacturing security lead time <inventory/warehouses_storage/manuf-security-lt>`{.interpreted-text
    role="ref"}: moves the scheduled date of the
    `MO (Manufacturing Order)`{.interpreted-text role="abbr"} forward by
    a specified number of days. When used in conjunction with
    `replenish to order <inventory/management/products/strategies>`{.interpreted-text
    role="ref"}, the security lead time makes the need appear earlier on
    the replenishment report.

Sales lead times {#inventory/warehouses_storage/customer-lt}
----------------

Customer lead times and sales security lead times can be configured to
automatically compute an *expected delivery date* on a
`SO (Sales Order)`{.interpreted-text role="abbr"}. The expected delivery
date ensures a realistic *delivery dates* setting for shipments from the
warehouse.

Odoo issues a warning message if the set delivery date is earlier than
the expected date, as it may not be feasible to fulfill the order by
that time, which would impact other warehouse operations.

::: {.example}
A `SO (Sales Order)`{.interpreted-text role="abbr"} containing a
[Coconut-scented candle]{.title-ref} is confirmed on July 11th. The
product has a customer lead time of 14 days, and the business uses a
sales security lead time of 1 day. Based on the lead time inputs, Odoo
suggests a delivery date in 15 days, on July 26th.


:::

The following sections demonstrate how to automatically compute expected
delivery dates.

### Customer lead time

Set the customer lead time on each product form, by navigating to the
products page. To do so, go to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"}. From there, select the desired product, and
switch to the `Inventory`{.interpreted-text role="guilabel"} tab. Then,
under the `Customer Lead Time`{.interpreted-text role="guilabel"} field,
fill in the number of calendar days required to fulfill the delivery
order from start to finish.

::: {.example}
Set a 14-day customer lead time for the [Coconut-scented
candle]{.title-ref} by navigating to its product form. Then, in the
`Inventory`{.interpreted-text role="guilabel"} tab, type
[14.00]{.title-ref} days into the `Customer Lead
Time`{.interpreted-text role="guilabel"} field.


:::

### Sales security lead time {#inventory/warehouses_storage/sales-security-lt}

*Sales security lead time* is set globally for the business in
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

On the configuration page, under the
`Advanced Scheduling`{.interpreted-text role="guilabel"} heading, locate
the box for `Security Lead Time for Sales`{.interpreted-text
role="guilabel"}, and click the checkbox to enable the feature.

Next, enter the desired number of calendar days. This security lead time
is a buffer notifying the team to prepare for outgoing shipments earlier
than the scheduled date.

::: {.example}
Setting the `Security Lead Time for Sales`{.interpreted-text
role="guilabel"} to [1.00]{.title-ref} day, pushes the
`Scheduled Date`{.interpreted-text role="guilabel"} of a delivery order
(DO) forward by one day. In that case, if a product is initially
scheduled for delivery on April 6th, but with a one-day security lead
time, the new scheduled date for the delivery order would be April 5th.


:::

### Deliver several products

For orders that include multiple products with different lead times, the
lead times can be configured directly from the quotation itself. On a
quotation, click the `Other Info`{.interpreted-text role="guilabel"}
tab, and set the `Shipping Policy`{.interpreted-text role="guilabel"}
to:

1.  `As soon as possible`{.interpreted-text role="guilabel"} to deliver
    products as soon as they are ready. The
    `Scheduled Date`{.interpreted-text role="guilabel"} of the
    `DO (Delivery Order)`{.interpreted-text role="abbr"} is determined
    by adding today\'s date to the shortest lead time among the products
    in the order.
2.  `When all products are ready`{.interpreted-text role="guilabel"} to
    wait to fulfill the entire order at once. The
    `Scheduled Date`{.interpreted-text role="guilabel"} of the
    `DO (Delivery Order)`{.interpreted-text role="abbr"} is determined
    by adding today\'s date to the longest lead time among the products
    in the order.



::: {.example}
In a quotation containing 2 products, [Yoga mat]{.title-ref} and
[Resistance band,]{.title-ref} the products have a lead time of 8 days
and 5 days, respectively. Today\'s date is April 2nd.

When the `Shipping Policy`{.interpreted-text role="guilabel"} is set to
`As soon as possible`{.interpreted-text role="guilabel"}, the scheduled
delivery date is 5 days from today: April 7th. On the other hand,
selecting `When all
products are ready`{.interpreted-text role="guilabel"} configures the
scheduled date to be 8 days from today: April 10th.
:::

Purchase lead times {#inventory/warehouses_storage/purchase-lt}
-------------------

Automatically determining the dates on which to place orders from
suppliers can help simplify the procurement process.

Odoo calculates the supplier shipment *receipt date*, and
`PO (Purchase Order)`{.interpreted-text role="abbr"} deadline, based on
the required date the product is needed in the warehouse. By working
backwards from the receipt date, vendor lead times and purchase security
lead times are taken into account, in order to determine the
`PO (Purchase Order)`{.interpreted-text role="abbr"} deadline.

This deadline is the date by which the order should be confirmed, in
order to ensure timely arrival by the expected receipt date.



::: {.seealso}
`PO scheduling with reordering rules <reordering_rules>`{.interpreted-text
role="doc"}
:::

### Vendor lead time

To set a vendor lead time for orders arriving in the warehouse from a
vendor location, begin by navigating to a product form through
`Purchase app --> Products --> Products`{.interpreted-text
role="menuselection"}.

Next, select the desired product, and switch to the
`Purchase`{.interpreted-text role="guilabel"} tab. In the editable
vendor pricelist, click the `Add a line`{.interpreted-text
role="guilabel"} button to add vendor details, such as the
`Vendor`{.interpreted-text role="guilabel"} name,
`Price`{.interpreted-text role="guilabel"} offered for the product, and
lastly, the `Delivery Lead Time`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Multiple vendors and lead times can be added to the vendor pricelist.
The default vendor and lead time selected will be the entry at the top
of the list.
:::

::: {.example}
On the vendor pricelist of the product form, the
`Delivery Lead Time`{.interpreted-text role="guilabel"} for the selected
vendor is set to [10 days.]{.title-ref}


:::

By setting the vendor lead time, the expected arrival date of the item
is automatically determined as the date of the
`PO (Purchase Order)`{.interpreted-text role="abbr"} confirmation, plus
the vendor lead time. This ensures that warehouse employees are
notified, if the products do **not** arrive within the expected
timeframe.

::: {.example}
On a `PO (Purchase Order)`{.interpreted-text role="abbr"} confirmed on
July 11th, for a product configured with a 10-day vendor lead time, Odoo
automatically sets the `Receipt Date`{.interpreted-text role="guilabel"}
to July 21st. The receipt date also appears as the
`Scheduled Date`{.interpreted-text role="guilabel"} on the warehouse
receipt form, accessible from the `Receipt`{.interpreted-text
role="guilabel"} smart button, located on the
`PO (Purchase Order)`{.interpreted-text role="guilabel"}.




:::

### Purchase security lead time {#inventory/warehouses_storage/purchase-security-lt}

*Purchase security lead time* is set globally for the business in
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

On the `Settings`{.interpreted-text role="guilabel"} page, under the
`Advanced Scheduling`{.interpreted-text role="guilabel"} heading, tick
the checkbox for `Security Lead Time for Purchase`{.interpreted-text
role="guilabel"}.

Next, enter the desired number of calendar days. By configuring the
security lead time, a buffer is set to account for potential delays in
supplier deliveries. Then, click `Save`{.interpreted-text
role="guilabel"}.

::: {.example}
Setting the `Security Lead Time for Purchase`{.interpreted-text
role="guilabel"} to [2.00]{.title-ref} days, pushes the
`Scheduled Date`{.interpreted-text role="guilabel"} of receipt back by
two days. In that case, if a product is initially scheduled to arrive on
April 6th, with a two-day security lead time, the new scheduled date for
the receipt would be April 8th.


:::

### Days to purchase lead time {#inventory/warehouses_storage/days-to-purchase}

To set it up, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Advanced Scheduling`{.interpreted-text
role="guilabel"} section, in the `Days to Purchase`{.interpreted-text
role="guilabel"} field, specify the number of days required for the
vendor to confirm a `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"} after receiving it from the company.

Manufacturing lead times {#inventory/warehouses_storage/manuf-lt}
------------------------

Lead times can help simplify the procurement process for consumable
materials and components used in manufactured products with bills of
materials (BoMs).

The `MO (Manufacturing Order)`{.interpreted-text role="abbr"} deadline,
which is the deadline to begin the manufacturing process to complete the
product by the scheduled delivery date, can be determined by configuring
the manufacturing lead times and manufacturing security lead times.



### Manufacturing lead time

Manufacturing lead times for products are configured from a product\'s
bill of materials (BoM) form.

To add a lead time to a `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, navigate to `Manufacturing app --> Products --> Bills
of Materials`{.interpreted-text role="menuselection"}, and select the
desired `BoM (Bill of Materials)`{.interpreted-text role="abbr"} to
edit.

On the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} form,
click the `Miscellaneous`{.interpreted-text role="guilabel"} tab. Change
the value (in days) in the `Manuf. Lead Time`{.interpreted-text
role="guilabel"} field to specify the calendar days needed to
manufacture the product.



::: {.note}
::: {.title}
Note
:::

If the selected `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
is a multi-level `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, the manufacturing lead times of the components are added.

If the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} product
is subcontracted, the `Manuf. Lead Time`{.interpreted-text
role="guilabel"} can be used to determine the date at which components
should be sent to the subcontractor.
:::

Establish a `MO (Manufacturing Order)`{.interpreted-text role="abbr"}
deadline, based on the *expected delivery date*, indicated in the
`Scheduled Date`{.interpreted-text role="guilabel"} field of the
`DO (Delivery Order)`{.interpreted-text role="abbr"}.

The `MO (Manufacturing Order)`{.interpreted-text role="abbr"} deadline,
which is the `Scheduled Date`{.interpreted-text role="guilabel"} field
on the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}, is
calculated as the *expected delivery date* subtracted by the
manufacturing lead time.

This ensures the manufacturing process begins on time, in order to meet
the delivery date.

However, it is important to note that lead times are based on calendar
days. Lead times do **not** consider weekends, holidays, or *work center
capacity* (`the number of operations that can be
performed at the work center simultaneously`{.interpreted-text
role="dfn"}).

::: {.seealso}
\-
`Manufacturing planning <../../../manufacturing/workflows/use_mps>`{.interpreted-text
role="doc"} -
`Schedule MOs with reordering rules <reordering_rules>`{.interpreted-text
role="doc"}
:::

::: {.example}
A product\'s scheduled shipment date on the
`DO (Delivery Order)`{.interpreted-text role="abbr"} is August 15th. The
product requires 14 days to manufacture. So, the latest date to start
the `MO
(Manufacturing Order)`{.interpreted-text role="abbr"} to meet the
commitment date is August 1st.
:::

### Days to prepare manufacturing order {#inventory/warehouses_storage/prepare-manufacturing-order}

Configure the days required to gather components to manufacture a
product by going to its `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}. To do that, go to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}, and select the desired
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

In the `Miscellaneous`{.interpreted-text role="guilabel"} tab of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, specify the
calendar days needed to obtain components of the product in the
`Days to prepare Manufacturing Order`{.interpreted-text role="guilabel"}
field. Doing so creates `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"} in advance, and ensures there is enough time to either
replenish components, or manufacture semi-finished products.

::: {.tip}
::: {.title}
Tip
:::

Clicking `Compute`{.interpreted-text role="guilabel"}, located next to
the `Days to prepare Manufacturing Order`{.interpreted-text
role="guilabel"} field, calculates the longest lead time among all the
components listed on the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

*Purchase security lead times* that impact this specific
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} are also added
to this value.
:::

::: {.example}
A `BoM (Bill of Materials)`{.interpreted-text role="abbr"} has two
components, one has a manufacturing lead time of two days, and the other
has a purchase lead time of four days. The
`Days to prepare Manufacturing Order`{.interpreted-text role="guilabel"}
is four days.
:::

### Manufacturing security lead time {#inventory/warehouses_storage/manuf-security-lt}

*Manufacturing security lead time* is set globally for the business in
`Manufacturing
app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Planning`{.interpreted-text
role="guilabel"} heading, tick the checkbox for
`Security Lead Time`{.interpreted-text role="guilabel"}.

Next, enter the desired number of calendar days. By configuring the
security lead time, a buffer is set to account for potential delays in
the manufacturing process. Then, click `Save`{.interpreted-text
role="guilabel"}.



::: {.example}
A product has a scheduled shipment date on the
`DO (Delivery Order)`{.interpreted-text role="abbr"} set for August
15th. The manufacturing lead time is 7 days, and manufacturing security
lead time is 3 days. So, the `Scheduled Date`{.interpreted-text
role="guilabel"} on the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} reflects the latest date to begin the manufacturing order.
In this example, the planned date on the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} is August 5th.
:::

Global example
--------------

See the following example to understand how all the lead times work
together to ensure timely order fulfillment:

-   **Sales security lead time**: 1 day
-   **Manufacturing security lead time**: 2 days
-   **Manufacturing lead time**: 3 days
-   **Purchase security lead time**: 1 day
-   **Vendor lead time**: 4 days

The customer places an order for a manufactured product on September
1st, and the scheduled delivery date from the warehouse is on September
20th. Odoo uses lead times and automated reordering rules to schedule
the necessary operations, based on the outgoing shipment delivery date,
September 20th:



-   **September 1st**: Sales order created, confirmed by salesperson.
-   **September 9th**: Deadline to order components to ensure they
    arrive in time when manufacturing begins (4-day supplier lead time).
-   **September 13th**: Scheduled date of receipt for components.
    Initially, it was set to 9/14, but the 1-day purchase security lead
    time pushed the date earlier by 1 day.
-   **September 14th**: Deadline to begin manufacturing. Calculated by
    subtracting the manufacturing lead time of 3 days, and the
    manufacturing security lead time of 2 days, from the expected
    delivery date of September 19th.
-   **September 19th**: `Scheduled Date`{.interpreted-text
    role="guilabel"} on the delivery order form indicates the updated
    expected delivery date, which was originally set as September 20th.
    But the sales security lead time pushed the date forward by a day.

Odoo\'s replenishment planning maps a business\' order fulfillment
process, setting pre-determined deadlines and raw material order dates,
including buffer days for potential delays. This ensures products are
delivered on time.
