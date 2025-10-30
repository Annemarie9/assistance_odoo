# File: /content/odoo_doc17.0/fr/content/applications/general/integrations/mail_plugins/outlook.md

Outlook Plugin
==============

Outlook allows for third-party applications to connect in order to
execute database actions from emails. Odoo has a plugin for Outlook that
allows for the creation of an opportunity from the email panel.

Configuration
-------------

The Outlook `Mail Plugin <../mail_plugins>`{.interpreted-text
role="doc"} needs to be configured both on Odoo and Outlook.

### Enable Mail Plugin {#mail-plugin/outlook/enable-mail-plugin}

First, enable the *Mail Plugin* feature in the database. Go to
`Settings --> General
Settings --> Integrations`{.interpreted-text role="menuselection"},
enable `Mail Plugin`{.interpreted-text role="guilabel"}, and
`Save`{.interpreted-text role="guilabel"} the configuration.

### Install the Outlook Plugin {#mail-plugin/outlook/install-plugin}

Download (`Save Page As --> Web Page XML only`{.interpreted-text
role="menuselection"}) the following XML file to upload later:
<https://download.odoocdn.com/plugins/outlook/manifest.xml>.

Next, open the Outlook mailbox, and select any email. After completing
this, click on the `More actions`{.interpreted-text role="guilabel"}
button in the upper right-side and select
`Get Add-ins`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For locally installed versions of Microsoft Outlook, access the
`Get Add-ins`{.interpreted-text role="guilabel"} menu item while in
preview mode (**not** with a message open). First, click on the `...
(ellipsis)`{.interpreted-text role="guilabel"} icon in the upper right
of the previewed message, then scroll down, and click on
`Get Add-ins`{.interpreted-text role="guilabel"}.
:::

Following this step, select the `My add-ins`{.interpreted-text
role="guilabel"} tab on the left-side.

{.align-center}

Under `Custom add-ins`{.interpreted-text role="guilabel"} towards the
bottom, click on `+ Add a custom add-in`{.interpreted-text
role="guilabel"}, and then on `Add from file...`{.interpreted-text
role="guilabel"}

{.align-center}

For the next step, attach the [manifest.xml]{.title-ref} file downloaded
above, and press `OK`{.interpreted-text role="guilabel"}. Next, read the
warning and click on `Install`{.interpreted-text role="guilabel"}.

{.align-center}

### Connect the database {#mail-plugin/outlook/connect-database}

Now, Outlook will be connected to the Odoo database. First, open any
email in the Outlook mailbox, click on the
`More actions`{.interpreted-text role="guilabel"} button in the upper
right-side, and select `Odoo for
Outlook`{.interpreted-text role="guilabel"}.

{.align-center}

The right-side panel can now display **Company Insights**. At the
bottom, click on `Login`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Only a limited amount of **Company Insights** (*Lead Enrichment*)
requests are available as a trial database. This feature requires
`prepaid credits <mail_plugins/pricing>`{.interpreted-text role="ref"}.
:::

::: {.tip}
::: {.title}
Tip
:::

If, after a short while, the panel is still empty, it is possible that
the browser cookie settings prevented it from loading. Note that these
settings also change if the browser is in \"Incognito\" mode.

To fix this issue, configure the browser to always allow cookies on
Odoo\'s plugin page.

For Google Chrome, change the browser cookie settings by following the
guide at: <https://support.google.com/chrome/answer/95647> and adding
[download.odoo.com]{.title-ref} to the list of
`Sites that can always use cookies`{.interpreted-text role="guilabel"}.

Once this is complete, the Outlook panel needs to be opened again.
:::

Now, enter the Odoo database URL and click on `Login`{.interpreted-text
role="guilabel"}.

{.align-center}

Next, click on `Allow`{.interpreted-text role="guilabel"} to open the
pop-up window.

{.align-center}

If the user isn\'t logged into the database, enter the credentials.
Click on `Allow`{.interpreted-text role="guilabel"} to let the Outlook
Plugin connect to the database.

{.align-center}

### Add a shortcut to the plugin {#mail-plugin/outlook/add-shortcut}

By default, the Outlook Plugin can be opened from the *More actions*
menu. However, to save time, it\'s possible to add it next to the other
default actions.

In the Outlook mailbox, click on `Settings`{.interpreted-text
role="guilabel"}, then on `View all Outlook
settings`{.interpreted-text role="guilabel"}.

{.align-center}

Now, select `Customize actions`{.interpreted-text role="guilabel"} under
`Mail`{.interpreted-text role="guilabel"}, click on `Odoo for
Outlook`{.interpreted-text role="guilabel"}, and then
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Following this step, open any email; the shortcut should be displayed.

{.align-center}

### Using the plugin

Now that the plug-in is installed and operational, all that needs to be
done to create a lead is to click on the [O]{.title-ref} \[Odoo icon\]
or navigate to `More actions`{.interpreted-text role="guilabel"} and
click on `Odoo
for Outlook`{.interpreted-text role="guilabel"}. The side panel will
appear on the right-side, and under `Opportunities`{.interpreted-text
role="guilabel"} click on `New`{.interpreted-text role="guilabel"}. A
new window with the created opportunity in the Odoo database will
populate.
