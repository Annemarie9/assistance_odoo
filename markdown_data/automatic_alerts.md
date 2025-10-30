Automation rules
================

With subscriptions up-and-running, it is important to stay up-to-date
with customers. It is efficient to use automation to avoid having to
manually go through the list of subscribers to see how things are going.
That is where Odoo\'s *automation rules* feature comes into play.

The Odoo *Subscriptions* application allows users to set up automatic
emails, create tasks for salespeople, and even send satisfaction surveys
for subscribers to evaluate their experience.

Create automation rules
-----------------------

To create an automated rule, start by navigating to
`Subscriptions app -->
Configuration --> Automation Rules`{.interpreted-text
role="menuselection"}. This is where all the automation rules for
subscriptions can be found.

The `Automation Rules`{.interpreted-text role="guilabel"} page shows
each rule\'s `Name`{.interpreted-text role="guilabel"},
`Action To Do`{.interpreted-text role="guilabel"}, what the automated
rule will `Trigger On`{.interpreted-text role="guilabel"}, and the
`Company`{.interpreted-text role="guilabel"} to which the rule applies.

To view or modify any existing automation rule, simply click the desired
rule from this page.

::: {.note}
::: {.title}
Note
:::

When modifying an existing automation rule, Odoo \"grays-out\" the
`Action`{.interpreted-text role="guilabel"} section of the form, and
provides the following warning: *Action data can not be updated to avoid
unexpected behaviors. Create a new action instead.*
:::

To create a new automation rule, click `New`{.interpreted-text
role="guilabel"}.

{.align-center}

Clicking `New`{.interpreted-text role="guilabel"} reveals a blank
`Automation Rules`{.interpreted-text role="guilabel"} form with numerous
fields to configure.

{.align-center}

### Automation rule form fields

-   `Action Name`{.interpreted-text role="guilabel"}: title of the
    automated action rule.

#### Apply On section

The `Apply On`{.interpreted-text role="guilabel"} section dictates which
subscription orders/customers this automated action applies to.

-   `MRR Between`{.interpreted-text role="guilabel"}: designate a range
    of monthly recurring revenue to target.
-   `MRR Change More`{.interpreted-text role="guilabel"}: designate a
    change of monthly recurring revenue to target, in either percentage
    or unit of currency.
-   `Over`{.interpreted-text role="guilabel"}: choose a period of time
    over which the designated KPIs (Key Performance Indicators) are
    calculated.
-   `Rating Satisfaction`{.interpreted-text role="guilabel"}: designate
    satisfaction as `greater than`{.interpreted-text role="guilabel"} or
    `less than`{.interpreted-text role="guilabel"} a percentage.
-   `Status`{.interpreted-text role="guilabel"}: select the status of
    the subscriptions to be included in this automation rule. The
    options are: `Quotation`{.interpreted-text role="guilabel"},
    `Quotation Sent`{.interpreted-text role="guilabel"},
    `Sales Order`{.interpreted-text role="guilabel"}, and
    `Cancelled`{.interpreted-text role="guilabel"}.
-   `Stage goes from`{.interpreted-text role="guilabel"}: designate when
    the automation rule should be activated using two fields that
    represent two different stages of the subscription.
-   `Subscription Plans`{.interpreted-text role="guilabel"}: choose
    specific subscription plans to target with the automation rule.
-   `Products`{.interpreted-text role="guilabel"}: select specific
    product(s) to target with the automation rule.
-   `Customers`{.interpreted-text role="guilabel"}: select specific
    customer(s) to target with the automation rule.
-   `Company`{.interpreted-text role="guilabel"}: in a multi-company
    environment, select a specific company\'s subscription data to
    target with the automation rule.
-   `Sales Team`{.interpreted-text role="guilabel"}: select the data of
    specific sales team(s) to target with the automation rule.

::: {.note}
::: {.title}
Note
:::

If any field is left blank, the rule applies to every subscription
without that specific designation.
:::

::: {.tip}
::: {.title}
Tip
:::

The number of subscriptions that match the configured criteria of the
customized automation rule are displayed at the bottom of the
`Apply On`{.interpreted-text role="guilabel"} field.

If that green subscriptions link is clicked, Odoo reveals a separate
page showcasing all the subscriptions that meet that automation rule\'s
criteria.
:::

#### Action section

The `Action`{.interpreted-text role="guilabel"} section dictates what
action occurs when an automated rule is triggered.

In the `Action To Do`{.interpreted-text role="guilabel"} field, choose
the action that will occur once the automated rule is triggered. When
clicked, the following options become available on a drop-down menu:

-   `Create next activity`{.interpreted-text role="guilabel"}: creates
    the next activity to occur, which is configured in the
    `Activity`{.interpreted-text role="guilabel"} section that appears
    at the bottom of the automation rule form.
-   `Send an email to the customer`{.interpreted-text role="guilabel"}:
    sends an email to the customer(s) who fit the specified criteria of
    the automation rule.
