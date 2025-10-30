# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/checkout.md

Checkout
========

You can customize the **checkout steps**, add more content using the
**website builder**, and enable additional features such as **express
checkout** and **sign in/up at checkout**.

You can use **building blocks** to add content at any step of the
checkout process. To do so, from any **checkout page**, go to
`Edit --> Blocks`{.interpreted-text role="menuselection"}, and drag and
drop **building blocks** to the page.

::: {.note}
::: {.title}
Note
:::

Note that content added through building blocks is **specific** to each
step.
:::

Checkout steps
--------------

### Review order: promo code (and subtotal)

If you have enabled `Discounts, Loyalty, & Gift Card`{.interpreted-text
role="guilabel"} in the settings
(`Website --> Configuration --> Settings --> Shop - Products`{.interpreted-text
role="menuselection"}), you can enable the
`Promo Code`{.interpreted-text role="guilabel"} field
(`Edit --> Customize`{.interpreted-text role="menuselection"}) from any
checkout page. Customers can then redeem gift cards and promotional
codes at the `Review Order`{.interpreted-text role="guilabel"} step.

Furthermore, you can display the subtotal with discounts applied by
enabling `Show
Discount in Subtotal`{.interpreted-text role="guilabel"}.

{.align-center}

### Address: B2B fields

Optional `TIN/VAT`{.interpreted-text role="guilabel"} and
`Company Name`{.interpreted-text role="guilabel"} fields can be added to
the `Billing Address`{.interpreted-text role="guilabel"} form for B2B
customers, at the `Address`{.interpreted-text role="guilabel"} step. To
add the fields, go to `Edit --> Customize`{.interpreted-text
role="menuselection"} from any checkout page, and enable
`Show B2B fields`{.interpreted-text role="guilabel"}.

### Request extra info (additional step)

You can request `Extra Info`{.interpreted-text role="guilabel"} from the
customer by adding an `Extra Info`{.interpreted-text role="guilabel"}
step between the `Address`{.interpreted-text role="guilabel"} and
`Confirm Order`{.interpreted-text role="guilabel"} steps. To do so, go
to `Edit --> Customize`{.interpreted-text role="menuselection"} from any
checkout page, and enable `Extra Step
Option`{.interpreted-text role="guilabel"}.

{.align-center}

The `Extra Info`{.interpreted-text role="guilabel"} step is an online
form linked to the quotation or sales order of the customer. The
information added during that step can be found on the quotation or
sales order of the customer from the back end, in the **Sales** app.

When enabled, you can remove, add, and modify fields of the form by
clicking on `Edit`{.interpreted-text role="guilabel"} in the top-right
corner, and then clicking on any of the form\'s fields. All
customization options, as well as the `+ Field`{.interpreted-text
role="guilabel"} button to add new fields, are available at the bottom
of the `Customize`{.interpreted-text role="guilabel"} menu under the
`Field`{.interpreted-text role="guilabel"} section.

{.align-center}

### Confirm order: terms and conditions

You can ask customers to agree to the
`Terms & Conditions`{.interpreted-text role="guilabel"} in order to
confirm their order by enabling
`Accept Terms & Conditions`{.interpreted-text role="guilabel"} under
`Edit --> Customize`{.interpreted-text role="menuselection"} on any
checkout page.

{.align-center}

Express checkout
----------------

You can enable a `Buy Now`{.interpreted-text role="guilabel"} button on
products\' pages which instantly takes the customer to the
`Confirm Order`{.interpreted-text role="guilabel"} checkout page,
instead of adding the product to the cart. To do so, go to
`Website --> Configuration --> Settings --> Shop - Checkout Process section`{.interpreted-text
role="menuselection"} and tick `Buy Now`{.interpreted-text
role="guilabel"}. Alternatively, the `Buy Now`{.interpreted-text
role="guilabel"} button can also be enabled from any product\'s page by
going `Edit --> Customize`{.interpreted-text role="menuselection"}, in
the `Cart`{.interpreted-text role="guilabel"} section.

The button can be found next to the `Add to Cart`{.interpreted-text
role="guilabel"} button on the product\'s page.

{.align-center}

Guest and signed-in checkout {#checkout-sign}
----------------------------

It is possible to introduce a **checkout policy** under which customers
can either checkout as **guests** or **signed-in users only**. Customers
can also checkout as guest, and **optionally sign up later** in order to
track their order, if enabled.

To select a policy, go to
`Website --> Configuration --> Settings --> Shop - Checkout
Process`{.interpreted-text role="menuselection"}. You can choose
between:

-   `Optional`{.interpreted-text role="guilabel"}: allows guests to
    checkout and later register from the **order confirmation** email to
    track their order;
-   `Disabled (buy as guest)`{.interpreted-text role="guilabel"}:
    customers can only checkout as guests;
-   `Mandatory (no guest checkout)`{.interpreted-text role="guilabel"}:
    customers can only checkout if they have signed-in.

::: {.seealso}
\- `customer_accounts`{.interpreted-text role="doc"} -
`/applications/general/users/portal`{.interpreted-text role="doc"}
:::

### B2B access restriction

If you wish to restrict checkout only to **selected B2B customers**,
enable `Mandatory (no
guest checkout)`{.interpreted-text role="guilabel"} and go to
`Website --> eCommerce --> Customers`{.interpreted-text
role="menuselection"}. Select the customer you wish to **grant access
to**, click `Action --> Grant portal access`{.interpreted-text
role="menuselection"}, and click `Grant Access`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Settings are **website-specific**, which means you can set up a B2C
website allowing **guest** checkout, and another for B2B customers with
**mandatory sign-in**.
:::

::: {.note}
::: {.title}
Note
:::

Users can only have one portal access per **email**. They *cannot* be
granted access to two different portals with the same **email address**.
:::

### Shared customer accounts

If you enable `Shared Customer Accounts`{.interpreted-text
role="guilabel"} under `Website --> Configuration
--> Settings --> Privacy section`{.interpreted-text
role="menuselection"}, you can allow or disallow access to *all*
websites for one same account.
