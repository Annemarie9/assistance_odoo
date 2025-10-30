Pricelists, discounts, and formulas
===================================

Odoo *Sales* has a useful pricelist feature that can be tailored to fit
any unique pricing strategy.

A *pricelist* is a list of prices (or price rules) that Odoo uses to
determine the appropriate price for a customer. These pricelists can be
set with specific criteria (such as time periods, minimum quantity sold,
and more) in order to apply certain prices or discounts.

Pricelists suggest certain prices, but they can always be overridden on
the sales order.

Pricing strategy options
------------------------

To choose a pricing strategy, first navigate to
`Sales app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. In the
`Pricing`{.interpreted-text role="guilabel"} section, click the checkbox
next to the `Pricelists`{.interpreted-text role="guilabel"} feature.

Doing so reveals two additional options beneath it:
`Multiple prices per product`{.interpreted-text role="guilabel"} and
`Advanced price rules (discounts, formulas)`{.interpreted-text
role="guilabel"}. A link labeled `Pricelists`{.interpreted-text
role="guilabel"} also appears, which leads to a separate pricelists
page, wherein pricelists can be created and/or modified.

-   `Multiple prices per product`{.interpreted-text role="guilabel"}:
    provides the option to set several different prices per product.
-   `Advanced price rules (discounts, formulas)`{.interpreted-text
    role="guilabel"}: provides the option to create detailed price rules
    and apply discounts, margins, and roundings.

{.align-center}

After clicking the checkbox beside the `Pricelists`{.interpreted-text
role="guilabel"} feature, select one of those two options, then click
`Save`{.interpreted-text role="guilabel"} to save all changes.

Pricelists {#sales/product_prices/pricelist}
----------

After activating and saving the `Pricelists`{.interpreted-text
role="guilabel"} feature, the `Settings`{.interpreted-text
role="guilabel"} page reloads and, from here, either select the
`Pricelists`{.interpreted-text role="guilabel"} link (beneath the
`Pricelists`{.interpreted-text role="guilabel"} feature on the
`Settings`{.interpreted-text role="guilabel"} page), or navigate to
`Sales app --> Products --> Pricelists`{.interpreted-text
role="menuselection"}.

Either option reveals the `Pricelists`{.interpreted-text
role="guilabel"} page, in which pricelists can be created and/or
modified at any time.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The order of the pricelists on the `Pricelists`{.interpreted-text
role="guilabel"} page has an impact on how they are applied. If several
pricelists share the same criteria, **only** the first listed pricelist
is applied.

For example, for two pricelists with different rules, but same criteria
(e.g., same website, same country), only the *first* pricelist in the
list is applied.
:::

::: {.note}
::: {.title}
Note
:::

The `Public Pricelist`{.interpreted-text role="guilabel"} is the default
pricelist used with Odoo *Sales* and *eCommerce*. This pricelist is
applied by default, if there are no matching criteria.
:::

::: {.note}
::: {.title}
Note
:::

In Odoo 17 (and above), it is no longer required to have a pricelist
entered in the `Pricelist`{.interpreted-text role="guilabel"} field on a
quotation form in order to confirm it (i.e. turn it into a sales order).

It should also be noted that, in Odoo 17 (and above), a chatter section
can be found on pricelist forms, which enhances the ability to
communicate about them.
:::

From the `Pricelists`{.interpreted-text role="guilabel"} page, either
select the desired pricelist to edit, or click `New`{.interpreted-text
role="guilabel"} to create a new pricelist, which reveals a blank
pricelist form that can be configured in a number of different ways.

{.align-center}

When creating a new pricelist, start by adding a name for the pricelist
at the top of the form, in the blank field. Next, select which
`Currency`{.interpreted-text role="guilabel"} should be used.

Then, if working in a multi-company environment, select which company
this pricelist should apply to in the `Company`{.interpreted-text
role="guilabel"} field. If this field is left blank, the pricelist is
automatically applied to all companies in the database.

### Price Rules tab

The `Price Rules`{.interpreted-text role="guilabel"} tab functionality
on a pricelist form varies depending on the
`Pricelists`{.interpreted-text role="guilabel"} setting chosen: either
`Multiple prices per product`{.interpreted-text role="guilabel"} or
`Advanced price rules (discounts, formulas)`{.interpreted-text
role="guilabel"}.

However, the `Time-based rules`{.interpreted-text role="guilabel"} tab
and `Configuration`{.interpreted-text role="guilabel"} tab are always
the same, regardless of the chosen `Pricelists`{.interpreted-text
role="guilabel"} setting.

#### Multiple prices per product

With the `Multiple prices per product`{.interpreted-text
role="guilabel"} setting activated, the `Price Rules`{.interpreted-text
role="guilabel"} tab on pricelist forms provides the option to add
specific products, with a specific price, to a pricelist.

To add a specific product and price to a pricelist form, click the
`Price Rules`{.interpreted-text role="guilabel"} tab, then click
`Add a line`{.interpreted-text role="guilabel"} in the
`Products`{.interpreted-text role="guilabel"} column. Then, select the
desired product for which a specific price should be applied.

Next, if necessary, select a product variant under the
`Variants`{.interpreted-text role="guilabel"} column (e.g. a specific
product size, color, etc.). If no variants are selected, then this price
will apply to all variants of the product.

If a minimum amount of the product must be purchased in order to apply
the specific price, enter the amount under the
`Min. Quantity`{.interpreted-text role="guilabel"} column.

To configure the price of the product for this specific pricelist, enter
the desired amount under the `Price`{.interpreted-text role="guilabel"}
column. Then, there is the option to add a
`Start Date`{.interpreted-text role="guilabel"} and
`End Date`{.interpreted-text role="guilabel"} to the configured product
price, if desired.

To add another product line, click `Add a line`{.interpreted-text
role="guilabel"} again, and repeat the process. There is no limit to how
many products can be added in the `Price Rules`{.interpreted-text
role="guilabel"} tab of a pricelist form.

For more information, check out the following section:
`Multiple prices per product
<sales/multiple-prices-per-product>`{.interpreted-text role="ref"}.

#### Advanced price rules

With the `Advanced price rules (discounts, formulas)`{.interpreted-text
role="guilabel"} setting activated, the `Price Rules`{.interpreted-text
role="guilabel"} tab on pricelist forms provides the option to configure
detailed price rules based on formulas.

Check out the
`Advanced price rules (discounts, formulas) <sales/advanced-price-rules>`{.interpreted-text
role="ref"} section for detailed steps on how to add advanced price
rules to a pricelist.

### Recurring Prices tab

Time-based rules are used specifically with subscription products. Be
sure to check out the Odoo
`Subscriptions </applications/sales/subscriptions>`{.interpreted-text
role="doc"} documentation for more information.

Under the `Recurring Prices`{.interpreted-text role="guilabel"} tab, the
same functionality of the `Price Rules`{.interpreted-text
role="guilabel"} tab is present. The only difference being that a
recurring time period can be applied in the
`Recurring Plan`{.interpreted-text role="guilabel"} column.

Once `Products`{.interpreted-text role="guilabel"} and/or
`Product Variants`{.interpreted-text role="guilabel"} are selected,
click `Add a
price rule`{.interpreted-text role="guilabel"}, and select the blank
field in the `Recurring Plan`{.interpreted-text role="guilabel"} column
to reveal a drop-down menu of pre-designated recurrence periods (e.g.
[Monthly]{.title-ref}, [Quarterly]{.title-ref}, [Weekly]{.title-ref},
etc.).

New recurrence periods can also be created from this column. To do so,
type in the name for the new `Recurring Plan`{.interpreted-text
role="guilabel"}, then select `Create`{.interpreted-text
role="guilabel"} from the resulting drop-down menu to create the time
period, which can be edited later.

Or, select `Create and edit...`{.interpreted-text role="guilabel"} to
reveal a `Create Recurring Plan`{.interpreted-text role="guilabel"}
pop-up form. From this pop-up form, the new recurrence period can be
configured, with specific `Details`{.interpreted-text role="guilabel"},
`Self-Service`{.interpreted-text role="guilabel"}, and
`Pricing`{.interpreted-text role="guilabel"} options. When the
configurations are complete, click the `Save & Close`{.interpreted-text
role="guilabel"} button.

{.align-center}

Lastly, add the desired price for this recurring price rule in the
`Recurring Price`{.interpreted-text role="guilabel"} column.

::: {.seealso}
`../../../subscriptions`{.interpreted-text role="doc"}
:::

### Rental rules tab

Under the `Rental rules`{.interpreted-text role="guilabel"} tab,
specific price rules can be configured for various rental products,
using the same methodology as the `Price Rules`{.interpreted-text
role="guilabel"} and `Recurring Prices`{.interpreted-text
role="guilabel"} tabs.

To add a rental rule, click `Add a line`{.interpreted-text
role="guilabel"}, and select a desired product in the
`Products`{.interpreted-text role="guilabel"} column. Then, select any
specific `Variants`{.interpreted-text role="guilabel"}, if necessary.

Next, designate a `Period`{.interpreted-text role="guilabel"} of time
for the rental rule (e.g. [Daily]{.title-ref}, [Hourly]{.title-ref},
etc.).

Lastly, configure a `Price`{.interpreted-text role="guilabel"} for the
rental rule in the respective column.

### Configuration tab

Under the `Configuration`{.interpreted-text role="guilabel"} tab, there
are a few options that can further customize the pricelist.

{.align-center}

From here, under the `Availability`{.interpreted-text role="guilabel"}
section, in the `Country Groups`{.interpreted-text role="guilabel"}
field, certain country groups can be added to the pricelist. There is no
limit to how many country groups can be added in this field.

::: {.note}
::: {.title}
Note
:::

If no country is set for a customer, Odoo takes the first pricelist
without any country group.
:::

Under the `Website`{.interpreted-text role="guilabel"} section, there
are a few options that can be configured. In the
`Website`{.interpreted-text role="guilabel"} field, this pricelist can
be applied to a specific website, if working in a multi-website
environment. If left blank, the pricelist is applied to all websites in
the database.

Tick the `Selectable`{.interpreted-text role="guilabel"} checkbox to
have this pricelist as a selectable option for customers to choose as
they shop. If the `Selectable`{.interpreted-text role="guilabel"} box is
left unticked, customers **cannot** select this pricelist for
themselves.

Lastly, there is the option to add an
`E-commerce Promotional Code`{.interpreted-text role="guilabel"}. To add
a code, type in the desired promo code that, when entered during the
checkout process, applies the pricelist to the customer, even if the
customer does not fall into the previously-specified criteria.

#### Show discount percentage to customers {#sales/products_prices/discounts}

In the `Discounts`{.interpreted-text role="guilabel"} section, there is
a `Discount Policy`{.interpreted-text role="guilabel"} label with two
radio options to choose from:
`Discount included in the price`{.interpreted-text role="guilabel"} or
`Show public price &
discount to the customer`{.interpreted-text role="guilabel"}.

If `Discount included in the price`{.interpreted-text role="guilabel"}
is selected, the price shown to the customer already accounts for the
discount being applied. However, if `Show public price & discount to the
customer`{.interpreted-text role="guilabel"} is selected, the customer
sees the actual public price *and* how much they are saving with this
pricelist discount.

Customer pricelist application
------------------------------

While the default pricelist applied to any customer is the
`Public Pricelist`{.interpreted-text role="guilabel"}, Odoo provides the
opportunity to directly apply a different pricelist to customers on
their contact form.

To do that, open the desired customer\'s contact form, either by
navigating to `Sales
app --> Orders --> Customers`{.interpreted-text role="menuselection"}
and selecting the customer from the main `Customers`{.interpreted-text
role="guilabel"} page, or by clicking on the customer\'s name on a sales
order.

{.align-center}

On the desired customer\'s contact form, under the
`Sales & Purchase`{.interpreted-text role="guilabel"} tab, in the
`Sales`{.interpreted-text role="guilabel"} section, designate what
pricelist should be applied to this specific customer from the drop-down
menu in the `Pricelist`{.interpreted-text role="guilabel"} field.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When a customer is added to the database, the default pricelist is
automatically applied to them. There is **no way** to have a blank
*Pricelist* field on a contact form. Even if that field is left blank,
the default pricelist appears when that contact form is opened again.

However, when that contact is added to a quotation, and the *Pricelist*
field is auto-populated (based on the information from their contact
form), that predetermined pricelist can be removed from the *Pricelist*
field, and the quotation can still be confirmed, and subsequently,
turned into a sales order.
:::

Multiple prices per product {#sales/multiple-prices-per-product}
---------------------------

To apply several prices per individual product, select the
`Multiple prices per product`{.interpreted-text role="guilabel"} option,
after enabling the `Pricelists`{.interpreted-text role="guilabel"}
feature on the *Sales* app setting page
(`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}), and click `Save`{.interpreted-text
role="guilabel"}.

