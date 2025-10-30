# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/basic_setup/configure_manufacturing_product.md

Manufacturing product configuration
===================================

In order to manufacture a product in Odoo *Manufacturing*, the product
must be properly configured. Doing so consists of enabling the
*Manufacturing* route and configuring a bill of materials (BoM) for the
product. Once these steps are completed, the product is selectable when
creating a new manufacturing order.

Activate the Manufacture route
------------------------------

The Manufacture route is activated for each product on its own product
page. To do so, begin by navigating to
`Manufacturing --> Products --> Products`{.interpreted-text
role="menuselection"}. Then, select an existing product, or create a new
one by clicking `New`{.interpreted-text role="guilabel"}.

On the product page, select the `Inventory`{.interpreted-text
role="guilabel"} tab, then enable the `Manufacture`{.interpreted-text
role="guilabel"} checkbox in the `Routes`{.interpreted-text
role="guilabel"} section. This tells Odoo the product can be
manufactured.

{.align-center}

### Lot/serial number tracking {#manufacturing/basic_setup/lot-serial-tracking}

The assignment of lots or serial numbers to newly manufactured products
is optional. To optionally
`assign lots or serial numbers <../../inventory/product_management/product_tracking/create_sn>`{.interpreted-text
role="doc"} to newly manufactured products, go to the
`Traceability`{.interpreted-text role="guilabel"} section in the
`Inventory`{.interpreted-text role="guilabel"} tab. In the
`Tracking`{.interpreted-text role="guilabel"} field, select
`By Unique Serial
Number`{.interpreted-text role="guilabel"} or
`By Lots`{.interpreted-text role="guilabel"}.

Doing so enables the *Lot/Serial Number* field on a manufacturing order,
or the *Register Production* instruction on a work order card in the
*Shop Floor* app.

![**Lot/Serial Number** field on the
MO.](configure_manufacturing_product/lot-number-field.png){.align-center}

![**Register Production** option to generate lot/serial number on a work
order
card.](configure_manufacturing_product/register-production.png){.align-center}

Configure a bill of materials (BoM)
-----------------------------------

Next, a must be configured for the product so Odoo knows how it is
manufactured. A is a list of the components and operations required to
manufacture a product.

To create a for a specific product, navigate to
`Manufacturing --> Products -->
Products`{.interpreted-text role="menuselection"}, then select the
product. On the product page, click the
`Bill of Materials`{.interpreted-text role="guilabel"} smart button at
the top of the page, then select `New`{.interpreted-text
role="guilabel"} to configure a new .

{.align-center}

On the , the `Product`{.interpreted-text role="guilabel"} field
auto-populates with the product. In the `Quantity`{.interpreted-text
role="guilabel"} field, specify the number of units that the BoM
produces.

Add a component to the by selecting the `Components`{.interpreted-text
role="guilabel"} tab and clicking `Add
a line`{.interpreted-text role="guilabel"}. Select a component from the
`Component`{.interpreted-text role="guilabel"} drop-down menu, then
enter the quantity in the `Quantity`{.interpreted-text role="guilabel"}
field. Continue adding components on new lines until all components have
been added.

{.align-center}

Next, select the `Operations`{.interpreted-text role="guilabel"} tab.
Click `Add a line`{.interpreted-text role="guilabel"} and a `Create
Operations`{.interpreted-text role="guilabel"} pop-up window appears. In
the `Operation`{.interpreted-text role="guilabel"} field, specify the
name of the operation being added (e.g. Assemble, Cut, etc.). Select the
work center where the operation will be carried out from the
`Work Center`{.interpreted-text role="guilabel"} drop-down menu.
Finally, click `Save & Close`{.interpreted-text role="guilabel"} to
finish adding operations, or `Save & New`{.interpreted-text
role="guilabel"} to add more.

::: {.important}
::: {.title}
Important
:::

The `Operations`{.interpreted-text role="guilabel"} tab only appears if
the `Work Orders`{.interpreted-text role="guilabel"} setting is enabled.
To do so, navigate to
`Manufacturing --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, then enable the `Work Orders`{.interpreted-text
role="guilabel"} checkbox.
:::

{.align-center}

::: {.admonition}
Learn more

The section above provides instructions for creating a basic that allows
a product to be manufactured in Odoo. However, it is by no means an
exhaustive summary of all the options available when configuring a . For
more information about bills of materials, see the documentation on how
to `create a bill of materials <bill_configuration>`{.interpreted-text
role="doc"}.
:::
