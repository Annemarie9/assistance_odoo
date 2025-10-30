# File: /content/odoo_doc17.0/fr/content/applications/finance/fiscal_localizations/vietnam.md

Vietnam
=======

Modules {#localizations/vietnam/modules}
-------

The following modules are installed automatically with the Vietnamese
localization:

  Name                                                         Technical name                         Description
  ------------------------------------------------------------ -------------------------------------- -------------------------------------------------------------------------------------------------------------------------------
  `Vietnam - Accounting`{.interpreted-text role="guilabel"}    [l10n\_vn]{.title-ref}                 This module includes the default `fiscal localization package <fiscal_localizations/packages>`{.interpreted-text role="ref"}.
  `Vietnam - E-invoicing`{.interpreted-text role="guilabel"}   [l10n\_vn\_edi\_viettel]{.title-ref}   This module includes the features required for integration with `SInvoice
                                                                                                      <localizations/vietnam/sinvoice>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

In some cases, such as when upgrading to a version with additional
modules, it is possible that modules may not be installed automatically.
Any missing modules can be manually `installed
<general/install>`{.interpreted-text role="ref"}.
:::

Company {#localizations/vietnam/company}
-------

To use all the features of this fiscal localization, the following
fields are required on the
`company record </applications/general/companies>`{.interpreted-text
role="doc"}:

-   `Name`{.interpreted-text role="guilabel"}

-   `Address`{.interpreted-text role="guilabel"}, including the
    `City`{.interpreted-text role="guilabel"}, `State`{.interpreted-text
    role="guilabel"}, `Zip Code`{.interpreted-text role="guilabel"}, and
    `Country`{.interpreted-text role="guilabel"}.

    > -   In the `Street`{.interpreted-text role="guilabel"} field,
    >     enter the street name, number, and any additional address
    >     information.
    > -   In the `Street 2`{.interpreted-text role="guilabel"} field,
    >     enter the neighborhood.

-   `Tax ID`{.interpreted-text role="guilabel"}: tax identification
    number.

E-invoicing with SInvoice {#localizations/vietnam/sinvoice}
-------------------------

 is an e-invoice service platform
provided by Viettel, one of the biggest e-invoice service providers in
Vietnam. Odoo supports integration with SInvoice to submit invoices
generated in Odoo.

### Configuration

#### SInvoice platform

To send electronic invoices to SInvoice, the following must be created
on :

-   `SInvoice account <localizations/vietname/sinvoice-registration>`{.interpreted-text
    role="ref"}
-   `Invoice template <localizations/vietname/sinvoice-template>`{.interpreted-text
    role="ref"}
-   `Invoice symbol <localizations/vietname/sinvoice-symbol>`{.interpreted-text
    role="ref"}
-   `Invoice issuance notice <localizations/vietname/sinvoice-notice>`{.interpreted-text
    role="ref"}

##### SInvoice registration {#localizations/vietname/sinvoice-registration}

To create an account, go to  and
register for the desired plan. Fill in the form that opens to be
contacted by  to create an account.

Once you have an account, log into 
using your `Username`{.interpreted-text role="guilabel"} and
`Password`{.interpreted-text role="guilabel"}.

##### Invoice template creation {#localizations/vietname/sinvoice-template}

1.  On the left side of the overview page, in the
    `Release management`{.interpreted-text role="guilabel"} menu, click
    `Create business information`{.interpreted-text role="guilabel"}.

2.  In the `Update key information`{.interpreted-text role="guilabel"}
    step, fill in the following fields and other optional information if
    needed: `Unit name`{.interpreted-text role="guilabel"},
    `Address`{.interpreted-text role="guilabel"},
    `Contact person`{.interpreted-text role="guilabel"},
    `Type of representative documents`{.interpreted-text
    role="guilabel"}.

3.  Click `Update`{.interpreted-text role="guilabel"}.

4.  In the `Look up digital certificate`{.interpreted-text
    role="guilabel"} step, click `Add new`{.interpreted-text
    role="guilabel"} to add a digital certificate.

5.  Select the `Branch/Enterprise`{.interpreted-text role="guilabel"}
    and the `Type of digital certificate`{.interpreted-text
    role="guilabel"}, then fill in the required fields for each type:

    > -   `Supplier`{.interpreted-text role="guilabel"}: CloudCA
    > -   `Signer ID`{.interpreted-text role="guilabel"}: CloudCA
    > -   `Digital Certificate`{.interpreted-text role="guilabel"}:
    >     CloudCA
    > -   `How to download file`{.interpreted-text role="guilabel"}: HSM
    > -   `File Upload`{.interpreted-text role="guilabel"}: HSM,
    >     USB-TOKEN

6.  Click `Generate key pair`{.interpreted-text role="guilabel"} to
    generate encryption keys for authentication, and
    `Save`{.interpreted-text role="guilabel"}.

7.  In the `Manage invoice templates`{.interpreted-text role="guilabel"}
    step, add a new `Invoice template`{.interpreted-text
    role="guilabel"}.

8.  Select the `Invoice type`{.interpreted-text role="guilabel"} and
    fill in the `Invoice template code`{.interpreted-text
    role="guilabel"}, `Invoice template name`{.interpreted-text
    role="guilabel"}, and other optional information if needed.

9.  Click `Update`{.interpreted-text role="guilabel"}.

::: {.seealso}
[SInvoice documentation on electronic invoice template
creation](https://www.sinvoice.vn/2021/02/hdsd-tai-lieu-nghiep-vu-tao-mau-hoa-don-dien-tu.html?debug=1)
:::

##### Invoice symbol creation {#localizations/vietname/sinvoice-symbol}

On the left side of the main screen, in the
`Release management`{.interpreted-text role="guilabel"} menu, click
`Invoice symbol`{.interpreted-text role="guilabel"} and follow these
steps:

1.  Click `Add new`{.interpreted-text role="guilabel"} and select the
    `Invoice template`{.interpreted-text role="guilabel"}.
2.  Set the `Status`{.interpreted-text role="guilabel"} to
    `Active`{.interpreted-text role="guilabel"} to activate the symbol
    and fill in the `Invoice symbol`{.interpreted-text role="guilabel"}.
3.  Enable `Stop automatic sending to tax authorities`{.interpreted-text
    role="guilabel"} and `Default for built-in
    API`{.interpreted-text role="guilabel"} based on preference.
4.  Click `Save`{.interpreted-text role="guilabel"}.

##### Invoice issuance notice {#localizations/vietname/sinvoice-notice}

On the left side of the main screen, in the
`Release management`{.interpreted-text role="guilabel"} menu, click
`Create issuance notice`{.interpreted-text role="guilabel"} and follow
these steps:

1.  Click `Add new`{.interpreted-text role="guilabel"}, select the
    `Name of the business unit to issue an e-invoice`{.interpreted-text
    role="guilabel"} and the `Tax agency name`{.interpreted-text
    role="guilabel"}. Based on the business unit and tax agency
    selected, the `Tax code`{.interpreted-text role="guilabel"},
    `Address`{.interpreted-text role="guilabel"},
    `Phone number`{.interpreted-text role="guilabel"}, and `Separator
    used`{.interpreted-text role="guilabel"} are automatically filled
    and uneditable.
2.  Click `Select the invoice type for issuance`{.interpreted-text
    role="guilabel"}, and then select and fill in the following
    information :
    -   `Invoice type`{.interpreted-text role="guilabel"}: The invoice
        type on which to declare an issuance notice.
    -   `Invoice template`{.interpreted-text role="guilabel"}: Select
        from the list of templates available based on the invoice type.
    -   `Symbol`{.interpreted-text role="guilabel"}: Select from the
        list of symbols available based on the invoice type.
    -   `Quantity`{.interpreted-text role="guilabel"}: Total number of
        invoices to issue for the selected type. Based on the type and
        template selected, this field is filled in automatically. It can
        be changed if needed.
    -   `Start date of use`{.interpreted-text role="guilabel"}: The date
        from which the invoice template, range, and quantity are used
        for the issuance notice.
3.  Click `Save`{.interpreted-text role="guilabel"} and select more
    invoice types if necessary by repeating the steps above. Click
    `Save`{.interpreted-text role="guilabel"} to finish drafting the
    notice.
4.  Click `Send to tax authorities`{.interpreted-text role="guilabel"}
    for approval. Once approved, the notice\'s
    `Status`{.interpreted-text role="guilabel"} is changed to
    `Active`{.interpreted-text role="guilabel"}.

#### Odoo database {#localizations/vietnam/sinvoice-odoo}

##### Link Odoo to SInvoice

To connect Odoo with SInvoice, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Vietnamese Integration`{.interpreted-text
role="guilabel"} section, fill in your SInvoice
`Username`{.interpreted-text role="guilabel"} and
`Password`{.interpreted-text role="guilabel"}. Add a
`Default symbol`{.interpreted-text role="guilabel"} to generate a prefix
for the invoice number managed in SInvoice if needed.

##### Invoice template

To create SInvoice templates, go to
`Accounting --> Configuration --> Templates`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"}
and add a `Template code`{.interpreted-text role="guilabel"} and a
`Template Invoice Type`{.interpreted-text role="guilabel"}. The
`Template code`{.interpreted-text role="guilabel"} is the initial
sequence of digits in the name assigned by SInvoice. For example, if the
invoice template is [1/001 - Hóa đơn GTGT - ND123]{.title-ref}, the
`Template
code`{.interpreted-text role="guilabel"} is [1/001]{.title-ref}. The
SInvoice templates in Odoo must match the ones in SInvoice.

To add `Invoice Symbols`{.interpreted-text role="guilabel"}, click
`Add a new line`{.interpreted-text role="guilabel"}.

### Sending invoices to SInvoice

Invoices can be sent to SInvoice once they have been confirmed. To do
so, follow the
`invoice sending <accounting/invoice/sending>`{.interpreted-text
role="ref"} steps. In the `Send`{.interpreted-text role="guilabel"}
popup, enable `Send to SInvoice`{.interpreted-text role="guilabel"} and
click `Send & Print`{.interpreted-text role="guilabel"}.

Once the invoice has been successfully submitted to SInvoice, the
`SInvoice Status`{.interpreted-text role="guilabel"} field in the
`SInvoice`{.interpreted-text role="guilabel"} tab of the invoice is
updated to `Sent`{.interpreted-text role="guilabel"}. The
`SInvoice Number`{.interpreted-text role="guilabel"},
`Issue Date`{.interpreted-text role="guilabel"},
`Secret Code`{.interpreted-text role="guilabel"} and `eInvoice
Number`{.interpreted-text role="guilabel"} fields are also updated. The
same information is available on SInvoice.

#### Replacement or adjustment invoices

A replacement invoice is issued to correct an invoice that has **yet to
be tax declared**, whereas an adjustment invoice is issued to correct
one that has **already been tax declared**. Follow these steps to issue
a replacement or adjustment invoice:

1.  Open the invoice and click `Credit Note`{.interpreted-text
    role="guilabel"}.
2.  In the `Credit Note`{.interpreted-text role="guilabel"} popup, fill
    in the following fields:
    -   `Reason displayed on Credit Note`{.interpreted-text
        role="guilabel"}
    -   `Adjustment type`{.interpreted-text role="guilabel"}
    -   `Agreement Name`{.interpreted-text role="guilabel"}
    -   `Agreement Date`{.interpreted-text role="guilabel"}
    -   `Journal`{.interpreted-text role="guilabel"}
    -   `Reversal date`{.interpreted-text role="guilabel"}
3.  Click `Reverse and Create Invoice`{.interpreted-text
    role="guilabel"} to issue a replacement invoice, or
    `Reverse`{.interpreted-text role="guilabel"} to issue an adjustment
    invoice.

The `SInvoice Status`{.interpreted-text role="guilabel"} in the
`SInvoice`{.interpreted-text role="guilabel"} invoice tab is updated to
`Replaced`{.interpreted-text role="guilabel"} for a replacement invoice
or `Adjusted`{.interpreted-text role="guilabel"} for an adjustment
invoice.

#### Invoice cancellation

If an invoice needs to be canceled, open the invoice and click
`Request Cancel`{.interpreted-text role="guilabel"}. In the
`Invoice Cancellation`{.interpreted-text role="guilabel"} popup, enter
the cancellation `Reason`{.interpreted-text role="guilabel"},
`Agreement Name`{.interpreted-text role="guilabel"}, and
`Agreement Date`{.interpreted-text role="guilabel"}, and click `Request
Cancellation`{.interpreted-text role="guilabel"}.

The `SInvoice Status`{.interpreted-text role="guilabel"} in the
`SInvoice`{.interpreted-text role="guilabel"} invoice tab is updated to
`Canceled`{.interpreted-text role="guilabel"}.

QR banking codes {#localizations/vietnam/qrcode}
----------------

Vietnamese QR banking is a payment service platform that allows
customers to make instant domestic payments to individuals and merchants
in Vietnamese dong via online and mobile banking.

### Configuration

To activate QR banking codes, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and enable `QR Codes`{.interpreted-text
role="guilabel"} in the `Customer Payments`{.interpreted-text
role="guilabel"} section.

#### Bank account

To activate QR banking for a bank account, go to
`Contacts --> Configuration -->
Bank Accounts`{.interpreted-text role="menuselection"} and select the
bank account. Fill in the `Bank Identifier Code`{.interpreted-text
role="guilabel"}, `Proxy Type`{.interpreted-text role="guilabel"} (based
on the information used to identify the
`Merchant Account`{.interpreted-text role="guilabel"}, such as the card
number and bank account numbers), and `Proxy Value`{.interpreted-text
role="guilabel"} fields.

Enable `Include Reference`{.interpreted-text role="guilabel"} to include
the invoice number in the QR code.

::: {.important}
::: {.title}
Important
:::

\- The account holder\'s country must be set to [Vietnam]{.title-ref},
and their city must be specified on the contact form. - The
`account number <accounting/bank/account-number>`{.interpreted-text
role="ref"} and bank must be set on the `Bank`{.interpreted-text
role="guilabel"} journal.
:::

::: {.seealso}
`../accounting/bank`{.interpreted-text role="doc"}
:::

### Generating QR codes on invoices

When creating a new invoice, open the `Other Info`{.interpreted-text
role="guilabel"} tab and select `EMV
Merchant-Presented QR-code`{.interpreted-text role="guilabel"} in the
`Payment QR-code`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

Ensure the `Recipient Bank`{.interpreted-text role="guilabel"} is
configured, as Odoo uses this field to generate QR codes.
:::
