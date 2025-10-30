# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/manage_deals/manage.md

Manage vendor bills
===================

::: {#inventory/purchase/manage_deals/manage}
A *vendor bill* is an invoice received for products and/or services
purchased by a company from a vendor. Vendor bills record payables as
they arrive from vendors, and can include amounts owed for the goods
and/or services purchased, sales taxes, freight and delivery charges,
and more.
:::

In Odoo, a vendor bill can be created at different points in the
purchasing process, depending on the *bill control* policy chosen in the
*Purchase* app\'s settings.

Bill control policies
---------------------

To configure the default bill control policy, navigate to
`Purchase app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}, and
scroll to the `Invoicing`{.interpreted-text role="guilabel"} section.

The `Bill Control`{.interpreted-text role="guilabel"} feature lists two
policy options: `Ordered quantities`{.interpreted-text role="guilabel"}
and `Received quantities`{.interpreted-text role="guilabel"}.

The policy selected acts as the default for any new product created.
Each policy acts as follows:

-   `Ordered quantities`{.interpreted-text role="guilabel"}: creates a
    vendor bill as soon as a purchase order is confirmed. The products
    and quantities in the purchase order are used to generate a draft
    bill.
-   `Received quantities`{.interpreted-text role="guilabel"}: a bill is
    only created **after** all (or part) of the total order has been
    received. The products and quantities received are used to generate
    a draft bill.

{.align-center}

Once a policy is selected, click `Save`{.interpreted-text
role="guilabel"} to save the changes.

::: {.tip}
::: {.title}
Tip
:::

If a product needs a different control policy than the one set in the
*Purchase* app settings, that product\'s control policy can be
overridden by going to the `Purchase`{.interpreted-text role="guilabel"}
tab on a product form, and selecting the desired policy in the
`Control Policy`{.interpreted-text role="guilabel"} field.

{.align-center}
:::

### 3-way matching

The *3-way matching* policy ensures vendor bills are only paid once all
(or some) products in a purchase order (PO) have been received.

To activate 3-way matching, navigate to
`Purchase app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and scroll to the
`Invoicing`{.interpreted-text role="guilabel"} section.

Tick the checkbox next to `3-way matching`{.interpreted-text
role="guilabel"}, and click `Save`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

The `3-way matching`{.interpreted-text role="guilabel"} feature is
**only** intended to work with the `Bill
Control`{.interpreted-text role="guilabel"} policy set to
`Received quantities`{.interpreted-text role="guilabel"}.
:::

Create and manage vendor bills on receipts
------------------------------------------

When products are received into a company\'s warehouse, receipts are
created. Once the company processes the received quantities, they can
choose to create a vendor bill directly from the warehouse receipt form.

Depending on the bill control policy chosen in the settings, vendor bill
creation is completed at different steps of the procurement process.

### Ordered quantities

To create and manage vendor bills for receipts with the *Bill Control*
policy set to *Ordered Quantities*, first navigate to the
`Purchase app`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"} from the
`Requests for Quotation`{.interpreted-text role="guilabel"} dashboard.

Doing so opens a new `Request for Quotation`{.interpreted-text
role="guilabel"} (RfQ) form. On the blank
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} form, add a
`Vendor`{.interpreted-text role="guilabel"}, and click
`Add a line`{.interpreted-text role="guilabel"} under the
`Product`{.interpreted-text role="guilabel"} tab to add products to the
order.

On the product line, select a product from the drop-down menu in the
`Product`{.interpreted-text role="guilabel"} field, and enter the
quantity to order in the `Quantity`{.interpreted-text role="guilabel"}
field.

Once ready, click `Confirm Order`{.interpreted-text role="guilabel"} to
confirm the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}
into a `PO (Purchase Order)`{.interpreted-text role="abbr"}.

Then, click `Create Bill`{.interpreted-text role="guilabel"} to create a
vendor bill. This opens a `Vendor Bill`{.interpreted-text
role="guilabel"} form in the `Draft`{.interpreted-text role="guilabel"}
state. From here, add a billing date in the
`Bill Date`{.interpreted-text role="guilabel"} field.

Once ready, confirm the bill by clicking `Confirm`{.interpreted-text
role="guilabel"} on the `Vendor Bill`{.interpreted-text role="guilabel"}
page.

