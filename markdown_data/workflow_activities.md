# File: /content/odoo_doc17.0/fr/content/applications/marketing/marketing_automation/workflow_activities.md

Campaign workflow activities
============================

A *workflow* is the overall *activity* structure of a marketing
automation campaign. There can only be a single workflow in each
campaign. However, a workflow can be made up of any number of
`activities <marketing_automation/activities>`{.interpreted-text
role="ref"} to meet the needs of the campaign.

![Workflow sequence of three activities; the last child activity has a
`trigger type
<marketing_automation/trigger-type>`{.interpreted-text role="ref"} of
**Mail: not
opened**.](workflow_activities/workflow-activities.png){.align-center}

Activities {#marketing_automation/activities}
----------

Activities are the methods of communication or server actions, organized
in a workflow, that are executed within a campaign; they are the
building blocks of the campaign\'s workflow.

A new activity can be added to the workflow on a campaign form by
selecting an existing campaign or
`creating a new campaign <marketing_automation/campaigns>`{.interpreted-text
role="ref"} from the `Marketing
Automation app --> Campaigns`{.interpreted-text role="menuselection"}
dashboard, then clicking the `Add new activity`{.interpreted-text
role="guilabel"} button in the `Workflow`{.interpreted-text
role="guilabel"} section. Doing so opens the
`Create Activities`{.interpreted-text role="guilabel"} pop-up window.

First, define the name of the activity in the
`Activity Name`{.interpreted-text role="guilabel"} field, and select the
`type of activity <marketing_automation/activity-types>`{.interpreted-text
role="ref"} to be executed from the `Activity Type`{.interpreted-text
role="guilabel"} field.

Then, configure the activity\'s
`Trigger <marketing_automation/trigger>`{.interpreted-text role="ref"},
and optionally, the
`Expiry Duration <marketing_automation/expiry-duration>`{.interpreted-text
role="ref"} and the `DOMAIN
<marketing_automation/activity-domain>`{.interpreted-text role="ref"} of
the activity.

Once the activity is fully configured, click
`Save & Close`{.interpreted-text role="guilabel"} to add it to the
campaign\'s workflow, or click `Save & New`{.interpreted-text
role="guilabel"} to add the activity to the workflow and open a new
`Create Activities`{.interpreted-text role="guilabel"} pop-up window to
add another activity. Clicking `Discard`{.interpreted-text
role="guilabel"} closes the pop-up window without saving the activity.

{.align-center}

### Activity types {#marketing_automation/activity-types}

There are three different types of activities available in the
*Marketing Automation* app:

-   `Email <marketing_automation/email-activity-type>`{.interpreted-text
    role="ref"}: an email that is sent to the target audience.
-   `Server action <marketing_automation/sa-activity-type>`{.interpreted-text
    role="ref"}: an internal action within the database that is
    executed.
-   `SMS <marketing_automation/sms-activity-type>`{.interpreted-text
    role="ref"}: a text message that is sent to the target audience.

#### Email {#marketing_automation/email-activity-type}

If `Email`{.interpreted-text role="guilabel"} is selected as the
`Activity Type`{.interpreted-text role="guilabel"}, the option to
`Pick a
Template`{.interpreted-text role="guilabel"} in the
`Mail Template`{.interpreted-text role="guilabel"} field is available.

To create a new template directly from the
`Mail Template`{.interpreted-text role="guilabel"} field, start typing
the title of the new template, then select
`Create and edit...`{.interpreted-text role="guilabel"} to reveal a
`Create
Marketing Template`{.interpreted-text role="guilabel"} pop-up window.
Proceed to create and configure the new email template.

{.align-center}

