# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md

Automatic inventory valuation
=============================

All of a company\'s stock on-hand contributes to the valuation of its
inventory. That value should be reflected in the company\'s accounting
records to accurately show the value of the company and all of its
assets.

By default, Odoo uses a periodic inventory valuation (also known as
manual inventory valuation). This method implies that the accounting
team manually posts journal entries, based on the physical inventory of
the company, and warehouse employees take the time to count the stock.
In Odoo, each product category reflects this, with the
`Costing Method`{.interpreted-text role="guilabel"} set to `Standard
Price`{.interpreted-text role="guilabel"}, and the
`Inventory Valuation`{.interpreted-text role="guilabel"} (not visible by
default) set to `Manual`{.interpreted-text role="guilabel"}.

{.align-center}

Alternatively, perpetual (automatic) inventory valuation creates
real-time *journal entries* in the *Accounting* app whenever stock
enters or leaves the company\'s warehouse.

This document is focused on the proper setup of automatic inventory
valuation, which is an integrated valuation method that ensures journal
entries in the *Accounting* app match stock valuation updates in the
*Inventory* app. For an introduction of inventory valuation in Odoo,
refer to the `using_inventory_valuation`{.interpreted-text role="doc"}
documentation.

::: {.warning}
::: {.title}
Warning
:::

Switching from manual to automatic inventory valuation may cause
discrepancies between stock valuation and accounting journals.

One  for switching to
automated valuation:

1.  Clear existing stock (possibly with an `inventory adjustment
    <../../warehouses_storage/inventory_management/count_products>`{.interpreted-text
    role="doc"})
2.  Change the inventory valuation method to *Automatic*
3.  Return the existing stock, with the original monetary value (using
    an inventory adjustment)

Once the existing stock is recovered, the Odoo *Accounting* app
automatically generates the journal entries to corresponding stock
valuation records.
:::

Configuration
-------------

To properly set up automatic inventory valuation, follow these steps in
Odoo:

1.  `Install Accounting app and enable specific settings
    <inventory/warehouses_storage/accounting-setup>`{.interpreted-text
    role="ref"}
2.  `Set Automatic inventory valuation on product categories
    <inventory/warehouses_storage/valuation-on-product-category>`{.interpreted-text
    role="ref"}
3.  `Set costing method <inventory/warehouses_storage/costing_methods>`{.interpreted-text
    role="ref"}

### Accounting setup {#inventory/warehouses_storage/accounting-setup}

