Product images with Google Images
=================================

Having appropriate product images in Odoo is useful for a number of
reasons. However, if a lot of products need images, assigning them can
become incredibly time-consuming.

Fortunately, by configuring the *Google Custom Search* API within an
Odoo database, finding product images for products (based on their
barcode) is extremely efficient.

Configuration {#product_images/configuration}
-------------

In order to utilize *Google Custom Search* within an Odoo database, both
the database and the Google API must be properly configured.

::: {.note}
::: {.title}
Note
:::

Free Google accounts allow users to select up to 100 free images per
day. If a higher amount is needed, a billing upgrade is required.
:::

### Google API dashboard {#product_images/google-api-dashboard}

1.  Go to the [Google Cloud Platform API &
    Services](https://console.developers.google.com/) page to generate
    Google Custom Search API credentials. Then, log in with a Google
    account. Next, agree to their `Terms of Service`{.interpreted-text
    role="guilabel"} by checking the box, and clicking `Agree and
    Continue`{.interpreted-text role="guilabel"}.

2.  From here, select (or create) an API project to store the
    credentials. Start by giving it a memorable
    `Project Name`{.interpreted-text role="guilabel"}, select a
    `Location`{.interpreted-text role="guilabel"} (if any), then click
    `Create`{.interpreted-text role="guilabel"}.

3.  With the `Credentials`{.interpreted-text role="guilabel"} option
    selected in the left sidebar, click `Create
    Credentials`{.interpreted-text role="guilabel"}, and select
    `API key`{.interpreted-text role="guilabel"} from the drop-down
    menu.

    {.align-center}

4.  Doing so reveals an `API key created`{.interpreted-text
    role="guilabel"} pop-up window, containing a custom `API
    key`{.interpreted-text role="guilabel"}. Copy and save
    `Your API key`{.interpreted-text role="guilabel"} in the pop-up
    window \-- it will be used later. Once the key is copied (and saved
    for later use), click `Close`{.interpreted-text role="guilabel"} to
    remove the pop-up window.

    {.align-center}

5.  On this page, search for [Custom Search API]{.title-ref}, and select
    it.

    {.align-center}

6.  From the `Custom Search API`{.interpreted-text role="guilabel"}
    page, enable the API by clicking `Enable`{.interpreted-text
    role="guilabel"}.

    {.align-center}

### Google Programmable Search dashboard {#product_images/google-pse-dashboard}

1.  Next, go to [Google Programmable Search
    Engine](https://programmablesearchengine.google.com/), and click
    either of the `Get started`{.interpreted-text role="guilabel"}
    buttons. Log in with a Google account, if not already logged in.

    {.align-center}

2.  On the `Create a new search engine`{.interpreted-text
    role="guilabel"} form, fill out the name of the search engine, along
    with what the engine should search, and be sure to enable
    `Image Search`{.interpreted-text role="guilabel"} and
    `SafeSearch`{.interpreted-text role="guilabel"}.

    {.align-center}

3.  Validate the form by clicking `Create`{.interpreted-text
    role="guilabel"}.

4.  Doing so reveals a new page with the heading:
    `Your new search engine has been
    created`{.interpreted-text role="guilabel"}.

    {.align-center}

5.  From this page, click `Customize`{.interpreted-text role="guilabel"}
    to open the `Overview --> Basic`{.interpreted-text
    role="menuselection"} page. Then, copy the ID in the
    `Search engine ID`{.interpreted-text role="guilabel"} field. This ID
    is needed for the Odoo configuration.

    {.align-center}

### Odoo {#product_images/setup-in-odoo}

1.  In the Odoo database, go to the `Settings app`{.interpreted-text
    role="menuselection"} and scroll to the
    `Integrations`{.interpreted-text role="guilabel"} section. From
    here, check the box beside `Google Images`{.interpreted-text
    role="guilabel"}. Then, click `Save`{.interpreted-text
    role="guilabel"}.

    {.align-center}

2.  Next, return to the `Settings app`{.interpreted-text
    role="menuselection"}, and scroll to the
    `Integrations`{.interpreted-text role="guilabel"} section. Then,
    enter the `API Key`{.interpreted-text role="guilabel"} and
    `Search Engine ID`{.interpreted-text role="guilabel"} in the fields
    beneath the `Google Images`{.interpreted-text role="guilabel"}
    feature.

3.  Click `Save`{.interpreted-text role="guilabel"}.

Product images in Odoo with Google Custom Search API {#product_images/get-product-images}
----------------------------------------------------

Adding images to products in Odoo can be done on any product or product
variant. This process can be completed in any Odoo application that
provides access to product pages (e.g. *Sales* app, *Inventory* app,
etc.).

Below is a step-by-step guide detailing how to utilize the *Google
Custom Search API* to assign images to products in Odoo using the Odoo
*Sales* application:

1.  Navigate to the `Products`{.interpreted-text role="guilabel"} page
    in the *Sales* app (`Sales app -->
    Products --> Products`{.interpreted-text role="menuselection"}). Or,
    navigate to the `Product Variants`{.interpreted-text
    role="guilabel"} page in the *Sales* app
    (`Sales app --> Products --> Product Variants`{.interpreted-text
    role="menuselection"}).

2.  Select the desired product that needs an image.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Only products (or product variants) that have a barcode, but **not**
    an image, are processed.

    If a product with one or more variants is selected, each variant
    that matches the aforementioned criteria is processed.
    :::

3.  Click the `Action ⚙️ (gear)`{.interpreted-text role="guilabel"} icon
    on the product page, and select `Get
    Pictures from Google Images`{.interpreted-text role="guilabel"} from
    the menu that pops up.

    {.align-center}

4.  On the pop-up window that appears, click
    `Get Pictures`{.interpreted-text role="guilabel"}.

    {.align-center}

5.  Once clicked, the image(s) will appear incrementally.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Only the first 10 images are fetched immediately. If you selected
    more than 10, the rest are fetched as a background job.

    The background job processes about 100 images in a minute. If the
    quota authorized by Google (either with a free or a paid plan) is
    reached, the background job puts itself on hold for 24 hours. Then,
    it will continue where it stopped the day before.
    :::

::: {.seealso}
[Create, modify, or close your Google Cloud Billing
account](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
:::
