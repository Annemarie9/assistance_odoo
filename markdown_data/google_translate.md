# File: /content/odoo_doc17.0/fr/content/applications/general/integrations/google_translate.md

Google Translate
================

*Google Translate* can be used to translate user generated text in the
Odoo chatter.

Google API console
------------------

A majority of the setup for integrating *Google Translate* into Odoo is
done with the *Google API console*. Once the following processes are
complete, an *API key* is created to input in Odoo.

::: {.seealso}
[Google Translate setup on
Google](https://cloud.google.com/translate/docs/setup)
:::

### Create a new project

To get started, go to the [Google API
Console](https://console.developers.google.com). Then, log in with a
*Google Workspace* account, if there is one. If not, log in with a
personal Gmail account (this should match the email address that has
billing attached to it).

Next, click `Create Project`{.interpreted-text role="guilabel"} on the
far-right of the `OAuth consent screen`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If the *Google API Console* has existing projects, click the drop-down
menu next to the `Google Cloud`{.interpreted-text role="guilabel"} icon,
and a pop-over window appears. Next, click
`New Project`{.interpreted-text role="guilabel"} top-right of the
pop-over window.
:::

On the `New Project`{.interpreted-text role="guilabel"} screen, rename
the `Project name`{.interpreted-text role="guilabel"} to [Odoo
Translate]{.title-ref}, and browse for the `Location`{.interpreted-text
role="guilabel"}. Set the `Location`{.interpreted-text role="guilabel"}
as the *Google Workspace organization*. If a personal Gmail account is
being used, leave the `Location`{.interpreted-text role="guilabel"} as
`No Organization`{.interpreted-text role="guilabel"}.

{.align-center}

Click on `Create`{.interpreted-text role="guilabel"} to finish this
step.

### API library

Next, the *Cloud Translation API* needs to be installed on this
newly-created project. To do that, click `Library`{.interpreted-text
role="menuselection"} in the left menu. Then, search the term [Cloud
Translation API]{.title-ref}, and click into the result. This should be
a *Google Enterprise API* labeled `Cloud Translation
API`{.interpreted-text role="guilabel"}.

Click `Enable`{.interpreted-text role="guilabel"} to install the library
on this project.

::: {.important}
::: {.title}
Important
:::

Using the *Google Translate* API **requires** a current billing account
with .
:::

Once a billing account is setup with *Google* and the library is
enabled, click `Manage`{.interpreted-text role="guilabel"} to finish
configuration on the API.

### Create credentials

Now that the project is set up, and the *Cloud Translation API* is
enabled, credentials **must** be created. This includes the *API key*.

To begin this process, click `Credentials`{.interpreted-text
role="menuselection"} in the left sidebar menu.

Then, click `Create Credentials`{.interpreted-text role="guilabel"} in
the top menu, and select `API key`{.interpreted-text role="guilabel"}
from the drop-down menu.

{.align-center}

Copy the `API key`{.interpreted-text role="guilabel"} for use in the
next section.

::: {.important}
::: {.title}
Important
:::

For security purposes, the usage of the *API key* can be restricted.

To do that, go to the *API restrictions* by clicking on
`Edit API key`{.interpreted-text role="guilabel"} in the pop-over
window, or by clicking on the listed API key on the
`Credentials`{.interpreted-text role="guilabel"} page. From here, key
restrictions can be set. This includes setting an application to
restrict the use of the API key, and whether this API key can call any
API.

It is recommended that the Odoo *Translate API* be restricted to
**only** allow requests from the configured Odoo database and to the
*Cloud Translation API*.

To add the website restriction, click `Websites`{.interpreted-text
role="guilabel"}, under the `Set an
application restriction`{.interpreted-text role="guilabel"}. Then, enter
the address of the database *Google Translate* is being used in, by
clicking on `Add`{.interpreted-text role="guilabel"}. Lastly, add the
`URL (Uniform Resource Locator)`{.interpreted-text role="abbr"}, and
click `Done`{.interpreted-text role="guilabel"}.

To restrict use of the key to a selected API, first, select
`Restrict key`{.interpreted-text role="guilabel"}, under the
`API restrictions`{.interpreted-text role="guilabel"} section. Then use
the drop-down menu to choose the API being configured (*Cloud
Translation API*).
:::

::: {.tip}
::: {.title}
Tip
:::

\- Save the API key: copy the API key and store it somewhere secure. -
Do **not** share the API key publicly or expose it in client-side code.
:::

Odoo configuration
------------------

To access the integration in Odoo, navigate to the
`Settings app --> Discuss
section`{.interpreted-text role="menuselection"}. Enter the API key into
the field labeled `Message Translation`{.interpreted-text
role="guilabel"}. Then, `Save`{.interpreted-text role="guilabel"} the
settings, and *Google Translate* can be used in any chatter throughout
the database.

{.align-center}

Translate chatter
-----------------

To translate a user\'s text from another language, click the
`... (three dot)`{.interpreted-text role="guilabel"} icon menu to the
right of the chatter. Then, select `Translate`{.interpreted-text
role="guilabel"}. The content translates to the *language* set on the
user\'s preferences.

{.align-center}

::: {.seealso}
`language/install`{.interpreted-text role="ref"}
:::
