# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/cdn.md

Set up a content delivery network (CDN)
=======================================

Deploying with KeyCDN {#reference/cdn/keycdn}
---------------------

A `CDN (Content Delivery Network)`{.interpreted-text role="abbr"} or
*content distribution network*, is a geographically distributed network
of servers that provides high speed internet content. The `CDN (Content
Delivery Network)`{.interpreted-text role="abbr"} provides quick,
high-quality content delivery for content-heavy websites.

This document will guide you through the setup of a
 account with an Odoo powered website.

### Create a pull zone in the KeyCDN dashboard

On the KeyCDN dashboard, start by navigating to the
`Zones`{.interpreted-text role="menuselection"} menu item on the left.
On the form, give a value to the `Zone Name`{.interpreted-text
role="guilabel"}, which will appear as part of the `CDN
(Content Delivery Network)`{.interpreted-text role="abbr"}\'s
`URL (Uniform Resource Locator)`{.interpreted-text role="abbr"}. Then,
set the `Zone
Status`{.interpreted-text role="guilabel"} to `active`{.interpreted-text
role="guilabel"} to engage the zone. For the
`Zone Type`{.interpreted-text role="guilabel"} set the value to
`Pull`{.interpreted-text role="guilabel"}, and then, finally, under the
`Pull Settings`{.interpreted-text role="guilabel"}, enter the
`Origin URL`{.interpreted-text role="guilabel"}--- this address should
be the full Odoo database `URL (Uniform Resource
Locator)`{.interpreted-text role="abbr"}.

::: {.example}
Use `https://yourdatabase.odoo.com` and replace the *yourdatabase*
subdomain prefix with the actual name of the database. A custom
`URL (Uniform Resource Locator)`{.interpreted-text role="abbr"} can be
used, as well, in place of the Odoo subdomain that was provided to the
database.
:::

{.align-center}

Under the `General Settings`{.interpreted-text role="guilabel"} heading
below the zone form, click the `Show all
settings`{.interpreted-text role="guilabel"} button to expand the zone
options. This should be the last option on the page. After expanding the
`General Settings`{.interpreted-text role="guilabel"} ensure that the
`CORS`{.interpreted-text role="guilabel"} option is
`enabled`{.interpreted-text role="guilabel"}.

Next, scroll to the bottom of the zone configuration page and
`Save`{.interpreted-text role="guilabel"} the changes. KeyCDN will
indicate that the new zone will be deployed. This can take about 10
minutes.

{.align-center}

::: {.note}
::: {.title}
Note
:::

A new `Zone URL`{.interpreted-text role="guilabel"} has been generated
for your Zone, in this example it is `pulltest-xxxxx.kxcdn.com`. This
value will differ for each database.
:::

Copy this `Zone URL`{.interpreted-text role="guilabel"} to a text editor
for later, as it will be used in the next steps.

### Configure the Odoo instance with the new zone

In the Odoo `Website`{.interpreted-text role="guilabel"} app, go to the
`Settings`{.interpreted-text role="menuselection"} and then activate the
`Content Delivery Network (CDN)`{.interpreted-text role="guilabel"}
setting and copy/paste the `Zone URL`{.interpreted-text role="guilabel"}
value from the earlier step into the `CDN Base URL`{.interpreted-text
role="guilabel"} field. This field is only visible and configurable when
the `developer mode <developer-mode>`{.interpreted-text role="ref"} is
activated.

::: {.note}
::: {.title}
Note
:::

Ensure that there are two *forward slashes* ([//]{.title-ref}) before
the `CDN Base URL`{.interpreted-text role="guilabel"} and one forward
slash ([/]{.title-ref}) after the `CDN Base URL`{.interpreted-text
role="guilabel"}.
:::

`Save`{.interpreted-text role="guilabel"} the settings when complete.

{.align-center}

Now the website is using the CDN for the resources matching the
`CDN filters`{.interpreted-text role="guilabel"} regular expressions.

In the HTML of the Odoo website, the
`CDN (content delivery network)`{.interpreted-text role="abbr"}
integration is evidenced as working properly by checking the
`URL (Uniform Resource Locators)`{.interpreted-text role="abbr"} of
images. The *CDN Base URL* value can be seen by using your web
browser\'s `Inspect`{.interpreted-text role="guilabel"} feature on the
Odoo website. Look for it\'s record by searching within the
`Network`{.interpreted-text role="guilabel"} tab inside of devtools.

{.align-center}

### Prevent security issues by activating cross-origin resource sharing (CORS)

A security restriction in some browsers (such as Mozilla Firefox and
Google Chrome) prevents a remotely linked CSS file to fetch relative
resources on this same external server.

If the `CORS (Cross-Origin Resource Sharing)`{.interpreted-text
role="abbr"} option isn\'t enabled in the `CDN
Zone`{.interpreted-text role="guilabel"}, the more obvious resulting
problem on a standard Odoo website will be the lack of *Font Awesome*
icons because the font file declared in the *Font Awesome* CSS won\'t be
loaded from the remote server.

When these cross-origin resource issues occur, a security error message
similar to the output below will appear in the web browser\'s developer
console:

`Font from origin 'http://pulltest-xxxxx.kxcdn.com' has been blocked from loading /shop:1 by Cross-Origin Resource Sharing policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://yourdatabase.odoo.com' is therefore not allowed access.`

{.align-center}

Enabling the `CORS (Cross-Origin Resource Sharing)`{.interpreted-text
role="abbr"} option in the `CDN (Content Delivery
Network)`{.interpreted-text role="abbr"} settings fixes this issue.
