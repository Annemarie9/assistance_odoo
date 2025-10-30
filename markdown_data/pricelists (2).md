Pricelists
==========

Pricelists allow you to adjust product prices depending on various
criteria automatically. For example, you can set POS-specific prices,
create temporary discount periods, reward specific customers, or offer
discounts when set quantities are ordered.

Configuration {#pricelists/configuration}
-------------

Navigate to the
`general POS app settings <configuration/settings>`{.interpreted-text
role="ref"} and ensure `Flexible Pricelists`{.interpreted-text
role="guilabel"} are enabled under the `Pricing`{.interpreted-text
role="guilabel"} section.

`Multiple prices per product <pricelists/simple>`{.interpreted-text
role="ref"} is the default pricelist option for setting simple fixed
price rules per product. Select
`Advanced price rules (discounts, formulas)
<pricelists/advanced>`{.interpreted-text role="ref"} to apply price
rules to multiple products at once and to compute prices dynamically
using percentage discounts or more complex formulas in addition to
setting fixed prices.



::: {.note}
::: {.title}
Note
:::

The selected pricelist type applies to the entire database, including
the `Sales
<../../sales/products_prices/prices/pricing>`{.interpreted-text
role="doc"} and `eCommerce <ecommerce/pricelists>`{.interpreted-text
role="ref"} apps.
:::

### Create pricelists {#pricelists/create}

Go to `Point of Sale --> Products --> Pricelists`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text role="guilabel"}
or select an existing pricelist. The pricelist setup differs depending
on the `selected pricelist
option <pricelists/configuration>`{.interpreted-text role="ref"}.

#### Multiple prices per product {#pricelists/simple}

When pricelists are configured to use the
`Multiple prices per product`{.interpreted-text role="guilabel"} option,
it is possible to use multiple fixed prices for different products or
their variants depending, if necessary, on one or several conditions. To
add a new price rule to a pricelist:

1.  Click `Add a line`{.interpreted-text role="guilabel"}, and select a
    **product** and its **variant** if needed.
2.  Add the condition(s):
    -   a product quantity to be reached by using the
        `Min. Quantity`{.interpreted-text role="guilabel"} column;
    -   a determined period during which the pricelist is applied by
        using the `Start Date`{.interpreted-text role="guilabel"} and
        `End Date`{.interpreted-text role="guilabel"} columns.
3.  Add the `Price`{.interpreted-text role="guilabel"} to be applied
    when the conditions are met (if any).



#### Advanced price rules {#pricelists/advanced}

When pricelists are configured to use the
`Advanced price rules (discounts, formulas)`{.interpreted-text
role="guilabel"} option, it is possible to use percentage
discounts/mark-ups and formulas in addition to using fixed prices. To
add a new price rule to a pricelist, click
`Add a line`{.interpreted-text role="guilabel"}. In the pop-up windows:

1.  Select a `Computation`{.interpreted-text role="guilabel"} method:
    -   `Fixed Price`{.interpreted-text role="guilabel"} to set a new
        fixed price (similarly to the `Multiple prices
        per product`{.interpreted-text role="guilabel"} option).
    -   `Discount`{.interpreted-text role="guilabel"} to compute a
        percentage discount (e.g., [10.00]{.title-ref} %) or mark-up
        (e.g., [-10.00]{.title-ref} %).
    -   `Formula`{.interpreted-text role="guilabel"} to compute the
        price according to a formula. It is required to define what the
        calculation is **based on** (`Sales Price`{.interpreted-text
        role="guilabel"}, `Cost`{.interpreted-text role="guilabel"}, or
        `Other
        Pricelist`{.interpreted-text role="guilabel"}). You can then:
        -   Apply a percentage `Discount`{.interpreted-text
            role="guilabel"} or mark-up.

        -   Add an `Extra Fee`{.interpreted-text role="guilabel"} (e.g.,
            \$ [5.00]{.title-ref}) or subtract a fixed amount (e.g., \$
            [-5.00]{.title-ref}).

        -   Define a `Rounding Method <cash_rounding>`{.interpreted-text
            role="doc"} by forcing the price after
            `Discount`{.interpreted-text role="guilabel"} to be a
            multiple of the value set. The `Extra Fee`{.interpreted-text
            role="guilabel"} is applied afterward.

            ::: {.example}
            To have the final price end with [.99]{.title-ref}, set the
            `Rounding Method`{.interpreted-text role="guilabel"} to
            [1.00]{.title-ref} and the `Extra Fee`{.interpreted-text
            role="guilabel"} to [-0.01]{.title-ref}.
            :::

        -   Specify the minimum (e.g., \$ [20.00]{.title-ref} ) and
            maximum (e.g., \$ [50.00]{.title-ref} ) profit
            `Margins`{.interpreted-text role="guilabel"} for
            computations based on `Cost`{.interpreted-text
            role="guilabel"}.
2.  Select on which product(s) the price rule should be **applied**:
    -   `All Products`{.interpreted-text role="guilabel"}
    -   a `Product Category`{.interpreted-text role="guilabel"}
    -   a `Product`{.interpreted-text role="guilabel"}
    -   a `Product Variant`{.interpreted-text role="guilabel"}
3.  Add conditions, such as a specific quantity to reach for the price
    to change by using the `Min. Quantity`{.interpreted-text
    role="guilabel"} field or a specific period during which the
    pricelist should be applied by using the
    `Validity`{.interpreted-text role="guilabel"} fields.



### Select pricelists

Go to the
`specific POS settings <configuration/settings>`{.interpreted-text
role="ref"} and add all the available pricelists in the
`Available`{.interpreted-text role="guilabel"} field. Then, set its
**default pricelist** in the `Default`{.interpreted-text
role="guilabel"} field.

When you `open a POS session <pos/session-start>`{.interpreted-text
role="ref"}, click the **pricelists** button, and select the desired
pricelist from the list.



::: {.note}
::: {.title}
Note
:::

\- Multiple pricelists must be selected for the **pricelist button** to
be displayed. - If a pricelist is selected on a POS order while its
conditions are **not** met, the price will **not** be adjusted.
:::

::: {.tip}
::: {.title}
Tip
:::

You can also set a pricelist to be selected automatically once a
specific `customer is set
<pos/customers>`{.interpreted-text role="ref"}. To do so, go to the
customer form and switch to the preferred pricelist in the
`Pricelist`{.interpreted-text role="guilabel"} field of the
`Sales & Purchase`{.interpreted-text role="guilabel"} tab.
:::

::: {.seealso}
\- `../../sales/products_prices/prices/pricing`{.interpreted-text
role="doc"} -
`How to use pricelists in an ecommerce environment <ecommerce/pricelists>`{.interpreted-text
role="ref"}
:::