Next, apply pricelists to specific products using the product form.
Navigate to the `Sales app --> Products --> Products`{.interpreted-text
role="menuselection"} and select the product for which multiple prices
should be applied. Selecting a product from the
`Products`{.interpreted-text role="guilabel"} page reveals that specific
product\'s product form on a separate page.

On the product form, click the `Extra Prices`{.interpreted-text
role="guilabel"} smart button, located at the top of the form.

{.align-center}

Doing so reveals a separate page displaying the
`Price Rules`{.interpreted-text role="guilabel"} that are specific to
that particular product. Here, price rules can be edited or created at
any time.

{.align-center}

To create a new price rule for a product from this specific
`Price Rules`{.interpreted-text role="guilabel"} page, click
`New`{.interpreted-text role="guilabel"} to add a new, customizable row
that has the desired product already populated in the
`Applied On`{.interpreted-text role="guilabel"} column.

Next, select which `Pricelist`{.interpreted-text role="guilabel"} this
specific product price rule should apply to, via the drop-down menu in
the `Pricelist`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

The `Public Pricelist`{.interpreted-text role="guilabel"} is the default
pricelist used with Odoo *Sales* and *eCommerce*.
:::

::: {.tip}
::: {.title}
Tip
:::

To create a new pricelist from this page, type in the desired name of
the new pricelist in the `Pricelist`{.interpreted-text role="guilabel"}
column, then select `Create`{.interpreted-text role="guilabel"} from the
drop-down menu. All pricelists can be modified at any time, by
navigating to `Sales app --> Products
--> Pricelists`{.interpreted-text role="menuselection"}. Pricelists can
also be created on that specific `Pricelists`{.interpreted-text
role="guilabel"} page, as well.
:::

