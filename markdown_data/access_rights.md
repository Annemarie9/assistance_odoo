# File: /content/odoo_doc17.0/fr/content/applications/general/users/access_rights.md

Access rights
=============

*Access rights* are permissions that determine the content and
applications users can access and edit. In Odoo, these permissions can
be set for individual users or for groups of users. Limiting permissions
to only those who need them ensures that users do not modify or delete
anything they should not have access to.

**Only** an *administrator* can change access rights.

::: {.danger}
::: {.title}
Danger
:::

Making changes to access rights can have a detrimental impact on the
database. This includes *impotent admin*, which means that no user in
the database can make changes to the access rights. For this reason,
Odoo recommends contacting an Odoo Business Analyst, or our Support
Team, before making changes.
:::

::: {.tip}
::: {.title}
Tip
:::

A user **must** have the specific *Administration* access rights set on
their user profile, in order to make changes on another user\'s settings
for access rights.

To access this setting, navigate to
`Settings app --> Manage users --> select a
user --> Access Rights tab --> Administration section --> Administration field`{.interpreted-text
role="menuselection"}.

Once at the setting, an already existing administrator **must** change
the setting in the `Administration`{.interpreted-text role="guilabel"}
field to `Access Rights`{.interpreted-text role="guilabel"}.

Once complete, click `Save`{.interpreted-text role="guilabel"} to save
the changes, and implement the user as an administrator.
:::

Users
-----

The access rights for
`individual users <users/add-individual>`{.interpreted-text role="ref"}
are set when the user is added to the database, but they can be adjusted
at any point in the user\'s profile.

To make changes to a user\'s rights, click on the desired user to edit
their profile.

{.align-center}

On the user\'s profile page, in the `Access Rights`{.interpreted-text
role="guilabel"} tab, scroll down to view the current permissions.

For each app, use the drop-down menu to select what level of permission
this user should have. The options vary for each section, yet the most
common are: `Blank/None`{.interpreted-text role="guilabel"}, `User: Own
Documents`{.interpreted-text role="guilabel"},
`User: All Documents`{.interpreted-text role="guilabel"}, or
`Administrator`{.interpreted-text role="guilabel"}.

The `Administration`{.interpreted-text role="guilabel"} field in the
`Access Rights`{.interpreted-text role="guilabel"} tab has the following
options: `Settings`{.interpreted-text role="guilabel"} or
`Access Rights`{.interpreted-text role="guilabel"}.

{.align-center}

