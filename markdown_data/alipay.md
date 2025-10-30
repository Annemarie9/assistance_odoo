# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/alipay.md

Alipay
======

 is an online payments platform
established in China by Alibaba Group.

::: {.warning}
::: {.title}
Warning
:::

The provider Alipay is deprecated. It is recommended to use
`asiapay`{.interpreted-text role="doc"} instead.
:::

Configuration
-------------

::: {.seealso}
\- `payment_providers/add_new`{.interpreted-text role="ref"}
:::

### Credentials tab

Odoo needs your **API Credentials** to connect with your Alipay account,
which comprise:

-   **Account**: Depending on where you are situated
    -   [Express Checkout]{.title-ref} if your are a Chinese Merchant.
    -   [Cross-border]{.title-ref} if you are not.
-   **Alipay Seller Email**: Your public Alipay partner email (for
    express checkout only).
-   **Merchant Partner ID**: The public partner ID solely used to
    identify the account with Alipay.
-   **MD5 Signature Key**: The signature key.

You can copy your credentials from your Alipay account, and paste them
in the related fields under the **Credentials** tab.

To retrieve them, log into your Alipay account, they are on the front
page.

::: {.important}
::: {.title}
Important
:::

If you are trying Alipay as a test, in the *sandbox*, change the
**State** to *Test Mode*. We recommend doing this on a test Odoo
database, rather than on your main database.
:::

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::
