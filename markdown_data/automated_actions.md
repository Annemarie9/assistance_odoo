# File: /content/odoo_doc17.0/fr/content/applications/studio/automated_actions.md

Automation rules
================

Automation rules are used to trigger automatic changes based on user
actions (e.g., apply a modification when a field is set to a specific
value), email events, time conditions (e.g., archive a record 7 days
after its last update), or external events.

To create an automation rule with Studio, proceed as follows:

1.  `Open Studio <studio/access>`{.interpreted-text role="ref"} and
    click `Automations`{.interpreted-text role="guilabel"}, then
    `New`{.interpreted-text role="guilabel"}.
2.  Select the `studio/automated-actions/trigger`{.interpreted-text
    role="ref"} and, if necessary, fill in the fields that appear on the
    screen based on the chosen trigger.
3.  Click `Add an action`{.interpreted-text role="guilabel"}, then
    select the `Type`{.interpreted-text role="guilabel"} of
    `action <studio/automated-actions/action>`{.interpreted-text
    role="ref"} and fill in the fields that appear on the screen based
    on your selected action.
4.  Click `Save & Close`{.interpreted-text role="guilabel"} or
    `Save & New`{.interpreted-text role="guilabel"}.

::: {.example}

:::

::: {.tip}
::: {.title}
Tip
:::

\- To modify the `model <models_modules_apps>`{.interpreted-text
role="doc"} of the automation rule, switch models before clicking
`Automations`{.interpreted-text role="guilabel"} in Studio, or
`activate the developer mode
<developer-mode>`{.interpreted-text role="ref"}, create or edit an
automation rule, and select the `Model`{.interpreted-text
role="guilabel"} in the `Automation Rules`{.interpreted-text
role="guilabel"} form. - You can also create automation rules from any
kanban stage by clicking the gear icon (`⚙`{.interpreted-text
role="guilabel"} ) next to the kanban stage name, then selecting
`Automations`{.interpreted-text role="guilabel"}. In this case, the
`Trigger`{.interpreted-text role="guilabel"} is set to
`Stage is set to`{.interpreted-text role="guilabel"} by default, but you
can change it if necessary.


:::

