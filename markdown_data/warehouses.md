# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses.md

Warehouses
==========

In the Odoo *Inventory* app, a *warehouse* is a physical space with an
address for storing items, such as a storage facility, distribution
center, or physical store.

Each database has a pre-configured warehouse with the company\'s
address. Users can set up multiple warehouses, and
`create stock moves <../../shipping_receiving/daily_operations/use_routes>`{.interpreted-text
role="doc"} between them.

Configuration
-------------

To create or manage warehouses, go to
`Inventory app --> Configuration -->
Warehouses`{.interpreted-text role="menuselection"}.

Then, select an existing warehouse, or create a new one by clicking
`New`{.interpreted-text role="guilabel"}. Doing so opens the warehouse
form, which contains the following fields:

-   `Warehouse`{.interpreted-text role="guilabel"} (*required field*):
    the full name of the warehouse.

-   `Short Name`{.interpreted-text role="guilabel"} (*required field*):
    the abbreviated code for the warehouse (maximum five characters).
    The short name for the default warehouse in Odoo is
    [WH]{.title-ref}.

    ::: {.important}
    ::: {.title}
    Important
    :::

    The `Short Name`{.interpreted-text role="guilabel"} appears on
    warehouse documents, so it is recommended to use an memorable one,
    like \"WH\[first letters of location\]\" (e.g. [WHA]{.title-ref},
    [WHB]{.title-ref}, etc.).
    :::

-   `Address`{.interpreted-text role="guilabel"} (*required field*): the
    address of the warehouse. To change the warehouse address when
    creating two or more warehouses, hover over the field, and click the
    `fa-arrow-right`{.interpreted-text role="icon"}
    `(right arrow)`{.interpreted-text role="guilabel"}.

-   `Company`{.interpreted-text role="guilabel"} (*required field*): the
    company that owns the warehouse; this can be set as the company that
    owns the Odoo database, or the company of a customer or vendor.

-   `Intrastat region`{.interpreted-text role="guilabel"}: `region name
    <../../../../finance/accounting/reporting/intrastat>`{.interpreted-text
    role="doc"} required for companies in the European Union.

::: {.important}
::: {.title}
Important
:::

The options below are available **only** when the *Multi-Step Routes*
feature is enabled in
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.
:::

-   `Incoming Shipments`{.interpreted-text role="guilabel"}: select the
    option to receive products from the warehouse in
    `one <../../shipping_receiving/daily_operations/receipts_delivery_one_step>`{.interpreted-text
    role="doc"}, `two
    <../../shipping_receiving/daily_operations/receipts_delivery_two_steps>`{.interpreted-text
    role="doc"}, or `three
    <../../shipping_receiving/daily_operations/receipts_three_steps>`{.interpreted-text
    role="doc"} steps.
-   `Outgoing Shipments`{.interpreted-text role="guilabel"}: select the
    option to deliver products from the warehouse in
    `one <../../shipping_receiving/daily_operations/receipts_delivery_one_step>`{.interpreted-text
    role="doc"}, `two
    <../../shipping_receiving/daily_operations/receipts_delivery_two_steps>`{.interpreted-text
    role="doc"}, or `three
    <../../shipping_receiving/daily_operations/delivery_three_steps>`{.interpreted-text
    role="doc"} steps.
-   `Dropship Subcontractors`{.interpreted-text role="guilabel"}:
    available with the *Subcontracting* feature enabled in
    `Manufacturing app --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}. Tick this checkbox to purchase components
    from vendors, and dropship them to subcontractors.
-   `Resupply Subcontractors`{.interpreted-text role="guilabel"}:
    available with the *Subcontracting* feature, tick this checkbox to
    supply subcontractors with raw materials stored in *this* specific
    warehouse.
-   `Manufacture to Resupply`{.interpreted-text role="guilabel"}: tick
    this checkbox to allow for items to be manufactured in this
    warehouse.
-   `Manufacture`{.interpreted-text role="guilabel"}: choose whether to
    manufacture products in `one
    <../../../manufacturing/basic_setup/one_step_manufacturing>`{.interpreted-text
    role="doc"}, `two
    <../../../manufacturing/basic_setup/two_step_manufacturing>`{.interpreted-text
    role="doc"}, or `three steps
    <../../../manufacturing/basic_setup/three_step_manufacturing>`{.interpreted-text
    role="doc"}.
-   `Buy to Resupply`{.interpreted-text role="guilabel"}: tick this
    checkbox to allow for purchased products to be delivered to the
    warehouse.
-   `Resupply From`{.interpreted-text role="guilabel"}: available with
    multiple warehouses in the database, select warehouses to pull stock
    *from* to fulfill orders.

::: {.seealso}
`Use inventory adjustments to add stock to new warehouses <count_products>`{.interpreted-text
role="doc"}
:::

{.align-center}
