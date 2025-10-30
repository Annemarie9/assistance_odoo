# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders.md

Call for tenders
================

::: {#purchase/manage_deals/alternative-rfqs}
Sometimes, companies might want to invite vendors to submit offers for
similar goods or services all at once. This helps companies select the
cheapest, fastest vendors for their specific business needs.
:::

In Odoo, this can be done by creating alternative requests for quotation
(RfQs) for different vendors. Once a response is received from each
vendor, the product lines from each
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} can be
compared, and a decision can be made for which products to purchase from
which vendors.

::: {.note}
::: {.title}
Note
:::

Sometimes referred to as a *call for tender*, this process is primarily
used by organizations in the public sector, who are legally bound to use
it when making a purchase. However, private companies can also use
alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"} to spend money efficiently.
:::

Configuration
-------------

To create alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"}, the *Purchase Agreements* feature **must** be enabled in
the *Purchase* app settings. To enable the feature, navigate to
`Purchase app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Under the `Orders`{.interpreted-text role="guilabel"} section, click the
checkbox for `Purchase Agreements`{.interpreted-text role="guilabel"}.

Then, click `Save`{.interpreted-text role="guilabel"} to apply the
change.

{.align-center}

Create an `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} {#purchase/manage_deals/create-rfq}
----------------------------------------------------------------------

To create a new `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"}, follow the instructions in the `rfq`{.interpreted-text
role="doc"} documentation.

::: {.seealso}
[Odoo Tutorial: Purchase Basics and Your First Request for
Quotation](https://www.youtube.com/watch?v=o_uI718P1Dc)
:::

Create alternative `RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} {#purchase/manage_deals/create-alternatives}
---------------------------------------------------------------------------------

Once a `PO (Purchase Order)`{.interpreted-text role="abbr"} is created
and sent to a vendor, alternative
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} can be
created for additional vendors to compare prices, delivery times, and
other factors, to help make a decision for the order.

To create alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"} from the original, click the
`Alternatives`{.interpreted-text role="guilabel"} tab. Then, click
`Create Alternative`{.interpreted-text role="guilabel"}. When clicked, a
`Create alternative`{.interpreted-text role="guilabel"} pop-up window
appears.

{.align-center}

From this window, select an alternative vendor from the drop-down menu
next to the `Vendor`{.interpreted-text role="guilabel"} field, to whom
the alternative quotation is assigned.

Next to this, there is a `Copy Products`{.interpreted-text
role="guilabel"} checkbox that is selected by default. When selected,
the product quantities of the original
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} are copied
over to the alternative. For this first alternative quotation, leave the
checkbox checked. Once finished, click `Create
Alternative`{.interpreted-text role="guilabel"}. This opens a new
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} form.

Since the `Create Alternative`{.interpreted-text role="guilabel"}
checkbox was left checked, the new form is already pre-populated with
the same products, quantities, and other details as the previous,
original `RfQ (Request for Quotation)`{.interpreted-text role="abbr"}.

::: {.note}
::: {.title}
Note
:::

When the `Copy Products`{.interpreted-text role="guilabel"} checkbox is
selected while creating an alternative quotation, additional products do
**not** need to be added, unless desired.

However, if a chosen vendor is listed in the `Vendor`{.interpreted-text
role="guilabel"} column under a specific product form included in the
order, the values set on the product form carry over to the
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, and
**must** be changed manually, if necessary.
:::

Once ready, create a second alternative quotation by clicking the
`Alternatives`{.interpreted-text role="guilabel"} tab, followed by
`Create Alternative`{.interpreted-text role="guilabel"}.

