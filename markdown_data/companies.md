# File: /content/odoo_doc17.0/fr/content/applications/general/companies.md

show-content

:   

Companies
=========

In Odoo, a company is an individual business entity that operates
independently, with its own legal identity, financial records, and
specific operational settings.

::: {.seealso}
\- `general/companies/branches`{.interpreted-text role="ref"} -
`Multi-company <companies/multi_company>`{.interpreted-text role="doc"}
:::

Configuration {#general/companies/configuration}
-------------

To set up a company, follow these steps:

1.  `Configure the company details <general/companies/company>`{.interpreted-text
    role="ref"}.
2.  `Manage users and their access rights <general/companies/users>`{.interpreted-text
    role="ref"}.
3.  `Customize the document layout <general/companies/document-layout>`{.interpreted-text
    role="ref"}.

### Company {#general/companies/company}

To create a company, open the Settings app, navigate to the
`Companies`{.interpreted-text role="guilabel"} section, and click
`oi-arrow-right`{.interpreted-text role="icon"}
`Manage Companies`{.interpreted-text role="guilabel"}. In the
`Companies`{.interpreted-text role="guilabel"} list view, click
`New`{.interpreted-text role="guilabel"} and configure the following
fields:

-   `Company Name`{.interpreted-text role="guilabel"}
-   `Address`{.interpreted-text role="guilabel"}
-   `Tax ID`{.interpreted-text role="guilabel"}: tax identification
    number.
-   `LEI`{.interpreted-text role="guilabel"}: legal entity identifier.
-   `Company ID`{.interpreted-text role="guilabel"}: company\'s registry
    number, if different from `Tax ID`{.interpreted-text
    role="guilabel"}
-   `Currency <multi-currency/config-main-currency>`{.interpreted-text
    role="ref"}
-   `Phone`{.interpreted-text role="guilabel"} and
    `Mobile`{.interpreted-text role="guilabel"}
-   `Email`{.interpreted-text role="guilabel"}
-   `Website`{.interpreted-text role="guilabel"}
-   `Email Domain`{.interpreted-text role="guilabel"}
-   `Color`{.interpreted-text role="guilabel"}

Upload the company\'s logo and `Save`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- Alternatively, it is possible to create a company by going to
`Settings -->
Users & Companies --> Companies`{.interpreted-text
role="menuselection"}. - The company\'s
`General information`{.interpreted-text role="guilabel"} may vary based
on the `fiscal localization
<../finance/fiscal_localizations>`{.interpreted-text role="doc"}.
:::

### Users {#general/companies/users}

After setting up a company, add `users <users>`{.interpreted-text
role="doc"} and configure their `access
<users/add-individual>`{.interpreted-text role="ref"} and
`access rights <users/access_rights>`{.interpreted-text role="doc"}.

::: {.seealso}
`Users in multi-company environment <users/multi-companies>`{.interpreted-text
role="ref"}
:::

### Document layout {#general/companies/document-layout}

Configure the
`default layout <studio/pdf-reports/default-layout>`{.interpreted-text
role="ref"} for all company documents.

Branches {#general/companies/branches}
--------

Branches represent subdivisions within a company, such as regional
offices or departments, that operate under a common parent company. They
support hierarchical company structures through
`configurable settings <general/companies/branches/configuration>`{.interpreted-text
role="ref"}, enabling
`comprehensive or branch-specific views <general/companies/branches/consolidated-view>`{.interpreted-text
role="ref"} with flexible
`access control <general/companies/branches/user-access>`{.interpreted-text
role="ref"}, `entity-specific or
shared record visibility <general/companies/branches/shared-records>`{.interpreted-text
role="ref"}, and customizable
`reporting <general/companies/branches/reporting>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

Independent subsidiaries should be created as additional companies, not
branches.
:::

::: {.seealso}
\-
`Multi-company </applications/general/companies/multi_company>`{.interpreted-text
role="doc"} -
`Branch accounting <accounting/branches>`{.interpreted-text role="ref"}
:::

### Configuration {#general/companies/branches/configuration}

Each branch is linked to its parent company but may contain different or
specific information, such as its address or logo. A branch can be a
parent company of branches at a lower level to create a multi-level
architecture.

::: {.important}
::: {.title}
Important
:::

\- Clarify the company\'s structure and hierarchy before creating
companies and branches in Odoo. A company defined as a parent cannot be
converted into a branch later, as doing so may result in
`access rights <users/access_rights>`{.interpreted-text role="doc"}
issues. - Always create the parent company first.
:::

To create a branch, follow these steps in the Settings app:

1.  Navigate to the `Companies`{.interpreted-text role="guilabel"}
    section, click `oi-arrow-right`{.interpreted-text role="icon"}
    `Manage
    Companies`{.interpreted-text role="guilabel"}, or go to
    `Settings --> Users & Companies --> Companies`{.interpreted-text
    role="menuselection"}.
2.  In the `Companies`{.interpreted-text role="guilabel"} list view,
    open the desired parent company form.
3.  In the `Branches`{.interpreted-text role="guilabel"} tab, click
    `Add a line`{.interpreted-text role="guilabel"} and fill in the
    `General
    Information <general/companies/company>`{.interpreted-text
    role="ref"} fields in the `Create Branches`{.interpreted-text
    role="guilabel"} window.

To create branches from a branch and create a multi-level architecture,
click `Add a line`{.interpreted-text role="guilabel"} in the new
branch\'s `Branches`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

Activate the `developer mode <developer-mode>`{.interpreted-text
role="ref"} to set `social media accounts
<../marketing/social_marketing>`{.interpreted-text role="doc"} and
company-specific `email <email_communication>`{.interpreted-text
role="doc"} system parameters.
:::

::: {.warning}
::: {.title}
Warning
:::

Adding a branch to a company enables
`multi-company <companies/multi_company>`{.interpreted-text role="doc"}
functions.
:::

### Comprehensive or branch-specific view {#general/companies/branches/consolidated-view}

::: {.note}
::: {.title}
Note
:::

Selecting the parent company automatically links all its branches, while
selecting a branch connects to that branch only. To switch between them,
use the `company selector
<general/multi-company/company-selector>`{.interpreted-text role="ref"}.
:::

All configurations, except for
`accounting <accounting/branches>`{.interpreted-text role="ref"}
settings inherited from the parent company, must be set individually per
branch. This allows for branch-specific setups such as
`loyalty programs <../sales/point_of_sale/pricing/loyalty>`{.interpreted-text
role="doc"}, `price lists
<../sales/point_of_sale/pricing/pricelists>`{.interpreted-text
role="doc"}, or `inventory locations
<../inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations>`{.interpreted-text
role="doc"}.

#### User access {#general/companies/branches/user-access}

Like in a multi-company environment, parent companies and branches
support flexible `user
access <users/multi-companies>`{.interpreted-text role="ref"} control
and `access rights <users/access_rights>`{.interpreted-text role="doc"}.
User access can be granted or restricted at the parent company level,
the branch level, or both. For example, a user can be limited to a
specific branch, while an administrator with access to the parent
company can manage all associated branches.

#### Shared records {#general/companies/branches/shared-records}

In Odoo, some records are, by default, either specific to a single
entity or shared across the parent company and all its branches.

When creating a quotation, invoice, or vendor bill, the active company
or branch is automatically selected and displayed in the
`Company`{.interpreted-text role="guilabel"} field. If the active
company is the parent company or one of its branches, then records
specifically linked to that entity are accessible only within that
entity and will only be visible when the company or branch is selected
using the `company
selector <general/multi-company/company-selector>`{.interpreted-text
role="ref"}.

In contrast, some records, such as `products or contacts
<general/multi-company/shared-and-unshared-records>`{.interpreted-text
role="ref"}, are not tied to any particular entity and are shared by
default across the parent company and all its branches. However, they
can be restricted to a single entity by setting the appropriate value in
the `Company`{.interpreted-text role="guilabel"} field, if needed.

::: {.seealso}
`Branches accounting <accounting/branches>`{.interpreted-text
role="ref"}
:::

#### Reporting {#general/companies/branches/reporting}

All `reports <../finance/accounting/reporting>`{.interpreted-text
role="doc"} can be generated for the parent company alone or with its
branches, based on
`user access <general/multi-company/user-access>`{.interpreted-text
role="ref"}.

::: {.toctree titlesonly=""}
companies/multi\_company companies/digest\_emails
companies/email\_template
:::
