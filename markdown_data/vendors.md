# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch/vendors.md

Vendors
=======

Before `products can be added <products>`{.interpreted-text role="doc"}
to the *Lunch* app, the restaurants that provide the food **must** be
configured.

To add a new vendor, first navigate to
`Lunch app --> Configuration --> Vendors`{.interpreted-text
role="menuselection"}. Here, all currently configured vendors for the
*Lunch* app appear in a default Kanban view. To change to a list view,
click the `oi-view-list`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon in the top-right
corner.

::: {.note}
::: {.title}
Note
:::

No vendors are preconfigured in the *Lunch* app, so all vendors **must**
be added to the database.
:::

To add a new vendor, click the `New`{.interpreted-text role="guilabel"}
button in the top-left corner, and a new lunch supplier form loads.

Fill out the following fields on the vendor form:

-   `Vendor information <lunch/vendor-info>`{.interpreted-text
    role="ref"}
-   `Availability <lunch/availability>`{.interpreted-text role="ref"}
-   `Orders <lunch/orders>`{.interpreted-text role="ref"}
-   `Extras <lunch/extras>`{.interpreted-text role="ref"}

Vendor information {#lunch/vendor-info}
------------------

-   `Vendor`{.interpreted-text role="guilabel"}: enter a name for the
    vendor.

-   `Vendor`{.interpreted-text role="guilabel"} (beneath the line for
    vendor name): select the vendor from the drop-down menu. If the
    vendor has not already been entered in the system, type in the
    vendor name, and click either
    `Create "new vendor name"`{.interpreted-text role="guilabel"} to add
    them. Alternatively, click `Create
    and edit...`{.interpreted-text role="guilabel"} to create the
    vendor, and edit the vendor form. The vendor form allows for more
    detail, aside from the name, to be entered, such as contact
    information.

    ::: {.note}
    ::: {.title}
    Note
    :::

    If a selection is made to the drop-down `Vendor`{.interpreted-text
    role="guilabel"} field, the `Vendor`{.interpreted-text
    role="guilabel"} text field (above, for the vendor\'s name) updates
    with the name of the vendor chosen from the drop-down menu.

    The list of vendors that is presented in the drop-down menu is
    pulled from the *Contacts* application.
    :::

-   `Address`{.interpreted-text role="guilabel"}: enter the vendor\'s
    address in the various fields.

-   `Email`{.interpreted-text role="guilabel"}: enter the vendor\'s
    email.

-   `Phone`{.interpreted-text role="guilabel"}: enter the vendor\'s
    phone number.

-   `Company`{.interpreted-text role="guilabel"}: if this vendor is only
    available to a specific company, select the company from the
    drop-down menu. If this field is left blank, the vendor\'s items are
    available to **all** companies.

{.align-center}

Availability {#lunch/availability}
------------

The `AVAILABILITY`{.interpreted-text role="guilabel"} section presents a
table with two rows. The days of the week populate the top row, and the
bottom row has checkboxes. Tick the corresponding checkbox for each day
of the week the vendor is available.

By default, Monday through Friday are ticked.

{.align-center}

Orders {#lunch/orders}
------

The `ORDERS`{.interpreted-text role="guilabel"} section of the vendor
form details which locations the vendor is available for, in addition to
how and when orders are placed and received.

-   `Delivery`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select `Delivery`{.interpreted-text role="guilabel"} if the
    vendor delivers to the office, or select
    `No Delivery`{.interpreted-text role="guilabel"} if orders must be
    picked up.

-   `Location`{.interpreted-text role="guilabel"}: select which
    locations are able to order from this vendor. Multiple locations can
    be selected. If this field is left blank, **all** locations can
    order from the vendor.

    ::: {.note}
    ::: {.title}
    Note
    :::

    An [HQ Office]{.title-ref} location is created by default when
    creating a database, and is available to select from the list.
    :::

-   `Send Order By`{.interpreted-text role="guilabel"}: click the radio
    button to select how orders are sent to the vendor. The available
    options are `Phone`{.interpreted-text role="guilabel"} or
    `Email`{.interpreted-text role="guilabel"}.

-   `Order Time`{.interpreted-text role="guilabel"}: this field **only**
    appears if `Email`{.interpreted-text role="guilabel"} is selected in
    the `Send Order By`{.interpreted-text role="guilabel"} field. Enter
    the time that an order must be emailed for it to be accepted. Enter
    the time in the following format: [HH:MM]{.title-ref}. Then select
    either `AM`{.interpreted-text role="guilabel"} or
    `PM`{.interpreted-text role="guilabel"} from the drop-down menu,
    next to the time field.

{.align-center}

Extras {#lunch/extras}
------

When ordering an item in the *Lunch* app, optional extra items,
sometimes referred to as *add-ons*, can be shown. These can be
configured in any manner that suits the products being offered.

By default, Odoo allows for three types of extra items, which can be
thought of as *categories*. By default, the first type (or *category*)
of add-ons is labeled [Extras]{.title-ref}, the second is labeled
[Beverages]{.title-ref}, and the third is labeled [Extra Label
3]{.title-ref}.

::: {.important}
::: {.title}
Important
:::

When configuring the extras, it is important to keep in mind that all
the extras configured appear for **every item** offered by the vendor.
That means that only items which apply to **all** products from the
vendor should be added.
:::

### Configure extras {#lunch/configure-extras}

Enter the following information for each of the three available extra
sections:

-   `Extra (#) Label`{.interpreted-text role="guilabel"}: enter a name
    for the type of extra, such as [Toppings]{.title-ref}. This can be
    thought of as a *category*.
-   `Extra (#) Quantity`{.interpreted-text role="guilabel"}: select how
    the extras are selected. The options are:
    -   `None or More`{.interpreted-text role="guilabel"}: select this
        if the user is not required to make a selection.
    -   `One or More`{.interpreted-text role="guilabel"}: select this to
        **require** the user to make **at least one** selection.
    -   `Only One`{.interpreted-text role="guilabel"}: select this to
        **require** the user to **make only one** selection.

### Add extras

After the labels and quantities have been configured for an extra
category, the individual extra items must be added for each category.

Click `Add a line`{.interpreted-text role="guilabel"} at the bottom of
the list that appears on the right-hand side of the extra category.
Enter the `Name`{.interpreted-text role="guilabel"} and
`Price`{.interpreted-text role="guilabel"} for each item being added.
The price can remain at [\$0.00]{.title-ref} if there is no cost. This
is common for items like disposable silverware or condiments.

::: {.example}
For a pizzeria that only offers personal pizzas, see their extras
configured as follows:

The first extra is configured for the various toppings they offer. The
`Extra 1 Label`{.interpreted-text role="guilabel"} is set to
[Toppings]{.title-ref}, and the `Extra 1 Quantity`{.interpreted-text
role="guilabel"} is set to `None or More`{.interpreted-text
role="guilabel"}. The various toppings are then added, with their
corresponding costs.

{.align-center}

The pizzeria also offers a free beverage with any purchase. To set this
up, the `Extra
2 Label`{.interpreted-text role="guilabel"} is set to
[Beverages]{.title-ref}, and the `Extra 2 Quantity`{.interpreted-text
role="guilabel"} is set to `Only
One`{.interpreted-text role="guilabel"}. The various beverage choices
are added, and the cost for each remains zero.

{.align-center}
:::
