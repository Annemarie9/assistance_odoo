# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/advanced_configuration/kit_shipping.md

Kits
====

In Odoo, a *kit* is a type of bill of materials (BoM) that can be
manufactured and sold. Kits are sets of unassembled components sold to
customers. They may be sold as standalone products, and are also useful
tools for managing more complex bills of materials (BoMs).

::: {.note}
::: {.title}
Note
:::

To use, manufacture, and sell kits, both the
`Manufacturing`{.interpreted-text role="guilabel"} and
`Inventory`{.interpreted-text role="guilabel"} apps need to be
installed.
:::

Create the kit as a product
---------------------------

To use a kit as a sellable product, or as a component organization tool,
the kit should first be created as a product.

To create a kit product, go to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and then click `New`{.interpreted-text
role="guilabel"}.

Then, assign a name to the new kit product. Next, set the kit\'s product
type depending on inventory tracking needs and accounting requirements.
To do this, under the `General Information`{.interpreted-text
role="guilabel"} tab, set the `Product Type`{.interpreted-text
role="guilabel"} to either `Consumable`{.interpreted-text
role="guilabel"} or `Storable`{.interpreted-text role="guilabel"}.

The kit\'s components must also be configured as products via
`Inventory app -->
Products --> Products`{.interpreted-text role="menuselection"}. These
components require no specific configuration.

### Consumable kit setup details

Consumable products do not have inventory tracking. Consider setting the
kit as a consumable product when the kit is used in other manufacturing
processes or when tracking inventory for the kit itself is not needed.

-   **Recommended for Continental Accounting**: If costs are expensed
    immediately upon purchase, then setting the kit\'s type to
    *consumable* is recommended.
-   **Replenishment via Components**: Inventory count is managed at the
    component level, so reordering rules must be set to individual
    components.
-   **Selling & Stock Constraints**: Kits cannot be sold if any required
    component is out of stock. Since availability depends on individual
    components, a sales order may appear valid, but delivery can be
    delayed if components are unavailable.

### Storable kit setup details

Storable products have detailed tracking and inventory management since
they are expected to be *stored* once they are created. Consider setting
the kit as a storable product when the kit is a tangible product or
warehouse and inventory tracking is essential.

-   **Recommended for Angle-Saxon Accounting**: If the Cost of Goods
    Sold (COGS) needs to be recorded in journals, then setting the
    kit\'s type to *storable* is recommended.
-   **Component Purchase Constraints**: Only the kit\'s minimum required
    components can be added to an **eCommerce** cart unless the option
    to `continue
    selling<../../../websites/ecommerce/products>`{.interpreted-text
    role="doc"} is disabled.
-   **No Kit Serial Numbers**: Serial number tracking does not track the
    kit, only its shipped components.
-   **Reordering Rule Recommendation**: Reordering rules should be set
    at the component-level.
-   **Stock Replenishment Recommendation**: Stock replenishment should
    also be done at the component-level.

### Kit setup similarities

Regardless of which setup is used, there are some similarities between
the two options.

-   **No Kit-Level Stock Adjustments**: Stock adjustments cannot be
    handled at the kit-level.
-   **Kit Value Does Not Change**: The stock\'s value is the same
    whether the kit is consumable or storable.
-   **Kit Internal Transfers**: An internal transfer for the kit breaks
    it into components.

Set up the kit BoM
------------------

After fully configuring the kit product and its components, a new
`BoM (bill of materials)`{.interpreted-text role="abbr"} can be created
for the kit product.

To do so, go to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}, and then click `New`{.interpreted-text
role="guilabel"}. Next to the `Product`{.interpreted-text
role="guilabel"} field, click the drop-down menu to reveal a list of
products, and then select the previously configured kit product.

Then, for the `BoM Type`{.interpreted-text role="guilabel"} field, click
the `Kit`{.interpreted-text role="guilabel"} option. Finally, under the
`Components`{.interpreted-text role="guilabel"} tab, click
`Add a line`{.interpreted-text role="guilabel"}, and add each desired
component, and specify their quantities under the
`Quantity`{.interpreted-text role="guilabel"} column.

Once ready, click `Save`{.interpreted-text role="guilabel"} to save the
newly created `BoM (bill of materials)`{.interpreted-text role="abbr"}.



If the kit is solely being used as a sellable product, then only
components need to be added under the `Components`{.interpreted-text
role="guilabel"} tab, and configuring manufacturing operations is not
necessary.

::: {.note}
::: {.title}
Note
:::

When a kit is sold as a product, it appears as a single line item on the
quotation and sales order. However, on delivery orders, each component
of the kit is listed.
:::

Use kits to manage complex BoMs
-------------------------------

Kits can also be used for complex
`BoMs (Bills of Materials)`{.interpreted-text role="abbr"}. This method
nests BoMs within other BoMs, organizing complex products while
simplifying manufacturing by defining each procurement and production
step separately.

Sublevel BoMs (subassemblies or semi-finished products) streamline these
workflows, helping with traceability efforts.

::: {.seealso}
`sub_assemblies`{.interpreted-text role="doc"}
:::
