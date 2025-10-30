# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.md

Master production schedule
==========================

In Odoo\'s *Manufacturing* app, the *master production schedule* (MPS)
is used to manually plan manufacturing orders (MOs) and purchase orders
(POs), based on forecasted quantities of products and components.

By considering the impact of confirmed
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} and
`POs (purchase orders)`{.interpreted-text role="abbr"}, along with
manually adjusted demand forecasts, the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} can
be used to manage long-term product replenishment. This ensures the
continued availability of the necessary products and components.

Since the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} allows for manual intervention, it is useful for
replenishing products where the demand of existing sales orders (SOs)
does **not** reflect probable future demand.

::: {.example}
A retail store sells artificial *Christmas trees* during the holiday
season. It is currently September, and the store has less than ten
Christmas tree `MOs (manufacturing orders)`{.interpreted-text
role="abbr"} confirmed for the month of December.

Despite the number of confirmed
`MOs (manufacturing orders)`{.interpreted-text role="abbr"}, the
procurement manager knows that the demand for Christmas trees in
December is going to be much higher, once the holiday season starts. As
a result, they manually enter a greater demand in the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}, so
they can properly replenish the product in time for the increase in
customer demand.
:::

::: {.important}
::: {.title}
Important
:::

It is essential to remember that the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} is a
**MANUAL** tool. Adding a product to the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} does
not cause it to be manufactured or purchased automatically. The
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}
simply suggests the amount of the product that should be replenished,
but requires user input to create the
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} or
`POs (purchase orders)`{.interpreted-text role="abbr"} that are used to
replenish it.

For this reason, it is recommended that the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}
**NOT** be used alongside reordering rules for the same product. Because
reordering rules are an automated workflow, they conflict with the
manual replenishment method of
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}.
Using both, in unison, can lead to inaccurate forecasts and the creation
of unnecessary replenishment orders.
:::

Enable and configure `MPS (Master Production Schedules)`{.interpreted-text role="abbr"}
---------------------------------------------------------------------------------------

To use the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} feature, navigate to
`Manufacturing app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and tick the
`Master Production Schedule`{.interpreted-text role="guilabel"} checkbox
in the `Planning`{.interpreted-text role="guilabel"} section. Finally,
click `Save`{.interpreted-text role="guilabel"}.

After enabling the `Master Production Schedule`{.interpreted-text
role="guilabel"} feature, two new fields appear under it on the
`Settings`{.interpreted-text role="guilabel"} page:
`Time Range`{.interpreted-text role="guilabel"} and
`Number of Columns`{.interpreted-text role="guilabel"}.

The `Time Range`{.interpreted-text role="guilabel"} field is used to
select the period of time over which planning takes place, and offers
three options: `Monthly`{.interpreted-text role="guilabel"},
`Weekly`{.interpreted-text role="guilabel"}, and
`Daily`{.interpreted-text role="guilabel"}. For example, if
`Monthly`{.interpreted-text role="guilabel"} is selected, the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} plans
the production requirements of products and components on a monthly
basis.

The `Number of Columns`{.interpreted-text role="guilabel"} field is used
to specify the quantity of the selected `Time Range`{.interpreted-text
role="guilabel"} units shown on the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} page.
For example, if the `Time Range`{.interpreted-text role="guilabel"}
field is set to `Monthly`{.interpreted-text role="guilabel"}, and
[12]{.title-ref} is entered in the `Number of Columns`{.interpreted-text
role="guilabel"} field, the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} shows
one column for the next 12 months, starting with the current month.

If the values of the `Time Range`{.interpreted-text role="guilabel"} or
`Number of Columns`{.interpreted-text role="guilabel"} fields are
altered, click `Save`{.interpreted-text role="guilabel"} again to save
the changes.

{.align-center}

`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} dashboard
----------------------------------------------------------------------------

To open the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"}, navigate to
`Manufacturing app --> Planning --> Master Production
Schedule`{.interpreted-text role="menuselection"}. The
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} view
appears as follows:

{.align-center}

The grey column on the left side of the screen shows a section for every
product added to the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}, with
each product section being broken down into smaller rows. The
information shown in the rows depends on the filters selected in the
`Search...`{.interpreted-text role="guilabel"} bar drop-down menu at the
top of the page. The default categories that appear in the rows are:

