# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication/google_oauth.md

Connect Gmail to Odoo using Google OAuth
========================================

Odoo is compatible with Google\'s OAuth for Gmail. In order to send
secure emails from a custom domain, all that is required is to configure
a few settings on Google\'s *Workspace* platform, as well as on the back
end of the Odoo database. This configuration works by using either a
personal email address or an address created by a custom domain.

::: {.tip}
::: {.title}
Tip
:::

For more information, visit [Google\'s
documentation](https://support.google.com/cloud/answer/6158849) on
setting up OAuth.
:::

::: {.seealso}
\- `/applications/general/users/google`{.interpreted-text role="doc"} -
`/applications/productivity/calendar/google`{.interpreted-text
role="doc"}
:::

Setup in Google
---------------

### Create a new project

To get started, go to the [Google API
Console](https://console.developers.google.com). Log in with your
*Google Workspace* account if you have one, otherwise log in with your
personal Gmail account (this should match the email address you want to
configure in Odoo).

After that, click on `Create Project`{.interpreted-text
role="guilabel"}, located on the far right of the `OAuth
consent screen`{.interpreted-text role="guilabel"}. If a project has
already been created in this account, then the `New
Project`{.interpreted-text role="guilabel"} option will be located on
the top right under the `Select a project`{.interpreted-text
role="guilabel"} drop-down menu.

On the `New Project`{.interpreted-text role="menuselection"} screen,
rename the `Project name`{.interpreted-text role="guilabel"} to
[Odoo]{.title-ref} and browse for the `Location`{.interpreted-text
role="guilabel"}. Set the `Location`{.interpreted-text role="guilabel"}
as the *Google Workspace organization*. If you are using a personal
Gmail account, then leave the `Location`{.interpreted-text
role="guilabel"} as `No Organization`{.interpreted-text
role="guilabel"}.

{.align-center}

Click on `Create`{.interpreted-text role="guilabel"} to finish this
step.

### OAuth consent screen

If the page doesn\'t redirect to the `User Type`{.interpreted-text
role="menuselection"} options, click on `OAuth
consent screen`{.interpreted-text role="guilabel"} in the left menu.

Under `User Type`{.interpreted-text role="guilabel"} options, select the
appropriate `User Type`{.interpreted-text role="guilabel"}, and then
click on `Create`{.interpreted-text role="guilabel"} again, which will
finally navigate to the `Edit app registration`{.interpreted-text
role="menuselection"} page.

::: {.warning}
::: {.title}
Warning
:::

*Personal* Gmail Accounts are only allowed to be **External** User Type,
which means Google may require an approval, or for *Scopes* to be added
on. However, using a *Google WorkSpace* account allows for **Internal**
User Type to be used.

Note, as well, that while the API connection is in the *External*
testing mode, then no approval is necessary from Google. User limits in
this testing mode is set to 100 users.
:::

### Edit app registration

Next we will configure the app registration of the project.

On the `OAuth consent screen`{.interpreted-text role="guilabel"} step,
under the `App information`{.interpreted-text role="guilabel"} section,
enter [Odoo]{.title-ref} in the `App name`{.interpreted-text
role="guilabel"} field. Select the organization\'s email address under
the `User support`{.interpreted-text role="guilabel"} email field.

Next, under `App Domain --> Authorized domains`{.interpreted-text
role="menuselection"}, click on `Add Domain`{.interpreted-text
role="guilabel"} and enter [odoo.com]{.title-ref}.

After that, under the `Developer contact information`{.interpreted-text
role="guilabel"} section, enter the organization\'s email address.
Google uses this email address to notify the organization about any
changes to your project.

Next, click on the `Save and Continue`{.interpreted-text
role="guilabel"} button. Then, skip the `Scopes`{.interpreted-text
role="menuselection"} page by scrolling to the bottom and clicking on
`Save and Continue`{.interpreted-text role="guilabel"}.

If continuing in testing mode (External), add the email addresses being
configured under the `Test users`{.interpreted-text role="guilabel"}
step, by clicking on `Add Users`{.interpreted-text role="guilabel"}, and
then the `Save and
Continue`{.interpreted-text role="guilabel"} button. A summary of the
app registration appears.

Finally, scroll to the bottom and click on
`Back to Dashboard`{.interpreted-text role="guilabel"} to finish setting
up the project.

### Create Credentials

Now that the project is set up, credentials should be created, which
includes the *Client ID* and *Client Secret*. First, click on
`Credentials`{.interpreted-text role="guilabel"} in the left sidebar
menu.

Then, click on `Create Credentials`{.interpreted-text role="guilabel"}
in the top menu and select `OAuth client ID`{.interpreted-text
role="guilabel"} from the dropdown menu.

-   Under `Application Type`{.interpreted-text role="guilabel"}, select
    `Web Application`{.interpreted-text role="guilabel"} from the
    dropdown menu.
-   In the `Name`{.interpreted-text role="guilabel"} field, enter
    [Odoo]{.title-ref}.
-   Under the `Authorized redirect URIs`{.interpreted-text
    role="guilabel"} label, click the button `ADD URI`{.interpreted-text
    role="guilabel"}, and then input
    [https://yourdbname.odoo.com/google\_gmail/confirm]{.title-ref} in
    the `URIs 1`{.interpreted-text role="guilabel"} field. Be sure to
    replace the *yourdbname* part of the URL with the actual Odoo
    database name.
-   Next, click on `Create`{.interpreted-text role="guilabel"} to
    generate an OAuth `Client ID`{.interpreted-text role="guilabel"} and
    `Client
    Secret`{.interpreted-text role="guilabel"}. Finally, copy each
    generated value for later use when configuring in Odoo, and then
    navigate to the Odoo database.

{.align-center}

Setup in Odoo
-------------

### Enter Google Credentials

First, open Odoo and navigate to the `Apps`{.interpreted-text
role="guilabel"} module. Then, remove the `Apps`{.interpreted-text
role="guilabel"} filter from the search bar and type in
[Google]{.title-ref}. Install the module called `Google
Gmail`{.interpreted-text role="guilabel"}.

Next, navigate to `Settings --> General Settings`{.interpreted-text
role="menuselection"}, and under the `Discuss`{.interpreted-text
role="guilabel"} section, ensure that the checkbox for
`Custom Email Servers`{.interpreted-text role="guilabel"} or
`External Email
Servers`{.interpreted-text role="guilabel"} is checked. This populates a
new option for `Gmail Credentials`{.interpreted-text role="guilabel"} or
`Use
a Gmail Sever`{.interpreted-text role="guilabel"}. Then, copy and paste
the respective values into the `Client ID`{.interpreted-text
role="guilabel"} and `Client Secret`{.interpreted-text role="guilabel"}
fields and `Save`{.interpreted-text role="guilabel"} the settings.

### Configure outgoing email server

To configure the external Gmail account, return to the top of the
`Custom Email Servers`{.interpreted-text role="guilabel"} setting and
then click the `Outgoing Email Servers`{.interpreted-text
role="guilabel"} link.

{.align-center}

Then, click on `New`{.interpreted-text role="guilabel"} or
`Create`{.interpreted-text role="guilabel"} to create a new email
server, and fill in the `Name`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and the email
`Username`{.interpreted-text role="guilabel"} (if required).

Next, click on `Gmail OAuth Authentication`{.interpreted-text
role="guilabel"} or `Gmail`{.interpreted-text role="guilabel"} (under
the `Authenticate with`{.interpreted-text role="guilabel"} or
`Connection`{.interpreted-text role="guilabel"} section). Finally, click
on `Connect your Gmail Account`{.interpreted-text role="guilabel"}.

A new window labeled `Google`{.interpreted-text role="guilabel"} opens
to complete the authorization process. Select the appropriate email
address that is being configured in Odoo.

If the email address is a personal account, then an extra step pops up,
so click `Continue`{.interpreted-text role="guilabel"} to allow the
verification and connect the Gmail account to Odoo.

Then, allow Odoo to access the Google account by clicking on
`Continue`{.interpreted-text role="guilabel"} or
`Allow`{.interpreted-text role="guilabel"}. After that, the page
navigates back to the newly configured outgoing email server in Odoo.
The configuration automatically loads the token in Odoo, and a tag
stating `Gmail Token Valid`{.interpreted-text role="guilabel"} appears
in green.

{.align-center}

Finally, `Test the Connection`{.interpreted-text role="guilabel"}. A
confirmation message should appear. The Odoo database can now send safe,
secure emails through Google using OAuth authentication.

Google OAuth FAQ
----------------

### Production VS Testing Publishing Status

Choosing `Production`{.interpreted-text role="guilabel"} as the
`Publishing Status`{.interpreted-text role="guilabel"} (instead of
`Testing`{.interpreted-text role="guilabel"}) will display the following
warning message:

{.align-center}

To correct this warning, navigate to the [Google API
Platform](https://console.cloud.google.com/apis/credentials/consent). If
the `Publishing status`{.interpreted-text role="guilabel"} is
`In Production`{.interpreted-text role="guilabel"}, click
`Back to Testing`{.interpreted-text role="guilabel"} to correct the
issue.

### No Test Users Added

If no test users are added to the OAuth consent screen, then a 403
access denied error will populate.

{.align-center}

To correct this error, return to the
`OAuth consent screen`{.interpreted-text role="guilabel"} under `APIs &
Services`{.interpreted-text role="guilabel"} and add test user(s) to the
app. Add the email that you are configuring in Odoo.

### Gmail Module not updated

If the *Google Gmail* module in Odoo has not been updated to the latest
version, then a `Forbidden`{.interpreted-text role="guilabel"} error
message populates.

{.align-center}

To correct this error, go to the `Apps`{.interpreted-text
role="menuselection"} module and clear out the search terms. Then,
search for [Gmail]{.title-ref} or [Google]{.title-ref} and upgrade the
`Google Gmail`{.interpreted-text role="guilabel"} module. Finally, click
on the three dots on the upper right of the module and select
`Upgrade`{.interpreted-text role="guilabel"}.

### Application Type

When creating the credentials (OAuth *Client ID* and *Client Secret*),
if `Desktop App`{.interpreted-text role="guilabel"} is selected for the
`Application Type`{.interpreted-text role="guilabel"}, an
`Authorization Error`{.interpreted-text role="guilabel"} appears.

{.align-center}

To correct this error, delete the credentials already created and create
new credentials, selecting `Web Application`{.interpreted-text
role="guilabel"} for the `Application Type`{.interpreted-text
role="guilabel"}. Then, under `Authorized
redirect URIs`{.interpreted-text role="guilabel"}, click
`ADD URI`{.interpreted-text role="guilabel"} and type:
[https://yourdbname.odoo.com/google\_gmail/confirm]{.title-ref} in the
field, being sure to replace *yourdbname* in the URL with the Odoo
database name.
