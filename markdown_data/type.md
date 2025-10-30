# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/configure/type.md

Product type
============

Define *product types* in Odoo to track products in varying levels of
detail.

Classify products as *storable* to track stock counts, allowing users to
trigger `reordering
rules <../../warehouses_storage/replenishment/reordering_rules>`{.interpreted-text
role="doc"} for generating purchase orders. *Consumable* products are
assumed to always be in stock, and *service* products are performed and
served by the business.

::: {.seealso}
[Odoo Tutorials: Product
Type](https://www.youtube.com/watch?v=l6j0ZkP5mLM)
:::

Set product type
----------------

To set a product type, go to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select the desired product from the list.

On the product form, in the `Product Type`{.interpreted-text
role="guilabel"} field, select:

-   `Storable Product`{.interpreted-text role="guilabel"} for products
    tracked with stock counts. Only storable products can trigger
    reordering rules for generating purchase orders;

    > ::: {.tip}
    > ::: {.title}
    > Tip
    > :::
    >
    > Choose `Storable Product`{.interpreted-text role="guilabel"} if it
    > is necessary to track a product\'s stock at various locations,
    > inventory valuations, or if the product has lots and/or serial
    > numbers.
    > :::

-   `Consumable`{.interpreted-text role="guilabel"} for products that
    are always assumed to be in stock, whose quantities are not
    necessary to track or forecast (e.g. nails, toilet paper, coffee,
    etc.). Consumables are replaceable and essential, but exact counts
    are unnecessary; or

-   `Service`{.interpreted-text role="guilabel"} for sellable service
    products that are performed, and not tracked with stock counts (i.e.
    maintenance, installation, or repair services).

    {.align-center}

::: {.note}
::: {.title}
Note
:::

The product types listed above are part of the standard *Inventory* app.
For access to the fields below,
`install <general/install>`{.interpreted-text role="ref"} the
corresponding apps **in addition** to *Inventory*.
:::

-   `Booking Fees`{.interpreted-text role="guilabel"}: charge a fee for
    booking appointments through the *Appointments* app. Requires the
    installation of the *Calendar* app and *Pay to Book*
    ([appointment\_account\_payment]{.title-ref}) module
-   `Combo`{.interpreted-text role="guilabel"}: create discounted
    products sold in a bundle. Requires the installation of the *PoS*
    app.
-   `Event Ticket`{.interpreted-text role="guilabel"}: sold to attendees
    wanting to go to an event. Requires the installation of the *Events*
    app
-   `Event Booth`{.interpreted-text role="guilabel"}: sold to partners
    or sponsors to set up a booth at an event. Requires the installation
    of the *Events* app
-   `Course`{.interpreted-text role="guilabel"}: sell access to an
    educational course. Requires the installation of the *eLearning* app

Compare types
-------------

Below is a summary of how each product type affects common *Inventory*
operations, like transfers, reordering rules, and the forecasted report.
Click the chart item with an asterisk (\*) to navigate to detailed
sections.

  Product type                                                                                             Storable                                                                             Consumable                                                                         Service
  -------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  Physical product                                                                                         Yes                                                                                  Yes                                                                                No
  On-hand quantity                                                                                         `Yes* <inventory/product_management/on-hand-store>`{.interpreted-text role="ref"}    `Yes* <inventory/product_management/on-hand-con>`{.interpreted-text role="ref"}    No
  `Inventory valuation <../inventory_valuation/using_inventory_valuation>`{.interpreted-text role="doc"}   Yes                                                                                  No                                                                                 No
  Create transfer                                                                                          `Yes* <inventory/product_management/transfer-store>`{.interpreted-text role="ref"}   `Yes* <inventory/product_management/transfer-con>`{.interpreted-text role="ref"}   `No* <inventory/product_management/transfer-serv>`{.interpreted-text role="ref"}
  `Lot/serial number tracking <../product_tracking>`{.interpreted-text role="doc"}                         Yes                                                                                  No                                                                                 No
  Create purchase order                                                                                    Yes                                                                                  `Yes* <inventory/product_management/po>`{.interpreted-text role="ref"}             No
  Can be manufactured or subcontracted                                                                     `Yes* <inventory/product_management/manufacture>`{.interpreted-text role="ref"}      `Yes* <inventory/product_management/manufacture>`{.interpreted-text role="ref"}    No
  Can be in a kit                                                                                          Yes                                                                                  Yes                                                                                No
  Placed in package                                                                                        Yes                                                                                  `Yes* <inventory/product_management/package>`{.interpreted-text role="ref"}        No
  Appears on Inventory report                                                                              `Yes <inventory/product_management/report>`{.interpreted-text role="ref"}            No                                                                                 No

### On-hand quantity {#inventory/product_management/on-hand-store}

A storable product\'s on-hand and forecasted quantities, based on
incoming and outgoing orders, are reflected on the product form,
accessed by going to `Inventory app --> Products -->
Products`{.interpreted-text role="menuselection"}, and selecting the
desired product.

![Current and forecasted quantities are displayed in the **On Hand** and
**Forecasted** smart buttons on the product
form.](type/on-hand.png){.align-center}

::: {#inventory/product_management/on-hand-con}
On the other hand, consumable products are regarded as always available,
and they **cannot** be managed using reordering rules or lot/serial
numbers.
:::

### Create transfer {#inventory/product_management/transfer-store}

*Transfers* are any warehouse operation, such as receipts, internal or
batch transfers, or deliveries.

When creating a transfer for storable products in the *Inventory* app,
transfers modify the on-hand quantity at each location.

For example, transferring five units from the internal location
[WH/Stock]{.title-ref} to [WH/Packing Zone]{.title-ref} decreases the
recorded quantity at [WH/Stock]{.title-ref} and increases it at
[WH/Packing Zone]{.title-ref}.

::: {#inventory/product_management/transfer-con}
For consumable products, transfers can be created, but exact quantities
at each storage location are not tracked.
:::

::: {#inventory/product_management/transfer-serv}
Service products cannot be included in transfers, but these products can
be [linked to projects and tasks for deadline
tracking](https://www.youtube.com/watch?v=fix2LGkv13c).
:::

### Create purchase order {#inventory/product_management/po}

Both storable and consumable products can be included in a request for
quotation in the *Purchase* app.

However, when receiving consumable products, their on-hand quantity does
not change upon validating the receipt (e.g. [WH/IN]{.title-ref}).

### Manufacture or subcontract {#inventory/product_management/manufacture}

Storable and consumable products can be manufactured, subcontracted, or
included in a bill of materials (BoM).

![When the **Bill of Materials** and **Used In** smart buttons are
visible on the product form, this indicates the product can be
manufactured or used as a component of a
`BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.](type/manufacture.png){.align-center}

### Packages {#inventory/product_management/package}

Both storable and consumable products can be placed in
`packages <package>`{.interpreted-text role="doc"}.

However, for consumable products, the quantity is not tracked, and the
product is not listed in the package\'s `Contents`{.interpreted-text
role="guilabel"}, accessed by going to `Inventory app --> Products -->
Packages`{.interpreted-text role="menuselection"}, and selecting the
desired package.

![A consumable product was placed in the package, but the **Content**
section does not list it.](type/package-content.png){.align-center}

If the *Move Entire Package* feature is enabled, moving a package
updates the location of the contained storable products. However, the
location of consumable products are not updated.

### Inventory report {#inventory/product_management/report}

**Only** storable products appear on the following reports.

The *stock report* is a comprehensive list of all on-hand, unreserved,
incoming, and outgoing storable products. The report is only available
to users with `administrator access
<../../../../general/users/access_rights>`{.interpreted-text
role="doc"}, and is found by navigating to `Inventory
app --> Reporting --> Stock`{.interpreted-text role="menuselection"}.

{.align-center}

The *location report* is a breakdown of each location (internal,
external, or virtual) and the on-hand and reserved quantity of each
storable product. The report is only available with the *Storage
Location* feature activated (`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}), and to users with
`administrator access <../../../../general/users/access_rights>`{.interpreted-text
role="doc"}.

Navigate to the location report by going to
`Inventory app --> Reporting -->
Locations`{.interpreted-text role="menuselection"}.

{.align-center}
