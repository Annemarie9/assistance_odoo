# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch/user-accounts.md

Manage user accounts
====================

In Odoo\'s *Lunch* application, users pay for products directly from
their *Lunch* app account. For funds to appear in their account, a
*Lunch* app manager **must** transfer funds into each user\'s account.

::: {.important}
::: {.title}
Important
:::

To add funds and manage user accounts, the user must have
`Administrator`{.interpreted-text role="guilabel"} access rights set for
the *Lunch* application. This is verified by navigating to `Settings app
--> → Manage Users`{.interpreted-text role="menuselection"}. Then, click
on a user to view their various settings and access rights.

For more information, refer to the
`Access rights <../../general/users/access_rights/>`{.interpreted-text
role="doc"} documentation.
:::

The *Lunch* application does **not** directly interface in any way with
software or products linked to any monetary accounts or billing. Money
**cannot** be transferred from users\' bank accounts, nor can users\'
credit cards be charged.

Odoo\'s *Lunch* application **only** allows for manual entries of cash
exchanges that are handled by the *Lunch* app manager. It is up to each
individual company to create the method with which lunch accounts are
replenished.

::: {.example}
Some examples of how money can be organized and transferred within a
company:

-   Cash is handed to the *Lunch* app manager, who then updates the
    user\'s account.
-   Money is automatically deducted from the user\'s paychecks, then the
    *Lunch* app manager updates the account when paychecks are issued.
    This requires `adding a salary attachment
    <payroll/worked-days-inputs>`{.interpreted-text role="ref"} for the
    user\'s payslip in the *Payroll* app.
-   Companies can sell \"lunch tickets\" at a set price (for example,
    one ticket costs \$5.00). Users can purchase tickets from a *Lunch*
    app manager, who then updates the user\'s account.
:::

Cash Moves {#lunch/cash-moves}
----------

To add funds to user accounts, each cash move must be individually
logged. To view all cash move records, or create a new cash move,
navigate to `Lunch app --> Manager --> Cash
Moves`{.interpreted-text role="menuselection"}. Doing so reveals the
`Cash Moves`{.interpreted-text role="guilabel"} dashboard.

On the `Cash Moves`{.interpreted-text role="guilabel"} dashboard, all
cash moves are presented in a default list view, displaying each
record\'s `Date`{.interpreted-text role="guilabel"},
`User`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and
`Amount`{.interpreted-text role="guilabel"}. The total of all the cash
moves is displayed at the bottom of the `Amount`{.interpreted-text
role="guilabel"} column.

{.align-center}

### Add funds

To add funds to a lunch account, click the `New`{.interpreted-text
role="guilabel"} button, located in the top-left corner of the
`Cash Moves`{.interpreted-text role="guilabel"} dashboard.

A blank `Cash Moves`{.interpreted-text role="guilabel"} form loads.
Enter the following information on the form:

-   `User`{.interpreted-text role="guilabel"}: select the user
    depositing cash into their account from the drop-down menu. If the
    user is not in the database, they can be created by typing their
    name in the `User`{.interpreted-text role="guilabel"} field, and
    clicking either `Create "user"`{.interpreted-text role="guilabel"}
    or `Create and edit...`{.interpreted-text role="guilabel"} to create
    the user and edit the `Create User`{.interpreted-text
    role="guilabel"} form.
-   `Date`{.interpreted-text role="guilabel"}: using the calendar
    popover, select the date the transaction occurred.
-   `Amount`{.interpreted-text role="guilabel"}: enter the amount being
    added to the lunch account.
-   `Description`{.interpreted-text role="guilabel"}: enter a brief
    description of the transaction.

{.align-center}

Control Accounts
----------------

An overview of every transaction in the *Lunch* app, including all cash
deposits and purchases, can be viewed on the main *Control Accounts*
dashboard. To access this dashboard, navigate to
`Lunch app --> Manager --> Control Accounts.`{.interpreted-text
role="menuselection"}

All transactions are grouped `By Employee`{.interpreted-text
role="guilabel"}, and listed alphabetically by the user\'s first name.
At the end of the user\'s name, a number appears. This indicates the
number of individual records logged for that user.

The default view is to have all individual transactions hidden. To view
all transactions for a user, click the `▶ (triangle)`{.interpreted-text
role="guilabel"} icon to the left of the desired name to expand that
specific group.

Each record includes the `Date`{.interpreted-text role="guilabel"},
`User`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and
`Amount`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

This list only displays the various transactions within the *Lunch* app,
and does **not** allow modifications to be made to any records listed.

Cash moves can be modified, but **only** from the
`Cash Moves <lunch/cash-moves>`{.interpreted-text role="ref"} dashboard,
not from the `Control Accounts`{.interpreted-text role="guilabel"}
dashboard.

It is **not** possible to modify any product-related records.
:::
