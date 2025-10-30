# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/maintenance/maintenance_requests.md

Maintenance requests
====================

In order to keep equipment and work centers functioning properly, it is
often necessary to perform maintenance on them. This can include
preventive maintenance, intended to prevent equipment from breaking
down, or corrective maintenance, which is used to fix equipment that is
broken or otherwise unusable.

In Odoo *Maintenance*, users can create *maintenance requests* to
schedule and track the progress of equipment and work center
maintenance.

Create maintenance request
--------------------------

To create a new maintenance request, navigate to
`Maintenance app --> Maintenance -->
Maintenance Requests`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"}.

Begin filling out the form by entering a descriptive title in the
`Request`{.interpreted-text role="guilabel"} field (e.g., [Drill not
working]{.title-ref}).

The `Created By`{.interpreted-text role="guilabel"} field auto-populates
with the user creating the request, but a different user can be selected
by clicking on the drop-down menu.

In the `For`{.interpreted-text role="guilabel"} drop-down menu, select
`Equipment`{.interpreted-text role="guilabel"} if the maintenance
request is being created for a piece of equipment, or
`Work Center`{.interpreted-text role="guilabel"} if it is being created
for a work center.

Depending on the option selected in the `For`{.interpreted-text
role="guilabel"} field, the next field is titled either
`Equipment`{.interpreted-text role="guilabel"} or
`Work Center`{.interpreted-text role="guilabel"}. Using the drop-down
menu for either field, select a piece of equipment or a work center.

If the *Custom Maintenance Worksheets* setting is enabled in the
*Maintenance* app\'s settings, a `Worksheet Template`{.interpreted-text
role="guilabel"} field appears below the `Equipment`{.interpreted-text
role="guilabel"} or `Work
Center`{.interpreted-text role="guilabel"} field. If necessary, use this
field to select a worksheet to be filled out by the employee performing
the maintenance.

The next field is titled `Request Date`{.interpreted-text
role="guilabel"}, and is set by default to the date on which the
maintenance request is created. This date cannot be changed by the user.

In the `Maintenance Type`{.interpreted-text role="guilabel"} field,
select the `Corrective`{.interpreted-text role="guilabel"} option if the
request is intended to fix an existing issue, or the
`Preventive`{.interpreted-text role="guilabel"} option if the request is
intended to prevent issues from occurring in the future.

If the request is being created to address an issue that arose during a
specific manufacturing order (MO), select it in the
`Manufacturing Order`{.interpreted-text role="guilabel"} field.

If an `MO (Manufacturing Order)`{.interpreted-text role="abbr"} was
selected in the `Manufacturing Order`{.interpreted-text role="guilabel"}
field, a `Work Order`{.interpreted-text role="guilabel"} field appears
below it. If the issue arose during a specific work order, specify it in
this field.

In the `Team`{.interpreted-text role="guilabel"} field, select the
maintenance team that is responsible for managing the request. If a
specific team member is responsible, select them in the
`Responsible`{.interpreted-text role="guilabel"} field.

The `Scheduled Date`{.interpreted-text role="guilabel"} field is used to
specify the date on which maintenance should take place, and the time it
should begin. Choose a date by clicking on the field to open a calendar
in a pop-up window, and then select a day on the calendar. Enter an hour
and minute in the two fields below the calendar, and click
`Apply`{.interpreted-text role="guilabel"} to save the date and time.

The `Duration`{.interpreted-text role="guilabel"} field is used to
specify the time it takes to complete the maintenance request. Use the
text-entry field to enter the time in a [00:00]{.title-ref} format.

If `Work Center`{.interpreted-text role="guilabel"} was selected in the
`For`{.interpreted-text role="guilabel"} field, a
`Block Workcenter`{.interpreted-text role="guilabel"} checkbox appears
below the `Duration`{.interpreted-text role="guilabel"} field. Enable
the checkbox to prevent work orders or other maintenance from being
scheduled at the specified work center while the maintenance request is
being processed.

The `Priority`{.interpreted-text role="guilabel"} field is used to
communicate the importance (or urgency) of the maintenance request.
Assign the request a priority between zero and three
`⭐⭐⭐ (stars)`{.interpreted-text role="guilabel"}, by clicking on the
desired star number. Requests assigned a higher priority appear above
those with a lower priority, on the Kanban board used to track the
progression of maintenance requests.

In the `Notes`{.interpreted-text role="guilabel"} tab at the bottom of
the form, enter any relevant details about the maintenance request (why
the maintenance issue arose, when it occurred, etc.).

The `Instructions`{.interpreted-text role="guilabel"} tab is used to
include instructions for how maintenance should be performed. Select one
of the three options, and then include the instructions as detailed
below:

-   `PDF`{.interpreted-text role="guilabel"}: click the
    `Upload your file`{.interpreted-text role="guilabel"} button to open
    the device\'s file manager, and then select a file to upload.
-   `Google Slide`{.interpreted-text role="guilabel"}: enter a
    `Google Slide link`{.interpreted-text role="guilabel"} in the
    text-entry field that appears after the option is selected.
-   `Text`{.interpreted-text role="guilabel"}: enter the instructions in
    the text-entry field that appears after the option is selected.

{.align-center}

Process maintenance request
---------------------------

Once a maintenance request has been created, it appears in the *New
Request* stage of the *Maintenance Requests* page, which can be accessed
by navigating to `Maintenance app
--> Maintenance --> Maintenance Requests`{.interpreted-text
role="menuselection"}.

Maintenance requests can be moved to different stages by dragging and
dropping them. They can also be moved by clicking on a request to open
it in a new page, and then selecting the desired stage from the stage
indicator bar, located above the top-right corner of the request\'s
form.

Successful maintenance requests should be moved to the
`Repaired`{.interpreted-text role="guilabel"} stage, indicating that the
specified piece of equipment or work center is repaired.

Failed maintenance requests should be moved to the
`Scrap`{.interpreted-text role="guilabel"} stage, indicating the
specified piece of equipment, or work center, could not be repaired, and
must instead be scrapped.
