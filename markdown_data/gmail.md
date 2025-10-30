# File: /content/odoo_doc17.0/fr/content/applications/general/integrations/mail_plugins/gmail.md

Gmail Plugin
============

The *Gmail Plugin* integrates an Odoo database with a Gmail inbox, so
users can keep track of all their work between Gmail and Odoo, without
losing any information.

Odoo Online users
-----------------

For databases hosted on Odoo Online (or Odoo.sh), follow the steps below
to configure the Gmail Plugin.

### Install the Gmail Plugin

First, log in to the Gmail account that the user wishes to connect to
Odoo.

From the Gmail inbox, click the plus sign icon on the right side panel
to get add-ons. If the side panel is not visible, click on the arrow
icon at the bottom right corner of the inbox to reveal it.

{.align-center}

Then, use the search bar to search for [Odoo]{.title-ref} and locate the
`Odoo Inbox Addin`{.interpreted-text role="guilabel"}.

{.align-center}

Or, go directly to the `Odoo Inbox Addin`{.interpreted-text
role="guilabel"} page on the [Google Workspace
Marketplace](https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275).

Once the plugin is located, click `Install`{.interpreted-text
role="guilabel"}. Then, click `Continue`{.interpreted-text
role="guilabel"} to start the installation.

Next, select which Gmail account the user wishes to connect to Odoo.
Then click `Allow`{.interpreted-text role="guilabel"} to let Odoo access
the Google account. Google will then show a pop-up window confirming
that the installation was successful.

### Configure the Odoo database

The `Mail Plugin`{.interpreted-text role="guilabel"} feature must be
enabled in the Odoo database in order to use the Gmail Plugin. To enable
the feature, go to `Settings --> General Settings`{.interpreted-text
role="menuselection"}. Under the `Integrations`{.interpreted-text
role="guilabel"} section, activate `Mail Plugin`{.interpreted-text
role="guilabel"}, and then click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

### Configure the Gmail inbox

In the Gmail inbox, a purple Odoo icon is now visible on the right side
panel. Click on the Odoo icon to open up the Odoo plugin window. Then,
click on any email in the inbox. Click
`Authorize Access`{.interpreted-text role="guilabel"} in the plugin
window to grant Odoo access to the Gmail inbox.

{.align-center}

Next, click `Login`{.interpreted-text role="guilabel"}. Then, enter the
URL of the Odoo database that the user wishes to connect to the Gmail
inbox, and log in to the database.

::: {.note}
::: {.title}
Note
:::

Use the general URL for the database, not the URL of a specific page in
the database. For example, use [https://mycompany.odoo.com]{.title-ref},
not [https://mycompany.odoo.com/web\#cids=1&action=menu]{.title-ref}.
:::

Finally, click `Allow`{.interpreted-text role="guilabel"} to let Gmail
access the Odoo database. The browser will then show a
`Success!`{.interpreted-text role="guilabel"} message. After that, close
the window. The Gmail inbox and Odoo database are now connected.

Odoo On-Premise users
---------------------

For databases hosted on servers other than Odoo Online (or Odoo.sh),
follow the steps below to configure the Gmail Plugin.

::: {.note}
::: {.title}
Note
:::

As part of their security guidelines, Google requires add-on creators to
provide a list of URLs that can be used in actions and redirections
launched by the add-on. This protects users by ensuring, for example,
that no add-on redirects users toward a malicious website. (Read more on
[Google Apps
Script](https://developers.google.com/apps-script/manifest/allowlist-url).)

Since Odoo can only list the [odoo.com]{.title-ref} domain and not every
on-premise customer\'s unique server domain, on-premise customers cannot
install the Gmail Plugin from the Google Workspace Marketplace.
:::

### Install the Gmail Plugin

First, access the [GitHub
repository](https://github.com/odoo/mail-client-extensions) for the Odoo
Mail Plugins. Next, click on the green `Code`{.interpreted-text
role="guilabel"} button. Then, click `Download ZIP`{.interpreted-text
role="guilabel"} to download the Mail Plugin files onto the user\'s
computer.

{.align-center}

Open the ZIP file on the computer. Then, go to
`mail-client-extensions-master -->
gmail --> src --> views`{.interpreted-text role="menuselection"}, and
open the `login.ts`{.interpreted-text role="file"} file using any text
editor software, such as Notepad (Windows), TextEdit (Mac), or Visual
Studio Code.

Delete the following three lines of text from the
`login.ts`{.interpreted-text role="file"} file:

``` {.}
if (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
     return notify("The URL must be a subdomain of odoo.com");
}
```

This removes the [odoo.com]{.title-ref} domain constraint from the Gmail
Plugin program.

Next, in the ZIP file, go to
`mail-client-extensions-master --> gmail`{.interpreted-text
role="menuselection"}, and open the file called
`appsscript.json`{.interpreted-text role="guilabel"}. In the
`urlFetchWhitelist`{.interpreted-text role="guilabel"} section, replace
all the references to [odoo.com]{.title-ref} with the Odoo customer\'s
unique server domain.

Then, in the same `gmail`{.interpreted-text role="guilabel"} folder,
open the file called `README.md`{.interpreted-text role="guilabel"}.
Follow the instructions in the `README.md`{.interpreted-text
role="guilabel"} file to push the Gmail Plugin files as a Google
Project.

::: {.note}
::: {.title}
Note
:::

The computer must be able to run Linux commands in order to follow the
instructions on the `README.md`{.interpreted-text role="guilabel"} file.
:::

After that, share the Google Project with the Gmail account that the
user wishes to connect to Odoo. Then, click `Publish`{.interpreted-text
role="guilabel"} and `Deploy from manifest`{.interpreted-text
role="guilabel"}. Lastly, click `Install the add-on`{.interpreted-text
role="guilabel"} to install the Gmail Plugin.

### Configure the Odoo database

The `Mail Plugin`{.interpreted-text role="guilabel"} feature must be
enabled in the Odoo database in order to use the Gmail Plugin. To enable
the feature, go to `Settings --> General Settings`{.interpreted-text
role="menuselection"}. Under the `Integrations`{.interpreted-text
role="guilabel"} section, activate `Mail Plugin`{.interpreted-text
role="guilabel"}, and then click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

### Configure the Gmail inbox

In the Gmail inbox, a purple Odoo icon is now visible on the right side
panel. Click on the Odoo icon to open up the Odoo plugin window. Then,
click on any email in the inbox. Click
`Authorize Access`{.interpreted-text role="guilabel"} in the plugin
window to grant Odoo access to the Gmail inbox.

{.align-center}

Next, click `Login`{.interpreted-text role="guilabel"}. Then, enter the
URL of the Odoo database that the user wishes to connect to the Gmail
inbox, and log in to the database.

::: {.note}
::: {.title}
Note
:::

Use the general URL for the database, not the URL of a specific page in
the database. For example, use [https://mycompany.odoo.com]{.title-ref},
not [https://mycompany.odoo.com/web\#cids=1&action=menu]{.title-ref}.
:::

Finally, click `Allow`{.interpreted-text role="guilabel"} to let Gmail
access the Odoo database. The browser will then show a
`Success!`{.interpreted-text role="guilabel"} message. After that, close
the window. The Gmail inbox and Odoo database are now connected.
