Quotation templates
===================

In Odoo *Sales*, salespeople have the ability to create reusable
quotation templates for common products or services that the business
offers.

By using these templates, quotations can be tailored and sent to
customers at a much faster pace, without having to create new quotations
from scratch every time a sales negotiation occurs.

Configuration {#sales/send_quotations/templates}
-------------

Begin by activating the setting in
`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and scroll to the
`Quotations \& Orders`{.interpreted-text role="guilabel"} heading.

In that section, check the box beside the
`Quotation Templates`{.interpreted-text role="guilabel"} option. Doing
so reveals a new `Default Template`{.interpreted-text role="guilabel"}
field, in which a default quotation template can be chosen from a
drop-down menu.

{.align-center}

Also, upon activating the `Quotation Template`{.interpreted-text
role="guilabel"} feature, an internal `➡️
Quotation Templates`{.interpreted-text role="guilabel"} link appears
beneath the `Default Template`{.interpreted-text role="guilabel"} field.

Clicking that link reveals the `Quotation Templates`{.interpreted-text
role="guilabel"} page, from which templates can be created, viewed, and
edited.

Before leaving the `Settings`{.interpreted-text role="guilabel"} page,
don\'t forget to click the `Save`{.interpreted-text role="guilabel"}
button to save all changes made during the session.

Create quotation templates
--------------------------

Click the `Quotation Templates`{.interpreted-text role="guilabel"} link
on the `Settings`{.interpreted-text role="guilabel"} page, or navigate
to
`Sales app --> Configuration --> Quotation Templates`{.interpreted-text
role="menuselection"}. Both options reveal the
`Quotation Templates`{.interpreted-text role="guilabel"} page, where
quotation templates can be created, viewed, and edited.

{.align-center}

To create a new quotation template, click the `New`{.interpreted-text
role="guilabel"} button, located in the upper-left corner. Doing so
reveals a blank quotation template form that can be customized in a
number of ways.

{.align-center}

Start by entering a name for the template in the
`Quotation Template`{.interpreted-text role="guilabel"} field.

Then, in the `Quotation Validity`{.interpreted-text role="guilabel"}
field, designate how many days the quotation template will remain valid
for, or leave the field on the default [0]{.title-ref} to keep the
template valid indefinitely.

Next, in the `Confirmation Mail`{.interpreted-text role="guilabel"}
field, click the blank field to reveal a drop-down menu. From the
drop-down menu, select a pre-configured email template to be sent to
customers upon confirmation of an order.

::: {.tip}
::: {.title}
Tip
:::

To create a new email template directly from the
`Confirmation Mail`{.interpreted-text role="guilabel"} field, start
typing the name of the new email template in the field, and select
either: `Create`{.interpreted-text role="guilabel"} or
`Create and edit...`{.interpreted-text role="guilabel"} from the
drop-down menu that appears.

Selecting `Create`{.interpreted-text role="guilabel"} creates the email
template, which can be edited later.

Selecting `Create and edit...`{.interpreted-text role="guilabel"}
creates the email template, and a `Create
Confirmation Mail`{.interpreted-text role="guilabel"} pop-up window
appears, in which the email template can be customized and configured
right away.

{.align-center}

When all modifications are complete, click
`Save \& Close`{.interpreted-text role="guilabel"} to save the email
template and return to the quotation form.
:::

If working in a multi-company environment, use the
`Company`{.interpreted-text role="guilabel"} field to designate to which
company this quotation template applies.

If a journal is set in the `Invoicing Journal`{.interpreted-text
role="guilabel"} field, all sales orders with this template will invoice
in that specified journal. If no journal is set in this field, the sales
journal with the lowest sequence is used.

If the `Online Signature`{.interpreted-text role="guilabel"} and/or
`Online Payment`{.interpreted-text role="guilabel"} features are
activated in the `Settings`{.interpreted-text role="guilabel"}
(`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}), those options are available on quotation
template forms.

Check the box beside `Online Signature`{.interpreted-text
role="guilabel"} to request an online signature from the customer to
confirm an order.

