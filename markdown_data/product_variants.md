# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants.md

Managing BoMs for product variants
==================================

Odoo allows one bill of materials (BoM) to be used for multiple variants
of the same product. Having a consolidated
`BoM (bill of materials)`{.interpreted-text role="abbr"} for a product
with variants saves time by preventing the need to manage multiple
`BoMs (bills of materials)`{.interpreted-text role="abbr"}.

Activate product variants
-------------------------

To activate the product variants feature, navigate to `Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}, and
scroll down to the `Products`{.interpreted-text role="guilabel"}
section. Then, click the checkbox to enable the
`Variants`{.interpreted-text role="guilabel"} option. After that, click
`Save`{.interpreted-text role="guilabel"} to apply the setting.

For more information on configuring product variants, refer to the
`product variants
<../../../sales/sales/products_prices/products/variants>`{.interpreted-text
role="doc"} documentation.

{.align-center}

Create custom product attributes
--------------------------------

Once the product variants feature is activated, create and edit product
attributes on the `Attributes`{.interpreted-text role="guilabel"} page.

The `Attributes`{.interpreted-text role="guilabel"} page is accessible
either from `Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"} by
clicking the `Attributes`{.interpreted-text role="guilabel"} button, or
by clicking
`Inventory app --> Configuration --> Attributes`{.interpreted-text
role="menuselection"}.

Once on the `Attributes`{.interpreted-text role="guilabel"} page, either
click into an existing attribute, or click `Create`{.interpreted-text
role="guilabel"} to create a new one. Clicking
`Create`{.interpreted-text role="guilabel"} reveals a new, blank form
for customizing an attribute. For an existing attribute, click
`Edit`{.interpreted-text role="guilabel"} on its form to make changes.

Assign an `Attribute Name`{.interpreted-text role="guilabel"}, and
choose a category from the `Category`{.interpreted-text role="guilabel"}
field\'s drop-down menu. Then, select the desired options next to the
`Display Type`{.interpreted-text role="guilabel"} and
`Variants Creation Mode`{.interpreted-text role="guilabel"} fields. Once
the desired options are selected, click `Add a line`{.interpreted-text
role="guilabel"} under the `Attribute Values`{.interpreted-text
role="guilabel"} tab to add a new value.

::: {.tip}
::: {.title}
Tip
:::

Included on the `Value`{.interpreted-text role="guilabel"} row is a
`Is custom value`{.interpreted-text role="guilabel"} checkbox. If
selected, this value will be recognized as a custom value, which allows
customers to type special customization requests upon ordering a custom
variant of a product.
:::

::: {.example align="center" alt="Product variant attribute configuration screen."}
.. image:: product\_variants/product-variants-attribute.png
:::

Once all desired `Values`{.interpreted-text role="guilabel"} have been
added, click `Save`{.interpreted-text role="guilabel"} to save the new
attribute.

Add product variants on the product form
----------------------------------------

Created attributes can be applied on specific variants for particular
products. To add product variants to a product, navigate to the product
form by going to `Inventory app -->
Products --> Products`{.interpreted-text role="menuselection"}. To make
changes to the product, click `Edit`{.interpreted-text role="guilabel"}.
Then, click the `Variants`{.interpreted-text role="guilabel"} tab.

Under the `Attribute`{.interpreted-text role="guilabel"} header, click
`Add a line`{.interpreted-text role="guilabel"} to add a new attribute,
and select one to add from the drop-down menu.

Then, under the `Values`{.interpreted-text role="guilabel"} header,
click the drop-down menu to choose from the list of existing values.
Click on each desired value to add them, and repeat this process for any
additional attributes that should be added to the product.

Once finished, click `Save`{.interpreted-text role="guilabel"} to save
changes.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

`BoM (bill of materials)`{.interpreted-text role="abbr"} products with
multiple variants that are manufactured in-house should either have a
**0,0 reordering rule** set up, or have their replenishment routes set
to *Replenish on Order (MTO)*.
:::

Apply BoM components to product variants
----------------------------------------

Next, create a new `BoM (bill of materials)`{.interpreted-text
role="abbr"}. Or, edit an existing one, by going to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}. Then, click `Create`{.interpreted-text
role="guilabel"} to open a new `Bills of Materials`{.interpreted-text
role="guilabel"} form to configure from scratch.

Add a product to the `BoM (bill of materials)`{.interpreted-text
role="abbr"} by clicking the drop-down menu in the
`Product`{.interpreted-text role="guilabel"} field and selecting the
desired product.

Then, add components by clicking `Add a line`{.interpreted-text
role="guilabel"} under the `Component`{.interpreted-text
role="guilabel"} section of the `Components`{.interpreted-text
role="guilabel"} tab, and choosing the desired components from the
drop-down menu.

Choose the desired values in the `Quantity`{.interpreted-text
role="guilabel"} and `Product Unit of Measure`{.interpreted-text
role="guilabel"} columns. Then, choose the desired values in the
`Apply on Variants`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

