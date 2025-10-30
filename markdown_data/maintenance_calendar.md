# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/maintenance/maintenance_calendar.md

Maintenance calendar
====================

Avoiding equipment breakdowns, and blocks in warehouse work centers,
requires constant equipment maintenance. Timely corrective maintenance
for machines and tools that break unexpectedly, as well as preventive
maintenance to ensure that such issues are avoided, are key to keeping
warehouse operations running smoothly.

In Odoo *Maintenance*, users can access the *Maintenance Calendar* to
create, schedule, and edit both corrective and preventive maintenance
requests, to stay on top of equipment and work centers.

Create maintenance request
--------------------------

Maintenance requests can be created directly from the *Maintenance
Calendar*. To access the calendar, navigate to
`Maintenance app --> Maintenance --> Maintenance Calendar`{.interpreted-text
role="menuselection"}.

To create a new request, click anywhere on the calendar. Doing so opens
a `New Event`{.interpreted-text role="guilabel"} pop-up window. In the
`Name:`{.interpreted-text role="guilabel"} field, assign a title to the
new request.

{.align-center}

Clicking `Create`{.interpreted-text role="guilabel"} on the pop-up
window saves the new request with no additional details. If the
request\'s creation should be canceled, click `Cancel`{.interpreted-text
role="guilabel"}.

To add more details and schedule the request for a specific date and
time, click `Edit`{.interpreted-text role="guilabel"}.

Clicking `Edit`{.interpreted-text role="guilabel"} opens a blank
maintenance request form, where various details about the request can be
filled out.

### Edit maintenance request

In the `Request`{.interpreted-text role="guilabel"} field, assign a
title to the new request. In the `Created By`{.interpreted-text
role="guilabel"} field, from the drop-down menu, select which user the
request was created by. By default, this field populates with the user
actually creating the request.

{.align-center}

In the `For`{.interpreted-text role="guilabel"} field, from the
drop-down menu, select if this request is being created for a piece of
`Equipment`{.interpreted-text role="guilabel"}, or a
`Work Center`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If `Work Center`{.interpreted-text role="guilabel"} is selected in the
`For`{.interpreted-text role="guilabel"} field\'s drop-down menu, two
additional fields appear on the form: `Work Center`{.interpreted-text
role="guilabel"} and `Block Workcenter`{.interpreted-text
role="guilabel"}.

In the `Work Center`{.interpreted-text role="guilabel"} field, select
which work center in the warehouse this maintenance request applies to.

If the `Block Workcenter`{.interpreted-text role="guilabel"} option\'s
checkbox is ticked, it is not possible to plan work orders, or other
maintenance requests, in this work center during the time that this
request is being performed.
:::

If `Equipment`{.interpreted-text role="guilabel"} is selected in the
`For`{.interpreted-text role="guilabel"} field, which it is by default,
select which machine or tool requires maintenance from the
`Equipment`{.interpreted-text role="guilabel"} field. Once a specific
piece of equipment is selected, a greyed-out
`Category`{.interpreted-text role="guilabel"} field appears, listing the
*Equipment Category* to which the equipment belongs.

In the `Worksheet Template`{.interpreted-text role="guilabel"} field, if
necessary, click the drop-down menu to select a worksheet template.
These templates are custom templates that can be filled out by the
employee performing the maintenance.

Under the `Category`{.interpreted-text role="guilabel"} field, the
`Request Date`{.interpreted-text role="guilabel"} field displays the
date requested for the maintenance to happen.

The `Maintenance Type`{.interpreted-text role="guilabel"} field provides
two selectable radio button options: `Corrective`{.interpreted-text
role="guilabel"} and `Preventive`{.interpreted-text role="guilabel"}.

`Corrective`{.interpreted-text role="guilabel"} maintenance is for
requests that arise for immediate needs, such as broken equipment, while
`Preventive`{.interpreted-text role="guilabel"} maintenance is for
planned requests, to avoid breakdowns in the future.

If this request is tied to a specific
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, select that
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} from the
`Manufacturing
Order`{.interpreted-text role="guilabel"} field.

