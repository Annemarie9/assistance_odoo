# File: /content/odoo_doc17.0/fr/content/applications/finance/fiscal_localizations/uruguay.md

Uruguay
=======

Introduction {#uruguay/intro}
------------

With the Uruguayan localization, you can generate electronic documents
with its XML, fiscal folio, electronic signature and connection to tax
authority Dirección General Impositiva (DGI) through Uruware.

The supported documents are:

-   `e-Invoice`{.interpreted-text role="guilabel"},
    `e-Invoice Credit Note`{.interpreted-text role="guilabel"},
    `e-Invoice Debit Note`{.interpreted-text role="guilabel"};
-   `e-Ticket`{.interpreted-text role="guilabel"},
    `e-Ticket Credit Note`{.interpreted-text role="guilabel"},
    `e-Ticket Debit Note`{.interpreted-text role="guilabel"};
-   `Export e-Invoice`{.interpreted-text role="guilabel"},
    `Export e-Invoice Credit Note`{.interpreted-text role="guilabel"},
    `Export
    e-Invoice Debit Note`{.interpreted-text role="guilabel"}.

The localization requires an Uruware account, which enables users to
generate electronic documents within Odoo.

### Glossary

The following terms are used throughout the Uruguayan localization:

-   **DGI**: *Dirección General Impositiva* is the government entity
    responsible for enforcing tax payments in Uruguay.
-   **EDI**: *Electronic Data Interchange* refers to the sending of
    electronic documents.
-   **Uruware**: is the third-party organization that facilitates the
    interchange of electronic documents between companies and the
    Uruguayan government.
-   **CAE**: *Constancia de Autorización de Emisión* is a document
    requested from the tax authority\'s website to enable electronic
    invoice issuance.

Configuration
-------------

### Modules installation

`Install <general/install>`{.interpreted-text role="ref"} the following
modules to get all the features of the Uruguayan localization:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                         Technical name                Description
  -------------------------------------------- ----------------------------- --------------------------------------------------------------------------------------------------
  `Uruguay - Accounting`{.interpreted-text     [l10n\_uy]{.title-ref}        The default `fiscal localization package <../fiscal_localizations>`{.interpreted-text role="doc"}.
  role="guilabel"}                                                           It adds accounting characteristics for the Uruguayan localization, which represent the minimum
                                                                             configuration required for a company to operate in Uruguay according to the guidelines set by the
                                                                             `DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}. The module\'s installation
                                                                             automatically loads: chart of accounts, taxes, documents types, and tax supported types.

  `Uruguay Accounting EDI`{.interpreted-text   [l10n\_uy\_edi]{.title-ref}   Includes all the technical and functional requirements to generate and validate
  role="guilabel"}                                                           `Electronics Documents <../accounting/customer_invoices/electronic_invoicing>`{.interpreted-text
                                                                             role="doc"}, based on the technical documentation published by the
                                                                             `DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}. The authorized documents are
                                                                             `listed
                                                                             above <uruguay/intro>`{.interpreted-text role="ref"}.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

::: {.note}
::: {.title}
Note
:::

Odoo automatically installs the base module **Uruguay - Accounting**
when a database is installed with [Uruguay]{.title-ref} selected as the
country. However, to enable electronic invoicing, the **Uruguay
Accounting EDI** ([l10n\_uy\_edi]{.title-ref}) module needs to be
manually `installed <general/install>`{.interpreted-text role="ref"}.
:::

### Company

To configure your company information, open the **Settings** app, scroll
down to the `Companies`{.interpreted-text role="guilabel"} section,
click `Update Info`{.interpreted-text role="guilabel"}, and configure
the following:

-   `Company Name`{.interpreted-text role="guilabel"}

-   `Address`{.interpreted-text role="guilabel"}, including the
    `Street`{.interpreted-text role="guilabel"},
    `City`{.interpreted-text role="guilabel"}, `State`{.interpreted-text
    role="guilabel"}, `ZIP`{.interpreted-text role="guilabel"}, and
    `Country`{.interpreted-text role="guilabel"}

-   `Tax ID`{.interpreted-text role="guilabel"}: enter the
    identification number for the selected taxpayer type.

