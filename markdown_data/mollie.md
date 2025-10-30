# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/mollie.md

Mollie
======

 is an online payments platform
established in the Netherlands.

Configuration
-------------

::: {.seealso}
\- `payment_providers/add_new`{.interpreted-text role="ref"}
:::

### Credentials tab

Odoo needs your **API Credentials** to connect with your Mollie account,
which comprise:

-   **API Key**: The test or live API Key depending on the configuration
    of the provider.

You can copy your credentials from your Mollie account, and paste them
in the related fields under the **Credentials** tab.

To retrieve your API key, log into your Mollie account, go to
`Developers --> API keys`{.interpreted-text role="menuselection"}, and
copy your Test or Live **API Key**.

::: {.important}
::: {.title}
Important
:::

If you are trying Mollie as a test, with the Test API key, change the
**State** to *Test Mode*. We recommend doing this on a test Odoo
database, rather than on your main database.
:::

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::
