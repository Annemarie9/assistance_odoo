# File: /content/odoo_doc17.0/fr/content/applications/finance/payment_providers/authorize.md

Authorize.Net
=============

 is a United States-based
online payment solution provider, allowing businesses to accept **credit
cards**.

Configuration
-------------

::: {.seealso}
\- `payment_providers/add_new`{.interpreted-text role="ref"}
:::

### Credentials tab

Odoo needs your **API Credentials & Keys** to connect with your
Authorize.Net account, which comprise:

-   **API Login ID**: The ID solely used to identify the account with
    Authorize.Net.
-   **API Transaction Key**
-   **API Signature Key**
-   **API Client Key**

To retrieve them, log into your Authorize.Net account, go to
`Account --> Settings
--> Security Settings --> API Credentials & Keys`{.interpreted-text
role="menuselection"}, generate your **Transaction Key** and **Signature
Key**, and paste them on the related fields in Odoo. Then, click on
**Generate Client Key**.

::: {.important}
::: {.title}
Important
:::

To test Authorize.Net with a *sandbox* account, change the
`State`{.interpreted-text role="guilabel"} to `Test
Mode`{.interpreted-text role="guilabel"}. We recommend doing this on a
test Odoo database, rather than on your main database.

If you use the `Test Mode`{.interpreted-text role="guilabel"} with a
regular account, it results in the following error: *The merchant login
ID or password is invalid or the account is inactive*.
:::

### Configuration tab

#### Place a hold on a card

With Authorize.Net, you can enable the `manual capture
<payment_providers/manual_capture>`{.interpreted-text role="ref"}. If
enabled, the funds are reserved for 30 days on the customer\'s card, but
not charged yet.

::: {.warning}
::: {.title}
Warning
:::

After **30 days**, the transaction is **voided automatically** by
Authorize.Net.
:::

::: {.seealso}
\- `../payment_providers`{.interpreted-text role="doc"}
:::

