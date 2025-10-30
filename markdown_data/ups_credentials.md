# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials.md

UPS integration
===============

UPS is a shipping carrier service that integrates with Odoo to
coordinate shipping to all regions. Once integrated, users can create
shipping methods that estimate shipping costs and `generate
labels <labels>`{.interpreted-text role="doc"}.

::: {.seealso}
`third_party_shipper`{.interpreted-text role="doc"}
:::

To set up the UPS shipping connector in Odoo, complete these steps:

1.  Create a UPS account to get `account number
    <inventory/shipping_receiving/ups-account-number>`{.interpreted-text
    role="ref"}
2.  Create UPS developer account to get `client credentials
    <inventory/shipping_receiving/ups-client-id>`{.interpreted-text
    role="ref"}
3.  Set up shipping method in Odoo

UPS account setup
-----------------

To get started, go to the  and click
the `Log In`{.interpreted-text role="guilabel"} button in the top-right
corner to log in or create a UPS account.

After logging in, click the profile icon in the top-right corner, and
select `Accounts and
Payment`{.interpreted-text role="guilabel"} from the drop-down menu.

{.align-center}

On the `Accounts and Payment Options`{.interpreted-text role="guilabel"}
page, two accounts must be configured: an Odoo shipment account and a
payment card.

### Shipping account

To add an Odoo shipment account, select
`Add New Account`{.interpreted-text role="guilabel"} from the `Add a
Payment Method`{.interpreted-text role="guilabel"} drop-down menu, and
click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

On the next screen, labeled `Open a Shipping Account`{.interpreted-text
role="guilabel"}, complete the forms to configure the shipping account
type (e.g. `Business`{.interpreted-text role="guilabel"}) and if any
regulated items will be shipped. Then finish the remaining three steps
in the wizard to `Add Addresses`{.interpreted-text role="guilabel"},
`Verify
Identity`{.interpreted-text role="guilabel"}, and
`Explore Discounts`{.interpreted-text role="guilabel"}, with the last
option being optional.

When complete, submit the application on the last page of the wizard to
finish setting up the shipping account.

{.align-center}

### Get account number {#inventory/shipping_receiving/ups-account-number}

With the shipping account set up, the UPS
`Account Number`{.interpreted-text role="guilabel"} becomes available.
To access it, navigate to
`Profile --> Accounts and Payment`{.interpreted-text
role="menuselection"} and refer to the shipping account\'s
`Number`{.interpreted-text role="guilabel"} field.

{.align-center}

### Payment card

Navigate back to the `Accounts and Payments`{.interpreted-text
role="guilabel"} page and select the `Add Payment
Card`{.interpreted-text role="guilabel"} option from the
`Add a Payment Method`{.interpreted-text role="guilabel"} drop-down
menu. Then, complete the form to add the credit card information.

{.align-center}

UPS developer account setup
---------------------------

Next, log into the  to
generate the developer key. To begin, click the profile icon in the
top-right corner, and choose the `Apps`{.interpreted-text
role="guilabel"} option from the drop-down menu.

{.align-center}

### Add app

Then, click the `Add Apps`{.interpreted-text role="guilabel"} button to
begin filling out the form. In the `I need
API credentials because \*`{.interpreted-text role="guilabel"} field,
select `I want to integrate UPS technology into my
business`{.interpreted-text role="guilabel"}.

Under the next label,
`Choose an account to associate with these credentials. \*`{.interpreted-text
role="guilabel"}, select `Add existing account`{.interpreted-text
role="guilabel"} from the drop-down menu in the corresponding field, and
then select the
`account number <inventory/shipping_receiving/ups-account-number>`{.interpreted-text
role="ref"} linked to the UPS account created in the previous step.

{.align-center}

Click `Next`{.interpreted-text role="guilabel"}, and proceed to the
`Add App`{.interpreted-text role="guilabel"} form, and fill out the
fields:

-   `App Name`{.interpreted-text role="guilabel"}: Type the name to
    identify the app by.
