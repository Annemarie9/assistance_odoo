# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/vendor_bills.md

show-content

:   

Vendor bills
============

Vendor bills can be registered either **manually** or **automatically**
in Odoo. The
`Aged Payable report <accounting/vendor_bills/age-payable-report>`{.interpreted-text
role="ref"} provides an overview of all outstanding bills to help ensure
timely payment of the correct amounts.

::: {.seealso}
\- Tutorial [Registering a vendor
bill](https://www.odoo.com/slides/slide/register-a-vendor-bill-6582) -
`/applications/inventory_and_mrp/purchase/manage_deals/manage`{.interpreted-text
role="doc"}
:::

Bill creation {#accounting/vendor_bills/creation}
-------------

### Manually {#accounting/vendor_bills/creation-manual}

To create a vendor bill manually, go to
`Accounting --> Vendors --> Bills`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Alternatively, it is possible to create a vendor bill from the
Accounting dashboard:

-   either click `Create Manually`{.interpreted-text role="guilabel"} on
    the `Vendor Bills`{.interpreted-text role="guilabel"} journal;
-   or click the `fa-ellipsis-v`{.interpreted-text role="icon"}
    `(vertical ellipsis)`{.interpreted-text role="guilabel"} icon of the
    `Vendor Bills`{.interpreted-text role="guilabel"} journal, then
    `Bill`{.interpreted-text role="guilabel"} under the
    `New`{.interpreted-text role="guilabel"} section.
:::

### Automatically {#accounting/vendor_bills/automatic}

Vendor bills can be automatically created by **sending an email** to an
`email alias
<accounting/bill-digitization/email-alias>`{.interpreted-text
role="ref"} associated with the purchase journal, or by
`uploading a PDF <accounting/bill-digitization/manual-upload>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

\- Once the bill is uploaded, the PDF document appears on the right side
of the screen, making it easy to fill in the bill information. - Bills
can be `digitized <vendor_bills/invoice_digitization>`{.interpreted-text
role="doc"} for automatic completion and `matched with purchase orders
<accounting/bill-digitization/vendor-bills-matching-po>`{.interpreted-text
role="ref"} to replace OCR-detected data with the existing purchase
order\'s details. - Services such as digitizing scanned or PDF vendor
bills in Odoo require `In-App
Purchase (IAP) </applications/essentials/in_app_purchase>`{.interpreted-text
role="doc"} credit or tokens.
:::

::: {.seealso}
`Vendor bills matching with purchase orders
<accounting/bill-digitization/vendor-bills-matching-po>`{.interpreted-text
role="ref"}
:::

Bill completion {#accounting/vendor_bills/bill-completion}
---------------

Whether the bill is created manually or automatically, make sure the
following fields are appropriately completed:

-   `Vendor`{.interpreted-text role="guilabel"}: Odoo automatically
    fills in some information based on the information on the vendor\'s
    contact record as well as previous purchase orders and bills.
-   `Bill Reference`{.interpreted-text role="guilabel"}: Add the sales
    order reference provided by the vendor. This field is used to
    `match <accounting/payments/payments-matching>`{.interpreted-text
    role="ref"} the products when they are received.
-   `Auto-Complete`{.interpreted-text role="guilabel"}: Select a past
    bill/purchase order to complete the document automatically. The
    `Vendor`{.interpreted-text role="guilabel"} field should be
    completed before completing this field.
-   `Bill Date`{.interpreted-text role="guilabel"}: Select the
    document\'s issuance date.
-   `Accounting Date`{.interpreted-text role="guilabel"}: Update the
    document\'s accounting registration date if needed.
-   `Payment Reference`{.interpreted-text role="guilabel"}: The
    `Memo`{.interpreted-text role="guilabel"} field automatically
    includes the payment reference once the payment is registered.
-   `Recipient Bank`{.interpreted-text role="guilabel"}: Indicates the
    account number to which the payment will be made. This field is
    required when paying via batch payment files (such as `NACHA
    <l10n_us/ach-electronic-transfers>`{.interpreted-text role="ref"}
    and `SEPA <payments/pay_sepa>`{.interpreted-text role="doc"}).
-   `Due Date`{.interpreted-text role="guilabel"} or
    `Payment Terms`{.interpreted-text role="guilabel"} must be specified
    for the bill payment.
-   `Journal`{.interpreted-text role="guilabel"}: Select which journal
    should record the bill and in which `currency
    <get_started/multi_currency>`{.interpreted-text role="doc"}.

::: {.note}
::: {.title}
Note
:::

Multiple bills for the same purchase order may be issued if the vendor
is on back-order and sends invoices as products are shipped or if the
vendor sends partial bills or requests a deposit. In this case, multiple
bills may have the same `Bill Reference`{.interpreted-text
role="guilabel"}.
:::

Bill confirmation {#accounting/vendor_bills/bill-confirmation}
-----------------

Click `Confirm`{.interpreted-text role="guilabel"} when the document is
completed. The status changes to `Posted`{.interpreted-text
role="guilabel"}, and a journal entry is generated based on the vendor
bill information. On confirmation, Odoo assigns each vendor bill a
unique number from a defined
`sequence <vendor_bills/sequence>`{.interpreted-text role="doc"}.

::: {.note}
::: {.title}
Note
:::

Once confirmed, a vendor bill can no longer be updated. Click
`Reset to draft`{.interpreted-text role="guilabel"} if changes are
required.
:::

Payment and reconciliation {#accounting/vendor_bills/bill-payment}
--------------------------

To register a payment, click on `Register Payment`{.interpreted-text
role="guilabel"}. In the `Register Payment`{.interpreted-text
role="guilabel"} window, select the `Journal`{.interpreted-text
role="guilabel"}, the `Payment Method`{.interpreted-text
role="guilabel"}, the `Amount`{.interpreted-text role="guilabel"}, and
the `Currency`{.interpreted-text role="guilabel"}.

When the `Amount`{.interpreted-text role="guilabel"} paid is less than
the total remaining amount on the vendor bill, the payment is
`partial <accounting/payments/partial-payment>`{.interpreted-text
role="ref"}, and the `Payment
Difference`{.interpreted-text role="guilabel"} field displays the
outstanding balance.

The `Memo`{.interpreted-text role="guilabel"} field is filled
automatically if the `Payment Reference`{.interpreted-text
role="guilabel"} has been set correctly on the vendor bill. If the field
is empty, select the vendor invoice number as a reference.

Then click `Create payment`{.interpreted-text role="guilabel"}. An
`In Payment`{.interpreted-text
role="guilabel"}/`Partial`{.interpreted-text role="guilabel"} banner
appears on the bill until it is
`reconciled <bank/reconciliation>`{.interpreted-text role="doc"} and its
status updates to `Paid`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `payments`{.interpreted-text role="doc"} -
`bank/reconciliation`{.interpreted-text role="doc"}
:::

Aged payable report {#accounting/vendor_bills/age-payable-report}
-------------------

To get an overview of the open vendor bills and their due dates, go to
`Accounting
--> Reporting --> Aged payable`{.interpreted-text role="menuselection"}.

Click the `fa-caret-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon next to a vendor
to view the details of all their outstanding bills, including the due
dates and amounts.

::: {.note}
::: {.title}
Note
:::

Click `PDF`{.interpreted-text role="guilabel"} or
`XLSX`{.interpreted-text role="guilabel"} to generate a PDF or XLSX
file, respectively.
:::

::: {.toctree titlesonly=""}
vendor\_bills/invoice\_digitization vendor\_bills/assets
vendor\_bills/deferred\_expenses vendor\_bills/sequence
:::