Check the box beside `Online Payment`{.interpreted-text role="guilabel"}
to request an online payment from the customer to confirm an order. When
`Online Payment`{.interpreted-text role="guilabel"} is checked, a new
percentage field appears, in which a specific percentage of payment can
be entered.

Both options, `Online Signature`{.interpreted-text role="guilabel"} and
`Online Payment`{.interpreted-text role="guilabel"} can be enabled
simultaneously, in which case the customer must provide **both** a
signature **and** a payment to confirm an order.

### Lines tab

In the `Lines`{.interpreted-text role="guilabel"} tab, products can be
added to the quotation template by clicking
`Add a product`{.interpreted-text role="guilabel"}, organized by
clicking `Add a section`{.interpreted-text role="guilabel"} (and
dragging/dropping section headers), and further explained with
discretionary information (such as warranty details, terms, etc.) by
clicking `Add a note`{.interpreted-text role="guilabel"}.

To add a product to a quotation template, click
`Add a product`{.interpreted-text role="guilabel"} in the
`Lines`{.interpreted-text role="guilabel"} tab of a quotation template
form. Doing so reveals a blank field in the `Product`{.interpreted-text
role="guilabel"} column.

When clicked, a drop-down menu with existing products in the database
appear. Select the desired product from the drop-down menu to add it to
the quotation template.

If the desired product isn\'t readily visible, type the name of the
desired product in the `Product`{.interpreted-text role="guilabel"}
field, and the option appears in the drop-down menu. Products can also
be found by clicking `Search More...`{.interpreted-text role="guilabel"}
from the drop-down menu.

::: {.tip}
::: {.title}
Tip
:::

In Odoo 17, it is now possible to add event-related products (booths and
registrations) to quotation templates. To do so, click the
`Product`{.interpreted-text role="guilabel"} field, type in
[Event]{.title-ref}, and select the desired event-related product from
the resulting drop-down menu.
:::

::: {.note}
::: {.title}
Note
:::

When a product is added to a quotation template, the default
`Quantity`{.interpreted-text role="guilabel"} is [1]{.title-ref}, but
that can be edited at any time.
:::

Then, drag-and-drop the product to the desired position, via the
`six squares`{.interpreted-text role="guilabel"} icon, located to the
left of each line item.

To add a *section*, which serves as a header to organize the lines of a
sales order, click `Add a section`{.interpreted-text role="guilabel"} in
the `Lines`{.interpreted-text role="guilabel"} tab. When clicked, a
blank field appears, in which the desired name of the section can be
typed. When the name has been entered, click away to secure the section
name.

Then, drag-and-drop the section name to the desired position, via the
`six squares`{.interpreted-text role="guilabel"} icon, located to the
left of each line item.

To add a note, which would appear as a piece of text for the customer on
the quotation, click `Add a note`{.interpreted-text role="guilabel"} in
the `Lines`{.interpreted-text role="guilabel"} tab. When clicked, a
blank field appears, in which the desired note can be typed. When the
note has been entered, click away to secure the note.

Then, drag-and-drop the note to the desired position, via the
`six squares`{.interpreted-text role="guilabel"} icon.

To delete any line item from the `Lines`{.interpreted-text
role="guilabel"} tab (product, section, and/or note), click the
`🗑️ (trash can)`{.interpreted-text role="guilabel"} icon on the
far-right side of the line.

### Optional Products tab

The use of *optional products* is a marketing strategy that involves the
cross-selling of products along with a core product. The aim is to offer
useful and related products to customers, which may result in an
increased sale.

For instance, if a customer wants to buy a car, they have the choice to
order massaging seats, as well, or ignore the offer and simply buy the
car. Presenting the choice to purchase optional products enhances the
customer experience.

Optional products appear as a section on the bottom of sales orders and
eCommerce pages. Customers can immediately add them to their online
sales orders themselves, if desired.

{.align-center}

In the `Optional Products`{.interpreted-text role="guilabel"} tab,
`Add a line`{.interpreted-text role="guilabel"} for each cross-selling
product related to the original items in the `Lines`{.interpreted-text
role="guilabel"} tab, if applicable. The products added here ideally
complement the original offering as added value for the prospective
buyer.

Clicking `Add a line`{.interpreted-text role="guilabel"} reveals a blank
field in the `Product`{.interpreted-text role="guilabel"} column.