This opens the `Create alternative`{.interpreted-text role="guilabel"}
pop-up window. Once again, choose a different vendor from the drop-down
menu next to `Vendor`{.interpreted-text role="guilabel"}. For this
particular `RfQ (Request for Quotation)`{.interpreted-text role="abbr"},
however, *uncheck* the `Copy Products`{.interpreted-text
role="guilabel"} checkbox. Doing so removes all products on the new
alternative `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"}, leaving it blank. The specific products which should be
ordered from this particular vendor can be added in as needed.

Once ready, click `Create Alternative`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If an alternative quotation should be removed from the
`Alternatives`{.interpreted-text role="guilabel"} tab, they can be
individually removed by clicking on the `X (remove)`{.interpreted-text
role="guilabel"} icon at the end of their row.
:::

This creates a third, new
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}. But, since
the product quantities of the original
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} were
**not** copied over, the product lines are empty, and new products can
be added as needed by clicking `Add a product`{.interpreted-text
role="guilabel"}, and selecting the desired products from the drop-down
menu.

Once the desired number of specific products are added, click
`Send by Email`{.interpreted-text role="guilabel"}.

{.align-center}

This opens a `Compose Email`{.interpreted-text role="guilabel"} pop-up
window, wherein the message to the vendor can be customized, and
attachments can be added, if necessary. Once ready, click
`Send`{.interpreted-text role="guilabel"}.

From this newest form, click the `Alternatives`{.interpreted-text
role="guilabel"} tab. Under this tab, all three
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} can be
seen in the `Reference`{.interpreted-text role="guilabel"} column.
Additionally, the vendors are listed under the
`Vendor`{.interpreted-text role="guilabel"} column, and the order
`Total`{.interpreted-text role="guilabel"} (and
`Status`{.interpreted-text role="guilabel"}) of the orders are in the
rows, as well.

The date in the `Expected Arrival`{.interpreted-text role="guilabel"}
column is calculated for each vendor, based on any pre-configured lead
times in the vendor and product forms.

Link new `RfQ (Request for Quotation)`{.interpreted-text role="abbr"} to existing quotations {#purchase/manage_deals/link-rfq}
--------------------------------------------------------------------------------------------

Even if a quotation is not created directly from the
`Alternatives`{.interpreted-text role="guilabel"} tab of another
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, it can
still be linked to existing
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.

To do that, begin by creating a new
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}. Navigate
to `Purchase app --> New`{.interpreted-text role="menuselection"}. Fill
out the `RfQ (Request for Quotation)`{.interpreted-text role="abbr"},
according to the
`previous instructions <purchase/manage_deals/create-rfq>`{.interpreted-text
role="ref"}.

Then, once ready, click the `Alternatives`{.interpreted-text
role="guilabel"} tab. Since this new
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} was created
separately, there are no other orders linked yet.

However, to link this `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} with existing alternatives, click
`Link to Existing RfQ`{.interpreted-text role="guilabel"} on the first
line in the `Vendor`{.interpreted-text role="guilabel"} column.

{.align-center}

This opens an `Add: Alternative POs`{.interpreted-text role="guilabel"}
pop-up window. Select the desired previously-created
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}, and
click `Select`{.interpreted-text role="guilabel"}. All of these orders
are now copied to this `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"}, and can be found under the
`Alternatives`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

If a large number of `POs (Purchase Orders)`{.interpreted-text
role="abbr"} are being processed, and the previous
`POs (Purchase Orders)`{.interpreted-text role="abbr"} can\'t be
located, click the `fa-chevron-down`{.interpreted-text role="icon"}
`(chevron)`{.interpreted-text role="guilabel"} icon to the right of the
search bar, at the top of the pop-up window.

Then, under the `Group By`{.interpreted-text role="guilabel"} section,
click `Vendor`{.interpreted-text role="guilabel"}. Vendors are displayed
in their own nested drop-down lists, and each vendor\'s list can be
expanded to view open `POs (Purchase Orders)`{.interpreted-text
role="abbr"} for that vendor.
:::

Compare product lines {#purchase/manage_deals/compare-product-lines}
---------------------

Alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"} can be compared side-by-side, in order to determine which
vendors offer the best deals on the products included in the orders.

To compare alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"}, navigate to the `Purchase`{.interpreted-text
role="menuselection"} app, and select one of the previously-created
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.

Then, click the `Alternatives`{.interpreted-text role="guilabel"} tab to
see all linked `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"}. Next, under the `Create Alternative`{.interpreted-text
role="guilabel"} option, click `Compare Product Lines`{.interpreted-text
role="guilabel"}. This navigates to the
`Compare Order Lines`{.interpreted-text role="guilabel"} page.

{.align-center}

