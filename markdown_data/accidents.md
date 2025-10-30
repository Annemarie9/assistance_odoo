# File: /content/odoo_doc17.0/fr/content/applications/hr/fleet/accidents.md

Accidents
=========

When managing a fleet, accidents are inevitable. Tracking accidents is
crucial for understanding vehicle maintenance costs and identifying safe
drivers.

Odoo\'s *Fleet* app offers multiple ways to track accidents. Below are
step-by-step instructions for only **one** method to monitor accidents
and repair costs.

Structure
---------

For this example, to track accidents, two
`service types <fleet/new-type>`{.interpreted-text role="ref"} are
created: [Accident - Driver\'s Fault]{.title-ref} and [Accident - No
Fault]{.title-ref}.

This tracks various repairs associated with accidents, organized by who
was at fault.

When an accident occurs, a service record is created. The specific
repairs needed for the accident are logged in the *Description* of the
service record, and the details about the accident are logged in the
*Notes* section.

With this organizational structure, it is possible to view all accidents
organized by fault, car, driver, or cost.

::: {.note}
::: {.title}
Note
:::

To manage accidents, the creation of service records is **required**.

Refer to the `service`{.interpreted-text role="doc"} documentation for
detailed instructions on creating service records in Odoo\'s *Fleet*
app.
:::

Log accidents and repairs
-------------------------

To log an accident, and initiate the repair process, the first step is
to `create a service
record <fleet/service-form>`{.interpreted-text role="ref"} detailing the
specific repairs needed.

::: {.note}
::: {.title}
Note
:::

Some accidents require multiple repairs with several different vendors.
For these scenarios, a separate service record is needed for each vendor
performing repairs. To keep records organized, it is recommended to keep
the *Notes* field identical, as well as attaching the same important
documentation, such as a police report.
:::

Navigate to `Fleet app --> Fleet --> Services`{.interpreted-text
role="menuselection"} to view the main `Services`{.interpreted-text
role="guilabel"} dashboard. Click `New`{.interpreted-text
role="guilabel"} in the top-left corner, and a blank service form loads.

Enter the following information on the form:

-   `Description`{.interpreted-text role="guilabel"}: enter the
    description of repairs needed to fully repair the vehicle, such as
    [Bodywork]{.title-ref}, [Windshield Replacement]{.title-ref}, or
    [Replacement Bumper, Tires, and Windows]{.title-ref}.

