# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/event_tracks.md

Event tracks
============

Odoo *Events* provides the ability to create, schedule, and manage
talks, lectures, demonstrations, presentations, etc., which known as
*Tracks* in Odoo.

The Odoo *Events* application also has an option to allow event
attendees to propose talks (tracks) for an event, which can then be
approved (or disapproved).

Configuration
-------------

First, there are some settings that need to be enabled, in order to get
the most out of event tracks.

To do that, navigate to
`Events app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the checkbox beside the
`Schedule & Tracks`{.interpreted-text role="guilabel"} setting. Doing so
provides the ability to manage and publish an event schedule with
various tracks.

Also, when that setting checkbox is ticked, two additional setting
options appear beneath it: `Live Broadcast`{.interpreted-text
role="guilabel"} and `Event Gamification`{.interpreted-text
role="guilabel"}.

{.align-center}

The `Live Broadcast`{.interpreted-text role="guilabel"} option provides
the ability to air tracks online through a *YouTube* integration.

The `Event Gamification`{.interpreted-text role="guilabel"} options
provides the ability to share a quiz with track attendees once the track
is over, in order to test how much they learned.

::: {.note}
::: {.title}
Note
:::

With the `Event Gamification`{.interpreted-text role="guilabel"} setting
enabled, an `Add Quiz`{.interpreted-text role="guilabel"} button appears
on track forms, providing the ability to
`quickly create a quiz <events/track-add-quiz>`{.interpreted-text
role="ref"} specific to the topic related to that particular track.
:::

Once all desired settings have been enabled, be sure to click the
`Save`{.interpreted-text role="guilabel"} button in the upper-left
corner of the `Settings`{.interpreted-text role="guilabel"} page.

Event Tracks page
-----------------

To access, modify, and/or create tracks for an event, first navigate to
a preconfigured event, or
`create a new one <create_events>`{.interpreted-text role="doc"} from
the *Events* application.

To do that, navigate to `Events app`{.interpreted-text
role="menuselection"}, and either select a pre-existing event from the
`Events`{.interpreted-text role="guilabel"} dashboard, or create a new
one by clicking `New`{.interpreted-text role="guilabel"}.

Once on the desired event form, click into the
`Tracks`{.interpreted-text role="guilabel"} smart button at the top of
the form.

::: {.tip}
::: {.title}
Tip
:::

If the `Tracks`{.interpreted-text role="guilabel"} smart button is not
readily available, click the `More`{.interpreted-text role="guilabel"}
`fa-sort-desc`{.interpreted-text role="icon"} drop-down menu to reveal
hidden smart buttons. Then, click `Tracks`{.interpreted-text
role="guilabel"} from the resulting drop-down menu.
:::

Clicking the `Tracks`{.interpreted-text role="guilabel"} smart button
reveals the `Event Tracks`{.interpreted-text role="guilabel"} page for
that particular event, which presents all the tracks (both scheduled and
proposed) for the event, if there are any.

{.align-center}

The tracks are presented in a default `oi-view-kanban`{.interpreted-text
role="icon"} `(Kanban)`{.interpreted-text role="guilabel"} view, but
there is also the option to view these tracks in a
`oi-view-list`{.interpreted-text role="icon"} `(List)`{.interpreted-text
role="guilabel"}, `oi-view-cohort`{.interpreted-text role="icon"}
`(Gantt)`{.interpreted-text role="guilabel"} chart,
`fa-calendar-check-o`{.interpreted-text role="icon"}
`(Calendar)`{.interpreted-text role="guilabel"},
`fa-area-chart`{.interpreted-text role="icon"}
`(Graph)`{.interpreted-text role="guilabel"}, or
`fa-clock-o`{.interpreted-text role="icon"}
`(Activity)`{.interpreted-text role="guilabel"} view. All of which are
accessible in the upper-right corner of the `Tracks`{.interpreted-text
role="guilabel"} page.

In the default `oi-view-kanban`{.interpreted-text role="icon"}
`(Kanban)`{.interpreted-text role="guilabel"} view, the tracks are
categorized into different stages. The default stages are:
`Proposal`{.interpreted-text role="guilabel"},
`Confirmed`{.interpreted-text role="guilabel"},
`Announced`{.interpreted-text role="guilabel"},
`Published`{.interpreted-text role="guilabel"},
`Refused`{.interpreted-text role="guilabel"} (collapsed stage), and
`Cancelled`{.interpreted-text role="guilabel"} (collapsed stage). All of
which can be edited, if needed.

::: {.tip}
::: {.title}
Tip
:::

To edit a stage, hover over the stage name, click the
`fa-cog`{.interpreted-text role="icon"} `(Settings)`{.interpreted-text
role="guilabel"} icon, and select `Edit`{.interpreted-text
role="guilabel"} from the resulting drop-down menu.
:::

Clicking into a track from the `Event Tracks`{.interpreted-text
role="guilabel"} page reveals the track form for that particular track.

### Create event track

From the `Event Tracks`{.interpreted-text role="guilabel"} page, click
`New`{.interpreted-text role="guilabel"} in the upper-left corner to
reveal a blank event track form to create an event track.

{.align-center}

Start by giving this track a `Title`{.interpreted-text role="guilabel"}.
This field is **required** by Odoo.

Then, if desired, add an accompanying image to the track via the
`fa-pencil`{.interpreted-text role="icon"} `(pencil)`{.interpreted-text
role="guilabel"} icon that appears when the cursor hovers over the
`fa-camera`{.interpreted-text role="icon"} `(camera)`{.interpreted-text
role="guilabel"} icon in the upper-right corner of the form. When
clicked, proceed to upload the desired image for the track. This image
appears on the front-end of the event website, on this specific tracks
webpage.

Next, enter a `Track Date`{.interpreted-text role="guilabel"} and time
for the track, and designate a `Location`{.interpreted-text
role="guilabel"} where the talk is planning to be held.

::: {.tip}
::: {.title}
Tip
:::

To access a complete list of locations for event tracks, which can be
modified (and added to) at any time, navigate to
`Events app --> Configuration --> Track Locations`{.interpreted-text
role="menuselection"}.
:::

Then, add a `Duration`{.interpreted-text role="guilabel"} to the track
(in minutes).

If the *Live Broadcast* setting has been enabled in the *Events* app
settings, the option to add a corresponding link in the
`YouTube Video Link`{.interpreted-text role="guilabel"} field is
available.

If the `Always Wishlisted`{.interpreted-text role="guilabel"} checkbox
is ticked, the talk is automatically set as a favorite for each
registered event attendee.

Assign someone to be in charge of managing this track in the
`Responsible`{.interpreted-text role="guilabel"} field. By default, the
person who initially created the track is assigned.

Then, ensure the track is applied to the correct event in the
`Event`{.interpreted-text role="guilabel"} field. By default, this field
is auto-populated with the event related to the *Event Tracks* page the
track was originally created from.

Next, choose to add existing tags, or create new ones, to further
organize the track. These tags, and their corresponding tag categories
are utilized on the event specific website - mainly on the *Talks* web
page on the event website, via the drop-down filter menus.

Beneath that general information section, there are three tabs: `Speaker
<events/track-speaker-tab>`{.interpreted-text role="ref"},
`Description <events/track-description-tab>`{.interpreted-text
role="ref"}, and
`Interactivity <events/track-interactivity-tab>`{.interpreted-text
role="ref"}.

#### Speaker tab {#events/track-speaker-tab}

The `Speaker`{.interpreted-text role="guilabel"} tab on an event track
form is filled with various fields related to the specific speaker who
is planning to conduct/host the track.

{.align-center}

##### Contact Details section

In the `Contact Details`{.interpreted-text role="guilabel"} section,
proceed to use the `Contact`{.interpreted-text role="guilabel"}
drop-down field to select an existing contact from the database as the
main point of contact for the talk.

If this contact is not yet in the database, type in the name of the
contact, and click `Create`{.interpreted-text role="guilabel"} to create
and edit the contact form later, or click `Create and
edit...`{.interpreted-text role="guilabel"} to be taken to that new
contact\'s contact form, where the rest of their pertinent information
can be entered.

The `Contact Email`{.interpreted-text role="guilabel"} and
`Contact Phone`{.interpreted-text role="guilabel"} fields are greyed-out
and populated with the information found on that chosen contact\'s
contact form. These fields are not modifiable once the
`Contact`{.interpreted-text role="guilabel"} field is selected.

##### Speaker Bio section

In the `Speaker Bio`{.interpreted-text role="guilabel"} section, proceed
to enter information related to the specific speaker scheduled to
conduct/host the track. This section may auto-populate based on the
`Contact`{.interpreted-text role="guilabel"} selected in the
`Contact Details`{.interpreted-text role="guilabel"} section. If not,
enter information in the necessary fields.

::: {.note}
::: {.title}
Note
:::

This information appears on the front-end of the event website, on the
specific track webpage, providing more information about the speaker to
the track attendees.
:::

Start by entering a `Name`{.interpreted-text role="guilabel"},
`Email`{.interpreted-text role="guilabel"}, and
`Phone`{.interpreted-text role="guilabel"} number for the speaker.

Next, if desired, add an image to appear alongside the speaker biogrpahy
on the event website, via the `fa-pencil`{.interpreted-text role="icon"}
`(pencil)`{.interpreted-text role="guilabel"} icon that appears when the
cursor hovers over the `fa-camera`{.interpreted-text role="icon"}
`(camera)`{.interpreted-text role="guilabel"} icon. When clicked,
proceed to upload the desired image for the speaker.

Then, enter a `Job Position`{.interpreted-text role="guilabel"} for the
designated speaker, followed by the `Company Name`{.interpreted-text
role="guilabel"} associated with the speaker.

In the `Biography`{.interpreted-text role="guilabel"} field, proceed to
enter in a custom biography with any speaker-related information.

#### Description tab {#events/track-description-tab}

The `Description`{.interpreted-text role="guilabel"} tab of an event
track form is a blank text field, in which a description of the track
can be entered. The information entered here appears on the specific
track page on the event website.

#### Interactivity tab {#events/track-interactivity-tab}

The `Interactivity`{.interpreted-text role="guilabel"} tab on an event
track form features a single option at first:
`Magic Button`{.interpreted-text role="guilabel"}.

{.align-center}

When the checkbox beside `Magic Button`{.interpreted-text
role="guilabel"} is ticked, Odoo displays a *call to action* button to
attendees on the track sidebar, while the track is taking place.

With that checkbox ticked, three more options appear, all of which are
related to the `Magic Button`{.interpreted-text role="guilabel"}:

-   `Button Title`{.interpreted-text role="guilabel"}: enter a title to
    appear on the button for attendees.
-   `Button Target URL`{.interpreted-text role="guilabel"}: enter a URL
    that leads attendees, who click the button, to a specific page.
-   `Show Button`{.interpreted-text role="guilabel"}: enter a number in
    the field, and the button will appear that number of
    `minutes after Track start`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The magic button **only** appears if there is more than one published
track.
:::

#### Add Quiz button {#events/track-add-quiz}

The `Add Quiz`{.interpreted-text role="guilabel"} button **only**
appears on event track forms if the *Event Gamification* setting is
enabled in the Odoo *Events* settings.

To add a quiz to the event track, click the `Add Quiz`{.interpreted-text
role="guilabel"} button. Doing so reveals a separate page where an event
track quiz can be created and configured.

{.align-center}

Start by entering a title for the quiz in the blank field at the top of
the page. Then, if participants should be allowed to try the quiz
multiple times, tick the checkbox beside
`Allow multiple tries`{.interpreted-text role="guilabel"}.

The `Event`{.interpreted-text role="guilabel"} and
`Event Track`{.interpreted-text role="guilabel"} fields are
non-modifiable, and show the corresponding event and track this quiz is
associated with.

To add questions to the quiz, click `Add a line`{.interpreted-text
role="guilabel"} beneath the `Question`{.interpreted-text
role="guilabel"} column. Doing so reveals a
`Create Questions`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

::: {.note}
::: {.title}
Note
:::

**All** track quiz questions are multiple choice.
:::

From the pop-up window, enter the question in the blank field at the
top. Then, click `Add
a line`{.interpreted-text role="guilabel"} to add answer options. Upon
clicking `Add a line`{.interpreted-text role="guilabel"}, a new line
appears, in which an answer option can be entered.

Once an answer option has been entered, proceed to designate whether it
is the `Correct`{.interpreted-text role="guilabel"} response, by ticking
the checkbox in the `Correct`{.interpreted-text role="guilabel"} column.

Then, there is the option to add a point value in the
`Points`{.interpreted-text role="guilabel"} column.

And, if there are any additional comments that should accompany an
answer option, type them into the `Extra Comment`{.interpreted-text
role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Correct`{.interpreted-text role="guilabel"},
`Points`{.interpreted-text role="guilabel"}, and
`Extra Comment`{.interpreted-text role="guilabel"} fields are all
optional.
:::