-   `Send an SMS Text Message to the customer`{.interpreted-text
    role="guilabel"}: sends an SMS message to the customer(s) who fit
    the specified criteria of the automation rule.
-   `Set Contract Health value`{.interpreted-text role="guilabel"}: set
    the health value of the subscription contract.

If `Send an email to the customer`{.interpreted-text role="guilabel"} is
selected in the `Action To Do`{.interpreted-text role="guilabel"} field,
the following field appears:

-   `Email Template`{.interpreted-text role="guilabel"}: create (and
    edit) a new email template *or* select from a list of pre-configured
    email templates to send to the customer(s).

If `Send an SMS Text Message to the customer`{.interpreted-text
role="guilabel"} is selected in the `Action To Do`{.interpreted-text
role="guilabel"} field, the following field appears:

-   `SMS Template`{.interpreted-text role="guilabel"}: create (and edit)
    a new SMS template *or* select from a list of pre-configured SMS
    templates to send to the customer(s).

If `Set Contract Health value`{.interpreted-text role="guilabel"} is
selected in the `Action To Do`{.interpreted-text role="guilabel"} field,
the following field appears:

-   `Health`{.interpreted-text role="guilabel"}: designate the health of
    the subscription by choosing one of the following options:
    `Neutral`{.interpreted-text role="guilabel"},
    `Good`{.interpreted-text role="guilabel"}, or
    `Bad`{.interpreted-text role="guilabel"}.

In the `Trigger On`{.interpreted-text role="guilabel"} field, decide
whether the automated rule should be triggered on a
`Modification`{.interpreted-text role="guilabel"} or
`Timed Condition`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

A `Trigger Now`{.interpreted-text role="guilabel"} button appears at the
top of the automation rule form *only* when a trigger has been
configured for the rule.
:::

::: {.warning}
::: {.title}
Warning
:::

When the `Trigger Now`{.interpreted-text role="guilabel"} button is
clicked, Odoo will trigger the action on *all* linked subscriptions,
regardless of possible timed conditions.
:::

::: {.note}
::: {.title}
Note
:::

Sending a SMS text message in Odoo requires In-App Purchase (IAP) credit
or tokens. For more information on
`IAP (In-App Purchase)`{.interpreted-text role="abbr"}, visit
`../../essentials/in_app_purchase`{.interpreted-text role="doc"}. For
more information on sending SMS messages, visit
`../../marketing/sms_marketing`{.interpreted-text role="doc"}.
:::

If `Timed Condition`{.interpreted-text role="guilabel"} is selected in
the `Trigger On`{.interpreted-text role="guilabel"} field, the following
fields appear:

-   `Trigger Date`{.interpreted-text role="guilabel"}: represents when
    the condition should be triggered. If left blank, the action is
    created upon subscription creation *and* updates.
-   `Delay After Trigger`{.interpreted-text role="guilabel"}: select a
    delayed amount of time (`Minutes`{.interpreted-text
    role="guilabel"}, `Hours`{.interpreted-text role="guilabel"},
    `Days`{.interpreted-text role="guilabel"}, or
    `Months`{.interpreted-text role="guilabel"}) for Odoo to wait before
    triggering the configured action. If a negative number is entered,
    the \"delay\" will occur *before* the
    `Trigger Date`{.interpreted-text role="guilabel"}.

##### Activity section

If `Create next activity`{.interpreted-text role="guilabel"} is selected
in the `Action To Do`{.interpreted-text role="guilabel"} field, an
`Activity`{.interpreted-text role="guilabel"} section appears at the
bottom of the `Automation Rules`{.interpreted-text role="guilabel"}
form.

-   `Activity Type`{.interpreted-text role="guilabel"}: select an
    pre-configured activity type from the drop-down menu.
-   `Title`{.interpreted-text role="guilabel"}: enter a custom title for
    the chosen activity.
-   `Note`{.interpreted-text role="guilabel"}: leave a note for the
    employee to whom the activity is assigned.
-   `Due Date In`{.interpreted-text role="guilabel"}: enter an amount of
    days within which the activity should be completed.
-   `Assign To`{.interpreted-text role="guilabel"}: choose to assign the
    specified activity to either: `Subscription
    Salesperson`{.interpreted-text role="guilabel"},
    `Sales Team Leader`{.interpreted-text role="guilabel"}, or
    `Specific Users`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If `Specific Users`{.interpreted-text role="guilabel"} is selected as
the `Assign To`{.interpreted-text role="guilabel"} option, a new
`Specific Users`{.interpreted-text role="guilabel"} field appears
beneath it, where a specific employee(s) can be chosen as the
assignee(s) for the configured activity.
:::

::: {.seealso}
\- `../subscriptions`{.interpreted-text role="doc"} -
`../../essentials/in_app_purchase`{.interpreted-text role="doc"}
:::