-   `Service Type`{.interpreted-text role="guilabel"}: for this example,
    select either [Accident - Driver\'s Fault]{.title-ref} or
    [Accident - No Fault]{.title-ref}, depending on the situation.

    When entering either of these two `Service Types`{.interpreted-text
    role="guilabel"} for the first time, type in the new service type,
    then click `Create (new service type)`{.interpreted-text
    role="guilabel"}. A `Create Service Type`{.interpreted-text
    role="guilabel"} pop-up window appears, with the new service type
    populating the `Name`{.interpreted-text role="guilabel"} field. In
    the `Category`{.interpreted-text role="guilabel"} field, select
    `Service`{.interpreted-text role="guilabel"} from the drop-down
    menu, then click the `Save & Close`{.interpreted-text
    role="guilabel"} button.

    Once an accident service type has been added to the database, it is
    available to select from the drop-down menu in the
    `Service Type`{.interpreted-text role="guilabel"} field.

-   `Date`{.interpreted-text role="guilabel"}: using the calendar
    popover window, select the date the accident occurred. Navigate to
    the desired month using the `fa-chevron-left`{.interpreted-text
    role="icon"} `fa-chevron-right`{.interpreted-text role="icon"}
    `(arrow)`{.interpreted-text role="guilabel"} icons, then click the
    date to select it.

-   `Cost`{.interpreted-text role="guilabel"}: leave this field blank,
    as the repair cost is not yet known.

-   `Vendor`{.interpreted-text role="guilabel"}: select the vendor
    performing the repairs using the drop-down menu. If the vendor has
    not already been entered in the system, type in the vendor name, and
    click either `Create`{.interpreted-text role="guilabel"} to add
    them, or `Create and edit...`{.interpreted-text role="guilabel"} to
    `add and configure the
    vendor <fleet/new-vendor>`{.interpreted-text role="ref"}.

-   `Vehicle`{.interpreted-text role="guilabel"}: select the vehicle
    that was in the accident from the drop-down menu. When the vehicle
    is selected, the `Driver`{.interpreted-text role="guilabel"} field
    is populated, and the unit of measure for the
    `Odometer Value`{.interpreted-text role="guilabel"} field appears.

-   `Driver`{.interpreted-text role="guilabel"}: the current driver
    listed for the selected vehicle populates this field when the
    `Vehicle`{.interpreted-text role="guilabel"} is selected. If a
    different driver was operating the vehicle when the accident
    occurred, select the correct driver from the drop-down menu.

-   `Odometer Value`{.interpreted-text role="guilabel"}: enter the
    odometer reading when the accident occurred. The units of measure
    are either in kilometers (`km`{.interpreted-text role="guilabel"})
    or miles (`mi`{.interpreted-text role="guilabel"}), depending on how
    the selected vehicle was configured.

-   `NOTES`{.interpreted-text role="guilabel"}: enter the specific
    details of the accident at the bottom of the service form, such as
    [Hit a deer]{.title-ref} or [Rear-ended at an intersection while
    stopped]{.title-ref}.

Odoo provides the ability to attach any important paperwork, such as
repair estimates and police reports, to the service record. To do so,
click the `fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon, located in the
*chatter* of the form, and a file explorer pop-up window appears.
Navigate to the desired record, and click `Open`{.interpreted-text
role="guilabel"} to upload the file.

> ::: {.note}
> ::: {.title}
> Note
> :::
>
> Once a file is added to a service record, a `Files`{.interpreted-text
> role="guilabel"} section appears in the *chatter*. To attach more
> records, click `fa-plus-square`{.interpreted-text role="icon"}
> `Attach files`{.interpreted-text role="guilabel"} to add more
> documents.
> :::

{.align-center}

Service stages
--------------

In Odoo\'s *Fleet* app, there are four default service stages:

::: {.tabs}
::: {.tab}
New

The default stage when a service record is created. The service has been
requested, but repairs have not begun. The `Cost`{.interpreted-text
role="guilabel"} field for this stage remains zero.
:::

::: {.tab}
Running

The repair is in-process, but not yet complete. The estimate for repairs
is listed in the `Cost`{.interpreted-text role="guilabel"} field.
:::

::: {.tab}
Completed

All repairs listed on the service form have been completed. The
`Cost`{.interpreted-text role="guilabel"} field is updated to reflect
the final total cost charged for the repairs.
:::

::: {.tab}
Cancelled

The service request has been cancelled.
:::
:::

During the repair process, change the service status to reflect the
vehicle\'s current state in one of two ways: on the individual
`service record <fleet/service_record>`{.interpreted-text role="ref"},
or in the `Kanban
service view <fleet/Kanban>`{.interpreted-text role="ref"}.

### Service record {#fleet/service_record}

Open the main *Services* dashboard, by navigating to
`Fleet app --> Fleet -->
Services`{.interpreted-text role="menuselection"}. Next, click on the
individual service record to open the detailed service form. Click the
desired stage in the top-right corner, above the service form, to change
the status.

{.align-center}

### Kanban view {#fleet/Kanban}

Open the main *Services* dashboard, by navigating to
`Fleet app --> Fleet -->
Services`{.interpreted-text role="menuselection"}. First, click the
`oi-view-kanban`{.interpreted-text role="icon"}
`Kanban`{.interpreted-text role="guilabel"} icon in the top-right of the
screen, which organizes all repairs by vehicle.

Next, remove the default `Service Type`{.interpreted-text
role="guilabel"} filter in the search bar. Upon doing so, all services
appear in a Kanban view, organized by their respective
`Status`{.interpreted-text role="guilabel"}.

Drag-and-drop the service record to the desired stage.

{.align-center}

Accident reporting
------------------

One of the main reasons to track accidents using the method outlined in
this document is the ability to view the total accident cost, determine
the safest drivers, and calculate the actual total cost for specific
vehicles.

The main
`Services dashboard <fleet/services_dashboard>`{.interpreted-text
role="ref"} displays all the various accident information, while the
`Reporting dashboard <fleet/reporting_dashboard>`{.interpreted-text
role="ref"} displays the total cost for specific vehicles.

### Services dashboard {#fleet/services_dashboard}

Navigate to `Fleet app --> Fleet --> Services`{.interpreted-text
role="menuselection"} to view the `Services`{.interpreted-text
role="guilabel"} dashboard. All service records are displayed in a
`oi-view-list`{.interpreted-text role="icon"} `(List)`{.interpreted-text
role="guilabel"} view, grouped alphabetically, by
`Service Type`{.interpreted-text role="guilabel"}.

The two service types created for accident tracking appear in the list:
`Accident -
Driver Fault`{.interpreted-text role="guilabel"} and
`Accident - No Fault`{.interpreted-text role="guilabel"}.

Each grouping displays the number of records within each type, and lists
the individual records beneath each grouping title.

::: {.example}
In this example, there are six accidents where the driver was at fault,
and four accidents that were not the driver\'s fault. This dashboard
also displays the estimated total `Cost`{.interpreted-text
role="guilabel"} for all the accidents in each group.

An estimated [\$19,164.81]{.title-ref} dollars are for driver-caused
accident repairs, and an estimated [\$2,548.21]{.title-ref} dollars are
for no-fault accidents.

{.align-center}
:::

::: {.note}
::: {.title}
Note
:::

The total `Cost`{.interpreted-text role="guilabel"} calculates **all**
costs on the repair form, including estimated costs, as well as final
repair costs. This number may not be accurate, if there are any repairs
in the *Running* stage, and the final bill has not yet been calculated.
:::

### Reporting dashboard {#fleet/reporting_dashboard}

Navigate to `Fleet app --> Reporting --> Costs`{.interpreted-text
role="menuselection"} to view the `Cost
Analysis`{.interpreted-text role="menuselection"} report. This report
displays a `fa-bar-chart`{.interpreted-text role="icon"}
`(Bar Chart)`{.interpreted-text role="guilabel"} of all
`Contract`{.interpreted-text role="guilabel"} and
`Service`{.interpreted-text role="guilabel"} costs for the current year,
organized by month (`Date : (year)`{.interpreted-text role="guilabel"}),
by default. The `Sum`{.interpreted-text role="guilabel"}, represented by
a gray dotted line, is the combined total of both the
`Contract`{.interpreted-text role="guilabel"} and
`Service`{.interpreted-text role="guilabel"} costs.

To view the total cost by vehicle, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon at the right of
the search bar, revealing a drop-down menu. Click
`Vehicle`{.interpreted-text role="guilabel"} in the
`oi-group`{.interpreted-text role="icon"} `Group By`{.interpreted-text
role="guilabel"} column, and the data is organized by vehicle.

This displays the true cost for each vehicle, including both the
contract cost (such as the monthly vehicle lease cost) and all service
costs, including all accidents. Hover over a column to reveal a data
popover window, which displays the vehicle name and the total cost. This
allows for a more complete view of the vehicle cost.

{.align-center}

To view the individual cost details for both contract costs and repairs,
click the `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} icon in the top-right
corner of the `Cost
Analysis`{.interpreted-text role="guilabel"} dashboard. This displays
each vehicle on a separate line, and displays the
`Contract`{.interpreted-text role="guilabel"} cost and
`Service`{.interpreted-text role="guilabel"} cost, as well as the
`Total`{.interpreted-text role="guilabel"} cost.

