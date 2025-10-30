# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/asiapay.md

AsiaPay
=======

 is an online payments provider
established in Hong Kong and covering several Asian countries and
payment methods.

Configuration on AsiaPay Dashboard {#payment_providers/asiapay/configure_dashboard}
----------------------------------

1.  Log into AsiaPay Dashboard according to the account provided by
    AsiaPay.
    -   :
        For markets in HK, CN, MO, TW, SG, MY, IN, VN, NZ and AU
    -   :
        For market in PH
    -   :
        For market in TH
    -   :
        For market in ID

2.  Go to `Profile --> Account Information`{.interpreted-text
    role="menuselection"}. Copy the values of the
    `Currency`{.interpreted-text role="guilabel"} and
    `Secure Hash`{.interpreted-text role="guilabel"} fields and save
    them for later.

3.  | Go to `Profile --> Payment Account Settings`{.interpreted-text
      role="menuselection"} and enable the option
      `Return Value Link (Datefeed)`{.interpreted-text role="guilabel"};
    | Enter your Odoo database URL followed by
      [/payment/asiapay/webhook]{.title-ref} in the
      `Return Value Link (Datefeed)`{.interpreted-text role="guilabel"}
      text field. For example:
      [https://yourcompany.odoo.com/payment/asiapay/webhook]{.title-ref};
    | Click on `Test`{.interpreted-text role="guilabel"} to check if the
      webhook is working correctly.

4.  Click on `Update`{.interpreted-text role="guilabel"} to finalize the
    configuration.

Configuration on Odoo {#payment_providers/asiapay/configure_odoo}
---------------------

1.  `Navigate to the payment provider AsiaPay <payment_providers/add_new>`{.interpreted-text
    role="ref"} and change its state to `Enabled`{.interpreted-text
    role="guilabel"}.

2.  | In the `Credentials`{.interpreted-text role="guilabel"} tab,
      choose the `Brand`{.interpreted-text role="guilabel"} of your
      Asiapay account. Then fill in the `Merchant ID`{.interpreted-text
      role="guilabel"} and `Secure Hash Secret`{.interpreted-text
      role="guilabel"}, and the `Currency`{.interpreted-text
      role="guilabel"} in the `Configuration`{.interpreted-text
      role="guilabel"} tab with the values you saved at the step
      `payment_providers/asiapay/configure_dashboard`{.interpreted-text
      role="ref"};
    | By default, the payment provider AsiaPay is configured to verify
      the secret hash with the hash function [SHA1]{.title-ref}. If a
      different function is
      `set on your account  <payment_providers/asiapay/configure_dashboard>`{.interpreted-text
      role="ref"}, activate the
      `developer mode  <developer-mode>`{.interpreted-text role="ref"}
      and set the same value to the field
      `Secure Hash Function`{.interpreted-text role="guilabel"} in the
      `Credentials`{.interpreted-text role="guilabel"} tab.

3.  Configure the rest of the options to your liking.

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::
