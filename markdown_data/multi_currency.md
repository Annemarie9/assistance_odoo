# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/get_started/multi_currency.md

Multi-currency system
=====================

Odoo allows you to issue invoices, receive bills, and record
transactions in currencies other than the main currency configured for
your company. You can also set up bank accounts in other currencies and
run reports on your foreign currency activities.

::: {.seealso}
\- `../bank/foreign_currency`{.interpreted-text role="doc"}
:::

Configuration {#multi-currency/config}
-------------

### Main currency {#multi-currency/config-main-currency}

The **main currency** is defined by default according to the company\'s
country. You can change it by going to
`Accounting --> Configuration --> Settings --> Currencies`{.interpreted-text
role="menuselection"} and changing the currency in the
`Main Currency`{.interpreted-text role="guilabel"} setting.

### Enable foreign currencies {#multi-currency/config-enable}

Go to `Accounting --> Configuration --> Currencies`{.interpreted-text
role="menuselection"}, and enable the currencies you wish to use by
toggling the `Active`{.interpreted-text role="guilabel"} button.

{.align-center}

### Currency rates {#multi-currency/config-rates}

#### Manual update

To manually create and set a currency rate, go to
`Accounting --> Configuration -->
Currencies`{.interpreted-text role="menuselection"}, click on the
currency you wish to change the rate of, and under the
`Rates`{.interpreted-text role="guilabel"} tab, click
`Add a line`{.interpreted-text role="guilabel"} to create a new rate.

{.align-center}

#### Automatic update

When you activate a second currency for the first time,
`Automatic Currency Rates`{.interpreted-text role="guilabel"} appears
under
`Accounting Dashboard --> Configuration --> Settings --> Currencies`{.interpreted-text
role="menuselection"}. By default, you have to click on the **Update
now** button (`🗘`{.interpreted-text role="guilabel"}) to update the
rates.

Odoo can update the rates at regular intervals. To do so, change the
`Interval`{.interpreted-text role="guilabel"} from
`Manually`{.interpreted-text role="guilabel"} to
`Daily`{.interpreted-text role="guilabel"}, `Weekly`{.interpreted-text
role="guilabel"}, or `Monthly`{.interpreted-text role="guilabel"}. You
can also select the web service from which you want to retrieve the
latest currency rates by clicking on the `Service`{.interpreted-text
role="guilabel"} field.

### Exchange difference entries {#multi-currency/config-exch-diff}

Odoo automatically records exchange differences entries on dedicated
accounts, in a dedicated journal.

You can define which journal and accounts to use to **post exchange
difference entries** by going to
`Accounting --> Configuration --> Settings --> Default Accounts`{.interpreted-text
role="menuselection"} and editing the `Journal`{.interpreted-text
role="guilabel"}, `Gain Account`{.interpreted-text role="guilabel"}, and
`Loss Account`{.interpreted-text role="guilabel"}.

::: {.example}
If you receive a payment for a customer invoice one month after it was
issued, the exchange rate has likely changed since. Therefore, this
fluctuation implies some profit or loss due to the exchange difference,
which Odoo automatically records in the default **Exchange Difference**
journal.
:::

### Chart of accounts {#multi-currency/config-coa}

Each account can have a set currency. By doing so, all moves relevant to
the account are forced to have that account\'s currency.

To do so, go to
`Accounting --> Configuration --> Charts of Accounts`{.interpreted-text
role="menuselection"} and select a currency in the field
`Account Currency`{.interpreted-text role="guilabel"}. If left empty,
all active currencies are handled instead of just one.

### Journals {#multi-currency/config-journals}

If a currency is set on a **journal**, that journal only handles
transactions in that currency.

To do so, go to
`Accounting --> Configuration --> Journals`{.interpreted-text
role="menuselection"}, open the journal you want to edit, and select a
currency in the field `Currency`{.interpreted-text role="guilabel"}.

{.align-center}

Multi-currency accounting {#multi-currency/mca}
-------------------------

### Invoices, bills, and other documents {#multi-currency/mca-documents}

For all documents, you can select the currency and journal to use for
the transaction on the document itself.

{.align-center}

### Payment registration {#multi-currency/mca-payment}

To register a payment in a currency other than your company\'s main
currency, click on the `Register Payment`{.interpreted-text
role="guilabel"} payment button of your document and, in the pop-up
window, select a **currency** in the `Amount`{.interpreted-text
role="guilabel"} field.

{.align-center}

### Bank transactions {#multi-currency/mca-statements}

When creating or importing bank transactions, the amount is in the
company\'s main currency. To input a **foreign currency**, select a
currency in the `Foreign Currency`{.interpreted-text role="guilabel"}.
Once selected, enter the `Amount`{.interpreted-text role="guilabel"} in
your main currency for it to automatically get converted in the foreign
currency in the `Amount in Currency field`{.interpreted-text
role="guilabel"}.

{.align-center}

When reconciling, Odoo displays both the foreign currency amount and the
equivalent amount in your company\'s main currency.

### Exchange rate journal entries {#multi-currency/mca-exch-entries}

To see **exchange difference journal entries**, go to
`Accounting Dashboard -->
Accounting --> Journals: Miscellaneous`{.interpreted-text
role="menuselection"}.

{.align-center}
