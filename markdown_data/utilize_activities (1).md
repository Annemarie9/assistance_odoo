Utilize activities for sales teams
==================================

*Activities* are follow-up tasks tied to a record in an *Odoo* database.
Activities can be scheduled on any page of the database that contains a
chatter thread, Kanban view, list view, or activities view of an
application.

![Planned Activities for Leads and
Opportunities.](utilize_activities/activities-view.png){.align-center}

Activity types
--------------

A set of preconfigured activity types is available in the *CRM* app. To
view the list of available activity types, navigate to the
`CRM app --> Configuration --> Activity Types`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Additional activity types are available within the database, and can be
utilized through different applications. To access the complete list of
activity types, go to the `Settings app`{.interpreted-text
role="menuselection"}, then scroll to the `Discuss`{.interpreted-text
role="guilabel"} section, and click `Activity Types`{.interpreted-text
role="guilabel"}.
:::

The preconfigured activity types for the *CRM* app are as follows:

> -   `Email`{.interpreted-text role="guilabel"}: adds a reminder to the
>     chatter that prompts the salesperson to send an email.
> -   `Call`{.interpreted-text role="guilabel"}: opens a calendar link
>     where the salesperson can schedule time to call the contact.
> -   `Meeting`{.interpreted-text role="guilabel"}: opens a calendar
>     link where the salesperson can schedule time to have a meeting
>     with the contact.
> -   `To Do`{.interpreted-text role="guilabel"}: adds a general
>     reminder task to the chatter.
> -   `Upload Document`{.interpreted-text role="guilabel"}: adds a link
>     on the activity where an external document can be uploaded. Note
>     that the *Documents* app is **not** required to utilize this
>     activity type.

::: {.note}
::: {.title}
Note
:::

If other applications are installed, such as *Sales* or *Accounting*,
other activity types are made available in the *CRM* app.
:::

### Create a new activity type {#crm/create-new-activity-type}

To create a new activity type, click `New`{.interpreted-text
role="guilabel"} at the top-left of the page to open a blank form.

At the top of the form, start by choosing a `Name`{.interpreted-text
role="guilabel"} for the new activity type.

#### Activity settings

##### Action

The *Action* field specifies the intent of the activity. Some actions
trigger specific behaviors after an activity is scheduled.

-   If `Upload Document`{.interpreted-text role="guilabel"} is selected,
    a link to upload a document is added directly to the planned
    activity in the chatter.
-   If either `Phonecall`{.interpreted-text role="guilabel"} or
    `Meeting`{.interpreted-text role="guilabel"} are selected, users
    have the option to open their calendar to schedule a time for this
    activity.
-   If `Request Signature`{.interpreted-text role="guilabel"} is
    selected, a link is added to the planned activity in the chatter
    that opens a signature request pop-up window.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The actions available to select on an activity type vary, depending on
the applications currently installed in the database.
:::

##### Default user

To automatically assign this activity to a specific user when this
activity type is scheduled, choose a name from the
`Default User`{.interpreted-text role="guilabel"} drop-down menu. If
this field is left blank, the activity is assigned to the user who
creates the activity.

##### Default summary

To include notes whenever this activity type is created, enter them into
the `Default
Summary`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The information in the `Default User`{.interpreted-text role="guilabel"}
and `Default Summary`{.interpreted-text role="guilabel"} fields are
included when an activity is created. However, they can be altered
before the activity is scheduled or saved.
:::

#### Next activity

To automatically suggest, or trigger, a new activity after an activity
has been marked complete, the `Chaining Type`{.interpreted-text
role="guilabel"} must be set.

##### Suggest next activity

In the `Chaining Type`{.interpreted-text role="guilabel"} field, select
`Suggest Next Activity`{.interpreted-text role="guilabel"}. Upon doing
so, the field underneath changes to: `Suggest`{.interpreted-text
role="guilabel"}. Click the `Suggest`{.interpreted-text role="guilabel"}
field drop-down menu to select any activities to recommend as follow-up
tasks to this activity type.

{.align-center}

In the `Schedule`{.interpreted-text role="guilabel"} field, choose a
default deadline for these activities. To do so, configure a desired
number of `Days`{.interpreted-text role="guilabel"},
`Weeks`{.interpreted-text role="guilabel"}, or
`Months`{.interpreted-text role="guilabel"}. Then, decide if it should
occur `after completion date`{.interpreted-text role="guilabel"} or
`after previous activity
deadline`{.interpreted-text role="guilabel"}.

This `Schedule`{.interpreted-text role="guilabel"} field information can
be altered before the activity is scheduled.

When all configurations are complete, click `Save`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If an activity has the `Chaining Type`{.interpreted-text
role="guilabel"} set to `Suggest Next Activity`{.interpreted-text
role="guilabel"}, and has activities listed in the
`Suggest`{.interpreted-text role="guilabel"} field, users are presented
with recommendations for activities as next steps.

{.align-center}
:::

##### Trigger next activity

Setting the `Chaining Type`{.interpreted-text role="guilabel"} to
`Trigger Next Activity`{.interpreted-text role="guilabel"} immediately
launches the next activity once the previous one is completed.

If `Trigger Next Activity`{.interpreted-text role="guilabel"} is
selected in the `Chaining Type`{.interpreted-text role="guilabel"}
field, the field beneath changes to: `Trigger`{.interpreted-text
role="guilabel"}. From the `Trigger`{.interpreted-text role="guilabel"}
field drop-down menu, select the activity that should be launched once
this activity is completed.