Create and modify groups {#access-rights/groups}
------------------------

*Groups* are app-specific sets of permissions that are used to manage
common access rights for a large amount of users. Administrators can
modify the existing groups in Odoo, or create new ones to define rules
for models within an application.

To access groups, first activate Odoo\'s
`developer mode <developer-mode>`{.interpreted-text role="ref"}, then go
to `Settings app --> Users & Companies --> Groups`{.interpreted-text
role="menuselection"}.

{.align-center}

To create a new group from the `Groups`{.interpreted-text
role="guilabel"} page, click `Create`{.interpreted-text
role="guilabel"}. Then, from the blank group form, select an
`Application`{.interpreted-text role="guilabel"}, and complete the group
form (detailed below).

To modify existing groups, click on an existing group from the list
displayed on the `Groups`{.interpreted-text role="guilabel"} page, and
edit the contents of the form.

Enter a `Name`{.interpreted-text role="guilabel"} for the group and tick
the checkbox next to `Share Group`{.interpreted-text role="guilabel"},
if this group was created to set access rights for sharing data with
some users.

::: {.important}
::: {.title}
Important
:::

Always test the settings being changed to ensure they are being applied
to the correct users.
:::

The group form contains multiple tabs for managing all elements of the
group. In each tab, click `Add a line`{.interpreted-text
role="guilabel"} to add a new row for users or rules, and click the
`❌ (remove)`{.interpreted-text role="guilabel"} icon to remove a row.

{.align-center}

-   `Users`{.interpreted-text role="guilabel"} tab: lists the current
    users in the group. Users listed in black have administrative
    rights. Users without administrative access appear in blue. Click
    `Add a
    line`{.interpreted-text role="guilabel"} to add users to this group.

-   `Inherited`{.interpreted-text role="guilabel"} tab: Inherited means
    that users added to this group are automatically added to the groups
    listed on this tab. Click `Add a line`{.interpreted-text
    role="guilabel"} to add inherited groups.

    ::: {.example}
    For example, if the group *Sales/Administrator* lists the group
    *Website/Restricted Editor* in its `Inherited`{.interpreted-text
    role="guilabel"} tab, then any users added to the
    *Sales/Administrator* group automatically receive access to the
    *Website/Restricted Editor* group, as well.
    :::

-   `Menus`{.interpreted-text role="guilabel"} tab: defines which models
    the group can have access to. Click `Add a line`{.interpreted-text
    role="guilabel"} to add a specific menu.

-   `Views`{.interpreted-text role="guilabel"} tab: lists which views in
    Odoo the group has access to. Click `Add a
    line`{.interpreted-text role="guilabel"} to add a view to the group.

-   `Access Rights`{.interpreted-text role="guilabel"} tab: lists the
    first level of rights (models) that this group has. The
    `Name`{.interpreted-text role="guilabel"} column represents the name
    for the current group\'s access to the model selected in the
    `Model`{.interpreted-text role="guilabel"} column.

    To link a new access right to a group, click
    `Add a line`{.interpreted-text role="guilabel"}. Select the
    appropriate model from the `Model`{.interpreted-text
    role="guilabel"} dropdown, then enter a name for the access right in
    the `Name`{.interpreted-text role="guilabel"} column. For each
    model, enable the following options as appropriate:

    -   `Read`{.interpreted-text role="guilabel"}: Users can see the
        object\'s existing values.
    -   `Write`{.interpreted-text role="guilabel"}: Users can edit the
        object\'s existing values.
    -   `Create`{.interpreted-text role="guilabel"}: Users can create
        new values for the object.
    -   `Delete`{.interpreted-text role="guilabel"}: Users can delete
        values for the object.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    While there are no conventions for naming access rights, it is
    advisable to choose a name that easily identifies its purpose.

    For example, the access that purchase managers have to the
    `Contact`{.interpreted-text role="guilabel"} model could be named
    [res.partner.purchase.manager]{.title-ref}. This consists of the
    technical name of the model, followed by a name identifying the
    group of users in question.

    

    To find the model\'s technical name from the current view, first
    enter a placeholder text in the `Name`{.interpreted-text
    role="guilabel"} field, then click the `Model`{.interpreted-text
    role="guilabel"} name, then the `fa-arrow-right`{.interpreted-text
    role="icon"} `(Internal link)`{.interpreted-text role="guilabel"}
    icon.
    :::

-   `Record Rules`{.interpreted-text role="guilabel"}: lists the second
    layer of editing and visibility rights.
    `Record Rules`{.interpreted-text role="guilabel"} overwrite, or
    refine, the group\'s access rights. Click `Add a
    line`{.interpreted-text role="guilabel"} to add a record rule to
    this group. For each rule, choose values for the following options:

    -   `Apply for Read`{.interpreted-text role="guilabel"}.
    -   `Apply for Write`{.interpreted-text role="guilabel"}.
    -   `Apply for Create`{.interpreted-text role="guilabel"}.
    -   `Apply for Delete`{.interpreted-text role="guilabel"}.

    ::: {.important}
    ::: {.title}
    Important
    :::

    Record rules are written using a *domain*, or conditions that filter
    data. A domain expression is a list of such conditions. For example:

    [\[(\'mrp\_production\_ids\', \'in\',
    user.partner\_id.commercial\_partner\_id.production\_ids.ids)\]]{.title-ref}

    This record rule is to enable MRP consumption warnings for
    subcontractors.

    Odoo has a library of preconfigured record rules for ease of use.
    Users without knowledge of domains (and domain expressions) should
    consult an Odoo Business Analyst, or the Odoo Support Team, before
    making changes.
    :::

Superuser mode {#access-rights/superuser}
--------------

*Superuser mode* allows the user to bypass record rules and access
rights. To activate *Superuser mode*, first, activate
`developer mode <developer-mode>`{.interpreted-text role="ref"}. Then,
navigate to the *debug* menu, represented by a
`🪲 (bug)`{.interpreted-text role="guilabel"} icon, located in the top
banner.

Finally, towards the bottom of the menu, click
`Become Superuser`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Only users with *Settings* access for the *Administration* section of
the *Access Rights* (in their user profile) are allowed to log in to
*Superuser mode*.
:::

::: {.danger}
::: {.title}
Danger
:::

*Superuser mode* allows for circumvention of record rules and access
rights, and therefore, should be exercised with extreme caution.

Upon exiting *Superuser mode*, users may be locked out of the database,
due to changes that were made. This can cause *impotent admin*, or an
administrator without the ability to change access rights/settings.

In this case contact Odoo Support here: [new help
ticket](https://www.odoo.com/help). The support team is able to restore
access using a support login.
:::

To leave *Superuser mode*, log out of the account, by navigating to the
upper-right corner, and clicking on the `OdooBot`{.interpreted-text
role="guilabel"} username. Then, select the `Log out`{.interpreted-text
role="guilabel"} option.

::: {.tip}
::: {.title}
Tip
:::

An alternative way to activate *Superuser mode* is to login as a
superuser. To do that, navigate to the login screen, and enter the
appropriate `Email`{.interpreted-text role="guilabel"} and
`Password`{.interpreted-text role="guilabel"}.

Instead of clicking `Login`{.interpreted-text role="guilabel"}, click
`Log in as superuser`{.interpreted-text role="guilabel"}.
:::
