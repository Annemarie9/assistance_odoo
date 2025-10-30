# File: /content/odoo_doc17.0/fr/content/applications/marketing/events.md

show-content

:   

Events
======

Explore the various aspects of the Odoo **Events** detailed dashboard,
and useful settings, that can be utilized to generate and gather
valuable data about events (and their attendees), which can then be used
to improve decision-making and event-planning.

::: {.seealso}

:::

::: {.cards}
::: {.card target="events/create_events"}
Create events

Discover how to create events with Odoo.
:::

::: {.card target="events/sell_tickets"}
Sell event tickets

Learn how to create, configure, and sell event tickets.
:::

::: {.card target="events/track_manage_talks"}
Track and manage talks

See how to create, track, and manage event tracks with Odoo.
:::

::: {.card target="events/event_templates"}
Event templates

Expedite the event-creation process with event templates.
:::

::: {.card target="events/event_tracks"}
Event tracks

Learn how to create, track, and manage event tracks with Odoo.
:::

::: {.card target="events/event_booths"}
Event booths

Create, manage, and sell event booths.
:::

::: {.card target="events/registration_desk"}
Registration Desk

Instantly grant access to event attendees with Odoo\'s Registration Desk
feature.
:::

::: {.card target="events/revenues_report"}
Revenues report

Analyze the financial success of events with Odoo.
:::
:::

Events dashboard
----------------

When the **Events** application is opened, Odoo reveals the main
`Events`{.interpreted-text role="guilabel"} dashboard, which can be
viewed in a number of different ways. Those different view options are
accessible from the `Events`{.interpreted-text role="guilabel"}
dashboard in the upper-right corner, via a series of view-related icon
buttons.

By default, the `Events`{.interpreted-text role="guilabel"} dashboard is
displayed in the `oi-view-kanban`{.interpreted-text role="icon"}
`Kanban`{.interpreted-text role="guilabel"} view, which is populated
with a variety of pipeline stages.

{.align-center}

This view showcases all the events in the database in their respective
stages. By default, the stages are: `New`{.interpreted-text
role="guilabel"}, `Booked`{.interpreted-text role="guilabel"},
`Announced`{.interpreted-text role="guilabel"},
`Ended`{.interpreted-text role="guilabel"}, and
`Cancelled`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Ended`{.interpreted-text role="guilabel"} and
`Cancelled`{.interpreted-text role="guilabel"} stages are folded, by
default, and located to the right of the other stages.
:::

On each event card, find the scheduled date of the event, the name of
the event, the location, the number of expected
`Attendees`{.interpreted-text role="guilabel"}, any scheduled activities
related to the event, the status of the event, and the person
responsible for the event.

To quickly add a new event to a pipeline, click the
`fa-plus`{.interpreted-text role="icon"} `(plus)`{.interpreted-text
role="guilabel"} icon at the top of the stage to which the event should
be added to reveal a blank Kanban card to fill out.

{.align-center}

In this blank Kanban card, enter the name of `Event`{.interpreted-text
role="guilabel"}, along with the start and end `Date`{.interpreted-text
role="guilabel"} and time.

Then, either click `Add`{.interpreted-text role="guilabel"} to add it to
the stage and edit it later, or click `Edit`{.interpreted-text
role="guilabel"} to add the event to stage and edit its configurations
on a separate page.

Each event card can be dragged-and-dropped into any stage on the Kanban
pipeline, providing easy organizational access.

Settings
--------

To access the event settings and feature options in Odoo **Events**,
navigate to
`Events app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. From here, tick the checkboxes beside the desired
settings and/or features, and click `Save`{.interpreted-text
role="guilabel"} to activate them.

### Events section

In the `Events`{.interpreted-text role="guilabel"} section of the
`Settings`{.interpreted-text role="guilabel"} page, there are selectable
features that can be enabled to add various elements to events created
with the Odoo **Events** application.

{.align-center}

The `Schedule & Tracks`{.interpreted-text role="guilabel"} feature
allows users to manage and publish a schedule with tracks for events.
*Tracks* is a catch-all term that refers to talks, lectures,
demonstrations, presentations, and other similar elements that users may
choose to include as part of an event.

When the `Schedule & Tracks`{.interpreted-text role="guilabel"} feature
is enabled, two additional fields appear beneath it:
`Live Broadcast`{.interpreted-text role="guilabel"} and
`Event Gamification`{.interpreted-text role="guilabel"}.

The `Live Broadcast`{.interpreted-text role="guilabel"} feature lets
users air tracks online, via a *YouTube* integration.

