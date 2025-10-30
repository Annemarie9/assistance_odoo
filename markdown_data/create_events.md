# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/create_events.md

Create events
=============

With the *Events* application, event organizers can create and configure
in-person or online-only events in Odoo. Each new event contains a
number of customizable options that are geared around specific event
logistics, as needed per event, such as ticket sales and registration
desk, booths, tracks, sponsors, rooms, and more.

Events can be manually created from scratch or built off of pre-made
templates. Once launched, the *Events* application then integrates with
the *Website* app for the front-end promotion and registration of the
event for attendees, the *Sales* app for the purchasing ability of paid
tickets, as well the *CRM* application through customizable lead
generation rules.

New event
---------

To create a new event, begin by navigating to the
`Events app`{.interpreted-text role="menuselection"} to land on the
default `Events`{.interpreted-text role="guilabel"} dashboard, in the
`oi-view-kanban`{.interpreted-text role="icon"}
`Kanban`{.interpreted-text role="guilabel"} view. From there, or
alternatively from the `oi-view-list`{.interpreted-text role="icon"}
`List`{.interpreted-text role="guilabel"} or
`fa-tasks`{.interpreted-text role="icon"} `Gantt`{.interpreted-text
role="guilabel"} views, click the `New`{.interpreted-text
role="guilabel"} button in the upper-left corner of the dashboard to
open up a new event form.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If certain fields do not readily appear on the event form, that means an
additional application needs to be installed, or the database is not
operating in a multi-company environment.

For example, the `Twitter Wall`{.interpreted-text role="guilabel"} field
**only** appears if the *Social Marketing* app is installed, and the
`Company`{.interpreted-text role="guilabel"} field **only** appears if
the database is working in a multi-company environment.

These are just *additional* elements that can be used for an event. They
are **not** required to create, host, and manage an event with Odoo
*Events*.
:::

Event form
----------

At the top of the event form are a series of smart buttons related to
various event metrics, which will autopopulate with pertinent data once
attendees begin to register, booths and sponsors sign on for the event,
the event takes place, and so on.

Primarily, these smart buttons are used as logistical portals to perform
specific actions for the event. The numeric displays are primarily for
quick reference points.

While those visual metrics are useful, they can still be clicked, and
used to navigate to specific event-related pages to modify and/or
perform any desired actions.

Beneath the smart buttons is the event form, which contains various
fields and clickable tabs that serve to configure the initial, necessary
details of the event.

The following are fields found on an event form:

-   `Event Name`{.interpreted-text role="guilabel"}: the title of the
    event. This field is **required**.

    ::: {.note}
    ::: {.title}
    Note
    :::

    To the right of the entered `Event Name`{.interpreted-text
    role="guilabel"}, there is a language tooltip, represented by an
    abbreviated language indicator (e.g. [EN]{.title-ref}). When
    clicked, a `Translate: name`{.interpreted-text role="guilabel"}
    pop-up window appears, displaying various pre-configured language
    translation options available in the database.
    :::

-   `Date`{.interpreted-text role="guilabel"}: when the event is
    scheduled to take place (expressed in your local timezone). This
    field is auto-populated, but modifiable, and is **required**.

-   `Display Timezone`{.interpreted-text role="guilabel"}: the timezone
    in which the event dates/times will be displayed on the website.
    This field is auto-populated, but modifiable, and is **required**.

-   `Language`{.interpreted-text role="guilabel"}: designate a specific
    language for all event communications to be translated into, if
    necessary. This field is blank, by default, so if event-related
    communications are being sent to recipients who speak a different
    language, be sure to configure this field properly.