From the drop-down menu for the `Team`{.interpreted-text
role="guilabel"} field, select the desired maintenance team who will
perform the maintenance. In the `Responsible`{.interpreted-text
role="guilabel"} field, select the technician responsible for the
request.

{.align-center}

In the `Scheduled Date`{.interpreted-text role="guilabel"} field, click
the date to open a calendar popover. From this popover, select the
planned date of the maintenance, and click `Apply`{.interpreted-text
role="guilabel"} to save the date.

In the `Duration`{.interpreted-text role="guilabel"} field, enter the
the amount of hours (in a [00:00]{.title-ref} format) that the
maintenance is planned to take.

In the `Priority`{.interpreted-text role="guilabel"} field, choose a
priority between one and three `⭐⭐⭐ (stars)`{.interpreted-text
role="guilabel"}. This indicates the importance of the maintenance
request.

If working in a multi-company environment, from the drop-down menu in
the `Company`{.interpreted-text role="guilabel"} field, select the
company to which this maintenance request belongs.

At the bottom of the form, there are two tabs: `Notes`{.interpreted-text
role="guilabel"} and `Instructions`{.interpreted-text role="guilabel"}.

In the `Notes`{.interpreted-text role="guilabel"} tab, type out any
internal notes for the team or technician assigned to the request, if
necessary.

In the `Instructions`{.interpreted-text role="guilabel"} tab, if
necessary, select one of the three radio button options to provide
maintenance instructions to the assigned team or technician. The
available methods for providing instructions are via
`PDF`{.interpreted-text role="guilabel"},
`Google Slide`{.interpreted-text role="guilabel"}, or
`Text`{.interpreted-text role="guilabel"}.

{.align-center}

Calendar elements
-----------------

The *Maintenance Calendar* provides various views, search functions, and
filters to help keep track of the progress of ongoing and planned
maintenance requests.

The following sections describe elements found across various views of
the calendar.

### Filters and Favorites

To access the maintenance calendar, navigate to
`Maintenance app --> Maintenance -->
Maintenance Calendar`{.interpreted-text role="menuselection"}.

To add and remove filters for sorting data on the *Maintenance
Calendar*, click the `🔻
(triangle pointed down)`{.interpreted-text role="guilabel"} icon, to the
right of the search bar at the top of the page.

The left-hand side of the resulting drop-down menu lists all the
different `Filters`{.interpreted-text role="guilabel"} users can select.
By default, `To Do`{.interpreted-text role="guilabel"} and
`Active`{.interpreted-text role="guilabel"} are selected, so all open
requests are displayed.

::: {.tip}
::: {.title}
Tip
:::

To add a custom filter to the `Maintenance Calendar`{.interpreted-text
role="guilabel"}, click `Add Custom
Filter`{.interpreted-text role="guilabel"}, under the
`Filters`{.interpreted-text role="guilabel"} section of the drop-down
menu. This opens an `Add Custom Filter`{.interpreted-text
role="guilabel"} pop-up window.

From this pop-up window, configure the properties of the new rule for
the filter. Once ready, click `Add`{.interpreted-text role="guilabel"}.
:::

The right-hand side of the drop-down menu lists the
`Favorites`{.interpreted-text role="guilabel"}, or any searches that
have been saved as a favorite to be revisited at a later date.

{.align-center}

To save a new `Favorite`{.interpreted-text role="guilabel"} search,
select the desired `Filters`{.interpreted-text role="guilabel"}. Then,
click `Save current search`{.interpreted-text role="guilabel"}. In the
field directly below `Save current search`{.interpreted-text
role="guilabel"}, assign a name to the search.

Under the assigned name, there are two options, to save the current
search either as the `Default filter`{.interpreted-text
role="guilabel"}, or as a `Shared`{.interpreted-text role="guilabel"}
filter.

Selecting `Default filter`{.interpreted-text role="guilabel"} sets this
filter as the default when opening this calendar view.

Selecting the `Shared`{.interpreted-text role="guilabel"} filter makes
this filter available to other users.

