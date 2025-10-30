Discount and loyalty programs
=============================

The Odoo *Sales*, *eCommerce*, and *Point of Sale* applications allow
users to create discount and loyalty programs that customers can use for
online and in-store shopping. These programs offer more varied, public,
and time-sensitive pricing options than `pricelists
</applications/sales/sales/products_prices/prices/pricing>`{.interpreted-text
role="doc"}.

Configure the settings
----------------------

To begin using discount and loyalty programs, navigate to
`Sales --> Configuration
--> Settings`{.interpreted-text role="menuselection"}. Under the
`Pricing`{.interpreted-text role="guilabel"} heading, activate the
`Discounts, Loyalty &
Gift Card`{.interpreted-text role="guilabel"} setting by checking the
box next to the feature. Finally, click `Save`{.interpreted-text
role="guilabel"} to save the changes.

Configure discount and loyalty programs
---------------------------------------

To create discount and loyalty programs, go to
`Sales --> Products --> Discount &
Loyalty`{.interpreted-text role="menuselection"}.

If no discount or loyalty programs have been created yet, Odoo provides
a choice of templates to help create the first program. Choose one of
the template cards, or click `New`{.interpreted-text role="guilabel"} to
create a new program from scratch.

Or, if there are already existing programs, select an existing program
to edit it.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Templates **only** appear when no programs have been created, and they
disappear once the first program is created.
:::

Creating or editing a program opens the program form.

{.align-center}

The program form contains the following fields:

-   `Program Name`{.interpreted-text role="guilabel"}: Enter the name of
    the program in this field. The program name is **not** visible to
    the customer.
-   `Program Type`{.interpreted-text role="guilabel"}: Select the
    desired `program type
    <sales/pricing_management/program-types>`{.interpreted-text
    role="ref"} from the drop-down menu.
-   `Currency`{.interpreted-text role="guilabel"}: Select the currency
    used for the program.
-   `Pricelist`{.interpreted-text role="guilabel"}: If desired, select a
    pricelist from the drop-down menu to have this loyalty program
    applied to a specific pricelist (and customers attached to the
    pricelist). More than one pricelist can be selected in this field.
    When a single loyalty program is linked to several pricelists, it
    makes it viable for different customer segments to have different
    pricelists, but the *same* loyalty programs. If this field is left
    blank, the program applies to everyone, regardless of pricelist.
-   `Points Unit`{.interpreted-text role="guilabel"}: Enter the name of
    the points used for the `Loyalty Cards`{.interpreted-text
    role="guilabel"} program (e.g. [Loyalty Points]{.title-ref}). The
    points unit name *is* visible to the customer. This field is
    **only** available when the `Program Type`{.interpreted-text
    role="guilabel"} is set to `Loyalty Cards`{.interpreted-text
    role="guilabel"}.
-   `Start Date`{.interpreted-text role="guilabel"}: Select the date on
    which the program becomes valid. Leave this field blank if the
    program should always be valid and not expire.
-   `End Date`{.interpreted-text role="guilabel"}: Select the date on
    which the program stops being valid. Leave this field blank if the
    program should always be valid and not expire.
-   `Limit Usage`{.interpreted-text role="guilabel"}: If desired, tick
    this checkbox, and enter a number of `usages`{.interpreted-text
    role="guilabel"} to limit the number of times the program can be
    used during the validity period.
-   `Company`{.interpreted-text role="guilabel"}: If working in a
    multi-company database, choose the one company for which the program
    is available. If left blank, the program is available to all
    companies in the database.
-   `Available On`{.interpreted-text role="guilabel"}: Select the apps
    on which the program is available.
-   `Website`{.interpreted-text role="guilabel"}: Select a website on
    which the program is available. Leave this field blank to make it
    available on all websites.
-   `Point of Sale`{.interpreted-text role="guilabel"}: Select the
    point(s) of sale at which the program is available. Leave this field
    blank to make it available at all
    `PoS (Point of Sale)`{.interpreted-text role="abbr"}.

::: {.note}
::: {.title}
Note
:::

The options available on the program form vary depending on the
`Program Type
<sales/pricing_management/program-types>`{.interpreted-text role="ref"}
selected.
:::

All of the existing cards, codes, coupons, etc. that have been generated
for the program are accessible through the smart button located at the
top of the form.

{.align-center}

::: {.note}
::: {.title}
Note
:::

In Odoo 17 (and later), when a loyalty card or coupon is associated with
a contact in the database, a `Loyalty Cards`{.interpreted-text
role="guilabel"} smart button conditionally appears on the contact form.

{.align-center}

This smart button **only** appears if a loyalty card or coupon is
associated with the contact.
:::

### Program types {#sales/pricing_management/program-types}

The different `Program Types`{.interpreted-text role="guilabel"}
available on the program form are:

-   `Coupons`{.interpreted-text role="guilabel"}: Generate and share
    single-use coupon codes that grant immediate access to rewards.
-   `Loyalty Cards`{.interpreted-text role="guilabel"}: When making
    purchases, the customer accumulates points to exchange for rewards
    on current and/or future orders.
-   `Promotions`{.interpreted-text role="guilabel"}: Set conditional
    rules for ordering products, which, when fulfilled, grant access to
    rewards for the customer.
-   `Discount Code`{.interpreted-text role="guilabel"}: Set codes which,
    when entered upon checkout, grant discounts to the customer.
-   `Buy X Get Y`{.interpreted-text role="guilabel"}: for every (X) item
    bought, the customer is granted 1 credit. After accumulating a
    specified amount of credits, the customer can trade them in to
    receive (Y) item.
-   `Next Order Coupons`{.interpreted-text role="guilabel"}: Generate
    and share single-use coupon codes that grant access to rewards on
    the customer\'s next order.

### Conditional rules