Once the email template is configured, click
`Save & Close`{.interpreted-text role="guilabel"} to save the activity,
and return to the `Create Activities`{.interpreted-text role="guilabel"}
pop-up window, in order to continue to configure the
`trigger <marketing_automation/trigger>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

The title used for the `Mail Template`{.interpreted-text
role="guilabel"} **must** be unique from any other mail template titles
in the campaign, and it also serves as the subject of the email.
:::

::: {.seealso}
`Creating and configuring email templates <../email_marketing>`{.interpreted-text
role="doc"}
:::

#### Server action {#marketing_automation/sa-activity-type}

If `Server Action`{.interpreted-text role="guilabel"} is selected as the
`Activity Type`{.interpreted-text role="guilabel"}, the option to
`Pick a Server Action`{.interpreted-text role="guilabel"} in the
`Server Action`{.interpreted-text role="guilabel"} field is available.
This field is a drop-down menu containing all the pre-configured server
actions for the campaign\'s `Target`{.interpreted-text role="guilabel"}
model. Optionally, `create a new server action
<marketing_automation/create-sa>`{.interpreted-text role="ref"}.

{.align-center}

After selecting a pre-configured server action, no other activity type
configuration is needed. Click `Save & Close`{.interpreted-text
role="guilabel"} to save the activity, and return to the
`Create Activities`{.interpreted-text role="guilabel"} pop-up window, in
order to configure the
`trigger <marketing_automation/trigger>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To view all server actions in the database, activate
`developer-mode`{.interpreted-text role="ref"}, and navigate to
`Settings app --> Technical --> Actions --> Server Actions`{.interpreted-text
role="menuselection"} dashboard.
:::

##### Create a new server action {#marketing_automation/create-sa}

The option to create a new server action is also available. To do so,
type in the `Server
Action`{.interpreted-text role="guilabel"} field a title for the new
action, then click `Create and edit...`{.interpreted-text
role="guilabel"}. Doing so reveals a blank
`Create Server Action`{.interpreted-text role="guilabel"} pop-up window,
wherein a custom server action can be created and configured.

{.align-center}

On the `Create Server Action`{.interpreted-text role="guilabel"} pop-up
window, select the `Type`{.interpreted-text role="guilabel"} of server
action. The configuration fields change, depending on the selected
`Type`{.interpreted-text role="guilabel"}:

-   `Update Record`{.interpreted-text role="guilabel"}: update the
    values of a record.
-   `Create Activity`{.interpreted-text role="guilabel"}: create an
    activity with the *Discuss* app.
-   `Send Email`{.interpreted-text role="guilabel"}: post a message, a
    note, or send an email with the *Discuss* app.
-   `Send SMS`{.interpreted-text role="guilabel"}: send an SMS, and log
    them on documents, with the *SMS* app.
-   `Add Followers`{.interpreted-text role="guilabel"} or
    `Remove Followers`{.interpreted-text role="guilabel"}: add or remove
    followers on a record with the *Discuss* app.
-   `Create Record`{.interpreted-text role="guilabel"}: create a new
    record with new values.
-   `Execute Code`{.interpreted-text role="guilabel"}: execute a block
    of Python code.
-   `Send Webhook Notification`{.interpreted-text role="guilabel"}: send
    a POST request to an external system.
-   `Execute Existing Actions`{.interpreted-text role="guilabel"}:
    define an action that triggers several other server actions.

