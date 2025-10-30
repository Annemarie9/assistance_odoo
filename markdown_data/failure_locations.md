# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/quality/quality_management/failure_locations.md

Failure locations
=================

In Odoo, *quality control points* (QCPs) are used to create *quality
checks*, which prompt employees to confirm the quality of products, when
they are included in certain operations. By setting one or more *failure
locations* on a `QCP (Quality Control Point)`{.interpreted-text
role="abbr"}, products that fail the quality checks it creates can be
sent to one of the specified locations.

::: {.important}
::: {.title}
Important
:::

The *Failure Location* feature was added in version 17.0 of Odoo, and
does **not** appear in any previous version. To upgrade an Odoo database
to a more recent version, see the documentation on
`database upgrades <../../../../administration/upgrade>`{.interpreted-text
role="doc"}.
:::

Configuration
-------------

To use failure locations, the *Storage Locations* setting **must** be
enabled in the settings of the *Inventory* app. This setting allows for
the creation of sub-locations within a warehouse, including failure
locations.

To enable the *Storage Locations* setting, navigate to
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}, and
tick the checkbox next to `Storage Locations`{.interpreted-text
role="guilabel"}, under the `Warehouses`{.interpreted-text
role="guilabel"} heading. Then, click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Failure locations are most effective when used for products configured
as *storable products*. This is because inventory counts are only
tracked for storable products, versus *consumable* products, for which
exact counts are not tracked.

Quality checks can still be created for consumable products, and those
products can be sent to a failure location if they fail a check.
However, Odoo does not track the exact quantity of a consumable product
stored at a failure location.

To configure a product as storable, navigate to
`Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and select a product.
In the `Product Type`{.interpreted-text role="guilabel"} field on the
`General
Information`{.interpreted-text role="guilabel"} tab, make sure that
`Storable Product`{.interpreted-text role="guilabel"} is selected from
the drop-down menu.
:::

Add failure location to QCP
---------------------------

To add a failure location to a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}, navigate
to `Quality app --> Quality Control
--> Control Points`{.interpreted-text role="menuselection"}. Select an
existing `QCP (Quality Control Point)`{.interpreted-text role="abbr"}
from the list, or create a new one by clicking `New`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The following instructions only detail the configuration settings
necessary for adding a failure location to a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"}. For a full
overview of `QCP (Quality Control Points)`{.interpreted-text
role="abbr"} and all of the options available when configuring them, see
the documentation on `quality control points
<quality_control_points>`{.interpreted-text role="doc"}.
:::

In the `Control Per`{.interpreted-text role="guilabel"} field on the
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} form,
select the `Quantity`{.interpreted-text role="guilabel"} option. Doing
so causes a `Failure Locations`{.interpreted-text role="guilabel"} field
to appear on the form. This field is only available when the
`Quantity`{.interpreted-text role="guilabel"} option is selected.

In the `Failure Locations`{.interpreted-text role="guilabel"} field,
select one or more locations from the drop-down menu. To create a new
location, type the desired location name into the field, and then select
`Create "[name]"`{.interpreted-text role="guilabel"} from the drop-down
menu.

{.align-center}

Send products to failure location
---------------------------------

Once a `QCP (Quality Control Point)`{.interpreted-text role="abbr"} has
been configured with one or more failure locations, products that fail a
check created by the `QCP (Quality Control Point)`{.interpreted-text
role="abbr"} can be routed to one of the locations.

To do so, open an order that requires a quality check created by a
`QCP (Quality Control Point)`{.interpreted-text role="abbr"} configured
with a failure location. For example, navigate to
`Inventory app --> Operations --> Receipts`{.interpreted-text
role="menuselection"}, and select a receipt.

At the top of the selected order, click the
`Quality Checks`{.interpreted-text role="guilabel"} button to open a
pop-up window, from which the quality check can be processed. At the
bottom of the pop-up window, click the `Fail`{.interpreted-text
role="guilabel"} button to fail the quality check, which opens a second
pop-up window, titled
`Quality Check Failed for [Product]`{.interpreted-text role="guilabel"}.

In the `Quantity Failed`{.interpreted-text role="guilabel"} field, enter
the quantity of the product that failed to pass the quality check. In
the `Failure Location`{.interpreted-text role="guilabel"} field, select
a location to which the failed quantity should be sent. Then, click
`Confirm`{.interpreted-text role="guilabel"} at the bottom of the pop-up
window to close it.

{.align-center}

Finally, on the order, click the `Validate`{.interpreted-text
role="guilabel"} button at the top of the page. Doing so confirms the
products that failed the quality check were sent to the failure
location, while products that passed it were sent to their normal
storage locations.

View failure location inventory
-------------------------------

To view the product quantities stored in a failure location, navigate to
`Inventory
app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}. Select a failure location from the list. Then,
click the `Current Stock`{.interpreted-text role="guilabel"} smart
button on the location\'s page.

A failure location\'s page lists all of the products stored within the
location, along with the quantity of each.
