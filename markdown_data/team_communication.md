# File: /content/odoo_doc17.0/fr/content/applications/productivity/discuss/team_communication.md

Use channels for team communication
===================================

Use channels in the Odoo *Discuss* app to organize discussions between
individual teams, departments, projects, or any other group that
requires regular communication. With channels, employees can communicate
inside dedicated spaces within the Odoo database around specific topics,
updates, and latest developments having to do with the organization.

Public and private channels
---------------------------

A *Public* channel can be seen by everyone, while a *Private* one is
only visible to users invited to it. To create a new channel, navigate
to the `Discuss`{.interpreted-text role="menuselection"} app, and then
click on the `➕ (plus)`{.interpreted-text role="guilabel"} icon next to
the `Channels`{.interpreted-text role="guilabel"} heading in the
left-side menu. After typing the name of the channel, two selectable
options will appear: The first is a channel with a hashtag
([\#]{.title-ref}) to indicate that it is a public channel; the second
option is a channel with a lock icon ([🔒]{.title-ref}) next to it, to
indicate that it is a private channel. Select the channel type that best
fits the communication needs.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

A public channel is best used when many employees need to access
information (such as company announcements), whereas a private channel
could be used whenever information should be limited to specific groups
(such as a specific department).
:::

### Configuration options

The channel\'s `Group Name`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and
`Privacy`{.interpreted-text role="guilabel"} settings can be modified by
clicking on the channel\'s settings, represented by a
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon in the left sidebar
menu, next to the channel\'s name.

{.align-center}

#### Privacy and Members tabs

Changing `Who can follow the group's activities?`{.interpreted-text
role="guilabel"} controls which groups can have access to the channel.

::: {.note}
::: {.title}
Note
:::

Allowing `Everyone`{.interpreted-text role="guilabel"} to follow a
private channel lets other users view and join it, as they would a
public one.
:::

When choosing `Invited people only`{.interpreted-text role="guilabel"},
specify in the `Members`{.interpreted-text role="guilabel"} tab which
members should be invited. Inviting members can also be done from the
*Discuss* app\'s main dashboard, by selecting the channel, clicking the
*add user* icon in the top-right corner of the dashboard, and finally
clicking `Invite to Channel`{.interpreted-text role="guilabel"} once all
the users have been added.

{.align-center}

When the `Selected group of users`{.interpreted-text role="guilabel"}
option is selected, it reveals the ability to add an
`Authorized Group`{.interpreted-text role="guilabel"}, along with the
options to `Auto Subscribe Groups`{.interpreted-text role="guilabel"}
and `Auto Subscribe Departments`{.interpreted-text role="guilabel"}.

The option to `Auto Subscribe Groups`{.interpreted-text role="guilabel"}
automatically adds users of that particular user group as followers. In
other words, while `Authorized Groups`{.interpreted-text
role="guilabel"} limits which users can access the channel,
`Auto Subscribe Groups`{.interpreted-text role="guilabel"} automatically
adds users as members as long as they are part of a specific user group.
The same is true for `Auto Subscribe Departments`{.interpreted-text
role="guilabel"}.

Quick search bar
----------------

Once at least 20 channels, direct messages, or live chat conversations
(if *Live Chat* module is installed on the database) are pinned in the
sidebar, a `Quick search…`{.interpreted-text role="guilabel"} bar is
displayed. This feature is a convenient way to filter conversations and
quickly find relevant communications.

{.align-center}

### Finding channels

Click on the settings `⚙️ (gear)`{.interpreted-text role="guilabel"}
icon, located in the left sidebar, to the right of the
`CHANNELS`{.interpreted-text role="guilabel"} collapsible menu item.
Doing so will lead to a mosaic view containing all the public channels
available. Users can join or leave channels on this screen by clicking
the `JOIN`{.interpreted-text role="guilabel"} or
`LEAVE`{.interpreted-text role="guilabel"} buttons that appear in the
channel boxes.

There is also the ability to apply filtering criteria and save them for
later use. The `Search...`{.interpreted-text role="guilabel"} function
accepts wildcards by using the underscore character \[ [\_]{.title-ref}
\], and specific searches can be saved by using the
`Favorites --> Save Current Search`{.interpreted-text
role="menuselection"} drop-down menu.

{.align-center}

Linking channel in chatter
--------------------------

Channels can be linked in the chatter (log note) of a record in Odoo. To
do so, simply type: [\#]{.title-ref} and the channel name. Click or
press enter on the *channel* name. Upon logging the note a link to the
channel will appear. After clicking on the link a chat window with the
channel conversation will pop up in the lower right corner of the
screen.

Users are able to contribute to this group channel (either public or
member based) by typing messages in window and pressing *enter*.

{.align-center}

::: {.seealso}
\- `../discuss`{.interpreted-text role="doc"} -
`/applications/essentials/activities`{.interpreted-text role="doc"}
:::
