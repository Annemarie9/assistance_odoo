# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/stock_warehouses.md

Sell stock from multiple warehouses using virtual locations
===========================================================

While keeping stock and selling inventory from one warehouse might work
for smaller companies, bigger companies might need to keep stock in, or
sell from, multiple warehouses in multiple locations.

Sometimes products included in a single sales order might take stock
from two (or more) warehouses; in Odoo, pulling products from multiple
warehouses to satisfy sales demands can be done using *virtual
locations*.

::: {.important}
::: {.title}
Important
:::

The solution in this document, describing the use of a virtual warehouse
to fulfill orders for multiple warehouses, has some limitations.
Consider the following before proceeding:

1.  When the `Warehouse`{.interpreted-text role="guilabel"} field is set
    to a virtual warehouse on a sales order, the virtual warehouse\'s
    address is indicated on the picking, packing, and delivery forms,
    **not** the actual warehouse\'s address.
2.  Each location has a [warehouse\_id]{.title-ref} (hidden field). This
    means that the stock in the virtual warehouse will **not** be the
    sum of the stock of the real warehouses, but rather the sum of the
    stock in the locations whose warehouse ID is the virtual warehouse.
:::

::: {.danger}
::: {.title}
Danger
:::

Potential limitation for those using `two
<../../shipping_receiving/daily_operations/receipts_delivery_two_steps>`{.interpreted-text
role="doc"} or `three-step
delivery <../../shipping_receiving/daily_operations/delivery_three_steps>`{.interpreted-text
role="doc"}:

1.  The output or packing zone on the various forms is incorrectly
    listed as the virtual warehouse\'s address.
2.  There is no workaround for two or three-step deliveries.
3.  Proceed **only** if setting a virtual warehouse\'s address as the
    output or packing zone makes sense for the company\'s workflow.
:::

::: {.note}
::: {.title}
Note
:::

In order to create virtual locations in warehouses, and proceed to the
following steps, the `Storage Locations`{.interpreted-text
role="guilabel"} and `Multi-Step Routes`{.interpreted-text
role="guilabel"} features **must** be enabled.

