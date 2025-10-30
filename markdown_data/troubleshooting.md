Troubleshooting eBay connector
==============================

::: {.seealso}
To learn more about the eBay connector visit these pages as well:

-   `setup`{.interpreted-text role="doc"}
-   `manage`{.interpreted-text role="doc"}
-   `linking_listings`{.interpreted-text role="doc"}
:::

Accept account deletion notifications
-------------------------------------

Since September 2021, **eBay requires supporting customer account
deletion/closure notifications**. As such, when eBay receives an account
request for deletion, all eBay partners must confirm the reception of
the request and take further action if necessary.

Odoo has a notification endpoint to receive those notifications, confirm
the reception of the request, and handle the first set of actions to
anonymize the account details in *Contacts* and remove the customer\'s
access to the portal.

::: {.important}
::: {.title}
Important
:::

Make sure to correctly
`set up the subscription to the marketplace account deletion
notifications <ebay/subscribe-account-deletion-notifications>`{.interpreted-text
role="ref"} as eBay may temporarily disable the related eBay account
until the subscription is completed.
:::

### Verify the installation of Odoo is up to date

In order to activate the endpoint, the module *eBay Connector - Account
Deletion* must be installed. If the Odoo database was first created
after September 2021, the module is installed automatically and the
administrator can proceed to the
`next step <ebay/retrieve-endpoint-details>`{.interpreted-text
role="ref"}.

#### Update Odoo to the latest release

The notification endpoint is made available through a new Odoo module;
to be able to install it, the administrator must make sure that the Odoo
source code is up-to-date.

-   If the company uses Odoo on Odoo.com or Odoo.sh platform, the code
    is already up-to-date, so proceed to the next step.
-   If the company uses Odoo with an on-premise setup or through a
    partner, then the administrator must update the installation as
    detailed in `this documentation page
    </administration/on_premise/update>`{.interpreted-text role="doc"}
    or by contacting an integrating partner.

#### Update the list of available modules

New modules must be *discovered* by the Odoo instance to be available in
the `Apps`{.interpreted-text role="menuselection"} menu.

To do so, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}, and go
to `Apps ->
Update Apps List`{.interpreted-text role="menuselection"}. A wizard will
ask for confirmation.

#### Install the eBay Connector - Account Deletion update

::: {.warning}
::: {.title}
Warning
:::

**Never** install new modules in the production database without testing
them in a duplicate or staging environment. For Odoo.com customers, a
duplicate database can be created from the database management page. For
Odoo.sh users, the administrator should use a staging or duplicate
database. For on-premise users, the administrator should use a staging
environment - contact the integrating partner for more information
regarding how to test a new module in a particular setup.
:::

To install the module, go to the `Apps`{.interpreted-text
role="menuselection"} menu, remove the [Apps]{.title-ref} search facet
and search for [eBay]{.title-ref}. If the module *eBay Connector -
Account Deletion* is present and marked as installed, the Odoo database
is already up-to-date and the administrator can proceed with the next
step. If it is not yet installed, install it now.

### Retrieve endpoint details from Odoo {#ebay/retrieve-endpoint-details}

The endpoint details can be found in
`Sales --> Configuration --> Settings --> eBay`{.interpreted-text
role="menuselection"}. First, input random text values for the
`Production App Key`{.interpreted-text role="guilabel"} and for the
`Production Cert Key`{.interpreted-text role="guilabel"}. Click on
`Generate Token`{.interpreted-text role="guilabel"} to retrieve the
`Verification Token`{.interpreted-text role="guilabel"}.

{.align-center}

### Subscribe to account deletion notifications {#ebay/subscribe-account-deletion-notifications}

Navigate to the .
Configure the account deletion/notification settings in eBay by
navigating to the [Hi \[username\]]{.title-ref} at the top right of
screen, then go to `Alerts & Notifications`{.interpreted-text
role="guilabel"}.

{.align-center}

To subscribe to deletion/closure notifications, eBay needs a few
details:

-   An *email address* to send notifications to if the endpoint is
    unreachable.
-   The *endpoint details*:
    -   The URL to Odoo\'s account deletion notification endpoint
    -   A verification token

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

The administrator can edit the last two fields once the email address
field is filled out.
:::

### Verify the connectivity with the endpoint

After setting the retrieved endpoint details in eBay\'s dashboard,
consider testing the connectivity with the
`Send Test Notification`{.interpreted-text role="guilabel"} button.

> The following confirmation message should be received: \"A test
> notification was sent successfully!\"

{.align-center}

::: {.seealso}
\- `/applications/sales/sales/ebay_connector/manage`{.interpreted-text
role="doc"} -
`/applications/sales/sales/ebay_connector/linking_listings`{.interpreted-text
role="doc"} -
`/applications/sales/sales/ebay_connector/setup`{.interpreted-text
role="doc"}
:::
