# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/product_management/configure/package.md

Packages
========

A *package* is a physical container holding one or more products.
Packages can also be used to store items in bulk.

Packages are commonly used for the following purposes:

1.  `Grouping products to move them in bulk <inventory/warehouses_storage/pack>`{.interpreted-text
    role="ref"}.
2.  `Shipping to customers <inventory/warehouses_storage/package-type>`{.interpreted-text
    role="ref"}: configure package types to align with shipping
    carriers\' size and weight requirements, streamlining the packing
    process, and ensuring compliance with carrier shipping
    specifications.
3.  Storing items in bulk.

*Package use* is a field on the package form in Odoo that is only
visible by enabling the *Batch Transfers* and *Packages* features
(`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}).

By default, the *Package Use* field on a packages form is set to
*Disposable Box*. Change this field to *Reusable Box* **only** when
configuring packages for `cluster pickings
<inventory/warehouses_storage/cluster-pack>`{.interpreted-text
role="ref"}.

*Package type* is an optional feature used for
`calculating shipping cost
<../../shipping_receiving/setup_configuration>`{.interpreted-text
role="doc"}, based on real shipping weight. Create package types to
include the weight of the package itself (e.g. boxes, pallets, other
shipping containers) in shipping cost calculations.

::: {.note}
::: {.title}
Note
:::

While packages are commonly used in the `three-step delivery route
<../../shipping_receiving/daily_operations/delivery_three_steps>`{.interpreted-text
role="doc"}, they can be used in any workflow involving storable
products.
:::

Configuration {#inventory/warehouses_storage/enable-package}
-------------

To use packages, first go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Operations`{.interpreted-text
role="guilabel"} heading, activate the `Packages`{.interpreted-text
role="guilabel"} feature. Then, click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {#inventory/product_management/move-entire-pack}
When moving packages internally, the *Move Entire Packages* feature can
be enabled on an operation type to update a package\'s contained item\'s
location upon updating the package\'s location.
:::

To do that, go to
`Inventory app --> Configuration --> Operations Types`{.interpreted-text
role="menuselection"} and select the desired operation this feature will
apply to (may have to set it for multiple).

On the operation type page, in the `Packages`{.interpreted-text
role="guilabel"} section, tick the `Move Entire
Packages`{.interpreted-text role="guilabel"} checkbox.

Pack items {#inventory/warehouses_storage/pack}
----------

Products can be added to packages in any transfer by:

1.  Clicking each
    `Detailed Operations <inventory/warehouses_storage/detailed-operations>`{.interpreted-text
    role="ref"} icon on the product line.
2.  Using the
    `Put in Pack <inventory/warehouses_storage/put-in-pack>`{.interpreted-text
    role="ref"} button to place everything in the transfer into a
    package.

### Detailed operations {#inventory/warehouses_storage/detailed-operations}

On any warehouse transfer (e.g. receipt, delivery order), add a product
to a package by clicking the `⦙≣ (bulleted list)`{.interpreted-text
role="guilabel"} icon in the `Operations`{.interpreted-text
role="guilabel"} tab.

{.align-center}

Doing so opens the `Detailed Operations`{.interpreted-text
role="guilabel"} pop-up window for the `Product`{.interpreted-text
role="guilabel"}.

To put the `Product`{.interpreted-text role="guilabel"} in a package,
click `Add a line`{.interpreted-text role="guilabel"}, and assign the
product to a `Destination Package`{.interpreted-text role="guilabel"}.
Select an existing package, or create a new one by typing the name of
the new package, then select `Create...`{.interpreted-text
role="guilabel"}.

![Twelve units of [Acoustic Bloc Screen]{.title-ref} are placed in
{.align-center}

Then, specify the quantity of items to go into the package in the
`Done`{.interpreted-text role="guilabel"} column. Repeat the above steps
to place the `Product`{.interpreted-text role="guilabel"} in different
packages. Once finished, click `Confirm`{.interpreted-text
role="guilabel"} to close the window.

::: {.seealso}
`Ship one order in multiple packages
<../../shipping_receiving/setup_configuration/multipack>`{.interpreted-text
role="doc"}
:::

### Put in pack {#inventory/warehouses_storage/put-in-pack}

Alternatively, click the `Put in Pack`{.interpreted-text
role="guilabel"} button on **any** warehouse transfer to create a new
package, and place all the items in the transfer in that newly-created
package.

::: {.important}
::: {.title}
Important
:::

The `Put in Pack`{.interpreted-text role="guilabel"} button appears on
receipts, delivery orders, and other transfer forms with the *Packages*
feature enabled in `Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}.
:::

![In batch transfer [BATCH/00003]{.title-ref}, the
`Put in Pack`{.interpreted-text role="guilabel"} button was clicked to
create a new package, [PACK0000002]{.title-ref}, and assign all items to
it in the `Destination Package`{.interpreted-text role="guilabel"}
field.](package/put-in-pack.png){.align-center}

Package type {#inventory/warehouses_storage/package-type}
------------

Create package types by navigating to
`Inventory app --> Configuration --> Package
Types`{.interpreted-text role="menuselection"}, in order to set custom
dimensions and weight limits. This feature is mainly used to calculate
package weights for shipping costs.

::: {.seealso}
\-
`Shipping carriers <../../shipping_receiving/setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"} -
`../../shipping_receiving/setup_configuration`{.interpreted-text
role="doc"}
:::

On the `Package Types`{.interpreted-text role="guilabel"} list, clicking
`New`{.interpreted-text role="guilabel"} opens a blank package type
form. The fields of the form are as follows:

-   `Package Type`{.interpreted-text role="guilabel"} (required): define
    the package type\'s name.
-   `Size`{.interpreted-text role="guilabel"}: define the dimensions of
    the package in millimeters (mm). The fields, from left to right,
    define the `Length`{.interpreted-text role="guilabel"},
    `Width`{.interpreted-text role="guilabel"}, and
    `Height`{.interpreted-text role="guilabel"}.
-   `Weight`{.interpreted-text role="guilabel"}: weight of an empty
    package (e.g. an empty box, pallet).

::: {.note}
::: {.title}
Note
:::

Odoo calculates the package\'s weight by adding the weight of the empty
package plus the weight of the item(s), which can be found in the
`Weight`{.interpreted-text role="guilabel"} field, in the
`Inventory`{.interpreted-text role="guilabel"} tab, of each product
form.
:::

-   `Max Weight`{.interpreted-text role="guilabel"}: maximum shipping
    weight allowed in the package.
-   `Barcode`{.interpreted-text role="guilabel"}: define a barcode to
    identify the package type from a scan.
-   `Company`{.interpreted-text role="guilabel"}: specify a company to
    make the package type available **only** at the selected company.
    Leave the field blank if it is available at all companies.
-   `Carrier`{.interpreted-text role="guilabel"}: specify the intended
    shipping carrier for this package type.
-   `Carrier Code`{.interpreted-text role="guilabel"}: define a code
    that is linked to the package type.

{.align-center}

Cluster packages {#inventory/warehouses_storage/cluster-pack}
----------------

To use *cluster packages*, first navigate to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and activate the
`Batch Transfers`{.interpreted-text role="guilabel"} feature, located in
the `Operations`{.interpreted-text role="guilabel"} section. Doing so
makes the *Package Use* field become visible on a package form.

{.align-center}

Add new packages by going to
`Inventory app --> Products --> Packages`{.interpreted-text
role="menuselection"}. Then, click `New`{.interpreted-text
role="guilabel"}, or select an existing package. Doing so opens the
package form, which contains the following fields:

-   `Package Reference`{.interpreted-text role="guilabel"} (required):
    name of the package.

-   `Package Type`{.interpreted-text role="guilabel"}: used for
    `configuring shipping boxes to ship to the customer
    <inventory/warehouses_storage/package-type>`{.interpreted-text
    role="ref"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    `Package Type`{.interpreted-text role="guilabel"} is unnecessary for
    configuring packages for cluster pickings.
    :::

-   `Shipping Weight`{.interpreted-text role="guilabel"}: used to input
    the weight of the package after measuring it on a scale.

-   `Company`{.interpreted-text role="guilabel"}: specify a company to
    make the package available **only** at the selected company. Leave
    the field blank if the package is available at all companies.

-   `Location`{.interpreted-text role="guilabel"}: current location of
    the package.

-   `Pack Date`{.interpreted-text role="guilabel"}: the date the package
    was created.

-   `Package Use`{.interpreted-text role="guilabel"}: choose
    `Reusable`{.interpreted-text role="guilabel"} for packages used for
    moving products within the warehouse; `Disposable`{.interpreted-text
    role="guilabel"} for packages used to ship products to customers.

{.align-center}

::: {.seealso}
`Using cluster packages <../../shipping_receiving/picking_methods/cluster>`{.interpreted-text
role="doc"}
:::