Trigger {#studio/automated-actions/trigger}
-------

The `Trigger`{.interpreted-text role="guilabel"} is used to define when
the automation rule should be applied. The available triggers depend on
the `model <models_modules_apps>`{.interpreted-text role="doc"}. Five
trigger categories are available overall:

-   `studio/automated-actions/trigger/values-updated`{.interpreted-text
    role="ref"}
-   `studio/automated-actions/trigger/email-events`{.interpreted-text
    role="ref"}
-   `studio/automated-actions/trigger/values-timing-conditions`{.interpreted-text
    role="ref"}
-   `studio/automated-actions/trigger/custom`{.interpreted-text
    role="ref"}
-   `studio/automated-actions/trigger/external`{.interpreted-text
    role="ref"}

::: {.tip}
::: {.title}
Tip
:::

You can also define a `Before Update Domain`{.interpreted-text
role="guilabel"} to specify the conditions that must be met *before* the
automation rule is triggered. In contrast, the conditions defined using
the
`Extra Conditions <studio/automated-actions/trigger/values-timing-conditions>`{.interpreted-text
role="ref"} and
`Apply on <studio/automated-actions/trigger/custom>`{.interpreted-text
role="ref"} filters are checked *during* the execution of the automation
rule.

To define a `Before Update Domain`{.interpreted-text role="guilabel"},
`activate the developer mode
<developer-mode>`{.interpreted-text role="ref"}, create or edit an
automation rule, click `Edit Domain`{.interpreted-text role="guilabel"},
then click `New Rule`{.interpreted-text role="guilabel"}.

For example, if you want the automated action to happen when an email
address is set on a contact that did not have an address before (in
contrast to modifying their existing address), define the
`Before Update Domain`{.interpreted-text role="guilabel"} to
`Email is not set`{.interpreted-text role="guilabel"}, and the
`Apply on`{.interpreted-text role="guilabel"} domain to
`Email is set`{.interpreted-text role="guilabel"}.


:::

### Values Updated {#studio/automated-actions/trigger/values-updated}

The triggers available in this category depend on the model and are
based on common field changes, such as adding a specific tag (e.g., to a
task) or setting the `User`{.interpreted-text role="guilabel"} field.
Select the trigger, then select a value if required.



### Email Events {#studio/automated-actions/trigger/email-events}

Trigger automated actions upon receiving or sending emails.

### Timing Conditions {#studio/automated-actions/trigger/values-timing-conditions}

Trigger automated actions based on a date field. The following triggers
are available:

-   `Based on date field`{.interpreted-text role="guilabel"}: Select the
    field to be used next to the `Delay`{.interpreted-text
    role="guilabel"} field.
-   `After creation`{.interpreted-text role="guilabel"}: The action is
    triggered when a record is created and saved.
-   `After last update`{.interpreted-text role="guilabel"}: The action
    is triggered when an existing record is edited and saved.

You can then define:

-   a `Delay`{.interpreted-text role="guilabel"}: Specify the number of
    minutes, hours, days, or months. To trigger the action before the
    trigger date, specify a negative number. If you selected the
    `Based on date
    field`{.interpreted-text role="guilabel"} trigger, you must also
    select the date field to be used to determine the delay.
-   `Extra Conditions`{.interpreted-text role="guilabel"}: Click
    `Add condition`{.interpreted-text role="guilabel"}, then specify the
    conditions to be met to trigger the automation rule. Click
    `New Rule`{.interpreted-text role="guilabel"} to add another
    condition.

The action is triggered when the delay is reached and the conditions are
met.

::: {.example}
If you want to send a reminder email 30 minutes before the start of a
calendar event, select the `Start (Calendar Event)`{.interpreted-text
role="guilabel"} under `Trigger Date`{.interpreted-text role="guilabel"}
and set the `Delay`{.interpreted-text role="guilabel"} to **-30**
`Minutes`{.interpreted-text role="guilabel"}.


:::

::: {.note}
::: {.title}
Note
:::

By default, the scheduler checks for trigger dates every 4 hours,
meaning lower granularity in time-based automations may not always be
honored.
:::

### Custom {#studio/automated-actions/trigger/custom}

Trigger automated actions:

-   `On save`{.interpreted-text role="guilabel"}: When the record is
    saved;
-   `On deletion`{.interpreted-text role="guilabel"}: When a record is
    deleted;
-   `On UI change`{.interpreted-text role="guilabel"}: When a field\'s
    value is changed on the `Form view
    <studio/views/general/form>`{.interpreted-text role="ref"}, even
    before saving the record.

For the `On save`{.interpreted-text role="guilabel"} and
`On UI change`{.interpreted-text role="guilabel"} triggers, you **must**
then select the field(s) to be used to trigger the automation rule in
the `When updating`{.interpreted-text role="guilabel"} field.

::: {.warning}
::: {.title}
Warning
:::

If no field is selected in the `When updating`{.interpreted-text
role="guilabel"} field, the automated action may be executed multiple
times per record.
:::

Optionally, you can also define additional conditions to be met to
trigger the automation rule in the `Apply on`{.interpreted-text
role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `On UI change`{.interpreted-text role="guilabel"} trigger can only
be used with the
`studio/automated-actions/action/python-code`{.interpreted-text
role="ref"} action and only works when a modification is made manually.
The action is not executed if the field is changed through another
automation rule.
:::

### External {#studio/automated-actions/trigger/external}

Trigger automated actions based on an external event using a webhook. A
webhook is a method of communication between two systems where the
source system sends an HTTP(S) request to a destination system based on
a specific event. It usually includes a data payload containing
information about the event that occurred.

To configure the `On webhook`{.interpreted-text role="guilabel"}
trigger, copy the `URL`{.interpreted-text role="guilabel"} generated by
Odoo into the destination system (i.e., the system receiving the
request). Then, in the `Target Record`{.interpreted-text
role="guilabel"} field, enter the code to run to define the record(s) to
be updated using the automation rule.

::: {.warning}
::: {.title}
Warning
:::

The URL must be treated as **confidential**; sharing it online or
without caution could potentially expose your system to malicious
parties. Click the `Rotate Secret`{.interpreted-text role="guilabel"}
button to change the URL\'s secret if necessary.
:::

::: {.note}
::: {.title}
Note
:::

\- The code defined by default in the `Target Record`{.interpreted-text
role="guilabel"} field works for webhooks coming from another Odoo
database. It is used to determine the record(s) to be updated using the
information in the payload. - If you wish to use the webhook\'s content
for a purpose other than to find the record(s) (e.g., *create* a
record), your only option is to use an
`studio/automated-actions/action/python-code`{.interpreted-text
role="ref"} action. In this case, the `Target record`{.interpreted-text
role="guilabel"} field must contain any valid code, but its result
doesn\'t have any effect on the automated action itself. - The webhook
content is available in the server action context as a
[payload]{.title-ref} variable (i.e., a dictionary that contains the GET
parameters or POST JSON body of the incoming request).
:::

You can also choose to `Log Calls`{.interpreted-text role="guilabel"} to
record the payloads received, e.g., to make sure the data sent by the
source system matches the expected format and content. This also helps
identify and diagnose any issues that may arise. To access the logs,
click the `Logs`{.interpreted-text role="guilabel"} smart button at the
top of the `Automation rules`{.interpreted-text role="guilabel"} form.

Actions To Do {#studio/automated-actions/action}
-------------

Once you have defined the automation rule\'s
`trigger <studio/automated-actions/trigger>`{.interpreted-text
role="ref"}, click `Add an action`{.interpreted-text role="guilabel"} to
define the action to be executed.

::: {.tip}
::: {.title}
Tip
:::

You can define multiple actions for the same trigger/automation rule.
The actions are executed in the order they are defined. This means, for
example, that if you define an `Update record`{.interpreted-text
role="guilabel"} action and then a `Send email`{.interpreted-text
role="guilabel"} action, the email uses the updated values. However, if
the `Send email`{.interpreted-text role="guilabel"} action is defined
before the `Update record`{.interpreted-text role="guilabel"} action,
the email uses the values set *before* the update action is run.
:::

### Update Record {#studio/automated-actions/action/update-record}

This action allows to update one of the record\'s (related) fields.
Click the `Update`{.interpreted-text role="guilabel"} field and, in the
list that opens, select or search for the field to be updated; click the
right arrow next to the field name to access the list of related fields
if needed.

If you selected a
`many2many field <studio/fields/relational-fields-many2many>`{.interpreted-text
role="ref"}, choose whether the field must be updated by
`Adding`{.interpreted-text role="guilabel"},
`Removing`{.interpreted-text role="guilabel"}, or
`Setting it to`{.interpreted-text role="guilabel"} the selected value or
by `Clearing it`{.interpreted-text role="guilabel"}.

::: {.example}
If you want the automated action to remove a tag from the customer
record, set the `Update`{.interpreted-text role="guilabel"} field to
`Customer > Tags`{.interpreted-text role="guilabel"}, select
`By Removing`{.interpreted-text role="guilabel"}, then select the tag.


:::

::: {.tip}
::: {.title}
Tip
:::

Alternatively, you can also set a record\'s field dynamically using
Python code. To do so, select `Compute`{.interpreted-text
role="guilabel"} instead of `Update`{.interpreted-text role="guilabel"},
then enter the code to be used for computing the field\'s value. For
example, if you want the automation rule to compute a custom
`datetime field <studio/fields/simple-fields-date-time>`{.interpreted-text
role="ref"} when a task\'s priority is set to [High]{.title-ref} (by
starring the task), you can define the trigger
`Priority is set to`{.interpreted-text role="guilabel"} to
[High]{.title-ref} and define the `Update Record`{.interpreted-text
role="guilabel"} action as follows:


:::

### Create Activity

This action is used to schedule a new activity linked to the record.
Select an `Activity
Type`{.interpreted-text role="guilabel"}, enter a
`Title`{.interpreted-text role="guilabel"} and description, then specify
when you want the activity to be scheduled in the
`Due Date In`{.interpreted-text role="guilabel"} field, and select a
`User type`{.interpreted-text role="guilabel"}:

-   To always assign the activity to the same user, select
    `Specific User`{.interpreted-text role="guilabel"} and add the user
    in the `Responsible`{.interpreted-text role="guilabel"} field;
-   To target a user linked to the record dynamically, select
    `Dynamic User (based on
    record)`{.interpreted-text role="guilabel"} and change the
    `User Field`{.interpreted-text role="guilabel"} if necessary.

::: {.example}
After a lead is turned into an opportunity, you want the automated
action to set up a call for the user responsible for the lead. To do so,
set the `Activity Type`{.interpreted-text role="guilabel"} to
`Call`{.interpreted-text role="guilabel"} and the
`User Type`{.interpreted-text role="guilabel"} to
`Dynamic User (based on record)`{.interpreted-text role="guilabel"}.


:::

### Send Email and Send SMS

These actions are used to send an email or a text message to a contact
linked to a specific record. To do so, select or create an
`Email Template`{.interpreted-text role="guilabel"} or an
`SMS Template`{.interpreted-text role="guilabel"}, then, in the
`Send Email As`{.interpreted-text role="guilabel"} or
`Send SMS As`{.interpreted-text role="guilabel"} field, choose how you
want to send the email or text message:

-   `Email`{.interpreted-text role="guilabel"}: to send the message as
    an email to the recipients of the `Email
    Template`{.interpreted-text role="guilabel"}.
-   `Message`{.interpreted-text role="guilabel"}: to post the message on
    the record and notify the record\'s followers.
-   `Note`{.interpreted-text role="guilabel"}: to send the message as an
    internal note visible to internal users in the chatter.
-   `SMS (without note)`{.interpreted-text role="guilabel"}: to send the
    message as a text message to the recipients of the
    `SMS template`{.interpreted-text role="guilabel"}.
-   `SMS (with note)`{.interpreted-text role="guilabel"}: to send the
    message as a text message to the recipients of the
    `SMS template`{.interpreted-text role="guilabel"} and post it as an
    internal note in the chatter.
-   `Note only`{.interpreted-text role="guilabel"}: to only post the
    message as an internal note in the chatter.

### Add Followers and Remove Followers {#studio/automated-actions/action/add-followers}

Use these actions to (un)subscribe existing contacts to/from the record.

### Create Record

This action is used to create a new record on any model.

Select the required model in the `Record to Create`{.interpreted-text
role="guilabel"} field; it contains the current model by default.
Specify a `Name`{.interpreted-text role="guilabel"} for the record, and
then, if you want to create the record on another model, select a field
in the `Link Field`{.interpreted-text role="guilabel"} field to link the
record that triggered the creation of the new record.

::: {.note}
::: {.title}
Note
:::

The dropdown list related to the `Link Field`{.interpreted-text
role="guilabel"} field only contains `one2many fields
<studio/fields/relational-fields-one2many>`{.interpreted-text
role="ref"} existing on the current model that are linked to a
`many2one field <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"} on the target model.
:::

::: {.tip}
::: {.title}
Tip
:::

You can create another automation rule with
`studio/automated-actions/action/update-record`{.interpreted-text
role="ref"} actions to update the fields of the new record if necessary.
For example, you can use a `Create Record`{.interpreted-text
role="guilabel"} action to create a new project task and then assign it
to a specific user using an `Update Record`{.interpreted-text
role="guilabel"} action.
:::

### Execute Code {#studio/automated-actions/action/python-code}

This action is used to execute Python code. You can write your code into
the `Code`{.interpreted-text role="guilabel"} tab using the following
variables:

-   \`env\`: environment on which the action is triggered
-   \`model\`: model of the record on which the action is triggered; is
    a void recordset
-   \`record\`: record on which the action is triggered; may be void
-   \`records\`: recordset of all records on which the action is
    triggered in multi-mode; this may be left empty
-   [time]{.title-ref}, [datetime]{.title-ref}, [dateutil]{.title-ref},
    \`timezone\`: useful Python libraries
-   \`float\_compare\`: utility function to compare floats based on
    specific precision
-   \`log(message, level=\'info\')\`: logging function to record debug
    information in ir.logging table
-   \`\_logger.info(message)\`: logger to emit messages in server logs
-   \`UserError\`: exception class for raising user-facing warning
    messages
-   \`Command\`: x2many commands namespace
-   \`action = {\...}\`: to return an action

::: {.tip}
::: {.title}
Tip
:::

The available variables are described both in the
`Code`{.interpreted-text role="guilabel"} and `Help`{.interpreted-text
role="guilabel"} tabs.
:::

### Send Webhook Notification

This action allows to send a POST request with the values of the
`Fields`{.interpreted-text role="guilabel"} to the URL specified in the
`URL`{.interpreted-text role="guilabel"} field.

The `Sample Payload`{.interpreted-text role="guilabel"} provides a
preview of the data included in the request using a random record\'s
data or dummy data if no record is available.

### Execute Existing Actions {#studio/automated-actions/action/several-actions}

The action is used to trigger multiple actions (linked to the current
model) at the same time. To do so, click on
`Add a line`{.interpreted-text role="guilabel"}, then, in the
`Add: Child Actions`{.interpreted-text role="guilabel"} pop-up, select
an existing action or click `New`{.interpreted-text role="guilabel"} to
create a new one.
