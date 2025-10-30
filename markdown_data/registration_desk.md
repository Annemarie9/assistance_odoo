# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/registration_desk.md

Registration Desk
=================

Use the *Registration Desk* feature in Odoo **Events** to grant access
to registered event attendees as they arrive, and store attendee-related
data in the reporting metrics.

Registration Desk page
----------------------

On a mobile device (on the Odoo app or in a browser), open the
`Events app`{.interpreted-text role="menuselection"}, and click the
`Registration Desk`{.interpreted-text role="guilabel"} to view the
`Registration Desk`{.interpreted-text role="guilabel"} page.

{.align-center}

At the bottom of the `Registration Desk`{.interpreted-text
role="guilabel"} box, there are options to either `Scan
a badge`{.interpreted-text role="guilabel"} or
`Select Attendee`{.interpreted-text role="guilabel"}.

Scan a badge
------------

Scan the codes present on event attendee badges, by navigating to
`Events app -->
Registration Desk`{.interpreted-text role="menuselection"}, and
selecting the `Scan a badge`{.interpreted-text role="guilabel"} option.

::: {.important}
::: {.title}
Important
:::

Odoo **must** be granted access to the camera being used for the
`Scan a badge`{.interpreted-text role="guilabel"} option to work.
:::

Once Odoo has access to the camera, a
`Barcode Scanner`{.interpreted-text role="guilabel"} pop-up window
appears, showing the camera\'s point-of-view. There is also a specified
view finder box present, whose size can be manually modified,
accordingly, using the `fa-crop`{.interpreted-text role="icon"}
`(crop)`{.interpreted-text role="guilabel"} icon.

{.align-center}

When the badge code is in the middle of the view finder box, the code is
scanned, the `Barcode Scanner`{.interpreted-text role="guilabel"} pop-up
window disappears, and the attendee is granted access to the event. Once
the code is scanned, their attendance is logged in the Odoo **Events**
app.

If the barcode being scanned is invalid, an error pop-up message appears
in the upper-right corner.

Select attendee
---------------

Manually grant access to event attendees, by navigating to
`Events app -->
Registration Desk`{.interpreted-text role="menuselection"}, and
selecting the `Select Attendee`{.interpreted-text role="guilabel"}
option.

Odoo reveals an `Attendees`{.interpreted-text role="guilabel"} page,
with all the attendees for every event in the database, in a default
`oi-view-kanban`{.interpreted-text role="icon"}
`Kanban`{.interpreted-text role="guilabel"} view.

{.align-center}

On the `Attendees`{.interpreted-text role="guilabel"} page, each
attendee card displays that person\'s name, which event they are
registered to attend, their associated company (if applicable), what
ticket tier they purchased (if applicable), along with two buttons: a
`fa-check`{.interpreted-text role="icon"}
`(checkmark)`{.interpreted-text role="guilabel"} and
`fa-undo`{.interpreted-text role="icon"}
`(counter-clockwise arrow)`{.interpreted-text role="guilabel"}.

To grant access to a person, marking them as attended, click the
`fa-check`{.interpreted-text role="icon"}
`(checkmark)`{.interpreted-text role="guilabel"} button on that
attendee\'s card.

Click the `fa-undo`{.interpreted-text role="icon"}
`(counter-clockwise arrow)`{.interpreted-text role="guilabel"} button on
an attendee\'s card to undo the previous action.

::: {.tip}
::: {.title}
Tip
:::

It is recommended to use an event-specific filter on the
`Attendees`{.interpreted-text role="guilabel"} page, via the search bar
drop-down menu.

To do that, click the `fa-sort-desc`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} beside the seach bar
to reveal a drop-down menu with `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} options.

For example, click the `Event`{.interpreted-text role="guilabel"}
option, in the `Group By`{.interpreted-text role="guilabel"} column.
Then, click away to remove the drop-down menu. Odoo reveals the
`Attendees`{.interpreted-text role="guilabel"} page with event-specific
columns, allowing users to locate specific event attendees.
:::

::: {.seealso}
`../../essentials/search`{.interpreted-text role="doc"}
:::
