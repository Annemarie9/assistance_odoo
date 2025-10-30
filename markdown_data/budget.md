# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/budget.md

Analytic budgets
================

Managing budgets is an essential part of running a business. Budgets
help people become more intentional with how money is spent and direct
people to organize and prioritize their work to meet financial goals.
They allow the planning of a desired financial outcome and then measure
the actual performance against the plan. Odoo manages budgets using both
**general** and **analytic accounts**.

Configuration
-------------

Go to
`Accounting --> Configuration --> Settings --> Analytics section`{.interpreted-text
role="menuselection"}, and enable `Budget Management`{.interpreted-text
role="guilabel"}.

### Budgetary positions

Budgetary positions are lists of accounts for which you want to keep
budgets (typically expense or income accounts).

To define budgetary positions, go to
`Accounting --> Configuration --> Management:
Budgetary Positions`{.interpreted-text role="menuselection"} and
`New`{.interpreted-text role="guilabel"}. Add a `Name`{.interpreted-text
role="guilabel"} to your budgetary position and select the
`Company`{.interpreted-text role="guilabel"} it applies to. Click
`Add a line`{.interpreted-text role="guilabel"} to add one or more
accounts.

::: {.note}
::: {.title}
Note
:::

Each budgetary position can have any number of accounts from the chart
of accounts, though it must have at least one.
:::

Use case
--------

Let's illustrate this with an example.

We just started a project with *Smith & Co*, and we would like to budget
the income and expenses of that project. We plan on having a revenue of
1000, and we don't want to spend more than 700.

First, we need to define what accounts relate to our project's expenses.
Go to
`Accounting --> Configuration --> Management: Budgetary positions`{.interpreted-text
role="menuselection"}, and click `New`{.interpreted-text
role="guilabel"} to add a position. Add the accounts wherein expenses
will be booked.

{.align-center}

Let\'s repeat the steps to create a budgetary position that reflects the
revenue.

{.align-center}

### Analytical accounts

Odoo needs to know which costs or expenses are relevant to a specified
budget, as the above general accounts may be used for different
projects. Go to `Accounting --> Configuration -->
Analytic Accounting: Analytic Accounts`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text role="guilabel"}
to add a new **Analytic Account** called *Smith & Co*.

The `Plan`{.interpreted-text role="guilabel"} field has to be completed.
Plans group multiple analytic accounts; they distribute costs and
benefits to analyze business performance. **Analytic Plans** can be
created or configured by going to
`Accounting --> Configuration --> Analytic Accounting:
Analytic Plans`{.interpreted-text role="menuselection"}.

When creating a new customer invoice and/or vendor bill, you have to
refer to this analytic account.

{.align-center}

### Define the budget

Let's set our targets. We specified that we expect to gain 1000 with
this project, and we would like not to spend more than 700. Go to
`Accounting --> Management: Budgets`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text role="guilabel"}
to create a new budget for *Smith & Co* project.

First, fill in your `Budget Name`{.interpreted-text role="guilabel"}.
Then, select the `Period`{.interpreted-text role="guilabel"} wherein the
budget is applicable. Next, add the
`Budgetary Position`{.interpreted-text role="guilabel"} you want to
track, define the related `Analytic Account`{.interpreted-text
role="guilabel"}, and add the `Planned Amount`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When recording a planned amount related to expenses, the amount must be
negative.
:::

### Check your budget

Go to `Accounting --> Management: Budgets`{.interpreted-text
role="menuselection"} and find the *Smith & Co* Project to see how it
evolves according to the expenses or income for the related analytic
account.

The `Practical Amount`{.interpreted-text role="guilabel"} evolves when a
new journal entry related to your analytic account and an account from
your budgetary position is created.

The `Theoretical Amount`{.interpreted-text role="guilabel"} represents
the amount of money you theoretically could have spent or should have
received based on the date. For example, suppose your budget is 1200 for
12 months (January to December), and today is 31 of January. In that
case, the theoretical amount will be 100 since this is the actual amount
that could have been made.
