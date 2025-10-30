# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/products.md

show-content

:   

Products
========

**Odoo eCommerce** allows you to
`add products <ecommerce/products/add-products>`{.interpreted-text
role="ref"} and manage your
`product pages <ecommerce/products/product-page>`{.interpreted-text
role="ref"} directly from the Website app. It also allows you to add
`product variants <ecommerce/products/product-variants>`{.interpreted-text
role="ref"} and
`digital files <ecommerce/products/digital-files>`{.interpreted-text
role="ref"},
`translating <ecommerce/products/translation>`{.interpreted-text
role="ref"} the product page content,
`managing stock <ecommerce/products/stock-management>`{.interpreted-text
role="ref"}, and enabling
`product comparisons <ecommerce/products/product-comparison>`{.interpreted-text
role="ref"}.

Add products {#ecommerce/products/add-products}
------------

### Create products {#ecommerce/products/create-products}

To create a product from the frontend, click `+ New`{.interpreted-text
role="guilabel"} in the top-right corner, then
`Product`{.interpreted-text role="guilabel"}. Enter the
`Product Name`{.interpreted-text role="guilabel"},
`Sales Price`{.interpreted-text role="guilabel"}, the default
`Customer Taxes`{.interpreted-text role="guilabel"} for local
transactions, and `Save`{.interpreted-text role="guilabel"}. You can
then update the product\'s details, add an image, and
`customize <ecommerce/products/customization>`{.interpreted-text
role="ref"} the product page. When you `Save`{.interpreted-text
role="guilabel"}, the product page is automatically published.

::: {.tip}
::: {.title}
Tip
:::

\- You can also create a product from the backend by going to
`Website --> eCommerce --> Products`{.interpreted-text
role="menuselection"} and clicking `New`{.interpreted-text
role="guilabel"}. - Products created from the frontend are automatically
`published <website/un-publish-page>`{.interpreted-text role="ref"},
while products created from the backend are not. To publish a product,
click the `Go to Website`{.interpreted-text role="guilabel"} smart
button to access the product page, then toggle the switch from
`Unpublished`{.interpreted-text role="guilabel"} to
`Published`{.interpreted-text role="guilabel"}.
:::

### Import products {#ecommerce/products/import-products}

To `import product data <import-data>`{.interpreted-text role="ref"}
using XLSX or CSV files, go to
`Website --> eCommerce --> Products`{.interpreted-text
role="menuselection"}, click the `fa-cog`{.interpreted-text role="icon"}
(`gear`{.interpreted-text role="guilabel"}) icon, then
`Import records <import-data>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To publish **large batches** of products, follow these steps:

1.  Go to `Website --> eCommerce --> Products`{.interpreted-text
    role="menuselection"}.
2.  Remove the `Published`{.interpreted-text role="guilabel"} filter and
    switch to the `List`{.interpreted-text role="guilabel"} view.
3.  Click the `fa-sliders`{.interpreted-text role="icon"}
    (`dropdown toggle`{.interpreted-text role="guilabel"}) icon and
    enable `Is published`{.interpreted-text role="guilabel"}.
4.  Click the `Is Published`{.interpreted-text role="guilabel"} column
    to re-order it by **published** or **unpublished** products.
5.  Select the products to publish by ticking their box.
6.  In the `Is Published`{.interpreted-text role="guilabel"} column,
    tick the box for any of the selected products, then
    `Confirm`{.interpreted-text role="guilabel"} to publish them.
:::

Shop page {#ecommerce/products/shop-page}
---------

To customize the layout of the main `Shop`{.interpreted-text
role="guilabel"} page or modify its content, click
`Edit`{.interpreted-text role="guilabel"}. Go to the
`Blocks`{.interpreted-text role="guilabel"} tab to add `building blocks
<../../websites/website/web_design/building_blocks>`{.interpreted-text
role="doc"} or to the `Customize`{.interpreted-text role="guilabel"} tab
to change the page layout or add features:

-   `Layout`{.interpreted-text role="guilabel"}: Select
    `Grid`{.interpreted-text role="guilabel"} or
    `List`{.interpreted-text role="guilabel"}.

    > -   `Size`{.interpreted-text role="guilabel"}: Set the number of
    >     products displayed per page and line.
    > -   `Style`{.interpreted-text role="guilabel"}: Select
    >     `Default`{.interpreted-text role="guilabel"},
    >     `Cards`{.interpreted-text role="guilabel"},
    >     `Thumbnails`{.interpreted-text role="guilabel"}, or
    >     `Grid`{.interpreted-text role="guilabel"}.
    > -   `Image Size`{.interpreted-text role="guilabel"}: Choose the
    >     aspect ratio for the product images:
    >     `Landscape (4/3)`{.interpreted-text role="guilabel"},
    >     `Default (1/1)`{.interpreted-text role="guilabel"},
    >     `Portrait (4/5)`{.interpreted-text role="guilabel"}, or
    >     `Vertical (2/3)`{.interpreted-text role="guilabel"}. You can
    >     also adjust the display by changing the
    >     `Fill`{.interpreted-text role="guilabel"} options to best fit
    >     your design preferences.

-   

    `Search Bar`{.interpreted-text role="guilabel"}: Toggle the switch to display a search bar at the top of the products

    :   page.

-   `Prod. Desc.`{.interpreted-text role="guilabel"}: Toggle the switch
    to display the product description below the product\'s name.

-   `Categories`{.interpreted-text role="guilabel"}: display product
    categories on the `Left`{.interpreted-text role="guilabel"}, on the
    `Top`{.interpreted-text role="guilabel"}, or both. If
    `Left`{.interpreted-text role="guilabel"} is selected, you can
    enable `Collapse Categories`{.interpreted-text role="guilabel"} to
    make the category menu collapsible.

-   `Datepicker`{.interpreted-text role="guilabel"}: Toggle the switch
    to display a date range calendar to check the availability of rental
    products over a specific period. The
    `Rental app <../../sales/rental>`{.interpreted-text role="doc"} must
    be installed to use this feature.

-   `Attributes`{.interpreted-text role="guilabel"}: Show product
    attributes on the `Left`{.interpreted-text role="guilabel"} and/or
    display a `fa-sliders`{.interpreted-text role="icon"}
    (`dropdown toggle`{.interpreted-text role="guilabel"}) icon at the
    `Top`{.interpreted-text role="guilabel"} allowing customers to
    filter products based on their attributes.

    -   `Price Filter`{.interpreted-text role="guilabel"}: Toggle the
        switch to display a `Price Range`{.interpreted-text
        role="guilabel"} bar, which allows customers to filter products
        according to a specific price range by dragging adjustable
        handles.
    -   `Product Tags`{.interpreted-text role="guilabel"}: Toggle the
        switch to display the `Product Template Tags`{.interpreted-text
        role="guilabel"} on the product page and allow customers to
        filter products using those tags by going to the
        `Tags`{.interpreted-text role="guilabel"} section in the left
        column.

-   `Top Bar`{.interpreted-text role="guilabel"}: Select
    `Sort By`{.interpreted-text role="guilabel"} to display a dropdown
    list in the top bar for sorting products and/or
    `Layout`{.interpreted-text role="guilabel"} to allow customers to
    switch to the grid or list view using the related icons.

-   `Default Sort`{.interpreted-text role="guilabel"}: Choose how
    products are sorted by default: `Featured`{.interpreted-text
    role="guilabel"}, `Newest Arrivals`{.interpreted-text
    role="guilabel"}, `Name (A-Z)`{.interpreted-text role="guilabel"},
    `Price - Low to High`{.interpreted-text role="guilabel"}, or
    `Price - High to Low`{.interpreted-text role="guilabel"}.

-   `Buttons`{.interpreted-text role="guilabel"}:

    -   Select the `fa-shopping-cart`{.interpreted-text role="icon"}
        (`Shopping cart`{.interpreted-text role="guilabel"}) option to
        display an `fa-shopping-cart`{.interpreted-text role="icon"}
        (`Add to cart`{.interpreted-text role="guilabel"}) icon on each
        product\'s image, which takes the customer to the checkout page.
    -   Select the `fa-heart-o`{.interpreted-text role="icon"}
        (`Wishlist`{.interpreted-text role="guilabel"}) option to
        display an `fa-shopping-cart`{.interpreted-text role="icon"}
        (`Add to wishlist`{.interpreted-text role="guilabel"}) icon on
        each product\'s image allowing logged-in customers to save
        products to a wishlist.
    -   Select the `fa-exchange`{.interpreted-text role="icon"}
        (`Compare`{.interpreted-text role="guilabel"}) option to display
        the `fa-exchange`{.interpreted-text role="icon"}
        (`Compare`{.interpreted-text role="guilabel"}) icon on each
        product\'s image allowing customers to `compare products
        <ecommerce/products/product-comparison>`{.interpreted-text
        role="ref"} based on their attributes.

::: {.tip}
::: {.title}
Tip
:::

To feature a product, go to the
`product form <ecommerce/products/product-form>`{.interpreted-text
role="ref"} and click the `fa-star-o`{.interpreted-text role="icon"}
(`Favorite`{.interpreted-text role="guilabel"}) icon next to the
product\'s name.
:::

Product page {#ecommerce/products/product-page}
------------

To access a product\'s page, go to the `Shop`{.interpreted-text
role="guilabel"} and click on the product. Click
`Edit`{.interpreted-text role="guilabel"} to
`customize <ecommerce/products/customization>`{.interpreted-text
role="ref"} the page or
`edit its images <ecommerce/products/image-customization>`{.interpreted-text
role="ref"}.

::: {#ecommerce/products/product-form}
To access the backend **product form**, click the
`fa-cog`{.interpreted-text role="icon"} `Product`{.interpreted-text
role="guilabel"} button in the top-right corner of the product page.
Alternatively, navigate to `Website -->
eCommerce --> Products`{.interpreted-text role="menuselection"} and
select the product. You can configure the product page from the form by
adding
`variants <ecommerce/products/product-variants>`{.interpreted-text
role="ref"}, `digital documents
<ecommerce/products/digital-files>`{.interpreted-text role="ref"}, or
`translating <ecommerce/products/translation>`{.interpreted-text
role="ref"} content.
:::

::: {.tip}
::: {.title}
Tip
:::

Click the `Go to Website`{.interpreted-text role="guilabel"} smart
button to return to the frontend product\'s page.
:::

### Customization {#ecommerce/products/customization}

To customize a product page, click `Edit`{.interpreted-text
role="guilabel"} in the upper right corner of the page. Use the
`Blocks`{.interpreted-text role="guilabel"} tab to add
`building blocks <../../websites/website/web_design/building_blocks>`{.interpreted-text
role="doc"}.

::: {.tip}
::: {.title}
Tip
:::

\- When dragging and dropping a building block on the product page,
placing it above or below the top or bottom blue lines makes it visible
on all product pages. - You can edit any text on your website by
clicking on it while in `Edit`{.interpreted-text role="guilabel"} mode.
:::

Go to the `Customize`{.interpreted-text role="guilabel"} tab to modify
the page layout or add features:

-   `Terms and Conditions`{.interpreted-text role="guilabel"}: Toggle
    the switch to display a link to your
    `terms and conditions <../../finance/accounting/customer_invoices/terms_conditions>`{.interpreted-text
    role="doc"} on the product page.

-   `Customers`{.interpreted-text role="guilabel"}:

    > -   `Rating`{.interpreted-text role="guilabel"}: Allow logged-in
    >     portal users to submit product reviews by clicking the stars
    >     below the product\'s name and sharing their experience in the
    >     `Customer Reviews`{.interpreted-text role="guilabel"} section
    >     at the bottom. Reviews are visible from the product page using
    >     the `fa-plus`{.interpreted-text role="icon"}
    >     (`plus`{.interpreted-text role="guilabel"}) icon next to the
    >     `Customer Reviews`{.interpreted-text role="guilabel"} heading
    >     or from the product form\'s chatter. To restrict visibility to
    >     internal employees, toggle the `Public`{.interpreted-text
    >     role="guilabel"} switch next to the review comment.
    > -   `Share`{.interpreted-text role="guilabel"}: Add social media
    >     and email icon buttons allowing customers to share the product
    >     through those channels.

-   `Select Quantity`{.interpreted-text role="guilabel"}: Toggle the
    switch to allow customers to select the product quantity they want
    to purchase.

-   `Tax Indication`{.interpreted-text role="guilabel"}: Toggle the
    switch to indicate if the price is
    `VAT included or excluded <ecommerce-price-management-tax-display>`{.interpreted-text
    role="ref"}.

-   `Variants`{.interpreted-text role="guilabel"}: Show all possible
    product `variants
    <ecommerce/products/product-variants>`{.interpreted-text role="ref"}
    vertically as a `Products List`{.interpreted-text role="guilabel"}
    or horizontally as selectable `Options`{.interpreted-text
    role="guilabel"} to compose the variant yourself.

-   `Product Tags`{.interpreted-text role="guilabel"}: Toggle the switch
    to display the `Product Template Tags`{.interpreted-text
    role="guilabel"} on the product page and allow customers to filter
    products using those tags.

-   `Cart`{.interpreted-text role="guilabel"}:

    > -   `Buy Now`{.interpreted-text role="guilabel"}: Add a
    >     `fa-bolt`{.interpreted-text role="icon"}
    >     `Buy Now`{.interpreted-text role="guilabel"} option to take
    >     the customer to the checkout page.
    > -   `Wishlist`{.interpreted-text role="guilabel"}: Add an
    >     `fa-heart-o`{.interpreted-text role="icon"}
    >     `Add to wishlist`{.interpreted-text role="guilabel"} option
    >     allowing logged-in customers to save products in a wishlist.
    > -   `Compare`{.interpreted-text role="guilabel"}: Add a
    >     `fa-exchange`{.interpreted-text role="icon"}
    >     `Compare`{.interpreted-text role="guilabel"} option, allowing
    >     customers to
    >     `compare products <ecommerce/products/product-comparison>`{.interpreted-text
    >     role="ref"} based on their attributes.

-   `Specification`{.interpreted-text role="guilabel"}: Select
    `Bottom of Page`{.interpreted-text role="guilabel"} to display a
    detailed list of the attributes and their values available for the
    product. This option only works for products with
    `variants <ecommerce/products/product-variants>`{.interpreted-text
    role="ref"} if the
    `Product comparison tool <ecommerce/products/product-comparison>`{.interpreted-text
    role="ref"} is enabled in the Website `Settings`{.interpreted-text
    role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- `Variants`{.interpreted-text role="guilabel"},
`fa-heart-o`{.interpreted-text role="icon"} `Wishlist`{.interpreted-text
role="guilabel"}, and `fa-exchange`{.interpreted-text role="icon"}
`Compare`{.interpreted-text role="guilabel"} options must be enabled by
going to `Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, in the `Shop - Products`{.interpreted-text
role="guilabel"} section. - Enabled functions apply to all product
pages. - Products with single values for their attributes do not
generate variants but are still displayed in the
`Product Specifications`{.interpreted-text role="guilabel"}.
:::

### Product images and videos {#ecommerce/products/image-customization}

To add more media items, such as images and videos, navigate to the
`product form <ecommerce/products/product-form>`{.interpreted-text
role="ref"}, then go to the `Sales`{.interpreted-text role="guilabel"}
tab and click `Add a media`{.interpreted-text role="guilabel"} under the
`Extra Product Media`{.interpreted-text role="guilabel"} section. In the
`Create Extra Product Media`{.interpreted-text role="guilabel"} pop-up
window, enter the `Image Name`{.interpreted-text role="guilabel"}, and
add a video URL or hover your mouse over the
`fa-camera`{.interpreted-text role="icon"} `(camera)`{.interpreted-text
role="guilabel"} icon and click the `fa-pencil`{.interpreted-text
role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon to
upload images from your local drive.

To customize the images or videos, go to the ecommerce product page,
click `Edit`{.interpreted-text role="guilabel"} and select the relevant
media. In the `Customize`{.interpreted-text role="guilabel"} tab, use
the following features:

-   `Images Width`{.interpreted-text role="guilabel"}: Changes the width
    of the product images displayed on the page.
-   `Layout`{.interpreted-text role="guilabel"}: The
    `Carousel`{.interpreted-text role="guilabel"} layout allows
    customers to navigate from one image to the next using the
    `fa-angle-left`{.interpreted-text role="icon"}
    (`left arrow`{.interpreted-text role="guilabel"}) or
    `fa-angle-right`{.interpreted-text role="icon"}
    (`right arrow`{.interpreted-text role="guilabel"}); whereas the
    `Grid`{.interpreted-text role="guilabel"} displays four images in a
    square layout.
-   `Image Zoom`{.interpreted-text role="guilabel"}: Select the zoom
    effect for product images: `Magnifier on hover`{.interpreted-text
    role="guilabel"} `Pop-up on Click`{.interpreted-text
    role="guilabel"}, `Both`{.interpreted-text role="guilabel"}, or
    `None`{.interpreted-text role="guilabel"}.
-   `Thumbnails`{.interpreted-text role="guilabel"}: Align thumbnails on
    the `fa-long-arrow-left`{.interpreted-text role="icon"}
    (`Left`{.interpreted-text role="guilabel"}) or at the
    `fa-long-arrow-down`{.interpreted-text role="icon"}
    (`Bottom`{.interpreted-text role="guilabel"}).
-   `Main Image`{.interpreted-text role="guilabel"}: Click
    `Replace`{.interpreted-text role="guilabel"} to change the
    product\'s main image.
-   `Extra Images`{.interpreted-text role="guilabel"}:
    `Add`{.interpreted-text role="guilabel"} more extra images or videos
    (including via URL) or `Remove all`{.interpreted-text
    role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Images must be in PNG or JPG format and with a minimum size of 1024x1024
to trigger the zoom.
:::

Product variants {#ecommerce/products/product-variants}
----------------

`Product variants <../../sales/sales/products_prices/products/variants>`{.interpreted-text
role="doc"} are different versions of the same product, such as various
colors or materials, with potential differences in price and
availability.

To configure product variants for a product:

1.  Go to `Website --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.
2.  Scroll down to the `Shop - Products`{.interpreted-text
    role="guilabel"} section and enable the
    `Product Variants`{.interpreted-text role="guilabel"} feature.
3.  Access the
    `product forms <ecommerce/products/product-form>`{.interpreted-text
    role="ref"} and go to the `Attributes & Variants`{.interpreted-text
    role="guilabel"} tab, where you can add attributes and values,
    allowing customers to configure and select product variants on the
    product page. For multiple attributes, you can combine them to
    create specific variants.

To display or hide an attribute on the `Shop`{.interpreted-text
role="guilabel"} page and allow visitors to filter them, go to
`Website --> eCommerce --> Attributes`{.interpreted-text
role="menuselection"}, click on the attribute, and select
`Visible`{.interpreted-text role="guilabel"} or
`Hidden`{.interpreted-text role="guilabel"} in the
`eCommerce Filter Visibility`{.interpreted-text role="guilabel"} field.

::: {.tip}
::: {.title}
Tip
:::

\- To display the product attributes on
`the main Shop page <ecommerce/products/shop-page>`{.interpreted-text
role="ref"}, set the `Attributes`{.interpreted-text role="guilabel"}
feature to `Left`{.interpreted-text role="guilabel"} using the website
editor. - To group attributes under the same section when
`comparing products <ecommerce/products/product-comparison>`{.interpreted-text
role="ref"}, go to the `eCommerce Category`{.interpreted-text
role="guilabel"} field and either select an
`existing category or create a
new one <../../websites/ecommerce/products>`{.interpreted-text
role="doc"}.
:::

::: {.note}
::: {.title}
Note
:::

Two attribute values are needed to make the filter visible.
:::

::: {.seealso}
`Product variants <../../sales/sales/products_prices/products/variants>`{.interpreted-text
role="doc"}
:::

Digital files {#ecommerce/products/digital-files}
-------------

You can link digital files like certificates, eBooks, or user manuals to
the products. These documents are available
`before payment <ecommerce-products-digital-files-before-payment>`{.interpreted-text
role="ref"} on the product page or in the customer portal
`after checkout <ecommerce-products-digital-files-after-payment>`{.interpreted-text
role="ref"}.

To link a digital file to a product, go to the
`product form <ecommerce/products/product-form>`{.interpreted-text
role="ref"} and click the `Documents`{.interpreted-text role="guilabel"}
smart button. Then, click `Upload`{.interpreted-text role="guilabel"} to
upload a file directly, or for additional options, click
`New`{.interpreted-text role="guilabel"}, then
`Upload your file`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

\- You can link a URL instead of a digital file. To do so, click
`New`{.interpreted-text role="guilabel"}, go to the
`Type`{.interpreted-text role="guilabel"} field, and select
`URL`{.interpreted-text role="guilabel"}. - To edit an existing file,
click the `fa-ellipsis-v`{.interpreted-text role="icon"}
(`dropdown menu`{.interpreted-text role="guilabel"}) in the top-right
corner of the document card and click `Edit`{.interpreted-text
role="guilabel"}.
:::

### Digital files available before payment {#ecommerce-products-digital-files-before-payment}

To make the file available on the product page (before payment), leave
the `Visibility`{.interpreted-text role="guilabel"} field blank and
toggle the `Show on product page`{.interpreted-text role="guilabel"}
switch.



### Digital files available after payment {#ecommerce-products-digital-files-after-payment}

To make the file available (after payment), set the
`Visibility`{.interpreted-text role="guilabel"} field to
`Confirmed order`{.interpreted-text role="guilabel"} and turn off the
`Show on product page`{.interpreted-text role="guilabel"} switch.

Translation {#ecommerce/products/translation}
-----------

If multiple languages are available on your website, you can translate a
product\'s information directly on the
`product form <ecommerce/products/product-form>`{.interpreted-text
role="ref"}. Fields that support multiple languages are identifiable by
their abbreviation language (e.g., EN) next to their field.

The eCommerce-related fields to translate are:

-   `Product name`{.interpreted-text role="guilabel"}.
-   `Out-of-Stock Message`{.interpreted-text role="guilabel"} (under the
    `Sales`{.interpreted-text role="guilabel"} tab).
-   `Sales Description`{.interpreted-text role="guilabel"} (under the
    `Sales`{.interpreted-text role="guilabel"} tab).

::: {.note}
::: {.title}
Note
:::

\- Having untranslated content on a web page may be detrimental to the
user experience and
`SEO <../../websites/website/pages/seo>`{.interpreted-text role="doc"}.
You can use the
`Translate <../website/configuration/translate>`{.interpreted-text
role="doc"} feature to translate the page\'s content. - To check the
language(s) of your website, go to `Website --> Configuration -->
Settings`{.interpreted-text role="menuselection"} and go to the
`Website Info`{.interpreted-text role="guilabel"} section.
:::

### Website availability {#ecommerce/products/website-availability}

To set the product\'s website availability, navigate to the
`product form
<ecommerce/products/product-form>`{.interpreted-text role="ref"}, go to
the `Sales`{.interpreted-text role="guilabel"} tab, and in the
`eCommerce shop`{.interpreted-text role="guilabel"} section, select the
`Website`{.interpreted-text role="guilabel"} you wish the product to be
available on. Leave the field blank to make the product available on
*all* websites.

::: {.note}
::: {.title}
Note
:::

You can make a product available on either *one* website or *all*
websites, but selecting only *some* websites is not possible.
:::

Stock management {#ecommerce/products/stock-management}
----------------

To enable and configure inventory management options, go to `Website -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
scroll down to the `Shop - Products`{.interpreted-text role="guilabel"}
section and the `Inventory Defaults`{.interpreted-text role="guilabel"}
sub-section.

::: {.important}
::: {.title}
Important
:::

\- The **Inventory** app must be installed to see the inventory
management options. - To display the stock level on the product page,
the `Product Type`{.interpreted-text role="guilabel"} field must be set
to `Storable`{.interpreted-text role="guilabel"} in the
`product form <ecommerce/products/product-form>`{.interpreted-text
role="ref"}.
:::

### Inventory

In the `Inventory Defaults`{.interpreted-text role="guilabel"}
sub-section, fill in those fields:

-   `Warehouse <../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses>`{.interpreted-text
    role="doc"}.
-   `Out-of-Stock`{.interpreted-text role="guilabel"}: Enable
    `Continue Selling`{.interpreted-text role="guilabel"} to allow
    customers to place orders even when the product is **out of stock**.
    Leave the box unchecked to **prevent orders**.
-   `Show Available Qty`{.interpreted-text role="guilabel"}: Displays
    the available quantity left under a specified threshold on the
    product page. The available quantity is calculated based on the
    `On hand`{.interpreted-text role="guilabel"} quantity minus the
    quantity already reserved for outgoing transfers.

Product comparison {#ecommerce/products/product-comparison}
------------------

To allow website visitors to compare products based on their attributes,
go to `Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the
`Shop - Products`{.interpreted-text role="guilabel"} section, and enable
`Product Comparison Tool`{.interpreted-text role="guilabel"}.

The `fa-exchange`{.interpreted-text role="icon"}
(`Compare`{.interpreted-text role="guilabel"}) icon is now available on
each product card on the main shop page when customers hover their mouse
over it. To compare products, customers can click the
`fa-exchange`{.interpreted-text role="icon"}
(`Compare`{.interpreted-text role="guilabel"}) option on the products
they want to compare, then click `fa-exchange`{.interpreted-text
role="icon"} `Compare`{.interpreted-text role="guilabel"} in the pop-up
window at the bottom of the page to reach the comparison summary.



::: {.note}
::: {.title}
Note
:::

\- The `Product Comparison Tool`{.interpreted-text role="guilabel"} is
only available for products with
`attributes <ecommerce/products/product-variants>`{.interpreted-text
role="ref"}. - Selecting the `fa-exchange`{.interpreted-text
role="icon"} (`Compare`{.interpreted-text role="guilabel"}) option from
a product page is also possible.
:::

::: {.toctree titlesonly=""}
products/catalog products/price\_management products/cross\_upselling
:::
