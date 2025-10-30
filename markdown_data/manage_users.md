# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/manage_users.md

Manage users in Axivox
======================

Managing Axivox `VoIP (Voice over Internet Protocol)`{.interpreted-text
role="abbr"} users is an important part of setting up
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"} in
an Odoo database. Each Axivox user has a unique name, phone number
and/or extension, and a voicemail. This way, they can be reached in a
variety of convenient ways.

Axivox users are organized in a simple, straightforward way in the
Axivox console, so an administrator can manage users quickly and easily.

::: {.note}
::: {.title}
Note
:::

This documentation covers how to configure everything through a provider
called, Axivox. Depending on the chosen VoIP provider, the processes to
manage users may be different.
:::

Overview
--------

Begin at the Axivox management console by navigating to
<https://manage.axivox.com>. Log in with the appropriate administrator
credentials.

::: {.note}
::: {.title}
Note
:::

Actions in the Axivox management console **must** be double-saved, in
order for the changes to take effect. To save any changes, click
`Save`{.interpreted-text role="guilabel"} in the individualized changes
screen. Then, to implement those changes, click the
`Apply Changes`{.interpreted-text role="guilabel"} button in the
upper-right corner of the console.
:::

### Incoming numbers {#voip/axivox/incoming_number}

Incoming numbers are all the numbers a company is paying to use to
receive calls.

Click on `Incoming numbers`{.interpreted-text role="menuselection"} from
the menu on the left of the Axivox management console. Doing so reveals
the `Incoming numbers`{.interpreted-text role="guilabel"} page, where
all the incoming numbers are listed, along with their
`Destination`{.interpreted-text role="guilabel"} and SMS information.

The `Destination`{.interpreted-text role="guilabel"} determines the
action that is taken, or the path the caller follows when dialing said
numbers.

To edit the `Destination`{.interpreted-text role="guilabel"}, click the
`Edit`{.interpreted-text role="guilabel"} button to the far-right of the
incoming number line to be modified. Then, on the
`Edit number`{.interpreted-text role="guilabel"} page that appears, the
`Destination type for voice call`{.interpreted-text role="guilabel"} can
be changed.

The options available in the
`Destination type for voice call`{.interpreted-text role="guilabel"}
drop-down menu are as follows:

-   `Not configured`{.interpreted-text role="guilabel"}
-   `Extension`{.interpreted-text role="guilabel"}
-   `Dial plan`{.interpreted-text role="guilabel"}
-   `Voicemail`{.interpreted-text role="guilabel"}
-   `Hang up`{.interpreted-text role="guilabel"}
-   `Conference`{.interpreted-text role="guilabel"}

Depending on the selection made in the
`Destination type for voice call`{.interpreted-text role="guilabel"}
drop-down menu, a second, selection-specific drop-down menu is populated
with further configuration options. Additionally, more fields are
revealed, based on the selection made in the `Destination
type for voice call`{.interpreted-text role="guilabel"} drop-down menu.

Once the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner to
implement them.

New users
---------

Every employee using
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"} at
the company needs an Axivox user account associated with them.

To view existing users in the Axivox management console, click
`Users`{.interpreted-text role="guilabel"} from the menu on the left of
the console. Every user has a `Number`{.interpreted-text
role="guilabel"}, `Name`{.interpreted-text role="guilabel"}, option for
a `Voicemail`{.interpreted-text role="guilabel"}, and an
`Outgoing number`{.interpreted-text role="guilabel"} specified.

To create a new user in the Axivox console, click
`Add a user`{.interpreted-text role="guilabel"} to reveal a `New
user`{.interpreted-text role="guilabel"} form. The following tabs are
available for configuring the new user:

-   `General`{.interpreted-text role="guilabel"}: basic information,
    including the extension of the user, can be set.
-   `Forwardings`{.interpreted-text role="guilabel"}: internal forwards
    on \'no answer\' or busy signals.
-   `Follow Me`{.interpreted-text role="guilabel"}: external forward
    configuration.
-   `Keys`{.interpreted-text role="guilabel"}: set hot-keys within the
    `VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
    system.
-   `SIP Identifiers`{.interpreted-text role="guilabel"}:
    `SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
    username and password for external configuration.
