CRM Gamification
================

In Odoo\'s *CRM* app, *gamification tools* provide the opportunity to
evaluate and motivate users through customizable challenges, goals, and
rewards. Goals are created to target actions within the *CRM* app, and
can be tracked and rewarded automatically to participating sales teams.

Configuration
-------------

To install the *CRM Gamification* module, navigate to the
`Apps`{.interpreted-text role="menuselection"} application. Click into
the `Search...`{.interpreted-text role="guilabel"} bar at the top of the
page and remove the `Apps`{.interpreted-text role="guilabel"} filter.
Type [CRM Gamification]{.title-ref} to search.

On the `CRM Gamification`{.interpreted-text role="guilabel"} module,
click `Install`{.interpreted-text role="guilabel"}. This module features
goals and challenges related to the *CRM* and *Sales* applications.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If **both** the *CRM* and *Sales* apps are installed, the *CRM
Gamification* module is automatically installed on the database.
:::

To access the *Gamification Tools* menu, first enable
`developer-mode`{.interpreted-text role="ref"}.

Next, navigate to
`Settings app --> Gamification Tools`{.interpreted-text
role="menuselection"}.

{.align-center}

Create badges {#crm/create-rewards}
-------------

*Badges* are awarded to users when they have completed a challenge.
Different badges can be awarded based on the type of task completed, and
can be issued to more than one user, depending on the time they
accomplish the goal.

To view the existing badges, or create a new one, navigate to
`Settings -->
Gamification Tools --> Badges`{.interpreted-text role="menuselection"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Some badges can be awarded outside of challenges, as well. Select the
Kanban card for the desired badge, then click `Grant`{.interpreted-text
role="guilabel"}. This opens a `Grant Badge`{.interpreted-text
role="guilabel"} pop-up window. Select a user from the
`Who would you like to reward?`{.interpreted-text role="guilabel"}
field.

Add any additional information regarding why the user is receiving the
reward in the field below, then click `Grant Badge`{.interpreted-text
role="guilabel"}.
:::

To create a new badge, click `New`{.interpreted-text role="guilabel"} at
the top-left of the page to open a blank form. Enter a name for the
`Badge`{.interpreted-text role="guilabel"}, followed by a description.

The `Allowance to Grant`{.interpreted-text role="guilabel"} field
determines when a badge can be granted, and by whom:

-   `Everyone`{.interpreted-text role="guilabel"}: this badge can be
    manually granted by any user.
-   `A selected list of users`{.interpreted-text role="guilabel"}: this
    badge can only be granted by a select group of users. If this option
    is selected, it generates a new field,
    `Authorized Users`{.interpreted-text role="guilabel"}. Choose the
    appropriate users from this drop-down list.
-   `People having some badges`{.interpreted-text role="guilabel"}: this
    badge can only be granted by users who have already been awarded a
    specific badge. If this option is selected it generates a new field,
    `Required Badges`{.interpreted-text role="guilabel"}. Use this
    drop-down list to select the badge(s) a user must have before they
    can award this badge to others.
-   `No one, assigned through challenges`{.interpreted-text
    role="guilabel"}: this badge cannot be manually granted, it can only
    be awarded through challenges.

To limit the number of badges a user can send, tick the
`Monthly Limited Spending`{.interpreted-text role="guilabel"} checkbox.
This sets a limit on the number of times a user can grant this badge. In
the `Limitation Number`{.interpreted-text role="guilabel"} field, enter
the maximum number of times this badge can be sent per month, per
person.

{.align-center}

Create a challenge {#crm/create-challenge}
------------------

To create a challenge, navigate to to
`Settings --> Gamification Tools -->
Challenges`{.interpreted-text role="menuselection"}. Click
`New`{.interpreted-text role="guilabel"} in the top-left corner to open
a blank challenge form.

At the top of the form, enter a `Challenge Name`{.interpreted-text
role="guilabel"}.

### Create assignment rules

To assign the challenge to specific users, one or more assignment rules
must be utilized.

Click into the first field under `Assign Challenge to`{.interpreted-text
role="guilabel"}, and select a parameter from the drop-down list to
define the rule. Then, click into the next field to define the rule\'s
operator. If necessary, click into the third field to further define the
parameter.

::: {.tip}
::: {.title}
Tip
:::

To include all users with permissions in the *Sales* app, create a rule
with the following parameters:

-   `Groups`{.interpreted-text role="guilabel"}
-   `is in`{.interpreted-text role="guilabel"}
-   [Sales/User: Own Documents Only]{.title-ref}

{.align-center}
:::

In the `Periodicity`{.interpreted-text role="guilabel"} field, select a
time frame for goals to be automatically assessed.

### Add goals

Challenges can be based on a single goal, or can include multiple goals
with different targets. To add a goal to the challenge, click
`Add a line`{.interpreted-text role="guilabel"} on the
`Goals`{.interpreted-text role="guilabel"} tab.

In the `Goal Definition`{.interpreted-text role="guilabel"} field,
choose a goal from the drop-down list. The `Condition`{.interpreted-text
role="guilabel"} field automatically updates to reflect the condition
set on the goal definition.

::: {.tip}
::: {.title}
Tip
:::

The *CRM Gamification* module contains preconfigured goals geared
towards salesteams:

-   `New Leads`{.interpreted-text role="guilabel"}
-   `Time to Qualify a Lead`{.interpreted-text role="guilabel"}
-   `Days to Close a Deal`{.interpreted-text role="guilabel"}
-   `New Opportunities`{.interpreted-text role="guilabel"}
-   `New Sales Orders`{.interpreted-text role="guilabel"}
:::

Enter a `Target`{.interpreted-text role="guilabel"} for the goal based
on the `Suffix`{.interpreted-text role="guilabel"}.

Repeat these steps for each additional goal.

{.align-center}

### Add rewards

Next, click the `Reward`{.interpreted-text role="guilabel"} tab. Choose
the `badges <crm/create-rewards>`{.interpreted-text role="ref"} to be
awarded `For 1st User`{.interpreted-text role="guilabel"} and
`For Every Succeeding User`{.interpreted-text role="guilabel"} by
selecting them from the drop-down lists.

::: {.note}
::: {.title}
Note
:::

Badges are granted when a challenge is finished. This is either at the
end of a running period, at the end date of a challenge, or when the
challenge is manually closed.
:::

After setup is complete, click the `Start Challenge`{.interpreted-text
role="guilabel"} button at the top-left of the page to begin the
challenge.
