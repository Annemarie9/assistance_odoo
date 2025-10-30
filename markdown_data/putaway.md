# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/putaway.md

Putaway rules
=============

Putaway is the process of routing products to appropriate storage
locations upon shipment arrival.

Odoo can accomplish this seamlessly using *putaway rules*, which dictate
how products move through specified warehouse locations.

Upon shipment arrival, operations are generated based on putaway rules
to efficiently move products to specified locations, and ensure easy
retrieval for future delivery orders.

In warehouses that process specific kinds of products, putaway rules can
also prevent volatile substances from being stored in close proximity,
by directing them to different locations determined by the warehouse
manager.

::: {.seealso}
[Odoo Tutorials: Putaway
Rules](https://www.youtube.com/watch?v=nCQMf6sj_w8)
:::

Configuration
-------------

To use putaway rules, navigate to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and activate the
`Multi-Step Routes`{.interpreted-text role="guilabel"} feature under the
`Warehouse`{.interpreted-text role="guilabel"} section. By doing so, the
`Storage Locations`{.interpreted-text role="guilabel"} feature is also
automatically activated.

Finally, click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

### Define putaway rule {#inventory/routes/putaway-rule}

To manage where specific products are routed for storage, navigate to
`Inventory app
--> Configuration --> Putaway Rules`{.interpreted-text
role="menuselection"}. Use the `Create`{.interpreted-text
role="guilabel"} button to configure a new putaway rule on a
`Product`{.interpreted-text role="guilabel"} or
`Product Category`{.interpreted-text role="guilabel"} that the rule
affects.

::: {.important}
::: {.title}
Important
:::

Putaway rules can be defined either per product/product category, and/or
package type (the *Packages* setting must be enabled in
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"} for that).
:::

In the same line, the `When product arrives in`{.interpreted-text
role="guilabel"} location is where the putaway rule is triggered to
create an operation to move the product to the
`Store to`{.interpreted-text role="guilabel"} location.

For this to work, the `Store to`{.interpreted-text role="guilabel"}
location must be a *sub-location* of the first (e.g.,
[WH/Stock/Fruits]{.title-ref} is a specific, named location inside
[WH/Stock]{.title-ref} to make the products stored here easier to find).

::: {.example}
In a warehouse location, **WH/Stock**, there are the following
sub-locations:

-   WH/Stock/Fruits
-   WH/Stock/Vegetables

Ensure all apples are stored in the fruits section by filling the field
`Store to`{.interpreted-text role="guilabel"} with the location
[WH/Stock/Fruits]{.title-ref} when the `Product`{.interpreted-text
role="guilabel"}, [Apple]{.title-ref} arrives in [WH/Stock]{.title-ref}.

Repeat this for all products and hit `Save`{.interpreted-text
role="guilabel"}.

{.align-center}
:::

### Putaway rule priority

Odoo selects a putaway rule based on the following priority list (from
highest to lowest) until a match is found:

1.  Package type and product
2.  Package type and product category
3.  Package type
4.  Product
5.  Product category

::: {.example}
The product [Lemonade can]{.title-ref} has the following putaway rules
configured:

1.  When receiving a [Pallet]{.title-ref}
    (`Package Type`{.interpreted-text role="guilabel"}) of [Lemonade
    cans]{.title-ref}, it is redirected to
    [WH/Stock/Pallets/PAL1]{.title-ref}.
2.  [Lemonade can]{.title-ref}\'s `Product Category`{.interpreted-text
    role="guilabel"} is [All/drinks]{.title-ref}, and when receiving a
    [Box]{.title-ref} of any item in this product category, items are
    redirected to [WH/Stock/Shelf 1]{.title-ref}.
3.  Any product on a [Pallet]{.title-ref} is redirected to
    [WH/Stock/Pallets]{.title-ref}
4.  The product [Lemonade can]{.title-ref} is redirected to
    [WH/Stock/Shelf 2]{.title-ref}
5.  Items in the [All/drinks]{.title-ref} product category are
    redirected to [WH/Stock/Small Refrigerator]{.title-ref}.

{.align-center}
:::
