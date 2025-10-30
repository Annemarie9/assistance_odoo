# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.md

Locations
=========

A *location* is a specific space within a warehouse. This can be a
shelf, room, aisle, etc.

Configuration
-------------

To create specific storage locations, enable the *Storage Locations*
feature by going to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Warehouses`{.interpreted-text
role="guilabel"} section, tick the `Storage Locations`{.interpreted-text
role="guilabel"} checkbox. Then, click `Save`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Typically, the `Storage Locations`{.interpreted-text role="guilabel"}
feature is used with `Multi-Step Routes
<../../shipping_receiving/daily_operations/use_routes>`{.interpreted-text
role="doc"}, which controls how products move between locations.
:::

{.align-center}

Create new location
-------------------

After enabling *Storage Locations*, go to
`Inventory app --> Configuration -->
Locations`{.interpreted-text role="menuselection"}.

{.align-center}

On this page, click `New`{.interpreted-text role="guilabel"}. The new
location form can then be configured as follows:

-   `Location Name`{.interpreted-text role="guilabel"}: recognizable
    name of the location.

-   `Parent Location`{.interpreted-text role="guilabel"}: the location
    within which the new location exists. After the location is created,
    it is listed on the `Locations`{.interpreted-text role="guilabel"}
    page using a *location hierarchy*, to describe how a specific
    location fits within larger areas of the warehouse.

    ::: {.example}
    In [WH/Stock/Zone A/Refrigerator 1]{.title-ref}, \"Refrigerator 1\"
    is the location name, \"Zone A\" is the parent location, and
    everything before it is the path showing where this spot is within
    the warehouse.
    :::

### Additional Information section

In addition to the required fields above, configure the following
location fields to ensure the location serves its intended purpose in
the database:

-   `Location Type`{.interpreted-text role="guilabel"}: from the
    drop-down menu, choose `Vendor Location`{.interpreted-text
    role="guilabel"}, `View`{.interpreted-text role="guilabel"},
    `Internal Location`{.interpreted-text role="guilabel"},
    `Customer Location`{.interpreted-text role="guilabel"},
    `Inventory Loss`{.interpreted-text role="guilabel"},
    `Production`{.interpreted-text role="guilabel"}, or
    `Transit Location`{.interpreted-text role="guilabel"} to categorize
    the location. For details on each location type, refer to the
    `Location Types section
    <inventory/warehouses_storage/location-type>`{.interpreted-text
    role="ref"}.
-   `Storage Category`{.interpreted-text role="guilabel"}: only
    available with the `Storage Categories
    <../../shipping_receiving/daily_operations/storage_category>`{.interpreted-text
    role="doc"} feature enabled in
    `Inventory app --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.
-   `Company`{.interpreted-text role="guilabel"}: the company the
    location belongs to.
-   `Is a Scrap Location?`{.interpreted-text role="guilabel"}: tick this
    checkbox to allow for scrapped/damaged goods to be stored in this
    location.
-   `Is a Return Location?`{.interpreted-text role="guilabel"}: tick
    this checkbox to allow products to be returned to this location.
-   `Barcode`{.interpreted-text role="guilabel"}: used with the
    *Barcode* app, enter the barcode to `identify actions
    <barcode/setup/location>`{.interpreted-text role="ref"} at this
    location when scanned.
-   `Replenish Location`{.interpreted-text role="guilabel"}: used for
    `configuring routes
    <../../shipping_receiving/daily_operations/use_routes>`{.interpreted-text
    role="doc"}, tick this checkbox to set the location as a destination
    for receiving products from *Buy*, *Manufacture*, or other
    procurement routes, ensuring products are correctly supplied to the
    warehouse.

{.align-center}

Configure the remaining fields in the
`Additional Information`{.interpreted-text role="guilabel"} section as
follows:

-   `Company`{.interpreted-text role="guilabel"}: the company whose
    warehouse the location is inside of. Leave this field blank if this
    location is shared between companies.
-   `Is a Scrap Location?`{.interpreted-text role="guilabel"}: tick this
    checkbox to allow for scrapped/damaged goods to be stored in this
    location.
-   `Is a Return Location?`{.interpreted-text role="guilabel"}: tick
    this checkbox to allow products to be returned to this location.
-   `Barcode`{.interpreted-text role="guilabel"}: the barcode assigned
    to the location.
-   `Replenish Location`{.interpreted-text role="guilabel"}: tick this
    checkbox to get all quantities to replenish at this location.

In the `Cyclic Counting`{.interpreted-text role="guilabel"} section,
change the value in the `Inventory Frequency
(Days)`{.interpreted-text role="guilabel"} field from the default
[0]{.title-ref}, if necessary.

{.align-center}

When different than [0]{.title-ref}, the inventory count dates for
products stored at this location are automatically set at the defined
frequency.

In the `Logistics`{.interpreted-text role="guilabel"} section, in the
`Removal Strategy`{.interpreted-text role="guilabel"} field, click the
drop-down menu and select the
`removal strategy <../../shipping_receiving/removal_strategies>`{.interpreted-text
role="doc"} for how items should be removed from this location.

### Cyclic Counting section {#inventory/location-hierarchy}

To schedule regular inventory counts at this location, set the
`Inventory Frequency
(Days)`{.interpreted-text role="guilabel"} field to the desired
interval. By default, it is set to [0]{.title-ref} (no scheduled
counts).

For example, setting this field to [30]{.title-ref}, schedules a count
every thirty days. For more specifics on setting up and using this
feature, refer to the
`Cycle Counts documentation <cycle_counts>`{.interpreted-text
role="doc"}.

The `Last Effective Inventory`{.interpreted-text role="guilabel"} field
displays the date the last inventory count at this location occurred.
When scheduled inventory counts are enabled, the `Next Expected
Inventory`{.interpreted-text role="guilabel"} field displays the date of
the next inventory count.

::: {.example}
With inventory counts scheduled to occur every [30]{.title-ref} days,
and the `Last Effective
Inventory`{.interpreted-text role="guilabel"} count occurring on July
16, the `Next Expected Inventory`{.interpreted-text role="guilabel"} is
August 15.

{.align-center}
:::

### Logistics section

In the `Logistics`{.interpreted-text role="guilabel"} section of the
locations form, optionally select a `Removal
Strategy`{.interpreted-text role="guilabel"} to determine the order and
priority of how products are picked from inventory. The options are:
`First In First Out (FIFO)`{.interpreted-text role="guilabel"},
`Last In First Out (LIFO)`{.interpreted-text role="guilabel"}, `Closest
Location`{.interpreted-text role="guilabel"}, and
`First Expiry First Out (FEFO)`{.interpreted-text role="guilabel"}.

::: {.seealso}
`../../shipping_receiving/removal_strategies`{.interpreted-text
role="doc"}
:::

Current stock at location
-------------------------

To view the current stock at a single location, go to `Inventory app -->
Configuration --> Locations`{.interpreted-text role="menuselection"},
and select the desired location.

Next, click the `Current Stock`{.interpreted-text role="guilabel"} smart
button to get a list of all products at the location.

::: {.example}
A list of current stock at [Shelf 1]{.title-ref} consists of
[266]{.title-ref} cabinets and [39]{.title-ref} desks.

{.align-center}
:::
