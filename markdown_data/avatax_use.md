# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/avatax/avatax_use.md

AvaTax use
==========

AvaTax is a tax calculation software that can be integrated with Odoo in
the United States and Canada. Once the
`integration setup <../avatax>`{.interpreted-text role="doc"} is
complete, the calculated tax is simple and automatic.

Tax calculation
---------------

Automatically calculate taxes on Odoo quotations and invoices with
AvaTax by confirming the documents during the sales flow. Alternatively,
calculate the taxes manually by clicking the
`Compute Taxes`{.interpreted-text role="guilabel"} button, while these
documents are in draft stage.

::: {.tip}
::: {.title}
Tip
:::

Clicking the `Compute Taxes`{.interpreted-text role="guilabel"} button
recalculates taxes, if any product lines are edited on the invoice.
:::

{.align-center}

The tax calculation is triggered during the following `automatic trigger
<avatax/automatic-triggers>`{.interpreted-text role="ref"} and
`manual trigger <avatax/manual-triggers>`{.interpreted-text role="ref"}
circumstances.

### Automatic triggers {#avatax/automatic-triggers}

-   When the sales rep sends the quote by email with
    `Send by email`{.interpreted-text role="guilabel"} button (pop-up).
-   When the customer views the online quote on the portal.
-   When a quote is confirmed and becomes a sales order.
-   When the customer views the invoice on the portal.
-   When a draft invoice is validated.
-   When the customer views the subscription in the portal.
-   When a subscription generates an invoice.
-   When the customer gets to the last screen of the eCommerce checkout.

### Manual triggers {#avatax/manual-triggers}

-   `Compute Taxes`{.interpreted-text role="guilabel"} button at the
    bottom of the quote.
-   `Compute Taxes`{.interpreted-text role="guilabel"} button at the top
    of the invoice.

Use each of these buttons to manually re-calculate the sales tax.

::: {.tip}
::: {.title}
Tip
:::

Use the `Avalara Partner Code`{.interpreted-text role="guilabel"} field
that is available on customer records, quotations, and invoices to
cross-reference data in Odoo and AvaTax. This field is located under the
`Other info`{.interpreted-text role="menuselection"} tab of the sales
order or quotation in the `Sales`{.interpreted-text role="guilabel"}
section.

On the customer record, navigate to *Contacts app* and select a contact.
Then open the `Sales & Purchase`{.interpreted-text role="guilabel"} tab
and the `Avalara Partner Code`{.interpreted-text role="guilabel"} under
the `Sales`{.interpreted-text role="guilabel"} section.
:::

::: {.important}
::: {.title}
Important
:::

The `Automatic Tax Mapping (AvaTax)`{.interpreted-text role="guilabel"}
fiscal position is also applied on those Odoo documents, like
subscriptions.
:::

::: {.seealso}
\- `../fiscal_positions`{.interpreted-text role="doc"}
:::

AvaTax synchronization
----------------------

Synchronization occurs with AvaTax, when the *invoice* is created in
Odoo. This means the sales tax is recorded with Avalara (AvaTax software
developer).

To do so, navigate to
`Sales app --> Orders --> Quotations`{.interpreted-text
role="menuselection"}. Select a quotation from the list.

After confirming a quotation and validating the delivery, click
`Create Invoice`{.interpreted-text role="guilabel"}. Indicate whether it
is a `Regular invoice`{.interpreted-text role="guilabel"},
`Down payment (percentage)`{.interpreted-text role="guilabel"}, or
`Down payment (fixed amount)`{.interpreted-text role="guilabel"}.

Then click `Create and view invoice`{.interpreted-text role="guilabel"}.
The recorded taxes can be seen in the `Journal Items`{.interpreted-text
role="guilabel"} tab of the invoice. There will be different taxes
depending on the location of the `Delivery Address`{.interpreted-text
role="guilabel"}.

{.align-center}

Finally, press the `Confirm`{.interpreted-text role="guilabel"} button
to complete the invoice and synchronize with the AvaTax portal.

::: {.warning}
::: {.title}
Warning
:::