Repeat this process for all the answer options.

To remove an answer option, click the `fa-trash-o`{.interpreted-text
role="icon"} `(trash can)`{.interpreted-text role="guilabel"} icon on
the far-right.

Once all desired answer options (and their configurations) are complete,
click `Save &
Close`{.interpreted-text role="guilabel"} to save the question, close
the pop-up window, and return to the track quiz form. Or, click
`Save & New`{.interpreted-text role="guilabel"} to save this question,
and instantly start creating another question on a new
`Create Questions`{.interpreted-text role="guilabel"} pop-up form.

To remove any question from the quiz, click the
`fa-trash-o`{.interpreted-text role="icon"}
`(trash can)`{.interpreted-text role="guilabel"} icon on the far-right
of the question line.

Publish event track
-------------------

Once all the desired configurations are complete on an event track form,
click the desired stage it should be in from the status bar in the
upper-right corner (e.g. `Confirmed`{.interpreted-text role="guilabel"},
`Announced`{.interpreted-text role="guilabel"}, etc.).

::: {.note}
::: {.title}
Note
:::

The stage of a track can also be changed from the
`Event Tracks`{.interpreted-text role="guilabel"} page, where the
desired track card can be dragged-and-dropped into the appropriate
Kanban stage.
:::

If an event track has *not* been published yet, and it is moved to the
`Published`{.interpreted-text role="guilabel"} stage, Odoo automatically
publishes the track on the event website.

An event track can *also* be published by opening the desired event
track form, and clicking the `Go to Website`{.interpreted-text
role="guilabel"} smart button. Then, in order for the track page to be
viewable (and accessible) for event attendees, toggle the
`fa-toggle-off`{.interpreted-text role="icon"}
`Unpublished`{.interpreted-text role="guilabel"} switch at the top of
the page to `fa-toggle-on`{.interpreted-text role="icon"}
`Published`{.interpreted-text role="guilabel"}; thus turning it from red
to green, and making it accessible for attendees.

{.align-center}

::: {.seealso}
\- `create_events`{.interpreted-text role="doc"} -
`track_manage_talks`{.interpreted-text role="doc"}
:::
