# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md

Third-party shipping carriers
=============================

::: {#inventory/shipping/third_party}
Users can link third-party shipping carriers to Odoo databases, in order
to verify carriers\' delivery to specific addresses,
`automatically calculate shipping costs
<../setup_configuration>`{.interpreted-text role="doc"}, and
`generate shipping labels <labels>`{.interpreted-text role="doc"}.
:::

In Odoo, shipping carriers can be applied to a sales order (SO),
invoice, or delivery order. For tips on resolving common issues when
configuring shipping connectors, skip to the
`Troubleshooting <inventory/shipping_receiving/third-party-troubles>`{.interpreted-text
role="ref"} section.

::: {.seealso}
\- `dhl_credentials`{.interpreted-text role="doc"} -
`sendcloud_shipping`{.interpreted-text role="doc"} -
`ups_credentials`{.interpreted-text role="doc"}
:::

The following is a list of available shipping connectors in Odoo:

  Carrier                                                            Region availability
  ------------------------------------------------------------------ ---------------------------------------------
  `FedEx <fedex>`{.interpreted-text role="doc"}                      All
  `DHL Express <dhl_credentials>`{.interpreted-text role="doc"}      All
  `UPS <ups_credentials>`{.interpreted-text role="doc"}              All
  US Postal Service                                                  United States of America
  `Sendcloud <sendcloud_shipping>`{.interpreted-text role="doc"}     Some European countries (see details below)
  `Bpost <bpost>`{.interpreted-text role="doc"}                      Belgium
  Easypost                                                           North America
  Shiprocket                                                         India
  `Starshipit <starshipit_shipping>`{.interpreted-text role="doc"}   Australia and New Zealand

::: {.important}
::: {.title}
Important
:::

Other services from DHL are **not** supported.

Sendcloud currently supports shipping **from** Austria, Belgium, France,
Germany, Italy, the Netherlands, Spain, and the United Kingdom, and
**to** any European country.
:::

Configuration
-------------

To ensure proper setup of a third-party shipping carrier with Odoo,
follow these steps:

1.  `Install the shipping connector <inventory/shipping_receiving/shipping-connector>`{.interpreted-text
    role="ref"}.
2.  `Set up delivery method <inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
    role="ref"}.
3.  `Activate production environment <inventory/shipping_receiving/production-env>`{.interpreted-text
    role="ref"}.
4.  `Configure warehouse <inventory/shipping_receiving/configure-source-address>`{.interpreted-text
    role="ref"}.
5.  `Specify weight of products <inventory/shipping_receiving/configure-weight>`{.interpreted-text
    role="ref"}.

### Install shipping connector {#inventory/shipping_receiving/shipping-connector}

To install shipping connectors, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.

Under the `Shipping Connectors`{.interpreted-text role="guilabel"}
section, tick the third-party shipping carrier\'s checkbox to install
it. Multiple third-party shipping connectors can be selected at once.
Then, click `Save`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

`Delivery methods <../setup_configuration>`{.interpreted-text
role="doc"} can also be integrated with operations in the *Sales*,
*eCommerce*, and *Website* apps. To install, refer to the
`install apps and modules
<general/install>`{.interpreted-text role="ref"} documentation.
:::

{.align-center}

### Delivery method {#inventory/shipping_receiving/configure-delivery-method}

To configure the API credentials, and activate the shipping carrier,
begin by going to
`Inventory app --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}, and select the desired delivery method.

::: {.note}
::: {.title}
Note
:::

The list often includes **two** delivery methods from the same
`Provider`{.interpreted-text role="guilabel"}: one for international
shipping and one for domestic shipping.

Additional delivery methods can be created for specific purposes, such
as `packaging
<../../product_management/configure/packaging>`{.interpreted-text
role="doc"}.
:::

::: {.seealso}
`Configure delivery methods <../setup_configuration>`{.interpreted-text
role="doc"}
:::

::: {.note}
::: {.title}
Note
:::

