# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/paypal.md

PayPal
======

 is an American online payment provider
available worldwide, and one of the few that does not charge a
subscription fee.

::: {.note}
::: {.title}
Note
:::

While PayPal is available in [over 200
countries/regions](https://www.paypal.com/webapps/mpp/country-worldwide),
only [a selection of currencies are
supported](https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies).
:::

Settings in PayPal
------------------

To access your PayPal account settings, log into PayPal, open the
`Account Settings`{.interpreted-text role="guilabel"}, and open the
`Website payments`{.interpreted-text role="guilabel"} menu.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Note that for PayPal to work **in Odoo**, the options
`Auto Return <paypal/auto-return>`{.interpreted-text role="ref"} and
`PDT <paypal/pdt>`{.interpreted-text role="ref"} **must** be enabled.
:::

### Auto Return {#paypal/auto-return}

The **Auto Return** feature automatically redirects customers to Odoo
once the payment is processed.

From `Website payments`{.interpreted-text role="guilabel"}, go to
`Website preferences --> Update --> Auto
return for website payments --> Auto return`{.interpreted-text
role="menuselection"} and select `On`{.interpreted-text
role="guilabel"}. Enter the address of your Odoo database (e.g.,
[https://yourcompany.odoo.com]{.title-ref}) in the
`Return URL`{.interpreted-text role="guilabel"} field, and
`Save`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Any URL does the job. Odoo only needs the setting to be enabled since it
uses another URL.
:::

### Payment Data Transfer (PDT) {#paypal/pdt}

`PDT (Payment Data Transfer)`{.interpreted-text role="abbr"} allows to
receive payment confirmations, displays the payment status to the
customers, and verifies the authenticity of the payments. From `Website
preferences --> Update`{.interpreted-text role="menuselection"}, scroll
down to `Payment data transfer`{.interpreted-text role="guilabel"} and
select `On`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

PayPal displays your **PDT Identity Token** as soon as
`Auto return <paypal/auto-return>`{.interpreted-text role="ref"} and
`Payment Data Transfer (PDT) <paypal/pdt>`{.interpreted-text role="ref"}
are enabled. If you need the **PDT Identity Token**, disable and
re-enable `Payment data transfer`{.interpreted-text role="guilabel"} to
display the token again.
:::

### PayPal Account Optional

We advise not to prompt customers to log in with a PayPal account upon
payment. It is better and more accessible for customers to pay with a
debit/credit card. To disable that prompt, go to
`Account Settings --> Website payments --> Update`{.interpreted-text
role="menuselection"} and select `On`{.interpreted-text role="guilabel"}
for `PayPal account optional`{.interpreted-text role="guilabel"}.

### Payment Messages Format

If you use accented characters (or anything other than primary Latin
characters) for customer names or addresses, then you **must** configure
the encoding format of the payment request sent by Odoo to PayPal. If
you do not, some transactions fail without notice.

To do so, go to [your production account
\<https://www.paypal.com/cgi-bin/customerprofileweb
?cmd=\_profile-language-encoding\>](). Then, click
`More Options`{.interpreted-text role="guilabel"} and set the two
default encoding formats as `UTF-8`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

\- For Encrypted Website Payments & EWP\_SETTINGS error, please check
the . -
Configure your
`Paypal Sandbox account <paypal/testing>`{.interpreted-text role="ref"},
then follow this

to configure the encoding format in a test environment.
:::

Settings in Odoo
----------------

::: {.seealso}
`payment_providers/add_new`{.interpreted-text role="ref"}
:::

Odoo needs your **API Credentials** to connect with your PayPal account.
To do so, go to
`Accounting --> Configuration --> Payment Providers`{.interpreted-text
role="menuselection"} and `Activate`{.interpreted-text role="guilabel"}
PayPal. Then, enter your PayPal account credentials in the
`Credentials`{.interpreted-text role="guilabel"} tab:

-   `Email`{.interpreted-text role="guilabel"}: the login email address
    in Paypal;
-   `PDT Identity Token`{.interpreted-text role="guilabel"}: the key
    used to verify the authenticity of transactions.

Test environment {#paypal/testing}
----------------

### Configuration

Thanks to PayPal sandbox accounts, you can test the entire payment flow
in Odoo.

Log into the 
using your PayPal credentials, which creates two sandbox accounts:

-   A business account (to use as merchants, e.g.,
    <pp.merch01-facilitator@example.com>);
-   A default personal account (to use as shoppers, e.g.,
    <pp.merch01-buyer@example.com>).

Log into PayPal sandbox using the merchant account and follow the same
configuration instructions. Enter your sandbox credentials in Odoo
(`Accounting --> Configuration --> Payment
Providers --> PayPal`{.interpreted-text role="menuselection"} in the
`Credentials`{.interpreted-text role="guilabel"} tab, and make sure the
status is set on `Test Mode`{.interpreted-text role="guilabel"}.

Run a test transaction from Odoo using the sandbox personal account.

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::
