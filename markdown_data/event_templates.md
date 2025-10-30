# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/event_templates.md

Event templates
===============

The Odoo *Events* application provides the ability to customize and
configure event templates, which can be used to expedite the
event-creation process.

These templates can be created and personalized in the application, and
then selected from an event form, in order to quickly apply a series of
settings and elements to the new event, all of which can be further
modified, if needed.

Event templates page
--------------------

In the Odoo *Events* application, event templates can quickly be created
and modified.

To begin, navigate to
`Events app --> Configuration --> Event Templates`{.interpreted-text
role="menuselection"}. Doing so reveals the
`Event Templates`{.interpreted-text role="guilabel"} page. Here, find
all the existing event templates in the database.

{.align-center}

By default, Odoo provides three pre-configured event templates:
`Exhibition`{.interpreted-text role="guilabel"},
`Training`{.interpreted-text role="guilabel"}, and
`Sport`{.interpreted-text role="guilabel"}, which all have their own
unique customizations applied to them.

To change how these event templates appear on the *Template* drop-down
field on an event form, drag-and-drop them into any desired order, using
the `oi-draggable`{.interpreted-text role="icon"}
`(draggable)`{.interpreted-text role="guilabel"} icon, located to the
left of each event template line on the
`Event Templates`{.interpreted-text role="guilabel"} page.

::: {.seealso}
To learn more about event forms, refer to the
`create_events`{.interpreted-text role="doc"} documentation.
:::

Create event template
---------------------

There are two ways to create and configure an event template in Odoo
*Events*.

1.  **On the dashboard**, by navigating to
    `Events app --> Configuration --> Event
    Templates`{.interpreted-text role="menuselection"} and clicking the
    `New`{.interpreted-text role="guilabel"} button in the upper-left
    corner. Doing so reveals a blank event template form that can be
    customized in a number of different ways.
2.  **On an event form itself**. Start by typing the name of a new event
    template in the *Template* field, and click
    `Create and edit...`{.interpreted-text role="guilabel"} from the
    resulting drop-down menu. Doing so reveals a *Create Template*
    pop-up window, featuring all the same configurable fields and
    elements found on a standard event template form.

::: {.note}
::: {.title}
Note
:::

Clicking `Create "[template name]"`{.interpreted-text role="guilabel"}
from the resulting drop-down menu, via the *Template* field on an event
form creates the event template in the database, but does **not**
present the user with the *Create Template* pop-up window.

The event template would have to be modified, by selecting it on the
*Event Templates* page
(`Events app --> Configuration --> Event Templates`{.interpreted-text
role="menuselection"}).
:::

### Event template form

All the fields on a standard `Event Template`{.interpreted-text
role="guilabel"} form are *also* on the *Create Template* pop-up window,
accessible via the *Template* field on an event form.

{.align-center}

Start by providing the event template with a name in the
`Event Template`{.interpreted-text role="guilabel"} field, located at
the top of the form.

Beneath that field, there is a series of selectable checkboxes, all of
which are related to how the event menu will be displayed on the event
web page.

-   `Website Submenu`{.interpreted-text role="guilabel"}: enables a
    submenu on the event\'s website. When this checkbox is ticked, every
    other checkbox in this series is automatically ticked, as well.
    Then, choose to untick (deselect) any of the checkbox options, as
    desired.

-   `Tracks Menu Item`{.interpreted-text role="guilabel"}: adds a
    submenu item to navigate to a page displaying all planned tracks for
    the event.

-   `Track Proposals Menu Item`{.interpreted-text role="guilabel"}: adds
    a submenu item to navigate to a page, in which visitors can fill out
    a form to propose a track (talk, lecture, presentation, etc.) to
    happen during the event.

-   `Booth Menu Item`{.interpreted-text role="guilabel"}: adds a submenu
    item that takes visitors to a separate page, where an event booth
    can be purchased. Event booths can be customized and configured in
    the `Booths`{.interpreted-text role="guilabel"} tab of the event
    template form, from the *Booth Categories* page
    (`Events app --> Configuration --> Booth Categories`{.interpreted-text
    role="menuselection"}).

    ::: {.important}
    ::: {.title}
    Important
    :::

    First, users **must** create a booth product with the required
    *Event Booth* option set as the `Product Type`{.interpreted-text
    role="guilabel"} on the product form.
    :::

-   `Exhibitors Menu Item`{.interpreted-text role="guilabel"}: adds a
    submenu item that takes visitors to a separate page, showcasing all
    the exhibitors related to that specific event. Icons representing
    those exhibitors are also found on the footer of every
    event-specific web page, as well.

-   `Community`{.interpreted-text role="guilabel"}: adds a submenu item
    allowing attendees to access pre-configured virtual community rooms
    to meet with other attendees, and discuss various topics related to
    the event. When this checkbox is ticked, the
    `Allow Room Creation`{.interpreted-text role="guilabel"} feature
    becomes available.

-   `Allow Room Creation`{.interpreted-text role="guilabel"}: allow
    visitors to create community rooms of their own.

-   `Register Button`{.interpreted-text role="guilabel"}: adds a button
    at the end of the event submenu that takes visitors to the
    event-specific registration page when clicked.

Once the desired checkboxes have been ticked, select an appropriate
`Timezone`{.interpreted-text role="guilabel"} for the event from the
available drop-down menu.

Then, for organizational purposes, there is the option to add
`Tags`{.interpreted-text role="guilabel"} to this event template.

There is also the option to `Limit Registrations`{.interpreted-text
role="guilabel"} to this specific event template by ticking that
checkbox. If ticked, proceed to enter the number of
`Attendees`{.interpreted-text role="guilabel"} this template should be
limited to.

Beneath those general information fields at the top of the event
template form, there are five tabs:

