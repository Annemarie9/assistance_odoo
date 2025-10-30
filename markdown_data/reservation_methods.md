# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods.md

show-content

:   

hide-page-toc

:   

Reservation methods
===================

Companies that sell and deliver goods to customers need to make sure
they always have stock on-hand, so when new sales orders are confirmed,
they can deliver products on time.

In Odoo, this can be handled using *reservation methods*. Reservation
methods control how products included in a delivery order (DO) should be
reserved for delivery, ensuring they are reserved at the correct times,
for the correct orders.

There are three different reservation methods in Odoo: *At
Confirmation*, *Manually*, and *Before scheduled date*.

::: {.tabs}
::: {.tab}
At Confirmation

Reserves products **only** when a sales order is confirmed, **and** if
stock is already available.
:::

::: {.tab}
Manually

Once a quote is confirmed, product availability **must** be checked
manually, and the required quantity **must** be reserved manually.
:::

::: {.tab}
Before scheduled date

A specific number of days can be selected; this is the maximum number of
days **before** a scheduled delivery date that products should be
reserved.
:::
:::

Configuration
-------------

Reservation methods are set on individual operations types. To configure
reservation methods, go to
`Inventory app --> Configuration --> Operations Types`{.interpreted-text
role="menuselection"}. Then, select the desired operation type. Or,
create a new one by clicking `New`{.interpreted-text role="guilabel"}.

In the `General`{.interpreted-text role="guilabel"} tab of the operation
type form, locate the `Reservation Method`{.interpreted-text
role="guilabel"} option, and choose which method should be used for this
type of operation.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

If the `Before scheduled date`{.interpreted-text role="guilabel"}
reservation method is selected, a new
`Reserve before scheduled date`{.interpreted-text role="guilabel"} field
appears below. From this field, the number of
`days before`{.interpreted-text role="guilabel"} and
`days before when starred`{.interpreted-text role="guilabel"} can be
changed from the default [0]{.title-ref}.

Changing the `days before`{.interpreted-text role="guilabel"} value
changes the maximum number of days before a scheduled date that products
should be reserved.

Changing the `days before when starred`{.interpreted-text
role="guilabel"} value changes the maximum number of days before a
scheduled date that starred (favorited) transfers for products should be
reserved.

{.align-center}
:::

Required applications
---------------------

The two required applications that **must** be
`installed <general/install>`{.interpreted-text role="ref"} to use
reservation methods are the *Sales* and *Inventory* apps.

::: {.note}
::: {.title}
Note
:::

In addition to delivery orders, reservation methods can also be used for
*manufacturing orders*, *resupply subcontractor* orders, orders for
*repairs*, and *internal transfers*, if desired. To enable this,
configure the additional settings:

-   **For manufacturing orders:** Install the *Manufacturing*
    application by going to the `Apps`{.interpreted-text
    role="menuselection"} application, locating the *Manufacturing* app,
    and clicking `Install`{.interpreted-text role="guilabel"}.
-   **For resupply subcontractor:** Navigate to
    `Manufacturing app --> Configuration
    --> Settings`{.interpreted-text role="menuselection"}, and under the
    `Operations`{.interpreted-text role="guilabel"} section, enable
    `Subcontracting`{.interpreted-text role="guilabel"}. Then, click
    `Save`{.interpreted-text role="guilabel"}.
-   **For repairs:** Install the *Repairs* application by going to the
    `Apps`{.interpreted-text role="menuselection"} application, locating
    the *Repairs* app, and clicking `Install`{.interpreted-text
    role="guilabel"}.
-   **For internal transfers:** Navigate to
    `Inventory app --> Configuration -->
    Settings`{.interpreted-text role="menuselection"}, and under the
    `Warehouse`{.interpreted-text role="guilabel"} section, enable
    `Storage Locations`{.interpreted-text role="guilabel"}. Then, click
    `Save`{.interpreted-text role="guilabel"}.
:::

Once these apps are installed, no additional features need to be enabled
from the settings for reservation methods to work. They will be
available by default on certain operations types, and can be viewed and
changed by navigating to `Inventory app --> Configuration -->
Operations Types`{.interpreted-text role="menuselection"}, and then
clicking on a specific operations type.

::: {.note}
::: {.title}
Note
:::

When the `Type of Operation`{.interpreted-text role="guilabel"} is
changed to `Receipt`{.interpreted-text role="guilabel"} on an
`Operations Type`{.interpreted-text role="guilabel"} form, reservation
methods are **not** available.
:::

{.align-center}

::: {.seealso}
\- `reservation_methods/at_confirmation`{.interpreted-text role="doc"} -
`reservation_methods/manually`{.interpreted-text role="doc"} -
`reservation_methods/before_scheduled_date`{.interpreted-text
role="doc"}
:::

::: {.toctree titlesonly=""}
reservation\_methods/at\_confirmation reservation\_methods/manually
reservation\_methods/before\_scheduled\_date
:::
