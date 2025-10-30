# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/maintenance/maintenance_setup.md

Maintenance setup
=================

Odoo *Maintenance* helps companies schedule corrective and preventive
maintenance on equipment used in their warehouse. This helps companies
avoid equipment breakdowns, blocks in warehouse work centers, and
emergency repair costs.

Maintenance teams
-----------------

When creating maintenance requests, a *maintenance team* can be assigned
to the request as the team responsible for handling the request.

To view existing maintenance teams, navigate to
`Maintenance app --> Configuration
--> Maintenance Teams`{.interpreted-text role="menuselection"}.

From the resulting `Teams`{.interpreted-text role="guilabel"} page, a
list of all existing teams (if any) is displayed, with the
`Team Name`{.interpreted-text role="guilabel"},
`Team Members`{.interpreted-text role="guilabel"}, and
`Company`{.interpreted-text role="guilabel"} listed in the columns, by
default.

{.align-center}

To add a new team, click `New`{.interpreted-text role="guilabel"}. This
adds a blank line at the bottom of the list of teams. In the blank field
that appears below the `Team Name`{.interpreted-text role="guilabel"}
column, assign a name to the new maintenance team.

In the `Team Members`{.interpreted-text role="guilabel"} column, click
the field to reveal a drop-down menu with existing users in the
database. Choose which users should be members of the new maintenance
team.

Click `Search More...`{.interpreted-text role="guilabel"} to open a
`Search: Team Members`{.interpreted-text role="guilabel"} pop-up window
to search for users **not** shown on the initial drop-down menu.

{.align-center}

In the `Company`{.interpreted-text role="guilabel"} column, if in a
multi-company environment, click the drop-down menu to select the
company in the database to which this new maintenance team belongs.

Once ready, click `Save`{.interpreted-text role="guilabel"} to save
changes.

::: {.tip}
::: {.title}
Tip
:::

The team members assigned to maintenance teams are also referred to as
*Technicians*, when viewing the *Maintenance Calendar*.

Navigate to
`Maintenance app --> Maintenance --> Maintenance Calendar`{.interpreted-text
role="menuselection"}, and click on an existing maintenance request.
From the resulting popover, locate the `Technician`{.interpreted-text
role="guilabel"} field. The name listed in the field is the team member,
and is the user responsible for that particular request.

{.align-center}

At the far-right side of the page is a sidebar column, containing a
minimized calendar set to today\'s date, and a
`Technician`{.interpreted-text role="guilabel"} list, displaying all the
technicians (or team members) with requests currently open.
:::

Equipment
---------

In Odoo *Maintenance*, *equipment* refers to machines and tools used
internally in warehouse work centers. Equipment can include technology
such as computers or tablets, power tools, machines used for
manufacturing, and more.

### Equipment categories

Each piece of equipment belongs to an *equipment category*. Before
adding new equipment, make sure that a fitting equipment category is
created.

To create a new equipment category, navigate to
`Maintenance app --> Configuration
--> Equipment Categories`{.interpreted-text role="menuselection"}, and
click `New`{.interpreted-text role="guilabel"}. Doing so opens a blank
equipment category form.

{.align-center}

On the blank form, assign a name in the
`Category Name`{.interpreted-text role="guilabel"} field.

In the `Responsible`{.interpreted-text role="guilabel"} field, assign a
user to be responsible for the equipment in this category, if necessary.
By default, the user who creates the category is selected as
`Responsible`{.interpreted-text role="guilabel"}, by default.

If in a multi-company environment, click the drop-down menu in the
`Company`{.interpreted-text role="guilabel"} field, and select the
company in the database to whom the equipment in this category belongs.

In the `Email Alias`{.interpreted-text role="guilabel"} field, assign an
email alias to this category, if necessary.

In the `Comments`{.interpreted-text role="guilabel"} field, type any
comments or notes for internal users to reference in relation to this
category, if necessary.

::: {.note}
::: {.title}
Note
:::

Once a new equipment category is created, all equipment belonging to
that category, as well as any past or currently open maintenance
requests, are available from the equipment category form.

Navigate to
`Maintenance app --> Configuration --> Equipment Categories`{.interpreted-text
role="menuselection"}, and select a category to view. Locate the
`Equipment`{.interpreted-text role="guilabel"} and
`Maintenance`{.interpreted-text role="guilabel"} smart buttons at the
top of the form.

{.align-center}

Click the `Equipment`{.interpreted-text role="guilabel"} smart button to
view all equipment belonging to this category. Click the
`Maintenance`{.interpreted-text role="guilabel"} smart button to view
any past, or currently open, maintenance requests.
:::

### Machines & tools

To add new equipment, navigate to
`Maintenance app --> Equipment --> Machines &
Tools`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}. This opens a blank equipment
form.

In the `Name`{.interpreted-text role="guilabel"} field, assign a name
for the new equipment. In the `Equipment
Category`{.interpreted-text role="guilabel"} field, click the drop-down
menu and select which category this new equipment should belong to.

If in a multi-company environment, click the drop-down menu in the
`Company`{.interpreted-text role="guilabel"} field, and select the
company in the database to whom the new equipment belongs.

In the `Used By`{.interpreted-text role="guilabel"} field, select from
one of three radio button options: `Department`{.interpreted-text
role="guilabel"}, `Employee`{.interpreted-text role="guilabel"}, or
`Other`{.interpreted-text role="guilabel"}.

{.align-center}

