# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/manage_deals/rfq.md

Requests for quotation
======================

::: {#purchase/manage_deals/rfq}
Odoo\'s requests for quotation (RFQs) feature in the **Purchase** app
standardizes ordering products from multiple vendors with varying prices
and delivery times.
:::

`RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} are
documents companies send to vendors requesting product pricing. In Odoo,
once the vendor approves the
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"}, the
purchase order (PO) is confirmed to align on lead times and pricing.

Configuration
-------------

### Product

To auto-populate product information and prices on an
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"}, configure
products by going to
`Purchase app --> Products --> Products`{.interpreted-text
role="menuselection"}. Select an existing product, or create a new one
by selecting `New`{.interpreted-text role="guilabel"}. Doing so opens
the product form, where various sales and purchasing data can be
configured.

To configure purchasable products, tick the
`Can be purchased`{.interpreted-text role="guilabel"} checkbox, under
the product name. Then, go to the `Inventory`{.interpreted-text
role="guilabel"} tab, and enable the `Buy`{.interpreted-text
role="guilabel"} route.

{.align-center}

### Vendor pricelist {#purchase/manage_deals/vendor-pricelist}

In the `Purchase`{.interpreted-text role="guilabel"} tab of the product
form, input the vendor and their price, to have this information
auto-populate on an `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"} each time the product is listed.

::: {.seealso}
`../products/pricelist`{.interpreted-text role="doc"}
:::

Default columns include `Quantity`{.interpreted-text role="guilabel"},
`Price`{.interpreted-text role="guilabel"}, and
`Delivery Lead Time`{.interpreted-text role="guilabel"}, but other
columns like, `Product Variant`{.interpreted-text role="guilabel"} or
`Discounts`{.interpreted-text role="guilabel"}, can also be enabled.

To enable or disable columns, click the
`oi-settings-adjust`{.interpreted-text role="icon"}
`(additional options)`{.interpreted-text role="guilabel"} icon on the
right side of the header row to reveal a drop-down menu of additional
columns that can be added (or removed) from the
`Purchase`{.interpreted-text role="guilabel"} tab.

::: {.note}
::: {.title}
Note
:::

Alternatively, prices and delivery lead times for existing products can
be added in bulk by going to
`Purchase app --> Configuration --> Vendor Pricelists`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} in
the top-left corner. In the `Vendor`{.interpreted-text role="guilabel"}
section of the pricelist form that appears, add the product information
as it pertains to the vendor.
:::

Order products
--------------

With products and prices configured, follow these steps to create and
send `RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} to
make purchases for the company.

### `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} dashboard

To get started, navigate to
`Purchase app --> Orders --> Requests for Quotation`{.interpreted-text
role="menuselection"}.

The `Requests for Quotation`{.interpreted-text role="guilabel"}
dashboard displays an overview of the company\'s
`RFQs (Requests for Quotation)`{.interpreted-text role="abbr"},
`POs (Purchase Orders)`{.interpreted-text role="abbr"}, and their
status. The top of the screen breaks down all
`RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} in the
company, as well as individual ones (where the user is the buyer) with a
summary of their status.

The top-right corner also provides a quick report of the company\'s
recent purchases by total value, lead times, and number of
`RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} sent.

Additionally, the dashboard includes buttons for:

-   `To Send`{.interpreted-text role="guilabel"}: orders in the
    `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} stage
    that have not been sent to the vendor.
-   `Waiting`{.interpreted-text role="guilabel"}:
    `RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} that
    have been sent by email, and are waiting on vendor confirmation.
-   `Late`{.interpreted-text role="guilabel"}:
    `RFQs (Requests for Quotation)`{.interpreted-text role="abbr"} or
    `POs (Purchase Orders)`{.interpreted-text role="abbr"} where the
    `Order Deadline`{.interpreted-text role="guilabel"} has passed.

{.align-center}

In addition to various view options, the
`Requests for Quotation`{.interpreted-text role="guilabel"} dashboard
provides `Filters`{.interpreted-text role="guilabel"} and
`Group By`{.interpreted-text role="guilabel"} options, accessible via
the search bar drop-down menu.

::: {.seealso}
`../../../essentials/search`{.interpreted-text role="doc"}
:::

### Create new `RFQ (Request for Quotation)`{.interpreted-text role="abbr"}

To create a new `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"}, click the `New`{.interpreted-text role="guilabel"} button
on the top-left corner of the `Requests for Quotation`{.interpreted-text
role="guilabel"} dashboard to reveal a new
`PO (Purchase Order)`{.interpreted-text role="abbr"} form.

Start by assigning a `Vendor`{.interpreted-text role="guilabel"}.

The `Vendor Reference`{.interpreted-text role="guilabel"} field points
to the sales and delivery order numbers sent by the vendor. This comes
in handy once products are received, and the
`PO (Purchase Order)`{.interpreted-text role="abbr"} needs to be matched
to the delivery order.

The `Blanket Order`{.interpreted-text role="guilabel"} field refers to
long-term purchase agreements on recurring orders with set pricing. To
view and configure blanket orders, head to `Purchase app --> Orders
--> Purchase agreements`{.interpreted-text role="menuselection"}.

The `Currency`{.interpreted-text role="guilabel"} can be changed, if
purchasing products from a vendor in another country.

Next, configure an `Order Deadline`{.interpreted-text role="guilabel"},
which is the date by which the vendor must confirm their agreement to
supply the products.

::: {.note}
::: {.title}
Note
:::

After the `Order Deadline`{.interpreted-text role="guilabel"} is
exceeded, the `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"} is marked as late, but the products can still be ordered.
:::

