# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/silverfin.md

Silverfin integration
=====================

 is a third-party service provider
that offers a cloud platform for accountants.

Odoo and Silverfin provide an integration to automate the
synchronization of data.

Configuration
-------------

To configure this integration, you need to input the following data into
your Silverfin account:

-   user\'s email address
-   `Odoo API key <silverfin/api-key>`{.interpreted-text role="ref"}
-   URL of the Odoo database
-   name of your Odoo database

### Odoo API key {#silverfin/api-key}

You can create Odoo external API keys either
`for a single database <silverfin/api-singledb>`{.interpreted-text
role="ref"} (hosting: Odoo Online, On-premise, and Odoo.sh) or
`for all databases managed by a single user
<silverfin/api-multipledb>`{.interpreted-text role="ref"} (hosting: Odoo
Online).

::: {.important}
::: {.title}
Important
:::

\- These API keys are personal and provide full access to your user
account. Store it securely. - You can copy the API key only at its
creation. It is not possible to retrieve it later. - If you need it
again, create a new API key (and delete the old one).
:::

::: {.seealso}
`/developer/reference/external_api`{.interpreted-text role="doc"}
:::

#### Per database {#silverfin/api-singledb}

To add an API key to a **single** database, connect to the database,
enable the `developer
mode <developer-mode>`{.interpreted-text role="ref"}, click on the user
menu, and then `My Profile`{.interpreted-text role="guilabel"} /
`Preferences`{.interpreted-text role="guilabel"}. Under the
`Account Security`{.interpreted-text role="guilabel"} tab, click on
`New API
Key`{.interpreted-text role="guilabel"}, confirm your password, give a
descriptive name to your new key, and copy the API key.



::: {.seealso}
`api/external_api/keys`{.interpreted-text role="ref"}
:::

#### For all databases (fiduciaries) {#silverfin/api-multipledb}

To add an API key to **all** databases managed by a single user at the
same time **(the easiest method for fiduciaries)**, navigate to [Odoo\'s
website](https://www.odoo.com) and sign in with your administrator
account. Next, open [your account security settings in developer
mode](https://www.odoo.com/my/security?debug=1), click on
`New API Key`{.interpreted-text role="guilabel"}, confirm your password,
give a descriptive name to your new key, and copy the new API key.

::: {.tip}
::: {.title}
Tip
:::

Open the  to view
all databases that will be linked to the single API key.
:::


