# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/workflows/byproducts.md

By-Products
===========

When manufacturing certain products, it is common to be left with
residual materials, in addition to the finished product. These materials
are known as *by-products*. By specifying the by-products created during
manufacturing on a product\'s bill of materials (BoM), the quantity of
by-products on-hand is tracked by Odoo.

::: {.example}
Manufacturing a *rocking chair* requires ten pieces of wood. During
production, five pieces of *scrap wood* are created, in addition to the
rocking chair. By designating the scrap wood as a by-product on the
rocking chair\'s `BoM (bill of materials)`{.interpreted-text
role="abbr"}, Odoo tracks the on-hand count of scrap wood, as well as
the quantity of rocking chairs produced.
:::

Configuration
-------------

To specify by-products on a product\'s
`BoM (bill of materials)`{.interpreted-text role="abbr"}, the
*By-Products* setting **must** be enabled. To do so, navigate to
`Manufacturing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the `By-Products`{.interpreted-text
role="guilabel"} checkbox, located under the
`Operations`{.interpreted-text role="guilabel"} heading. Then, click
`Save`{.interpreted-text role="guilabel"} to apply the change.

{.align-center}

With the `By-Products`{.interpreted-text role="guilabel"} setting
enabled, a `By-products`{.interpreted-text role="guilabel"} tab appears
on product `BoMs (bills of materials)`{.interpreted-text role="abbr"}.

Add byproduct to BoM
--------------------

To add by-products to a `BoM (bill of materials)`{.interpreted-text
role="abbr"}, navigate to `Manufacturing app --> Products --> Bills
of Materials`{.interpreted-text role="menuselection"}, and select a
`BoM (bill of materials)`{.interpreted-text role="abbr"}.

On the `BoM (bill of materials)`{.interpreted-text role="abbr"}, select
the `By-products`{.interpreted-text role="guilabel"} tab. Click
`Add a line`{.interpreted-text role="guilabel"}, and select the
by-product in the `By-product`{.interpreted-text role="guilabel"}
drop-down field. In the `Quantity`{.interpreted-text role="guilabel"}
field, enter the quantity of the by-product produced during
manufacturing.

If the by-product is produced during a specific operation of a
manufacturing order (MO), select the operation in the
`Produced in Operation`{.interpreted-text role="guilabel"} field. For
example, if a scrap wood by-product is produced during an *Assemble*
operation, select that operation in the `Produced in
Operation`{.interpreted-text role="guilabel"} field.

{.align-center}

Manufacture by-product
----------------------

When an `MO (manufacturing order)`{.interpreted-text role="abbr"} is
completed and marked as *Done*, Odoo registers the quantity of
by-products created during the manufacturing process. To create a new
`MO (manufacturing order)`{.interpreted-text role="abbr"}, navigate to
`Manufacturing
app --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}.

In the `Bill of Material`{.interpreted-text role="guilabel"} field,
select a `BoM (bill of materials)`{.interpreted-text role="abbr"} on
which by-products have been specified. After doing so, the
`Product`{.interpreted-text role="guilabel"} field auto-populates with
the corresponding product. Click `Confirm`{.interpreted-text
role="guilabel"} to confirm the
`MO (manufacturing order)`{.interpreted-text role="abbr"}.

When manufacturing is completed, click the
`Produce All`{.interpreted-text role="guilabel"} button at the top of
the `MO (manufacturing order)`{.interpreted-text role="abbr"}. After
doing so, inventory counts update to reflect the quantity of
by-product(s) produced, as well as the quantity of the product.

Click the `Product Moves`{.interpreted-text role="guilabel"} smart
button at the top of the `MO (manufacturing order)`{.interpreted-text
role="abbr"} page to see the movements of components and products. Each
by-product is listed on the resulting
`Inventory Moves`{.interpreted-text role="guilabel"} page, with the
`From`{.interpreted-text role="guilabel"} column displaying the virtual
production location, and the `To`{.interpreted-text role="guilabel"}
column displaying the location where the by-product is stored.

{.align-center}
