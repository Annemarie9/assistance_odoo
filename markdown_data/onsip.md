# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/onsip.md

Use VoIP services in Odoo with OnSIP
====================================

::: {.important}
::: {.title}
Important
:::

OnSIP `VoIP (voice over internet protocol)`{.interpreted-text
role="abbr"} services are only available in the **United States** (US).
OnSIP `VoIP (voice over internet protocol)`{.interpreted-text
role="abbr"} services are widely available in the lower-48, contiguous
United States. In Alaska or Hawaii, charges for service can be higher.

Additionally, a `US (United States)`{.interpreted-text role="abbr"}
billing address, and `US (United States)`{.interpreted-text role="abbr"}
credit card are required to use the service.

Before setting up an account with OnSIP, the business will need to make
sure the business telephone numbers are portable to OnSIP.

OnSIP makes every attempt to work with all telephone service providers.
However, certain local or regional guidelines may preclude the
company\'s current provider from releasing the number.
:::

Introduction
------------

Odoo *VoIP* can be set up to work together with [OnSIP (Odoo Landing
Page)](https://info.onsip.com/odoo/). OnSIP is a VoIP provider. An
account is needed with OnSIP in order to use this service.

Before setting up an account with OnSIP, make sure the company\'s home
area, and the areas that will be called, are covered by OnSIP services.

After opening an OnSIP account, follow the configuration procedure below
to configure it on an Odoo database.

Configuration
-------------

To configure the Odoo database to connect to OnSIP services, first
navigate to the `Apps application`{.interpreted-text
role="menuselection"} from the main Odoo dashboard. Then, remove the
default [Apps]{.title-ref} filter from the `Search...`{.interpreted-text
role="guilabel"} bar, and search for [OnSIP]{.title-ref}.

Next, activate the `VOIP OnSIP`{.interpreted-text role="guilabel"}
module.

{.align-center}

### Odoo VoIP setting

After installing the *VOIP OnSIP* module, go to the
`Settings app`{.interpreted-text role="menuselection"}, scroll down to
the `Integrations`{.interpreted-text role="guilabel"} section, and
locate the `Asterisk (VoIP)`{.interpreted-text role="guilabel"} fields.
Then, proceed to fill in those three fields with the following
information:

-   `OnSIP Domain`{.interpreted-text role="guilabel"}: the domain that
    was assigned when creating an account on
    .
-   `WebSocket`{.interpreted-text role="guilabel"}:
    [wss://edge.sip.onsip.com]{.title-ref}
-   `VoIP Environment`{.interpreted-text role="guilabel"}:
    `Production`{.interpreted-text role="guilabel"}

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To access the OnSIP domain, navigate to 
and log in. Then, click the `Administrators`{.interpreted-text
role="guilabel"} link in the top-right of the page.

Next, in the left menu, click `Users`{.interpreted-text
role="guilabel"}, and then select any user. By default, the selected
user opens on the `User Info`{.interpreted-text role="guilabel"} tab.

Click on the `Phone Settings`{.interpreted-text role="guilabel"} tab to
reveal OnSIP configuration credentials (first column).

![Domain setting revealed (highlighted) on administrative panel of OnSIP management
console.](onsip/domain-setting.png){.align-center}
:::

### Odoo user setting

Next, the user needs to be set up in Odoo. Every user associated with an
OnSIP user **must** also be configured in the Odoo user\'s
settings/preferences.

To do that, navigate to
`Settings app --> Manage Users --> Select the User`{.interpreted-text
role="menuselection"}.

On the user form, click `Edit`{.interpreted-text role="guilabel"} to
configure the user\'s OnSIP account. Then, click the
`Preferences`{.interpreted-text role="guilabel"} tab, and scroll to the
`VoIP Configuration`{.interpreted-text role="guilabel"} section.

In this section, fill in the fields with OnSIP credentials.

Fill in the following fields with the associated credentials listed
below:

-   `Voip Username`{.interpreted-text role="guilabel"} = OnSIP
    `Username`{.interpreted-text role="guilabel"}
-   `OnSIP Auth Username`{.interpreted-text role="guilabel"} = OnSIP
    `Auth Username`{.interpreted-text role="guilabel"}
-   `VoIP Secret`{.interpreted-text role="guilabel"} = OnSIP
    `SIP Password`{.interpreted-text role="guilabel"}

::: {.tip}
::: {.title}
Tip
:::

The OnSIP extension can be found in the *User* banner line above the
tabs.
:::

When these steps are complete, navigate away from the user form in Odoo
to save the configurations.

Once saved, Odoo users can make phone calls by clicking the
`☎️ (phone)`{.interpreted-text role="guilabel"} icon in the top-right
corner of Odoo.

::: {.seealso}
Additional setup and troubleshooting steps can be found on [OnSIP\'s
knowledge base](https://support.onsip.com/hc/en-us).
:::

### Incoming calls

The Odoo database also receives incoming calls that produce pop-up
windows in Odoo. When those call pop-up windows appear, click the green
`📞 (phone)`{.interpreted-text role="guilabel"} icon to answer the call.

To ignore the call, click the red `📞 (phone)`{.interpreted-text
role="guilabel"} icon.

{.align-center}

::: {.seealso}
`voip_widget`{.interpreted-text role="doc"}
:::

### Troubleshooting

#### Missing parameters

If a *Missing Parameters* message appears in the Odoo widget, make sure
to refresh the Odoo browser window (or tab), and try again.

{.align-center}

#### Incorrect number

If an *Incorrect Number* message appears in the Odoo widget, make sure
to use the international format for the number. This means leading with
the international country code.

A country code is a locator code that allows access to the desired
country\'s phone system. The country code is dialed first, prior to the
target number. Each country in the world has its own specific country
code.

For example, [16505555555]{.title-ref} (where [1]{.title-ref} is the
international prefix for the United States).

{.align-center}

::: {.seealso}
For a list of comprehensive country codes, visit:
<https://countrycode.org>.
:::

OnSIP on mobile phone
---------------------

In order to make and receive phone calls when the user is not in front
of Odoo on their computer, a softphone app on a mobile phone can be used
in parallel with Odoo *VoIP*.

This is useful for convenient, on-the-go calls, and to make sure
incoming calls are heard. Any SIP softphone will work.

::: {.seealso}
\- `devices_integrations`{.interpreted-text role="doc"} - [OnSIP App
Download](https://www.onsip.com/app/download)
:::