-   `Tickets <events/event-tickets>`{.interpreted-text role="ref"}
-   `Communication <events/event-communication>`{.interpreted-text
    role="ref"}
-   `Booths <event_templates/event_template/booths>`{.interpreted-text
    role="ref"}
-   `Questions <events/event-questions>`{.interpreted-text role="ref"}
-   `Notes <events/event-notes>`{.interpreted-text role="ref"}

#### Booths tab {#event_templates/event_template/booths}

The `Booths`{.interpreted-text role="guilabel"} tab on an event template
form is the only tab that differentiates itself from a standard event
form, where the other tabs (`Tickets`{.interpreted-text
role="guilabel"}, `Communication`{.interpreted-text role="guilabel"},
`Questions`{.interpreted-text role="guilabel"}, and
`Notes`{.interpreted-text role="guilabel"}) are present and configured
using the same process. For more information about those tabs, refer to
the `create_events`{.interpreted-text role="doc"} documentation.

::: {.important}
::: {.title}
Important
:::

To create a booth or booth category, an event booth product **must** be
created in the database first, with the *Product Type* set to *Event
Booth*. **Only** products with that specific configuration can be
selected in the required *Product* field of a booth or booth category
form.
:::

::: {.note}
::: {.title}
Note
:::

Event booths can be created and customized in two ways in the Odoo
*Events* application. Either in the `Booths`{.interpreted-text
role="guilabel"} tab of an event template form, or by navigating to
`Events app --> Configuration --> Booth Categories`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}.
:::

To add a booth from the `Booths`{.interpreted-text role="guilabel"} tab
of an event template form, click `Add a
line`{.interpreted-text role="guilabel"}. Doing so reveals a blank
`Create Booths`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

Start by providing a `Name`{.interpreted-text role="guilabel"} for this
booth in the corresponding field at the top of the pop-up window.

Then, select an appropriate `Booth Category`{.interpreted-text
role="guilabel"} from the drop-down field below. Booth categories can be
created and modified from the *Booth Categories* page in the *Events*
application, which is accessible by navigating to
`Events app --> Configuration --> Booth
Categories`{.interpreted-text role="menuselection"}.

::: {.tip}
::: {.title}
Tip
:::

A `Booth Category`{.interpreted-text role="guilabel"} can be created
directly from this field on the `Create
Booths`{.interpreted-text role="guilabel"} pop-up window. To accomplish
that, type the name of the new booth category in the
`Booth Category`{.interpreted-text role="guilabel"} field, and select
either `Create`{.interpreted-text role="guilabel"} or `Create and
edit...`{.interpreted-text role="guilabel"} from the resulting drop-down
menu.

Clicking `Create`{.interpreted-text role="guilabel"} merely creates the
category, which can (and should be) customized at a later date. Clicking
`Create and edit...`{.interpreted-text role="guilabel"} reveals a new
`Create Booth
Category`{.interpreted-text role="guilabel"} pop-up window, from which
the category can be configured in a number of different ways.

{.align-center}

From this pop-up window, proceed to name the
`Booth Category`{.interpreted-text role="guilabel"}, modify its
`Booth Details`{.interpreted-text role="guilabel"} settings, configure
its `Sponsorship`{.interpreted-text role="guilabel"} options (if
applicable), and leave an optional `Description`{.interpreted-text
role="guilabel"} to explain any pertinent details related to this
specific category of booths.

There is also the option to add a photo/visual representation of the
booth category, via the `(camera)`{.interpreted-text role="guilabel"}
icon in the upper-right corner.

When all desired configurations are complete, click the
`Save & Close`{.interpreted-text role="guilabel"} button.

The same configurations and options are available by navigating to
`Events app -->
Configuration --> Booth Categories`{.interpreted-text
role="menuselection"}, and clicking `New`{.interpreted-text
role="guilabel"}.
:::

Once the desired `Booth Category`{.interpreted-text role="guilabel"} is
selected, the remaining fields on the `Create Booths`{.interpreted-text
role="guilabel"} pop-up window (`Currency`{.interpreted-text
role="guilabel"}, `Product`{.interpreted-text role="guilabel"}, and
`Price`{.interpreted-text role="guilabel"}) autopopulate, based on
information configured for that selected `Booth
Category`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

These fields **cannot** be modified from the
`Create Booths`{.interpreted-text role="guilabel"} pop-up window. They
can only be modified from the specific booth category form page.
:::

When all desired configurations are complete, click
`Save & Close`{.interpreted-text role="guilabel"} to save the booth, and
return to the event template form. Or, click
`Save & New`{.interpreted-text role="guilabel"} to save the booth, and
start creating another booth on a fresh
`Create Booths`{.interpreted-text role="guilabel"} pop-up window. Click
`Discard`{.interpreted-text role="guilabel"} to remove all changes, and
return to the event template form.

Once the booth has been saved, it appears in the
`Booths`{.interpreted-text role="guilabel"} tab on the event template
form.

Use event templates
-------------------

Once an event template is complete, it is accessible on all event forms
in the Odoo *Events* application.

To use an event template, navigate to the `Events app`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text role="guilabel"}
to open a new event form.

From the event form, click the `Template`{.interpreted-text
role="guilabel"} field to reveal all the existing event templates in the
database. They appear in the same order as they are listed in on the
*Event Templates* page
(`Events app --> Configuration --> Event Templates`{.interpreted-text
role="menuselection"}).

Select the desired event template from the `Template`{.interpreted-text
role="guilabel"} drop-down field on the event form. Pre-configured
settings automatically populate the event form, saving time during the
event creation process.

Any of these pre-configured settings related to the selected event
template chosen in the `Template`{.interpreted-text role="guilabel"}
field on an event form can be modified, as desired.

::: {.seealso}
`create_events`{.interpreted-text role="doc"}
:::
