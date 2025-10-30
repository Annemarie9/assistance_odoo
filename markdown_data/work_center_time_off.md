# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off.md

Work center time off
====================

In Odoo, *work centers* are used to carry out manufacturing operations
at specific locations. However, if a work center cannot be used for some
reason, work orders begin to pile up at the work center until it is
operational again.

As a result, it is necessary to make the work center unavailable in Odoo
so new work orders are routed to alternative work centers that are
operational. Using Odoo\'s **Time Off** app, it is possible to designate
a work center as being unavailable for a set period of time. Doing so
ensures manufacturing operations can continue until the impacted work
center is available again.

Configuration
-------------

Before a work center can be designated as unavailable, the Odoo platform
must be properly configured. First, it is necessary to enable
`developer mode <developer-mode>`{.interpreted-text role="ref"}. This
allows the *Time Off* smart button to appear on each work center\'s
*Working Hours* page.

Next, install the **Time Off** app. This is the app used for managing
time off for all resources within Odoo, including employees and work
centers.

To do so, navigate to the `Apps`{.interpreted-text role="menuselection"}
app, then search [Time Off]{.title-ref} in the search bar. The card for
the `Time Off`{.interpreted-text role="guilabel"} app should be the only
one that appears on the page. Click the `Install`{.interpreted-text
role="guilabel"} button on the card to install the app.

The last step is to properly configure work centers. For this workflow,
it is necessary to have at least two work centers: one that is made
unavailable, and a second that receives the work orders that the other
cannot accept. If no second work center is configured, Odoo cannot route
work orders away from the unavailable work center, and they pile up in
its queue.

To create a work center, navigate to
`Manufacturing app --> Configuration --> Work
Centers --> New`{.interpreted-text role="menuselection"}.

::: {.seealso}
For a full guide to work center creation, refer to the documentation on
`work centers
<../advanced_configuration/using_work_centers>`{.interpreted-text
role="doc"}.
:::

Make sure both work centers have the same equipment listed under the
`Equipment`{.interpreted-text role="guilabel"} tab. This ensures
operations carried out at one work center can also be performed at the
other.

On the work center that is made unavailable, select the second work
center from the `Alternative Workcenters`{.interpreted-text
role="guilabel"} drop-down menu. Now, Odoo knows to send work orders to
the second work center when the first is unavailable for any reason.

{.align-center}

Add time off for a work center
------------------------------

With configuration completed, time off can now be assigned to a work
center. Begin by navigating to
`Manufacturing app --> Configuration --> Work Centers`{.interpreted-text
role="menuselection"}, and selecting the affected work center. Click the
`oi-arrow-right`{.interpreted-text role="icon"}
`(Internal link)`{.interpreted-text role="guilabel"} button on the right
side of the `Working Hours`{.interpreted-text role="guilabel"} drop-down
menu, to open the working hours page for the work center.

{.align-center}

The working hours page displays the standard working hours for the work
center. With developer mode activated, a `fa-plane`{.interpreted-text
role="icon"} `Time Off`{.interpreted-text role="guilabel"} smart button
appears at the top of the page. Click it to open the
`Resource Time Off`{.interpreted-text role="guilabel"} page.

On this page, click `New`{.interpreted-text role="guilabel"} to
configure a new time-off entry. On the time-off form, note the
`Reason`{.interpreted-text role="guilabel"} for the work center closure
(e.g. broken equipment, maintenance, etc.), select the affected work
center as the `Resource`{.interpreted-text role="guilabel"}, and choose
a `Start Date`{.interpreted-text role="guilabel"} and
`End Date`{.interpreted-text role="guilabel"} to specify the period
during which the work center is unavailable.

{.align-center}

Alternative work center planning
--------------------------------

Once a work center is within its specified time-off period, work orders
sent to it can be automatically routed to an alternative work center
using the *Plan* button.

Begin by creating a new manufacturing order (MO), by navigating to
`Manufacturing app
--> Operations --> Manufacturing Orders --> New`{.interpreted-text
role="menuselection"}. On the
`MO (manufacturing order)`{.interpreted-text role="abbr"} form, specify
a `Product`{.interpreted-text role="guilabel"} that uses the unavailable
work center for one of its operations. Click `Confirm`{.interpreted-text
role="guilabel"} to confirm the
`MO (manufacturing order)`{.interpreted-text role="abbr"}.

On the confirmed `MO (manufacturing order)`{.interpreted-text
role="abbr"}, select the `Work Orders`{.interpreted-text
role="guilabel"} tab. By default, the unavailable work center is
specified in the `Work Center`{.interpreted-text role="guilabel"}
column. There is also a `Plan`{.interpreted-text role="guilabel"} button
at the top left of the page.

Click `Plan`{.interpreted-text role="guilabel"}, and the work center
listed in the `Work Center`{.interpreted-text role="guilabel"} column of
the `Work Orders`{.interpreted-text role="guilabel"} tab is
automatically changed to the alternative work center.

![Before clicking `Plan`{.interpreted-text role="guilabel"}, the work
order is scheduled at `Main Assembly Line`{.interpreted-text
role="guilabel"}.](work_center_time_off/before-planning.png){.align-center}

![After clicking `Plan`{.interpreted-text role="guilabel"}, the work
order is rescheduled at `Alternative Assembly
Line`{.interpreted-text
role="guilabel"}.](work_center_time_off/after-planning.png){.align-center}

Once the time-off period for the unavailable work center ends, Odoo
recognizes the work center is available again. At this point, clicking
the `Plan`{.interpreted-text role="guilabel"} button does not route work
orders to an alternative work center unless the first one is at
capacity.
