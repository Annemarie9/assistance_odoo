# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/bpost.md

Bpost integration
=================

Set up the *Bpost* shipping connector in Odoo to manage Bpost shipments
to clients directly within Odoo. To configure it, complete these steps:

1.  Create a Bpost account.
2.  Get the
    `Account ID and passphrase <inventory/shipping_receiving/bpost-account>`{.interpreted-text
    role="ref"}.
3.  `Set up the shipping method in Odoo <inventory/shipping_receiving/bpost-method>`{.interpreted-text
    role="ref"}.

Upon completion, it is possible to calculate the cost of shipping, based
on package size and weight, have the charges applied directly to a Bpost
business account, and automatically print Bpost tracking labels through
Odoo.

::: {.seealso}
\- `third_party_shipper`{.interpreted-text role="doc"} -
`../setup_configuration`{.interpreted-text role="doc"} -
`dhl_credentials`{.interpreted-text role="doc"} -
`ups_credentials`{.interpreted-text role="doc"}
:::

Account setup
-------------

To begin, go to the [Bpost
website](https://parcel.bpost.be/en/home/business) to create, or log
into, the company\'s Bpost business account. When creating the Bpost
account, have the company\'s VAT number and mobile phone number ready.

Follow the website\'s steps to complete registration, and sign up for
shipping services. Doing so submits a request to enter a contractual
business relationship between the company and Bpost.

::: {.important}
::: {.title}
Important
:::

Odoo **cannot** be integrated with [non-business
Bpost](https://www.odoo.com/r/Z4wZ) accounts.
:::

After completing the setup, get the Bpost account ID and passphrase, by
navigating to the `Shipping Manager`{.interpreted-text role="guilabel"}
menu item.

::: {#inventory/shipping_receiving/bpost-account}
On the `Shipping Manager`{.interpreted-text role="guilabel"} page, go to
the `Admin`{.interpreted-text role="guilabel"} tab, then the
`General Settings`{.interpreted-text role="guilabel"} tab, to find the
`Account ID`{.interpreted-text role="guilabel"} and
`Passphrase`{.interpreted-text role="guilabel"} needed to configure
Odoo\'s shipping method.
:::



Shipping method configuration {#inventory/shipping_receiving/bpost-method}
-----------------------------

With those necessary credentials, configure the Bpost shipping method in
Odoo by going to
`Inventory app --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}.

On the `Shipping Methods`{.interpreted-text role="guilabel"} page, click
`Create`{.interpreted-text role="guilabel"}.

In the `Provider`{.interpreted-text role="guilabel"} field, select
`Bpost`{.interpreted-text role="guilabel"} from the drop-down menu.
Doing so reveals the `Bpost Configuration`{.interpreted-text
role="guilabel"} tab at the bottom of the form, where the Bpost
credentials can be entered.

For details on configuring the other fields on the shipping method, such
as `Delivery
Product`{.interpreted-text role="guilabel"}, refer to the
`Configure third-party carrier <third_party_shipper>`{.interpreted-text
role="doc"} documentation.

::: {.note}
::: {.title}
Note
:::

To generate Bpost `shipping labels <labels>`{.interpreted-text
role="doc"} through Odoo, ensure the `Integration
Level`{.interpreted-text role="guilabel"} option is set to
`Get Rate and Create Shipment`{.interpreted-text role="guilabel"}.
:::

In the `Bpost Configuration`{.interpreted-text role="guilabel"} tab,
complete the following fields:

-   `Bpost Account Number`{.interpreted-text role="guilabel"} (required
    field): enter the company\'s unique `account ID
    <inventory/shipping_receiving/bpost-account>`{.interpreted-text
    role="ref"} from the Bpost website.

-   `Passphrase`{.interpreted-text role="guilabel"} (required field):
    enter the `passphrase
    <inventory/shipping_receiving/bpost-account>`{.interpreted-text
    role="ref"} from the Bpost website.

-   `Bpost Delivery Nature`{.interpreted-text role="guilabel"}: select
    either `Domestic`{.interpreted-text role="guilabel"} or
    `International`{.interpreted-text role="guilabel"} shipping
    services. Choosing `Domestic`{.interpreted-text role="guilabel"}
    shows the `Options`{.interpreted-text role="guilabel"} section,
    while `International`{.interpreted-text role="guilabel"} enables the
    `Bpost Shipment Type`{.interpreted-text role="guilabel"} and
    `Bpost Parcel
    Return Instructions`{.interpreted-text role="guilabel"} fields.

-   `Bpost Package Type`{.interpreted-text role="guilabel"}: select the
    type of shipping service from the drop-down menu.

    For , the options
    are: `bpack 24h
    Pro`{.interpreted-text role="guilabel"},
    `bpack 24h business`{.interpreted-text role="guilabel"}, or
    `bpack Bus`{.interpreted-text role="guilabel"}.

    For , the
    options are: `bpack
    World Express Pro`{.interpreted-text role="guilabel"},
    `bpack World Business`{.interpreted-text role="guilabel"}, or
    `bpack Europe Business`{.interpreted-text role="guilabel"}.

-   `Bpost Shipment Type`{.interpreted-text role="guilabel"} (required
    field): for international deliveries, declare the type of goods in
    the package as `SAMPLE`{.interpreted-text role="guilabel"},
    `GIFT`{.interpreted-text role="guilabel"}, `GOODS`{.interpreted-text
    role="guilabel"}, `DOCUMENTS`{.interpreted-text role="guilabel"}, or
    `OTHER`{.interpreted-text role="guilabel"}.

-   `Bpost Parcel Return Address`{.interpreted-text role="guilabel"}:
    return address when an international shipment fails to deliver.
    Select from the drop-down menu: `Destroy`{.interpreted-text
    role="guilabel"}, `Return to sender by air`{.interpreted-text
    role="guilabel"}, or `Return to sender by road`{.interpreted-text
    role="guilabel"}.

-   `Label Type`{.interpreted-text role="guilabel"}: choose
    `A6`{.interpreted-text role="guilabel"} or `A4`{.interpreted-text
    role="guilabel"} label sizes from the drop-down menu.

-   `Label Format`{.interpreted-text role="guilabel"}: choose
    `PDF`{.interpreted-text role="guilabel"} or `PNG`{.interpreted-text
    role="guilabel"} from the drop-down menu.

For domestic deliveries, these features are available in the
`Options`{.interpreted-text role="guilabel"} section:

-   Enable the `Delivery on Saturday`{.interpreted-text role="guilabel"}
    feature to include Saturdays as possible delivery dates. Depending
    on the `Bpost Package Type`{.interpreted-text role="guilabel"}
    selected, this option might incur additional costs to the company.
-   Enable the `Generate Return Label`{.interpreted-text
    role="guilabel"} feature to automatically print a return label upon
    validating the delivery order.


