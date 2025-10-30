eBay connector setup
====================

Overview
--------

Odoo\'s eBay connector allows eBay listings to connect with Odoo
products. Once connected,
`updates to the listings <linking_listings>`{.interpreted-text
role="doc"} can be made in Odoo or in eBay. When an item sells on eBay,
draft *sales orders* are created in Odoo for the user to review and
confirm. Once the sales order is confirmed, Odoo *Inventory* and *Sales*
apps function standard to pull products out of inventory, and allow the
user to create invoices.

::: {.seealso}
To learn more about the eBay connector visit these pages as well:

-   `manage`{.interpreted-text role="doc"}
-   `linking_listings`{.interpreted-text role="doc"}
-   `troubleshooting`{.interpreted-text role="doc"}
:::

### eBay - Odoo linked fields

The following are eBay product details. Each of these eBay fields update
corresponding fields in Odoo.

-   eBay URL
-   eBay status
-   Quantity sold
-   Start date
-   Title
-   Subtitle
-   Item condition
-   Category
-   Category 2
-   Store category
-   Store category 2
-   Payment policy
-   Seller profiles
-   Postal code
-   Shipping policy
-   Listing type (fixed price or auction)
    -   Starting price for Auction
    -   Buy it now price
    -   Fixed Price amount
-   Use stock quantity
-   Quantity on eBay
-   Duration
-   Allow best offer
-   Private listing
-   eBay description
-   eBay product image
-   Country

### eBay terms

*Variations* group multiple products into one, with variation (or
variant) options. Variations can sync to Odoo\'s attributes and values.
Variations will appear in drop down menus near the top of the page when
viewing an eBay listing. These are comparable to product variants in
Odoo.

{.align-center}

*Item specifics*, located at the bottom of the listing, detail
product-specific information. These specifics don\'t sync with Odoo
fields by default; a development is required to link these fields.

{.align-center}

*Sandbox* and *Production* are terms that are used to categorize the
eBay environments as either still in development/testing (*Sandbox*) or
for use in the real instance of the database with real customer
information/dataset (*Production*). It is recommended to start first in
the *Sandbox* to test, and then following the processes below, create a
*Production* instance.

::: {.tip}
::: {.title}
Tip
:::

