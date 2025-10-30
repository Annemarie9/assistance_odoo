# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping.md

Sendcloud integration
=====================

Sendcloud is a shipping service aggregator that facilitates the
integration of European shipping carriers with Odoo. Once integrated,
users can select shipping carriers on inventory operations in their Odoo
database.

::: {.seealso}
[Sendcloud integration documentation
\<https://support.sendcloud.com/hc/en-us/articles
/360059470491-Odoo-integration\>]()
:::

Setup in Sendcloud
------------------

### Create an account and activate carriers

To get started, go to 
to configure the account and generate the connector credentials. Log in
with the Sendcloud account, or create a new one if needed.

::: {.note}
::: {.title}
Note
:::

For new account creation, Sendcloud will ask for a
`VAT (Value-Added Tax Identification)`{.interpreted-text role="abbr"}
number or
`EORI (Economic Operators' Registration and Identification)`{.interpreted-text
role="abbr"} number. After completing the account setup, activate (or
deactivate) the shipping carriers that will be used in the Odoo
database.
:::

::: {.important}
::: {.title}
Important
:::

Odoo integration of Sendcloud works on free Sendcloud plans *only* if a
bank account is linked, since Sendcloud won\'t ship for free. To use
shipping rules, or individual custom carrier contacts, a paid plan of
Sendcloud is **required**.
:::

### Warehouse configuration {#inventory/shipping_receiving/sendcloud-warehouse-config}

Once logged into the Sendcloud account, navigate to
`Settings --> Shipping -->
Addresses`{.interpreted-text role="menuselection"}, and fill in the
field for `Warehouse address`{.interpreted-text role="guilabel"}.

{.align-center}

To allow Sendcloud to process returns as well, a
`Return Address`{.interpreted-text role="guilabel"} is required. Under
the `Miscellaneous section`{.interpreted-text role="guilabel"}, there is
a field called `Address Name (optional)`{.interpreted-text
role="guilabel"}. The Odoo warehouse name should be entered here, and
the characters should be exactly the same.

