# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/ogone.md

Ogone
=====

, also known as **Ingenico Payment
Services** is a France-based company that provides the technology
involved in secure electronic transactions.

::: {.seealso}
\- `payment_providers/add_new`{.interpreted-text role="ref"} - [Ogone\'s
documentation](https://epayments-support.ingenico.com/get-started/).
:::

::: {.warning}
::: {.title}
Warning
:::

The provider Ogone is deprecated. It is recommended to use
`stripe`{.interpreted-text role="doc"} instead.
:::

Settings in Ogone
-----------------

### Create an API user

Log into your Ogone account and head to the
`Configuration`{.interpreted-text role="guilabel"} tab.

You need to create an **API user** to be used in the creation of
transactions from Odoo. While you can use your main account to do so,
using an **API user** ensures that if the credentials used in Odoo are
leaked, no access to your Ogone configuration is possible. Additionally,
passwords for **API users** do not need to be updated regularly, unlike
normal users.

To create an **API user**, go to
`Configuration --> Users`{.interpreted-text role="menuselection"} and
click on `New User`{.interpreted-text role="guilabel"}. The following
fields must be configured:

::: {#ogone/ogone}
-   `UserID`{.interpreted-text role="guilabel"}: you can choose anything
    you want.
-   `User's Name, E-mail and Timezone`{.interpreted-text
    role="guilabel"}: you can enter the information you want.
-   `Profile`{.interpreted-text role="guilabel"}: should be set to
    `Admin`{.interpreted-text role="guilabel"}.
-   `Special user for API`{.interpreted-text role="guilabel"}: should be
    checked.
:::

After the creation of the user, you are required to generate a password.
Save the password and **UserID**, as they will be required later on
during the setup.

::: {.tip}
::: {.title}
Tip
:::

If you already have an user set up, make sure it is activated without
any error. If not, simply click the `Activate(Errors)`{.interpreted-text
role="guilabel"} button to reset the user.
:::

### Set up Ogone for Odoo

Ogone must now be configured to accept payments from Odoo. Head to
`Configuration -->
Technical Information --> Global Security Parameters`{.interpreted-text
role="menuselection"}, select `SHA-512`{.interpreted-text
role="guilabel"} as `Hash Algorithm`{.interpreted-text role="guilabel"}
and `UTF-8`{.interpreted-text role="guilabel"} as
`character encoding`{.interpreted-text role="guilabel"}. Then, go to the
`Data and Origin verification`{.interpreted-text role="guilabel"} tab of
the same page and leave the URL field of the
`e-Commerce and Alias Gateway`{.interpreted-text role="guilabel"}
section blank.

::: {.tip}
::: {.title}
Tip
:::

If you need to use another algorithm, such as [sha-1]{.title-ref} or
[sha-256]{.title-ref}, within Odoo, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"} and go
to the **Payment Providers** page in
`Accounting --> Configuration --> Payment Providers`{.interpreted-text
role="menuselection"}. Click on `Ogone`{.interpreted-text
role="guilabel"}, and in the `Credentials`{.interpreted-text
role="guilabel"} tab, select the algorithm you wish to use in the
`Hash function`{.interpreted-text role="guilabel"} field.
:::

You are now required to generate **SHA-IN** passphrases. **SHA-IN** and
**SHA-OUT** passphrases are used to digitally sign the transaction
requests and responses between Odoo and Ogone. By using these secret
passphrases and the [sha-1]{.title-ref} algorithm, both systems can
ensure that the information they receive from the other was not altered
or tampered with.

Enter the same **SHA-IN** passphrase in both
`Checks for e-Commerce & Alias Gateway`{.interpreted-text
role="guilabel"} and
`Checks for DirectLink and Batch (Automatic)`{.interpreted-text
role="guilabel"}. You can leave the IP address field blank.

Your **SHA-IN** and **SHA-OUT** passphrases should be different, and
between 16 and 32 characters long. Make sure to use the same **SHA-IN**
and **SHA-OUT** passphrases throughout the entire Ogone configuration,
as Odoo only allows a single **SHA-IN** and single **SHA-OUT**
passphrase.

In order to retrieve the **SHA-OUT** key, log into your Ogone account,
go to
`Configuration --> Technical Information --> Transaction feedback --> All
transaction submission modes`{.interpreted-text role="menuselection"},
and get or generate your **API Key** and **Client Key**. Be careful to
copy your API key as you'll not be allowed to get it later without
generating a new one.

When done, head to
`Configuration --> Technical Information --> Transaction Feedback`{.interpreted-text
role="menuselection"} and check the following options:

-   The `URL`{.interpreted-text role="guilabel"} fields for
    `HTTP redirection in the browser`{.interpreted-text role="guilabel"}
    can be left empty, as Odoo will specify these URLs for every
    transaction request.
-   `I would like to receive transaction feedback parameters on the redirection URLs`{.interpreted-text
    role="guilabel"}: should be checked.
-   `Direct HTTP server-to-server request`{.interpreted-text
    role="guilabel"}: should to be set to [Online but switch to a
    deferred request when the online request fails]{.title-ref}.
-   Both **URL** fields should contain the same following URL, with
    [\<example\>]{.title-ref} replaced by your database:
    [https://\<example\>/payment/ogone/return]{.title-ref}.
-   `Dynamic eCommerce Parameters`{.interpreted-text role="guilabel"}
    should contain the following values: [ALIAS]{.title-ref},
    [AMOUNT]{.title-ref}, [CARDNO]{.title-ref}, [CN]{.title-ref},
    [CURRENCY]{.title-ref}, [IP]{.title-ref}, [NCERROR]{.title-ref}
    [ORDERID]{.title-ref}, [PAYID]{.title-ref}, [PM]{.title-ref},
    [STATUS]{.title-ref}, [TRXDATE]{.title-ref}. Other parameters can be
    included (if you have another integration with Ogone that requires
    them), but are not advised.
-   In the `All transaction submission modes`{.interpreted-text
    role="guilabel"} section, fill out **SHA-OUT** passphrase and
    disable [HTTP request for status change]{.title-ref}.

To allow your customers to save their credit card credentials for future
use, head to
`Configuration --> Alias --> My alias information`{.interpreted-text
role="menuselection"}. From this tab, you can configure how the user can
have its card details saved, for how long the information is saved, if a
checkbox to save the card information should be displayed, etc.

Settings in Odoo
----------------

To set up Ogone in Odoo, head to
`Accounting --> Configuration --> Payment Providers`{.interpreted-text
role="menuselection"} and open the Ogone provider. In the
`Credentials`{.interpreted-text role="guilabel"} tab, enter the
**PSPID** of your Ogone account, and fill out the other fields as
configured in your `Ogone portal <ogone/ogone>`{.interpreted-text
role="ref"}.
