# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.md

Bill of materials
=================

A *bill of materials* (or *BoM* for short) documents specific
components, along with their respective quantities, that are needed to
produce or repair a product. In Odoo,
`BoMs (Bills of Materials)`{.interpreted-text role="abbr"} serve as
blueprints for manufactured goods and kits, and often include production
operations and step-by-step guidelines, as well.

BoM setup
---------

To create a `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, go
to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text
role="guilabel"}.

Next, set the `BoM Type`{.interpreted-text role="guilabel"} to
`Manufacture this Product`{.interpreted-text role="guilabel"}.

Then, specify
`required components <manufacturing/basic_setup/setup-components>`{.interpreted-text
role="ref"} and, if necessary, define any
`manufacturing operations <manufacturing/basic_setup/setup-operations>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

Individual `BoMs (Bills of Materials)`{.interpreted-text role="abbr"}
can also be quickly accessed or created by clicking the `Bill of
Materials`{.interpreted-text role="guilabel"} smart button on any
product form, as accessible through the *Sales*, *Inventory*, and
*Manufacturing* apps, as well as through any internal links where a
product is referenced (such as in a field or a line item).
:::

![BoM for [Drawer]{.title-ref}, displaying the **Components**
tab.](bill_configuration/bom-example.png){.align-center}

::: {.seealso}
\- `../advanced_configuration/kit_shipping`{.interpreted-text
role="doc"} - `../subcontracting/subcontracting_basic`{.interpreted-text
role="doc"}
:::

### Components {#manufacturing/basic_setup/setup-components}

In the `Components`{.interpreted-text role="guilabel"} tab of a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, specify
components used to manufacture the product by clicking
`Add a line`{.interpreted-text role="guilabel"}. From the
`Components`{.interpreted-text role="guilabel"} drop-down menu, select
from existing products or create a new product by typing the name and
selecting either the `Create " "`{.interpreted-text role="guilabel"}
option to quickly add the line item, or the
`Create and edit...`{.interpreted-text role="guilabel"} option to add
the component and continue to its configuration form.

{.align-center}

Optionally, access additional fields by clicking the
`oi-settings-adjust`{.interpreted-text role="icon"} `(settings
adjust)`{.interpreted-text role="guilabel"} icon to the far-right of the
`Components`{.interpreted-text role="guilabel"} tab. Tick the checkboxes
for the following features to enable these columns:

-   `Apply on Variants`{.interpreted-text role="guilabel"}: specify
    which `product variant
    <../advanced_configuration/product_variants>`{.interpreted-text
    role="doc"} each component is used in. When the field is left blank,
    the component is used in all product variants.

