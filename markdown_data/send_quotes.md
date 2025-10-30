Create and send quotations
==========================

Once a qualified lead has been converted into an opportunity, the next
step is to create and deliver a quotation. This process can be easily
handled through Odoo\'s *CRM* application.

Create a new quotation
----------------------

To create a new quotation, open the `CRM app`{.interpreted-text
role="menuselection"}, revealing the `Pipeline`{.interpreted-text
role="guilabel"} page on the main *CRM* dashboard.

From here, click on any opportunity to open it. Review the existing
information and update any fields, if necessary.

::: {.note}
::: {.title}
Note
:::

If a quotation has already been created for this opportunity, it can be
found by clicking on the `Quotations`{.interpreted-text role="guilabel"}
smart button at the top of the top of the form. The number of existing
quotations is listed on the smart button, as well.
:::

At the top-left of the form, click the `New Quotation`{.interpreted-text
role="guilabel"} button.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The **Sales** application **must** be installed for the
`New Quotation`{.interpreted-text role="guilabel"} button to appear.
:::

::: {.important}
::: {.title}
Important
:::

The `Customer`{.interpreted-text role="guilabel"} field is **not**
required on the opportunity form.

However, customer information must be added or linked before a quotation
can be sent. If the `Customer`{.interpreted-text role="guilabel"} field
is left blank on the opportunity, clicking the `New
Quotation`{.interpreted-text role="guilabel"} button opens a pop-up
window with the following options:

-   `Create a new customer`{.interpreted-text role="guilabel"}: creates
    a new customer record, using any available information provided on
    the opportunity form.
-   `Link to an existing customer`{.interpreted-text role="guilabel"}:
    opens a drop-down field with existing customer names. Select a name
    to link this new quotation to an existing customer record.
-   `Do not link to a customer`{.interpreted-text role="guilabel"}: the
    quotation will **not** be linked to a customer, and no changes are
    made to the customer information.
:::

Once this button is clicked, a new quotation form appears. Confirm the
information in the top half of the form, and update any missing or
incorrect fields:

-   `Customer`{.interpreted-text role="guilabel"}: the company or
    contact for whom this quotation was created.
-   `Referrer`{.interpreted-text role="guilabel"}: if this customer was
    referred by another customer or contact, select it from the
    drop-down menu in this field.
-   `Invoice Address`{.interpreted-text role="guilabel"}: physical
    address where the invoice should be sent.
-   `Delivery Address`{.interpreted-text role="guilabel"}: physical
    address where any products should be delivered.
-   `Quotation Template`{.interpreted-text role="guilabel"}: if
    applicable, select a pre-configured `quotation template
    </applications/sales/sales/send_quotations/quote_template>`{.interpreted-text
    role="doc"} from this field.
-   `Expiration`{.interpreted-text role="guilabel"}: date when this
    quotation is no longer valid.
-   `Quotation Date`{.interpreted-text role="guilabel"}: creation date
    of draft/sent orders, confirmation date of confirmed orders. Note
    that this field is only visible if `Developer mode (debug mode)
    </applications/general/developer_mode>`{.interpreted-text
    role="doc"} is active.
-   `Recurring Plan`{.interpreted-text role="guilabel"}: if this
    quotation is for a recurring product or subscription, select the
    recurring plan configuration to be used.
-   `Pricelist`{.interpreted-text role="guilabel"}: select a pricelist
    to be applied to this order.
-   `Payment Terms`{.interpreted-text role="guilabel"}: select any
    applicable payment terms for this quotation.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

The `Expiration`{.interpreted-text role="guilabel"} field automatically
populates based on the creation date of the quotation, and the default
validity time frame.

To update the default validity time frame, navigate to `Sales app -->
Configuration --> Settings --> Quotations & Orders`{.interpreted-text
role="menuselection"} and update the `Default Quotation
Validity`{.interpreted-text role="guilabel"} field. To disable automatic
expiration, enter [0]{.title-ref} in this field.

