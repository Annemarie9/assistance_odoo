# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/products/price_management.md

Price management
================

Odoo offers multiple options to select the price displayed on your
website, as well as condition-specific prices based on set criteria.

Taxes
-----

### Tax configuration

To add a tax on a product, you can either set a tax in the
`Customer Taxes`{.interpreted-text role="guilabel"} field of the
**product template** or use
`fiscal positions </applications/finance/accounting/taxes/fiscal_positions>`{.interpreted-text
role="doc"}.

::: {.seealso}
\- `/applications/finance/accounting/taxes`{.interpreted-text
role="doc"} -
`/applications/finance/accounting/taxes/avatax`{.interpreted-text
role="doc"} -
`/applications/finance/accounting/taxes/fiscal_positions`{.interpreted-text
role="doc"}
:::

### Tax display {#ecommerce-price-management-tax-display}

Choosing the displayed price tax usually depends on a country\'s
regulations or the type of customers **(B2B vs. B2C)**. To select the
type of price displayed, go to `Website -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
scroll down to the `Shop - Products`{.interpreted-text role="guilabel"}
category, and select `Tax Excluded`{.interpreted-text role="guilabel"}
or `Tax Included`{.interpreted-text role="guilabel"}.

-   `Tax Excluded`{.interpreted-text role="guilabel"}: the price
    displayed on the website is **tax-excluded**, and the tax is
    computed at the cart-review step;
-   `Tax Included`{.interpreted-text role="guilabel"}: the price
    displayed on the website is **tax-included**.

::: {.note}
::: {.title}
Note
:::

This setting is **global**, and the tax-display type is the same for
(all of) your website(s). It is, therefore, not possible to select
different tax displays for different websites. This may be a significant
point of consideration when implementing a database with multiple
ecommerce websites aimed at varying customer types (i.e., B2B and B2C).
:::

You can choose to display the type of pricing next to the product price
by going to `Website --> Site --> Homepage --> Shop`{.interpreted-text
role="menuselection"}, selecting a product, and then
`Edit --> Customize tab`{.interpreted-text role="menuselection"} and
enabling `Tax Indication`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
`/applications/finance/accounting/taxes/B2B_B2C`{.interpreted-text
role="doc"}
:::

Price per unit
--------------

It is possible to display a `price per unit
<../../../inventory_and_mrp/inventory/product_management/configure/uom>`{.interpreted-text
role="doc"} on the product page. To do that, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and enable `Product
Reference Price`{.interpreted-text role="guilabel"} under the
`Shop - Products`{.interpreted-text role="guilabel"} section. When
enabled, ensure an amount is set in the
`Base Unit Count`{.interpreted-text role="guilabel"} field of the
**product template**, and in the `Sales Price`{.interpreted-text
role="guilabel"}.

{.align-center}

The price per unit of measure can be found above the
`Add to Cart`{.interpreted-text role="guilabel"} button on the product
page.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Pay attention that having the price per unit may be **mandatory** in
some countries.
:::

::: {.seealso}
`../../../inventory_and_mrp/inventory/product_management/configure/uom`{.interpreted-text
role="doc"}
:::

### Price configuration: pricelists {#ecommerce/pricelists}

Pricelists are the primary tool to manage prices on your eCommerce. They
allow you to define website-specific prices - different from the price
on the product template - based on the **country group**, **currency**,
**minimum quantity**, **period**, or **variant**. You can create as many
pricelists as needed, but it is mandatory to have at least one pricelist
configured per website. If no custom pricelists are added, Odoo defaults
to the **Public Pricelist** for all websites.

::: {.seealso}
`/applications/sales/sales/products_prices/prices/pricing`{.interpreted-text
role="doc"}
:::

#### Configuration

Pricelists can be found under
`Website --> eCommerce --> Pricelists`{.interpreted-text
role="menuselection"}, but must first be activated. For that, head to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and scroll down to the
`Shop - Products`{.interpreted-text role="guilabel"} section. There, you
can find two options:

-   `Multiple prices per product`{.interpreted-text role="guilabel"};
-   `Advanced price rules (discounts, formulas)`{.interpreted-text
    role="guilabel"}.

The **first** option allows you to set different prices per customer
*segment*, i.e., registered customers, gold customers, regular
customers, etc. The **second** option allows you to set *price change*
rules such as **discounts**, **margins**, **roundings**, etc.

#### Foreign currency

If you are selling in **multiple currencies** and have pricelists in
foreign currencies, customers can select their corresponding pricelist
anywhere on the `Shop`{.interpreted-text role="guilabel"} page from the
drop-down menu next to the **search bar**.

{.align-center}

::: {.seealso}
\-
`/applications/sales/sales/products_prices/prices/pricing`{.interpreted-text
role="doc"} -
`/applications/sales/sales/products_prices/prices/currencies`{.interpreted-text
role="doc"}
:::

### Permanent discount

If you have permanently reduced the price of a product, a popular means
to attract customers is the **strikethrough** strategy. The strategy
consists in displaying the previous price crossed out and the **new
discounted price** next to it.

{.align-center}

To display a \'striked\' price, enable the
`Comparison Price`{.interpreted-text role="guilabel"} option under
`Website --> Configuration --> Settings --> Shop - Products category`{.interpreted-text
role="menuselection"}. Then, head to the product\'s template
(`Website --> eCommerce --> Products`{.interpreted-text
role="menuselection"}), and in the `Compare to Price`{.interpreted-text
role="guilabel"} field, enter the **new** price.
