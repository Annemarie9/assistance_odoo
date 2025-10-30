# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration.md

show-content

:   

hide-page-toc

:   

Delivery methods
================

When activated in Odoo, the *Delivery Methods* setting adds the option
of calculating the cost of shipping on sales orders and e-commerce
shopping carts.

When integrated with a
`third-party carrier <inventory/shipping/third_party>`{.interpreted-text
role="ref"}, shipping prices are calculated based on the carrier\'s
pricing and packaging information.

::: {.seealso}
\-
`Third-party shipping carrier setup <inventory/shipping/third_party>`{.interpreted-text
role="ref"} - [Odoo Tutorials: Delivery
Prices](https://www.odoo.com/slides/slide/delivery-prices-613?fullscreen=1)
:::

Configuration
-------------

To calculate shipping on sales orders and e-commerce, the *Delivery
Costs* module must be installed. To do so, navigate to the
`Apps`{.interpreted-text role="menuselection"} application from the main
Odoo dashboard.

Then, remove the `Apps`{.interpreted-text role="guilabel"} filter, and
type in [Delivery Costs]{.title-ref} in the
`Search...`{.interpreted-text role="guilabel"} bar. After finding the
`Delivery Costs`{.interpreted-text role="guilabel"} module, click
`Activate`{.interpreted-text role="guilabel"} to install it.

{.align-center}

Add shipping method
-------------------

To configure delivery methods, go to
`Inventory app --> Configuration --> Shipping
Methods`{.interpreted-text role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

If the `Shipping Methods`{.interpreted-text role="guilabel"} option is
not available from the `Configuration`{.interpreted-text
role="guilabel"} drop-down menu, verify whether the feature is enabled
by following these steps:

1.  Go to
    `Inventory app --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.
2.  Scroll to the `Shipping`{.interpreted-text role="guilabel"} section
    and enable the `Delivery Methods`{.interpreted-text role="guilabel"}
    feature by checking the corresponding checkbox.

{.align-center}
:::

On the `Shipping Methods`{.interpreted-text role="guilabel"} page, add a
method by clicking `New`{.interpreted-text role="guilabel"}. Doing so
opens a form to provide details about the shipping provider, including:

-   `Shipping Method`{.interpreted-text role="guilabel"} (*Required
    field*): the name of the delivery method (e.g. [flat-rate
    shipping]{.title-ref}, [same day delivery]{.title-ref}, etc.).

-   `Provider`{.interpreted-text role="guilabel"} (*Required field*):
    choose the delivery service, like Fedex, if using a
    `third-party carrier <inventory/shipping/third_party>`{.interpreted-text
    role="ref"}. Ensure the integration with the shipping carrier is
    properly installed and select the provider from the drop-down menu.

    For more details on configuring custom shipping methods, such as
    `fixed price
    <inventory/shipping/fixed>`{.interpreted-text role="ref"},
    `based on rules <inventory/shipping/rules>`{.interpreted-text
    role="ref"}, or `pickup in
    store <inventory/shipping/pickup>`{.interpreted-text role="ref"}
    options, refer to their respective sections below.

-   `Website`{.interpreted-text role="guilabel"}: configure shipping
    methods for an e-commerce page. Select the applicable website from
    the drop-down menu, or leave it blank to apply the method to all web
    pages.

-   `Company`{.interpreted-text role="guilabel"}: If the shipping method
    should apply to a specific company, select it from the drop-down
    menu. Leave the field blank to apply the method to all companies.

-   `Routes`{.interpreted-text role="guilabel"}: select the applicable
    route(s) to define different delivery methods, such as standard or
    express shipping, based on varying lead times. For more information,
    jump to the
    `Set routes on shipping method <inventory/shipping_receiving/shipping-route>`{.interpreted-text
    role="ref"} section.

::: {#inventory/shipping_receiving/delivery-product}
-   `Delivery Product`{.interpreted-text role="guilabel"} (*Required
    field*): the product listed on the `sales order line
    <inventory/shipping/sales-order>`{.interpreted-text role="ref"} as
    the delivery charge.
-   `Free if order amount is above`{.interpreted-text role="guilabel"}:
    checking this box enables free shipping if the customer spends above
    the specified amount.
:::

For examples on how to configure specific shipping methods, refer to the
sections below.

### Fixed price {#inventory/shipping/fixed}

To configure a shipping price that is the same for all orders, go to
`Inventory app
--> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}. Then, click `New`{.interpreted-text
role="guilabel"}, and on the shipping method form, set the
`Provider`{.interpreted-text role="guilabel"} to the
`Fixed Price`{.interpreted-text role="guilabel"} option. Selecting this
option makes the `Fixed Price`{.interpreted-text role="guilabel"} field
become available, which is where the fixed rate shipping amount is
defined.

To enable free shipping if the amount of the order exceeds a specified
amount, check the box `Free if order amount is above`{.interpreted-text
role="guilabel"} and fill in the amount.

::: {.example}
To set up [\$20]{.title-ref} flat-rate shipping that becomes free if the
customer spends over [\$100]{.title-ref}, fill in the following fields:

-   `Shipping Method`{.interpreted-text role="guilabel"}: [Flat-rate
    shipping]{.title-ref}
-   `Provider`{.interpreted-text role="guilabel"}:
    `Fixed Price`{.interpreted-text role="guilabel"}
-   `Fixed Price`{.interpreted-text role="guilabel"}:
    [\$20.00]{.title-ref}
-   `Free if order amount is above`{.interpreted-text role="guilabel"}:
    [\$100.00]{.title-ref}
-   `Delivery Product`{.interpreted-text role="guilabel"}: [\[SHIP\]
    Flat]{.title-ref}

{.align-center}
:::

### Based on rules {#inventory/shipping/rules}

To calculate the price of shipping based on pricing rules, set the
`Provider`{.interpreted-text role="guilabel"} field to the
`Based on Rules`{.interpreted-text role="guilabel"} option. Optionally,
adjust `Margin on Rate`{.interpreted-text role="guilabel"} and
`Additional margin`{.interpreted-text role="guilabel"} to include
additional shipping costs.

#### Create pricing rules

Navigate to the `Pricing`{.interpreted-text role="guilabel"} tab and
click `Add a line`{.interpreted-text role="guilabel"}. Doing so opens
the `Create Pricing Rules`{.interpreted-text role="guilabel"} window,
where the `Condition`{.interpreted-text role="guilabel"} related to the
product weight, volume, price, or quantity is compared to a defined
amount to calculate the `Delivery Cost`{.interpreted-text
role="guilabel"}.

Once finished, click either `Save & New`{.interpreted-text
role="guilabel"} to add another rule, or
`Save & Close`{.interpreted-text role="guilabel"}.

::: {.example}
To charge customers \$20 in shipping for orders with five or fewer
products, set the `Condition`{.interpreted-text role="guilabel"} to
[Quantity \<= 5.00]{.title-ref}, and the
`Delivery Cost`{.interpreted-text role="guilabel"} to
[\$20]{.title-ref}.

{.align-center}
:::

To restrict shipping to specific destinations on the eCommerce website,
in the shipping method form, navigate to the
`Destination Availability`{.interpreted-text role="guilabel"} tab and
define the `Countries`{.interpreted-text role="guilabel"},
`States`{.interpreted-text role="guilabel"}, and
`Zip Prefixes`{.interpreted-text role="guilabel"}. Leave these fields
empty if all locations apply.

#### Calculate delivery cost

Shipping cost is the `Delivery cost`{.interpreted-text role="guilabel"}
specified in the rule that satisfies the `Condition`{.interpreted-text
role="guilabel"}, plus any extra charges from the
`Margin on rate`{.interpreted-text role="guilabel"} and
`Additional margin`{.interpreted-text role="guilabel"}.

$$Total = Rule's~Delivery~Cost + (Margin~on~rate \times Rule's~Delivery~Cost) + Additional~margin$$