Ensure the delivery method is published when it should be available on
the *Website* app. To publish a delivery method on the website, click
the desired delivery method, then click the
`Unpublished`{.interpreted-text role="guilabel"} smart button. Doing so
changes that smart button to read: `Published`{.interpreted-text
role="guilabel"}.
:::

::: {#inventory/shipping_receiving/shipping-methods-details}
The `Shipping Method`{.interpreted-text role="guilabel"} page contains
details about the provider, including:
:::

-   `Shipping Method`{.interpreted-text role="guilabel"} (*Required
    field*): the name of the delivery method (e.g. [FedEx
    US]{.title-ref}, [FedEx EU]{.title-ref}, etc.).

-   `Website`{.interpreted-text role="guilabel"}: configure shipping
    methods for an *eCommerce* page that is connected to a specific
    website in the database. Select the applicable website from the
    drop-down menu, or leave it blank to apply the method to all web
    pages.

-   `Provider`{.interpreted-text role="guilabel"} (*Required field*):
    choose the third-party delivery service, like FedEx. Upon choosing a
    provider, the `Integration Level`{.interpreted-text
    role="guilabel"}, `Invoicing Policy`{.interpreted-text
    role="guilabel"} and `Insurance Percentage`{.interpreted-text
    role="guilabel"} fields become available.

-   `Integration Level`{.interpreted-text role="guilabel"}: choose
    `Get Rate`{.interpreted-text role="guilabel"} to simply get an
    `estimated
    shipment cost <inventory/shipping_receiving/third-party-so>`{.interpreted-text
    role="ref"} on an `SO (Sales Order)`{.interpreted-text role="abbr"}
    or invoice.

    ::: {.important}
    ::: {.title}
    Important
    :::

    Select `Get Rate and Create Shipment`{.interpreted-text
    role="guilabel"} to also `generate shipping labels
    <labels>`{.interpreted-text role="doc"}.
    :::

-   `Company`{.interpreted-text role="guilabel"}: if the shipping method
    should apply to a specific company, select it from the drop-down
    menu. Leave the field blank to apply the method to all companies.

-   `Delivery Product`{.interpreted-text role="guilabel"} (*Required
    field*): the delivery charge name that is added to the
    `SO (Sales Order)`{.interpreted-text role="abbr"} or invoice.

-   `Invoicing Policy`{.interpreted-text role="guilabel"}: select and
    calculate an `Estimated cost`{.interpreted-text role="guilabel"} of
    shipping directly from the shipping carrier. If the
    `Real cost`{.interpreted-text role="guilabel"} of shipping is wanted
    instead, refer to
    `Invoice real shipping costs <invoicing>`{.interpreted-text
    role="doc"} document.

-   `Margin on Rate`{.interpreted-text role="guilabel"}: specify an
    additional percentage amount added to the base shipping rate to
    cover extra costs, such as handling fees, packaging materials,
    exchange rates, etc.

-   `Free if order amount is above`{.interpreted-text role="guilabel"}:
    enables free shipping for orders surpassing a specified amount
    entered in the corresponding `Amount`{.interpreted-text
    role="guilabel"} field.

-   `Insurance Percentage`{.interpreted-text role="guilabel"}: specify a
    percentage amount of the shipping costs reimbursed to the senders if
    the package is lost or stolen in transit.

![**Shipping Method** configuration page for [FedEx
US]{.title-ref}.](third_party_shipper/fedex.png){.align-center}

In the `Configuration`{.interpreted-text role="guilabel"} tab, fill out
the API credential fields (e.g. API key, password, account number,
etc.). Depending on the third-party shipping carrier chosen in the
`Provider`{.interpreted-text role="guilabel"} field, the
`Configuration`{.interpreted-text role="guilabel"} tab will contain
different required fields. For more details about configuring specific
carriers\' credentials, refer to the following documents:

::: {.seealso}
\- `DHL credentials <dhl_credentials>`{.interpreted-text role="doc"} -
`Sendcloud credentials <sendcloud_shipping>`{.interpreted-text
role="doc"} - `UPS credentials <ups_credentials>`{.interpreted-text
role="doc"}
:::

### Production environment {#inventory/shipping_receiving/production-env}

With the delivery method details configured, click the
`Test Environment`{.interpreted-text role="guilabel"} smart button to
set it to `Production Environment`{.interpreted-text role="guilabel"}.

::: {.warning}
::: {.title}
Warning
:::

Setting the delivery method to `Production`{.interpreted-text
role="guilabel"} creates **real** shipping labels, and users are at risk
of being charged through their carrier account (e.g. UPS, FedEx, etc.)
**before** users charge customers for shipping. Verify all
configurations are correct before launching the delivery method to
`Production`{.interpreted-text role="guilabel"}.
:::

{.align-center}

### Warehouse configuration {#inventory/shipping_receiving/configure-source-address}

Ensure the warehouse\'s `Address`{.interpreted-text role="guilabel"}
(including ZIP code) and `Phone`{.interpreted-text role="guilabel"}
number are entered accurately. To do that, go to
`Inventory app --> Configuration -->
Warehouses`{.interpreted-text role="menuselection"}, and select the
desired warehouse.

On the warehouse configuration page, open the warehouse contact page by
clicking the `Company`{.interpreted-text role="guilabel"} field.

{.align-center}

Verify that the `Address`{.interpreted-text role="guilabel"} and
`Phone`{.interpreted-text role="guilabel"} number are correct, as they
are required for the shipping connector to work properly.

{.align-center}

### Product weight {#inventory/shipping_receiving/configure-weight}

For the carrier integration to work properly, specify the weight of
products by going to
`Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and selecting the desired product.

Then, switch to the `Inventory`{.interpreted-text role="guilabel"} tab,
and define the `Weight`{.interpreted-text role="guilabel"} of the
product in the `Logistics`{.interpreted-text role="guilabel"} section.

{.align-center}

Apply third-party shipping carrier {#inventory/shipping_receiving/apply-third-party-carrier}
----------------------------------

Shipping carriers can be applied on a
`SO (Sales Order)`{.interpreted-text role="abbr"}, invoice, or delivery
order.

After configuring the third-party carrier\'s `delivery method
<inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"} in Odoo, create or navigate to a quotation by going to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}.

### Sales order {#inventory/shipping_receiving/third-party-so}

To assign a third-party shipping carrier, and get an estimated cost of
shipping, begin by going to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}. Create or select an existing quotation, and add
the cost of shipping through a third-party carrier to a quotation, by
clicking the `Add Shipping`{.interpreted-text role="guilabel"} button in
the bottom-right corner of the `Order Lines`{.interpreted-text
role="guilabel"} tab.

