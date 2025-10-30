# File: /content/odoo_doc17.0/fr/content/applications/general/users/google.md

Google Sign-In Authentication
=============================

The *Google Sign-In Authentication* is a useful function that allows
Odoo users to sign in to their database with their Google account.

This is particularly helpful if the organization uses Google Workspace,
and wants employees within the organization to connect to Odoo using
their Google Accounts.

::: {.warning}
::: {.title}
Warning
:::

Databases hosted on Odoo.com should not use Oauth login for the owner or
administrator of the database as it would unlink the database from their
Odoo.com account. If Oauth is set up for that user, the database will no
longer be able to be duplicated, renamed or otherwise managed from the
Odoo.com portal.
:::

::: {.seealso}
\- `/applications/productivity/calendar/google`{.interpreted-text
role="doc"} - `../email_communication/google_oauth`{.interpreted-text
role="doc"}
:::

Configuration {#google-sign-in/configuration}
-------------

The integration of the Google sign-in function requires configuration
both on Google *and* Odoo.

### Google API Dashboard {#google-sign-in/api}

1.  Go to the [Google API
    Dashboard](https://console.developers.google.com/).

2.  Make sure the right project is opened. If there isn\'t a project
    yet, click on `Create
    Project`{.interpreted-text role="guilabel"}, fill out the project
    name and other details of the company, and click on
    `Create`{.interpreted-text role="guilabel"}.

    {.align-center}

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Choose the name of the company from the drop-down menu.
    :::

#### OAuth consent screen {#google-sign-in/oauth}

1.  On the left side menu, click on
    `OAuth consent screen`{.interpreted-text role="menuselection"}.

    {.align-center}

2.  Choose one of the options (`Internal`{.interpreted-text
    role="guilabel"} / `External`{.interpreted-text role="guilabel"}),
    and click on `Create`{.interpreted-text role="guilabel"}.

    {.align-center}

    ::: {.warning}
    ::: {.title}
    Warning
    :::

    *Personal* Gmail Accounts are only allowed to be **External** User
    Type, which means Google may require an approval, or for *Scopes* to
    be added on. However, using a *Google WorkSpace* account allows for
    **Internal** User Type to be used.

    Note, as well, that while the API connection is in the *External*
    testing mode, then no approval is necessary from Google. User limits
    in this testing mode is set to 100 users.
    :::

3.  Fill out the required details and domain info, then click on
    `Save and Continue`{.interpreted-text role="guilabel"}.

4.  On the `Scopes`{.interpreted-text role="menuselection"} page, leave
    all fields as is, and click on `Save and
    Continue`{.interpreted-text role="guilabel"}.

5.  Next, if continuing in testing mode (*External*), add the email
    addresses being configured under the `Test users`{.interpreted-text
    role="guilabel"} step by clicking on `Add Users`{.interpreted-text
    role="guilabel"}, and then the `Save and Continue`{.interpreted-text
    role="guilabel"} button. A summary of the app registration appears.

6.  Finally, scroll to the bottom, and click on
    `Back to Dashboard`{.interpreted-text role="guilabel"}.

#### Credentials {#google-sign-in/credentials}

1.  On the left side menu, click on `Credentials`{.interpreted-text
    role="menuselection"}.

    {.align-center}

2.  Click on `Create Credentials`{.interpreted-text role="guilabel"},
    and select `OAuth client ID`{.interpreted-text role="guilabel"}.

    {.align-center}

3.  Select `Web Application`{.interpreted-text role="guilabel"} as the
    `Application Type`{.interpreted-text role="guilabel"}. Now,
    configure the allowed pages on which Odoo will be redirected.

    In order to achieve this, in the
    `Authorized redirect URIs`{.interpreted-text role="guilabel"} field,
    enter the database\'s domain immediately followed by
    [/auth\_oauth/signin]{.title-ref}. For example:
    [https://mydomain.odoo.com/auth\_oauth/signin]{.title-ref}, then
    click on `Create`{.interpreted-text role="guilabel"}.

4.  Now that the *OAuth client* has been created, a screen will appear
    with the `Client ID`{.interpreted-text role="guilabel"} and
    `Client Secret`{.interpreted-text role="guilabel"}. Copy the
    `Client ID`{.interpreted-text role="guilabel"} for later, as it will
    be necessary for the configuration in Odoo, which will be covered in
    the following steps.

### Google Authentication on Odoo {#google-sign-in/auth-odoo}

#### Retrieve the Client ID {#google-sign-in/client-id}

Once the previous steps are complete, two keys are generated on the
Google API Dashboard: `Client ID`{.interpreted-text role="guilabel"} and
`Client Secret`{.interpreted-text role="guilabel"}. Copy the
`Client ID`{.interpreted-text role="guilabel"}.

{.align-center}

#### Odoo activation {#google-sign-in/odoo-activation}

1.  Go to `Odoo General Settings --> Integrations`{.interpreted-text
    role="menuselection"} and activate `OAuth
    Authentication`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Odoo may prompt the user to log-in again after this step.
    :::

2.  Go back to
    `General Settings --> Integrations --> OAuth Authentication`{.interpreted-text
    role="menuselection"}, activate the selection and
    `Save`{.interpreted-text role="guilabel"}. Next, return to
    `General Settings -->
    Integrations --> Google Authentication`{.interpreted-text
    role="menuselection"} and activate the selection. Then fill out the
    `Client ID`{.interpreted-text role="guilabel"} with the key from the
    Google API Dashboard, and `Save`{.interpreted-text role="guilabel"}.

    {.align-center}

    ::: {.note}
    ::: {.title}
    Note
    :::

    Google OAuth2 configuration can also be accessed by clicking on
    `OAuth Providers`{.interpreted-text role="guilabel"} under the
    `OAuth Authentication`{.interpreted-text role="guilabel"} heading in
    `Integrations`{.interpreted-text role="menuselection"}.
    :::

Log in to Odoo with Google {#google-sign-in/log-in}
--------------------------

To link the Google account to the Odoo profile, click on
`Log in with Google`{.interpreted-text role="guilabel"} when first
logging into Odoo.

> {.align-center}

Existing users must
`reset their password <users/reset-password>`{.interpreted-text
role="ref"} to access the `Reset Password`{.interpreted-text
role="menuselection"} page, while new users can directly click on
`Log in with
Google`{.interpreted-text role="guilabel"}, instead of choosing a new
password.

::: {.seealso}
\- [Google Cloud Platform Console Help - Setting up OAuth
2.0](https://support.google.com/cloud/answer/6158849)
:::
