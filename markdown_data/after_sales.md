# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/advanced/after_sales.md

After-Sales services
====================

*After-Sales* services can be configured in the *Helpdesk* application
for individual teams. Once enabled, users can
`issue refunds <helpdesk/refunds>`{.interpreted-text role="ref"},
`generate coupons
<helpdesk/coupons>`{.interpreted-text role="ref"},
`process returns <helpdesk/returns>`{.interpreted-text role="ref"}, and
`schedule repairs
<helpdesk/repairs>`{.interpreted-text role="ref"} or
`field service interventions <helpdesk/field>`{.interpreted-text
role="ref"} directly from a ticket.

Set up after-sales services
---------------------------

Start by enabling the after-sales services on a specific *Helpdesk*
team, by going to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} and click on the team the services should be
applied to. Then, scroll to the `After-Sales`{.interpreted-text
role="guilabel"} section on the team\'s settings page, and choose which
of the following options to enable:

-   `Refunds`{.interpreted-text role="guilabel"}: issues credit notes to
    refund a customer, or adjust the remaining amount due.
-   `Coupons`{.interpreted-text role="guilabel"}: offers discounts and
    free products through an existing coupon program.
-   `Returns`{.interpreted-text role="guilabel"}: initiates a product
    return from a customer through a reverse transfer.
-   `Repairs`{.interpreted-text role="guilabel"}: creates repair orders
    for broken or faulty products.
-   `Field Service`{.interpreted-text role="guilabel"}: plans onsite
    intervention through the *Field Service* application.

![The services that are enabled can vary based on the type of support a
team provides.](after_sales/after-sales-enable.png){.align-center}

::: {.danger}
::: {.title}
Danger
:::

Since all the after-sales services in Odoo require integration with
other applications, enabling any of them may result in the installation
of additional modules or applications. Installing a new application on a
One-App-Free database triggers a 15-day trial. At the end of the trial,
if a paid subscription has not been added to the database, it will no
longer be accessible.
:::

