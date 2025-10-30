# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/fedex.md

FedEx integration
=================

Integrating a FedEx account with Odoo\'s **Inventory** app makes it
possible to `calculate
shipping rates <../setup_configuration>`{.interpreted-text role="doc"},
and `generate shipping labels <labels>`{.interpreted-text role="doc"}
within Odoo. This is accomplished by enabling the FedEx *shipping
connector*, then configuring at least one *shipping method*.

::: {.note}
::: {.title}
Note
:::

This documentation contains configuration details specific to FedEx
integration. See the documentation on
`third-party shippers <third_party_shipper>`{.interpreted-text
role="doc"} for general shipper integration instructions.
:::

Enable shipping connector
-------------------------

To enable the shipping connector for FedEx, navigate to
`Inventory app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Scroll down to the `Shipping Connectors`{.interpreted-text
role="guilabel"} section, and tick the checkbox next to
`FedEx Connector`{.interpreted-text role="guilabel"}.

Finally, click `Save`{.interpreted-text role="guilabel"} to save the
changes. After doing so, a `oi-arrow-right`{.interpreted-text
role="icon"} `FedEx Shipping Methods`{.interpreted-text role="guilabel"}
button appears below `FedEx Connector`{.interpreted-text
role="guilabel"}.

{.align-center}

Configure shipping method
-------------------------

Once the FedEx shipping connector is enabled, it is necessary to
configure at least one shipping method. After doing so, the shipping
method can be included in sales orders (SOs), and used to compute
shipping costs, and print shipping labels.

To enable a shipping method, navigate to
`Inventory app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and click the
`FedEx Shipping Methods`{.interpreted-text role="guilabel"} button below
the `FedEx
Connector`{.interpreted-text role="guilabel"} checkbox. Doing so opens a
page that shows all existing FedEx shipping methods.

::: {.note}
::: {.title}
Note
:::

