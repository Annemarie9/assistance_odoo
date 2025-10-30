Resellers
=========

Within Odoo\'s *CRM* app, leads can be forwarded to resellers (or
partners). Leads can be manually assigned, or automatically assigned,
based on the resellers\' designated *level* and location.

Configuration
-------------

To utilize the reseller features, the *Resellers* module first needs to
be installed. Navigate to the `Apps application`{.interpreted-text
role="menuselection"}, and remove the `Apps`{.interpreted-text
role="guilabel"} filter from the `Search...`{.interpreted-text
role="guilabel"} bar. Then, search for [Resellers]{.title-ref}.

{.align-center}

Click `Activate`{.interpreted-text role="guilabel"} on the
`Resellers`{.interpreted-text role="guilabel"} module card that appears.
Doing so installs the module, and returns to the main Odoo dashboard.

After the module is installed, navigate to the
`CRM app`{.interpreted-text role="menuselection"}. Under the
`Configuration`{.interpreted-text role="menuselection"} menu is a new
section, titled `Resellers`{.interpreted-text role="guilabel"}, with
three options beneath it: `Partner Levels`{.interpreted-text
role="guilabel"}, `Partner Activations`{.interpreted-text
role="guilabel"}, and `Commission Plans`{.interpreted-text
role="guilabel"}.

Partner levels {#crm/partner-levels}
--------------

Partner *levels* are used to differentiate between various resellers. To
view the partner levels, navigate to
`CRM app --> Configuration --> Resellers: Partner Levels`{.interpreted-text
role="menuselection"}.

On the `Partner Levels`{.interpreted-text role="guilabel"} page that
appears, there are three default levels:

-   `Gold`{.interpreted-text role="guilabel"}
-   `Silver`{.interpreted-text role="guilabel"}
-   `Bronze`{.interpreted-text role="guilabel"}

New levels can be added, as needed, by clicking `New`{.interpreted-text
role="guilabel"}, and filling out the resulting level form.

Existing levels can also be edited and renamed, if desired, as well. To
modify a level, select it from the list, and proceed to make any desired
changes from the level form page that appears.

Level weight is used to decide the probability a partner to be assigned
a lead or opportunity. On the level form, assign a numerical value
(greater than zero) to the `Level Weight`{.interpreted-text
role="guilabel"} field. If the weight is zero, no leads are assigned.

::: {.tip}
::: {.title}
Tip
:::

*Level Weight* can be assigned on an individual contact record. The
weight assigned on the individual record overwrites the default weight
assigned on the level configuration form.
:::

Partner activations {#crm/partner-activations}
-------------------

Partner *activations* are used to identify the status of a partner.
Activations are assigned on an individual contact record, and can be
used to group or filter the *Partnership Analysis* report
(`CRM app --> Reporting --> Partnerships`{.interpreted-text
role="menuselection"}).

To view the partner levels, navigate to
`CRM app --> Configuration --> Partner
Activations`{.interpreted-text role="menuselection"}.

Three activation types are created by default in the *CRM* app:

-   `Fully Operational`{.interpreted-text role="guilabel"}
-   `Ramp-up`{.interpreted-text role="guilabel"}
-   `First Contact`{.interpreted-text role="guilabel"}

New partner activations can be added, as needed, by clicking
`New`{.interpreted-text role="guilabel"}, and entering a
`Name`{.interpreted-text role="guilabel"} on the new line that appears.
Then, select the desired status in the `Active`{.interpreted-text
role="guilabel"} column.

Existing partner activations can also be edited and renamed, if desired.
To rename a status, click the `Name`{.interpreted-text role="guilabel"}
field of a desired level, and enter a new name.

To change the active status of an activation, slide the toggle in the
`Active`{.interpreted-text role="guilabel"} column of the desired
activation to the *inactive* position.

![The list of default Partner Activations in the CRM app. The toggle for
First Contact is in the inactive position, while the rest are
active.](resellers/activations-toggle.png){.align-center}

Partner assignments
-------------------

After `partner levels <crm/partner-levels>`{.interpreted-text
role="ref"} and `partner activations
<crm/partner-activations>`{.interpreted-text role="ref"} configured.

To update an individual partner record, navigate to
`CRM app --> Sales -->
Customers`{.interpreted-text role="menuselection"}, and click the Kanban
card for the desired partner to open the customer record.

On the customer record, click the `Partner Assignment`{.interpreted-text
role="guilabel"} tab.

Click the `Partner Level`{.interpreted-text role="guilabel"} field, and
select an option from the drop-down menu to assign a level. Click the
`Activation`{.interpreted-text role="guilabel"} field, and select a
partner activation type from the drop-down list, if desired. Then, click
the `Level Weight`{.interpreted-text role="guilabel"} field to assign a
different level weight, if necessary.

Publish partners
----------------

With the Odoo *Website* and *Resellers* apps installed, a new webpage
([/partners]{.title-ref}) is created to display a list of all active
partners from the *CRM* app.

Next, return to `CRM app --> Sales --> Customers`{.interpreted-text
role="menuselection"}, and click the Kanban card for a partner. From
that partner\'s contact form, click the
`Go to Website`{.interpreted-text role="guilabel"} smart button at the
top of the page to open that partner\'s webpage.

Next, click `Edit`{.interpreted-text role="guilabel"} at the top-right
of the partner\'s webpage, and use the `building
blocks <../../../websites/website/web_design/building_blocks>`{.interpreted-text
role="doc"} to add any additional design elements, or information about
the partner.

::: {.tip}
::: {.title}
Tip
:::

A company summary is a useful addition to this page.
:::

After making any necessary changes to the page, click
`Save`{.interpreted-text role="guilabel"}. At the top of the page, slide
the `Unpublished`{.interpreted-text role="guilabel"} toggle to the
active, `Published`{.interpreted-text role="guilabel"} position, if
needed.

Repeat these steps for all partners.

{.align-center}