To use automatic inventory valuation, install the *Accounting* app.
Next, go to
`Accounting app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and in the `Stock
Valuation`{.interpreted-text role="guilabel"} section, tick the
`Automatic Accounting`{.interpreted-text role="guilabel"} checkbox.
Then, click `Save`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Enabling `Automatic Accounting`{.interpreted-text role="guilabel"} shows
the previously invisible *Inventory Valuation* field on a product
category.
:::

{.align-center}

Refer to the
`Expense <inventory/warehouses_storage/expense-account>`{.interpreted-text
role="ref"} and `Stock
input/output <inventory/warehouses_storage/stock-account>`{.interpreted-text
role="ref"} sections of documentation for details on configuring the
accounting journals shown.

### Product category setup {#inventory/warehouses_storage/valuation-on-product-category}

After
`enabling inventory valuation <inventory/warehouses_storage/accounting-setup>`{.interpreted-text
role="ref"}, the next step is to set the product category to use
automatic inventory valuation.

Go to
`Inventory app --> Configuration --> Product Categories`{.interpreted-text
role="menuselection"}, and select the desired product category. In the
`Inventory Valuation`{.interpreted-text role="guilabel"} section, set
the `Inventory Valuation`{.interpreted-text role="guilabel"} field to
`Automated`{.interpreted-text role="guilabel"}. Repeat this step for
every product category intending to use automatic inventory valuation.

::: {.note}
::: {.title}
Note
:::

After enabling automatic accounting, each new stock move layer (SVL),
that is created during inventory valuation updates, generates a journal
entry.
:::

{.align-center}

Costing method {#inventory/warehouses_storage/costing_methods}
--------------

After
`enabling inventory valuation <inventory/warehouses_storage/accounting-setup>`{.interpreted-text
role="ref"}, the *costing method* for calculating and recording
inventory costs is defined on the product category in Odoo.

Go to
`Inventory app --> Configuration --> Product Categories`{.interpreted-text
role="menuselection"} and select the desired product category. In the
`Inventory Valuation`{.interpreted-text role="guilabel"} section, select
the appropriate `Costing Method`{.interpreted-text role="guilabel"}:

::: {.tabs}
::: {.tab}
Standard Price

The default costing method in Odoo. The cost of the product is manually
defined on the product form, and this cost is used to compute the
valuation. Even if the purchase price on a purchase order differs, the
valuation is the cost defined on the product form.

  Operation                          Unit Cost   Qty On Hand   Incoming Value   Inventory Value
  ---------------------------------- ----------- ------------- ---------------- -----------------
                                     \$10        0                              \$0
  Receive 8 products for \$10/unit   \$10        8             8 \* \$10        \$80
  Receive 4 products for \$16/unit   \$10        12            4 \* \$10        \$120
  Deliver 10 products                \$10        2             -10 \* \$10      \$20
  Receive 2 products for \$9/unit    \$10        4             2 \* \$10        \$40
:::

::: {.tab}
Average Cost (AVCO)

Calculates the valuation of a product based on the average cost of that
product, divided by the total number of available stock on-hand. With
this costing method, inventory valuation is *dynamic*, and constantly
adjusts based on the purchase price of products.

  Operation                          Unit Cost   Qty On Hand   Incoming Value   Inventory Value
  ---------------------------------- ----------- ------------- ---------------- -----------------
                                     \$0         0                              \$0
  Receive 8 products for \$10/unit   \$10        8             8 \* \$10        \$80
  Receive 4 products for \$16/unit   \$12        12            4 \* \$16        \$144
  Deliver 10 products                \$12        2             -10 \* \$12      \$24
  Receive 2 products for \$6/unit    \$9         4             2 \* \$6         \$36

How are unit cost and inventory value calculated at each step?

-   When receiving four products for \$16 each:
    -   Inventory value is calculated by adding the previous inventory
        value with the incoming value: $$80 + (4 * $16) = $144$.
    -   Unit cost is calculated by dividing the inventory value by the
        quantity on-hand: $$144 / 12 = $12$.
-   When delivering ten products, the average unit cost is used to
    calculate the inventory value, regardless of the purchase price of
    the product. Therefore, inventory value is
    $$144 + (-10 * $12) = $24$.
-   Receive two products for \$6 each:
    -   Inventory value: $$24 + (2 * $6) = $36$
    -   Unit cost: $$36 / 4 = $9$

::: {.note}
::: {.title}
Note
:::

When choosing `Average Cost (AVCO)`{.interpreted-text role="guilabel"}
as the `Costing Method`{.interpreted-text role="guilabel"}, changing the
numerical value in the *Cost* field for products in the respective
product category creates a new record in the *Inventory Valuation*
report to adjust the value of the product. The *Cost* amount is then
automatically updated, based on the average purchase price of both the
inventory on-hand and the costs accumulated from validated purchase
orders.
:::
:::

::: {.tab}
First In First Out (FIFO)

Tracks the costs of incoming and outgoing items in real-time, and uses
the real price of the products to change the valuation. The oldest
purchase price is used as the cost for the next good sold, until an
entire lot of that product is sold. When the next inventory lot moves up
in the queue, an updated product cost is used based on the valuation of
that specific lot.

This method is arguably the most accurate inventory valuation method for
a variety of reasons, but it is highly sensitive to input data and human
error.

+-------------+-----------+-------------+-------------+-------------+
| Operation   | Unit Cost | Qty On Hand | Incoming    | Inventory   |
|             |           |             | Value       | Value       |
+=============+===========+=============+=============+=============+
|             | \$0       | 0           |             | \$0         |
+-------------+-----------+-------------+-------------+-------------+
| Receive 8   | \$10      | 8           | 8 \* \$10   | \$80        |
| products    |           |             |             |             |
| for         |           |             |             |             |
| \$10/unit   |           |             |             |             |
+-------------+-----------+-------------+-------------+-------------+
| Receive 4   | \$12      | 12          | 4 \* \$16   | \$144       |
| products    |           |             |             |             |
| for         |           |             |             |             |
| \$16/unit   |           |             |             |             |
+-------------+-----------+-------------+-------------+-------------+
| Deliver 10  | \$16      | 2           | | -8 \*     | \$32        |
| products    |           |             |   \$10      |             |
|             |           |             | | -2 \*     |             |
|             |           |             |   \$16      |             |
+-------------+-----------+-------------+-------------+-------------+
| Receive 2   | \$11      | 4           | 2 \* \$6    | \$44        |
| products    |           |             |             |             |
| for         |           |             |             |             |
| \$6/unit    |           |             |             |             |
+-------------+-----------+-------------+-------------+-------------+

How are unit cost and inventory value calculated at each step?

-   When receiving four products for \$16 each:

    -   Inventory value is calculated by adding the previous inventory
        value to the incoming value: $$80 + (4 * $16) = $144$.
    -   Unit cost is calculated by dividing the inventory value by the
        quantity on-hand: $$144 / 12 = $12$.

    > -   When delivering ten products, eight units were purchased for
    >     \$10, and two units were purchased for \$16.

    -   First, the incoming value is calculated by multiplying the
        on-hand quantity by the purchased price:
        $(-8 * $10) + (-2 * $16) = -112$.
    -   The inventory value is calculated by subtracting the incoming
        value from the previous inventory value: $$144 - $112 = $32$.
    -   Unit cost is calculated by dividing the inventory value by the
        remaining quantity: $$32 / 2 = $16$.

-   When receiving two products for \$6, inventory value is
    $$32 + $12 = $44$. Unit cost is $$44 / 4 = $11$.
:::
:::

::: {.warning}
::: {.title}
Warning
:::

Changing the costing method greatly impacts inventory valuation. It is
highly recommended to consult an accountant first before making any
adjustments here.
:::

::: {.seealso}
`using_inventory_valuation`{.interpreted-text role="doc"}
:::

When the `Costing Method`{.interpreted-text role="guilabel"} is changed,
products already in stock that were using the
`Standard`{.interpreted-text role="guilabel"} costing method **do not**
change value; rather, the existing units keep their value, and any
product moves from then on affect the average cost, and the cost of the
product will change. If the value in the `Cost`{.interpreted-text
role="guilabel"} field on a product form is changed manually, Odoo
generates a corresponding record in the *Inventory Valuation* report.

::: {.note}
::: {.title}
Note
:::

It is possible to use different valuation settings for different product
categories.
:::

Types of accounting {#inventory/warehouses_storage/accounting-types}
-------------------

With automated inventory valuation set up, the generated journal entries
depend on the chosen accounting mode: *Continental* or *Anglo-Saxon*.

::: {.tip}
::: {.title}
Tip
:::

Verify the accounting mode by activating the
`developer-mode`{.interpreted-text role="ref"}, and navigating to
`Accounting app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

