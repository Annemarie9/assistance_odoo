# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/shop_floor/shop_floor_overview.md

Shop Floor overview
===================

The *Shop Floor* module is a companion module to the *Manufacturing*
app. *Shop Floor* provides a visual interface for processing
manufacturing orders (MOs) and work orders. It also allows manufacturing
employees to track the amount of time spent working on manufacturing and
work orders.

The *Shop Floor* module is installed alongside the *Manufacturing* app.
It cannot be installed by itself. To install the *Manufacturing* app,
navigate to `Apps`{.interpreted-text role="menuselection"}, search for
[manufacturing]{.title-ref} in the `Search...`{.interpreted-text
role="guilabel"} bar, and then click `Install`{.interpreted-text
role="guilabel"} on the `Manufacturing`{.interpreted-text
role="guilabel"} app card.

::: {.important}
::: {.title}
Important
:::

The *Shop Floor* module replaces the tablet view functionality of the
*Manufacturing* app, and is only available in Odoo versions 16.4 and
later.

To check the version number of an Odoo database, navigate to
`Settings`{.interpreted-text role="menuselection"} and scroll down to
the `About`{.interpreted-text role="guilabel"} section at the bottom of
the page. The version number is displayed there.

To switch to a newer version of Odoo, see the documentation on
`upgrading a database
<../../../../administration/upgrade>`{.interpreted-text role="doc"}.
:::

Navigation
----------

*Shop Floor* is broken down into three main views, which can be selected
from the navigation bar at the top of the module:

-   The `All`{.interpreted-text role="guilabel"} page serves as the main
    dashboard for the module, and displays information cards for
    `MOs (Manufacturing Orders)`{.interpreted-text role="abbr"}.
-   Each work center also has a dedicated page, which shows information
    cards for work orders assigned to that work center. Work center
    pages can be toggled on or off by clicking the `+
    (plus)`{.interpreted-text role="guilabel"} button in the navigation
    bar, selecting or deselecting them on the pop-up window that
    appears, and then clicking `Confirm`{.interpreted-text
    role="guilabel"}.
-   The `My`{.interpreted-text role="guilabel"} page shows information
    cards for all work orders assigned to the employee whose profile is
    currently active in the operator panel on the left side of the
    module. Other than only showing work orders assigned to the active
    employee, this page functions the same as the pages for each work
    center.

::: {.tip}
::: {.title}
Tip
:::

To isolate an or work order, so that no other orders appear, simply
search the reference number of the in the `Search...`{.interpreted-text
role="guilabel"} bar at the top of the module. This search filter
remains active while switching between the different module views.
:::

On the left side of the module is the operator panel, which shows all of
the employees currently signed in to *Shop Floor*, and allows new
employees to sign in. The operator panel is always available in the
module, regardless of which view is selected. It can be toggled on or
off by clicking the `sidebar`{.interpreted-text role="guilabel"} button
at the extreme left of the navigation bar.

{.align-center}

### All page

By default, the `All`{.interpreted-text role="guilabel"} page shows an
information card for every that is *ready to start*. An is considered
ready to start once it has been confirmed, and all required components
are available.

To view every confirmed regardless of readiness, click the
`x`{.interpreted-text role="guilabel"} button on the
`Ready to Start`{.interpreted-text role="guilabel"} filter to remove it
from the `Search...`{.interpreted-text role="guilabel"} bar.

#### MO information card

An information card on the `All`{.interpreted-text role="guilabel"} page
shows all of the relevant details of the associated , and also provides
employees with options for processing the .

The header for an card shows the number, the product and number of units
being produced, and the status of the . If work has not yet begun on the
, the status appears as `Confirmed`{.interpreted-text role="guilabel"}.
Once work has begun, the status updates to
`In Progress`{.interpreted-text role="guilabel"}. If all work orders for
an have been completed and the is ready to close, the status updates to
`To Close`{.interpreted-text role="guilabel"}.

The main body of an card shows a line for each completed work order, if
any, followed by the current work order that needs to be completed.
Completed work orders are indicated by a green check mark to the right
of title of the work order. The current work order is indicated by a
button that opens the page for the work center to which the order is
assigned.

Below the current work order is a line titled
`Register Production`{.interpreted-text role="guilabel"}, which is used
to record the number of product units produced. To manually enter the
number of units produced, click on the
`Register Production`{.interpreted-text role="guilabel"} line, enter a
value in the `Units`{.interpreted-text role="guilabel"} field of the
resulting pop-up window, then click `Validate`{.interpreted-text
role="guilabel"}.

