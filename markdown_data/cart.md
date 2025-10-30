# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/cart.md

Add to cart
===========

The `Add to Cart`{.interpreted-text role="guilabel"} button can be
customized in multiple ways. You can:

-   Choose on which page customers go after clicking the \'Add to Cart\'
    button;
-   Hide the \'Add to Cart\' button to prevent sales;
-   Add a \'Buy Now\' button to skip the cart step and lead customers
    straight to checkout;
-   Create additional \'Add to Cart / Buy Now\' buttons;
-   Add an \'Order Again\' button to the customer portal.

::: {.seealso}
`checkout`{.interpreted-text role="doc"}
:::

\'Add to Cart\' action customization
------------------------------------

When customers click on the `Add to Cart`{.interpreted-text
role="guilabel"} button, the product is added to their cart, and
customers remain **by default** on the product\'s page. However,
customers can either immediately be **redirected** to their cart, or
given the choice on what to do through a **dialog box**.

To change the default behavior, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the
`Shop - Checkout Process`{.interpreted-text role="guilabel"} section,
look for `Add to Cart`{.interpreted-text role="guilabel"} and select one
of the options.

::: {.note}
::: {.title}
Note
:::

If a product has
`optional products <products/cross_upselling>`{.interpreted-text
role="doc"}, the **dialog box** will always appear.
:::

::: {.seealso}
`products/catalog`{.interpreted-text role="doc"}
:::

Replace \'Add to Cart\' button by \'Contact Us\' button {#cart/prevent-sale}
-------------------------------------------------------

You can replace the \'Add to Cart\' button with a \'Contact Us\' button
which redirects users to the URL of your choice.

::: {.note}
::: {.title}
Note
:::

Hiding the `Add to Cart`{.interpreted-text role="guilabel"} button is
often used by B2B eCommerces that need to restrict purchases only to
`customers with an account <checkout-sign>`{.interpreted-text
role="ref"}, but still want to display an online product catalog for
those without.
:::

To do so, go to
`Website --> Configuration --> Settings --> Shop - Products`{.interpreted-text
role="menuselection"} and tick
`Prevent Sale of Zero Priced Product`{.interpreted-text
role="guilabel"}. This creates a new `Button url`{.interpreted-text
role="guilabel"} field where you can enter the **redirect URL** to be
used. Then, set the price of the product to [0.00]{.title-ref} either
from the **product\'s template**, or from a
`pricelist </applications/sales/sales/products_prices/prices/pricing>`{.interpreted-text
role="doc"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The \'Contact Us\' button and \'*Not Available For Sale*\' text can both
be modified using the **website builder** on the product\'s page
(`Edit --> Customize`{.interpreted-text role="menuselection"}) by
clicking on them.
:::

Customizable \'Add to Cart\' button
-----------------------------------

You can also create a customizable \'Add to Cart\' button and link it to
a specific product. The **customized button** can be added on any page
of the website as an **inner content** building block, and is an
*additional* button to the regular `Add to Cart`{.interpreted-text
role="guilabel"} button.

To add it, go on the `Shop`{.interpreted-text role="guilabel"} page of
your choice, click `Edit --> Blocks`{.interpreted-text
role="menuselection"} and place the building block. Once placed, you
have the following options:

-   `Product`{.interpreted-text role="guilabel"}: select the product to
    link the button with. Selecting a product renders the
    `Action`{.interpreted-text role="guilabel"} field available;
-   `Action`{.interpreted-text role="guilabel"}: choose if the button
    should `Add to Cart`{.interpreted-text role="guilabel"} or
    `Buy Now`{.interpreted-text role="guilabel"} (instant checkout).

{.align-center}

\'Buy Now\' button {#cart/buy-now}
------------------

You can enable the \'Buy Now\' button to instantly take the customer to
**checkout** instead of adding the product to the cart. The
`Buy Now`{.interpreted-text role="guilabel"} button is an *additional*
button and does not replace the `Add to Cart`{.interpreted-text
role="guilabel"} button. To enable it, go to
`Website --> Configuration --> Settings --> Shop - Checkout Process`{.interpreted-text
role="menuselection"} and tick `Buy Now`{.interpreted-text
role="guilabel"}.

{.align-center}

Re-order from portal
--------------------

Customers have the possibility to **re-order** items from **previous
sales orders** on the customer portal. To do so, go to
`Website --> Configuration --> Settings --> Shop - Checkout
Process`{.interpreted-text role="menuselection"} and enable
`Re-order From Portal`{.interpreted-text role="guilabel"}. Customers can
find the `Order Again`{.interpreted-text role="guilabel"} button on
their **sales order** from the **customer portal**.

{.align-center}
