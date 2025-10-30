Create quotations
=================

In Odoo **Sales**, quotations can be created and sent to customers. Once
a quotation has been confirmed, it officially turns into a *sales
order*, which can then be invoiced and paid for.

Quotation settings {#sales/quotation-settings}
------------------

To access these setting options, navigate to
`Sales app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and scroll to the
`Quotations & Orders`{.interpreted-text role="guilabel"} section.

{.align-center}

-   `Quotation Templates`{.interpreted-text role="guilabel"}: Enable
    this option to create quotation templates featuring standard product
    offers, which are then selectable on quotation forms. When this
    checkbox is ticked, an additional field,
    `Default Template`{.interpreted-text role="guilabel"}, appears,
    along with a link to the `Quotation Templates`{.interpreted-text
    role="guilabel"} page.
-   `Online Signature`{.interpreted-text role="guilabel"}: Request an
    online signature to confirm orders.
-   `Online Payment`{.interpreted-text role="guilabel"}: Request an
    online prepayment from customers to confirm orders. Request a full
    or partial payment (via down payment). When this checkbox is ticked,
    an additional field, `Prepayment amount (%)`{.interpreted-text
    role="guilabel"}, appears. There is also a link to the `Payment
    Providers`{.interpreted-text role="guilabel"} page.
-   `Default Quotation Validity`{.interpreted-text role="guilabel"}:
    Determine a set amount (in `days`{.interpreted-text
    role="guilabel"}) that quotations can remain valid for.
-   `Default Recurrence`{.interpreted-text role="guilabel"}: Select a
    default period from the drop-down menu to use as a recurrence period
    for a new quotation.
-   `Sale Warnings`{.interpreted-text role="guilabel"}: Get warning
    messages about orders that include specific products or customers.
-   `PDF Quote builder`{.interpreted-text role="guilabel"}: Customize
    the look of quotations with header pages, product descriptions,
    footer pages, and more.
-   `Lock Confirmed Sales`{.interpreted-text role="guilabel"}: Ensure no
    further edits can be made to confirmed orders.
-   `Pro-Forma Invoice`{.interpreted-text role="guilabel"}: Send
    pro-forma invoices to customers.

To activate any of these settings, tick the checkbox beside the desired
option(s). Then, click `Save`{.interpreted-text role="guilabel"}.

Quotations dashboard
--------------------

The *Quotations* dashboard is the page that appears when the
`Sales app`{.interpreted-text role="menuselection"} is opened.

By default, the `Quotations`{.interpreted-text role="guilabel"}
dashboard displays all quotations in the database related to the current
user, as indicated by the default `My Quotations`{.interpreted-text
role="guilabel"} filter present in the search bar.

{.align-center}

::: {.note}
::: {.title}
Note
:::

To view *all* quotations in the database, remove the
`My Quotations`{.interpreted-text role="guilabel"} filter from the
search bar.
:::

Quotations on this page appear in a default list view, but can also be
viewed in a `oi-view-kanban`{.interpreted-text role="icon"}
`Kanban`{.interpreted-text role="guilabel"} view,
`fa-calendar`{.interpreted-text role="icon"}
`Calendar`{.interpreted-text role="guilabel"},
`oi-view-pivot`{.interpreted-text role="icon"} `Pivot`{.interpreted-text
role="guilabel"} table, `fa-area-chart`{.interpreted-text role="icon"}
`Graph`{.interpreted-text role="guilabel"}, or
`fa-clock-o`{.interpreted-text role="icon"} `Activity`{.interpreted-text
role="guilabel"} view.

To view and/or modify any listed quotation from the
`Quotations`{.interpreted-text role="guilabel"} dashboard, click on the
desired quotation line from the list, and Odoo reveals the specific form
for that selected quotation.

Create quotation
----------------

To create a quotation, open the `Sales app`{.interpreted-text
role="menuselection"}, and click the `New`{.interpreted-text
role="guilabel"} button, located in the upper-left corner of the main
`Quotations`{.interpreted-text role="guilabel"} dashboard.

::: {.important}
::: {.title}
Important
:::

The `New`{.interpreted-text role="guilabel"} button is **only** present
if the `Quotations`{.interpreted-text role="guilabel"} dashboard is in
list or Kanban view.
:::

Clicking the `New`{.interpreted-text role="guilabel"} button reveals a
blank quotation form, with various fields and tabs to configure.

{.align-center}

Begin by entering the customer\'s name in the
`Customer`{.interpreted-text role="guilabel"} field at the top of the
form. This is a **required** field.

If the customer\'s information is already in the database, the
`Invoice Address`{.interpreted-text role="guilabel"} and
`Delivery Address`{.interpreted-text role="guilabel"} fields
auto-populate with the saved information for those respective fields,
based on the data from that customer\'s contact record (found in the
**Contacts** application).

If the customer was referred by another customer or contact, enter their
name in the `Referrer`{.interpreted-text role="guilabel"} field.

If a `Referrer`{.interpreted-text role="guilabel"} is selected, a new
field, `Commission Plan`{.interpreted-text role="guilabel"} appears, in
which a commission can be selected from the drop-down menu. This
commission is rewarded to the contact selected in the
`Referrer`{.interpreted-text role="guilabel"} field.

Next, if they have not already been auto-populated with the customer\'s
information, enter the appropriate addresses in the
`Invoice Address`{.interpreted-text role="guilabel"} and
`Delivery Address`{.interpreted-text role="guilabel"} fields. Both of
these fields are **required**.

Then, if desired, choose a `Quotation Template`{.interpreted-text
role="guilabel"} from the drop-down field to apply to this quotation. It
should be noted that some additional fields may appear, depending on the
template selected.

The default date that appears in the `Expiration`{.interpreted-text
role="guilabel"} field is based on the number configured in the
`Default Quotation Validity setting <sales/quotation-settings>`{.interpreted-text
role="ref"} (in
`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}).