-   `Permissions`{.interpreted-text role="guilabel"}: set access rights
    for users in the Axivox management console.

### General tab

Under the `General`{.interpreted-text role="guilabel"} tab of the
`New user`{.interpreted-text role="guilabel"} form, in the
`Extension`{.interpreted-text role="guilabel"} field, input an extension
that is unique to the user. This is the number internal users dial to
reach a specific employee.

In the `Name`{.interpreted-text role="guilabel"} field, input the
employee name.

Next, fill out the `Email address of the user`{.interpreted-text
role="guilabel"} field. A valid email address for the employee should be
added here, where the user receives business emails.

In the `GSM number`{.interpreted-text role="guilabel"} field, enter an
alternative number at which the user can be reached. Be sure to include
the country code.

::: {.note}
::: {.title}
Note
:::

A country code is a locator code that allows access to the desired
country\'s phone system. The country code is dialed first, prior to the
target number. Each country in the world has its own specific country
code.

For a list of comprehensive country codes, visit:
<https://countrycode.org>.
:::

{.align-center}

In the `Voicemail`{.interpreted-text role="guilabel"} field, select
either `Yes`{.interpreted-text role="guilabel"} or
`No`{.interpreted-text role="guilabel"} from the drop-down menu.

In the `Directory`{.interpreted-text role="guilabel"} field, the
administrator has the option to leave it blank, by making no changes, or
selecting `Default`{.interpreted-text role="guilabel"} from the
drop-down menu. The `Directory`{.interpreted-text role="guilabel"} is
used in the *Digital Receptionist* feature element of a dial-plan.

At the bottom of the `General`{.interpreted-text role="guilabel"} tab,
there are two separate options with selection boxes.

The first option is
`This user can receive multiple calls at the same time`{.interpreted-text
role="guilabel"}. By selecting this option, users are able to receive
calls when on another call.

The second option, `This user must log-in to call`{.interpreted-text
role="guilabel"}, provides the option to make it mandatory for the user
to log in.

::: {.note}
::: {.title}
Note
:::

If a company uses physical VoIP phones on desks, and wants their
employees to be able to log in from *any* phone or desk in the office,
they would make the selection for `This user
must log-in to call`{.interpreted-text role="guilabel"}.
:::

Once the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner.

### Forwardings tab {#voip/axivox/forwardings_tab}

Under the `Forwardings`{.interpreted-text role="guilabel"} tab of the
`New user`{.interpreted-text role="guilabel"} form, a company can decide
what happens if someone calls a user, and the call is not answered.

::: {.important}
::: {.title}
Important
:::

Forwardings are disabled when the `Follow Me`{.interpreted-text
role="guilabel"} option is enabled.
:::

For example, under the `Forwarding on no answer`{.interpreted-text
role="guilabel"} field, when the button for `Add
a destination`{.interpreted-text role="guilabel"} is selected, the
option to add a specific user or phone number is revealed. After
entering the `Destination`{.interpreted-text role="guilabel"}, a
specific time frame can be selected by sliding the
`seconds bar`{.interpreted-text role="guilabel"} to the desired ring
time.

Additional `Destinations`{.interpreted-text role="guilabel"} can be
added on with different ring times.

::: {.note}
::: {.title}
Note
:::

Ring times can be staggered, so the call is forwarded to another user
after the first user does not pick up the call. The option to
`Send to voicemail as a last resort`{.interpreted-text role="guilabel"}
is available to the administrator, should the
`Destinations`{.interpreted-text role="guilabel"} not pick up.
:::

Under the `Forwarding on busy`{.interpreted-text role="guilabel"} field,
an administrator can `Add a destination`{.interpreted-text
role="guilabel"}. When clicked, they can then set the
`Destination`{.interpreted-text role="guilabel"} (user) and time frame.
Should the original user\'s
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
extension, or incoming number, be busy, the call is forwarded to the
destination(s).

{.align-center}

When the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner of
the page.

### Follow Me tab

When the `Follow Me`{.interpreted-text role="guilabel"} option is
selected, under the `Follow Me`{.interpreted-text role="guilabel"} tab
of the `New user`{.interpreted-text role="guilabel"} form, no
`Forwardings`{.interpreted-text role="menuselection"} can be made.

