# File: /content/odoo_doc17.0/fr/content/applications/general/companies/multi_company.md

Multi-company
=============

::: {.seealso}
`Branches <general/companies/branches>`{.interpreted-text role="ref"}
:::

In Odoo, multiple companies can be configured under one database. This
allows some data to be shared among companies while maintaining some
separation between entities.

A centralized management environment allows authorized users to select
multiple companies simultaneously and set their specific warehouses,
customers, equipment, and contacts. It also generates reports of
aggregated figures without switching interfaces, facilitating daily
tasks and enhancing the overall management process.

::: {.warning}
::: {.title}
Warning
:::

Enabling multi-company functionality in an Odoo database on a *Standard*
plan automatically triggers an upsell to the *Custom* plan. This does
not apply to databases on the *One-App Free* plan.

-   **For yearly or multi-year contracts**: An upsell order is created
    with a 30-day limit.
-   **For monthly contracts**: The subscription automatically switches
    to the *Custom* plan and the new rate is applied when the next bill
    is generated.

For more information, refer to [Odoo\'s pricing
page](https://www.odoo.com/pricing-plan) or contact your account
manager.
:::

Configuration {#general/multi-company/configuration}
-------------

Open the Settings app, navigate to the `Companies`{.interpreted-text
role="guilabel"} section, and click `oi-arrow-right`{.interpreted-text
role="icon"} `Manage Companies`{.interpreted-text role="guilabel"}.
Then, click `New`{.interpreted-text role="guilabel"} and `fill in
the form with the company's information <general/companies/company>`{.interpreted-text
role="ref"} or select an existing company to edit it.

::: {.note}
::: {.title}
Note
:::

Alternatively, it is possible to create a company by going to
`Settings --> Users
& Companies --> Companies`{.interpreted-text role="menuselection"}.
:::

::: {.tip}
::: {.title}
Tip
:::

To archive a company, follow these steps:

1.  In the Settings app, navigate to the `Companies`{.interpreted-text
    role="guilabel"} section and click
    `oi-arrow-right`{.interpreted-text role="icon"}
    `Manage Companies`{.interpreted-text role="guilabel"}.
2.  In the `Companies`{.interpreted-text role="guilabel"} list view,
    select the company to be archived.
3.  Click the `fa-cog`{.interpreted-text role="icon"}
    `Actions`{.interpreted-text role="guilabel"} menu and select
    `Archive`{.interpreted-text role="guilabel"}.
4.  Click `Archive`{.interpreted-text role="guilabel"} to confirm.
:::

Multi-company environment {#general/multi-company/multi-company-environment}
-------------------------

In a multi-company environment, users are granted
`access to one or more companies
<general/multi-company/user-access>`{.interpreted-text role="ref"}, and
`data
<general/multi-company/shared-and-unshared-records>`{.interpreted-text
role="ref"} is created or modified based on its intended use within that
structure.

### User access {#general/multi-company/user-access}

A multi-company environment allows flexible control over
`user access <users/multi-companies>`{.interpreted-text role="ref"} and
`access rights <../users/access_rights>`{.interpreted-text role="doc"}
that can be granted or restricted as needed.

### Company selector {#general/multi-company/company-selector}

To switch between (or select) multiple companies, follow these steps:

1.  Click the company selector in the top-right corner of the header
    menu.
2.  In the drop-down list, select the checkboxes next to the desired
    companies.
3.  The highlighted company indicates the current active environment.
4.  To switch to another company, click its name in the list of selected
    companies.

::: {.example}
In the example below, the user can access six companies, two of which
are selected. The current active company is *My Company (San
Francisco)*.


:::

### Shared and company-specific records {#general/multi-company/shared-and-unshared-records}

Data, such as products, contacts, and equipment can either be shared
across companies or restricted to a specific company by setting the
`Company`{.interpreted-text role="guilabel"} field on the relevant
records:

-   either leave the field blank to make it accessible to all companies;
-   or select the company to make it visible to users logged in to that
    specific company.

Records specifically linked to a particular company are accessible only
within that entity. For instance, quotations, invoices, and vendor bills
associated with a company are visible only when logged into that
company, and the corresponding company is automatically selected by
default and displayed in the `Company`{.interpreted-text
role="guilabel"} field.

In a multi-company database, new products and contacts are shared across
companies by default. To restrict them to a specific company, set the
`Company`{.interpreted-text role="guilabel"} field on the record\'s
form.

Inter-company transactions {#general/multi-company/inter-company-transactions}
--------------------------

The `Inter-Company Transactions`{.interpreted-text role="guilabel"}
feature allows one company in the database to sell or purchase goods and
services from another company within the same database. Depending on the
configuration settings, counterpart documents for orders and invoices
can be automatically generated and synchronized.

::: {.warning}
::: {.title}
Warning
:::

To handle inter-company transactions correctly, `general
<../../finance/accounting/get_started>`{.interpreted-text role="doc"}
and specific configurations must be set properly, including
`fiscal positions <../../finance/accounting/taxes/fiscal_positions>`{.interpreted-text
role="doc"} and
`localizations <../../finance/fiscal_localizations>`{.interpreted-text
role="doc"}.
:::

To activate inter-company transactions, select the relevant company in
the `company selector
<general/multi-company/company-selector>`{.interpreted-text role="ref"},
open the Settings app, navigate to the `Companies`{.interpreted-text
role="guilabel"} section, enable
`Inter-Company Transactions`{.interpreted-text role="guilabel"}, and
`Save`{.interpreted-text role="guilabel"}. Then, choose one of the
following `Rule`{.interpreted-text role="guilabel"} options to create a
counterpart for the selected company:

-   `Do not synchronize`{.interpreted-text role="guilabel"}: Do not
    synchronize any inter-company transactions.

-   `Synchronized invoice/bills`{.interpreted-text role="guilabel"}:
    Generate a bill/invoice when a company confirms a bill/invoice for
    the selected company.

-   `Synchronize Sales Order`{.interpreted-text role="guilabel"}:
    Generate a quotation (drafted sales order) when a sales order is
    confirmed for the selected company. To generate a validated sales
    order instead of a quotation, enable
    `Automatic Validation`{.interpreted-text role="guilabel"}.\*

-   `Synchronize Purchase Order`{.interpreted-text role="guilabel"}:
    Generate a request for quotation (drafted purchase order) using the
    selected company warehouse in the `Use Warehouse`{.interpreted-text
    role="guilabel"} field when a purchase order is confirmed for the
    selected company. To generate a validated purchase order instead of
    a request for quotation, enable
    `Automatic Validation`{.interpreted-text role="guilabel"}.\*

-   `Synchronize Sales and Purchase Order`{.interpreted-text
    role="guilabel"}: Generate a drafted purchase/sales order using the
    selected company warehouse in the `Use Warehouse`{.interpreted-text
    role="guilabel"} field when a sales/purchase order is confirmed for
    the selected company. To generate a validated purchase/sales order
    instead of a draft one, enable
    `Automatic Validation`{.interpreted-text role="guilabel"}.\*

    \* This rule option needs to be selected for
    `Automatic Validation`{.interpreted-text role="guilabel"} to appear
    in the configuration.

::: {.note}
::: {.title}
Note
:::

For inter-company transactions, the `products must be shared
<general/multi-company/shared-and-unshared-records>`{.interpreted-text
role="ref"} among the involved companies.
:::

::: {.example}
`Synchronize invoices/bills`{.interpreted-text role="guilabel"}: when an
invoice for `Customer`{.interpreted-text role="guilabel"} [JS Store
US]{.title-ref} is posted on [JS Store Belgium]{.title-ref}, a vendor
bill is automatically created in [JS Store US]{.title-ref}.

`Synchronize sales/purchase order`{.interpreted-text role="guilabel"}:
when a sales order for `Customer`{.interpreted-text role="guilabel"} [JS
Store US]{.title-ref} is confirmed on [JS Store Belgium]{.title-ref}, a
purchase order on [JS Store US]{.title-ref} is automatically created
(and confirmed if the `Automatic Validation`{.interpreted-text
role="guilabel"} feature is enabled).
:::

::: {.seealso}
\-
`Multi-company Guidelines <../../../developer/howtos/company>`{.interpreted-text
role="doc"} -
`../../finance/accounting/get_started/multi_currency`{.interpreted-text
role="doc"}
:::

Use cases {#general/multi-company/use-cases}
---------

### Multinational companies {#general/multi-company/use-cases-multinational-companies}

A multinational retail chain operating in the United States and Canada
must manage transactions in USD and CAD.

Since each country has its own tax laws and regulations, using Odoo's
multi-company feature is highly beneficial.

This setup allows for inter-company transactions, which is essential for
managing cross-border inventory transfers. It also simplifies the sales
process by enabling customers transactions in their local currency.

### Separate processes {#general/multi-company/use-cases-seperate-processes}

A small furniture company is launching a new product line that requires
separate procurement, inventory, and manufacturing workflows. These new
products differ significantly from the existing catalog. To manage this
efficiently, the company is considering using the multi-company feature
to manage the new line as a separate business entity.

However, creating a completely new company might add unnecessary
complexity to the database. Instead, the company can leverage existing
features such as `analytic accounting
<../../finance/accounting/reporting/analytic_accounting>`{.interpreted-text
role="doc"} and multiple warehouses to manage the new product line
without complicating overall operations.