Alternatively, click the `# Units`{.interpreted-text role="guilabel"}
button on the right side of the line, which automatically records the
number of units the was created for as the number of units produced. For
example, if an is created for 10 units of a dining table, clicking the
`10 units`{.interpreted-text role="guilabel"} button records that 10
units were produced.

The footer of the card displays a `Close Production`{.interpreted-text
role="guilabel"} button. This is used to close the once production is
completed. However, if there are any quality checks required for the as
a whole (not the work orders within it), a
`Quality Checks`{.interpreted-text role="guilabel"} button appears
instead. Clicking `Quality Checks`{.interpreted-text role="guilabel"}
opens a pop-up window, from which any required quality checks can be
completed.

After clicking `Close Production`{.interpreted-text role="guilabel"},
the card begins to fade away, and an `Undo`{.interpreted-text
role="guilabel"} button appears on the footer. Clicking
`Undo`{.interpreted-text role="guilabel"} causes the to remain open.
Once the card disappears completely, the work order is closed.

On the right side of the footer is an `⋮ (options)`{.interpreted-text
role="guilabel"} button, which opens a pop-up window with additional
options for the :

-   `Scrap`{.interpreted-text role="guilabel"} is used to send
    components to a scrap location when they are found to be defective.
-   `Add Work Order`{.interpreted-text role="guilabel"} is used to add
    an additional work order to the .
-   `Add Component`{.interpreted-text role="guilabel"} is used to add an
    additional component to the .
-   `Open Backend MO`{.interpreted-text role="guilabel"} opens the in
    the Manufacturing app.

{.align-center}

### Work center pages

By default, the page for each work center shows an information card for
every work order assigned to it that is *ready to start*. A work order
is considered ready to start once the it is a part of is ready to start,
and any preceding work orders have been completed.

To view every confirmed work order assigned to a work center regardless
of readiness, click the `x`{.interpreted-text role="guilabel"} button on
the `Ready to Start`{.interpreted-text role="guilabel"} filter to remove
it from the `Search...`{.interpreted-text role="guilabel"} bar.

#### Work order information card

A work order information card on a work center\'s page shows all of the
relevant details of the associated work order, and also provides
employees with options for processing the work order.

The header for a work order card shows the reference number of the that
the work order is a part of, the product and number of units being
produced, and the status of the work order. If work has not yet begun on
the work order, the status appears as `To Do`{.interpreted-text
role="guilabel"}. Once work has begun, the status updates to display a
timer showing the total time the work order has been worked on.

The main body of a work order card shows a line for each step required
to complete the work order. Work order steps can be completed by
clicking on the line, then following the instructions on the pop-up
window that appears. Alternatively, clicking the checkbox on the right
side of each line automatically marks the step as completed.

Below the final step of the work order is a line titled
`Register Production`{.interpreted-text role="guilabel"}, which
functions the same as the `Register Production`{.interpreted-text
role="guilabel"} line on an card. Registering the number of units
produced using the `Register Production`{.interpreted-text
role="guilabel"} line on a work order card also completes the step for
the associated card.

If the work order being processed is the final work order for the , a
`Close
Production`{.interpreted-text role="guilabel"} button appears on the
footer of the work order card. Clicking `Close
Production`{.interpreted-text role="guilabel"} closes both the work
order and the , unless a quality check is required for the . In this
case, the quality check must be completed from the card before the can
be closed.

Alternatively, if the requires the completion of additional work orders,
a `Mark as
Done`{.interpreted-text role="guilabel"} button appears instead.
Clicking `Mark as Done`{.interpreted-text role="guilabel"} marks the
current work order as completed, and causes the next work order to
appear on the page for the work center it is assigned to.

After clicking `Close Production`{.interpreted-text role="guilabel"} or
`Mark as Done`{.interpreted-text role="guilabel"}, the work order card
begins to fade away, and an `Undo`{.interpreted-text role="guilabel"}
button appears on the footer. Clicking `Undo`{.interpreted-text
role="guilabel"} causes the work order to remain open. Once the work
order card disappears completely, the work order is marked as
`Finished`{.interpreted-text role="guilabel"} on the .

