PDF quote builder
=================

The *PDF Quote Builder* in Odoo *Sales* provides the opportunity to send
customers a fully customized PDF file for quotes, showcasing the company
and products, with various information and design elements, instead of
just showing the price and total.

The PDF Quote Builder groups header pages, product descriptions, the
price(s), and footer pages to create a detailed quote. It can also
inject dynamic texts in the PDF to personalize the offer for the
customer.

Having a customized PDF in quotes provides a heightened conclusion to
the shopping experience for customers, and adds an elegant level of
professionalism to a company.

::: {.seealso}
[Odoo Quick Tips - Create a PDF quote
\
:::

::: {.note}
::: {.title}
Note
:::

It is recommended to edit PDF forms with Adobe software. The form fields
on the header and footer PDF templates are necessary to get dynamic
values with Odoo.
:::

Configuration
-------------

In order to add custom PDF files for quotes, the
`PDF Quote builder`{.interpreted-text role="guilabel"} feature *must* be
configured.

To do that, navigate to
`Sales app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, on the `Settings`{.interpreted-text
role="guilabel"} page, scroll to the
`Quotations & Orders`{.interpreted-text role="guilabel"} section, and
locate the `PDF Quote builder`{.interpreted-text role="guilabel"}
feature.

{.align-center}

Here, custom `Header pages`{.interpreted-text role="guilabel"} and
`Footer pages`{.interpreted-text role="guilabel"} can be uploaded. To
upload either, click the `Upload your file`{.interpreted-text
role="guilabel"} button, or the `✏️ (pencil)`{.interpreted-text
role="guilabel"} icon to the right of the desired field, and proceed to
locate, select, and upload the desired PDF file.

::: {.note}
::: {.title}
Note
:::

Headers and footers can also be added directly in a quotation template,
so it\'s possible to have different variations per template.
:::

Clicking the `🗑️ (trash)`{.interpreted-text role="guilabel"} icon
deletes the current PDF file and replaces the blank field with an
`Upload your file`{.interpreted-text role="guilabel"} button.

Once the desired PDF file(s) are uploaded in the appropriate fields in
the `PDF Quote
builder`{.interpreted-text role="guilabel"} section of the *Sales*
`Settings`{.interpreted-text role="guilabel"} page, be sure to click
`Save`{.interpreted-text role="guilabel"}.

The files uploaded here will be the default PDF used for all quotes.

::: {.note}
::: {.title}
Note
:::

Values set in the PDF Quote Builder settings are company-specific.
:::

Dynamic text in PDFs
--------------------

While creating custom PDFs for quotes, use *dynamic text* for Odoo to
auto-fill the PDF content with information related to the quote from the
Odoo database, like names, prices, etc.

Dynamic text values are form components (text inputs) that can be added
in a PDF file, and Odoo automatically fills those values in with
information related to the quote.

### Dynamic text values

Below are common dynamic text values used in custom PDFs, and what they
represent:

-   `name`{.interpreted-text role="guilabel"}: Sales Order Reference
-   `partner_id__name`{.interpreted-text role="guilabel"}: Customer Name
-   `user_id__name`{.interpreted-text role="guilabel"}: Salesperson Name
-   `amount_untaxed`{.interpreted-text role="guilabel"}: Untaxed Amount
-   `amount_total`{.interpreted-text role="guilabel"}: Total Amount
-   `delivery_date`{.interpreted-text role="guilabel"}: Delivery Date
-   `validity_date`{.interpreted-text role="guilabel"}: Expiration Date
-   `client_order_ref`{.interpreted-text role="guilabel"}: Customer
    Reference

::: {.note}
::: {.title}
Note
:::

Double underscore notation for `partner_id__name`{.interpreted-text
role="guilabel"} and `user_id__name`{.interpreted-text role="guilabel"}
values are used in place of the typically used [.]{.title-ref} symbol
because the library currently does not support the [.]{.title-ref}
symbol.
:::

Product-specific dynamic text values are as follows:

-   `description`{.interpreted-text role="guilabel"}: Product
    Description
-   `quantity`{.interpreted-text role="guilabel"}: Quantity
-   `uom`{.interpreted-text role="guilabel"}: Unit of Measure (UoM)
-   `price_unit`{.interpreted-text role="guilabel"}: Price Unit
-   `discount`{.interpreted-text role="guilabel"}: Discount
-   `product_sale_price`{.interpreted-text role="guilabel"}: Product
    List Price
-   `taxes`{.interpreted-text role="guilabel"}: Taxes name joined by a
    comma ([,]{.title-ref})
-   `tax_excl_price`{.interpreted-text role="guilabel"}: Tax Excluded
    Price
-   `tax_incl_price`{.interpreted-text role="guilabel"}: Tax Included
    Price

::: {.example}
When a PDF is built, it\'s best practice to use common dynamic text
values (`name`{.interpreted-text role="guilabel"} and
`partner_id_name`{.interpreted-text role="guilabel"}). When uploaded
into the database, Odoo auto-populates those fields with the information
from their respective fields.

In this case, Odoo would auto-populate the Sales Order Reference in the
`name`{.interpreted-text role="guilabel"} dynamic text field, and the
Customer Name in the `partner_id_name`{.interpreted-text
role="guilabel"} field.

{.align-center}
:::

Once the PDF file(s) are complete, save them to the computer\'s hard
drive, and proceed to upload them to Odoo via
`Sales app --> Configuration --> Settings --> PDF Quote builder`{.interpreted-text
role="menuselection"}.

Upload the created PDF in the `Header pages`{.interpreted-text
role="guilabel"} or `Footer pages`{.interpreted-text role="guilabel"}
field.

Once the upload(s) are complete, click `Save`{.interpreted-text
role="guilabel"}.

Add PDF to product
------------------

In Odoo *Sales*, it\'s also possible to add a custom PDF to a product
form. When a PDF is added to a product, and that product is used in a
quotation, that PDF is also inserted in the final PDF.

To add a custom PDF to a product, start by navigating to
`Sales app --> Products -->
Products`{.interpreted-text role="menuselection"}, and select the
desired product to which a custom PDF should be added.

::: {.note}
::: {.title}
Note
:::

A document could also be added to a product variant, instead of a
product. If there are documents on a product *and* on its variant,
**only** the documents in the variant are shown.

To add a custom document to a product variant, navigate to
`Sales app --> Products
--> Product Variants`{.interpreted-text role="menuselection"}. Select
the desired variant, click the `Documents`{.interpreted-text
role="guilabel"} smart button, and proceed to upload the custom
document(s) to the specific product variant.
:::

On the product page, click the `Documents`{.interpreted-text
role="guilabel"} smart button at the top of the page.

{.align-center}

Doing so reveals a separate `Documents`{.interpreted-text
role="guilabel"} page for that product, wherein files related to that
product can be uploaded. From this page, either click
`New`{.interpreted-text role="guilabel"} or `Upload`{.interpreted-text
role="guilabel"}.

Clicking `Upload`{.interpreted-text role="guilabel"} instantly provides
the opportunity to upload the desired document. Then, the document can
be further configured on the document card, or by clicking the three
dots icon in the top right corner of the document card, and then
clicking `Edit`{.interpreted-text role="guilabel"}.

Clicking `New`{.interpreted-text role="guilabel"} reveals a blank
documents form, in which the desired PDF can be uploaded via the
`Upload your file`{.interpreted-text role="guilabel"} button on the
form, located in the `File Content`{.interpreted-text role="guilabel"}
field.

{.align-center}

Various information and configurations related to the uploaded document
can be modified here.

The first field on the documents form is for the
`Name`{.interpreted-text role="guilabel"} of the document, and it is
grayed-out (not clickable) until a document is uploaded. Once a PDF has
been uploaded, the `Name`{.interpreted-text role="guilabel"} field is
auto-populated with the name of the PDF, and it can then be edited.

Prior to uploading a document, there\'s the option to designate whether
the document is a `File`{.interpreted-text role="guilabel"} or
`URL`{.interpreted-text role="guilabel"} from the
`Type`{.interpreted-text role="guilabel"} drop-down field menu.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If a PDF is uploaded, the `Type`{.interpreted-text role="guilabel"}
field is auto-populated to `File`{.interpreted-text role="guilabel"},
and it cannot be modified.
:::

Then, in the `Sales`{.interpreted-text role="guilabel"} section, in the
`Visible at`{.interpreted-text role="guilabel"} field, click the
drop-down menu, and select either: `Quotation`{.interpreted-text
role="guilabel"}, `Confirmed order`{.interpreted-text role="guilabel"},
or `Inside
quote`{.interpreted-text role="guilabel"}.

-   `Quotation`{.interpreted-text role="guilabel"}: the document is sent
    to (and accessible by) customers at any time.
-   `Confirmed order`{.interpreted-text role="guilabel"}: the document
    is sent to customers upon the confirmation of an order. This is best
    for user manuals and other supplemental documents.
-   `Inside quote`{.interpreted-text role="guilabel"}: the document is
    included in the PDF of the quotation, between the header pages and
    the `Pricing`{.interpreted-text role="guilabel"} section of the
    quote.

::: {.example}
When the `Inside quote`{.interpreted-text role="guilabel"} option for
the `Visible at`{.interpreted-text role="guilabel"} field is chosen, and
the custom PDF file, [Sample Builder.pdf]{.title-ref} is uploaded, the
PDF is visible on the quotation the in the *customer portal* under the
`Documents`{.interpreted-text role="guilabel"} field.

{.align-center}
:::

Lastly, in the `E-Commerce`{.interpreted-text role="guilabel"} section,
decide whether or not to `Show on product
page`{.interpreted-text role="guilabel"} on the front-end (in the online
store).

::: {.example}
When the `Show on product page`{.interpreted-text role="guilabel"}
option is enabled, a link to the uploaded document, [Sample
Builder.pdf]{.title-ref}, appears on the product\'s page, located on the
frontend in the online store.

It appears beneath a `Documents`{.interpreted-text role="guilabel"}
heading, with a link showcasing the name of the uploaded document.

> {.align-center}
:::

PDF quote
---------

Once a quote with a pre-configured PDF has been confirmed, Odoo provides
the option to print the confirmed quote to check for errors, or to keep
for records.

To print the PDF quote, navigate to the confirmed quote, and click the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon to reveal a
drop-down menu. From this drop-down menu, select
`Print`{.interpreted-text role="guilabel"}, then select
`PDF Quote`{.interpreted-text role="guilabel"}.

{.align-center}

Doing so instantly downloads the PDF quote. When opened, the PDF quote,
along with the configured product PDF that was set to be visible inside
the quote, can be viewed and printed.

::: {.note}
::: {.title}
Note
:::

Download these `PDF quote builder examples
<pdf_quote_builder/pdfquotebuilderexamples.zip>`{.interpreted-text
role="download"} for added reference.
:::

::: {.seealso}
\-
`/applications/sales/sales/send_quotations/quote_template`{.interpreted-text
role="doc"}
:::