::: {.example}
With the two following rules set up:

1.  If the order contains five or fewer products, shipping is \$20
2.  If the order contains more than five products, shipping is \$50.

`Margin on Rate`{.interpreted-text role="guilabel"} is [10%]{.title-ref}
and `Additional margin`{.interpreted-text role="guilabel"} is
[\$9.00]{.title-ref}.

{.align-center}

When the first rule is applied, the delivery cost is \$31 (20 + (0.1 \*
20) + 9). When the second rule is applied, the delivery cost is \$64 (50
+ (0.1 \* 50) + 9).
:::

### Pickup in store {#inventory/shipping/pickup}

To configure in-store pickup, select `Pickup in store`{.interpreted-text
role="guilabel"} in the `Provider`{.interpreted-text role="guilabel"}
field and specify the pickup location in `Warehouse`{.interpreted-text
role="guilabel"}.

To invoice the customer for the shipping cost to the pickup location,
choose the `Get Rate
and Create Shipment`{.interpreted-text role="guilabel"} option in the
`Integration Level`{.interpreted-text role="guilabel"} field. Then, pick
either the `Estimated cost`{.interpreted-text role="guilabel"} or
`Real cost`{.interpreted-text role="guilabel"} radio options in the
`Invoicing
Policy`{.interpreted-text role="guilabel"} field to decide whether the
added shipping charge on the sales order is the precise cost from the
shipping carrier.