Once the server action is configured, click
`Save & Close`{.interpreted-text role="guilabel"} to save the activity,
and return to the `Create Activities`{.interpreted-text role="guilabel"}
pop-up window, in order to configure the `trigger
<marketing_automation/trigger>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

Some of the server action types have advanced configurations available
when `developer-mode`{.interpreted-text role="ref"} is activated, such
as specifying the `Allowed Groups`{.interpreted-text role="guilabel"}
that can execute this server action.
:::

#### SMS {#marketing_automation/sms-activity-type}

If `SMS`{.interpreted-text role="guilabel"} is selected as the
`Activity Type`{.interpreted-text role="guilabel"}, the option to
`Pick a
Template`{.interpreted-text role="guilabel"} in the
`SMS Template`{.interpreted-text role="guilabel"} field is available.

To create a new template directly from the
`SMS Template`{.interpreted-text role="guilabel"} field, start typing
the title of the new template, and select
`Create and edit...`{.interpreted-text role="guilabel"} to reveal a
`Create Marketing
Template`{.interpreted-text role="guilabel"} pop-up window. Proceed to
create and configure the new SMS template.

{.align-center}

Once the SMS template is configured, click
`Save & Close`{.interpreted-text role="guilabel"} to save the activity,
and return to the `Create Activities`{.interpreted-text role="guilabel"}
pop-up window, in order to configure the `trigger
<marketing_automation/trigger>`{.interpreted-text role="ref"}.

::: {.seealso}
`Creating and configuring SMS templates <../sms_marketing>`{.interpreted-text
role="doc"}
:::

### Trigger {#marketing_automation/trigger}

Once an
`activity type <marketing_automation/activity-types>`{.interpreted-text
role="ref"} is configured, the next step in the
`Create Activities`{.interpreted-text role="guilabel"} pop-up window is
to define when the activity should be executed. This is done in the
`Trigger`{.interpreted-text role="guilabel"} field group.

{.align-center}

To set an execution delay for the activity from when the `trigger type
<marketing_automation/trigger-type>`{.interpreted-text role="ref"}
occurs, type a whole number in the *interval number* input (e.g.
[2]{.title-ref} is valid, [0]{.title-ref} is also valid, and
[1.5]{.title-ref} is not).

Next, select the unit of time for the interval number in the *interval
type* drop-down menu, the options are: `Hours`{.interpreted-text
role="guilabel"}, `Days`{.interpreted-text role="guilabel"},
`Weeks`{.interpreted-text role="guilabel"}, and
`Months`{.interpreted-text role="guilabel"}.

::: {.example}
If the interval number is set to [0]{.title-ref} and the interval type
is set to `Hours`{.interpreted-text role="guilabel"}, the activity will
be executed immediately after the trigger type occurs (at the next
scheduled run of the
`Mail: Email Queue Manager cron <email-issues-outgoing-execution-time>`{.interpreted-text
role="ref"}).
:::

#### Trigger type {#marketing_automation/trigger-type}

To define the event occurrence that sets the activity into motion,
select a *trigger type* from the drop-down menu:

-   `beginning of workflow`{.interpreted-text role="guilabel"}: the
    activity is executed when the campaign is started.

All other trigger types reveal a drop-down menu
`Activity`{.interpreted-text role="guilabel"} field containing all of
the other activities in the campaign. Selecting one of these types
converts this activity into a
`child activity <marketing_automation/child-activities>`{.interpreted-text
role="ref"} to be executed directly after the selected
`Activity`{.interpreted-text role="guilabel"}:

-   `another activity`{.interpreted-text role="guilabel"}: to be
    executed after another activity in the campaign.
-   `Mail: opened`{.interpreted-text role="guilabel"}: the activity\'s
    email was opened by the participant.
-   `Mail: not opened`{.interpreted-text role="guilabel"}: the
    activity\'s email was **not** opened by the participant.
-   `Mail: replied`{.interpreted-text role="guilabel"}: the activity\'s
    email was replied to by the participant.
-   `Mail: not replied`{.interpreted-text role="guilabel"}: the
    activity\'s email was **not** replied to by the participant.
-   `Mail: clicked`{.interpreted-text role="guilabel"}: a link in the
    activity\'s email was clicked by the participant.
-   `Mail: not clicked`{.interpreted-text role="guilabel"}: a link in
    the activity\'s email was **not** clicked by the participant.
-   `Mail: bounced`{.interpreted-text role="guilabel"}: the activity\'s
    email has bounced.
-   `SMS: clicked`{.interpreted-text role="guilabel"}: a link in the
    activity\'s SMS was clicked by the participant.
-   `SMS: not clicked`{.interpreted-text role="guilabel"}: a link in the
    activity\'s SMS was **not** clicked by the participant.
-   `SMS: bounced`{.interpreted-text role="guilabel"}: the activity\'s
    SMS has bounced.

::: {.example}
If the trigger type is set to `Mail: clicked`{.interpreted-text
role="guilabel"}, this activity is converted to a
`child activity <marketing_automation/child-activities>`{.interpreted-text
role="ref"} and will execute **after** a participant clicks on a link
from the parent activity defined in the `Activity`{.interpreted-text
role="guilabel"} field.
:::

### Expiry duration {#marketing_automation/expiry-duration}

Optionally, an `Expiry Duration`{.interpreted-text role="guilabel"} can
be defined in the `Create Activities`{.interpreted-text role="guilabel"}
pop-up window to cancel the execution of this activity after a specific
amount of time. Selecting this checkbox reveals the
`Cancel after`{.interpreted-text role="guilabel"} field with *interval*
and *interval type* inputs.

Type a whole number in the interval number input (e.g. [2]{.title-ref}
is valid, [0]{.title-ref} is also valid, and [1.5]{.title-ref} is not).
Then, select the unit of time for the interval number in the interval
type drop-down menu, the options are: `Hours`{.interpreted-text
role="guilabel"}, `Days`{.interpreted-text role="guilabel"},
`Weeks`{.interpreted-text role="guilabel"}, and
`Months`{.interpreted-text role="guilabel"}.

::: {.example}
If the interval number is set to [2]{.title-ref} and the interval type
is set to `Days`{.interpreted-text role="guilabel"}, the activity will
be cancelled if it has not been executed within 2 days of the trigger
type.
:::

### Activity domain {#marketing_automation/activity-domain}

The `DOMAIN`{.interpreted-text role="guilabel"} section of the
`Create Activities`{.interpreted-text role="guilabel"} pop-up window
contains fields to further filter the target audience of the activity.

The `Activity Filter`{.interpreted-text role="guilabel"} field focuses
this activity, **and** its `child activities
<marketing_automation/child-activities>`{.interpreted-text role="ref"},
even further on a specific group of the campaign\'s filter. The process
is the same as
`defining filters <marketing_automation/defining-filters>`{.interpreted-text
role="ref"} for the campaign, and the fields that are available to
filter are also specific to the `Target`{.interpreted-text
role="guilabel"} of the campaign.

The `# record(s)`{.interpreted-text role="guilabel"} beside the
`Activity Filter`{.interpreted-text role="guilabel"} field indicates how
many records are currently being targeted by this
`Activity Filter`{.interpreted-text role="guilabel"}.