Issue refund with credit note {#helpdesk/refunds}
-----------------------------

A *credit note* is a document issued to a customer informing them that
they have been credited a certain amount of money. They can be used to
provide a full refund to a customer, or to adjust any remaining amount
due. While they are usually created through the *Accounting* or
*Invoicing* applications, they can be created through a *Helpdesk*
ticket, as well.

::: {.important}
::: {.title}
Important
:::

Invoices **must** be posted before a credit note can be generated.
:::

To create a credit note, navigate to a ticket on the
`Helpdesk app`{.interpreted-text role="menuselection"}, and click the
`Refund`{.interpreted-text role="guilabel"} button in the top-left
corner of the ticket form. This opens a `Refund`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

Fill out the fields with the necessary information:

> -   `Sales Order`{.interpreted-text role="guilabel"}: if a sales order
>     was referenced on the original ticket, it automatically populates
>     in this field.
> -   `Product`{.interpreted-text role="guilabel"}: the product the
>     ticket is about. If an item is selected in this field, only the
>     sales orders, deliveries, and invoices including this product can
>     be selected.
> -   `Lot/Serial Number`{.interpreted-text role="guilabel"}: this field
>     is **only** visible if the `Product`{.interpreted-text
>     role="guilabel"} selected has associated lot or serial numbers.
> -   `Invoices to Refund`{.interpreted-text role="guilabel"}: this
>     field is **required**. If no invoices are available in the
>     drop-down, it indicates this customer currently has no posted
>     invoices, or the `Product`{.interpreted-text role="guilabel"} has
>     no related invoices.
> -   `Reason displayed on Credit Note`{.interpreted-text
>     role="guilabel"}: this field automatically populates with the
>     ticket number, though it can be edited with additional
>     information.
> -   `Journal`{.interpreted-text role="guilabel"}: the accounting
>     journal where the credit note should be posted. After an invoice
>     is selected, this field defaults to the journal listed on the
>     original invoice, though it can be changed, if necessary.
> -   `Reversal date`{.interpreted-text role="guilabel"}: when this
>     field is clicked, use the pop-up calendar that appears to select a
>     date for the credit note invoice. This field is **required**.

After the necessary fields are filled in, click
`Reverse`{.interpreted-text role="guilabel"} or `Reverse and Create
Invoice`{.interpreted-text role="guilabel"}.

`Reverse`{.interpreted-text role="guilabel"} creates a credit note in a
draft state that can be edited before it is posted. This option can be
used to provide a partial refund.

`Reverse and Create Invoice`{.interpreted-text role="guilabel"} creates
a credit note that is automatically posted as well as an invoice in a
draft state. The invoice contains the same information as the original
invoice, though this information can be altered.

Once the credit note has been posted, a `Credit Notes`{.interpreted-text
role="guilabel"} smart button is added to the *Helpdesk* ticket.

{.align-center}

::: {.seealso}
`../../../finance/accounting/customer_invoices/credit_notes`{.interpreted-text
role="doc"}
:::

Generate coupons from a ticket {#helpdesk/coupons}
------------------------------

Coupons can be used to alter the price of products or orders.
Conditional rules define the usage constraints of a coupon. *Coupon
Programs* are configured in the *Sales*, *Point of Sale*, or *Website*
applications.

::: {.important}
::: {.title}
Important
:::

The *eCommerce* module **must** be installed to create coupon codes from
the *Website*.
:::

To generate a coupon, open a *Helpdesk* ticket and click on the
`Coupon`{.interpreted-text role="guilabel"} button in the top-left
corner. Select an option from the `Coupon Program`{.interpreted-text
role="guilabel"} drop-down menu in the
`Generate a Coupon`{.interpreted-text role="guilabel"} pop-up window
that appears.

{.align-center}

::: {.note}
::: {.title}
Note
:::

To create a new `Coupon Program`{.interpreted-text role="guilabel"},
navigate to `Sales app --> Products
--> Discount & Loyalty`{.interpreted-text role="menuselection"} and
click `New`{.interpreted-text role="guilabel"}. To make the program
available to share with *Helpdesk* customers, the
`Program Type`{.interpreted-text role="guilabel"} **must** be set to
`Coupons`{.interpreted-text role="guilabel"}. This generates single-use
coupon codes that grant immediate access to rewards and discounts.

Coupon programs can also be created in the *Point of Sale* application
or *Website* application. Refer to `discount and loyalty programs
<../../../sales/sales/products_prices/loyalty_discount>`{.interpreted-text
role="doc"} for more information.
:::

Click on the `Valid Until`{.interpreted-text role="guilabel"} field, and
use the pop-up calendar to select an expiration date for this coupon
code. If this field is left blank, the code does **not** expire.

Click `Send by Email`{.interpreted-text role="guilabel"} to compose an
email to send to the customer with the coupon code.

::: {.note}
::: {.title}
Note
:::

When emailing a coupon code, **all** the followers of the ticket are
added as recipients to the email. Additional recipients can be added to
the email as well, in the `Recipients`{.interpreted-text
role="guilabel"} field of the `Compose Email`{.interpreted-text
role="guilabel"} pop-up window. If an expiration date was selected for
the code, it is included in the message template.

{.align-center}
:::

Click `Get Share Link`{.interpreted-text role="guilabel"} to generate a
link to send directly to the customer. Doing so opens a
`Share Coupons`{.interpreted-text role="guilabel"} pop-up window. Click
the `Copy`{.interpreted-text role="guilabel"} button next to the
`Share Link`{.interpreted-text role="guilabel"} field and paste the
results to any communication with the customer. When the customer uses
the link, the code is automatically applied to their cart.

After a `Coupon Code`{.interpreted-text role="guilabel"} has been
generated, a `Coupons`{.interpreted-text role="guilabel"} smart button
is added to the top of the ticket; click the smart button to view the
coupon code, expiration date, and additional information.

{.align-center}

::: {.seealso}
\-  -
`../../../sales/sales/products_prices/loyalty_discount`{.interpreted-text
role="doc"}
:::

Facilitate a product return with a reverse transfer {#helpdesk/returns}
---------------------------------------------------

Returns are completed through *reverse transfers*, which generate new
warehouse operations for the returning products. Click the
`Return`{.interpreted-text role="guilabel"} button in the top-left
corner of a ticket to open the `Reverse Transfer`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The `Return`{.interpreted-text role="guilabel"} button **only** appears
on a ticket if the customer has a recorded delivery in the database.
:::

Select a `Sales Order`{.interpreted-text role="guilabel"} or
`Delivery to Return`{.interpreted-text role="guilabel"} to identify the
products that need to be returned.

By default, the quantity matches the validated quantity from the
delivery order. Update the `Quantity`{.interpreted-text role="guilabel"}
field, if necessary. To remove a line, click the
`🗑️ (trash can)`{.interpreted-text role="guilabel"} icon.

Select a `Return Location`{.interpreted-text role="guilabel"} where the
items should be directed after the return is completed.

{.align-center}

Click `Return`{.interpreted-text role="guilabel"} to confirm the return.
This generates a new warehouse operation for the incoming returned
products.

Use the breadcrumbs to return to the helpdesk ticket. A new
`Return`{.interpreted-text role="guilabel"} smart button can now be
accessed at the top of the ticket.

{.align-center}

::: {.seealso}
`../../../sales/sales/products_prices/returns`{.interpreted-text
role="doc"}
:::

Send products for repair from a ticket {#helpdesk/repairs}
--------------------------------------

If the ticket is related to an issue with a faulty or broken product, a
*repair order* can be created from the *Helpdesk* ticket, and managed
through the *Repairs* application.

To create a new repair order, open a `Helpdesk`{.interpreted-text
role="menuselection"} ticket and click on the `Repair`{.interpreted-text
role="guilabel"} button in the top-left corner. This opens a
`Repair Reference`{.interpreted-text role="guilabel"} form.

{.align-center}

Fill out the fields with the necessary information:

> -   `Customer`{.interpreted-text role="guilabel"}: this field carries
>     over from the ticket, though a new contact can been selected from
>     the drop-down menu.
> -   `Product to Repair`{.interpreted-text role="guilabel"}: if a
>     product was specified in the `Product`{.interpreted-text
>     role="guilabel"} field on the ticket, it is added to this field
>     automatically. If not, click into the field to select a product
>     from the drop-down menu.
> -   `Lot/Serial`{.interpreted-text role="guilabel"}: this field is
>     **only** visible if the products being repaired are tracked, via
>     lot or serial numbers.
> -   `Return`{.interpreted-text role="guilabel"}: return order from
>     which the product to be repaired comes from.
> -   `Under Warranty`{.interpreted-text role="guilabel"}: if this box
>     is checked, the sale price for all products from the repair order
>     are set to zero.
> -   `Scheduled Date`{.interpreted-text role="guilabel"}: this field
>     defaults to the current date. To select a new date, click into the
>     field and select a date using the drop-down calendar.
> -   `Responsible`{.interpreted-text role="guilabel"}: assign a user
>     from the drop-down menu to manage the repair.
> -   `Tags`{.interpreted-text role="guilabel"}: click into this field
>     to assign an existing tag or create a new one. Multiple tags can
>     be assigned.

If parts are required for the repair, they can be added in the
`Parts`{.interpreted-text role="guilabel"} tab. Additional information
for the internal repair team can be added to the
`Repair Notes`{.interpreted-text role="guilabel"} tab.

Once the form is complete, click `Confirm Repair`{.interpreted-text
role="guilabel"}. To create, edit, and send a quote for this repair,
click `Create Quotation`{.interpreted-text role="guilabel"}.

A `Repairs`{.interpreted-text role="guilabel"} smart button is then
added to the ticket, linking to the repair order.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Once a user creates a repair order from a *Helpdesk* ticket, they can
access it through the ticket\'s `Repair`{.interpreted-text
role="guilabel"} smart button, or from a link in the chatter, even if
they do not have access rights to the *Repair* application.
:::

Create field service task from a ticket {#helpdesk/field}
---------------------------------------

On-site interventions can be planned from a ticket and managed through
the *Field Service* application. Customers with
`portal access <../../../general/users/portal>`{.interpreted-text
role="doc"} are able to track the progress of a *Field Service* task
just as they would a *Helpdesk* ticket.

::: {.tip}
::: {.title}
Tip
:::

To change the default *Field Service* project for the team, go to
`Helpdesk app
--> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} to select a `Team`{.interpreted-text
role="guilabel"}. Scroll to the `After-Sales`{.interpreted-text
role="guilabel"} section, and choose a project under
`Field Service`{.interpreted-text role="guilabel"}.
:::

To create a new *Field Service* task, navigate to a
`Helpdesk`{.interpreted-text role="menuselection"} ticket. Click
`Plan Intervention`{.interpreted-text role="guilabel"} to open the
`Create a Field Service task`{.interpreted-text role="guilabel"} pop-up
window.

{.align-center}

Confirm or update the task `Title`{.interpreted-text role="guilabel"}.

The `Project`{.interpreted-text role="guilabel"} field on the
`Create a Field Service task`{.interpreted-text role="guilabel"} pop-up
window defaults to the same *Field Service* project that was identified
on the team\'s settings page. To change the project for this specific
task, select one from the `Project`{.interpreted-text role="guilabel"}
field.

If applicable, select a `Worksheet Template`{.interpreted-text
role="guilabel"} from the drop-down menu.

::: {.note}
::: {.title}
Note
:::

*Field Service Worksheets* are reports that detail the work completed
during an on-site task. When work is completed, worksheets are signed by
the customer to confirm the job is done and the customer is satisfied.

If the *Field Service* project assigned to the *Helpdesk* team has
worksheets enabled, and has a default template assigned, that template
automatically appears in the `Worksheet
Template`{.interpreted-text role="guilabel"} drop-down field. Even so,
the field can be edited, and another template can be selected.

If the *Field Service* project does **not** have worksheets enabled, the
`Worksheet
Template`{.interpreted-text role="guilabel"} field does not appear on
the `Create a Field Service task`{.interpreted-text role="guilabel"}
pop-up window.
:::

Click `Create Task`{.interpreted-text role="guilabel"} or
`Create & View Task`{.interpreted-text role="guilabel"}.

After the task is created, a `Tasks`{.interpreted-text role="guilabel"}
smart button is added to the ticket, linking the
`Field Service`{.interpreted-text role="guilabel"} task to the ticket.

{.align-center}

::: {.seealso}
[Field
Service](https://www.odoo.com/slides/slide/advanced-settings-862?fullscreen=1)
:::
