# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/manage_deals/blanket_orders.md

Blanket orders
==============

::: {#purchase/manage_deals/blanket-orders}
Blanket orders are long-term purchase agreements between a company and a
vendor to deliver products on a recurring basis with predetermined
pricing.
:::

Blanket orders are helpful when products are consistently purchased from
the same vendor, but in different quantities, and at different times.

By simplifying the ordering process, blanket orders not only save time,
they also save money, since they can be advantageous when negotiating
bulk pricing with vendors.

Create a new blanket order
--------------------------

To create blanket orders, enable the *Purchase Agreements* feature from
the *Purchase* app settings. Navigate to
`Purchase app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and under the `Orders`{.interpreted-text
role="guilabel"} section, click the checkbox for
`Purchase Agreements`{.interpreted-text role="guilabel"}. Then click
`Save`{.interpreted-text role="guilabel"} to implement the changes.

::: {.note}
::: {.title}
Note
:::

In addition to creating blanket orders, the *Purchase Agreements*
setting also allows users to create alternative requests for quotation
(RfQs).
:::

{.align-center}

To create a blanket order, go to
`Purchase app --> Orders --> Blanket Orders`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"}. This opens a new blanket order form.

Configure the following fields in the new blanket order form to
establish predetermined rules for the recurring long-term agreement:

-   `Purchase Representative`{.interpreted-text role="guilabel"}: the
    user assigned to this specific blanket order. By default, this is
    the user who created the agreement; the user can be changed directly
    from the drop-down menu next to this field.
-   `Agreement Type`{.interpreted-text role="guilabel"}: the type of
    purchase agreement this blanket order is classified as. In Odoo,
    blanket orders are the only official purchase agreement.
-   `Vendor`{.interpreted-text role="guilabel"}: the supplier to whom
    this agreement is tied, either once or on a recurring basis. The
    vendor can be selected directly from the drop-down menu next to this
    field.
-   `Currency`{.interpreted-text role="guilabel"}: the agreed-upon
    currency to be used for this exchange. If multiple currencies have
    been activated in the database, the currency can be changed from the
    drop-down menu next to this field.
-   `Agreement Deadline`{.interpreted-text role="guilabel"}: the date
    that this purchase agreement will be set to expire on. If this
    blanket order should not expire, leave this field blank.
-   `Ordering Date`{.interpreted-text role="guilabel"}: the date that
    this blanket order should be placed on if a new quotation is created
    directly from the blanket order form. If a new quotation is created,
    this value automatically populates the *Order Deadline* field on the
    `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}.
-   `Delivery Date`{.interpreted-text role="guilabel"}: the expected
    delivery date that the products included in an
    `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} are
    expected, if created directly from a blanket order form. If a new
    quotation is created, this value automatically populates the
    *Expected Arrival* field on the
    `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}.
-   `Source Document`{.interpreted-text role="guilabel"}: the source
    purchase order (PO) that this blanket order is tied to. If this
    blanket order should not be tied to any existing
    `PO (Purchase Order)`{.interpreted-text role="abbr"}, leave this
    field blank.
-   `Company`{.interpreted-text role="guilabel"}: the company assigned
    to this specific blanket order. By default, this is the company that
    the user creating the blanket order is listed under. If the database
    is not a multi-company database, this field **cannot** be changed,
    and defaults to the only company listed in the database.

{.align-center}

Once all relevant fields have been filled out, click
`Add a line`{.interpreted-text role="guilabel"} to add products under
the `Product`{.interpreted-text role="guilabel"} column. Then, in the
`Quantity`{.interpreted-text role="guilabel"} column, change the
quantity of each product, and set a price in the
`Unit Price`{.interpreted-text role="guilabel"} column.

::: {.important}
::: {.title}
Important
:::

When adding products to a new blanket order, the pre-existing prices of
products are not automatically added to the product lines. Instead, the
prices **must** be manually assigned, by changing the value in the
`Unit Price`{.interpreted-text role="guilabel"} column to an agreed-upon
price with the listed vendor. Otherwise, the price will remain
[0]{.title-ref}.
:::

To view and change the default purchase agreement settings for blanket
orders directly from the blanket order form, click the
`➡️ (right arrow)`{.interpreted-text role="guilabel"} icon that becomes
visible when hovering over the `Agreement Type`{.interpreted-text
role="guilabel"} field, where `Blanket Order`{.interpreted-text
role="guilabel"} is listed. This navigates to the blanket order
settings.

{.align-center}

From here, the settings for blanket orders can be edited. Under the
`Agreement Type`{.interpreted-text role="guilabel"} section, the name of
the `Agreement Type`{.interpreted-text role="guilabel"} can be changed,
and the `Agreement
Selection Type`{.interpreted-text role="guilabel"} can be changed, as
well. There are two options that can be activated for the type of
selection:

