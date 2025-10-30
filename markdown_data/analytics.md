# File: /content/odoo_doc17.0/fr/content/applications/websites/website/reporting/analytics.md

Website analytics
=================

Website analytics helps website owners monitor how people use their
site. It provides data on visitor demographics, behavior, and
interactions, helping improve websites and marketing strategies.

You can track your Odoo website\'s traffic using
`analytics/plausible`{.interpreted-text role="ref"} or
`analytics/google-analytics`{.interpreted-text role="ref"}. We recommend
using Plausible.io as it is privacy-friendly, lightweight, and easy to
use.

The Plausible analytics dashboard is also integrated into Odoo and can
be accessed via `Website --> Reporting --> Analytics`{.interpreted-text
role="menuselection"}.

Plausible.io {#analytics/plausible}
------------

Odoo hosts its own Plausible.io server and provides a free and
ready-to-work Plausible.io solution for **Odoo Online** databases. Odoo
automatically creates and sets up your account. You can start using it
by going to `Website --> Reporting --> Analytics`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

**If you already have a Plausible.io account** and you want to connect
it to your Odoo Online database, you must create two
[ir.config.parameters]{.title-ref} to use Plausible.io\'s servers. To do
so, enable the `developer mode <developer-mode>`{.interpreted-text
role="ref"} and go to `General Settings -->
Technical -- System Parameters`{.interpreted-text role="menuselection"}.
Click `New`{.interpreted-text role="guilabel"} and fill in the following
`Key`{.interpreted-text role="guilabel"} and `Value`{.interpreted-text
role="guilabel"} fields:

  Key                                       Value
  ----------------------------------------- ----------------------------------------------------
  [website.plausible\_script]{.title-ref}   [https://plausible.io/js/plausible.js]{.title-ref}
  [website.plausible\_server]{.title-ref}   [https://plausible.io]{.title-ref}

Then, follow the steps below to connect your existing account with
Plausible.io servers.
:::

If your database is hosted on **Odoo.sh** or **On-premise**, or if you
wish to use your own Plausible.io account, proceed as follows:

1.  Create or sign in to a Plausible account using the following link:
    <https://plausible.io/register>.

2.  If you are creating a new account, go through the registration and
    activation steps. When asked to provide your website details, add
    its `Domain`{.interpreted-text role="guilabel"} without including
    [www]{.title-ref} (e.g., [example.odoo.com]{.title-ref}) and change
    the `Reporting Timezone`{.interpreted-text role="guilabel"} if
    necessary. Click `Add snippet`{.interpreted-text role="guilabel"} to
    proceed to the next step. Ignore the
    `Add JavaScript snippet`{.interpreted-text role="guilabel"}
    instructions and click `Start collecting data`{.interpreted-text
    role="guilabel"}.

3.  Once done, click the Plausible logo in the upper-left part of the
    page to access your ,
    then click the gear icon next to the website.

    

4.  In the sidebar, select `Visibility`{.interpreted-text
    role="guilabel"}, then click `+ New link`{.interpreted-text
    role="guilabel"}.

5.  Enter a `Name`{.interpreted-text role="guilabel"}, leave the
    `Password`{.interpreted-text role="guilabel"} field empty, as the
    Plausible analytics dashboard integration in Odoo doesn\'t support
    it, then click `Create shared link`{.interpreted-text
    role="guilabel"}.

    

6.  Copy the shared link.

    

7.  In Odoo, go to
    `Website --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.

8.  In the `SEO`{.interpreted-text role="guilabel"} section, enable
    `Plausible Analytics`{.interpreted-text role="guilabel"}, then paste
    the `Shared Link`{.interpreted-text role="guilabel"} and click
    `Save`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If you have
`multiple websites <../configuration/multi_website>`{.interpreted-text
role="doc"}, add your websites to your Plausible.io account by going to
<https://plausible.io/sites> and clicking `+ Add
website`{.interpreted-text role="guilabel"}. In Odoo, in the **Website
settings**, make sure to select the website in the
`Settings of Website`{.interpreted-text role="guilabel"} field before
pasting the `Shared link`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

Odoo automatically pushes two custom goals: [Lead
Generation]{.title-ref} and [Shop]{.title-ref}.
:::

::: {.seealso}

:::

Google Analytics {#analytics/google-analytics}
----------------

To follow your Odoo website\'s traffic with Google Analytics:

1.  Create or sign in to a Google account using the following link:
    <https://analytics.google.com>.

2.  -   If you are setting up Google Analytics for the first time, click
        `Start measuring`{.interpreted-text role="guilabel"} and go
        through the account creation step.

    -   If you already have a Google Analytics account, sign in and
        click the gear icon in the bottom-left corner of the page to
        access the **Admin** page. Then, click `+ Create
        Property`{.interpreted-text role="guilabel"}.

        

3.  Complete the next steps: [property
    creation](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property),
    business details, and business objectives.

4.  When you reach the **Data collection** step, choose the
    `Web`{.interpreted-text role="guilabel"} platform.

    

5.  Set up your data stream: Specify your
    `Website URL`{.interpreted-text role="guilabel"} and a
    `Stream name`{.interpreted-text role="guilabel"}, then click
    `Create stream`{.interpreted-text role="guilabel"}.

6.  Copy the `Measurement ID`{.interpreted-text role="guilabel"}.

    

7.  In Odoo, go to
    `Website --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.

8.  In the `SEO`{.interpreted-text role="guilabel"} section, enable
    `Google Analytics`{.interpreted-text role="guilabel"}, then paste
    the `Measurement ID`{.interpreted-text role="guilabel"} and click
    `Save`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If you have
`multiple websites <../configuration/multi_website>`{.interpreted-text
role="doc"} with separate domains, it is recommended to create [one
property](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property)
per domain. In Odoo, in the **Website settings**, make sure to select
the website in the `Settings of Website`{.interpreted-text
role="guilabel"} field before pasting the
`Measurement ID`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
[Google documentation on setting up Analytics for a
website](https://support.google.com/analytics/answer/1008015?hl=en/)
:::

Google Tag Manager {#analytics/google-tag-manager}
------------------

`GTM (Google Tag Manager)`{.interpreted-text role="abbr"} is a tag
management system that allows you to easily update measurement codes and
related code fragments, collectively known as tags on your website or
mobile app, directly through the code injector.

::: {.warning}
::: {.title}
Warning
:::

\- Some GTM tags use data layers (e.g., advanced eCommerce tracking data
layers) to retrieve variables and send them to Google Analytics. Data
layers are currently not managed in Odoo. - Google Tag Manager may not
be compliant with local data protection regulations.
:::

To use GTM, proceed as follows:

1.  Create or sign in to a Google account by going to
    <https://tagmanager.google.com/>.

2.  In the `Accounts`{.interpreted-text role="guilabel"} tab, click
    `Create account`{.interpreted-text role="guilabel"}.

3.  Enter an `Account Name`{.interpreted-text role="guilabel"} and
    select the account\'s `Country`{.interpreted-text role="guilabel"}.

4.  Enter your website\'s URL in the `Container name`{.interpreted-text
    role="guilabel"} field and select the `Target
    platform`{.interpreted-text role="guilabel"}.

5.  Click `Create`{.interpreted-text role="guilabel"} and agree to the
    Terms of Service.

6.  Copy the [\<head\>]{.title-ref} and [\<body\>]{.title-ref} codes
    from the popup window. Then, go to your website, click
    `Edit`{.interpreted-text role="guilabel"}, go to the
    `Themes`{.interpreted-text role="guilabel"} tab, scroll down to the
    `Website Settings`{.interpreted-text role="guilabel"} section, then
    click `<head>`{.interpreted-text role="guilabel"} and
    `</body>`{.interpreted-text role="guilabel"} to paste the codes.

    

::: {.note}
::: {.title}
Note
:::

The data is collected in the marketing tools used to monitor the website
(e.g., Google Analytics, Plausible, Facebook Pixel), not in Odoo.
:::
