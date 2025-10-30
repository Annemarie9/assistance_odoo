# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/storage_category.md

Storage categories
==================

A *storage category* is used with
`putaway rules <putaway>`{.interpreted-text role="doc"}, as an extra
location attribute to automatically propose optimal storage locations
for products.

Follow these steps to complete the setup:

1.  `Enable the Storage Category feature <inventory/routes/enable-storage-categories>`{.interpreted-text
    role="ref"}
2.  `Define a storage category <inventory/routes/define-storage>`{.interpreted-text
    role="ref"} with specific limitations
3.  Assign a
    `category to storage locations <inventory/routes/assign-location>`{.interpreted-text
    role="ref"}
4.  Add the storage category as an attribute to a `putaway rule
    <inventory/routes/set-putaway-attribute>`{.interpreted-text
    role="ref"}

::: {.seealso}
`putaway`{.interpreted-text role="doc"}
:::

::: {.note}
::: {.title}
Note
:::

Assigning categories to storage locations tells Odoo these locations
meet specific requirements, such as temperature or accessibility. Odoo
then evaluates these locations, based on defined capacity, and
recommends the best one on the warehouse transfer form.
:::

Configuration {#inventory/routes/enable-storage-categories}
-------------

To enable storage categories, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, in the `Warehouse`{.interpreted-text
role="guilabel"} section, ensure the
`Storage Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} features are
enabled.

Next, activate the `Storage Categories`{.interpreted-text
role="guilabel"} feature. Finally, click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

Define storage category {#inventory/routes/define-storage}
-----------------------

A storage category with specific limitations **must** be created first,
before it is applied to locations, in order to decide the optimal
storage location.

To create a storage category, go to
`Inventory app --> Configuration --> Storage
Categories`{.interpreted-text role="menuselection"}, and click
`Create`{.interpreted-text role="guilabel"}.

On the storage category form, type a name for the category in the
`Storage Category`{.interpreted-text role="guilabel"} field.

Options are available to limit capacity by weight, product, and package
type.

::: {.note}
::: {.title}
Note
:::

Weight limits can be combined with capacity by package or product (e.g.
a maximum of one hundred products with a total weight of two hundred
kilograms).

While it is possible to limit capacity by product and package type at
the same location, it may be more practical to store items in different
amounts across various locations, as shown in this example of
`capacity by package <inventory/routes/set-capacity-package>`{.interpreted-text
role="ref"}.
:::

The `Allow New Product`{.interpreted-text role="guilabel"} field defines
when the location is considered available to store a product:

-   `If location is empty`{.interpreted-text role="guilabel"}: a product
    can be added there only if the location is empty.
-   `If products are the same`{.interpreted-text role="guilabel"}: a
    product can be added there only if the same product is already
    there.
-   `Allow mixed products`{.interpreted-text role="guilabel"}: several
    different products can be stored in this location at the same time.

::: {.tip}
::: {.title}
Tip
:::

When clicked, the `Location`{.interpreted-text role="guilabel"} smart
button shows which storage locations the category has been assigned to.
:::

### Capacity by weight

On a storage category form (`Inventory app --> Configuration --> Storage
Categories`{.interpreted-text role="menuselection"}), set a maximum
product weight in the `Max Weight`{.interpreted-text role="guilabel"}
field. This limit applies to each location assigned this storage
category.

### Capacity by product

In the `Capacity by Product`{.interpreted-text role="guilabel"} tab,
click `Add a Line`{.interpreted-text role="guilabel"} to input items,
and enter their capacities in the `Quantity`{.interpreted-text
role="guilabel"} field.

::: {.example}
Ensure only a maximum of five [Large Cabinets]{.title-ref} and two
[Corner Desk Right Sit]{.title-ref} are stored at a single storage
location, by specifying those amounts in the
`Capacity by Product`{.interpreted-text role="guilabel"} tab of a
storage category form.

{.align-center}
:::

### Capacity by package {#inventory/routes/set-capacity-package}

For companies using
`packages <../../product_management/configure/package>`{.interpreted-text
role="doc"}, it becomes possible to ensure real-time storage capacity
checks, based on package types (e.g., crates, bins, boxes, etc.).

::: {.important}
::: {.title}
Important
:::

Enable the `Packages`{.interpreted-text role="guilabel"} feature in
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"} to show the
`Capacity by Package`{.interpreted-text role="guilabel"} tab.
:::

::: {.example}
Create putaway rules for pallet-stored items, by creating the [High
Frequency pallets]{.title-ref} storage category.

In the `Capacity by Package`{.interpreted-text role="guilabel"} tab,
specify the number of packages for the designated
`Package Type`{.interpreted-text role="guilabel"}, and set a maximum of
[2.00]{.title-ref} [Pallets]{.title-ref} for a specific location.

{.align-center}
:::

Assign to location {#inventory/routes/assign-location}
------------------

Once the storage category is created, assign it to a location. Navigate
to the location by going to
`Inventory app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}, and select the desired location. Then, select the
created category in the `Storage Category`{.interpreted-text
role="guilabel"} field.

::: {.example}
Assign the [High Frequency pallets]{.title-ref} storage category (which
limits pallets stored at any location to two pallets) to the
[WH/Stock/pallets/PAL 1]{.title-ref} sub-location.

{.align-center}
:::

Putaway rule {#inventory/routes/set-putaway-attribute}
------------

With the
`storage category <inventory/routes/define-storage>`{.interpreted-text
role="ref"} and `location
<inventory/routes/assign-location>`{.interpreted-text role="ref"} set
up, create the `putaway rule <putaway>`{.interpreted-text role="doc"} by
navigating to
`Inventory app --> Configuration --> Putaway Rules`{.interpreted-text
role="menuselection"}.

Click the `Create`{.interpreted-text role="guilabel"} button to create
the putaway rule. In the `Having Category`{.interpreted-text
role="guilabel"} field of the new putaway rule form, select the storage
category.

::: {.example}
Continuing the example from above, the [High Frequency
Pallets]{.title-ref} storage category is assigned to the putaway rule
directing pallets of lemonade to locations with the [High Frequency
Pallets]{.title-ref} storage category
`assigned to them <inventory/routes/assign-location>`{.interpreted-text
role="ref"}.

{.align-center}
:::

Use case: limit capacity by package
-----------------------------------

To limit the capacity of a storage location by a specific number of
packages, `create a storage
category with a Capacity By Package <inventory/routes/set-capacity-package>`{.interpreted-text
role="ref"}.

Continuing the example from above, the [High Frequency
Pallets]{.title-ref} storage category is assigned to the
[PAL1]{.title-ref} and [PAL2]{.title-ref} locations.

Then, `putaway rules <inventory/routes/putaway-rule>`{.interpreted-text
role="ref"} are set, so that any pallets received in the warehouse are
directed to be stored in [PAL1]{.title-ref} and [PAL2]{.title-ref}
locations.

Depending on the number of pallets on-hand at each of the storage
locations, when one pallet of lemonade cans is received, the following
scenarios happen:

-   If [PAL1]{.title-ref} and [PAL2]{.title-ref} are empty, the pallet
    is redirected to [WH/Stock/Pallets/PAL1]{.title-ref}.
-   If [PAL1]{.title-ref} is full, the pallet is redirected to
    [WH/Stock/Pallets/PAL2]{.title-ref}.
-   If [PAL1]{.title-ref} and [PAL2]{.title-ref} are full, the pallet is
    redirected to [WH/Stock/Pallets]{.title-ref}.