{.align-center}

In the resulting `Add a shipping method`{.interpreted-text
role="guilabel"} pop-up window, select the intended carrier from the
`Shipping Method`{.interpreted-text role="guilabel"} drop-down menu. The
`Cost`{.interpreted-text role="guilabel"} field is automatically filled
based on:

-   the amount specified in the `Total Order Weight`{.interpreted-text
    role="guilabel"} field (if it is not provided, the sum of
    `product weights <inventory/shipping_receiving/configure-weight>`{.interpreted-text
    role="ref"} in the order is used)
-   the distance between the warehouse\'s `source address
    <inventory/shipping_receiving/configure-source-address>`{.interpreted-text
    role="ref"} and the customer\'s address.

::: {#inventory/shipping_receiving/third-party-rate}
After selecting a third-party provider in the
`Shipping Method`{.interpreted-text role="guilabel"} field, click
`Get Rate`{.interpreted-text role="guilabel"} in the
`Add a shipping method`{.interpreted-text role="guilabel"} pop-up window
to get the estimated cost through the shipping connector. Then, click
the `Add`{.interpreted-text role="guilabel"} button to add the delivery
charge to the `SO (Sales Order)`{.interpreted-text role="abbr"} or
invoice.
:::

::: {.seealso}
`Charge customers for shipping after product delivery <invoicing>`{.interpreted-text
role="doc"}
:::

### Delivery order {#inventory/shipping_receiving/third-party-do}

For users making shipments without installing the *Sales* app, assign
the shipping carrier to the delivery order, by first going to the
`Inventory`{.interpreted-text role="menuselection"} app. Then, from the
`Inventory Overview`{.interpreted-text role="guilabel"} dashboard,
select the `Delivery Orders`{.interpreted-text role="guilabel"}
operation type, and choose the desired delivery order that is not
already marked as `Done`{.interpreted-text role="guilabel"} or
`Cancelled`{.interpreted-text role="guilabel"}.

In the `Additional info`{.interpreted-text role="guilabel"} tab, set the
`Carrier`{.interpreted-text role="guilabel"} field to the desired
third-party shipping carrier. When the delivery method is set to
`production mode
<inventory/shipping_receiving/configure-delivery-method>`{.interpreted-text
role="ref"}, a `Tracking Reference`{.interpreted-text role="guilabel"}
is provided.

::: {.seealso}
`Generate shipping labels <labels>`{.interpreted-text role="doc"}
:::

{.align-center}

Troubleshooting {#inventory/shipping_receiving/third-party-troubles}
---------------

Since shipping connectors can sometimes be complex to set up, here are
some checks to try when things are not working as expected:

1.  Ensure the
    `warehouse information <inventory/shipping_receiving/configure-source-address>`{.interpreted-text
    role="ref"} (e.g., address and phone number) in Odoo is correct
    **and** matches the records saved in the shipping provider\'s
    website.

2.  Verify that the
    `package type <inventory/warehouses_storage/package-type>`{.interpreted-text
    role="ref"} and parameters are valid for the shipping carrier. To
    check, ensure the shipment can be directly created on the shipping
    carrier\'s website.

3.  When encountering a price mismatch between Odoo\'s estimated cost
    and the provider\'s charge, first ensure the delivery method is set
    to `production environment
    <inventory/shipping_receiving/production-env>`{.interpreted-text
    role="ref"}.

    Then, create the shipment in both the carrier\'s website and Odoo,
    and verify the prices are the same across Odoo, the shipping
    provider, and in the *debug logs*.

    ::: {.example}
    When checking for a price mismatch in the debug logs, if the request
    says the package weighs six kilograms, but the response from FedEx
    says the package weights seven kilograms, it concludes that the
    issue is on FedEx\'s side.
    :::

### Debug log

Track shipping data inconsistencies by activating debug logging. To do
that, go to the delivery method\'s configuration page
(`Inventory app --> Configuration --> Shipping
Method`{.interpreted-text role="menuselection"}), and select the desired
shipping method. Click the `No Debugging`{.interpreted-text
role="guilabel"} smart button to activate
`Debug Requests`{.interpreted-text role="guilabel"}.

{.align-center}

With `Debug Requests`{.interpreted-text role="guilabel"} activated, each
time the shipping connector is used to estimate the cost of shipping,
records are saved in the `Logging`{.interpreted-text role="guilabel"}
report. To access the report, turn on
`developer mode <developer-mode>`{.interpreted-text role="ref"}, and go
to `Settings app --> Technical -->
Database Structure section --> Logging`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Logs are created for a shipping method each time the `Get Rate
<inventory/shipping_receiving/third-party-rate>`{.interpreted-text
role="ref"} button is clicked on `SOs (Sales Orders)`{.interpreted-text
role="abbr"} and invoices, **and** when a customer adds the shipping
carrier to their order through the *Website* app.
:::

{.align-center}

Click the *HTTP request* line item to open a detailed page, and verify
the correct information is sent from Odoo to the shipping carrier. In
the *HTTP response*, verify that the same information is received.

{.align-center}