In the `Schedule`{.interpreted-text role="guilabel"} field, choose a
default deadline for these activities. To do so, configure a desired
number of `Days`{.interpreted-text role="guilabel"},
`Weeks`{.interpreted-text role="guilabel"}, or
`Months`{.interpreted-text role="guilabel"}. Then, decide if it should
occur `after completion date`{.interpreted-text role="guilabel"} or
`after previous activity
deadline`{.interpreted-text role="guilabel"}.

This `Schedule`{.interpreted-text role="guilabel"} field information can
be altered before the activity is scheduled.

When all configurations are complete, click `Save`{.interpreted-text
role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

When an activity has the `Chaining Type`{.interpreted-text
role="guilabel"} set to `Trigger Next Activity`{.interpreted-text
role="guilabel"}, marking the activity as *Done* immediately launches
the next activity listed in the `Trigger`{.interpreted-text
role="guilabel"} field.
:::

Activity tracking
-----------------

To keep the pipeline up to date with the most accurate view of the
status of activities, as soon as a lead is interacted with, the
associated activity should be marked as *Done*. This ensures the next
activity can be scheduled as needed. It also prevents the pipeline from
becoming cluttered with past due activities.

The pipeline is most effective when it is kept up-to-date and accurate
to the interactions it is tracking.

Activity plans {#crm/activity-plans}
--------------

*Activity plans* are preconfigured sequences of activities. When an
activity plan is launched, every activity in the sequence is scheduled
automatically.

To create a new plan, navigate to
`CRM app --> Configuration --> Activity Plan`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} at
the top-left of the page to open a blank `Lead Plans`{.interpreted-text
role="guilabel"} form.

Enter a name for the new plan in the `Plan Name`{.interpreted-text
role="guilabel"} field. On the `Activities to
Create`{.interpreted-text role="guilabel"} tab, click
`Add a line`{.interpreted-text role="guilabel"} to add a new activity.

Select an `Activity Type`{.interpreted-text role="guilabel"} from the
drop-down menu. Click `Search More`{.interpreted-text role="guilabel"}
to see a complete list of available activity types, or to create a
`new one
<crm/create-new-activity-type>`{.interpreted-text role="ref"}.

Next, in the `Summary`{.interpreted-text role="guilabel"} field, enter
any details to describe the specifics of the activity, including
instructions for the salesperson or information due upon the completion
of the activity. The contents of this field are included with the
scheduled activity, and can be edited later.

In the `Assignment`{.interpreted-text role="guilabel"} field, select one
of the following options:

> -   `Ask at launch`{.interpreted-text role="guilabel"}: activities are
>     assigned to a user when the plan is scheduled.
> -   `Default user`{.interpreted-text role="guilabel"}: activities are
>     always assigned to a specific user.

If `Default user`{.interpreted-text role="guilabel"} is selected in the
`Assignment`{.interpreted-text role="guilabel"} field, choose a user in
the `Assigned to`{.interpreted-text role="guilabel"} field.

::: {.tip}
::: {.title}
Tip
:::

Activity plans can feature activities that are assigned to default users
and users assigned at the plan launch.

{.align-center}
:::

Next, configure the timeline for the activity. Activities can be
scheduled to occur either before the plan date or after. Use the
`Interval`{.interpreted-text role="guilabel"} and
`Units`{.interpreted-text role="guilabel"} fields to set the deadline
for this activity. Lastly, in the `Trigger`{.interpreted-text
role="guilabel"} field, select whether the activity should occur before
or after the plan date.

::: {.example}
An activity plan is created to handle high priority leads. Specifically,
these leads should be contacted quickly, with a meeting scheduled within
two days of the initial contact. The plan is configured with the
following activities:

-   Email two days **before** plan date
-   Meeting zero days **before** plan date
-   Make quote three days **after** plan date
-   Upload document three days **after** plan date
-   Follow-up five days **after** plan date

This sets the *plan date* as the meeting deadline, which is the
objective of the plan. Before that date, there is lead time to contact
the customer and prepare for the meeting. After that date, the
salesperson has time to create a quote, upload the document, and
follow-up.
:::

Repeat these steps for each activity included in the plan.

### Launch an activity plan

To launch an activity plan on a *CRM* opportunity, navigate to
`CRM app`{.interpreted-text role="menuselection"} and click on the
Kanban card of an opportunity to open it.

At the top-right of the chatter, click `Activities`{.interpreted-text
role="guilabel"} to open the `Schedule
Activity`{.interpreted-text role="guilabel"} pop-up window.

In the `Plan`{.interpreted-text role="guilabel"} field, select the
desired activity plan to launch. This generates a
`Plan summary`{.interpreted-text role="guilabel"}, listing out the
activities included in the plan. Select a `Plan
Date`{.interpreted-text role="guilabel"} using the calendar popover.
This updates the `Plan summary`{.interpreted-text role="guilabel"} with
deadlines based on the intervals configured on the
`activity plan <crm/activity-plans>`{.interpreted-text role="ref"}.

Select a user in the `Assigned To`{.interpreted-text role="guilabel"}
field. This user is assigned to any of the activities on the plan were
configured with `Ask at launch`{.interpreted-text role="guilabel"} in
the `Assignment`{.interpreted-text role="guilabel"} field.

{.align-center}

Click `Schedule`{.interpreted-text role="guilabel"}.

The details of the plan are added to the chatter, in addition to each of
the activities.

{.align-center}

::: {.seealso}
\- `Activities </applications/essentials/activities>`{.interpreted-text
role="doc"}
:::
