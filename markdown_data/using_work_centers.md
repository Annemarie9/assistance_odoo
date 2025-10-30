# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.md

Manage work orders using work centers
=====================================

Odoo Manufacturing allows for work orders to be carried out at specific
work centers. When a manufacturing order is created for a product, any
work orders listed in the `Operations`{.interpreted-text
role="guilabel"} tab of the product bill of materials (BoM) will be
automatically created as well and assigned to the specified work center.
Work orders can be managed in the `Manufacturing`{.interpreted-text
role="guilabel"} module by selecting
`Operations --> Work Orders`{.interpreted-text role="menuselection"}.

In order to use work centers, the `Work Orders`{.interpreted-text
role="guilabel"} feature must first be enabled. To do so, go to the
`Manufacturing`{.interpreted-text role="guilabel"} module, select
`Configuration --> Settings`{.interpreted-text role="menuselection"},
and activate the checkbox next to `Work Orders`{.interpreted-text
role="guilabel"}. Work centers can then be created and managed by
selecting `Configuration --> Work Centers`{.interpreted-text
role="menuselection"}.

Create a work center
--------------------

Within the `Manufacturing`{.interpreted-text role="guilabel"} module,
select `Configuration --> Work Centers
--> Create`{.interpreted-text role="menuselection"}. The work center
form can then be filled out as follows:

-   `Work Center Name`{.interpreted-text role="guilabel"}: give the work
    center a concise name that describes the type of operations it will
    be used for
-   `Alternative Workcenters`{.interpreted-text role="guilabel"}:
    specify an alternative work center for operations to be carried out
    at if the main work center is not available
-   `Code`{.interpreted-text role="guilabel"}: assign the work center a
    reference code
-   `Working Hours`{.interpreted-text role="guilabel"}: define the
    number of hours that the work center can be in use each week
-   `Company`{.interpreted-text role="guilabel"}: select the company
    that the work center belongs to

{.align-center}

### Set standards for work center productivity {#manufacturing/management/using_work_centers/wc-setup}

The `General Information`{.interpreted-text role="guilabel"} tab on the
work center form allows for productivity goals to be assigned to a work
center:

-   `Time Efficiency`{.interpreted-text role="guilabel"}: used to
    calculate the expected duration of a work order at the work center;
    for example, if a work order normally takes one hour and the
    efficiency is set to 200%, the work order will take 30 minutes
-   `Capacity`{.interpreted-text role="guilabel"}: the number of
    products that can be processed at the work center simultaneously
-   `OEE Target`{.interpreted-text role="guilabel"}: the target for
    efficiency at the work center
-   `Time before prod.`{.interpreted-text role="guilabel"}: setup time
    required before work can commence
-   `Time after prod.`{.interpreted-text role="guilabel"}: breakdown or
    cleanup time required after work is finished
-   `Cost per hour`{.interpreted-text role="guilabel"}: the cost of
    operating the work center for one hour
-   `Analytic Account`{.interpreted-text role="guilabel"}: the account
    where the cost of the work center should be recorded

{.align-center}

### Assign equipment to a work center

Using the `Equipment`{.interpreted-text role="guilabel"} tab, it is
possible for specific pieces of equipment to be assigned to a work
center. The following information will be displayed for each piece of
equipment added:

-   `Equipment Name`{.interpreted-text role="guilabel"}: the name of the
    piece of equipment
-   `Technician`{.interpreted-text role="guilabel"}: the technician
    responsible for servicing the equipment
-   `Equipment Category`{.interpreted-text role="guilabel"}: the
    category the equipment belongs to
-   `MTBF`{.interpreted-text role="guilabel"}: mean time between
    failures; the average time that the piece of equipment will operate
    before failing
-   `MTTR`{.interpreted-text role="guilabel"}: mean time to recovery;
    the average time it takes for the equipment to become fully
    operational again
-   `Est. Next Failure`{.interpreted-text role="guilabel"}: an estimate
    of when the next equipment failure will occur

{.align-center}

::: {.note}
::: {.title}
Note
:::

`MTBF`{.interpreted-text role="guilabel"}, `MTTR`{.interpreted-text
role="guilabel"}, and `Est. Next Failure`{.interpreted-text
role="guilabel"} are all calculated automatically based on past failure
data, if any exists.
:::

### Integrate IoT devices {#workcenter_iot}

The `IoT Triggers`{.interpreted-text role="guilabel"} tab enables the
integration of `IoT (Internet of Things)`{.interpreted-text role="abbr"}
devices with a work center:

-   `Device`{.interpreted-text role="guilabel"}: specifies the IoT
    device to be triggered
-   `Key`{.interpreted-text role="guilabel"}: the security key for the
    device
-   `Action`{.interpreted-text role="guilabel"}: the IoT device action
    triggered

{.align-center}

Use case: configure an alternative work center
----------------------------------------------

When a work center is at capacity, it cannot accept any new work orders.
Instead of waiting for the work center to become available, it is
possible to specify an alternative work center where surplus work orders
should be carried out.

Begin by creating a new work center. Configure the
`Equipment`{.interpreted-text role="guilabel"} tab so that it has all of
the same equipment as the main work center. This will ensure that the
same tasks can be carried out at both work centers. Navigate to the main
work center and include the new work center in the
`Alternative Workcenters`{.interpreted-text role="guilabel"} selection
field.

Now, create a new manufacturing order that uses the main work center for
one of its operations. The main work center will automatically be
selected for the operation in the `Work Orders`{.interpreted-text
role="guilabel"} tab. After confirming the manufacturing order, click
the `Plan`{.interpreted-text role="guilabel"} button that appears at the
top left of the form.

{.align-center}

If the main work center is at capacity, the work center selected for the
operation will be automatically changed to the alternative work center.

{.align-center}

Monitor work center performance
-------------------------------

Performance for an individual work center can be viewed by selecting
`Configuration --> Work Centers`{.interpreted-text
role="menuselection"}, and clicking on a work center. A variety of
metrics showing work center performance can be viewed at the top right
of the form:

-   `OEE`{.interpreted-text role="guilabel"}: overall effective
    efficiency, the percentage of time that the work center has been
    fully productive
-   `Lost`{.interpreted-text role="guilabel"}: the amount of time lost
    due to work stoppages
-   `Load`{.interpreted-text role="guilabel"}: the amount of time it
    will take to complete the current workload
-   `Performance`{.interpreted-text role="guilabel"}: the real duration
    of work time, shown as a percentage of the expected duration
