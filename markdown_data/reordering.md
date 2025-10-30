# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/products/reordering.md

Configure reordering rules
==========================

For certain products, it is necessary to ensure that there is always a
minimum amount available on hand at any given time. By adding a
reordering rule to a product, it is possible to automate the reordering
process so that a purchase order is automatically created whenever the
amount on hand falls below a set threshold.

::: {.important}
::: {.title}
Important
:::

The *Inventory* module must be installed to use reordering rules.
:::

Configure products for reordering
---------------------------------

Products must be configured in a specific way before a reordering rule
can be added to them.

Starting from the `Inventory`{.interpreted-text role="menuselection"},
`Manufacturing`{.interpreted-text role="menuselection"},
`Purchase`{.interpreted-text role="menuselection"}, or
`Sales`{.interpreted-text role="menuselection"} module, navigate to
`Products
--> Products`{.interpreted-text role="menuselection"} and then click
`Create`{.interpreted-text role="guilabel"} to make a new product.
Alternatively, find a product that already exists in the database and
click into it\'s product form.

Next, on the product form, enable reordering by checking the
`Can be Purchased`{.interpreted-text role="guilabel"} option underneathe
the `Product Name`{.interpreted-text role="guilabel"} field. Finally,
set the `Product Type`{.interpreted-text role="guilabel"} to [Storable
Product]{.title-ref} under the `General Information`{.interpreted-text
role="guilabel"} tab.

{.align-center}

Add a reordering rule to a product
----------------------------------

After properly configuring a product, a reordering rule can be added to
it by selecting the now visible `Reordering Rules`{.interpreted-text
role="guilabel"} tab at the top of that product\'s form, and then
clicking `Create`{.interpreted-text role="guilabel"} on the
`Reordering Rules`{.interpreted-text role="guilabel"} dashboard.

{.align-center}

Once created, the reordering rule can be configured to generate purchase
orders automatically by defining the following fields:

-   `Location`{.interpreted-text role="guilabel"} specifies where the
    ordered quantities should be stored once they are received and
    entered into stock.

-   `Min Quantity`{.interpreted-text role="guilabel"} sets the lower
    threshold for the reordering rule while `Max
    Quantity`{.interpreted-text role="guilabel"} sets the upper
    threshold. If the stock on hand falls below the minimum quantity, a
    new purchase order will be created to replenish it up to the maximum
    quantity.

    > ::: {.example}
    > If `Min Quantity`{.interpreted-text role="guilabel"} is set to
    > [5]{.title-ref} and `Max Quantity`{.interpreted-text
    > role="guilabel"} is set to [25]{.title-ref} and the stock on hand
    > falls to four, a purchase order will be created for 21 units of
    > the product.
    > :::

-   `Multiple Quantity`{.interpreted-text role="guilabel"} can be
    configured so that products are only ordered in batches of a certain
    quantity. Depending on the number entered, this can result in the
    creation of a purchase order that would put the resulting stock on
    hand above what is specified in the `Max
    Quantity`{.interpreted-text role="guilabel"} field.

    > ::: {.example}
    > If `Max Quantity`{.interpreted-text role="guilabel"} is set to
    > [100]{.title-ref} but `Multiple Quantity`{.interpreted-text
    > role="guilabel"} is set to order the product in batches of
    > [200]{.title-ref}, a purchase order will be created for 200 units
    > of the product.
    > :::

-   `UoM`{.interpreted-text role="guilabel"} specifies the unit of
    measurement by which the quantity will be ordered. For discrete
    products, this should be set to [Units]{.title-ref}. However, it can
    also be set to units of measurement like [Volume]{.title-ref} or
    [Weight]{.title-ref} for non-discrete products like water or bricks.

{.align-center}

Manually trigger reordering rules using the scheduler
-----------------------------------------------------

Reordering rules will be automatically triggered by the scheduler, which
runs once a day by default. To trigger reordering rules manually,
navigate to `Inventory --> Operations
--> Run Scheduler`{.interpreted-text role="menuselection"}. On the
pop-up window, confirm the manual action by clicking `Run
Scheduler`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Manually triggering reordering rules will also trigger any other
scheduled actions.
:::

Manage reordering rules
-----------------------

To manage the reordering rules for a single product, navigate to that
product page\'s form and select the `Reordering Rules`{.interpreted-text
role="guilabel"} tab at the top of the form.

To manage all reordering rules for every product, go to
`Inventory --> Configuration
--> Reordering Rules`{.interpreted-text role="menuselection"}. From this
dashboard, typical bulk actions in Odoo can be performed such as
exporting data or archiving rules that are no longer needed. As well,
the `Filters`{.interpreted-text role="guilabel"},
`Group By`{.interpreted-text role="guilabel"} or triple-dotted menu on
the form are available to search for and/or organize the reordering
rules as desired.
