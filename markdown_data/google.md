# File: /content/odoo_doc17.0/fr/content/applications/productivity/calendar/google.md

Google Calendar synchronization
===============================

Synchronize Google Calendar with Odoo to see and manage meetings from
both platforms (updates go in both directions). This integration helps
organize schedules, so a meeting is never missed.

::: {.seealso}
\- `/applications/general/users/google`{.interpreted-text role="doc"} -
`/applications/general/email_communication/google_oauth`{.interpreted-text
role="doc"}
:::

Setup in Google
---------------

### Select (or create) a project

Create a new Google API project and enable the Google Calendar API.
First, go to the [Google API
Console](https://console.developers.google.com) and log into the Google
account.

::: {.note}
::: {.title}
Note
:::

If this is the first time visiting this page, Google will prompt the
user to enter a country and agree to the Terms of Service. Select a
country from the drop-down list and agree to the
`ToS (Terms of Service)`{.interpreted-text role="abbr"}.
:::

Next, click `Select a project`{.interpreted-text role="guilabel"} and
select (or create) an API project to configure OAuth in, and store
credentials. Click `New Project`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Give the API Project a clear name, like \"Odoo Sync\", so it can be
easily identified.
:::

### Enable Google calendar API

Now, click on `Enabled APIs and Services`{.interpreted-text
role="guilabel"} in the left menu. Select `Enabled APIs
and Services`{.interpreted-text role="guilabel"} again if the
`Search bar`{.interpreted-text role="guilabel"} doesn\'t appear.

{.align-center}

After that, search for [Google Calendar API]{.title-ref} using the
search bar and select `Google
Calendar API`{.interpreted-text role="guilabel"} from the search
results. Click `Enable`{.interpreted-text role="guilabel"}.

{.align-center}

### OAuth consent screen

Now that the API project has been created, OAuth should be configured.
To do that, click on `OAuth consent`{.interpreted-text role="guilabel"}
in the left menu and then select the `User Type`{.interpreted-text
role="guilabel"}.

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

In the second step, `OAuth Consent Screen`{.interpreted-text
role="guilabel"}, type [Odoo]{.title-ref} in the
`App name`{.interpreted-text role="guilabel"} field, select the email
address for the `User support email`{.interpreted-text role="guilabel"}
field, and type the email address for the
`Developer contact information`{.interpreted-text role="guilabel"}
section. Then, click `Save and
Continue`{.interpreted-text role="guilabel"}.

Skip the third step, `Scopes`{.interpreted-text role="menuselection"},
by clicking `Save and Continue`{.interpreted-text role="guilabel"}.

Next, if continuing in testing mode (External), add the email addresses
being configured under the `Test users`{.interpreted-text
role="guilabel"} step, by clicking on `Add Users`{.interpreted-text
role="guilabel"}, and then the `Save and
Continue`{.interpreted-text role="guilabel"} button. A summary of the
app registration appears.

Finally, scroll to the bottom, and click on
`Back to Dashboard`{.interpreted-text role="guilabel"}.

Now, the OAuth consent has been configured, and it\'s time to create
credentials.

### Create credentials

The *Client ID* and the *Client Secret* are both needed to connect
Google Calendar to Odoo. This is the last step in the Google console.
Begin by clicking `Credentials`{.interpreted-text role="guilabel"} in
the left menu. Then, click `Create Credentials`{.interpreted-text
role="guilabel"}, and select `OAuth client ID`{.interpreted-text
role="guilabel"}, Google will open a guide to create credentials.

Under `Create OAuth Client ID`{.interpreted-text role="menuselection"},
select `Website application`{.interpreted-text role="guilabel"} for the
`Application Type`{.interpreted-text role="guilabel"} field, and type
[My Odoo Database]{.title-ref} for the `Name`{.interpreted-text
role="guilabel"}.

-   Under the `Authorized JavaScript Origins`{.interpreted-text
    role="guilabel"} section, click `+ Add URI`{.interpreted-text
    role="guilabel"} and type the company\'s Odoo full
    `URL (Uniform Resource Locator)`{.interpreted-text role="abbr"}
    address.
-   Under the `Authorized redirect URIs`{.interpreted-text
    role="guilabel"} section, click `+ Add URI`{.interpreted-text
    role="guilabel"} and type the company\'s Odoo
    `URL (Uniform Resource Locator)`{.interpreted-text role="abbr"}
    address followed by [/google\_account/authentication]{.title-ref}.
    Finally, click `Create`{.interpreted-text role="guilabel"}.

{.align-center}

A `Client ID`{.interpreted-text role="guilabel"} and
`Client Secret`{.interpreted-text role="guilabel"} will appear, copy
these to a notepad.

Setup in Odoo
-------------

Once the *Client ID* and the *Client Secret* are located, open the Odoo
database and go to
`Settings --> General Settings --> Integrations --> Google Calendar`{.interpreted-text
role="menuselection"}. Check the box next to
`Google Calendar`{.interpreted-text role="guilabel"}.

{.align-center}

Next, copy and paste the *Client ID* and the *Client Secret* from the
Google Calendar API credentials page into their respective fields below
the `Google Calendar`{.interpreted-text role="guilabel"} checkbox. Then,
click `Save`{.interpreted-text role="guilabel"}.

Sync calendar in Odoo
---------------------

Finally, open the `Calendar`{.interpreted-text role="menuselection"} app
in Odoo and click on the `Google`{.interpreted-text role="guilabel"}
sync button to sync Google Calendar with Odoo.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When syncing Google Calendar with Odoo for the first time, the page will
redirect to the Google Account. From there, select the
`Email Account`{.interpreted-text role="guilabel"} that should have
access, then select `Continue`{.interpreted-text role="guilabel"}
(should the app be unverifed), and finally select
`Continue`{.interpreted-text role="guilabel"} (to give permission for
the transfer of data)\`.
:::

{.align-center}

Now, Odoo Calendar is successfully synced with Google Calendar!

::: {.warning}
::: {.title}
Warning
:::

Odoo highly recommends testing the Google calendar synchronization on a
test database and a test email address (that is not used for any other
purpose) before attempting to sync the desired Google Calendar with the
user\'s production database.

Once a user synchronizes their Google calendar with the Odoo calendar:

-   Creating an event in Odoo causes Google to send an invitation to all
    event attendees.
-   Deleting an event in Odoo causes Google to send a cancellation to
    all event attendees.
-   Adding a contact to an event causes Google to send an invitation to
    all event attendees.
-   Removing a contact from an event causes Google to send a
    cancellation to all event attendees.

Events can be created in *Google Calendar* without sending a
notification by selecting `Don't Send`{.interpreted-text
role="guilabel"} when prompted to send invitation emails.
:::

