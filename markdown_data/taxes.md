# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes.md

show-content

:   

Taxes
=====

There are numerous types of **taxes**, and their application varies
greatly, depending mostly on your company\'s localization. To make sure
they are recorded with accuracy, Odoo\'s tax engine supports all kinds
of uses and computations.

Default taxes {#taxes/default}
-------------

**Default taxes** define which taxes are automatically selected when
creating a new product. They are also used to prefill the
`Taxes`{.interpreted-text role="guilabel"} field when adding a new line
on an invoice in
`Accounting Firms <accounting/fiduciaries>`{.interpreted-text
role="ref"} mode.



To change your **default taxes**, go to
`Accounting --> Configuration --> Settings
--> Taxes --> Default Taxes`{.interpreted-text role="menuselection"},
select the appropriate taxes for your default sales tax and purchase
tax, and click on `Save`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

**Default taxes** are automatically set up according to the country
selected at the creation of your database, or when you set up a
`fiscal localization package
<fiscal_localizations/packages>`{.interpreted-text role="ref"} for your
company.
:::

Activate taxes from the list view {#taxes/list_activation}
---------------------------------

As part of your
`fiscal localization package <fiscal_localizations/packages>`{.interpreted-text
role="ref"}, most of your country\'s sales taxes are already
preconfigured on your database. However, only a few taxes are activated
by default. To activate taxes relevant to your business, go to
`Accounting
--> Configuration --> Taxes`{.interpreted-text role="menuselection"} and
enable the toggle button under the `Active`{.interpreted-text
role="guilabel"} column.



Configuration {#taxes/configuration}
-------------

To edit or create a **tax**, go to
`Accounting --> Configuration --> Taxes`{.interpreted-text
role="menuselection"} and open a tax or click on `New`{.interpreted-text
role="guilabel"}.



### Basic options

#### Tax name {#taxes/name}

The **tax name** is displayed for backend users in the
`Taxes`{.interpreted-text role="guilabel"} field in
`sales orders <../../sales/sales>`{.interpreted-text role="doc"},
`invoices <customer_invoices>`{.interpreted-text role="doc"}, product
forms, etc.

#### Tax computation {#taxes/computation}

-   **Group of Taxes**

    The tax is a combination of multiple sub-taxes. You can add as many
    taxes as you want, in the order you want them to be applied.

    ::: {.important}
    ::: {.title}
    Important
    :::

    Make sure that the tax sequence is correct, as the order in which
    they are may impact the taxes\' amounts computation, especially if
    one of the taxes `affects the base of the
    subsequent ones <taxes/base-subsequent>`{.interpreted-text
    role="ref"}.
    :::

-   **Fixed**

    The tax has a fixed amount in the default currency. The amount
    remains the same, regardless of the sales price.

::: {.example}
A product has a sales price of \$1000, and we apply a \$10 *fixed* tax.
We then have:

  -------------------------------------------------
  Product sales Price without Tax        Total
  price         tax                      
  ------------- ------------- ---------- ----------
  1,000         1,000         10         1,010.00

  -------------------------------------------------
:::

-   **Percentage of price**

    The *sales price* is the taxable basis: the tax amount is computed
    by multiplying the sales price by the tax percentage.

::: {.example}
A product has a sales price of \$1000, and we apply a *10% of Price*
tax. We then have:

  -------------------------------------------------
  Product sales Price without Tax        Total
  price         tax                      
  ------------- ------------- ---------- ----------
  1,000         1,000         100        1,100.00

  -------------------------------------------------
:::

-   **Percentage of Price Tax Included**

    The **total** is the taxable basis: the tax amount is a percentage
    of the total.

::: {.example}
A product has a Sales Price of \$1000, and we apply a *10% of Price Tax
Included* tax. We then have:

  -------------------------------------------------
  Product sales Price without Tax        Total
  price         tax                      
  ------------- ------------- ---------- ----------
  1,000         1,000         111.11     1,111.11

  -------------------------------------------------
:::

-   **Python code**

    A tax defined as **Python code** consists of two snippets of Python
    code that are executed in a local environment containing data such
    as the unit price, product or partner.
    `Python Code`{.interpreted-text role="guilabel"} defines the amount
    of the tax, and `Applicable Code`{.interpreted-text role="guilabel"}
    defines if the tax is to be applied. The formula is found at the
    bottom of the `Definition`{.interpreted-text role="guilabel"} tab.

::: {.example}
`Python Code`{.interpreted-text role="guilabel"}: [result = price\_unit
\* 0.10]{.title-ref} `Applicable Code`{.interpreted-text
role="guilabel"}: [result = true]{.title-ref}
:::

#### Active {#taxes/active}

Only **active** taxes can be added to new documents.

::: {.important}
::: {.title}
Important
:::

It is not possible to delete taxes that have already been used. Instead,
you can deactivate them to prevent future use.
:::

::: {.note}
::: {.title}
Note
:::

This field can be modified from the
`list view <taxes/list_activation>`{.interpreted-text role="ref"}.
:::

#### Tax type {#taxes/scope}

The `Tax Type`{.interpreted-text role="guilabel"} determines the tax
application, which also restricts where it is displayed.

-   **Sales**: Customer invoices, product customer taxes, etc.
-   **Purchase**: Vendor bills, product vendor taxes, etc.
-   **None**

::: {.tip}
::: {.title}
Tip
:::

You can use `None`{.interpreted-text role="guilabel"} for taxes that you
want to include in a `Group of Taxes
<taxes/computation>`{.interpreted-text role="ref"} but that you do not
want to list along with other sales or purchase taxes.
:::

#### Tax scope

The `Tax Scope`{.interpreted-text role="guilabel"} restricts the use of
taxes to a type of product, either **goods** or **services**.

### Definition tab {#taxes/definition-tab}

Allocate with precision the amount of the taxable basis or percentages
of the computed tax to multiple accounts and tax grids.



-   **Based On**:
    -   `Base`{.interpreted-text role="guilabel"}: the price on the
        invoice line
    -   `% of tax`{.interpreted-text role="guilabel"}: a percentage of
        the computed tax.
-   **Account**: if defined, an additional journal item is recorded.
-   **Tax Grids**: used to generate
    `tax reports <reporting/tax_returns>`{.interpreted-text role="doc"}
    automatically, according to your country\'s regulations.

### Advanced options tab {#taxes/advanced-tab}

#### Label on invoices {#taxes/label-invoices}

The tax label is displayed on each invoice line in the
`Taxes`{.interpreted-text role="guilabel"} column. This is visible to
*front-end* users on exported invoices, in customer portals, etc.



#### Tax group {#taxes/tax-group}

Select which **tax group** the tax belongs to. The tax group name is the
displayed above the **total** line on exported invoices and in customer
portals.

Tax groups include different iterations of the same tax. This can be
useful when you must record the same tax differently according to
`fiscal positions <taxes/fiscal_positions>`{.interpreted-text
role="doc"}.

::: {.example}


In the example above, the `0% EU S`{.interpreted-text role="guilabel"}
tax for intra-community customers in Europe records the amount on
specific accounts and tax grids. However, it remains a 0% tax to the
customer. This is why the label indicates `0% EU S`{.interpreted-text
role="guilabel"}, and the tax group name above the
`Total`{.interpreted-text role="guilabel"} line indicates
`VAT 0%`{.interpreted-text role="guilabel"}.
:::

::: {.important}
::: {.title}
Important
:::

Taxes have three different labels, each one having a specific use. Refer
to the following table to see where they are displayed.

  --------------------------------------------------------------------------------------------------------------------
  `Tax Name                         `Label on Invoice                           `Tax Group
  <taxes/name>`{.interpreted-text   <taxes/label-invoices>`{.interpreted-text   <taxes/tax-group>`{.interpreted-text
  role="ref"}                       role="ref"}                                 role="ref"}
  --------------------------------- ------------------------------------------- --------------------------------------
  Backend                           `Taxes`{.interpreted-text role="guilabel"}  Above the `Total`{.interpreted-text
                                    column on exported invoices                 role="guilabel"} line on exported
                                                                                invoices

  --------------------------------------------------------------------------------------------------------------------
:::

#### Include in analytic cost {#taxes/analytic-cost}

With this option activated, the tax amount is assigned to the same
**analytic account** as the invoice line.

#### Included in price {#taxes/included-in-price}

With this option activated, the total (including the tax) equals the
**sales price**.

[Total = Sales Price = Computed Tax-Excluded price + Tax]{.title-ref}

::: {.example}
A product has a sales price of \$1000, and we apply a *10% of Price*
tax, which is *included in the price*. We then have:

  -------------------------------------------------
  Product sales Price without Tax        Total
  price         tax                      
  ------------- ------------- ---------- ----------
  1,000         900.10        90.9       1,000.00

  -------------------------------------------------
:::

::: {.note}
::: {.title}
Note
:::

If you need to define prices accurately, both tax-included and
tax-excluded, please refer to the following documentation:
`taxes/B2B_B2C`{.interpreted-text role="doc"}.
:::

::: {.note}
::: {.title}
Note
:::

By default, only the `Tax excluded`{.interpreted-text role="guilabel"}
column is displayed on invoices. To display the
`Tax included`{.interpreted-text role="guilabel"} column, click the
**dropdown toggle** button and check `Tax incl.`{.interpreted-text
role="guilabel"}.


:::

#### Affect base of subsequent taxes {#taxes/base-subsequent}

With this option, the total tax-included becomes the taxable basis for
the other taxes applied to the same product.

You can configure a new
`group of taxes <taxes/computation>`{.interpreted-text role="ref"} to
include this tax or add it directly to a product line.



::: {.warning}
::: {.title}
Warning
:::

The order in which you add the taxes on a product line has no effect on
how amounts are computed. If you add taxes directly on a product line,
only the tax sequence determines the order in which they are applied.

To reorder the sequence, go to
`Accounting --> Configuration --> Taxes`{.interpreted-text
role="menuselection"}, and drag and drop the lines with the handles next
to the tax names.


:::

Extra taxes
-----------

\"Extra taxes\" is a broad term referring to additional taxes beyond the
standard or basic taxes imposed by governments. These extra taxes can be
**luxury** taxes, **environmental** taxes, **import** or **export
duties** taxes, etc.

::: {.note}
::: {.title}
Note
:::

The method to compute these taxes varies across different countries. We
recommend consulting your country\'s regulations to understand how to
calculate them for your business.
:::

To compute an extra tax in Odoo,
`create a tax <taxes/configuration>`{.interpreted-text role="ref"},
enter a tax name, select a
`Tax Computation <taxes/configuration>`{.interpreted-text role="ref"},
set an `Amount`{.interpreted-text role="guilabel"}, and in the
`Advanced Options`{.interpreted-text role="guilabel"} tab, check
`Affect Base of Subsequent Taxes`{.interpreted-text role="guilabel"}.
Then, drag and drop the taxes in the
`order they should be computed <taxes/base-subsequent>`{.interpreted-text
role="ref"}.

::: {.example}
\- In Belgium, the formula to compute an environmental tax is: [(product
price + environmental tax) x sales tax]{.title-ref}. Therefore, our
environmental tax has to come *before* the sales tax in the computation
sequence. - In our case, we created a 5% environmental tax (Ecotax) and
put it *before* the Belgian base tax of 21%.


:::

::: {.seealso}
\- `taxes/fiscal_positions`{.interpreted-text role="doc"} -
`taxes/B2B_B2C`{.interpreted-text role="doc"} -
`taxes/taxcloud`{.interpreted-text role="doc"} -
`reporting/tax_returns`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
taxes/cash\_basis taxes/retention taxes/vat\_verification
taxes/fiscal\_positions taxes/avatax taxes/taxcloud
taxes/eu\_distance\_selling taxes/B2B\_B2C
:::
