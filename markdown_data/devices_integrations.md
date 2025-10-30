# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/devices_integrations.md

Devices and integrations
========================

`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"} can
be used on many different devices, such as a computer, tablet, mobile
phone, and many more. This is helpful in that it reduces costs, and
employees can work from anywhere in the world, so long as they have a
broadband internet connection.

Odoo *VoIP* is SIP (Session Initiation Protocol) compatible, which means
it can be used with *any*
`SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
compatible application.

This document covers the process of setting up Odoo *VoIP* across
different devices and integrations.

Odoo is fully-integrated with all Odoo apps, allowing users to click
into any app, and schedule a call as an activity in the chatter.

::: {.example}
For example, in the *CRM* app, a user can click into an opportunity, and
click on `Activities`{.interpreted-text role="guilabel"} in the chatter.

Next, they can choose `Call`{.interpreted-text role="guilabel"}, and
under `Due Date`{.interpreted-text role="guilabel"}, they can select a
date.

Once they click `Save`{.interpreted-text role="guilabel"}, an activity
shows up in the chatter.

Should the `Due Date`{.interpreted-text role="guilabel"} be for today\'s
date, the activity shows up in the `VoIP
(Voice over Internet Protocol)`{.interpreted-text role="abbr"} widget.

{.align-center}
:::

Odoo VoIP (laptop/desktop computer)
-----------------------------------

The Odoo *VoIP* (Voice over Internet Protocol) module and widget can be
used from any browser on a laptop or desktop device. Simply click on the
`☎️ (phone)`{.interpreted-text role="guilabel"} icon in the upper-right
corner, while in the Odoo database, and the widget appears.

::: {.seealso}
To see how to use the
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
widget on a desktop/laptop computer, check out this documentation:
`voip_widget`{.interpreted-text role="doc"}.
:::

Odoo VoIP (tablet/mobile device)
--------------------------------

The Odoo *VoIP* app can be used on tablets and mobile phones, through
the Odoo Android or Apple IOS applications. Additionally, a mobile web
browser can be used to access the database.

::: {.warning}
::: {.title}
Warning
:::

Odoo Android and Apple IOS applications are no longer being maintained
by Odoo on the Android and Apple portals. This means Odoo support only
handles limited scopes of Odoo Android or Apple IOS support tickets.
:::

::: {.important}
::: {.title}
Important
:::

While outgoing calls can be placed using Odoo on a mobile device, be
aware that Odoo is **not** a full
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
application, and does **not** ring on incoming calls. If the user needs
to be reachable on a mobile device at all times, an app, like Zoiper,
should be used. Apps like that stay connected in the background at all
times.

For more information, see this documentation:
`voip/zoiper`{.interpreted-text role="ref"}.
:::

While in the mobile application on a mobile device/tablet, access the
Odoo *VoIP* widget, by tapping on the `☎️ (phone)`{.interpreted-text
role="guilabel"} icon in the upper-right corner. The widget appears in
the lower-left corner.

When first making a call from the tablet using the mobile application,
the user is prompted to `Allow`{.interpreted-text role="guilabel"} the
database to use the microphone. Click `Allow`{.interpreted-text
role="guilabel"} when prompted to continue with the call using the
microphone.

This step is **necessary**, whether using the mobile Odoo application or
web browser.

{.align-center}

Odoo then asks how to make the call. The two options are :
`VOIP`{.interpreted-text role="guilabel"} or `Phone`{.interpreted-text
role="guilabel"} (should the tablet be enabled for calling). Click the
box next to `Remember ?`{.interpreted-text role="guilabel"} should this
decision be the default moving forward.

{.align-center}

Here is the layout of what the Odoo *VoIP* app looks like on a mobile
device:

{.align-center}

