# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/address_autocomplete.md

Address autocomplete
====================

You can use the Google Places API on your website to ensure that your
users\' delivery addresses exist and are understood by the carrier. The
Google Places API allows developers to access detailed information about
places using HTTP requests. The autocompletion predicts a list of places
when the user starts typing the address.



::: {.seealso}
\- 
- [Google Developers Documentation: Google Places
API](https://developers.google.com/maps/documentation/places/web-service/autocomplete)
:::

To do so, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and enable
`Address Autocomplete`{.interpreted-text role="guilabel"} in the
`SEO`{.interpreted-text role="guilabel"} section.



Insert your `Google Places API key`{.interpreted-text role="guilabel"}
in the `API Key`{.interpreted-text role="guilabel"} field. If you don\'t
have one, create yours on the [Google Cloud
Console](https://console.cloud.google.com/getting-started) and follow
these steps.

Step 1: Enable the Google Places API {#address_autocomplete/generate_api_key}
------------------------------------

**Create a New Project:** To enable the **Google Places API**, you first
need to create a project. To do so, click
`Select a project`{.interpreted-text role="guilabel"} in the top left
corner, `New Project`{.interpreted-text role="guilabel"}, and follow the
prompts to set up your project.

**Enable the Google Places API:** Go to the
`Enabled APIs & Services`{.interpreted-text role="guilabel"} and click
`+ ENABLE APIS AND SERVICES.`{.interpreted-text role="guilabel"} Search
for `"Places API"`{.interpreted-text role="guilabel"} and select it.
Click on the `"Enable"`{.interpreted-text role="guilabel"} button.

::: {.note}
::: {.title}
Note
:::

Google\'s pricing depends on the number of requests and their
complexity.
:::

Step 2: Create API Credentials
------------------------------

Go to [APIs & Services \--\>
Credentials](https://console.cloud.google.com/apis/credentials).

**Create credentials:** To create your credentials, go to
`Credentials`{.interpreted-text role="guilabel"}, click
`Create Credentials`{.interpreted-text role="guilabel"}, and select
`API key`{.interpreted-text role="guilabel"}.

::: {.admonition}
Restrict the API Key (Optional)

For security purposes, you can restrict the usage of your API key. You
can go to the `API restrictions`{.interpreted-text role="guilabel"}
section to specify which APIs your key can access. For the Google Places
API, you can restrict it to only allow requests from specific websites
or apps.
:::

::: {.important}
::: {.title}
Important
:::

\- Save Your API Key: copy your API key and securely store it. - Do not
share it publicly or expose it in client-side code.
:::