::: {.example}
| **SendClould configuration**
| `Miscellaneous`{.interpreted-text role="guilabel"}
| `Address Name (optional)`{.interpreted-text role="guilabel"}:
  [Warehouse \#1]{.title-ref}
| `Brand`{.interpreted-text role="guilabel"}: [Default]{.title-ref}

| **Odoo warehouse configuration**
| `Warehouse`{.interpreted-text role="guilabel"}: [Warehouse
  \#1]{.title-ref}
| `Short Name`{.interpreted-text role="guilabel"}: [WH]{.title-ref}
| `Company`{.interpreted-text role="guilabel"}: [My company (San
  Francisco)]{.title-ref}
| `Address`{.interpreted-text role="guilabel"}: [My Company (San
  Francisco)]{.title-ref}

Notice how the inputs for the `Warehouse`{.interpreted-text
role="guilabel"} field, for both the Odoo configuration and the
Sendcloud configuration, are the exact same.
:::

### Generate Sendcloud credentials

In the Sendcloud account, navigate to
`Settings --> Integrations`{.interpreted-text role="menuselection"} in
the menu on the right. Next, search for `Odoo Native`{.interpreted-text
role="guilabel"}. Then, click on `Connect`{.interpreted-text
role="guilabel"}.

After clicking on `Connect`{.interpreted-text role="guilabel"}, the page
redirects to the `Sendcloud API`{.interpreted-text role="guilabel"}
settings page, where the `Public and Secret Keys`{.interpreted-text
role="guilabel"} are produced. The next step is to name the
`Integration`{.interpreted-text role="guilabel"}. The naming convention
is as follows: [Odoo CompanyName]{.title-ref}, with the user\'s company
name replacing [CompanyName]{.title-ref} (e.g. [Odoo
StealthyWood]{.title-ref}).

Then, check the box next to `Service Points`{.interpreted-text
role="guilabel"} and select the shipping services for this integration.
After saving, the `Public and Secret Keys`{.interpreted-text
role="guilabel"} are generated.

{.align-center}

Setup in Odoo
-------------

To ensure seamless Sendcloud integration with Odoo, `install
<inventory/shipping_receiving/sendcloud-module>`{.interpreted-text
role="ref"} and `link
<inventory/shipping_receiving/link-sendcloud-module>`{.interpreted-text
role="ref"} the Sendcloud shipping connector to the Sendcloud account.
Then, `configure Odoo fields
<inventory/shipping_receiving/sendcloud-shipping-info>`{.interpreted-text
role="ref"}, so Sendcloud can accurately pull shipping data to generate
labels.

::: {.seealso}
`Enable pickup points on websites <inventory/shipping_receiving/sendcloud-pickups>`{.interpreted-text
role="ref"}
:::

### Install Sendcloud shipping module {#inventory/shipping_receiving/sendcloud-module}

After the Sendcloud account is set up and configured, it\'s time to
configure the Odoo database. To get started, go to Odoo\'s
`Apps`{.interpreted-text role="guilabel"} module, search for the
[Sendcloud Shipping]{.title-ref} integration, and install it.

{.align-center}

### Sendcloud shipping connector configuration {#inventory/shipping_receiving/link-sendcloud-module}

Once installed, activate the `Sendcloud Shipping`{.interpreted-text
role="guilabel"} module in `Inventory -->
Configuration --> Settings`{.interpreted-text role="menuselection"}. The
`Sendcloud Connector`{.interpreted-text role="guilabel"} setting is
found under the `Shipping Connectors`{.interpreted-text role="guilabel"}
section.

After activating the `Sendcloud Connector`{.interpreted-text
role="guilabel"}, click on the `Sendcloud Shipping
Methods`{.interpreted-text role="guilabel"} link below the listed
connector. Once on the `Shipping Methods`{.interpreted-text
role="guilabel"} page, click `New`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

`Shipping Methods`{.interpreted-text role="guilabel"} can also be
accessed by going to `Inventory -->
Configuration --> Delivery --> Shipping Methods`{.interpreted-text
role="menuselection"}.
:::

Fill out the following fields in the
`New Shipping Method`{.interpreted-text role="guilabel"} form:

-   `Shipping Method`{.interpreted-text role="guilabel"}: type
    [Sendcloud DPD]{.title-ref}.
-   `Provider`{.interpreted-text role="guilabel"}: select
    `Sendcloud`{.interpreted-text role="guilabel"} from the drop-down
    menu.
-   `Delivery Product`{.interpreted-text role="guilabel"}: set the
    product that was configured for this shipping method or create a new
    product.
-   In the `SendCloud Configuration`{.interpreted-text role="guilabel"}
    tab, enter the `Sendcloud Public Key`{.interpreted-text
    role="guilabel"}.
-   In the `SendCloud Configuration`{.interpreted-text role="guilabel"}
    tab, enter the `Sendcloud Secret Key`{.interpreted-text
    role="guilabel"}.

#### Pickup points {#inventory/shipping_receiving/sendcloud-pickups}

Sendcloud\'s [service point
delivery](https://support.sendcloud.com/hc/en-us/articles/360026097951-FAQ-Service-Points)
lets customers choose a pickup location (such as a nearby shop or
locker) instead of entering a private delivery address.

To enable the feature, go to the shipping method form, and in the
`SendCloud
Configuration`{.interpreted-text role="guilabel"} tab, under the
`Options`{.interpreted-text role="guilabel"} section, enable
`Use Sendcloud
Locations`{.interpreted-text role="guilabel"} feature.

::: {.important}
::: {.title}
Important
:::

Pickup point selection is only available through the **Website** app
(the online checkout view). It is not currently possible to select a
pickup point manually through the **Sales** app (the internal database
view).

For example, if the customer selects a shipping method like *Sendcloud
Mondial Relay*, they must choose a pickup point during the checkout
process on the website. If no pickup point is selected, the delivery
order cannot be validated in Odoo.
:::

#### Load shipping products

After configuring and saving the form, follow these steps to load the
shipping products:

-   In the `SendCloud Configuration`{.interpreted-text role="guilabel"}
    tab of the `New Shipping Method`{.interpreted-text role="guilabel"}
    form, click on the
    `Load your SendCloud shipping products`{.interpreted-text
    role="guilabel"} link.
-   Select the shipping products the company would like to use for
    deliveries and returns.
-   Click `Select`{.interpreted-text role="guilabel"}.

::: {.example}
Sample Sendcloud shipping products configured in Odoo:

| `DELIVERY`{.interpreted-text role="guilabel"}
| `Shipping Product`{.interpreted-text role="guilabel"}: [DPD Home
  0-31.5kg]{.title-ref}
| `Carrier`{.interpreted-text role="guilabel"}: [DPD]{.title-ref}
| `Minimum Weight`{.interpreted-text role="guilabel"}:
  [0.00]{.title-ref}
| `Maximum Weight`{.interpreted-text role="guilabel"}:
  [31.50]{.title-ref}

`Countries`{.interpreted-text role="guilabel"}: [Austria]{.title-ref}
[Belgium]{.title-ref} [Bosnia]{.title-ref} [Herzegovina]{.title-ref}
[Bulgaria]{.title-ref} [Croatia]{.title-ref} [Czech]{.title-ref}
[Republic]{.title-ref} [Denmark]{.title-ref} [Estonia]{.title-ref}
[Finland]{.title-ref} [France]{.title-ref} [Germany]{.title-ref}
[Greece]{.title-ref} [Hungary]{.title-ref} [Iceland]{.title-ref}
[Ireland]{.title-ref} [Italy]{.title-ref} [Latvia]{.title-ref}
[Liechtenstein]{.title-ref} [Lithuania]{.title-ref}
[Luxembourg]{.title-ref} [Monaco]{.title-ref} [Netherlands]{.title-ref}
[Norway]{.title-ref} [Poland]{.title-ref} [Portugal]{.title-ref}
[Romania]{.title-ref} [Serbia]{.title-ref} [Slovakia]{.title-ref}
[Slovenia]{.title-ref} [Spain]{.title-ref} [Sweden]{.title-ref}
[Switzerland]{.title-ref}

| `RETURN`{.interpreted-text role="guilabel"}
| `Return Shipping Product`{.interpreted-text role="guilabel"}: [DPD
  Return 0-20kg]{.title-ref}
| `Return Carrier`{.interpreted-text role="guilabel"}: [DPD]{.title-ref}
| `Return Minimum Weight`{.interpreted-text role="guilabel"}:
  [0.00]{.title-ref}
| `Return Maximum Weight`{.interpreted-text role="guilabel"}:
  [20.00]{.title-ref}
| `Return Countries`{.interpreted-text role="guilabel"}:
  [Belgium]{.title-ref} [Netherlands]{.title-ref}
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Sendcloud does not provide test keys when a company tests the sending of
a package in Odoo. This means if a package is created, the configured
Sendcloud account will be charged, unless the associated package is
canceled within 24 hours of creation.

Odoo has a built-in layer of protection against unwanted charges when
using test environments. Within a test environment, if a shipping method
is used to create labels, then those labels are immediately canceled
after the creation --- this occurs automatically. The test and
production environment settings can be toggled back and forth from their
respective smart buttons.
:::

### Shipping information {#inventory/shipping_receiving/sendcloud-shipping-info}

To use Sendcloud to generate shipping labels, the following information
**must** be filled out accurately and completely in Odoo:

1.  **Customer information**: when creating a quotation, ensure the
    selected `Customer`{.interpreted-text role="guilabel"} has a valid
    phone number, email address, and shipping address.

    To verify, select the `Customer`{.interpreted-text role="guilabel"}
    field to open their contact page. Here, add their shipping address
    in the `Contact`{.interpreted-text role="guilabel"} field, along
    with their `Mobile`{.interpreted-text role="guilabel"} number and
    `Email`{.interpreted-text role="guilabel"} address.

2.  **Product weight**: ensure all products in an order have a specified
    `Weight`{.interpreted-text role="guilabel"} in the
    `Inventory`{.interpreted-text role="guilabel"} tab of their product
    form. Refer to the `Product weight section
    <inventory/shipping_receiving/configure-weight>`{.interpreted-text
    role="ref"} of this article for detailed instructions.

3.  **Warehouse address**: ensure the warehouse name and address in Odoo
    match the `previously
    defined warehouse <inventory/shipping_receiving/sendcloud-warehouse-config>`{.interpreted-text
    role="ref"} in the Sendcloud setup. For details on warehouse
    configuration in Odoo, refer to the `warehouse configuration
    section <inventory/shipping_receiving/configure-source-address>`{.interpreted-text
    role="ref"} of the third-party shipping documentation.

Generate labels with Sendcloud
------------------------------

When creating a quotation in Odoo, add shipping and a
`Sendcloud shipping product`{.interpreted-text role="guilabel"}. Then,
`Validate`{.interpreted-text role="guilabel"} the delivery. Shipping
label documents are automatically generated in the chatter, which
include the following:

1.  `Shipping label(s)`{.interpreted-text role="guilabel"} depending on
    the number of packages.
2.  `Return label(s)`{.interpreted-text role="guilabel"} if the
    Sendcloud connector is configured for returns.
3.  `Customs document(s)`{.interpreted-text role="guilabel"} should the
    destination country require them.

Additionally, the tracking number is now available.

::: {.important}
::: {.title}
Important
:::

When return labels are created, Sendcloud automatically charges the
configured Sendcloud account.
:::

### Shipping rules

Optionally, create shipping rules to automatically generate shipping
labels tailored to different product needs. For example, a shipping rule
can be created for customers shipping expensive jewelry items to
purchase insurance.

::: {.note}
::: {.title}
Note
:::

Shipping rules do **not** affect `shipping rate calculations
<inventory/shipping_receiving/third-party-rate>`{.interpreted-text
role="ref"}, and are only used to improve the process of
`generating shipping labels <labels>`{.interpreted-text role="doc"}.
:::

To use shipping rules, navigate to
`Inventory app --> Configuration --> Delivery:
Shipping Methods`{.interpreted-text role="menuselection"}, and select
the intended [Sendcloud]{.title-ref} shipping method.

Under the `Sendcloud Configuration`{.interpreted-text role="guilabel"}
tab, in the `OPTIONS`{.interpreted-text role="guilabel"} section, choose
the kind of shipments the shipping rules apply to, via the
`Use Sendcloud shipping rules`{.interpreted-text role="guilabel"} field.

From here, choose either: `Shipping`{.interpreted-text role="guilabel"}
to customers, `Returns`{.interpreted-text role="guilabel"} from
customers, or `Both`{.interpreted-text role="guilabel"}.

{.align-center}

Then, in the Sendcloud website, navigate to
`Settings --> Shipping rules`{.interpreted-text role="menuselection"}.
Create a new shipping rule by clicking `Create New`{.interpreted-text
role="guilabel"}.

In the `Actions`{.interpreted-text role="guilabel"} section, set a
`Condition`{.interpreted-text role="guilabel"} to determine when the
rule applies. Then, configure what to do when packages meet the
condition.

::: {.seealso}
[Create shipping rules on
Sendcloud](https://support.sendcloud.com/hc/en-us/articles/10274470454292-How-to-create-shipping-rules#examples-smart-shipping-rules)
:::

FAQ
---

### Shipment is too heavy

If the shipment is too heavy for the Sendcloud service that is
configured, then the weight is split to simulate multiple packages.
Products will need to be put in different `Packages`{.interpreted-text
role="guilabel"} to `Validate`{.interpreted-text role="guilabel"} the
transfer and generate labels.

`Rules`{.interpreted-text role="guilabel"} can also be set up in
Sendcloud to use other shipping methods when the weight is too heavy.
However, note that these rules will not apply to the shipping price
calculation on the calculation on the sales order.

### Personal carrier contract

Use custom prices from a direct carrier contract, via CSV upload, by
first logging into Sendcloud, navigating to
`Settings --> Carriers --> My contracts`{.interpreted-text
role="menuselection"}, and then selecting the intended contract.

{.align-center}

Under the `Contract prices`{.interpreted-text role="guilabel"} section,
click `Download CSV`{.interpreted-text role="guilabel"} and fill out the
contract prices in the `price`{.interpreted-text role="guilabel"} column
of the CSV file template.

::: {.warning}
::: {.title}
Warning
:::

Ensure the CSV file includes the correct prices to avoid any
inaccuracies.
:::

{.align-center}

`Upload`{.interpreted-text role="guilabel"} the completed CSV file to
Sendcloud, then click `Save these prices`{.interpreted-text
role="guilabel"}.

::: {.seealso}
[Sendcloud: How to upload contract prices with
carriers](https://support.sendcloud.com/hc/en-us/articles/5163547066004)
:::

### Measuring volumetric weight

Many carriers have several measures for weight. There is the actual
weight of the products in the parcel, and there is the *volumetric
weight* (`Volumetric weight is the volume that a package
occupies when in transit. In other words it is the physical size of a package`{.interpreted-text
role="dfn"}).

::: {.tip}
::: {.title}
Tip
:::

Check to see if selected carrier(s) already have defined formulas to
compute the volumetric weight.
:::

::: {.seealso}
[Sendcloud: How to calculate & automate parcel volumetric weight
\<https://support.sendcloud.com/
hc/en-us/articles/360059644051-How-to-calculate-automate-parcel-volumetric-weight\>]()
:::

### Unable to calculate shipping rate

First, verify that the product being shipped has a weight that is
supported by the selected shipping method. If this is set, then verify
that the destination country (from the customer address) is supported by
the carrier. The country of origin (warehouse address) should also be
supported by the carrier.
