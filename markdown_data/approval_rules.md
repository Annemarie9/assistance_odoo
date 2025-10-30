# File: /content/odoo_doc17.0/fr/content/applications/studio/approval_rules.md

Approval rules
==============

Approval rules are used to automate approval processes for actions. They
allow you to define the criteria for when an approval is required before
an action can be performed using a button.

Configuration
-------------

To add approval rules with Studio, proceed as follows:

1.  `Open Studio <studio/access>`{.interpreted-text role="ref"} and
    switch to the required `view <views>`{.interpreted-text role="doc"}.
2.  Select the button for which you want to add approval rules.
3.  In the `Properties`{.interpreted-text role="guilabel"} tab on the
    left, enable the `Set approval rules`{.interpreted-text
    role="guilabel"} feature.
4.  Specify the `Allowed Group`{.interpreted-text role="guilabel"} to
    limit the approval permission to a specific user group.
5.  Select the `Responsible`{.interpreted-text role="guilabel"} user to
    create an activity for a specific user when approval is requested
    from them.
6.  Select the `Users to notify`{.interpreted-text role="guilabel"} via
    internal note.
7.  Add a `Description`{.interpreted-text role="guilabel"} to be
    displayed in the
    `Approval dialog <approval-rules/use>`{.interpreted-text
    role="ref"}.

Optionally, you can also add conditions for the approval rule to be
applied by clicking the `fa-filter`{.interpreted-text role="icon"}
(`filter`{.interpreted-text role="guilabel"}) icon next to the
`Allowed Group`{.interpreted-text role="guilabel"} field.

To add another rule, click `Add an approval rule`{.interpreted-text
role="guilabel"}. When there are multiple approval rules, you can:

-   enable `Exclusive Approval`{.interpreted-text role="guilabel"} to
    require approvers to be different users;
-   change the `Notification Order`{.interpreted-text role="guilabel"}
    of the approval rule so that the `Responsible`{.interpreted-text
    role="guilabel"} and `Users to notify`{.interpreted-text
    role="guilabel"} are only notified when the previous rule has been
    approved, and their approval is required. If the approval rules have
    the same `Notification Order`{.interpreted-text role="guilabel"},
    all users are notified at the same time when the first approval is
    requested.

Click the `fa-trash`{.interpreted-text role="icon"}
(`trash`{.interpreted-text role="guilabel"}) icon next to the
`Allowed Group`{.interpreted-text role="guilabel"} field to delete the
approval rule.

::: {.tip}
::: {.title}
Tip
:::

You can create `user groups <access-rights/groups>`{.interpreted-text
role="ref"} specifically for approvals.
:::

Use {#approval-rules/use}
---

Once approval rules have been defined for a button:

-   A **user avatar** icon is displayed next to the button\'s label for
    each approval rule that has been defined.

    > 

-   When an unauthorized user clicks the button, an error message is
    displayed in the top-right corner and an activity is created for the
    user specified in the `Responsible`{.interpreted-text
    role="guilabel"} field.

-   Only users from the group defined in the
    `Allowed Group`{.interpreted-text role="guilabel"} field are
    authorized to approve or reject the action.

Authorized users can:

-   approve and perform the action by clicking the button;
-   approve the action and allow another user to perform it by clicking
    the **user avatar** icon next to the button\'s label, then clicking
    the `fa-check`{.interpreted-text role="icon"}
    (`Approve`{.interpreted-text role="guilabel"}) button in the dialog
    that opens;
-   reject the action by clicking the **user avatar** icon next to the
    button\'s label, then clicking the `fa-times`{.interpreted-text
    role="icon"} (`Reject`{.interpreted-text role="guilabel"}) button in
    the dialog that opens.



::: {.tip}
::: {.title}
Tip
:::

\- The user who approved/rejected the action can revoke their decision
by clicking the **user avatar** icon next to the button\'s label, then
clicking the `fa-undo`{.interpreted-text role="icon"}
(`Revoke`{.interpreted-text role="guilabel"}) button. - Approvals are
tracked in the record\'s chatter. An approval entry is also created
every time a Studio approval-related action is performed. To access the
approval entries, `activate
the developer mode </applications/general/developer_mode>`{.interpreted-text
role="doc"} and go to `Settings
--> Technical --> Studio Approval Entries`{.interpreted-text
role="menuselection"}.
:::