::: {.seealso}
`Invoice cost of shipping <setup_configuration/invoicing>`{.interpreted-text
role="doc"}
:::

### Route on shipping method {#inventory/shipping_receiving/shipping-route}

Optionally, set different warehouse delivery processes for a shipping
method by configuring different
`routes <daily_operations/use_routes>`{.interpreted-text role="doc"} for
it.

::: {.example}
Configuring multiple routes per shipping method is helpful for adjusting
warehouse delivery processes based on:

-   speed (e.g., use
    `one-step delivery <daily_operations/receipts_delivery_one_step>`{.interpreted-text
    role="doc"} for express shipping, or
    `two-step <daily_operations/receipts_delivery_two_steps>`{.interpreted-text
    role="doc"} for standard shipping).
-   international shipping (e.g. use `three-step delivery
    <daily_operations/delivery_three_steps>`{.interpreted-text
    role="doc"} to prepare documents for customs)
-   in-store pickup or home delivery: ship from the central warehouse,
    or pick from the store\'s stock, depending on customer selection.
:::

To set up routes, go to
`Inventory app --> Configuration --> Routes`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"},
or select the desired route.

On the route form, in the `Applicable On`{.interpreted-text
role="guilabel"} section, tick the `Shipping Methods`{.interpreted-text
role="guilabel"} checkbox.

![Routes form with the Shipping Methods checkbox
ticked.](setup_configuration/shipping-route.png){.align-center}

Then, go to
`Inventory app --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}, and select the desired shipping method.

On the shipping method form, in the `Routes`{.interpreted-text
role="guilabel"} field, select the available fulfillment routes from the
drop-down menu.

::: {.note}
::: {.title}
Note
:::

If the desired route is not selectable, check that the *Shipping
Methods* option is enabled in the route\'s *Applicable On* section.
:::

![By default, most shipping methods are created with two routes
available for standard or express
delivery.](setup_configuration/set-routes.png){.align-center}

Add shipping {#inventory/shipping/sales-order}
------------

Shipping methods can be added to sales orders in the form of delivery
products, which appear as individual line items. First, navigate to the
desired sales order by going to `Sales
app --> Orders --> Orders`{.interpreted-text role="menuselection"}.

On the sales order, click the `Add shipping`{.interpreted-text
role="guilabel"} button, which opens the `Add a
shipping method`{.interpreted-text role="guilabel"} pop-up window. Then,
choose a `Shipping Method`{.interpreted-text role="guilabel"} from the
list.

The `Total Order Weight`{.interpreted-text role="guilabel"} is
pre-filled based on product weights (that are defined in the
`Inventory`{.interpreted-text role="guilabel"} tab for each product
form). Edit the field to specify the exact weight, and then click
`Add`{.interpreted-text role="guilabel"} to add the shipping method.

::: {.note}
::: {.title}
Note
:::

The amount defined in `Total Order Weight`{.interpreted-text
role="guilabel"} overwrites the total product weights defined on the
product form.
:::

The shipping cost is added to the *sales order line* as the
`Delivery Product`{.interpreted-text role="guilabel"} detailed on the
shipping method form.

::: {.example}
[Furniture Delivery]{.title-ref}, a delivery product with a fixed rate
of [\$200]{.title-ref}, is added to sales order [S00088]{.title-ref}.

{.align-center}
:::

### Delivery order

The shipping method added to the sales order is linked to the shipping
carrier details on the delivery order. To add or change the delivery
method on the delivery itself, go to the
`Additional Info`{.interpreted-text role="guilabel"} tab and modify the
`Carrier`{.interpreted-text role="guilabel"} field.

{.align-center}

::: {.toctree titlesonly=""}
setup\_configuration/third\_party\_shipper setup\_configuration/labels
setup\_configuration/bpost setup\_configuration/dhl\_credentials
setup\_configuration/fedex setup\_configuration/sendcloud\_shipping
setup\_configuration/starshipit\_shipping
setup\_configuration/ups\_credentials setup\_configuration/zebra
setup\_configuration/cancel setup\_configuration/invoicing
setup\_configuration/label\_type setup\_configuration/multipack
setup\_configuration/print\_on\_validation
:::