When the desired changes are complete, click `Save`{.interpreted-text
role="guilabel"}.

When using a quotation template, the expiration date is based off of the
`Quotation
Validity`{.interpreted-text role="guilabel"} field on the template. To
alter the validity date computation on a template, go to
`Sales app --> Configuration --> Sales Orders --> Quotation Templates`{.interpreted-text
role="menuselection"}.

Then, click on a template to open it, and update the number in the
`Quotation Validity`{.interpreted-text role="guilabel"} field.
:::

### Order lines

After updating the customer, payment, and deadline information on the
new quotation, the `Order Lines`{.interpreted-text role="guilabel"} tab
can be updated with the appropriate product information.

To do that, click `Add a product`{.interpreted-text role="guilabel"} in
the `Order Lines`{.interpreted-text role="guilabel"} tab.

Next, type the name of an item into the `Product`{.interpreted-text
role="guilabel"} field to search through the product catalog. Then,
select a product from the drop-down menu, or create a new one by
selecting `Create`{.interpreted-text role="guilabel"} or
`Create and Edit`{.interpreted-text role="guilabel"}.

After selecting a product, update the `Quantity`{.interpreted-text
role="guilabel"}, if necessary. Confirm the information in the remaining
fields.

To remove a line from the quotation, click the
`fa-trash-o`{.interpreted-text role="icon"}
`(trash can)`{.interpreted-text role="guilabel"} icon.

To organize products into sections click
`Add a section`{.interpreted-text role="guilabel"} and type a name for
the section. Then, click the `oi-draggable`{.interpreted-text
role="icon"} `(drag)`{.interpreted-text role="guilabel"} icon to the
left of the name and drag to move the section to the appropriate
location. Move each product using the same method to finish organizing
the quotation order lines.

{.align-center}

#### Product catalog

To quickly add numerous products to the quotation, click the
`Catalog`{.interpreted-text role="guilabel"} button to open the product
catalog.

All products in the database are listed as cards and can be sorted in
the left panel by `Product Category`{.interpreted-text role="guilabel"}
and `Attributes`{.interpreted-text role="guilabel"}.

{.align-center}

To add a product, click the `fa-shopping-cart`{.interpreted-text
role="icon"} `Add`{.interpreted-text role="guilabel"} button on the
product card. Set the quantity of the item using the
`fa-plus`{.interpreted-text role="icon"} `(add)`{.interpreted-text
role="guilabel"} or `fa-minus`{.interpreted-text role="icon"}
`(subtract)`{.interpreted-text role="guilabel"} buttons, or type the
quantity in the number field between the two buttons. To remove an item,
click the `fa-trash`{.interpreted-text role="icon"}
`Remove`{.interpreted-text role="guilabel"} button on the product card.

{.align-center}

Once all product quantities are set, click the
`Back to Quotation`{.interpreted-text role="guilabel"} button to return
to the quotation. The items selected in the product catalog now appear
in the `Order Lines`{.interpreted-text role="guilabel"} tab.

Preview and send quotation
--------------------------

To see a preview of the quotation as the customer will see it, click the
`Preview`{.interpreted-text role="guilabel"} button. Doing so opens a
preview in the `Customer Portal`{.interpreted-text role="guilabel"}.

After reviewing the customer preview, click
`Return to edit mode`{.interpreted-text role="guilabel"} to return to
the quotation form in the backend.

When the quotation is ready to deliver to the customer, click the
`Send by Email`{.interpreted-text role="guilabel"} button.

Doing so opens a pop-up window with a pre-configured email message.
Information from the quotation, including the contact information, total
cost, and quotation title are be imported from the quotation.

A PDF of the quotation is added as an attachment to the email.

::: {.note}
::: {.title}
Note
:::

A pre-loaded template is used to create the email message. To alter the
template, click the internal link to the right of the
`Load template`{.interpreted-text role="guilabel"} field, located at the
bottom of the email pop-up window.