On the right side of the footer is an `⋮ (options)`{.interpreted-text
role="guilabel"} button, which opens a pop-up window with additional
options for the work order:

-   `Scrap`{.interpreted-text role="guilabel"} is used to send
    components to a scrap location when they are found to be defective.
-   `Add Component`{.interpreted-text role="guilabel"} is used to add an
    additional component to the .
-   `Move to work center`{.interpreted-text role="guilabel"} is used to
    transfer the work order to a different work center.
-   `Suggest a Worksheet improvement`{.interpreted-text role="guilabel"}
    allows the user to propose a change to the work order\'s
    instructions or steps.
-   `Create a Quality Alert`{.interpreted-text role="guilabel"} opens a
    quality alert form that can be filled out to alert a quality team
    about a potential issue.

{.align-center}

### Operator panel

The operator panel is used to manage the employees that are signed in to
the *Shop Floor* module. The panel shows the name and profile picture of
every employee that is currently signed in across all instances of the
database.

To interact with *Shop Floor* as a specific employee, click the
employee\'s name to activate their profile. Profiles that are not active
appear with their names and profile pictures greyed-out.

When an employee is selected in the operator panel, they can begin
working on a work order by clicking the work order\'s heading. If an
employee is working on one or more work orders, the work order title(s)
appear under their name, along with a timer showing how long they\'ve
been working on each order.

To add a new employee to the operator panel, click the
`+ Add Operator`{.interpreted-text role="guilabel"} button at the bottom
of the panel. Then, select an employee from the
`Select Employee`{.interpreted-text role="guilabel"} pop-up window.

To remove an employee from the operator panel, simply click the
`x`{.interpreted-text role="guilabel"} button next to their name in the
panel.

{.align-center}

MO/WO prioritization
--------------------

The **Shop Floor** module uses the *scheduled date* entered on
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"} to
prioritize the `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"} and work orders that appear on the module\'s dashboard and
work center pages. `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"} and work orders scheduled sooner are more highly
prioritized, and appear before orders which are scheduled further out.

To specify the scheduled date on an , begin by navigating to
`Manufacturing app
--> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"} to create a new .

Click on the `Scheduled Date`{.interpreted-text role="guilabel"} field
to open a calendar popover window. By default, the
`Scheduled Date`{.interpreted-text role="guilabel"} field, and its
corresponding pop-up window, show the current date and time.

Use the calendar to select the date on which processing should begin for
the . In the two fields at the bottom of the popover window, enter the
hour and minute at which processing should begin, using the 24-hour
clock format.

Finally, click `Apply`{.interpreted-text role="guilabel"} at the bottom
of the popover window to set the date and time for the
`Scheduled Date`{.interpreted-text role="guilabel"} field. Then, click
the `Confirm`{.interpreted-text role="guilabel"} button at the top of
the to confirm it.

Once the is confirmed, it appears in the **Shop Floor** module, as long
is it has the `Ready`{.interpreted-text role="guilabel"} status, which
means all components are available.

On the Odoo dashboard, click on the `Shop Floor`{.interpreted-text
role="menuselection"} module to open it. The
`All MO #`{.interpreted-text role="guilabel"} page of the dashboard
displays *Ready* `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"}, organized in order of their scheduled dates.

At the top of the module, select a work center to see the work orders
assigned to it. The page for each work center organizes work orders,
based on the scheduled dates of their corresponding
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"}.

::: {.example}
Three `MOs (Manufacturing Orders)`{.interpreted-text role="abbr"} are
confirmed for a *Bookcase* product:

-   WH/MO/00411 has a `Scheduled Date`{.interpreted-text
    role="guilabel"} of August 16th.
-   WH/MO/00412 has a `Scheduled Date`{.interpreted-text
    role="guilabel"} of August 20th.
-   WH/MO/00413 has a `Scheduled Date`{.interpreted-text
    role="guilabel"} of August 18th.

On the `All MO #`{.interpreted-text role="guilabel"} page of the **Shop
Floor** module, the cards for each appear in this order: WH/MO/00411,
WH/MO/00413, WH/MO/00412.

{.align-center}

Each requires one work order, carried out at
`Assembly Station 1`{.interpreted-text role="guilabel"}. Clicking on the
`Assembly Station 1`{.interpreted-text role="guilabel"} button at the
top of the screen opens the page for the work center, which displays one
card for each work order, appearing in the same order as their
corresponding `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"}.
:::