Next, configure the `Conditional rules`{.interpreted-text
role="guilabel"} that determine when the program applies to a
customer\'s order.

In the `Rules & Rewards`{.interpreted-text role="guilabel"} tab, click
`Add`{.interpreted-text role="guilabel"} next to
`Conditional rules`{.interpreted-text role="guilabel"} to add
*conditions* to the program. This reveals a
`Create Conditional rules`{.interpreted-text role="guilabel"} pop-up
window.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The options for `Conditional rules`{.interpreted-text role="guilabel"}
vary depending on the selected `Program Type
<sales/pricing_management/program-types>`{.interpreted-text role="ref"}.
:::

The following options are available for configuring conditional rules:

-   `Discount Code`{.interpreted-text role="guilabel"}: Enter a custom
    code to be used for the `Discount Code`{.interpreted-text
    role="guilabel"} program, or use the default one generated by Odoo.
    This field is only available when the
    `Program Type`{.interpreted-text role="guilabel"} is set to
    `Discount Code`{.interpreted-text role="guilabel"}.
-   `Minimum Quantity`{.interpreted-text role="guilabel"}: Enter the
    minimum number of products that must be purchased in order to access
    the reward. Set the minimum quantity to at least [1]{.title-ref} to
    ensure that the customer must make a purchase in order to access the
    reward.
-   `Minimum Purchase`{.interpreted-text role="guilabel"}: Enter the
    minimum amount (in currency), with `tax
    Included`{.interpreted-text role="guilabel"} or
    `tax Excluded`{.interpreted-text role="guilabel"}, that must be
    spent in order to access the reward. If both a minimum quantity
    *and* minimum purchase amount are entered, then the customer\'s
    order must meet both conditions.
-   `Products`{.interpreted-text role="guilabel"}: Select the specific
    product(s) for which the program applies. Leave this field blank to
    apply it to all products.
-   `Categories`{.interpreted-text role="guilabel"}: Select the category
    of products for which the program applies. Choose
    `All`{.interpreted-text role="guilabel"} to apply it to all product
    categories.
-   `Product Tag:`{.interpreted-text role="guilabel"} Select a tag to
    apply the program to products with that specific tag.
-   `Grant`{.interpreted-text role="guilabel"}: Enter the number of
    points the customer earns `per order`{.interpreted-text
    role="guilabel"}, `per currency spent`{.interpreted-text
    role="guilabel"}, or `per unit paid`{.interpreted-text
    role="guilabel"} (for the `Loyalty Cards`{.interpreted-text
    role="guilabel"} and `Buy X Get Y`{.interpreted-text
    role="guilabel"} programs).

{.align-center}

Click `Save & Close`{.interpreted-text role="guilabel"} to save the rule
and close the pop-up window, or click `Save & New`{.interpreted-text
role="guilabel"} to save the rule and immediately create a new one.

### Rewards

In the `Rules & Rewards`{.interpreted-text role="guilabel"} tab of the
program form, click `Add`{.interpreted-text role="guilabel"} next to
`Rewards`{.interpreted-text role="guilabel"} to add *rewards* to the
program. This reveals a `Create Rewards`{.interpreted-text
role="guilabel"} pop-up window.

::: {.note}
::: {.title}
Note
:::

The options for `Rewards`{.interpreted-text role="guilabel"} vary
depending on the selected `Program Type
<sales/pricing_management/program-types>`{.interpreted-text role="ref"}.
:::

The following options are available for configuring rewards:

-   `Reward Type`{.interpreted-text role="guilabel"}: Select the reward
    type among `Free Product`{.interpreted-text role="guilabel"},
    `Discount`{.interpreted-text role="guilabel"}, and
    `Free Shipping`{.interpreted-text role="guilabel"}. The other
    options for reward configuration depend on the
    `Reward Type`{.interpreted-text role="guilabel"} selected.
    -   `Free Product`{.interpreted-text role="guilabel"}:
        -   `Quantity Rewarded`{.interpreted-text role="guilabel"}:
            Select the number of free products rewarded to the customer.
        -   `Product`{.interpreted-text role="guilabel"}: Select the
            product given for free as a reward. Only one product can be
            selected.
        -   `Product Tag`{.interpreted-text role="guilabel"}: Select a
            tag to further specify the free product eligible for the
            reward.
    -   `Discount`{.interpreted-text role="guilabel"}:
        -   `Discount`{.interpreted-text role="guilabel"}: Enter the
            discounted amount in either `percentage`{.interpreted-text
            role="guilabel"}, `currency per point`{.interpreted-text
            role="guilabel"}, or `currency per order`{.interpreted-text
            role="guilabel"}. Then, select whether the discount applies
            to the entire `Order`{.interpreted-text role="guilabel"},
            only the `Cheapest Product`{.interpreted-text
            role="guilabel"} on the order, or only
            `Specific Products`{.interpreted-text role="guilabel"}.
        -   `Max Discount`{.interpreted-text role="guilabel"}: Enter the
            maximum amount (in currency) that this reward may grant as a
            discount. Leave this field at [0]{.title-ref} for no limit.
    -   `Free Shipping`{.interpreted-text role="guilabel"}:
        -   `Max Discount`{.interpreted-text role="guilabel"}: Enter the
            maximum amount (in currency) that this reward may grant as a
            discount. Leave this field at [0]{.title-ref} for no limit.
-   `In exchange of`{.interpreted-text role="guilabel"}: Enter the
    number of points required to exchange for the reward (for the
    `Loyalty Cards`{.interpreted-text role="guilabel"} and
    `Buy X Get Y`{.interpreted-text role="guilabel"} programs).
-   `Description on order`{.interpreted-text role="guilabel"}: Enter the
    description of the reward, which is displayed to the customer upon
    checkout.

{.align-center}
