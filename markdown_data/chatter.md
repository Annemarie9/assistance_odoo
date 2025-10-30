# File: /content/odoo_doc17.0/fr/content/applications/productivity/discuss/chatter.md

Chatter
=======

The *Chatter* feature is integrated throughout Odoo to streamline
communication, maintain traceability, and provide accountability among
team members. Chatter windows, known as *composers*, are located on
almost every record within the database, and allow users to communicate
with both internal users and external contacts.

Chatter composers also enable users to log notes, upload files, and
schedule activities.

Chatter thread
--------------

A *chatter thread* can be found on most pages in the database, and
serves as a record of the updates and edits made to a record. A note is
logged in the chatter thread when a change is made. The note includes
details of the change, and a time stamp.

::: {.example}
A user, Mitchell Admin, needs to update the email address of a contact.
After they save the changes to the contact record, a note is logged in
the chatter of the contact record with the following information:

-   The date when the change occurred.
-   The email address as it was previously listed.
-   The updated email address.

{.align-center}
:::

If a record was created, or edited, via an imported file, or was
otherwise updated through an intervention by the system, the chatter
thread creates a log note, and credits the change to OdooBot.

{.align-center}

Add followers {#discuss/add-followers}
-------------

A *follower* is a user or contact that is added to a record and is
notified when the record is updated, based on specific
`follower subscription settings <discuss/edit-subscription>`{.interpreted-text
role="ref"}. Followers can add themselves, or can be added by another
user.

::: {.note}
::: {.title}
Note
:::

If a user creates, or is assigned to a record, they are automatically
added as a follower.
:::

To follow a record, navigate to any record with a chatter thread. For
example, to open a *Helpdesk* ticket, navigate to
`Helpdesk app --> Tickets --> All Tickets`{.interpreted-text
role="menuselection"}, and select a ticket from the list to open it.

At the top-right, above the chatter composer, click
`Follow`{.interpreted-text role="guilabel"}. Doing this changes the
button to read `Following`{.interpreted-text role="guilabel"}. Click it
again to `Unfollow`{.interpreted-text role="guilabel"}.

### Manage followers

To add another user, or contact, as a follower, click the
`fa-user-o`{.interpreted-text role="icon"} `(user)`{.interpreted-text
role="guilabel"} icon. This opens a drop-down list of the current
followers. Click `Add Followers`{.interpreted-text role="guilabel"} to
open an `Invite Follower`{.interpreted-text role="guilabel"} pop-up
window.

Select one or more contacts from the `Recipients`{.interpreted-text
role="guilabel"} drop-down list. To notify the contacts, tick the
`Send Notification`{.interpreted-text role="guilabel"} checkbox. Edit
the message template as desired, then click
`Add Followers`{.interpreted-text role="guilabel"}.

To remove followers, click the `fa-user-o`{.interpreted-text
role="icon"} `(user)`{.interpreted-text role="guilabel"} icon to open
the current followers list. Find the name of the follower to be removed,
and click the `fa-remove`{.interpreted-text role="icon"}
`(remove)`{.interpreted-text role="guilabel"} icon.

### Edit follower subscription {#discuss/edit-subscription}

The updates a follower receives can vary based on their subscription
settings. To see the type of updates a follower is subscribed to, and to
edit the list, click the `fa-user-o`{.interpreted-text role="icon"}
`(user)`{.interpreted-text role="guilabel"} icon. Find the appropriate
follower in the list, then click the `fa-pencil`{.interpreted-text
role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon. This
opens the `Edit Subscription`{.interpreted-text role="guilabel"} pop-up
window for the follower.

The list of available subscription settings varies depending on the
record type. For example, a follower of a *Helpdesk* ticket may be
informed when the ticket is rated. This option would not be available
for the followers of a *CRM* opportunity.

Tick the checkbox for any updates the follower should receive, and clear
the checkbox for any updates they should **not** receive. Click
`Apply`{.interpreted-text role="guilabel"} when finished.

![The Edit Subscription options vary depending on the record type. These
are the options for a Helpdesk
ticket.](chatter/chatter-edit-subscription.png){.align-center}

Log notes {#discuss/log-notes}
---------

The chatter function includes the ability to log internal notes on
individual records. These notes are only accessible to internal users,
and are available on any records that feature a chatter thread.

To log an internal note, first navigate to a record. For example, to
open a *CRM* opportunity, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}, and click on the Kanban card of an opportunity to
open it. Then, at the top-right, above the chatter composer, click `Log
note`{.interpreted-text role="guilabel"}.

Enter the note in the chatter composer. To tag an internal user, type
[@]{.title-ref}, and begin typing the name of the person to tag. Then,
select a name from the drop-down menu. Depending on their notification
settings, the user is notified by email, or through Odoo.

::: {.important}
::: {.title}
Important
:::

Outside contacts can also be tagged in an internal log note. The contact
then receives an email with the contents of the note they were tagged
in, including any attachments added directly to the note. If they
respond to the email, their response is logged in the chatter, and they
are added to the record as a follower.

Outside contacts are **not** able to log in to view the entire chatter
thread, and are only notified of specific updates, based on their
`follower subscription settings
<discuss/edit-subscription>`{.interpreted-text role="ref"}, or when they
are tagged directly.
:::

Send messages {#discuss/send-messages}
-------------

Chatter composers can send messages to outside contacts, without having
to leave the database, or open a different application. This makes it
easy to communicate with potential customers in the *Sales* and *CRM*
applications, or vendors in the *Purchase* app.

To send a message, first navigate to a record. For example, to send a
message from a *CRM* opportunity, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}, and click on the Kanban card of an opportunity to
open it. Then, at the top-right, above the chatter composer, click
`Send message`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Press `Ctrl + Enter`{.interpreted-text role="command"} to send a
message, instead of using the `Send`{.interpreted-text role="guilabel"}
button.
:::

If any `followers <discuss/add-followers>`{.interpreted-text role="ref"}
have been added to the record, they are added as recipients of the
message.

::: {.warning}
::: {.title}
Warning
:::

`Followers <discuss/add-followers>`{.interpreted-text role="ref"} of a
record are added as recipients of a message automatically. If a follower
should **not** receive a message, they must be removed as a follower
before the message is sent, or a note is logged.
:::

![A chatter composer preparing to send a message to the followers of a CRM opportunity and
the customer listed on the opportunity record.](chatter/send-message-followers.png){.align-center}

### Expand full composer

The chatter composer can be expanded to a larger pop-up window, allowing
for additional customizations.

To open the full composer, click the `fa-expand`{.interpreted-text
role="icon"} `(expand)`{.interpreted-text role="guilabel"} icon in the
bottom-right corner of the composer window.

![The expand icon in a chatter
composer.](chatter/chatter-expand-icon.png){.align-center}

Doing this opens a `Compose Email`{.interpreted-text role="guilabel"}
pop-up window. Confirm or edit the intended
`Recipients`{.interpreted-text role="guilabel"} of the message, or add
additional recipients. The `Subject`{.interpreted-text role="guilabel"}
field auto-populates based on the title of the record, though it can be
edited, if desired.

To use an
`email template <../../general/companies/email_template/>`{.interpreted-text
role="doc"} for the message, select it from the drop-down menu in the
`Load template`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The number and type of templates available vary, based on the record the
message is created from.
:::

Click `fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon to add any files
to the message, then click `Send`{.interpreted-text role="guilabel"}.

{.align-center}

### Edit sent messages

Messages can be edited after they are sent, to fix typos, correct
mistakes, or add missing information.

::: {.note}
::: {.title}
Note
:::

When messages are edited after they have been sent, an updated message
is **not** sent to the recipient.
:::

To edit a sent message, click the `fa-ellipsis-h`{.interpreted-text
role="icon"} `(ellipsis)`{.interpreted-text role="guilabel"} icon menu
to the right of the message. Then, select `Edit`{.interpreted-text
role="guilabel"}. Make any necessary adjustments to the message.

{.align-center}

To save the changes, press `Ctrl + Enter`{.interpreted-text
role="command"}. To discard the changes, press
`Escape`{.interpreted-text role="command"}.

::: {.important}
::: {.title}
Important
:::

Users with Admin-level access rights can edit any sent messages. Users
without Admin rights can **only** edit messages they created.
:::

Search messages {#discuss/search-messages}
---------------

Chatter threads can become long after a while, because of all the
information they contain. To make it easier to find a specific entry,
users can search the text of messages and notes for specific keywords.

First, select a record with a chatter thread. For example, to search a
*CRM* opportunity, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}, and click on the Kanban card of an opportunity to
open it. Then, at the top-right, above the chatter composer, click the
`oi-search`{.interpreted-text role="icon"} `(search)`{.interpreted-text
role="guilabel"} icon to open the search bar.

Enter a keyword or phrase into the search bar, then hit
`Enter`{.interpreted-text role="command"}, or click the
`oi-search`{.interpreted-text role="icon"} `(search)`{.interpreted-text
role="guilabel"} icon to the right of the search bar. Any messages or
notes containing the keyword or phrase entered are listed below the
search bar, with the keyword highlighted.

To be taken directly to a particular message in the chatter thread,
hover over the upper-right corner of the result to reveal a
`Jump`{.interpreted-text role="guilabel"} button. Click this button to
be directed to that message\'s location in the thread.

![Search results in a chatter thread. Hover over the upper-right corner
of a result to see the **Jump** option. Click it to be taken directly to
that message in the chatter
thread.](chatter/chatter-search.png){.align-center}

Schedule activities {#discuss/schedule-activities}
-------------------

*Activities* are follow-up tasks tied to a record in an Odoo database.
Activities can be scheduled on any database page that contains a chatter
thread, Kanban view, list view, or activities view of an application.

To schedule an activity through a chatter thread, click the
`Activities`{.interpreted-text role="guilabel"} button, located at the
top of the chatter on any record. On the
`Schedule Activity`{.interpreted-text role="guilabel"} pop-up window
that appears, select an `Activity Type`{.interpreted-text
role="guilabel"} from the drop-down menu.

::: {.tip}
::: {.title}
Tip
:::

Individual applications have a list of *Activity Types* dedicated to
that application. For example, to view and edit the activities available
for the *CRM* application, go to
`CRM app --> Configuration --> Activity Types`{.interpreted-text
role="menuselection"}.
:::

Enter a title for the activity in the `Summary`{.interpreted-text
role="guilabel"} field, located in the `Schedule
Activity`{.interpreted-text role="guilabel"} pop-up window.

Select a name from the `Assigned to`{.interpreted-text role="guilabel"}
drop-down menu to assign the activity to a different user. Otherwise,
the user creating the activity is automatically assigned.

Add any additional information in the optional
`Log a note...`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Due Date`{.interpreted-text role="guilabel"} field on the
`Schedule Activity`{.interpreted-text role="guilabel"} pop-up window
auto-populates based on the configuration settings for the selected
`Activity Type`{.interpreted-text role="guilabel"}. However, this date
can be changed by selecting a day on the calendar in the
`Due Date`{.interpreted-text role="guilabel"} field.
:::

Lastly, click one of the following buttons:

-   `Schedule`{.interpreted-text role="guilabel"}: adds the activity to
    the chatter under `Planned activities`{.interpreted-text
    role="guilabel"}.
-   `Mark as Done`{.interpreted-text role="guilabel"}: adds the details
    of the activity to the chatter under `Today`{.interpreted-text
    role="guilabel"}. The activity is not scheduled, it is automatically
    marked as completed.
-   `Done \& Schedule Next`{.interpreted-text role="guilabel"}: adds the
    task under `Today`{.interpreted-text role="guilabel"} marked as
    done, and opens a new activity window.
-   `Discard`{.interpreted-text role="guilabel"}: discards any changes
    made on the pop-up window.

Scheduled activities are added to the chatter for the record under
`Planned activities`{.interpreted-text role="guilabel"}, and are
color-coded based on their due date.

-   **Red** icons indicate an overdue activity.
-   **Yellow** icons indicate an activity with a due date scheduled for
    the current date.
-   **Green** icons indicate an activity with a due date scheduled in
    the future.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Click the `fa-info-circle`{.interpreted-text role="icon"}
`(info)`{.interpreted-text role="guilabel"} icon next to a planned
activity to see additional details.

{.align-center}
:::

After completing an activity, click `Mark Done`{.interpreted-text
role="guilabel"} under the activity entry in the chatter. This opens a
`Mark Done`{.interpreted-text role="guilabel"} pop-up window, where
additional notes about the activity can be entered. After adding any
comments to the pop-up window, click:
`Done \& Schedule Next`{.interpreted-text role="guilabel"},
`Done`{.interpreted-text role="guilabel"}, or
`Discard`{.interpreted-text role="guilabel"}.

After the activity is marked complete, an entry with the activity type,
title, and any other details that were included in the pop-up window are
listed in the chatter.

{.align-center}

Attach files {#discuss/attach-files}
------------

Files can be added as attachments in the chatter, either to send with
messages, or to include with a record.

::: {.note}
::: {.title}
Note
:::

After a file has been added to a chatter thread, it can be downloaded by
any user with access to the thread. Click the
`fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon to make the files
header visible, if necessary. Then, click the
`fa-download`{.interpreted-text role="icon"}
`(download)`{.interpreted-text role="guilabel"} icon the file to
download it.
:::

To attach a file, click the `fa-paperclip`{.interpreted-text
role="icon"} `(paperclip)`{.interpreted-text role="guilabel"} icon
located at the top of the chatter composer of any record that contains a
chatter thread.

This opens a file explorer pop-up window. Navigate to the desired file,
select it, then click `Open`{.interpreted-text role="guilabel"} to add
it to the record. Alternatively, files can be dragged and dropped
directly onto a chatter thread.

After files have been added, they are listed in the chatter thread,
under a `Files`{.interpreted-text role="guilabel"} heading.

::: {.note}
::: {.title}
Note
:::

After at least one file has been added to a chatter record, a new button
labeled `Attach files`{.interpreted-text role="guilabel"} appears below
the `Files`{.interpreted-text role="guilabel"} heading. To attach any
additional files, this is the button that **must** be used, instead of
the `fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon at the top of the
chatter thread.

After the `Files`{.interpreted-text role="guilabel"} section heading
appears in the thread, clicking the `fa-paperclip`{.interpreted-text
role="icon"} `(paperclip)`{.interpreted-text role="guilabel"} icon no
longer opens a file explorer pop-up window. Instead, clicking the
`fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon toggles the
`Files`{.interpreted-text role="guilabel"} section from visible to
invisible in the chatter thread.

{.align-center}
:::

Integrations {#discuss/integrations}
------------

Beyond the standard features, additional integrations can be enabled to
work with the chatter feature, specifically *WhatsApp* and *Google
Translate*.

::: {.important}
::: {.title}
Important
:::

Before the *WhatsApp* and *Google Translate* integrations can be used
with the chatter, they **must** be configured. Step-by-step instructions
on how to set-up each of these features can be found in the
documentation below:

-   `WhatsApp <../whatsapp>`{.interpreted-text role="doc"}
-   `Google Translate <../../general/integrations/google_translate>`{.interpreted-text
    role="doc"}
:::

### WhatsApp

*WhatsApp* is an instant messaging and voice-over-IP app that allows
users to send and receive messages, as well as share content.

::: {.warning}
::: {.title}
Warning
:::

*WhatsApp* is an Odoo Enterprise-only application that does **not** work
in the Odoo Community edition. To sign up for an Odoo Enterprise
edition, click here: .
:::

After *WhatsApp* has been configured and enabled within a database, a
`WhatsApp`{.interpreted-text role="guilabel"} button is added above the
chatter composer on any applicable record. If one or more approved
*WhatsApp* templates are found for that model, clicking this button
opens a `Send WhatsApp Message`{.interpreted-text role="guilabel"}
pop-up window.

::: {.important}
::: {.title}
Important
:::

*WhatsApp* templates **must** be approved before they can be used. See
`WhatsApp templates
<productivity/whatsapp/templates>`{.interpreted-text role="ref"} for
more information.
:::

{.align-center}

### Google Translate

*Google Translate* can be used to translate user-generated text in the
Odoo chatter.

To enable *Google Translate* on a database, an *API key* must first
`be created
<../../general/integrations/google_translate>`{.interpreted-text
role="doc"} through the [Google API
Console](https://console.developers.google.com/).

After creating the API key, navigate to the
`Settings app --> Discuss section`{.interpreted-text
role="menuselection"} and paste the key in the
`Message Translation`{.interpreted-text role="guilabel"} field. Click
`Save`{.interpreted-text role="guilabel"} to save the changes.

#### Translate a chatter message

To translate a user\'s text from another language, click the
`fa-ellipsis-h`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} menu to the right of the
chatter. Then, select `Translate`{.interpreted-text role="guilabel"}.
The content translates to the language set in the `user's preferences
<../../general/users/language/>`{.interpreted-text role="doc"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Using the *Google Translate* API **requires** a current billing account
with .
:::

::: {.seealso}
\- `Discuss <../discuss>`{.interpreted-text role="doc"} -
`Discuss Channels <../discuss/team_communication/>`{.interpreted-text
role="doc"} -
`Activities <../../essentials/activities>`{.interpreted-text role="doc"}
- `WhatsApp <../whatsapp>`{.interpreted-text role="doc"}
:::