Then, in the `Search...`{.interpreted-text role="guilabel"} bar, look
for [Anglo-Saxon Accounting]{.title-ref}, to see if the feature is
enabled. If it is **not** enabled, *Continental* accounting mode is in
use.

{.align-center}
:::

In *Anglo-Saxon* accounting, the costs of goods sold (COGS) are reported
when products are sold or delivered. This means the cost of a good is
only recorded as an expense when a customer is invoiced for a product.

So, for **manual** valuation method, set the *Expense Account* to *Stock
Valuation* for the current asset type; for **automatic** valuation
method, set the *Expense Account* to an *Expenses* or a *Cost of
Revenue* type (e.g. *Cost of Production*, *Cost of Goods Sold*, etc.).

In *Continental* accounting, the cost of a good is reported as soon as a
product is received into stock. Because of this, the *Expense Account*
can be set to **either** *Expenses* or a *Cost of Revenue* type,
however, it is more commonly set to an *Expenses* account.

Refer to the
`Expense <inventory/warehouses_storage/expense-account>`{.interpreted-text
role="ref"} and `Stock
input/output <inventory/warehouses_storage/stock-account>`{.interpreted-text
role="ref"} sections for details on configuring each account type.

### Expense account {#inventory/warehouses_storage/expense-account}

To configure the *expense account*, which is used in both manual and
automatic inventory valuation, go to the
`Account Properties`{.interpreted-text role="guilabel"} section of the
intended product category
(`Inventory app --> Configuration --> Product Categories`{.interpreted-text
role="menuselection"}). Then, choose an existing account from the
`Expense Account`{.interpreted-text role="guilabel"} drop-down menu.

