# File: /content/odoo_doc17.0/fr/content/applications/general/users/facebook.md

Facebook sign-in authentication
===============================

The *Facebook* OAuth sign-in function allows Odoo users to sign in to
their database with their Facebook account.

::: {.danger}
::: {.title}
Danger
:::

Databases housed on Odoo.com should **not** use OAuth login for the
owner or administrator of the database, as it would unlink the database
from their Odoo.com account. If OAuth is setup for that user, the
database can no longer be duplicated, renamed, or otherwise managed from
the Odoo.com portal.
:::

Meta for Developers setup
-------------------------

Go to  and log
in. Click `My
Apps`{.interpreted-text role="guilabel"}. On the
`Apps`{.interpreted-text role="guilabel"} page, click
`Create App`{.interpreted-text role="guilabel"}.

On the `Use cases`{.interpreted-text role="guilabel"} page, select
`Authenticate and request data from users with
Facebook Login`{.interpreted-text role="guilabel"}, then click
`Next`{.interpreted-text role="guilabel"}.

In the `Add an app name`{.interpreted-text role="guilabel"} field, enter
[Odoo Login OAuth]{.title-ref}, or a similar title.

::: {.note}
::: {.title}
Note
:::

The `App contact email`{.interpreted-text role="guilabel"} automatically
defaults to the email address associated with the Meta account. If this
email address is not regularly monitored, it may be wise to use another
email address.
:::

Click `Next`{.interpreted-text role="guilabel"}. Review the
`Publishing requirements`{.interpreted-text role="guilabel"}, the `Meta
Platform Terms`{.interpreted-text role="guilabel"}, and
`Developer Policies`{.interpreted-text role="guilabel"}. Then, click
`Create app`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Clicking `Create app`{.interpreted-text role="guilabel"} may require
password re-entry.
:::

### Customize app

After the new app is created, the `Dashboard`{.interpreted-text
role="guilabel"} page appears, with a list of steps to be completed
before the app can be published. From here, click
`Customize adding a Facebook
Login button`{.interpreted-text role="guilabel"}.

{.align-center}

On the `Customize`{.interpreted-text role="guilabel"} page, click
`Settings`{.interpreted-text role="guilabel"}.

In the `Valid OAuth Redirect URIs`{.interpreted-text role="guilabel"}
field, enter [https://\<odoo base url\>/auth\_oauth/signin]{.title-ref},
replacing [\<odoo base url\>]{.title-ref} with the URL of the applicable
database.

::: {.example}
If a database has the URL [https://example.odoo.com]{.title-ref}, the
URL [https://example.odoo.com/auth\_oauth/signin]{.title-ref} would be
entered in the `Valid OAuth
Redirect URIs`{.interpreted-text role="guilabel"} field.
:::

Click `Save changes`{.interpreted-text role="guilabel"} when finished.

### Configure settings

At the far left of the page, click
`App settings --> Basic`{.interpreted-text role="menuselection"}. This
page contains additional settings that are required before the app can
be submitted for approval.

In the `Privacy Policy URL`{.interpreted-text role="guilabel"} field,
enter [https://www.odoo.com/privacy]{.title-ref}.

::: {.note}
::: {.title}
Note
:::

<https://www.odoo.com/privacy> is the default privacy policy for
databases hosted on Odoo.com.
:::

Click the `App Icon`{.interpreted-text role="guilabel"} field to open a
file upload window. From here, select and upload an app icon.

In the `User data deletion`{.interpreted-text role="guilabel"} field,
enter
[https://www.odoo.com/documentation/17.0/administration/odoo\_accounts.html]{.title-ref}.

::: {.note}
::: {.title}
Note
:::

This document provides instructions on how a user can delete their Odoo
account.
:::

Lastly, click the `Category`{.interpreted-text role="guilabel"} field,
and select `Business and pages`{.interpreted-text role="guilabel"} from
the drop-down menu.

Click `Save changes`{.interpreted-text role="guilabel"}.

{.align-center}

### Capture app ID {#users/app-id}

After the app is created, and approved, select and copy the
`App ID`{.interpreted-text role="guilabel"}. Paste this information on a
clipboard or notepad file, as it is needed in a later step to complete
the setup.

### Publish

On the left side of the page, click `Publish`{.interpreted-text
role="guilabel"}. Depending on the status of the connected Facebook
account, additional verification and testing steps may be required, and
are listed on this page.

After reviewing the information, click `Publish`{.interpreted-text
role="guilabel"}.

::: {.seealso}
Additional information regarding Meta App Development, including further
details on building, testing, and use cases, can be found in the [Meta
for developers
documentation](https://developers.facebook.com/docs/development).
:::

Odoo setup
----------

First, activate
`Developer mode <developer-mode/activation>`{.interpreted-text
role="ref"}.

Navigate to the `Settings app`{.interpreted-text role="menuselection"},
and scroll down to the `Integrations`{.interpreted-text role="guilabel"}
section. There, tick the checkbox labeled,
`OAuth Authentication`{.interpreted-text role="guilabel"}. Click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

Then, sign in to the database once the login screen loads.

After successfully logging in, navigate to
`Settings app --> Users & Companies -->
OAuth Providers`{.interpreted-text role="menuselection"}. Click
`Facebook Graph`{.interpreted-text role="guilabel"}.

In the `Client ID`{.interpreted-text role="guilabel"} field, enter the
`App ID <users/app-id>`{.interpreted-text role="ref"} from the previous
section, then tick the `Allowed`{.interpreted-text role="guilabel"}
checkbox.

{.align-center}