Also, when the `Follow Me`{.interpreted-text role="guilabel"} option is
selected, the `Add a destination`{.interpreted-text role="guilabel"}
button can be selected to add users, or a destination phone number, to
the original user\'s account. That way, these added numbers ring when a
call is received.

After entering the `Destination`{.interpreted-text role="guilabel"}, a
specific time frame can be made by sliding the
`seconds bar`{.interpreted-text role="guilabel"} to the desired ring
time. Additional `Destinations`{.interpreted-text role="guilabel"} can
be added with different ring times.

::: {.note}
::: {.title}
Note
:::

The original user\'s
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"}
number does **not** ring with this option selected. Ring times can also
be staggered, so the call is forwarded to another user after the first
user does not pick up the call.
:::

{.align-center}

::: {.important}
::: {.title}
Important
:::

The Odoo mobile app, or another
`SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
mobile client, allows for simultaneous ringing of the user\'s extension
or incoming number. For more information, visit the
`VoIP Mobile Integrations <../devices_integrations>`{.interpreted-text
role="doc"} documentation.
:::

Once all desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner.

### Keys tab

Under the `Keys`{.interpreted-text role="guilabel"} tab of the
`New user`{.interpreted-text role="guilabel"} form, speed dial actions
for the user can be configured. Some more advanced options are
available, as well.

The following options are available to set to numerical values
[1-20]{.title-ref}.

These actions can be set on each number:

-   `Not configured`{.interpreted-text role="guilabel"}: the default
    action, which is nothing.
-   `BLF (Busy lamp fields)`{.interpreted-text role="guilabel"}: this
    action shows the status of other users\' phones connected to the
    Axivox phone system. This is primarily used on a desk-phone.
-   `Quick Call`{.interpreted-text role="guilabel"}: this action allows
    for a speed-dial of an external number.
-   `Line`{.interpreted-text role="guilabel"}: this action allows the
    user to call another user.
-   `Switch`{.interpreted-text role="guilabel"}: this action allows the
    user to switch between calls from a desk-phone.
-   `Pickup`{.interpreted-text role="guilabel"}: this action allows the
    user to pick up an incoming call from a desk-phone.

![Manage user page with Keys tab highlighted and number 2 key drop-down menu selected (with
highlight)](manage_users/user-keys.png){.align-center}

Once all the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner.

::: {.important}
::: {.title}
Important
:::

Many of the preceding options have secondary options available, as well,
that can be used to link a user, or external phone number. These
**must** be filled out in conjunction with the initial action.
:::

::: {.note}
::: {.title}
Note
:::

The `Number of keys`{.interpreted-text role="guilabel"} field can be
changed by entering in the desired numerical value in the
`Number of keys`{.interpreted-text role="guilabel"} field, located at
the top of the `Keys`{.interpreted-text role="guilabel"} tab of the
`New user`{.interpreted-text role="guilabel"} form.
:::

### SIP Identifiers tab

*SIP*, which stands for Session Initiation Protocol telephony, allows
one to make and receive calls through an internet connection. The
`SIP Identifiers`{.interpreted-text role="guilabel"} tab on the
`New user`{.interpreted-text role="guilabel"} form, contains credentials
needed to configure Axivox users in Odoo and/or a different `SIP
(Session Initiation Protocol)`{.interpreted-text role="abbr"} mobile
client.

::: {.seealso}
See the documentation on configuring Axivox, using the SIP identifiers:

-   `Use VoIP services in Odoo with Axivox <axivox_config>`{.interpreted-text
    role="doc"}
-   `Axivox Mobile Integrations <../devices_integrations>`{.interpreted-text
    role="doc"}
:::

Under the `SIP Identifiers`{.interpreted-text role="guilabel"} tab, the
`SIP username`{.interpreted-text role="guilabel"} field represents the
user\'s information that was entered in the
`Extension`{.interpreted-text role="guilabel"} field, under the
`General`{.interpreted-text role="guilabel"} tab.

The `Domain`{.interpreted-text role="guilabel"} field is assigned to the
company by the Axivox representative.

The value in the `SIP Password`{.interpreted-text role="guilabel"} field
is unique for every Axivox user. This value is used to sign into Axivox
on Odoo, and for any mobile
`SIP (Session Initiation Protocol)`{.interpreted-text role="abbr"}
clients.

{.align-center}

The value listed in the `Address of the proxy server`{.interpreted-text
role="guilabel"} field is typically: [pabx.axivox.com]{.title-ref}, but
is subject to change by Axivox, so be sure to check the `SIP
Identifiers`{.interpreted-text role="guilabel"} tab for the most
accurate value.

Once all desired configurations have been made, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner.

### Permissions tab

Under the `Permissions`{.interpreted-text role="guilabel"} tab of a
`New user`{.interpreted-text role="guilabel"} form, a
`Username`{.interpreted-text role="guilabel"} and
`Password`{.interpreted-text role="guilabel"} can be entered for the
user.

Beneath those fields, the following permissions can be granted to Axivox
users for portal access:

-   `User portal access`{.interpreted-text role="guilabel"}
-   `User management`{.interpreted-text role="guilabel"}
-   `Administrator access`{.interpreted-text role="guilabel"}
-   `Phone management`{.interpreted-text role="guilabel"}
-   `User group management`{.interpreted-text role="guilabel"}
-   `Phone number management`{.interpreted-text role="guilabel"}
-   `Dial plan management`{.interpreted-text role="guilabel"}
-   `Pickup group management`{.interpreted-text role="guilabel"}
-   `Switch management`{.interpreted-text role="guilabel"}
-   `Conference management`{.interpreted-text role="guilabel"}
-   `Queue management`{.interpreted-text role="guilabel"}
-   `Voicemail management`{.interpreted-text role="guilabel"}
-   `Audio messages management`{.interpreted-text role="guilabel"}
-   `Music on hold management`{.interpreted-text role="guilabel"}
-   `Directory management`{.interpreted-text role="guilabel"}
-   `Call list`{.interpreted-text role="guilabel"}
-   `Connected user list`{.interpreted-text role="guilabel"}
-   `Global settings`{.interpreted-text role="guilabel"}
-   `Apply changes button`{.interpreted-text role="guilabel"}
-   `Invoice download`{.interpreted-text role="guilabel"}
-   `Invoice details`{.interpreted-text role="guilabel"}
-   `Blacklist management`{.interpreted-text role="guilabel"}
-   `Conference participant management`{.interpreted-text
    role="guilabel"}

To access credentials for the Axivox user portal, navigate to the top of
the `Permissions`{.interpreted-text role="menuselection"} tab. Then,
copy the `Username`{.interpreted-text role="guilabel"}, and enter the
correct `Password`{.interpreted-text role="guilabel"} for the individual
user. There is a minimum of 8 characters for a user password.

::: {.note}
::: {.title}
Note
:::

These are the same permissions granted to the Axivox administrator that
are listed in the menu on the left in the Axivox management console.
Should a selection state `No`{.interpreted-text role="guilabel"}, or
`No access`{.interpreted-text role="guilabel"}, then the menu option
does **not** populate for the user.
:::

Once all the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner.

Upon finishing the setup for a new user, an
`voip/axivox/incoming_number`{.interpreted-text role="ref"} can be
linked.

![Manage a user page, with the permissions tab highlighted, along with the first permission
highlighted indicating a no selection.](manage_users/user-permissions.png){.align-center}

User groups {#voip/axivox/user_groups}
-----------

A user group is a grouping of Axivox users that can be linked to a queue
for call center capability.

To begin using user groups, navigate to <https://manage.axivox.com>.

Then, log in with the appropriate administrator credentials. From the
menu on the left of the Axivox administrative panel, click into
`User Groups`{.interpreted-text role="guilabel"}.

To add a user group from the `User Groups`{.interpreted-text
role="guilabel"} page, click `Add a group`{.interpreted-text
role="guilabel"}.

Next, name the group, by entering text into the `Name`{.interpreted-text
role="guilabel"} field. Then, add a member to the group by typing the
first few letters of the user\'s name into the
`Members`{.interpreted-text role="guilabel"} field. The user populates
in a drop-down menu below the field. Then, click on the desired user,
and they are added to the user group.

Repeat this process to add more users to the group.

Once all desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner.
