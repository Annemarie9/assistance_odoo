Use eWallets and gift cards
===========================

With Odoo, customers can use **eWallets** and **gift cards** for online
and in-store shopping.

To enable eWallets and gift cards for eCommerce and Point of Sale (PoS),
first enable `Discounts, Loyalty & Gift Card`{.interpreted-text
role="guilabel"} under `Sales app --> Configuration -->
Settings --> Pricing section`{.interpreted-text role="menuselection"}.
Once enabled, go to `Sales app --> Products --> Gift
cards & eWallet`{.interpreted-text role="menuselection"} and
`Create`{.interpreted-text role="guilabel"} a new eWallet or gift card
program.

eWallets
--------

eWallets allow customers to save credits on their online account and use
these credits as a payment method when buying items in an online store
or a brick-and-mortar store. eWallets can also be used to centralize
multiple `gift cards <ewallet_gift/gift-cards>`{.interpreted-text
role="ref"}.

Before creating an eWallet program, it is necessary to create an eWallet
**top-up** product. Top-ups are pre-defined digital credit values added
to an eWallet in exchange for its equivalent in real currency. These
credits can then be used as a payment method in the eCommerce shop or
`PoS
(Point of Sale)`{.interpreted-text role="abbr"}. Top-up values can be of
different amounts.

::: {.example}
A \$50 top-up can be bought for \$50, and adds that same amount of
credits to the eWallet.
:::

To create a top-up product, go to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"} and `Create`{.interpreted-text role="guilabel"} a
new product. On the product template, configure the options as follows:

-   `Product Name`{.interpreted-text role="guilabel"}: enter a name for
    the top-up product (for example, [\$50 Top-Up]{.title-ref})
-   `Can be Sold`{.interpreted-text role="guilabel"}: enabled
-   `Product Type`{.interpreted-text role="guilabel"}: select
    `Service`{.interpreted-text role="guilabel"}
-   `Invoicing Policy`{.interpreted-text role="guilabel"}: select
    `Prepaid/Fixed Price`{.interpreted-text role="guilabel"}
-   `Create on Order`{.interpreted-text role="guilabel"}: select
    `Nothing`{.interpreted-text role="guilabel"}
-   `Sales Price`{.interpreted-text role="guilabel"}: enter the amount
    of the top-up

::: {.note}
::: {.title}
Note
:::

In order to have eWallet top-ups of different amounts, create multiple
top-up products and modify the `Sales Price`{.interpreted-text
role="guilabel"} accordingly.
:::

Once the top-up is created, go to
`Sales app --> Products --> Gift cards & eWallet`{.interpreted-text
role="menuselection"} to `Create`{.interpreted-text role="guilabel"} an
eWallet program. The following configuration options are available:

-   `Program Name`{.interpreted-text role="guilabel"}: enter a name for
    the eWallet program
-   `Program Type`{.interpreted-text role="guilabel"}: select
    `eWallet`{.interpreted-text role="guilabel"}
-   `eWallet Products`{.interpreted-text role="guilabel"}: select the
    eWallet top-up created earlier. Repeat the process if you created
    top-ups of different amounts.
-   `Email template`{.interpreted-text role="guilabel"}: select the
    email template used for the email sent to the customer. To create a
    new template, click on the field, select
    `Search More`{.interpreted-text role="guilabel"}, and then click
    `Create`{.interpreted-text role="guilabel"}.
-   `Currency`{.interpreted-text role="guilabel"}: select the currency
    to use for the eWallet program
-   `Company`{.interpreted-text role="guilabel"}: select the company for
    which the program is valid and available
-   `Available On`{.interpreted-text role="guilabel"}: select the
    applications on which the program is valid and available
-   `Website`{.interpreted-text role="guilabel"}: select the website on
    which the program is valid and available. Leave this field empty to
    include all websites.
-   `Point of Sale`{.interpreted-text role="guilabel"}: select the
    `PoS (Point of Sale)`{.interpreted-text role="abbr"} in which the
    program is valid and available. Leave this field empty to include
    all `PoS (Point of Sale)`{.interpreted-text role="abbr"}.

{.align-center}

Once the program is configured, click the
`Generate eWallet`{.interpreted-text role="guilabel"} button in the
upper-left corner to generate eWallets. eWallets can be generated based
on `Customers`{.interpreted-text role="guilabel"} and/or
`Customer Tags`{.interpreted-text role="guilabel"}. The quantity is
automatically adapted according to the `Customers`{.interpreted-text
role="guilabel"} and `Customer Tags`{.interpreted-text role="guilabel"}
selected. Then, set the `eWallet
value`{.interpreted-text role="guilabel"}. Finally, set the
`Valid Until`{.interpreted-text role="guilabel"} period if applicable.

Generated eWallets can be accessed through the
`eWallets`{.interpreted-text role="guilabel"} smart button in the
upper-right corner. From there, `Send`{.interpreted-text
role="guilabel"} or `Share`{.interpreted-text role="guilabel"} the
eWallets via email or a URL link.

