Foreign currencies
==================

With Odoo, pricelists can be used to manage prices in a number of
foreign currencies. Specifically, Odoo has the ability to work with 167
total currencies.

::: {.note}
::: {.title}
Note
:::

In order to use multiple currencies in Odoo *Sales*, the *Accounting*
application **must** be installed.
:::

Settings
--------

Once the *Accounting* app has been installed, foreign currencies can be
added to the database. Navigate to
`Accounting app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll to the `Currencies`{.interpreted-text
role="guilabel"} section, and locate the
`Main Currency`{.interpreted-text role="guilabel"} setting.

{.align-center}

Odoo automatically sets the main currency as the currency of the country
the company is based in.

To change the main currency of the company, select the drop-down menu in
the `Currency`{.interpreted-text role="guilabel"} field, select the
desired currency, and be sure to `Save`{.interpreted-text
role="guilabel"} the changes.

::: {.tip}
::: {.title}
Tip
:::

To ensure currency rates are updated automatically, enable the
*automatic currency rates* feature on the *Accounting* settings page
(`Accounting app --> Configuration --> Settings
--> Currencies section`{.interpreted-text role="menuselection"}).

{.align-center}

Click the checkbox beside the
`Automatic Currency Rates`{.interpreted-text role="guilabel"} feature,
choose a designated bank to get the currency rates from in the
`Service`{.interpreted-text role="guilabel"} field drop-down menu, and
select an `Interval`{.interpreted-text role="guilabel"} of time for the
updates to take place. Then determine when the date of the
`Next Run`{.interpreted-text role="guilabel"} should be.

To instantly update the currency rates, click the
`🔁 (circular arrows)`{.interpreted-text role="guilabel"} icon, located
to the right of the `Next Run`{.interpreted-text role="guilabel"} field.

When all configurations are complete, be sure to
`Save`{.interpreted-text role="guilabel"} all changes.
:::

::: {.note}
::: {.title}
Note
:::

All payment methods **must** be in the same currency as the sales
journal, or the company currency, if the company currency is not set. If
it is not the same, a `Validation
Error`{.interpreted-text role="guilabel"} message appears.
:::

View, edit, and add currencies
------------------------------

To view, edit, and add currencies to the database, making them available
on pricelists and on the `Main Currency`{.interpreted-text
role="guilabel"} drop-down menu, click the
`Currencies`{.interpreted-text role="guilabel"} link, located beneath
the `Currency`{.interpreted-text role="guilabel"} field on the
`Accounting app --> Settings`{.interpreted-text role="menuselection"}
page.

When the `Currencies`{.interpreted-text role="guilabel"} link is
clicked, a separate `Currencies`{.interpreted-text role="guilabel"} page
is revealed.

{.align-center}

On this page, Odoo provides a master list of 167 global currencies. Each
row shows the corresponding `Currency`{.interpreted-text
role="guilabel"}, `Symbol`{.interpreted-text role="guilabel"},
`Name`{.interpreted-text role="guilabel"}, date of the
`Last Update`{.interpreted-text role="guilabel"}, and
`Current Rate`{.interpreted-text role="guilabel"} (compared to the
default currency of the country in which the company is based).

To the far right, there are two columns, which can be toggled on or off:

-   `Use on eBay`{.interpreted-text role="guilabel"}: this currency can
    be used with the connected eBay account (if applicable).
-   `Active`{.interpreted-text role="guilabel"}: this currency is
    activated, which means it can be added to a pricelist, or used as
    the main currency of the company, if desired (via
    `Accounting app -->
    Configuration --> Settings --> Currencies section`{.interpreted-text
    role="menuselection"}).

::: {.note}
::: {.title}
Note
:::

By default, all the `Active`{.interpreted-text role="guilabel"} currency
options are at the top of the list.
:::

::: {.tip}
::: {.title}
Tip
:::

It is recommended that *at least* one pricelist is created per
`Active`{.interpreted-text role="guilabel"} currency. See
`./pricing`{.interpreted-text role="doc"} to learn more about pricelist
configuration.
:::

To toggle options on/off, click the toggle switch in the row for the
corresponding column. When *on* the color of the switch is green. When
*off*, the color of the switch is grey.

### Currency detail form

To edit any currency on the `Currencies`{.interpreted-text
role="guilabel"} page, click the desired currency to reveal the detail
form for that specific currency, and proceed to make any necessary
changes.

{.align-center}

On the currency detail form, the relevant currency code appears in the
`Currency`{.interpreted-text role="guilabel"} field. Beneath that, the
name for the currency is in the `Name`{.interpreted-text
role="guilabel"} field.

Then, toggle the currency\'s availability with the
`Active`{.interpreted-text role="guilabel"} toggle: *on* is indicated
with a green switch, and *off* is indicated with a grey switch.

On the right of the currency detail form, the appropriate
`Currency Unit`{.interpreted-text role="guilabel"} (e.g.
[Dollars]{.title-ref}) and `Currency Subunit`{.interpreted-text
role="guilabel"} (e.g. [Cents]{.title-ref}) can be found.

If the currency is meant to be used for eBay purposes, toggle the
`Use on eBay`{.interpreted-text role="guilabel"} option to the desired
activation.

Next, under the `Rates`{.interpreted-text role="guilabel"} tab, the
various conversion rates can be viewed, added, or deleted. Each row
shows the `Date`{.interpreted-text role="guilabel"} of that specific
rate, the `Company`{.interpreted-text role="guilabel"} to which it is
connected, followed by the `Unit per...`{.interpreted-text
role="guilabel"} and `...per Unit`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The *\...* in each of the last two columns represents the main currency
set for the company. For example, if the main currency is set to
[USD]{.title-ref}, the columns are titled
`Unit per USD`{.interpreted-text role="guilabel"} and
`USD per Unit`{.interpreted-text role="guilabel"}.
:::

To add a new rate, click `Add a line`{.interpreted-text role="guilabel"}
in the `Rates`{.interpreted-text role="guilabel"} tab, and proceed to
fill in the necessary information in the aforementioned columns.

### Main currency detail form

If the selected currency is the main currency of the company, a blue
banner appears at the top of the currency detail form with the message:
`This is your company's currency.`{.interpreted-text role="guilabel"}.

