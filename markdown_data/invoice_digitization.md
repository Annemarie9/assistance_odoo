# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/vendor_bills/invoice_digitization.md

Document digitization
=====================

Document digitization refers to the process of converting paper or
digital documents into records in a database. Using
`OCR (optical character recognition)`{.interpreted-text role="abbr"} and
artificial intelligence technologies, Odoo reads the content and
automatically creates and fills in the record\'s details. This process
is mainly used for vendor bills (or refunds).

::: {.note}
::: {.title}
Note
:::

Although less common, this digitization process can also be applied to
customer invoices and credit notes. The
`settings <accounting/bill-digitization/configuration>`{.interpreted-text
role="ref"} need to be adjusted accordingly.
:::

::: {.seealso}
\- [Test Odoo\'s invoice
digitization](https://www.odoo.com/app/invoice-automation) - [Odoo
Tutorials: Vendor Bill
Digitization](https://www.odoo.com/slides/slide/vendor-bill-digitization-7065)
- `/applications/essentials/in_app_purchase`{.interpreted-text
role="doc"}
:::

Configuration {#accounting/bill-digitization/configuration}
-------------

Go to `Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and navigate to the
`Digitization`{.interpreted-text role="guilabel"} section. Enable the
`Document Digitization`{.interpreted-text role="guilabel"} option and
choose whether `Vendor Bills`{.interpreted-text role="guilabel"} should
be processed automatically or on demand.

::: {.note}
::: {.title}
Note
:::

If the `Single Invoice Line Per Tax`{.interpreted-text role="guilabel"}
option is enabled, only one line is created per tax in the new vendor
bill, regardless of the number of lines on it.
:::

Vendor bills upload {#accounting/bill-digitization/vendor-bills-upload}
-------------------

Vendor bills are
`uploaded manually <accounting/bill-digitization/manual-upload>`{.interpreted-text
role="ref"} or sent to a
`designated email alias <accounting/bill-digitization/email-alias>`{.interpreted-text
role="ref"} to be digitized. Once the bill is uploaded, the document
preview appears on the right side of the screen.

::: {.seealso}
`Vendor bills <../vendor_bills>`{.interpreted-text role="doc"}
:::

### Manual upload {#accounting/bill-digitization/manual-upload}

From the `Accounting Dashboard`{.interpreted-text role="guilabel"},
click `Upload`{.interpreted-text role="guilabel"} on the `Vendor
Bills`{.interpreted-text role="guilabel"} journal.

### Upload via email alias {#accounting/bill-digitization/email-alias}

Vendor bills can be uploaded via an email alias associated with the
relevant journal in two ways:

-   scanned from a connected scanner configured to send email to an
    email alias;
-   sent directly to an email alias.

Each PDF attached to the email is automatically converted into a new
draft vendor bill.

::: {.note}
::: {.title}
Note
:::

\- Only PDF and XML formats are processed via an email alias associated
with a journal. - JPEG files must be processed via
`email alias in the Documents app <documents/upload>`{.interpreted-text
role="ref"}.
:::

To add an email alias to a journal, follow these steps:

1.  Make sure an
    `alias domain <../../../websites/website/configuration/domain_names>`{.interpreted-text
    role="doc"} has been configured.
2.  The default email alias [vendor-bills@]{.title-ref} followed by the
    alias domain is automatically created and available in the
    `Advanced Settings`{.interpreted-text role="guilabel"} tab of the
    `Vendor Bills`{.interpreted-text role="guilabel"} journal.
3.  To change a default email alias, go to
    `Accounting --> Configuration -->
    Journals`{.interpreted-text role="menuselection"}, select the
    corresponding journal, and edit the `Email Alias`{.interpreted-text
    role="guilabel"} in the `Advanced Settings`{.interpreted-text
    role="guilabel"} tab.
4.  Configure the connected scanner to send scanned documents to the
    email alias, if needed.

::: {.note}
::: {.title}
Note
:::

Alternatively, an
`email alias in the Documents app <documents/upload>`{.interpreted-text
role="ref"} can be used to automatically send vendor bills to the
`Finance`{.interpreted-text role="guilabel"} `workspace
<documents/workspaces>`{.interpreted-text role="ref"} (e.g.,
[inbox-financial\@example.odoo.com]{.title-ref}).
:::

Digitization and data recognition with AI {#accounting/bill-digitization/digitization}
-----------------------------------------

Depending on the
`settings <accounting/bill-digitization/configuration>`{.interpreted-text
role="ref"}, documents are either automatically digitized or require
manual processing if digitization is set to on-demand only.

To manually digitize an `uploaded document
<accounting/bill-digitization/vendor-bills-upload>`{.interpreted-text
role="ref"}, click `Digitize document`{.interpreted-text
role="guilabel"}.

Once the document has been digitized, a blue banner appears; click
`oi-arrow-right`{.interpreted-text role="icon"}
`Refresh`{.interpreted-text role="guilabel"} if needed. Review and
correct any information uploaded during digitization: click on the
related field(s) to edit them, or click
`Reload AI data`{.interpreted-text role="guilabel"} to refresh the data.

Then, click `Confirm`{.interpreted-text role="guilabel"} to post the
document.

::: {.tip}
::: {.title}
Tip
:::

Once a document has been digitized, the `Vendor`{.interpreted-text
role="guilabel"} field remains empty if the vendor doesn\'t exist in the
database. To add it, click the `fa-caret-down`{.interpreted-text
role="icon"} `(down arrow)`{.interpreted-text role="guilabel"} in the
`Vendor`{.interpreted-text role="guilabel"} field; the vendor name
appears highlighted in the document preview on the right. Click it to
open a new vendor form with the name pre-filled.
:::

::: {.note}
::: {.title}
Note
:::

The following vendor bill fields are recognized by OCR:

-   `Vendor`{.interpreted-text role="guilabel"},
    `Bill Reference`{.interpreted-text role="guilabel"},
    `Bill Date`{.interpreted-text role="guilabel"}, `Payment
    Reference`{.interpreted-text role="guilabel"} (only in the Belgian
    +++xxx/xxxx/xxxxx+++ format), `Recipient Bank`{.interpreted-text
    role="guilabel"}, `Due Date`{.interpreted-text role="guilabel"}, and
    the currency (in a `multi-currency
    <../get_started/multi_currency>`{.interpreted-text role="doc"}
    environment and if the currency is activated).
-   From the `Invoices Lines`{.interpreted-text role="guilabel"} tab:
    `Product`{.interpreted-text role="guilabel"} description/label,
    `Quantity`{.interpreted-text role="guilabel"}, unit
    `Price`{.interpreted-text role="guilabel"},
    `Taxes`{.interpreted-text role="guilabel"} (if the `tax is activated
    <taxes/list_activation>`{.interpreted-text role="ref"}; this field
    is not recognized by OCR for the `Indian
    localization <../../fiscal_localizations/india>`{.interpreted-text
    role="doc"}), `Untaxed Amount`{.interpreted-text role="guilabel"},
    and `Total`{.interpreted-text role="guilabel"}.
:::

### Vendor bill matching with purchase orders {#accounting/bill-digitization/vendor-bills-matching-po}

When a digitized vendor bill is recognized by OCR, Odoo first searches
the database for a matching purchase order and its number. If a match is
found, the system copies as much information as possible from the
purchase order to the vendor bill. For example, the vendor `Bill
Reference`{.interpreted-text role="guilabel"} number is overwritten by
the `Vendor Reference`{.interpreted-text role="guilabel"} from the
purchase order.

::: {.note}
::: {.title}
Note
:::

\- All changes are logged in the chatter. - A smart button linking to
the related purchase order is available on the vendor bill.
:::

To correct any mismatches, update the incorrect fields on the vendor
bill.

::: {.tip}
::: {.title}
Tip
:::

\- Electronic vendor bills with embedded XML ensure more accurate and
efficient processing. - Alternatively, the
`Auto-complete <accounting/vendor_bills/bill-completion>`{.interpreted-text
role="ref"} feature can be used to transfer information from the
purchase order to the vendor bill, without requiring OCR.
:::

Pricing {#accounting/bill-digitization/pricing}
-------

The document digitization feature is an In-App Purchase (IAP) service
requiring prepaid credits. Digitizing one document uses one credit.

To buy credits,
`go to the Settings app <iap/buying_credits>`{.interpreted-text
role="ref"} or `Accounting -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
navigate to the `Digitization`{.interpreted-text role="guilabel"}
section, and click `Buy credits`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- Odoo Enterprise users with a valid subscription get free credits to
test IAP features before purchasing more credits for the database. This
includes demo/training databases, educational databases, and
one-app-free databases. - XML files don\'t require OCR credits because
they contain structured data that can be processed directly, without
OCR.
:::

::: {.seealso}
\- [Odoo In-App Purchase Privacy
Policy](https://iap.odoo.com/privacy#header_6) -
`/applications/essentials/in_app_purchase`{.interpreted-text role="doc"}
:::
