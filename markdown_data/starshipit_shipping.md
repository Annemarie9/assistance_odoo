# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/starshipit_shipping.md

Starshipit shipping
===================

Starshipit is a shipping service operator that facilitates the
integration of Australasian shipping couriers with Odoo. Once
integrated, users can create shipping methods that will automatically
get rates from specific couriers (such as Australia Post, NZ Post,
DHL,\...) based on predefined conditions.

::: {.seealso}
\-
`Automatically calculate shipping <../setup_configuration>`{.interpreted-text
role="doc"} -
`Integrate other third-party couriers <third_party_shipper>`{.interpreted-text
role="doc"}
:::

Setup in Starshipit
-------------------

### Create an account and activate couriers

To get started, go to 
to configure the account and generate the connector credentials. Log in
with the Starshipit account, or create a new one if needed.

### Pickup address configuration

Once logged into the Starshipit account, navigate to
`Settings --> Pickup address`{.interpreted-text role="menuselection"},
and fill in the `Pickup address`{.interpreted-text role="guilabel"}.
Ensure this field matches the warehouse address.

{.align-center}

### Couriers configuration

To integrate with third-party couriers, navigate to
`Settings --> Couriers`{.interpreted-text role="menuselection"}, and
select `Couriers`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

For details on integrating with different couriers, refer to
[Starshipit\'s support
center](https://support.starshipit.com/hc/en-us/).
:::

### Checkout rates

To configure shipping rate calculations, navigate to
`Settings --> Checkout rates`{.interpreted-text role="menuselection"}.
The selected delivery costs are automatically applied in Odoo when
calculating shipping costs.

{.align-center}

### Starshipit API key

Configure shipping rules to assign the correct shipping methods to
orders based on specific conditions.

To create a rule, go to `Settings --> Rules`{.interpreted-text
role="menuselection"} and click `Add a new rule`{.interpreted-text
role="guilabel"}.

While there are multiple ways to configure rules, it is recommended to
set:

1.  `Condition`{.interpreted-text role="guilabel"} to
    `Contains`{.interpreted-text role="guilabel"}
2.  `Value`{.interpreted-text role="guilabel"} to the
    `product code`{.interpreted-text role="guilabel"}
3.  `Action`{.interpreted-text role="guilabel"} to
    `Set Courier & Product Code`{.interpreted-text role="guilabel"}

{.align-center}

### Finding Starshipit API credentials {#inventory/shipping_receiving/star-api}

In the Starshipit account, navigate to
`Settings --> API`{.interpreted-text role="menuselection"} in the side
menu. This page contains the
`API (Application Programming Interface)`{.interpreted-text role="abbr"}
keys needed to connect to Odoo.

{.align-center}

Setup in Odoo
-------------

### Install

After the Starshipit account is set up, integrate it with the Odoo
database. To do that, go to Odoo\'s `Apps`{.interpreted-text
role="guilabel"} module, search for the
`Starshipit Shipping`{.interpreted-text role="guilabel"} module, and
click `Activate`{.interpreted-text role="guilabel"} to install it.

{.align-center}

### Configuration