The `Event Gamification`{.interpreted-text role="guilabel"} feature lets
users share a quiz after any event track, in order for attendees to
gauge how much they learned from the track they just saw/heard.
Companies can also benefit from this feature, in that the subsequent
responses and results of the quizzes can help determine where a
company\'s strengths and weaknesses are, when it comes to their
presentations.

Next, is the `Online Exhibitors`{.interpreted-text role="guilabel"}
feature. This feature allows users to display sponsors and exhibitors on
event pages, which can serve as a valuable incentive to encourage
partners and businesses to participate in the event.

The `Jitsi Server Domain`{.interpreted-text role="guilabel"} field
represents an external conferencing service that is integrated with
Odoo. It is what is used to create and host virtual conferences,
community rooms, and other similar elements for events.

The `Community Chat Rooms`{.interpreted-text role="guilabel"} feature
allows users to create virtual conference rooms for event attendees,
providing them with a centralized place to meet and discuss anything
related to the event.

Lastly, there is the `Booth Management`{.interpreted-text
role="guilabel"} feature. This feature provides users with the ability
to create and manage event booths and booth reservations. When enabled,
users can create different booth tiers, with individual price points,
and sell them to interested parties.

### Registration section

The `Registration`{.interpreted-text role="guilabel"} section of the
`Settings`{.interpreted-text role="guilabel"} page provides selectable
settings that are directly related to event registration.

{.align-center}

The `Tickets`{.interpreted-text role="guilabel"} setting allows users to
sell event tickets, via standard sales orders.

The `Online Ticketing`{.interpreted-text role="guilabel"} setting
creates a selectable *Event Ticket* product type on product forms, which
provides users with the ability to sell event tickets online, via their
website/eCommerce store.

### Attendance section

In the `Attendance`{.interpreted-text role="guilabel"} section of the
`Settings`{.interpreted-text role="guilabel"} page, there is a
selectable setting that is directly related to how attendees can
attend/enter the event.

{.align-center}

The `Use Event Barcode`{.interpreted-text role="guilabel"} setting, when
activated, enables barcode (and QR code) scanning for attendees to enter
the event. This provides attendees with quick access, and helps Odoo
users easily track, manage, and analyze all event attendees.

The `Barcode Nomenclature`{.interpreted-text role="guilabel"} field,
beneath the `Use Event Barcode`{.interpreted-text role="guilabel"}
setting, is set to `Default Nomenclature`{.interpreted-text
role="guilabel"}, by default, but can be changed at any time.

Create events
-------------

With Odoo **Events**, events can be manually created from scratch or
built off of pre-made templates.

Once launched, the **Events** application then integrates with the
**Website** app for the front-end promotion and registration of the
event for attendees, the **Sales** app for the purchasing ability of
paid tickets, and the **CRM** application through customizable lead
generation rules.

::: {.seealso}
`events/create_events`{.interpreted-text role="doc"}
:::

Sell event tickets
------------------

Create custom ticket tiers (with various price points) for potential
event attendees to choose from, directly on the event template form,
under the *Tickets* tab.

Odoo simplifies the ticket-purchasing process by providing plenty of
payment method options, as well.

::: {.seealso}
`events/sell_tickets`{.interpreted-text role="doc"}
:::

Track and manage talks
----------------------

Discover how to access various event tracks (talks, presentations,
etc.), view entire agendas, and learn how attendees can propose talks
for the event.

::: {.seealso}
`events/track_manage_talks`{.interpreted-text role="doc"}
:::

Event templates
---------------

Learn the process to customize and configure event templates, which can
be used to expedite the event-creation process.

::: {.seealso}
`events/event_templates`{.interpreted-text role="doc"}
:::

Event booths
------------

Explore the various ways to create, manage, and sell event booths with
the Odoo **Events** application.

::: {.seealso}
`events/event_booths`{.interpreted-text role="doc"}
:::

Event tracks
------------

Find out how to create, manage, and schedule different experiences (aka
*Tracks*) for events with Odoo.

::: {.seealso}
`events/event_tracks`{.interpreted-text role="doc"}
:::

Registration desk
-----------------

Grant access to event attendees quickly and easily with the Odoo
**Events** *Registration Desk* feature.

::: {.seealso}
`events/registration_desk`{.interpreted-text role="doc"}
:::

Revenues report
---------------

Gain invaluable insight into event-related revenues with customizable
reports and metrics.

::: {.seealso}
`events/revenues_report`{.interpreted-text role="doc"}
:::

::: {.toctree}
events/create\_events events/sell\_tickets events/track\_manage\_talks
events/event\_templates events/event\_booths events/event\_tracks
events/registration\_desk events/revenues\_report
:::