Once ready, click `Save`{.interpreted-text role="guilabel"}. When
clicked, the new `Favorite`{.interpreted-text role="guilabel"} filter
appears in the `Favorites`{.interpreted-text role="guilabel"} column,
and a `⭐ (gold star)`{.interpreted-text role="guilabel"} icon appears
with the filter\'s name in the search bar.

### Views

The `Maintenance Calendar`{.interpreted-text role="guilabel"} is
available in six different views: `Calendar`{.interpreted-text
role="guilabel"} (default), `Kanban`{.interpreted-text role="guilabel"},
`List`{.interpreted-text role="guilabel"}, `Pivot`{.interpreted-text
role="guilabel"}, `Graph`{.interpreted-text role="guilabel"}, and
`Activity`{.interpreted-text role="guilabel"}.

{.align-center}

#### Calendar view

`Calendar`{.interpreted-text role="guilabel"} is the default view
displayed when the `Maintenance Calendar`{.interpreted-text
role="guilabel"} is opened. There are a number of options in this view
type for sorting and grouping information about maintenance requests.

In the top-left corner of the page, there is a drop-down menu set to
`Week`{.interpreted-text role="guilabel"}, by default. Clicking that
drop-down menu reveals the different periods of time, in which the
calendar can be viewed: `Day`{.interpreted-text role="guilabel"},
`Month`{.interpreted-text role="guilabel"}, and `Year`{.interpreted-text
role="guilabel"}. There is also an option to
`Show weekends`{.interpreted-text role="guilabel"}, selected by default.
If unselected, weekends are not shown on the calendar.

{.align-center}

To the left of this menu, there is a `⬅️ (left arrow)`{.interpreted-text
role="guilabel"} icon and a `➡️ (right
arrow)`{.interpreted-text role="guilabel"} icon. Clicking these arrows
moves the calendar backward or forward in time, respectively.

To the right of the drop-down menu set to `Week`{.interpreted-text
role="guilabel"}, by default, is a `Today`{.interpreted-text
role="guilabel"} button. Clicking this button resets the calendar to
view today\'s date, no matter which point in time is being viewed before
clicking it.

At the far-right side of the page is a sidebar column, containing a
minimized calendar set to today\'s date, and a
`Technician`{.interpreted-text role="guilabel"} list, displaying all the
*Technicians* with requests currently open. Click the
`(panel)`{.interpreted-text role="guilabel"} icon at the top of this
sidebar to open or close the sidebar.

::: {.note}
::: {.title}
Note
:::

The `Technician`{.interpreted-text role="guilabel"} list only displays
if technicians are assigned to open requests, and individual technicians
are only listed, if they are listed as `Responsible`{.interpreted-text
role="guilabel"} on at least **one** maintenance request form.
:::

#### Kanban view

With the `Kanban`{.interpreted-text role="guilabel"} view, all open
maintenance requests are displayed in Kanban-style columns, in their
respective stages of the maintenance process.

Each maintenance request appears on its own task card, and each task
card can be dragged-and-dropped to a different stage of the Kanban
pipeline.

Each column has a name (i.e. `In Progress`{.interpreted-text
role="guilabel"}). Hovering at the top of a column reveals a
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon. Clicking the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon reveals a list of
options for that column: `Fold`{.interpreted-text role="guilabel"},
`Edit`{.interpreted-text role="guilabel"},
`Automations`{.interpreted-text role="guilabel"}, and
`Delete`{.interpreted-text role="guilabel"}.

{.align-center}

Clicking `Fold`{.interpreted-text role="guilabel"} folds the column to
hide its contents.

Clicking `Edit`{.interpreted-text role="guilabel"} opens an
`Edit: (stage name)`{.interpreted-text role="guilabel"} pop-up window,
with the corresponding stage name, wherein the column\'s details can be
edited. The following are the column options that can be edited:

{.align-center}

-   `Name`{.interpreted-text role="guilabel"}: the name of the stage in
    the Kanban pipeline.
-   `Folded in Maintenance Pipe`{.interpreted-text role="guilabel"}:
    when checked, this stage\'s column is folded by default in the
    `Kanban`{.interpreted-text role="guilabel"} view type.
