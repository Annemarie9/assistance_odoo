# File: /content/odoo_doc17.0/fr/content/applications/general/users/azure.md

Microsoft Azure sign-in authentication
======================================

The Microsoft Azure OAuth sign-in authentication is a useful function
that allows Odoo users to sign in to their database with their Microsoft
Azure account.

This is particularly helpful if the organization uses Azure Workspace,
and wants employees within the organization to connect to Odoo using
their Microsoft Accounts.

::: {.warning}
::: {.title}
Warning
:::

Databases hosted on Odoo.com should not use OAuth login for the owner or
administrator of the database as it would unlink the database from their
Odoo.com account. If OAuth is set up for that user, the database will no
longer be able to be duplicated, renamed, or otherwise managed from the
Odoo.com portal.
:::

::: {.seealso}
\- `../../productivity/calendar/outlook`{.interpreted-text role="doc"} -
`../email_communication/azure_oauth`{.interpreted-text role="doc"}
:::

Configuration
-------------

Integrating the Microsoft sign-in function requires configuration on
Microsoft and Odoo.

### Odoo System Parameter

First activate the `developer mode <developer-mode>`{.interpreted-text
role="ref"}, and then go to `Settings
--> Technical --> System Parameters`{.interpreted-text
role="menuselection"}.

Click `Create`{.interpreted-text role="guilabel"} and on the new/blank
form that appears, add the following system parameter
[auth\_oauth.authorization\_header]{.title-ref} to the
`Key`{.interpreted-text role="guilabel"} field, and set the
`Value`{.interpreted-text role="guilabel"} to [1]{.title-ref}. Then
click `Save`{.interpreted-text role="guilabel"} to finish.

### Microsoft Azure dashboard

#### Create a new application

