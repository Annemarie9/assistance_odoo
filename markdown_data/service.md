# File: /content/odoo_doc17.0/fr/content/applications/hr/fleet/service.md

Services
========

To properly maintain a fleet of vehicles, regular maintenance as well as
periodic repairs are needed. Scheduling repairs and managing services
for an entire fleet is necessary to ensure all vehicles are in good
working order when they are needed.

Create service records {#fleet/service-form}
----------------------

To log a service for a vehicle, go to the main
`Services`{.interpreted-text role="guilabel"} dashboard by navigating to
`Fleet app --> Fleet --> Services`{.interpreted-text
role="menuselection"}. Open a new service form by clicking the
`New`{.interpreted-text role="guilabel"} button in the top-left corner.

Fill out the information on the form. The only two fields that are
required to be populated are `Service Type`{.interpreted-text
role="guilabel"} and `Vehicle`{.interpreted-text role="guilabel"}.

The service form automatically saves as data is entered. However, the
form can be saved manually at any time by clicking the
`Save manually`{.interpreted-text role="guilabel"} option, represented
by a `(cloud
upload)`{.interpreted-text role="guilabel"} icon.

The fields on the form are:

-   `Description`{.interpreted-text role="guilabel"}: enter a brief
    description of the service.

-   `Service Type`{.interpreted-text role="guilabel"}: select the type
    of service performed using the drop-down menu. Or, enter a new type
    of service, and click either
    `Create "service type"`{.interpreted-text role="guilabel"} or
    `Create and
    edit...`{.interpreted-text role="guilabel"} to
    `add the service type and configure it <fleet/new-type>`{.interpreted-text
    role="ref"}.

    ::: {.important}
    ::: {.title}
    Important
    :::

    `Service Types`{.interpreted-text role="guilabel"} are **not**
    pre-configured in Odoo. When logging a service for the first time,
    the *type* of service needs to be
    `created <fleet/new-type>`{.interpreted-text role="ref"} before it
    can be selected.
    :::

-   `Date`{.interpreted-text role="guilabel"}: using the calendar
    popover window, select the date the service was provided, or is
    scheduled to be performed. Navigate to the desired month using the
    `< > (arrow)`{.interpreted-text role="guilabel"} icons, then click
    on the date to select it.

-   `Cost`{.interpreted-text role="guilabel"}: enter the cost of the
    service.

-   `Vendor`{.interpreted-text role="guilabel"}: select the vendor who
    performed the service using the drop-down menu. If the vendor has
    not already been entered in the system, type in the vendor name, and
    click either `Create`{.interpreted-text role="guilabel"} to add
    them, or `Create and edit...`{.interpreted-text role="guilabel"} to
    `add and configure the
    vendor <fleet/new-vendor>`{.interpreted-text role="ref"}.

-   `Vehicle`{.interpreted-text role="guilabel"}: select the vehicle
    that was serviced from the drop-down menu. When the vehicle is
    selected, the `Driver`{.interpreted-text role="guilabel"} field is
    populated, and the unit of measure for the
    `Odometer Value`{.interpreted-text role="guilabel"} field appears.

-   `Driver`{.interpreted-text role="guilabel"}: the current driver
    listed for the selected vehicle is populated when the
    `Vehicle`{.interpreted-text role="guilabel"} is selected. If the
    driver needs to be changed, another driver can be selected from the
    drop-down menu.

-   `Odometer Value`{.interpreted-text role="guilabel"}: enter the
    odometer reading when the service was done. The units of measure are
    either in kilometers (`km`{.interpreted-text role="guilabel"}) or
    miles (`mi`{.interpreted-text role="guilabel"}), depending on how
    the selected vehicle was configured.

    When the `Vehicle`{.interpreted-text role="guilabel"} is selected,
    the unit of measure for this field is populated. This comes from the
    vehicle form.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    To change from kilometers to miles, or vice versa, click the
    `Internal Link`{.interpreted-text role="guilabel"} button to the
    right of the vehicle selected in the `Vehicle`{.interpreted-text
    role="guilabel"} field.

    Change the unit of measure, then navigate back to the service form,
    via the breadcrumb links. The unit of measure is then updated in the
    `Odometer Value`{.interpreted-text role="guilabel"} field.
    :::

-   `Notes`{.interpreted-text role="guilabel"}: enter any notes for the
    repair at the bottom of the service form.

{.align-center}

### Create service type {#fleet/new-type}

Service types must be created from a service form. There is no other way
to access the list of service types.

On the `service form <fleet/service-form>`{.interpreted-text
role="ref"}, type in the name of the new `Service
Type`{.interpreted-text role="guilabel"} in the corresponding field.
Then, click `Create and edit...`{.interpreted-text role="guilabel"}, and
a `Create Service Type`{.interpreted-text role="guilabel"} pop-up form
appears.

The service type entered on the service form automatically populates the
`Name`{.interpreted-text role="guilabel"} field, which can be modified,
if desired.

Then, select the `Category`{.interpreted-text role="guilabel"} for the
new service type from the drop-down menu in that field. The two default
options to choose from are `Contract`{.interpreted-text role="guilabel"}
or `Service`{.interpreted-text role="guilabel"}. Additional categories
**cannot** be created.

If the service applies to **only** contracts or services, select the
corresponding `Category`{.interpreted-text role="guilabel"}. If the
service applies to **both** contracts *and* services, leave this field
blank.

When done, click `Save & Close`{.interpreted-text role="guilabel"}.

### Create vendor {#fleet/new-vendor}

When a service is done for the first time, typically, the vendor is not
in the database yet. It is best practice to add the full details for a
vendor in the database, so that any necessary information can be easily
retrieved.

On the `service form <fleet/service-form>`{.interpreted-text
role="ref"}, type in the name of the new `Vendor`{.interpreted-text
role="guilabel"} in the corresponding field. Then, click
`Create and edit...`{.interpreted-text role="guilabel"}, and a `Create
Vendor`{.interpreted-text role="guilabel"} form appears.

The vendor name entered on the service form populates the
`Name`{.interpreted-text role="guilabel"} field, by default. This field
can be modified, if desired.

::: {.note}
::: {.title}
Note
:::

Different tabs or fields may be visible on the
`Create Vendor`{.interpreted-text role="guilabel"} form, depending on
what other applications are installed.
:::

#### General information

Fill out the following information in the top-half of the form:

-   `Individual`{.interpreted-text role="guilabel"} or
    `Company`{.interpreted-text role="guilabel"}: select whether the new
    vendor being added is an individual or a company, by clicking the
    corresponding radio button.

    When a selection is made, some fields may disappear from the form.
    If any of the fields below are not visible, that is because
    `Company`{.interpreted-text role="guilabel"} was selected, instead
    of `Individual`{.interpreted-text role="guilabel"}.

-   `Name`{.interpreted-text role="guilabel"}: enter a name for the
    individual or company in this field.

-   `Company Name`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the company that the vendor is associated
    with, if any.

    If the `Company`{.interpreted-text role="guilabel"} radio button at
    the top of the form is selected, this field does not appear.

-   `Contact`{.interpreted-text role="guilabel"}: enter the contact
    information in this section.

    If desired, the `Contact`{.interpreted-text role="guilabel"} field
    can be changed to a different type of contact. Click on
    `Contact`{.interpreted-text role="guilabel"} to reveal a drop-down
    menu. The available options to select are
    `Contact`{.interpreted-text role="guilabel"},
    `Invoice Address`{.interpreted-text role="guilabel"},
    `Delivery Address`{.interpreted-text role="guilabel"},
    `Follow-up Address`{.interpreted-text role="guilabel"}, or
    `Other Address`{.interpreted-text role="guilabel"}.

    If desired, select one of these other options for the
    `Contact`{.interpreted-text role="guilabel"} field, and enter the
    corresponding information.

    If `Company`{.interpreted-text role="guilabel"} is selected for the
    `Individual`{.interpreted-text role="guilabel"} or
    `Company`{.interpreted-text role="guilabel"} field, this field is
    labeled `Address`{.interpreted-text role="guilabel"}, and **cannot**
    be modified.

-   `Tax ID`{.interpreted-text role="guilabel"}: enter the vendor\'s tax
    ID in this field.

-   `Job Position`{.interpreted-text role="guilabel"}: enter the
    vendor\'s job position in this field. If the
    `Company`{.interpreted-text role="guilabel"} radio button at the top
    of the form is selected, this field does not appear.

-   `Phone`{.interpreted-text role="guilabel"}: enter the vendor\'s
    phone number in this field.

-   `Mobile`{.interpreted-text role="guilabel"}: enter the vendor\'s
    mobile number in this field.

-   `Email`{.interpreted-text role="guilabel"}: enter the vendor\'s
    email address in this field.

-   `Website`{.interpreted-text role="guilabel"}: enter the vendor\'s
    website address in this field.

-   `Title`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the vendor\'s title in this field. The default options
    are `Doctor`{.interpreted-text role="guilabel"},
    `Madam`{.interpreted-text role="guilabel"}, `Miss`{.interpreted-text
    role="guilabel"}, `Mister`{.interpreted-text role="guilabel"}, and
    `Professor`{.interpreted-text role="guilabel"}.

    If the `Company`{.interpreted-text role="guilabel"} radio button at
    the top of the form is selected, this field does not appear.

-   `Tags`{.interpreted-text role="guilabel"}: using the drop-down menu,
    select any tags that apply to the vendor.

    To add a new tag, type in the tag, then click
    `Create "tag"`{.interpreted-text role="guilabel"}.

    There is no limit to the number of tags that can be selected.

-   `Image`{.interpreted-text role="guilabel"}: a photo of either the
    main contact person, or the company logo, can be added to the form.
    Hover over the `📷 (camera)`{.interpreted-text role="guilabel"} box,
    in the top-right of the form, to reveal a
    `✏️ (pencil)`{.interpreted-text role="guilabel"} icon, and click it.
    A file explorer window appears. Navigate to the desired file, then
    click `Open`{.interpreted-text role="guilabel"} to select it.

{.align-center}

##### Contacts & Addresses tab

After the top-half of the `Create Vendor`{.interpreted-text
role="guilabel"} form is filled out, add any other contacts and
addresses associated with the vendor in this tab.

Click the `Add`{.interpreted-text role="guilabel"} button to add a new
contact, and a `Create Contact`{.interpreted-text role="guilabel"}
pop-up window appears.

Select one of the appropriate contact type options from the radio
buttons, located at the top of the pop-up window. Those options are as
follows:

-   `Contact`{.interpreted-text role="guilabel"}: select this option to
    add general contact details for employees of the associated vendor.
-   `Invoice Address`{.interpreted-text role="guilabel"}: select this
    option to add a preferred address for all invoices. When added to
    the form, this address is selected by default when sending an
    invoice to the associated vendor.
-   `Delivery Address`{.interpreted-text role="guilabel"}: select this
    option to add a preferred address for all deliveries. When added to
    the form, this address is selected by default when delivering an
    order to the associated vendor.
-   `Follow-up Address`{.interpreted-text role="guilabel"}: select this
    option to add a preferred address for all follow-up correspondence.
    When added to the form, this address is selected by default when
    sending reminders about overdue invoices.
-   `Other Address`{.interpreted-text role="guilabel"}: select this
    option to add any other necessary addresses for the vendor.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If an option *other than* `Contact`{.interpreted-text role="guilabel"}
is selected for the contact type, an `Address`{.interpreted-text
role="guilabel"} section appears on the form. Enter the address details
in the `Address`{.interpreted-text role="guilabel"} section.
:::

Add any notes to the `Internal notes...`{.interpreted-text
role="guilabel"} section of the form.

After all of the information is added, click either
`Save & Close`{.interpreted-text role="guilabel"} to add the one new
contact, or `Save & New`{.interpreted-text role="guilabel"} to add the
current address record and create another address record.

As contacts are added to this tab, each contact appears in a separate
box, with an icon indicating what type of contact is listed.

::: {.example}
A `Delivery Address`{.interpreted-text role="guilabel"} displays a
`⛟ (truck)`{.interpreted-text role="guilabel"} icon inside that specific
address box, whereas an `Invoice Address`{.interpreted-text
role="guilabel"} displays a `💵 (dollar bill)`{.interpreted-text
role="guilabel"} icon inside.

{.align-center}
:::

##### Sales & Purchase tab

Enter the following sales and purchasing information for the various
sections below. Depending on the other installed applications,
additional fields and sections may appear. The following are all default
fields for the *Fleet* application only.

###### Sales

-   `Salesperson`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select a user as the main point of contact for sales
    with this vendor.

    This person **must** be an internal user of the company, meaning
    they can log into the database as a user.

###### Misc

-   `Company ID`{.interpreted-text role="guilabel"}: if the company has
    an ID number **other than** its *tax ID*, enter it in this field.

-   `Reference`{.interpreted-text role="guilabel"}: enter any text to
    give more information regarding the contact. This is an internal
    note to provide any additional information.

    ::: {.example}
    A company has several people with the same name, Mary Jones. The
    `Reference`{.interpreted-text role="guilabel"} field could state
    [Mary Jones at X108 - returns]{.title-ref} to provide additional
    details.
    :::

##### Internal Notes tab

Add any notes that pertain to the vendor, or any other necessary
information, in this tab.

List of services
----------------

To view all services logged in the database, including old and new
requests, navigate to
`Fleet app --> Fleet --> Services`{.interpreted-text
role="menuselection"}. All services appear in a list view, including all
the details for each service.

The service records are grouped by
`service type <fleet/new-type>`{.interpreted-text role="ref"}. The
number of repairs for each service type appears in parentheses after the
name of the service type.

Each service listed displays the following information:

-   `Date`{.interpreted-text role="guilabel"}: the date that the
    service, or repair, was performed (or requested to be performed).
-   `Description`{.interpreted-text role="guilabel"}: a short
    description of the specific type of service, or repair, performed to
    clarify the specific service.
-   `Service Type`{.interpreted-text role="guilabel"}: the type of
    service, or repair, performed. This is selected from a list of
    services that
    `must be configured <fleet/new-type>`{.interpreted-text role="ref"}.
-   `Vehicle`{.interpreted-text role="guilabel"}: the specific vehicle
    the service was performed on.
-   `Driver`{.interpreted-text role="guilabel"}: the current driver for
    the vehicle.
-   `Vendor`{.interpreted-text role="guilabel"}: the specific vendor who
    performed the service, or repair.
-   `Notes`{.interpreted-text role="guilabel"}: any information
    associated with the service, or repair, that is documented to add
    clarification.
-   `Cost`{.interpreted-text role="guilabel"}: the total cost of the
    service, or repair.
-   `Stage`{.interpreted-text role="guilabel"}: the status of the
    service, or repair. Options are `New`{.interpreted-text
    role="guilabel"}, `Running`{.interpreted-text role="guilabel"},
    `Done`{.interpreted-text role="guilabel"}, or
    `Canceled`{.interpreted-text role="guilabel"}.

At the bottom of the `Cost`{.interpreted-text role="guilabel"} column,
the total cost of all services and repairs are listed.

{.align-center}

### View services

It is recommended to view the list of services in one of several
pre-configured ways to better view the information presented. In the
top-right corner of the list, there are several icons that when clicked,
sort the data in different ways.

![The icons in the top right corner than can be clicked to present the information in
different ways.](service/views.png){.align-center}

#### List view

The default view of the service records is a list view. This presents
all the services, first grouped alphabetically by type of service, then
grouped by status.

The information can be re-sorted by any column. At the top of each
column, hover over the column name, and an arrow appears in the
far-right of that column. Click the arrow to sort the data by that
specific column.

The default sorting is in descending alphabetical order (A to Z),
represented by a `⌄
(down arrow)`{.interpreted-text role="guilabel"} icon. Click the
`⌄ (down arrow)`{.interpreted-text role="guilabel"} icon to reverse the
alphabetical order (Z to A). The `⌄ (down arrow)`{.interpreted-text
role="guilabel"} icon changes to an `^ (up arrow)`{.interpreted-text
role="guilabel"} icon.

The two exceptions to this sorting are the default
`Date`{.interpreted-text role="guilabel"} column and the
`Cost`{.interpreted-text role="guilabel"} column. The
`Date`{.interpreted-text role="guilabel"} column sorts the information
in chronological order (January to December), instead of alphabetical
order. The `Cost`{.interpreted-text role="guilabel"} column sorts the
information by repair price, from lowest to highest.

##### Add a service

To add a service record from the list view, click the
`New`{.interpreted-text role="guilabel"} button, and a service form
loads.
`Enter all the information <fleet/service-form>`{.interpreted-text
role="ref"} on the service form.

The form automatically saves as data is entered.

#### Kanban view

To view services by their stage, click the `Kanban`{.interpreted-text
role="guilabel"} button, which is the second icon in the top-right
corner, and appears as two different length bars beneath a line.

All services are organized by service type, and appear in the
corresponding Kanban column.

The number of repairs for each type of service appears in the far-right
of each Kanban column header.

The collective status of the scheduled activities for each service type
appears in the color-coded bar beneath each Kanban column title. Repairs
with activities scheduled in the future appear green, activities due
today appear yellow, overdue activities appear red, and repairs with no
activities scheduled appear gray.

Each Kanban card displays a color-coded activity-related icon, such as a
`🕘 (clock)`{.interpreted-text role="guilabel"} icon or
`📞 (phone)`{.interpreted-text role="guilabel"} icon, for example. These
icons indicate both the type of scheduled activity and the status. The
status of the activity corresponds to the colors in the status bar.
Click on an activity icon to view the details of that specific activity.

The length of the color bar is proportionate to the number of
corresponding activities with that specific status in that particular
stage. Hover over a color section to reveal the number of service
records in that specific grouping.

{.align-center}

To view **only** the records with a specific status, click the desired
color bar section. The background color for the column changes to a pale
hue of the same color (either green, yellow, red, or gray), and the
color bar appears striped instead of solid. **Only** repairs and
services with the selected status appear in the column.

{.align-center}

##### Schedule activities {#fleet/schedule-activity}

To schedule an activity for a repair or service from the Kanban view,
click the activity icon in the lower-right corner of the service record,
and click `+ Schedule an activity`{.interpreted-text role="guilabel"}. A
`Schedule Activity`{.interpreted-text role="guilabel"} pop-up window
appears.

::: {.note}
::: {.title}
Note
:::

Depending on what kind of activity, if any, is scheduled, the activity
icon may appear differently. For example, a
`📞 (phone)`{.interpreted-text role="guilabel"} appears if a phone call
is scheduled, or an `✉️ (envelope)`{.interpreted-text role="guilabel"}
appears if an email is scheduled.
:::

Enter the following information on the form:

-   `Activity Type`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the activity being scheduled. The default
    options are `Email`{.interpreted-text role="guilabel"},
    `Call`{.interpreted-text role="guilabel"},
    `Meeting`{.interpreted-text role="guilabel"},
    `To-Do`{.interpreted-text role="guilabel"}, and
    `Upload Document`{.interpreted-text role="guilabel"}.
-   `Summary`{.interpreted-text role="guilabel"}: enter a short
    description of the activity, such as [Schedule oil
    change]{.title-ref}.
-   `Due Date`{.interpreted-text role="guilabel"}: using the calendar
    popover, select the date the activity must be completed. Using the
    `< (left)`{.interpreted-text role="guilabel"} and
    `> (right)`{.interpreted-text role="guilabel"} arrow icons, navigate
    to the desired month, then click on the date to select it.
-   `Assigned to`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the user responsible for the activity.
-   `Notes`{.interpreted-text role="guilabel"}: add any notes or details
    in the blank area in the bottom-half of the form.

When the `Schedule Activity`{.interpreted-text role="guilabel"} is
completed, click `Schedule`{.interpreted-text role="guilabel"} to
schedule the activity, or click `Done & Schedule Next`{.interpreted-text
role="guilabel"} to schedule the current activity and schedule another
activity for the same repair.

::: {.seealso}
For more detailed information regarding activities, refer to the main
`activities
<../../essentials/activities>`{.interpreted-text role="doc"} document.
:::

##### Add a service

A new repair can be added from this view. Click the
`➕ (plus icon)`{.interpreted-text role="guilabel"} in the top-right
corner of the Kanban column, and a new block appears at the top of the
column, beneath the Kanban title.

Enter a `Title`{.interpreted-text role="guilabel"} for the service or
repair, then click `Add`{.interpreted-text role="guilabel"}. A
`Create`{.interpreted-text role="guilabel"} service form appears in a
pop-up window. `Enter all the information
<fleet/service-form>`{.interpreted-text role="ref"} on the service form,
then click `Save & Close`{.interpreted-text role="guilabel"} to add the
record. The new record now appears in the Kanban column.

#### Graph view

Another way to view the data is in a graph. To change to the graph view,
click the `Graph`{.interpreted-text role="guilabel"} icon, which is the
third icon in the top-right, and appears as a small graph.

The default graph view displays the service information in a stacked bar
chart, grouped by `Service Type`{.interpreted-text role="guilabel"}. The
X-axis represents the `Service Type`{.interpreted-text role="guilabel"}
and the Y-axis represents the `Cost`{.interpreted-text role="guilabel"}.

Each column visually represents the total cost for all repairs and
services for that specific `Service Type`{.interpreted-text
role="guilabel"}. Hover over any bar to reveal a popover window that
displays the total `Cost`{.interpreted-text role="guilabel"} for the
service and repairs the bar represents.

The graph can change to either a `Line Chart`{.interpreted-text
role="guilabel"} or a `Pie Chart`{.interpreted-text role="guilabel"} by
clicking the corresponding button above the graph. Additionally, the
graph can display the data in either `Stacked`{.interpreted-text
role="guilabel"}, `Descending`{.interpreted-text role="guilabel"}, or
`Ascending`{.interpreted-text role="guilabel"} order, by clicking the
corresponding buttons.

{.align-center}

#### Pivot view

Another way to view the service data is in a spreadsheet pivot table.
Click the `Pivot`{.interpreted-text role="guilabel"} icon, which is the
fourth icon in the top-right, and appears as a small spreadsheet.

The default way the data is presented shows the total cost of each type
of service. The horizontal rows represent the various types of service,
with a different service type in its own line. The vertical columns
represent the total costs for each specific type of service, further
divided by the type of service.

{.align-center}

The table can either be inserted in a spreadsheet or downloaded, if
desired.

To add the pivot table to a spreadsheet in Odoo, first, the appearance
of the pivot table must change. The default pivot table view does not
allow it to be inserted into a spreadsheet (the
`Insert in Spreadsheet`{.interpreted-text role="guilabel"} button is
grayed out).

First, click the `➖ (minus)`{.interpreted-text role="guilabel"} icon to
the left of `Total`{.interpreted-text role="guilabel"} at the top of the
pivot table. This collapses the service types, leaving only a single
`Cost`{.interpreted-text role="guilabel"} column visible.

Then, click the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button, which is no longer grayed out, and a
`Select a spreadsheet to insert your pivot`{.interpreted-text
role="guilabel"} pop-up window appears. Two tabs are visible in this
pop-up window, a `Spreadsheets`{.interpreted-text role="guilabel"} tab
and a `Dashboards`{.interpreted-text role="guilabel"} tab.

Click the desired tab to indicate where the spreadsheet should be
placed, either in a `Spreadsheet`{.interpreted-text role="guilabel"} or
on a `Dashboard`{.interpreted-text role="guilabel"}. After clicking the
desired option, click `Confirm`{.interpreted-text role="guilabel"}. The
spreadsheet then loads on the screen.

::: {.note}
::: {.title}
Note
:::

Spreadsheets are stored in Odoo\'s *Documents* application, while
dashboards are stored in Odoo\'s *Dashboards* application.
:::

Click `Services`{.interpreted-text role="guilabel"} in the top-left
corner to navigate back to the previous pivot table view.

To download the table in an *xlsx* format, click the download xlsx icon,
represented by a `⬇️ (down arrow above a line)`{.interpreted-text
role="guilabel"} icon.

::: {.seealso}
For more detailed information regarding reporting, refer to the main
`reporting
<../../essentials/reporting>`{.interpreted-text role="doc"} document.
:::

#### Activity view

To view the scheduled activities for services or repairs, click the
`🕗 (clock)`{.interpreted-text role="guilabel"} activity icon in the
top-right corner of the screen. This presents all activities, organized
by vehicle and activity type.

The vertical columns are organized by activity type, and the horizontal
lines are organized by vehicle.

The entries are color-coded according to the status of each activity.
Green activities are scheduled in the future, yellow activities are due
today, and red activities are overdue.

The user responsible for the activity appears in a photo in the
lower-left corner of each activity entry.

The due date of each activity is written in the top-center of each
activity entry.

A color-coded bar at the top of each activity column indicates the
status of the activities within that column.

The number of activities for each activity type is written on the right
side of the color-coded bar beneath the column name.

{.align-center}

##### Schedule an activity

To add a service record from the activity view, click
`+ Schedule an activity`{.interpreted-text role="guilabel"} in the
bottom-left corner of the list, and a
`Search: Services`{.interpreted-text role="guilabel"} pop-up window
loads. Click the service that the activity is being scheduled for, and a
`Schedule Activity`{.interpreted-text role="guilabel"} form loads.

`Enter all the information <fleet/schedule-activity>`{.interpreted-text
role="ref"} on the activity form.

When the form is complete, click the `Schedule`{.interpreted-text
role="guilabel"} button. Then, both pop-up windows close, and the
activity now appears on the activity view.
