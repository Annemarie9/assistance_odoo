Product variants
================

Product variants are used to give single products a variety of different
characteristics and options for customers to choose from, such as size,
style, or color, just to name a few.

Products variants can be managed via their individual product template,
or by navigating to either the `Product Variants`{.interpreted-text
role="guilabel"} or `Attributes`{.interpreted-text role="guilabel"}
page. All of these options are located within the Odoo *Sales*
application.

::: {.example}
An apparel company has the following variant breakdown for one their
best-selling t-shirts:

-   Unisex Classic Tee
    -   Color: Blue, Red, White, Black
    -   Size: S, M, L, XL, XXL

Here, the **T-shirt** is the product template, and **T-shirt: Blue, S**
is a specific product variant.

**Color** and **Size** are *attributes*, and the corresponding options
(like **Blue** and **S**) are *values*.

In this instance, there is a total of twenty different product variants:
four **Color** options multiplied by five **Size** options. Each variant
has its own inventory count, sales totals, and other similar records in
Odoo.
:::

::: {.seealso}
`ecommerce/products/product-variants`{.interpreted-text role="ref"}
:::

Configuration
-------------

To use product variants, the *Variants* setting **must** be activated in
the Odoo *Sales* application.

To do that, go to
`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and locate the
`Product Catalog`{.interpreted-text role="guilabel"} section at the top
of the page.

In that section, check the box to enable the
`Variants`{.interpreted-text role="guilabel"} feature.

{.align-center}

Then, click `Save`{.interpreted-text role="guilabel"} at the top of the
`Settings`{.interpreted-text role="guilabel"} page.

Attributes
----------

Before product variants can be set up, attributes **must** be created.
To create, manage, and modify attributes, navigate to
`Sales app --> Configuration --> Attributes`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

The order of attributes on the `Attributes`{.interpreted-text
role="guilabel"} page dictates how they appear on the *Product
Configurator*, *Point of Sale* dashboard, and *eCommerce* pages.
:::

To create a new attribute from the `Attributes`{.interpreted-text
role="guilabel"} page, click `New`{.interpreted-text role="guilabel"}.
Doing so reveals a blank attributes form that can be customized and
configured in a number of ways.

{.align-center}

First, create an `Attribute Name`{.interpreted-text role="guilabel"},
such as [Color]{.title-ref} or [Size]{.title-ref}.

Next, select one of the options from the
`Display Type`{.interpreted-text role="guilabel"} field. The `Display
Type`{.interpreted-text role="guilabel"} determines how this product is
shown on the online store, *Point of Sale* dashboard, and *Product
Configurator*.

The `Display Type`{.interpreted-text role="guilabel"} options are:

-   `Pills`{.interpreted-text role="guilabel"}: options appear as
    selectable buttons on the product page of the online store.
-   `Color`{.interpreted-text role="guilabel"}: options appear as small,
    colored squares, which reflect any HTML color codes
-   `Radio`{.interpreted-text role="guilabel"}: options appear in a
    bullet-style list on the product page of the online store.
-   `Select`{.interpreted-text role="guilabel"}: options appear in a
    drop-down menu on the product page of the online store. set, on the
    product page of the online store.
-   `Multi-checkbox (option)`{.interpreted-text role="guilabel"}:
    options appear as selectable checkboxes on the product page of the
    online store.

{.align-center}

The `Variant Creation Mode`{.interpreted-text role="guilabel"} field
informs Odoo when to automatically create a new variant once an
attribute is added to a product.

::: {.note}
::: {.title}
Note
:::

The `Variant Creation Mode`{.interpreted-text role="guilabel"} field
**must** be set to `Never (option)`{.interpreted-text role="guilabel"}
in order for the `Multi-checkbox (option)`{.interpreted-text
role="guilabel"} to work properly as the `Display
Type`{.interpreted-text role="guilabel"}.
:::

-   `Instantly`{.interpreted-text role="guilabel"}: creates all possible
    variants as soon as attributes and values are added to a product
    template.
-   `Dynamically`{.interpreted-text role="guilabel"}: creates variants
    **only** when corresponding attributes and values are added to a
    sales order.
-   `Never (option)`{.interpreted-text role="guilabel"}: never
    automatically creates variants.

::: {.warning}
::: {.title}
Warning
:::

Once added to a product, an attribute\'s
`Variants Creation Mode`{.interpreted-text role="guilabel"} cannot be
edited.
:::

The `eCommerce Filter Visibility`{.interpreted-text role="guilabel"}
field determines whether or not these attribute options are visible to
the customer on the front-end, as they shop on the online store.

-   `Visible`{.interpreted-text role="guilabel"}: the attribute values
    are visible to customers on the front-end.
-   `Hidden`{.interpreted-text role="guilabel"}: the attribute values
    are hidden from customers on the front-end.

Lastly, in the optional `eCommerce Category`{.interpreted-text
role="guilabel"} field, select a category from a drop-down menu to group
similar attributes under the same section for added specificity and
organization.

::: {.note}
::: {.title}
Note
:::

To view the details related to the attribute category selected, click
the internal link `fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon to the far-right
of the `eCommerce Category`{.interpreted-text role="guilabel"} field,
once an option has been selected. Doing so reveals that attribute
category\'s detail form.