-   `[Product] by [unit]`{.interpreted-text role="guilabel"}
    `fa-area-chart`{.interpreted-text role="icon"}: the forecasted stock
    quantity at the beginning of each time period.
    `[Product]`{.interpreted-text role="guilabel"} and
    `fa-area-chart`{.interpreted-text role="icon"} are selectable
    buttons which open the product\'s page, or the forecast report for
    the product, respectively.

-   `- Forecasted Demand`{.interpreted-text role="guilabel"}: the demand
    forecast, which is entered manually. This represents an estimate of
    the demand for the product during each time period.

-   `- Indirect Demand Forecast`{.interpreted-text role="guilabel"}:
    while this is a default category, it **only** appears for products
    that are components of other products. It represents the demand for
    the component from existing MOs.

-   `+ Suggested Replenishment`{.interpreted-text role="guilabel"}: the
    quantity of the product that is suggested to be replenished through
    `MOs (manufacturing orders)`{.interpreted-text role="abbr"} or
    `POs (purchase orders)`{.interpreted-text role="abbr"}. To the right
    of the category title is a `Replenish`{.interpreted-text
    role="guilabel"} button, which is used to manually replenish the
    product, based on the quantity suggested to be replenished.

    ![The \"Replenish\" button on the \"+ Suggested Replenishment\"
    row.](use_mps/replenish-button.png){.align-center}

-   `= Forecasted Stock`{.interpreted-text role="guilabel"}: the
    quantity of the product forecasted to be in stock at the end of each
    time period, assuming that suggested replenishment numbers are
    fulfilled.

Altogether, these default categories form an equation:

$$\text{Forecasted Demand} + \text{Suggested Replenishment} = \text{Forecasted Stock}$$

In the case of components, the
`Indirect Demand Forecast`{.interpreted-text role="guilabel"} is taken
into account as well.

The `- Forecasted Demand`{.interpreted-text role="guilabel"} and
`+ Suggested Replenishment`{.interpreted-text role="guilabel"} fields
can be edited for any of the time periods to the right of the product
column. Doing so changes the equation, and updates the value displayed
in the `Forecasted Stock`{.interpreted-text role="guilabel"} field.

Changing the value in the `+ Suggested Replenishment`{.interpreted-text
role="guilabel"} field also makes an `fa-times`{.interpreted-text
role="icon"} `(reset)`{.interpreted-text role="guilabel"} button appear
to the left of the field. Click the `fa-times`{.interpreted-text
role="icon"} `(reset)`{.interpreted-text role="guilabel"} button next to
the field to reset its value back to the one calculated by the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}.

::: {.important}
::: {.title}
Important
:::

While the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} can be used with only the default categories enabled, it is
advisable to also enable the `Actual Demand`{.interpreted-text
role="guilabel"} category. This is done by clicking the
`fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} on the right side of
the `Search...`{.interpreted-text role="guilabel"} bar, and enabling the
`Actual Demand`{.interpreted-text role="guilabel"} option under the
`Rows`{.interpreted-text role="guilabel"} header.

With the `Actual Demand`{.interpreted-text role="guilabel"} option
enabled, the `- Forecasted Demand`{.interpreted-text role="guilabel"}
category changes to the `- Actual / Forecasted Demand`{.interpreted-text
role="guilabel"} category. In addition to the manually entered
forecasted demand, this category also displays the confirmed demand for
the product, which is based on confirmed
`SOs (sales orders)`{.interpreted-text role="abbr"}.
:::

Each column to the right of the products column lists one unit of the
time period selected in the *Time Range* field on the *Manufacturing*
app *Settings* page (ex. months). The number of time period columns
corresponds to the value entered in the *Number of Columns* field.

The first time period column represents the current time period. For
example, if the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} is configured to use months, the first column displays data
for the current month. On this first column, the
`+ Suggested Replenishment`{.interpreted-text role="guilabel"} field
appears in one of five colors:

-   `Green`{.interpreted-text role="guilabel"}: a replenishment order
    must be generated to keep stock at the `Safety
    Stock Target`{.interpreted-text role="guilabel"}.
-   `Gray`{.interpreted-text role="guilabel"}: a replenishment order has
    already been generated to keep stock at the
    `Safety Stock Target`{.interpreted-text role="guilabel"}.
-   `Yellow`{.interpreted-text role="guilabel"}: a replenishment order
    has already been generated, but the quantity it was created for is
    not enough to keep stock at the
    `Safety Stock Target`{.interpreted-text role="guilabel"}.
-   `Red`{.interpreted-text role="guilabel"}: a replenishment order has
    already been generated, but the quantity it was created for puts the
    amount of stock above the `Safety Stock Target`{.interpreted-text
    role="guilabel"}.

The `+ Suggested Replenishment`{.interpreted-text role="guilabel"} field
appears white, if no replenishment order has been generated, and it is
not necessary to generate one at the current moment.

Add a product
-------------

To use `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} to manage the replenishment of a product, navigate to
`Manufacturing app
--> Planning --> Master Production Schedule`{.interpreted-text
role="menuselection"}. At the top of the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} page,
click `Add a
Product`{.interpreted-text role="guilabel"} to open the
`Add a Product`{.interpreted-text role="guilabel"} pop-up window.