-   `DGI Main Branch Code`{.interpreted-text role="guilabel"}: this is
    part of the XML when creating an electronic document. If this field
    is not set, all electronic documents will be rejected.

    To find the `DGI Main Branch Code`{.interpreted-text
    role="guilabel"}, follow these steps:

    1.  From your [DGI
        account](https://servicios.dgi.gub.uy/serviciosenlinea), go to
        `Servicios en línea DGI --> Registro único tributario --> Consulta de datos`{.interpreted-text
        role="menuselection"}.
    2.  Select
        `Consulta de Datos Registrales --> Consulta de Datos de Entidades`{.interpreted-text
        role="menuselection"}.
    3.  Open the generated PDF to get the *DGI Main Branch Code* from
        the `Domicilio Fiscal
        Número de Local`{.interpreted-text role="guilabel"} section.

After configuring the company in the database settings, navigate to
`Contacts`{.interpreted-text role="menuselection"} and search for your
company to verify the following:

-   the company type is set to `Company`{.interpreted-text
    role="guilabel"}.
-   the `Identification Number`{.interpreted-text role="guilabel"}
    `Type`{.interpreted-text role="guilabel"} is
    `RUT / RUC`{.interpreted-text role="guilabel"}.

### Set up a Uruware account {#l10n_uy/uruware-account}

To set up a Uruware account, follow these steps:

1.  Verify that you have a valid Odoo subscription.
2.  Locate the Uruware credentials settings by navigating to the
    `Accounting -->
    Configuration --> Settings`{.interpreted-text role="menuselection"}.
3.  Scroll down to the `Uruguayan Localization`{.interpreted-text
    role="guilabel"} section and select the environment
    (`Production`{.interpreted-text role="guilabel"} or
    `Testing`{.interpreted-text role="guilabel"}).
4.  Click on `Create Uruware Account`{.interpreted-text
    role="guilabel"}.

Upon doing so, an email is sent to the address associated with your Odoo
subscription with the password to enter Uruware\'s portal and set up
your account.

::: {.tip}
::: {.title}
Tip
:::

\- The email with the credentials is not immediate; it might take up to
48 hours for the account to be created. - The company\'s
`Tax ID`{.interpreted-text role="guilabel"} needs to be set up to be
able to create an Uruware account. - The password sent expires after 24
hours. In this case, reset it by using the *Forgot Password* link in
Uruware\'s portal.
:::

::: {.note}
::: {.title}
Note
:::

This action will create an account with Uruware with the following
information:

-   Legal name (razón social)
-   RUT from the company
-   Username (the Odoo subscription email or [RUT]{.title-ref}.odoo. For
    example: [213344556677.odoo]{.title-ref})
-   Odoo database link

To ensure your account is created correctly, please add any missing
information from above.
:::

Once the account is created and you have received the email containing
the credentials, configure your accounts directly in the Uruware
 or [production
portal](https://prod6109.ucfe.com.uy/Gestion/):

Use the account credentials in the email to log in to the to the
corresponding ( or
) portal.

In Uruware\'s portal, the following steps are needed to be able to issue
invoices from Odoo:

1.  Complete and correct the company\'s information.
2.  Add your digital certificate.
3.  Add your
    `CAEs (Constancia de Autorización para Emisión)`{.interpreted-text
    role="abbr"} for each document-type you plan to issue.
4.  Configure the format of the PDF to be printed and sent to your
    customers.

::: {.important}
::: {.title}
Important
:::

Be sure to configure two accounts, one for testing and one for
production. The certificate is needed in both environments, but
`CAEs (Constancia de Autorización para Emisión)`{.interpreted-text
role="abbr"} are only needed in production.
:::

::: {.seealso}
\- [Odoo Tutorials: Uruguay
Localization](https://www.odoo.com/slides/smart-tutorial-localizacion-de-uruguay-432)
- [Odoo Help Forum:
Uruguay](https://www.odoo.com/forum/help-1?search=l10n_uy)
:::

### Electronic invoice data

To configure the electronic invoice data, an environment and credentials
need to be configured. To do so, navigate to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and scroll down to the
`Uruguayan Localization`{.interpreted-text role="guilabel"} section.

First, select the `UCFE Web Services`{.interpreted-text role="guilabel"}
environment:

-   `Production`{.interpreted-text role="guilabel"}: for production
    databases. In this mode, electronic documents are sent to
    `DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}
    through Uruware for their validation.
-   `Testing`{.interpreted-text role="guilabel"}: for test databases. In
    this mode, the direct connection flows can be tested, with the files
    sent to the `DGI (Dirección General Impositiva)`{.interpreted-text
    role="abbr"} testing environment through Uruware.
-   `Demo`{.interpreted-text role="guilabel"}: files are created and
    accepted automatically in demo mode but are **not** sent to the
    `DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}.
    For this reason, rejection errors will not appear in this mode.
    Every internal validation can be tested in demo mode. Avoid
    selecting this option in a production database.

::: {.note}
::: {.title}
Note
:::

Using `Demo`{.interpreted-text role="guilabel"} mode does not require a
Uruware account.
:::

Then, enter the `Uruware Data`{.interpreted-text role="guilabel"}:

-   `Uruware WS Password`{.interpreted-text role="guilabel"}
-   `Commerce Code`{.interpreted-text role="guilabel"}
-   `Terminal Code`{.interpreted-text role="guilabel"}



::: {.note}
::: {.title}
Note
:::

This data can be obtained from the Uruware portal after configuring the
`Uruware account
<l10n_uy/uruware-account>`{.interpreted-text role="ref"}.

To get the `Uruware WS Password`{.interpreted-text role="guilabel"}, go
to `Configuration --> Company -->
Edit`{.interpreted-text role="menuselection"} and look for the
`Validators and Additional Information`{.interpreted-text
role="guilabel"} tab to find `WS Password`{.interpreted-text
role="guilabel"}.

To get the `Commerce Code`{.interpreted-text role="guilabel"}, go to
`Configuration --> Branches`{.interpreted-text role="menuselection"}.

To get the `Terminal Code`{.interpreted-text role="guilabel"}, go to
`Configuration --> Issuing Points`{.interpreted-text
role="menuselection"}.
:::

### Master data

#### Chart of accounts

The
`chart of accounts <../accounting/get_started/chart_of_accounts>`{.interpreted-text
role="doc"} is installed by default as part of the set of data included
in the localization module, the accounts are mapped automatically in
taxes, default accounts payable, and default accounts receivable.

Accounts can be added or deleted according to the company\'s needs.

::: {.seealso}
`../accounting/get_started/chart_of_accounts`{.interpreted-text
role="doc"}
:::

#### Contacts

To create a contact, navigate to `Contacts app`{.interpreted-text
role="menuselection"} and select `New`{.interpreted-text
role="guilabel"}. Then enter the following information:

-   `Company Name`{.interpreted-text role="guilabel"}
-   `Address`{.interpreted-text role="guilabel"}:
    -   `Street`{.interpreted-text role="guilabel"}: required to confirm
        an electronic invoice.
    -   `City`{.interpreted-text role="guilabel"}
    -   `State`{.interpreted-text role="guilabel"}
    -   `ZIP`{.interpreted-text role="guilabel"}
    -   `Country`{.interpreted-text role="guilabel"}: required to
        confirm an electronic invoice.
-   `Identification Number`{.interpreted-text role="guilabel"}:
    -   `Type`{.interpreted-text role="guilabel"}: select a
        identification type.
    -   `Number`{.interpreted-text role="guilabel"}: required to confirm
        an electronic invoice.

#### Taxes

As part of the Uruguay localization module, taxes are automatically
created with its configuration and related financial accounts.



#### Document types

Some accounting transactions, like *customer invoices* and *vendor
bills* are classified by document types. These are defined by the
government fiscal authorities, in this case by the
`DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}.

Each document type can have a unique sequence per journal where it is
assigned. The data is created automatically when the localization module
is installed, and the information required for the document types is
included by default.

To review the document types included in the localization, navigate to
`Accounting
--> Configuration --> Document Types`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

In Uruguay,
`CAEs (Constancia de Autorización de Emisión)`{.interpreted-text
role="abbr"} **must** be uploaded in Uruware. Sequences (and PDFs) are
received in Odoo from Uruware, based on their
`CAEs (Constancia de Autorización de Emisión)`{.interpreted-text
role="abbr"}.
`CAEs (Constancia de Autorización de Emisión)`{.interpreted-text
role="abbr"} are **only** used in production. When testing, only a range
of sequences used in Uruware need to be set.
:::



#### Sales journals

To generate and confirm an electronic document that will be validated by
`DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}, the
sales journal needs to be configured with the following:

-   `Invoicing Type`{.interpreted-text role="guilabel"}: by default
    `Electronic`{.interpreted-text role="guilabel"} option is set. This
    is necessary to send electronic documents via web service to the
    Uruguayan government through Uruware. The other option,
    `Manual`{.interpreted-text role="guilabel"}, is for open invoices
    previously stamped in another system, for example, in the
    `DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"}.
-   `Use Documents?`{.interpreted-text role="guilabel"}: Activate this
    option if this journal will use documents from the list of document
    types in Odoo.

Workflows
---------

Once you have configured your database, you can create your documents.

### Sales documents

#### Customer invoices

`Customer invoices <../accounting/customer_invoices>`{.interpreted-text
role="doc"} are electronic documents that, when validated, are sent to
`DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"} via
Uruware. These documents can be created from your sales order or
manually. They must contain the following data:

-   `Customer`{.interpreted-text role="guilabel"}: type the customer\'s
    information.
-   `Due date`{.interpreted-text role="guilabel"}: to compute if the
    invoice is due now or later (*contado* or *crédito*, respectively).
-   `Journal`{.interpreted-text role="guilabel"}: select the electronic
    sales journal.
-   `Document Type`{.interpreted-text role="guilabel"}: document type in
    this format, for example, [(111) e-Invoice]{.title-ref}.
-   `Products`{.interpreted-text role="guilabel"}: specify the
    product(s) with the correct taxes.

::: {.note}
::: {.title}
Note
:::

Every document type has a specific credit note and debit note (e.g., the
document type `(111) e-Invoice`{.interpreted-text role="guilabel"} has
an `(112) e-Invoice Credit Note`{.interpreted-text role="guilabel"}).
:::

#### Customer credit note

The
`Customer credit note <../accounting/customer_invoices/credit_notes>`{.interpreted-text
role="doc"} is an electronic document that, when validated, is sent to
`DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"} via
Uruware. It is necessary to have a validated (posted) invoice to
register a credit note. On the invoice, click the
`Credit note`{.interpreted-text role="guilabel"} button to access the
`Create credit note`{.interpreted-text role="guilabel"} form, then
complete the following information:

-   `Reason`{.interpreted-text role="guilabel"}: type the reason for the
    credit note.
-   `Journal`{.interpreted-text role="guilabel"}: select the journal
    that has to be electronic and has the `Use
    Documents?`{.interpreted-text role="guilabel"} option active.
-   `Document Type`{.interpreted-text role="guilabel"}: select the
    credit note document type.
-   `Reversal Date`{.interpreted-text role="guilabel"}: type the date.

#### Customer debit note

The
`Customer debit note <../accounting/customer_invoices/credit_notes>`{.interpreted-text
role="doc"} is an electronic document that, when validated, is sent to
`DGI (Dirección General Impositiva)`{.interpreted-text role="abbr"} via
Uruware. It is necessary to have a validated (posted) invoice to
register a debit note. On the invoice, click the
`fa-cog`{.interpreted-text role="icon"} (`action menu`{.interpreted-text
role="guilabel"}) icon, select the `Debit note`{.interpreted-text
role="guilabel"} option to access the
`Create credit note`{.interpreted-text role="guilabel"} form, then
complete the following information:

-   `Reason`{.interpreted-text role="guilabel"}: Type the reason for the
    debit note.
-   `Journal`{.interpreted-text role="guilabel"}: Select the journal
    that has to be electronic and has the `Use
    Documents?`{.interpreted-text role="guilabel"} option active.
-   `Copy lines`{.interpreted-text role="guilabel"}: Tick the checkbox
    to copy the invoice lines to the debit note.
-   `Debit note date`{.interpreted-text role="guilabel"}: Type the date.

::: {.note}
::: {.title}
Note
:::

Confirm the invoice to create it with an internal reference. To send the
document to `DGI (Dirección General Impositiva)`{.interpreted-text
role="abbr"} via Uruware, click on `Send and Print`{.interpreted-text
role="guilabel"} and select the checkbox `Create CFE`{.interpreted-text
role="guilabel"}. The legal document sequence (number) is brought from
Uruware once the document has been processed. Make sure you have
`CAEs (Constancia de Autorización de Emisión)`{.interpreted-text
role="abbr"} available in Uruware.
:::

::: {.note}
::: {.title}
Note
:::

The PDF of the validated document is pulled from Uruware following the
specification by the Uruguayan government (DGI).
:::

Addendas and disclosures
------------------------

*Addendas* and *disclosures* are additional notes and comments added to
an electronic document that can be mandatory or optional. To create a
new addenda, go to `Accounting -->
Configuration --> Addendas and disclosures`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text
role="guilabel"}.

Enter the following information:

-   `Name`{.interpreted-text role="guilabel"}: name of the addenda or
    mandatory disclosure.
-   `Type`{.interpreted-text role="guilabel"}: Select the type of
    remark, this will add it to the specific section in the XML.
-   `Is legend`{.interpreted-text role="guilabel"}: Select this box if
    the text is a mandatory disclosure, leave it blank if it is
    additional information.
-   `Content`{.interpreted-text role="guilabel"}: Add the complete text
    of the addenda or disclosure.

### Leyenda and additional information in product

To add a *leyenda* or additional information to the product and XML, it
is necessary to add the preconfigured addenda and disclosure to the
product in the invoice line. Add the *leyenda* in the
`Disclosure`{.interpreted-text role="guilabel"} field of the product
specified in the line.

### Leyenda and additional information

To add a *leyenda* or additional information to the electronic invoice
and XML, access the invoice, go to the `Other Info`{.interpreted-text
role="guilabel"} tab, and select the desired addenda in the `Addenda and
Disclosure`{.interpreted-text role="guilabel"} field. The addenda and
disclosures added here will appear in the XML and visibly in the PDF
document.

This applies to the following types of *addendas*:

-   Document
-   Issuer
-   Receiver
-   Addendas

::: {.note}
::: {.title}
Note
:::

To add a temporary note to the electronic document, use the
`Terms and Conditions`{.interpreted-text role="guilabel"} field. This
information will be sent in the addenda of the invoice, but it won\'t be
saved for future documents.
:::
