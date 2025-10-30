# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/track_manage_talks.md

Talks, proposals, and agenda
============================

With Odoo *Events*, users can utilize a fully-integrated event website,
where attendees can quickly access various tracks (talks, presentations,
etc.), view entire agendas, and propose talks for the event.

Event website
-------------

To access an event website, navigate to the specific event form in the
Odoo *Events* app, and click the `Go to Website`{.interpreted-text
role="guilabel"} smart button. Or, while on the Odoo-built website for
the company, click the `Events`{.interpreted-text role="guilabel"}
header option, and select the desired event to view that event\'s
website.

On the event website, there is an event-specific subheader menu with
different options to choose from.

With the *Schedule & Tracks* setting enabled in the Odoo *Events* app,
the following links are automatically added to the subheader menu,
located on the event website: `Talks`{.interpreted-text
role="guilabel"}, `Talk Proposals`{.interpreted-text role="guilabel"},
and `Agenda`{.interpreted-text role="guilabel"}.

{.align-center}

To enable the `Schedule & Tracks`{.interpreted-text role="guilabel"}
setting, navigate to `Events app -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
tick the checkbox beside `Schedule & Tracks`{.interpreted-text
role="guilabel"}, and click `Save`{.interpreted-text role="guilabel"}.

### Talks page

The `Talks`{.interpreted-text role="guilabel"} link takes the attendee
to a page filled with all the planned tracks for the event.

{.align-center}

At the top of `Talks`{.interpreted-text role="guilabel"} page, there are
drop-down filter menus beside a `Search
a talk...`{.interpreted-text role="guilabel"} search bar.

The first drop-down filter menu (with the starting title:
`Favorites`{.interpreted-text role="guilabel"}) is the only drop-down
filter menu that appears by default. When clicked, the resulting menu
presents two options: `Favorites`{.interpreted-text role="guilabel"} and
`All Talks`{.interpreted-text role="guilabel"}.

Selecting `Favorites`{.interpreted-text role="guilabel"} shows *only*
the tracks that have been favorited by the attendee.

::: {.note}
::: {.title}
Note
:::

If no tracks have been favorited, and the `Favorites`{.interpreted-text
role="guilabel"} filter is selected, Odoo presents all the event tracks.
:::

Selecting `All Talks`{.interpreted-text role="guilabel"} shows *all* the
tracks, regardless if they have been favorited or not.

The other drop-down filter menus that appear on this page are related to
any configured tags (and tag categories) created for event tracks in the
backend.

::: {.tip}
::: {.title}
Tip
:::

To add tags and tag categories to track forms, open a desired event
track form, and start typing a new tag in the `Tags`{.interpreted-text
role="guilabel"} field. Then, click
`Create and edit...`{.interpreted-text role="guilabel"} from the
resulting drop-down menu.

Doing so reveals a `Create Tags`{.interpreted-text role="guilabel"}
pop-up form.

{.align-center}

From here, users see the recently added tag in the
`Tag Name`{.interpreted-text role="guilabel"} field. Beneath that, there
is an option to add a specific `Color Index`{.interpreted-text
role="guilabel"} to the tag for added organization.

Lastly, there is the `Category`{.interpreted-text role="guilabel"}
field, where users can either select a pre-existing category for this
new tag, or create a new one.

All options in the `Category`{.interpreted-text role="guilabel"} field
for tags appear as their own drop-down filter menu on the
`Talks`{.interpreted-text role="guilabel"} page, located on the event
website.
:::

Beneath the drop-down filter menus at the top of the
`Talks`{.interpreted-text role="guilabel"} page, there is a list of
planned tracks for the specific event, organized by day.

If an attendee wishes to favorite a track, they can click the
`fa-bell-o`{.interpreted-text role="icon"} `(empty
bell)`{.interpreted-text role="guilabel"} icon, located to the right of
the track title. Attendees will know a track has been favorited when
they notice the icon has been changed to `fa-bell`{.interpreted-text
role="icon"} `(filled bell)`{.interpreted-text role="guilabel"} icon.

Favoriting a track this way places it on the list of
`Favorites`{.interpreted-text role="guilabel"}, which is accessible from
the default drop-down filter menu, located at the top of the
`Talks`{.interpreted-text role="guilabel"} page.

### Talk Proposals page

The `Talk Proposals`{.interpreted-text role="guilabel"} link takes
attendees to a page on the event website, wherein they can formerly
submit a proposal for a talk (`track`{.interpreted-text role="dfn"}) for
the event, via a custom online form.

{.align-center}

In addition to the form, an introduction to the page, along with any
other pertinent information related to the types of talks the event will
feature can be added, if needed.

The talk proposal form can be modified in a number of different ways,
via the web builder tools, accessible by clicking
`Edit`{.interpreted-text role="guilabel"} while on the specific page.

Then, proceed to edit any of the default fields, or add new forms with
the `Form`{.interpreted-text role="guilabel"} building block (located in
the `Blocks`{.interpreted-text role="guilabel"} section of the web
builder tools sidebar).

Once all the necessary information is entered into the form, the
attendees just need to click the `Submit Proposal`{.interpreted-text
role="guilabel"} button.

Then, that talk, and all the information entered on the form, can be
accessed on the `Event Tracks`{.interpreted-text role="guilabel"} page
for that specific event in the `Proposal`{.interpreted-text
role="guilabel"} stage, which is accessible via the
`Tracks`{.interpreted-text role="guilabel"} smart button on the event
form.

At that point, an internal user can review the proposed talk, and choose
to accept or deny the proposal.

If accepted, the internal user can then move the track to the next
appropriate stage in the Kanban pipeline on the
`Event Tracks`{.interpreted-text role="guilabel"} page for the event.
Then, they can open that track form, and click the
`Go to Website`{.interpreted-text role="guilabel"} smart button to
reveal that track\'s page on the event website.

From there, they can toggle the `Unpublished`{.interpreted-text
role="guilabel"} switch in the header to `Published`{.interpreted-text
role="guilabel"}, which allows all event attendees to view and access
the talk.

### Agenda page

The `Agenda`{.interpreted-text role="guilabel"} link takes attendees to
a page on the event website, showcasing an event calendar, depicting
when (and where) events are taking place for that specific event.

{.align-center}

Clicking any track on the calendar takes the attendee to that specific
track\'s detail page on the event website.

If an attendee wishes to favorite a track, they can click the
`fa-bell-o`{.interpreted-text role="icon"} `(empty
bell)`{.interpreted-text role="guilabel"} icon, located to the right of
the track title. Attendees will know a track has been favorited when
they notice the icon has been changed to `fa-bell`{.interpreted-text
role="icon"} `(filled bell)`{.interpreted-text role="guilabel"} icon.