::: {.tip}
::: {.title}
Tip
:::

When using a quotation template, the date in the
`Expiration`{.interpreted-text role="guilabel"} field is based off the
`Quotation Validity`{.interpreted-text role="guilabel"} figure on the
template form.
:::

If the quotation is for a recurring product or subscription, select the
desired `Recurring
Plan`{.interpreted-text role="guilabel"} from that specific drop-down
menu.

If desired, select a specific `Pricelist`{.interpreted-text
role="guilabel"} to be applied to this quotation.

Lastly, select any specific `Payment Terms`{.interpreted-text
role="guilabel"} to be used for this quotation.

### Order Lines tab

The first tab on the quotation form is the
`Order Lines`{.interpreted-text role="guilabel"} tab.

In this tab, select products, and quantities of those products, to add
them to the quotation.

There are two ways to add products to the quotation from this tab.

Click `Add a product`{.interpreted-text role="guilabel"}, select the
desired item from the `Product`{.interpreted-text role="guilabel"}
drop-down field, and proceed to adjust the quantity of that selected
product, if necessary.

Or, click `Catalog`{.interpreted-text role="guilabel"} to reveal a
separate page, showcasing every item (and every potential product
variant) in an organized catalog display, with items organizable by
`Product
Category`{.interpreted-text role="guilabel"} and
`Attributes`{.interpreted-text role="guilabel"}.

{.align-center}

From here, simply locate the desired items, click the
`fa-shopping-cart`{.interpreted-text role="icon"}
`Add`{.interpreted-text role="guilabel"} button on the product card, and
adjust the quantity, if needed. When complete, click the
`Back to Quotation`{.interpreted-text role="guilabel"} button in the
upper-left corner to return to the quotation, where the newly-selected
catalog items can be found in the `Order Lines`{.interpreted-text
role="guilabel"} tab.

If multiple items should be presented in a more organized way on the
quotation, click `Add
a section`{.interpreted-text role="guilabel"}, enter a name for the
section, and drag-and-drop that section heading in the desired location
amongst the items in the `Order Lines`{.interpreted-text
role="guilabel"} tab. The section heading appears in bold.

If needed, click `Add a note`{.interpreted-text role="guilabel"} beneath
a certain product line to add a custom note about that specific product.
The note appears in italics. Then, if needed, proceed to drag-and-drop
the note beneath the desired product line.

Beneath the product lines, there are buttons that can be clicked to
apply any of the following: `Coupon Code`{.interpreted-text
role="guilabel"}, `Promotions`{.interpreted-text role="guilabel"},
`Discount`{.interpreted-text role="guilabel"}, and/or `Add
shipping`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `../products_prices/ewallets_giftcards`{.interpreted-text role="doc"}
- `../products_prices/loyalty_discount`{.interpreted-text role="doc"} -
`../products_prices/prices/pricing`{.interpreted-text role="doc"}
:::

### Optional Products tab

