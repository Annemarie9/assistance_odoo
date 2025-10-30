# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/fiscal_positions.md

Fiscal positions (tax and account mapping)
==========================================

Default taxes and accounts are set on products and customers to create
new transactions on the fly. However, depending on the customers\' and
providers\' localization and business type, using different taxes and
accounts for a transaction might be necessary.

**Fiscal positions** allow the creation of rules to adapt the taxes and
accounts used for a transaction automatically.

They can be applied
`automatically <fiscal_positions/automatic>`{.interpreted-text
role="ref"}, `manually
<fiscal_positions/manual>`{.interpreted-text role="ref"}, or
`assigned to a partner <fiscal_positions/partner>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

Several default fiscal positions are available as part of your
`fiscal localization
package <fiscal_localizations/packages>`{.interpreted-text role="ref"}.
:::

Configuration
-------------

### Tax and account mapping

To edit or create a fiscal position, go to
`Accounting --> Configuration --> Fiscal
Positions`{.interpreted-text role="menuselection"}, and open the entry
to modify or click on `New`{.interpreted-text role="guilabel"}.

The mapping of taxes and accounts is based on the default taxes and
accounts defined in the product form.

-   To map to another tax or account, fill out the right column
    (`Tax to Apply`{.interpreted-text role="guilabel"}/
    `Account to Use Instead`{.interpreted-text role="guilabel"}).

{.align-center}

{.align-center}

-   To remove a tax, leave the field `Tax to Apply`{.interpreted-text
    role="guilabel"} empty.
-   To replace a tax with several other taxes, add multiple lines using
    the same `Tax on
    Product`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The mapping only works with *active* taxes. Therefore, make sure they
are active by going to
`Accounting --> Configuration --> Taxes`{.interpreted-text
role="menuselection"}.
:::

Application
-----------

### Automatic application {#fiscal_positions/automatic}

To automatically apply a fiscal position following a set of conditions,
go to
`Accounting --> Configuration --> Fiscal Positions`{.interpreted-text
role="menuselection"}, open the fiscal position to modify, and tick
`Detect Automatically`{.interpreted-text role="guilabel"}.

From there, several conditions can be activated:

-   `VAT Required`{.interpreted-text role="guilabel"}: the customer\'s
    VAT number must be present on their contact form.
-   `Country Group`{.interpreted-text role="guilabel"} and
    `Country`{.interpreted-text role="guilabel"}: the fiscal position is
    only applied to the selected country or country group.

{.align-center}

::: {.note}
::: {.title}
Note
:::

\- If the `Verify VAT Numbers <vat_verification>`{.interpreted-text
role="doc"} feature is enabled, any fiscal positions with
`VAT required`{.interpreted-text role="guilabel"} enabled will require
Intra-Community valid VAT numbers to apply automatically. - Taxes on
**eCommerce orders** are automatically updated once the customer has
logged in or filled out their billing details.
:::

::: {.important}
::: {.title}
Important
:::

The fiscal positions\' **sequence** defines which fiscal position is
applied if all conditions set on multiple fiscal positions are met
simultaneously.

For example, suppose the first fiscal position in a sequence targets
*country A* while the second fiscal position targets a *country group*
that comprises *country A*. In that case, only the first fiscal position
will be applied to customers from *country A*.
:::

### Manual application {#fiscal_positions/manual}

To manually select a fiscal position, open a sales order, invoice, or
bill, go to the `Other Info`{.interpreted-text role="guilabel"} tab and
select the desired `Fiscal Position`{.interpreted-text role="guilabel"}
before adding product lines.

{.align-center}

### Assign to a partner {#fiscal_positions/partner}

To define which fiscal position must be used by default for a specific
partner, go to
`Accounting --> Customers --> Customers`{.interpreted-text
role="menuselection"}, select the partner, open the
`Sales & Purchase`{.interpreted-text role="guilabel"} tab, and select
the `Fiscal Position`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
-   `../taxes`{.interpreted-text role="doc"}
-   `B2B_B2C`{.interpreted-text role="doc"}
:::