::: {.tip}
::: {.title}
Tip
:::

Since the bill control policy is set to *Ordered quantities*, the draft
bill can be confirmed as soon as it is created, before any products have
been received.
:::

Once a payment has been received, click
`Register Payment`{.interpreted-text role="guilabel"} at the top of the
bill to record it.

Doing so causes a `Register Payment`{.interpreted-text role="guilabel"}
pop-up window to appear, wherein a payment `Journal`{.interpreted-text
role="guilabel"} can be chosen, and a `Payment Method`{.interpreted-text
role="guilabel"} selected.

Additionally, the bill `Amount`{.interpreted-text role="guilabel"},
`Payment Date`{.interpreted-text role="guilabel"}, and
`Memo`{.interpreted-text role="guilabel"}
(`Reference Number`{.interpreted-text role="dfn"}) can be edited from
this pop-up window, if necessary.

Once ready, click `Create Payment`{.interpreted-text role="guilabel"} to
finish creating the `Vendor Bill`{.interpreted-text role="guilabel"}.
Doing so displays a green `Paid`{.interpreted-text role="guilabel"}
banner on the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} form.

{.align-center}

### Received quantities

To create and manage vendor bills for receipts with the bill control
policy set to *Received quantities*, first navigate to the
`Purchase`{.interpreted-text role="menuselection"} app, and click
`New`{.interpreted-text role="guilabel"}.