To select a new template, select an option from the
`Load template`{.interpreted-text role="guilabel"} drop-down menu.
:::

Proceed to make any necessary changes to the email, then click
`Send`{.interpreted-text role="guilabel"}. A copy of the message is
added to the *Chatter* of the of the record.

After a quotation is sent, the originating opportunity\'s
`Quotations`{.interpreted-text role="guilabel"} smart button updates
with a new count. This quotation, and all other quotations can be
accessed through this smart button at the top of the opportunity in the
*CRM* app.

Any quotations attached to the opportunity that are confirmed, and have
therefore been converted to sales orders, will be deducted from the
number listed on the `Quotations`{.interpreted-text role="guilabel"}
smart button. Instead, the value of the sales order will appear in the
`Orders`{.interpreted-text role="guilabel"} smart button located in the
same control panel.

Mark an opportunity won or lost
-------------------------------

In order to keep the pipeline up to date and accurate, opportunities
need to be identified as *won* or *lost* once a customer has responded
to a quotation.

To mark an opportunity as *won* or *lost*, return to the opportunity
using the breadcrumbs at the top-left of the quotation form. Or navigate
to `CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"} and click on the correct opportunity to open it.

At the top-left of the form, click on either the `Won`{.interpreted-text
role="guilabel"} or `Lost`{.interpreted-text role="guilabel"} button.

If the opportunity is marked *won*, a green `Won`{.interpreted-text
role="guilabel"} banner is added to the record, and it is moved to the
`Won`{.interpreted-text role="guilabel"} stage.

Marking an opportunity as *lost*, via the `Lost`{.interpreted-text
role="guilabel"} button opens a `Mark Lost`{.interpreted-text
role="guilabel"} pop-up window, where a `Lost Reason`{.interpreted-text
role="guilabel"} can be entered.

From the `Lost Reason`{.interpreted-text role="guilabel"} drop-down
field, choose an existing lost reason. If no applicable reason is
available, create a new one by entering it into the
`Lost Reason`{.interpreted-text role="guilabel"} field, and clicking
`Create`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

It\'s best practice to try and use pre-configured
`Lost Reason`{.interpreted-text role="guilabel"} values as much as
possible or to limit the creation of new values only to sales team
leads. Using consistent values for this parameter will make pipeline
analysis easier and more accurate when filtering for the
`Lost Reason`{.interpreted-text role="guilabel"} parameter.

To set up new values for this field, navigate to
`CRM --> Configuration --> Lost
Reasons`{.interpreted-text role="menuselection"}, and click both
`New`{.interpreted-text role="guilabel"} and `Save`{.interpreted-text
role="guilabel"} for each new entry added to the list.
:::

Additional notes and comments can be added in the
`Closing Note`{.interpreted-text role="guilabel"} field.

When all the desired information has been entered in the
`Mark Lost`{.interpreted-text role="guilabel"} pop-up window, click
`Mark as Lost`{.interpreted-text role="guilabel"}.

Upon clicking `Mark as Lost`{.interpreted-text role="guilabel"}, the
pop-up window disappears, and Odoo returns to the opportunity form,
where a new red `Lost`{.interpreted-text role="guilabel"} banner is now
present in the upper-right corner of the opportunity.

Once an opportunity is marked as *lost*, it is no longer considered
active, and it is removed from the pipeline.

In order to view a *lost* opportunity from the pipeline, click the
`down arrow icon`{.interpreted-text role="guilabel"} to the right of the
search bar, and select either `Lost`{.interpreted-text role="guilabel"}
or `Archived`{.interpreted-text role="guilabel"} from the drop-down menu
that appears.

::: {.important}
::: {.title}
Important
:::

While opportunities that have been marked as *lost* are considered
*Archived*, be advised that, in order for an opportunity to be included
as *lost* in reporting, it **must** be specifically marked as *lost*,
not *Archived*.
:::