-   `Callback URL`{.interpreted-text role="guilabel"}: Type the URL of
    the Odoo database, in the format:
    [https://databaseName.odoo.com]{.title-ref}. Do **not** include
    [www]{.title-ref} in the URL.

In the `Add Products`{.interpreted-text role="guilabel"} section on the
right, search for and click the `+ (plus)`{.interpreted-text
role="guilabel"} icon to add the following products to the app:

-   `Authorization (O Auth)`{.interpreted-text role="guilabel"}: Used to
    generate the authorization token to request information from the UPS
    API.
-   `Address Validation`{.interpreted-text role="guilabel"}: Validates
    addresses at the street level in the United States and Puerto Rico.
-   `Locator`{.interpreted-text role="guilabel"}: Enables search for UPS
    shipping locations based on type and available services.
-   `Paperless Documents`{.interpreted-text role="guilabel"}: Enables
    the upload of document images to link to shipments.
-   `Shipping`{.interpreted-text role="guilabel"}: Enables UPS shipping
    services, such as preparing packages for shipment, managing returns,
    and canceling scheduled shipments.
-   `Rating`{.interpreted-text role="guilabel"}: Compare delivery
    services and shipping rates.

Finally, click `Save`{.interpreted-text role="guilabel"} and accept
UPS\'s terms and conditions.

::: {.seealso}

:::

{.align-center}

### Client ID and Client Secret {#inventory/shipping_receiving/ups-client-id}

With the new app created, in the
`Profile --> My Apps --> App`{.interpreted-text role="menuselection"}
page, select the app from the `Credentials`{.interpreted-text
role="guilabel"} section to view the UPS credentials.

{.align-center}

In the `Credentials`{.interpreted-text role="guilabel"} section, copy
the `Client ID`{.interpreted-text role="guilabel"} and
`Client Secret`{.interpreted-text role="guilabel"} key.

{.align-center}

Setup in Odoo
-------------

With the credentials obtained, configure the UPS shipping method in Odoo
by going to
`Inventory app --> Configuration --> Shipping Methods`{.interpreted-text
role="menuselection"}.

On the `Shipping Methods`{.interpreted-text role="guilabel"} page, click
the `New`{.interpreted-text role="guilabel"} button.

::: {.note}
::: {.title}
Note
:::

For existing UPS shipping methods whose `Provider`{.interpreted-text
role="guilabel"} is `UPS Legacy`{.interpreted-text role="guilabel"},
archive it and create a new shipping method using
`UPS`{.interpreted-text role="guilabel"}.
:::

In the `Provider`{.interpreted-text role="guilabel"} field, select
`UPS`{.interpreted-text role="guilabel"}. Doing so reveals the `UPS
Configuration`{.interpreted-text role="guilabel"} tab, where various
fields must be entered. For details instructions on configuring the
other fields on the shipping method, refer to the
`Configure third-party carrier
<third_party_shipper>`{.interpreted-text role="doc"} documentation.

In the `UPS Configuration`{.interpreted-text role="guilabel"} tab,
complete the following fields:

-   `UPS Account Number`{.interpreted-text role="guilabel"}:
    (*required*) Get the `account number
    <inventory/shipping_receiving/ups-account-number>`{.interpreted-text
    role="ref"} from the UPS portal.
-   `UPS Client ID`{.interpreted-text role="guilabel"}: (*required*) Get
    the `Client ID
    <inventory/shipping_receiving/ups-client-id>`{.interpreted-text
    role="ref"} from the UPS developer website.
-   `UPS Client Secret`{.interpreted-text role="guilabel"}: (*required*)
    Get the `Client Secret
    <inventory/shipping_receiving/ups-client-id>`{.interpreted-text
    role="ref"} key from the UPS developer website.
-   `UPS Service Type`{.interpreted-text role="guilabel"}: Select from
    the drop-down menu the type of shipping service.
-   `UPS Package Type`{.interpreted-text role="guilabel"}: (*required*)
    Select from the drop-down menu the `package type
    <../../product_management/configure/package>`{.interpreted-text
    role="doc"} that is supported for the shipping service.
-   `Package Weight Unit`{.interpreted-text role="guilabel"}: The unit
    of measure for the package weight.
-   `Package Size Unit`{.interpreted-text role="guilabel"}: The unit of
    measure for the package dimensions.
-   `Label Format`{.interpreted-text role="guilabel"}: Choose the label
    format shipping labels: `PDF`{.interpreted-text role="guilabel"},
    `ZPL`{.interpreted-text role="guilabel"}, `EPL`{.interpreted-text
    role="guilabel"}, or `SPL`{.interpreted-text role="guilabel"}.

{.align-center}

In the `Options`{.interpreted-text role="guilabel"} section, the
following features are available:

-   `Bill My Account`{.interpreted-text role="guilabel"}: Charge the
    user\'s UPS account for shipping in the *eCommerce* app.
-   `Collect on Delivery`{.interpreted-text role="guilabel"}: Collect
    payment from customers for shipping after the shipment is delivered.
-   `Generate Return Label`{.interpreted-text role="guilabel"}: Print
    the return label for the order after the delivery order is
    validated.
-   `Duties paid by`{.interpreted-text role="guilabel"}: Select whether
    duties or other fees are charged to the `Sender`{.interpreted-text
    role="guilabel"} or `Recipient`{.interpreted-text role="guilabel"}
    of the order.