eBay\'s sandbox environment can be accessed by navigating to [eBay\'s
sandbox portal](https://sandbox.ebay.com/) at
[https://sandbox.ebay.com/]{.title-ref}. eBay\'s production environment
can be accessed by navigating to [eBay.com
portal](https://www.ebay.com/) or [https://www.ebay.com/]{.title-ref}.
:::

::: {.important}
::: {.title}
Important
:::

The environment selection **must** remain the same for all environment
settings on eBay and on Odoo throughout this setup.
:::

### eBay actions available on Odoo

The following are built-in actions in Odoo that add or update eBay
listings:

-   **List**/ **Link**: generate a new eBay listing with an Odoo product
    by clicking `List
    Item on eBay`{.interpreted-text role="guilabel"} or
    `Link With Existing eBay Listing`{.interpreted-text
    role="guilabel"}.
-   `Revise item`{.interpreted-text role="guilabel"} button: after
    making changes to an eBay listing in Odoo, save the record, and then
    click the `Revise Item`{.interpreted-text role="guilabel"} in Odoo
    to update the eBay listing.
-   **Relist**: if an item\'s listing was ended early or
    `auto-relist`{.interpreted-text role="guilabel"} was not selected, a
    user can relist the item from Odoo. The start date will reset.
-   `End item's listing`{.interpreted-text role="guilabel"} button: end
    a listing on eBay directly from Odoo.
-   **Unlink product listings**: users can unlink a product from the
    eBay listing; the listing will stay intact on eBay.

Setup required on Odoo prior to eBay setup
------------------------------------------

To link eBay with Odoo, install the eBay module by navigating to the
Odoo dashboard and clicking into the `Apps`{.interpreted-text
role="guilabel"} application. Search the term [eBay]{.title-ref} and
install the [eBay Connector]{.title-ref} module.

The following items must be configured before eBay is set up:

-   In Odoo, create and configure products that are intended to be
    listed in eBay. eBay does not import new products into Odoo. All
    products must first be created in Odoo, and then linked to listings.

    -   Odoo does not allow multiple eBay listings to be linked per
        product in Odoo. If the company sells the same product for
        multiple listings, follow these instructions:

        -   Set up one *base* product (noted in the
            `Component`{.interpreted-text role="guilabel"} field of the
            `BoM (Bill
            of Materials)`{.interpreted-text role="abbr"}) from which
            all eBay listings will pull from. This will be a storable
            product so stock can be kept. Highlighted in green below,
            this product will be included in the kit on each subsequent
            "linked" product below.
        -   Set up 2+ *linked* products (noted in the
            `Product`{.interpreted-text role="guilabel"} field of the
            `BoM (Bill
            of Materials)`{.interpreted-text role="abbr"}, one for each
            eBay listing. The product type will be determined by the
            company\'s accounting settings, as explained in the Odoo
            documentation. Highlighted in yellow below, each product
            should have a `BoM type`{.interpreted-text role="guilabel"}
            equal to `Kit`{.interpreted-text role="guilabel"} and have
            the base product as a `Component`{.interpreted-text
            role="guilabel"} of the kit. When this linked eBay product
            is sold, the delivery order created will have the base
            product listed in lieu of the linked product.

        {.align-center}

    > ::: {.seealso}
    > `../../../inventory_and_mrp/manufacturing/basic_setup/bill_configuration/`{.interpreted-text
    > role="doc"}
    > :::

-   eBay does not automatically create invoices for eBay orders that get
    pushed into Odoo. Set invoicing policy on eBay products: invoicing
    policy will dictate when the product can be invoiced. Since most
    eBay users collect payment before the product is shipped, "invoice
    on ordered" will allow users to mass create invoices for eBay orders
    every day.

-   Set the `Outgoing Shipments`{.interpreted-text role="guilabel"}
    route for the warehouse to `Deliver goods
    directly (1 step)`{.interpreted-text role="guilabel"}.

    ::: {.warning}
    ::: {.title}
    Warning
    :::

    When the `Outgoing Shipments`{.interpreted-text role="guilabel"}
    route is set to two or three steps, a known bug occurs: eBay wrongly
    marks orders as delivered when the pick operation in Odoo is
    confirmed. The expected behavior is to mark orders as delivered
    **after** the *delivery order* is confirmed. This mislabeling
    prevents tracking numbers in eBay from being imported onto the
    delivery order.
    :::

-   If the Accounting/Invoicing apps are installed, practice registering
    payment and reconciling invoices created from eBay orders with
    incoming eBay money.

    ::: {.seealso}
    `../../..//finance/accounting/bank/reconciliation`{.interpreted-text
    role="doc"}
    :::

-   Generate a marketplace account deletion/closure notification token.
    To begin, navigate to
    `Sales app --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}. Under the `eBay`{.interpreted-text
    role="guilabel"} heading, change the mode to
    `Production`{.interpreted-text role="guilabel"}, and input random
    text values for the `Production Cert Key`{.interpreted-text
    role="guilabel"}. Then click the `Generate Token`{.interpreted-text
    role="guilabel"} button under the
    `eBay Marketplace Account Deletion/Closure Notifications`{.interpreted-text
    role="guilabel"} section. This token will be used during the setup
    on eBay for the deletion/closure notifications configuration.

{.align-center}

Set up on eBay
--------------

### Set up eBay developer account

To start, create an eBay developer account via [eBay\'s developer
portal](https://go.developer.ebay.com/). This site requires a different
login and password than the eBay account, though the same email address
can be used to register. The verification to create a developer account
is around 24 hours.

### Set up eBay keyset

Once the eBay developer account is created, set up an application on
. Next,
navigate to the `Hi [username]`{.interpreted-text role="guilabel"}
heading at top right of screen, then from the drop-down menu options,
click `Application Keysets`{.interpreted-text role="guilabel"}. Doing so
opens a pop-up that prompts the user to
`Enter Application Title`{.interpreted-text role="guilabel"} (up to
fifty characters), and choose a development environment
(`Sandbox`{.interpreted-text role="guilabel"} or
`Production`{.interpreted-text role="guilabel"}). These two fields
generate first keyset. This application title is not saved until the
keyset is generated. Click on `Create a keyset`{.interpreted-text
role="guilabel"} to generate the keyset.

::: {.warning}
::: {.title}
Warning
:::

The newly created *production keyset* is disabled by default. Activate
it by subscribing to the eBay Marketplace \'account deletion or closure
notifications\' or by applying to eBay for an exemption. Once enabled,
the database can make 5000 calls per day using this keyset.
:::

{.align-center}

#### Configure account deletion / notification settings (Production)

To configure notifications or delete the database on a production
environment, navigate to the [eBay developer
portal](https://go.developer.ebay.com/). Configure the account
deletion/notification settings in eBay by navigating to the [Hi
\[username\]]{.title-ref} at top right of screen, then
`Application Keysets`{.interpreted-text role="guilabel"}.

Next, click the
`marketplace deletion/account closure notification`{.interpreted-text
role="guilabel"} option under the `Production`{.interpreted-text
role="guilabel"} keyset column. Enter an email under
`Email to notify if marketplace
account deletion notification endpoint is down`{.interpreted-text
role="guilabel"}. Click `Save`{.interpreted-text role="guilabel"} to
enable the email.

Following this action, enter the
`Marketplace account deletion notification endpoint`{.interpreted-text
role="guilabel"} URL provided by Odoo. This HTTPs endpoint is found in
Odoo by navigating to `Sales app
--> Configuration --> Settings`{.interpreted-text role="menuselection"},
in the `eBay Marketplace Account Deletion/Closure
Notifications`{.interpreted-text role="guilabel"} field.

Clicking the `Generate Token`{.interpreted-text role="guilabel"} button
in Odoo below this field creates a verification token for the eBay
production environment. In Odoo, `Copy`{.interpreted-text
role="guilabel"} the newly created token and navigate to eBay to fill in
the `Verification token`{.interpreted-text role="guilabel"} field. Click
`Save`{.interpreted-text role="guilabel"} to enable the
`Event Notification Delivery Method`{.interpreted-text role="guilabel"}.

{.align-center}

After completing the above fields, click
`Send Test Notification`{.interpreted-text role="guilabel"} to test the
new notifications. Proceed to the next step when the green check mark
appears. Revisit the above settings if the test post is not as expected.

After configuring notification settings, go back to the
`Application Keys`{.interpreted-text role="menuselection"} page to
generate production keysets.

#### Creating the keyset

A successful setup of the notifications enables the ability to create
Production Keysets which are needed in the remainder of the Odoo
configuration. Navigate back to the `Application
Keys`{.interpreted-text role="menuselection"} page generate a production
keyset.

The administrator is prompted to
`Confirm the Primary Contact`{.interpreted-text role="menuselection"}.
Enter or confirm the account owner (the person legally responsible for
the eBay API License Agreement). Fill out `First Name`{.interpreted-text
role="guilabel"}, `Last Name`{.interpreted-text role="guilabel"},
`Email`{.interpreted-text role="guilabel"}, `Phone`{.interpreted-text
role="guilabel"}. Then, select either the `Individual`{.interpreted-text
role="guilabel"} or `Business`{.interpreted-text role="guilabel"}
options.

::: {.note}
::: {.title}
Note
:::

The provided email address or phone number does **not** have to match
the account\'s. eBay uses this information to contacting the business or
individual in case of issues with user tokens. Additional contacts can
be added from the `Profile & Contacts`{.interpreted-text
role="guilabel"} page on eBay.
:::

Click on `Continue to Create Keys`{.interpreted-text role="guilabel"} to
confirm the primary contact. The `Application Keys`{.interpreted-text
role="guilabel"} populates in a new screen and an email is also sent to
the developer account. An `App ID (Client ID)`{.interpreted-text
role="guilabel"}, `Dev ID`{.interpreted-text role="guilabel"}, and
`Cert ID (Client
Secret)`{.interpreted-text role="guilabel"} all populate.

{.align-center}

Copy these values down as they will be input into Odoo later in the
process.

### Create eBay user token

Now, create a *user token* in eBay by navigating to the [Hi
\[username\]]{.title-ref} at top right of screen, then
`User Access Tokens`{.interpreted-text role="guilabel"}.

{.align-center}

Select the correct `Environment`{.interpreted-text role="guilabel"}:
`Sandbox`{.interpreted-text role="guilabel"} for testing or
`Production`{.interpreted-text role="guilabel"} for the live database.
Maintain the same selection for all environment settings on both eBay
and Odoo.

Next, select the radio button labeled `Auth'n'Auth`{.interpreted-text
role="guilabel"}.

Choose `Sign in to Production`{.interpreted-text role="guilabel"} or
`Sign in to Sandbox`{.interpreted-text role="guilabel"} to get a user
token in the chosen environment. This button varies based on the
selection made above for either `Sandbox`{.interpreted-text
role="guilabel"} or `Production`{.interpreted-text role="guilabel"}.

Doing so triggers a a pop-up window to
`Confirm your Legal Address`{.interpreted-text role="guilabel"}.
Complete the required fields, which are `First Name`{.interpreted-text
role="guilabel"}, `Last Name`{.interpreted-text role="guilabel"},
`Primary Email`{.interpreted-text role="guilabel"},
`Legal Address`{.interpreted-text role="guilabel"}, and
`Account Type`{.interpreted-text role="guilabel"}. For
`Account Type`{.interpreted-text role="guilabel"}, select either
`Individual`{.interpreted-text role="guilabel"} or
`Business`{.interpreted-text role="guilabel"}. To complete the
confirmation, click `Sign
into eBay to get a Token`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

eBay will contact this individual or business should there be any issues
with the application keys. Other contacts can be added on the
`Profile & Contacts`{.interpreted-text role="menuselection"} eBay page.
:::

The administrator will be redirected to either a sandbox or production
sign-in page for eBay. This login is different than the eBay
developer\'s console, it is the eBay account where the items will be
sold on. This email and/or login can differ from the eBay developer
account.

Enter the `Email`{.interpreted-text role="guilabel"} or
`Username`{.interpreted-text role="guilabel"} for the eBay account and
sign into the eBay account.

::: {.important}
::: {.title}
Important
:::

Should an additional user be needed for the sandbox simulation, a test
user needs to be created. Visit [eBay\'s Register for Sandbox
form](https://developer.ebay.com/sandbox/register). Detailed
instructions can be found on eBay\'s help pages: [Create a test Sandbox
user](https://developer.ebay.com/api-docs/static/gs_create-a-test-sandbox-user.html).
:::

### Grant application access

After signing into the production or sandbox environment, eBay presents
the administrator with an *agreement* to grant access to the user\'s
eBay data.

Clicking `Agree`{.interpreted-text role="guilabel"} allows eBay to link
the eBay account with the *application programming interface* (API).
This agreement can be changed at any time by visiting eBay\'s account
preferences.

::: {.warning}
::: {.title}
Warning
:::

eBay has a timed sequence between signing in and agreeing to the terms
for the `API
(Application Programming Interface)`{.interpreted-text role="abbr"}
linkage to the account. Once complete a `User
Token`{.interpreted-text role="guilabel"} will populate on the
`User Tokens`{.interpreted-text role="menuselection"} page.
:::

A `User Token`{.interpreted-text role="guilabel"} will populate on the
screen. Make sure to copy this token down as it will be used in the next
steps along with the `Application Keyset`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Signing in to the eBay account is necessary to create to the token. The
eBay developer can also revoke the token by clicking on the
`Revoke a Token`{.interpreted-text role="guilabel"} link.
:::

### API explorer

Now that the `Application Keyset`{.interpreted-text role="guilabel"} and
`User Token`{.interpreted-text role="guilabel"} have been created, a
test can be executed via the [API
Explorer](https://developer.ebay.com/DevZone/build-test/test-tool/default.aspx)
to ensure that the
`API (Application Programming Interface)`{.interpreted-text role="abbr"}
is configured correctly. This test will execute a simple search using
the `API (Application Programming Interface)`{.interpreted-text
role="abbr"}.

To begin the `API (Application Programming Interface)`{.interpreted-text
role="abbr"} test, click on `Get OAuth
Application Token`{.interpreted-text role="guilabel"}. This will
populate the key into the `Token`{.interpreted-text role="guilabel"}
field.

A basic search function is set to execute. Click on
`Execute`{.interpreted-text role="guilabel"} to complete the test. A
successful test will respond with a `Call Response`{.interpreted-text
role="guilabel"} of [200 OK]{.title-ref} with a corresponding
`Time`{.interpreted-text role="guilabel"}.

Entering credentials into Odoo
------------------------------

The previously copied `User Token`{.interpreted-text role="guilabel"}
and `Application Keyset`{.interpreted-text role="guilabel"} are now
ready to be entered into the Odoo database.

Navigate back the eBay settings in Odoo
(`Sales app --> Configuration --> Settings
--> eBay`{.interpreted-text role="menuselection"}) and paste the
following credentials from eBay into the corresponding fields in Odoo.

  Platform   Dev Key/ID      Token                      App Key/ID                   Cert Key/ID
  ---------- --------------- -------------------------- ---------------------------- -----------------------------
  eBay       Dev ID          User Token                 App ID (Client ID)           Cert ID (Client Secret)
  Odoo       Developer Key   Production/Sandbox Token   Production/Sandbox App Key   Production/Sandbox Cert Key

::: {.important}
::: {.title}
Important
:::

The `Application Keyset`{.interpreted-text role="guilabel"} can be
accessed by going to [eBay\'s developer
portal](https://go.developer.ebay.com/) and navigate to the [Hi
\[username\]]{.title-ref} at top right of screen, then click on
`Application Keysets`{.interpreted-text role="guilabel"}. Get to the
*User Token* in eBay by navigating to the [Hi \[username\]]{.title-ref}
at top right of screen, then `User Access Tokens`{.interpreted-text
role="guilabel"} and click on `Sign in to Sandbox`{.interpreted-text
role="guilabel"}. The `User Token`{.interpreted-text role="guilabel"}
can also be accessed by clicking on `User Tokens`{.interpreted-text
role="guilabel"} from the `Application Keys`{.interpreted-text
role="menuselection"} page.
:::

Confirm that the setup is correct by saving the credentials in Odoo.
Once the initial setup is complete, a new menu tab in products will
appear called [eBay]{.title-ref} with the option to `Sell on
eBay`{.interpreted-text role="guilabel"}. See the
`manage`{.interpreted-text role="doc"} documentation on how to list
products.

::: {.tip}
::: {.title}
Tip
:::

Sync product categories by clicking
`Product Categories`{.interpreted-text role="guilabel"}. After syncing,
a new menu item, [eBay Category]{.title-ref}, appears available for
products to be configured with. These eBay categories are imported from
the Odoo database and are available when listing an item on eBay through
Odoo.

::: {.important}
::: {.title}
Important
:::

If Product Categories beyond four paths are required, users will need to
manually add those paths. This has historically been done by getting a
list of all product categories beyond four paths, manually importing
them into the Product Category model in Odoo, and then linking them
individually to the product.
:::
:::

::: {.seealso}
Now that the setup is complete, proceed to either:

-   `Create listings <manage>`{.interpreted-text role="doc"}
-   `Link existing listings <linking_listings>`{.interpreted-text
    role="doc"}
:::