![The Cost Analysis report, displaying the contract and service costs separately, as well as
the total.](accidents/fleet-pivot.png){.align-center}

::: {.note}
::: {.title}
Note
:::

The `oi-view-pivot`{.interpreted-text role="icon"}
`(Pivot)`{.interpreted-text role="guilabel"} view organizes the data by
vehicle, by default, therefore grouping the data by
`Vehicle`{.interpreted-text role="guilabel"} is not required. If this
filer is already activated, it does not affect the presented data.
:::

Manage accident repairs
-----------------------

For companies with multiple employees, who manage a large fleet of
vehicles, displaying only service records in the `New`{.interpreted-text
role="guilabel"} and `Running`{.interpreted-text role="guilabel"} stages
can be time-saving, if there are a large number of records in the
*Services* dashboard.

Navigate to `Fleet app --> Fleet --> Services`{.interpreted-text
role="menuselection"}, where all service requests are organized by
`Service Type`{.interpreted-text role="guilabel"}. Next, click the
`fa-caret-down`{.interpreted-text role="icon"} `(down
arrow)`{.interpreted-text role="guilabel"} icon at the right of the
search bar, revealing a drop-down menu. Click `Add Custom
Filter`{.interpreted-text role="guilabel"} in the
`fa-filter`{.interpreted-text role="icon"} `Filters`{.interpreted-text
role="guilabel"} column, and a `Add Custom Filter`{.interpreted-text
role="guilabel"} pop-up window appears.

Three drop-down fields need to be configured on the pop-up window.

In the first field, scroll down, and select `Stage`{.interpreted-text
role="guilabel"}.

Leave the second field set to `=`{.interpreted-text role="guilabel"}.

Select `Running`{.interpreted-text role="guilabel"} from the drop-down
menu in the last field.

Next, click the `fa-plus`{.interpreted-text role="icon"}
`(plus)`{.interpreted-text role="guilabel"} icon to the right of the
last field, and an identical rule appears beneath the current rule.

Then, change `Running`{.interpreted-text role="guilabel"} to
`New`{.interpreted-text role="guilabel"} in the third field of the
second rule, leaving the other fields as-is.

Click the `Add`{.interpreted-text role="guilabel"} button at the bottom
to add the new custom filter.

{.align-center}

This slight modification only presents services in the
`New`{.interpreted-text role="guilabel"} and `Running`{.interpreted-text
role="guilabel"} stages. This is a helpful report for a company managing
a high number of repairs at any given time.

To have this report appear as the default report when opening the
`Services`{.interpreted-text role="guilabel"} dashboard, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} icon at the far-right
of the search bar. Next, click `Save current search`{.interpreted-text
role="guilabel"}, beneath the `fa-star`{.interpreted-text role="icon"}
`Favorites`{.interpreted-text role="guilabel"} column, which reveals
another drop-down column beneath it. Tick the checkbox beside
`Default Filter`{.interpreted-text role="guilabel"}, then click
`Save`{.interpreted-text role="guilabel"}. Then, this customized
`Services`{.interpreted-text role="guilabel"} dashboard appears, by
default, anytime the `Services`{.interpreted-text role="guilabel"}
dashboard is accessed.
