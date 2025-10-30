# File: /content/odoo_doc17.0/fr/content/applications/general/users/2fa.md

Two-factor authentication
=========================

*Two-factor authentication (2FA)* is a way to improve security, and
prevent unauthorized persons from accessing user accounts.

Practically, `2FA (two-factor authentication)`{.interpreted-text
role="abbr"} means storing a secret inside an *authenticator*, usually
on a mobile phone, and exchanging a code from the authenticator when
trying to log in.

This means an unauthorized user would need to guess the account password
*and* have access to the authenticator, which is a more difficult
proposition.

Requirements
------------

::: {.important}
::: {.title}
Important
:::

These lists are just examples. They are **not** endorsements of any
specific software.
:::

Phone-based authenticators are the easiest and most commonly used.
Examples include:

-   
-   
-   [Google
    Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)
-   
-   [Microsoft
    Authenticator](https://www.microsoft.com/en-gb/account/authenticator?cmp=h66ftb_42hbak)

Password managers are another option. Common examples include:

-   
-   ,

::: {.note}
::: {.title}
Note
:::

The remainder of this document uses Google Authenticator as an example,
as it is one of the most commonly used. This is **not** an endorsement
of the product.
:::

Two-factor authentication setup
-------------------------------

After selecting an authenticator, log in to Odoo, then click the profile
avatar in the upper-right corner, and select
`My Profile`{.interpreted-text role="guilabel"} from the resulting
drop-down menu.

Click the `Account Security`{.interpreted-text role="guilabel"} tab,
then slide the `Two-Factor Authentication`{.interpreted-text
role="guilabel"} toggle to *active*.

{.align-center}

This generates a `Security Control`{.interpreted-text role="guilabel"}
pop-up window that requires password confirmation to continue. Enter the
appropriate password, then click `Confirm Password`{.interpreted-text
role="guilabel"}. Next, a
`Two-Factor Authentication Activation`{.interpreted-text
role="guilabel"} pop-up window appears, with a
`QR (Quick Response)`{.interpreted-text role="abbr"} code.

{.align-center}

Using the desired authenticator application, scan the
`QR (Quick Response)`{.interpreted-text role="abbr"} code when prompted.

::: {.tip}
::: {.title}
Tip
:::

If scanning the screen is not possible (e.g. the setup is being
completed on the *same* device as the authenticator application),
clicking the provided `Cannot scan it?`{.interpreted-text
role="guilabel"} link, or copying the secret to manually set up the
authenticator, is an alternative.

{.align-center}

{.align-center}
:::

Afterwards, the authenticator should display a *verification code*.

{.align-center}

Enter the code into the `Verification Code`{.interpreted-text
role="guilabel"} field, then click `Activate`{.interpreted-text
role="guilabel"}.

{.align-center}

Logging in
----------

To confirm `2FA (two-factor authentication)`{.interpreted-text
role="abbr"} setup is complete, log out of Odoo.

On the login page, input the username and password, then click
`Log in`{.interpreted-text role="guilabel"}. On the
`Two-factor Authentication`{.interpreted-text role="guilabel"} page,
input the code provided by the chosen authenticator in the
`Authentication Code`{.interpreted-text role="guilabel"} field, then
click `Log in`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.danger}
::: {.title}
Danger
:::

If a user loses access to their authenticator, an administrator **must**
deactivate `2FA (two-factor authentication)`{.interpreted-text
role="abbr"} on the account before the user can log in.
:::

Enforce two-factor authentication
---------------------------------

To enforce the use of
`2FA (two-factor authentication)`{.interpreted-text role="abbr"} for all
users, first navigate to `Main Odoo Dashboard -->
Apps`{.interpreted-text role="menuselection"}. Remove the
`Apps`{.interpreted-text role="guilabel"} filter from the
`Search...`{.interpreted-text role="guilabel"} bar, then search for [2FA
by mail]{.title-ref}.

Click `Install`{.interpreted-text role="guilabel"} on the Kanban card
for the `2FA by mail`{.interpreted-text role="guilabel"} module.

{.align-center}

After installation is complete, go to
`Settings app: Permissions`{.interpreted-text role="guilabel"}. Tick the
checkbox labeled, `Enforce two-factor authentication`{.interpreted-text
role="guilabel"}. Then, use the radio buttons to choose whether to apply
this setting to `Employees only`{.interpreted-text role="guilabel"}, or
`All users`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Selecting `All users`{.interpreted-text role="guilabel"} applies the
setting to portal users, in addition to employees.
:::

{.align-center}

Click `Save`{.interpreted-text role="guilabel"} to commit any unsaved
changes.
