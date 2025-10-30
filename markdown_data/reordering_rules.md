# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/reordering_rules.md

Reordering rules
================

*Reordering rules* are used to keep forecasted stock levels above a
certain threshold without exceeding a specified upper limit. This is
accomplished by specifying a minimum quantity that stock should not fall
below and a maximum quantity that stock should not exceed.

Reordering rules can be configured for each product based on the route
used to replenish it. If a product uses the *Buy* route, then a *request
for quotation* (RFQ) is created when the reordering rule is triggered.
If a product uses the *Manufacture* route, then a *manufacturing order*
(MO) is created instead. This is the case regardless of the selected
replenishment route.

::: {.seealso}
\- [Odoo Tutorials: Automatic Reordering
Rules](https://www.youtube.com/watch?v=XEJZrCjoXaU) - [Odoo Tutorials:
Manual Reordering Rules](https://www.youtube.com/watch?v=deIREJ1FFj4)
:::

To set up reordering rules for the first time, refer to:

-   `Reordering rules setup <inventory/warehouses_storage/configure-rr>`{.interpreted-text
    role="ref"}
-   `Trigger <inventory/product_management/trigger>`{.interpreted-text
    role="ref"}
-   `Preferred route <inventory/warehouses_storage/route>`{.interpreted-text
    role="ref"}

To understand and optimize replenishment using advanced features, see:

-   `Just-in-time logic <inventory/warehouses_storage/just-in-time>`{.interpreted-text
    role="ref"}
-   `Visibility days <inventory/product_management/visibility-days>`{.interpreted-text
    role="ref"}

Reordering rules setup {#inventory/warehouses_storage/configure-rr}
----------------------

To configure automatic and manual reordering rules, complete the
following:

1.  `Product type configuration <inventory/warehouses_storage/set-product-type>`{.interpreted-text
    role="ref"}
2.  `Create rule <inventory/warehouses_storage/rr-fields>`{.interpreted-text
    role="ref"}

### Product type configuration {#inventory/warehouses_storage/set-product-type}

A product must be configured correctly to use reordering rules. Begin by
navigating to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, then select an existing product, or create a new
one by clicking `New`{.interpreted-text role="guilabel"}.

On the product form, under the `General Information`{.interpreted-text
role="guilabel"} tab, set the `Product Type`{.interpreted-text
role="guilabel"} to `Storable Product`{.interpreted-text
role="guilabel"}. This is necessary because Odoo only tracks stock
quantities for storable products, and quantities are needed to trigger
reordering rules.



Next, click the `Inventory`{.interpreted-text role="guilabel"} tab and
select one or more routes from the `Routes`{.interpreted-text
role="guilabel"} section. Doing so tells Odoo which route to use to
replenish the product.



If the product is reordered using the `Buy`{.interpreted-text
role="guilabel"} route, confirm that the `Can be
Purchased`{.interpreted-text role="guilabel"} checkbox is enabled under
the product name. This makes the `Purchase`{.interpreted-text
role="guilabel"} tab appear. Click on the `Purchase`{.interpreted-text
role="guilabel"} tab, and specify at least one vendor, and the price
that they sell the product for, so that Odoo knows which company the
product should be purchased from.



If the product is replenished using the `Manufacture`{.interpreted-text
role="guilabel"} route, it needs to have at least one *bill of
materials* (BoM) associated with it. This is necessary because Odoo only
creates manufacturing orders for products with a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

If a `BoM (Bill of Materials)`{.interpreted-text role="abbr"} does not
already exist for the product, select the
`Bill of Materials`{.interpreted-text role="guilabel"} smart button at
the top of the product form, then click `New`{.interpreted-text
role="guilabel"} to configure a new
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.



### Create new reordering rules {#inventory/warehouses_storage/rr-fields}

To create a new reordering rule, navigate to
`Inventory app --> Operations --> Replenishment`{.interpreted-text
role="menuselection"}, then click `New`{.interpreted-text
role="guilabel"}, and fill out the following fields for the new
reordering rule line item:

-   `Product`{.interpreted-text role="guilabel"}: The product that
    requires replenishment.
-   `Location`{.interpreted-text role="guilabel"}: The specific location
    where the product is stored.
-   `Min Quantity`{.interpreted-text role="guilabel"}: The minimum
    amount of product that should be available. When inventory levels
    goes below this number, the replenishment is triggered.
-   `Max Quantity`{.interpreted-text role="guilabel"}: The amount of
    product that should be available after replenishing the product.
-   `Multiple Quantity`{.interpreted-text role="guilabel"}: If the
    product should be ordered in specific quantities, enter the number
    that should be ordered. For example, if the
    `Multiple Quantity`{.interpreted-text role="guilabel"} is set to
    [5]{.title-ref}, and only 3 are needed, 5 products are replenished.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Reordering rules can also be created from the
`Reordering Rules`{.interpreted-text role="guilabel"} smart button on
the product form.
:::

::: {.note}
::: {.title}
Note
:::

To learn how the `On Hand`{.interpreted-text role="guilabel"},
`Forecast`{.interpreted-text role="guilabel"}, and
`To Order`{.interpreted-text role="guilabel"} fields are calculated
using on-hand quantities and future demand, see the `Just-in-time logic
<inventory/warehouses_storage/just-in-time>`{.interpreted-text
role="ref"} section.
:::

For advanced usage of reordering rules, learn about the following
reordering rule fields:

-   `Trigger <inventory/product_management/trigger>`{.interpreted-text
    role="ref"}
-   `Preferred route <inventory/warehouses_storage/route>`{.interpreted-text
    role="ref"}
-   `Vendor <inventory/warehouses_storage/set-vendor>`{.interpreted-text
    role="ref"}
-   `Bill of materials <inventory/warehouses_storage/set-bom-field>`{.interpreted-text
    role="ref"}
-   `Procurement group <inventory/warehouses_storage/procurement-grp>`{.interpreted-text
    role="ref"}
-   `Visibility days <inventory/product_management/visibility-days>`{.interpreted-text
    role="ref"}

::: {.note}
::: {.title}
Note
:::

The fields above are not available by default, and must be enabled by
selecting the `oi-settings-adjust`{.interpreted-text role="icon"}
`(adjust)`{.interpreted-text role="guilabel"} icon in the far-right
corner and selecting the desired column from the drop-down menu.
:::

### 0/0/1 reordering rule {#inventory/warehouses_storage/zero-zero}

The *0/0/1* reordering rule is a specialty rule used to replenish a
product that is not kept on-hand, each time a sales order (SO) is
confirmed for that product.

::: {.important}
::: {.title}
Important
:::

The 0/0/1 reordering rule is similar to the *Replenish on Order (MTO)*
route, in that both workflows are used to replenish a product upon
confirmation of an `SO (Sales Order)`{.interpreted-text role="abbr"}.

The main difference between the two methods is that the *Replenish on
Order* route automatically reserves the product for the
`SO (Sales Order)`{.interpreted-text role="abbr"} that caused it to be
replenished. This means the product **cannot** be used for a different
`SO (Sales Order)`{.interpreted-text role="abbr"}.

The 0/0/1 reordering rule does not have this limitation. A product
replenished using the rule is not reserved for any specific
`SO (Sales Order)`{.interpreted-text role="abbr"}, and can be used as
needed.

Another key difference is that replenishment orders created by the
*Replenish on Order* route are linked to the original
`SO (Sales Order)`{.interpreted-text role="abbr"} by a smart button at
the top of the order. When using the 0/0/1 reordering rule, a
replenishment order is created, but is not linked to the original
`SO (Sales Order)`{.interpreted-text role="abbr"}.

See the `Replenish on Order (MTO) <mto>`{.interpreted-text role="doc"}
documentation for a full overview of the MTO route.
:::

To create a 0/0/1 reordering rule, navigate to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and select a product.

At the top of the product\'s page, click the
`fa-refresh`{.interpreted-text role="icon"}
`Reordering Rules`{.interpreted-text role="guilabel"} smart button to
open the `Reordering Rules`{.interpreted-text role="guilabel"} page for
the product. On the resulting page, click `New`{.interpreted-text
role="guilabel"} to begin configuring a new reordering rule.

In the `Location`{.interpreted-text role="guilabel"} field of the new
reordering rule, select the location in which replenished products
should be stored. By default, this location is set to
`WH/Stock`{.interpreted-text role="guilabel"}.

In the `Route`{.interpreted-text role="guilabel"} field, select the
route the rule should use to replenish the item. For example, if the
product should be purchased from a vendor, select the
`Buy`{.interpreted-text role="guilabel"} route.

In the `Min Quantity`{.interpreted-text role="guilabel"} field and
`Max Quantity`{.interpreted-text role="guilabel"} field, leave the
values set to [0.00]{.title-ref}. In the `To Order`{.interpreted-text
role="guilabel"} field, enter a value of [1.00]{.title-ref}.



With the reordering rule configured using these values, each time an
`SO (Sales Order)`{.interpreted-text role="abbr"} causes the forecasted
quantity of the product to fall below the
`Min Quantity`{.interpreted-text role="guilabel"} of [0.00]{.title-ref},
the selected `Route`{.interpreted-text role="guilabel"} is used to
replenish the product in one-unit increments, back up to the
`Max Quantity`{.interpreted-text role="guilabel"} of [0.00]{.title-ref}.

::: {.example}
A picture frame is configured with a 0/0/1 reordering rule that uses the
*Buy* route. Zero units of the picture frame are kept on-hand at any
given time.

An `SO (Sales Order)`{.interpreted-text role="abbr"} is confirmed for
one unit of the picture frame, which causes the forecasted quantity to
drop to [-1.00]{.title-ref}. This triggers the reordering rule, which
automatically creates a `PO (Purchase Order)`{.interpreted-text
role="abbr"} for one unit of the picture frame.

Once the product is received from the vendor, the forecasted quantity of
the picture frame returns to [0.00]{.title-ref}. There is now one
picture frame on-hand, but it is not reserved for the
`SO (Sales Order)`{.interpreted-text role="abbr"} which triggered its
purchase. It can be used to fulfill that
`SO (Sales Order)`{.interpreted-text role="abbr"}, or reserved for a
different order.
:::

Trigger {#inventory/product_management/trigger}
-------

A reordering rule\'s *trigger* can be set to *automatic* or *manual*.
While both function the same way, the difference between the two types
of reordering rules is how the rule is launched:

-   `Auto <inventory/warehouses_storage/auto-rr>`{.interpreted-text
    role="ref"}: A purchase or manufacturing order is automatically
    created when the forecasted stock falls below the reordering rule\'s
    minimum quantity. By default, the `Auto`{.interpreted-text
    role="guilabel"} trigger is selected.
-   `Manual <inventory/warehouses_storage/manual-rr>`{.interpreted-text
    role="ref"}: The `Replenishment report <report>`{.interpreted-text
    role="doc"} lists products needing replenishment, showing
    current/forecasted stock, lead times, and arrival dates. Users can
    review forecasts before clicking *Order Once*.

To enable the `Trigger`{.interpreted-text role="guilabel"} field, go to
`Inventory app --> Operations -->
Replenishment`{.interpreted-text role="menuselection"} or
`Inventory app --> Configuration --> Reordering Rules`{.interpreted-text
role="menuselection"}. Then, click the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(adjust)`{.interpreted-text role="guilabel"} icon, located to the
far-right of the column titles, and tick the `Trigger`{.interpreted-text
role="guilabel"} checkbox.

In the `Trigger`{.interpreted-text role="guilabel"} column, select
`Auto`{.interpreted-text role="guilabel"} or `Manual`{.interpreted-text
role="guilabel"}. Refer to the sections below to learn about the
different types of reordering rules.

### Auto {#inventory/warehouses_storage/auto-rr}

*Automatic reordering rules*, enabled by setting the reordering rule\'s
`Trigger`{.interpreted-text role="guilabel"} field to
`Auto`{.interpreted-text role="guilabel"}, generate purchase or
manufacturing orders when either:

1.  The scheduler runs, and the *Forecasted* quantity is below the
    minimum, or
2.  A sales order is confirmed, and lowers the *Forecasted* quantity of
    the product below the minimum.

If the `Buy`{.interpreted-text role="guilabel"} route is selected, then
an `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} is
generated. To view and manage
`RFQs (Requests for Quotations)`{.interpreted-text role="abbr"},
navigate to
`Purchase app --> Orders --> Requests for Quotation`{.interpreted-text
role="menuselection"}.

If the `Manufacture`{.interpreted-text role="guilabel"} route is
selected, then an `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} is generated. To view and manage
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"}, navigate to
`Manufacturing app --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}.

When no route is selected, Odoo selects the `Route`{.interpreted-text
role="guilabel"} specified in the `Inventory`{.interpreted-text
role="guilabel"} tab of the product form.

::: {.tip}
::: {.title}
Tip
:::

The scheduler is set to run once a day, by default.

To manually trigger a reordering rule before the scheduler runs, ensure
`developer mode
<developer-mode>`{.interpreted-text role="ref"} is enabled, and select
`Inventory app --> Operations --> Run
Scheduler`{.interpreted-text role="menuselection"}. Then, click the
purple `Run Scheduler`{.interpreted-text role="guilabel"} button on the
pop-up window that appears.

Be aware that this also triggers any other scheduled actions.
:::

::: {.example}
The product, [Office Lamp]{.title-ref}, has an automatic reordering rule
set to trigger when the forecasted quantity falls below the
`Min Quantity`{.interpreted-text role="guilabel"} of [5.00]{.title-ref}.
Since the current `Forecast`{.interpreted-text role="guilabel"} is
[55.00]{.title-ref}, the reordering rule is **not** triggered.


:::

### Manual {#inventory/warehouses_storage/manual-rr}

*Manual reordering rules*, configured by setting the reordering rule\'s
`Trigger`{.interpreted-text role="guilabel"} field to
`Manual`{.interpreted-text role="guilabel"}, list a product on the
`replenishment dashboard <report>`{.interpreted-text role="doc"} when
the forecasted quantity falls below a specified minimum. Products on
this dashboard are called *needs*, because they are needed to fulfill
upcoming sales orders, for which the forecasted quantity is not enough.

The replenishment dashboard, accessible by navigating to
`Inventory app -->
Operations --> Replenishment`{.interpreted-text role="menuselection"},
considers sales order deadlines, forecasted stock levels, and vendor
lead times. It displays needs **only** when it is time to reorder items,
thanks to the `To
Reorder`{.interpreted-text role="guilabel"} filter.

When a product appears on the replenishment dashboard, clicking the
`Order Once`{.interpreted-text role="guilabel"} button generates the
purchase or manufacturing order with the specified amounts
`To Order`{.interpreted-text role="guilabel"}.



Route {#inventory/warehouses_storage/route}
-----

Odoo allows for multiple routes to be selected as replenishment methods
under the `Inventory`{.interpreted-text role="guilabel"} tab on each
product form. For instance, it is possible to select both
`Buy`{.interpreted-text role="guilabel"} and
`Manufacture`{.interpreted-text role="guilabel"}, indicating to Odoo
that the product can be bought or manufactured.

Odoo also enables users to set a preferred route for a product\'s
reordering rule. This is the route that the rule defaults to, if
multiple are selected. To select a preferred route, begin by navigating
to
`Inventory app --> Configuration --> Reordering Rules`{.interpreted-text
role="menuselection"}.

By default, the `Route`{.interpreted-text role="guilabel"} column is
hidden on the `Reordering Rules`{.interpreted-text role="guilabel"}
page.

Reveal the `Route`{.interpreted-text role="guilabel"} column by
selecting the `(slider)`{.interpreted-text role="guilabel"} icon to the
far-right of the column titles, and checking the
`Route`{.interpreted-text role="guilabel"} option from the drop-down
menu that appears.

Click inside of the column on the row of a reordering rule, and a
drop-down menu shows all available routes for that rule. Select one to
set it as the preferred route.



::: {.important}
::: {.title}
Important
:::

If multiple routes are enabled for a product but no preferred route is
set for its reordering rule, the product is reordered using the selected
route that is listed first on the `Inventory`{.interpreted-text
role="guilabel"} tab of the product form.
:::

### Advanced uses

Pairing `Preferred Route`{.interpreted-text role="guilabel"} with one of
the following fields on the replenishment report unlocks advanced
configurations of reordering rules. Consider the following:

::: {#inventory/warehouses_storage/set-vendor}
-   `Vendor`{.interpreted-text role="guilabel"}: When the selected
    `Preferred Route`{.interpreted-text role="guilabel"} is
    `Buy`{.interpreted-text role="guilabel"}, setting the
    `Vendor`{.interpreted-text role="guilabel"} field to one of the
    multiple vendors on the vendor pricelist indicates to Odoo that the
    vendor is automatically populated on
    `RFQs (Requests for Quotations)`{.interpreted-text role="abbr"} when
    a reordering rule triggers the creation of a purchase order.
:::

::: {#inventory/warehouses_storage/set-bom-field}
-   `Bill of Materials`{.interpreted-text role="guilabel"}: When the
    `Preferred Route`{.interpreted-text role="guilabel"} is set to
    `Manufacture`{.interpreted-text role="guilabel"}, and there are
    multiple `BoMs (Bills of Materials)`{.interpreted-text role="abbr"}
    in use, specifying the desired
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} in the
    replenishment report, draft manufacturing orders are created with
    this `BoM (Bill of Materials)`{.interpreted-text role="abbr"} in
    use.
:::

::: {#inventory/warehouses_storage/procurement-grp}
-   `Procurement Group`{.interpreted-text role="guilabel"}: This is a
    way to group related `POs (Purchase Orders)`{.interpreted-text
    role="abbr"} or `MOs (Manufacturing Orders)`{.interpreted-text
    role="abbr"} that are tied to fulfilling a specific demand, like an
    `SO (Sales Order)`{.interpreted-text role="abbr"} or a project. It
    helps organize and track which orders are linked to a particular
    demand.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Procurement groups link replenishment methods to demand, enabling
    smart buttons to appear when using the
    `MTO route <mto>`{.interpreted-text role="doc"}.

    ![Sales order (demand) with a linked purchase order (replenishment
    method).](reordering_rules/po-smartbutton.png)
    :::

    In the context of reordering rules:

    -   Reordering rules do not automatically assign a procurement
        group, which is why there are no smart buttons that link
        `SOs (Sales Orders)`{.interpreted-text role="abbr"} to
        `POs (Purchase Orders)`{.interpreted-text role="abbr"}, unlike
        the `MTO (Make to Order)`{.interpreted-text role="abbr"} route.
    -   To enable smart buttons for products replenished by reordering
        rules (not `MTO (Make to
        Order)`{.interpreted-text role="abbr"}), with specific
        quantities linked to specific demands (e.g.
        `SOs (Sales Orders)`{.interpreted-text role="abbr"}), assign a
        procurement group.
    -   Without a procurement group, demands for the same product can be
        combined into a single
        `RFQ (Request for Quotation)`{.interpreted-text role="abbr"},
        even if the reordering rule is executed multiple times for those
        demands. This allows for more efficient procurement by
        consolidating demands into fewer orders.

    Selecting a procurement group in the
    `Procurement Group`{.interpreted-text role="guilabel"} field on the
    replenishment report ensures that all linked orders are grouped
    under the same demand, based on the defined route.

    ::: {.exercise}
    How can you set the *Procurement Group*, *Vendor*, and *Preferred
    Route* fields on the replenishment report to generate a single
    `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} for
    five different products in sales order SO35, given they share the
    same vendor, Azure Interior, and ensure other demands for these
    products are handled separately?

    ::: {.spoiler}
    View the answer

    1.  Set the `Procurement Group`{.interpreted-text role="guilabel"}
        to [SO35]{.title-ref}, in the reordering rule for all five
        products. This groups the demands for [SO35]{.title-ref} in the
        same `RFQ (Request for Quotation)`{.interpreted-text
        role="abbr"} or `MO (Manufacturing Order)`{.interpreted-text
        role="abbr"}.
    2.  Set the `Vendor`{.interpreted-text role="guilabel"} to [Azure
        Interior]{.title-ref} to ensure the
        `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} is
        created for the same supplier.
    3.  Set the `Preferred Route`{.interpreted-text role="guilabel"} to
        `Buy`{.interpreted-text role="guilabel"} to generate an
        `RFQ (Request for Quotation)`{.interpreted-text role="abbr"}.
    4.  Click the `Order Once`{.interpreted-text role="guilabel"} button
        to generate a single
        `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} for
        the five products tied to [SO35]{.title-ref}.

    | After placing the order, remove [SO35]{.title-ref} from the
      `Procurement Group`{.interpreted-text role="guilabel"} field of
      the five products\' reordering rules. This ensures future demands
      for these products are managed separately and assigned to
      different `RFQs (Requests for Quotations)`{.interpreted-text
      role="abbr"} (the usual behavior).
    :::
    :::
:::

Just-in-time logic {#inventory/warehouses_storage/just-in-time}
------------------

*Just-in-time logic* in Odoo minimizes storage costs by placing orders
precisely to meet deadlines. This is achieved using the
`forecasted date <inventory/warehouses_storage/forecasted-date>`{.interpreted-text
role="ref"}, which determines when replenishment is necessary to avoid
overstocking.

The forecasted date is the **earliest possible date** to receive a
product if the replenishment process starts immediately. It is
calculated by summing the lead times linked to the replenishment
process, such as
`vendor lead times <inventory/warehouses_storage/purchase-lt>`{.interpreted-text
role="ref"} and
`purchasing delays <inventory/warehouses_storage/purchase-security-lt>`{.interpreted-text
role="ref"} for purchases, or
`manufacturing lead times <inventory/warehouses_storage/manuf-lt>`{.interpreted-text
role="ref"} for production. Both automatic and manual reordering rules
work this way.

::: {.example}
For a product with a 5-day total lead time and a sales order delivery
date in 10 days, Odoo waits 5 days to place the order, ensuring it
arrives just in time for delivery.
:::

Important considerations:

-   **If this feels risky**, consider adding buffer time or
    `adjusting lead times <lead_times>`{.interpreted-text role="doc"}
    for more flexibility.
-   While lead times and just-in-time logic provide additional control,
    **reordering rules work perfectly fine without them**. Keeping
    delivery dates on sales orders as their *creation date* ensures
    purchases are immediately triggered when needed

### Forecasted date and To Order quantity {#inventory/warehouses_storage/forecasted-date}

To view the *forecasted date*, go to the replenishment report and click
the `fa-info-circle`{.interpreted-text role="icon"}
`(info)`{.interpreted-text role="guilabel"} icon for the desired
reordering rule. The `Replenishment Information`{.interpreted-text
role="guilabel"} pop-up window displays the
`Forecasted Date`{.interpreted-text role="guilabel"} and various lead
times.

The *forecasted date* is the total time needed to procure a product in
Odoo. It is calculated by summing the lead times linked to the
product\'s replenishment process. The total of these lead times, added
to the current date, determines when Odoo checks for demanded stock.

::: {.important}
::: {.title}
Important
:::

The forecasted date is the **earliest possible date** the customer can
receive the product if the replenishment process began right **now**. It
is calculated by adding all lead times related to the product to the
current date.
:::

::: {.example}
A manual reordering rule is set up with no minimum or maximum
quantities.

-   Vendor lead time is 4 days, the purchase security lead time is 1
    day, and the days to purchase is 2 days.
-   Today\'s date is November 26.
-   These add up to 7 days, making the forecasted date, December 3rd.

A confirmed `SO (Sales Order)`{.interpreted-text role="abbr"} for 5
units has a delivery date of December 3rd (7 days from today). This
demand will appear on the replenishment report today, in the **To
Order** field.

However, if the delivery date were later than December 3rd, it would not
yet appear on the report. Odoo only displays quantities to replenish
when they fall within the forecasted date window, ensuring orders are
placed precisely when needed.


:::

The *just-in-time* logic ensures replenishment happens only when it\'s
necessary for the forecasted date\'s demand, helping avoid overstocking.

For example:

-   If the forecasted quantity drops below the minimum **on** the
    forecasted date, replenishment must begin immediately to avoid
    shortages.
-   If the quantity drops below the minimum **after** the forecasted
    date, replenishment can wait.

The **To Order** quantity is the total demand on the forecasted date.

By timing purchase orders based on the combined lead times, Odoo
optimizes stock levels, keeping inventory minimal while ensuring future
requirements are ordered at the last possible moment---strategic
procrastination without the stress!

### Common confusion about forecasted quantities

`SOs (Sales Orders)`{.interpreted-text role="abbr"} due **after** the
`Forecasted Date`{.interpreted-text role="guilabel"} are not accounted
for in the `Forecast`{.interpreted-text role="guilabel"} quantities of
the reordering rule.

They are, however, accounted for on the forecasted report that is opened
by clicking the `fa-area-chart`{.interpreted-text role="icon"}
`(graph)`{.interpreted-text role="guilabel"} icon on the replenishment
report, as this one represents the **long-term forecasted quantity**.

::: {.example}
![Continuing the above example, when the sales order\'s deadline is
adjusted to December 4th, the `Forecast`{.interpreted-text
role="guilabel"} and `To Order`{.interpreted-text role="guilabel"}
quantities are zero.](reordering_rules/zero-forecast.png)

![Opening the `Forecasted Report`{.interpreted-text role="guilabel"}
shows the `Forecasted`{.interpreted-text role="guilabel"} units is

:::

Visibility days {#inventory/product_management/visibility-days}
---------------

*Visibility days* enable the ability to determine if additional
quantities should be added to the planned replenishment. Odoo checks if
forecasted stock on the forecasted date will drop below the minimum in
the reordering rule. **Only if** it is time to reorder, visibility days
check additional future demand by the specified number of days.

This feature helps consolidate orders by grouping immediate and
near-future needs, reducing transport costs and enabling supplier
discounts for larger orders.

To set visibility days to incorporate orders for a specified number of
days in the future, navigate to
`Inventory app --> Operations --> Replenishment`{.interpreted-text
role="menuselection"}, or by clicking the *Reordering Rules* smart
button from the product form.

Next, enable the `Visibility Days`{.interpreted-text role="guilabel"}
field by clicking the `oi-settings-adjust`{.interpreted-text
role="icon"} `(adjust)`{.interpreted-text role="guilabel"} icon to the
far right and choosing the feature from the drop-down menu. Then, enter
the desired visibility days.

::: {.important}
::: {.title}
Important
:::

The forecasted date is never pushed forward or extended; Odoo only
checks the extra visibility days if the stock falls below the minimum
threshold on the forecasted date.
:::

### Example where visibility days is triggered

A product shipped from Asia has a combined vendor lead time of 30 days
and a shipping cost of \$100 (including
`landed costs <../../product_management/inventory_valuation/landed_costs>`{.interpreted-text
role="doc"} and tariffs).

-   November 4: Current date. The forecasted date is December 4 (30 days
    later).
-   `SO (Sales Order)`{.interpreted-text role="abbr"} 1: Requires the
    product by Dec 4. Odoo places the order today, costing \$100.
-   `SO (Sales Order)`{.interpreted-text role="abbr"} 2: Requires the
    product by Dec 19. Normally, Odoo would order on Nov 19, costing an
    additional \$100.
-   `SO (Sales Order)`{.interpreted-text role="abbr"} 3: Requires the
    product by Dec 25. Normally, Odoo would order on Nov 25, costing
    another \$100.

Ordering separately for these sales orders totals \$300 in shipping
costs.



Setting `Visibility Days`{.interpreted-text role="guilabel"} to
[20.0]{.title-ref} allows Odoo to \"look ahead\" 20 days from December 4
(`SO (Sales Order)`{.interpreted-text role="abbr"} 1\'s forecasted date)
to December 24.

-   It groups `SO (Sales Order)`{.interpreted-text role="abbr"} 2\'s
    order with `SO (Sales Order)`{.interpreted-text role="abbr"} 1,
    reducing shipping costs by consolidating orders.
-   `SO (Sales Order)`{.interpreted-text role="abbr"} 3, which is due on
    Dec 25, is one day late and is not grouped with the other two
    orders.



### Counterexample where visibility days is not triggered

Considering the example above, if `SO (Sales Order)`{.interpreted-text
role="abbr"} 1 does not exist, then:

-   **November 4**: Current date. The forecasted date is December 4 (30
    days later).
-   **November 5**: The forecasted date shifts to December 5.
-   `SO (Sales Order)`{.interpreted-text role="abbr"} 2: Requires the
    product by December 19. Odoo will only trigger the order on November
    19, meaning the user will not see a replenishment notification until
    then.

This shows that visibility days complement just-in-time logic by
optimizing it to balance replenishment costs more effectively.


