# File: /content/odoo_doc17.0/fr/content/applications/general/users/ldap.md

LDAP authentication
===================

To configure
`LDAP (Lightweight Directory Access Protocol)`{.interpreted-text
role="abbr"} authentication in Odoo:

1.  Open the Settings app, scroll down to the
    `Integrations`{.interpreted-text role="guilabel"} section, and
    enable `LDAP Authentication`{.interpreted-text role="guilabel"}.
2.  Click `Save`{.interpreted-text role="guilabel"}, then go back to the
    `Integrations`{.interpreted-text role="guilabel"} section and click
    `LDAP Server`{.interpreted-text role="guilabel"}.
3.  In the `Set up your LDAP Server`{.interpreted-text role="guilabel"}
    list, click `New`{.interpreted-text role="guilabel"}, then select
    the required company in the dropdown list.
4.  In the `Server information`{.interpreted-text role="guilabel"}
    section, enter the server\'s IP address and port in the
    `LDAP server address`{.interpreted-text role="guilabel"} and
    `LDAP Server port`{.interpreted-text role="guilabel"} fields,
    respectively.
5.  Enable `Use TLS`{.interpreted-text role="guilabel"} to request
    secure TLS/SSL encryption when connecting to the LDAP server,
    providing the server has StartTLS enabled.
6.  In the `Login information`{.interpreted-text role="guilabel"}
    section, enter the ID and password of the account used to query the
    server in the `LDAP binddn`{.interpreted-text role="guilabel"} and
    `LDAP password`{.interpreted-text role="guilabel"} fields,
    respectively. If the fields are left empty, the server will perform
    the query anonymously.
7.  In the `Process parameter`{.interpreted-text role="guilabel"}
    section, enter:
    -   the LDAP server\'s name in the `LDAP base`{.interpreted-text
        role="guilabel"} field using LDAP format (e.g.,
        `dc=example,dc=com`);
    -   `uid=%s` in the `LDAP filter`{.interpreted-text role="guilabel"}
        field.
8.  In the `User information`{.interpreted-text role="guilabel"}
    section:
    -   Enable `Create user`{.interpreted-text role="guilabel"} to
        create a user profile in Odoo the first time someone logs in
        using LDAP;
    -   Select the `User template`{.interpreted-text role="guilabel"} to
        be used to create the new user profiles. If no template is
        selected, the administrator\'s profile is used.

::: {.note}
::: {.title}
Note
:::

When using Microsoft Active Directory (AD) for LDAP authentication, if
users experience login issues despite using valid credentials, create a
new system parameter to disable referral chasing in the LDAP client:

1.  `Activate the developer mode. <developer-mode>`{.interpreted-text
    role="ref"}
2.  Go to
    `Settings --> Technical --> System Parameters`{.interpreted-text
    role="menuselection"} and click `New`{.interpreted-text
    role="guilabel"}.
3.  Fill in the fields:
    -   `Key`{.interpreted-text role="guilabel"}:
        `auth_ldap.disable_chase_ref`
    -   `Value`{.interpreted-text role="guilabel"}: `True`
:::