{.align-center}

Click on an eWallet to change the `Expiration Date`{.interpreted-text
role="guilabel"}, `Partner`{.interpreted-text role="guilabel"}, or
`Balance`{.interpreted-text role="guilabel"}. The
`Code`{.interpreted-text role="guilabel"} of an eWallet *cannot* be
changed, deleted, or duplicated.

Gift cards {#ewallet_gift/gift-cards}
----------

Gift cards can be purchased by customers, and in turn used as a payment
method upon checkout at an eCommerce shop or
`PoS (Point of Sale)`{.interpreted-text role="abbr"}.

Before creating a new gift card program, it is necessary to first create
gift cards as products. To do so, go to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"} and `Create`{.interpreted-text role="guilabel"} a
product. On the product template, configure the options as follows:

-   `Product Name`{.interpreted-text role="guilabel"}: enter a name for
    the gift card product
-   `Can be Sold`{.interpreted-text role="guilabel"}: enabled
-   `Product Type`{.interpreted-text role="guilabel"}: select
    `Service`{.interpreted-text role="guilabel"}
-   `Invoicing Policy`{.interpreted-text role="guilabel"}: select
    `Prepaid/Fixed Price`{.interpreted-text role="guilabel"}
-   `Create on Order`{.interpreted-text role="guilabel"}: select
    `Nothing`{.interpreted-text role="guilabel"}
-   `Sales Price`{.interpreted-text role="guilabel"}: enter the amount
    of the gift card

::: {.note}
::: {.title}
Note
:::

In order to have gift cards of different amounts, create multiple gift
card products and modify the `Sales Price`{.interpreted-text
role="guilabel"} accordingly.
:::

Once the gift card product is created, go to
`Sales app --> Products --> Gift cards
& eWallet`{.interpreted-text role="menuselection"} to
`Create`{.interpreted-text role="guilabel"} a gift card program. The
following configuration options are available:

-   `Program Name`{.interpreted-text role="guilabel"}: enter a name for
    the gift card program
-   `Program Type`{.interpreted-text role="guilabel"}: select
    `Gift Card`{.interpreted-text role="guilabel"}
-   `Gift Card Products`{.interpreted-text role="guilabel"}: select the
    gift card product created earlier. Repeat the process if you created
    gift card products of different amounts.
-   `Email template`{.interpreted-text role="guilabel"}: select the
    default `Gift Card: Gift Card Information`{.interpreted-text
    role="guilabel"} template, or create a new template by clicking on
    the field, selecting `Search More`{.interpreted-text
    role="guilabel"}, and then clicking `Create`{.interpreted-text
    role="guilabel"}.
-   `Print Report`{.interpreted-text role="guilabel"}: select
    `Gift Card`{.interpreted-text role="guilabel"}
-   `Currency`{.interpreted-text role="guilabel"}: select the currency
    to use for the gift card program
-   `Company`{.interpreted-text role="guilabel"}: select the company for
    which the program is valid and available
-   `Available On`{.interpreted-text role="guilabel"}: select the
    applications on which the program is valid and available
-   `Website`{.interpreted-text role="guilabel"}: select the website on
    which the program is valid and available. Leave this field empty to
    include all websites.
-   `Point of Sale`{.interpreted-text role="guilabel"}: select the
    `PoS (Point of Sale)`{.interpreted-text role="abbr"} in which the
    program is valid and available. Leave this field empty to include
    all `PoS (Point of Sale)`{.interpreted-text role="abbr"}.

{.align-center}

Once the program is configured, click the
`Generate Gift Cards`{.interpreted-text role="guilabel"} button in the
upper-left corner to generate gift cards. Gift cards can be generated
either for `Anonymous
Customers`{.interpreted-text role="guilabel"} or
`Selected Customers`{.interpreted-text role="guilabel"}. Set the
`Quantity to generate`{.interpreted-text role="guilabel"} for
`Anonymous Customers`{.interpreted-text role="guilabel"}, or select the
`Customers`{.interpreted-text role="guilabel"} and/or `Customer
Tags`{.interpreted-text role="guilabel"} for
`Selected Customers`{.interpreted-text role="guilabel"}. Then, set the
`Gift Card value`{.interpreted-text role="guilabel"}. Finally, set the
`Valid Until`{.interpreted-text role="guilabel"} period if applicable.

Generated gift cards can be accessed through the
`Gift Cards`{.interpreted-text role="guilabel"} smart button in the
upper-right corner. From there, `Send`{.interpreted-text
role="guilabel"} or `Share`{.interpreted-text role="guilabel"} the gift
cards via email or a URL link.

{.align-center}

Click on a gift card to change the `Expiration Date`{.interpreted-text
role="guilabel"}, `Partner`{.interpreted-text role="guilabel"}, or
`Balance`{.interpreted-text role="guilabel"}. The
`Code`{.interpreted-text role="guilabel"} of a gift card *cannot* be
changed, deleted, or duplicated.