::: {.important}
::: {.title}
Important
:::

Products **must** be properly configured to be replenished through the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}.

In the case of manufactured products, the *Manufacture* route must be
selected in the *Routes* section of the *Inventory* tab, on the
product\'s form.

In the case of products that are purchased, the *Buy* route must be
selected in the *Routes* section of the *Inventory* tab, on the
product\'s form. Additionally, a vendor and the price they sell the
product for must also be specified on the *Purchase* tab.
:::

On the pop-up window, select the product to add in the
`Product`{.interpreted-text role="guilabel"} drop-down menu. If the
product is replenished through manufacturing, select the product\'s
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} in the `Bill of
Materials`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

Selecting a BoM when adding a product to the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} also
adds any components listed on the BoM. If it is not necessary to manage
the replenishment of components through the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"},
simply leave the `Bill of Materials`{.interpreted-text role="guilabel"}
field blank.
:::

If the database is configured with multiple warehouses, a
`Production Warehouse`{.interpreted-text role="guilabel"} field appears
on the `Add a Product`{.interpreted-text role="guilabel"} pop-up window.
Use this field to specify which warehouse the product is replenished to.

In the `Safety Stock Target`{.interpreted-text role="guilabel"} field,
specify the minimum quantity of the product that should be kept
available for orders at all times. For example, if there should always
be 20 units of the product available for order fulfillment, enter
[20]{.title-ref} in the `Safety Stock Target`{.interpreted-text
role="guilabel"} field.

In the `Minimum to Replenish`{.interpreted-text role="guilabel"} field,
enter the minimum product quantity for orders created to replenish the
product. For example, if [5]{.title-ref} is entered in this field,
replenishment orders for the product include a minimum of five units.

In the `Maximum to Replenish`{.interpreted-text role="guilabel"} field,
enter the maximum product quantity for orders created to replenish the
product. For example, if [100]{.title-ref} is entered in this field,
replenishment orders for the product include a maximum of 100 units.

Finally, click `Save`{.interpreted-text role="guilabel"} to add the
product to the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"}. The product now appears on the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} page
each time it is opened. If a `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} was selected in the `Bill of Materials`{.interpreted-text
role="guilabel"} field of the `Add a Product`{.interpreted-text
role="guilabel"} pop-up window, any components listed on the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} appear on the
page, as well.

{.align-center}

### Edit a product

After adding a product to the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}, it
may be necessary to change the replenishment values entered on the
`Add a Product`{.interpreted-text role="guilabel"} pop-up window. To do
so, click the `# ≤…≤ #`{.interpreted-text role="guilabel"} button to the
immediate right of the `Replenish`{.interpreted-text role="guilabel"}
button, on the `+ Suggested
Replenishment`{.interpreted-text role="guilabel"} row, below the
product\'s name.

::: {.note}
::: {.title}
Note
:::

The first and second number displayed on the `# ≤…≤ #`{.interpreted-text
role="guilabel"} button correspond to the values entered in the
`Minimum to Replenish`{.interpreted-text role="guilabel"} and
`Maximum to Replenish`{.interpreted-text role="guilabel"} fields when
adding the product to the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}.