After the desired pricelist is added to the row, designate a
`Min. Quantity`{.interpreted-text role="guilabel"} for the price rule.

::: {.example}
If the `Min. Quantity`{.interpreted-text role="guilabel"} column is set
to [2]{.title-ref}, the new price in the `Price`{.interpreted-text
role="guilabel"} column will be applied to orders of 2 or more products.
So, in theory, if a single product costs \$100, customers can be
encouraged to buy more, if the `Price`{.interpreted-text
role="guilabel"} is set at \$85 per product for a
`Min. Quantity`{.interpreted-text role="guilabel"} of [2]{.title-ref}
products.
:::

Next, enter the desired amount in the `Price`{.interpreted-text
role="guilabel"} column. Then, if needed, enter a
`Start Date`{.interpreted-text role="guilabel"} and
`End Date`{.interpreted-text role="guilabel"} for the product\'s price
rule.

And lastly, if working in a multi-company environment, select which
company this price rule should be applied to in the
`Company`{.interpreted-text role="guilabel"} field. Leaving this field
blank means the price rule applies for all companies in the database.

Click away from the row to activate Odoo\'s auto-save capability,
meaning that newly-created price rule is now ready to be used.

Proceed to add as many unique price rules per product as desired. There
is no limit to how many price rules can be added per product.