ACH payments (USA only) {#authorize/ach_payments}
-----------------------

`ACH (automated clearing house)`{.interpreted-text role="abbr"} is an
electronic funds transfer system used between bank accounts in the
United States.

### Configuration

To give customers the possibility to pay using ACH, [sign up for
Authorize.Net eCheck\'s
service](https://www.authorize.net/payments/echeck.html). Once eCheck is
activated, duplicate the previously configured Authorize.Net payment
provider on Odoo by going to `Accounting
--> Configuration --> Payment Providers --> Authorize.net`{.interpreted-text
role="menuselection"}. Then, click the cog icon (`⛭`{.interpreted-text
role="guilabel"}) and select `Duplicate`{.interpreted-text
role="guilabel"}. Change the provider\'s name to differentiate both
versions (e.g., [Authorize.net - Banks]{.title-ref}).

When ready, change the provider\'s `State`{.interpreted-text
role="guilabel"} to `Enabled`{.interpreted-text role="guilabel"} for a
regular account or `Test Mode`{.interpreted-text role="guilabel"} for a
sandbox account.

Import an Authorize.Net statement
---------------------------------

### Export from Authorize.Net {#authorize-import-template}

::: {.admonition}
Template

`Download the Excel import template. <authorize/authorize-net-magic-sheet.xlsx>`{.interpreted-text
role="download"}
:::

-   Log in to Authorize.Net.
-   Go to
    `Account --> Statements --> eCheck.Net Settlement Statement`{.interpreted-text
    role="menuselection"}.
-   Define an export range using an *opening* and *closing* batch
    settlement. All transactions within the two batch settlements will
    be exported to Odoo.
-   Select all transactions within the desired range, copy them, and
    paste them into the `Report 1 Download`{.interpreted-text
    role="guilabel"} sheet of the `Excel import template
    <authorize-import-template>`{.interpreted-text role="ref"}.



::: {.example}
{.align-center}

In this case, the first batch (01/01/2021) of the year belongs to the
settlement of 12/31/2020, so the **opening** settlement is from
12/31/2020.
:::

Once the data is in the `Report 1 Download`{.interpreted-text
role="guilabel"} sheet:

-   Go to the `Transaction Search`{.interpreted-text role="guilabel"}
    tab on Authorize.Net.
-   Under the `Settlement Date`{.interpreted-text role="guilabel"}
    section, select the previously used range of batch settlement dates
    in the `From:`{.interpreted-text role="guilabel"} and
    `To:`{.interpreted-text role="guilabel"} fields and click
    `Search`{.interpreted-text role="guilabel"}.
-   When the list has been generated, click
    `Download to File`{.interpreted-text role="guilabel"}.
-   In the pop-up window, select
    `Expanded Fields with CAVV Response/Comma Separated`{.interpreted-text
    role="guilabel"}, enable `Include Column Headings`{.interpreted-text
    role="guilabel"}, and click `Submit`{.interpreted-text
    role="guilabel"}.
-   Open the text file, select `All`{.interpreted-text role="guilabel"},
    copy the data, and paste it into the `Report
    2 Download`{.interpreted-text role="guilabel"} sheet of the
    `Excel import template <authorize-import-template>`{.interpreted-text
    role="ref"}.
-   Transit lines are automatically filled in and updated in the
    `transit for report 1`{.interpreted-text role="guilabel"} and
    `transit for report 2`{.interpreted-text role="guilabel"} sheets of
    the `Excel import template
    <authorize-import-template>`{.interpreted-text role="ref"}. Make
    sure all entries are present, and **if not**, copy the formula from
    previously filled-in lines of the
    `transit for report 1`{.interpreted-text role="guilabel"} or
    `2`{.interpreted-text role="guilabel"} sheets and paste it into the
    empty lines.

::: {.important}
::: {.title}
Important
:::

To get the correct closing balance, **do not remove** any line from the
Excel sheets.
:::

### Import into Odoo

To import the data into Odoo:

-   Open the
    `Excel import template <authorize-import-template>`{.interpreted-text
    role="ref"}.
-   Copy the data from the `transit for report 2`{.interpreted-text
    role="guilabel"} sheet and use *paste special* to only paste the
    values in the `Odoo Import to CSV`{.interpreted-text
    role="guilabel"} sheet.
-   Look for *blue* cells in the `Odoo Import to CSV`{.interpreted-text
    role="guilabel"} sheet. These are chargeback entries without any
    reference number. As they cannot be imported as such, go to
    `Authorize.Net --> Account --> Statements --> eCheck.Net Settlement Statement`{.interpreted-text
    role="menuselection"}.
-   Look for `Charge Transaction/Chargeback`{.interpreted-text
    role="guilabel"}, and click it.
-   Copy the invoice description, paste it into the
    `Label`{.interpreted-text role="guilabel"} cell of the `Odoo
    Import to CSV`{.interpreted-text role="guilabel"} sheet, and add
    [Chargeback /]{.title-ref} before the description.
-   If there are multiple invoices, add a line into the
    `Excel import template
    <authorize-import-template>`{.interpreted-text role="ref"} for each
    invoice and copy/paste the description into each respective
    `Label`{.interpreted-text role="guilabel"} line.

::: {.note}
::: {.title}
Note
:::

For **combined chargeback/returns** in the payouts, create a new line in
the `Excel import
template <authorize-import-template>`{.interpreted-text role="ref"} for
each invoice.
:::

::: {.example}

:::

-   Next, delete *zero transaction* and *void transaction* line items,
    and change the format of the `Amount`{.interpreted-text
    role="guilabel"} column in the
    `Odoo Import to CSV`{.interpreted-text role="guilabel"} sheet to
    *Number*.
-   Go back to
    `eCheck.Net Settlement Statement --> Search for a Transaction`{.interpreted-text
    role="menuselection"} and search again for the previously used batch
    settlements dates.
-   Verify that the batch settlement dates on eCheck.Net match the
    related payments\' dates found in the `Date`{.interpreted-text
    role="guilabel"} column of the
    `Odoo Import to CSV`{.interpreted-text role="guilabel"}.
-   If it does not match, replace the date with the one from eCheck.Net.
    Sort the column by *date*, and make sure the format is
    [MM/DD/YYYY]{.title-ref}.
-   Copy the data - column headings included - from the
    `Odoo Import to CSV`{.interpreted-text role="guilabel"} sheet, paste
    it into a new Excel file, and save it using the CSV format.
-   Open the Accounting app, go to
    `Configuration --> Journals`{.interpreted-text
    role="menuselection"}, tick the `Authorize.Net`{.interpreted-text
    role="guilabel"} box, and click
    `Favorites --> Import records --> Load
    file`{.interpreted-text role="menuselection"}. Select the CSV file
    and upload it into Odoo.

::: {.tip}
::: {.title}
Tip
:::

List of [eCheck.Net return
codes](https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293)
:::
