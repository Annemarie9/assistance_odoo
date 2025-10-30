# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/workflows/unbuild_orders.md

Unbuild orders
==============

In some cases, it is necessary to dismantle manufactured products into
their individual components. This may be required if too many units of a
product were built, or if the components of one product must be
reclaimed to use in the manufacturing of another.

In Odoo *Manufacturing*, products can be dismantled, and their
components returned to inventory, using *unbuild orders*. By using
unbuild orders to accomplish this task, inventory counts for the
finished product and its components remain accurate, based on the
quantity of products dismantled, and the quantity of components
reclaimed.

Create unbuild order
--------------------

A new unbuild order can be created by navigating to
`Manufacturing app --> Operations
--> Unbuild Orders`{.interpreted-text role="menuselection"}, and
clicking `New`{.interpreted-text role="guilabel"}.

Begin filling out the new unbuild order by selecting a
`Product`{.interpreted-text role="guilabel"} to unbuild. After doing so,
the `Bill of Material`{.interpreted-text role="guilabel"} field
auto-populates with the corresponding bill of materials (BoM). If a
different `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
should be used, click on the `Bill of Material`{.interpreted-text
role="guilabel"} field, and select it from the drop-down menu.

Alternatively, a specific `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} can be selected in the `Bill of Material`{.interpreted-text
role="guilabel"} field before selecting a product, which causes the
corresponding product to auto-populate in the
`Product`{.interpreted-text role="guilabel"} field.

Next, specify the `Quantity`{.interpreted-text role="guilabel"} of the
product that is being unbuilt.

If the product being unbuilt was originally manufactured in a specific
manufacturing order (MO), select it in the
`Manufacturing Order`{.interpreted-text role="guilabel"} field.

In the `Source Location`{.interpreted-text role="guilabel"} field,
select the location where the product being unbuilt is currently stored.

In the `Destination Location`{.interpreted-text role="guilabel"} field,
select the location where the reclaimed components are stored after the
unbuild order is completed.

If the *Lots & Serial Numbers* feature is enabled in the settings of the
*Inventory* app, a `Lot/Serial Number`{.interpreted-text
role="guilabel"} field appears on the unbuild order, which can be used
to specify the lot(s) or serial number(s) of the product being unbuilt,
if any are assigned.

If the Odoo database has been configured with multiple companies, a
`Company`{.interpreted-text role="guilabel"} field appears on the
unbuild order, which can be used to specify the company that owns the
product being unbuilt.

Finally, once the product has been unbuilt, click the
`Unbuild`{.interpreted-text role="guilabel"} button at the top of the
order to confirm that it has been completed.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

While it is possible to create unbuild orders for products that have
zero (or fewer) units on-hand, this is not advised, since it can lead to
inventory inconsistencies.

If an unbuild order is created for a product with zero (or fewer) units
on-hand, a pop-up window appears, warning the user that there is an
insufficient quantity to unbuild.

To ignore the warning, and proceed with the unbuild order, click
`Confirm`{.interpreted-text role="guilabel"} at the bottom of the pop-up
window. To return to the unconfirmed unbuild order, click
`Discard`{.interpreted-text role="guilabel"}, instead.

![The insufficient quantity pop-up that appears after trying to confirm an unbuild order
for a product with zero or fewer units on hand.](unbuild_orders/insufficient-quantity.png){.align-center}
:::

After completing an unbuild order, inventory counts automatically
update, based on the quantity of products unbuilt, and the quantity of
components reclaimed.

::: {.example}
A [Coat Rack]{.title-ref} product is comprised of one [Wooden
Pole]{.title-ref} component and six [Wooden Dowel]{.title-ref}
components.

An unbuild order is created for one unit of the [Coat Rack]{.title-ref}.
Once the order is completed, the on-hand quantity of [Coat
Racks]{.title-ref} decreases by one, while the on-hand quantities of
[Wooden Poles]{.title-ref} and [Wooden Dowels]{.title-ref} increase by
one and six, respectively.
:::

Scrap unusable components
-------------------------

In some cases, components may be unusable after the unbuilding process
is completed. To ensure that inventory counts accurately reflect the
quantity of usable components on-hand, any component that can no longer
be used should be removed from inventory using a `scrap order
<../../inventory/warehouses_storage/inventory_management/scrap_inventory>`{.interpreted-text
role="doc"}.
