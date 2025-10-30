# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch/products.md

Products
========

Odoo\'s *Lunch* app does **not** come with any products preconfigured.
The individual products being offered must first be configured before
orders can be placed.

To add and configure products for the *Lunch* app, navigate to
`Lunch app -->
Configuration --> Products`{.interpreted-text role="menuselection"}.
Next, click the `New`{.interpreted-text role="guilabel"} button in the
top-left corner, and a blank product form loads.

Enter the following information on the form:

-   `Product Name`{.interpreted-text role="guilabel"}: enter the name
    for the product. This field is **required**.
-   `Product Category`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the `category
    <lunch/product-categories>`{.interpreted-text role="ref"} this
    product falls under. This field is **required**.
-   `Vendor`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the vendor that supplies this product. This field is
    **required**.
-   `Price`{.interpreted-text role="guilabel"}: enter the price for the
    product. The currency is determined by the company\'s localization.
-   `Description`{.interpreted-text role="guilabel"}: enter a
    description of the product in this field. This description appears
    beneath the product photo when users are viewing the day\'s options.
-   `New Until`{.interpreted-text role="guilabel"}: using the calendar
    popover, select the date on which the product is no longer labeled
    as new. Until this date, a green [New]{.title-ref} tag appears on
    the product.
-   `Company`{.interpreted-text role="guilabel"}: if the product should
    only be available to a specific company, select it from the
    drop-down menu. If this field is left blank, this product is
    available for all companies in the database.
-   **Image**: hover over the image box in the top-right corner of the
    form, and click the `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon that appears. A
    file explorer pop-up window appears. Navigate to the image, then
    click `Open`{.interpreted-text role="guilabel"}.

{.align-center}

Product categories {#lunch/product-categories}
------------------

Product categories organize the offerings in the *Lunch* app, and allows
users to quickly filter them when reviewing the menu for the day.

To add or modify categories, navigate to
`Lunch app --> Configuration: Product
Categories`{.interpreted-text role="menuselection"}. The available
categories appear in a list view.

In the *Lunch* app, there are four default categories:
`Sandwich`{.interpreted-text role="guilabel"}, `Pizza`{.interpreted-text
role="guilabel"}, `Burger`{.interpreted-text role="guilabel"}, and
`Drinks`{.interpreted-text role="guilabel"}.

To add a new category, click the `New`{.interpreted-text
role="guilabel"} button in the top-left corner, and a blank category
form loads.

Enter a name in the `Product Category`{.interpreted-text
role="guilabel"} field. If the category is company-specific and should
only appear for a certain company, select the
`Company`{.interpreted-text role="guilabel"} from the drop-down menu.

If desired, add a photo for the category. Hover over the image box in
the top-right, and click the `fa-pencil`{.interpreted-text role="icon"}
`(pencil)`{.interpreted-text role="guilabel"} icon that appears. This
opens a file explorer pop-up window. Navigate to the image, then click
`Open`{.interpreted-text role="guilabel"}.

{.align-center}