To ensure the chosen account is the correct `Type,`{.interpreted-text
role="guilabel"} click the `fa-arrow-right`{.interpreted-text
role="icon"} `(right arrow)`{.interpreted-text role="guilabel"} icon to
the right of the account. Then, set the account type based on the
information below.

::: {.tabs}
::: {.group-tab}
Anglo-Saxon

::: {.tabs}
::: {.group-tab}
Automated

In Anglo-Saxon accounting for automated inventory valuation, set the
`Expense
Account`{.interpreted-text role="guilabel"} to the
[Expenses]{.title-ref} account. Then, click the
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon to the right of
the account.

In the pop-up window, choose `Expenses`{.interpreted-text
role="guilabel"} or `Cost of Revenue`{.interpreted-text role="guilabel"}
from the `Type`{.interpreted-text role="guilabel"} drop-down menu.

{.align-center}
:::

::: {.group-tab}
Manual

To configure the `Expense Account`{.interpreted-text role="guilabel"},
choose `Stock Valuation`{.interpreted-text role="guilabel"} from the
field\'s drop-down menu. Verify the account\'s type by clicking the
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon, and then ensure
the `Type`{.interpreted-text role="guilabel"} is
`Current Assets`{.interpreted-text role="guilabel"}.

{.align-center}
:::
:::
:::

::: {.group-tab}
Continental

::: {.tabs}
::: {.group-tab}
Automated

Set the `Expense Account`{.interpreted-text role="guilabel"} to the
`Expenses`{.interpreted-text role="guilabel"} or `Cost of
Revenue`{.interpreted-text role="guilabel"} account type.
:::

::: {.group-tab}
Manual

Set the `Expense Account`{.interpreted-text role="guilabel"} to the
`Expenses`{.interpreted-text role="guilabel"} or `Cost of
Revenue`{.interpreted-text role="guilabel"} account type.
:::
:::
:::
:::

#### Stock input/output (automated only) {#inventory/warehouses_storage/stock-account}

To configure the `Stock Input Account`{.interpreted-text
role="guilabel"} and `Stock Output Account`{.interpreted-text
role="guilabel"}, go to
`Inventory app --> Configuration --> Product Categories`{.interpreted-text
role="menuselection"} and select the desired product category.

In the `Inventory Valuation`{.interpreted-text role="guilabel"} field,
select `Automated`{.interpreted-text role="guilabel"}. Doing so makes
the `Account Stock Properties`{.interpreted-text role="guilabel"}
section appear. These accounts are defined as follows:

-   `Stock Valuation Account`{.interpreted-text role="guilabel"}: when
    automated inventory valuation is enabled on a product, this account
    will hold the current value of the products.