For example, if [5]{.title-ref} was entered in the
`Minimum to Replenish`{.interpreted-text role="guilabel"} field, and
[100]{.title-ref} was entered in the
`Maximum to Replenish`{.interpreted-text role="guilabel"} field, the
button appears as `5 ≤…≤
100`{.interpreted-text role="guilabel"}.
:::

Clicking the `# ≤…≤ #`{.interpreted-text role="guilabel"} button opens
the `Edit Production Schedule`{.interpreted-text role="guilabel"} pop-up
window. This pop-up window is the same as the
`Add a Product`{.interpreted-text role="guilabel"} pop-up window, except
that the `Product`{.interpreted-text role="guilabel"} and
`Bill of Materials`{.interpreted-text role="guilabel"} fields cannot be
edited.

On the `Edit Production Schedule`{.interpreted-text role="guilabel"}
pop-up window, enter the desired values in the
`Safety Stock Target`{.interpreted-text role="guilabel"},
`Minimum to Replenish`{.interpreted-text role="guilabel"}, and
`Maximum to
Replenish`{.interpreted-text role="guilabel"} fields. Then, click
`Save`{.interpreted-text role="guilabel"} to save the changes.

### Remove a product

To remove a product from the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}, tick
the checkbox to the left of its name. Then, click the
`fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
role="guilabel"} button at the top of the screen, and select
`Delete`{.interpreted-text role="guilabel"} from the resulting drop-down
menu. Finally, click `Ok`{.interpreted-text role="guilabel"} on the
`Confirmation`{.interpreted-text role="guilabel"} pop-up window.

Deleting a product from the
`MPS (Master Production Schedules)`{.interpreted-text role="abbr"}
removes it, along with all of its data. If the product is re-added, its
replenishment values must be reconfigured.

`MPS (Master Production Schedules)`{.interpreted-text role="abbr"} replenishment
--------------------------------------------------------------------------------

Products in the `MPS (Master Production Schedules)`{.interpreted-text
role="abbr"} can be replenished in one of three ways:

-   Click the `Replenish`{.interpreted-text role="guilabel"} button at
    the top of the screen to generate replenishment orders for every
    product below its `Safety Stock Target`{.interpreted-text
    role="guilabel"} for the current month.
-   Click the `Replenish`{.interpreted-text role="guilabel"} button on
    the right side of the `+ Suggested
    Replenishment`{.interpreted-text role="guilabel"} row of a specific
    product, to generate a replenishment order for that specific
    product.
-   Tick the checkbox to the left of the product name of one or more
    products. Then, click the `fa-cog`{.interpreted-text role="icon"}
    `Actions`{.interpreted-text role="guilabel"} button at the top of
    the screen, and select `Replenish`{.interpreted-text
    role="guilabel"} from the resulting drop-down menu. Doing so
    generates a replenishment order for each selected product.

The type of replenishment order generated corresponds to the route
selected on the *Inventory* tab of the product\'s form:

-   If the *Buy* route is selected, an
    `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} is
    generated to replenish the product.
    `RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} can
    be selected by navigating to the `Purchase`{.interpreted-text
    role="menuselection"} app. Any
    `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}
    generated by the
    `MPS (Master Production Schedules)`{.interpreted-text role="abbr"}
    lists `MPS`{.interpreted-text role="guilabel"} in its
    `Source Document`{.interpreted-text role="guilabel"} field.
-   If the *Manufacture* route is selected, an
    `MO (manufacturing order)`{.interpreted-text role="abbr"} is
    generated to replenish the product.
    `MOs (manufacturing orders)`{.interpreted-text role="abbr"} can be
    selected by navigating to
    `Manufacturing app --> Operations --> Manufacturing
    Orders`{.interpreted-text role="menuselection"}. Any
    `MO (manufacturing order)`{.interpreted-text role="abbr"} generated
    by the `MPS (Master Production Schedules)`{.interpreted-text
    role="abbr"} lists `MPS`{.interpreted-text role="guilabel"} in its
    `Source Document`{.interpreted-text role="guilabel"} field.