Open the `Optional Products`{.interpreted-text role="guilabel"} tab to
select related products that can be presented to the customer, which may
result in an increased sale.

For example, if the customer wants to buy a car, an optional product
that could be offered is a *Trailer Hitch*.

::: {.seealso}
`optional_products`{.interpreted-text role="doc"}
:::

### Other Info tab

In the `Other Info`{.interpreted-text role="guilabel"} tab, there are
various quotation-related configurations separated into four different
sections: `Sales`{.interpreted-text role="guilabel"},
`Delivery`{.interpreted-text role="guilabel"},
`Invoicing`{.interpreted-text role="guilabel"}, and
`Tracking`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Some fields **only** appear if specific settings and options have been
configured.
:::

#### Sales section

In the `Sales`{.interpreted-text role="guilabel"} section of the
`Other Info`{.interpreted-text role="guilabel"} tab, there are sales
specific fields that can be configured.

{.align-center}

-   `Salesperson`{.interpreted-text role="guilabel"}: Assign a
    salesperson from the drop-down menu to be associated with this
    quotation. The user who originally created the quotation is selected
    in this field, by default.
-   `Sales Team`{.interpreted-text role="guilabel"}: Assign a specific
    sales team to this quotation. If the selected
    `Salesperson`{.interpreted-text role="guilabel"} is a member of a
    sales team, that team is auto-populated in the field.
-   `Company`{.interpreted-text role="guilabel"}: Select a company from
    the drop-down menu this quotation should be associated with. This
    field only appears when working in a multi-company environment.
-   `Online signature`{.interpreted-text role="guilabel"}: Tick this
    checkbox to request an online signature from the customer to confirm
    the order. This field only appears if the *Online Signature* setting
    has been enabled.
-   `Online payment`{.interpreted-text role="guilabel"}: Tick this
    checkbox, and enter a desired percentage in the adjacent field, to
    request an online payment from the customer (for that designated
    percentage of the total amount) to confirm the order. This field
    only appears if the *Online Payment* setting has been enabled.
-   `Customer Reference`{.interpreted-text role="guilabel"}: Enter a
    custom reference ID for this customer. The entered reference ID can
    contain letters, numbers, or a mix of both.
-   `Tags`{.interpreted-text role="guilabel"}: Add specific tags to the
    quotation for added organization and enhanced searchability in the
    Odoo **Sales** application. Multiple tags can be added, if
    necessary.

#### Delivery section

In the `Delivery`{.interpreted-text role="guilabel"} section of the
`Other Info`{.interpreted-text role="guilabel"} tab, there are
delivery-specific fields that can be configured.

{.align-center}

-   `Shipping Weight`{.interpreted-text role="guilabel"}: Displays the
    weight of the items being shipped. This field is not modifiable.
    Product weight is configured on individual product forms.
-   `Incoterm`{.interpreted-text role="guilabel"}: Select an Incoterm
    (International Commerical Term) to use as predefined commerical
    terms for international transactions.
-   `Incoterm Location`{.interpreted-text role="guilabel"}: If an
    Incoterm is being used, enter the international location in this
    field.
-   `Shipping Policy`{.interpreted-text role="guilabel"}: Select a
    desired shipping policy from the drop-down menu. If all products are
    delivered at once, the delivery order is scheduled, based on the
    greatest product lead time. Otherwise, it is based on the shortest
    lead time. The available options are:
    `As soon as possible`{.interpreted-text role="guilabel"} or
    `When all products are ready`{.interpreted-text role="guilabel"}.
-   `Delivery Date`{.interpreted-text role="guilabel"}: Click into the
    empty field to reveal a calendar popover, from which a customer
    delivery date can be selected. If no custom date is required, refer
    to the `Expected`{.interpreted-text role="guilabel"} date listed to
    the right of that field.

#### Invoicing section

In the `Invoicing`{.interpreted-text role="guilabel"} section of the
`Other Info`{.interpreted-text role="guilabel"} tab, there are invoicing
specific fields that can be configured.

{.align-center}

-   `Fiscal Position`{.interpreted-text role="guilabel"}: Select a
    fiscal position to be used to adapt taxes and accounts for
    particular customers or sales orders/invoices. The default value
    comes from the customer. If a selection is made in this field, an
    `fa-refresh`{.interpreted-text role="icon"}
    `Update Taxes`{.interpreted-text role="guilabel"} clickable link and
    icon appear. When clicked, the taxes for this partiuclar customer
    and quotation are updated. A confirmation window appears, as well.