Once installed, activate the feature by going to
`Inventory --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Under the
`Shipping Connectors`{.interpreted-text role="guilabel"} section,
activate the `Starshipit
Connector`{.interpreted-text role="guilabel"} option.

After activating `Starshipit Connector`{.interpreted-text
role="guilabel"}, click the
`Starshipit Shipping Methods`{.interpreted-text role="guilabel"} link
below the listed connector. Once on the
`Shipping Methods`{.interpreted-text role="guilabel"} page, click
`Create`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

`Shipping Methods`{.interpreted-text role="guilabel"} can also be
accessed by going to `Inventory -->
Configuration --> Delivery --> Shipping Methods`{.interpreted-text
role="menuselection"}.
:::

Configure Starshipit in Odoo by filling out the fields on the
`Shipping Methods`{.interpreted-text role="guilabel"} form as follows:

-   `Shipping Method`{.interpreted-text role="guilabel"}: type
    [Starshipit]{.title-ref}.

-   `Provider`{.interpreted-text role="guilabel"}: select
    `Starshipit`{.interpreted-text role="guilabel"} from the drop-down
    menu.

-   `Delivery Product`{.interpreted-text role="guilabel"}: assign or
    create the delivery product that will appear on the sales order line
    when the cost of shipping is computed.

    ::: {.note}
    ::: {.title}
    Note
    :::

    The fields discussed in this section are specific to configuring
    Starshipit. For more information about the other fields, refer to
    `../setup_configuration`{.interpreted-text role="doc"}.
    :::

In the `Starshipit Configuration`{.interpreted-text role="guilabel"}
tab, fill out these fields:

-   `Starshipit API Key`{.interpreted-text role="guilabel"}: enter the
    `API (Application Programming Interface)`{.interpreted-text
    role="abbr"} key
    `obtained from Starshipit <inventory/shipping_receiving/star-api>`{.interpreted-text
    role="ref"}.
-   `Starshipit Subscription Key`{.interpreted-text role="guilabel"}:
    enter the subscription key obtained from the same place as the
    `API key <inventory/shipping_receiving/star-api>`{.interpreted-text
    role="ref"}.
-   `Origin Address`{.interpreted-text role="guilabel"}: Enter the
    address where products are shipped from. This field is crucial for
    calculating shipping rates and `generating shipping labels
    <inventory/shipping_receiving/star-label>`{.interpreted-text
    role="ref"}.
-   `Default Package Type`{.interpreted-text role="guilabel"}: Set a
    default package type to include the weight of the empty package when
    automatically calculating shipping rates.

::: {.important}
::: {.title}
Important
:::

To set a default package type, the *Packages* feature **must** be
enabled in `Inventory --> Configuration --> Settings`{.interpreted-text
role="menuselection"}.
:::

-   Manually `Save`{.interpreted-text role="guilabel"} the form by
    clicking the cloud icon next to the `Shipping
    Methods / New`{.interpreted-text role="guilabel"} breadcrumbs.

To load the newly configured shipping products, click the
`Select a service linked to the
Starshipit account`{.interpreted-text role="guilabel"} link at the
bottom of the `Starshipit Configuration`{.interpreted-text
role="guilabel"} tab.

Doing so opens the
`Choose Starshipit Shipping Service`{.interpreted-text role="guilabel"}
pop-up window. In the `Delivery Service`{.interpreted-text
role="guilabel"} field, choose the desired shipping service for
deliveries and returns from the drop-down menu. Finally, click
`Confirm`{.interpreted-text role="guilabel"}.

The chosen delivery service will populate in the
`Service Name`{.interpreted-text role="guilabel"} field.

::: {.example}
Sample of a Starshipit shipping product configured in Odoo:

| `Sendle: Sendle drop off`{.interpreted-text role="guilabel"}
| `Shipping Product`{.interpreted-text role="guilabel"}: [Sendle
  Delivery]{.title-ref}
| `Starshipit Service Code`{.interpreted-text role="guilabel"}:
  [STANDARD-DROPOFF]{.title-ref}
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Starshipit does not provide test keys when a company tests the sending
of a package in Odoo. This means that if a package is created, the
account may be charged.

Odoo has a built-in layer of protection against unwanted charges when
using test environments. Within a test environment, if a shipping method
is used to create labels, then those labels are immediately canceled
after creation --- this occurs automatically. Please note that depending
on the shipping provider being used, the account might be charged for
printing label, unless the order is cancelled manually on the couriers's
portal.

Switch between the test and production environment by clicking the
`Environment`{.interpreted-text role="guilabel"} smart button at the top
of the shipping method form.
:::

### Generate a label with Starshipit {#inventory/shipping_receiving/star-label}

When creating a quotation in Odoo, add the Starshipit shipping method by
clicking the `Add
shipping`{.interpreted-text role="guilabel"} button.

In the `Add a shipping method`{.interpreted-text role="guilabel"} pop-up
window, select Starshipit in the `Shipping
Method`{.interpreted-text role="guilabel"} field.

Calculate the shipping rate by clicking `Get rate`{.interpreted-text
role="guilabel"}. Finally, click `Add`{.interpreted-text
role="guilabel"} to include the cost of shipping to the sales order
line, labeled as the *delivery product*.

::: {.note}
::: {.title}
Note
:::

Automatically calculate shipping costs for Starshipit in **both** Odoo
*Sales* and *eCommerce* applications.
:::

Then, `Validate`{.interpreted-text role="guilabel"} the delivery.
Shipping label documents are automatically generated in the chatter,
which includes the following:

1.  `Shipping label(s)`{.interpreted-text role="guilabel"} depending on
    the number of packages.
2.  `Tracking number(s)`{.interpreted-text role="guilabel"} if the
    selected courier supports it.
3.  `Return label(s)`{.interpreted-text role="guilabel"} if the
    Starshipit connector is configured for returns.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Package weight in Odoo is calculated by adding the weights of the
products plus the empty package saved in the database. Ensure the
correct shipping option is selected, as the package weight is not
automatically verified.

Verify the destination address, as Starshipit checks it when the order
is created.

Finally, some couriers may require other information, such as an email
address or phone number. Please ensure that all necessary information
are set upon sending a shipping order.
:::

### Returns

Starshipit allows returns with the following couriers:

:   -   Australia Post eParcel
    -   TNT
    -   Couriers Please
    -   Aramex
    -   StarTrack
    -   DHL Express
    -   NZ Post Domestic

This can be done by clicking the `Return`{.interpreted-text
role="guilabel"} smart button on the intended delivery order. If the
selected courier supports returns, the
`Print Return Label`{.interpreted-text role="guilabel"} button will be
available.

### Cancellations

If a delivery order is cancelled in Odoo, it will be automatically
archived in Starshipit. However, the cancellation will not be sent to
the courier itself, so make sure to log onto the courier\'s platform to
handle the cancellation manually.
