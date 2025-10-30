# File: /content/odoo_doc17.0/fr/content/applications/general/users/portal.md

Portal access
=============

::: {#portal/main}
Portal access is given to users who need the ability to view certain
documents or information within an Odoo database.
:::

Some common use cases for providing portal access include allowing
customers to read/view any or all of the following in Odoo:

-   leads/opportunities
-   quotations/sales orders
-   purchase orders
-   invoices & bills
-   projects
-   tasks
-   timesheets
-   tickets
-   signatures
-   subscriptions

::: {.note}
::: {.title}
Note
:::

Portal users only have read/view access, and will not be able to edit
any documents in the database.
:::

Provide portal access to customers
----------------------------------

From the main Odoo dashboard, select the `Contacts`{.interpreted-text
role="guilabel"} application. If the contact is not yet created in the
database, click on the `Create`{.interpreted-text role="guilabel"}
button, enter the details of the contact, and then click
`Save`{.interpreted-text role="guilabel"}. Otherwise, choose an existing
contact, and then click on the `Action`{.interpreted-text
role="guilabel"} drop-down menu located at the top-center of the
interface.

{.align-center}

Then select `Grant portal access`{.interpreted-text role="guilabel"}. A
pop-up window appears, listing three fields:

-   `Contact`{.interpreted-text role="guilabel"}: the recorded name of
    the contact in the Odoo database
-   `Email`{.interpreted-text role="guilabel"}: the contact\'s email
    address that they will use to log into the portal
-   `In Portal`{.interpreted-text role="guilabel"}: whether or not the
    user has portal access

To grant portal access, first enter the contact\'s
`Email`{.interpreted-text role="guilabel"} they will use to log into the
portal. Then, check the box under the `In Portal`{.interpreted-text
role="guilabel"} column. Optionally, add text to the invitation message
the contact will receive. Then click `Apply`{.interpreted-text
role="guilabel"} to finish.

![An email address and corresponding checkbox for the contact need to be filled in before
sending a portal invitation.](portal/add-contact-to-portal.png){.align-center}

An email will be sent to the specified email address, indicating that
the contact is now a portal user for that Odoo database.

::: {.tip}
::: {.title}
Tip
:::

To grant portal access to multiple users at once, navigate to a company
contact, then click `Action --> Grant portal access`{.interpreted-text
role="menuselection"} to view a list of all of the company\'s related
contacts. Check the box under the `In Portal`{.interpreted-text
role="guilabel"} column for all the contacts that need portal access,
then click `Apply`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

At any time, portal access can be revoked by navigating to the contact,
clicking `Action --> Grant portal access`{.interpreted-text
role="menuselection"}, and then unselecting the checkbox under the
`In Portal`{.interpreted-text role="guilabel"} column and clicking
`Apply`{.interpreted-text role="guilabel"}.
:::

Change portal username {#portal/login}
----------------------

There may be times when a portal user wants to change their user login.
This can be done by any user in the database with administrator access
rights. The following process outlines the necessary steps to change the
portal user login.

::: {.seealso}
`See the documentation on setting access rights
</applications/general/users/access_rights>`{.interpreted-text
role="doc"}.
:::

First, navigate to `Settings app --> Users`{.interpreted-text
role="menuselection"}. Then, under `Filters`{.interpreted-text
role="guilabel"}, select `Portal Users`{.interpreted-text
role="guilabel"}, or select `Add Custom Filter`{.interpreted-text
role="guilabel"} and set the following configuration
`Groups`{.interpreted-text role="guilabel"} \>
`contains`{.interpreted-text role="guilabel"} \> [portal]{.title-ref}.
After making this selection, search for (and open) the portal user that
needs to be edited.

Next, click `Edit`{.interpreted-text role="guilabel"} (if necessary),
click into the `Email Address`{.interpreted-text role="guilabel"} field,
and proceed to make any necessary changes to this field. The
`Email Address`{.interpreted-text role="guilabel"} field is used to log
into the Odoo portal.

::: {.note}
::: {.title}
Note
:::

Changing the `Email Address`{.interpreted-text role="guilabel"} (or
login) only changes the *username* on the customer\'s portal login.

In order to change the contact email, this change needs to take place on
the contact template in the *Contacts* app. Alternatively, the customer
can change their email directly from the portal, but the login
**cannot** be changed.
`See change customer info <portal/custinfo>`{.interpreted-text
role="ref"}.
:::

Customer portal changes
-----------------------

There may be times when the customer would like to make changes to their
contact information, password/security, or payment information attached
to the portal account. This can be performed by the customer from their
portal. The following process is how a customer can change their contact
information.

### Change customer info {#portal/custinfo}

First enter the username and password (login) into the database login
page to access the portal user account. A portal dashboard will appear
upon successfully logging in. Portal documents from the various
installed Odoo applications will appear with the number count of each.

::: {.seealso}
`Portal access documentation <portal/main>`{.interpreted-text
role="ref"}.
:::

Next, navigate to the upper-right corner of the portal, and click the
`Edit`{.interpreted-text role="guilabel"} button, next to the
`Details`{.interpreted-text role="guilabel"} section. Then, change the
pertinent information, and click `Confirm`{.interpreted-text
role="guilabel"}.

### Change password

First enter the username and password (login) into the database login
page to access the portal user account. A portal dashboard will appear
upon successfully logging in.

If the customer would like to change their password for portal access,
click on the `Edit
Security Settings`{.interpreted-text role="guilabel"} link, below the
`Account Security`{.interpreted-text role="guilabel"} section. Then,
make the necessary changes, by typing in the current
`Password`{.interpreted-text role="guilabel"},
`New Password`{.interpreted-text role="guilabel"}, and verify the new
password. Lastly, click on `Change Password`{.interpreted-text
role="guilabel"} to complete the password change.

::: {.note}
::: {.title}
Note
:::

If a customer would like to change the login, as documented above,
contact the Odoo database point-of-contact.
`See above documentation on changing the portal username <portal/login>`{.interpreted-text
role="ref"}.
:::

::: {.note}
::: {.title}
Note
:::

Passwords for portal users and Odoo.com users remain separate, even if
the same email address is used.
:::

### Add two-factor authentication

First enter the username and password (login) into the database login
page to access the portal user account. A portal dashboard will appear
upon successfully logging in.

If the customer would like to turn on two-factor authentication (2FA)
for portal access, click on the
`Edit Security Settings`{.interpreted-text role="guilabel"} link, below
the `Account Security`{.interpreted-text role="guilabel"} section.

Click on `Enable two-factor authentication`{.interpreted-text
role="guilabel"} to turn on `2FA (two-factor
authentication)`{.interpreted-text role="abbr"}. Confirm the current
portal password in the `Password`{.interpreted-text role="guilabel"}
field. Then, click on `Confirm Password`{.interpreted-text
role="guilabel"}. Next, activate
`2FA (two-factor authentication)`{.interpreted-text role="abbr"} in a
`2FA (two-factor authentication)`{.interpreted-text role="abbr"} app
(Google Authenticator, Authy, etc.), by scanning the
`QR code`{.interpreted-text role="guilabel"} or entering a
`Verification Code`{.interpreted-text role="guilabel"}.

Finally, click `Enable two-factor authentication`{.interpreted-text
role="guilabel"} to complete the setup.

### Change payment info {#users-portal-payment-methods}

First enter the username and password (login) into the database login
page to access the portal user account. A portal dashboard will appear
upon successfully logging in.

If the customer would like to manage payment options, navigate to the
`Manage payment
methods`{.interpreted-text role="guilabel"} in the menu on the right.
Then, add the new payment information, and select `Add
new card`{.interpreted-text role="guilabel"}.