-   `Request Confirmed`{.interpreted-text role="guilabel"}: when this
    box is not ticked, and the maintenance request type is set to *Work
    Center*, no leave is created for the respective work center when a
    maintenance request is created. If the box *is* ticked, the work
    center is automatically blocked for the listed duration, either at
    the specified date, or as soon as possible, if the work center is
    unavailable.
-   `Sequence`{.interpreted-text role="guilabel"}: the order in the
    maintenance process, in which this stage appears.
-   `Request Done`{.interpreted-text role="guilabel"}: if ticked, this
    box indicates this stage is the final step of the maintenance
    process. Requests moved to this stage are closed.

Once ready, click `Save & Close`{.interpreted-text role="guilabel"}. If
no changes have been made, click `Discard`{.interpreted-text
role="guilabel"}, or click the `X`{.interpreted-text role="guilabel"}
icon to close the pop-up window.

#### List view

With the `List`{.interpreted-text role="guilabel"} view selected, all
open maintenance requests are displayed in a list, with information
about each request listed in its respective row.

The columns of information displayed in this view type are the
following:

-   `Subjects`{.interpreted-text role="guilabel"}: the name assigned to
    the maintenance request.
-   `Employee`{.interpreted-text role="guilabel"}: the employee who
    originally created the maintenance request.
-   `Technician`{.interpreted-text role="guilabel"}: the technician
    responsible for the maintenance request.
-   `Category`{.interpreted-text role="guilabel"}: the category the
    equipment being repaired belongs to.
-   `Stage`{.interpreted-text role="guilabel"}: the stage of the
    maintenance process the request is currently in.
-   `Company`{.interpreted-text role="guilabel"}: if in a multi-company
    environment, the company in the database the request is assigned to.

#### Pivot view

With the `Pivot`{.interpreted-text role="guilabel"} view selected,
maintenance requests are displayed in a pivot table, and can be
customized to show different data metrics.

To add more data to the pivot table, click the
`Measures`{.interpreted-text role="guilabel"} button to reveal a
drop-down menu. By default, `Count`{.interpreted-text role="guilabel"}
is selected. Additional options to add to the table are
`Additional Leaves to Plan Ahead`{.interpreted-text role="guilabel"},
`Duration`{.interpreted-text role="guilabel"}, and
`Repeat Every`{.interpreted-text role="guilabel"}.

{.align-center}

To the right of the `Measures`{.interpreted-text role="guilabel"} button
is the `Insert in Spreadsheet`{.interpreted-text role="guilabel"}
button. Clicking this button opens a pop-up window titled
`Select a spreadsheet to insert your
pivot.`{.interpreted-text role="guilabel"}.

There are two tabs in this pop-up window:
`Spreadsheets`{.interpreted-text role="guilabel"} and
`Dashboards`{.interpreted-text role="guilabel"}. Click into one of these
tabs, and select a spreadsheet or dashboard in the database to add this
pivot table to. Once ready, click `Confirm`{.interpreted-text
role="guilabel"}. If this table shouldn\'t be added to a spreadsheet or
dashboard, click `Cancel`{.interpreted-text role="guilabel"}, or click
the `X`{.interpreted-text role="guilabel"} icon to close the pop-up
window.

To the right of the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button are three buttons:

-   `Flip axis`{.interpreted-text role="guilabel"}: the x and y axis of
    the pivot data table flip.
-   `Expand all`{.interpreted-text role="guilabel"}: all the available
    rows and columns of the pivot data table expand fully.
-   `Download xlsx`{.interpreted-text role="guilabel"}: the pivot data
    table is downloaded as an .xlsx file.

#### Graph view

