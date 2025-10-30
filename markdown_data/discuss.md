# File: /content/odoo_doc17.0/fr/content/applications/productivity/discuss.md

show-content

:   

hide-page-toc

:   

Discuss
=======

Odoo **Discuss** is an internal communication app that allows users to
connect through messages, notes, file sharing, and video calls.
**Discuss** enables communication through a persistent chat window that
works across applications, or through the dedicated *Discuss* dashboard.

Upon opening the `Discuss app`{.interpreted-text role="menuselection"},
the `Discuss`{.interpreted-text role="guilabel"} dashboard appears.

Inbox, starred, and history
---------------------------

Upon opening the `Discuss app`{.interpreted-text role="menuselection"},
the *Discuss* dashboard appears.

On the `Discuss`{.interpreted-text role="guilabel"} dashboard, unread
messages are visible in the `fa-inbox`{.interpreted-text role="icon"}
`Inbox`{.interpreted-text role="guilabel"}.
`fa-star-o`{.interpreted-text role="icon"} `Starred`{.interpreted-text
role="guilabel"} is where starred messages are stored.
`fa-history`{.interpreted-text role="icon"} `History`{.interpreted-text
role="guilabel"} shows chatter updates for records in the Odoo database
the user has been assigned to, or tagged on.

Direct messages
---------------

*Direct messages* allow the user to communicate privately with one or
multiple team members. To start a new direct message, click the
`fa-plus`{.interpreted-text role="icon"} icon, next to
`Direct Messages`{.interpreted-text role="guilabel"} on the
`Discuss`{.interpreted-text role="guilabel"} dashboard, and enter the
name of the desired person in the `Start
a conversation`{.interpreted-text role="guilabel"} search bar that
appears.

::: {.tip}
::: {.title}
Tip
:::

Multiple names can be selected in the
`Start a conversation`{.interpreted-text role="guilabel"} search bar.
Once all of the names have been entered, press `Enter`{.interpreted-text
role="kbd"}.
:::

### Direct message actions

Hover over a direct message in the chat window to see a menu of actions
to take on the message.

-   `oi-smile-add`{.interpreted-text role="icon"}
    `(Add a Reaction)`{.interpreted-text role="guilabel"}: open a
    drop-down menu of emojis that can be used to react to the direct
    message.
-   `fa-reply`{.interpreted-text role="icon"}
    `(Reply)`{.interpreted-text role="guilabel"}: reply to the direct
    message in a thread.
-   `fa-star-o`{.interpreted-text role="icon"}
    `(Mark as Todo)`{.interpreted-text role="guilabel"}: add the message
    to the `Starred`{.interpreted-text role="guilabel"} tab.
-   `fa-ellipsis-h`{.interpreted-text role="icon"}
    `(Expand)`{.interpreted-text role="guilabel"}: reveals more message
    actions, including:
    -   `fa-thumb-tack`{.interpreted-text role="icon"}
        `Pin`{.interpreted-text role="guilabel"}
    -   `fa-eye-slash`{.interpreted-text role="icon"}
        `Mark as Unread`{.interpreted-text role="guilabel"}
    -   `fa-pencil`{.interpreted-text role="icon"}
        `Edit`{.interpreted-text role="guilabel"}
    -   `fa-trash`{.interpreted-text role="icon"}
        `Delete`{.interpreted-text role="guilabel"}

### Conversation actions

The icons in the top-right corner of a direct message conversation
represent different actions the user can take on that conversation.

Click `fa-bell`{.interpreted-text role="icon"}
`Notification Settings`{.interpreted-text role="guilabel"} to set up
notification preferences for the conversation, or click
`fa-phone`{.interpreted-text role="icon"}
`Start a Call`{.interpreted-text role="guilabel"} to begin a meeting.
See the `Meetings <discuss/meetings>`{.interpreted-text role="ref"}
section for more information about meetings.

At the top of the direct message window, click the name of the direct
message to change the group name, and choose to add a description in the
adjacent `Add a description`{.interpreted-text role="guilabel"} field.