When clicked, a drop-down menu with products from the database appear.
Select the desired product from the drop-down menu to add it as an
optional product to the quotation template.

To delete any line item from the `Optional Products`{.interpreted-text
role="guilabel"} tab, click the `🗑️ (trash
can)`{.interpreted-text role="guilabel"} icon.

::: {.note}
::: {.title}
Note
:::

Optional products are **not** required to create a quotation template.
:::

### Terms & Conditions tab

The `Terms \& Conditions`{.interpreted-text role="guilabel"} tab
provides the opportunity to add terms and conditions to the quotation
template. To add terms and conditions, simply type (or copy/paste) the
desired terms and conditions in this tab.

::: {.seealso}
`../../../finance/accounting/customer_invoices/terms_conditions`{.interpreted-text
role="doc"}
:::

::: {.note}
::: {.title}
Note
:::

Terms and conditions are **not** required to create a quotation
template.
:::

### PDF Quote Builder tab

The `PDF Quote Builder`{.interpreted-text role="guilabel"} tab provides
options to compose an attractive quotation, with more information and
visually-pleasing elements, to highlight products and/or services.

To upload customer `Header pages`{.interpreted-text role="guilabel"} and
`Footer pages`{.interpreted-text role="guilabel"}, click the `✏️
(pencil)`{.interpreted-text role="guilabel"} icon to the right of the
respective pages. Click the `🗑️ (trash)`{.interpreted-text
role="guilabel"} icon to delete an uploaded PDF.

::: {.seealso}
`/applications/sales/sales/send_quotations/pdf_quote_builder`{.interpreted-text
role="doc"}
:::

Use quotation templates
-----------------------

When creating a quotation (`Sales app --> New`{.interpreted-text
role="menuselection"}), choose a pre-configured template in the
`Quotation Template`{.interpreted-text role="guilabel"} field.

{.align-center}

To view what the customer will see, click the
`Preview`{.interpreted-text role="guilabel"} button at the top of the
page to see how the quotation template appears on the front-end of the
website through Odoo\'s customer portal.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Quotation template design uses the same methodology and functionality
with design building blocks as a typical web page design with Odoo
*Website*. Be sure to check out the
`../../../websites/website`{.interpreted-text role="doc"} documentation
to learn more.
:::

When all blocks and customizations are complete, click the
`Save`{.interpreted-text role="guilabel"} button to put those
configurations into place.

There is also a blue banner at the top of the quotation template design
with a link to quickly return `Back to edit mode`{.interpreted-text
role="guilabel"}. When clicked, Odoo returns to the quotation form in
the back-end of the *Sales* application.

Mass cancel quotations/sales orders
-----------------------------------

Cancel multiple quotations (or sales orders) by navigating to the
`Sales app -->
Orders --> Quotations`{.interpreted-text role="menuselection"}
dashboard, landing, by default, in the list view. Then, on the left side
of the table, tick the preferred checkboxes for removal.

::: {.tip}
::: {.title}
Tip
:::

Select all records in the table by selecting the checkbox column header
at the top-left of the table; the total number of selected items are
displayed at the top of the page.
:::

Then, with the desired quotations (or sales orders) selected from the
list view on the `Quotations`{.interpreted-text role="guilabel"} page,
click the `fa-cog`{.interpreted-text role="icon"}
`Actions`{.interpreted-text role="guilabel"} button to reveal a
drop-down menu.

From this drop-down menu, select `Cancel quotations`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

This action can be performed for quotations in *any* stage, even if it
is confirmed as a sales order.
:::

Upon selecting the `Cancel quotations`{.interpreted-text
role="guilabel"} option, a `Cancel quotations`{.interpreted-text
role="guilabel"} confirmation pop-up window appears. To complete the
cancellation, click the `Cancel
quotations`{.interpreted-text role="guilabel"} button.

::: {.note}
::: {.title}
Note
:::

An error pop-up message appears when attempting to cancel an order for
an ongoing subscription that has an invoice.
:::

::: {.seealso}
\- `get_signature_to_validate`{.interpreted-text role="doc"} -
`get_paid_to_validate`{.interpreted-text role="doc"}
:::