The `Applied Filter`{.interpreted-text role="guilabel"} displays the
combined filters from the `Activity Filter`{.interpreted-text
role="guilabel"} and the inherited campaign
`Filter <target_audience>`{.interpreted-text role="doc"}. This field is
read-only.

The `# record(s)`{.interpreted-text role="guilabel"} beside the
`Applied Filter`{.interpreted-text role="guilabel"} field indicates how
many records, in total, are currently being targeted by the activity.

Child activities {#marketing_automation/child-activities}
----------------

Activities that are connected to, and triggered by, another activity are
known as, *child activities*.

The activity that triggers a child activity is known as its *parent
activity*.

A child activity can be added to a campaign\'s workflow by hovering over
the `➕ Add child
activity`{.interpreted-text role="guilabel"} button, located beneath the
desired parent activity.

The child activity\'s
`trigger types <marketing_automation/trigger-type>`{.interpreted-text
role="ref"} are specific to the parent
`activity type <marketing_automation/activity-types>`{.interpreted-text
role="ref"} (*Email*, *SMS*, or *Server Action*), and are as follows:

::: {.tabs}
::: {.tab}
Email

{.align-center}

Each trigger the child activity on the following conditions of the
parent activity:

-   `Add Another Activity`{.interpreted-text role="guilabel"}: to be
    executed after the parent activity.
-   `Opened`{.interpreted-text role="guilabel"}: the email was opened by
    the participant.
-   `Not Opened`{.interpreted-text role="guilabel"}: the email was
    **not** opened by the participant.
-   `Replied`{.interpreted-text role="guilabel"}: the email was replied
    to by the participant.
-   `Not Replied`{.interpreted-text role="guilabel"}: the email was
    **not** replied to by the participant.
-   `Clicked`{.interpreted-text role="guilabel"}: a link in the email
    was clicked by the participant.
-   `Not Clicked`{.interpreted-text role="guilabel"}: a link in the
    email was **not** clicked by the participant.
-   `Bounced`{.interpreted-text role="guilabel"}: the email has bounced.
:::

::: {.tab}
Server Action

{.align-center}

Triggers the child activity on the following condition of the parent
activity:

-   `Add Another Activity`{.interpreted-text role="guilabel"}: to be
    executed after the parent activity.
:::

::: {.tab}
SMS

{.align-center}

Each trigger the child activity on the following conditions of the
parent activity:

-   `Add Another Activity`{.interpreted-text role="guilabel"}: to be
    executed after the parent activity.
-   `Clicked`{.interpreted-text role="guilabel"}: a link in the SMS was
    clicked by the participant.
-   `Not Clicked`{.interpreted-text role="guilabel"}: a link in the SMS
    was **not** clicked by the participant.
-   `Bounced`{.interpreted-text role="guilabel"}: the SMS has bounced.
:::
:::

Once a trigger type is selected, the
`Create Activities`{.interpreted-text role="guilabel"} pop-up window
opens to configure the child activity. The process is the same as
`creating a new activity
<marketing_automation/activities>`{.interpreted-text role="ref"}, with
the exception that the `Trigger`{.interpreted-text role="guilabel"}
field is pre-filled with the selected trigger type, and the
`Activity`{.interpreted-text role="guilabel"} field has the parent
activity selected.

::: {.seealso}
\- `testing_running`{.interpreted-text role="doc"} -
`understanding_metrics`{.interpreted-text role="doc"} -
`target_audience`{.interpreted-text role="doc"}
:::
