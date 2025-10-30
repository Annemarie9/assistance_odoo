# File: /content/odoo_doc17.0/fr/content/applications/general/users.md

show-content

:   

Users
=====

Odoo defines a *user* as someone who has access to a database. An
administrator can add as many users as the company needs and, in order
to restrict the type of information each user can access, rules can be
applied to each user. Users and access rights can be added and changed
at any point.

::: {.seealso}
\- `users/language`{.interpreted-text role="doc"} -
`users/access_rights`{.interpreted-text role="doc"} -
`access-rights/superuser`{.interpreted-text role="ref"} -
`access-rights/groups`{.interpreted-text role="ref"}
:::

Add individual users {#users/add-individual}
--------------------

To add new users, navigate to
`Settings app --> Users section --> Manage Users`{.interpreted-text
role="menuselection"}, and click on `New`{.interpreted-text
role="guilabel"}.

{.align-center}

Fill in the form with all the required information. Under the
`Access Rights
<users/access_rights>`{.interpreted-text role="doc"} tab, choose the
group within each application the user can have access to.

The list of applications shown is based on the applications installed on
the database.

{.align-center}

After filling out all the necessary fields on the page, manually
`Save`{.interpreted-text role="guilabel"}. An invitation email is
automatically sent to the user, using the email in the
`Email Address`{.interpreted-text role="guilabel"} field. The user must
click on the link included in the email to accept the invitation, and to
create a database login.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

If the company is on a monthly subscription plan, the database
automatically updates to reflect the added users. If the company is on a
yearly or multi-year plan, an expiration banner appears in the database.
An upsell quotation can be created by clicking the banner to update the
subscription. Alternatively, [send a support
ticket](https://www.odoo.com/help) to resolve the issue.
:::

### User type

`User Type`{.interpreted-text role="guilabel"} can be selected from the
`Access Rights`{.interpreted-text role="guilabel"} tab of the user form,
accessible via
`Settings app --> Users section --> Manage Users`{.interpreted-text
role="menuselection"}.

There are three types of users: `Internal User`{.interpreted-text
role="guilabel"}, `Portal`{.interpreted-text role="guilabel"}, and
`Public`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Users are considered internal database users. Portal users are external
users, who only have access to the database portal to view records. See
the documentation on `users/portal`{.interpreted-text role="doc"}.

Public users are those visiting websites, via the website\'s frontend.
:::

The `Portal`{.interpreted-text role="guilabel"} and
`Public`{.interpreted-text role="guilabel"} user options do **not**
allow the administrator to choose access rights. These users have
specific access rights pre-set (such as, record rules and restricted
menus), and usually do not belong to the usual Odoo groups.

Deactivate users {#users/deactivate}
----------------

To deactivate (i.e. archive) a user, navigate to
`Settings app --> Users section -->
Manage Users`{.interpreted-text role="menuselection"}. Then, tick the
checkbox to the left of the user(s) to be deactivated.

After selecting the appropriate user to be archived, click the
`⚙️ Actions`{.interpreted-text role="guilabel"} icon, and select
`Archive`{.interpreted-text role="guilabel"} from the resulting
drop-down menu. Then, click `OK`{.interpreted-text role="guilabel"} from
the `Confirmation`{.interpreted-text role="guilabel"} pop-up window that
appears.

::: {.danger}
::: {.title}
Danger
:::

**Never** deactivate the main/administrator user (admin). Making changes
to admin users can have a detrimental impact on the database. This
includes *impotent admin*, which means that no user in the database can
make changes to the access rights. For this reason, Odoo recommends
contacting an Odoo Business Analyst, or our Support Team, before making
changes.
:::

### Error: too many users

If there are more users in an Odoo database than provisioned in the Odoo
Enterprise subscription, the following message is displayed.

{.align-center}

When the message appears, the database administrator has 30 days to act
before the database expires. The countdown is updated every day.

To resolve the issue, either:

-   Add more users to the subscription by clicking the
    `Upgrade your subscription`{.interpreted-text role="guilabel"} link
    displayed in the message to validate the upsell quotation, and pay
    for the extra users.
-   `Deactivate users <users/deactivate>`{.interpreted-text role="ref"},
    and reject the upsell quotation.

::: {.warning}
::: {.title}
Warning
:::

If the company is on a monthly subscription plan, the database
automatically updates to reflect the added users. If the company is on a
yearly or multi-year plan, an expiration banner appears in the database.
An upsell quotation can be created by clicking the banner to update the
subscription. Alternatively, users can [send a support
ticket](https://www.odoo.com/help) to resolve the issue.
:::

Once the database has the correct number of users, the expiration
message disappears automatically after a few days, when the next
verification occurs.

Password management {#users/passwords-management}
-------------------

Password management is an important part of granting users autonomous
access to the database at all times. Odoo offers a few different methods
to reset a user\'s password.

::: {.tip}
::: {.title}
Tip
:::

Odoo has a setting to specify the length needed for a password. This
setting can be accessed by navigating to
`Settings app --> Permissions`{.interpreted-text role="menuselection"}
section, and entering the desired password length in the
`Minimum Password Length`{.interpreted-text role="guilabel"} field. By
default the value is [8]{.title-ref}.
:::

{.align-center}

### Reset password {#users/reset-password}

Sometimes, users might wish to reset their personal password for added
security, so they are the only ones with access to the password. Odoo
offers two different reset options: one initiated by the user to reset
the password, and another where the administrator triggers a reset.

#### Enable password reset from login page {#users/reset-password-login}

It is possible to enable/disable password resets directly from the login
page. This action is completed by the individual user, and this setting
is enabled by default.

To change this setting, go to
`Settings app --> Permissions`{.interpreted-text role="menuselection"}
section, activate `Password Reset`{.interpreted-text role="guilabel"},
and then click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

On the login page, click `Reset Password`{.interpreted-text
role="guilabel"} to initiate the password reset process, and have a
reset-token sent to the email on file.

{.align-center}

#### Send reset instructions {#users/reset-password-email}

Go to `Settings app --> Users & Companies --> Users`{.interpreted-text
role="menuselection"}, select the user from the list, and click on
`Send Password Reset Instructions`{.interpreted-text role="guilabel"} on
the user form. An email is automatically sent to them with password
reset instructions.

::: {.note}
::: {.title}
Note
:::

The `Send Password Reset Instructions`{.interpreted-text
role="guilabel"} button **only** appears if the Odoo invitation email
has already been confirmed by the user. Otherwise, a
`Re-send Invitation Email`{.interpreted-text role="guilabel"} button
appears.
:::

This email contains all the instructions needed to reset the password,
along with a link redirecting the user to an Odoo login page.

{.align-center}

### Change user password {#users/change-password}

Go to `Settings app --> Users & Companies --> Users`{.interpreted-text
role="menuselection"}, and select a user to access its form. Click on
the `⚙️ Actions`{.interpreted-text role="guilabel"} icon, and select
`Change Password`{.interpreted-text role="guilabel"} from, the resulting
drop-down menu. Enter a new password in the
`New Password`{.interpreted-text role="guilabel"} column of the
`Change Password`{.interpreted-text role="guilabel"} pop-up window that
appears, and confirm the change by clicking
`Change Password`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

This operation only modifies the password of the users locally, and does
**not** affect their odoo.com account.

If the odoo.com password needs to be changed, use the
`send the password reset instructions
<users/reset-password-email>`{.interpreted-text role="ref"}. Odoo.com
passwords grant access to the *My Databases* page, and other portal
features.
:::

After clicking `Change Password`{.interpreted-text role="guilabel"}, the
page is redirected to an Odoo login page where the database can be
re-accessed using the new password.

Multi Companies {#users/multi-companies}
---------------

The `Multi Companies`{.interpreted-text role="guilabel"} field on a user
form allows an administrator to provide access to multiple companies for
users. To configure a multi-company environment for a user, navigate to
the desired user by going to:
`Settings app --> Users section --> Manage users`{.interpreted-text
role="menuselection"}. Then, select the user to open their user form,
and configure with multi-company access.

Under `Multi Companies`{.interpreted-text role="guilabel"} in the
`Access Rights`{.interpreted-text role="guilabel"} tab, set the fields
labeled `Allowed Companies`{.interpreted-text role="guilabel"} and
`Default Company`{.interpreted-text role="guilabel"}.

The `Allowed Companies`{.interpreted-text role="guilabel"} field can
contain multiple companies. These are the companies the user can access
and edit, according to the set access rights. The
`Default Company`{.interpreted-text role="guilabel"} is the company the
user defaults to, upon logging in each time. This field can contain only
**one** company.

::: {.warning}
::: {.title}
Warning
:::

If multi-company access is not configured correctly, it could lead to
inconsistent multi-company behaviors. Because of this, only experienced
Odoo users should make access rights changes to users for databases with
a multi-company configuration. For technical explanations, refer to the
developer documentation on
`../../../developer/howtos/company`{.interpreted-text role="doc"}.
:::

{.align-center}

::: {.seealso}
`companies`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
users/language users/2fa users/access\_rights users/portal
users/facebook users/google users/azure users/ldap
:::
