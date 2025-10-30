# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.md

Manufacturing order costs
=========================

The ability to accurately calculate the cost of manufacturing a product
is critical when determining product profitability. Odoo\'s
*Manufacturing* app simplifies this calculation by automatically
calculating the cost to complete each manufacturing order (MO), as well
as the average production cost of a product, based on all completed
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"}.

::: {.important}
::: {.title}
Important
:::

Odoo\'s Manufacturing app distinguishes between the *manufacturing order
cost* and the *real cost* of an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

The `MO (Manufacturing Order)`{.interpreted-text role="abbr"} cost
represents how much it *should* cost to complete an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, based on the
configuration of the product\'s bill of materials (BoM). This takes into
account the cost and quantity of components, as well as the cost of
completing the necessary operations.

The real cost represents how much it *actually* costs to complete the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}. A few factors
can cause the real cost to differ from the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} cost. For
example, an operation may take longer to complete than estimated, a
greater component quantity might be needed than was specified on the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, or the price
of components may change during manufacturing.
:::

Cost configuration
------------------

Odoo computes `MO (Manufacturing Order)`{.interpreted-text role="abbr"}
costs based on the configuration of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} used to
manufacture a product. This includes the cost and quantity of components
and operations listed on the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, in addition to the operating costs of the work centers
where those operations are carried out.

### Component cost

Component cost is calculated automatically, based on the average
purchase cost of a component across all purchase orders (POs). To view a
component\'s cost, navigate to `Inventory app -->
Products --> Products`{.interpreted-text role="guilabel"}, and select a
component product. The cost is displayed in the `Cost`{.interpreted-text
role="guilabel"} field of the `General Information`{.interpreted-text
role="guilabel"} tab, on the component\'s product form.

It is possible to set the cost of a component manually, by clicking the
`Cost`{.interpreted-text role="guilabel"} field on the component\'s
product form, and entering a value. However, any future
`POs (Purchase Orders)`{.interpreted-text role="abbr"} for the component
override a value entered manually, resetting the
`Cost`{.interpreted-text role="guilabel"} field back to an automatically
computed value.

### Work center cost

To set the operating cost for a specific work center, navigate to
`Manufacturing app
--> Configuration --> Work Centers`{.interpreted-text
role="menuselection"}, and select a work center.

To set the operating cost for the work center, as a whole, enter a value
in the `per
workcenter`{.interpreted-text role="guilabel"} field, located beside the
`Cost per hour`{.interpreted-text role="guilabel"} section on the work
center\'s `General Information`{.interpreted-text role="guilabel"} tab.
This operating cost is used regardless of how many employees are working
at the work center at any given time.

To set the operating cost for the work center based on the number of
employees working there at a given time, enter a value in the
`per employee`{.interpreted-text role="guilabel"} field, located beside
the `Cost
per hour`{.interpreted-text role="guilabel"} section on the work
center\'s `General Information`{.interpreted-text role="guilabel"} tab.
For example, if [25.00]{.title-ref} is entered in the
`per employee`{.interpreted-text role="guilabel"} field, it costs
\$25.00 per hour for *each* employee working at the work center.

Note that, if values are entered in both the
`per workcenter`{.interpreted-text role="guilabel"} *and* `per
employee`{.interpreted-text role="guilabel"} fields, the value in the
`per workcenter`{.interpreted-text role="guilabel"} field takes
precedence, and the value in the `per employee`{.interpreted-text
role="guilabel"} field is ignored.

::: {.important}
::: {.title}
Important
:::

It is also possible to set a per hour cost for specific employees, by
navigating to the `Employees`{.interpreted-text role="menuselection"}
app, selecting an employee, clicking the `HR Settings`{.interpreted-text
role="guilabel"} tab on their employee form, and entering a value in the
`Hourly Cost`{.interpreted-text role="guilabel"} field.

Just like the *per workcenter* field on a work center form, the
`Hourly Cost`{.interpreted-text role="guilabel"} field on an employee\'s
form overrides the *per employee* field on a work center form.

However, the *per workcenter* field takes precedence over both the *per
employee* field on the workcenter form *and* the
`Hourly Cost`{.interpreted-text role="guilabel"} field on the employee
form.
:::

### `BoM (Bill of Materials)`{.interpreted-text role="abbr"} cost

Configuring a `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
so Odoo can accurately calculate the cost of
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"} that use it
requires two steps. First, components **must** be added, and the
required quantity specified. Second, operations **must** be added, along
with the work centers where they are carried out.