To see all shipping methods for every shipper with a connector enabled,
navigate to
`Inventory app --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}.
:::

Select a shipping method to open its form. Alternatively, click
`New`{.interpreted-text role="guilabel"} to open a blank form, and
configure a new shipping method.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Enabling the FedEx shipping connector automatically creates two default
shipping methods: `FedEx US`{.interpreted-text role="guilabel"} and
`FedEx International`{.interpreted-text role="guilabel"}. Each of these
methods are pre-configured with test credentials, allowing them to be
used for testing purposes.

Before the shipping method can be used to create actual shipments, the
test credentials must be replaced with credentials from a valid FedEx
account.
:::

### General information

At the very top of a shipping method form are fields used to configure
the way the method operates in Odoo. In the `Provider`{.interpreted-text
role="guilabel"} field, select `FedEx`{.interpreted-text
role="guilabel"} from the drop-down menu, if it is not already selected.

The rest of the fields in this section are general to all shipping
providers. For details on how to fill them out, see the documentation on
`third-party shippers <third_party_shipper>`{.interpreted-text
role="doc"}.

### Fedex Configuration tab

The options in the `Fedex Configuration`{.interpreted-text
role="guilabel"} tab of a FedEx shipping method form are used to connect
the method to a FedEx account, and configure the shipping details
associated with the method (drop-off type, package type, etc.).

A FedEx business account is required to obtain the information needed to
fill out the fields in this tab. To create a new account, navigate to
FedEx\'s 
page, click on `Create Account`{.interpreted-text role="guilabel"}, and
follow the instructions.

#### Developer Key and Meter Number fields

A *developer key* is used to integrate a FedEx account with an external
service, like the Odoo **Inventory** app. A *meter number* is a unique
ID number used by FedEx to identify negotiated shipping rates for each
account.

To get a developer key and meter number, begin by navigating to FedEx\'s
[Developer Resource
Center](https://www.fedex.com/en-us/developer/web-services.html). Then,
click on the `FedEx Web
Services`{.interpreted-text role="guilabel"} drop-down menu.

Click `Get Test Key`{.interpreted-text role="guilabel"} to start the
process of getting a developer key and meter number which can be used to
configure a shipping method for testing purposes.

Click `Get Production Key`{.interpreted-text role="guilabel"} to start
the process of getting a developer key and meter number, which can be
used to configure a shipping method that generates real shipments with
FedEx.

After clicking either option, follow the instructions until the
`Confirmation`{.interpreted-text role="guilabel"} screen is reached.
This screen displays the developer key and meter number.

Once the developer key and meter number are determined, enter them in
the `Developer Key`{.interpreted-text role="guilabel"} and
`Meter Number`{.interpreted-text role="guilabel"} fields on the
`Fedex Configuration`{.interpreted-text role="guilabel"} tab of the
shipping method form.

#### Password and Account Number fields

A *password* is used, along with a username, to log into a FedEx
account. An *account number* is the unique number assigned to each FedEx
account.

To find a FedEx account number, log in to a FedEx account at
<https://www.fedex.com>. Click on the account holder\'s name in the
top-right corner of the screen, and select
`My Profile`{.interpreted-text role="menuselection"} from the drop-down
menu.

On the profile page, click `Account Management`{.interpreted-text
role="guilabel"} on the left side of the screen. The account number is
displayed on this screen.

Once the password and account number are determined, enter them in the
`Password`{.interpreted-text role="guilabel"} and
`Account Number`{.interpreted-text role="guilabel"} fields on the
`Fedex Configuration`{.interpreted-text role="guilabel"} tab of the
shipping method form.

#### Shipping details

The main section of the `Fedex Configuration`{.interpreted-text
role="guilabel"} tab includes a number of additional fields used provide
information about the shipping method:

-   `Fedex Service Type`{.interpreted-text role="guilabel"}: The FedEx
    service used to ship a package.
-   `Fedex Drop-Off Type`{.interpreted-text role="guilabel"}: The method
    for getting a package into FedEx\'s possession.
-   `Fedex Package Type`{.interpreted-text role="guilabel"}: The type of
    package used for the shipping method.
-   `Package Weight Unit`{.interpreted-text role="guilabel"}: The unit
    of measure used to weigh packages.
-   `Package Length Unit`{.interpreted-text role="guilabel"}: The unit
    of measure used to determine the dimensions of packages.
-   `Label Type`{.interpreted-text role="guilabel"}: The type of
    shipping label used for packages.
-   `Label Format`{.interpreted-text role="guilabel"}: The file format
    used by Odoo to generate shipping labels.
-   `Commercial Invoice Type`{.interpreted-text role="guilabel"}: The
    dimensions and type of the paper used to print invoices.

::: {.important}
::: {.title}
Important
:::

The options that should be selected on the
`Fedex Configuration`{.interpreted-text role="guilabel"} tab of a
shipping method depend on the negotiated shipping services of the
associated FedEx account. To confirm the available services for a FedEx
account, visit the *Account Management* page after logging in to the
FedEx website, or speak with a customer service representative.
:::

#### Options section

The `Options`{.interpreted-text role="guilabel"} section of the
`Fedex Configuration`{.interpreted-text role="guilabel"} tab provides a
few additional options to further configure the shipping method:

-   `Saturday Delivery`{.interpreted-text role="guilabel"}: Tick the
    checkbox to allow packages shipped with the delivery method to be
    delivered on Saturdays.
-   `Generate Return Label`{.interpreted-text role="guilabel"}: Tick the
    checkbox to automatically generate a return label upon validation of
    a delivery order.
-   `Duties paid by`{.interpreted-text role="guilabel"}: Use the
    drop-down menu to select whether duty charges should be paid by the
    `Sender`{.interpreted-text role="guilabel"} or
    `Recipient`{.interpreted-text role="guilabel"}.

Activate shipping method
------------------------

By default, shipping methods in Odoo are created within a *test
environment*. This means they can only be used for testing purposes, and
are unable to generate actual shipping orders.

To activate a shipping method in a *production environment*, click the
`fa-stop`{.interpreted-text role="icon"}
`Test Environment`{.interpreted-text role="guilabel"} smart button at
the top of the shipping method form. After doing so, the smart buttons
changes to read `fa-play`{.interpreted-text role="icon"}
`Production Environment`{.interpreted-text role="guilabel"}.

With the production environment enabled, validating a delivery order
using the shipping method generates an actual shipping label with FedEx.

Click the `fa-play`{.interpreted-text role="icon"}
`Production Environment`{.interpreted-text role="guilabel"} smart button
to return the shipping method to a test environment.

::: {.warning}
::: {.title}
Warning
:::

**Do not** enable the production environment for a shipping method
before it is ready to be used for actual shipping orders. Doing so may
lead to the creation of unwanted charges with FedEx.
:::