::: {.note}
::: {.title}
Note
:::

The `Add a description`{.interpreted-text role="guilabel"} field is
**only** available for group messages with more than two participants.
:::

### User status

It is helpful to see what colleagues are up to, and how quickly they can
respond to messages, by checking their status. The status is displayed
as a circle in the bottom-right corner of a contact\'s photo in the
`fa-users`{.interpreted-text role="icon"}
`(Members List)`{.interpreted-text role="guilabel"}.

The color of the circle represents the user\'s status:

-   Green = online
-   Orange = away
-   White = offline
-   Airplane = out of the office

### Leave a direct message conversation

To leave a direct message conversations, click the
`fa-times`{.interpreted-text role="icon"}
`(Leave this channel)`{.interpreted-text role="guilabel"} icon next to
the conversation name in the `Direct Messages`{.interpreted-text
role="guilabel"} section of the sidebar.

::: {.note}
::: {.title}
Note
:::

Leaving a conversation does **not** delete the direct messages in the
conversation. The direct message conversation\'s history is visible when
another direct message with the same person, or group, is created.
:::

Meetings {#discuss/meetings}
--------

In **Discuss**, *Meetings* are video calls. To start a meeting from the
`Discuss`{.interpreted-text role="guilabel"} dashboard, click
`Start a meeting`{.interpreted-text role="guilabel"} in the top-left
corner, and select who to invite to the meeting, via the
`Invite People`{.interpreted-text role="guilabel"} drop-down window that
appears. To start a meeting from a direct message, click the
`fa-phone`{.interpreted-text role="icon"}
`Start a Call`{.interpreted-text role="guilabel"} icon in the top-right
corner.



Once a meeting has been started, the following buttons can be used:

  ----------------------------------------------------------------------------------
  Icon                                      Use
  ----------------------------------------- ----------------------------------------
  `fa-microphone`{.interpreted-text         `Mute`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-microphone-slash`{.interpreted-text   `Unmute`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-headphones`{.interpreted-text         `Deafen`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-deaf`{.interpreted-text role="icon"}  `Undeafen`{.interpreted-text
                                            role="guilabel"}

  `fa-video-camera`{.interpreted-text       `Turn camera on/off`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-hand-paper-o`{.interpreted-text       `Raise Hand`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-desktop`{.interpreted-text            `Share Screen`{.interpreted-text
  role="icon"}                              role="guilabel"}

  `fa-arrows-alt`{.interpreted-text         `Enter Full Screen`{.interpreted-text
  role="icon"}                              role="guilabel"}
  ----------------------------------------------------------------------------------

User-specific notification preferences {#discuss_app/notification_preferences}
--------------------------------------

Access user-specific preferences for the **Discuss** app by navigating
to `Settings
app --> Manage Users`{.interpreted-text role="menuselection"}, select a
user, then click the `Preferences`{.interpreted-text role="guilabel"}
tab.



By default, the `Notification`{.interpreted-text role="guilabel"} field
is set as `Handle by Emails`{.interpreted-text role="guilabel"}. With
this setting enabled, a notification email is sent by Odoo every time a
message is sent from the chatter of a record, a note is sent with an
[@]{.title-ref} mention (from the chatter of a record), or a
notification is sent for a record the user follows.

By choosing `Handle in Odoo`{.interpreted-text role="guilabel"}, the
above notifications are shown in the **Discuss** app\'s *Inbox*.

Chat from different applications
--------------------------------

The **Discuss** application enables communication across all of Odoo\'s
applications. To view chats and channels, or start a new message, select
the speech bubbles that are consistently present in the upper-right
corner of the database header.



::: {.seealso}
\- `discuss/team_communication`{.interpreted-text role="doc"} -
`/applications/essentials/activities`{.interpreted-text role="doc"} -
`discuss/ice_servers`{.interpreted-text role="doc"} -
`discuss/chatter`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
discuss/team\_communication discuss/ice\_servers discuss/chatter
:::
