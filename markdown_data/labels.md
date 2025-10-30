# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels.md

Print shipping labels
=====================

Integrate Odoo with `third-party shipping carriers
<../setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"} to automatically generate shipping labels that includes
prices, destination addresses, tracking numbers, and barcodes.

::: {.seealso}
`Automatically print shipping carrier labels <inventory/shipping_receiving/carrier-labels>`{.interpreted-text
role="ref"}
:::

Configuration
-------------

To generate labels for a third-party shipping carrier, first
`install the third-party shipping
connector <../setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"}. Then, configure and activate the
`delivery method <inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"}, being sure to set the `Integration Level`{.interpreted-text
role="guilabel"} to `Get Rate and Create Shipment`{.interpreted-text
role="guilabel"} to generate shipping labels. Finally, provide the
company\'s `source address
<inventory/shipping_receiving/configure-source-address>`{.interpreted-text
role="ref"} and `product weights
<inventory/shipping_receiving/configure-weight>`{.interpreted-text
role="ref"}.

::: {.seealso}
`../setup_configuration/third_party_shipper`{.interpreted-text
role="doc"}
:::

{.align-center}

### Labels for multi-step {#inventory/shipping_receiving/picking-config}

For companies using
`two <../daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"} or `three step
delivery <../daily_operations/delivery_three_steps>`{.interpreted-text
role="doc"}, labels can be triggered to print after validating the
picking or packing operation. To do that, go to `Inventory app -->
Configuration --> Operations Types`{.interpreted-text
role="menuselection"}, and choose the desired operation.

On the `Operation Type`{.interpreted-text role="guilabel"} configuration
page, tick the `Print Label`{.interpreted-text role="guilabel"}
checkbox. Enabling this feature ensures that the third-party shipping
label is printed upon validating this operation.

::: {.example}
For
`two-step delivery <../daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"}, where products are placed directly in packages during
picking, companies can print shipping labels during picking instead of
delivery. Odoo allows users to enable the
`Print Label`{.interpreted-text role="guilabel"} feature on the
[Pick]{.title-ref} operation itself to achieve this flexibility.

{.align-center}
:::

Print tracking labels
---------------------

Tracking labels are printed when specific operations are validated. By
default, validating a delivery order (DO) generates a tracking label in
the chatter.

::: {.note}
::: {.title}
Note
:::

For companies using two or three step delivery, refer to the
`printing labels for multi-step
delivery <inventory/shipping_receiving/picking-config>`{.interpreted-text
role="ref"} section to learn how to print the label after validating a
picking or packing operation.
:::

When both the *Sales* and *Inventory* apps are installed, begin in the
`Sales`{.interpreted-text role="menuselection"} app, and proceed to the
desired quotation or sales order (SO). There, and `add the shipping cost
<inventory/shipping_receiving/add-shipping-quote>`{.interpreted-text
role="ref"} to the order. Then, navigate to the linked
`DO (Delivery Order)`{.interpreted-text role="abbr"} --- or another
operation type when using multi-step delivery --- to validate the
operation and print the label.

If only the *Inventory* app is installed, create
`DOs (Delivery Orders)`{.interpreted-text role="abbr"} directly in the
`Inventory`{.interpreted-text role="menuselection"} app,
`add the third-party carrier
<inventory/shipping_receiving/validate-print-label>`{.interpreted-text
role="ref"} in the `Carrier`{.interpreted-text role="guilabel"} field,
and validate the `DO (Delivery Order)`{.interpreted-text role="abbr"}.

### Add shipping on quotation {#inventory/shipping_receiving/add-shipping-quote}

To generate a tracking label for an order, begin by creating a quotation
in `Sales
app --> Orders --> Quotations`{.interpreted-text role="menuselection"},
clicking `New`{.interpreted-text role="guilabel"}, and filling out the
quotation form. Then, click the `Add Shipping`{.interpreted-text
role="guilabel"} button in the bottom-right corner of the quotation.

{.align-center}

In the resulting pop-up window, select the intended carrier from the
`Shipping Method`{.interpreted-text role="guilabel"} drop-down menu. The
`Total Order Weight`{.interpreted-text role="guilabel"} field is
automatically populated, based on the
`weight of products in the order <inventory/shipping_receiving/configure-weight>`{.interpreted-text
role="ref"}. Modify this field to overwrite the predicted weight, and
use this weight to estimate the cost of shipping.

Next, click `Get Rate`{.interpreted-text role="guilabel"} to display the
shipping cost for the customer, via the third-party carrier in the
`Cost`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

If clicking `Get Rate`{.interpreted-text role="guilabel"} results in an
error, ensure the `warehouse's address
<inventory/shipping_receiving/configure-source-address>`{.interpreted-text
role="ref"} and `weight of products in the
order <inventory/shipping_receiving/configure-weight>`{.interpreted-text
role="ref"} are properly configured.
:::

Click `Add`{.interpreted-text role="guilabel"} to add the cost to the
quotation, which is listed as the `configured
delivery product <inventory/shipping_receiving/delivery-product>`{.interpreted-text
role="ref"}. Finally, click `Confirm`{.interpreted-text role="guilabel"}
on the quotation, and click the `Delivery`{.interpreted-text
role="guilabel"} smart button to access the
`DO (Delivery Order)`{.interpreted-text role="abbr"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For users who do not have the *Sales* app installed, specify the
`Carrier`{.interpreted-text role="guilabel"} by going to the
`Inventory`{.interpreted-text role="menuselection"} app, navigating to
the `DO (Delivery Order)`{.interpreted-text role="abbr"}, and going to
the `Additional Info`{.interpreted-text role="guilabel"} tab.

{.align-center}
:::

### Validate delivery order {#inventory/shipping_receiving/validate-print-label}

On a delivery order form, navigate to the
`Additional Info`{.interpreted-text role="guilabel"} tab to ensure the
third-party shipping carrier has been added to the
`Carrier`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

If the *Sales* app is not installed, the third-party carrier is set in
the `Carrier`{.interpreted-text role="guilabel"} field.
:::

After the items in the order have been packed, click
`Validate`{.interpreted-text role="guilabel"} to get the shipping
carrier\'s tracking number, and generate the shipping label.

::: {.note}
::: {.title}
Note
:::

Create or select an existing delivery order by going to the
`Inventory`{.interpreted-text role="menuselection"} app, and selecting
the `Delivery Orders`{.interpreted-text role="guilabel"} card.
:::

The `Tracking Reference`{.interpreted-text role="guilabel"} number is
generated in the `Additional Info`{.interpreted-text role="guilabel"}
tab of the delivery order. Click the `Tracking`{.interpreted-text
role="guilabel"} smart button to access the tracking link from the
shipping carrier\'s website.

The tracking label is found in PDF format in the chatter.

{.align-center}

::: {.note}
::: {.title}
Note
:::

For multi-package shipping, one label is generated per package. Each
label appears in the chatter.
:::

![Sample label generated from Odoo\'s shipping connector with
FedEx.](labels/sample-label.png){.align-center}

::: {.seealso}
\- `invoicing`{.interpreted-text role="doc"} -
`multipack`{.interpreted-text role="doc"}
:::