-   `Select only one RfQ (exclusive)`{.interpreted-text
    role="guilabel"}: when a purchase order is confirmed, the remaining
    purchase orders are canceled.
-   `Select multiple RfQ (non-exclusive)`{.interpreted-text
    role="guilabel"}: when a purchase order is confirmed, remaining
    purchase orders are **not** canceled. Instead, multiple purchase
    orders are allowed.

Under the `Data For New Quotations`{.interpreted-text role="guilabel"}
section, the `Lines`{.interpreted-text role="guilabel"} and
`Quantities`{.interpreted-text role="guilabel"} fields can be edited.
Doing so sets how new quotations should be populated when using this
purchase agreement.

{.align-center}

There are two options that can be activated for
`Lines`{.interpreted-text role="guilabel"}:

-   `Use lines of agreement`{.interpreted-text role="guilabel"}: when
    creating a new quotation, the product lines pre-populate with the
    same products listed on the blanket order, if said blanket order is
    chosen for the new quotation.
-   `Do not create RfQ lines automatically`{.interpreted-text
    role="guilabel"}: when creating a new quotation, **and** selecting
    an existing blanket order, the settings carry over to the new
    quotation, but the product lines do **not** populate.

And, there are two options that can be activated for
`Quantities`{.interpreted-text role="guilabel"}:

-   `Use quantities of agreement`{.interpreted-text role="guilabel"}:
    when creating a new quotation, the product quantities listed on the
    blanket order pre-populate on the product lines, if said blanket
    order is chosen for the new quotation.
-   `Set quantities manually`{.interpreted-text role="guilabel"}: when
    creating a new quotation, **and** selecting an existing blanket
    order, the product lines pre-populate, but all quantities are set to
    [0]{.title-ref}. The quantities **must** be manually set by the
    user.

Once any desired changes have been made, click `New`{.interpreted-text
role="guilabel"} (via the breadcrumbs, at the top of the page) to
navigate back to the blanket order form. Then, click
`Confirm`{.interpreted-text role="guilabel"} to save this new purchase
agreement.

Once confirmed, the blanket order\'s stage (in the upper-right corner)
changes from `Draft`{.interpreted-text role="guilabel"} to
`Ongoing`{.interpreted-text role="guilabel"}, meaning this agreement can
be selected and used when creating new
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.

::: {.tip}
::: {.title}
Tip
:::

After creating and confirming a blanket order, products, quantities, and
prices can still be edited, added, and removed from the purchase
agreement.
:::

Create a new `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} from the blanket order
------------------------------------------------------------------------------------------------

After confirming a blanket order, new quotations can be created directly
from the blanket order form.
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} using
this form are pre-populated with information based on the rules set in
the form. Additionally, new quotations are automatically linked to this
blanket order form, via the `RFQs/Orders`{.interpreted-text
role="guilabel"} smart button at the top-right of the form.

To create a new quotation from the blanket order form, click the
`New Quotation`{.interpreted-text role="guilabel"} button. This opens a
new `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, that
is pre-populated with the correct information, depending on the settings
configured on the blanket order form.

From the new `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} form, click `Send by Email`{.interpreted-text
role="guilabel"} to compose and send an email to the listed vendor.
Click `Print RFQ`{.interpreted-text role="guilabel"} to generate a
printable PDF of the quotation; or, once ready, click
`Confirm Order`{.interpreted-text role="guilabel"} to confirm the
`PO (Purchase Order)`{.interpreted-text role="abbr"}.

{.align-center}

Once the `PO (Purchase Order)`{.interpreted-text role="abbr"} has been
confirmed, click back to the blanket order form (via the breadcrumbs, at
the top of the page). From the blanket order form, there is now one
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} listed in
the `RFQs/Orders`{.interpreted-text role="guilabel"} smart button at the
top-right of the form. Click the `RFQs/Orders`{.interpreted-text
role="guilabel"} smart button to see the
`PO (Purchase Order)`{.interpreted-text role="abbr"} that was just
created.

{.align-center}

Replenishment
-------------

Once a blanket order is confirmed, a new vendor line is added under the
`Purchase`{.interpreted-text role="guilabel"} tab of the products
included in the order.

This makes blanket orders useful with `automated replenishment
<../../purchase/products/reordering>`{.interpreted-text role="doc"},
because information about the `Vendor`{.interpreted-text
role="guilabel"}, `Price`{.interpreted-text role="guilabel"}, and the
`Agreement`{.interpreted-text role="guilabel"} are referenced on the
vendor line. This information dictates when, where, and at what price
the product should be replenished.

{.align-center}

::: {.seealso}
`calls_for_tenders`{.interpreted-text role="doc"}
:::