`Expected Arrival`{.interpreted-text role="guilabel"} is automatically
calculated based on the `Order Deadline`{.interpreted-text
role="guilabel"} and vendor lead time. Tick the checkbox for
`Ask confirmation`{.interpreted-text role="guilabel"} to ask for signage
at delivery.

With the `Storage Locations feature
<../../inventory/warehouses_storage/inventory_management/use_locations>`{.interpreted-text
role="doc"} activated, the `Deliver to`{.interpreted-text
role="guilabel"} field appears, with options for the order shipment.

Select the receiving warehouse address here, or select
`Dropship`{.interpreted-text role="guilabel"} to indicate that this
order is to be shipped directly to the end customer. When
`Dropship`{.interpreted-text role="guilabel"} is selected, the
`Dropship address`{.interpreted-text role="guilabel"} field is enabled.
Contact names auto-populate here from the **Contacts** app.

#### Products tab

In the `Products`{.interpreted-text role="guilabel"} tab, add the
products to be ordered. Click `Add a product`{.interpreted-text
role="guilabel"}, and type in the product name, or select the item from
the drop-down menu.

To create a new product and add it, type the new product name in the
`Product`{.interpreted-text role="guilabel"} column, select
`Create [product name]`{.interpreted-text role="guilabel"} from the
resulting drop-down menu, and manually add the unit price. Or, select
`Create and edit...`{.interpreted-text role="guilabel"} to be taken to
the product form for that new item.

`Catalog`{.interpreted-text role="guilabel"} can also be selected to
navigate to a product menu from the chosen vendor. From here, products
can be added to the cart.

::: {.note}
::: {.title}
Note
:::

To make adjustments to products and prices, access the product form by
clicking the `oi-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon that becomes
available upon hovering over the `Product`{.interpreted-text
role="guilabel"} name.
:::

### Send `RFQ (Request for Quotation)`{.interpreted-text role="abbr"}

Clicking `Send by Email`{.interpreted-text role="guilabel"} reveals a
`Compose Email`{.interpreted-text role="guilabel"} pop-up window, with a
`Purchase: Request for Quotation`{.interpreted-text role="guilabel"}
template loaded, ready to send to the vendor\'s email address
(configured in the **Contacts** app).

After crafting the desired message, click `Send`{.interpreted-text
role="guilabel"}. Once sent, the
`RFQ (Request for Quotation)`{.interpreted-text role="abbr"} moves to
the `RFQ Sent`{.interpreted-text role="guilabel"} stage.

Clicking `Print RFQ`{.interpreted-text role="guilabel"} downloads a PDF
of the `RFQ (Request for Quotation)`{.interpreted-text role="abbr"}.

### Confirm order

Clicking `Confirm Order`{.interpreted-text role="guilabel"} directly
transforms the `RFQ (Request for Quotation)`{.interpreted-text
role="abbr"} into an active `PO (Purchase Order)`{.interpreted-text
role="abbr"}.

::: {.tip}
::: {.title}
Tip
:::

Odoo tracks communications on each order through the chatter of the
`PO (Purchase Order)`{.interpreted-text role="abbr"} form. This shows
the emails sent between the user and the contact, as well as any
internal notes and activities. Messages, notes, and activities can also
be logged on the chatter.
:::

Once an `RFQ (Request for Quotation)`{.interpreted-text role="abbr"} is
confirmed, it creates a `PO (Purchase Order)`{.interpreted-text
role="abbr"}.

On the new `PO (Purchase Order)`{.interpreted-text role="abbr"}, the
`Order Deadline`{.interpreted-text role="guilabel"} field changes to
`Confirmation Date`{.interpreted-text role="guilabel"}, which displays
the date and time the user confirmed the order.

Depending on the user\'s chosen configuration in the **Purchase** app
settings, a *vendor bill* is created once products have been ordered or
received. For more information, refer to the documentation on
`managing vendor bills <manage>`{.interpreted-text role="doc"}.

::: {.note}
::: {.title}
Note
:::

After an order is placed, clicking `Receive Products`{.interpreted-text
role="guilabel"} records the reception of new products into the
database.
:::

::: {.note}
::: {.title}
Note
:::

With the **Inventory** app installed, confirming a
`PO (Purchase Order)`{.interpreted-text role="abbr"} automatically
creates a receipt document, with the product information and expected
arrival dates automatically populated.
:::

::: {.seealso}
`manage`{.interpreted-text role="doc"}
:::