-   `Twitter Wall`{.interpreted-text role="guilabel"}: creates a
    separate page on the event website to feature specific social posts
    on X (formerly Twitter) that contain pre-determined desired
    elements.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    To create and customize a `Twitter Wall`{.interpreted-text
    role="guilabel"}, type the name of the desired wall into the field,
    and select `Create and edit...`{.interpreted-text role="guilabel"}
    from the resulting drop-down menu.

    Doing so reveals `Create Twitter Wall`{.interpreted-text
    role="guilabel"} pop-up window.

    {.align-center}

    From this window, enter a `Wall Name`{.interpreted-text
    role="guilabel"}. Then, select a certain word or hashtag for Odoo to
    search for on X, like [\#WoodWorkingExpo24]{.title-ref}, for
    example.

    Next, determine the `Type of tweets`{.interpreted-text
    role="guilabel"} Odoo should showcase with that predetermined
    criteria. The choices in this field are: `Recent`{.interpreted-text
    role="guilabel"}, `Popular`{.interpreted-text role="guilabel"}, or
    `Mixed`{.interpreted-text role="guilabel"}.

    Users also have the option to add a brief
    `Description`{.interpreted-text role="guilabel"} to the wall, as
    well.

    Lastly, the greyed-out, non-modifiable
    `Website URL`{.interpreted-text role="guilabel"} field will
    autopopulate with the full URL needed to access the document through
    the event website.

    An image can also be added to the wall by clicking the
    `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon that appears when
    the cursor hovers over the `(camera)`{.interpreted-text
    role="guilabel"} placeholder image in the upper-right corner of the
    pop-up window.

    Then, from the resulting file explorer window, select the desired
    image to be added to the wall.

    This `Twitter Wall`{.interpreted-text role="guilabel"} field
    **only** appears on the event form if the *Social Marketing* app is
    installed, and an X account has been added as a stream on the
    application. To learn more, check out the
    `Social Marketing <../social_marketing>`{.interpreted-text
    role="doc"} documentation.
    :::

-   `Template`{.interpreted-text role="guilabel"}: choose a
    pre-configured event template from the resulting drop-down menu.

    Or, create a new one directly from this field, by typing in the name
    of the new template, and selecting either:

    -   `Create`{.interpreted-text role="guilabel"} (which creates the
        template, and can be edited later) or
    -   `Create and edit...`{.interpreted-text role="guilabel"} (which
        creates the template, and reveals a separate template page to
        configure the template in greater detail).

-   `Tags`{.interpreted-text role="guilabel"}: add any corresponding
    tags to briefly describe the event (e.g. [Online]{.title-ref},
    [Conference]{.title-ref}, etc.). Multiple tags can be added per
    event.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Tags can be displayed on events that are listed on the website by
    enabling the *Show on Website* checkbox from
    `Events app --> Configuration --> Event Tag Categories`{.interpreted-text
    role="menuselection"}.
    :::

-   `Organizer`{.interpreted-text role="guilabel"}: designate the
    organizer of the event (a company, contact, or employee).

-   `Responsible`{.interpreted-text role="guilabel"}: designate a user
    in the database to be responsible for this event.

-   `Company`{.interpreted-text role="guilabel"}: designate which
    company in the database to which this event is related. This field
    **only** appears if working in a multi-company environment. This
    field is auto-populated, but modifiable, and is **required**.

-   `Website`{.interpreted-text role="guilabel"}: choose to restrict the
    publishing of this event to a specific website created in Odoo. If
    this field is left blank, the event can be published on *all*
    websites in the database. To learn more, refer to the
    `Multiple websites
    <../../websites/website/configuration/multi_website>`{.interpreted-text
    role="doc"} documentation.

-   `Venue`{.interpreted-text role="guilabel"}: enter event venue
    details. This field pulls pertinent information from the *Contacts*
    application. Alternatively, `Venue`{.interpreted-text
    role="guilabel"} information can be manually added in this field, as
    well. At the very least, there **must** be a venue name, address,
    city, zip code/region, and country entered.

-   `Exhibition Map`{.interpreted-text role="guilabel"}: if desired,
    click the `Upload your file`{.interpreted-text role="guilabel"}
    button to upload an image of the event venue map.

-   `Limit Registrations`{.interpreted-text role="guilabel"}: if this
    checkbox is ticked, a limit to the amount of registrations is added
    to the event, and that desired limit amount **must** be entered in
    the blank field before `Attendees`{.interpreted-text
    role="guilabel"}.

-   `Badge Dimension`{.interpreted-text role="guilabel"}: select a
    desired paper format dimension for event badges. The options are:
    `A4 foldable`{.interpreted-text role="guilabel"},
    `A6`{.interpreted-text role="guilabel"}, or
    `4 per sheet`{.interpreted-text role="guilabel"}.

-   `Badge Background`{.interpreted-text role="guilabel"}: if desired,
    click the `Upload your file`{.interpreted-text role="guilabel"}
    button to upload a custom background image for event badges.

When the above fields in the event form have been adequately filled in,
move on to the four tabs at the bottom of the event form for further
customization.

Those tabs are: `Tickets <events/event-tickets>`{.interpreted-text
role="ref"}, `Communication
<events/event-communication>`{.interpreted-text role="ref"},
`Questions <events/event-questions>`{.interpreted-text role="ref"}, and
`Notes
<events/event-notes>`{.interpreted-text role="ref"}.

### Tickets tab {#events/event-tickets}

Create custom tickets (and ticket tiers) for events in the
`Tickets`{.interpreted-text role="guilabel"} tab of an event form.

{.align-center}

To create a ticket, click `Add a line`{.interpreted-text
role="guilabel"} in the `Tickets`{.interpreted-text role="guilabel"}
tab. Then, enter a name for the ticket (e.g. [Basic Ticket]{.title-ref}
or [VIP]{.title-ref}) in the `Name`{.interpreted-text role="guilabel"}
field.

In the `Product`{.interpreted-text role="guilabel"} field, either select
the pre-configured `Event Registration`{.interpreted-text
role="guilabel"} product, or create a new one by typing in the name of
the new event registration product, and then select either
`Create`{.interpreted-text role="guilabel"} or
`Create and edit...`{.interpreted-text role="guilabel"} from the
resulting drop-down menu.

::: {.important}
::: {.title}
Important
:::

Upon installing Odoo *Events*, a new product type, *Event Ticket*,
becomes available on product forms
(`Sales --> Products --> Products`{.interpreted-text
role="menuselection"}). In order for an event registration product to be
selectable in the *Tickets* tab, the event registration
`Product Type`{.interpreted-text role="guilabel"} **must** be set to
`Event Ticket`{.interpreted-text role="guilabel"}.
:::

::: {.tip}
::: {.title}
Tip
:::

Existing event registration products can be modified directly from this
field, as well, by clicking the `oi-arrow-right`{.interpreted-text
role="icon"} `(right arrow)`{.interpreted-text role="guilabel"} icon,
located beside the event registration product. Doing so reveals that
product\'s form. If the *Inventory* application is installed, additional
choices are available to customize for the product.
:::

Next, set the registration cost of the ticket in the
`Price`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The *Sales Price* defined on the event registration product\'s product
form sets the default cost of a ticket. Modifying the
`Price`{.interpreted-text role="guilabel"} of a ticket in the
`Tickets`{.interpreted-text role="guilabel"} tab, sets a new
registration cost of the ticket for that event.
:::

Next, determine a `Sales Start`{.interpreted-text role="guilabel"} and
`Sales End`{.interpreted-text role="guilabel"} date in their respective
fields. To do that, click into the blank field to reveal a calendar
popover. From there, select the desired date and time, then click
`fa-check`{.interpreted-text role="icon"} `Apply`{.interpreted-text
role="guilabel"}.

Then, if desired, designate a `Maximum`{.interpreted-text
role="guilabel"} amount of that specific ticket that can be sold.

The `Taken`{.interpreted-text role="guilabel"} column populates with the
number of tickets that are sold.

Optionally, in the `Color`{.interpreted-text role="guilabel"} column,
add a custom color to differentiate ticket badges. The selected color
displays on ticket badges when printed.

To delete any tickets from the `Tickets`{.interpreted-text
role="guilabel"} tab, click the `fa-trash-o`{.interpreted-text
role="icon"} `(trash can)`{.interpreted-text role="guilabel"} icon on
the corresponding line for the ticket that should be deleted.

::: {.tip}
::: {.title}
Tip
:::

To add an optional `Description`{.interpreted-text role="guilabel"}
column to the `Tickets`{.interpreted-text role="guilabel"} tab, click
the `oi-settings-adjust`{.interpreted-text role="icon"}
`(additional options)`{.interpreted-text role="guilabel"} drop-down
menu, located to the far-right of the column titles.

Then, tick the checkbox beside `Description`{.interpreted-text
role="guilabel"} from the resulting drop-down menu.

When added, the option to add brief descriptions for each event ticket
appears, which can be used to inform attendees of any perks or amenities
that may coincide with specific ticket purchases.
:::

### Communication tab {#events/event-communication}

In the `Communication`{.interpreted-text role="guilabel"} tab of an
event form, create various marketing communications that can be
scheduled to be sent at specific intervals leading up to, and following,
the event.

{.align-center}

::: {.note}
::: {.title}
Note
:::

By default, Odoo provides three separate pre-configured communications
on every new event form. One is an email sent after each registration to
confirm the purchase with the attendee. The other two are email event
reminders that are scheduled to be sent at different time intervals
leading up to the event to remind the recipient of the upcoming event.
:::

To add a communication in the `Communication`{.interpreted-text
role="guilabel"} tab, click `Add a line`{.interpreted-text
role="guilabel"}. Then, select the desired type of communication in the
`Send`{.interpreted-text role="guilabel"} field. The options are:
`Mail`{.interpreted-text role="guilabel"}, `SMS`{.interpreted-text
role="guilabel"}, `Social Post`{.interpreted-text role="guilabel"}, or
`WhatsApp`{.interpreted-text role="guilabel"}.

There is no limit to the number of communications that can be added in
the `Communication`{.interpreted-text role="guilabel"} tab of an event
form.

To delete a communication from the `Communication`{.interpreted-text
role="guilabel"} tab, click the `fa-trash-o`{.interpreted-text
role="icon"} `(trash can)`{.interpreted-text role="guilabel"} icon on
the corresponding communication line. Doing so removes the communication
from the event entirely.

::: {.important}
::: {.title}
Important
:::

The `Social Post`{.interpreted-text role="guilabel"} option **only**
appears if the *Social Marketing* application is installed. The
`WhatsApp`{.interpreted-text role="guilabel"} option **only** appears if
the *WhatsApp Integration* module is installed.

`WhatsApp <../../productivity/whatsapp>`{.interpreted-text role="doc"}
templates **cannot** be edited during active configuration. A separate
approval from *Meta* is required.
:::

#### Mail

Select an existing email template from the `Template`{.interpreted-text
role="guilabel"} drop-down menu.

Next, define the `Interval`{.interpreted-text role="guilabel"},
`Unit`{.interpreted-text role="guilabel"}, and
`Trigger`{.interpreted-text role="guilabel"} from their respective
drop-down fields, letting Odoo know when the communication should be
sent.

The `Unit`{.interpreted-text role="guilabel"} options are:
`Immediately`{.interpreted-text role="guilabel"},
`Hours`{.interpreted-text role="guilabel"}, `Days`{.interpreted-text
role="guilabel"}, `Weeks`{.interpreted-text role="guilabel"}, and
`Months`{.interpreted-text role="guilabel"}.

Then, select an option from the `Trigger`{.interpreted-text
role="guilabel"} drop-down menu. The options are:
`After each registration`{.interpreted-text role="guilabel"},
`Before the event`{.interpreted-text role="guilabel"}, and
`After the event`{.interpreted-text role="guilabel"}.

The `Sent`{.interpreted-text role="guilabel"} column populates with the
number of sent communications. And, beside the number are different
icons that appear, depending on the status of that particular
communication.

The status of *Running* is represented by a `fa-cogs`{.interpreted-text
role="icon"} `(three gears)`{.interpreted-text role="guilabel"} icon.
The status of *Sent* is represented by a `fa-check`{.interpreted-text
role="icon"} `(checkmark)`{.interpreted-text role="guilabel"} icon. And,
the status of *Scheduled* is represented by an
`fa-hourglass-half`{.interpreted-text role="icon"}
`(hourglass)`{.interpreted-text role="guilabel"} icon.

::: {.example}
To send a confirmation email an hour after an attendee registers for an
event, configure the following communication:

-   `Interval`{.interpreted-text role="guilabel"}: [1]{.title-ref}
-   `Unit`{.interpreted-text role="guilabel"}: `Hours`{.interpreted-text
    role="guilabel"}
-   `Trigger`{.interpreted-text role="guilabel"}:
    `After each registration`{.interpreted-text role="guilabel"}
:::

::: {.note}
::: {.title}
Note
:::

Existing email templates can be modified directly from the
`Template`{.interpreted-text role="guilabel"} drop-down menu, if
necessary, by clicking the `oi-arrow-right`{.interpreted-text
role="icon"} `(right arrow)`{.interpreted-text role="guilabel"} icon
next to the template name. Doing so reveals a separate page where users
can edit the `Content`{.interpreted-text role="guilabel"},
`Email Configuration`{.interpreted-text role="guilabel"}, and
`Settings`{.interpreted-text role="guilabel"} of that particular email
template.

To view and manage all email templates, activate
`developer-mode`{.interpreted-text role="ref"} and navigate to
`Settings --> Technical --> Email: Email Templates`{.interpreted-text
role="menuselection"}. Modify with caution as email templates effect all
communications where the template is used.
:::

### Questions tab {#events/event-questions}

In the `Questions`{.interpreted-text role="guilabel"} tab of an event
form, users can create brief questionnaires for registrants to interact
with, and respond to, after they register for the event.

These questions can be focused on gathering basic information about the
attendee, learning about their preferences, expectations, and other
things of that nature. This information can also be used to create more
detailed reporting metrics, in addition to being utilized to create
specific lead generation rules.

{.align-center}

::: {.note}
::: {.title}
Note
:::

By default, Odoo provides three questions in the
`Questions`{.interpreted-text role="guilabel"} tab for every event form.
The default questions require the registrant(s) to provide their
`Name`{.interpreted-text role="guilabel"} and `Email`{.interpreted-text
role="guilabel"}, and make it optional to include their
`Phone`{.interpreted-text role="guilabel"} number, as well.

The information gathered from the `Questions`{.interpreted-text
role="guilabel"} tab can be found on the `Attendees`{.interpreted-text
role="guilabel"} dashboard, accessible via the
`fa-users`{.interpreted-text role="icon"} `Attendees`{.interpreted-text
role="guilabel"} smart button. Odoo populates individual records that
contain basic information about the registrant(s), as well as their
preferences.
:::

To add a question in the `Questions`{.interpreted-text role="guilabel"}
tab, click `Add a line`{.interpreted-text role="guilabel"}. Doing so
reveals a `Create Question`{.interpreted-text role="guilabel"} pop-up
window. From here, users can create and configure their question.

{.align-center}

First, enter the question in the field at the top of the form. Then,
decide if the question should require a
`Mandatory Answer`{.interpreted-text role="guilabel"} and/or if Odoo
should `Ask once per order`{.interpreted-text role="guilabel"}, by
ticking their respective boxes, if desired.

If the `Ask once per order`{.interpreted-text role="guilabel"} checkbox
is ticked, the question will only be asked once, and its value is
propogated to every attendee in the order (if multiple tickets are
purchased at once). If the checkbox is *not* ticked for this setting,
Odoo will present the question for every attendee that is connected to
that registration.

Next, select a `Question Type`{.interpreted-text role="guilabel"}
option:

-   `Selection`{.interpreted-text role="guilabel"}: provide answer
    options to the question for registrants to choose from. Selectable
    answer options can be managed in the `Answers`{.interpreted-text
    role="guilabel"} column at the bottom of the pop-up window.
-   `Text Input`{.interpreted-text role="guilabel"}: lets the users
    enter a custom response to the question in a text field.
-   `Name`{.interpreted-text role="guilabel"}: provides registrants with
    a field for them to enter their name.
-   `Email`{.interpreted-text role="guilabel"}: provides registrants
    with a field for them to enter their email address.
-   `Phone`{.interpreted-text role="guilabel"}: provides registrants
    with a field for them to enter their phone number.
-   `Company`{.interpreted-text role="guilabel"}: provides registrants
    with a field for them to enter a company they are associated with.

Once all the desired configurations have been entered, either click
`Save & Close`{.interpreted-text role="guilabel"} to save the question,
and return to the `Questions`{.interpreted-text role="guilabel"} tab on
the event form, or click `Save & New`{.interpreted-text role="guilabel"}
to save the question and immediately create a new question on a new
`Create Question`{.interpreted-text role="guilabel"} pop-up window.

As questions are added to the `Questions`{.interpreted-text
role="guilabel"} tab, the informative columns showcase the
configurations of each question.

The informative columns are the following:

-   `Title`{.interpreted-text role="guilabel"}
-   `Mandatory`{.interpreted-text role="guilabel"}
-   `Once per Order`{.interpreted-text role="guilabel"}
-   `Type`{.interpreted-text role="guilabel"}
-   `Answers`{.interpreted-text role="guilabel"} (if applicable)

For `Selection`{.interpreted-text role="guilabel"} and
`Text Input`{.interpreted-text role="guilabel"} types, a
`fa-bar-chart`{.interpreted-text role="icon"} `Stats`{.interpreted-text
role="guilabel"} button appears on the right side of the question line.
When clicked, Odoo reveals a separate page, showcasing the response
metrics to that specific question.

To delete any question from the `Questions`{.interpreted-text
role="guilabel"} tab, click the `fa-trash-o`{.interpreted-text
role="icon"} `(trash can)`{.interpreted-text role="guilabel"} icon on
the corresponding question line.

There is no limit to the number of questions that can be added in the
`Questions`{.interpreted-text role="guilabel"} tab of an event form.

### Notes tab {#events/event-notes}

In the `Notes`{.interpreted-text role="guilabel"} tab of an event form,
users can leave detailed internal notes and/or event-related
instructions/information for attendees.

{.align-center}

In the `Note`{.interpreted-text role="guilabel"} field of the
`Notes`{.interpreted-text role="guilabel"} tab, users can leave internal
notes for other event employees, like \"to-do\" lists, contact
information, instructions, and so on.

In the `Ticket Instructions`{.interpreted-text role="guilabel"} field of
the `Notes`{.interpreted-text role="guilabel"} tab, users can leave
specific instructions for people attending the event that appear on the
attendees ticket.

Publish events
--------------

Once all configurations and modifications are complete on the event
form, it is time to publish the event on the website. Doing so makes the
event visible to website visitors, and makes it possible for people to
register for the event.

To publish an event after all the customizations are complete, click the
`fa-globe`{.interpreted-text role="icon"}
`Go to Website`{.interpreted-text role="guilabel"} smart button at the
top of the event form. Doing so reveals the event\'s web page, which can
be customized like any other web page on the site, via the
`Edit`{.interpreted-text role="guilabel"} button.

To learn more about website design functionality and options, consult
the `Building block
<../../websites/website/web_design/building_blocks>`{.interpreted-text
role="doc"} documentation.

Once the event website is ready to be shared, click the red
`Unpublished`{.interpreted-text role="guilabel"} toggle switch in the
header menu, changing it to a green `Published`{.interpreted-text
role="guilabel"} switch. At this point, the event web page is published,
and viewable/accessible by all website visitors.

Send event invites
------------------

To send event invites to potential attendees, navigate to the desired
event form, via `Events app --> Events`{.interpreted-text
role="menuselection"}, and click into the desired event. Following this,
click the `Invite`{.interpreted-text role="guilabel"} button in the
upper-left corner of the event form.

Doing so reveals a blank email form to fill out, as desired. To learn
more about how to create and customize emails like this, refer to the
`Create an email <email_marketing/create_email>`{.interpreted-text
role="ref"} documentation.

Proceed to create and customize an email message to send as an invite to
potential attendees. Remember to include a link to the registration page
on the event website, allowing interested recipients to quickly
register.

::: {.tip}
::: {.title}
Tip
:::

Sending emails from Odoo is subject to a daily limit, which, by default,
is 200. To learn more about daily limits, visit the
`email-issues-outgoing-delivery-failure-messages-limit`{.interpreted-text
role="ref"} documentation.
:::

::: {.seealso}
`track_manage_talks`{.interpreted-text role="doc"}
:::
