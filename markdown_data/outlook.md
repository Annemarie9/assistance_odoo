# File: /content/odoo_doc17.0/fr/content/applications/productivity/calendar/outlook.md

Outlook Calendar synchronization
================================

Synchronizing a user\'s *Outlook Calendar* with Odoo is useful for
keeping track of tasks and appointments across all related applications.

::: {.seealso}
\- `../../general/users/azure`{.interpreted-text role="doc"} -
`../../general/email_communication/azure_oauth`{.interpreted-text
role="doc"}
:::

Microsoft Azure setup
---------------------

To sync the *Outlook Calendar* with Odoo\'s *Calendar*, a Microsoft
*Azure* account is required. Creating an account is free for users who
have never tried, or paid for, *Azure*. For more information, view the
account options on the [Azure
website](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F).

Refer to [Microsoft\'s documentation
\<https://docs.microsoft.com/en-us/azure/active-directory/
develop/quickstart-create-new-tenant\>]() on how to set up a Microsoft
*Entra ID* (formally called Microsoft *Azure Active Directory (Azure
AD)*). This is an API console to manage and register Microsoft
applications.

Existing Microsoft *Entra ID* users should log in at the [Microsoft
Azure developer portal](https://portal.azure.com/#home). Next, select
`View`{.interpreted-text role="guilabel"} under the section labeled
`Manage Microsoft Entra ID`{.interpreted-text role="guilabel"}.

### Register application

After logging in with the Microsoft *Entra ID*, [register an
application](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

To create an application, click `+ Add`{.interpreted-text
role="guilabel"} in the top menu. From the resulting drop-down menu,
select `App Registration`{.interpreted-text role="guilabel"}.

{.align-center}

Enter a unique `Name`{.interpreted-text role="guilabel"} for the
connected application.

Choosing the appropriate `Supported account type`{.interpreted-text
role="guilabel"} is essential, or else the connected application will
not work. Users who wish to connect their *Outlook Calendar* to Odoo
should select the
`Accounts in any organizational directory (Any Microsoft Entra ID directory -
Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)`{.interpreted-text
role="guilabel"} option for `Supported
account types`{.interpreted-text role="guilabel"}.

When configuring the `Redirect URI`{.interpreted-text role="guilabel"},
choose the `Web`{.interpreted-text role="guilabel"} option from the
first drop-down menu. Then, enter the Odoo database URI (URL) followed
by [/microsoft\_account/authentication]{.title-ref}.

::: {.example}
Enter
[https://yourdbname.odoo.com/microsoft\_account/authentication]{.title-ref}
for the `Redirect
URI`{.interpreted-text role="guilabel"}. Replace
[yourdbname.odoo.com]{.title-ref} with the
`URL (Uniform Resource Locator)`{.interpreted-text role="abbr"}.
:::

::: {.tip}
::: {.title}
Tip
:::

Ensure the database\'s
`URL (Uniform Resource Locator)`{.interpreted-text role="abbr"} (domain)
used in the URI is the exact same domain as the one configured on the
[web.base.url]{.title-ref} system parameter.

Access the [web.base.url]{.title-ref} by activating
`developer mode <developer-mode>`{.interpreted-text role="ref"}, and
navigating to
`Settings app --> Technical header menu --> Parameters section --> System
Parameters`{.interpreted-text role="menuselection"}. Then, select it
from the `Key`{.interpreted-text role="guilabel"} list on the
`System Parameters`{.interpreted-text role="guilabel"} page.
:::

{.align-center}

For more information on the restrictions and limitations of URIs, check
Microsoft\'s [Redirect URI (reply URL) restrictions and
limitations](https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url)
page.

Finally, on the application registration page, click
`Register`{.interpreted-text role="guilabel"} button to complete the
application registration. The
`Application (client) ID`{.interpreted-text role="guilabel"} is
produced. Copy this value, as it is needed later, in the
`outlook_calendar/odoo_setup`{.interpreted-text role="ref"}.

![Application client ID highlighted in the essentials section of the newly created
application.](outlook/app-client-id.png){.align-center}

### Create client secret

The second credential needed to complete the synchronization of the
Microsoft *Outlook Calendar* is the *Client Secret*. The user **must**
add a client secret, as this allows Odoo to authenticate itself,
requiring no interaction from the user\'s side. *Certificates* are
optional.

To add a client secret, click `Certificates & secrets`{.interpreted-text
role="menuselection"} in the left menu. Then click
`+ New client secret`{.interpreted-text role="guilabel"} to create the
client secret.

![New client secret page with certificates and secrets menu and new client secret option
highlighted.](outlook/client-secret.png){.align-center}

Next, type a `Description`{.interpreted-text role="guilabel"}, and
select when the client secret `Expires`{.interpreted-text
role="guilabel"}. Available options include:
`90 days (3 months)`{.interpreted-text role="guilabel"},
`365 days (12 months)`{.interpreted-text role="guilabel"},
`545 days (18 months)`{.interpreted-text role="guilabel"},
`730 days (24 months)`{.interpreted-text role="guilabel"} or
`Custom`{.interpreted-text role="guilabel"}. The
`Custom`{.interpreted-text role="guilabel"} option allows the
administrator to set a `Start`{.interpreted-text role="guilabel"} and
`End`{.interpreted-text role="guilabel"} date.

Finally, click `Add`{.interpreted-text role="guilabel"} to
`Add a client secret`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Since resetting the synchronization can be tricky, Odoo recommends
setting the maximum allowed expiration date for the client secret (24
months or custom), so there is no need to re-synchronize soon.
:::

Copy the `Value`{.interpreted-text role="guilabel"} for use in the next
section.

::: {.warning}
::: {.title}
Warning
:::

Client secret values cannot be viewed, except immediately after
creation. Be sure to save the secret when created *before* leaving the
page.
:::

Configuration in Odoo {#outlook_calendar/odoo_setup}
---------------------

In the Odoo database, go to
`Calendar app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the checkbox beside the
`Outlook Calendar`{.interpreted-text role="guilabel"} setting. Remember
to click `Save`{.interpreted-text role="guilabel"} to implement the
changes.



From the Microsoft *Azure* portal, under the
`Overview`{.interpreted-text role="guilabel"} section of the
application, copy the `Application (Client) ID`{.interpreted-text
role="guilabel"}, if it has not already been copied, and paste it into
the `Client ID`{.interpreted-text role="guilabel"} field in Odoo.

{.align-center}

Copy the previously-acquired `Value`{.interpreted-text role="guilabel"}
(Client Secret Value), and paste it into the
`Client Secret`{.interpreted-text role="guilabel"} field in Odoo.

{.align-center}

Finally, on the Odoo `Settings --> General Settings`{.interpreted-text
role="menuselection"} page, click `Save`{.interpreted-text
role="guilabel"}.

Sync with Outlook {#outlook/sync}
-----------------

::: {.warning}
::: {.title}
Warning
:::

Odoo highly recommends testing the Outlook calendar synchronization on a
test database and a test email address (that is not used for any other
purpose) before attempting to sync the desired Outlook Calendar with the
user\'s production database.

If the user has any past, present, or future events on their Odoo
calendar before syncing their Outlook calendar, Outlook will treat the
events pulled from Odoo\'s calendar during the sync as new events,
causing an email notification to be sent from Outlook to all the event
attendees.

To avoid unwanted emails being sent to all past, present, and future
event attendees, the user must add the events from the Odoo calendar to
the Outlook calendar before the first ever sync, delete the events from
Odoo, and then start the sync.

Even after synchronizing the Odoo Calendar with the Outlook calendar,
Outlook will still send a notification to all event participants every
time an event is edited (created, deleted, unarchived, or event
date/time changed), with no exceptions. This is a limitation that cannot
be fixed from Odoo\'s side.

In summary, once a user synchronizes their Outlook calendar with the
Odoo calendar:

-   Creating an event in Odoo causes Outlook to send an invitation to
    all event attendees.
-   Deleting an event in Odoo causes Outlook to send a cancellation to
    all event attendees.
-   Unarchiving an event in Odoo causes Outlook to send an invitation to
    all event attendees.
-   Archiving an event in Odoo causes Outlook to send a cancellation to
    all event attendees.
-   Adding a contact to an event causes Outlook to send an invitation to
    all event attendees.
-   Removing a contact from an event causes Outlook to send a
    cancellation to all event attendees.
:::

### Sync Odoo Calendar and Outlook

In the Odoo database, open to the *Calendar* module, and click the
`Outlook`{.interpreted-text role="guilabel"} sync button on the
right-side of the page, beneath the monthly calendar.

{.align-center}

The synchronization is a two-way process, meaning that events are
reconciled in both accounts (*Outlook* and Odoo). The page redirects to
a Microsoft login page, and the user is asked to log in to their
account, if they are not already. Finally, grant the required
permissions by clicking `Accept`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

All users that want to use the synchronization simply need to
`sync their calendar with
Outlook <outlook/sync>`{.interpreted-text role="ref"}. The configuration
of Microsoft\'s *Azure* account is only done once, as Microsoft *Entra
ID* tenants\' client IDs and client secrets are unique, and help the
user manage a specific instance of Microsoft cloud services for internal
and external users.
:::

::: {.seealso}
\- `../../general/integrations/mail_plugins/outlook`{.interpreted-text
role="doc"} - `google`{.interpreted-text role="doc"}
:::

Troubleshoot sync
-----------------

There may be times when the *Microsoft Outlook Calendar* account does
not sync correctly with Odoo. Sync issues can be seen in the database
logs.

In these cases, the account needs troubleshooting. A reset can be
performed using the `Reset Account`{.interpreted-text role="guilabel"}
button, which can be accessed by navigating to `Settings
app --> Manage Users`{.interpreted-text role="menuselection"}. Then,
select the user to modify the calendar, and click on the
`Calendar`{.interpreted-text role="guilabel"} tab.

{.align-center}

Next, click `Reset Account`{.interpreted-text role="guilabel"} under the
correct calendar.

### Reset options

The following reset options are available for troubleshooting *Microsoft
Outlook Calendar* sync with Odoo:

{.align-center}

`User's Existing Events`{.interpreted-text role="guilabel"}:

> -   `Leave them untouched`{.interpreted-text role="guilabel"}: no
>     changes to the events.
> -   `Delete from the current Microsoft Calendar account`{.interpreted-text
>     role="guilabel"}: delete the events from *Microsoft Outlook
>     Calendar*.
> -   `Delete from Odoo`{.interpreted-text role="guilabel"}: delete the
>     events from the Odoo calendar.
> -   `Delete from both`{.interpreted-text role="guilabel"}: delete the
>     events from both *Microsoft Outlook Calendar* and Odoo calendar.

`Next Synchronization`{.interpreted-text role="guilabel"}:

> -   `Synchronize only new events`{.interpreted-text role="guilabel"}:
>     sync new events on *Microsoft Outlook Calendar* and/or Odoo
>     calendar.
> -   `Synchronize all existing events`{.interpreted-text
>     role="guilabel"}: sync all events on *Microsoft Outlook Calendar*
>     and/or Odoo calendar.

Click `Confirm`{.interpreted-text role="guilabel"} after making the
selection to modify the user\'s events and the calendar synchronization.