Begin by navigating to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"}. Select a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, or create a
new one by clicking `New`{.interpreted-text role="guilabel"}.

In the `Components`{.interpreted-text role="guilabel"} tab of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} form, add each
component by clicking `Add a
line`{.interpreted-text role="guilabel"}, selecting the component from
the drop-down menu in the `Component`{.interpreted-text role="guilabel"}
column, and entering the quantity in the `Quantity`{.interpreted-text
role="guilabel"} column.

In the `Operations`{.interpreted-text role="guilabel"} tab, add an
operation by clicking `Add a line`{.interpreted-text role="guilabel"} to
open the `Create Operations`{.interpreted-text role="guilabel"} pop-up
window. Enter a title for the operation in the
`Operation`{.interpreted-text role="guilabel"} field.

Select the `Work Center`{.interpreted-text role="guilabel"} where the
operation is carried out. Then, add a
`Default Duration`{.interpreted-text role="guilabel"}, which is the
estimated amount of time the operation takes to complete.

By default, the `Duration Computation`{.interpreted-text
role="guilabel"} field is set to
`Set duration manually`{.interpreted-text role="guilabel"}, which means
that the number entered in `Default Duration`{.interpreted-text
role="guilabel"} field is always used as the expected duration of the
operation.

Selecting `Compute based on tracked time`{.interpreted-text
role="guilabel"} causes Odoo to automatically compute the default
duration based on a certain number of work orders, which is set in the
`Based on`{.interpreted-text role="guilabel"} field. Before there are
work orders to compute this duration, the value in the
`Default Duration`{.interpreted-text role="guilabel"} field is used
instead.

The hourly cost of operating the work center, and the duration of the
operation, are used to calculate the operation\'s cost.

Finally, click `Save & Close`{.interpreted-text role="guilabel"} to add
the operation to the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}, and close the `Create Operations`{.interpreted-text
role="guilabel"} pop-up window. Alternatively, click
`Save & New`{.interpreted-text role="guilabel"} to add the operation to
the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, and open a
blank `Create Operations`{.interpreted-text role="guilabel"} pop-up
window to add another operation.

::: {.seealso}
For a full overview of `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} configuration, see the documentation on `bills of materials
<bill_configuration>`{.interpreted-text role="doc"}.
:::

`MO (Manufacturing Order)`{.interpreted-text role="abbr"} overview
------------------------------------------------------------------

Each `MO (Manufacturing Order)`{.interpreted-text role="abbr"} has an
*overview* page, which lists a variety of information about the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, including
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} cost and real
cost. To view the overview for an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, navigate to
`Manufacturing
app --> Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}, and select an
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}. Then, click
the `fa-bars`{.interpreted-text role="icon"}
`Overview`{.interpreted-text role="guilabel"} smart button at the top of
the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

Both the `MO (Manufacturing Order)`{.interpreted-text role="abbr"} cost
and real cost take into account the cost and quantity of components, as
well as the cost of completing each work order. The overview page lists
a row for each of these values, with the sum of them listed at the
bottom of the `MO Cost`{.interpreted-text role="guilabel"} and
`Real Cost`{.interpreted-text role="guilabel"} columns.

Before work begins on an `MO (Manufacturing Order)`{.interpreted-text
role="abbr"}, the `MO Cost`{.interpreted-text role="guilabel"} and
`Real Cost`{.interpreted-text role="guilabel"} columns display the same
costs. This is the *estimated* cost of completing the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

However, once work commences, the values in the
`Real Cost`{.interpreted-text role="guilabel"} column may begin to
diverge from the values in the `MO Cost`{.interpreted-text
role="guilabel"} column. This happens if a different component quantity
is used than was listed on the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}, or if the
duration of a work order is different than expected.