{.align-center}

Here, the `Category Name`{.interpreted-text role="guilabel"} and
`Sequence`{.interpreted-text role="guilabel"} is displayed at the top.
Followed by `Related Attributes`{.interpreted-text role="guilabel"}
associated with the category. These attributes can be
dragged-and-dropped into a desirable order of priority.

Attributes can be directly added to the category, as well, by clicking
`Add a line`{.interpreted-text role="guilabel"}.
:::

::: {.tip}
::: {.title}
Tip
:::

To create an attribute category directly from this field, start typing
the name of the new category, then select either
`Create`{.interpreted-text role="guilabel"} or
`Create and edit...`{.interpreted-text role="guilabel"} from the
drop-down menu that appears.

Clicking `Create`{.interpreted-text role="guilabel"} creates the
category, which can be modified later. Clicking
`Create and edit...`{.interpreted-text role="guilabel"} creates the
category and reveals a `Create Category`{.interpreted-text
role="guilabel"} pop-up window, in which the new attribute category can
be configured and customized.
:::

### Attribute values

Attribute values should be added to the
`Attribute Values`{.interpreted-text role="guilabel"} tab. Values can be
added to an attribute at any time, if needed.

To add a value, click `Add a line`{.interpreted-text role="guilabel"} in
the `Attribute Values`{.interpreted-text role="guilabel"} tab.

Then, enter the name of the value in the `Value`{.interpreted-text
role="guilabel"} column. Next, check the box in the
`Is custom value`{.interpreted-text role="guilabel"} column, if the
value is custom (i.e. the customer gets to provide unique specifications
that are specific to this particular value).

#### Colors

Next to `Display Type`{.interpreted-text role="guilabel"}, select the
`Color`{.interpreted-text role="guilabel"} option. Go to the
`Attribute Values`{.interpreted-text role="guilabel"} tab to modify the
value settings.



To choose a color, click the blank circle in the
`Color`{.interpreted-text role="guilabel"} column, which reveals an HTML
color selector pop-up window.



In this pop-up window, select a specific color by dragging the color
slider to a particular hue, and clicking on the color portion directly
on the color gradient window.

Or, choose a specific color by clicking the *dropper* icon, and
selecting a desired color that\'s currently clickable on the screen.

If you sell products with specific patterns, you can also add an image
to display the pattern of the product. To do so, click the
`fa-camera`{.interpreted-text role="icon"} `(camera)`{.interpreted-text
role="guilabel"} icon, then click the `fa-pencil`{.interpreted-text
role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon and
select an image from your local drive. This pattern will appear as a
color option on the ecommerce product page.



::: {.tip}
::: {.title}
Tip
:::

Attributes can also be created directly from the product template by
adding a new line and typing the name into the
`Variants`{.interpreted-text role="guilabel"} tab.
:::

Once an attribute is added to a product, that product is listed and
accessible, via the attribute\'s `Related Products`{.interpreted-text
role="guilabel"} smart button. That button lists every product in the
database currently using that attribute.

Product variants
----------------

Once an attribute is created, use the attribute (and its values) to
create a product variant. To do that, go to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select an existing product to view that
desired product\'s form. Or, click `Create`{.interpreted-text
role="guilabel"} to create a new product, to which a product variant can
be added.

On the product form, click the
`Attributes \& Variants`{.interpreted-text role="guilabel"} tab to view,
manage, and modify attributes and values for the product.

{.align-center}

