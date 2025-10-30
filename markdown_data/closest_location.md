# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/closest_location.md

Closest location removal
========================

For the *Closest Location* removal strategy, products are picked based
on the alphanumeric order of storage location titles.

The goal of this strategy is to save the warehouse worker from taking a
long journey to a farther shelf when the product is also available at a
closer location.

::: {.seealso}
`About removal strategies <../removal_strategies>`{.interpreted-text
role="doc"}
:::

::: {#inventory/warehouses_storage/sequence}
To understand *location sequence* in the closest removal strategy,
consider the following example:
:::

::: {.example}
A product is stored in the following locations: [Shelf
A/Pallet]{.title-ref}, [Shelf A/Rack 1]{.title-ref}, and [Shelf A/Rack
2]{.title-ref}.

{.align-center}

The sublocation, [Pallet]{.title-ref}, is on the ground level. Products
stored here are easier to retrieve, compared to requiring a forklift to
reach [Rack 1]{.title-ref} and [Rack 2]{.title-ref}. The storage
locations were strategically named in alphabetic order, based on ease of
access.
:::

::: {.important}
::: {.title}
Important
:::

To use this removal strategy, the `Storage Locations`{.interpreted-text
role="guilabel"} and `Multi-Step Routes`{.interpreted-text
role="guilabel"} settings **must** be enabled in
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.
:::

::: {.seealso}
`Set up removal strategy <inventory/warehouses_storage/removal-config>`{.interpreted-text
role="ref"}
:::

Location names {#inventory/warehouses_storage/location-name}
--------------

To configure location names, begin by navigating to
`Inventory app --> Configuration
--> Locations`{.interpreted-text role="menuselection"}. Then, select an
existing location, or click `New`{.interpreted-text role="guilabel"} to
create a new one, and then enter the desired name in the
`Location Name`{.interpreted-text role="guilabel"} field.

Once the locations are named in alphabetical order, based on their
proximity to the output or packing location, set the removal strategy on
the `parent location
<inventory/location-hierarchy>`{.interpreted-text role="ref"}.

To do that, in the `Locations`{.interpreted-text role="guilabel"} list,
select the parent location of the alphabetically named storage
locations.

Doing so opens the form for the parent location. In the
`Removal Strategy`{.interpreted-text role="guilabel"} field, select
`Closest Location`{.interpreted-text role="guilabel"}.

::: {.example}
In a warehouse, the storage location [WH/Stock/Shelf 1]{.title-ref} is
located closest to the packing area, where products retrieved from
shelves are packed for shipment. The popular product, [iPhone
charger]{.title-ref} is stored in three locations, [WH/Stock/Shelf
1]{.title-ref}, [WH/Stock/Shelf 2]{.title-ref}, and [WH/Stock/Shelf
3]{.title-ref}.

To use closest location, set the removal strategy on the parent
location, \'WH/Stock\'.
:::

Workflow
--------

To see how the closest location removal strategy works, consider the
following example, featuring the popular product, [iPhone
charger]{.title-ref}, which is stored in [WH/Stock/Shelf 1]{.title-ref},
[WH/Stock/Shelf 2]{.title-ref}, and [WH/Stock/Shelf 3]{.title-ref}.

Fifteen, five, and thirty units are in stock at each respective
location.

::: {.tip}
::: {.title}
Tip
:::

To check the on-hand stock at each storage location, navigate to the
product form, and click the `On Hand`{.interpreted-text role="guilabel"}
smart button.

{.align-center}
:::

Create a
`delivery order <inventory/delivery/one-step>`{.interpreted-text
role="ref"} for eighteen units of the [iPhone charger]{.title-ref} by
navigating to the `Sales app`{.interpreted-text role="menuselection"}
and creating a new quotation.

After adding the products, clicking `Confirm`{.interpreted-text
role="guilabel"} creates a delivery order that reserves items stored at
the closest location, using the removal strategy.

For more details about *where* the units were picked, select the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon, located on
the far-right. Doing so opens the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window that displays how the reserved items were
picked, according to the removal strategy.

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, the `Pick from`{.interpreted-text role="guilabel"} field
displays where the quantities to fulfill the `Demand`{.interpreted-text
role="guilabel"} are picked. All fifteen of the units stored at the
closest location, [WH/Stock/Shelf 1]{.title-ref}, are picked first. The
remaining three units are then selected from the second closest
location, [WH/Stock/Shelf 2]{.title-ref}.

{.align-center}
