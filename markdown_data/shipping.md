# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/shipping.md

Shipping
========

Odoo eCommerce allows you to configure various shipping methods,
enabling customers to choose their preferred option at checkout. These
methods include `external providers
<ecommerce/shipping/external-provider>`{.interpreted-text role="ref"},
`custom options <ecommerce/shipping/custom-method>`{.interpreted-text
role="ref"} such as flat-rate or free shipping, local carriers via
`Sendcloud </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping>`{.interpreted-text
role="doc"} or
`Based on Rules <inventory/shipping/rules>`{.interpreted-text
role="ref"}, and `in-store pickup
<ecommerce/shipping/instore-pickup>`{.interpreted-text role="ref"}.

External provider integration {#ecommerce/shipping/external-provider}
-----------------------------

To handle product delivery, you can connect your database to
`third-party shipping carriers
</applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"} like
`FedEx </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/fedex>`{.interpreted-text
role="doc"},
`UPS </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials>`{.interpreted-text
role="doc"}, or
`DHL </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials>`{.interpreted-text
role="doc"}. A shipping connector links to these providers, automating
`tracking labels
</applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels>`{.interpreted-text
role="doc"} and shipping processes.

To enable a third-party shipping provider, go to
`Website --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, scroll to the
`Shipping`{.interpreted-text role="guilabel"} section, select the
desired shipping provider(s), and `Save`{.interpreted-text
role="guilabel"}.

Go to `Website --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"} and select the shipping method in the list to
`configure it <inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"}.

::: {.seealso}
`Third-party shipping carriers
</applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper>`{.interpreted-text
role="doc"}
:::

::: {.important}
::: {.title}
Important
:::

The field used to define additional fees **must** be filled **in your
third-party shipping provider account**, even if you do not plan to
charge customers any additional fee. If you do not want to apply a fee,
enter [0]{.title-ref}. If the field is left empty, the delivery price
cannot be calculated, and an error message prompts the customer to
select an alternative shipping method.
:::

### Margin on delivery rate

To add an additional fee to the base shipping rate (e.g., to cover extra
costs), log into your carrier account and set the desired fee in the
related field. The shipping connector retrieves this fee and includes it
in the final price at checkout. Contact your carrier for further
assistance with this configuration.

Alternatively, enter [0]{.title-ref} in your third-party shipping
provider account, then set the fee in Odoo. To do so, access the desired
`shipping method's form
<inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"} and enter the fee in the `Margin
on Rate`{.interpreted-text role="guilabel"} field to add a percentage to
the shipping costs and/or the `Additional margin`{.interpreted-text
role="guilabel"} field to add a fixed amount.

::: {.important}
::: {.title}
Important
:::

The field used to define additional fees cannot be left empty in your
third-party shipping provider account.
:::

Custom shipping method {#ecommerce/shipping/custom-method}
----------------------

Custom shipping methods must be created, for example:

-   to integrate shipping carriers through `Sendcloud
    </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping>`{.interpreted-text
    role="doc"};
-   to configure specific rules (e.g., to offer free shipping for orders
    above a specific amount) for a specific provider;
-   to configure
    `Fixed Price <inventory/shipping/fixed>`{.interpreted-text
    role="ref"} shipping or shipping
    `Based on Rules <inventory/shipping/rules>`{.interpreted-text
    role="ref"}.

To create a custom shipping method, go to `Website --> Configuration -->
Shipping Methods`{.interpreted-text role="menuselection"}, click
`New`{.interpreted-text role="guilabel"} and fill in the `fields
<inventory/shipping_receiving/shipping-methods-details>`{.interpreted-text
role="ref"}.

In the `Provider`{.interpreted-text role="guilabel"} field, select
`Based on Rules <inventory/shipping/rules>`{.interpreted-text
role="ref"}, `Fixed Price <inventory/shipping/fixed>`{.interpreted-text
role="ref"}, or
`Pickup in store <inventory/shipping/pickup>`{.interpreted-text
role="ref"} if the shiping method does not involve any specific
provider.

::: {.tip}
::: {.title}
Tip
:::

Upon
`configuring <inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"} a shipping method, you can:

-   restrict it
    `to a specific website <../website/configuration/multi_website>`{.interpreted-text
    role="doc"} by selecting it in `Website`{.interpreted-text
    role="guilabel"} field;
-   use the `Destination availability`{.interpreted-text
    role="guilabel"} tab to filter the delivery carriers displayed based
    on the customer\'s area;
-   click the `Test Environment`{.interpreted-text role="guilabel"}
    smart button to switch to the
    `Production Environment`{.interpreted-text role="guilabel"}, then
    click `Unpublished`{.interpreted-text role="guilabel"} to
    `Publish`{.interpreted-text role="guilabel"} the shipping method and
    make it available to website visitors.
:::

In-store pickup {#ecommerce/shipping/instore-pickup}
---------------

To allow customers to reserve products online and pay for/collect them
in person at the store, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll to the `Shipping`{.interpreted-text
role="guilabel"} section, enable
`On Site Payments & Picking`{.interpreted-text role="guilabel"}, and
`Save`{.interpreted-text role="guilabel"}.

Then, click `Customize Pickup Sites`{.interpreted-text role="guilabel"},
select the shipping method or click `New`{.interpreted-text
role="guilabel"} to create a new one and
`configure <inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"} the fields. Make sure the `Provider`{.interpreted-text
role="guilabel"} field is set to `Pickup in store`{.interpreted-text
role="guilabel"}.
