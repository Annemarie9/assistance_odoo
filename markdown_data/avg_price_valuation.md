# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/get_started/avg_price_valuation.md

Average price on returned goods
===============================

::: {#inventory/avg_cost/definition}
*Average cost valuation* (AVCO) is an inventory valuation method that
evaluates cost based on the total cost of goods bought or produced
during a period, divided by the total number of items on-hand. Inventory
valuation is used to:
:::

-   reflect the value of a company\'s assets;
-   keep track of the amount of unsold goods;
-   account for monetary value in goods that have yet to generate
    profit;
-   report on flow of goods throughout the quarter.

Because `AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"}
uses the weighted average to evaluate the cost, it is a good fit for
companies that sell only a few different products in large quantities.
In Odoo, this costing analysis is *automatically updated* each time
products are received.

Thus, when shipments are returned to their supplier, Odoo automatically
generates accounting entries to reflect the change in inventory
valuation. However, Odoo does **not** automatically update the
`AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"}
calculation, because
`this can potentially create inconsistencies with inventory
valuation <inventory/avg_price/leaving_inventory>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

This document addresses a specific use case for theoretical purposes.
For instructions on how to set up and use
`AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"}, refer to
the `inventory valuation configuration
<../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config>`{.interpreted-text
role="doc"} doc.
:::

::: {.seealso}
\- `Using inventory valuation
<../../../inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation>`{.interpreted-text
role="doc"} -
`Other inventory valuation methods <inventory/warehouses_storage/costing_methods>`{.interpreted-text
role="ref"}
:::

Configuration
-------------

To use average cost inventory valuation on a product, navigate to
`Inventory -->
Configuration --> Product Categories`{.interpreted-text
role="menuselection"} and select the category that will be using
`AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"}. On the
product category page, set `Costing Method`{.interpreted-text
role="guilabel"} to [Average Cost (AVCO)]{.title-ref} and
`Inventory Valuation`{.interpreted-text role="guilabel"} to
[Automated]{.title-ref}.

::: {.seealso}
`Inventory valuation configuration
<../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config>`{.interpreted-text
role="doc"}
:::

Using average cost valuation
----------------------------

The average cost method adjusts the inventory valuation when products
are received in the warehouse. This section explains how it works, but
if the explanation is unnecessary, skip to the `return
to supplier use case <inventory/avg_cost/return>`{.interpreted-text
role="ref"} section.

### Formula {#inventory/avg_cost/formula}

When new products arrive, the new average cost for each product is
recomputed using the formula:

$$Avg~Cost = \frac{(Old~Qty \times Old~Avg~Cost) + (Incoming~Qty \times Purchase~Price)}{Final~Qty}$$

-   **Old Qty**: product count in stock before receiving the new
    shipment;
-   **Old Avg Cost**: calculated average cost for a single product from
    the previous inventory valuation;
-   **Incoming Qty**: count of products arriving in the new shipment;
-   **Purchase Price**: estimated price of products at the reception of
    products (since vendor bills may arrive later). The amount includes
    not only the price for the products, but also added costs, such as
    shipping, taxes, and `landed costs
    <../../../inventory_and_mrp/inventory/product_management/inventory_valuation/landed_costs>`{.interpreted-text
    role="doc"}. At reception of the vendor bill, this price is
    adjusted;
-   **Final Qty**: quantity of on-hand stock after the stock move.

::: {#inventory/avg_cost/definite_rule}
::: {.important}
::: {.title}
Important
:::

When products leave the warehouse, the average cost **does not** change.
Read about why the average cost valuation is **not** adjusted
`here <inventory/avg_price/leaving_inventory>`{.interpreted-text
role="ref"}.
:::
:::

### Compute average cost {#inventory/avg_cost/math_table}

To understand how the average cost of a product changes with each
shipment, consider the following table of warehouse operations and stock
moves. Each is a different example of how the average cost valuation is
affected.

  ------------------------------------------------------------------------
  Operation               Incoming    Inventory      Qty On Hand Avg Cost
                          Value       Value                      
  ----------------------- ----------- -------------- ----------- ---------
                                      \$0            0           \$0

  Receive 8 tables at     8 \* \$10   \$80           8           \$10
  \$10/unit                                                      

  Receive 4 tables at     4 \* \$16   \$144          12          \$12
  \$16/unit                                                      

  Deliver 10 tables       -10 \* \$12 \$24           2           \$12
  ------------------------------------------------------------------------

::: {#inventory/avg_cost/ex-1}
::: {.exercise}
Ensure comprehension of the above computations by reviewing the
\"Receive 8 tables at \$10/unit\" example.

Initially, the product stock is 0, so all values are \$0.

In the first warehouse operation, [8]{.title-ref} tables are received at
[\$10]{.title-ref} each. The average cost is calculated using the
`formula <inventory/avg_cost/formula>`{.interpreted-text role="ref"}:

$$Avg~Cost = \frac{0 + 8 \times $10}{8} = \frac{$80}{8} = $10$$

-   Since the *incoming quantity* of tables is [8]{.title-ref} and the
    *purchase price* for each is [\$10]{.title-ref},
-   The inventory value in the numerator is evaluated to
    [\$80]{.title-ref};
-   [\$80]{.title-ref} is divided by the total amount of tables to
    store, [8]{.title-ref};
-   [\$10]{.title-ref} is the average cost of a single table from the
    first shipment.

To verify this in Odoo, in the *Purchase* app, order [8]{.title-ref}
quantities of a new product, [Table]{.title-ref}, with no previous stock
moves, for [\$10]{.title-ref} each.

In the table\'s `Product Category`{.interpreted-text role="guilabel"}
field in the `General Information`{.interpreted-text role="guilabel"}
tab of the product form, click the `➡️ (arrow)`{.interpreted-text
role="guilabel"} icon, to open an `External Link`{.interpreted-text
role="guilabel"} to edit the product category. Set the
`Costing Method`{.interpreted-text role="guilabel"} to [Average Cost
(AVCO)]{.title-ref} and `Inventory Valuation`{.interpreted-text
role="guilabel"} to [Automated]{.title-ref}.

Then, return to the purchase order. Click
`Confirm Order`{.interpreted-text role="guilabel"}, and click `Receive
Products`{.interpreted-text role="guilabel"} to confirm receipt.

Next, check the inventory valuation record generated by the product
reception by navigating to
`Inventory --> Reporting --> Inventory Valuation`{.interpreted-text
role="menuselection"}. Select the drop-down for [Table]{.title-ref}, and
view the `Total Value`{.interpreted-text role="guilabel"} column for the
*valuation layer* (`inventory
valuation at a specific point in time = on-hand quantity * unit price`{.interpreted-text
role="dfn"}). The 8 tables in-stock are worth \$80.

{.align-center}
:::
:::

::: {.tip}
::: {.title}
Tip
:::

When the product category\'s `Costing Method`{.interpreted-text
role="guilabel"} is set to `AVCO`{.interpreted-text role="guilabel"},
then the average cost of a product is also displayed on the
`Cost`{.interpreted-text role="guilabel"} field, under the
`General Information`{.interpreted-text role="guilabel"} tab, on the
product page itself.
:::

#### Product delivery (use case)

For outgoing shipments,
`outbound products have no effect on the average cost valuation
<inventory/avg_cost/definite_rule>`{.interpreted-text role="ref"}.
Although the average cost valuation is not recalculated, the inventory
value still decreases because the product is removed from stock and
delivered to the customer location.

::: {.exercise}
To demonstrate that the average cost valuation is not recalculated,
examine the \"Deliver 10 tables\" example.

$$Avg~Cost = \frac{12 \times $12 + (-10) \times $12}{12-10} = \frac{24}{2} = $12$$

1.  Because 10 tables are being sent out to customers, the *incoming
    quantity* is [-10]{.title-ref}. The previous average cost
    ([\$12]{.title-ref}) is used in lieu of a vendor\'s *purchase
    price*;
2.  The *incoming inventory value* is [-10 \* \$12 =
    -\$120]{.title-ref};
3.  The old *inventory value* ([\$144]{.title-ref}) is added to the
    *incoming inventory value* ([-\$120]{.title-ref}), so [\$144 +
    -\$120 = \$24]{.title-ref};
4.  Only [2]{.title-ref} tables remain after shipping out
    [10]{.title-ref} tables from [12]{.title-ref}. So the current
    *inventory value* ([\$24]{.title-ref}) is divided by the on-hand
    quantity ([2]{.title-ref});
5.  [\$24 / 2 = \$12]{.title-ref}, which is the same average cost as the
    previous operation.

To verify this in Odoo, sell [10]{.title-ref} tables in the *Sales* app,
validate the delivery, and then review the inventory valuation record by
going to in `Inventory --> Reporting -->
Inventory Valuation`{.interpreted-text role="menuselection"}. In the
topmost valuation layer, delivering [10]{.title-ref} tables reduces the
product\'s value by [-\$120]{.title-ref}.

**Note**: What is not represented in this stock valuation record is the
revenue made from this sale, so this decrease is not a loss to the
company.

{.align-center}
:::

Return items to supplier (use case) {#inventory/avg_cost/return}
-----------------------------------

Because the price paid to suppliers can differ from the price the
product is valued at with the
`AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"} method,
Odoo handles returned items in a specific way.

1.  Products are returned to suppliers at the original purchase price,
    but;
2.  The internal cost valuation remains unchanged.

The above
`example table <inventory/avg_cost/math_table>`{.interpreted-text
role="ref"} is updated as follows:

  ------------------------------------------------------------------------
  Operation               Qty\*Avg    Inventory      Qty On Hand Avg Cost
                          Cost        Value                      
  ----------------------- ----------- -------------- ----------- ---------
                                      \$24           2           \$12

  Return 1 table bought   -1 \* \$12  \$12           1           \$12
  at \$10                                                        
  ------------------------------------------------------------------------

In other words, returns to vendors are perceived by Odoo as another form
of a product exiting the warehouse. To Odoo, because the table is valued
at \$12 per unit, the inventory value is reduced by [\$12]{.title-ref}
when the product is returned; the initial purchase price of
[\$10]{.title-ref} is unrelated to the table\'s average cost.

::: {.example}
To return a single table that was purchased for [\$10]{.title-ref},
navigate to the receipt in the *Inventory* app for the
`8 tables purchased in Exercise 1 <inventory/avg_cost/ex-1>`{.interpreted-text
role="ref"} by going to the `Inventory Overview`{.interpreted-text
role="guilabel"}, clicking on `Receipts`{.interpreted-text
role="guilabel"}, and selecting the desired receipt.

Then, click `Return`{.interpreted-text role="guilabel"} on the validated
delivery order, and modify the quantity to [1]{.title-ref} in the
reverse transfer window. This creates an outgoing shipment for the
table. Select `Validate`{.interpreted-text role="guilabel"} to confirm
the outgoing shipment.

Return to
`Inventory --> Reporting --> Inventory Valuation`{.interpreted-text
role="menuselection"} to see how the outgoing shipment decreases the
inventory value by \$12.

{.align-center}
:::

### Eliminate stock valuation errors in outgoing products {#inventory/avg_price/leaving_inventory}

Inconsistencies can occur in a company\'s inventory when the average
cost valuation is recalculated on outgoing shipments.

To demonstrate this error, the table below displays a scenario in which
1 table is shipped to a customer and another is returned to a supplier
at the purchased price.

  ---------------------------------------------------------------------------
  Operation                    Qty\*Price   Inventory     Qty On     Avg Cost
                                            Value         Hand       
  ---------------------------- ------------ ------------- ---------- --------
                                            \$24          2          \$12

  Ship 1 product to customer   -1 \* \$12   \$12          1          \$12

  Return 1 product initially   -1 \* \$10   **\$2**       **0**      \$12
  bought at \$10                                                     
  ---------------------------------------------------------------------------

In the final operation above, the final inventory valuation for the
table is [\$2]{.title-ref} even though there are [0]{.title-ref} tables
left in stock.

::: {.admonition}
Correct method

Use the average cost to value the return. This does not mean the company
gets \$12 back for a \$10 purchase; the item returned for \$10 is valued
internally at \$12. The inventory value change represents a product
worth \$12 no longer being accounted for in company assets.
:::

Anglo-Saxon accounting
----------------------

In addition to using `AVCO (Average Cost Valuation)`{.interpreted-text
role="abbr"}, companies that use **Anglo-Saxon accounting** also keep a
holding account that tracks the amount to be paid to vendors. Once a
vendor delivers an order, **inventory value** increases based on the
vendor price of the products that have entered the stock. The holding
account (called **stock input**) is credited and only reconciled once
the vendor bill is received.

::: {.seealso}
\-
`Anglo-Saxon vs. Continental <inventory/warehouses_storage/accounting-types>`{.interpreted-text
role="ref"}
:::

The table below reflects journal entries and accounts. The *stock input*
account stores the money intended to pay vendors when the vendor bill
has not yet been received. To balance accounts when returning products
that have a price difference between the price the product is **valued
at** and the price it was bought for, a *price difference* account is
created.

::: {#inventory/avg_price/price-table}
  ---------------------------------------------------------------------------
  Operation                Stock      Price     Inventory   Qty On    Avg
                           Input      Diff      Value       Hand      Cost
  ------------------------ ---------- --------- ----------- --------- -------
                                                \$0         0         \$0

  Receive 8 tables at \$10 (\$80)               \$80        8         \$10

  Receive vendor bill \$80 \$0                  \$80        8         \$10

  Receive 4 tables at \$16 (\$64)               \$144       12        \$12

  Receive vendor bill \$64 \$0                  \$144       12        \$12

  Deliver 10 tables to     \$0                  \$24        2         \$12
  customer                                                            

  Return 1 table initially **\$10**   **\$2**   **\$12**    1         \$12
  bought at \$10                                                      

  Receive vendor refund    \$0        \$2       \$12        1         \$12
  \$10                                                                
  ---------------------------------------------------------------------------
:::

### Product reception

#### Summary

At product reception, Odoo ensures companies can pay for goods that were
purchased by preemptively moving an amount matching the price of
received goods into the `liability account
</applications/finance/accounting/get_started/cheat_sheet>`{.interpreted-text
role="doc"}, **Stock Input**. Then, once the bill has been received, the
amount in the holding account is transferred to *Accounts Payable*.
Transfers into this account means the bill has been paid. **Stock
Input** is reconciled once the vendor bill is received.

Inventory valuation is a method of calculating how much each in-stock
product is worth internally. Since there is a difference between the
price the product is **valuated at** and the price the product was
actually **purchased for**, the **Inventory Valuation** account is
unrelated to the crediting and debiting operations of the **Stock
Input** account.

To conceptualize all this, follow the breakdown below.

#### Accounts balanced at received products

In this example, a company starts with zero units of a product,
[table]{.title-ref}, in stock. Then, 8 tables are received from the
vendor:

1.  The **Stock Input** account stores [\$80]{.title-ref} of credit owed
    to the vendor. The amount in this account is unrelated to the
    inventory value.
2.  [\$80]{.title-ref} worth of tables came **in** (**debit** the
    *Inventory Value* account [\$80]{.title-ref}), and
3.  [\$80]{.title-ref} must be paid **out** for received goods
    (**credit** the *Stock Input* account [\$80]{.title-ref}).

##### In Odoo

Odoo generates an accounting journal entry when shipments that use
`AVCO (Average Cost Valuation)`{.interpreted-text role="abbr"} costing
method are received. Configure a
`Price Difference Account`{.interpreted-text role="guilabel"} by
selecting the `➡️ (arrow)`{.interpreted-text role="guilabel"} icon next
to the `Product Category`{.interpreted-text role="guilabel"} field on
the product page.

Under `Account Properties`{.interpreted-text role="guilabel"}, create a
new `Price Difference Account`{.interpreted-text role="guilabel"} by
typing in the name of the account and clicking
`Create and Edit`{.interpreted-text role="guilabel"}. Then set the
account `Type`{.interpreted-text role="guilabel"} as
[Expenses]{.title-ref}, and click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

Then, receive the shipment in the *Purchase* app or *Inventory* app, and
navigate to the
`Accounting app --> Accounting --> Journal Entries`{.interpreted-text
role="menuselection"}. In the list, find the
`Reference`{.interpreted-text role="guilabel"} that matches the
warehouse reception operation for the relevant product.

{.align-center}

Click on the line for 8 tables. This accounting journal entry shows that
when the 8 tables were received, the [Stock Valuation]{.title-ref}
account increased by [\$80]{.title-ref}. Conversely, the **Stock Input**
account (set as [Stock Interim (Received)]{.title-ref} account by
default) is credited [\$80]{.title-ref}.

{.align-center}

#### Accounts balanced at received vendor bill

In this example, a company starts with zero units of a product, table,
in stock. Then, 8 tables are received from the vendor. When the bill is
received from vendor for 8 tables:

1.  Use [\$80]{.title-ref} in the **Stock Input** account to pay the
    bill. This cancels out and the account now holds [\$0]{.title-ref}.
2.  Debit **Stock Input** [\$80]{.title-ref} (to reconcile this
    account).
3.  Credit **Accounts payable** [\$80]{.title-ref}. This account stores
    the amount the company owes others, so accountants use the amount to
    write checks to vendors.

##### In Odoo

Once the vendor requests payment, navigate to the
`Purchase app --> Orders -->
Purchase`{.interpreted-text role="menuselection"} and select the
`PO (Purchase Order)`{.interpreted-text role="abbr"} for 8 tables.
Inside the `PO (Purchase
Order)`{.interpreted-text role="abbr"}, select
`Create Bill`{.interpreted-text role="guilabel"}.

Switch to the `Journal Items`{.interpreted-text role="guilabel"} tab to
view how [\$80]{.title-ref} is transferred from the holding account,
[Stock Interim (Received)]{.title-ref} to [Accounts
Payable]{.title-ref}. `Confirm`{.interpreted-text role="guilabel"} the
bill to record the payment to the vendor.

{.align-center}

### On product delivery

In the
`above example table <inventory/avg_price/price-table>`{.interpreted-text
role="ref"}, when 10 products are delivered to a customer, the **Stock
Input** account is untouched because there are no new products coming
in. To put it simply:

1.  **Inventory valuation** is credited [\$120]{.title-ref}. Subtracting
    from inventory valuation represents [\$120]{.title-ref} worth of
    products exiting the company.
2.  Debit **Accounts Receivable** to record revenue from the sale.

{.align-center}

::: {.spoiler}
Understand Anglo-Saxon expensing

In the accounting journal entry invoicing a customer for 10 tables, the
accounts **Product Sales**, **Tax Received**, and **Accounts
Receivable** all pertain to the sale of the product. **Accounts
Receivable** is the account where the customer payment will be received.

Anglo-Saxon accounting recognizes the cost of goods sold (COGS) once the
sale is made. So, up until the product is sold, scrapped, or returned,
costs of keeping the product in stock are not accounted for. The
**Expense** account is debited [\$120]{.title-ref} to log the costs of
storing 10 tables during this period of time.
:::

### On product return

In the
`above example table <inventory/avg_price/price-table>`{.interpreted-text
role="ref"}, when returning 1 product to a vendor purchased at
[\$10]{.title-ref}, a company expects [\$10]{.title-ref} in the
**Accounts Payable** account from the vendor. However, **Stock Input**
account must be debited [\$12]{.title-ref} because the average cost is
[\$12]{.title-ref} at the time of the return. The missing
[\$2]{.title-ref} is accounted for in the `Price Difference
Account`{.interpreted-text role="guilabel"}, which is set up in the
product\'s `Product Category`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Behavior of *price difference accounts* varies from localization. In
this case, the account is intended to store differences between vendor
price and *automated* inventory valuation methods.
:::

Summary:

1.  Debit **Stock Input** account [\$10]{.title-ref} to move the table
    from stock to stock input. This move is to indicate that the table
    is to be processed for an outgoing shipment.
2.  Debit **Stock Input** an additional [\$2]{.title-ref} to account for
    the **Price Difference**.
3.  Credit **Stock Valuation** [\$12]{.title-ref} because the item is
    leaving the stock.

{.align-center}

Once the vendor\'s refund is received,

1.  Credit **Stock Input** account [\$10]{.title-ref} to reconcile the
    price of the table.
2.  Debit **Accounts Payable** [\$10]{.title-ref} to have the
    accountants collect and register the payment in their journal.

{.align-center}
