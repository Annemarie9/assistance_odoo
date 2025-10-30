# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management.md

show-content

:   

hide-page-toc

:   

Inventory management
====================

In the Odoo *Inventory* app,
`warehouses <inventory_management/warehouses>`{.interpreted-text
role="doc"} handle the broader organization and distribution of stock
across different physical sites, while `locations
<inventory_management/use_locations>`{.interpreted-text role="doc"}
provide a more detailed breakdown within each warehouse for efficient
item management.

This document serves as an introduction to the terminology and concepts
necessary to master *Inventory*. For specific instructions and examples
of how things work, refer to individual documentation pages.

::: {.seealso}
[Odoo Tutorials: Warehouses &
Locations](https://www.youtube.com/watch?v=zMvudZVLuUo)
:::

Warehouses
----------

`Warehouses <inventory_management/warehouses>`{.interpreted-text
role="doc"} represent a physical place, with a physical address, where a
company\'s items are stored.

Configure
`routes <../shipping_receiving/daily_operations/use_routes>`{.interpreted-text
role="doc"} in a warehouse to control how products move to customers,
from vendors, within the warehouse, or `between
warehouses <replenishment/resupply_warehouses>`{.interpreted-text
role="doc"}.

Locations
---------

`Locations <inventory_management/use_locations>`{.interpreted-text
role="doc"} refer to specific areas within a warehouse, such as shelves,
floors, or aisles. These are sub-divisions within a warehouse, and are
unique to that warehouse. Users can create and manage numerous locations
within a single warehouse to organize inventory more precisely.

::: {.seealso}
\- `inventory_management/use_locations`{.interpreted-text role="doc"} -
`inventory_management/count_products`{.interpreted-text role="doc"} -
`inventory_management/cycle_counts`{.interpreted-text role="doc"} -
`inventory_management/scrap_inventory`{.interpreted-text role="doc"}
:::

### Location types {#inventory/warehouses_storage/location-type}

*Location types* in Odoo help categorize and manage where products are,
and what actions need to be taken with them. By default, on the
`Inventory app --> Configuration --> Locations`{.interpreted-text
role="menuselection"} page, only internal locations are displayed.

To view the seven location types in Odoo, select any location, and in
the `Location Type`{.interpreted-text role="guilabel"} field, there are:

-   `Vendor Location`{.interpreted-text role="guilabel"}: defines an
    area where products purchased from vendors originate. Items here are
    **not** in stock.

-   `View`{.interpreted-text role="guilabel"}: used to organize and
    structure the warehouse hierarchy. For example, the view location
    [WH]{.title-ref} (short for warehouse) groups all internal
    locations, such as [Stock]{.title-ref}, receiving docks, quality
    checkpoints, and packing areas to show they all belong to the same
    warehouse.

    ::: {.important}
    ::: {.title}
    Important
    :::

    View locations should **not** contain products, but it is possible
    to move them there.
    :::

-   `Internal Location`{.interpreted-text role="guilabel"}: storage
    locations within the warehouse. Items stored in these locations are
    accounted for in `inventory valuation
    <../product_management/inventory_valuation/using_inventory_valuation>`{.interpreted-text
    role="doc"}.

-   `Customer Location`{.interpreted-text role="guilabel"}: where sold
    products are tracked; items here are no longer in stock.

-   `Inventory Loss`{.interpreted-text role="guilabel"}: counterpart
    location to consume missing items or create stock, accounting for
    discrepancies.

    In Odoo, examples of inventory loss locations are *Inventory
    Adjustment*, used to account for discrepancies during an inventory
    count, and *Scrap*, which is where damaged goods are sent to account
    for inventory losses.

    > ::: {.example}
    > [Virtual Locations/Inventory Adjustment]{.title-ref} is a location
    > with the `Inventory Loss`{.interpreted-text role="guilabel"} type.
    > The database shows [65]{.title-ref} units in
    > [WH/Stock]{.title-ref}, but an inventory check reveals
    > [60]{.title-ref}. To correct the quantity, five units are moved
    > from [WH/Stock]{.title-ref} to [Virtual Locations/Inventory
    > Adjustment]{.title-ref}.
    >
    > {.align-center}
    > :::

-   `Production`{.interpreted-text role="guilabel"}: where raw materials
    are consumed, and `manufactured products
    <../../manufacturing>`{.interpreted-text role="doc"} are created.

-   `Transit Location`{.interpreted-text role="guilabel"}: used for
    inter-company or inter-warehouse operations to track products
    shipped between different addresses, such as
    `Physical Locations/Inter-warehouse
    transit <inventory/warehouses_storage/interwarehouse-transit>`{.interpreted-text
    role="ref"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

In Odoo, location types are color-coded: - **Red**: internal locations -
**Blue**: view locations - **Black**: external locations (including
inventory loss, vendor, and customer locations).
:::

### View locations in Odoo

Odoo databases include preconfigured view locations to organize the
hierarchy of locations. These provide helpful context, and distinguish
between internal and external locations.

-   *Physical locations* group internal locations---such as secondary
    warehouses and subcontractor sites. Because `inventory valuation
    <../product_management/inventory_valuation/inventory_valuation_config>`{.interpreted-text
    role="doc"} changes only when goods move from internal to external
    locations, Odoo uses physical locations to track stock that is
    off-site or in transit without affecting valuation.

::: {#inventory/warehouses_storage/interwarehouse-transit}
> ::: {.example}
> When moving products in warehouses [WH]{.title-ref} and
> [WH2]{.title-ref}, the items are not in either warehouse, but still
> belong to the company. While in transit, they are placed in the
> [Inter-warehouse transit]{.title-ref} location, a
> `Transit Location`{.interpreted-text role="guilabel"} type.
>
> This location is under the view location, [Physical
> Locations]{.title-ref}, indicating that [Inter-warehouse
> transit]{.title-ref} is outside of a warehouse, but still part of the
> company. Doing so does not affect the inventory valuation of the
> products.
> :::
:::

-   *Partner locations* group customer and vendor locations (external
    locations) together. Transfers to these locations affect inventory
    valuation.
-   *Virtual locations* are locations that do **not** exist physically,
    but it is where items that are not in inventory can be placed. These
    can be items that are no longer in inventory due to loss, or other
    factors.

::: {.toctree titlesonly=""}
inventory\_management/warehouses inventory\_management/use\_locations
inventory\_management/count\_products
inventory\_management/cycle\_counts
inventory\_management/scrap\_inventory
:::