-   `Analytic Account`{.interpreted-text role="guilabel"}: Select an
    analytic account to apply to this customer/quotation.

#### Tracking section

In the `Tracking`{.interpreted-text role="guilabel"} section of the
`Other Info`{.interpreted-text role="guilabel"} tab, there are tracking
specific fields that can be configured.

{.align-center}

-   `Source Document`{.interpreted-text role="guilabel"}: Enter the
    reference of the document that generated the quotation/sales order,
    if applicable.
-   `Opportunity`{.interpreted-text role="guilabel"}: Select the
    specific opportunity (from the **CRM** app) related to this
    quotation, if applicable.
-   `Campaign`{.interpreted-text role="guilabel"}: Select the marketing
    campaign related to this quotation, if applicable.
-   `Medium`{.interpreted-text role="guilabel"}: Select the method by
    which this quotation originated (e.g. *Email*), if applicable.
-   `Source`{.interpreted-text role="guilabel"}: Select the source of
    the link used to generate this quotation (e.g. *Facebook*), if
    applicable.

::: {.seealso}
`../../../websites/website/reporting/link_tracker`{.interpreted-text
role="doc"}
:::

### Notes tab

In the `Notes`{.interpreted-text role="guilabel"} tab of the quotation
form, enter any specific internal notes about the quotation and/or
customer, if desired.

Sending and confirming quotations
---------------------------------

Once all the necessary fields and tabs have been configured, it is time
to send the quotation to the customer for confirmation. Upon
confirmation, the quotation turns into an official sales order.

At the top of the form, there is a series of buttons:

-   `Send by Email`{.interpreted-text role="guilabel"}: When clicked, a
    pop-up window appears with the customer\'s name and email address in
    the `Recipients`{.interpreted-text role="guilabel"} field, the
    quotation (and reference ID) in the `Subject`{.interpreted-text
    role="guilabel"} field, and a brief default message in the body of
    the email, which can be modified, if needed.

    Below that, a PDF copy of the quotation is attached. When ready,
    click `Send`{.interpreted-text role="guilabel"} to send the
    quotation, via email, to the customer, so they can review and
    confirm it.

-   `Send PRO-FORMA Invoice`{.interpreted-text role="guilabel"}: This
    button **only** appears if the *Pro-Forma Invoice* setting has been
    enabled. When clicked, a pop-up window appears with the customer\'s
    name and email address in the `Recipients`{.interpreted-text
    role="guilabel"} field, the *Proforma* invoice (and reference ID) in
    the `Subject`{.interpreted-text role="guilabel"} field, and a brief
    default message in the body of the email, which can be modified, if
    needed.

    Below that, a PDF copy of the quotation is attached. When ready,
    click `Send`{.interpreted-text role="guilabel"} to send the
    quotation, via email, to the customer, so they can review and
    confirm it.

-   `Confirm`{.interpreted-text role="guilabel"}: When clicked, the
    quotation is confirmed, and the status changes to
    `Sales Order`{.interpreted-text role="guilabel"}.

-   `Preview`{.interpreted-text role="guilabel"}: When clicked, Odoo
    reveals a preview of the quotation the customer sees when they log
    into their customer portal. Click the
    `fa-arrow-right`{.interpreted-text role="icon"} `Back to edit
    mode`{.interpreted-text role="guilabel"} link at the top of the
    preview page, in the blue banner, to return to the quotation form.

-   `Cancel`{.interpreted-text role="guilabel"}: When clicked, the
    quotation is canceled.

::: {.note}
::: {.title}
Note
:::

If the *Lock Confirmed Sales* setting is enabled, the sales order
becomes `Locked`{.interpreted-text role="guilabel"}, and is indicated as
such on the sales order form.
:::

At this point, the quotation has been confirmed, turned into a sales
order, and is now ready to be invoiced and paid for.

For more information about invoicing, refer to the
`Invoice based on delivered or ordered
quantities <../invoicing/invoicing_policy>`{.interpreted-text
role="doc"}

::: {.seealso}
\- `quote_template`{.interpreted-text role="doc"} -
`deadline`{.interpreted-text role="doc"} -
`get_signature_to_validate`{.interpreted-text role="doc"} -
`get_paid_to_validate`{.interpreted-text role="doc"} -
`pdf_quote_builder`{.interpreted-text role="doc"} -
`../invoicing/proforma`{.interpreted-text role="doc"}
:::