Once the `MO (Manufacturing Order)`{.interpreted-text role="abbr"} has
been completed by clicking `Produce All`{.interpreted-text
role="guilabel"}, the values in the `MO Cost`{.interpreted-text
role="guilabel"} column update to match those displayed in the
`Real Cost`{.interpreted-text role="guilabel"} column.

{.align-center}

Average manufacturing cost
--------------------------

In addition to the cost of each individual
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} for a product,
Odoo also tracks the average cost of manufacturing the product, taking
into account the cost of every completed
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}. To view this,
navigate to `Inventory app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product.

The manufacturing cost of the product is displayed per unit of measure
in the `Cost`{.interpreted-text role="guilabel"} field, located in the
`General Information`{.interpreted-text role="guilabel"} tab. The value
continues to update as the costs of additional
`MOs (Manufacturing Orders)`{.interpreted-text role="abbr"} are factored
into the average cost.

To the right of the `Cost`{.interpreted-text role="guilabel"} field is a
`Compute Price from BoM`{.interpreted-text role="guilabel"} button,
which only appears for products with at least one
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. Click this
button to reset the cost of the product to the expected cost, which only
takes into account the components and operations listed on the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

::: {.important}
::: {.title}
Important
:::

Be aware that clicking `Compute Price from BoM`{.interpreted-text
role="guilabel"} does not set the price permanently. The cost continues
to update based on the average of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} price and the
real cost of any future `MOs (Manufacturing Orders)`{.interpreted-text
role="abbr"}.
:::

::: {.admonition .alert .alert-success}
Example workflow: manufacturing cost

Golf product manufacturer *Fairway Fields* produces a variety of golf
products, including an indoor *putting green*. They have configured a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} for the putting
green, so Odoo automatically calculates the manufacturing cost of each
putting green `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.

The `BoM (Bill of Materials)`{.interpreted-text role="abbr"} lists two
components:

-   One unit of *green felt*, which costs \$20.00.
-   One unit of a *rubber pad*, which costs \$30.00.

The `BoM (Bill of Materials)`{.interpreted-text role="abbr"} also lists
four operations, all of which are carried out at *Assembly Station 1*,
which has an hourly operating cost of \$30.00. Those operations are as
follows:

-   *Cut felt*: default duration of seven minutes, for a total cost of
    \$3.50.
-   *Cut rubber pad*: default duration of five minutes, for a total cost
    of \$2.50.
-   *Attach pad to felt*: default duration of 15 minutes, for a total
    cost of \$7.50.
-   *Cut holes*: default duration of three minutes, for a total cost of
    \$1.50.

Altogether, the components required to produce one putting green cost
\$50.00, and the operations required cost \$15.00, for a total
manufacturing cost of \$65.00. This cost is reflected in the
`Cost`{.interpreted-text role="guilabel"} field on the putting green\'s
product form.

Fairway Fields confirms an `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} for one putting green. Before manufacturing starts, the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} overview lists
a cost of [\$65.00]{.title-ref} in both the `MO Cost`{.interpreted-text
role="guilabel"} and `Real Cost`{.interpreted-text role="guilabel"}
fields.

{.align-center}

Manufacturing begins, and the operations take ten minutes longer than
expected, for a total manufacturing time of 40 minutes. This deviation
from the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} is
reflected on the `MO (Manufacturing Order)`{.interpreted-text
role="abbr"} overview, which now lists a `Real Cost`{.interpreted-text
role="guilabel"} of [\$70.00]{.title-ref}.

{.align-center}

Once manufacturing is finished, and the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} is marked as
*Done*, the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}
overview updates again, so the values in the `MO Cost`{.interpreted-text
role="guilabel"} and `Real Cost`{.interpreted-text role="guilabel"}
columns match, each displaying a value of [\$70.00]{.title-ref}.

On the putting green\'s product page, the `Cost`{.interpreted-text
role="guilabel"} field now displays a cost of [\$67.50]{.title-ref}, the
average of the original cost of \$65.00 and the real cost of \$70.00
from the `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.
:::
