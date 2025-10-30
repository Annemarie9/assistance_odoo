# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/analytic_accounting.md

Analytic accounting
===================

Analytic accounting helps track costs and revenues and analyze a
project\'s or service\'s profitability. When creating journal entries,
costs can be `distributed
<accounting/analytic_accounting/analytic-distribution>`{.interpreted-text
role="ref"} across one or more analytic accounts.

To activate this feature, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and enable `Analytic Accounting`{.interpreted-text
role="guilabel"} in the `Analytics`{.interpreted-text role="guilabel"}
section.

::: {.seealso}
`Analytic budget <budget>`{.interpreted-text role="doc"}
:::

Analytic accounts {#accounting/analytic_accounting/analytic_accounts}
-----------------

Analytic accounts give an overview of costs and revenue.

To access analytic accounts, go to
`Accounting --> Configuration --> Analytic
Accounts`{.interpreted-text role="menuselection"}. To create a new
analytic account, click `New`{.interpreted-text role="guilabel"} and
fill in the following information:

-   `Analytic Account`{.interpreted-text role="guilabel"}: Assign the
    name of the analytic account.
-   `Customer`{.interpreted-text role="guilabel"}: Select the customer
    linked to the project, if applicable.
-   `Reference`{.interpreted-text role="guilabel"}: Include a reference
    to make the account easier to find if needed.
-   `Plan`{.interpreted-text role="guilabel"}: Link the
    `Analytic Account`{.interpreted-text role="guilabel"} to an
    `analytic plan
    <accounting/analytic_accounting/analytic_plans>`{.interpreted-text
    role="ref"}.
-   `Company`{.interpreted-text role="guilabel"}: In a
    `multi-company </applications/general/companies/multi_company>`{.interpreted-text
    role="doc"} environment, select the company using the analytic
    account. To make the analytic account accessible to all companies,
    leave the field empty.
-   `Currency`{.interpreted-text role="guilabel"}: Update the currency
    of the analytic account if needed.

Then, the `budget <budget>`{.interpreted-text role="doc"} information
can be filled in.

Analytic plans {#accounting/analytic_accounting/analytic_plans}
--------------

Analytic plans group
`analytic accounts <accounting/analytic_accounting/analytic_accounts>`{.interpreted-text
role="ref"}, allowing the company to analyze its accounting, such as
tracking costs and revenues by project or department.

To access analytic plans, go to
`Accounting --> Configuration --> Analytic Plans`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a new plan, add a name, and fill in the following information:

-   `Parent`{.interpreted-text role="guilabel"}: Link the plan to
    another analytic plan if a hierarchy between plans must be built.
-   `Default Applicability`{.interpreted-text role="guilabel"}: Define
    how the plan is applied when creating a new journal entry:
    -   `Optional`{.interpreted-text role="guilabel"}: Adding the
        analytic plan is not mandatory.
    -   `Mandatory`{.interpreted-text role="guilabel"}: The entry cannot
        be confirmed if no analytic account is selected.
    -   `Unavailable`{.interpreted-text role="guilabel"}: The plan is
        not available.
-   `Color`{.interpreted-text role="guilabel"}: Set a color for the tag
    related to this specific plan.

To fine-tune a plan\'s applicability, create a new line in the
`Applicability`{.interpreted-text role="guilabel"} tab and set the
following fields:

-   `Domain`{.interpreted-text role="guilabel"}: Choose the accounting
    documents to which the plan applies.
-   `Financial Accounts Prefix`{.interpreted-text role="guilabel"}:
    Enter the prefix of the account(s) to which the plan applies.
-   `Product Category`{.interpreted-text role="guilabel"}: Choose the
    product category to which the plan applies.
-   `Applicability`{.interpreted-text role="guilabel"}: Define how the
    plan is applied when creating a new journal entry. The applicability
    set here always overrides the default applicability.
-   `Company`{.interpreted-text role="guilabel"}: In a
    `multi-company </applications/general/companies/multi_company>`{.interpreted-text
    role="doc"} environment, select the company using the plan. To make
    the analytic plan accessible to all companies, leave the field
    empty.

Two smart buttons are available:

-   `Subplans`{.interpreted-text role="guilabel"}: To have a more
    complex analytic structure. Click the smart button, then click
    `New`{.interpreted-text role="guilabel"} to add a subplan. This
    creates a parent-child relationship between the two plans, and the
    `Parent`{.interpreted-text role="guilabel"} field of the subplan is
    automatically populated with the original plan.
-   `Analytic Accounts`{.interpreted-text role="guilabel"}: To access
    the `analytic accounts
    <accounting/analytic_accounting/analytic_accounts>`{.interpreted-text
    role="ref"} linked to the plan.

::: {.note}
::: {.title}
Note
:::

Each analytic plan must have at least one analytic account.
:::

Analytic distribution {#accounting/analytic_accounting/analytic-distribution}
---------------------

The distribution of costs in one or more analytic accounts can be set in
each `invoice/bill
<accounting/analytic_accounting/distribution-invoices-bills>`{.interpreted-text
role="ref"} or `en masse
<accounting/analytic_accounting/distribution-mass>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

The analytic distribution is prefilled based on the applicability and
the `analytic
distribution models <accounting/analytic_distribution_models>`{.interpreted-text
role="ref"}.
:::

### Analytic distribution on invoices or bills {#accounting/analytic_accounting/distribution-invoices-bills}

To add analytic distribution, click the
`Analytic Distribution`{.interpreted-text role="guilabel"} column when
creating an `invoice <accounting/invoice/creation>`{.interpreted-text
role="ref"} or
`bill <accounting/vendor_bills/creation>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

The `Analytic Distribution`{.interpreted-text role="guilabel"} field is
mandatory only if the `analytic plan
<accounting/analytic_accounting/analytic_plans>`{.interpreted-text
role="ref"} has been set as `Mandatory`{.interpreted-text
role="guilabel"} in either the `Default Applicability`{.interpreted-text
role="guilabel"} field on an analytic plan or the
`Applicability`{.interpreted-text role="guilabel"} field on an analytic
plan line.
:::

In the `Analytic`{.interpreted-text role="guilabel"} window, select the
desired `Analytic Accounts`{.interpreted-text role="guilabel"} in the
different `Analytic Plans`{.interpreted-text role="guilabel"} displayed
in columns. Then, split the costs between the accounts by modifying the
percentage.



### Analytic distribution en masse {#accounting/analytic_accounting/distribution-mass}

To mass-edit analytic accounts in several entries simultaneously, go to
`Accounting
--> Accounting --> Journal items`{.interpreted-text
role="menuselection"}, and select the ones that need to be updated.
Click the `Analytic Distribution`{.interpreted-text role="guilabel"}
column and add the required distribution in the
`Analytic`{.interpreted-text role="guilabel"} column, then click the
`oi-close`{.interpreted-text role="icon"} `(cross)`{.interpreted-text
role="guilabel"} and `Confirm`{.interpreted-text role="guilabel"}. The
analytic distribution is then added to the selected journal items.

### Analytic distribution models {#accounting/analytic_distribution_models}

Analytic distribution models automatically apply a specific distribution
based on defined criteria.

To create a new analytic distribution model, go to
`Accounting --> Configuration -->
Analytic Distribution Models`{.interpreted-text role="menuselection"},
click `New`{.interpreted-text role="guilabel"}, and set the conditions
the model has to meet to apply automatically:

::: {.note}
::: {.title}
Note
:::

All specified conditions of an analytic distribution model must be met
for the model to be applied. To apply an analytic distribution model
based on individual conditions, create separate analytic distribution
models for each condition.
:::

-   `Accounts Prefix`{.interpreted-text role="guilabel"}: Apply the
    distribution model only to journal items involving an account that
    begins with a specific prefix.
-   `Partner`{.interpreted-text role="guilabel"}: Apply the distribution
    model only to journal items involving a specific partner.
-   `Product`{.interpreted-text role="guilabel"}: Apply the distribution
    model only to journal items involving a specific product.
-   `Company`{.interpreted-text role="guilabel"}: In a
    `multi-company </applications/general/companies/multi_company>`{.interpreted-text
    role="doc"} environment, apply the distribution model only to
    journal items involving a specific company. To apply it across all
    companies, leave the field empty.
-   `Analytic Distribution`{.interpreted-text role="guilabel"}:
    `Analytic distribution
    <accounting/analytic_accounting/analytic-distribution>`{.interpreted-text
    role="ref"} that will be applied when the above conditions are met.

::: {.example}
Any time a journal item is posted to the
`Utilities (601000)`{.interpreted-text role="guilabel"} account, it
should be automatically distributed in the
`Departments`{.interpreted-text role="guilabel"} analytic plan as
follows:

-   60% to the `Manufacturing`{.interpreted-text role="guilabel"}
    analytic account
-   30% to the `Marketing`{.interpreted-text role="guilabel"} analytic
    account
-   10% to the `Admin`{.interpreted-text role="guilabel"} analytic
    account

To automate this distribution, the `Accounts Prefix`{.interpreted-text
role="guilabel"} can be set to [601]{.title-ref}, as
`Utilities (601000)`{.interpreted-text role="guilabel"} is the only
account in the chart of accounts that begins with [601]{.title-ref}.

If additional accounts such as `Electricity (601100)`{.interpreted-text
role="guilabel"} or `Gas (601200)`{.interpreted-text role="guilabel"}
are available in the chart of accounts, the distribution will also apply
to both since they share the same prefix.
:::

To define more criteria, use the `oi-settings-adjust`{.interpreted-text
role="icon"} `(adjust settings)`{.interpreted-text role="guilabel"} icon
to reveal more columns or click `View`{.interpreted-text
role="guilabel"} on an individual analytic distribution model.

-   `Partner Category`{.interpreted-text role="guilabel"}: Apply this
    distribution model only to journal items involving a partner in a
    specific category.
-   `Product Category`{.interpreted-text role="guilabel"}: Apply this
    distribution model to journal items involving a product in a
    specific category.

::: {.tip}
::: {.title}
Tip
:::

Alternatively, it is possible to create an analytic distribution model
from the `Analytic`{.interpreted-text role="guilabel"} window by
clicking `New Model`{.interpreted-text role="guilabel"}:

-   either when creating an invoice/bill and filling in the
    `analytic distribution
    <accounting/analytic_accounting/distribution-invoices-bills>`{.interpreted-text
    role="ref"};
-   or when `mass-editing analytic accounts
    <accounting/analytic_accounting/distribution-mass>`{.interpreted-text
    role="ref"} in several entries simultaneously.
:::
