Subscriptions in the eCommerce shop
===================================

Subscription products can be sold in the Odoo *eCommerce* shop just like
regular sales products.

However, by default, the eCommerce product page **only** displays the
shortest recurrence period listed in the
`Recurring Prices`{.interpreted-text role="guilabel"} tab of the product
form.

For example, if a subscription product has *monthly* and *annaul*
recurrence periods configured, then *only* the monthly price appears on
the eCommerce page for that product, by default.

To add more recurrence periods to the eCommerce product page, create a
*product variant* for each recurrence period.

::: {.seealso}
\-
`Configure subscription products </applications/sales/subscriptions>`{.interpreted-text
role="doc"} -
`Product variants </applications/sales/sales/products_prices/products/variants>`{.interpreted-text
role="doc"}
:::

Create recurrence periods as product variants
---------------------------------------------

To set up each recurrence period as a product variant, go to
`Subscriptions app -->
Products --> Products`{.interpreted-text role="menuselection"}, and
select a product. In the `Attributes & Variants`{.interpreted-text
role="guilabel"} tab, click `Add a line`{.interpreted-text
role="guilabel"}.

Then proceed to create an `Attribute`{.interpreted-text role="guilabel"}
called [Billing Period]{.title-ref} (or something similar), by typing in
the name, and clicking `Create`{.interpreted-text role="guilabel"} from
the mini drop-down menu that appears. This attribute name appears as
option heading on the product page of the eCommerce shop.

Next, create `Values`{.interpreted-text role="guilabel"} that correspond
to the recurrence periods that are configured in the
`Recurring Prices`{.interpreted-text role="guilabel"} tab of the product
form.

To do that, type in the name of the recurrence period in the
`Values`{.interpreted-text role="guilabel"} column, on the same
`Attribute`{.interpreted-text role="guilabel"} line, in the
`Attributes & Variants`{.interpreted-text role="guilabel"} tab. Then,
click `Create`{.interpreted-text role="guilabel"} from the mini
drop-down menu that appears.

These value names appear as selectable options on the product page of
the eCommerce shop.

![Recurrence periods configured as product variants in the \"Attributes & Variants\" tab of
the product form.](ecommerce/recurrence-period-attributes-variants.png){.align-center}

With those configurations in place and saved, a
`Product Variants`{.interpreted-text role="guilabel"} column appears in
the `Recurring Prices`{.interpreted-text role="guilabel"} tab. Proceed
to assign the different `Product Variants`{.interpreted-text
role="guilabel"} to their corresponding recurrence
`Period`{.interpreted-text role="guilabel"} and
`Price`{.interpreted-text role="guilabel"}.

{.align-center}

After following those aforementioned steps, the product variants are
available for selection on the eCommerce product page.

{.align-center}