{.align-center}

All the fields are the same as a typical currency detail form, but there
will **not** be a `Rates`{.interpreted-text role="guilabel"} tab because
all other currency rates are based off the main currency of the company.

Create new currency
-------------------

If a desired currency isn\'t on the `Currencies`{.interpreted-text
role="guilabel"} page, click the `New`{.interpreted-text
role="guilabel"} button to open a blank currency template form.

::: {.tip}
::: {.title}
Tip
:::

The same `New`{.interpreted-text role="guilabel"} button is located in
the upper-right corner of any currency detail form.
:::

{.align-center}

On the blank currency detail form, proceed to enter the desired currency
code in the `Currency`{.interpreted-text role="guilabel"} field. Beneath
that, enter the name for the currency in the `Name`{.interpreted-text
role="guilabel"} field.

Then, toggle the currency\'s availability with the
`Active`{.interpreted-text role="guilabel"} toggle switch.

On the right of the currency detail form, enter the appropriate
`Currency Unit`{.interpreted-text role="guilabel"} (e.g.
[Dollars]{.title-ref}) and appropriate
`Currency Subunit`{.interpreted-text role="guilabel"} (e.g.
[Cents]{.title-ref}).

If the currency is meant to be used for eBay purposes, toggle the
`Use on eBay`{.interpreted-text role="guilabel"} to the desired
activation.

Next, under the `Rates`{.interpreted-text role="guilabel"} tab, add a
new rate by clicking `Add a line`{.interpreted-text role="guilabel"}.
Then, proceed to confirm and adjust the `Date`{.interpreted-text
role="guilabel"}, `Company`{.interpreted-text role="guilabel"},
`Unit per...`{.interpreted-text role="guilabel"}, and
`...per Unit`{.interpreted-text role="guilabel"} fields to ensure all
the auto-populated information is accurate.

::: {.note}
::: {.title}
Note
:::

The *\...* in each of the last two columns represents the main currency
set for the company. For example, if the main currency is set to
[USD]{.title-ref}, the columns are titled
`Unit per USD`{.interpreted-text role="guilabel"} and
`USD per Unit`{.interpreted-text role="guilabel"}.
:::

Currency-specific pricelists
----------------------------

It is recommended that *at least* one pricelist is created per active
currency in the database. To create (or assign) a pricelist to a
specific currency, start by navigating to `Sales
app --> Products --> Pricelists`{.interpreted-text
role="menuselection"}.

From the `Pricelists`{.interpreted-text role="guilabel"} page, either
select an existing pricelist to edit, or click `New`{.interpreted-text
role="guilabel"} to create a new pricelist.

On the pricelist detail form, for either a new or existing pricelist,
adjust the `Currency`{.interpreted-text role="guilabel"} field as
desired.

::: {.seealso}
`./pricing`{.interpreted-text role="doc"} to learn more about pricelist
configuration.
:::

Auto-conversion from public price
---------------------------------

It should be noted that the public price seen on products is directly
related to the main currency the company has set, which is configured by
navigating to `Accounting app -->
Configuration --> Settings --> Currencies section --> Main Currency --> Currency drop-down menu`{.interpreted-text
role="menuselection"}.

The sales price automatically updates if the pricelist is changed to a
different pricelist that has a different currency than the company\'s
main currency. The change in price is directly related to the updated
conversion rate for that currency.

Set product prices
------------------

In order to have product prices set in place to avoid any changes in
currency rates, start by navigating to
`Sales app --> Products --> Products`{.interpreted-text
role="menuselection"}.

From the `Products`{.interpreted-text role="guilabel"} page, select the
desired product to modify. Or, create a new product by clicking the
`New`{.interpreted-text role="guilabel"} button.

Then, on the product detail form, click the
`Extra Prices`{.interpreted-text role="guilabel"} smart button, located
in the upper-left corner. Doing so reveals a separate
`Price Rules`{.interpreted-text role="guilabel"} page, specific to that
particular product.

{.align-center}

Click `New`{.interpreted-text role="guilabel"}, and select the desired
pricelist from the drop-down menu in the `Pricelist`{.interpreted-text
role="guilabel"} column.

The `Applied On`{.interpreted-text role="guilabel"} field is
auto-populated with the product, so proceed to enter in the desired
figures in the `Min. Quantity`{.interpreted-text role="guilabel"} and
`Price`{.interpreted-text role="guilabel"} fields.

::: {.note}
::: {.title}
Note
:::

The figure in the `Min. Quantity`{.interpreted-text role="guilabel"}
field means the `Price`{.interpreted-text role="guilabel"} being set
will **only** trigger if at least that amount of product is purchased.
:::

If necessary, configure a `Start Date`{.interpreted-text
role="guilabel"} and `End Date`{.interpreted-text role="guilabel"} for
the set prices. Leaving those columns blank ensures the set price will
remain valid, regardless of the date of sale.

If working in a multi-company environment, designate to which company
this price rule should be applied in the `Company`{.interpreted-text
role="guilabel"} field. Leaving that field blank ensures the price rule
applies to all companies in the database.

With those configurations complete, regardless of any changes/updates in
conversion, whenever those designated pricelists are applied to a
customer trying to purchase this specific product, these pre-determined
set prices appear.

::: {.seealso}
`./pricing`{.interpreted-text role="doc"}
:::