To do so, go to
`Inventory app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the `Warehouse`{.interpreted-text
role="guilabel"} section, and enable the
`Storage Locations`{.interpreted-text role="guilabel"} and
`Multi-Step Routes`{.interpreted-text role="guilabel"} options. Then,
`Save`{.interpreted-text role="guilabel"} the changes to finish.
:::

Create virtual parent location {#inventory/routes/virtual-wh}
------------------------------

Before creating any virtual stock locations, create a new warehouse that
acts as a *virtual* warehouse --- the *parent* location of other
physical warehouses.

::: {.spoiler}
Why a \"virtual\" warehouse?

Virtual warehouses are great for companies with multiple physical
warehouses. This is because a situation might arise when one warehouse
runs out of stock of a particular product, but another warehouse still
has stock on-hand. In this case, stock from these two (or more)
warehouses could be used to fulfill a single sales order.

The \"virtual\" warehouse acts as a single aggregator of all the
inventory stored in a company\'s physical warehouses, and is used (for
traceability purposes) to create a hierarchy of locations in Odoo.
:::

To create a new warehouse, go to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, and click `Create`{.interpreted-text
role="guilabel"}. From here, the warehouse `Name`{.interpreted-text
role="guilabel"} and `Short Name`{.interpreted-text role="guilabel"} can
be changed, and other warehouse details can be changed under the
`Warehouse
Configuration`{.interpreted-text role="guilabel"} tab.

Lastly, click `Save`{.interpreted-text role="guilabel"} to finish
creating a *regular* warehouse. Continue following the steps below to
finish configuring the virtual parent warehouse.

{.align-center}

::: {.seealso}
\-
`Warehouse configurations <../../warehouses_storage/inventory_management/warehouses>`{.interpreted-text
role="doc"} -
`Incoming and outgoing shipments <inventory/receipts_delivery_one_step/wh>`{.interpreted-text
role="ref"} -
`../../warehouses_storage/replenishment/resupply_warehouses`{.interpreted-text
role="doc"}
:::

Create child warehouses {#inventory/routes/child-wh}
-----------------------

Create at least two *child* warehouses to link to the virtual warehouse.

::: {.important}
::: {.title}
Important
:::

In order to take stock from multiple warehouses to fulfill a sales
order, there needs to be at least **two** warehouses acting as child
locations of the virtual parent location warehouse.
:::

To do that, navigate to
`Inventory app --> Configuration --> Warehouses`{.interpreted-text
role="menuselection"}, click `Create`{.interpreted-text
role="guilabel"}, and follow the
`preceding instructions <inventory/routes/virtual-wh>`{.interpreted-text
role="ref"} to configure the physical stock locations.

::: {.example}
| **Parent Warehouse**
| `Warehouse`{.interpreted-text role="guilabel"}: [Virtual
  Warehouse]{.title-ref}
| `Location`{.interpreted-text role="guilabel"}: [VWH/Stock]{.title-ref}

| **Child Warehouses**
| `Warehouses`{.interpreted-text role="guilabel"}: [Warehouse
  A]{.title-ref} and [Warehouse B]{.title-ref}
| `Locations`{.interpreted-text role="guilabel"}: [WHA]{.title-ref} and
  [WHB]{.title-ref}

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

While the virtual stock location will be changed to \'View\' later, the
`Location Type`{.interpreted-text role="guilabel"} **must** be
`Internal Location`{.interpreted-text role="guilabel"} at this point to
`link the child warehouses
<inventory/routes/link-to-vwh>`{.interpreted-text role="ref"} in the
next section.
:::

Link child warehouses to virtual stock {#inventory/routes/link-to-vwh}
--------------------------------------

To set physical warehouses as child locations of the virtual location
configured in the
`previous step <inventory/routes/virtual-wh>`{.interpreted-text
role="ref"}, navigate to `Inventory app -->
Configuration --> Locations`{.interpreted-text role="menuselection"}.

Remove any filters from the search bar. Then, click the physical
warehouse `Location`{.interpreted-text role="guilabel"} that was
previously created to be a child location (e.g. [WHA]{.title-ref}), and
click `Edit`{.interpreted-text role="guilabel"}.

Change the `Parent Location`{.interpreted-text role="guilabel"} field
from `Physical Locations`{.interpreted-text role="guilabel"} to the
virtual warehouse\'s **stock location** (e.g. [VWH/Stock]{.title-ref})
from the drop-down menu, and click `Save`{.interpreted-text
role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

To select the virtual warehouse\'s stock location in the
`Parent Location`{.interpreted-text role="guilabel"} drop-down menu, the
parent warehouse stock location (e.g. [VWH/Stock]{.title-ref}) **must**
have its `Location Type`{.interpreted-text role="guilabel"} set to
`Internal Location`{.interpreted-text role="guilabel"}.
:::

{.align-center}

Repeat the preceding steps to configure two or more child warehouses.

Once complete, the virtual, parent warehouse (e.g.
[VWH/Stock]{.title-ref}) fulfills orders using stock from child
warehouses (e.g. [WHA]{.title-ref} and [WHB]{.title-ref}), if there is
insufficient stock in any one location.

Set virtual stock location as \'view\'
--------------------------------------

Set the virtual stock location\'s `Location Type`{.interpreted-text
role="guilabel"} to `View`{.interpreted-text role="guilabel"}, as it is
a non-existent location used to group various physical warehouses
together.

To do that, navigate to
`Inventory app --> Configuration --> Locations`{.interpreted-text
role="menuselection"}.

Click the virtual warehouse\'s stock location (e.g.
[VWH/Stock]{.title-ref}) that was `previously created
<inventory/routes/virtual-wh>`{.interpreted-text role="ref"}, from the
`Locations`{.interpreted-text role="guilabel"} list.

On the location form, under the
`Additional Information`{.interpreted-text role="guilabel"} heading, set
the `Location Type`{.interpreted-text role="guilabel"} to
`View`{.interpreted-text role="guilabel"}. `Save`{.interpreted-text
role="guilabel"} the changes.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To view the total quantity across **all** linked child warehouses, go to
the product form and click the `On Hand`{.interpreted-text
role="guilabel"} smart button.

{.align-center}
:::

Example: sell products from a virtual warehouse
-----------------------------------------------

To sell products from multiple warehouses using a virtual parent
location, the database must have at least **two** warehouses configured
--- with at least **one** product, with quantity on-hand in each
warehouse, respectively.

::: {.example}
The following product, [Toy soldier]{.title-ref}, is available at each
location with the quantities:

-   [WHA/Stock]{.title-ref} : 1
-   [WHB/Stock]{.title-ref} : 2
-   Warehouses [WHA]{.title-ref} and [WHB]{.title-ref} are child
    warehouses of the virtual warehouse [VWH]{.title-ref}.
:::

Create a quotation for the product by navigating to the
`Sales`{.interpreted-text role="menuselection"} app and clicking
`Create`{.interpreted-text role="guilabel"}. On the quote, add a
`Customer`{.interpreted-text role="guilabel"}, and click
`Add a product`{.interpreted-text role="guilabel"} to add the two
products stored in the two warehouses.

Then, click the `Other Info`{.interpreted-text role="guilabel"} tab on
the sales order form. Under the `Delivery`{.interpreted-text
role="guilabel"} section, change the `Warehouse`{.interpreted-text
role="guilabel"} field value to the virtual warehouse that was
`previously created <inventory/routes/virtual-wh>`{.interpreted-text
role="ref"}. Next, `Confirm`{.interpreted-text role="guilabel"} the
sales order.

{.align-center}

Then, click the `Delivery`{.interpreted-text role="guilabel"} smart
button. From the warehouse delivery form, confirm that the
`Source Location`{.interpreted-text role="guilabel"} value matches the
`Warehouse`{.interpreted-text role="guilabel"} field value from the
sales order. Both should list the virtual warehouse location.

Finally, on the warehouse delivery form, under the
`Detailed Operations`{.interpreted-text role="guilabel"} tab, confirm
that the `Locations`{.interpreted-text role="guilabel"} in the
`From`{.interpreted-text role="guilabel"} column for each product match
the child locations that are tied to the virtual parent location.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The `Source Location`{.interpreted-text role="guilabel"} on the
warehouse delivery form, and the `Warehouse`{.interpreted-text
role="guilabel"} under the `Other Info`{.interpreted-text
role="guilabel"} tab on the sales order, **must** match for products in
the sales order to be pulled from different warehouses.

-   If the virtual warehouse is not in the
    `Source Location`{.interpreted-text role="guilabel"} field on the
    warehouse delivery form, retry product reservation by:
    -   Running the scheduler: turn on
        `developer mode <developer-mode>`{.interpreted-text role="ref"},
        and then go to
        `Inventory app --> Operations --> Run Scheduler`{.interpreted-text
        role="menuselection"}.
    -   Clicking `Check Availability`{.interpreted-text role="guilabel"}
        on the delivery order.
-   If the virtual warehouse is **not** assigned to the
    `Warehouse`{.interpreted-text role="guilabel"} field on the sales
    order, then cancel it, and create a new sales order with the virtual
    warehouse set in the `Warehouse`{.interpreted-text role="guilabel"}
    field.
-   If the `Warehouse`{.interpreted-text role="guilabel"} field is
    missing on the sales order form, then the multiple child warehouses
    may not have been set up correctly. Review the `previous section
    <inventory/routes/child-wh>`{.interpreted-text role="ref"} to ensure
    the correct settings.
:::

::: {.tip}
::: {.title}
Tip
:::

To use a virtual *parent* location as the default warehouse for sales
orders, each salesperson should have the virtual warehouse assigned to
them from the drop-down menu next to
`Default Warehouse`{.interpreted-text role="guilabel"} on their employee
form.

{.align-center}
:::