The `Apply on Variants`{.interpreted-text role="guilabel"} option to
assign components to specific product variants on the
`BoM (bill of materials)`{.interpreted-text role="abbr"} is available
once the `Variants`{.interpreted-text role="guilabel"} setting is
activated from the `Inventory`{.interpreted-text role="menuselection"}
application. If the `Apply on Variants`{.interpreted-text
role="guilabel"} field is not immediately visible, activate it from the
additional options menu (three-dots icon, to the right of the header
row).
:::

{.align-center}

Each component can be assigned to multiple variants. Components with no
variants specified are used in every variant of the product. The same
principle applies when configuring operations and by-products.

When defining variant `BoMs (bills of material)`{.interpreted-text
role="abbr"} by component assignment, the
`Product Variant`{.interpreted-text role="guilabel"} field in the main
section of the `BoM (bill of materials)`{.interpreted-text role="abbr"}
should be left blank. This field is *only* used when creating a
`BoM (bill of materials)`{.interpreted-text role="abbr"} specifically
for one product variant.

When all desired configurations have been made to the
`BoM (bill of materials)`{.interpreted-text role="abbr"}, click
`Save`{.interpreted-text role="guilabel"} at the top of the form to save
changes.

::: {.tip}
::: {.title}
Tip
:::

For components that only apply for specific variants, choose which
operations the components should be consumed in. If the
`Consumed in Operation`{.interpreted-text role="guilabel"} column is
*not* immediately visible, activate it from the additional options menu
(three-dots icon, to the right of the header row).
:::

Sell and manufacture variants of BoM products
---------------------------------------------

To sell and manufacture variants of
`BoM (bill of materials)`{.interpreted-text role="abbr"} products to
order, navigate to `Sales app --> Create`{.interpreted-text
role="menuselection"} to create a new quotation.

### Sell variant of BoM product

Once on the blank `Quotation`{.interpreted-text role="guilabel"} form,
click the drop-down next to the `Customer`{.interpreted-text
role="guilabel"} field to add a customer.

Then, under the `Order Lines`{.interpreted-text role="guilabel"} tab,
click `Add a product`{.interpreted-text role="guilabel"}, and select the
previously-created `BoM (bill of materials)`{.interpreted-text
role="abbr"} product with variants from the drop-down menu. Doing so
reveals a `Configure a product`{.interpreted-text role="guilabel"}
pop-up.

From the pop-up window, click the desired attribute options to configure
the correct variant of the product to manufacture. Then, click the green
`+`{.interpreted-text role="guilabel"} or `-`{.interpreted-text
role="guilabel"} icons next to the [1]{.title-ref} to change the
quantity to sell and manufacture, if desired.

{.align-center}

Once all the specifications have been chosen, click
`Add`{.interpreted-text role="guilabel"}. This will change the pop-up to
a second `Configure`{.interpreted-text role="guilabel"} pop-up, where
available optional products will appear, if they have been created
previously.

Once ready, click `Confirm`{.interpreted-text role="guilabel"} to close
the pop-up.

Then, click `Save`{.interpreted-text role="guilabel"} to save all
changes, and click `Confirm`{.interpreted-text role="guilabel"} at the
top of the `Quotation`{.interpreted-text role="guilabel"} form to create
and confirm a new sales order (SO).

### Manufacture variant of BoM product

Once the `SO (sales order)`{.interpreted-text role="abbr"} is confirmed,
a `Manufacturing`{.interpreted-text role="guilabel"} smart button
appears at the top of the `SO (sales order)`{.interpreted-text
role="abbr"} form. Click the `Manufacturing`{.interpreted-text
role="guilabel"} smart button to open the
`Manufacturing Order`{.interpreted-text role="guilabel"} form.

On this form, under the `Components`{.interpreted-text role="guilabel"}
tab, the appropriate components for the chosen variant are listed. And,
depending on the variant, different components will be listed. To see
any mandatory or optional `Operation`{.interpreted-text role="guilabel"}
steps, click the `Work Orders`{.interpreted-text role="guilabel"} tab.

To enter the tablet view work order screen, click the
`tablet icon`{.interpreted-text role="guilabel"} to the right of the row
for the desired operation to be completed.

From the tablet view, click `Mark as Done`{.interpreted-text
role="guilabel"} as the operation progresses to complete the operation
steps.

Alternatively, click the `Mark as Done`{.interpreted-text
role="guilabel"} button at the top of the manufacturing order form to
complete the order.

{.align-center}

Then, navigate back to the `SO (sales order)`{.interpreted-text
role="abbr"} via the breadcrumbs at the top of the page.

Now that the product has been manufactured, click the
`Delivery`{.interpreted-text role="guilabel"} smart button to deliver
the product to the customer. From the `Delivery Order`{.interpreted-text
role="guilabel"} form, click `Validate`{.interpreted-text
role="guilabel"}, then click `Apply`{.interpreted-text role="guilabel"}
to deliver the product.

To finish the sale, click back to the
`SO (sales order)`{.interpreted-text role="abbr"} via the
`breadcrumbs`{.interpreted-text role="guilabel"} at the top of the page
again. Then, click `Create Invoice`{.interpreted-text role="guilabel"}
followed by `Create
Invoice`{.interpreted-text role="guilabel"} again to invoice the
customer for the order.
