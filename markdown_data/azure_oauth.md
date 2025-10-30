# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication/azure_oauth.md

Connect Microsoft Outlook 365 to Odoo using Azure OAuth
=======================================================

Odoo is compatible with Microsoft\'s Azure OAuth for Microsoft 365. In
order to send and receive secure emails from a custom domain, all that
is required is to configure a few settings on the Azure platform and on
the back end of the Odoo database. This configuration works with either
a personal email address or an address created by a custom domain.

::: {.seealso}
[Microsoft Learn: Register an application with the Microsoft identity
platform](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app)
:::

::: {.seealso}
\- `/applications/general/users/azure`{.interpreted-text role="doc"} -
`/applications/productivity/calendar/outlook`{.interpreted-text
role="doc"}
:::

Setup in Microsoft Azure Portal
-------------------------------

### Create a new application

To get started, go to [Microsoft\'s Azure
Portal](https://portal.azure.com/). Log in with the
`Microsoft Outlook Office 365`{.interpreted-text role="guilabel"}
account if there is one, otherwise log in with the personal
`Microsoft account`{.interpreted-text role="guilabel"}. A user with
administrative access to the Azure Settings will need to connect and
perform the following configuration. Next, navigate to the section
labeled `Manage Microsoft Entra ID`{.interpreted-text role="guilabel"}
(formally *Azure Active Directory*).

Now, click on `Add (+)`{.interpreted-text role="guilabel"}, located in
the top menu, and then select `App
registration`{.interpreted-text role="guilabel"}. On the
`Register an application`{.interpreted-text role="guilabel"} screen,
rename the `Name`{.interpreted-text role="guilabel"} to
[Odoo]{.title-ref} or something recognizable. Under the
`Supported account types`{.interpreted-text role="guilabel"} section
select
`Accounts in any organizational directory (Any Microsoft Entra ID directory - Multitenant)
and personal Microsoft accounts (e.g. Skype, Xbox)`{.interpreted-text
role="guilabel"}.

Under the `Redirect URL`{.interpreted-text role="guilabel"} section,
select `Web`{.interpreted-text role="guilabel"} as the platform, and
then input [https://\<web base
url\>/microsoft\_outlook/confirm]{.title-ref} in the
`URL`{.interpreted-text role="guilabel"} field. The
[web.base.url]{.title-ref} is subject to change depending on the URL
used to log in to the database.

::: {.note}
::: {.title}
Note
:::

The documentation about the
`web.base.url <domain-name/web-base-url>`{.interpreted-text role="ref"}
explains how to freeze a unique URL. It is also possible to add
different redirect URLs on the Microsoft app.
:::

After the URL has been added to the field, `Register`{.interpreted-text
role="guilabel"} the application, so it is created.

### API permissions

The `API permissions`{.interpreted-text role="guilabel"} should be set
next. Odoo will need specific API permissions to be able to read (IMAP)
and send (SMTP) emails in the Microsoft 365 setup. First, click the
`API permissions`{.interpreted-text role="guilabel"} link, located in
the left menu bar. Next, click on the `(+)
Add a Permission`{.interpreted-text role="guilabel"} button and select
`Microsoft Graph`{.interpreted-text role="guilabel"} under
`Commonly Used
Microsoft APIs`{.interpreted-text role="guilabel"}. After, select the
`Delegated Permissions`{.interpreted-text role="guilabel"} option.

In the search bar, search for the following
`Delegated permissions`{.interpreted-text role="guilabel"} and click
`Add permissions`{.interpreted-text role="guilabel"} for each one:

-   `SMTP.Send`{.interpreted-text role="guilabel"}
-   `IMAP.AccessAsUser.All`{.interpreted-text role="guilabel"}

::: {.note}
::: {.title}
Note
:::

The `User.Read`{.interpreted-text role="guilabel"} permission will be
added by default.
:::

{.align-center}

Assign users and groups
-----------------------

After adding the API permissions, navigate back to the
`Overview`{.interpreted-text role="guilabel"} of the
`Application`{.interpreted-text role="guilabel"} in the top of the left
sidebar menu.

Now, add users to this application. Under the
`Essentials`{.interpreted-text role="guilabel"} overview table, click on
the link labeled
`Managed Application in Local Directory`{.interpreted-text
role="guilabel"}, or the last option on the bottom right-hand side of
the table.

![Add users/groups by clicking the Managed application in local directory link for the
created application.](azure_oauth/managed-application.png){.align-center}

In the left sidebar menu, select `Users and Groups`{.interpreted-text
role="guilabel"}. Next, click on `(+) Add
User/Group`{.interpreted-text role="guilabel"}. Depending on the
account, either a `Group`{.interpreted-text role="guilabel"} and a
`User`{.interpreted-text role="guilabel"} can be added, or only
`Users`{.interpreted-text role="guilabel"}. Personal accounts will only
allow for `Users`{.interpreted-text role="guilabel"} to be added.

Under `Users`{.interpreted-text role="guilabel"} or
`Groups`{.interpreted-text role="guilabel"}, click on
`None Selected`{.interpreted-text role="guilabel"} and add the users or
group of users that will be sending emails from the
`Microsoft account`{.interpreted-text role="guilabel"} in Odoo.
`Add`{.interpreted-text role="guilabel"} the users/groups, click
`Select`{.interpreted-text role="guilabel"}, and then
`Assign`{.interpreted-text role="guilabel"} them to the application.

### Create credentials

Now that the Microsoft Azure app is set up, credentials need to be
created for the Odoo setup. These include the
`Client ID`{.interpreted-text role="guilabel"} and
`Client Secret`{.interpreted-text role="guilabel"}. To start, the
`Client ID`{.interpreted-text role="guilabel"} can be copied from the
`Overview`{.interpreted-text role="guilabel"} page of the app. The
`Client ID`{.interpreted-text role="guilabel"} or
`Application ID`{.interpreted-text role="guilabel"} is located under the
`Display Name`{.interpreted-text role="guilabel"} in the
`Essentials`{.interpreted-text role="guilabel"} overview of the app.

{.align-center}

Next, the `Client Secret Value`{.interpreted-text role="guilabel"} needs
to be retrieved. To get this value, click on
`Certificates & Secrets`{.interpreted-text role="guilabel"} in the left
sidebar menu. Then, a `Client Secret`{.interpreted-text role="guilabel"}
needs to be produced. In order to do this, click on the
`(+) New Client Secret`{.interpreted-text role="guilabel"} button.

A window on the right will populate with a button labeled
`Add a client secret`{.interpreted-text role="guilabel"}. Under
`Description`{.interpreted-text role="guilabel"}, type in [Odoo
Fetchmail]{.title-ref} or something recognizable, and then set the
`expiration date`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

A new `Client Secret`{.interpreted-text role="guilabel"} will need to be
produced and configured if the first one expires. In this event, there
could be an interruption of service, so the expiration date should be
noted and set to the furthest possible date.
:::

Next, click on `Add`{.interpreted-text role="guilabel"} when these two
values are entered. A `Client Secret Value`{.interpreted-text
role="guilabel"} and `Secret ID`{.interpreted-text role="guilabel"} will
be created. It is important to copy the `Value`{.interpreted-text
role="guilabel"} or `Client Secret Value`{.interpreted-text
role="guilabel"} into a notepad as it will become encrypted after
leaving this page. The `Secret ID`{.interpreted-text role="guilabel"} is
not needed.

{.align-center}

After these steps, the following items should be ready to be set up in
Odoo:

-   A client ID (`Client ID`{.interpreted-text role="guilabel"} or
    `Application ID`{.interpreted-text role="guilabel"})
-   A client secret (`Value`{.interpreted-text role="guilabel"} or
    `Client Secret Value`{.interpreted-text role="guilabel"})

This completes the setup on the
`Microsoft Azure Portal`{.interpreted-text role="guilabel"} side.

Setup in Odoo
-------------

### Enter Microsoft Outlook credentials

First, open the Odoo database and navigate to the
`Apps`{.interpreted-text role="guilabel"} module. Then, remove the
`Apps`{.interpreted-text role="guilabel"} filter from the search bar and
type in [Outlook]{.title-ref}. After that, install the module called
`Microsoft Outlook`{.interpreted-text role="guilabel"}.

Next, navigate to `Settings --> General Settings`{.interpreted-text
role="menuselection"}, and under the `Discuss`{.interpreted-text
role="guilabel"} section, ensure that the checkbox for
`Custom Email Servers`{.interpreted-text role="guilabel"} is checked.
This populates a new option for `Outlook Credentials`{.interpreted-text
role="guilabel"}.

`Save`{.interpreted-text role="guilabel"} the progress.

Then, copy and paste the `Client ID`{.interpreted-text role="guilabel"}
(Application ID) and `Client Secret
(Client Secret Value)`{.interpreted-text role="guilabel"} into the
respective fields and `Save`{.interpreted-text role="guilabel"} the
settings.

{.align-center}

### Configure outgoing email server

On the `General Settings`{.interpreted-text role="guilabel"} page, under
the `Custom Email Servers`{.interpreted-text role="guilabel"} setting,
click the `Outgoing Email Servers`{.interpreted-text role="guilabel"}
link to configure the Microsoft account.

Then, create a new email server and check the box for
`Outlook`{.interpreted-text role="guilabel"}. Next, fill in the
`Name`{.interpreted-text role="guilabel"} (it can be anything) and the
Microsoft Outlook email `Username`{.interpreted-text role="guilabel"}.

If the `From Filter`{.interpreted-text role="guilabel"} field is empty,
enter either a `domain or email address
<email-outbound-unique-address>`{.interpreted-text role="ref"}.

Then, click on `Connect your Outlook account`{.interpreted-text
role="guilabel"}.

A new window from Microsoft opens to complete the
`authorization process`{.interpreted-text role="guilabel"}. Select the
appropriate email address that is being configured in Odoo.

{.align-center}

Then, allow Odoo to access the Microsoft account by clicking on
`Yes`{.interpreted-text role="guilabel"}. After this, the page will
navigate back to the newly configured
`Outgoing Mail Server`{.interpreted-text role="guilabel"} in Odoo. The
configuration automatically loads the `token`{.interpreted-text
role="guilabel"} in Odoo, and a tag stating
`Outlook Token Valid`{.interpreted-text role="guilabel"} appears in
green.

{.align-center}

Finally, click `Test Connection`{.interpreted-text role="guilabel"}. A
confirmation message should appear. The Odoo database can now send safe,
secure emails through Microsoft Outlook using OAuth authentication.

#### Configuration with a single outgoing mail server {#azure_oauth/notifications}

Configuring a single outgoing server is the simplest configuration
available for Microsoft Azure and it doesn\'t require extensive access
rights for the users in the database.

A generic email address would be used to send emails for all users
within the database. For example it could be structured with a
[notifications]{.title-ref} alias
([notifications\@example.com]{.title-ref}) or [contact]{.title-ref}
alias ([contact\@example.com]{.title-ref}). This address must be set as
the `FROM Filtering`{.interpreted-text role="guilabel"} on the server.
This address must also match the
[{mail.default.from}@{mail.catchall.domain}]{.title-ref} key combination
in the system parameters.

::: {.seealso}
Visit the
`From Filtering documentation <email-outbound-different-servers-personalized-from-filtering>`{.interpreted-text
role="ref"} for more information.
:::

::: {.note}
::: {.title}
Note
:::

The `System Parameters`{.interpreted-text role="guilabel"} can be
accessed by activating `developer-mode`{.interpreted-text role="ref"} in
the
`Settings --> Technical --> Parameters --> System Parameters`{.interpreted-text
role="menuselection"} menu.
:::

When using this configuration, every email that is sent from the
database will use the address of the configured
[notification]{.title-ref} mailbox. However it should be noted that the
name of the sender will appear but their email address will change:

{.align-center}

::: {.example}
Single outgoing mail server configuration:

-   Outgoing mail server **username** (login) =
    [notifications\@example.com]{.title-ref}
-   Outgoing mail server `FROM Filtering`{.interpreted-text
    role="guilabel"} = [notifications\@example.com]{.title-ref}
-   [mail.catchall.domain]{.title-ref} in system parameters =
    [example.com]{.title-ref}
-   [mail.default.from]{.title-ref} in system parameters =
    [notifications]{.title-ref}
:::

#### User-specific (multiple user) configuration

In addition to a generic email server, individual email servers can be
set up for users in a database. These email addresses must be set as the
`FROM Filtering`{.interpreted-text role="guilabel"} on each individual
server for this configuration to work.

This configuration is the more difficult of the two Microsoft Azure
configurations, in that it requires all users configured with email
servers to have access rights to settings in order to establish a
connection to the email server.

##### Setup

Each user should have a separate email server set up. The
`FROM Filtering`{.interpreted-text role="guilabel"} should be set so
that only the user\'s email is sent from that server. In other words,
only a user with an email address that matches the set
`FROM Filtering`{.interpreted-text role="guilabel"} is able to use this
server.

::: {.seealso}
Visit the
`From Filtering documentation <email-outbound-different-servers-personalized-from-filtering>`{.interpreted-text
role="ref"} for more information.
:::

A `fallback server <azure_oauth/notifications>`{.interpreted-text
role="ref"} must be setup to allow for the sending of
`notifications`{.interpreted-text role="guilabel"}. The
`FROM Filtering`{.interpreted-text role="guilabel"} for this server
should have the value of the
[{mail.default.from}@{mail.catchall.domain}]{.title-ref}.

::: {.note}
::: {.title}
Note
:::

The `System Parameters`{.interpreted-text role="guilabel"} can be
accessed by activating `developer-mode`{.interpreted-text role="ref"} in
the
`Settings --> Technical --> Parameters --> System Parameters`{.interpreted-text
role="menuselection"} menu.
:::

::: {.important}
::: {.title}
Important
:::

The configuration for this transactional email server can work alongside
an outgoing mass-mailing email server. The
`FROM Filtering`{.interpreted-text role="guilabel"} for the mass-mailing
email server can remain empty, but it\'s require to be added in the
settings of the *Email Marketing* application.

::: {.seealso}
For more information on setting the mass-mailing email server visit
`email-outbound-custom-domain-smtp-server`{.interpreted-text
role="ref"}.
:::
:::

::: {.example}
Multiple user outgoing mail server configuration:

-   

    User \#1 mailbox

    :   -   Outgoing mail server \#1 **username** (login) =
            [john\@example.com]{.title-ref}
        -   Outgoing mail server \#1 `FROM Filtering`{.interpreted-text
            role="guilabel"} = [john\@example.com]{.title-ref}

