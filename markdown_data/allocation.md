# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/reporting/allocation.md

Allocation reports
==================

When fulfilling sales orders (SOs), or sourcing components for
manufacturing orders (MOs), it is sometimes necessary to prioritize one
`SO (sales order)`{.interpreted-text role="abbr"} or
`MO (manufacturing order)`{.interpreted-text role="abbr"} over another.
In situations where there is insufficient stock on-hand to fulfill every
`SO (sales order)`{.interpreted-text role="abbr"} or
`MO (manufacturing order)`{.interpreted-text role="abbr"}, ensuring that
products and components are reserved for priority orders is essential.

In Odoo *Manufacturing*, allocation reports are used on
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} to assign
products to specific sales orders `SOs (sales orders)`{.interpreted-text
role="abbr"}, or components to specific
`MOs (manufacturing orders)`{.interpreted-text role="abbr"}. This
ensures the products or components are available for those orders, and
are not used by mistake.

Configuration
-------------

To use allocation reports, the *Allocation Report for Manufacturing
Orders* feature **must** be enabled. To do so, navigate to
`Manufacturing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the checkbox next to
`Allocation Report for Manufacturing Orders`{.interpreted-text
role="guilabel"}. Then, click `Save`{.interpreted-text role="guilabel"}.

For products that are sold, it is also necessary to configure them so
they can be included in `SOs (sales orders)`{.interpreted-text
role="abbr"}. To do so, begin by navigating to
`Inventory --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product. Under the
`Product Name`{.interpreted-text role="guilabel"} field on the product
form, make sure that the `Can Be Sold`{.interpreted-text
role="guilabel"} checkbox is ticked.

Allocate products
-----------------