::: {#manufacturing/basic_setup/consumed-in-operation}
-   `Consumed in Operation`{.interpreted-text role="guilabel"}: specify
    the operation using the component. Useful for determining
    `manufacturing readiness <manufacturing/basic_setup/manufacturing-readiness>`{.interpreted-text
    role="ref"}.

-   `Manual Consumption`{.interpreted-text role="guilabel"}: tick the
    checkbox to force operators to check the
    `Consumed`{.interpreted-text role="guilabel"} checkbox on a
    manufacturing order (MO).

    {.align-center}

    Not doing so triggers the `Consumption Warning`{.interpreted-text
    role="guilabel"} error message, where the consumed component
    quantity must be manually inputted. Otherwise, the operation cannot
    be completed.

    {.align-center}
:::

### Operations {#manufacturing/basic_setup/setup-operations}

Add an *operation* to a `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} to specify instructions for production and register time
spent on an operation. To use this feature, first enable the *Work
Orders* feature by going to
`Manufacturing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Operations`{.interpreted-text
role="guilabel"} section, tick the `Work Orders`{.interpreted-text
role="guilabel"} checkbox to enable the feature.

::: {.seealso}
`../advanced_configuration/work_order_dependencies`{.interpreted-text
role="doc"}
:::

{.align-center}

Next, navigate to the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} by going to `Manufacturing app --> Products --> Bill of
Materials`{.interpreted-text role="menuselection"} and selecting the
desired `BoM (Bill of Materials)`{.interpreted-text role="abbr"}. To add
a new operation, go to the `Operations`{.interpreted-text
role="guilabel"} tab, and click `Add a line`{.interpreted-text
role="guilabel"}.

Doing so opens the `Create Operations`{.interpreted-text
role="guilabel"} pop-up window, where the various fields of the
operation are configured:

-   `Operation`{.interpreted-text role="guilabel"}: name of the
    operation.

-   `Work Center`{.interpreted-text role="guilabel"}: select existing
    locations to perform the operation, or create a new work center by
    typing the name and selecting the `Create " "`{.interpreted-text
    role="guilabel"} option.

-   `Apply on Variants`{.interpreted-text role="guilabel"}: specify if
    this operation is only available for certain product variants. If
    the operation applies to all product variants, leave this field
    blank.

    ::: {.seealso}
    `Configuring BoMs for product variants <../advanced_configuration/product_variants>`{.interpreted-text
    role="doc"}
    :::

-   `Duration Computation`{.interpreted-text role="guilabel"}: choose
    how time spent on the operation is tracked. Opt for
    `Compute based on tracked time`{.interpreted-text role="guilabel"}
    to use the operation\'s time tracker or `Set
    duration manually`{.interpreted-text role="guilabel"} if operators
    can record and modify time themselves.

    Choosing the `Compute based on tracked time`{.interpreted-text
    role="guilabel"} option enables the `Based on last
    __ work orders`{.interpreted-text role="guilabel"} option, which
    automatically estimates the time to complete this operation based on
    the last few operations. Choosing
    `Set duration manually`{.interpreted-text role="guilabel"} enables
    the `Default
    Duration`{.interpreted-text role="guilabel"} field instead.

-   `Default Duration`{.interpreted-text role="guilabel"}: estimated
    amount of time to complete the operation; used for [planning
    manufacturing orders](https://www.youtube.com/watch?v=TK55jIq00pc)
    and determining [work center
    availability](https://www.youtube.com/watch?v=3YwFlD97Bio).

-   `Company`{.interpreted-text role="guilabel"}: specify the company
    the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} is
    available in.

Include operation details in the `Work Sheet`{.interpreted-text
role="guilabel"} tab. Choose `PDF`{.interpreted-text role="guilabel"} to
attach a file or `Google Slide`{.interpreted-text role="guilabel"} with
*public* access to share a link. Select `Text`{.interpreted-text
role="guilabel"} to type instructions in the
`Description`{.interpreted-text role="guilabel"} text field.

::: {.tip}
::: {.title}
Tip
:::

Type [/]{.title-ref} for a list of formatting options and features,
including ChatGPT.

{.align-center}
:::

{.align-center}

Finally, click `Save \& Close`{.interpreted-text role="guilabel"} to
close the pop-up window. To add more operations, click
`Save & New`{.interpreted-text role="guilabel"} and repeat the same
steps above to configure another operation.

::: {.note}
::: {.title}
Note
:::

Each operation is unique, as it is always exclusively linked to one
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.
:::

::: {.tip}
::: {.title}
Tip
:::

After creating an operation, click the
`Copy Existing Operations`{.interpreted-text role="guilabel"} button to
choose an operation to duplicate.

{.align-center}
:::

#### Instructions

::: {.important}
::: {.title}
Important
:::

To add detailed instructions to operations, the *Quality* app must be
installed.
:::

Add specific instructions to an existing operation by clicking the
operation\'s `fa-list-ul`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon in the
`Instructions`{.interpreted-text role="guilabel"} column. The number in
the `Instructions`{.interpreted-text role="guilabel"} column shows the
number of existing detailed instructions there are for the operation.

{.align-center}

On the `Steps`{.interpreted-text role="guilabel"} dashboard, click
`New`{.interpreted-text role="guilabel"} to open a blank quality control
point form where the new manufacturing step can be created. Here, give
the specific instruction a `Title`{.interpreted-text role="guilabel"}
and set the `Type`{.interpreted-text role="guilabel"} to
`Instructions`{.interpreted-text role="guilabel"}. In the
`Instructions`{.interpreted-text role="guilabel"} tab of the form, write
out the directions for the step in the operation.

::: {.note}
::: {.title}
Note
:::

Further customizations can be made here on this form, beyond ordinary
instructions, to also include specific types of quality control points
that carry specific (or complex) conditions. For more details about
quality control points refer the `Instruction check
<../../quality/quality_check_types/instructions_check>`{.interpreted-text
role="doc"} documentation.
:::

{.align-center}

### Miscellaneous

The `Miscellaneous`{.interpreted-text role="guilabel"} tab contains more
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} configurations
to customize procurement, calculate costs, and define how components are
consumed.

::: {#manufacturing/basic_setup/manufacturing-readiness}
-   `Manufacturing Readiness`{.interpreted-text role="guilabel"}:
    choosing `When components for the 1st operation are
    available`{.interpreted-text role="guilabel"} shows the
    `Component Status`{.interpreted-text role="guilabel"} as a **green**
    `Not Available`{.interpreted-text role="guilabel"}, when only the
    components that are consumed in the first operation are in stock.
    This indicates that although not all components are available,
    operators can at least begin with the first operation. Choosing
    `When all components are available`{.interpreted-text
    role="guilabel"} displays a **red** `Not
    Available`{.interpreted-text role="guilabel"} component status
    unless all components are in available.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Specify which operation consumes each component on the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} in the
    `Manual Consumption
    field <manufacturing/basic_setup/consumed-in-operation>`{.interpreted-text
    role="ref"}.
    :::

    {.align-center}

-   `Version`{.interpreted-text role="guilabel"}: displays the current
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} version,
    visible with the Odoo *PLM* app installed for managing
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} changes.

-   `Flexible Consumption`{.interpreted-text role="guilabel"}: specifies
    if components used can deviate from the quantity defined on the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"}. Choose
    `Blocked`{.interpreted-text role="guilabel"} if operators **must**
    adhere strictly to the `BoM (Bill of Materials)`{.interpreted-text
    role="abbr"} quantity. Otherwise, choose `Allowed`{.interpreted-text
    role="guilabel"} or `Allowed with Warning`{.interpreted-text
    role="guilabel"}.

-   `Routing`{.interpreted-text role="guilabel"}: select the preferred
    warehouse\'s manufacturing operation type for products produced in
    multiple warehouses. If left blank, this warehouse\'s
    [Manufacturing]{.title-ref} operation type is used by default.

-   `Analytic Distribution`{.interpreted-text role="guilabel"}: select
    pre-created `analytic distribution models
    <../../../finance/accounting/reporting/analytic_accounting>`{.interpreted-text
    role="doc"} from the list to automatically record the cost of
    manufacturing products in the chosen journal.

-   `Manuf Lead Time`{.interpreted-text role="guilabel"}: define the
    number of days needed to complete a
    `MO (Manufacturing Order)`{.interpreted-text role="abbr"} from the
    date of confirmation.

-   `Days to prepare Manufacturing Order`{.interpreted-text
    role="guilabel"}: number of days needed to replenish components, or
    manufacture sub-assemblies of the product.
:::

::: {.seealso}
\-
`Analytic distribution <../../../finance/accounting/reporting/analytic_accounting>`{.interpreted-text
role="doc"} -
`Lead times <../../inventory/warehouses_storage/replenishment/lead_times>`{.interpreted-text
role="doc"}
:::

{.align-center}

Add by-products to BoMs
-----------------------

A *by-product* is a residual product that is created during production
in addition to the main product of a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. Unlike the
primary product, there can be more than one by-product on a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

To add by-products to a `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, first enable the *By-Products* feature in
`Manufacturing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Operations`{.interpreted-text
role="guilabel"} section, tick the checkbox for
`By-Products`{.interpreted-text role="guilabel"} to enable the feature.

{.align-center}

Once the feature is enabled, add by-products to a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} by clicking the
`By-products`{.interpreted-text role="guilabel"} tab. Click
`Add a line`{.interpreted-text role="guilabel"}, and fill in the
`By-product`{.interpreted-text role="guilabel"},
`Quantity`{.interpreted-text role="guilabel"}, and
`Unit of Measure`{.interpreted-text role="guilabel"}. Optionally,
specify a `Produced in Operation`{.interpreted-text role="guilabel"} for
the by-product.

::: {.example}
The by-product, [Mush]{.title-ref}, is created in the [Grind
grapes]{.title-ref} operation when producing [Red Wine]{.title-ref}.

{.align-center}
:::