Now that the system parameters in Odoo have been set up, it\'s time to
create a corresponding application inside of Microsoft Azure. To get
started creating the new application, go to [Microsoft\'s Azure
Portal](https://portal.azure.com/). Log in with the `Microsoft
Outlook Office 365`{.interpreted-text role="guilabel"} account if there
is one, otherwise, log in with a personal `Microsoft
account`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

A user with administrative access to the *Azure Settings* must connect
and perform the following configuration steps below.
:::

Next, navigate to the section labeled
`Manage Microsoft Entra ID`{.interpreted-text role="guilabel"} (formally
*Azure Active Directory*). The location of this link is usually in the
center of the page.

Now, click on the `Add (+)`{.interpreted-text role="guilabel"} icon,
located in the top menu, and then select `App
registration`{.interpreted-text role="guilabel"} from the drop-down
menu. On the `Register an application`{.interpreted-text
role="guilabel"} screen, rename the `Name`{.interpreted-text
role="guilabel"} field to [Odoo Login OAuth]{.title-ref} or a similarly
recognizable title. Under the
`Supported account types`{.interpreted-text role="guilabel"} section
select the option for `Accounts in this
organizational directory only (Default Directory only - Single tenant)`{.interpreted-text
role="guilabel"}.

::: {.warning}
::: {.title}
Warning
:::

The `Supported account types`{.interpreted-text role="guilabel"} can
vary by Microsoft account type and end use of the OAuth. For example: Is
the login meant for internal users within one organization or is it
meant for customer portal access? The above configuration is used for
internal users in an organization.

Choose `Personal Microsoft accounts only`{.interpreted-text
role="guilabel"} if the target audience is meant for portal users.
Choose
`Accounts in this organizational directory only (Default Directory only -
Single tenant)`{.interpreted-text role="guilabel"} if the target
audience is company users.
:::

Under the `Redirect URL`{.interpreted-text role="guilabel"} section,
select `Web`{.interpreted-text role="guilabel"} as the platform, and
then input [https://\<odoo base url\>/auth\_oauth/signin]{.title-ref} in
the `URL`{.interpreted-text role="guilabel"} field. The Odoo base `URL
(Uniform Resource Locator)`{.interpreted-text role="abbr"} is the
canonical domain at which your Odoo instance can be reached (e.g.
*mydatabase.odoo.com* if you are hosted on Odoo.com) in the
`URL`{.interpreted-text role="guilabel"} field. Then, click
`Register`{.interpreted-text role="guilabel"}, and the application is
created.

#### Authentication

Edit the new app\'s authentication by clicking on the
`Authentication`{.interpreted-text role="guilabel"} menu item in the
left menu after being redirected to the application\'s settings from the
previous step.

Next, the type of *tokens* needed for the OAuth authentication will be
chosen. These are not currency tokens but rather authentication tokens
that are passed between Microsoft and Odoo. Therefore, there is no cost
for these tokens; they are used merely for authentication purposes
between two
`APIs (application programming interfaces)`{.interpreted-text
role="abbr"}. Select the tokens that should be issued by the
authorization endpoint by scrolling down the screen and check the boxes
labeled: `Access tokens (used for implicit flows)`{.interpreted-text
role="guilabel"} and `ID tokens (used for implicit and
hybrid flows)`{.interpreted-text role="guilabel"}.

{.align-center}

Click `Save`{.interpreted-text role="guilabel"} to ensure these settings
are saved.

#### Gather credentials

With the application created and authenticated in the Microsoft Azure
console, credentials will be gathered next. To do so, click on the
`Overview`{.interpreted-text role="guilabel"} menu item in the left-hand
column. Select and copy the `Application (client) ID`{.interpreted-text
role="guilabel"} in the window that appears. Paste this credential to a
clipboard / notepad, as this credential will be used in the Odoo
configuration later.

After finishing this step, click on `Endpoints`{.interpreted-text
role="guilabel"} on the top menu and click the *copy icon* next to
`OAuth 2.0 authorization endpoint (v2)`{.interpreted-text
role="guilabel"} field. Paste this value in the clipboard / notepad.

{.align-center}

### Odoo setup

Finally, the last step in the Microsoft Azure OAuth configuration is to
configure some settings in Odoo. Navigate to
`Settings --> Integrations --> OAuth Authentication`{.interpreted-text
role="menuselection"} and check the box to activate the OAuth login
feature. Click `Save`{.interpreted-text role="guilabel"} to ensure the
progress is saved. Then, sign in to the database once the login screen
loads.

Once again, navigate to
`Settings --> Integrations --> OAuth Authentication`{.interpreted-text
role="menuselection"} and click on `OAuth Providers`{.interpreted-text
role="guilabel"}. Now, select `New`{.interpreted-text role="guilabel"}
in the upper-left corner and name the provider [Azure]{.title-ref}.

Paste the `Application (client) ID`{.interpreted-text role="guilabel"}
from the previous section into the `Client
ID`{.interpreted-text role="guilabel"} field. After completing this,
paste the new `OAuth 2.0 authorization endpoint (v2)`{.interpreted-text
role="guilabel"} value into the `Authorization URL`{.interpreted-text
role="guilabel"} field.

For the `UserInfo URL`{.interpreted-text role="guilabel"} field, paste
the following `URL (Uniform Resource Locator)`{.interpreted-text
role="abbr"}: [https://graph.microsoft.com/oidc/userinfo]{.title-ref}

In the `Scope`{.interpreted-text role="guilabel"} field, paste the
following value: [openid profile email]{.title-ref}. Next, the Windows
logo can be used as the CSS class on the login screen by entering the
following value: [fa fa-fw fa-windows]{.title-ref}, in the
`CSS class`{.interpreted-text role="guilabel"} field.

Check the box next to the `Allowed`{.interpreted-text role="guilabel"}
field to enable the OAuth provider. Finally, add [Microsoft
Azure]{.title-ref} to the `Login button label`{.interpreted-text
role="guilabel"} field. This text will appear next to the Windows logo
on the login page.

{.align-center}

`Save`{.interpreted-text role="guilabel"} the changes to complete the
OAuth authentication setup in Odoo.

### User experience flows

For a user to log in to Odoo using Microsoft Azure, the user must be on
the `Odoo
password reset page`{.interpreted-text role="menuselection"}. This is
the only way that Odoo is able to link the Microsoft Azure account and
allow the user to log in.

::: {.note}
::: {.title}
Note
:::

Existing users must
`reset their password <users/reset-password>`{.interpreted-text
role="ref"} to access the `Odoo password reset page`{.interpreted-text
role="menuselection"}. New Odoo users must click the new user invitation
link that was sent via email, then click on
`Microsoft Azure`{.interpreted-text role="guilabel"}. Users should not
set a new password.
:::

To sign in to Odoo for the first time using the Microsoft Azure OAuth
provider, navigate to the `Odoo password reset page`{.interpreted-text
role="menuselection"} (using the new user invitation link). A password
reset page should appear. Then, click on the option labeled
`Microsoft Azure`{.interpreted-text role="guilabel"}. The page will
redirect to the Microsoft login page.

{.align-center}

Enter the `Microsoft Email Address`{.interpreted-text role="guilabel"}
and click `Next`{.interpreted-text role="guilabel"}. Follow the process
to sign in to the account. Should
`2FA (Two Factor Authentication)`{.interpreted-text role="abbr"} be
turned on, then an extra step may be required.

{.align-center}

Finally, after logging in to the account, the page will redirect to a
permissions page where the user will be prompted to
`Accept`{.interpreted-text role="guilabel"} the conditions that the Odoo
application will access their Microsoft information.

{.align-center}