-   `Stock Journal`{.interpreted-text role="guilabel"}: accounting
    journal where entries are automatically posted when a product\'s
    inventory valuation changes.
-   `Stock Input Account`{.interpreted-text role="guilabel"}:
    counterpart journal items for all incoming stock moves will be
    posted in this account, unless there is a specific valuation account
    set on the source location. This is the default value for all
    products in a given category, and can also be set directly on each
    product.
-   `Stock Output Account`{.interpreted-text role="guilabel"}:
    counterpart journal items for all outgoing stock moves will be
    posted in this account, unless there is a specific valuation account
    set on the destination location. This is the default value for all
    products in a given category, and can also be set directly on each
    product.

::: {.tabs}
::: {.group-tab}
Anglo-Saxon

In Anglo-Saxon accounting, the `Stock Input Account`{.interpreted-text
role="guilabel"} and `Stock Output
Account`{.interpreted-text role="guilabel"} are set to *different*
`Current Assets`{.interpreted-text role="guilabel"} accounts. This way,
delivering products and invoicing the customer balance the *Stock
Output* account, while receiving products and billing vendors balance
the *Stock Input* account.

To modify the account type, go to the click the
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon to the right of
the stock input/output account. In the pop-up window, choose
`Current Assets`{.interpreted-text role="guilabel"} from the
`Type`{.interpreted-text role="guilabel"} drop-down menu.

![The *Stock Input* account is set to [Stock Interim
(Received)]{.title-ref}, a *Current Asset* account
type.](inventory_valuation_config/account-type.png){.align-center}
:::

::: {.group-tab}
Continental

In Continental accounting, the `Stock Input Account`{.interpreted-text
role="guilabel"} and `Stock Output
Account`{.interpreted-text role="guilabel"} are set to **the same**
`Current Assets`{.interpreted-text role="guilabel"} account. That way,
one account can be balanced when items are bought and sold.

::: {.example}
The stock input and output accounts are both set to [Stock Interim
(Received)]{.title-ref}, a `Current Assets`{.interpreted-text
role="guilabel"} account type. They can also be set to the [Stock
Interim (Delivered)]{.title-ref}, as long as the input and output
accounts are assigned to the **same** account.

{.align-center}
:::
:::
:::

Inventory valuation reporting
-----------------------------

To start, go to
`Accounting app --> Reporting --> Balance Sheet`{.interpreted-text
role="menuselection"}. Click the `Current Assets`{.interpreted-text
role="guilabel"} line item to unfold the drop-down menu, and look for
the nested `Stock Valuation`{.interpreted-text role="guilabel"},
`Stock Interim (Received)`{.interpreted-text role="guilabel"}, and
`Stock Interim
(Delivered)`{.interpreted-text role="guilabel"} lines.

::: {.tip}
::: {.title}
Tip
:::

At the top of the dashboard, click the `As of [date]`{.interpreted-text
role="guilabel"} button to display accounting records up to a specified
date.
:::

::: {.seealso}
\-
`Stock accounts and what they do <inventory/warehouses_storage/stock-account>`{.interpreted-text
role="ref"} -
`../../../../finance/accounting/get_started/cheat_sheet`{.interpreted-text
role="doc"}
:::

{.align-center}

Access more specific information by clicking the
`fa-ellipsis-v`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} icon to the right of the
desired journal. Select `General Ledger`{.interpreted-text
role="guilabel"} to see a list of all of the journal entries, where each
line item\'s `fa-ellipsis-v`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} icon can be clicked to
reveal the `View Journal Entry`{.interpreted-text role="guilabel"}
option to open the individualized journal entry.

Additionally, annotations to the `Balance Sheet`{.interpreted-text
role="guilabel"} can be added by choosing `Annotate`{.interpreted-text
role="guilabel"}, filling in the text box, and clicking
`Save`{.interpreted-text role="guilabel"}.

{.align-center}
