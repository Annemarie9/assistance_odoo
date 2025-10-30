# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/buckaroo.md

Buckaroo
========

 is a Dutch-based company that
offers several online payment possibilities.

Configuration on Buckaroo Plaza {#payment_providers/buckaroo/configure_dashboard}
-------------------------------

1.  Log into , go to
    `My Buckaroo -->
    Websites`{.interpreted-text role="menuselection"} and select the
    `Push settings`{.interpreted-text role="guilabel"} tab.
2.  Tick the `Enable Push Response`{.interpreted-text role="guilabel"}
    check box in the `Delayed and Push responses`{.interpreted-text
    role="guilabel"} section.
3.  Enter the URL of your Odoo database, followed by
    [/payment/buckaroo/webhook]{.title-ref} in both the
    `Push URI Success/Pending`{.interpreted-text role="guilabel"} and
    `Push URI Failure`{.interpreted-text role="guilabel"} text fields.
    For example:
    [https://yourcompany.odoo.com/payment/buckaroo/webhook]{.title-ref}.
4.  Leave the other fields as they are and click
    `Save`{.interpreted-text role="guilabel"}.
5.  In the `General`{.interpreted-text role="guilabel"} tab, copy the
    website `Key`{.interpreted-text role="guilabel"} (i.e., the key used
    to uniquely identify your website with Buckaroo) and save it for
    later.
6.  Go to `Configuration --> Security --> Secret key`{.interpreted-text
    role="menuselection"}, enter or `Generate`{.interpreted-text
    role="guilabel"} a `Secret key`{.interpreted-text role="guilabel"}
    and click `Save`{.interpreted-text role="guilabel"}. Save the key
    for later.

Configuration on Odoo
---------------------

1.  `Navigate to the payment provider Buckaroo <payment_providers/add_new>`{.interpreted-text
    role="ref"} and change its state to `Enabled`{.interpreted-text
    role="guilabel"}.
2.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill
    the `Website Key`{.interpreted-text role="guilabel"} and
    `Secret Key`{.interpreted-text role="guilabel"} fields with the
    values you saved at the step
    `payment_providers/buckaroo/configure_dashboard`{.interpreted-text
    role="ref"}.
3.  Configure the options in the other tabs to your liking.

::: {.seealso}
`../payment_providers`{.interpreted-text role="doc"}
:::