If `Department`{.interpreted-text role="guilabel"} is selected, a
`Department`{.interpreted-text role="guilabel"} field appears below the
`Used By`{.interpreted-text role="guilabel"} field. Click the drop-down
menu and select the department that uses this equipment.

If `Employee`{.interpreted-text role="guilabel"} is selected, an
`Employee`{.interpreted-text role="guilabel"} field appears below the
`Used
By`{.interpreted-text role="guilabel"} field. Click the drop-down menu,
and select the employee who uses this equipment.

If the `Other`{.interpreted-text role="guilabel"} option is selected,
both the `Department`{.interpreted-text role="guilabel"} and
`Employee`{.interpreted-text role="guilabel"} fields appear below the
`Used By`{.interpreted-text role="guilabel"} field. Click the drop-down
menus for the respective fields, and choose which department and
employee uses this equipment.

In the `Maintenance Team`{.interpreted-text role="guilabel"} field,
select the team responsible for this equipment. In the
`Technician`{.interpreted-text role="guilabel"} field, select the team
member/user responsible for this equipment.

{.align-center}

In the `Used in location`{.interpreted-text role="guilabel"} field,
enter the location wherein this equipment will be used, if not in an
internal work center (e.g. in an office).

In the `Work Center`{.interpreted-text role="guilabel"} field, click the
drop-down menu, and select which work center this equipment will be used
in.

In the blank space under the `Description`{.interpreted-text
role="guilabel"} tab at the bottom of the form, add any relevant
information describing the equipment for users to reference.

#### Product Information tab

To add any relevant information while creating a new piece of equipment,
from the equipment form, click the
`Product Information`{.interpreted-text role="guilabel"} tab.

{.align-center}

In the `Vendor`{.interpreted-text role="guilabel"} field, add the vendor
from which the equipment was purchased. In the
`Vendor Reference`{.interpreted-text role="guilabel"} field, add the
product reference number obtained from the vendor, if applicable.

In the `Model`{.interpreted-text role="guilabel"} field, specify which
model this equipment is, if applicable. If the equipment is serialized,
add a serial number in the `Serial Number`{.interpreted-text
role="guilabel"} field.

In the `Effective Date`{.interpreted-text role="guilabel"} field, click
the date to reveal a calendar popover, and select a date. This date
indicates when this equipment was first put in use, and will be used to
compute the Mean Time Between Failure (MTBF) in the equipment\'s
`Maintenance`{.interpreted-text role="guilabel"} tab.

In the `Cost`{.interpreted-text role="guilabel"} field, specify how much
the equipment cost to acquire, if applicable.

If the equipment is covered under a warranty, specify the
`Warranty Expiration Date`{.interpreted-text role="guilabel"} by
selecting a date from the calendar popover in that field.

#### Maintenance tab

Various maintenance metrics are available for each piece of equipment,
and are automatically computed, based on corrective maintenance, and
planned preventive maintenance.

To view the maintenance metrics for a specific piece of equipment, from
the equipment form, click the `Maintenance`{.interpreted-text
role="guilabel"} tab.

{.align-center}

Doing so reveals the following fields:

-   `Expected Mean Time Between Failure`{.interpreted-text
    role="guilabel"}: the amount of time (in days) before the next
    failure is expected. This is the **only** field not greyed-out, and
    the **only** field users can edit.
-   `Mean Time Between Failure`{.interpreted-text role="guilabel"}: the
    amount of time (in days) between reported failures. This value is
    computed based on completed corrective maintenances.
-   `Estimated Next Failure`{.interpreted-text role="guilabel"}: the
    date on which the next failure is expected. This date is computed as
    the Latest Failure Date +
    `MTBF (Mean Time Between Failure)`{.interpreted-text role="abbr"}.
-   `Latest Failure`{.interpreted-text role="guilabel"}: The date of the
    latest failure. The value in this field updates once a failure is
    reported for this equipment.
-   `Mean Time To Repair`{.interpreted-text role="guilabel"}: the amount
    of time (in days) it takes to repair this equipment upon failure.
    This value updates once a maintenance request is completed for this
    equipment.

Work centers
------------

To view the work centers where equipment is being used, and how the
equipment is being used in them, navigate to
`Maintenance app --> Equipment --> Work Centers`{.interpreted-text
role="menuselection"}, and click into a work center.

From the resulting work center form, click the
`Equipment`{.interpreted-text role="guilabel"} tab to view all machines
and tools being used in that specific work center.

Each piece of equipment is listed with certain relevant information: the
`Equipment Name`{.interpreted-text role="guilabel"}, the responsible
`Technician`{.interpreted-text role="guilabel"}, the
`Equipment Category`{.interpreted-text role="guilabel"} it belongs to,
and a few important maintenance metrics: its
`MTBF (Mean Time Between Failure)`{.interpreted-text role="abbr"},
`MTTR (Mean Time To Repair)`{.interpreted-text role="abbr"}, and
`Est. Next Failure`{.interpreted-text role="guilabel"} date.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To add new equipment to a work center directly from the work center
form, click `Add a
line`{.interpreted-text role="guilabel"} under the
`Equipment`{.interpreted-text role="guilabel"} tab. This opens an
`Add: Maintenance Equipment`{.interpreted-text role="guilabel"} pop-up
window.

From the pop-up window, select the equipment that should be added to the
work center, and click `Select`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
`add_new_equipment`{.interpreted-text role="doc"}
:::
