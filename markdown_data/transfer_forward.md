# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/transfer_forward.md

Make, receive, transfer, and forward calls
==========================================

Calling prospective clients, customers, or colleagues is an essential
part of any business. A company also needs to be available when
customers call, in order to build trust and make connections.

This document covers how to make, receive, transfer, and forward calls
with Odoo *VoIP*.

Make calls
----------

Starting on the Odoo dashboard, a call can be made by opening the phone
widget in the the upper-right corner, which is represented by a
`☎️ (phone)`{.interpreted-text role="guilabel"} icon.

Then, a user can click on the `Contacts`{.interpreted-text
role="guilabel"} tab, and click into any contact in the database to make
a call.

Additionally, one can also use the `Search bar`{.interpreted-text
role="guilabel"} in the `VOIP`{.interpreted-text role="guilabel"} pop-up
window to find any desired contact.

{.align-center}

To manually make a call, click the `⌨️ (keyboard)`{.interpreted-text
role="guilabel"} icon, and proceed to manually key in the desired
number. Do not forget to lead with the `+ (plus)`{.interpreted-text
role="guilabel"} icon, followed by the international country code.

::: {.example}
For the United States of America, the country code and
`+ (plus)`{.interpreted-text role="guilabel"} icon, would look like
this: [+1]{.title-ref}. If one were to dial Belgium, the number would be
prefixed by [+32]{.title-ref}, and for Great Britain it would be
[+44]{.title-ref}.
:::

After entering the full number, with the required
`+ (plus)`{.interpreted-text role="guilabel"} icon prefix and country
code, click the green `📞 (phone)`{.interpreted-text role="guilabel"}
icon to start the call. When finished, click the red
`📞 (phone)`{.interpreted-text role="guilabel"} icon to end the call.

{.align-center}

Receive calls
-------------

An incoming call automatically opens the *VoIP* widget, when a user is
using the Odoo database. Should the database be open in another tab, a
sound plays (the sound **must** be activated on the device).

Once back to the tab, the calling screen of the *VoIP* phone widget
appears.

Click the green `📞 (phone)`{.interpreted-text role="guilabel"} icon to
pick up the call, or the red `📞 (phone)`{.interpreted-text
role="guilabel"} icon to reject the call.

{.align-center}

Add to call queue
-----------------

All the contacts and customers that need to be called can be seen in one
place with the Odoo *VoIP* phone widget, under the
`Next activities`{.interpreted-text role="guilabel"} tab.

{.align-center}

To add a call to the `Next activities`{.interpreted-text
role="guilabel"} tab, click the green `📞 (phone)`{.interpreted-text
role="guilabel"} icon, while in kanban view of the *CRM* application.

To remove them from the call queue, hover over the opportunity that has
a call scheduled, and click the red `📞 (phone)`{.interpreted-text
role="guilabel"} icon that appears with the
`- (minus)`{.interpreted-text role="guilabel"} icon.

When navigating back to the *VoIP* phone widget, **only** the calls that
are scheduled immediately for that day appear in the queue under the
`Next Activities`{.interpreted-text role="guilabel"} tab of the *VoIP*
pop-up widget.

{.align-center}

The `Next Activities`{.interpreted-text role="guilabel"} tab of the
*VoIP* phone widget is integrated with the following Odoo apps: *CRM*,
*Project*, and *Helpdesk*.

A call can be added in the chatter of records within those applications.

To manually add a call, via the chatter, click
`Activities`{.interpreted-text role="guilabel"} (next to the `🕗
(clock)`{.interpreted-text role="guilabel"} icon). Under
`Activity Type`{.interpreted-text role="guilabel"}, select
`Call`{.interpreted-text role="guilabel"} from the drop-down menu that
appears.

Next, set a `Due Date`{.interpreted-text role="guilabel"}, and add a
`Summary`{.interpreted-text role="guilabel"}.

Lastly, change the `Assigned to`{.interpreted-text role="guilabel"}
field to the person that should make the call. Whomever is set in this
last field (`Assigned to`{.interpreted-text role="guilabel"}) has this
call show up in their `Next
Activities`{.interpreted-text role="guilabel"} call queue in the Odoo
*VoIP* phone widget.

::: {.important}
::: {.title}
Important
:::

Only calls for the immediate day (today\'s date) appear in the
`Next Activities`{.interpreted-text role="guilabel"} tab of the *VoIP*
phone widget for that specific user.
:::

If specified, click `Save`{.interpreted-text role="guilabel"} or
`Open Calendar`{.interpreted-text role="guilabel"} to complete the
scheduling of the call.

Transfer calls
--------------

A call can be transferred from one user to another in the Odoo *VoIP*
phone widget. However, this can **only** occur after speaking to the
caller first. Without picking up the call in the Odoo *VoIP* phone
widget, the only way to transfer a call is automatically though the
provider console/portal.

::: {.seealso}
For more information on transfers, visit
`voip/axivox/forwardings_tab`{.interpreted-text role="ref"}.
:::

To transfer a call within the Odoo *VoIP* phone widget, first, answer
the call using the green `📞 (phone)`{.interpreted-text role="guilabel"}
icon.

Once the incoming call is answered, click the
`↔ (left-right arrow)`{.interpreted-text role="guilabel"} icon. Then,
enter the extension of the user the call should be forwarded to.
Finally, click `Transfer`{.interpreted-text role="guilabel"} to route
the call to that phone number.

::: {.tip}
::: {.title}
Tip
:::

To find the extension for a user, consult the
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
administrator, or, if the user has *Settings* access rights to
*Administration*, navigate to
`Settings App --> Manage Users --> Select the user --> Preferences --> VOIP -->
VoIP username / Extension number`{.interpreted-text
role="menuselection"}.

For more information on access rights, visit:
`/applications/general/users/access_rights`{.interpreted-text
role="doc"}.
:::

{.align-center}

Forward calls
-------------

To forward a call within the Odoo *VoIP* phone widget, first, answer the
call using the green `📞 (phone)`{.interpreted-text role="guilabel"}
icon. Once the incoming call is answered, click the `↔ (left-right
arrow)`{.interpreted-text role="guilabel"} icon.

Then, enter the full phone number of the user the call should be
forwarded to. Finally, click `Transfer`{.interpreted-text
role="guilabel"} to route the call to that phone number.

::: {.seealso}
For more information on forwarding, visit
`voip/axivox/forwardings_tab`{.interpreted-text role="ref"}.
:::