Doing so opens a new `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} form. On the blank
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} form, add a
`Vendor`{.interpreted-text role="guilabel"}, and click
`Add a line`{.interpreted-text role="guilabel"} under the
`Product`{.interpreted-text role="guilabel"} tab to add products to the
order.

On the product line, select a product from the drop-down menu in the
`Product`{.interpreted-text role="guilabel"} field, and enter the
quantity to order in the `Quantity`{.interpreted-text role="guilabel"}
field.

Once ready, click `Confirm Order`{.interpreted-text role="guilabel"} to
confirm the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}
into a `PO (Purchase Order)`{.interpreted-text role="abbr"}.

::: {.important}
::: {.title}
Important
:::

When using the *Received quantities* control policy, clicking
`Create Bill`{.interpreted-text role="guilabel"} before any products are
received causes an `Invalid Operation`{.interpreted-text
role="guilabel"} pop-up window to appear.

Odoo requires at least partial quantities of the items included in the
`PO (Purchase Order)`{.interpreted-text role="abbr"} to be received in
order to create a vendor bill.

{.align-center}
:::

On the `PO (Purchase Order)`{.interpreted-text role="abbr"}, click the
`Receipt`{.interpreted-text role="guilabel"} smart button to view the
warehouse receipt form.

From here, click `Validate`{.interpreted-text role="guilabel"} to
register the `Done`{.interpreted-text role="guilabel"} (received)
quantities.

Then, navigate back to the `PO (Purchase Order)`{.interpreted-text
role="abbr"}, via the breadcrumb, and click
`Create Bill`{.interpreted-text role="guilabel"}.

This opens a `Vendor Bill`{.interpreted-text role="guilabel"} form in
the `Draft`{.interpreted-text role="guilabel"} state. From here, add a
billing date in the `Bill Date`{.interpreted-text role="guilabel"}
field. Once ready, confirm the bill by clicking
`Confirm`{.interpreted-text role="guilabel"} at the top of the draft.

Once a payment has been received, click
`Register Payment`{.interpreted-text role="guilabel"} at the top of the
bill to record it.

Doing so causes a `Register Payment`{.interpreted-text role="guilabel"}
pop-up window to appear, wherein a payment `Journal`{.interpreted-text
role="guilabel"} can be chosen, and a `Payment Method`{.interpreted-text
role="guilabel"} selected.

Additionally, the bill `Amount`{.interpreted-text role="guilabel"},
`Payment Date`{.interpreted-text role="guilabel"}, and
`Memo`{.interpreted-text role="guilabel"}
(`Reference Number`{.interpreted-text role="dfn"}) can be edited from
this pop-up window, if necessary.

Once ready, click `Create Payment`{.interpreted-text role="guilabel"} to
finish creating the `Vendor Bill`{.interpreted-text role="guilabel"}.
Doing so displays a green `Paid`{.interpreted-text role="guilabel"}
banner on the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} form.

Manage vendor bills in Accounting
---------------------------------

Vendor bills can also be created directly from the *Accounting* app,
without having to create a purchase order first.

Navigate to `Accounting app --> Vendors --> Bills`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}. Doing so reveals a blank
`Vendor Bill`{.interpreted-text role="guilabel"} form.

Add a vendor in the `Vendor`{.interpreted-text role="guilabel"} field.
Then, in the `Invoice Lines`{.interpreted-text role="guilabel"} tab,
click `Add a line`{.interpreted-text role="guilabel"} to add products.

Select a product from the drop-down menu in the
`Product`{.interpreted-text role="guilabel"} field, and enter the
quantity to order in the `Quantity`{.interpreted-text role="guilabel"}
field.

Select a `Bill Date`{.interpreted-text role="guilabel"}, and configure
any other necessary information. Finally, click
`Confirm`{.interpreted-text role="guilabel"} to confirm the bill.

Once confirmed, click the `Journal Items`{.interpreted-text
role="guilabel"} tab to view the `Account`{.interpreted-text
role="guilabel"} journals. These journals are populated based on the
configuration on the corresponding `Vendor`{.interpreted-text
role="guilabel"} and `Product`{.interpreted-text role="guilabel"} forms.

If necessary, click `Credit Note`{.interpreted-text role="guilabel"} to
add a credit note to the bill. Additionally, a
`Bill Reference`{.interpreted-text role="guilabel"} number can be added.

Once ready, click `Register Payment`{.interpreted-text role="guilabel"},
followed by `Create Payment`{.interpreted-text role="guilabel"}, to
complete the `Vendor Bill`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

To link a draft bill to an existing purchase order, click the drop-down
menu next to `Auto-Complete`{.interpreted-text role="guilabel"} *before*
clicking `Confirm`{.interpreted-text role="guilabel"}, and select a
`PO (Purchase Order)`{.interpreted-text role="abbr"} from the menu.

The bill auto-populates with the information from the chosen
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

{.align-center}
:::

Batch billing
-------------

Vendor bills can be processed and managed in batches in the *Accounting*
app.

Navigate to `Accounting app --> Vendors --> Bills`{.interpreted-text
role="menuselection"}. Then, click the `checkbox`{.interpreted-text
role="guilabel"} in the top-left corner, beside the
`Number`{.interpreted-text role="guilabel"} column, under the
`New`{.interpreted-text role="guilabel"} button.

This selects all existing vendor bills with a `Status`{.interpreted-text
role="guilabel"} of `Posted`{.interpreted-text role="guilabel"} or
`Draft`{.interpreted-text role="guilabel"}.

Click the `fa-print`{.interpreted-text role="icon"}
`Print`{.interpreted-text role="guilabel"} button to print the selected
invoices or bills.

Click `Register Payment`{.interpreted-text role="guilabel"} to create
and process payments for multiple vendor bills at once.

::: {.note}
::: {.title}
Note
:::

Only payments with their `Status`{.interpreted-text role="guilabel"}
listed as `Posted`{.interpreted-text role="guilabel"} can be billed in
batches. Payments in the `Draft`{.interpreted-text role="guilabel"}
stage **must** be posted before they can be included in a batch billing.
:::

Clicking `Register Payment`{.interpreted-text role="guilabel"} opens a
`Register Payment`{.interpreted-text role="guilabel"} pop-up window.
From the pop-up window, select the `Journal`{.interpreted-text
role="guilabel"} the bills should post to, choose a `Payment
Date`{.interpreted-text role="guilabel"}, and select a
`Payment Method`{.interpreted-text role="guilabel"}.

There is also the option to `Group Payments`{.interpreted-text
role="guilabel"} together from this pop-up window, as well. If this
checkbox is ticked, only one payment is created, instead of one per
bill. This option only appears if the *Batch Payments* feature is
enabled in the settings of the `Accounting`{.interpreted-text
role="menuselection"} app.

Once ready, click the `Create Payment`{.interpreted-text
role="guilabel"} button. This creates a list of journal entries on a
separate page. The journal entries on this list are all tied to their
corresponding vendor bills.

{.align-center}

::: {.seealso}
`control_bills`{.interpreted-text role="doc"}
:::
