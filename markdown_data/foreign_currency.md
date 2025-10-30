# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/bank/foreign_currency.md

Manage a bank account in a foreign currency
===========================================

In Odoo, every transaction is recorded in the default currency of the
company, and reports are all based on that default currency. When you
have a bank account in a foreign currency, for every transaction, Odoo
stores two values:

-   The debit/credit in the currency of the *company*;
-   The debit/credit in the currency of the *bank account*.

Currency rates are updated automatically using the web services of a
banking institution. By default, Odoo uses the European Central Bank\'s
web services but other options are available.

Configuration
-------------

### Activate multi-currencies

To work with multiple currencies, go to
`Accounting --> Configuration --> Settings
--> Currencies`{.interpreted-text role="menuselection"} and tick
`Multi-Currencies`{.interpreted-text role="guilabel"}. Under
`Post Exchange difference
entries in:`{.interpreted-text role="guilabel"}, provide a
`Journal`{.interpreted-text role="guilabel"}, a
`Gain Account`{.interpreted-text role="guilabel"}, a
`Loss Account`{.interpreted-text role="guilabel"}, and then click on
`Save`{.interpreted-text role="guilabel"}.

### Configure currencies

Once Odoo is configured to support multiple currencies, they are all
created by default, but not necessarily active. To activate the new
currencies, click on `Activate Other Currencies`{.interpreted-text
role="guilabel"} under the `Multi-Currencies`{.interpreted-text
role="guilabel"} setting or go to `Accounting --> Configuration
--> Accounting: Currencies`{.interpreted-text role="menuselection"}.

When the currencies are activated, you can choose to **automate** the
currency rate update, or leave it on **manual**. To configure the rate
update, go back to `Accounting -->
Configuration --> Settings --> Currencies`{.interpreted-text
role="menuselection"}, check
`Automatic Currency Rates`{.interpreted-text role="guilabel"}, set
`Interval`{.interpreted-text role="guilabel"} to your desired frequency,
and then click on `Save`{.interpreted-text role="guilabel"}. You also
have the option to choose the `Service`{.interpreted-text
role="guilabel"} you wish to obtain currency rates from.

Click on the Update now button (`🗘`{.interpreted-text role="guilabel"})
besides the `Next Run`{.interpreted-text role="guilabel"} field to
update the currency rates manually.

### Create a new bank account

In the accounting application, go to
`Accounting --> Configuration --> Journals`{.interpreted-text
role="menuselection"} and create a new one. Enter a
`Journal Name`{.interpreted-text role="guilabel"} and set the
`Type`{.interpreted-text role="guilabel"} to [Bank]{.title-ref}. In the
`Journal Entries`{.interpreted-text role="guilabel"} tab, enter a
**short code**, a **currency**, and then finally click on the
`Bank Account`{.interpreted-text role="guilabel"} field to create a new
account. In the pop-up window of the account creation, enter a name, a
code (ex.: 550007), set its type to [Bank and Cash]{.title-ref}, set a
currency type, and save. When you are back on the **journal**, click on
the `Account Number`{.interpreted-text role="guilabel"} field, and in
the pop-up window, fill out the `Account Number`{.interpreted-text
role="guilabel"}, `Bank`{.interpreted-text role="guilabel"} of your
account, and save.

{.align-center}

Upon creation of the journal, Odoo automatically links the bank account
to the journal. It can be found under
`Accounting --> Configuration --> Accounting: Chart of Accounts`{.interpreted-text
role="menuselection"}.

Vendor bill in a foreign currency
---------------------------------

To pay a bill in a foreign currency, simply select the currency next to
the `Journal`{.interpreted-text role="guilabel"} field and register the
payment. Odoo automatically creates and posts the foreign **exchange
gain or loss** as a new journal entry.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Note that you can pay a foreign bill with another currency. In that
case, Odoo automatically converts between the two currencies.
:::

Unrealized Currency Gains/Losses Report
---------------------------------------

This report gives an overview of all unrealized amounts in a foreign
currency on your balance sheet, and allows you to adjust an entry or
manually set an exchange rate. To access this report, go to
`Reporting --> Management: Unrealized Currency Gains/Losses`{.interpreted-text
role="menuselection"}. From here, you have access to all open entries in
your **balance sheet**.

{.align-center}

If you wish to use a different currency rate than the one set in
`Accounting -->
Configuration --> Settings --> Currencies`{.interpreted-text
role="menuselection"}, click the `Exchange Rates`{.interpreted-text
role="guilabel"} button and change the rate of the foreign currencies in
the report.

{.align-center}

When manually changing **exchange rates**, a yellow banner appears
allowing you to reset back to Odoo\'s rate. To do so, simply click on
`Reset to Odoo's Rate`{.interpreted-text role="guilabel"}.

{.align-center}

In order to update your **balance sheet** with the amount of the
`adjustment`{.interpreted-text role="guilabel"} column, click on the
`Adjustment Entry`{.interpreted-text role="guilabel"} button. In the
pop-up window, select a `Journal`{.interpreted-text role="guilabel"},
`Expense Account`{.interpreted-text role="guilabel"} and
`Income Account`{.interpreted-text role="guilabel"} to calculate and
process the **unrealized gains and losses**.

You can set the date of the report in the `Date`{.interpreted-text
role="guilabel"} field. Odoo automatically reverses the booking entry to
the date set in `Reversal Date`{.interpreted-text role="guilabel"}.

Once posted, the `adjustment`{.interpreted-text role="guilabel"} column
should indicate [0.00]{.title-ref}, meaning all **unrealized
gains/losses** have been adjusted.

{.align-center}