To add an attribute to a product, and subsequent attribute values, click
`Add a line`{.interpreted-text role="guilabel"} in the
`Attributes \& Variants`{.interpreted-text role="guilabel"} tab. Then,
choose the desired attribute from the drop-down menu that appears.

::: {.tip}
::: {.title}
Tip
:::

Attributes can be created directly from the
`Attributes \& Variants`{.interpreted-text role="guilabel"} tab of a
product form. To do that, start typing the name of the new attribute in
the blank field, and select either `Create`{.interpreted-text
role="guilabel"} or `Create and edit...`{.interpreted-text
role="guilabel"} from the mini drop-down menu that appears.

Clicking `Create`{.interpreted-text role="guilabel"} creates the
attribute, which can be customized later. Clicking
`Create and edit...`{.interpreted-text role="guilabel"} creates the
attribute, and a `Create Attribute`{.interpreted-text role="guilabel"}
pop-up form appears. In the pop-up form, proceed to modify the attribute
in a number of ways.
:::

Once an attribute is selected in the `Attribute`{.interpreted-text
role="guilabel"} column, proceed to select the specific attribute values
to apply to the product, via the drop-down menu available in the
`Values`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

There is no limit to how many values can be added.
:::

::: {.tip}
::: {.title}
Tip
:::

Similar product variant creation processes are accessible through the
Purchase, Inventory, and eCommerce applications.
:::

### Configure variants

To the far-right of the attribute line is a
`Configure`{.interpreted-text role="guilabel"} button. When clicked,
Odoo reveals a separate page showcasing those specific
`Product Variant Values`{.interpreted-text role="guilabel"}.

{.align-center}

Here, the specific `Value`{.interpreted-text role="guilabel"} name,
`HTML Color Index`{.interpreted-text role="guilabel"} (if applicable),
and `Value Price Extra`{.interpreted-text role="guilabel"} are viewable.

::: {.note}
::: {.title}
Note
:::

The `Value Price Extra`{.interpreted-text role="guilabel"} represents
the increase in the sales price if the attribute is selected.
:::

When a value is clicked on the
`Product Variant Values`{.interpreted-text role="guilabel"} page, Odoo
reveals a separate page, detailing that value\'s related details.

{.align-center}

On the specific product variant detail page, the
`Value`{.interpreted-text role="guilabel"} and
`Value Price Extra`{.interpreted-text role="guilabel"} fields can be
found, along with an `Exclude for`{.interpreted-text role="guilabel"}
field.

In the `Exclude for`{.interpreted-text role="guilabel"} field, different
`Product Templates`{.interpreted-text role="guilabel"} and specific
`Attribute Values`{.interpreted-text role="guilabel"} can be added. When
added, this specific attribute value will be excluded from those
specific products.

### Variants smart button

When a product has attributes and variants configured in its
`Attributes \& Variants`{.interpreted-text role="guilabel"} tab, a
`Variants`{.interpreted-text role="guilabel"} smart button appears at
the top of the product form. The `Variants`{.interpreted-text
role="guilabel"} smart button indicates how many variants are currently
configured for that specific product.

{.align-center}

When the `Variants`{.interpreted-text role="guilabel"} smart button is
clicked, Odoo reveals a separate page showcasing all the specific
product variant combinations configured for that specific product.

{.align-center}

Impact of variants
------------------

In addition to offering more detailed product options to customers,
product variants have their own impacts that can be taken advantage of
throughout the Odoo database.

-   `Barcode`{.interpreted-text role="guilabel"}: barcodes are
    associated with each variant, instead of the product template. Each
    individual variant can have its own unique barcode/SKU.

-   `Price`{.interpreted-text role="guilabel"}: every product variant
    has its own public price, which is the sum of the product template
    price *and* any extra charges for particular attributes.

    ::: {.example}
    A red shirt\'s sales price is \$23 \-- because the shirt\'s template
    price is \$20, plus an additional \$3 for the red color variant.
    Pricelist rules can be configured to apply to the product template,
    or to the variant.
    :::

-   `Inventory`{.interpreted-text role="guilabel"}: inventory is counted
    for each individual product variant. On the product template form,
    the inventory reflects the sum of all variants, but the actual
    inventory is computed by individual variants.

-   `Picture`{.interpreted-text role="guilabel"}: each product variant
    can have its own specific picture.

::: {.note}
::: {.title}
Note
:::

Changes to the product template automatically apply to every variant of
that product.
:::

::: {.seealso}
`import`{.interpreted-text role="doc"}
:::