With the price rule(s) in place for a specific product, customers who
fall into those corresponding pricelists automatically see those new
prices applied. The number of price rules applied to a particular
product are also displayed in the `Extra Prices`{.interpreted-text
role="guilabel"} smart button, located on every product form.

::: {.note}
::: {.title}
Note
:::

When a price rule/pricelist is added to a product via the
`Extra Prices`{.interpreted-text role="guilabel"} smart button, it is
also reflected on the pricelist itself. Similarly, when a price rule for
a specific product is added to a pricelist, it is also reflected on the
product form via the `Extra
Prices`{.interpreted-text role="guilabel"} smart button.
:::

Discounts {#sales/discounts}
---------

The *Discounts* feature allows the ability to set a discount or increase
the price on *individual items* in a sales order. This is calculated as
a percentage of that product\'s sales price.

To access discounts, navigate to the *Sales* app setting page
(`Sales app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}),
and click the `Discounts`{.interpreted-text role="guilabel"} checkbox,
then click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

After the setting has been activated, navigate to the desired quotation
by going to `Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"} at the top of the page. Once there, click on the
desired quote from the list.

In the order lines section of the quotation form, a new column heading
will appear labeled `Disc.%`{.interpreted-text role="guilabel"}. This
column is used to set discounts on individual line items. Enter the
desired discount for each product line and the new price will
automatically be calculated in the quote `Total`{.interpreted-text
role="guilabel"} at the bottom of the page.

::: {.tip}
::: {.title}
Tip
:::

A discount can also be added directly to a sales order in the same way.
Navigate to `Sales app --> Orders --> Orders`{.interpreted-text
role="menuselection"}, click on the desired sales order, and add the
discount to `Disc.%`{.interpreted-text role="guilabel"} as described
above.
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Positive values for `Disc.%`{.interpreted-text role="guilabel"} will
apply a *discount*, while negative values can be used to *increase* the
price.
:::

### Discount button {#sales/pricing/discount-button}

In Odoo 17, with the
`Discounts setting <sales/discounts>`{.interpreted-text role="ref"}
enabled, a `Discount`{.interpreted-text role="guilabel"} button appears
at the bottom of sales orders.

{.align-center}

When the `Discount`{.interpreted-text role="guilabel"} button on a sales
order is clicked, a `Discount`{.interpreted-text role="guilabel"} pop-up
window appears.

On this pop-up window, configure the `Discount`{.interpreted-text
role="guilabel"} percentage, and select one of the following discount
options: `On All Order Lines`{.interpreted-text role="guilabel"},
`Global Discount`{.interpreted-text role="guilabel"}, or
`Fixed Amount`{.interpreted-text role="guilabel"}.

-   `On All Order Lines`{.interpreted-text role="guilabel"}: When
    selected, Odoo provides the ability to add the specified discount
    percentage (configured in the `Discount`{.interpreted-text
    role="guilabel"} field of the pop-up window) on all existing order
    lines of the sales order.

-   `Global Discount`{.interpreted-text role="guilabel"}: When selected,
    Odoo adds a discount product to the order, which has the cumulative
    value equivalent to the specified discount percentage (configured in
    the `Discount`{.interpreted-text role="guilabel"} field of the
    pop-up window). Any product added (or removed) *after* the discount
    is added does **not** affect the discount value on the order line.

    ::: {.example}
    In this example, since the total of the order is \$600, and there is
    a 30% global discount, that specific line is added to the sales
    order with a -180 value (which is 30% of \$600).

    {.align-center}
    :::

-   `Fixed Amount`{.interpreted-text role="guilabel"}: When selected,
    the percentage designation in the `Discount`{.interpreted-text
    role="guilabel"} field turns to a monetary value (e.g. dollars),
    wherein a specific amount must be entered. This configured value is
    added as a discount line on the sales order.

::: {.note}
::: {.title}
Note
:::

It is more beneficial to add a `Fixed Amount`{.interpreted-text
role="guilabel"} discount after **all** desired products have been added
to a sales order. If there are changes made to the sales order *after*
the discount is added, make sure to change the value on the
`Discount`{.interpreted-text role="guilabel"} line, or remove the line
and add the discount again.
:::

Advanced price rules {#sales/advanced-price-rules}
--------------------

The `Advanced price rules (discounts, formulas)`{.interpreted-text
role="guilabel"} pricelist feature provides the option to set price
change rules based on discounts and formulas. These changes can be
relative to the product list/catalog price, the product\'s cost, or
another pricelist.

To use advanced pricing rules, with discounts and formulas, select the
`Advanced price
rules (discounts, formulas)`{.interpreted-text role="guilabel"} option,
after enabling the `Pricelists`{.interpreted-text role="guilabel"}
feature on the *Sales* app setting page
(`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}), and click `Save`{.interpreted-text
role="guilabel"}.

After activating and saving that `Pricelists`{.interpreted-text
role="guilabel"} feature, the `Settings`{.interpreted-text
role="guilabel"} page reloads and, from here, either select the
`Pricelists`{.interpreted-text role="guilabel"} link (beneath the
`Pricelists`{.interpreted-text role="guilabel"} feature on the
`Settings`{.interpreted-text role="guilabel"} page), or navigate to
`Sales app --> Products --> Pricelists`{.interpreted-text
role="menuselection"}.

Either option reveals the `Pricelists`{.interpreted-text
role="guilabel"} page, in which pricelists can be created and/or
modified at any time.

From the `Pricelists`{.interpreted-text role="guilabel"} page, select a
desired pricelist to modify, or create a new pricelist by clicking the
`New`{.interpreted-text role="guilabel"} button.

On the pricelist form, under the `Price Rules`{.interpreted-text
role="guilabel"} tab, click `Add a line`{.interpreted-text
role="guilabel"} to add an advanced price rule. Doing so reveals a
`Create Pricelist Rules`{.interpreted-text role="guilabel"} pop-up form,
in which the advanced rule is configured.

{.align-center}

### Price computation

On this form, first choose one of the three
`Computation`{.interpreted-text role="guilabel"} options:

-   `Fixed Price`{.interpreted-text role="guilabel"}: the price
    computation is based on a fixed price.
-   `Discount`{.interpreted-text role="guilabel"}: the price computation
    is based on a discount.
-   `Formula`{.interpreted-text role="guilabel"}: the price computation
    is based on a formula.

::: {.note}
::: {.title}
Note
:::

Each `Computation`{.interpreted-text role="guilabel"} option reveals its
own computation-specific fields on the form.
:::

If `Fixed Price`{.interpreted-text role="guilabel"} is selected, enter
the desired price in the `Fixed Price`{.interpreted-text
role="guilabel"} field below. If `Discount`{.interpreted-text
role="guilabel"} is selected, enter the desired discount percentage in
the `Discount`{.interpreted-text role="guilabel"} field that appears.

If `Formula`{.interpreted-text role="guilabel"} is selected, a number of
configurable options appear.

{.align-center}

To configure the `Formula`{.interpreted-text role="guilabel"}
computation option, start by selecting an option from the
`Based on`{.interpreted-text role="guilabel"} field:
`Sales Price`{.interpreted-text role="guilabel"},
`Cost`{.interpreted-text role="guilabel"}, or `Other
Pricelist`{.interpreted-text role="guilabel"}. This determines what the
advanced price rule formula will be based on.

Next, in the `Discount`{.interpreted-text role="guilabel"} field,
determine how much of a discount should be applied. It should be noted
that a mark-up can be applied by setting a negative discount in this
field.

::: {.example}
To formulate a 100% markup (or 2 times the cost of the product), with a
\$5 minimum margin, set the `Based on`{.interpreted-text
role="guilabel"} field to `Cost`{.interpreted-text role="guilabel"}, the
`Discount`{.interpreted-text role="guilabel"} to [-100]{.title-ref}, and
the `Margins`{.interpreted-text role="guilabel"} to [5]{.title-ref}.
This is often seen in retail situations.

{.align-center}
:::

Then, in the `Extra Fee`{.interpreted-text role="guilabel"} field,
specify a fixed amount to add (or subtract) to the amount calculated
with the discount. After that, enter a desired figure in the
`Rounding Method`{.interpreted-text role="guilabel"} field. The rounding
method sets the price so that it is a multiple of the value in the
field.

::: {.note}
::: {.title}
Note
:::

Rounding is applied *after* the discount and *before* the surcharge.
:::

::: {.tip}
::: {.title}
Tip
:::

To have prices that end in 9.99, set the
`Rounding Method`{.interpreted-text role="guilabel"} to [10]{.title-ref}
and the `Extra Fee`{.interpreted-text role="guilabel"} to
[-0.01]{.title-ref}.
:::

Lastly, specify the minimum amount of margin over the base price in the
`Margins`{.interpreted-text role="guilabel"} field.

Once all formula-related configurations are complete, Odoo provides an
example of the formula in a blue block to the right of the
configurations.

::: {.example}
To apply 20% discounts, with prices rounded up to 9.99, set the
`Based on`{.interpreted-text role="guilabel"} field to
`Sales Price`{.interpreted-text role="guilabel"}, the
`Discount`{.interpreted-text role="guilabel"} field to [20]{.title-ref},
the `Extra Fee`{.interpreted-text role="guilabel"} field to
[-0.01]{.title-ref}, and the `Rounding Method`{.interpreted-text
role="guilabel"} field to [10]{.title-ref}.

{.align-center}
:::

### Conditions

At the bottom of the `Create Pricelist Rules`{.interpreted-text
role="guilabel"} pop-up form is the `Conditions`{.interpreted-text
role="guilabel"} section.

Here, start by selecting one of the options in the
`Apply On`{.interpreted-text role="guilabel"} field:

-   `All Products`{.interpreted-text role="guilabel"}: the advanced
    pricelist rule will be applied to all products.
-   `Product Category`{.interpreted-text role="guilabel"}: the advanced
    pricelist rule will be applied to a specific category of products.
-   `Product`{.interpreted-text role="guilabel"}: the advanced pricelist
    rule will be applied to a specific product.
-   `Product Variant`{.interpreted-text role="guilabel"}: the advanced
    pricelist rule will be applied to a specific product variant.

If any of those options, apart from `All Products`{.interpreted-text
role="guilabel"}, are selected, a new option-specific field appears, in
which the specific `Product Category`{.interpreted-text
role="guilabel"}, `Product`{.interpreted-text role="guilabel"}, or
`Product Variant`{.interpreted-text role="guilabel"} must be chosen.

Then, select a minimum quantity to be applied to the advanced pricelist
rule in the `Min.
Quantity`{.interpreted-text role="guilabel"} field. Lastly, select a
range of dates for the pricelist item validation in the
`Validity`{.interpreted-text role="guilabel"} field.

Once all configurations are complete, either click
`Save & Close`{.interpreted-text role="guilabel"} to save the advanced
pricelist rule, or click `Save & New`{.interpreted-text role="guilabel"}
to immediately create another advanced pricelist rule on a fresh form.

::: {.note}
::: {.title}
Note
:::

If a price rule is set for a particular product, and another one for its
product category, Odoo takes the rule of the product itself.
:::

::: {.seealso}
\-
`/applications/sales/sales/products_prices/prices/currencies`{.interpreted-text
role="doc"} -
`/applications/websites/ecommerce/products/price_management`{.interpreted-text
role="doc"}
:::
