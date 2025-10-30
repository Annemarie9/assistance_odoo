# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/least_packages.md

Least packages removal
======================

The *Least Packages* removal strategy fulfills an order by opening the
fewest number of packages, which is ideal for maintaining organized
stock without needing to open multiple boxes.

::: {.seealso}
\- `About removal strategies <../removal_strategies>`{.interpreted-text
role="doc"} - [Odoo Tutorials: Least
Packages](https://www.odoo.com/slides/slide/5477/share)
:::

To understand how the removal strategy works, consider the following
example, featuring a warehouse that stores packages of flour in bulk
packages of [100 kg]{.title-ref}.

To minimize moisture, and/or prevent pests from entering open packages,
the least packages removal strategy is used to pick from a single,
opened package.

::: {#inventory/warehouses_storage/pkg-qty}
::: {.example}
A package of [100 kg]{.title-ref} of flour is depleted to [54
kg]{.title-ref} after fulfilling some orders. There are other packages
of [100 kg]{.title-ref} in stock.

1.  When an order for [14 kg]{.title-ref} of flour is placed, the
    package of [54 kg]{.title-ref} is selected.
2.  When an order for *more* than [54 kg]{.title-ref} of flour is
    placed, an unopened [100 kg]{.title-ref} package is used to fulfill
    the order. While this temporarily results in two open packages,
    these open packages are prioritized in the next picking.
:::
:::

Workflow
--------

Using the least package removal strategy, the fewest number of packages
is used to fulfill an order.

::: {.important}
::: {.title}
Important
:::

The
`Packages feature <inventory/warehouses_storage/pack-setup>`{.interpreted-text
role="ref"} **must** be enabled to use this strategy.
:::

Consider the following example, featuring the product,
[Flour]{.title-ref}. The product\'s `Units of
Measure`{.interpreted-text role="guilabel"} field, located on the
product form, is set to [kg]{.title-ref}. The product is stored in
packages of [100 kg]{.title-ref}, with one remaining package containing
[54 kg]{.title-ref}. The product category\'s `Force
Removal Strategy`{.interpreted-text role="guilabel"} is set to
`Least Packages`{.interpreted-text role="guilabel"}.

::: {.seealso}
\-
`Set removal strategy on product category <inventory/warehouses_storage/removal-config>`{.interpreted-text
role="ref"}
:::

::: {.tip}
::: {.title}
Tip
:::

To check the product\'s on-hand stock, navigate to the product form, and
click the `On
Hand`{.interpreted-text role="guilabel"} smart button.

{.align-center}
:::

Create a
`delivery order <inventory/delivery/one-step>`{.interpreted-text
role="ref"} for eighty kilograms of flour by going to the
`Sales app`{.interpreted-text role="menuselection"} and creating a new
quotation. After clicking `Confirm`{.interpreted-text role="guilabel"},
the delivery order is created.

On the delivery order, the `Quantity`{.interpreted-text role="guilabel"}
field displays the amount automatically picked, according to the removal
strategy.

For more details about *where* the units were picked, select the
`⦙≣ (bulleted list)`{.interpreted-text role="guilabel"} icon, located on
the far-right. Doing so opens the `Open: Stock move`{.interpreted-text
role="guilabel"} pop-up window, displaying how the reserved items were
picked, according to the removal strategy.

In the `Open: Stock move`{.interpreted-text role="guilabel"} pop-up
window, the `Pick from`{.interpreted-text role="guilabel"} field
displays where the quantities to fulfill the `Demand`{.interpreted-text
role="guilabel"} are picked. Since the order demanded eighty kilograms,
which exceeds the quantity in the opened package of [54 kg]{.title-ref},
an unopened package of [100 kg]{.title-ref} is selected.

{.align-center}
