# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/conference_calls.md

Conference calls
================

Conference calls help employees connect quickly and efficiently, so
matters can be discussed in an open forum of sorts. Attendees can be
limited, via a sign-in code. That way, confidential matters stay
private.

This document covers the configuration of conference calls in Axivox for
use in Odoo *VoIP*.

Add a virtual conference
------------------------

To add a virtual conference room, navigate to the [Axivox management
console](https://manage.axivox.com). After logging in, click on
`Conferences`{.interpreted-text role="guilabel"} in the menu on the
left.

Next, click the green button labeled,
`Add a conference`{.interpreted-text role="guilabel"}, and a
`New conference`{.interpreted-text role="guilabel"} form appears.

{.align-center}

From here, fill in the `Name`{.interpreted-text role="guilabel"} field,
and set an `Internal extension`{.interpreted-text role="guilabel"}.

The internal extension is what everyone in the network uses to quickly
dial into the conference call, instead of typing in the whole phone
number.

::: {.tip}
::: {.title}
Tip
:::

Pick a number between three and five digits long, making it easy to
remember and dial.
:::

Next, set the `Access code`{.interpreted-text role="guilabel"}, if the
conference room requires security. This is a password to get into the
conference, once the extension for the conference is dialed. Immediately
after dialing the extension, a digital receptionist prompts for the
`Access code`{.interpreted-text role="guilabel"}.

In the `Administrator extension`{.interpreted-text role="guilabel"}
field, click the drop-down menu, and select the user\'s extension that
manages the call.

Finally, in the
`Wait for the administrator to start the conference`{.interpreted-text
role="guilabel"} field, click the drop-down menu, and select
`Yes`{.interpreted-text role="guilabel"} or `No`{.interpreted-text
role="guilabel"}.

Should the selection be `Yes`{.interpreted-text role="guilabel"}, then
nobody is allowed to utilize the virtual conference room until the
administrator is present, and logged into the conference call.

When all fields are filled in, be sure to `Save`{.interpreted-text
role="guilabel"} the configuration. Then, click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner to implement the change in production.

Upon doing so, the conference is added, and the Axivox administrator has
the option to `Delete`{.interpreted-text role="guilabel"} or
`Edit`{.interpreted-text role="guilabel"} the conference from the Axivox
`Conference`{.interpreted-text role="guilabel"} main dashboard.

To invite an Axivox user to a specific conference call, click
`Invite`{.interpreted-text role="guilabel"} to the right of the desired
conference, and proceed to enter the extension or phone number of the
invitee in the pop-up window that appears.

Once the extension or number is added into the
`Please enter the phone number of the
person you want to invite`{.interpreted-text role="guilabel"} field,
click the green `Invite`{.interpreted-text role="guilabel"} button, and
the recipient immediately receives a phone call, automatically linking
them to the conference.

{.align-center}

Incoming numbers
----------------

To open a conference to a wider audience, an Axivox conference can be
linked to *Incoming numbers*.

To do that, log into the [Axivox management
console](https://manage.axivox.com), and click
`Incoming numbers`{.interpreted-text role="guilabel"} in the menu on the
left.

On the `Incoming numbers`{.interpreted-text role="guilabel"} dashboard,
click `Edit`{.interpreted-text role="guilabel"} to the far-right of the
`Number`{.interpreted-text role="guilabel"} to which the conference
should be attached.

Then, under the first field, labeled,
`Destination type for voice call`{.interpreted-text role="guilabel"},
click the drop-down menu, and select `Conference`{.interpreted-text
role="guilabel"}.

Next, in the `Conference`{.interpreted-text role="guilabel"} field,
click the drop-down menu, and select the specific conference that should
be attached to this incoming number.

Now, whenever this incoming number is dialed, the caller is let into the
conference, if there is not an `Access code`{.interpreted-text
role="guilabel"} required. If there *is* an
`Access code`{.interpreted-text role="guilabel"} required, the caller is
then prompted to enter the `Access code`{.interpreted-text
role="guilabel"} to enter the conference.

Start call in Odoo
------------------

Anywhere in the Odoo database, open the *VoIP* widget, by clicking the
`☎️ (phone)`{.interpreted-text role="guilabel"} icon, located in the
upper-right corner. Then, dial the specific extension number for the
conference, and click the `📞 (phone)`{.interpreted-text role="guilabel"}
icon.

{.align-center}

Once the digital receptionist answers, enter the
`Access code`{.interpreted-text role="guilabel"} (if needed), and press
the `# (pound)`{.interpreted-text role="guilabel"} icon/key.