-   

    User \#2 mailbox

    :   -   Outgoing mail server \#2 **username** (login) =
            [jane\@example.com]{.title-ref}
        -   Outgoing mail server \#2 `FROM Filtering`{.interpreted-text
            role="guilabel"} = [jane\@example.com]{.title-ref}

-   

    Notifications mailbox

    :   -   Outgoing mail server \#3 **username** (login) =
            [notifications\@example.com]{.title-ref}
        -   Outgoing mail server \#3 `FROM Filtering`{.interpreted-text
            role="guilabel"} = [notifications\@example.com]{.title-ref}

-   

    System Parameters

    :   -   [mail.catchall.domain]{.title-ref} in system parameters =
            [example.com]{.title-ref}
        -   [mail.default.from]{.title-ref} in system parameters =
            [notifications]{.title-ref}
:::

### Configure incoming email server

The incoming account should be configured in a similar way to the
outgoing email account. Navigate to the
`Incoming Mail Servers`{.interpreted-text role="guilabel"} in the
`Technical Menu`{.interpreted-text role="guilabel"} and
`Create`{.interpreted-text role="guilabel"} a new configuration. Check
or Select the button next to
`Outlook Oauth Authentication`{.interpreted-text role="guilabel"} and
enter the `Microsoft Outlook username`{.interpreted-text
role="guilabel"}. Click on `Connect your Outlook
account`{.interpreted-text role="guilabel"}. Odoo will state:
`Outlook Token Valid`{.interpreted-text role="guilabel"} Now
`Test and Confirm`{.interpreted-text role="guilabel"} the account. The
account should be ready to receive email to the Odoo database.
