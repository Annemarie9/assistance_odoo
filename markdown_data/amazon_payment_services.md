# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/amazon_payment_services.md

Amazon Payment Services
=======================

 or APS is
an online payment provider established in Dubai offering several online
payment options.

Configuration on APS Dashboard {#payment_providers/aps/configure-dashboard}
------------------------------

1.  Log into your [Amazon Payment Services
    Dashboard](https://fort.payfort.com/) and go to
    `Integration Settings --> Security Settings`{.interpreted-text
    role="menuselection"}. Generate the `Access Code`{.interpreted-text
    role="guilabel"} if none has been generated yet. Copy the values of
    the `Merchant Identifier`{.interpreted-text role="guilabel"},
    `Access Code`{.interpreted-text role="guilabel"},
    `SHA Request Phrase`{.interpreted-text role="guilabel"} and
    `SHA Response Phrase`{.interpreted-text role="guilabel"} fields, and
    save them for later.

2.  Enter your Odoo database URL in the `Origin URL`{.interpreted-text
    role="guilabel"}, for example:
    [https://yourcompany.odoo.com/]{.title-ref}. Then, click on
    `Save Changes`{.interpreted-text role="guilabel"}.

3.  Navigate to
    `Integration Settings --> Technical Settings`{.interpreted-text
    role="menuselection"} and click on `Redirection`{.interpreted-text
    role="guilabel"}. Make sure `Status`{.interpreted-text
    role="guilabel"} is set to [Active]{.title-ref} and select your
    preferred payment methods underneath in
    `Payment Options`{.interpreted-text role="guilabel"}.

4.  | Set `Send Response Parameters`{.interpreted-text role="guilabel"}
      to `Yes`{.interpreted-text role="guilabel"} and enter your
      database URL followed by [/payment/aps/return]{.title-ref} in the
      `Redirection URL`{.interpreted-text role="guilabel"}.
    | For example
      [https://yourcompany.odoo.com/payment/aps/return]{.title-ref}.
    | Enter your database URL followed by
      [/payment/aps/webhook]{.title-ref} in the
      `Direct Transaction Feedback`{.interpreted-text role="guilabel"}
      and `Notification URL`{.interpreted-text role="guilabel"} fields.
    | For example
      [https://yourcompany.odoo.com/payment/aps/webhook]{.title-ref}.
    | Click on `Save Changes`{.interpreted-text role="guilabel"}.

5.  Under
    `Integration Settings --> Payment Page Template`{.interpreted-text
    role="menuselection"} you can customize the look and feel of the
    Amazon Payment Services payment page (where customers fill out their
    credit card details during payment).

Configuration on Odoo {#payment_providers/aps/configure-odoo}
---------------------

1.  `Navigate to the payment provider Amazon Payment Services <payment_providers/add_new>`{.interpreted-text
    role="ref"}, change its state to `Enabled`{.interpreted-text
    role="guilabel"}, and make sure it is `Published`{.interpreted-text
    role="guilabel"}.
2.  In the `Credentials`{.interpreted-text role="guilabel"} tab, fill
    the `Merchant Identifier`{.interpreted-text role="guilabel"},
    `Access Code`{.interpreted-text role="guilabel"},
    `SHA Request Phrase`{.interpreted-text role="guilabel"} and
    `SHA Response Phrase`{.interpreted-text role="guilabel"} with the
    values you saved at the step
    `payment_providers/aps/configure-dashboard`{.interpreted-text
    role="ref"}.
3.  Configure the rest of the options to your liking.