The `Compare Order Lines`{.interpreted-text role="guilabel"} page, by
default, groups by `Product`{.interpreted-text role="guilabel"}. Each
product included in any of the
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} is
displayed in its own nested drop-down list, and features all of the
`PO (Purchase Order)`{.interpreted-text role="abbr"} numbers in the
`Reference`{.interpreted-text role="guilabel"} column.

::: {.note}
::: {.title}
Note
:::

To remove product lines from the `Compare Order Lines`{.interpreted-text
role="guilabel"} page, click `Clear`{.interpreted-text role="guilabel"}
at the far-right end of that product line\'s row.

Doing so removes this specific product as a selectable option from the
page, and changes the `Total`{.interpreted-text role="guilabel"} price
of that product on the page to [0]{.title-ref}.

Additionally, on the `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} form, in which that product was included, its ordered
quantity is also changed to [0]{.title-ref}.
:::

Once the best offers have been identified, individual products can be
selected by clicking the `Choose`{.interpreted-text role="guilabel"}
button at the end of each corresponding row.

Once all desired products have been chosen, click
`Requests for Quotation`{.interpreted-text role="guilabel"} (in the
breadcrumbs, at the top of the page) to navigate back to an overview of
all `RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.

Cancel (or keep) alternatives {#purchase/manage_deals/cancel-keep-alternatives}
-----------------------------

Once the desired products have been chosen from the
`Compare Order Lines`{.interpreted-text role="guilabel"} page, the
remaining `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"}, from which no products were chosen, can be canceled.

The cost in the `Total`{.interpreted-text role="guilabel"} column for
each product that wasn\'t chosen is automatically set to
[0]{.title-ref}, indicated at the far-right of each corresponding row.

Although they haven\'t been canceled yet, this indicates that each of
those orders can be canceled without having an effect on the other live
orders, once those orders have been confirmed.

{.align-center}

To confirm an `RfQ (Request for Quotation)`{.interpreted-text
role="abbr"} for which products were selected, click into an
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"}, and click
`Confirm Order`{.interpreted-text role="guilabel"}.

This causes a
`What about the alternative Requests for Quotations?`{.interpreted-text
role="guilabel"} pop-up window to appear.

To view a detailed form of one of the
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"} listed,
click the line item for that quotation. This opens an
`Open: Alternative POs`{.interpreted-text role="guilabel"} pop-up
window, from which all details of that particular
`RfQ (Request for Quotation)`{.interpreted-text role="abbr"} can be
viewed.

Once ready, click `Close`{.interpreted-text role="guilabel"} to close
the pop-up window.

In the
`What about the alternative Requests for Quotations?`{.interpreted-text
role="guilabel"} pop-up window, two options are presented:
`Cancel Alternatives`{.interpreted-text role="guilabel"} and
`Keep Alternatives`{.interpreted-text role="guilabel"}.

If this `PO (Purchase Order)`{.interpreted-text role="abbr"} should
**not** be confirmed, click `Discard`{.interpreted-text
role="guilabel"}.

Selecting `Cancel Alternatives`{.interpreted-text role="guilabel"}
automatically cancels the alternative
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.
Selecting `Keep Alternatives`{.interpreted-text role="guilabel"} keeps
the alternative `RfQs (Requests for Quotation)`{.interpreted-text
role="abbr"} open, so they can still be accessed, if any additional
product quantities need to be ordered later.

Once all products are ordered, select
`Cancel Alternatives`{.interpreted-text role="guilabel"} from whichever
`PO (Purchase Order)`{.interpreted-text role="abbr"} is open at that
time.

{.align-center}

Finally, using the breadcrumbs at the top of the page, click
`Requests for Quotation`{.interpreted-text role="guilabel"} to navigate
back to an overview of all
`RfQs (Requests for Quotation)`{.interpreted-text role="abbr"}.

The canceled orders can be seen, greyed out and listed with a
`Cancelled`{.interpreted-text role="guilabel"} status, under the
`Status`{.interpreted-text role="guilabel"} column at the far-right of
their respective rows.

Now that all product quantities have been ordered, the purchase process
can be completed, and the products can be received into the warehouse.

::: {.seealso}
`blanket_orders`{.interpreted-text role="doc"}
:::