With the graph view selected, the following options appear between the
search bar and visual representation of the data. These graph-specific
options are located to the right of the `Measures`{.interpreted-text
role="guilabel"} and `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} buttons.

{.align-center}

There are three different types of graphs available to users to view the
data:

-   `Bar Chart`{.interpreted-text role="guilabel"}: the data is
    displayed in a bar chart.
-   `Line Chart`{.interpreted-text role="guilabel"}: the data is
    displayed in a line chart.
-   `Pie Chart`{.interpreted-text role="guilabel"}: the data is
    displayed in a pie chart.

When viewing the data as a `Bar Chart`{.interpreted-text
role="guilabel"} graph, the data can be formatted in the following ways:

-   `Stacked`{.interpreted-text role="guilabel"}: the data is stacked on
    the graph.
-   `Descending`{.interpreted-text role="guilabel"}: the data is
    displayed in descending order.
-   `Ascending`{.interpreted-text role="guilabel"}: the data is
    displayed in ascending order.

When viewing the data as a `Line Chart`{.interpreted-text
role="guilabel"} graph, the data can be formatted in the following ways:

-   `Stacked`{.interpreted-text role="guilabel"}: the data is stacked on
    the graph.
-   `Cumulative`{.interpreted-text role="guilabel"}: the data is
    increasingly accumulated.
-   `Descending`{.interpreted-text role="guilabel"}: the data is
    displayed in descending order.
-   `Ascending`{.interpreted-text role="guilabel"}: the data is
    displayed in ascending order.

When viewing the data as a `Pie Chart`{.interpreted-text
role="guilabel"} graph, all relevant data is displayed by default, and
no additional formatting options are available.

#### Activity view

With the `Activity`{.interpreted-text role="guilabel"} view selected,
all open maintenance requests are listed in their own row, with the
ability to schedule activities related to those requests.

{.align-center}

Maintenance requests are listed in the
`Maintenance Request`{.interpreted-text role="guilabel"} column as
activities. Clicking a request opens a
`Maintenance Request`{.interpreted-text role="guilabel"} popover that
indicates the status of the request, and the responsible technician. To
schedule an activity directly from the popover, click
`➕ Schedule an activity`{.interpreted-text role="guilabel"}. This opens
a `Schedule Activity`{.interpreted-text role="guilabel"} pop-up window.

From the pop-up window, choose the `Activity Type`{.interpreted-text
role="guilabel"}, provide a `Summary`{.interpreted-text
role="guilabel"}, schedule a `Due Date`{.interpreted-text
role="guilabel"}, and choose the responsible user in the
`Assigned to`{.interpreted-text role="guilabel"} field.

{.align-center}

Type any additional notes for the new activity in the blank space under
the greyed-out `Log a note...`{.interpreted-text role="guilabel"} field.
When clicked, this changes to `Type "/" for commands`{.interpreted-text
role="guilabel"}.

Once ready, click `Schedule`{.interpreted-text role="guilabel"} to
schedule the activity. Alternatively, click
`Schedule & Mark as Done`{.interpreted-text role="guilabel"} to close
the activity, click `Done & Schedule Next`{.interpreted-text
role="guilabel"} to close the activity and open a new one, or click
`Cancel`{.interpreted-text role="guilabel"} to cancel the activity.

With the `Activity`{.interpreted-text role="guilabel"} view selected,
each activity type available when scheduling an activity is listed as
its own column. These columns are `Email`{.interpreted-text
role="guilabel"}, `Call`{.interpreted-text role="guilabel"},
`Meeting`{.interpreted-text role="guilabel"},
`Maintenance Request`{.interpreted-text role="guilabel"},
`To-Do`{.interpreted-text role="guilabel"}, `Upload
Document`{.interpreted-text role="guilabel"},
`Request Signature`{.interpreted-text role="guilabel"}, and
`Grant Approval`{.interpreted-text role="guilabel"}.

To schedule an activity with that specific activity type, click into any
blank box on the corresponding row for the desired maintenance request,
and click the `➕ (plus)`{.interpreted-text role="guilabel"} icon. This
opens an `Odoo`{.interpreted-text role="guilabel"} pop-up window,
wherein the activity can be scheduled.

{.align-center}

::: {.seealso}
\- `maintenance_requests`{.interpreted-text role="doc"} -
`add_new_equipment`{.interpreted-text role="doc"}
:::
