# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/vm_audio_messages.md

Voicemails and audio messages
=============================

Managing voicemail is an important part of any business. A company needs
to access their messages with ease, and stay on top of any missed calls.
Recording audio messages, like thanking a caller for reaching out, or
directing them to the right extension, is also a great way to
personalize the business interaction, and set the tone with the
customer.

This document covers the configuration of both voicemail and audio
messages in the Axivox administrative portal.

Set global language {#voip/axivox/global_language}
-------------------

To start using voicemails and audio messages with Axivox, the global
language should be set in the Axivox admin portal settings. To do that,
navigate to . After
logging into the portal, go to
`Settings --> Global language (e.g.: voicemail
messages,...)`{.interpreted-text role="menuselection"}.

From here, set the language to either: `Francais`{.interpreted-text
role="guilabel"}, `English`{.interpreted-text role="guilabel"},
`Espanol`{.interpreted-text role="guilabel"}, or
`Deutsch`{.interpreted-text role="guilabel"}.

Then, click `Save`{.interpreted-text role="guilabel"}, followed by
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner of the `General Settings`{.interpreted-text role="guilabel"} page
to implement the change into production.

Activate voicemail {#voip/axivox/activate_voicemail}
------------------

In order for a user to utilize voicemail in Axivox, the voicemail
feature **must** be turned on in the Axivox administrative portal. To
begin using voicemail with a user, navigate to
. Then, log in with the
appropriate administrator credentials.

On the left menu of the Axivox administrative panel, click into
`Users`{.interpreted-text role="guilabel"}.

Then, click into the specific user the voicemail should be activated
for. Under the section marked, `Voicemail`{.interpreted-text
role="guilabel"}, open the drop-down menu, and click on
`Yes`{.interpreted-text role="guilabel"}.

Lastly, `Save`{.interpreted-text role="guilabel"} the change, then click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner of the screen.

Voicemail
---------

The next step is to set up the individual voicemail boxes on the Axivox
administrative portal. To access the portal, visit
 and log in. Then,
navigate to `Voicemails`{.interpreted-text role="menuselection"},
located in the menu on the left.

If the voicemail option was activated in the user profile, using this
process `voip/axivox/activate_voicemail`{.interpreted-text role="ref"},
then a voicemail is automatically created on the
`Voicemails`{.interpreted-text role="guilabel"} page.

::: {.tip}
::: {.title}
Tip
:::

It should be noted that some of the administrative portal language is in
French, as Axivox is a Belgian company. The global language is still set
to one of the four options as seen here:
`voip/axivox/global_language`{.interpreted-text role="ref"}.
:::

### Manually create voicemail

To manually create a new voicemail box, click
`Add a voicemail`{.interpreted-text role="guilabel"} on the
`Voicemails`{.interpreted-text role="guilabel"} page. Or, edit an
existing voicemail box, by clicking `Edit`{.interpreted-text
role="guilabel"} to the far-right of an existing voicemail box on the
`Voicemails`{.interpreted-text role="guilabel"} page.

::: {.example}
Suppose a sales or support team needs a general voicemail box. The
voicemail would need to be created manually, and attached to an incoming
number.
:::

The new, manually-created voicemail box should be attached to an
incoming number, so it can receive messages. To do so, navigate to
`Incoming numbers`{.interpreted-text role="menuselection"}, located in
the menu on the left. Then, click `Edit`{.interpreted-text
role="guilabel"} to the far-right of the specific number the voicemail
should be linked to.

In the `Destination type for voice call`{.interpreted-text
role="guilabel"} field, click the drop-down menu, and select
`Voicemail`{.interpreted-text role="guilabel"}. Then, open the drop-down
menu on the next line labeled, `Voicemail`{.interpreted-text
role="guilabel"}, and select the manually-created voicemail box.

::: {.important}
::: {.title}
Important
:::

If an incoming number is capable of receiving SMS/text messages, an
additional field,
`Destination email address for Incoming SMS`{.interpreted-text
role="guilabel"}, is present.

To determine whether an incoming number is capable of receiving SMS/text
messages, click `Incoming numbers`{.interpreted-text role="guilabel"}
from the menu on the left, then check the
`SMS compatible`{.interpreted-text role="guilabel"} column for the
incoming number.
:::

Then, if applicable, in the field labeled,
`Destination email address for Incoming SMS`{.interpreted-text
role="guilabel"}, enter an email to which incoming text messages sent to
the incoming number can be received. Some incoming numbers (US +1) in
Axivox are capable of receiving text messages from individuals and
automated numbers.

Should this field be left empty, the default destination address is
used, instead (as previously set in the beginning of the process for
manually creating a voicemail).

Once all desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click `Apply
changes`{.interpreted-text role="guilabel"} in the upper-right corner of
the screen to implement the change into production.

### Notifications

Now, whenever a voicemail is received on any of the automatically
pre-configured or manually-linked voicemail boxes, an email is sent to
the user\'s email address, as listed in the
`Voicemails`{.interpreted-text role="guilabel"} page, or in the user\'s
Axivox profile.

This information can be accessed by navigating to
`Users`{.interpreted-text role="menuselection"} in the left menu, and
clicking `Edit`{.interpreted-text role="guilabel"} next to the specific
user in question.

Forwarding to voicemail {#voip/axivox/vm_forwarding}
-----------------------

In Axivox, there are also numerous forwarding settings for a user. To
access these forwarding settings, go to
 and log in.

Next, navigate to `Users`{.interpreted-text role="menuselection"},
located in the menu on the left.

From there, click into the specific user the forwarding should be added
to. Then, open the `Forwardings`{.interpreted-text role="guilabel"} tab.

If the user is busy on another call, or away from the phone, there is an
option present in this tab to
`Send to voicemail as a last resort`{.interpreted-text role="guilabel"},
located in the `Forwarding on no
answer`{.interpreted-text role="guilabel"} and
`Forwarding on busy`{.interpreted-text role="guilabel"} fields.

{.align-center}

If the `Send to voicemail as a last resort`{.interpreted-text
role="guilabel"} box is ticked, when the forwarding actions stated in
each section are not successful, the caller is routed to the voicemail
set on the particular user.

::: {.seealso}
For more information on forwarding and transfers, visit
`voip/axivox/forwardings_tab`{.interpreted-text role="ref"}.
:::

When all the desired configurations are complete, click
`Save`{.interpreted-text role="guilabel"}, then click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner of the screen to implement the change.

Audio messages {#voip/axivox/audio_messages}
--------------

It is possible to add audio messages *before* a customer\'s call is even
taken, to inform them about the waiting time for deliveries, the
availability of a product, or any other important promotional messages.

To record an audio message in Axivox, navigate to
 and log in.

Next, click on `Audio messages`{.interpreted-text role="guilabel"} in
the menu on the left. From the `Audio
messages`{.interpreted-text role="guilabel"} page, click
`Add a message`{.interpreted-text role="guilabel"}.

Type in a `Name`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}.

Upon clicking `Save`{.interpreted-text role="guilabel"}, the browser
redirects back to the main `Audio messages`{.interpreted-text
role="guilabel"} page, where the newly-created message can be found on
the list.

There are two different ways to make the audio message. The user could
either record the message over the phone, or type the message (in text),
and select a computer-generated speaker to read the message.

### Record audio message

To record an audio message over the phone, click the orange button
labeled, `Record/Listen`{.interpreted-text role="guilabel"}, located to
the right of the desired message on the list to record, on the
`Audio messages`{.interpreted-text role="guilabel"} page.

When clicked, a `Record / listen to a message`{.interpreted-text
role="guilabel"} pop-up window appears. From here, the message is then
recorded, via one of the extensions that is associated with the user.
Under `Extension to use for message management`{.interpreted-text
role="guilabel"} field, click the drop-down menu, and select the
extension where Axivox should call to record the message.

Then, click `OK`{.interpreted-text role="guilabel"} to begin the call.

::: {.note}
::: {.title}
Note
:::

The user **must** be active in the production database with
`VoIP (Voice over Internet
Protocol)`{.interpreted-text role="abbr"} configured. To configure
`VoIP (Voice over Internet Protocol)`{.interpreted-text role="abbr"} for
a user, see this documentation: `axivox_config`{.interpreted-text
role="doc"}.
:::

Upon connecting to the Axivox audio recorder management line, a recorded
French-speaking operator provides the following options:

1.  Press [1]{.title-ref} to record a message.
2.  Press [2]{.title-ref} to listen to the current message.

Press either [1]{.title-ref} or [2]{.title-ref}, depending on whether or
not there is already a message present in the system for this particular
audio message that requires a review, before recording a new one.

Record the new audio message after pressing [1]{.title-ref}, then press
[\#]{.title-ref} to end the recording.

The French-speaking operator returns to the line presenting the first
set of questions again:

1.  Press [1]{.title-ref} to record a message.
2.  Press [2]{.title-ref} to listen to the current message.

Press [\#]{.title-ref} to end the call.

### Write audio message

To type the message, and select a computerized speaker to say the text,
navigate to the `Audio messages`{.interpreted-text role="menuselection"}
in the menu on the left.

From the `Audio messages`{.interpreted-text role="guilabel"} page,
select the blue button labeled, `Text message`{.interpreted-text
role="guilabel"}, next to the corresponding audio message
`Name`{.interpreted-text role="guilabel"} that the message should be
attached to.

Doing so reveals a `Convert text to message`{.interpreted-text
role="guilabel"} pop-up window.

From the `Convert to text message`{.interpreted-text role="guilabel"}
pop-up window, click the drop-down menu next to the field labeled,
`Voice`{.interpreted-text role="guilabel"}, and select an option for the
`Text`{.interpreted-text role="guilabel"} to be read in.

After the `Voice`{.interpreted-text role="guilabel"} selection has been
made, and the message has been written in the `Text`{.interpreted-text
role="guilabel"} field, click `Generate`{.interpreted-text
role="guilabel"} to process the audio file.

The text is read in the same language it is written in the
`Text`{.interpreted-text role="guilabel"} field. Should the language
differ in the `Voice`{.interpreted-text role="guilabel"} field, then an
accent is used by the computerized speaker.

Finally, when these steps are complete, click `Save`{.interpreted-text
role="guilabel"} to save the audio message.

To implement the changes, click `Apply changes`{.interpreted-text
role="guilabel"} in the upper-right corner of the screen.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To set a greeting or audio message in a dial plan element double-click
on the element. This could be a `Play a file`{.interpreted-text
role="guilabel"} element, or a `Menu`{.interpreted-text role="guilabel"}
element, in which the caller should encounter an urgent message, or a
dial-by-number directory.

For more information on dial plans see this documentation:
`dial_plan_basics`{.interpreted-text role="doc"} or
`dial_plan_advanced`{.interpreted-text role="doc"}.
:::

Music on-hold {#voip/axivox/music_on_hold}
-------------

Axivox has the option to add custom hold music to the call whenever a
caller is waiting for their call to be answered. To add hold music to
the Axivox administrative portal, navigate to the
, and log in.

Then, click on `Music on hold`{.interpreted-text role="guilabel"} from
the menu on the left, and a `Change the
music on hold`{.interpreted-text role="guilabel"} pop-up window appears.

On the `Change the music on hold`{.interpreted-text role="guilabel"}
pop-up window, click the `Choose File`{.interpreted-text
role="guilabel"} button to select an MP3 (MPEG Audio Layer 3) or WAV
(Waveform Audio File Format ) file to be uploaded.

::: {.note}
::: {.title}
Note
:::

Only `MP3 (MPEG Audio Layer 3)`{.interpreted-text role="abbr"} or
`WAV (Waveform Audio File Format)`{.interpreted-text role="abbr"} files
can be uploaded to the Axivox administrative portal.
:::

Once the file is selected, the `Progression`{.interpreted-text
role="guilabel"} bar shows an upload status. When this activity
completes, the window can be closed, by clicking
`Close`{.interpreted-text role="guilabel"}.

When the desired changes are complete, click
`Apply changes`{.interpreted-text role="guilabel"} in the upper-right
corner of the screen.
