# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/products/temporary_reordering.md

Temporary reordering rules
==========================

Some businesses require certain products to always have a minimum
quantity of stock on-hand at any given time. To avoid stock falling
below a certain threshold, companies can create *reordering rules* in
Odoo to automate purchase orders for specific products.

Reordering rules keep the forecasted stock levels above a certain
threshold, without exceeding a specified upper limit, or maximum amount.
When a product with a reordering rule falls below a specified quantity,
Odoo generates an order using the specified *route* (e.g. *Buy* or
*Manufacture*) to replenish the stock.

In certain cases, businesses might opt for *temporary reordering rules*
when they do not want specific products to be replenished automatically.

In Odoo, a \"temporary\" reordering rule is created in the replenishment
dashboard when a product:

1.  is configured with a *Buy* route
2.  has no reordering rule configured
3.  has [0]{.title-ref} quantity in stock
4.  is included in a sales order (SO).

This rule is deleted upon confirmation of the purchase order (PO)
generated for the product.

::: {.seealso}
\-
`../../inventory/warehouses_storage/replenishment/reordering_rules`{.interpreted-text
role="doc"} - `../../purchase/products/reordering`{.interpreted-text
role="doc"}
:::

Configuration
-------------

To configure a product that triggers temporary reordering rules when its
stock reaches [0]{.title-ref}, begin by going to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The same configurations can also be made on an existing product, by
going to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and selecting an existing product.
:::

On the product form, enter the product name, and ensure the
`Can be Sold`{.interpreted-text role="guilabel"} and
`Can be Purchased`{.interpreted-text role="guilabel"} options are
enabled, located beneath the `Product Name`{.interpreted-text
role="guilabel"} field.

Then, set the `Product Type`{.interpreted-text role="guilabel"} to
[Storable Product]{.title-ref}, under the `General
Information`{.interpreted-text role="guilabel"} tab.

Next, click the `Purchase`{.interpreted-text role="guilabel"} tab, and
under `Vendor`{.interpreted-text role="guilabel"}, click
`Add a line`{.interpreted-text role="guilabel"} to select a vendor from
the drop-down menu. Then, set a purchase price under
`Price`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

A vendor **must** be set for temporary reordering rules to work. While a
`PO (purchase
order)`{.interpreted-text role="abbr"} can still be created
automatically, attempting to replenish the product from the
`Replenishment`{.interpreted-text role="guilabel"} dashboard in the
*Inventory* app triggers a warning to add a vendor on the product form.

{.align-center}
:::

Before creating a `SO (sales order)`{.interpreted-text role="abbr"} for
the product, ensure the `On Hand`{.interpreted-text role="guilabel"}
smart button on the product form reads [0.00 Units]{.title-ref}. Then,
ensure that the `Reordering Rules`{.interpreted-text role="guilabel"}
smart button reads [0]{.title-ref}, indicating there are no rules
applied to this product.

{.align-center}

Trigger temporary reordering rule
---------------------------------

To trigger a temporary reordering rule, create a new sales order for a
product by navigating to `Sales app --> New`{.interpreted-text
role="menuselection"}.

Then, add a customer in the `Customer`{.interpreted-text
role="guilabel"} field, and click `Add a product`{.interpreted-text
role="guilabel"} under the `Product`{.interpreted-text role="guilabel"}
column in the `Order Lines`{.interpreted-text role="guilabel"} tab.
Next, select the desired product from the drop-down menu. Lastly,
`Confirm`{.interpreted-text role="guilabel"} the
`SO (sales order)`{.interpreted-text role="abbr"}.

{.align-center}

Check replenishment report
--------------------------

To see the temporary reordering rule created for the out-of-stock
product included in the sales order, navigate to
`Inventory app --> Operations --> Replenishment`{.interpreted-text
role="menuselection"}. Doing so opens the
`Replenishment`{.interpreted-text role="guilabel"} dashboard.

On this dashboard, locate the product for which the temporary reordering
rule was created. On its product line, its `On Hand`{.interpreted-text
role="guilabel"} quantity, negative `Forecast`{.interpreted-text
role="guilabel"} quantity, *Buy* `Route`{.interpreted-text
role="guilabel"}, and `To Order`{.interpreted-text role="guilabel"}
quantity to replenish can be seen.

Additionally, two replenishment options are located to the far-right of
the row: `Order
Once`{.interpreted-text role="guilabel"} and
`Automate`{.interpreted-text role="guilabel"}.

{.align-center}

To use the one-time, temporary reordering rule, click
`Order Once`{.interpreted-text role="guilabel"}. This action triggers a
confirmation pop-up window in the top-right corner, reading
`The following replenishment
order has been generated`{.interpreted-text role="guilabel"}, along with
a new purchase order number.

::: {.tip}
::: {.title}
Tip
:::

Once the purchase order has been generated after clicking
`Order Once`{.interpreted-text role="guilabel"}, refresh the page. The
temporary reordering rule for the product no longer appears in the
`Replenishment`{.interpreted-text role="guilabel"} dashboard.
:::

Complete purchase order
-----------------------

To view the purchase order created from the
`Replenishment`{.interpreted-text role="guilabel"} dashboard, navigate
to the `Purchase app`{.interpreted-text role="menuselection"}, and
select the generated `PO (purchase order)`{.interpreted-text
role="abbr"} from the `Requests for Quotation`{.interpreted-text
role="guilabel"} overview.

From here, click `Confirm Order`{.interpreted-text role="guilabel"},
then click `Receive Products`{.interpreted-text role="guilabel"}.
Finally, click `Validate`{.interpreted-text role="guilabel"} to complete
the purchase order.

{.align-center}

Now, the original sales order can be delivered and invoiced.

::: {.note}
::: {.title}
Note
:::

Once the `SO (sales order)`{.interpreted-text role="abbr"} is delivered
and invoiced, ensure there are no reordering rules on the product form.

Go to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, select the product, and confirm that the
`Reordering Rules`{.interpreted-text role="guilabel"} smart button
displays [0]{.title-ref}.
:::