Troubleshoot sync
-----------------

There may be times when the *Google Calendar* account does not sync
correctly with Odoo. Sync issues can be seen in the database logs.

In these cases, the account needs troubleshooting. A reset can be
performed using the `Reset Account`{.interpreted-text role="guilabel"}
button, which can be accessed by navigating to `Settings
app --> Manage Users`{.interpreted-text role="menuselection"}. Then,
select the user to modify the calendar, and click the
`Calendar`{.interpreted-text role="guilabel"} tab.

{.align-center}

Next, click `Reset Account`{.interpreted-text role="guilabel"} under the
correct calendar.

### Reset options

The following reset options are available for troubleshooting Google
calendar sync with Odoo:

{.align-center}

`User's Existing Events`{.interpreted-text role="guilabel"}:

> -   `Leave them untouched`{.interpreted-text role="guilabel"}: no
>     changes to the events.
> -   `Delete from the current Google Calendar account`{.interpreted-text
>     role="guilabel"}: delete the events from *Google Calendar*.
> -   `Delete from Odoo`{.interpreted-text role="guilabel"}: delete the
>     events from the Odoo calendar.
> -   `Delete from both`{.interpreted-text role="guilabel"}: delete the
>     events from both *Google Calendar* and Odoo calendar.

`Next Synchronization`{.interpreted-text role="guilabel"}:

> -   `Synchronize only new events`{.interpreted-text role="guilabel"}:
>     sync new events on *Google Calendar* and/or Odoo calendar.
> -   `Synchronize all existing events`{.interpreted-text
>     role="guilabel"}: sync all events on *Google Calendar* and/or Odoo
>     calendar.

Click `Confirm`{.interpreted-text role="guilabel"} after making the
selection to modify the user\'s events and the calendar synchronization.

Google OAuth FAQ
----------------

At times there can be misconfigurations that take place, and
troubleshooting is needed to resolve the issue. Below are the most
common errors that may occur when configuring the *Google Calendar* for
use with Odoo.

### Production vs. testing publishing status

Choosing `Production`{.interpreted-text role="guilabel"} as the
`Publishing Status`{.interpreted-text role="guilabel"} (instead of
`Testing`{.interpreted-text role="guilabel"}) displays the following
warning message:

[OAuth is limited to 100 sensitive scope logins until the OAuth consent
screen is verified. This may require a verification process that can
take several days.]{.title-ref}

To correct this warning, navigate to the [Google API
Platform](https://console.cloud.google.com/apis/credentials/consent). If
the `Publishing Status`{.interpreted-text role="guilabel"} is
`In Production`{.interpreted-text role="guilabel"}, click
`Back to Testing`{.interpreted-text role="guilabel"} to correct the
issue.

### No test users added

If no test users are added to the
`OAuth consent screen`{.interpreted-text role="guilabel"}, then an
`Error 403:
access_denied`{.interpreted-text role="guilabel"} populates.

{.align-center}

To correct this error, return to the
`OAuth consent screen`{.interpreted-text role="guilabel"}, under `APIs &
Services`{.interpreted-text role="guilabel"}, and add test users to the
app. Add the email to be configured in Odoo.

### Application Type

When creating the credentials (OAuth *Client ID* and *Client Secret*),
if `Desktop App`{.interpreted-text role="guilabel"} is selected for the
`Application Type`{.interpreted-text role="guilabel"}, an
`Authorization Error`{.interpreted-text role="guilabel"} appears
(`Error 400:redirect_uri_mismatch`{.interpreted-text role="guilabel"}).

{.align-center}

To correct this error, delete the existing credentials, and create new
credentials, by selecting `Web Application`{.interpreted-text
role="guilabel"} for the `Application Type`{.interpreted-text
role="guilabel"}.

Then, under `Authorized redirect URIs`{.interpreted-text
role="guilabel"}, click `ADD URI`{.interpreted-text role="guilabel"},
and type:
[https://yourdbname.odoo.com/google\_account/authentication]{.title-ref}
in the field, being sure to replace *yourdbname* in the URL with the
**real** Odoo database name.

::: {.tip}
::: {.title}
Tip
:::

Ensure that the domain (used in the URI:
[https://yourdbname.odoo.com/google\_account/authentication]{.title-ref})
is the exact same domain as configured in the [web.base.url]{.title-ref}
system parameter.

Access the [web.base.url]{.title-ref} by activating
`developer mode <developer-mode>`{.interpreted-text role="ref"}, and
navigating to
`Settings app --> Technical header menu --> Parameters section --> System
Parameters`{.interpreted-text role="menuselection"}.
:::