To allocate products or components from an
`MO (manufacturing order)`{.interpreted-text role="abbr"} to an
`SO (sales order)`{.interpreted-text role="abbr"}, or to a different
`MO (manufacturing order)`{.interpreted-text role="abbr"}, begin by
navigating to
`Manufacturing app --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a new `MO (manufacturing order)`{.interpreted-text role="abbr"}.

On the `MO (manufacturing order)`{.interpreted-text role="abbr"} form,
select a product in the `Product`{.interpreted-text role="guilabel"}
field, and specify the quantity to be produced in the
`Quantity`{.interpreted-text role="guilabel"} field. Finally, click
`Confirm`{.interpreted-text role="guilabel"} to confirm the
`MO (manufacturing order)`{.interpreted-text role="abbr"}.

The rest of the allocation workflow depends on the current on-hand
quantity of the product being manufactured, and whether or not there are
any `SOs (sales orders)`{.interpreted-text role="abbr"} or
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} which
require the product, but have not already been allocated units.

If there **are** existing `SOs (sales orders)`{.interpreted-text
role="abbr"} and `MOs (manufacturing orders)`{.interpreted-text
role="abbr"} that require the product, **and** there are too few units
of the product on-hand to fulfill those orders, then an
`fa-list`{.interpreted-text role="icon"} `Allocation`{.interpreted-text
role="guilabel"} smart button appears at the top of the page as soon as
the `MO (manufacturing order)`{.interpreted-text role="abbr"} is
confirmed.

If there **are** existing `SOs (sales orders)`{.interpreted-text
role="abbr"} and `MOs (manufacturing orders)`{.interpreted-text
role="abbr"} that require the product, **and** there are enough units of
the product on-hand to fulfill those orders, then the
`fa-list`{.interpreted-text role="icon"} `Allocation`{.interpreted-text
role="guilabel"} smart button only appears at the top of the page once
the `MO (manufacturing order)`{.interpreted-text role="abbr"} has been
marked as done, by clicking `Produce All`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If there **are not** any existing `SOs (sales orders)`{.interpreted-text
role="abbr"} and `MOs (manufacturing orders)`{.interpreted-text
role="abbr"} that require the product, the `fa-list`{.interpreted-text
role="icon"} `Allocation`{.interpreted-text role="guilabel"} smart
button does not appear, even when the
`MO (manufacturing order)`{.interpreted-text role="abbr"} has been
marked as done.
:::

Click the `fa-list`{.interpreted-text role="icon"}
`Allocation`{.interpreted-text role="guilabel"} smart button to open the
`MRP Reception
Report`{.interpreted-text role="guilabel"} for the
`MO (manufacturing order)`{.interpreted-text role="abbr"}. This report
lists open delivery orders or
`MOs (manufacturing orders)`{.interpreted-text role="abbr"}, depending
on the type of product produced in the original
`MO (manufacturing order)`{.interpreted-text role="abbr"}.

### Allocate to delivery order

If the `MO (manufacturing order)`{.interpreted-text role="abbr"}
contains a finished product, the report lists any open delivery orders
for which quantities of the product have yet to be reserved.

::: {.example}
An `MO (manufacturing order)`{.interpreted-text role="abbr"} is created
to produce three units of a *rocking chair*. Clicking the
`Allocation`{.interpreted-text role="guilabel"} smart button on the
`MO (manufacturing order)`{.interpreted-text role="abbr"} opens an
allocation report that lists open delivery orders that require one or
more rocking chairs.
:::

Click the `Assign All`{.interpreted-text role="guilabel"} button to the
right of a specific order to assign products for each quantity required
to fulfill that order.

::: {.example}
If an order requires one quantity of four units of the product, and one
quantity of one unit of the product, clicking
`Assign All`{.interpreted-text role="guilabel"} assigns five units of
the product to fulfill both quantities.
:::

Alternatively, click `Assign`{.interpreted-text role="guilabel"} next to
a specific quantity to only assign products to that quantity, and not
any others in the order.

::: {.example}
If an order requires one quantity of four units of the product, and one
quantity of one unit of the product, clicking `Assign`{.interpreted-text
role="guilabel"} next to the quantity of one unit assigns a product to
that quantity, but leaves the quantity of four units without any
products assigned.
:::

{.align-center}

### Allocate to MO

If the `MO (manufacturing order)`{.interpreted-text role="abbr"}
contains a component, the report lists any open
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} for which
quantities of the component have yet to be reserved.

::: {.example}
An `MO (manufacturing order)`{.interpreted-text role="abbr"} is created
to produce three units of *wood*, which is used as a component for the
*rocking chair* product. Clicking the `Allocation`{.interpreted-text
role="guilabel"} smart button on the
`MO (manufacturing order)`{.interpreted-text role="abbr"} opens an
allocation report that lists open rocking chair
`MOs (manufacturing orders)`{.interpreted-text role="abbr"} that require
one or more pieces of wood.
:::

Click the `Assign All`{.interpreted-text role="guilabel"} or
`Assign`{.interpreted-text role="guilabel"} button to the right of a
specific `MO (manufacturing order)`{.interpreted-text role="abbr"} to
assign components to that `MO (manufacturing order)`{.interpreted-text
role="abbr"}.

{.align-center}

### Unassign products

After assigning products to a quantity within a delivery order, or
components to an `MO (manufacturing order)`{.interpreted-text
role="abbr"}, the `Assign`{.interpreted-text role="guilabel"} button
turns into an `Unassign`{.interpreted-text role="guilabel"} button.
Click `Unassign`{.interpreted-text role="guilabel"} to unreserve the
assigned products from that quantity, making them available for other
quantities.

### Print labels

After clicking `Assign All`{.interpreted-text role="guilabel"} or
`Assign`{.interpreted-text role="guilabel"}, the
`Print Labels`{.interpreted-text role="guilabel"} or
`Print Label`{.interpreted-text role="guilabel"} button to the right of
either button becomes selectable. Selecting either button generates and
downloads a PDF document with one label for each product that was
assigned. These labels are used to designate each product as being
reserved for that specific order.

{.align-center}
