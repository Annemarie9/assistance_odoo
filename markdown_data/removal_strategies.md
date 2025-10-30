# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies.md

show-content

:   

hide-page-toc

:   

Removal strategies
==================

For companies with warehouses, *removal strategies* determine **which**
products are taken from the warehouse, and **when**. For example, for
perishable products, prioritizing the picking of goods with the nearest
expiration date helps minimize food spoilage.

The following columns in the table below list the removal strategies
available in Odoo, and detail how pickings are determined along with the
picking order. Leverage these removal strategies to have Odoo
automatically select how products are selected for orders:

                    `FIFO <removal_strategies/fifo>`{.interpreted-text role="doc"}                              `LIFO <removal_strategies/lifo>`{.interpreted-text role="doc"}                              `FEFO <removal_strategies/fefo>`{.interpreted-text role="doc"}                             `Closest Location <removal_strategies/closest_location>`{.interpreted-text role="doc"}                       `Least Packages <removal_strategies/least_packages>`{.interpreted-text role="doc"}
  ----------------- ------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------
  Based on          `Incoming date <inventory/warehouses_storage/arrival_date>`{.interpreted-text role="ref"}   `Incoming date <inventory/warehouses_storage/arrival_date>`{.interpreted-text role="ref"}   `Removal date <inventory/warehouses_storage/removal-date>`{.interpreted-text role="ref"}   `Location sequence <inventory/warehouses_storage/sequence>`{.interpreted-text role="ref"}                    `Package quantity <inventory/warehouses_storage/pkg-qty>`{.interpreted-text role="ref"}
  Selection order   First in                                                                                    Last in                                                                                     `First to expire <inventory/warehouses_storage/exp-date>`{.interpreted-text role="ref"}    `Alphanumeric name of location <inventory/warehouses_storage/location-name>`{.interpreted-text role="ref"}   Quantity closest to fulfilling demand

For comprehensive examples for how to use each removal strategy, refer
to each individual documentation page.

Configuration {#inventory/warehouses_storage/removal-config}
-------------

Removal strategies are set on either the product category or storage
location.

{.align-center}

Configure removal strategies on the location by going to
`Inventory --> Configuration
--> Locations`{.interpreted-text role="menuselection"}, and selecting
the desired location. On the location form, choose a removal strategy
from the `Removal Strategy`{.interpreted-text role="guilabel"} field\'s
drop-down menu options.

::: {.important}
::: {.title}
Important
:::

To set a removal strategy on a location, the
`Storage Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} settings **must**
be enabled in `Inventory -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

These features are **only** necessary when setting the removal strategy
on a location.
:::

Configure removal strategies on product categories by going to
`Inventory -->
Configuration --> Product Categories`{.interpreted-text
role="menuselection"} and selecting the intended product category. Next,
choose a removal strategy from the
`Force Removal Strategy`{.interpreted-text role="guilabel"} drop-down
menu options.

::: {.important}
::: {.title}
Important
:::

When there are different removal strategies applied on both the location
and product category for a product, the value set on the
`Force Removal Strategy`{.interpreted-text role="guilabel"} field set on
a `Product Category`{.interpreted-text role="guilabel"} form is applied
as top priority.
:::

Required features
-----------------

While some removal strategies are available by default, some additional
features **must** be enabled in
`Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"} for the removal strategy option to appear in the
drop-down menu of the `Force Removal Strategy`{.interpreted-text
role="guilabel"} or `Removal
Strategy`{.interpreted-text role="guilabel"} field.

Refer to the table below for a summary of required features. Otherwise,
refer to the dedicated sections for the removal strategy for more
details on requirements and usage.

                      FIFO                    LIFO                    FEFO                                     Closest Location                       Least Packages
  ------------------- ----------------------- ----------------------- ---------------------------------------- -------------------------------------- ----------------
  Required features   Lots & Serial Numbers   Lots & Serial Numbers   Lots & Serial Numbers, Expiration Date   Storage Locations, Multi-Step Routes   Packages

### Lots and serial numbers {#inventory/warehouses_storage/lots-setup}

Lots and serial numbers differentiate identical products and track
information like arrival or expiration dates. To enable this feature,
navigate to `Inventory --> Configuration
--> Settings`{.interpreted-text role="menuselection"}. Under the
`Traceability`{.interpreted-text role="guilabel"} heading, check the box
beside `Lots &
Serial Numbers`{.interpreted-text role="guilabel"} to enable the
feature.

{.align-center}

Next, ensure the intended product is tracked by lots or serial numbers
by navigating to the product form through
`Inventory --> Products --> Products`{.interpreted-text
role="menuselection"}, and selecting the desired product. On the product
form, switch to the `Inventory`{.interpreted-text role="guilabel"} tab,
and under the `Tracking`{.interpreted-text role="guilabel"} field,
select either the `By Unique Serial Number`{.interpreted-text
role="guilabel"} or `By
Lots`{.interpreted-text role="guilabel"} options.

After enabling the features, assign lot or serial numbers to products
using an `inventory
adjustment <../warehouses_storage/inventory_management/count_products>`{.interpreted-text
role="doc"} or during `product
reception <inventory/product_management/assign-lots>`{.interpreted-text
role="ref"}.

### Locations and routes

**Storage locations** and **multi-step routes** are necessary features
for setting **all** types of removal strategies on a location. However,
these features are specifically required for the closest location
removal strategy since it is only applied at the location level.

To activate these features, navigate to
`Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Warehouse`{.interpreted-text
role="guilabel"} heading, enable the
`Storage Location`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} features.

{.align-center}

### Expiration date {#inventory/warehouses_storage/exp-setup}

Enable the **expiration date** feature to track expiration dates, best
before dates, removal dates, and alert dates on a lot or serial number
by navigating to `Inventory -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

Under the `Traceability`{.interpreted-text role="guilabel"} heading,
ensure the `Lots & Serial Numbers`{.interpreted-text role="guilabel"}
feature is selected, and then select the check box for
`Expiration Dates`{.interpreted-text role="guilabel"} to enable the
feature.

{.align-center}

### Packages {#inventory/warehouses_storage/pack-setup}

The *packages* feature is used to group products together and is
required for the least packages removal strategy.

Navigate to `Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and select the check box for the
`Packages`{.interpreted-text role="guilabel"} feature.

{.align-center}

::: {.seealso}
\-
`Packages <../product_management/configure/package>`{.interpreted-text
role="doc"} -
`2-step delivery <daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"} -
`3-step delivery <daily_operations/delivery_three_steps>`{.interpreted-text
role="doc"}
:::

::: {.toctree titlesonly=""}
removal\_strategies/fifo removal\_strategies/lifo
removal\_strategies/fefo removal\_strategies/closest\_location
removal\_strategies/least\_packages
:::
