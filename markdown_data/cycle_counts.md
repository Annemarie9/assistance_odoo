# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts.md

Cycle counts
============

For most companies, warehouse stock only needs to be counted once a
year. This is why, by default, after making an *inventory adjustment* in
Odoo, the scheduled date for the next inventory count is set for the
31st of December of the current year.

However, for some businesses, it\'s crucial to have an accurate
inventory count at all times. These companies use *cycle counts* to keep
critical stock levels accurate. Cycle counting is a method by which
companies count their inventory more often in certain *locations*, to
ensure that their physical inventory counts match their inventory
records.

Configuration
-------------

In Odoo, cycle counts are performed by location. Therefore, the *Storage
Locations* feature needs to be enabled before performing a cycle count.

To enable this feature, navigate to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and scroll down to the
`Warehouse`{.interpreted-text role="guilabel"} section. Then, tick the
checkbox next to `Storage Locations`{.interpreted-text role="guilabel"},
and click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

Change inventory count frequency by location
--------------------------------------------

Once the *Storage Locations* feature is enabled, and there are multiple
locations created in the warehouse, the inventory count frequency can be
changed for specific locations.

To view and edit locations, navigate to
`Inventory app --> Configuration -->
Locations`{.interpreted-text role="menuselection"}. This reveals a
`Locations`{.interpreted-text role="guilabel"} page containing every
location currently created and listed in the warehouse.

From this page, click into a location to reveal the settings and
configuration page for that location.

Under the `Cyclic Counting`{.interpreted-text role="guilabel"} section,
locate the `Inventory Frequency (Days)`{.interpreted-text
role="guilabel"} field, which should be set to [0]{.title-ref} by
default (if this location has not been edited previously). In this
field, change the value to any number of days desired for the frequency
of counts.

{.align-center}

::: {.example}
A location that needs an inventory count every 30 days should have the
`Inventory
Frequency (Days)`{.interpreted-text role="guilabel"} value set to
[30]{.title-ref}.
:::

Now, once an inventory adjustment is applied to this location, the next
scheduled count date is automatically set, based on the value entered
into the `Inventory Frequency (Days)`{.interpreted-text role="guilabel"}
field.

Count inventory by location
---------------------------

To perform a cycle count for a specific location in the warehouse,
navigate to
`Inventory app --> Operations --> Physical Inventory`{.interpreted-text
role="menuselection"}. This reveals an
`Inventory Adjustments`{.interpreted-text role="guilabel"} page
containing all products currently in-stock, with each product listed on
its own line.

From this page, the `Filters`{.interpreted-text role="guilabel"} and
`Group By`{.interpreted-text role="guilabel"} options (accessible by
clicking the `⬇️ (down arrow)`{.interpreted-text role="guilabel"} icon,
to the right of the `Search...`{.interpreted-text role="guilabel"} bar),
can be used to select specific locations and perform inventory counts.

To select a specific location, and view all products within that
location, click the `⬇️
(down arrow)`{.interpreted-text role="guilabel"} icon, to the right of
the `Search...`{.interpreted-text role="guilabel"} bar. Then, in the
`Group By`{.interpreted-text role="guilabel"} column, click
`Add Custom Group`{.interpreted-text role="guilabel"} to reveal a new
drop-down menu.

{.align-center}

Click `Location`{.interpreted-text role="guilabel"} from the drop-down
menu. Doing so sorts products into their storage locations on the
`Inventory Adjustments`{.interpreted-text role="guilabel"} page, and a
cycle count can be performed for all products in that location.

::: {.tip}
::: {.title}
Tip
:::

In large warehouses with multiple locations and a high volume of
products, it might be easier to search for the specific location
desired. To do this, from the `Inventory Adjustments`{.interpreted-text
role="guilabel"} page, click the `⬇️ (down arrow)`{.interpreted-text
role="guilabel"} icon to the right of the `Search...`{.interpreted-text
role="guilabel"} bar.

Then, in the `Filters`{.interpreted-text role="guilabel"} column, click
`Add Custom Filter`{.interpreted-text role="guilabel"} to open an
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

In the first field, click the value and select
`Location`{.interpreted-text role="guilabel"} from the list of options.
Select `contains`{.interpreted-text role="guilabel"} in the second
field. In the third field, type in the name of the location being
searched for.

Click `Add`{.interpreted-text role="guilabel"} for that location to
appear on the page.

{.align-center}
:::

Change full inventory count frequency
-------------------------------------

While cycle counts are typically performed per location, the scheduled
date for full inventory counts of all in-stock products in the warehouse
can also be manually changed, to push the date up sooner than the date
listed.

To modify the default scheduled date, go to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Then, in the
`Operations`{.interpreted-text role="guilabel"} section, locate the
`Annual Inventory Day
and Month`{.interpreted-text role="guilabel"} setting field, which
includes a drop-down field that is set to [31]{.title-ref}
`December`{.interpreted-text role="guilabel"}, by default.

{.align-center}

To change the day, click the [31]{.title-ref}, and change it to a day
within the range [1-31]{.title-ref}, depending on the desired month of
the year.

Then, to change the month, click `December`{.interpreted-text
role="guilabel"} to reveal the drop-down menu, and select the desired
month.

Once all necessary changes have been made, click
`Save`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `count_products`{.interpreted-text role="doc"} -
`use_locations`{.interpreted-text role="doc"}
:::
