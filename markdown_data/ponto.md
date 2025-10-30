# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/bank/bank_synchronization/ponto.md

Ponto
=====

**Ponto** is a service that allows companies and professionals to
aggregate their accounts in one place and directly see all their
transactions within one app. It is a third-party solution that is
continuously expanding the number of bank institutions that can be
synchronized with Odoo.

**Odoo** can synchronize directly with your bank to get all bank
statements imported automatically into your database.

Ponto is a paid third-party provider that can handle the synchronization
between your bank accounts and Odoo.

::: {.seealso}
\- `../bank_synchronization`{.interpreted-text role="doc"} -
`../transactions`{.interpreted-text role="doc"}
:::

Configuration
-------------

### Link your bank accounts with Ponto

1.  Go to .

2.  Create an account if you don\'t have one yet.

3.  Once you are logged in, create an *organization*.

    

4.  Go to `Accounts --> Live`{.interpreted-text role="menuselection"},
    and click `Add account`{.interpreted-text role="guilabel"}. You
    might have to add your **Billing Information** first.

5.  Select your country, your bank institutions, give your consent to
    Ponto, and follow the steps on-screen to link your bank account with
    your Ponto account.

    

6.  Add all bank accounts you want to synchronize with your Odoo
    database and move to the next steps.

### Link your Ponto account with your Odoo database

1.  Go to
    `Accounting --> Configuration --> Add a Bank Account`{.interpreted-text
    role="menuselection"}.

2.  Search for your institution and select it so you can verify that the
    third party provider is Ponto.

3.  Click `Connect`{.interpreted-text role="guilabel"} and follow the
    steps.

4.  Select **all accounts** you want to access and synchronize in Odoo,
    even the ones coming from other banking institutions.

    

5.  Finish the flow.

::: {.note}
::: {.title}
Note
:::

You have to authorize all the accounts you want to access in Odoo, but
Odoo will filter the accounts based on the institution you selected in
the second step.
:::

### Update your synchronization credentials

To update your Ponto credentials or modify the synchronization settings,
activate the `developer mode <developer-mode>`{.interpreted-text
role="ref"}, go to `Accounting --> Configuration -->
Online Synchronization`{.interpreted-text role="menuselection"}, and
select the institution from which you want to fetch the other accounts.
Click `Fetch Accounts`{.interpreted-text role="guilabel"} to start the
flow.

::: {.note}
::: {.title}
Note
:::

During the update, select **all accounts** you want to synchronize, even
the ones coming from other banking institutions.
:::

### Fetch new accounts

To add new online accounts to your connection, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}, go to
`Accounting --> Configuration --> Online Synchronization`{.interpreted-text
role="menuselection"}, and select the institution from which you want to
fetch the other accounts. Click `Fetch Accounts`{.interpreted-text
role="guilabel"} to start the flow.

::: {.note}
::: {.title}
Note
:::

Don\'t forget to keep authorization for existing accounts (for all
institutions that you have synchronized with Ponto).
:::

FAQ
---

### After my synchronization, no account appears

You selected an institution from the list and did not authorize any
accounts from this institution.

### I have an error about that my authorization has expired

Every **6 months** (180 days) you must re-authorize the connection
between your bank account and Ponto. This must be done from the [Ponto
website](https://myponto.com). If you do not do this, the
synchronization will stop for these accounts.

### I have some errors with my beta institution

Ponto provides institutions in *beta*, these institutions are not
directly supported by Odoo and we advise you to contact Ponto directly.

::: {.important}
::: {.title}
Important
:::

Using an institution in beta is beneficial for Ponto, it allows them to
have real feedback on the connection with the institution.
:::