Zoiper Lite {#voip/zoiper}
-----------

*Zoiper Lite* is a free
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
`SIP (Session Initiation
Protocol)`{.interpreted-text role="abbr"} dialer with voice and video.

To start using the *Zoiper* app, download it to the device, via the
[Zoiper download
page](https://www.zoiper.com/en/voip-softphone/download/current).

A mobile device is the most common installation, and this document
covers how to set up on the *Zoiper* IOS application. Screenshots and
steps may differ depending on the set up conditions.

After installing the *Zoiper* application on the mobile phone, open the
application, and tap on `Settings`{.interpreted-text role="guilabel"}.
Navigate to `Accounts`{.interpreted-text role="menuselection"}, and tap
on the `+ (plus)`{.interpreted-text role="guilabel"} icon to add an
account.

If the `VoIP (Voice over Internet Protocol)`{.interpreted-text
role="abbr"} account is already set up, then click
`Yes`{.interpreted-text role="guilabel"}. This means an account username
and password has already been produced.

{.align-center}

Next, tap on `Select a provider`{.interpreted-text role="guilabel"}. On
the screen that populates, tap `Country`{.interpreted-text
role="guilabel"}, in the upper-right corner, to narrow the providers
down to a specific country. Choose the country for the provider that is
being configured, then find the `Provider`{.interpreted-text
role="guilabel"}, and select it.

::: {.example}
If the provider being configured is *Axivox*, then select
`Belgium`{.interpreted-text role="guilabel"}. Then, choose
`Axivox`{.interpreted-text role="guilabel"} as the provider.
:::

{.align-center}

Under `SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
options, enter the `Account name`{.interpreted-text role="guilabel"},
`Domain`{.interpreted-text role="guilabel"},
`Username`{.interpreted-text role="guilabel"}, and
`Password`{.interpreted-text role="guilabel"}. All this information
varies, based on the account.

::: {.tip}
::: {.title}
Tip
:::

To access this information, via the *Axivox* portal, navigate to
`Users --> Choose
user --> Edit --> SIP Identifiers tab`{.interpreted-text
role="menuselection"}. The `SIP username`{.interpreted-text
role="guilabel"}, `Domain`{.interpreted-text role="guilabel"},
`SIP password`{.interpreted-text role="guilabel"}, and
`Address of the proxy server`{.interpreted-text role="guilabel"} are all
present in this tab.
:::

  Zoiper Field   Axivox Field
  -------------- -------------------
  Account name   *Can be anything*
  Domain         Domain
  Username       SIP username
  Password       SIP password

Once this account information is entered, click the green
`Register`{.interpreted-text role="guilabel"} button at the top of the
screen. Once the registration information is checked, *Zoiper* populates
a message, stating `Registration Status: OK`{.interpreted-text
role="guilabel"}.

At this point, *Zoiper* is now set up to make phone calls using the
`VoIP (Voice over Internet
Protocol)`{.interpreted-text role="abbr"} service.

{.align-center}

Linphone
--------

*Linphone* is an open-source
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
`SIP (Session
Initiation Protocol)`{.interpreted-text role="abbr"} softphone, used for
voice, video, messaging (group and individual), as well as conference
calls.

To start using the *Linphone* app, download it to the device, via the
[Linphone download
page](https://new.linphone.org/technical-corner/linphone?qt-technical_corner=2#qt-technical_corner).

A mobile device is the most common installation, and this document
covers how to set up the *Linphone* IOS application. Screenshots and
steps may differ depending on the circumstances.

To begin configuring *Linphone* for use with a
`SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
provider, first open *Linphone*, and an assistant screen appears.

From this screen, select `Use SIP Account`{.interpreted-text
role="guilabel"}. Then, on the following screen, enter the
`Username`{.interpreted-text role="guilabel"},
`Password`{.interpreted-text role="guilabel"},
`Domain`{.interpreted-text role="guilabel"}, and
`Display Name`{.interpreted-text role="guilabel"}. Once complete, press
`Login`{.interpreted-text role="guilabel"}.

At this point, *Linphone* is ready to start making calls, once there is
a green button at the top of the application screen that reads,
`Connected`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

*Linphone* makes a variety of applications for mobile and desktop
devices in operating systems, such as Windows, Linux, Apple, and
Android. Because *Linphone* is an open-source project, many new updates
are released on a regular basis.

See [Linphone\'s wiki-documentation
page](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/).
:::
