# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/axivox_config.md

VoIP services in Odoo with Axivox
=================================

Introduction
------------

Odoo VoIP (Voice over Internet Protocol) can be set up to work together
with . In that case, an Asterisk server
is **not** necessary, as the infrastructure is hosted and managed by
Axivox.

To use this service, 
to open an account. Before doing so, verify that Axivox covers the
company\'s area, along with the areas the company\'s users wish to call.

Configuration
-------------

To configure Axivox in Odoo, go to the `Apps`{.interpreted-text
role="menuselection"} application, and search for [VoIP]{.title-ref}.
Then, install the `VoIP`{.interpreted-text role="guilabel"} module.

Next, go to
`Settings app --> General Settings --> Integrations section`{.interpreted-text
role="menuselection"}, and fill out the
`Asterisk (VoIP)`{.interpreted-text role="guilabel"} field:

-   `OnSIP Domain`{.interpreted-text role="guilabel"}: set the domain
    created by Axivox for the account (e.g.,
    [yourcompany.axivox.com]{.title-ref})
-   `WebSocket`{.interpreted-text role="guilabel"}: type in
    [wss://pabx.axivox.com:3443]{.title-ref}
-   `VoIP Environment`{.interpreted-text role="guilabel"}: set as
    `Production`{.interpreted-text role="guilabel"}

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Access the domain on the Axivox administrative panel by navigating to
<https://manage.axivox.com/>. After logging into the portal, go to
`Users -->
Edit (next to any user) --> SIP Identifiers tab --> Domain`{.interpreted-text
role="menuselection"}.
:::

### Configure VoIP user in Odoo

Next, the user is configured in Odoo, which **must** take place for
every Axivox/Odoo user using VoIP.

In Odoo, go to
`Settings app --> Users & Companies --> Users`{.interpreted-text
role="menuselection"}, then open the desired user\'s form to configure
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}.
Under the `Preferences`{.interpreted-text role="guilabel"} tab, fill out
the `VOIP Configuration`{.interpreted-text role="guilabel"} section:

-   `VoIP username`{.interpreted-text role="guilabel"} /
    `Extension number`{.interpreted-text role="guilabel"}: (Axivox)
    `SIP username`{.interpreted-text role="guilabel"}
-   `OnSip Auth Username`{.interpreted-text role="guilabel"}: (Axivox)
    `SIP username`{.interpreted-text role="guilabel"}
-   `VoIP Secret`{.interpreted-text role="guilabel"}: (Axivox)
    `SIP Password`{.interpreted-text role="guilabel"}
-   `Call from another device`{.interpreted-text role="guilabel"}:
    option to always transfer phone calls to handset
-   `External device number`{.interpreted-text role="guilabel"}: SIP
    external phone extension
-   `Reject incoming calls`{.interpreted-text role="guilabel"}: option
    to reject all incoming calls
-   `How to place calls on mobile`{.interpreted-text role="guilabel"}:
    method to make calls on a mobile device

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Access the domain on the Axivox administrative panel by navigating to
<https://manage.axivox.com/>. After logging into the portal, go to
`Users -->
Edit (next to the user) --> SIP Identifiers tab --> SIP username / SIP password`{.interpreted-text
role="menuselection"}.

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

When entering the `SIP Password`{.interpreted-text role="guilabel"} into
the user\'s `Preferences`{.interpreted-text role="guilabel"} tab, this
value **must** be typed out manually and **not** pasted in. Pasting in
causes a [401 server rejection error]{.title-ref}.
:::