An invoice cannot be `Reset to draft`{.interpreted-text role="guilabel"}
because this causes de-synchronization with the AvaTax Portal. Instead,
click `Add credit note`{.interpreted-text role="guilabel"} and state:
[Sync with AvaTax Portal]{.title-ref}. See this documentation:
`../../../accounting/customer_invoices/credit_notes`{.interpreted-text
role="doc"}.
:::

Fixed price discounts
---------------------

Add a fixed price discount to a valuable customer, by clicking
`Add a line`{.interpreted-text role="guilabel"} on the customer\'s
invoice. Add the product discount, and set the `Price`{.interpreted-text
role="guilabel"} to either a positive or negative value. To recalculate
the taxes, click `Compute Taxes`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Tax calculation can even be done on negative subtotals and credit notes.
:::

Logging
-------

It is possible to log Avalara/*AvaTax* actions in Odoo for further
analysis, or verification of functionality. Logging is accessible
through the *AvaTax* settings.

To start logging *AvaTax* actions, first, navigate to the
`Accounting app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.

Then, in the `Taxes`{.interpreted-text role="guilabel"} section, under
the `AvaTax`{.interpreted-text role="guilabel"} settings, click
`Start logging for 30 minutes`{.interpreted-text role="guilabel"}.

Upon starting the log process, Odoo will log all Avalara/*AvaTax*
actions performed in the database.

To view the logs, click on `Show logs`{.interpreted-text
role="guilabel"} to the right of the `Start logging for 30
minutes`{.interpreted-text role="guilabel"}. This reveals a detailed
list of Avalara/*AvaTax* actions. This list is sortable by the following
columns:

-   `Created on`{.interpreted-text role="guilabel"}: timestamp of the
    *AvaTax* calculation.
-   `Created by`{.interpreted-text role="guilabel"}: numeric value of
    the user in the database.
-   `Database name`{.interpreted-text role="guilabel"}: name of the
    database.
-   `Type`{.interpreted-text role="guilabel"}: two values can be chosen
    for this field, `Server`{.interpreted-text role="guilabel"} or
    `Client`{.interpreted-text role="guilabel"}.
-   `Name`{.interpreted-text role="guilabel"}: Avalara service name. In
    this case, it will be *AvaTax*.
-   `Level`{.interpreted-text role="guilabel"}: by default, this will be
    [INFO]{.title-ref}.
-   `Path`{.interpreted-text role="guilabel"}: indicates the path taken
    to make the calculation.
-   `Line`{.interpreted-text role="guilabel"}: indicates the line the
    calculation is made on.
-   `Function`{.interpreted-text role="guilabel"}: indicates the
    calculation taken on the line.

{.align-center}

Click into the log line to reveal another field, called
`Message`{.interpreted-text role="guilabel"}.

This field populates a raw transcription of the transaction, which
involves the creation (or adjustment) of a sales invoice using the
Avalara *AvaTax* API.

The transaction includes details, such as addresses for shipping from
and to, line items describing the products or services, tax codes, tax
amounts, and other relevant information.

The `Message`{.interpreted-text role="guilabel"} contains the calculated
taxes for different jurisdictions and confirms the creation (or
adjustment) of the transaction.

::: {.tip}
::: {.title}
Tip
:::

Custom fields can be made using Odoo *Studio*. Click the
`fa-ellipsis-v`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} menu to the far-right of
the header row. Then click `fa-plus`{.interpreted-text role="icon"}
`Add custom field`{.interpreted-text role="guilabel"}. This action opens
Odoo *Studio*.
:::

::: {.important}
::: {.title}
Important
:::

Odoo *Studio* requires a *custom* pricing plan. Consult the database\'s
customer success manager for more information on switching plans. Or to
see if Odoo *Studio* is included in the database\'s current pricing
plan. See this documentation: `../../../../studio`{.interpreted-text
role="doc"}.
:::

::: {.seealso}
\- `../avatax`{.interpreted-text role="doc"} -
`avalara_portal`{.interpreted-text role="doc"} - [US Tax Compliance:
Avatax elearning
video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)
- `../fiscal_positions`{.interpreted-text role="doc"}
:::
